import random
import time
import os
import names

# Definindo parâmetros e semente de aleatoriedade
random.seed(40)
qtd_nomes_unicos = 39080
qtd_nomes_aleatorios = 10000000

# Gerando os nomes aleatórios únicos
aux=[]
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f'Gerando {qtd_nomes_aleatorios} nomes aleatórios')

dados=[]
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))


# Salvando os nomes em um arquivo de texto
with open("nomes_aleatorios.txt", "w", encoding="utf-8") as arquivo:
    for nome in dados:
        arquivo.write(f"{nome}\n")