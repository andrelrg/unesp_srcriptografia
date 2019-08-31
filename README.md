# Trabalho de Segurança de redes

## Código
O sistema é um script simples em python que utiliza a biblioteca [cryptography.fernet] para monta a criptografia de uma frase.

## Dependencias
O sistema tem como dependência a bibliteca cryptography do python, para a instalação segue o comando:
```
pip install cryptography
```

## Execução
Para a execução do projeto é necessário apenas executar o script via python:
```
python script.py
```
O script é compatível tanto com python 2.7+ quanto com o 3+.
Para realização de testes do script foi utilizado o docker, que é uma opção também.

## Execução via docker
```
docker pull python
docker run --rm -it -v $(pwd):/app -w /app python bash
```
E em seguida, executar a instalação da lib e executar o script.
 
