# ⚡ NEON-Fin: Gestão Financeira Local & Inteligente

## 🎯 1. Caso de Uso

### O Problema
O "Consumismo Invisível" e a desorganização financeira causada por uma alta frequência de transações impulsivas (delivery, games e pequenas compras não planejadas), que afastam o usuário de seus objetivos de longo prazo.

### A Solução
A **NEON-Fin** atua como uma camada de inteligência local. Ela não apenas registra gastos, mas intervém com "Insights de Impacto", analisando o comportamento do usuário e protegendo seus sonhos através de uma análise técnica e motivacional.

### Público-Alvo
Jovens profissionais, estudantes de tecnologia (como a comunidade da **DIO**) e entusiastas de hardware que precisam de um "consciente digital" para equilibrar diversão e economia.

---

## 👤 2. Persona e Tom de Voz

- **Nome:** NEON-Fin
- **Personalidade:** Consultiva, perspicaz e focada em performance. Inspirada em interfaces futuristas e sistemas de monitoramento.
- **Tom de Voz:** Informal, moderno e tecnológico. Usa gírias de dev e termos de sistema.
- **Exemplo de fala:** *"Sistemas online. Detectando dreno de capital... Ana Paula, esse gasto em 'impulso' vai atrasar seu setup novo em 15 dias. Confirmar operação?"*

---

## 🏗️ 3. Arquitetura e Stack

O projeto foi construído priorizando a soberania dos dados e a performance local.

- **LLM Engine:** Ollama (Modelo Llama 3.2)
- **Interface:** Streamlit (UI Dark/Neon)
- **Linguagem:** Python 3.11+
- **Processamento de Dados:** Pandas para análise de CSV e JSON para configurações.

---

## 📂 4. Base de Conhecimento

A NEON-Fin fundamenta suas respostas (técnica de *Grounding*) em dados locais estruturados:

| Arquivo | Formato | Utilização |
| :--- | :--- | :--- |
| `cliente.json` | JSON | Perfil da cliente Ana Paula, metas (Ex: Monitor 4K) e status. |
| `extrato_transacoes.csv` | CSV | Histórico detalhado com tags de `impulso` e `essencial` (Ex: Assinatura DIO PRO). |
| `regras_bolso.json` | JSON | Limites de gastos definidos pela usuária para categorias críticas. |
| `base_dicas.csv` | CSV | Biblioteca de gatilhos comportamentais e dicas financeiras. |

---

## 🤖 5. Engenharia de Prompt

Para garantir respostas precisas e evitar alucinações, foram aplicadas as seguintes técnicas:

- **System Prompt Rígido:** Define a persona e proíbe a invenção de dados financeiros.
- **Few-Shot Prompting:** Exemplos reais de interações "Pergunta e Resposta" inseridos no contexto para calibrar o tom de voz.
- **Chain-of-Thought (Cadeia de Pensamento):** Instrução para que a IA analise o saldo e as tags de impulso antes de emitir qualquer opinião de compra.

---

## 📊 6. Avaliação e Métricas

O agente é avaliado com base em três pilares fundamentais:

| Métrica | O que avalia | Status |
| :--- | :--- | :--- |
| **Assertividade** | O agente somou corretamente as tags de "impulso" do CSV? | ✅ Sucesso |
| **Segurança** | O agente evitou inventar informações fora da base local? | ✅ Sucesso |
| **Coerência** | A resposta faz sentido para o perfil de "Consumista em Recuperação"? | ✅ Sucesso |
| **Privacidade** | Os dados saíram da rede local? | 🔒 Protegido (Offline) |

---

## 🚀 7. Como Executar

1. **Setup da IA (Ollama):**
   - Instale o [Ollama](https://ollama.com/).
   - No terminal, execute: `ollama pull llama3.2`.

2. **Instalação das Dependências:**
   ```bash
   pip install streamlit ollama pandas
