# Criando a lista com 20 nomes de animais
animais = [
    "gato", "cachorro", "elefante", "tigre", "leão",
    "girafa", "zebra", "urso", "macaco", "coelho",
    "cavalo", "rato", "baleia", "golfinho", "panda",
    "lobo", "coruja", "cobra", "papagaio", "tartaruga"
]

# Ordenando em ordem crescente (alfabética)
animais.sort()

# Imprimindo cada animal (iterando com list comprehension)
[print(animal) for animal in animais]

# Salvando a lista em um arquivo de texto (um animal por linha)
with open("animais.txt", "w") as arquivo:
    for animal in animais:
        arquivo.write(f"{animal}\n")