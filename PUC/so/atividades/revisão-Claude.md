# Revisão P1 — Análise de Desempenho
## [27-04-2026][Claude]
---

**Resultado: 12/15 (80%)**

---

## Acertos (Q1–Q9, Q12, Q13, Q15)

Você acertou todo o bloco inicial com solidez. Isso indica boa compreensão dos fundamentos:

- **Processos & estados** (Q1, Q2): conceito correto de processo como entidade ativa vs. passiva, e o ciclo Ready→Running pelo dispatch.
- **Threads** (Q3, Q4): sabia o que é compartilhado (código, dados, recursos) e o que é privado (stack, PC, registradores), e a vantagem de custo.
- **IPC & comunicação** (Q5, Q6): distinguiu Shared Memory de Message Passing, e entendeu o conceito de blocking send.
- **Escalonamento** (Q7, Q8): dispatch latency e a otimalidade do SJF estavam claros.
- **Concorrência básica** (Q9): definição correta de race condition.
- **Deadlock** (Q12, Q13): soube identificar o deadlock e as quatro condições de Coffman corretamente.
- **Sockets** (Q15): definição correta.

---

## Erros

### Q10 — Requisitos da Seção Crítica
- **Sua resposta:** C — *Atomicidade, Durabilidade & Isolamento*
- **Correta:** B — *Exclusão Mútua, Progresso e Espera Limitada*
- **Por que errou:** Confusão entre as propriedades **ACID** (banco de dados/transações) e os três requisitos clássicos da seção crítica. São domínios diferentes. Os três requisitos são: (1) só um processo na seção crítica por vez, (2) a decisão de entrar não pode ser postergada indefinidamente, e (3) nenhum processo espera para sempre.

### Q11 — Semáforo de Contagem
- **Sua resposta:** A — *Garantir que apenas um processo entre na seção crítica por vez*
- **Correta:** B — *Controlar o acesso a um recurso com número finito de instâncias*
- **Por que errou:** O que foi descrito é a função de um **semáforo binário** (mutex). O semáforo de **contagem** é inicializado com N (número de instâncias do recurso) e permite até N processos simultâneos — pense em um pool de N conexões de banco de dados. A distinção binário vs. contagem é exatamente essa.

### Q14 — Banker's Algorithm
- **Sua resposta:** A — *Prevenção de Deadlock*
- **Correta:** C — *Evasão (Avoidance) de Deadlock*
- **Por que errou:** Há uma distinção técnica importante entre os quatro tratamentos de deadlock:
  - **Prevenção (Prevention):** elimina estaticamente uma das condições de Coffman na fase de projeto do sistema.
  - **Evasão (Avoidance):** o SO avalia dinamicamente cada pedido de recurso para garantir que o sistema permaneça em *estado seguro*. O Banker's Algorithm faz exatamente isso — simula a alocação e rejeita se o estado resultar em inseguro.
  - **Detecção & Recuperação:** deixa o deadlock ocorrer e depois age.
  - O Banker's é **Avoidance**, não Prevention.

---

## O que focar antes da P1

| Tópico | Lacuna identificada |
|---|---|
| Seção Crítica | Memorize os 3 requisitos: Exclusão Mútua + Progresso + Bounded Waiting. Não confundir com ACID. |
| Tipos de Semáforo | Binário = mutex (1 processo por vez). Contagem = pool de N recursos. |
| Taxonomia de Deadlock | Grave a hierarquia: Prevention → Avoidance (Banker's) → Detection → Recovery. |

Os dois primeiros erros têm raiz comum: confusão entre conceitos de domínios diferentes que soam parecidos. Vale revisar o capítulo de sincronização com foco em diferenciar semáforo binário de contagem, e separar mentalmente os conceitos de SO dos de banco de dados.
