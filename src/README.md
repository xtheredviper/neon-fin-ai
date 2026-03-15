# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
 ├── app.py           # Código principal (Interface + Lógica da IA + Leitura de Dados)
 ├── requirements.txt # Dependências do projeto
 └── data/            # Pasta com os arquivos cliente.json e extrato_transacoes.csv
```

## Exemplo de requirements.txt

```
streamlit
ollama
pandas
```

## Como Rodar

```bash
# 1. Certifique-se de que o Ollama está rodando no seu PC e baixe o modelo:
ollama pull llama3.2

# 2. Instalar as dependências do Python
pip install streamlit pandas ollama

# 3. Rodar a aplicação Neon-Fin
python -m streamlit run src/app.py
```
