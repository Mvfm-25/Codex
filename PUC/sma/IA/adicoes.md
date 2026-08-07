# Simulação & Métodos Analíticos — Adições & Aprofundamentos
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas. Segue os tópicos na ordem em que apareceram nas notas, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---

## Módulo 01 — Avaliação de Sistemas, Filas e a Lei Que Amarra Tudo

### As Quatro Métricas de Desempenho São, na Verdade, Uma Só Equação

O material fecha o módulo listando vazão, população, utilização e tempo de resposta como quatro fatores soltos. Eles **não são independentes** — são as quatro variáveis da teoria de filas, e existe uma relação exata entre três delas:

| Métrica do material | Símbolo | Nome formal |
|---|---|---|
| **Vazão** — taxa de atendimento de pedidos | $\lambda$ | Taxa de chegada / *throughput* |
| **População** — atendimentos num dado instante | $L$ | Número médio de clientes no sistema |
| **Utilização** — fatia de tempo ocupado | $\rho$ | Utilização |
| **Tempo de resposta** — do pedido à conclusão | $W$ | Tempo médio no sistema |

A relação é a **Lei de Little** (John Little, 1961):

$$\boxed{L = \lambda W}$$

A força dela é a generalidade: vale para **qualquer** sistema em regime estacionário, independentemente da distribuição de chegadas, da disciplina de atendimento (FIFO, prioridade, LIFO), do número de servidores ou da forma da fila. Não exige hipótese nenhuma sobre o processo — só que o sistema seja estável e que se observe tempo suficiente.

A intuição é direta: se chegam 10 clientes por minuto e cada um passa 3 minutos no sistema, há em média 30 clientes lá dentro. E o uso prático é medir duas variáveis e **deduzir** a terceira — normalmente $W$, que é a mais difícil de instrumentar diretamente. É a ferramenta mais barata de toda a disciplina.

### Determinístico vs. Estocástico: o Que "Estocástico" Compra

A separação que o material faz entre métodos determinísticos e estocásticos parece taxonômica, mas a escolha decide se o modelo serve para alguma coisa.

Um modelo **determinístico** assume que tudo é conhecido: se um caixa atende exatamente 1 cliente por minuto e chega exatamente 1 cliente por minuto, **nunca se forma fila**. Esse é o problema — o modelo prevê fila zero, e a realidade tem fila.

A fila existe por causa da **variabilidade**. Clientes não chegam em intervalos regulares e atendimentos não duram todos o mesmo tempo; ocasionalmente três chegam juntos e um deles demora o triplo. Modelar isso com **variáveis aleatórias** e distribuições de probabilidade é o que torna a previsão utilizável.

A notação padrão para descrever uma fila é a de **Kendall**, $A/S/c$:

- $A$ — distribuição dos **intervalos entre chegadas**
- $S$ — distribuição do **tempo de serviço**
- $c$ — número de **servidores**

com $M$ = *Markoviano* (exponencial, sem memória), $D$ = determinístico, $G$ = geral. Assim `M/M/1` é chegada exponencial, serviço exponencial, um servidor — e é o modelo do INSS do material, com um guichê. `M/M/c` seria a mesma agência com $c$ guichês e fila única.

Para a `M/M/1`, com taxa de chegada $\lambda$ e taxa de serviço $\mu$:

$$\rho = \frac{\lambda}{\mu}, \qquad L = \frac{\rho}{1-\rho}, \qquad W = \frac{1}{\mu - \lambda}$$

E é fácil conferir que a Lei de Little fecha: $\lambda W = \dfrac{\lambda}{\mu-\lambda} = \dfrac{\rho}{1-\rho} = L$.

### Por Que a Fila do INSS é Imortal — o $1/(1-\rho)$

A piada do material tem explicação matemática exata, e ela é o resultado mais útil do módulo. O tempo de espera não cresce proporcionalmente à carga: ele cresce com $\dfrac{1}{1-\rho}$, que **explode** quando $\rho \to 1$.

| Utilização $\rho$ | $L = \rho/(1-\rho)$ | Espera relativa |
|---|---|---|
| 50% | 1,0 | 1× (referência) |
| 80% | 4,0 | 4× |
| 90% | 9,0 | 9× |
| 95% | 19,0 | **19×** |
| 99% | 99,0 | **99×** |

Sair de 90% para 95% de utilização — cinco pontos percentuais, uma mudança que parece marginal em qualquer planilha — **mais que dobra** a fila. É por isso que serviços dimensionados "para usar toda a capacidade" ficam insuportáveis: o ponto de operação está do lado errado da curva, onde qualquer flutuação de demanda vira espera enorme. E quando $\lambda \ge \mu$ o sistema é **instável**: a fila cresce sem limite e nenhuma fórmula de regime estacionário se aplica. Literalmente imortal.

A consequência de engenharia é direta e vale para muito além de agências públicas: **capacidade ociosa não é desperdício, é o que compra tempo de resposta**. Datacenters operam CPUs bem abaixo do pico pela mesma razão, e é o mesmo fenômeno que faz um disco a 95% de utilização destruir a latência de um banco de dados.

### As Três Técnicas: Quando Cada Uma Vale a Pena

O material apresenta monitoração, simulação e métodos analíticos em sequência. O critério de escolha fica mais claro numa comparação direta:

| | **Monitoração** | **Simulação** | **Métodos Analíticos** |
|---|---|---|---|
| Exige o sistema existindo? | **Sim** | Não | Não |
| Fidelidade | Máxima | Média — depende do modelo | Menor — só o que a matemática captura |
| Custo de execução | Alto (hardware, tempo real) | Médio (CPU, mas escala) | Baixo (fórmula fechada) |
| Explora cenários hipotéticos? | Não | **Sim** | Sim, mas limitado |
| Resultado | Números reais, com ruído | Estimativa com **intervalo de confiança** | Valor exato **do modelo** |

A ironia registrada no material — a "desvantagem" da monitoração ser exigir que o sistema exista — é o ponto central da disciplina, não um detalhe. Decisões de dimensionamento são tomadas **antes** de construir; se a única técnica disponível exigisse o sistema pronto, não haveria como projetar nada. Modelagem é o que permite responder "o que acontece se dobrarmos a demanda?" sem dobrar a demanda.

E a observação final do material — que às vezes a resolução analítica fica mais cara que simular — tem nome: **explosão do espaço de estados**. Uma cadeia de Markov com $n$ componentes de $k$ estados cada tem $k^n$ estados, e resolver o sistema linear estacionário custa $O((k^n)^3)$ por eliminação direta. Com 20 componentes binários já são mais de um milhão de estados. As saídas são exatamente as duas que o texto menciona:

- **Soluções em forma de produto**, quando a estrutura permite. O **teorema de Jackson** (redes abertas) e o **teorema BCMP** garantem que, sob certas condições, a distribuição conjunta da rede é o **produto** das distribuições de cada fila isolada. A complexidade despenca: em vez de resolver $k^n$ estados, resolve-se $n$ filas separadamente. É o resultado que torna a análise de redes de filas viável.
- **Simulação de Monte Carlo**, quando nem isso vale. Aceita-se uma resposta com barra de erro em troca de conseguir uma resposta.

O comentário do material de que os números "devem ser interpretados, não apenas calculados" ganha peso aqui: uma simulação entrega um **intervalo de confiança**, não um valor. Reportar "tempo médio de resposta = 4,7 s" sem dizer que o intervalo de 95% é $[2{,}1;\ 9{,}3]$ é apresentar precisão que o método não tem. É o erro mais comum de quem simula pela primeira vez.

---

### Referências para ir além

- **Raj Jain, *The Art of Computer Systems Performance Analysis* (1991)** — a referência canônica da disciplina; cobre monitoração, simulação e teoria de filas com foco em sistemas computacionais, e tem um capítulo inteiro sobre erros comuns de análise.
- **Little & Graves, *Little's Law* (2008)** — capítulo que revisita a lei, suas hipóteses reais e os usos indevidos mais frequentes.
- **Mor Harchol-Balter, *Performance Modeling and Design of Computer Systems* (Cambridge, 2013)** — teoria de filas escrita para computação, com a melhor explicação do efeito $1/(1-\rho)$ e das redes em forma de produto.
- **Bolch, Greiner, de Meer & Trivedi, *Queueing Networks and Markov Chains*** — o tratamento formal de cadeias de Markov, teorema BCMP e a explosão do espaço de estados.
- **Averill Law, *Simulation Modeling and Analysis*** — a referência de simulação: geração de variáveis aleatórias, validação de modelo e análise estatística da saída (intervalos de confiança, período de aquecimento).
- **Gunther, *Guerrilla Capacity Planning*** — a versão pragmática, sobre aplicar essas fórmulas a sistemas reais com dados incompletos.
