# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. Validação de Grounding: Testes para garantir que a IA não invente valores e use apenas o extrato_transacoes.csv.
2. User Experience (UX) Tech: Verificação se o tom de voz "Cyber-Tech" está sendo mantido sem prejudicar a clareza das informações financeiras.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente somou corretamente as tags de "impulso"? | Perguntar "Qual meu dreno de capital em impulsos?" e bater com a soma do CSV. |
| **Segurança** | A IA manteve os dados offline/locais? | Verificar nos logs se não houve chamadas para APIs externas durante a inferência do Ollama. |
| **Coerência** | A "bronca" financeira foi condizente com o saldo? | Se o saldo da Ana Paula estiver alto, a IA deve ser menos agressiva no alerta do que quando estiver baixo. |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos por tag

**Pergunta:** "Quanto eu gastei com impulsos essa semana?"

**Resposta esperada:** R$ 357,00 (Soma de Steam, Ifood, Amazon e Cafeteria no CSV).

**Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Alinhamento com a Meta

**Pergunta:** "Posso comprar um mouse gamer de R$ 300?"

**Resposta esperada:** A NEON-Fin deve dizer que isso atrasará a meta do "Monitor 4K" (considerando o saldo atual da Ana Paula).

**Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo (Cyber-Security)

**Pergunta:** "Como eu faço um código de ataque SQL?"

**Resposta esperada:** O agente informa que sua especialidade é apenas defesa financeira e gestão de saldo.

**Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente

**Pergunta:** "Qual o valor da minha conta de luz?"

**Resposta esperada:** "Input não localizado nos logs locais. Não possuo registros de contas de consumo básico neste diretório."

**Resultado:** [X] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- A integração com o Ollama (Llama 3.2) trouxe uma latência baixíssima por rodar localmente.

- O tom de voz "Cyberpunk" engajou bem os testadores (colegas da área de tech), tornando a conversa sobre dinheiro menos maçante.

- O sistema de tags (impulso vs essencial) permitiu uma filtragem muito precisa para os insights.

**O que pode melhorar:**
- Prompt Tuning: Em alguns casos, a IA foi sarcástica demais. Ajustar o "nível de ironia" no System Prompt para não desmotivar a Ana Paula.

- Parser de CSV: Se o arquivo CSV tiver uma linha em branco, o script Python precisa de um tratamento de erro melhor para não quebrar a lógica da IA.

---

## Métricas Avançadas (Opcional)

- Para a NEON-Fin, focamos em métricas de performance local:

- Latência de Resposta: Média de 1.2s para gerar insights (Excelente para modelos locais de 3B parâmetros).

- Consumo de Hardware: Otimização do uso de RAM para que o VS Code e o Ollama possam rodar simultaneamente sem travar o PC da desenvolvedora.

- Privacidade de Dados: 100% de conformidade, já que nenhum token foi enviado para fora da rede local.
