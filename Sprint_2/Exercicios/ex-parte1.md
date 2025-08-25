## <p align="center"> EXERCÍCIOS - PARTE 1</p>

**1.** Dada a seguinte lista:


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


Faça um programa que gere uma nova lista contendo apenas números ímpares.

````py
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

impares = [n for n in a if n % 2 != 0]
print(impares)
````

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)

<br>

**2.** Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.

Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.

````py
palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for n in palavras:
    if n == n[::-1]:
        print("A palavra:", n, "é um palíndromo")
    else:
        print("A palavra:", n, "não é um palíndromo")
````
- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)


**3.** Dada as listas a seguir:

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']

sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']

idades = [19, 28, 25, 31]

Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".

````py
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, nome in enumerate(primeirosNomes):
    sobrenome = sobreNomes[indice]
    idade = idades[indice]
    print(f"{indice} - {nome} {sobrenome} está com {idade} anos")
````

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)


**4.** Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.

['abc', 'abc', 'abc', '123', 'abc', '123', '123']

````py
def sem_duplicados(lista):
    return list(set(lista))

lista_dupla= ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
resultado = sem_duplicados(lista_dupla)
print(resultado)
````

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)

**5.** Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

````py
import json

with open('person.json', 'r') as arquivo:
    dados = json.load(arquivo)
    
print(dados)
````
- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)