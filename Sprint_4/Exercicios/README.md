# LABORATÓRIOS

## LAB AWS S3

Criei um bucket com o nome "aline.com" e escolhei a região "US East (N. Virginia) us-east-1".

![imagem](../Evidencias/Exercicios/LAB-S3/bucket-regiao.jpg)

Em seguida, habilitei a opção de hospedagem de site estático e configurei o index.html como documento inicial e o 404.html como página de erro personalizada.

Para permitir que o site fosse acessado publicamente, desabilitei o bloqueio de acesso público e adicionei uma política de bucket que libera permissão de leitura para qualquer usuário, sendo ela:

````{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::aline.com/*"
            ]
        }
    ]
}
````

Depois disso, fiz o upload do arquivo index.html que funciona como a página principal, criei uma pasta chamada dados/ para armazenar o arquivo CSV ("nomes.csv") e adicionei também o arquivo 404.html.

![imagem](../Evidencias/Exercicios/LAB-S3/adicionando-arquivos.jpg)

Por fim, copiei o endpoint fornecido pelo S3 e testei no navegador, confirmando que o site estava disponível publicamente e que os arquivos podiam ser acessados através da hospedagem estática.

![imagem](../Evidencias/Exercicios/LAB-S3/site-hospedado.jpg)