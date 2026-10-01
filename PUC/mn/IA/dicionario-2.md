# Métodos Numéricos — Dicionário de Conceitos (2026/2)
## [Gerado por IA][mvfm]

> Glossário dos conceitos que aparecem nas aulas `aulaXX-2.md`, em [adicoes-2.md](./adicoes-2.md) e na [Lista 2026/2](../atividades/lista-2.md). Cada verbete traz o **conceito**, a **área** e, quando há, um **caso de uso** : um exemplo real, uma aplicação ou a questão da lista em que ele é cobrado.
> Os verbetes estão em ordem alfabética. O índice por área logo abaixo serve para revisar um bloco da matéria de cada vez.

---

### Áreas
| Sigla | Área | Aulas |
|---|---|---|
| **IEE** | IEEE 754 : representação, arredondamento e exceções | 02, 04 |
| **POL** | Polinômios : Taylor, contagem e localização de raízes | 05, 06 |
| **RAI** | Solução de equações : métodos iterativos para raízes | 06, 09, 10 |
| **SIS** | Sistemas lineares : métodos iterativos e decomposição LU | 14, 15 |
| **AJU** | Ajuste de curvas : mínimos quadrados | 16 |

### Índice por área
- **IEE** — [[#Aritmética intervalar]] · [[#Arredondamento direcionado]] · [[#Bias]] · [[#Bit implícito]] · [[#Bits de exceção]] · [[#Comparação com tolerância relativa]] · [[#Double rounding]] · [[#Epsilon de máquina]] · [[#Expoente]] · [[#FMA]] · [[#FTZ e DAZ]] · [[#IEEE 754]] · [[#IEEE 854]] · [[#Infinito]] · [[#Mantissa]] · [[#NaN]] · [[#NaN-boxing]] · [[#Número normalizado]] · [[#Ordenação por padrão de bits]] · [[#Overflow e underflow]] · [[#Precisão]] · [[#qNaN e sNaN]] · [[#Registrador de 80 bits]] · [[#roundTiesToEven]] · [[#Sinal-magnitude]] · [[#Subnormal]] · [[#Underflow gradual]] · [[#Zero com sinal]]
- **POL** — [[#Abel–Ruffini]] · [[#Cota de Cauchy]] · [[#Cota de Fujiwara]] · [[#Cota de Lagrange]] · [[#Deflação]] · [[#Divisão sintética]] · [[#Forma de Horner]] · [[#Função analítica]] · [[#Grupo de Galois]] · [[#Multiplicidade]] · [[#Plano complexo]] · [[#Polinômio]] · [[#Raízes complexas conjugadas]] · [[#Regra de Descartes]] · [[#Resto de Lagrange]] · [[#Série de Taylor]] · [[#Teorema Fundamental da Álgebra]]
- **RAI** — [[#Bisecção]] · [[#Convergência local e global]] · [[#Critério de parada]] · [[#Ehrlich–Aberth]] · [[#Índice de eficiência]] · [[#Inicialização de Bini]] · [[#Método de Brent]] · [[#Método de Newton]] · [[#Método da secante]] · [[#Newton modificado]] · [[#Ordem de convergência]] · [[#Ponto médio seguro]] · [[#Razão áurea]] · [[#Teorema de Bolzano]] · [[#Termo repulsor]] · [[#Weierstrass–Durand–Kerner]]
- **SIS** — [[#Chute inicial]] · [[#Criaturas felpudas]] · [[#Custo da eliminação]] · [[#Decomposição LU]] · [[#Dominância diagonal]] · [[#Eliminação de Gauss]] · [[#Gauss-Jacobi]] · [[#Gauss-Seidel]] · [[#Matriz de iteração]] · [[#Matriz triangular]] · [[#Método da Agatha]] · [[#Pivoteamento]] · [[#Raio espectral]] · [[#Sistema linear]] · [[#Substituição progressiva e regressiva]]
- **AJU** — [[#Ajuste de curvas]] · [[#Equações normais]] · [[#Função-base]] · [[#Gauss–Newton]] · [[#Interpolação]] · [[#Linear nos parâmetros]] · [[#Linearização]] · [[#Mínimos quadrados]] · [[#Resíduo]] · [[#Sobreajuste]]

---

## A

### Abel–Ruffini
- **Área :** POL
- **Conceito :** teorema segundo o qual não existe fórmula **geral**, **por radicais** ($+, -, \times, \div, \sqrt[n]{\ }$), para as raízes de polinômios de grau $\ge 5$. Ruffini publicou uma prova quase completa em 1799 ; Abel fechou o argumento em 1824. As raízes existem (Teorema Fundamental da Álgebra) : só não se escrevem com esse vocabulário. Quínticas específicas, como $x^5 - 2$, podem ter solução por radicais.
- **Caso de uso :** é o "*em 1830 se determinou : não se tem COMO*" da aula05, e o motivo de a segunda metade da matéria existir : acima do grau 4, só iteração numérica. Lista, objetiva 9.

### Ajuste de curvas
- **Área :** AJU
- **Conceito :** encontrar uma função de forma escolhida de antemão que descreva **a tendência** de uma nuvem de pontos, sem passar exatamente por eles. Tem dois passos : escolher o modelo (o "achismo" da aula16 : reta? quadrática? com cosseno?) e escolher os parâmetros. O segundo é resolvido por mínimos quadrados.
- **Caso de uso :** a órbita de Ceres ajustada por Gauss a 40 dias de observações com erro (Lista Q5). Em geral, qualquer medição experimental com ruído.

### Aritmética intervalar
- **Área :** IEE
- **Conceito :** calcular com intervalos $[a, b]$ em vez de números, com a garantia de que o valor verdadeiro está dentro do resultado. No produto, calculam-se os quatro produtos dos extremos e tomam-se o mínimo e o máximo, porque um sinal negativo troca qual par produz o extremo. Cada extremo é arredondado **para fora**.
- **Caso de uso :** a justificativa da aula04 para os arredondamentos direcionados existirem no hardware. Lista Q1e : $[-2, 3] \cdot [1, 4] = [-8, 12]$, e o "menor com menor" daria $-2$. Volta como ferramenta de otimização global na Aula 27 de 2026/1.

### Arredondamento direcionado
- **Área :** IEE
- **Conceito :** os três modos do IEEE 754 que arredondam sempre no mesmo sentido : para $+\infty$ (`roundTowardPositive`), para $-\infty$ (`roundTowardNegative`) e para zero (`roundTowardZero`, o truncamento). Junto com o modo padrão, somam os quatro arredondamentos da aula04.
- **Caso de uso :** os modos para $\pm\infty$ tornam a aritmética intervalar eficiente. O modo para zero, aplicado em série, causou o desastre do índice da Bolsa de Vancouver (Lista Q1c) : perda média de meio milésimo por operação, sempre para baixo.

---

## B

### Bias
- **Área :** IEE
- **Conceito :** deslocamento somado ao expoente antes de guardá-lo : $2^{k-1} - 1$ para $k$ bits de expoente, ou seja, **127** no `float` e **1023** no `double`. "*Antes de usar, tire 127. Quando guardar, adicione 127.*" Faz do expoente armazenado um inteiro **sem sinal** e crescente.
- **Caso de uso :** é o que permite ordenar floats positivos como inteiros (Lista, objetiva 4) e o que faz a linha `i = *(long *) &y` do *Quake III* funcionar como aproximação de logaritmo (Lista Q3e).

### Bisecção
- **Área :** RAI
- **Conceito :** dado $[a, b]$ com $f(a) \cdot f(b) < 0$, avalia-se o ponto médio $m$ e fica-se com a metade em que o sinal ainda troca. É a "pesquisa binária" da aula06 (ou "jogar pessoas na montanha"). Convergência **linear** com fator $1/2$ : um bit por iteração. O número de passos para largura $\le \epsilon$ é conhecido de antemão : $n \ge \log_2\big((b-a)/\epsilon\big)$.
- **Caso de uso :** o único método da matéria com garantia determinística. Não acha raízes de multiplicidade par (o sinal não troca) nem sai do intervalo. Na prática serve para chegar perto e passar a vez a um método rápido. Lista Q3a e objetiva 11.

### Bit implícito
- **Área :** IEE
- **Conceito :** o `1` antes da vírgula de todo número normalizado. Como ele está sempre lá, não é armazenado : "*nem precisa guardá-lo!*". Por isso o `float` guarda 23 bits de mantissa e tem 24 de precisão. Nos subnormais ele passa a valer 0.
- **Caso de uso :** resolve a conta das notas da aula02, $1 + 8 + 24 = 33$ num tipo de 32 bits (Lista, objetiva 1). O formato de 80 bits do x87 é a exceção : lá o bit da frente é explícito.

### Bits de exceção
- **Área :** IEE
- **Conceito :** as cinco flags do IEEE 754 : operação inválida, divisão por zero, overflow, underflow e inexato. São **grudentas** (*sticky*) : ligadas pelo evento e nunca desligadas pelo hardware. "*Usuário só pode zerar, e depois perguntar se algum bit foi levantado.*" A operação não para : entrega um resultado padrão (NaN, $\pm\infty$, subnormal ou arredondado) e segue.
- **Caso de uso :** `feclearexcept` antes de um bloco de álgebra linear e `fetestexcept` depois, sem nenhum teste dentro do laço. O flag *inexato* liga em quase toda conta (`0.1 + 0.2` já liga) e é o que todo mundo ignora.

---

## C

### Chute inicial
- **Área :** SIS / RAI
- **Conceito :** o ponto de partida de um método iterativo. Nos métodos para sistemas (Jacobi, Seidel), se o método converge, converge a partir de **qualquer** chute : o chute só muda quantos passos faltam. Em Newton e na secante, a convergência é local, e o chute decide se o método converge e para qual raiz.
- **Caso de uso :** "*Não existe um macete para começar com um chute melhor*", sobre o $(7, 5, 8)$ da turma na aula14. No *Quake III*, o chute vem do número mágico `0x5f3759df` e já erra só 3,4% (Lista Q3e).

### Comparação com tolerância relativa
- **Área :** IEE
- **Conceito :** comparar floats por $|a - b| \le k\,\varepsilon \cdot \max(|a|, |b|)$ em vez de por `==`. A tolerância **escala** com a magnitude dos números, porque o espaçamento entre floats vizinhos também escala.
- **Caso de uso :** o corolário prático do epsilon de máquina, e também o critério de parada correto da bisecção (`|b - a| <= tol * |m|`).

### Convergência local e global
- **Área :** RAI
- **Conceito :** um método tem convergência **local** se converge a partir de chutes *suficientemente perto* da solução ; **global** se converge a partir de qualquer chute (ou de um conjunto de chutes que se sabe construir). Newton, secante e Aberth têm garantia só local ; a bisecção, dentro do seu intervalo, é global.
- **Caso de uso :** o "buraco na teoria" da aula10 : Ehrlich–Aberth funciona em milhares de casos mas não tem prova de convergência global ; o Newton complexo de Hubbard, Schleicher e Sutherland (2001) tem prova, mas por muito tempo foi mais lento.

### Cota de Cauchy
- **Área :** POL
- **Conceito :** $1 + \max_i |a_i / a_m|$, com $a_m$ o coeficiente líder e o máximo tomado sobre os outros. **Todas** as raízes, inclusive as complexas, têm módulo menor ou igual a ela. Das cotas simples é a mais apertada.
- **Caso de uso :** dá o intervalo inicial da bisecção. Para $x^4 + 6x + 10$ vale 11, e o polinômio não tem raiz real nenhuma : cota não é raiz. Lista Q2b : 13 para $x^4 - 2x^3 - 7x^2 + 8x + 12$, cujas raízes vão até 3.

### Cota de Fujiwara
- **Área :** POL
- **Conceito :** $2 \max\left\{ |a_{m-1}/a_m|,\ |a_{m-2}/a_m|^{1/2},\ \ldots,\ |a_0/(2a_m)|^{1/m} \right\}$. Os coeficientes de grau baixo entram sob raízes de índice crescente, então pesam menos. Costuma ser bem mais apertada que Cauchy e Lagrange.
- **Caso de uso :** citada na aula05 junto com Cauchy e Lagrange, sem ser desenvolvida. Para $x^4 + 6x + 10$ : $2\max\{0,\ 0,\ 6^{1/3},\ 5^{1/4}\} = 2 \times 1{,}817 \approx 3{,}63$, contra 11 de Cauchy. As raízes têm módulo 2,13 e 1,49.

### Cota de Lagrange
- **Área :** POL
- **Conceito :** na forma vista em aula, $\max\left(1,\ \sum_i |a_i / a_m|\right)$ : soma todos os coeficientes normalizados em vez de pegar o maior. Vale também para as raízes complexas. É mais folgada que Cauchy.
- **Caso de uso :** para $x^4 + 6x + 10$ dá 16, contra 11 de Cauchy. Lista Q2b : 29 contra 13.

### Criaturas felpudas
- **Área :** SIS
- **Conceito :** o problema de modelagem do semestre passado retomado na aula14 (os "Lemmings do planeta Zorg" da aula15 de 2026/1). Cada incógnita representa a **chance** de, partindo de um nodo, chegar a outro ; cada equação diz que essa chance é a combinação das chances dos vizinhos. O sistema resultante tem 0's e −1's na diagonal principal.
- **Caso de uso :** a motivação da decomposição LU na aula15 : mudar o nodo de partida é só mudar o vetor $b$, e a fatoração da matriz serve para todos (Lista Q4e).

### Critério de parada
- **Área :** RAI
- **Conceito :** a regra que encerra um método iterativo. Parar quando $|f(x)| < \epsilon$ é tentador e enganoso : uma função quase plana tem $|f|$ minúsculo longe da raiz. O confiável é parar pelo tamanho do passo ou do intervalo, $|x_{n+1} - x_n| < \epsilon$, de preferência em forma relativa.
- **Caso de uso :** o número de passos que o JB reportou (226 para o Jacobi da aula14) depende do critério de parada do programa dele ; com erro $< 10^{-10}$ seriam cerca de 280 (Lista Q4c).

### Custo da eliminação
- **Área :** SIS
- **Conceito :** a eliminação de Gauss num sistema $n \times n$ custa $\sim \tfrac23 n^3$ operações ; resolver um sistema triangular custa $\sim n^2$. O $n^3$ domina : dobrar o tamanho da matriz multiplica o custo por 8.
- **Caso de uso :** a pergunta "*mas será que custa muito?*" da aula15. Com $n = 1000$ e 100 vetores $b$, refazer Gauss custa $\approx 6{,}7 \times 10^{10}$ ; fatorar uma vez e substituir, $\approx 8{,}7 \times 10^{8}$ (Lista Q4e).

---

## D

### Decomposição LU
- **Área :** SIS
- **Conceito :** fatorar $A = L \cdot U$, com $L$ triangular inferior (diagonal unitária, guardando os multiplicadores da eliminação) e $U$ triangular superior (a matriz que a eliminação produz). Então $Ax = b$ vira $Ly = b$ (substituição progressiva) e $Ux = y$ (regressiva). Nem toda matriz tem LU sem troca de linhas ; com pivoteamento, toda matriz inversível tem $PA = LU$.
- **Caso de uso :** a aula15 : resolver o sistema das criaturas felpudas para vários pontos de partida sem refazer a eliminação. Lista Q4d fatora uma $3 \times 3$ e resolve para dois $b$. É o que `numpy.linalg.solve` e o `\` do MATLAB fazem por baixo.

### Deflação
- **Área :** POL
- **Conceito :** depois de encontrar uma raiz $r$, dividir o polinômio por $(x - r)$ e continuar a busca no quociente de grau $n - 1$. Feita por divisão sintética, que é o próprio laço de Horner. O erro de $r$ contamina todos os coeficientes do quociente, e a precisão piora a cada deflação.
- **Caso de uso :** Lista Q2d : a deflação por $x = 3$ deixa $x^3 + x^2 - 4x - 4$, que se fatora de cabeça. Mitigações : deflacionar da menor raiz para a maior e refinar cada raiz com Newton no polinômio **original**. Os métodos simultâneos (Aberth) evitam a deflação por completo.

### Divisão sintética
- **Área :** POL
- **Conceito :** algoritmo de divisão de $p(x)$ por $(x - x_0)$ usando só os coeficientes. É **o mesmo laço** da forma de Horner : os valores intermediários são os coeficientes do quociente e o último é o resto, que pelo Teorema do Resto vale $p(x_0)$.
- **Caso de uso :** avaliar e deflacionar são uma conta só. Aplicada duas vezes, dá $p(x_0)$ e $p'(x_0)$ juntos — exatamente o que Newton precisa.

### Dominância diagonal
- **Área :** SIS
- **Conceito :** uma matriz é estritamente diagonalmente dominante por linhas se, em cada linha, $|a_{ii}| > \sum_{j \ne i} |a_{ij}|$. É condição **suficiente** para Jacobi e Seidel convergirem a partir de qualquer chute. **Não é necessária**.
- **Caso de uso :** "*O que garante que converge? A matriz ser diagonalmente dominante*" (aula14). Mas a matriz da própria aula14 **não é** (falha nas linhas 2 e 3), e o Jacobi convergiu assim mesmo (Lista Q4b). A condição que decide é o raio espectral.

### Double rounding
- **Área :** IEE
- **Conceito :** arredondar duas vezes — primeiro para a precisão do registrador (80 bits), depois para a do tipo (64 bits) ao guardar na memória — nem sempre dá o mesmo que arredondar uma vez só. O resultado passa a depender de *quando* o compilador tira o valor do registrador.
- **Caso de uso :** programas x87 que davam respostas diferentes com `-O0` e `-O2`, e que motivaram a macro `FLT_EVAL_METHOD` do C99. Desapareceu na prática com o SSE2 do x86-64.

---

## E

### Ehrlich–Aberth
- **Área :** RAI
- **Conceito :** método que acha **todas** as raízes de um polinômio ao mesmo tempo, com $n$ estimativas simultâneas. Cada uma dá um passo de Newton corrigido por um termo de repulsão, $\sum_{j \ne i} 1/(z_i - z_j)$, que as impede de cair na mesma raiz. Convergência cúbica para raízes simples, sem deflação. Ehrlich (1967) e Aberth (1973).
- **Caso de uso :** os "*vários newtonzinhos correndo pelo mundo*" com "*cargas de elétrons*" da aula10. É o método do MPSolve e de rotinas modernas de raízes de polinômios de grau alto.

### Eliminação de Gauss
- **Área :** SIS
- **Conceito :** método **direto** para $Ax = b$ : combinações de linhas zeram tudo abaixo da diagonal, e o sistema triangular resultante é resolvido de baixo para cima. Dá a resposta num número fixo de passos, a menos do arredondamento.
- **Caso de uso :** revista na aula14 de 2026/1 e base da LU : a LU é a eliminação de Gauss com os multiplicadores guardados em vez de descartados.

### Epsilon de máquina
- **Área :** IEE
- **Conceito :** a distância de $1$ até o próximo float representável : $\varepsilon = 2^{1-p}$. Vale $2^{-23} \approx 1{,}19 \times 10^{-7}$ no `float` e $2^{-52} \approx 2{,}22 \times 10^{-16}$ no `double`. Mede precisão **relativa**, não tamanho : **não** é o menor float.
- **Caso de uso :** o laço `enquanto 1.0 + EPS > 1.0` da aula04 imprime 24 vezes em `float` e o último valor é $\varepsilon$ (Lista Q1d). Em C : `FLT_EPSILON`, `DBL_EPSILON`.

### Equações normais
- **Área :** AJU
- **Conceito :** o sistema linear obtido ao derivar a soma dos quadrados dos resíduos em relação a cada parâmetro e igualar a zero. Com funções-base $\varphi_j$, a entrada $(j, k)$ da matriz é $\sum_i \varphi_j(x_i)\,\varphi_k(x_i)$ e o lado direito é $\sum_i y_i\,\varphi_j(x_i)$. A matriz é simétrica.
- **Caso de uso :** toda a aula16 é a derivação da primeira equação normal do modelo $ax^2 + bx + c + d\cos x$. Lista Q5c monta as quatro. Para problemas grandes ou mal condicionados, usa-se a fatoração QR em vez das equações normais, que pioram o condicionamento.

### Expoente
- **Área :** IEE
- **Conceito :** o campo que dá a escala do número, como a potência de 10 na notação científica, só que em base 2. 8 bits no `float`, 11 no `double`, guardado com bias. Os valores extremos são códigos especiais : todo zerado para zero e subnormais, todo ligado para infinito e NaN.
- **Caso de uso :** fica **antes** da mantissa no padrão de bits, ao contrário da notação científica escrita, para que a ordem dos bits siga a ordem dos números (aula02).

---

## F

### FMA
- **Área :** IEE
- **Conceito :** *fused multiply-add* : calcula $a \times b + c$ com **um único** arredondamento, em vez de dois. Entrou no padrão na revisão de 2008.
- **Caso de uso :** o laço de Horner é uma sequência de FMAs (`r = fma(r, x, a[i])`), o que o torna quase a operação ideal para um processador moderno. Também é a base de produtos escalares e multiplicação de matrizes em GPU.

### Forma de Horner
- **Área :** POL
- **Conceito :** reescrita aninhada de um polinômio : $p(x) = a_0 + x\,(a_1 + x\,(a_2 + \cdots + x\,a_n))$. Custa $n$ multiplicações e $n$ somas, e isso é **ótimo** : Ostrowski (1954) e Pan (1966) provaram que não dá para fazer com menos. Exige **todos** os coeficientes, inclusive os nulos.
- **Caso de uso :** o "*jeito mega-econômico*" da aula06, escrito "*de trás pra frente*", com o $0$ no lugar do $x^2$ ausente. Lista Q2c avalia $p$ em três pontos com os intermediários. Evita `pow()`, que é lenta e tem erro próprio.

### FTZ e DAZ
- **Área :** IEE
- **Conceito :** flags do registrador `MXCSR` do x86. *Flush-to-zero* zera resultados subnormais ; *denormals-are-zero* trata operandos subnormais como zero. Trocam a garantia do underflow gradual por velocidade.
- **Caso de uso :** em muito hardware, operar com subnormais é 10 a 100 vezes mais lento. Código de áudio e DSP, cujos sinais decaem para valores minúsculos, liga essas flags. `-ffast-math` as liga sem avisar.

### Função analítica
- **Área :** POL
- **Conceito :** função que, perto de cada ponto, é igual à soma da sua série de Taylor. Ter infinitas derivadas não basta : $e^{-1/x^2}$ (com valor 0 em $x = 0$) tem todas as derivadas nulas em 0, e sua série de Taylor é zero, sem se parecer com a função.
- **Caso de uso :** a ressalva que fecha a discussão de Taylor em adicoes-2 : o polinômio aproxima a função **se** ela for analítica. $\sin$, $\cos$, $e^x$ e os polinômios são ; por isso as aproximações da `libm` funcionam.

### Função-base
- **Área :** AJU
- **Conceito :** cada função conhecida que, multiplicada por um parâmetro, compõe um modelo linear nos parâmetros : $F(x) = \sum_j c_j\,\varphi_j(x)$. No modelo da aula16, as bases são $x^2$, $x$, $1$ e $\cos x$.
- **Caso de uso :** trocar de modelo é trocar de bases, e as equações normais continuam com a mesma forma (Lista Q5c). Séries de Fourier são mínimos quadrados com bases seno e cosseno.

---

## G

### Gauss-Jacobi
- **Área :** SIS
- **Conceito :** método iterativo para $Ax = b$ : isola-se cada variável na sua equação, chuta-se uma solução e recalcula-se **todas** as variáveis a partir dos valores da iteração anterior. Repete-se até estabilizar. Converge se o raio espectral da matriz de iteração for menor que 1.
- **Caso de uso :** a revisão da aula14, com 226 passos no sistema da aula. Como cada variável só depende da iteração anterior, todas podem ser calculadas **em paralelo** : é o argumento "*do cara da computação*". O PageRank do Google é resolvido com iterações desse tipo sobre bilhões de incógnitas.

### Gauss-Seidel
- **Área :** SIS
- **Conceito :** variação do Jacobi que usa cada valor novo **assim que é calculado** : o $x$ novo já entra na conta do $y$ da mesma iteração. "*À medida que tu aprende uma ideia melhor, use ela o mais cedo possível.*" Guarda só um vetor, mas cria dependência em série e impede o paralelismo.
- **Caso de uso :** na aula14, o Seidel se saiu **pior** que o Jacobi. Lista Q4c mostra por quê : o raio espectral do Seidel naquele sistema é $(2 + \sqrt5)/4 \approx 1{,}059 > 1$, ou seja, ele diverge. Tem convergência garantida para matrizes diagonalmente dominantes e simétricas definidas positivas.

### Gauss–Newton
- **Área :** AJU
- **Conceito :** método para mínimos quadrados **não lineares** : a cada iteração, lineariza-se o modelo em torno dos parâmetros atuais (pela derivada, como em Newton) e resolve-se um problema linear de mínimos quadrados para o passo.
- **Caso de uso :** a saída para a "notícia ruim" do fim da aula16, quando o modelo tem $e^{bx}$ e o sistema deixa de ser linear. O resultado da linearização por logaritmo serve de chute inicial (Lista Q5e).

### Grupo de Galois
- **Área :** POL
- **Conceito :** grupo das simetrias das raízes de um polinômio. Galois (1832) mostrou que a equação é solúvel por radicais se e somente se esse grupo é **solúvel**. Os grupos que aparecem até o grau 4 são solúveis ; $S_5$ não é, e por isso a fronteira fica no grau 5.
- **Caso de uso :** a explicação de *por que* Abel–Ruffini acontece no grau 5 e não em outro. Galois escreveu o resultado na véspera do duelo que o matou, aos 20 anos.

---

## I

### IEEE 754
- **Área :** IEE
- **Conceito :** o padrão de ponto flutuante binário, de 1985. Define os formatos (sinal, expoente com bias, mantissa com bit implícito), os valores especiais ($\pm 0$, $\pm\infty$, NaN, subnormais), os quatro modos de arredondamento e as cinco exceções. Exige que as operações básicas deem o resultado **exato arredondado**. Revisões em 2008 e 2019. Arquiteto : William Kahan, Turing Award de 1989.
- **Caso de uso :** todo `float` e `double` de todo processador moderno. O bug do FDIV do Pentium (1994) foi uma violação da exigência de resultado exato arredondado (Lista, Parte III.3).

### IEEE 854
- **Área :** IEE
- **Conceito :** padrão de 1987 que generalizou as ideias do 754 para **qualquer base** — o "multi-base" da aula02. Foi absorvido pela revisão de 2008 do 754, que acrescentou formatos decimais (`decimal32/64/128`).
- **Caso de uso :** a aritmética decimal existe para dinheiro : em base 10, $0{,}1$ é exato, e somar centavos não acumula erro de representação.

### Índice de eficiência
- **Área :** RAI
- **Conceito :** $E = p^{1/m}$, com $p$ a ordem de convergência e $m$ o número de avaliações de função por iteração. Mede precisão ganha por unidade de trabalho, e não por iteração.
- **Caso de uso :** Newton : $2^{1/2} \approx 1{,}414$ ; secante : $1{,}618$. Quando $f'$ custa o mesmo que $f$, a secante é **mais eficiente** que Newton, apesar da ordem menor (Lista, objetiva 13 e Q3c).

### Infinito
- **Área :** IEE
- **Conceito :** valor com expoente todo ligado e mantissa toda zerada, com sinal. Resulta de overflow e de divisão por zero de um número não nulo : $1/0 = +\infty$, $-1/0 = -\infty$. Segue a aritmética esperada ($\infty + 1 = \infty$), mas $\infty - \infty$ é NaN.
- **Caso de uso :** o `inf` que o JB imprimiu dividindo 1 por 0 na aula02. `0x7F800000` em `float` (Lista, objetiva 2).

### Inicialização de Bini
- **Área :** RAI
- **Conceito :** forma de posicionar os $n$ chutes iniciais do Ehrlich–Aberth em círculos concêntricos, com raios estimados pelo **polígono de Newton** das magnitudes dos coeficientes. Dario Bini e Fiorentino a implementaram no **MPSolve** (2000).
- **Caso de uso :** as notas da aula10 dizem que Aberth modificou uma ideia de Bini, mas a ordem é a inversa : Bini construiu sobre o método de Aberth e resolveu a parte que a fórmula não resolve, a inicialização.

### Interpolação
- **Área :** AJU
- **Conceito :** encontrar uma função que passe **exatamente** por todos os pontos dados. Com $n$ pontos, há um único polinômio de grau $\le n - 1$ que faz isso. É o oposto do ajuste : erro zero nos pontos, sem nenhuma filtragem do ruído.
- **Caso de uso :** certo para dados exatos (tabelas de funções). Errado para medições com ruído : um polinômio de grau 4 pelos 5 pontos da Lista Q5 oscila entre eles e diverge fora (Q5d). Newton e Lagrange em 2026/1, aulas 23 e 24.

---

## L

### Linear nos parâmetros
- **Área :** AJU
- **Conceito :** um modelo é linear nos parâmetros quando cada parâmetro aparece só multiplicando uma função conhecida de $x$. O modelo pode ser nada linear em $x$ : $ax^2 + bx + c + d\cos x$ é linear nos parâmetros. $a\,e^{bx}$ não é.
- **Caso de uso :** é a condição para que mínimos quadrados leve a um **sistema linear** e se resolva por Gauss (Lista, objetiva 16). O "*não é vezes $x$... é $e \cdot x$*" do fim da aula16 é justamente o modelo sair dessa classe.

### Linearização
- **Área :** AJU
- **Conceito :** transformar um modelo não linear em linear por uma mudança de variável. Para $y = a\,e^{bx}$ : $\ln y = \ln a + b\,x$, uma reta em $(x, \ln y)$. Muda o problema : minimiza-se o erro nos **logaritmos**, que é aproximadamente o erro relativo.
- **Caso de uso :** crescimento exponencial (populações, juros, decaimento radioativo) ajustado como reta num gráfico semilog. Lista Q5e.

---

## M

### Mantissa
- **Área :** IEE
- **Conceito :** a parte "quebrada" do número : os dígitos significativos, depois da vírgula, na forma $1{,}\text{mantissa}$. O `float` armazena 23 bits, o `double` 52. O nome oficial no padrão é *significand* ; "mantissa" é herança das tábuas de logaritmo.
- **Caso de uso :** num NaN, é a mantissa que carrega o bit quiet/signaling e o *payload*. No infinito, ela é toda zero.

### Matriz de iteração
- **Área :** SIS
- **Conceito :** num método iterativo escrito como $x^{(k+1)} = T\,x^{(k)} + c$, a matriz $T$. Separando $A = D + L + U$ (diagonal, parte estritamente inferior e estritamente superior) : $T_J = -D^{-1}(L + U)$ no Jacobi e $T_S = -(D + L)^{-1}U$ no Seidel. O erro evolui como $e^{(k+1)} = T\,e^{(k)}$.
- **Caso de uso :** tudo o que se quer saber sobre a convergência está nos autovalores de $T$. Lista Q4c calcula os de $T_S$ para o sistema da aula14.

### Matriz triangular
- **Área :** SIS
- **Conceito :** matriz com zeros acima (**inferior**, $L$) ou abaixo (**superior**, $U$) da diagonal. Um sistema triangular se resolve por substituição, uma variável por vez, em $\sim n^2$ operações. Zeros *dentro* da parte triangular são permitidos.
- **Caso de uso :** "*A matriz L é diagonal inferior. Para cima, tudo é 0. Não impede a existência de 0's embaixo*" (aula15). É o formato a que a eliminação de Gauss e a LU reduzem o problema.

### Método da Agatha
- **Área :** SIS
- **Conceito :** o híbrido descrito na aula14 : divide as variáveis em blocos (100 linhas de uma matriz $1000 \times 1000$, por exemplo), calcula cada bloco em paralelo como no Jacobi e usa os valores novos do bloco no bloco seguinte, como no Seidel. O tamanho do bloco é livre.
- **Caso de uso :** "*Malandro*". A ideia geral — paralelismo dentro do bloco, dependência entre blocos — é a mesma do Gauss-Seidel **por blocos** e da ordenação **vermelho-preto** usada em solvers de equações diferenciais em GPU, que colore as incógnitas para que cada cor seja atualizada em paralelo.

### Método de Brent
- **Área :** RAI
- **Conceito :** método híbrido para raízes : mantém um intervalo com troca de sinal (a garantia da bisecção) e tenta a cada passo um passo rápido por interpolação. Se o passo rápido sai do intervalo ou não encolhe o suficiente, faz bisecção. Tem a velocidade de um método superlinear e a garantia de terminação de um linear.
- **Caso de uso :** é o que roda de fato em `scipy.optimize.brentq`, no `fzero` do MATLAB e no `uniroot` do R. Ninguém usa bisecção pura ou Newton puro em produção.

### Método de Newton
- **Área :** RAI
- **Conceito :** $x_{n+1} = x_n - f(x_n)/f'(x_n)$ : aproxima $f$ pela tangente em $x_n$ e toma a raiz da tangente. É a secante no limite, quando os dois pontos se juntam. Convergência **quadrática** para raiz simples com chute próximo : os dígitos corretos dobram por iteração. Funciona no plano complexo. Falha com derivada nula, em ciclos, em funções como $\sqrt[3]{x}$ (onde $x_{n+1} = -2x_n$) e perde a ordem em raízes múltiplas.
- **Caso de uso :** a aula09 ("*negócio que só tem vantagens*"). O `Q_rsqrt` do *Quake III* é uma iteração de Newton em $1/y^2 - x$, escolhida para não ter divisão (Lista Q3d). Na Lista Q3b, três iterações levam de 2 a 14 casas corretas.

### Método da secante
- **Área :** RAI
- **Conceito :** $x_{n+1} = x_n - f(x_n)\,\dfrac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$ : a reta pelos dois últimos pontos substitui a tangente. Não precisa de derivada e usa **uma** avaliação nova por iteração. Ordem $\varphi \approx 1{,}618$. Não fica presa a um intervalo : "*sai andando*" atrás da raiz.
- **Caso de uso :** a opção quando $f$ vem de uma simulação ou de código de terceiros e não há $f'$. Por avaliação, é mais eficiente que Newton (Lista Q3c).

### Mínimos quadrados
- **Área :** AJU
- **Conceito :** escolher os parâmetros de um modelo que minimizam $\sum_i \big(F(x_i) - y_i\big)^2$. O quadrado substitui o módulo porque é derivável. Derivando em relação a cada parâmetro e igualando a zero, obtém-se um sistema — **linear** se o modelo é linear nos parâmetros.
- **Caso de uso :** "*Outro método de Gauss*" (aula16). Gauss o usou para reencontrar Ceres em 1801 ; Legendre o publicou primeiro, em 1805. Hoje é a regressão linear de qualquer planilha (Lista Q5).

### Multiplicidade
- **Área :** POL
- **Conceito :** quantas vezes uma raiz se repete : $r$ tem multiplicidade $m$ se $(x - r)^m$ divide $p$ e $(x - r)^{m+1}$ não. Numa raiz múltipla, $p$ e $p'$ se anulam juntos. Raízes de multiplicidade par não trocam o sinal de $p$.
- **Caso de uso :** a regra de Descartes conta raízes **com** multiplicidade. A bisecção não enxerga raízes de multiplicidade par, e Newton cai para convergência linear nelas.

---

## N

### NaN
- **Área :** IEE
- **Conceito :** *Not a Number* : expoente todo ligado e pelo menos um bit da mantissa ligado. Resultado de operações sem valor definido : $0/0$, $\infty - \infty$, $\sqrt{-1}$. É o único valor que **não é igual a si mesmo**, e o seu bit de sinal não significa nada.
- **Caso de uso :** o `-nan` que o JB conseguiu com $0/0$ na aula02 é o *real indefinite* do x86, `0xFFC00000`, que tem o bit de sinal ligado. `x != x` é o teste clássico de NaN (Lista, objetiva 3). Um NaN dentro de `std::sort` é comportamento indefinido.

### NaN-boxing
- **Área :** IEE
- **Conceito :** usar os ~51 bits livres do *payload* de um NaN de `double` para guardar ponteiros ou inteiros. Um único valor de 64 bits representa ou um `double` de verdade ou, se for NaN, outro tipo embutido.
- **Caso de uso :** é como motores de JavaScript e o LuaJIT representam qualquer valor dinâmico num registrador só.

### Newton modificado
- **Área :** RAI
- **Conceito :** para uma raiz de multiplicidade $m$ conhecida, $x_{n+1} = x_n - m\,f(x_n)/f'(x_n)$. Recupera a convergência quadrática que o Newton comum perde em raízes múltiplas, onde cai para linear com fator $1 - 1/m$.
- **Caso de uso :** para $f = (x - 1)^2$, Newton comum reduz o erro à metade por passo ; com $m = 2$, chega na raiz num passo só (Lista, objetiva 12).

### Número normalizado
- **Área :** IEE
- **Conceito :** número com o expoente nem todo zerado nem todo ligado, lido como $(-1)^s \times 1{,}\text{mantissa} \times 2^{e - \text{bias}}$. O primeiro `1` fica sempre antes da vírgula, "*pra não ficar com tantos zeros antes da parte verdadeiramente importante*". No `float`, o menor positivo é $2^{-126} \approx 1{,}18 \times 10^{-38}$.
- **Caso de uso :** a forma "arrumadinha" da aula02, que dá o bit implícito de graça. Abaixo de $2^{-126}$ entram os subnormais.

---

## O

### Ordem de convergência
- **Área :** RAI
- **Conceito :** um método tem ordem $p$ se $e_{n+1} \approx C\,e_n^{\,p}$ perto da solução. $p = 1$ é **linear** (ganha dígitos a taxa constante), $p = 2$ é **quadrática** (dobra os dígitos por iteração), $p = 3$ é **cúbica**.
- **Caso de uso :** bisecção 1, secante 1,618, Newton 2, Ehrlich–Aberth 3. Lista Q3b mostra os dígitos de Newton dobrando : $10^{-4} \to 10^{-7} \to 10^{-14}$.

### Ordenação por padrão de bits
- **Área :** IEE
- **Conceito :** para dois floats positivos, $a < b$ se e só se o padrão de bits de $a$, lido como inteiro sem sinal, é menor que o de $b$. Funciona pela ordem dos campos e pelo bias. Para negativos a ordem se inverte, porque o formato é sinal-magnitude ; o *radix sort* de floats corrige isso invertendo os bits dos negativos.
- **Caso de uso :** o "*ordenar float é ordenar uma string de 4 char*" da aula02 (com a ressalva de que em x86, little-endian, `memcmp` não funciona). O `Q_rsqrt` do *Quake III* usa a mesma propriedade para ler um logaritmo aproximado nos bits (Lista Q3e).

### Overflow e underflow
- **Área :** IEE
- **Conceito :** **overflow** : o resultado é grande demais para o formato e vira $\pm\infty$ (ou o maior finito, conforme o arredondamento). **Underflow** : o resultado é pequeno demais para um normal e vira subnormal ou zero. Os dois ligam o bit de exceção correspondente.
- **Caso de uso :** o Ariane 5 (1996) caiu por um overflow de outro tipo : a conversão de um `double` para inteiro de 16 bits, que não tem infinito para onde ir (Lista, Parte III.2).

---

## P

### Pivoteamento
- **Área :** SIS
- **Conceito :** trocar linhas durante a eliminação para usar como pivô o maior elemento (em módulo) da coluna. Evita dividir por zero e, principalmente, evita dividir por números pequenos, que amplificam o erro de arredondamento. Com pivoteamento, a fatoração vira $PA = LU$, com $P$ uma matriz de permutação.
- **Caso de uso :** a resposta à pergunta "*sempre vai existir uma LU?*" da aula15 : sem trocar linhas, não ; com trocas, para toda matriz inversível. Toda biblioteca séria faz pivoteamento parcial.

### Plano complexo
- **Área :** POL
- **Conceito :** representação dos números complexos com a parte real num eixo e a imaginária no outro. As raízes de um polinômio de coeficientes reais ficam simétricas em relação ao eixo real.
- **Caso de uso :** a animação da aula06 em que as raízes de $x^4 + 6x + a$ se aproximam no eixo real, colidem e saem para o plano complexo conforme $a$ cresce.

### Polinômio
- **Área :** POL
- **Conceito :** $p(x) = a_m x^m + a_{m-1}x^{m-1} + \cdots + a_1 x + a_0$. O **grau** é o maior expoente com coeficiente não nulo. Fáceis de avaliar, derivar e integrar ; difíceis de achar raízes. Um polinômio de grau $m$ tem exatamente $m$ raízes complexas, contadas com multiplicidade.
- **Caso de uso :** "*Quase tudo é mais fácil com polinômios*" (aula05). Por isso se aproximam funções por eles (Taylor) e por isso achar raízes é o problema central do bloco.

### Ponto médio seguro
- **Área :** RAI
- **Conceito :** calcular o ponto médio como `a + (b - a) / 2` em vez de `(a + b) / 2`. A segunda forma pode estourar (para $\pm\infty$ em float, ou para negativo em inteiros) quando $a$ e $b$ são grandes, e pode até cair fora de $[a, b]$ por arredondamento.
- **Caso de uso :** o bug do `java.util.Arrays.binarySearch`, que passou nove anos na biblioteca padrão do Java até 2006. A bisecção é uma busca binária e tem o mesmo problema.

### Precisão
- **Área :** IEE
- **Conceito :** o número $p$ de bits significativos do formato, **contando o bit implícito** : 24 no `float`, 53 no `double`, 64 no x87. Em decimal, $p \log_{10} 2$ : ~7 casas no `float`, ~16 no `double`.
- **Caso de uso :** a diferença entre "24" e "23" nas descrições do `float` é a diferença entre precisão e bits armazenados (Lista, objetiva 1).

---

## Q

### qNaN e sNaN
- **Área :** IEE
- **Conceito :** os dois tipos de NaN, distinguidos pelo bit mais alto da mantissa. O **quiet** (bit 1) propaga silenciosamente pelas contas e é o resultado padrão de operações inválidas. O **signaling** (bit 0, com outro bit ligado) dispara a exceção de operação inválida quando é usado.
- **Caso de uso :** a divisão que importa entre os "*dois sabores*" de NaN da aula02 não é de sinal, é esta. sNaN serve para marcar memória não inicializada.

---

## R

### Raio espectral
- **Área :** SIS
- **Conceito :** $\rho(T) = \max |\lambda_i|$, o maior módulo entre os autovalores de $T$. Um método iterativo $x^{(k+1)} = Tx^{(k)} + c$ converge a partir de qualquer chute **se e somente se** $\rho(T) < 1$, e o erro cai aproximadamente por um fator $\rho$ a cada passo.
- **Caso de uso :** a condição que decide de fato, onde a dominância diagonal é só suficiente. No sistema da aula14 : $\rho(T_J) \approx 0{,}914$ (Jacobi converge, em ~250 passos) e $\rho(T_S) \approx 1{,}059$ (Seidel diverge) — Lista Q4c. Introduzido na aula16 de 2026/1.

### Raízes complexas conjugadas
- **Área :** POL
- **Conceito :** se os coeficientes de $p$ são **reais** e $z = a + bi$ é raiz, então $\bar z = a - bi$ também é, porque $p(\bar z) = \overline{p(z)} = 0$. Raízes complexas vêm aos pares, e raízes reais só entram ou saem do eixo real aos pares.
- **Caso de uso :** é a explicação do "de 2 em 2" de Descartes (Lista, objetiva 8) e da ressalva da aula06 : "*as raízes complexas são espelhadas, mas não sempre. Só quando os coeficientes são reais.*"

### Razão áurea
- **Área :** RAI
- **Conceito :** $\varphi = (1 + \sqrt5)/2 \approx 1{,}618$, raiz positiva de $p^2 - p - 1 = 0$. É a ordem de convergência da secante : a recorrência do erro $e_{n+1} \approx C e_n e_{n-1}$, com a hipótese $e_{n+1} \approx K e_n^{\,p}$, leva a $p = 1 + 1/p$.
- **Caso de uso :** o link para a Wikipédia na aula09. É o mesmo motivo de $\varphi$ aparecer em Fibonacci : uma recorrência que depende dos dois termos anteriores.

### Registrador de 80 bits
- **Área :** IEE
- **Conceito :** o formato *double extended* do coprocessador x87 : 1 bit de sinal, 15 de expoente, 64 de mantissa com o bit da frente **explícito**. O padrão recomenda calcular em precisão maior que a do tipo, para proteger resultados intermediários.
- **Caso de uso :** o "*número bizarro de 80 bits*" da aula04. Causa double rounding e faz o laço do epsilon medir o epsilon do registrador em vez do tipo. Em x86-64 o caminho padrão é o SSE2, sem registradores estendidos.

### Regra de Descartes
- **Área :** POL
- **Conceito :** o número de raízes reais **positivas** de $p$, com multiplicidade, é igual ao número $v$ de trocas de sinal na sequência dos coeficientes não nulos, ou é menor que $v$ por um número par. Para as **negativas**, aplica-se a mesma regra a $p(-x)$, o que equivale a trocar o sinal dos coeficientes de grau ímpar.
- **Caso de uso :** $4x^5 - 6x^4 + 12x^3 - 17x + 9$ tem 4, 2 ou 0 positivas e exatamente 1 negativa (aula05). Descartes dá as possibilidades ; a varredura com Horner decide (Lista Q2a e Q2c).

### Resíduo
- **Área :** AJU
- **Conceito :** a diferença $r_i = y_i - F(x_i)$ entre o dado e o modelo em cada ponto. Mínimos quadrados minimiza $\sum r_i^2$. Se o modelo tem termo constante, os resíduos do ajuste ótimo **somam zero** : é a própria equação normal do termo constante.
- **Caso de uso :** Lista Q5b : resíduos $0, -0{,}2, 0{,}6, -0{,}6, 0{,}2$, soma zero e soma dos quadrados $0{,}8$. Olhar o gráfico dos resíduos é o jeito de descobrir se o "achismo" do modelo estava errado : resíduos com padrão indicam modelo ruim.

### Resto de Lagrange
- **Área :** POL
- **Conceito :** o erro de truncar a série de Taylor no grau $n$ em torno de $a$ : $R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x - a)^{n+1}$, para algum $\xi$ entre $a$ e $x$. Como $\xi$ é desconhecido, usa-se o máximo de $|f^{(n+1)}|$ no intervalo como cota.
- **Caso de uso :** quantifica o "*não imita 100% a função*" da aula05. Lista Q2f : a cota para $e^{0{,}5}$ com grau 3 é $0{,}0043$ e o erro real é $0{,}0029$.

### roundTiesToEven
- **Área :** IEE
- **Conceito :** o modo de arredondamento padrão do IEEE 754 : para o representável mais próximo, e em caso de **empate**, para o que tem mantissa **par**. $2{,}5 \to 2$, $3{,}5 \to 4$. Metade dos empates sobe e metade desce, então o erro não tem viés.
- **Caso de uso :** o erro de somas longas cresce como $\sqrt n$ em vez de $n$. Na Lista Q1c : um terço de ponto de erro acumulado na Bolsa de Vancouver, contra os ~574 pontos que o truncamento perdeu. Também é quem faz o laço do epsilon parar em $2^{-24}$.

---

## S

### Série de Taylor
- **Área :** POL
- **Conceito :** aproximação de uma função por um polinômio construído a partir das derivadas num ponto âncora $a$ : $f(x) \approx \sum_k \frac{f^{(k)}(a)}{k!}(x - a)^k$. Boa perto da âncora, ruim longe dela. O erro é dado pelo resto de Lagrange.
- **Caso de uso :** o jeito de "*transformar uma função qualquer num polinômio fofinho*" (aula05). Newton é Taylor truncado no grau 1. A `libm` calcula $\sin$, $\exp$ e $\log$ com polinômios desse tipo.

### Sinal-magnitude
- **Área :** IEE
- **Conceito :** representação em que um bit guarda o sinal e os outros guardam o valor absoluto, ao contrário do complemento de dois dos inteiros. É a do IEEE 754 : $-x$ e $x$ diferem só no bit mais alto.
- **Caso de uso :** é o que permite existir $-0$, e o que inverte a ordem dos negativos quando se comparam floats pelos bits.

### Sistema linear
- **Área :** SIS
- **Conceito :** um conjunto de equações lineares, escrito $Ax = b$. Resolve-se por métodos **diretos** (Gauss, LU : resposta em número fixo de passos) ou **iterativos** (Jacobi, Seidel : aproximações sucessivas, bons para matrizes grandes e esparsas).
- **Caso de uso :** o sistema $3 \times 3$ da aula14 (Lista Q4) e o das criaturas felpudas. Aparece também no fim de todo ajuste por mínimos quadrados.

### Sobreajuste
- **Área :** AJU
- **Conceito :** usar um modelo com parâmetros demais, que se ajusta ao **ruído** dos dados em vez da tendência. O erro nos pontos usados vai a zero, e o erro em pontos novos piora.
- **Caso de uso :** um polinômio de grau 4 por 5 pontos com ruído (Lista Q5d). "*Não uma função que siga EXATAMENTE cada pontinho, mas uma média*" (aula16). É o problema central de aprendizado de máquina, com outro nome (*overfitting*).

### Subnormal
- **Área :** IEE
- **Conceito :** número com expoente armazenado **zero** e mantissa não nula. O bit implícito passa a valer 0 e o expoente efetivo fica fixo em $-126$ : $(-1)^s \times 0{,}\text{mantissa} \times 2^{-126}$. Preenche o vazio entre zero e o menor normal, com precisão cada vez menor. O menor positivo do `float` é $2^{-149} \approx 1{,}4 \times 10^{-45}$.
- **Caso de uso :** os números que "*não conseguem ser normalizados*" (aula02) e "*preenchem aquele vazio perto do 0*" (aula04). `0x00000001` é o menor deles (Lista Q1b).

### Substituição progressiva e regressiva
- **Área :** SIS
- **Conceito :** resolução de sistemas triangulares. **Progressiva** (*forward*) : num sistema triangular inferior $Ly = b$, calcula-se $y_1$ primeiro e desce-se. **Regressiva** (*backward*) : num triangular superior $Ux = y$, calcula-se $x_n$ primeiro e sobe-se. Cada uma custa $\sim n^2$.
- **Caso de uso :** os dois passos da LU na aula15 (Lista Q4d). É por elas serem baratas que a LU compensa quando há muitos vetores $b$.

---

## T

### Teorema de Bolzano
- **Área :** RAI
- **Conceito :** se $f$ é contínua em $[a, b]$ e $f(a) \cdot f(b) < 0$, existe pelo menos uma raiz em $(a, b)$. Caso particular do Teorema do Valor Intermediário.
- **Caso de uso :** é a garantia da bisecção e explica suas limitações : raízes de multiplicidade par não trocam o sinal, e a garantia só vale dentro do intervalo. Na Lista Q2c, as trocas de sinal encontradas com Horner resolvem a ambiguidade de Descartes.

### Teorema Fundamental da Álgebra
- **Área :** POL
- **Conceito :** todo polinômio de grau $m \ge 1$ com coeficientes complexos tem exatamente $m$ raízes complexas, contadas com multiplicidade.
- **Caso de uso :** "*No polinômio sempre vamos saber quantas raízes vamos ter, olhando para o grau*" (aula05). É a etapa 1 do pipeline de raízes, e o que permite ao Aberth saber quantas estimativas lançar.

### Termo repulsor
- **Área :** RAI
- **Conceito :** o somatório $\sum_{j \ne i} 1/(z_i - z_j)$ no denominador do passo de Ehrlich–Aberth. Tem a forma do campo de uma carga pontual em duas dimensões : quando duas estimativas se aproximam ele cresce, e o passo encolhe. Longe umas das outras, ele some e o método volta a ser Newton.
- **Caso de uso :** as "*cargas de elétrons*" com que o JB explicou a aula10. É o que impede os "newtonzinhos" de caírem todos na mesma raiz.

---

## U

### Underflow gradual
- **Área :** IEE
- **Conceito :** a perda **progressiva** de precisão perto do zero, que os subnormais permitem, em vez de um salto direto do menor normal para zero. Garante $x - y = 0 \iff x = y$.
- **Caso de uso :** sem ele, `if (x != y) z = 1.0 / (x - y)` poderia dividir por zero (Lista, objetiva 6). Kahan defendeu essa propriedade na elaboração do padrão contra quem preferia *flush-to-zero* por desempenho.

---

## W

### Weierstrass–Durand–Kerner
- **Área :** RAI
- **Conceito :** método que atualiza $n$ estimativas simultâneas das raízes por $z_i \leftarrow z_i - \dfrac{p(z_i)}{a_n \prod_{j \ne i}(z_i - z_j)}$. O produto faz o papel de uma derivada aproximada usando as outras estimativas : é deflação sem modificar o polinômio. Weierstrass (1891), redescoberto por Durand (1960) e Kerner (1966). Convergência quadrática perto da solução.
- **Caso de uso :** o antecessor do Aberth na linha do tempo da aula10 ("*os métodos de '60, '66 e '68 são evoluções do de Weierstrass*").

---

## Z

### Zero com sinal
- **Área :** IEE
- **Conceito :** o IEEE 754 tem $+0$ (`0x00000000`) e $-0$ (`0x80000000`). Comparam como iguais, mas se comportam diferente em algumas operações : $1/{+0} = +\infty$ e $1/{-0} = -\infty$.
- **Caso de uso :** o sinal do zero guarda de que lado um resultado que sofreu underflow veio, o que importa em funções com corte, como $\log$ e $\operatorname{atan2}$. Lista Q1b.

---
### Ver também
- [adicoes-2.md](./adicoes-2.md) — o aprofundamento das aulas 02 a 10, de onde sai a maior parte dos verbetes de IEE, POL e RAI.
- [adicoes.md](./adicoes.md) — 2026/1 : Gauss-Jacobi, raio espectral, LU e mínimos quadrados aprofundados (aulas 16, 19 e 20).
- [Lista 2026/2](../atividades/lista-2.md) — as questões citadas nos casos de uso (objetivas 1–16, Questões 1–5, Parte III).
- [mn-index](../mn-index.md) — índice das aulas.
