from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext 
from pyspark.sql import functions as F


# etapa 1
spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv(r"C:\Users\josim\OneDrive\Área de Trabalho\ALINE\CC\COMPASS\scholarship-compass\Sprint_6\Exercicios\parte2\nomes_aleatorios.txt")
df_nomes.show(5)


# etapa 2
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes.printSchema()

df_nomes.show(10)


# etapa 3
df_nomes = df_nomes.withColumn(
    "Escolaridade",
    F.when(F.rand() < 1/3, "Fundamental")
     .when(F.rand() < 2/3, "Médio")
     .otherwise("Superior")
)

df_nomes.show(10)


# etapa 4
df_nomes = df_nomes.withColumn(
    "Pais",
    F.when(F.rand() < 1/13, "Brasil")
     .when(F.rand() < 2/13, "Argentina")
     .when(F.rand() < 3/13, "Chile")
     .when(F.rand() < 4/13, "Uruguai")
     .when(F.rand() < 5/13, "Paraguai")
     .when(F.rand() < 6/13, "Bolívia")
     .when(F.rand() < 7/13, "Peru")
     .when(F.rand() < 8/13, "Equador")
     .when(F.rand() < 9/13, "Colômbia")
     .when(F.rand() < 10/13, "Venezuela")
     .when(F.rand() < 11/13, "Guiana")
     .when(F.rand() < 12/13, "Suriname")
     .otherwise("Guiana Francesa")
)

df_nomes.show(10)


# etapa 5
df_nomes = df_nomes.withColumn(
    "AnoNascimento",
    (F.floor(F.rand() * (2010 - 1945 + 1)) + 1945).cast("int")
)

df_nomes.show(10)


## etapa 6
df_select = df_nomes.select("*").where(F.col("AnoNascimento") >= 2000)
df_select.show(10)


# etapa 7
df_nomes.createOrReplaceTempView("pessoas")

df_select_sql = spark.sql("""
    SELECT * FROM pessoas
    WHERE AnoNascimento >= 2000
""")

df_select_sql.show(10)


# etapa 8
df_millennials = df_nomes.filter(
    (F.col("AnoNascimento") >= 1980) & (F.col("AnoNascimento") <= 1994)
)

print("Número de Millennials:", df_millennials.count())


# etapa 9
df_millennials_sql = spark.sql("""
    SELECT COUNT(*) AS Qntd_millennials
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1980 AND 1994
""")

df_millennials_sql.show()


# etapa 10
df_geracoes = spark.sql("""
    SELECT
        Pais,
        CASE
            WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
            WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
            WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
            ELSE 'Outra'
        END AS Geracao,
        COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, Geracao
    ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
""")

df_geracoes.show(52)