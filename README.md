# ⚡ NEON-Fin: Gestão Financeira Local & Inteligente

## 🎯 1. Caso de Uso

### O Problema
O "Consumismo Invisível" e a desorganização financeira causada por uma alta frequência de transações impulsivas (delivery, games e pequenas compras não planejadas), que afastam o usuário de seus objetivos de longo prazo.

### A Solução
A **NEON-Fin** atua como uma camada de inteligência local. Ela não apenas registra gastos, mas intervém com "Insights de Impacto", analisando o comportamento do usuário e protegendo seus objetivos através de uma análise técnica e motivacional.

### Público-Alvo
Jovens profissionais, estudantes de tecnologia (como a comunidade da **DIO**) e entusiastas de hardware que precisam de um "consciente digital" para equilibrar diversão e economia.

---

## 👤 2. Persona e Tom de Voz

* **Nome:** NEON-Fin
* **Personalidade:** Consultiva, perspicaz e focada em performance. Inspirada em interfaces futuristas e sistemas de monitoramento.
* **Tom de Voz:** Informal, moderno e tecnológico. Usa gírias de dev e termos de sistema.
* **Exemplo de fala:** *"Sistemas online. Detectando dreno de capital... Ana Paula, esse gasto em 'impulso' vai atrasar seu setup novo em 15 dias. Confirmar operação?"*

---

## 🏗️ 3. Arquitetura e Stack

O projeto foi construído priorizando a soberania dos dados e a performance local (executado em hardware dedicado **NVIDIA RTX**).

* **LLM Engine:** Ollama (Modelo Llama 3.2)
* **Interface:** Streamlit (UI Dark/Neon)
* **Linguagem:** Python 3.14
* **Processamento de Dados:** Pandas para análise de CSV e JSON para configurações.

---

## 📂 4. Base de Conhecimento (Grounding)

A NEON-Fin fundamenta suas respostas em dados locais estruturados para garantir precisão:

| Arquivo | Formato | Utilização |
| :--- | :--- | :--- |
| `cliente.json` | JSON | Perfil da cliente **Ana Paula**, metas e status do sistema. |
| `extrato_transacoes.csv` | CSV | Histórico detalhado de gastos com tags de categoria e impacto. |

---

## 🤖 5. Engenharia de Prompt

Para garantir respostas precisas e evitar alucinações, foram aplicadas as seguintes técnicas:

1.  **System Prompt Rígido:** Define a persona e proíbe a invenção de dados financeiros não presentes nos arquivos.
2.  **Chain-of-Thought:** Instrução para que a IA analise o extrato e as metas antes de emitir qualquer opinião ou cálculo.
3.  **Context Injection:** Os dados do perfil e as últimas transações são injetados diretamente no prompt a cada consulta.

---

## 📊 6. Avaliação e Métricas

O agente é avaliado com base em quatro pilares fundamentais:

| Métrica | O que avalia | Status |
| :--- | :--- | :--- |
| **Assertividade** | O agente somou corretamente os gastos do CSV? | ✅ Sucesso |
| **Segurança** | O agente evitou inventar informações fora da base local? | ✅ Sucesso |
| **Coerência** | A resposta reflete o perfil de "Consumista em Recuperação"? | ✅ Sucesso |
| **Privacidade** | Os dados saíram da rede local? | 🔒 Protegido (Local) |

---

## 🚀 7. Como Executar

### 1. Setup da IA (Ollama)
* Instale o [Ollama](https://ollama.com/).
* No terminal, execute o comando para baixar o modelo:
    `ollama pull llama3.2`

### 2. Instalação das Dependências
No terminal do seu projeto, instale as bibliotecas necessárias:
```bash
pip install streamlit ollama pandas
