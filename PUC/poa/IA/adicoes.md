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
