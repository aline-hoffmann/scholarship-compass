# Escolhendo uma imagem oficial python, mas em uma versão mais leve
FROM python:3.9-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o etl para dentro do container
COPY etl.py .
COPY concert_tours_by_women.csv .


# Instalando dependências
RUN pip install pandas

# Definindo que ao rodar o container, o script etl será executado
CMD ["python", "etl.py"]