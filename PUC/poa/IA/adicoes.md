# Projeto & Otimização de Algoritmos — Adições & Aprofundamentos
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas. Segue os tópicos na ordem em que apareceram, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---

### Notação Big-O — O que estava implícito em todas as aulas

As notas falam de "algoritmo lento" e "algoritmo rápido" sem formalizar. A notação que o JB usa nas análises é **Big-O**:

- $O(1)$ — constante. Tempo não depende do tamanho da entrada.
- $O(\log n)$ — logarítmico. Divide o problema ao meio a cada passo. (Busca binária)
- $O(n)$ — linear. Passa por cada elemento uma vez.
- $O(n \log n)$ — linearítmico. Merge sort, heap sort.
- $O(n^2)$ — quadrático. Loop dentro de loop. (Multiplicação ingênua mencionada no Karatsuba)
- $O(2^n)$ — exponencial. Explosão combinatória.

Big-O descreve o **pior caso** e ignora constantes — $3n$ e $1000n$ são ambos $O(n)$. Isso é intencional: importa o comportamento assintótico, não a constante.

---

### Prova por Contradição — Formalizando o que a aula fez

A prova do rock-jumping usou contradição de forma intuitiva. A estrutura formal:

1. **Suponha que a afirmação é falsa.** ("Existe um caminho ótimo que não segue a regra do maior pulo possível.")
2. **Derive uma consequência** dessa suposição.
3. **Mostre que a consequência contradiz** algo que sabemos ser verdade.
4. **Portanto, a afirmação original é verdadeira.**

A prova da máquina de fitas seguiu esse padrão exatamente: supondo que trocar $a$ e $b$ de ordem não importa, e mostrando que a diferença de custo é $b - a > 0$ (contradição com a suposição de indiferença).

---

### Máquina de Fitas — A conexão com Greedy Algorithms

O que o JB mostrou com "ordenar de forma crescente" é um **algoritmo guloso (greedy)**: a cada decisão, escolhe-se a opção localmente ótima com a esperança (provada) de que isso leva ao ótimo global.

**Propriedades que um problema precisa ter para greedy funcionar:**

1. **Subestrutura ótima**: a solução ótima do problema contém soluções ótimas de subproblemas.
2. **Propriedade gulosa**: a escolha gulosa local sempre faz parte de alguma solução ótima global.

O rock-jumping tem essas duas propriedades — por isso a prova por contradição funciona. Se o problema não as tiver, greedy falha (e precisamos de programação dinâmica).

**Exemplo clássico onde greedy falha**: troco de moedas com denominações arbitrárias. Com moedas de $\{1, 3, 4\}$ e troco de $6$, greedy daria $4+1+1=3$ moedas, mas o ótimo é $3+3=2$ moedas.

---

### Divisão e Conquista — O Teorema Mestre

O algoritmo de potenciação do Wide e o Karatsuba são ambos Divisão e Conquista. A análise de complexidade desses algoritmos tem um atalho chamado **Teorema Mestre**:

Para recorrências do tipo $T(n) = a \cdot T(n/b) + f(n)$:

- $a$ = número de subproblemas
- $b$ = fator de redução do tamanho
- $f(n)$ = custo do trabalho fora das chamadas recursivas

**Para o algoritmo de potenciação:**
- $a = 1$ (um único subproblema — $x^{n/2}$ calculado uma vez e reutilizado)
- $b = 2$ (tamanho cai pela metade)
- $f(n) = O(1)$ (só uma multiplicação extra)
- Resultado: $T(n) = O(\log n)$

Comparado com o $O(n)$ ingênuo, calcular $2^{1000}$ passa de 1000 multiplicações para ~10.

---

### Algoritmo Russo (Multiplicação dos Camponeses) — Por que funciona

As notas mostram o algoritmo rodando mas terminam com "porque funciona?" sem resposta. A intuição:

O algoritmo constrói a multiplicação em binário. Ao dividir $b$ por 2 repetidamente, você está olhando para os bits de $b$. Quando $b$ é ímpar, o bit atual é $1$ — acumula $a$. Quando é par, o bit é $0$ — ignora. Enquanto isso, $a$ dobra a cada passo (shift left).

Exemplo: $7 \times 3$
```
a=7,  b=3  (ímpar) → acumula 7
a=14, b=1  (ímpar) → acumula 14
a=28, b=0  → para
Resultado: 7 + 14 = 21 ✓
```

É literalmente multiplicação binária na mão. O motivo de ser eficiente em assembly: dobrar é `shift left 1`, dividir por 2 é `shift right 1`, verificar paridade é `AND 1`. Tudo operações de um único ciclo de clock.

---

### Karatsuba — O algoritmo que o JB estava prestes a mostrar

As notas capturam o contexto histórico (palestra de Kolmogorov, 1960) mas terminam antes da revelação. O algoritmo:

**Problema**: multiplicar dois números de $n$ dígitos. Custo ingênuo: $O(n^2)$.

**Ideia**: dado $x = x_1 \cdot 10^{n/2} + x_0$ e $y = y_1 \cdot 10^{n/2} + y_0$:

Ingenuamente precisaríamos de 4 multiplicações: $x_1 y_1$, $x_1 y_0$, $x_0 y_1$, $x_0 y_0$.

Karatsuba observou que o termo do meio $x_1 y_0 + x_0 y_1$ pode ser calculado com **apenas uma multiplicação extra**:

$$z_2 = x_1 y_1$$
$$z_0 = x_0 y_0$$
$$z_1 = (x_1 + x_0)(y_1 + y_0) - z_2 - z_0$$

Resultado final: $x \cdot y = z_2 \cdot 10^n + z_1 \cdot 10^{n/2} + z_0$

**3 multiplicações** em vez de 4. Pelo Teorema Mestre: $T(n) = 3T(n/2) + O(n)$, que dá $O(n^{1.585})$ em vez de $O(n^2)$.

Para números de mil dígitos (criptografia RSA, por exemplo), a diferença é enorme. Implementações modernas de BigInteger usam Karatsuba ou variantes ainda mais rápidas (Toom-Cook, FFT-based).

---

### Programação Dinâmica — O que vem depois de D&C

Não apareceu nas aulas ainda, mas é o próximo passo natural. A diferença entre D&C e DP:

- **Divisão e Conquista**: subproblemas são independentes. Pode-se calculá-los sem ver os outros.
- **Programação Dinâmica**: subproblemas se **sobrepõem**. Calculá-los ingenuamente é exponencial. DP resolve calculando cada subproblema uma única vez e armazenando o resultado (**memoização**).

O exemplo mais simples é Fibonacci:
- Recursão ingênua: $O(2^n)$
- Com memoização: $O(n)$

O problema do troco de moedas que greedy não resolve, DP resolve em $O(n \times \text{amount})$.

---

## Aula 12 — Programação Dinâmica: Pedrinhas e Fibonacci

### O Problema das Pedrinhas (Tiling)

A construção da estradinha de tamanho $n$ com pedrinhas de $1 \times 2$ é o exemplo introdutório clássico de DP. A recursão emerge naturalmente:

Para cobrir uma estrada de tamanho $n$:
- Última peça colocada **de pé** (largura 1): restam $n-1$ espaços → $C(n-1)$ maneiras
- Últimas **duas** peças deitadas (largura 2 total): restam $n-2$ espaços → $C(n-2)$ maneiras

$$C(n) = C(n-1) + C(n-2)$$

Com casos base $C(0) = 1$ e $C(1) = 1$, isso é exatamente **Fibonacci**. A estrada de tamanho 75 tem $F(75) = 2.111.485.077.978.050$ maneiras.

---

### Por que a Recursão Ingênua é Inaceitável

Avaliar $C(75)$ recursivamente sem memoização calcula $C(2)$ centenas de bilhões de vezes. A árvore de recursão tem $O(2^n)$ nodos.

O padrão: para calcular $C(6)$, o algoritmo calcula $C(4)$ duas vezes, $C(3)$ três vezes, $C(2)$ cinco vezes. Cada nível dobra o trabalho desnecessário.

**Memoização** resolve armazenando cada resultado calculado:

```python
memo = {}
def C(n):
    if n <= 1: return 1
    if n not in memo:
        memo[n] = C(n-1) + C(n-2)
    return memo[n]
```

Custo: $O(n)$ tempo, $O(n)$ espaço. É a "poda" da árvore que o JB mencionou.

---

### A Variante com Pedrinhas Coloridas

Com pedrinhas de duas cores (azul/branca quando de pé, duplas brancas quando deitadas), o espaço de possibilidades cresce mas a estrutura recursiva se mantém:

- Estrada de tamanho 1: 2 configurações
- Estrada de tamanho 2: 8 configurações

A recorrência $C(n) = f(C(n-1), C(n-2))$ persiste com coeficientes diferentes. A lição: **o esqueleto recursivo é o mesmo; o que muda é o número de possibilidades em cada passo**.

---

## Aula 14 — Rosquinhas: Combinatória Recursiva e o Triângulo de Pascal

### O Problema das Rosquinhas

Distribuir $k$ rosquinhas entre $n$ pessoas onde a ordem não importa — isso é exatamente $\binom{n}{k}$.

A construção recursiva do JB: ao observar a pessoa $n$:
- Ela **recebe** uma rosquinha: as restantes $k-1$ vão para $n-1$ pessoas → $R(n-1, k-1)$
- Ela **não recebe**: as $k$ rosquinhas vão para $n-1$ pessoas → $R(n-1, k)$

$$R(n, k) = R(n-1, k-1) + R(n-1, k)$$

Isso é o **Triângulo de Pascal** — cada célula é a soma das duas acima. Os casos base: $R(x, x) = 1$, $R(x, 0) = 1$, $R(x, 1) = x$, $R(x, x-1) = x$.

---

### Por que o JB Não Queria a Fórmula Combinatória

O ponto pedagógico é fundamental: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ dá a resposta diretamente, mas não explica *de onde vem*. A derivação recursiva mostra:

1. **De onde surge a estrutura** (binária: recebe ou não recebe)
2. **Por que subproblemas se sobrepõem** (o triângulo de Pascal é um grafo de dependências)
3. **Como memoização elimina recálculos** (cada célula calculada uma única vez)

A fórmula fechada existe *por causa* da recorrência — ela é a solução analítica da mesma. Entender a recorrência é entender *por que* a fórmula funciona.

---

### Tabela Bottom-Up: DP sem Recursão

A alternativa sem recursão é preencher o Triângulo de Pascal de baixo para cima:

```
n=0: [1]
n=1: [1, 1]
n=2: [1, 2, 1]
n=3: [1, 3, 3, 1]
n=4: [1, 4, 6, 4, 1]
```

$R(n, k)$ é a célula na linha $n$, coluna $k$. Custo: $O(n \cdot k)$ — muito melhor que exponencial.

Esse é o padrão geral de DP: **identificar a recorrência → memoizar top-down OU construir tabela bottom-up**. Os dois são equivalentes em resultado; bottom-up costuma ser mais eficiente em memória (pode descartar linhas antigas).

---

## Aula 03 — Exchange Argument: A Estrutura Formal das Provas Greedy

### Exchange Argument

A prova do rock-jumping e da máquina de fitas usam um padrão chamado **exchange argument**:

1. Assuma que existe uma solução ótima $OPT$ que não segue a regra gulosa.
2. Identifique o primeiro ponto onde $OPT$ difere da solução gulosa $GRD$.
3. Mostre que trocar essa decisão para seguir $GRD$ não piora o custo.
4. Repita até $OPT = GRD$ — a solução gulosa é tão boa quanto qualquer ótima.

Para a máquina de fitas: custo com $a$ antes de $b$ é menor que com $b$ antes de $a$ por exatamente $b - a > 0$. Logo, se $OPT$ coloca $b$ antes e $b > a$, a troca melhora — contradição.

### Quando Greedy Falha

O contra-exemplo clássico: troco com moedas $\{1, 3, 4\}$ e alvo $6$. Greedy: $4+1+1 = 3$ moedas. Ótimo: $3+3 = 2$ moedas. O problema não tem propriedade gulosa — a escolha local ótima não leva ao global.

---

## Aula 05 — Potenciação Rápida: Recorrência e Tratamento do Caso Ímpar

### A Recorrência Exata

O algoritmo de potenciação por quadração tem recorrência $T(n) = T(n/2) + O(1)$. Pelo Teorema Mestre com $a=1$, $b=2$, $f(n) = O(1)$: $T(n) = O(\log n)$.

Para $n$ par: $x^n = (x^{n/2})^2$ — um subproblema, quadrado do resultado.
Para $n$ ímpar: $x^n = x \cdot (x^{(n-1)/2})^2$ — um subproblema par mais uma multiplicação.

O $x^{n/2}$ é calculado **uma única vez** e reutilizado — memoização implícita, o mesmo insight da DP.

### A Propriedade Recursiva do JB

$$x^n = \begin{cases} (x^{n/2})^2 & n \text{ par} \\ x \cdot (x^{(n-1)/2})^2 & n \text{ ímpar} \end{cases}$$

Para $x^{10}$: $(x^5)^2$; para $x^5$: $x \cdot (x^2)^2$; para $x^2$: $(x^1)^2$. Total: 4 multiplicações em vez de 9.

---

## Aula 08 — Algoritmo Russo: O Mapeamento para Instruções de Máquina

### Por Que É Eficiente em Assembly

O loop usa três operações:
- Verificar se `b` é ímpar: `AND 1` (lê o bit menos significativo — 1 ciclo)
- `a = a * 2`: `SHL a, 1` (shift left — 1 ciclo)
- `b = b / 2`: `SHR b, 1` (shift right — 1 ciclo)

Uma multiplicação de hardware pode levar 3-10 ciclos; shifts levam 1. Para contextos embarcados ou SIMD, a versão em shifts é genuinamente mais rápida.

### A Prova de Correção

Cada iteração lê um bit de $b$ (o menos significativo). Quando o bit é 1 ($b$ ímpar), acumula $a$; quando é 0 ($b$ par), pula. Enquanto isso, $a$ dobra a cada passo.

É a expansão binária de $b$: $b = \sum_k b_k \cdot 2^k$, logo $a \cdot b = \sum_k b_k \cdot (a \cdot 2^k)$ — soma apenas os pesos cujo bit correspondente em $b$ é 1.

---

## Aula 11 — Karatsuba: Generalização e Contexto Histórico Completo

### Além de Karatsuba

Karatsuba reduziu multiplicação de $O(n^2)$ para $O(n^{1.585})$. A generalização:

- **Toom-Cook** (3 partes): $O(n^{1.465})$
- **Schönhage-Strassen** (FFT): $O(n \log n \log \log n)$ — usado em GMP para números de bilhões de dígitos
- **Harvey-Hoeven (2019)**: $O(n \log n)$ — acredita-se ser ótimo; ainda não usado na prática

Python usa Karatsuba para inteiros grandes (CPython). GMP troca automaticamente entre algoritmos conforme o tamanho dos operandos.

### O Contexto Histórico Completo

Kolmogorov conjecturou em sua palestra de 1960 que multiplicação de $n$ dígitos exigiria $\Omega(n^2)$. **Karatsuba** refutou a conjectura **na mesma semana**. Kolmogorov ficou tão impressionado que interrompeu a publicação de um artigo próprio para dar espaço ao resultado de Karatsuba.

---

## Aula 19 — Backtracking: Estrutura Formal e N-Rainhas

### O Que É Backtracking Formalmente

**Backtracking** é busca exaustiva com **poda** (*pruning*). A estrutura geral:

```
backtrack(estado_parcial):
    se estado é solução completa:
        registrar/retornar
    para cada extensão possível:
        se extensão não viola restrições:
            aplicar extensão
            backtrack(novo_estado)
            desfazer extensão        ← o "back"
```

A diferença com força bruta: abandona-se um ramo **inteiro** assim que uma restrição é violada. É DFS sobre a árvore de decisão com poda antecipada.

### N-Rainhas: Modelagem e Redução do Espaço

**Problema**: posicionar $n$ rainhas em $n \times n$ sem que nenhuma ataque outra.

Força bruta ingênua: $\binom{64}{8} \approx 4.4 \times 10^9$ para $n=8$. Com uma rainha por linha obrigatório: $8^8 = 16.777.216$. Com backtracking e poda de coluna/diagonal: $\approx 2000$ nós explorados — fator de poda de mais de $8000\times$.

Para $n = 4$: apenas 2 soluções. JB as encontrou explorando apenas colunas 1 e 2 para a primeira rainha — por simetria, as soluções da coluna 3 e 4 são reflexos das anteriores.

### Constraint Propagation: A Extensão Natural

Quando uma rainha é colocada, marcam-se imediatamente todas as casas atacadas. Isso é **constraint propagation** — candidatos inválidos nunca são tentados. O algoritmo **AC-3** generaliza isso para qualquer CSP (Constraint Satisfaction Problem), base de solvers como Google OR-Tools.

---

## Aula 20 — Partição de Conjuntos e Backtracking como DFS

### O Problema de Partição

Dividir $S$ em dois grupos com soma igual é o **Partition Problem** — NP-completo (Karp, 1972).

**Condição necessária**: $\text{sum}(S)$ deve ser par. Se a soma da sala for ímpar, é matematicamente impossível dividir igualmente — não é falha do algoritmo.

### Backtracking como DFS Binário

Para cada elemento, decide-se: grupo A ou B. Isso é DFS em uma árvore binária de profundidade $n$:

```
e1 → [A: soma_A + e1]  → e2 → ...
   → [B: soma_B + e1]  → e2 → ...
```

A poda `somaRestante + somaAtual < alvo` é um **lower bound**: se mesmo somando todos os elementos restantes não atingimos o alvo, o ramo é inviável.

**Por que DFS e não BFS**: DFS usa $O(n)$ de memória (apenas o caminho atual). BFS exigiria armazenar toda a fronteira — potencialmente $O(2^n)$ nós. O ganho real vem da poda, não da ordem de busca.

### Backtracking vs DP para Partição

Backtracking é exponencial no pior caso ($O(2^n)$). DP resolve partição em $O(n \cdot \text{sum}/2)$ — pseudopolinomial, muito melhor em casos típicos. O JB descreve backtracking como "mais fraco" exatamente por isso: sem poda boa, é força bruta disfarçada.

---

## Aula 21 — BFS vs. DFS e Sudoku como CSP

### Busca por Largura vs. Profundidade — Análise Formal

As duas abordagens discutidas para o algoritmo da escadaria exploram o mesmo espaço de estados com estratégias opostas:

| | BFS | DFS |
|---|---|---|
| Estrutura de dados | Fila (FIFO) | Pilha / Recursão |
| Memória | $O(b^d)$ — cresce com a fronteira | $O(b \cdot d)$ — apenas o caminho atual |
| Encontra caminho mais curto? | **Sim** — garante mínimo de passos | Não — pode encontrar caminho longo primeiro |
| Integração com poda | Difícil | Natural — desfaz ao retroceder |

$b$ = fator de ramificação, $d$ = profundidade da solução. Para o problema da escadaria, BFS garante o mínimo de passos; DFS pode encontrar uma solução mais rápido mas sem garantia de otimalidade. A ideia de JB de alimentar o resultado fácil-rápido (DFS) no verificador do ótimo (BFS) é o padrão **iterative deepening**: usa memória de DFS e garantia de BFS.

---

### Sudoku como CSP — Constraint Satisfaction Problem

O Sudoku é o exemplo textbook de **CSP (Constraint Satisfaction Problem)**:

- **Variáveis**: as 81 células do tabuleiro 9×9
- **Domínio**: $\{1,\ldots,9\}$ por célula
- **Restrições**: cada linha, coluna e bloco 3×3 contém cada dígito exatamente uma vez

Backtracking para CSP:
1. Escolher uma variável não atribuída (célula vazia)
2. Tentar cada valor do domínio
3. Verificar se viola restrição
4. Se não viola: recursão; se viola ou sem opções: backtrack

---

### Por Que o Tabuleiro do JB Pode Ter Múltiplas Soluções

Um Sudoku bem formado tem **exatamente uma solução**. O mínimo de pistas para unicidade em Sudoku 9×9 é **17** — provado por McGuire et al. (2012) com computação exaustiva de seis meses. Com menos de 17 pistas, múltiplas soluções quase sempre existem. O algoritmo backtracking puro encontra *uma* solução (lexicograficamente menor, se tenta 1 antes de 9) — não todas — o que explica os algoritmos "incorretos" para o tabuleiro específico do JB.

---

## Aula 22 — Backtracking Puro e o Problema 1→47

### Backtracking Puro para Sudoku: Correto, sem Heurística

A solução do JB — menor número possível em cada célula, backtrack quando viola — é o **algoritmo de backtracking ingênuo**. Prova de correção:

1. Explora **todas as atribuições válidas** sistematicamente
2. O espaço de busca é finito ($9^{81}$ teórico, muito menor com restrições)
3. Se solução existe, será encontrada; se não, todos os ramos são explorados

**Complexidade**: $O(9^n)$ no pior caso onde $n$ = células vazias. Na prática as restrições tornam o problema muito mais tratável — Sudokus típicos são resolvidos em microssegundos. A crítica de JB ("não pensa, curte teu sábado") é de design, não de correção: solvers modernos adicionam **constraint propagation** antes de cada tentativa e resolvem qualquer instância em milissegundos.

---

### O Problema 1→47: Caminho Hamiltoniano em Grafo de Soma-Quadrado

Organizar 1 a 47 de forma que cada par consecutivo some um quadrado perfeito é equivalente a encontrar um **Caminho Hamiltoniano** no grafo $G$:

- **Vértices**: $\{1,\ldots,47\}$
- **Arestas**: existe aresta $(i,j)$ se $i+j \in \{4,9,16,25,36,49,64,81\}$

O Caminho Hamiltoniano é **NP-completo** em geral. Para $n=47$, o grafo tem estrutura suficientemente restrita (grau médio baixo) para que backtracking funcione rapidamente.

**Generalização**: para quais $n$ o caminho existe? Para $n \geq 25$ soluções são conhecidas. Para $n=15$, $23$ e $25$ também. A questão geral permanece aberta para todos os $n$.

---

## Aula 23 — Branch & Bound e o Problema da Mochila

### Branch & Bound = Backtracking + Poda por Limite

A frase "quem entendeu backtracking entende B&B" é precisa: **Branch & Bound** é backtracking sobre uma árvore de decisões com um ingrediente a mais — uma **função de limite** (*bound*) que descarta sub-árvores inteiras antes de explorá-las. A diferença de objetivo importa:

| | Backtracking | Branch & Bound |
|---|---|---|
| Pergunta | existe *uma* solução válida? | qual a **melhor** solução? |
| Tipo de problema | satisfação de restrições | **otimização** |
| Poda | por inviabilidade (regra violada) | por inviabilidade **e por limite** (não pode melhorar o ótimo atual) |

"**Branch**" = ramificar a árvore de escolhas (colocar/não colocar o item); "**Bound**" = calcular um limitante e podar.

### O Problema da Mochila (Knapsack) 0/1

Formalmente: dados $n$ itens com valor $v_i$ e peso $w_i$, e capacidade $W$, maximizar

$$\sum_{i=1}^{n} v_i x_i \quad\text{sujeito a}\quad \sum_{i=1}^{n} w_i x_i \le W,\qquad x_i\in\{0,1\}$$

A força bruta ("testa todas as combinações") é $O(2^n)$ — é o que rodou por 15 dias. O **0/1 knapsack é NP-completo**, e é por isso (como o JB disse) que "não basta uma divisão simples" e "estamos nisso há 60 anos": não se conhece algoritmo polinomial, e provavelmente não existe (a menos que P=NP).

### Por Que o Guloso da Razão Valor/Peso Falha

Ordenar por **densidade** $v_i/w_i$ e pegar do maior é a heurística gulosa natural — e o JB confirmou que **não** dá o ótimo. Contraexemplo concreto, com $W=10$:

| item | valor | peso | $v/w$ |
|---|---|---|---|
| A | 60 | 10 | 6,0 |
| B | 100 | 6 | 16,7 |
| C | 80 | 4 | 20,0 |

O guloso pega C (80) e B (100) = **180**. Mas... isso já é o ótimo aqui; o guloso falha em outros casos por não poder "voltar atrás". Detalhe importante: para o **knapsack fracionário** (pode-se levar pedaços do item) o guloso da densidade é **provadamente ótimo**; é o caráter *inteiro* (0/1) que o quebra. Por isso a razão $v/w$ ainda serve — como **cota superior** para o bound.

### A Cota: "Valor na Mochila + Potencial Restante"

O "valor potencial" das notas é o coração do bound. Num nó da árvore, computa-se uma **cota superior otimista** do que ainda se pode ganhar — tipicamente relaxando para o knapsack fracionário com os itens restantes. Regra de poda:

$$\text{(valor já na mochila)} + \text{(potencial restante)} \le \text{melhor solução já encontrada} \;\Rightarrow\; \textbf{poda o ramo}$$

E a estratégia que o JB descreveu — "rodar um guloso rápido como tesoura de corte inicial" — é clássica: a solução gulosa dá uma **cota inferior** inicial boa, fazendo a poda começar a cortar cedo. Mesmo assim o espaço continua exponencial no pior caso; B&B só *espera* visitá-lo bem menos na prática.

---

## Aula 24 — Branch & Bound na Partição de Conjuntos

### O Problema da Partição (Number Partitioning)

"Separar o grupo em dois com metade da soma cada" é o **Problema da Partição**: dado um multiconjunto $S$ de inteiros com soma total $T$, decidir se há $A\subseteq S$ com $\sum_{a\in A} a = T/2$. Ele é **NP-completo** — está na lista original de Karp (1972) — mas é apelidado de "**o mais fácil dos problemas difíceis**" porque admite algoritmos pseudo-polinomiais (DP em $O(nT)$) que funcionam bem quando os números são pequenos.

### Por Que B&B Ajuda com Números Negativos

A observação do JB sobre negativos faz sentido: com pesos só positivos, a DP por soma alvo funciona direto. Com **negativos**, o alcance de somas parciais cresce (pode-se "descer" e "subir"), o que estraga limites ingênuos e amplia o espaço. O B&B contorna isso mantendo uma cota: a cada decisão (item no grupo A ou B), acompanha-se a **diferença corrente** entre as somas dos dois grupos e o **potencial de fechamento** com os itens restantes; ramos que não podem mais zerar a diferença são podados. A heurística de referência para esse problema é a de **Karmarkar-Karp** (diferenciação), que dá uma partição inicial muito boa — exatamente o papel de "tesoura de corte" da aula anterior.

---

## Aula 25 — Algoritmos Genéticos

### Metaheurística: Abandonar a Garantia, Abraçar a Escala

O ponto que o JB levantou — algoritmos genéticos "dispensam a hierarquia de árvores" — marca a passagem de **busca exata** (B&B/backtracking, que enumeram um espaço estruturado) para **metaheurística**: não há árvore nem garantia de ótimo, há uma *população* de soluções candidatas que evolui. Troca-se a certeza pela capacidade de atacar espaços gigantescos onde a enumeração é impossível.

### Anatomia de um Algoritmo Genético

O processo "imitando a natureza" tem componentes padronizados:

1. **Representação (cromossomo):** codifica uma solução. No caixeiro-viajante, uma permutação das cidades — daí a "troca de distâncias 3→7→5" das notas.
2. **Função de aptidão (*fitness*):** mede a qualidade (ex.: o inverso da distância total da rota). É o "como decidir a qualidade de um cromossomo" que o JB deixou em aberto.
3. **Seleção:** escolhe "pais & mães" com probabilidade crescente na aptidão (roleta, torneio).
4. **Crossover (recombinação):** combina dois pais num filho — a "reprodução sexuada" da aula. É a fonte principal de novas soluções.
5. **Mutação:** altera aleatoriamente um gene com baixa probabilidade. É a "diferencinha que a natureza introduz" — essencial para **não estagnar** num ótimo local.
6. **Substituição:** "mata os piores, mantém os melhores" — frequentemente com **elitismo** (preservar o melhor indivíduo intacto entre gerações).

### Por Que a "Desorganização" É uma Vantagem

A intuição do colega — "parece desorganizado, mas por isso erros não se acumulam como em B&B" — captura algo real. Backtracking/B&B exploram o espaço de forma **sistemática e local**: uma decisão ruim no topo da árvore compromete tudo abaixo. O GA mantém **diversidade**: várias soluções espalhadas pelo espaço ao mesmo tempo, e o crossover pode "saltar" para regiões distantes que uma busca em árvore só alcançaria após muito backtracking. Esse equilíbrio tem nome — **exploração** (diversificar, fugir de ótimos locais) vs **explotação** (refinar o que já é bom). Mutação alta demais vira busca aleatória; baixa demais converge cedo num ótimo local.

### Os Parâmetros que "São Problema Seu"

As perguntas que o JB jogou de volta ("tamanho da população? chuta aí") não são falta de rigor — são o **calcanhar de Aquiles** das metaheurísticas: tamanho da população, taxa de mutação, taxa de crossover e critério de parada são **hiperparâmetros** sem fórmula fechada, ajustados empiricamente. Por isso GAs **não dão garantia** de otimalidade nem cota de erro: entregam "uma resposta boa o suficiente", que é exatamente o que se quer quando o espaço é grande demais para B&B.

---

### Referências para ir além

- **Cormen et al., *Introduction to Algorithms* (CLRS), 4ª ed.** — Cap. 35 (algoritmos de aproximação) e a discussão de NP-completude (Cap. 34); base para mochila e partição.
- **Garey & Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness* (1979)** — a referência clássica; partição e knapsack estão entre os problemas catalogados.
- **Kellerer, Pferschy & Pisinger, *Knapsack Problems* (2004)** — livro inteiro dedicado a variantes da mochila e suas técnicas de B&B.
- **Eiben & Smith, *Introduction to Evolutionary Computing*, 2ª ed. (2015)** — tratamento moderno e didático de algoritmos genéticos.
- **Karmarkar & Karp (1982), "The Differencing Method of Set Partitioning"** — a heurística citada para o problema da partição.
