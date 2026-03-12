import streamlit as st
import requests

st.title("Calculadora com API - DevRapido")

a = st.number_input("Primeiro numero")
b = st.number_input("Segundo numero")

operacao = st.selectbox(
    "Escolha a operação",
    ["soma", "subtracao", "multiplicacao", "divisao"]
)

if st.button("calcular"):

    dados = {
        "a": a,
        "b": b,
        "operacao": operacao
    }

    resposta =requests.post(
        "http://127.0.0.1:5000/calcular",
        json=dados
    )

    resultado = resposta.json()

    st.write("Resultado:", resultado)