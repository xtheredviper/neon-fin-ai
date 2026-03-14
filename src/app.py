import streamlit as st
import pandas as pd
import json
import ollama


st.set_page_config(page_title="NEON-Fin ⚡", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #00ff41; }
    stButton>button { background-color: #00ff41; color: black; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

def carregar_contexto():
    try:
        with open('data/cliente.json', 'r', encoding='utf-8') as f:
            cliente = json.load(f)
        extrato = pd.read_csv('data/extrato_transacoes.csv')
        return cliente, extrato
    except:
        return None, None

st.title("⚡ NEON-Fin | Interface de Comando")
st.write("---")

cliente, extrato = carregar_contexto()

if cliente:
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Usuária", cliente['cliente'])
        st.metric("Meta", cliente['meta_ativa']['nome'])
    with col2:
        st.metric("Saldo Simulado", "R$ 1.250,40")
        st.metric("Status", cliente['status_financeiro'])

    st.write("### 📜 Logs de Transações Recentes")
    st.dataframe(extrato.tail(5))

    pergunta = st.text_input("Digite seu comando (ex: 'Analise meus impulsos'):")

    if st.button("Executar Script"):
        if pergunta:
            with st.spinner("Processando dreno de capital..."):
                
                resumo_gastos = extrato.to_string()
                prompt = f"Contexto: {resumo_gastos}. Pergunta: {pergunta}"
                
                try:
                    response = ollama.chat(model='llama3.2', messages=[
                        {'role': 'system', 'content': 'Você é a NEON-Fin, assistente Cyberpunk. Seja direta e analise gastos de impulso.'},
                        {'role': 'user', 'content': prompt}
                    ])
                    st.markdown("### 🤖 Output do Agente:")
                    st.info(response['message']['content'])
                except:
                    st.error("Ollama não detectado localmente. Certifique-se de que o serviço está ativo.")
else:
    st.warning("Aguardando carregamento dos arquivos em /data...")
