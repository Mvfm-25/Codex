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

---

## Aula 06 — Cotas de Lagrange, Cauchy e Fujiwara

### O que são Cotas (Bounds)

Antes de procurar raízes, é útil saber *onde procurar*. As cotas determinam um valor $M$ tal que todas as raízes reais do polinômio estão no intervalo $[-M, M]$. Usam apenas os coeficientes do próprio polinômio.

Para $p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_0$:

---

### Cota de Lagrange

$$M = \max\!\left\{1,\ \sum_{i=0}^{n-1} \left|\frac{a_i}{a_n}\right|\right\}$$

Soma os módulos de todos os coeficientes divididos pelo coeficiente líder, e toma o máximo com 1.

Para $p(x) = 6x^8 - 4x^7 + 5x^5 + 4x^4 + 12x^3 - x + 10$:
$$M = \frac{4 + 0 + 5 + 4 + 12 + 0 + 1 + 10}{6} = \frac{36}{6} = 6$$

Todas as raízes estão em $[-6, 6]$.

---

### Cota de Cauchy

$$M = 1 + \max_{0 \le i < n}\!\left|\frac{a_i}{a_n}\right|$$

Em vez de somar, toma o **máximo** dos coeficientes normalizados e adiciona 1.

Para o mesmo polinômio: $\max = |12/6| = 2$, logo $M = 1 + 2 = 3$.

**Cauchy costuma ser mais apertada que Lagrange** (no exemplo: $3 < 6$). Não é garantido para todo polinômio — depende da distribuição dos coeficientes.

---

### Cota de Fujiwara

Mais refinada ainda: cada coeficiente recebe um expoente diferente conforme sua posição.

$$M = 2 \cdot \max_{1 \le i \le n}\!\left|\frac{a_{n-i}}{a_n}\right|^{1/i}$$

No exemplo do JB, Fujiwara retornou $\approx 2{,}29$ — menor que Cauchy ($3$) e muito menor que Lagrange ($6$). A precisão adicional vem de levar em conta a *posição* de cada coeficiente: coeficientes de grau maior influenciam mais onde as raízes podem estar.

No mundo dos complexos, a cota define um **raio** no plano complexo — um disco centrado na origem contém todas as raízes (reais e complexas).

---

## Aula 14 — Eliminação de Gauss e Sistemas Mal-Condicionados

### Sistemas Lineares como Novo Problema

A partir desta aula, o foco muda de **raízes de polinômios** para **sistemas de equações lineares** $Ax = b$. A maioria dos problemas de engenharia e física se reduz a sistemas lineares — simulações, redes de circuitos, elementos finitos.

---

### Eliminação de Gauss

O método de álgebra linear tem um nome formal: **eliminação gaussiana**.

**Procedimento**:
1. Escrever o sistema como matriz aumentada $[A | b]$
2. Usar operações elementares de linha para zerar os elementos abaixo da diagonal (forma escalonada)
3. Resolver de baixo para cima (**back substitution**)

Para $3x + 2y = 6$ e $2x - y = 4$:
```
[3  2 | 6]      eliminação      [3    2 | 6]      back-sub
[2 -1 | 4]   ───────────────→   [0  -7/3 | 0]   ─────────→   y=0, x=2
```

As operações de linha não alteram o conjunto solução — é o que o JB quis dizer com "tu pode operar, os resultados não se alteram".

---

### Sistemas Mal-Condicionados

Um sistema é **mal-condicionado** quando uma pequena perturbação nos dados causa uma **grande mudança na solução**. Visualmente: dois planos quase paralelos se intersectam em uma linha muito sensível — mover ligeiramente um plano desloca muito a interseção.

O **número de condicionamento** $\kappa(A) = \|A\| \cdot \|A^{-1}\|$ mede isso:
- $\kappa \approx 1$: bem condicionado
- $\kappa \gg 1$: mal condicionado

Mal-condicionamento amplifica erros de arredondamento IEEE 754 — a conexão direta com as primeiras aulas.

---

### Pivotamento e Subtração Catastrófica

Gauss ingênuo tem um problema: se o elemento da diagonal (o *pivô*) for próximo de zero, a divisão amplifica erros enormemente.

**Pivotamento parcial**: antes de eliminar a coluna $k$, trocar a linha atual pela linha abaixo que tem o **maior valor absoluto** na coluna $k$. Mantém os pivôs grandes.

**Subtração catastrófica** (*catastrophic cancellation*): quando dois números muito próximos são subtraídos, os bits significativos se cancelam e o resultado perde precisão:

```
a = 1.000001
b = 1.000000
a - b = 0.000001  ← apenas 1 dígito significativo dos 7 originais
```

Em Gauss, isso acontece ao eliminar linhas com coeficientes parecidos. O pivotamento reduz essa chance ao garantir que o divisor seja grande — a razão $a_{ij}/a_{kk}$ fica com módulo $\le 1$.

---

## Aula 16 — Gauss-Jacobi, Dominância Diagonal e Raio Espectral

### Gauss-Jacobi — A Fórmula Explícita

O método é iterativo: dado um sistema $Ax = b$, isola-se cada variável $x_i$ na sua própria equação e usa-se os valores do passo anterior para calcular o próximo passo.

Para o sistema genérico de $n$ equações:

$$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{\substack{j=1 \\ j \neq i}}^{n} a_{ij} x_j^{(k)} \right)$$

O superscrito $(k)$ indica a iteração atual. A **chave**: todos os $x_j^{(k)}$ usados no cálculo de $x_i^{(k+1)}$ ainda são do passo anterior — nenhuma atualização é usada dentro da mesma iteração. Isso é diferente de Gauss-Seidel, como veremos.

**Exemplo do exemplo da aula** — Sistema $3x - 4y + 7z = 8$, $6x + y + 2z = 5$, $x + 2y - z = 4$:

$$x^{(k+1)} = \frac{8 + 4y^{(k)} - 7z^{(k)}}{3} \qquad y^{(k+1)} = 5 - 6x^{(k)} - 2z^{(k)} \qquad z^{(k+1)} = -4 + x^{(k)} - 2y^{(k)}$$

Iniciando com $(3, 8, 4)$ (chute da aluna): a iteração produz novos valores que substituem os anteriores, e o processo repete até convergir — ou divergir.

---

### Convergência — A Condição Formal da Dominância Diagonal

O JB disse "se a matriz for diagonalmente dominante, o sistema converge." A definição precisa:

Uma matriz $A$ é **estritamente diagonalmente dominante** se, para todo $i$:

$$|a_{ii}| > \sum_{\substack{j=1 \\ j \neq i}}^{n} |a_{ij}|$$

O módulo do elemento da diagonal deve ser **estritamente maior** que a soma dos módulos de todos os outros elementos da mesma linha.

**Por que isso garante convergência?** Intuitivamente: se $|a_{ii}|$ domina, a equação $x_i = (\ldots) / a_{ii}$ faz o denominador "absorver" os erros dos outros termos. A cada iteração, o erro encolhe por um fator menor que 1 — convergência garantida.

A manobra de **reordenar linhas** para conseguir dominância diagonal funciona porque as equações de um sistema linear têm posição intercambiável. Trocar $\text{linha}_i$ e $\text{linha}_j$ não altera o conjunto solução.

---

### Auto-Vetores & Auto-Valores — O que são Formalmente

Dado uma matriz quadrada $A$ de ordem $n$, um **auto-vetor** $\mathbf{v} \neq \mathbf{0}$ e um **auto-valor** $\lambda$ satisfazem:

$$A\mathbf{v} = \lambda\mathbf{v}$$

Multiplicar $A$ pelo vetor $\mathbf{v}$ retorna o mesmo vetor — apenas escalonado por $\lambda$. A direção não muda, apenas o comprimento (e possivelmente o sentido, se $\lambda < 0$).

- Se $|\lambda| < 1$: o vetor encolhe a cada multiplicação por $A$.
- Se $|\lambda| > 1$: o vetor cresce a cada multiplicação por $A$.
- Se $|\lambda| = 1$: o vetor mantém o módulo.

**Por que são caros de encontrar?** Os auto-valores de $A$ são as raízes do **polinômio característico** $\det(A - \lambda I) = 0$, que tem grau $n$. Para $n$ grande, resolver esse polinômio é exatamente o problema que o JB passou o semestre inteiro estudando — e que, para $n \geq 5$, não tem fórmula fechada. Por isso métodos iterativos (como o Método da Potência) são usados na prática.

---

### Raio Espectral — A Segunda Condição Mágica Formalmente

O **raio espectral** $\rho(A)$ de uma matriz é o módulo do maior auto-valor:

$$\rho(A) = \max_i |\lambda_i|$$

A condição de convergência de Gauss-Jacobi é:

$$\rho(G_J) < 1$$

onde $G_J$ é a **matriz de iteração de Jacobi**: $G_J = -D^{-1}(L + U)$, sendo $D$ a diagonal de $A$ e $L, U$ as partes triangulares inferior e superior.

**Por que $< 1$ garante convergência?** O erro na iteração $k$ é proporcional a $G_J^k \cdot \mathbf{e}_0$. Se $\rho(G_J) < 1$, as potências $G_J^k \to 0$ — o erro vai a zero. Se $\rho(G_J) \geq 1$, pelo menos um componente do erro cresce ou oscila sem convergir.

Dominância diagonal estrita implica $\rho(G_J) < 1$ — mas a recíproca não é verdadeira. O raio espectral é condição **mais geral**: uma matriz não diagonalmente dominante ainda pode ter Jacobi convergindo se $\rho(G_J) < 1$.

---

### Gauss-Seidel — A Diferença com Jacobi

O JB anunciou Gauss-Seidel para a próxima aula. A diferença fundamental:

| | Jacobi | Gauss-Seidel |
|---|---|---|
| Valores usados | Todos do passo anterior $x^{(k)}$ | Mistura: usa $x_i^{(k+1)}$ assim que calculado |
| Atualização | Simultânea (todos de uma vez) | Sequencial (cada $x_i$ usa os mais recentes disponíveis) |
| Convergência | Mais lenta | Geralmente mais rápida (2× em casos típicos) |
| Condição | Mesma ($\rho < 1$ para convergência) | Garante mais com matrizes simétricas definidas positivas |

Na prática, a atualização sequencial de Gauss-Seidel é implementada naturalmente com um único array — sem precisar de um array separado para os valores do passo anterior.

---

## Aula 15 — Cadeias de Markov e o Problema dos Lemmings

### O que é uma Cadeia de Markov

O problema dos Lemmings no planeta Zorg é uma **Cadeia de Markov**: um sistema probabilístico onde o **estado futuro depende apenas do estado atual**, não da história passada.

**Propriedade de Markov** (ou "sem memória"):
$$P(\text{estado}_{t+1} \mid \text{estado}_t, \text{estado}_{t-1}, \ldots) = P(\text{estado}_{t+1} \mid \text{estado}_t)$$

No problema: a probabilidade do Lemming morrer ou atingir felicidade eterna depende apenas de onde ele *está agora*, não de como chegou lá.

---

### Estados Absorventes e Transitórios

- **Absorventes** (`%` morte, `$` felicidade): uma vez que o Lemming entra, nunca mais sai.
- **Transitórios** (`.` passagem, `A` posição inicial): o Lemming pode entrar e sair.

Para o cenário `%..A*$`:
- A pergunta fundamental é: dado que começo em `A`, qual a **probabilidade de absorção** em cada estado absorvente?

---

### Resolvendo com Eliminação de Gauss

As equações de probabilidade de absorção formam um **sistema linear** — é por isso que Gauss aparece nessa aula. Para um cenário simples `%..A*`:

Definindo $P_X$ = probabilidade de atingir felicidade partindo do estado $X$:

$$P_A = \frac{1}{2} \cdot P_\% + \frac{1}{2} \cdot P_* = \frac{1}{2}(0) + \frac{1}{2}(1) = 0{,}5$$

Para labirintos maiores com vários estados transitórios, monta-se o sistema $Ax = b$ e resolve-se com Gauss — conectando diretamente os dois conteúdos do semestre.

---

### Aplicações Reais de Cadeias de Markov

Cadeias de Markov aparecem em:
- **PageRank do Google**: cada página da web é um estado; links são transições probabilísticas; a importância de uma página é sua probabilidade de absorção na cadeia.
- **Modelos de linguagem (LLMs)**: cada token gerado depende do estado atual da sequência.
- **Previsão de tempo, análise de crédito, simulação de filas** — qualquer sistema onde "o passado importa apenas pelo estado em que deixou o presente".

---

## Aula 03 — Formatos Decimais e a Origem do IEEE 754

### Formatos Decimais vs. Binários

Além dos formatos binários (binary32, binary64 — os que aparecem em sala), o IEEE 754 define formatos **decimais**: decimal32, decimal64, decimal128. Eles representam números em base 10.

O problema fundamental: $0.1$ em binário é uma dízima periódica ($0.0\overline{0011}$). Somá-lo dez vezes não resulta exatamente em $1.0$. Em aplicações financeiras (onde $0.10 \times 10 = 1.00$ é um requisito legal), o formato decimal é necessário. Calculadoras físicas usam decimal; processadores de propósito geral usam binário — daí a distinção que JB menciona.

### Por Que o Padrão foi Necessário em 1985

Antes do IEEE 754, cada fabricante implementava ponto flutuante à sua maneira. O mesmo programa em um VAX e em um IBM 360 produzia resultados diferentes. O padrão garante **portabilidade bit-a-bit**: dado o mesmo input, qualquer hardware compatível produz exatamente os mesmos bits de saída.

---

## Aula 04 — FPU Status Word: Cada Bit e o Que Ele Protege

### Estrutura Detalhada dos 5 Bits de Exceção

O registrador mencionado nas notas (5 bits, sem variável associada) é parte do status register do x87 FPU:

| Bit | Nome | Quando é setado |
|---|---|---|
| **IE** | Invalid Operation | `0/0`, `sqrt(-1)`, NaN como operando |
| **DE** | Denormal | Um operando é número subnormal |
| **ZE** | Zero Divide | Divisão por zero exato |
| **OE** | Overflow | Resultado excede `MAX_FLOAT` |
| **UE** | Underflow | Resultado é menor que o menor normal |
| **PE** | Precision | Resultado foi arredondado |

O programador pode **mascarar** cada bit individualmente. Código numérico de produção frequentemente mascara **PE** (arredondamento é inevitável) mas deixa **IE** e **ZE** não mascarados para detectar erros reais e disparar interrupções de hardware.

---

## Aula 05 — Por Que Grau Ímpar Garante Raíz Real

O resultado que as notas mencionam tem prova direta pelo **Teorema do Valor Intermediário**:

Para $p(x) = a_n x^n + \ldots$ com $n$ ímpar e $a_n > 0$:
- $\lim_{x \to -\infty} p(x) = -\infty$
- $\lim_{x \to +\infty} p(x) = +\infty$

Como $p$ é contínua em $\mathbb{R}$ e assume valores de ambos os sinais, existe $c \in \mathbb{R}$ com $p(c) = 0$ — pelo Teorema de Bolzano. Para grau par, ambos os limites têm o mesmo sinal: $p(x) = x^2 + 1$ tem grau par e zero raízes reais.

### Raízes Complexas Conjugadas e o Plano Complexo

Quando o JB "desce o $10$" e as quatro raízes imaginárias vão se tornando reais, o que ocorre geometricamente: dois pares de raízes conjugadas $(a + bi, a - bi)$ se movem no plano complexo em direção ao eixo real. Quando $b \to 0$, as raízes "colidem" no eixo real e tornam-se duas raízes reais (possivelmente coincidentes). Isso é o mecanismo por trás de "desce de dois em dois".

---

## Aula 07 — Derivação da Fórmula da Secante e o Limite para Newton

### Por Que a Fórmula tem Aquele Formato

Reta passando por $(a, f(a))$ e $(b, f(b))$:
$$\ell(x) = f(a) + \frac{f(b) - f(a)}{b - a}(x - a)$$

Para $\ell(c) = 0$, isolando $c$:
$$c = a - f(a) \cdot \frac{b - a}{f(b) - f(a)} = \frac{b \cdot f(a) - a \cdot f(b)}{f(a) - f(b)}$$

Isso é exatamente o resultado final nas notas. **Newton é o caso limite**: quando $b \to a$, a razão $\frac{f(b) - f(a)}{b - a}$ converge para $f'(a)$ — a secante vira tangente, e o método usa só um ponto.

---

## Aula 09 — Por Que o Resultado foi 0.000000

### Subnormais e a Armadilha do `%f`

O exercício 1 do laboratório imprimiu `0.000000`. Isso não é zero aritmético — é um número muito pequeno impresso com `%f`, que exibe apenas 6 casas decimais. Se o resultado é $3.7 \times 10^{-12}$, aparece como `0.000000`.

Para inspecionar o valor real: `printf("%.15e\n", x)` mostra notação científica com 15 dígitos. O resultado aparecendo "três vezes" confirma que IEEE 754 é **determinístico**: dado o mesmo hardware e compilador, a mesma sequência produz os mesmos bits.

---

## Aula 12 — Laboratório: Matrizes Aumentadas e Regra de Descartes

### Matrizes Aumentadas em Código C

A estrutura natural para Gauss em C:

```c
double aug[N][N+1];  // última coluna é b
for (int k = 0; k < N; k++) {
    for (int i = k+1; i < N; i++) {
        double m = aug[i][k] / aug[k][k];
        for (int j = k; j <= N; j++)   // <= N inclui a coluna b
            aug[i][j] -= m * aug[k][j];
    }
}
```

O `j <= N` (e não `j < N`) garante que a eliminação se aplica também ao vetor $b$. Esquecer isso zera a matriz mas não propaga os efeitos para $b$, produzindo sistema inconsistente — erro silencioso e comum.

### Regra de Descartes Aplicada ao Exercício 2

Para $p(x) = 6x^5 + 18x^3 - 34x^2 - 493x + 1431$ (coeficientes ignorando zeros): $+6, +18, -34, -493, +1431$ → trocas de sinal: $(+18 \to -34)$ e $(-493 \to +1431)$ → **2 raízes positivas**.

Para raízes negativas, aplica-se a $p(-x)$: coeficientes $-6, -18, -34, +493, +1431$ → uma troca → **1 raíz negativa** (garantida, pois número ímpar).

---

## Aula 19 — Decomposição LU: Gauss para Múltiplos Sistemas

### O Problema que LU Resolve

Gauss custa $O(n^3)$ por sistema. Em simulações (o exemplo dos parquinhos), resolve-se $Ax = b_1, \ldots, Ax = b_m$ com a **mesma** $A$ e $m$ vetores $b$ diferentes. Custo ingênuo: $O(m \cdot n^3)$. Com LU: fatoriza-se $A = LU$ uma vez em $O(n^3)$, cada sistema adicional custa $O(n^2)$.

### Como a Fatoração Funciona

A decomposição produz:
- **L** (*Lower*): triangular inferior, diagonal de 1s (implícita — não armazenada)
- **U** (*Upper*): triangular superior — resultado da eliminação de Gauss

Os elementos de L são os **multiplicadores** que Gauss usaria para zerar cada posição. O programa `LU.awk` do JB não os descarta: armazena-os exatamente onde os zeros foram criados. L e U cabem na mesma memória que $A$.

### Resolução em Dois Passos

Para $Ax = b$ com $A = LU$:

**1. Substituição progressiva** — $Ly = b$ (diagonal de L são 1s, trivial):
$$y_i = b_i - \sum_{j=1}^{i-1} l_{ij} \, y_j \qquad O(n^2)$$

**2. Substituição regressiva** — $Ux = y$ (back substitution padrão):
$$x_i = \frac{1}{u_{ii}}\!\left(y_i - \sum_{j=i+1}^{n} u_{ij} \, x_j\right) \qquad O(n^2)$$

### O Pivotamento e a Matriz de Permutação

Se o pivô $a_{kk} = 0$ durante a fatoração, o multiplicador explode. **LU com pivotamento parcial** fatoriza $PA = LU$, onde $P$ é uma **matriz de permutação** que registra as trocas de linha. Resolver $Ax = b$ vira: $LUx = Pb$ — as substituições são as mesmas, mas $b$ é reordenado por $P$ primeiro.

**Quando LU não existe**: se $A$ é singular (determinante zero), a fatoração falha — o maior pivô disponível é exatamente zero. Isso detecta sistemas sem solução única.
