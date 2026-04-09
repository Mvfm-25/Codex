# Métodos Numéricos — Adições & Aprofundamentos
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas. Segue os tópicos na ordem em que apareceram nas notas, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---

### IEEE 754 — O que ficou por baixo dos panos

As notas capturam bem o espírito do padrão. O que ficou implícito é **como os bits são literalmente organizados** em um float de 32 bits:

```
[ 1 bit: sinal ] [ 8 bits: expoente ] [ 23 bits: mantissa ]
```

- **Sinal** : 0 para positivo, 1 para negativo. Simples.
- **Expoente** : não é armazenado diretamente. Existe um **bias de 127**. Se o expoente real é `5`, armazenamos `5 + 127 = 132`. Isso evita ter que guardar sinal no expoente também.
- **Mantissa** : representa a parte fracionária do número. Como a notação científica binária sempre começa com `1.xxx`, esse `1` inicial é implícito e nem precisa ser armazenado — ganhando um bit de precisão de graça.

Ou seja, um número float 32-bits representa : $(-1)^{sinal} \times 1.mantissa \times 2^{expoente - 127}$

#### NaN e os casos especiais
- Expoente **todo 1s** + mantissa **diferente de zero** = **NaN** (Not a Number). Resultado de operações impossíveis como $0/0$ ou $\sqrt{-1}$ no mundo real.
- Expoente **todo 1s** + mantissa **zero** = **Infinito** (+ ou −, dependendo do sinal). É o overflow que as notas mencionam.
- Expoente **todo 0s** = **números subnormais** (denormalizados). São os números pequeníssimos próximos do zero onde o padrão "trai" a regra do `1` implícito para conseguir representar mais coisas perto do underflow.

#### Por que o bias?
Porque com o bias, comparar dois floats se torna comparação direta de inteiros — o hardware de ordenação funciona sem precisar entender ponto flutuante.

---

### Arredondamento — O que o modo "Em direção ao zero" significa na prática

As quatro modalidades das notas têm nomes mais formais:

| Modo | Nome técnico | O que faz |
|---|---|---|
| +infinito | *Round up* | Sempre arredonda para cima |
| -infinito | *Round down* | Sempre arredonda para baixo |
| Mais próximo | *Round to nearest, ties to even* | O padrão default do IEEE 754 |
| Zero | *Truncation* | Simplesmente corta os bits extras |

O modo **"ties to even"** (empate vai para o par) é o padrão porque minimiza o acúmulo de erros em longas sequências de operações — se sempre arredondasse para cima em empates, a soma de mil operações teria um viés sistemático.

---

### Intervalos Numéricos — Aritmética Intervalar

A história do Pi entre $[3.14159\,;\,3.141593]$ é a porta de entrada para um campo chamado **Aritmética Intervalar**. As operações básicas se estendem:

$$[a_1, a_2] + [b_1, b_2] = [a_1+b_1,\ a_2+b_2]$$
$$[a_1, a_2] \times [b_1, b_2] = [\min(\ldots),\ \max(\ldots)]$$

A multiplicação é mais complicada porque números negativos invertem a ordem. O conceito central é: **o resultado real sempre está contido no intervalo resultado**. Garante-se que não se perde nada, ao custo de os intervalos crescerem ao longo dos cálculos (fenômeno chamado *dependency problem* ou *wrapping effect*).

Linguagens e bibliotecas modernas como `boost::numeric::interval` (C++) e `IntervalArithmetic.jl` (Julia) implementam isso.

---

### Série de Taylor — A fórmula que estava por trás do gráfico

A ideia do "faux-polinômio" tem forma concreta:

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots$$

Ou de forma compacta: $f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$

- Quando $a = 0$, chama-se **Série de Maclaurin**.
- O gráfico da aula05 que imitava bem no $0$ é exatamente uma Série de Maclaurin sendo construída termo a termo.
- Quanto mais termos, melhor a aproximação — mas só dentro do **raio de convergência**. Longe do ponto de ancoragem, a série pode divergir completamente.

**Exemplos clássicos** que computadores usam internamente para calcular funções:
$$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$$
$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

---

### Galois e o Quinto Grau — Os outros nomes esquecidos

JB mencionou três ou quatro nomes. Os históricos são:

- **Niels Henrik Abel** (norueguês, não finlandês) — provou em 1824 a impossibilidade de fórmula geral para grau ≥ 5 usando radicais. Morreu de tuberculose aos 26 anos.
- **Évariste Galois** (francês) — desenvolveu a **Teoria de Galois**, que não só prova o resultado de Abel mas classifica *quais* equações específicas de alto grau são solúveis. Morreu no duelo aos 20 anos.
- **Paolo Ruffini** (italiano) — tentou a prova antes de Abel, chegou quase lá mas com lacunas. É o "Ruffini" do dispositivo de Briot-Ruffini.
- O quarto provavelmente foi **Carl Friedrich Gauss**, que provou o **Teorema Fundamental da Álgebra**: todo polinômio de grau $n$ tem exatamente $n$ raízes no campo dos complexos.

---

### Regra de Descartes — O que "desce de dois em dois" quer dizer

A regra completa : o número de raízes reais positivas é igual ao número de trocas de sinal nos coeficientes, **ou a esse número menos um múltiplo de dois**.

O motivo do "desce de dois em dois" é o **Teorema das Raízes Complexas Conjugadas**: se um polinômio tem coeficientes reais, raízes complexas aparecem **sempre em pares** $(a + bi)$ e $(a - bi)$. Então quando duas raízes reais "somem" ao se tornarem complexas, somem juntas — daí o salto de dois.

Para raízes negativas, aplica-se a regra ao polinômio $p(-x)$ — troca-se o sinal dos coeficientes de grau ímpar e conta-se trocas de sinal novamente.

---

### Bisecção — O Teorema que a justifica

O método de busca binária para raízes tem um nome formal : **Método da Bisecção**, e sua validade vem do **Teorema de Bolzano** (caso particular do Teorema do Valor Intermediário):

> Se $f$ é contínua em $[a, b]$ e $f(a) \cdot f(b) < 0$, então existe pelo menos um $c \in (a, b)$ tal que $f(c) = 0$.

A exigência de sinais opostos nas pontas — que as notas chamam de "dificuldade extra" — é exatamente a condição de Bolzano.

**Taxa de convergência** : a cada passo o intervalo cai pela metade. Para atingir precisão $\varepsilon$ partindo de um intervalo de tamanho $L$:
$$n \geq \log_2\!\left(\frac{L}{\varepsilon}\right) \text{ iterações}$$

É convergência **linear** (lenta) — o que JB chamou de "bem lento para matemática".

---

### Método de Horner — Por que funciona

O esquema de Horner não é só "escrever ao contrário" — é uma otimização real. Para avaliar $p(x) = a_n x^n + \cdots + a_1 x + a_0$:

- **Ingênuo**: $n$ multiplicações por $x^k$ (calculadas separado) + $n$ somas. Custo $O(n^2)$.
- **Horner**: reescreve como $(\cdots((a_n x + a_{n-1})x + a_{n-2})x \cdots )x + a_0$. Custo $O(n)$.

Para o polinômio das notas:
$$p(x) = 6x^8 - 4x^7 + 5x^5 + 4x^4 + 12x^3 - x + 10$$
$$= 10 + x(-1 + x(0 + x(12 + x(4 + x(5 + x(0 + x(-4 + 6x)))))))$$

Além de mais eficiente, é **numericamente mais estável** — menos operações significa menos acúmulo de erros de arredondamento IEEE 754.

---

### Método da Secante — Taxa de convergência

As notas descrevem bem o mecanismo. O que ficou faltando: o Método da Secante converge a uma taxa **superlinear**, com expoente $\approx 1{,}618$ — o número de ouro $\phi$. Isso não é coincidência; é resultado direto da recorrência do método.

Comparação com os outros métodos:

| Método | Convergência | Requisitos |
|---|---|---|
| Bisecção | Linear ($1{,}0$) | $f(a) \cdot f(b) < 0$ |
| Secante | Superlinear ($\approx 1{,}618$) | Dois pontos iniciais quaisquer |
| Newton | Quadrática ($2{,}0$) | Um ponto + derivada disponível |

A razão pela qual Newton é quadrático: se o erro atual é $e_k$, o próximo erro é proporcional a $e_k^2$. Isso significa que o número de casas decimais corretas **dobra** a cada iteração.

---

### Método de Newton — Quando ele falha

JB mencionou que "costuma sair passeando". Os casos concretos de falha:

1. **Derivada zero no ponto**: $f'(x_1) = 0$ causa divisão por zero na fórmula $x_2 = x_1 - f(x_1)/f'(x_1)$.
2. **Ciclo infinito**: É possível que Newton oscile entre dois pontos sem nunca convergir.
3. **Ponto de inflexão entre o ponto atual e a raíz**: O método pode "pular" para uma região errada.
4. **Raíz múltipla**: Convergência cai para linear (perde a vantagem quadrática).

A condição suficiente para convergência (Teorema de Newton-Kantorovich) envolve que $f$, $f'$ e $f''$ sejam bem comportadas na região — é o que garante que o método "não saia passeando".

---

### Fractal de Newton — Por que é um fractal

A bacia de atração de cada raíz (os "coloridinhos" do gráfico de JB) forma uma fractal porque a fronteira entre regiões tem **dimensão de Hausdorff maior que 1** — ela é infinitamente detalhada em qualquer escala.

Matematicamente, a fronteira entre bacias é um **conjunto de Julia**, e o fenômeno de sensibilidade extrema às condições iniciais nas bordas é **caos determinístico**. A mínima diferença no ponto de partida pode levar a raízes completamente diferentes — o que as notas capturam perfeitamente.

---

### Método de Aberth (Aberth-Ehrlich) — O mecanismo real

A analogia das cargas elétricas de JB é uma boa intuição. A fórmula real do passo de atualização para o $k$-ésimo Newton:

$$w_k \leftarrow w_k - \frac{f(w_k)/f'(w_k)}{1 - \frac{f(w_k)}{f'(w_k)} \sum_{j \neq k} \frac{1}{w_k - w_j}}$$

O somatório $\sum_{j \neq k} \frac{1}{w_k - w_j}$ é exatamente o **termo de repulsão** — quanto mais próximo outro Newton estiver, maior o denominador, menor o passo. É a "carga elétrica" formalmente.

**Por que funciona de um em um?** A atualização simultânea de todos os $n$ Newtons ao mesmo tempo pode criar instabilidades. O método sequencial (Gauss-Seidel para raízes) usa imediatamente cada posição atualizada no cálculo do próximo — converge mais rápido e com mais estabilidade.

---

### Referências para ir além

- **IEEE 754-2008** — o padrão em si (acessível no site da IEEE).
- **"Numerical Analysis" — Burden & Faires** — o livro clássico que cobre bisecção, Newton e secante com rigor matemático acessível.
- **"Accuracy and Stability of Numerical Algorithms" — Higham** — para entender erros de ponto flutuante a fundo.
- **Wolfram Alpha** — útil para verificar cálculos de cotas e raízes na mão.
- [Visualizador de IEEE 754](https://www.h-schmidt.net/FloatConverter/IEEE754.html) — mostra os bits reais de qualquer float.
- [Fractal de Newton interativo](https://www.chiark.greenend.org.uk/~sgtatham/newton/) — para brincar com os "coloridinhos" do JB.
