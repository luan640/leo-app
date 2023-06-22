import streamlit as st

st.title("Primeiro app do leo")

def calcular_imc(peso, altura):
    imc=peso/(altura * altura)
    return imc

def interp_imc(imc):
    if imc <18.5:
        return "abaixo do peso"
    elif imc < 25:
        return "peso normal"
    elif imc < 30:
        return "sobrepeso"
    else:
        return "obesidade"

peso = float(st.number_input("Seu peso: "))
altura = float(st.number_input("Sua altura: "))

if st.button("Calcular"):

    imc = calcular_imc(peso, altura)
    classificacao = interp_imc(imc)

    st.write("O seu imc é: ", imc)
    st.write("Classificação: ", classificacao)