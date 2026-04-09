# Projeto de Desenvolvimento de Jogos — Adições & Aprofundamentos
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas. Segue os tópicos na ordem em que apareceram, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---

### Pipeline de Produção — O que cada fase realmente entrega

As notas descrevem as fases mas não o que é o artefato concreto de saída de cada uma:

| Fase | Entrega concreta |
|---|---|
| Conceito | High-concept (1-2 frases), pitch document, análise de viabilidade |
| Pré-produção | GDD (Game Design Document), protótipo jogável, pipeline técnico validado, orçamento |
| Produção | Alpha, Beta, Gold Master |
| Pós-produção | Patches, DLCs, port para outras plataformas, post-mortem |

O **GDD** é o documento central da pré-produção — especifica mecânicas, narrativa, arte conceitual, sistemas de áudio, UI e metas de performance. Em estúdios modernos ele vive em wikis (Confluence, Notion) em vez de um PDF estático, pois muda constantemente.

---

### Bartle Taxonomy — O que as notas não explicam sobre cada tipo

As quatro categorias (Socializador, Matador, Explorador, Conquistador) têm uma relação com **dois eixos**:

```
                Agir
                 ↑
Matador          |          Conquistador
(Players)        |          (World)
-----------------+------------------→ Interagir
(Players)        |          (World)
Socializador     |          Explorador
                 |
              Interagir
```

- Eixo X: foco em **jogadores** vs. foco no **mundo**
- Eixo Y: **agir** vs. **interagir**

Nenhum jogador real é 100% de um tipo — são combinações. Um jogo bem balanceado oferece algo para cada tipo. Counter-Strike atende Matadores e Socializadores. Dark Souls atende Conquistadores e Exploradores.

---

### MDA Framework — A direção que designer e jogador percorrem

O ponto mais importante do MDA que ficou implícito nas notas:

- **Designer** pensa de M → D → A (cria mecânicas, antecipa dinâmicas, projeta estética desejada)
- **Jogador** experimenta de A → D → M (sente a estética primeiro, percebe as dinâmicas depois, só eventualmente "vê" as mecânicas)

Isso explica por que mecânicas bem documentadas no papel frequentemente criam experiências ruins: o designer estava pensando em M enquanto o jogador só vai chegar lá muito depois, se chegar.

**Exemplo com Portal:**
- Mecânica: portais que preservam momentum
- Dinâmica: puzzles emergentes de troca de perspectiva e momentum acumulado
- Estética: sensação de descoberta e engenhosidade

---

### Flow State — A fórmula de Csikszentmihalyi

O gráfico das notas mostra o conceito. O que ficou faltando é a estrutura: o estado de flow ocorre quando **desafio e habilidade estão equilibrados e elevados simultaneamente**:

```
Desafio
  ↑  Ansiedade | FLOW
     ----------|----------
     Tédio     |
               └──────────→ Habilidade
```

- Desafio >> Habilidade = ansiedade, frustração
- Habilidade >> Desafio = tédio
- Ambos baixos = apatia
- Ambos altos e próximos = **flow**

A curva de dificuldade de um jogo bem desenhado não é linear — ela sobe junto com a habilidade do jogador, mantendo o equilíbrio. Tutoriais bem feitos são a entrada no eixo antes do flow começar.

---

### Dominância e Equilíbrio — O Nash que estava escondido no Dilema do Prisioneiro

As notas mencionam estratégia dominante no contexto do Dilema do Prisioneiro. O conceito formal que estava por baixo é o **Equilíbrio de Nash**: um estado onde nenhum jogador tem incentivo para mudar de estratégia dado o que os outros estão fazendo.

No Dilema do Prisioneiro, o único equilíbrio de Nash é **ambos confessarem** — mesmo que ambos calarem seja melhor para o grupo. Isso é o problema central do game design competitivo: o equilíbrio individual e o equilíbrio coletivo raramente coincidem.

**Consequências práticas:**
- Uma estratégia dominante elimina escolha real → jogo fica chato
- Sem equilíbrio claro → jogo fica caótico e injusto
- O sweet spot é ter múltiplas estratégias viáveis com trade-offs reais (rock-paper-scissors é o exemplo mínimo)

---

### Complexidade Emergente — Por que Go nunca teve dois jogos iguais

As notas citam Go como exemplo. O número de posições possíveis em Go é aproximadamente $2.08 \times 10^{170}$ — maior que o número de átomos no universo observável ($10^{80}$). Com apenas duas regras principais:

1. Stones do mesmo time conectados formam grupos
2. Grupos sem liberdades são capturados

Isso é **emergência**: regras simples, espaço de possibilidades astronômico. O mesmo princípio do Tetris, xadrez, e Magic: The Gathering.

**Regras de ouro para gerar emergência:**
- Cada elemento interage com múltiplos outros (não apenas com o sistema central)
- Contexto muda o resultado de uma mesma ação
- Consequências têm alcance temporal (decisão agora afeta situação depois)

---

### Pacing — A Estrutura Narrativa que estava por baixo

As notas mencionam a **Jornada do Herói** de passagem. A estrutura de três atos é mais diretamente aplicável ao pacing de jogos:

```
Ato 1 (Setup)      →  Ato 2 (Confronto)     →  Ato 3 (Resolução)
Introdução         →  Complicações escalando  →  Clímax + Desfecho
~25% do jogo       →  ~50% do jogo           →  ~25% do jogo
```

A cena da girafa em The Last of Us que as notas mencionam é um **beat de alívio** no meio do Ato 2 — a teoria chama isso de "valley" antes do próximo "peak". Sem valleys, o jogador dessensibiliza. Sem peaks, entedia.

O **Diretor do Left 4 Dead** é um caso raro de pacing algorítmico: ele monitora métricas do time (HP, ammo, distância do objetivo) e ajusta spawns e itens em tempo real para manter a tensão no nível ideal — flow state aplicado sistemicamente.

---

### Protótipos — Os três tipos e quando usar cada um

As notas mencionam papel & caneta, wireframe e prototipação digital. A distinção importante é a **fidelidade**:

- **Baixa fidelidade (papel)**: testa conceito e regras. Custo: horas. Ideal para validar "isso é divertido?"
- **Média fidelidade (wireframe/grey-box)**: testa layout, fluxo e feel. Custo: dias. Ideal para validar "isso funciona?"
- **Alta fidelidade (vertical slice)**: testa experiência completa de uma seção. Custo: semanas. Ideal para validar "isso está polido?"

O protótipo de papel do Spore que as notas mostram testava apenas as **regras de evolução** — sem gráficos, sem áudio, sem engine. A pergunta era só "a progressão é satisfatória?". Levou dias. O jogo final levou anos.

---

### Game Loop — O conceito que une tudo

Não apareceu nas notas mas é o fundamento técnico de qualquer jogo:

```
enquanto jogo_está_rodando:
    processar_input()
    atualizar_estado()
    renderizar()
```

O **game loop** roda dezenas a centenas de vezes por segundo. Todo sistema de jogo (física, IA, animação, audio) é chamado dentro dele. A frequência determina os FPS. As mecânicas são o que acontece em `atualizar_estado()`. As dinâmicas emergem de como os sistemas interagem nessa função.

**Fixed timestep vs. variable timestep**: física precisa de timestep fixo para ser determinística (mesmo input, mesmo resultado). Rendering usa timestep variável para maximizar FPS. Jogos modernos separam os dois.
