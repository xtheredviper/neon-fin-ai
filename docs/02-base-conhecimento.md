# Base de Conhecimento

## Dados Utilizados

O agente utiliza arquivos locais simulando uma estrutura de Open Finance para garantir que a análise de consumo seja precisa e personalizada.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `cliente.json` | JSON| Contém o perfil, metas (ex: novo setup) e teto de gastos diários. |
| `extrato_transacoes.csv` | CSV | Registro detalhado de compras (essenciais vs. supérfluas). |
| `regras_bolso.json` | JSON | Limites pré-definidos pelo usuário para categorias como "Lazer" e "Delivery". |
| `base_dicas.csv` | CSV | Biblioteca de frases e estratégias de economia com tom moderno/gamer. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram expandidos para incluir Tags de Comportamento. Em vez de apenas "Alimentação", as transações no CSV agora possuem tags como impulso, essencial ou assinatura_esquecida. Isso permite que a NEON-Fin identifique padrões de consumo emocional, algo fundamental para o público de jovens profissionais.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos são lidos localmente pelo script Python utilizando as bibliotecas json e pandas. Os dados são carregados no momento em que o usuário inicia o chat, criando uma "memória de curto prazo" para a sessão.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são injetados dinamicamente no System Prompt. A cada nova interação, o backend filtra as últimas 5 transações e o saldo atual, enviando um resumo estruturado para o Ollama. Isso garante que a IA sempre saiba "onde o dinheiro está indo" sem precisar ler o arquivo inteiro a cada segundo.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: Ana Paula
- Status: Estudante de Tech / Backend Jr.
- Saldo Disponível: R$ 1.250,40
- Meta Ativa: "Upgrade de Monitor 4K" (Progresso: 40%)

Últimas transações:
- 10/03: Steam Games - R$ 159,90 (Tag: impulso)
- 11/03: Ifood - R$ 65,00 (Tag: lazer)
- 12/03: Assinatura Cloud - R$ 29,90 (Tag: essencial)
...
```
