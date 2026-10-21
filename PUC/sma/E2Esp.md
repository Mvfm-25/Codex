# E2 — Avaliação de Aprendizagem : Especificação de Respostas
## Simulação & Métodos Analíticos — Turma 691 — Entrega : 21/10/2026, 23h59
---
### Regras de entrega
- Resolução feita **à mão livre** (papel ou tablet com caneta digital), digitalizada num **único PDF** por sala de entrega.
- O desenvolvimento é obrigatório : só a resposta final, mesmo correta, não é considerada.
- Usar a notação do material da disciplina (Processo de Nascimento & Morte; N, D, U, W). Formato de resposta de LLM é zerado.
- Para a faixa **DESTACADA**, usar precisão de **4 casas decimais ou mais**.
- Salas : [Questão 1](https://moodle.pucrs.br/mod/assign/view.php?id=3926746) & [Questão 2](https://moodle.pucrs.br/mod/assign/view.php?id=3926747).

---
## Questão 1 — Fila M/M/1 (sem perda)

### Enunciado
Fila da cafeteria Bauducco analisada por Processo de Nascimento e Morte, com **1 funcionário**. Clientes não são perdidos (sempre entram na fila e em algum momento são atendidos). Chegam em média **6 clientes/h** e são atendidos em média **9,5 clientes/h**. Chegadas e atendimentos seguem distribuições exponenciais.

1. Qual a probabilidade de se chegar nesta fila no intervalo de 1 hora e encontrá-la com **mais do que 10 clientes**? Demonstre passo a passo. **[30 pontos]**
2. Qual é o **tempo de serviço máximo (em minutos)** para que a fila continue com solução à forma-produto, ou seja, respeitando a hipótese da estacionariedade? Demonstre e disserte. **[20 pontos]**

### Rubrica
| Pergunta | Destacada | Satisfatória | Parcial | Insuficiente |
|---|---|---|---|---|
| 1.1 — P(N > 10) | 30 : cálculos corretos, ≥ 4 casas | 25 : cálculos corretos, < 4 casas | 15 : erro de conta sem comprometer o racional | 0 : não entregue ou resposta absurda |
| 1.2 — Tempo máximo | 20 : racional coerente, resposta precisa | 15 : racional coerente, resposta aproximada | 10 : racional coerente, resposta errada | 0 : não entregue ou racional sem sentido |

### Resposta esperada

**Dados :** λ = 6 cli/h ; μ = 9,5 cli/h ; 1 servidor ; capacidade infinita.

#### 1.1 — Probabilidade de mais de 10 clientes
1. Nascimento & Morte com λₖ = λ e μₖ = μ para todo k :
   Pₖ = P₀ · (λ/μ)ᵏ = P₀ · ρᵏ
2. ρ = λ/μ = 6 / 9,5 = **0,631579**
3. Normalização : Σ Pₖ = 1 ⇒ P₀ · 1/(1 − ρ) = 1 ⇒ P₀ = 1 − ρ = **0,368421**
4. P(N > 10) = 1 − Σₖ₌₀¹⁰ Pₖ = 1 − (1 − ρ)·(1 − ρ¹¹)/(1 − ρ) = ρ¹¹

| k | Pₖ = (1 − ρ)ρᵏ |
|---|---|
| 0 | 0,368421 |
| 1 | 0,232687 |
| 2 | 0,146960 |
| 3 | 0,092817 |
| 4 | 0,058621 |
| 5 | 0,037024 |
| 6 | 0,023384 |
| 7 | 0,014769 |
| 8 | 0,009328 |
| 9 | 0,005891 |
| 10 | 0,003721 |
| **Σ** | **0,993622** |

5. **P(N > 10) = 1 − 0,993622 = ρ¹¹ ≈ 0,006378 (≈ 0,6378 %)**

> O "intervalo de 1 hora" não altera o cálculo : pede-se a probabilidade estacionária de um cliente que chega encontrar o sistema com mais de 10 clientes.

#### 1.2 — Tempo de serviço máximo
- A solução em forma-produto (estacionária) só existe se a série Σ ρᵏ converge, ou seja, **ρ = λ/μ < 1 ⇔ μ > λ**.
- Tempo médio de serviço = 1/μ. Logo : 1/μ < 1/λ = 1/6 h.
- **Tempo de serviço máximo : 10 minutos** (limite estrito, 1/μ < 10 min).
- Atualmente : 1/μ = 60 / 9,5 ≈ 6,3158 min, então o sistema é estável.
- Racional : se 1/μ ≥ 10 min, os clientes chegam no mínimo tão rápido quanto são atendidos; a fila cresce sem limite, P₀ → 0 e não existe distribuição estacionária.

---
## Questão 2 — Fila M/M/3/5 (com perda)

### Enunciado
Continuação do estudo da cafeteria Bauducco por Processo de Nascimento e Morte, agora com **3 funcionários** e **capacidade igual a 5 clientes**. Cliente que chega com a fila cheia é **perdido**. Chegam em média **5 clientes/h** e são atendidos em média **2 clientes/h**. Chegadas e atendimentos seguem distribuições exponenciais.

1. Qual é a **perda de clientes por hora** da fila? Demonstre passo a passo. **[20 pontos]**
2. Qual o **tempo de resposta da fila em minutos**, ou seja, quantos minutos em média os clientes esperam, são atendidos e vão embora? **[30 pontos]**

### Rubrica
| Pergunta | Destacada | Satisfatória | Parcial | Insuficiente |
|---|---|---|---|---|
| 2.1 — Perda/h | 20 : cálculos corretos, ≥ 4 casas | 15 : cálculos corretos, < 4 casas | 10 : erro de conta sem comprometer o racional | 0 : não entregue ou resposta absurda |
| 2.2 — Tempo de resposta | 30 : todos os cálculos (inclusive N e D), resposta correta em minutos | 25 : erro em N e/ou D, resposta imprecisa mas em minutos | 15 : racional coerente, resposta não está em minutos | 0 : não entregue ou resposta absurda |

### Resposta esperada

**Dados :** λ = 5 cli/h ; μ = 2 cli/h ; c = 3 servidores ; K = 5 (capacidade total do sistema, incluindo quem está em atendimento → estados 0 a 5).

**Taxas de serviço por estado :** μₖ = min(k, 3) · μ → μ₁ = 2 ; μ₂ = 4 ; μ₃ = μ₄ = μ₅ = 6.

**Probabilidades de estado** (Pₖ = Pₖ₋₁ · λ / μₖ) :

| k | Pₖ / P₀ | Pₖ |
|---|---|---|
| 0 | 1 | 0,075713 |
| 1 | 5/2 = 2,5 | 0,189283 |
| 2 | 2,5 · 5/4 = 3,125 | 0,236603 |
| 3 | 3,125 · 5/6 = 2,604167 | 0,197170 |
| 4 | 2,604167 · 5/6 = 2,170139 | 0,164308 |
| 5 | 2,170139 · 5/6 = 1,808449 | 0,136923 |
| **Σ** | **13,207755** | **1** |

P₀ = 1 / 13,207755 = **0,075713**

#### 2.1 — Perda de clientes por hora
- Cliente é perdido quando chega com o sistema cheio (k = 5).
- **Perda = λ · P₅ = 5 × 0,136923 ≈ 0,6846 clientes/h**

#### 2.2 — Tempo de resposta em minutos
1. **População média (N) :**
   N = Σ k · Pₖ = 1·0,189283 + 2·0,236603 + 3·0,197170 + 4·0,164308 + 5·0,136923 = **2,5958 clientes**
2. **Vazão (D) :**
   D = Σ μₖ · Pₖ = 2·0,189283 + 4·0,236603 + 6·(0,197170 + 0,164308 + 0,136923) = **4,3154 clientes/h**
   - Verificação : D = λ · (1 − P₅) = 5 × 0,863077 = 4,3154 = λ − perda.
3. **Tempo de resposta (Lei de Little) :**
   W = N / D = 2,5958 / 4,3154 = 0,601533 h
4. **W ≈ 36,09 minutos**

> A resposta deve estar em minutos : deixar em horas cai para a faixa PARCIAL.

---
### Resumo
| Questão | Pergunta | Resposta |
|---|---|---|
| 1 | P(N > 10) | ρ¹¹ ≈ **0,006378** |
| 1 | Tempo de serviço máximo | **< 10 min** |
| 2 | Perda por hora | **≈ 0,6846 cli/h** |
| 2 | Tempo de resposta | **≈ 36,09 min** (N = 2,5958 ; D = 4,3154) |
