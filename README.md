# Atados

API escrita em Django, Docker com banco de dados postgresql. Nesta API você consegue fazer o CRUD das instituições, despesas e voluntarios. Mostrando quanto vai sobrar para a instituição,  a soma das despesas da instituição e a soma dos dinheiros doados pelos voluntarios.

Para rodas a api no seu computador rodar os comandos abaixo:

docker build .
docker-compose build
docker-compose up

## Instituições 

Registrar Instituições POST http://localhost:8000/instituicoes/


```javascript
{
    "instituicao": "",
    "rua": "",
    "bairro": "",
    "cidade": "",
    "descricao": "",
    "despesas": []
}
```

Atualizar Instituições PUT http://localhost:8000/instituicoes/2/


```javascript
{
        "instituicao": "Associação Bras de Instituições Filantrópicas de Combao Câncer",
        "rua": "Av teste",
        "bairro": "Bairro Dos Casas",
        "cidade": "SBC",
        "descricao": "Instituicao fundada a 1990 ....",
        "despesas": [
            1,
            2
        ]
 }
```

Deletar Instituições DELETE http://localhost:8000/instituicoes/2/

Listar Instituições GET http://localhost:8000/instituicoes/

```javascript
{
        "id": 1,
        "instituicao": "Associação Bras de Instituições Filantrópicas de Combao Câncer",
        "rua": "Av teste",
        "bairro": "Bairro Dos Casas",
        "cidade": "SBC",
        "descricao": "Instituicao fundada a 1990 ....",
        "despesas": [
            1,
            2
        ]
 }
```

## Voluntarios

Registrar voluntarios POST http://localhost:8000/voluntarios/

```javascript
{
    "nome": "Guilherme",
    "sobrenome": "Alves",
    "bairro": "Taboao",
    "cidade": "Diadema",
    "dinheiro_doado": 200.50,
    "instituicao": 1
}
```

Atualizar voluntarios PUT http://localhost:8000/voluntarios/2/

```javascript
{
    "nome": "Keka",
    "sobrenome": "Santos",
    "bairro": "Taboao da serra",
    "cidade": "Diadema",
    "dinheiro_doado": 200.50,
    "instituicao": 1
}
```

Deletar voluntarios DELETE http://localhost:8000/voluntarios/5/

Listar voluntarios GET http://localhost:8000/voluntarios/

```javascript
[
  {
    "id": 1,
    "nome": "Guilherme",
    "sobrenome": "Alves",
    "bairro": "Eldorado",
    "cidade": "Diadema",
    "dinheiro_doado": "100.40",
    "instituicao": "Associação Bras de Instituições Filantrópicas de Combao Câncer"
  },
  {
    "id": 2,
    "nome": "Keka",
    "sobrenome": "Santos",
    "bairro": "Taboao da serra",
    "cidade": "Diadema",
    "dinheiro_doado": "200.50",
    "instituicao": "Associação Bras de Instituições Filantrópicas de Combao Câncer"
  }
]
```

Soma do dinheiro doado pelos voluntarios GET http://localhost:8000/somaVoluntarios/

```javascript
{
  "soma": 300.9
}
```

## Despesas

Registrar despesas POST http://localhost:8000/despesas/

```javascript
 {
    "nome_conta": "Luz",
    "valor": "50.30"
 }
 ```
 
 Atualizar despesas PUT http://localhost:8000/despesas/5/
 
 ```javascript
  {
    "nome_conta": "net",
    "valor": "50.20"
 }
  ```
  
  Deletar despesas DELETE http://localhost:8000/despesas/5/
  
  Listar despesas GET http://localhost:8000/despesas/
  
   ```javascript
  [
  {
    "id": 1,
    "nome_conta": "Luz",
    "valor": "40.50"
  },
  {
    "id": 2,
    "nome_conta": "agua",
    "valor": "100.40"
  },
  {
    "id": 3,
    "nome_conta": "vivo",
    "valor": "50.00"
  },
  {
    "id": 5,
    "nome_conta": "net",
    "valor": "50.20"
  }
]
 ```
 
 Soma das despesas da instituição GET http://localhost:8000/somaDespesas/
```javascript
{
  "soma": 241.1
}
```

Esta URL faz o bate do dinheiro doado e das despesas mostrando a sobra que a instituição vai ter GET http://localhost:8000/sobra/

```javascript
{
  "sobra": 59.8
}
```
  
  
  
  













