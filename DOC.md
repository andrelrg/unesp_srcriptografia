# Trabalho de Segurança de redes

## Código
O sistema é um script simples em python que utiliza a classe `Criptograpy` para montar uma cruiptografia simples usando conceitos de cifra de César em cima da tabela ASCII com base numa chave.
Tal chave deve ser compartilhada entre quem precisa criptografar e descriptografar.
A palavra é criptografada caracter por caracter, a cada iteração a chave é remodelada para que uma nova crifra seja aplicada com base na chave.
Ou seja, qualquer alteração na chave irá gerar uma nova criptografia.
<br>
Essa chave deve ser salva como uma variável de ambiente `SECRETKEY`, para facilitar a execução o algoritmo já seta essa variável no arquivo `script.py`, e lá pode ser alterada.


## Execução
Para a execução do projeto é necessário apenas executar o script via python:
```
python3 script.py
```
O script é compatível com o python 3+.
Para realização de testes do script foi utilizado o docker, que é uma opção também.


## Execução via docker
```
docker run --rm -it -v $(pwd):/app -w /app python python script.py
```

## Testes
O script foi testado apenas no macOS, podendo haver bugs inesperados com outros sistemas operacionais pela criação da interface visual.
