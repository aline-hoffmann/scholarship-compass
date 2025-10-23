# Importando bibliotecas
import sys
import re
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

# Paramêtros
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'RAW_PATH', 'TRUSTED_BASE_PATH'])


# Inicializando o spark e glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

raw_path = args['RAW_PATH']
trusted_base_path = args['TRUSTED_BASE_PATH']

# Lendo os jsons
df = spark.read.option("multiline", True).json(raw_path)  # Lê todos os arquivos da pasta

# Limpando os dados
# Removendo duplicados
df = df.dropDuplicates()

# Removendo espaços extras de todas as colunas string e boolean, convertendo boolean para string
for c, dtype in df.dtypes:
    if dtype in ['string', 'boolean']:
        df = df.withColumn(c, F.when(F.col(c).isNotNull(), F.trim(F.col(c).cast("string"))).otherwise(None))

# Padronizando colunas de texto para maiúsculas
colunas_texto = ['title', 'original_title', 'genero', 'tipo']
for c in colunas_texto:
    if c in df.columns:
        df = df.withColumn(c, F.upper(F.col(c)))

# Convertendo as colunas numéricas
colunas_numericas = ['vote_average', 'vote_count', 'popularity', 'id']
for c in colunas_numericas:
    if c in df.columns:
        df = df.withColumn(c, F.col(c).cast("double"))

# Extraindo a data, deixando de forma dinâmica
json_path = df.inputFiles()[0]
padrao_data = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', json_path)
if padrao_data:
    ano, mes, dia = padrao_data.groups()
else:
    raise ValueError(f"Não foi possível extrair a data do arquivo: {json_path}")

# Montando o caminho de saída 
origem = "TMDB"
formato = "parquet"
especificacao = "filmes_comedia"
trusted_path = f"{trusted_base_path}/{origem}/{formato}/{especificacao}/{ano}/{mes}/{dia}/"
print(f"Salvando dados em: {trusted_path}")

# Salvando como parquet
df = df.coalesce(1)
df.write.mode("overwrite").format("parquet").save(trusted_path)

job.commit()