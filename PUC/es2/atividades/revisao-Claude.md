# Revisão Atividades P1 — Engenharia de Software II
## [08-05-2026][Claude]
---

**Resultado: ~3.5/5 — Q2 errada, Q5 incompleta**

---

## Acertos (Q1, Q3, Q4)

- **Estilos arquiteturais** (Q1): Identificou corretamente I e III. Soube que arquitetura orientada a objetos usa troca de mensagens (I verdadeira), que "monolítica = sistema dividido em pequenas partes" descreve microsserviços e não monolitos (II falsa), e que microsserviços têm baixo acoplamento, não alto (IV falsa).
- **Microsserviços** (Q3): Acertou direto. REST como mecanismo padrão de comunicação estava claro; identificou as outras alternativas como falsas (banco único, alto acoplamento, linguagem única).
- **Trade-offs monolito vs. microsserviços** (Q4): Tabela bem construída, pontos corretos e relevantes. Capturou o trade-off central de cada arquitetura — simplificidade inicial vs. complexidade operacional.

---

## Erros

### Q2 — Estilo arquitetural para aplicações em nuvem
- **Sua resposta:** b) em camadas
- **Correta:** d) cliente-servidor
- **Por que errou:** O enunciado descreve explicitamente *máquinas locais com poucos recursos* (clientes) acessando *recursos computacionais de maior desempenho* remotamente (servidores), com escalabilidade por adição de hosts. Esse é o modelo **cliente-servidor** por definição. "Em camadas" descreve a organização *interna* do software em camadas lógicas (apresentação → lógica de negócio → dados) — ela frequentemente coexiste com cliente-servidor, mas não é o que o enunciado descreve. A chave é a frase *"máquinas com poucos recursos utilizando recursos de maior desempenho"*: cliente fraco, servidor poderoso.

---

## Incompleto

### Q5 — Problemas com bancos de dados distribuídos em microsserviços
- **O que acertou:** Identificou o Teorema CAP corretamente e deu um exemplo concreto de trade-off disponibilidade vs. consistência. Esse é o problema mais conceitual e você foi direto ao ponto.
- **O que faltou:** A questão pede "quais *outros* problemas", no plural. Há pelo menos mais dois que o conteúdo do curso cobre:
  - **Transações distribuídas:** manter atomicidade (ACID) entre múltiplos bancos é inviável com 2-phase commit em escala. O padrão Saga resolve com consistência eventual e compensações.
  - **Consultas entre serviços:** JOINs simples em um banco único viram chamadas de API com latência adicional e maior complexidade de código (CQRS, views materializadas).
  - **Duplicação e sincronização:** microsserviços frequentemente replicam dados de outros serviços para evitar acoplamento, gerando overhead de sincronização e riscos de inconsistência.

---

## O que focar antes da P1

| Tópico | Lacuna identificada |
|---|---|
| Estilos arquiteturais | Diferencie cliente-servidor (topologia: quem usa quem na rede) de em camadas (organização lógica interna do código). Os dois coexistem mas descrevem dimensões diferentes. |
| Bancos distribuídos | CAP já está claro. Adicione transações distribuídas (Saga, 2PC) e o problema de queries cross-service (CQRS). |

Os acertos em Q1, Q3 e Q4 mostram boa base conceitual em microsserviços e arquitetura. O erro em Q2 é pontual — uma confusão entre dois estilos que frequentemente andam juntos. Em Q5 o raciocínio estava certo, só faltou ir mais fundo na lista de problemas práticos.
