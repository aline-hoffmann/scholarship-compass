# DESAFIO

## ETAPA 1 - Limpeza de dados
Antes do efetivo script em .py, utilizei o jupyter notebook para uma mais rápida visualização dos dados e dos erros, já que lá é possível trabalhar célula por célula. Esse arquivo inicial está [aqui](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_3/Desafio/etapa-1/etl.ipynb).

Para iniciar a limpeza de dados, importei as bibliotecas pandas, re e os, já que precisaria delas para manipular o CSV, usar regex na limpeza e trabalhar com os caminhos das pastas.

````
import pandas as pd
import re
import os
````

Após ler o arquivo "concert_tours_by_women.csv", selecionei apenas as colunas necessárias, conforme o modelo que me foi passado no desafio.

![imagem](../Evidencias/Desafio/selecionando-colunas.jpg)

Na coluna dos anos das turnês, foi necessário fazer uma divisão. Sendo assim, padronizei os traços de separação dos anos e dividi a coluna "Year(s)" nas colunas "Start year" e "End Year", excluindo a coluna original.

![imagem](../Evidencias/Desafio/dividindo-years.jpg)

Para a limpeza das colunas onde se tratava de dinheiro, removi os caracteres que não fossem pontos ou números.

````
def limpa_dinheiro(valor):
    if isinstance(valor, str):
        valor = re.sub(r"[^0-9.]", "", valor)
        if valor == "":
            return 0.0
        return float(valor)
    return float(valor)
````

Ademais, alterei os tipos das colunas e, nas de texto, transformei tudo em string e removi possíveis espaçoes em branco. Além disso, renomeei a coluna "Adjustedgross (in 2022 dollars)" para seguir o modelo fornecido.

![imagem](../Evidencias/Desafio/tipos-colunas.jpg)

Na coluna "Tour Tittle" foi necessário fazer uma limpeza mais profunda, pois existiam muitos tipos de símbolos nos nomes das turnês.

![imagem](../Evidencias/Desafio/tour-tittle.jpg) 


Para finalizar, determinei que o arquivo csv fosse salvo na pasta "volume", para que mais adiante fosse lido pelo "docker-compose.yml".

````
output_path = os.path.join(os.path.dirname(__file__), "..", "volume", "csv_limpo.csv")
df.to_csv(output_path, index=False, encoding="utf-8")
````