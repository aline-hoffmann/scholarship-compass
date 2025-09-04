# Escolhendo uma imagem oficial python, mas em uma versão mais leve
FROM python:3.9-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o masc-dados para dentro do container
COPY masc-dados.py /app

# Definindo que ao rodar o container, o script masc-dados será executado
CMD ["python", "masc-dados.py"]