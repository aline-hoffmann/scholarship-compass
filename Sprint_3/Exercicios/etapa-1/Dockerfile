# Escolhendo uma imagem oficial python, mas em uma versão mais leve
FROM python:3.9-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o carguru para dentro do container
COPY carguru.py .

# Definindo que ao rodar o container, o script carguru será executado
CMD ["python", "carguru.py"]