# API de Calculadora em Python

## Descrição

Este projeto consiste em uma API simples desenvolvida em Python para realizar operações matemáticas básicas.
A aplicação recebe dois números e uma operação (soma, subtração, multiplicação ou divisão) e retorna o resultado em formato JSON.

A API foi desenvolvida utilizando Flask.
Além da API, foi criada uma interface simples utilizando Streamlit para permitir que o usuário realize os cálculos de forma visual, através do navegador.

O objetivo do projeto é demonstrar a criação rápida de uma API e sua integração com uma interface simples, seguindo a proposta da disciplina de Desenvolvimento Rápido de Aplicações em Python.

---

## Tecnologias utilizadas

* Python
* Flask
* Streamlit
* Requests

---

## Estrutura do projeto

```
calculadora-api
│
├── app.py
├── interface.py
└── README.md
```

* **app.py**: implementação da API com Flask
* **interface.py**: interface gráfica simples feita com Streamlit que consome a API

---

## Instalação

Primeiro instale as dependências necessárias:

```
pip install flask
pip install streamlit
pip install requests
```

---

## Executando o projeto

Para que a interface funcione corretamente, a API precisa estar rodando.

### 1. Iniciar a API

No terminal execute:

```
python app.py
```

A API será iniciada em:

```
http://127.0.0.1:5000
```

---

### 2. Iniciar a interface

Em outro terminal execute:

```
python -m streamlit run interface.py
```

A interface será aberta automaticamente no navegador.

---

## Endpoint da API

### POST /calcular

Responsável por realizar os cálculos.

URL:

```
http://127.0.0.1:5000/calcular
```

---

## Exemplo de requisição

```
POST /calcular
Content-Type: application/json
```

```
{
  "a": 10,
  "b": 5,
  "operacao": "soma"
}
```

---

## Exemplo de resposta

```
{
  "a": 10,
  "b": 5,
  "operacao": "soma",
  "resultado": 15
}
```

---

## Operações disponíveis

* soma
* subtracao
* multiplicacao
* divisao

---

## Tratamento de erros

Caso seja realizada divisão por zero, a API retorna a seguinte resposta:

```
{
  "Erro": "Nao e possivel dividir por zero."
}
```

---

## Possíveis melhorias

- Adicionar mais operações matemáticas

- Implementar validação de dados de entrada

- Adicionar testes automatizados
