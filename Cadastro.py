import streamlit as st
import pandas as pd
import datetime
from datetime import date

def gravar_dados(nome_cliente, dt_nasc, tipo):
    if nome_cliente and dt_nasc <= date.today():
        with open('clientes.csv', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{nome_cliente},{dt_nasc},{tipo}\n")
        st.session_state['sucesso'] = True

    else:
        st.session_state['sucesso'] = False

st.set_page_config(
    page_title="Cadastro de Clientes", 
    page_icon=":bust_in_silhouette:", 
    layout="wide")

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input('Digite o nome do cliente:',
                     key='nome_cliente')

#Define o range da data 
min_date = datetime.date(1900, 1, 1)
max_date = datetime.date(2100,12,31)

dt_nasc = st.date_input('Data nascimento', format='DD/MM/YYYY', key='data_nascimento', min_value=min_date, max_value=max_date)

tipo = st.selectbox('Tipo do Cliente',
                    ['Pessoa Jurídica', 'Pessoa Física'], key='tipo_cliente')

btn_cadastrar = st.button('Cadastrar',
                          on_click=gravar_dados, args=(nome, dt_nasc,tipo))

if btn_cadastrar:
    if st.session_state['sucesso']:
        st.success('Cliente cadastrado com sucesso!',
                   icon="✅")
    else:
        st.error('Erro ao cadastrar cliente. Verifique os dados informados.',
                 icon="❌")
