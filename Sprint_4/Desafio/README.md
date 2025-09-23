## ETAPA 1
Primeiramente, defini os questionamentos que iria responder com a análise dos dados "Feminicídios 2023 - Estado de Minas Gerais, sendo eles:

QUESTIONAMENTOS AQUI!!!!!!!!!!!!!!

Após a importação da biblioteca "boto3" para interagir com a AWS, criei o bucket "aline-hp-pb", através do comando a seguir e verifiquei o mesmo no painel da AWS.

````
s3.create_bucket(Bucket='aline-hp-pb')
````

![imagem](../Evidencias/Desafio/bucket-criado.jpg)

Depois da criação do bucket, fiz o upload dos dados que irei utilizar para as análises na segunda etapa.

````
s3.upload_file(arquivo_local, bucket_name, nome_s3)
````

![imagem](../Evidencias/Desafio/upload-dados.jpg)

## ETAPA 2

Antes de começar a responder os questinamentos, realizei a limpeza dos dados. Para fazer a leitura do arquivo csv, utilizei o parâmetro sep=";", já que o pandas por padrão espera a separação por vírgula.

````
df = pd.read_csv(dados_fem, sep=";", encoding="utf-8")
````

Após isso, excluí as colunas "risp" e "rmbh" pois não vou utilizar para a análise.

````
df = df.drop(columns=["risp", "rmbh"])
````

Seguindo a limpeza, conferi os tipos de dados das colunaa através do "df.dtypes" e padronizei as com valores númericos, datas e strings.

````
df["municipio_cod"] = pd.to_numeric(df["municipio_cod"], errors="coerce", downcast="integer")
df["data_fato"] = pd.to_datetime(df["data_fato"], format="%d/%m/%Y", errors="coerce")
df["mes"] = pd.to_numeric(df["mes"], errors="coerce", downcast="integer")
df["ano"] = pd.to_numeric(df["ano"], errors="coerce", downcast="integer")
df["qtde_vitimas"] = pd.to_numeric(df["qtde_vitimas"], errors="coerce", downcast="integer")

df["municipio_fato"] = df["municipio_fato"].str.strip().str.upper()
df["tentado_consumado"] = df["tentado_consumado"].str.strip().str.upper()
````

Ademais, removi possíveis linhas duplicadas e reorganizei o indíce, caso alguma coisa tenha sido excluída.

````
df = df.drop_duplicates()

df = df.reset_index(drop=True)
````

Para garantir  o padrão, consultei se na coluna "tentado_consumado" só existia valores com esses dois resultados e na coluna "ano" só existia 2023.

![imagem](../Evidencias/Desafio/tent-cons-2023.jpg)

Por fim, verifiquei se existia algum valor nulo.

![imagem](../Evidencias/Desafio/NAN.jpg)