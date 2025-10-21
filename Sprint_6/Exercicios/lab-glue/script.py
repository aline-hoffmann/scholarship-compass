import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, upper, desc

# Lendo os parâmetros passados no Job (paths do S3)
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Lendo arquivo CSV do S3
df = spark.read.option("header", True).csv(args['S3_INPUT_PATH'])

# Imprimindo o schema
print("Schema do dataframe:")
df.printSchema()

# Colocando os nomes em maiúsculo
df_upper = df.withColumn("nome", upper(col("nome")))

# Contagem de linhas
print(f"Total de linhas: {df_upper.count()}")

# Contagem de nomes por ano e sexo (ordenando por ano desc)
contagem = (df_upper.groupBy("ano", "sexo")
            .count()
            .orderBy(desc("ano")))
print("Contagem por ano e sexo:")
contagem.show()

# Nome feminino mais frequente e ano
mais_feminino = (df_upper.filter(col("sexo") == "F")
                 .groupBy("nome", "ano")
                 .count()
                 .orderBy(desc("count"))
                 .limit(1))
print("Nome feminino mais frequente:")
mais_feminino.show()

# Nome masculino mais frequente e ano
mais_masculino = (df_upper.filter(col("sexo") == "M")
                  .groupBy("nome", "ano")
                  .count()
                  .orderBy(desc("count"))
                  .limit(1))
print("Nome masculino mais frequente:")
mais_masculino.show()

# Total de registros por ano (primeiros 10 ordenados por ano crescente)
totais_ano = (df_upper.groupBy("ano")
              .count()
              .orderBy("ano")
              .limit(10))
print("Total de registros por ano:")
totais_ano.show()

# Escrevendo resultado no S3 (JSON, particionado por sexo e ano)
output_path = args['S3_TARGET_PATH'] + "frequencia_registro_nomes_eua/"
(df_upper.write
 .mode("overwrite")
 .partitionBy("sexo", "ano")
 .json(output_path))

job.commit()