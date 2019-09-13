# Trabalho de Segurança de redes

## Código
O sistema é um script simples em python que utiliza a classe `Criptograpy` para montar uma cruiptografia simples usando conceitos de cifra de César em cima da tabela ASCII com base numa chave.
Tal chave deve ser compartilhada entre quem precisa criptografar e descriptografar.
<br>
Essa chave deve ser salva como uma variável de ambiente `SECRETKEY`.


## Execução
Para a execução do projeto é necessário apenas executar o script via python:
```
python script.py
```
O script é compatível com o 3+.
Para realização de testes do script foi utilizado o docker, que é uma opção também.

## Execução via docker
```
docker run --rm -it -v $(pwd):/app -w /app python python script.py
```
