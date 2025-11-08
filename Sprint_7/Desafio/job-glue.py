import sys
import datetime
import unicodedata
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.types import StringType

# Lendo os parâmetros
args = getResolvedOptions(sys.argv, [
    "JOB_NAME",
    "BUCKET_NAME",
    "TRUSTED_CSV_PATH",
    "TRUSTED_TMDB_PATH"
])

bucket = args["BUCKET_NAME"]
trusted_csv_path = args["TRUSTED_CSV_PATH"]
trusted_tmdb_path = args["TRUSTED_TMDB_PATH"]

# Caminho fixo da camada Refined
refined_base_path = f"s3://{bucket}/Refined/parquet/"

# Iniciando
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Usando a data atual de forma dinamica
data_atual = datetime.datetime.now()
ano = data_atual.year
mes = str(data_atual.month).zfill(2)
dia = str(data_atual.day).zfill(2)

# Limpando títulos para garantir o join correto
def normalizar_titulo(texto):
    if texto is None:
        return None
    # remove acentos
    texto = ''.join(
        c for c in unicodedata.normalize('NFKD', texto)
        if not unicodedata.combining(c)
    )
    # remove caracteres especiais e deixa tudo minúsculo
    texto = ''.join(e for e in texto if e.isalnum() or e.isspace())
    return texto.strip().lower()

normalizar_titulo_udf = F.udf(normalizar_titulo, StringType())

# Lendo os datasets da camada Trusted
df_csv = spark.read.parquet(trusted_csv_path)
df_tmdb = spark.read.parquet(trusted_tmdb_path)

# Padronizando os nomes das colunas com os nomes constantes na modelagem
df_csv = (df_csv
    .withColumnRenamed("tituloPincipal", "titulo_principal")
    .withColumnRenamed("anoLancamento", "ano_lancamento_csv")  # renomeado para evitar conflito
    .withColumnRenamed("tempoMinutos", "duracao_minutos")
    .withColumnRenamed("notaMedia", "nota_media")
    .withColumnRenamed("numeroVotos", "numero_votos")
    .withColumnRenamed("generoArtista", "genero_artista")
    .withColumnRenamed("nomeArtista", "nome_artista")
    .withColumn("titulo_principal", normalizar_titulo_udf(F.col("titulo_principal")))
)

df_tmdb = (df_tmdb
    .withColumnRenamed("title", "titulo_principal")
    .withColumnRenamed("vote_average", "nota_media_tmdb")
    .withColumnRenamed("vote_count", "numero_votos_tmdb")
    .withColumnRenamed("popularity", "popularidade")
    .withColumnRenamed("release_date", "ano_lancamento_str")
    # limpa e padroniza títulos
    .withColumn("titulo_principal", normalizar_titulo_udf(F.col("titulo_principal")))
    .withColumn("ano_lancamento", F.year(F.to_date("ano_lancamento_str", "yyyy-MM-dd")))
)

# Fazendo o join pelos títulos em comum, mantendo apenas os anos de lançamento do TMDB
df_join = (df_csv
    .join(df_tmdb, on="titulo_principal", how="inner")
    .drop("ano_lancamento_csv")  # evita ambiguidade
)

# Criando as dimensões
dim_filme = (df_join.select("titulo_principal", "duracao_minutos")
             .dropDuplicates()
             .withColumn("id_filme", F.monotonically_increasing_id()))

dim_artista = (df_join.select("nome_artista", "genero_artista")
               .dropDuplicates()
               .withColumn("id_artista", F.monotonically_increasing_id()))

dim_tempo = (df_join.select("ano_lancamento")
             .dropDuplicates()
             .withColumn("id_tempo", F.monotonically_increasing_id()))

# Criando a fato
fato_avaliacao = (df_join
    .join(dim_filme, on="titulo_principal", how="left")
    .join(dim_artista, on=["nome_artista", "genero_artista"], how="left")
    .join(dim_tempo, on="ano_lancamento", how="left")
    .select(
        F.monotonically_increasing_id().alias("id_avaliacao"),
        "nota_media",
        "numero_votos",
        "popularidade",
        "id_tempo",
        "id_artista",
        "id_filme"
    )
)

# Salvando na camada Refined (um único arquivo por tabela)
dim_filme.coalesce(1).write.mode("overwrite").parquet(f"{refined_base_path}dim_filme/{ano}/{mes}/{dia}/")
dim_artista.coalesce(1).write.mode("overwrite").parquet(f"{refined_base_path}dim_artista/{ano}/{mes}/{dia}/")
dim_tempo.coalesce(1).write.mode("overwrite").parquet(f"{refined_base_path}dim_tempo/{ano}/{mes}/{dia}/")
fato_avaliacao.coalesce(1).write.mode("overwrite").parquet(f"{refined_base_path}fato_avaliacao/{ano}/{mes}/{dia}/")

job.commit()