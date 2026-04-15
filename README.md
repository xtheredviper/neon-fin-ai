# ⚡ NEON-Fin: Smart & Local Financial Management

## 🎯 1. Use Case

### The Problem
"Invisible Consumerism" and financial disorganization caused by a high frequency of impulsive transactions (delivery, games, and small unplanned purchases), which drift the user away from their long-term goals.

### The Solution
**NEON-Fin** acts as a local intelligence layer. It doesn't just record expenses; it intervenes with "Impact Insights," analyzing user behavior and protecting their goals through technical and motivational analysis.

### Target Audience
Young professionals, tech students (like the **DIO** community), and hardware enthusiasts who need a "digital conscience" to balance fun and savings.

---

## 👤 2. Persona and Tone of Voice

* **Name:** NEON-Fin
* **Personality:** Advisory, insightful, and performance-focused. Inspired by futuristic interfaces and monitoring systems.
* **Tone of Voice:** Informal, modern, and tech-driven. Uses dev slang and system terminology.
* **Catchphrase Example:** *"Systems online. Detecting capital drain... Ana Paula, this 'impulse' expense will delay your new setup by 15 days. Confirm operation?"*

---

## 🏗️ 3. Architecture and Stack

The project was built prioritizing data sovereignty and local performance (running on dedicated **NVIDIA RTX** hardware).

* **LLM Engine:** Ollama (Llama 3.2 Model)
* **Interface:** Streamlit (Dark/Neon UI)
* **Language:** Python 3.14
* **Data Processing:** Pandas for CSV analysis and JSON for configurations.

---

## 📂 4. Knowledge Base (Grounding)

NEON-Fin bases its responses on structured local data to ensure accuracy:

| File | Format | Usage |
| :--- | :--- | :--- |
| `cliente.json` | JSON | **Ana Paula's** profile, goals, and system status. |
| `extrato_transacoes.csv` | CSV | Detailed spending history with category and impact tags. |

---

## 🤖 5. Prompt Engineering

To ensure accurate responses and avoid hallucinations, the following techniques were applied:

1. **Strict System Prompt:** Defines the persona and prohibits the invention of financial data not present in the files.
2. **Chain-of-Thought:** Instructions for the AI to analyze the statement and goals before issuing any opinion or calculation.
3. **Context Injection:** Profile data and latest transactions are injected directly into the prompt with each query.

---

## 📊 6. Evaluation and Metrics

The agent is evaluated based on four fundamental pillars:

| Metric | What it evaluates | Status |
| :--- | :--- | :--- |
| **Assertiveness** | Did the agent correctly sum the expenses from the CSV? | ✅ Success |
| **Safety** | Did the agent avoid inventing information outside the local base? | ✅ Success |
| **Coherence** | Does the response reflect the "Recovering Consumer" profile? | ✅ Success |
| **Privacy** | Did the data leave the local network? | 🔒 Protected (Local) |

---

## 🚀 7. How to Run

### 1. AI Setup (Ollama)
* Install [Ollama](https://ollama.com/).
* In the terminal, run the command to download the model:
    `ollama pull llama3.2`

### 2. Dependency Installation
In your project terminal, install the necessary libraries:
```bash
pip install streamlit ollama pandas
