# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Interface visual em Streamlit (A "cara" da NEON-Fin)
├── agente.py           # O "cérebro" que conversa com o Ollama
├── database_manager.py # Lógica para ler seus arquivos JSON e CSV
├── requirements.txt    # O que precisa instalar
└── data/               # Onde você salvou os arquivos que criamos antes
```

## Exemplo de requirements.txt

```
streamlit
ollama
pandas
```

## Como Rodar

```bash
# 1. Certifique-se de que o Ollama está rodando no seu PC e você baixou o modelo:
ollama pull llama3.2

# 2. Instalar as dependências do Python
pip install -r src/requirements.txt

# 3. Rodar a aplicação Neon-Fin
streamlit run src/app.py
```
