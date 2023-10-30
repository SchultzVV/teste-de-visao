# Makefile for Python Flask Application

# Define a imagem Docker a ser usada
DOCKER_IMAGE = teste-visao

# Diretório de código-fonte da aplicação
#SRC_DIR = /home/v/Desktop/fiesc-visao

# Alvo para construir a imagem Docker
build:
	docker build --no-cache -t $(DOCKER_IMAGE) .

# Alvo para executar a verificação de estilo com flake8
lint:
	flake8 src/*

# Alvo para iniciar o contêiner Docker
start:
	docker run -p 5000:5000 --name $(DOCKER_IMAGE)-container -d $(DOCKER_IMAGE)

# Alvo para parar e remover o contêiner Docker
stop:
	docker stop $(DOCKER_IMAGE)-container
	docker rm $(DOCKER_IMAGE)-container

.PHONY: build lint start stop
