# Escolhendo uma imagem oficial python, mas em uma versão mais leve
FROM python:3.9-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o job para dentro do container
COPY job.py .

# Instalando dependências
RUN pip install pandas matplotlib numpy

# Definindo que ao rodar o container, o script etl será executado
CMD ["python", "job.py"]