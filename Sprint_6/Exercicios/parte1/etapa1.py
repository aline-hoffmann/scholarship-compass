import random

# Criando lista com 250 números inteiros aleatórios entre 1 e 2000
numeros = [random.randint(1, 2000) for _ in range(250)]

# Invertendo a ordem da lista com o método reverse()
numeros.reverse()

# Imprimindo o resultado
print(numeros)