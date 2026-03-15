import streamlit as st
import pandas as pd
import json
import ollama

def carregar_dados():
    with open('data/cliente.json', 'r', encoding='utf-8') as f:
        cliente = json.load(f)
    extrato = pd.read_csv('data/extrato_transacoes.csv')
    return cliente, extrato

def consultar_ai(pergunta, dados_cliente, dados_extrato):
    contexto = f"Dados: {dados_cliente}\nExtrato: {dados_extrato.tail(10).to_string()}"
    
    resposta = ollama.chat(model='llama3.2', messages=[
        {'role': 'system', 'content': 'Você é a NEON-Fin, assistente financeira Cyberpunk.'},
        {'role': 'user', 'content': f"{contexto}\n\nPergunta: {pergunta}"}
    ])
    return resposta['message']['content']

st.set_page_config(page_title="NEON-Fin Local")
st.title("⚡ NEON-Fin: Painel de Controle")

try:
    usuario, transacoes = carregar_dados()
    st.header(f"Olá, {usuario['cliente']}!")
    
    aba1, aba2 = st.tabs(["Resumo Financeiro", "Consultar IA"])

    with aba1:
        st.subheader("Status Atual")
        st.write(f"**Meta:** {usuario['meta_ativa']['nome']}")
        st.dataframe(transacoes)

    with aba2:
        st.subheader("Pergunte ao Agente")
        user_query = st.text_input("Comando:")
        
        if st.button("Analisar"):
            if user_query:
                with st.spinner("Processando..."):
                    resultado = consultar_ai(user_query, usuario, transacoes)
                    st.info(resultado)

except FileNotFoundError:
    st.error("Erro: Arquivos não localizados na pasta 'data'.")
