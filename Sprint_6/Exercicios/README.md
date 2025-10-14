# PARTE 1.

## ETAPA 1
Comecei declarando e inicializando a lista com 250 números inteiros, obtidos de forma aleatória. Delimitei do 1 até o 2000.

````
numeros = [random.randint(1, 2000) for _ in range(250)]
````

Depois, inverti a ordem da lista utilizando o método "reverse", conforme solicitado.

````
numeros.reverse()
````

Por fim, imprimi o resultado.

````
print(numeros)
````

O código completo e o resultado impresso foram:

![imagem](../Evidencias/Exercicios/ex-p1-etapa1.jpg)
<br>

## ETAPA 2

Iniciei declarando e inicializando a lista com o nome de 20 animais.

````
animais = [
    "gato", "cachorro", "elefante", "tigre", "leão",
    "girafa", "zebra", "urso", "macaco", "coelho",
    "cavalo", "rato", "baleia", "golfinho", "panda",
    "lobo", "coruja", "cobra", "papagaio", "tartaruga"
]
````

Logo após, ordenei a lista em ordem crescente (ordem alfabética).

````
# Ordenando em ordem crescente (alfabética)
animais.sort()
````

Ademais, iterei sobre os itens utilizando o list comprehensior e imprimi um a um.

````
[print(animal) for animal in animais]
````

Por fim, armazenei o conteúdo da lista em um arquivo txt, com um item em cada linha, conforme solicitado.

````
with open("animais.txt", "w") as arquivo:
    for animal in animais:
        arquivo.write(f"{animal}\n")
````

O código completo e o resultado impresso foram:

![imagem](../Evidencias/Exercicios/cod-ex-p1-etapa2.jpg)

![imagem](../Evidencias/Exercicios/resultado-ex-p1-etapa2.jpg)

O arquivo txt gerado pode ser visualizado [aqui](COLOCAR O LINK DO GITBUH!!!!!!!!!!!!!).