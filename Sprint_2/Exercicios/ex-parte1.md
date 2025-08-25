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

**6.** Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.

Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.

````py
list_entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def my_map(list, f):
    list_resultado = []
    for elemento in list:
        list_resultado.append(f(elemento))
    return list_resultado

def potencia2(x):
    return x ** 2

resultado = my_map(list_entrada, potencia2)
print(resultado)
````
- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)

**7.** Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

````py
with open('arquivo_texto.txt', 'r') as arquivo:
    conteudo_arq = arquivo.read()

print(conteudo_arq, end='')
````

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)

**8.** Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.

Teste sua função com os seguintes parâmetros:

(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

````py
def print_parametros(*args, **kwargs):
    for arg in args:
        print(arg)
    for chave, valor in kwargs.items():
        print(valor)

print_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
````

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)

**9** Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:

liga(): muda o estado da lâmpada para ligada

desliga(): muda o estado da lâmpada para desligada

esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

Para testar sua classe:

Ligue a Lampada

Imprima: A lâmpada está ligada? True

Desligue a Lampada

Imprima: A lâmpada ainda está ligada? False

````py
class Lampada:
    def __init__(self, ligada=False):
        self.ligada = ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada

lampada = Lampada()  

lampada.liga()
print("A lâmpada está ligada?", lampada.esta_ligada())  

lampada.desliga()
print("A lâmpada ainda está ligada?", lampada.esta_ligada()) 
````

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)

**10.** Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.

A string deve ter valor  "1,3,4,6,10,76".

````py
def soma_numeros(string_numeros):
    numeros = map(int, string_numeros.split(","))  # transforma a string em inteiros
    return sum(numeros)  # soma todos os números

string_numeros = "1,3,4,6,10,76"
soma = soma_numeros(string_numeros)
print(soma)
````

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)

**11.** Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

````py
def dividindo_lista(lista):
    parte = len(lista) // 3
    parte1 = lista[:parte]
    parte2 = lista[parte:parte*2]
    parte3 = lista[parte*2:] 
    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = dividindo_lista(lista)
print(parte1, parte2, parte3)
````

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)

**12.** Dado o dicionário a seguir:

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.

````py
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

valores = list(speed.values())

sem_duplicidade = list(set(valores))

print(sem_duplicidade)
````

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)