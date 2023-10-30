# Use a imagem oficial do Python como imagem base
FROM python:3.9


# Define o diretório de trabalho no contêiner
WORKDIR /app

#RUN apt-get update

#RUN && apt-get install -y libsm6 libxext6 libx

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Copie o código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta em que a aplicação Flask irá rodar (substitua 5000 pela porta que você estiver usando)
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["python", "/app/src/app.py"]
