## <p align="center"> EXERCÍCIOS - PARTE 3</p>

**20.** Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.

Você deverá aplicar as seguintes funções no exercício:

map

filter

sorted

sum

Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):

a lista dos 5 maiores números pares em ordem decrescente;

a soma destes valores.

````py
with open('number.txt', 'r') as number:
    numeros = map(int, number)                  
    pares = filter(lambda x: x % 2 == 0, numeros) 
    pares_ordenados = sorted(pares, reverse=True)  
    cinco_maiores_pares = pares_ordenados[:5]     
    soma = sum(cinco_maiores_pares)               

print(cinco_maiores_pares)
print(soma)
````

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)

**21.** Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.

É obrigatório aplicar as seguintes funções:

len

filter

lambda

Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.

````py
def conta_vogais(texto: str) -> int:
    return len(list(filter(lambda c: c.lower() in "aeiou", texto)))

# Testando se conta e desconsidera acentuados
frase = "Programa Scholarship Compass UOL"
print(conta_vogais(frase))

frase = "Programa Scholarship é Compass UOL"
print(conta_vogais(frase))

# Verificado que sim pois em ambas as frases são contados 10, desconsiderando o "é"
````

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)

**22.** A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 

Abaixo apresentando uma possível entrada para a função.

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. Na lista anterior, por exemplo, teríamos como resultado final 200.

Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:

reduce (módulo functools)

map

````py
from functools import reduce

def calcula_saldo(lancamentos) -> float:
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    
    saldo = reduce(lambda a, b: a + b, valores)
    
    return saldo
    
# testando
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')]

print(calcula_saldo(lancamentos))
````

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)