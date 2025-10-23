# Importando bibliotecas
import sys
import re
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

# Parâmetros
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'RAW_PATH', 'TRUSTED_BASE_PATH'])

# Inicializando o Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

raw_path = args['RAW_PATH']
trusted_base_path = args['TRUSTED_BASE_PATH']

# Lendo o CSV
df = spark.read.option("header", True).option("sep", "|").csv(raw_path)

# Limpando os dados
# Removendo duplicados
df = df.dropDuplicates() 

# Removendo espaços extras de todas as colunas do tipo string
for c in df.columns:
    df = df.withColumn(
        c,
        F.when(F.col(c).isNotNull(), F.trim(F.col(c))).otherwise(F.col(c))
    )

# Padronizando colunas de texto para maiúsculas
colunas_texto = [
    'tituloPrincipal', 'tituloOriginal', 'genero',
    'generoArtista', 'personagem', 'nomeArtista',
    'profissao', 'titulosMaisConhecidos'
]
for c in colunas_texto:
    if c in df.columns:
        df = df.withColumn(c, F.upper(F.col(c)))

# Tratando valores '\N' e convertendo colunas numéricas
colunas_numericas = [
    'anoLancamento', 'tempoMinutos', 'notaMedia', 'numeroVotos',
    'anoNascimento', 'anoFalecimento'
]
for c in colunas_numericas:
    if c in df.columns:
        df = df.withColumn(
            c,
            F.when(F.col(c) == "\\N", None).otherwise(F.col(c).cast("double"))
        )

# Filtrando só os filmes de comédia
if "genero" in df.columns:
    df = df.filter(F.col("genero").contains("COMEDY"))

# Extraindo a data, deixando de forma dinâmica
filmes_path = df.inputFiles()[0] 

# Usando Regex para capturar ano/mês/dia do caminho: /YYYY/MM/DD/
padrao_data = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', filmes_path)
if padrao_data:
    ano, mes, dia = padrao_data.groups()
else:
    raise ValueError(f"Não foi possível extrair a data do caminho do arquivo: {filmes_path}")

# Montando o caminho de saída 

origem = "CSV"                 # origem do dado
formato = "parquet"            # formato de saída
especificacao = "filmes_comedia"  # tipo de dado

trusted_path = f"{trusted_base_path}/{origem}/{formato}/{especificacao}/{ano}/{mes}/{dia}/"
print(f"Salvando dados em: {trusted_path}")

# Salvando como único arquivo Parquet
df = df.coalesce(1)
df.write.mode("overwrite").format("parquet").save(trusted_path)

job.commit()