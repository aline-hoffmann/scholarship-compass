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