# Métodos Numéricos — Lista no formato da prova 2026/2
## [01-10-26][mvfm]
---
### Prefácio
- Lista montada sobre as aulas **2026/2** — [aula02-2](../aula02-2.md) a [aula16-2](../aula16-2.md), mais a revisão da [aula17](../aula17.md) — mas com a **cara da prova** : a estrutura copia o gabarito da G2 de 2026/I ([folha 1](../provas/p1-2026-2/G21.jpg) e [folha 2](../provas/p1-2026-2/G22.jpg)).
- A prova tem **7 questões curtas**, e cada uma tem um *tipo* fixo. Os três simulados abaixo repetem os sete tipos, na mesma ordem :

| # | Na prova do JB | Tipo | Aqui |
|---|---|---|---|
| 1 | Polinômio de menor grau por 3 pontos | conta curta, resposta é uma função | reta de mínimos quadrados (aula16/17) ou polinômio por pontos |
| 2 | Descartes : quantas raízes negativas | conta curta sobre polinômios | Descartes, cotas, Horner (aulas 05 e 06) |
| 3 | Custo da substituição regressiva | múltipla escolha de **custo** | custo de LU, bisecção, substituições |
| 4 | Duas iterações de método iterativo | conta, resposta é um vetor | Jacobi, Seidel, substituição com LU (aulas 14 e 15) |
| 5 | 5 afirmativas sobre IEEE 754 | analise e marque a combinação | IEEE 754 e solução de equações |
| 6 | Quando a LU é vantajosa | dissertativa de **uma frase** | Jacobi × Seidel, Aberth, dominância diagonal |
| 7 | Newton, valor após a 2ª iteração | múltipla escolha com "Outra resposta" | Newton e secante (aula09) |

- Três coisas que a prova ensina sobre o JB :
	- A questão 1 era uma **pegadinha** : três pontos sugerem grau 2, mas eles eram colineares e a resposta era uma reta. "Menor grau" é para ser levado a sério.
	- A questão 4 diz "Gauss-**Jordan**", mas pede *estimativa inicial* e *iterações* — é o **Gauss-Jacobi** (a resposta $[-2{,}5;\ -2{,}5;\ -42]$ só sai por Jacobi). E repare que o sistema da prova nem é diagonalmente dominante e os valores já saem explodindo : ninguém perguntou se convergia, só pediu duas iterações.
	- Na questão 7 a resposta certa era **"Outra resposta"**. Não confie que a sua conta precisa bater com uma das alternativas.
- Interpolação (questão 1 da prova) ainda não apareceu nas aulas de 2026/2. No lugar dela entra a **reta de mínimos quadrados**, que é o que a [aula17](../aula17.md) avisou que pode cair : *"no máximo, uma questão em que se encontra uma reta"*. O Simulado B mantém a versão original, resolvível por sistema linear.
- Cada **RESPOSTA** está num bloco recolhível logo abaixo da questão, com o resultado na primeira linha e o **passo a passo** em seguida. Resolva antes de abrir.
- Tempo sugerido : **50 minutos** por simulado, sem computador, com calculadora.
- Para treino mais longo e gabarito comentado em profundidade, veja a [lista de exercícios 2026/2](./lista-2.md).

---

## Simulado A

**1.** Encontre a reta $F(x) = ax + b$ que melhor se ajusta, por mínimos quadrados, aos pontos $(0, 1)$, $(1, 3)$, $(2, 4)$ e $(3, 8)$.

> [!success]- **RESPOSTA**
> $$F(x) = 2{,}2x + 0{,}7$$
> ou equivalente.
>
> **Passo 1 — de onde vêm as equações.** Queremos minimizar $\sum (a x_i + b - y_i)^2$. Derivando em relação a $a$ e a $b$ e igualando a zero (o mesmo "chuveirinho" da aula16, só que com dois parâmetros) :
> $$\begin{cases} a \sum x_i^2 + b \sum x_i = \sum x_i y_i \\ a \sum x_i + b \cdot n = \sum y_i \end{cases}$$
>
> **Passo 2 — tabela das somas.**
>
> | $x$ | $y$ | $x^2$ | $xy$ |
> |---|---|---|---|
> | 0 | 1 | 0 | 0 |
> | 1 | 3 | 1 | 3 |
> | 2 | 4 | 4 | 8 |
> | 3 | 8 | 9 | 24 |
> | **6** | **16** | **14** | **35** |
>
> **Passo 3 — montar o sistema**, com $n = 4$ :
> $$\begin{cases} 14a + 6b = 35 \\ 6a + 4b = 16 \end{cases}$$
>
> **Passo 4 — resolver.** Da segunda : $4b = 16 - 6a \Rightarrow b = 4 - 1{,}5a$. Substituindo na primeira : $14a + 6(4 - 1{,}5a) = 35 \Rightarrow 14a + 24 - 9a = 35 \Rightarrow 5a = 11 \Rightarrow a = 2{,}2$. Então $b = 4 - 3{,}3 = 0{,}7$.
>
> **Passo 5 — conferir.** Os resíduos $F(x_i) - y_i$ são $-0{,}3;\ -0{,}1;\ +1{,}1;\ -0{,}7$ e somam **zero** — isso sempre acontece na reta de mínimos quadrados (é a segunda equação normal), então serve de teste rápido.

**2.** Use a regra de Descartes para determinar quantas raízes negativas tem o polinômio $p(x)$ a seguir :
$$p(x) = x^5 - 3x^4 - 5x^3 + 15x^2 + 4x - 12$$

> [!success]- **RESPOSTA**
> **Duas ou nenhuma** raiz negativa.
>
> **Passo 1 — montar $p(-x)$.** Para as negativas, troca-se $x$ por $-x$ : os termos de expoente **ímpar** trocam de sinal, os de expoente **par** ficam como estão.
>
> | Termo | $x^5$ | $-3x^4$ | $-5x^3$ | $+15x^2$ | $+4x$ | $-12$ |
> |---|---|---|---|---|---|---|
> | Expoente | ímpar | par | ímpar | par | ímpar | par |
> | Em $p(-x)$ | $-x^5$ | $-3x^4$ | $+5x^3$ | $+15x^2$ | $-4x$ | $-12$ |
>
> **Passo 2 — contar as trocas de sinal** em $p(-x)$ : $-\ \ -\ \ +\ \ +\ \ -\ \ -$. Há troca de $-$ para $+$ (entre o 2º e o 3º) e de $+$ para $-$ (entre o 4º e o 5º) : **2 trocas**.
>
> **Passo 3 — aplicar a regra.** O número de raízes negativas é o número de trocas ou esse número menos um múltiplo de 2 : **2 ou 0**.
>
> **Para conferir** (não se pede na prova) : as raízes são $-2, -1, 1, 2, 3$, então são de fato duas negativas. Em $p(x)$ os sinais são $+\ -\ -\ +\ +\ -$, 3 trocas : 3 ou 1 positivas — e são 3.

**3.** Você já fatorou a matriz $A$, de tamanho $n \times n$, em $A = L \cdot U$. Chega um novo vetor $b$. O custo (em multiplicações e divisões) de obter a solução de $Ax = b$ a partir de $L$ e $U$ é :

- (a) $O(n)$
- (b) $O(n \log(n))$
- (c) $O(n^2)$
- (d) $O(n^3)$

> [!success]- **RESPOSTA**
> A resposta é $O(n^2)$ — opção **(c)**.
>
> **Passo 1 — o que falta fazer.** Com $A = LU$, resolver $Ax = b$ é resolver $Ly = b$ (substituição progressiva) e depois $Ux = y$ (substituição regressiva).
>
> **Passo 2 — contar a progressiva.** Na linha $i$ de $Ly = b$ multiplicam-se os $i - 1$ valores de $y$ já conhecidos : $0 + 1 + 2 + \cdots + (n-1) = \dfrac{n(n-1)}{2}$ multiplicações.
>
> **Passo 3 — contar a regressiva.** Na linha $i$ de $Ux = y$ (de baixo para cima) há uma divisão pelo pivô e uma multiplicação por cada $x$ já conhecido : $1 + 2 + \cdots + n = \dfrac{n(n+1)}{2}$ operações.
>
> **Passo 4 — somar.** $\dfrac{n(n-1)}{2} + \dfrac{n(n+1)}{2} = n^2$. Logo $O(n^2)$.
>
> O $O(n^3)$ de (d) é o custo da **fatoração**, que já foi paga — é essa a vantagem da LU.

**4.** Usando o sistema abaixo e a estimativa inicial $x = [1, 1, 1]$, mostre os valores obtidos depois de duas iterações do método de Gauss-Jacobi :
$$\begin{array}{rcrcrcr} +5x_1 & + & 1x_2 & - & 1x_3 & = & 5 \\ +1x_1 & - & 4x_2 & + & 2x_3 & = & -3 \\ +2x_1 & + & 1x_2 & + & 4x_3 & = & 12 \end{array}$$

> [!success]- **RESPOSTA**
> $[1{,}15;\ 2{,}125;\ 2{,}125]$
>
> **Passo 1 — isolar a variável da diagonal em cada linha.**
> $$x_1 = \frac{5 - x_2 + x_3}{5}, \qquad x_2 = \frac{-3 - x_1 - 2x_3}{-4}, \qquad x_3 = \frac{12 - 2x_1 - x_2}{4}$$
>
> **Passo 2 — iteração 1**, usando só o chute $[1, 1, 1]$ :
> - $x_1 = (5 - 1 + 1)/5 = 5/5 = 1$
> - $x_2 = (-3 - 1 - 2)/(-4) = -6/(-4) = 1{,}5$
> - $x_3 = (12 - 2 - 1)/4 = 9/4 = 2{,}25$
>
> **Passo 3 — iteração 2**, usando só $[1;\ 1{,}5;\ 2{,}25]$ :
> - $x_1 = (5 - 1{,}5 + 2{,}25)/5 = 5{,}75/5 = 1{,}15$
> - $x_2 = (-3 - 1 - 4{,}5)/(-4) = -8{,}5/(-4) = 2{,}125$
> - $x_3 = (12 - 2 - 1{,}5)/4 = 8{,}5/4 = 2{,}125$
>
> **Cuidado** : no Jacobi, as três contas de uma iteração usam **só** os valores da iteração anterior. Na iteração 2, o $x_2$ usa $x_1 = 1$, e não o $1{,}15$ recém-calculado — usar o valor novo seria Seidel.
>
> **Para conferir** : a solução exata é $[1, 2, 2]$ e a matriz é diagonalmente dominante ($5 > 2$, $4 > 3$, $4 > 3$), então a sequência converge para lá.

**5.** O padrão IEEE 754 guarda um `float` em sinal, expoente e mantissa. A partir disso analise as afirmativas abaixo :

1) $+0$ e $-0$ têm padrões de bits diferentes, mas são tratados como o mesmo zero ;
2) Um infinito tem o expoente todo ligado e a mantissa toda zerada ;
3) Um `float` armazena 24 bits de mantissa na memória ;
4) A expressão $0/0$ é avaliada como NaN ;
5) Os números subnormalizados também têm o bit `1` implícito na frente da mantissa ;

Em seguida assinale a opção correta :

- (a) São corretas as alternativas 1, 2 e 3.
- (b) São corretas as alternativas 1, 2 e 4.
- (c) São corretas as alternativas 2, 4 e 5.
- (d) São corretas as alternativas 1, 3 e 4.
- (e) São corretas as alternativas 1, 2, 4 e 5.

> [!success]- **RESPOSTA**
> São corretas as alternativas 1, 2 e 4 — opção **(b)**.
>
> **Passo 1 — julgar uma por uma.**
> - **1 — verdadeira.** O zero é "tudo zerado, com a talvez exceção do bit do sinal" (aula02) : $+0$ e $-0$ diferem nesse bit, mas o padrão os trata como iguais.
> - **2 — verdadeira.** É a definição do resumo da aula02 : expoente todo ligado, mantissa toda zerada.
> - **3 — falsa.** São **23** bits armazenados. A precisão é 24 porque o `1` da frente dos normalizados não precisa ser guardado : $1 + 8 + 23 = 32$.
> - **4 — verdadeira.** O JB conseguiu um `-NaN` dividindo $0/0$. (Já $1/0$ dá infinito — foi a afirmativa falsa da prova.)
> - **5 — falsa.** Subnormal é justamente o número **sem** o bit implícito : expoente zerado, mantissa não zerada (aula04).
>
> **Passo 2 — procurar a combinação.** Verdadeiras : 1, 2 e 4 → **(b)**. Dá para eliminar rápido : qualquer opção com 3 ou 5 cai fora, e só sobra (b).

**6.** Explique por que, "para o cara da computação", o método de Gauss-Jacobi pode ser preferível ao de Gauss-Seidel.

> [!success]- **RESPOSTA**
> Porque no Jacobi cada variável de uma iteração depende só dos valores da iteração anterior, e por isso todas podem ser calculadas **em paralelo** ; o Seidel usa cada valor novo imediatamente, o que obriga a calcular em série.
>
> **Como montar a resposta :**
> 1. Diga a diferença entre os dois : Jacobi usa só a iteração anterior ; Seidel usa o valor novo "o mais cedo possível".
> 2. Tire a consequência : no Seidel o $x_2$ precisa esperar o $x_1$ ficar pronto ; no Jacobi ninguém espera ninguém.
> 3. Conclua com a palavra que o JB quer ler : **paralelo**.
>
> A resposta da prova para a LU tinha uma frase só. Não escreva mais do que isso.

**7.** Usando o polinômio $p(x) = x^3 - 9x + 10$ para determinar $p(x) = 0$, usaremos o método de Newton iniciando com $x = 3$. Depois de fazermos a segunda iteração, teremos $x$ igual a :

- (a) 2.4444 ;
- (b) 2.0000 ;
- (c) 2.2500 ;
- (d) 2.0312 ;
- (e) Outra resposta : ________________

> [!success]- **RESPOSTA**
> Outra resposta : **2.1524512**
>
> **Passo 1 — derivar.** $p'(x) = 3x^2 - 9$.
>
> **Passo 2 — fórmula.** $x_{i+1} = x_i - \dfrac{p(x_i)}{p'(x_i)}$.
>
> **Passo 3 — primeira iteração**, com $x_0 = 3$ :
> - $p(3) = 27 - 27 + 10 = 10$
> - $p'(3) = 27 - 9 = 18$
> - $x_1 = 3 - \dfrac{10}{18} = 3 - 0{,}5556 = 2{,}4444$
>
> **Passo 4 — segunda iteração**, com $x_1 = 2{,}4444$ :
> - $x_1^2 = 5{,}9753$ e $x_1^3 = 14{,}6063$
> - $p(x_1) = 14{,}6063 - 22{,}0000 + 10 = 2{,}6063$
> - $p'(x_1) = 17{,}9259 - 9 = 8{,}9259$
> - $x_2 = 2{,}4444 - \dfrac{2{,}6063}{8{,}9259} = 2{,}4444 - 0{,}2920 = 2{,}1525$
>
> **Passo 5 — comparar com as alternativas.** Nenhuma bate : (a) é a armadilha de quem para na **primeira** iteração ; (b) é a raiz exata, que Newton ainda não alcançou. Marca-se (e) e escreve-se o valor.

---

## Simulado B

**1.** Encontre o polinômio de menor grau que passa pelos pontos $(2, 5)$, $(5, 11)$ e $(-1, -1)$.

> [!success]- **RESPOSTA**
> $$p(x) = 2x + 1$$
> ou equivalente.
>
> **Caminho curto — testar se é reta.**
> 1. Inclinação entre $(2, 5)$ e $(5, 11)$ : $\dfrac{11 - 5}{5 - 2} = 2$.
> 2. Inclinação entre $(-1, -1)$ e $(2, 5)$ : $\dfrac{5 - (-1)}{2 - (-1)} = 2$.
> 3. Inclinações iguais : os três pontos são **colineares**, e o menor grau é 1, não 2.
> 4. $p(x) = 2x + b$ passando por $(2, 5)$ : $4 + b = 5 \Rightarrow b = 1$.
> 5. Conferir no terceiro ponto : $p(-1) = -2 + 1 = -1$ ✓.
>
> **Caminho longo — sistema linear** (funciona sempre, colineares ou não). Com $p(x) = ax^2 + bx + c$ :
> $$\begin{cases} 4a + 2b + c = 5 \\ 25a + 5b + c = 11 \\ a - b + c = -1 \end{cases}$$
> 1. Segunda menos primeira : $21a + 3b = 6 \Rightarrow 7a + b = 2$.
> 2. Primeira menos terceira : $3a + 3b = 6 \Rightarrow a + b = 2$.
> 3. Subtraindo as duas : $6a = 0 \Rightarrow a = 0$. Então $b = 2$.
> 4. Na primeira : $0 + 4 + c = 5 \Rightarrow c = 1$.
>
> O $a = 0$ é o sistema avisando que o grau 2 não era necessário — a mesma pegadinha da prova.

**2.** Use a cota de Cauchy para determinar o raio do círculo, no plano complexo, que contém todas as raízes do polinômio $p(x)$ a seguir :
$$p(x) = 2x^4 - 6x^3 + x - 10$$

> [!success]- **RESPOSTA**
> Raio **6**.
>
> **Passo 1 — listar os coeficientes, sem esquecer os zeros.** $a_4 = 2$, $a_3 = -6$, $a_2 = 0$, $a_1 = 1$, $a_0 = -10$. O coeficiente da ponta é $a_m = 2$.
>
> **Passo 2 — dividir cada um pelo da ponta, em módulo.** O da ponta não entra na lista, só divide.
> $$\left|\tfrac{-10}{2}\right| = 5, \qquad \left|\tfrac{1}{2}\right| = 0{,}5, \qquad \left|\tfrac{0}{2}\right| = 0, \qquad \left|\tfrac{-6}{2}\right| = 3$$
>
> **Passo 3 — pegar o maior e somar 1.** $1 + \max\{5;\ 0{,}5;\ 0;\ 3\} = 1 + 5 = 6$.
>
> **Passo 4 — interpretar.** Todas as raízes, reais ou complexas, têm módulo menor ou igual a 6 : "não olha pra fora dessa caixinha".
>
> Por comparação, Lagrange dá $\max(1,\ 5 + 0{,}5 + 0 + 3) = 8{,}5$ — Cauchy é a mais apertada aqui. O erro clássico é esquecer de dividir por $a_m$ e responder $1 + 10 = 11$.

**3.** Você vai usar o método da bissecção no intervalo $[0, 8]$ e quer parar quando $a$ e $b$ estiverem a uma distância de no máximo $0{,}001$. O número de iterações necessárias é :

- (a) 10
- (b) 13
- (c) 20
- (d) 8000

> [!success]- **RESPOSTA**
> A resposta é **13** — opção **(b)**.
>
> **Passo 1 — o que cada iteração faz.** Troca $a$ ou $b$ pelo ponto médio : a largura do intervalo cai **pela metade**.
>
> **Passo 2 — largura depois de $n$ iterações.** Começa em $8 - 0 = 8$ ; depois de $n$ passos é $\dfrac{8}{2^n}$.
>
> **Passo 3 — impor a tolerância.** $\dfrac{8}{2^n} \le 0{,}001 \Rightarrow 2^n \ge 8000$.
>
> **Passo 4 — achar $n$.** $2^{10} = 1024$, $2^{11} = 2048$, $2^{12} = 4096$ (ainda não), $2^{13} = 8192 \ge 8000$ ✓. Logo $n = 13$.
>
> Dá para saber isso **antes** de rodar e sem olhar para a função. (a) é o chute "$2^{10} \approx 1000$", que esquece que a largura inicial é 8 e não 1 ; (d) é quem dividiu em vez de tirar o logaritmo.

**4.** Usando o sistema abaixo e a estimativa inicial $x = [0, 0, 0]$, mostre os valores obtidos depois de duas iterações do método de Gauss-Seidel :
$$\begin{array}{rcrcrcr} +4x_1 & - & 1x_2 & + & 1x_3 & = & 9 \\ +2x_1 & + & 5x_2 & - & 1x_3 & = & 3 \\ +1x_1 & + & 2x_2 & - & 4x_3 & = & -6 \end{array}$$

> [!success]- **RESPOSTA**
> $[1{,}696875;\ 0{,}30375;\ 2{,}07609375]$, ou aproximadamente $[1{,}70;\ 0{,}30;\ 2{,}08]$.
>
> **Passo 1 — isolar a variável da diagonal em cada linha.**
> $$x_1 = \frac{9 + x_2 - x_3}{4}, \qquad x_2 = \frac{3 - 2x_1 + x_3}{5}, \qquad x_3 = \frac{-6 - x_1 - 2x_2}{-4}$$
>
> **Passo 2 — iteração 1.** Cada valor novo entra **na conta seguinte**.
> - $x_1 = (9 + 0 - 0)/4 = 2{,}25$
> - $x_2 = (3 - 2 \cdot \mathbf{2{,}25} + 0)/5 = -1{,}5/5 = -0{,}3$ — já com o $x_1$ novo
> - $x_3 = (-6 - \mathbf{2{,}25} - 2 \cdot (\mathbf{-0{,}3}))/(-4) = -7{,}65/(-4) = 1{,}9125$ — com $x_1$ e $x_2$ novos
>
> **Passo 3 — iteração 2.**
> - $x_1 = (9 + (-0{,}3) - 1{,}9125)/4 = 6{,}7875/4 = 1{,}696875$
> - $x_2 = (3 - 2 \cdot 1{,}696875 + 1{,}9125)/5 = 1{,}51875/5 = 0{,}30375$
> - $x_3 = (-6 - 1{,}696875 - 2 \cdot 0{,}30375)/(-4) = -8{,}304375/(-4) = 2{,}07609375$
>
> **Comparação** : com Jacobi a iteração 1 seria $[2{,}25;\ 0{,}6;\ 1{,}5]$, porque $x_2$ e $x_3$ usariam $x_1 = 0$. A solução exata é $[1{,}8;\ 0{,}3;\ 2{,}1]$, e a matriz é diagonalmente dominante ($4 > 2$, $5 > 3$, $4 > 3$).

**5.** O padrão IEEE 754 define exceções e modos de arredondamento. A partir disso analise as afirmativas abaixo :

1) O laço `Enquanto 1.0 + EPS > 1.0 : EPS = EPS / 2` roda para sempre, porque `EPS` nunca chega a zero ;
2) Existem 4 modos de arredondamento : para o zero, para $+\infty$, para $-\infty$ e para o número mais próximo ;
3) Uma conta que estoura o maior número representável responde infinito e liga o bit de overflow ;
4) Antes de usar o expoente armazenado de um `float`, soma-se 127 a ele ;
5) Um número com o expoente todo zerado e a mantissa não zerada é subnormalizado ;

Em seguida assinale a opção correta :

- (a) São corretas as alternativas 1, 2 e 3.
- (b) São corretas as alternativas 2, 4 e 5.
- (c) São corretas as alternativas 2, 3 e 5.
- (d) São corretas as alternativas 1, 3 e 5.
- (e) São corretas as alternativas 2, 3, 4 e 5.

> [!success]- **RESPOSTA**
> São corretas as alternativas 2, 3 e 5 — opção **(c)**.
>
> **Passo 1 — julgar uma por uma.**
> - **1 — falsa.** O laço para, e muito antes de `EPS` zerar. Quando `EPS` fica menor que metade do espaçamento dos floats perto de 1, a soma `1.0 + EPS` **arredonda para 1.0** e a condição falha. É assim que se mede o epsilon de máquina (aula04).
> - **2 — verdadeira.** São os quatro arredondamentos listados na aula04.
> - **3 — verdadeira.** "Overflow — responde infinito, e liga o bit de overflow."
> - **4 — falsa.** É o contrário : "antes de usar, **tire** 127 ; quando guardar, adicione 127" (aula02).
> - **5 — verdadeira.** Expoente zerado com mantissa zerada é zero ; com mantissa não zerada é subnormalizado.
>
> **Passo 2 — procurar a combinação.** Verdadeiras : 2, 3 e 5 → **(c)**. Qualquer opção com 1 ou 4 cai fora, e só sobra (c).

**6.** Explique o que o método de Aberth acrescenta à ideia de soltar vários "newtonzinhos" ao mesmo tempo para achar todas as raízes de um polinômio.

> [!success]- **RESPOSTA**
> Uma **repulsão** entre as aproximações (como cargas elétricas de mesmo sinal), para que dois newtons não caiam na mesma raiz e todas as raízes sejam encontradas.
>
> **Como montar a resposta :**
> 1. Diga o defeito da ideia original : vários Newtons independentes podem encontrar a **mesma** raiz várias vezes e deixar outras de fora.
> 2. Diga o que Aberth muda : cada aproximação é empurrada para longe das outras — os "repulsores de newtons" da aula10.
> 3. Conclua : assim cada aproximação vai para uma raiz diferente, e saem todas de uma vez. (Só funciona para polinômios, porque é preciso saber quantas raízes existem.)

**7.** Usando a função $f(x) = x^3 - x - 2$ para determinar $f(x) = 0$, usaremos o método da secante iniciando com $x_0 = 1$ e $x_1 = 2$. Depois de fazermos a segunda iteração, teremos $x$ igual a :

- (a) 1.3333 ;
- (b) 1.5000 ;
- (c) 1.4627 ;
- (d) 1.5214 ;
- (e) Outra resposta : ________________

> [!success]- **RESPOSTA**
> **(c)** 1.4627
>
> **Passo 1 — fórmula.** A reta que liga os dois últimos pontos corta o eixo em
> $$x_{n+1} = x_n - f(x_n)\,\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$$
>
> **Passo 2 — avaliar nos pontos iniciais.** $f(1) = 1 - 1 - 2 = -2$ e $f(2) = 8 - 2 - 2 = 4$.
>
> **Passo 3 — primeira iteração**, com $x_0 = 1$ e $x_1 = 2$ :
> $$x_2 = 2 - 4 \cdot \frac{2 - 1}{4 - (-2)} = 2 - \frac{4}{6} = 1{,}3333$$
>
> **Passo 4 — avaliar no ponto novo.** $f(1{,}3333) = 2{,}3704 - 1{,}3333 - 2 = -0{,}9630$.
>
> **Passo 5 — segunda iteração**, com $x_1 = 2$ e $x_2 = 1{,}3333$ (o ponto mais antigo, $x_0$, é descartado) :
> $$x_3 = 1{,}3333 - (-0{,}9630) \cdot \frac{1{,}3333 - 2}{-0{,}9630 - 4} = 1{,}3333 + 0{,}9630 \cdot \frac{-0{,}6667}{-4{,}9630} = 1{,}3333 + 0{,}1294 = 1{,}4627$$
>
> **Passo 6 — comparar com as alternativas.** (a) é a primeira iteração ; (b) é o primeiro passo da **bissecção** em $[1, 2]$ ; (d) é a raiz exata.

---

## Simulado C

**1.** Encontre a reta $F(x) = ax + b$ que melhor se ajusta, por mínimos quadrados, aos pontos $(1, 1)$, $(2, 2)$, $(3, 2)$, $(4, 5)$ e $(5, 5)$.

> [!success]- **RESPOSTA**
> $$F(x) = 1{,}1x - 0{,}3$$
> ou equivalente.
>
> **Passo 1 — equações normais da reta** (as mesmas do Simulado A, questão 1) :
> $$\begin{cases} a \sum x_i^2 + b \sum x_i = \sum x_i y_i \\ a \sum x_i + b \cdot n = \sum y_i \end{cases}$$
>
> **Passo 2 — tabela das somas.**
>
> | $x$ | $y$ | $x^2$ | $xy$ |
> |---|---|---|---|
> | 1 | 1 | 1 | 1 |
> | 2 | 2 | 4 | 4 |
> | 3 | 2 | 9 | 6 |
> | 4 | 5 | 16 | 20 |
> | 5 | 5 | 25 | 25 |
> | **15** | **15** | **55** | **56** |
>
> **Passo 3 — montar o sistema**, com $n = 5$ :
> $$\begin{cases} 55a + 15b = 56 \\ 15a + 5b = 15 \end{cases}$$
>
> **Passo 4 — resolver.** Da segunda : $5b = 15 - 15a \Rightarrow b = 3 - 3a$. Substituindo na primeira : $55a + 15(3 - 3a) = 56 \Rightarrow 55a + 45 - 45a = 56 \Rightarrow 10a = 11 \Rightarrow a = 1{,}1$. Então $b = 3 - 3{,}3 = -0{,}3$.
>
> **Passo 5 — conferir.** $F$ nos cinco pontos dá $0{,}8;\ 1{,}9;\ 3{,}0;\ 4{,}1;\ 5{,}2$. Os resíduos são $-0{,}2;\ -0{,}1;\ +1{,}0;\ -0{,}9;\ +0{,}2$ e somam zero ✓.

**2.** Escreva o polinômio $p(x)$ a seguir na forma de Horner e use-a para calcular $p(2)$ :
$$p(x) = x^5 + 12x^4 - 6x^3 + 11x - 16$$

> [!success]- **RESPOSTA**
> $p(x) = -16 + x\,(11 + x\,(0 + x\,(-6 + x\,(12 + x))))$ e $p(2) = 182$.
>
> **Passo 1 — listar todos os coeficientes, do maior grau para o menor, com os zeros.** $1,\ 12,\ -6,\ \mathbf{0},\ 11,\ -16$. O $0$ é o coeficiente de $x^2$, que não aparece no polinômio mas **não pode ser pulado**.
>
> **Passo 2 — escrever a forma de Horner**, de trás para frente : começa no termo constante e vai abrindo parênteses, cada um com o próximo coeficiente.
> $$-16 + x\,(11 + x\,(0 + x\,(-6 + x\,(12 + x))))$$
>
> **Passo 3 — avaliar de dentro para fora.** A regra é sempre "multiplica por $x$, soma o próximo coeficiente", começando do coeficiente da ponta :
>
> | Coeficiente | Conta | Resultado |
> |---|---|---|
> | $1$ | — | $1$ |
> | $12$ | $1 \cdot 2 + 12$ | $14$ |
> | $-6$ | $14 \cdot 2 - 6$ | $22$ |
> | $0$ | $22 \cdot 2 + 0$ | $44$ |
> | $11$ | $44 \cdot 2 + 11$ | $99$ |
> | $-16$ | $99 \cdot 2 - 16$ | $\mathbf{182}$ |
>
> **Passo 4 — conferir pelo jeito ruim.** $32 + 192 - 48 + 22 - 16 = 182$ ✓. Horner fez 5 multiplicações, uma por grau, e nenhuma chamada a `pow()`.

**3.** Você recebeu um sistema $Ax = b$ com $n$ equações e vai fatorar a matriz $A$ em $L \cdot U$. O custo (em multiplicações e divisões) dessa fatoração é :

- (a) $O(n^2)$
- (b) $O(n^2 \log(n))$
- (c) $O(n^3)$
- (d) $O(2^n)$

> [!success]- **RESPOSTA**
> A resposta é $O(n^3)$ — opção **(c)**.
>
> **Passo 1 — o que é fatorar.** É fazer a eliminação de Gauss guardando os multiplicadores (os *aux's* da [aula17](../aula17.md)) em $L$ ; o que sobra da eliminação é a $U$.
>
> **Passo 2 — contar um pivô.** No pivô $k$ há $n - k$ linhas abaixo dele. Para cada uma : 1 divisão (o *aux*) e $n - k$ multiplicações (uma por coluna que resta). São cerca de $(n - k)^2$ operações.
>
> **Passo 3 — somar todos os pivôs.** $\sum_{k=1}^{n-1} (n-k)^2 = 1^2 + 2^2 + \cdots + (n-1)^2 \approx \dfrac{n^3}{3}$.
>
> **Passo 4 — concluir.** Três laços aninhados (pivô, linha, coluna) : $O(n^3)$.
>
> Compare com o Simulado A, questão 3 : depois da fatoração, cada $b$ custa só $O(n^2)$.

**4.** A matriz $A$ de um sistema $Ax = b$ já foi decomposta em $L \cdot U$, com
$$L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{pmatrix}, \qquad U = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}, \qquad b = \begin{pmatrix} 3 \\ 7 \\ 21 \end{pmatrix}$$
Mostre o vetor $y$ obtido na substituição progressiva e a solução $x$ do sistema.

> [!success]- **RESPOSTA**
> $y = [3, 1, 6]$ e $x = [1, -2, 3]$.
>
> **Passo 1 — o plano.** $Ax = b$ vira $L(Ux) = b$. Chamando $Ux = y$ : primeiro resolve-se $Ly = b$, depois $Ux = y$.
>
> **Passo 2 — substituição progressiva**, $Ly = b$, de **cima para baixo** :
> $$\begin{cases} 1y_1 = 3 \\ 2y_1 + 1y_2 = 7 \\ 4y_1 + 3y_2 + 1y_3 = 21 \end{cases}$$
> - $y_1 = 3$
> - $y_2 = 7 - 2 \cdot 3 = 1$
> - $y_3 = 21 - 4 \cdot 3 - 3 \cdot 1 = 21 - 12 - 3 = 6$
>
> **Passo 3 — substituição regressiva**, $Ux = y$, de **baixo para cima** :
> $$\begin{cases} 2x_1 + 1x_2 + 1x_3 = 3 \\ 1x_2 + 1x_3 = 1 \\ 2x_3 = 6 \end{cases}$$
> - $x_3 = 6/2 = 3$
> - $x_2 = 1 - 3 = -2$
> - $x_1 = (3 - (-2) - 3)/2 = 2/2 = 1$
>
> **Passo 4 — conferir em $A = LU$.** A primeira linha de $A$ é a primeira de $U$ : $2 \cdot 1 + 1 \cdot (-2) + 1 \cdot 3 = 3$ ✓. A segunda é $2 \cdot (2, 1, 1) + (0, 1, 1) = (4, 3, 3)$ : $4 - 6 + 9 = 7$ ✓. A terceira é $(8, 7, 9)$ : $8 - 14 + 27 = 21$ ✓.

**5.** Os métodos de solução de equações procuram raízes de uma função $f(x)$. A partir disso analise as afirmativas abaixo :

1) A bissecção fica presa ao intervalo inicial e devolve uma única raiz, mesmo que existam outras ;
2) O método da secante tem ordem de convergência de aproximadamente 1,618 ;
3) O método de Newton precisa de dois pontos iniciais e dispensa o cálculo de derivadas ;
4) O método de Newton pode ser usado para encontrar raízes complexas ;
5) Um polinômio de grau 5 com coeficientes reais pode ter todas as suas 5 raízes complexas, sem nenhuma real ;

Em seguida assinale a opção correta :

- (a) São corretas as alternativas 1, 2 e 3.
- (b) São corretas as alternativas 1, 3 e 5.
- (c) São corretas as alternativas 2, 4 e 5.
- (d) São corretas as alternativas 1, 2 e 4.
- (e) São corretas as alternativas 1, 2, 4 e 5.

> [!success]- **RESPOSTA**
> São corretas as alternativas 1, 2 e 4 — opção **(d)**.
>
> **Passo 1 — julgar uma por uma.**
> - **1 — verdadeira.** "Método limitado ao intervalo que tu deu ao início" e "só encontra uma única raiz, por mais que tenha milhões" (aulas 06 e 09).
> - **2 — verdadeira.** É o expoente da razão áurea (aula09).
> - **3 — falsa.** Quem usa dois pontos e não deriva é a **secante**. Newton parte de um ponto só e precisa de $f'$ — "o que incomoda é o cálculo de derivadas".
> - **4 — verdadeira.** A aula09 lista como vantagem : "vai atrás de raiz complexa".
> - **5 — falsa.** Grau ímpar vem do $-\infty$ e vai para o $+\infty$, e o polinômio é contínuo : é obrigado a cruzar o eixo pelo menos uma vez (aula05). Dito de outro jeito : com coeficientes reais as complexas vêm em pares, e 5 é ímpar.
>
> **Passo 2 — procurar a combinação.** Verdadeiras : 1, 2 e 4 → **(d)**. Qualquer opção com 3 ou 5 cai fora, e só sobra (d).

**6.** Explique o que significa uma matriz ser diagonalmente dominante e o que isso garante para os métodos de Gauss-Jacobi e Gauss-Seidel.

> [!success]- **RESPOSTA**
> Em cada linha, o módulo do elemento da diagonal é maior que a soma dos módulos dos outros elementos da linha ; isso **garante que os métodos convergem**, para qualquer chute inicial.
>
> **Como montar a resposta :**
> 1. Defina, linha por linha : $|a_{ii}| > \sum_{j \ne i} |a_{ij}|$. Um exemplo ajuda : na linha $5x_1 + x_2 - x_3$, $5 > 1 + 1$.
> 2. Diga o que se ganha : os chutes sucessivos "vão para um lugar e ficam quietos" em vez de "ir para o infinito" (aula14).
>
> Detalhe que vale ponto extra : é condição **suficiente**, não necessária. O sistema da [aula14](../aula14-2.md) não é dominante e o Jacobi convergiu mesmo assim.

**7.** Usando o polinômio $p(x) = x^3 - 2x - 5$ para determinar $p(x) = 0$, usaremos o método de Newton iniciando com $x = 2$. Depois de fazermos a segunda iteração, teremos $x$ igual a :

- (a) 2.1000 ;
- (b) 2.0946 ;
- (c) 2.0500 ;
- (d) 2.1250 ;
- (e) Outra resposta : ________________

> [!success]- **RESPOSTA**
> **(b)** 2.0946
>
> **Passo 1 — derivar.** $p'(x) = 3x^2 - 2$.
>
> **Passo 2 — fórmula.** $x_{i+1} = x_i - \dfrac{p(x_i)}{p'(x_i)}$.
>
> **Passo 3 — primeira iteração**, com $x_0 = 2$ :
> - $p(2) = 8 - 4 - 5 = -1$
> - $p'(2) = 12 - 2 = 10$
> - $x_1 = 2 - \dfrac{-1}{10} = 2 + 0{,}1 = 2{,}1$
>
> **Passo 4 — segunda iteração**, com $x_1 = 2{,}1$ :
> - $x_1^2 = 4{,}41$ e $x_1^3 = 9{,}261$
> - $p(2{,}1) = 9{,}261 - 4{,}2 - 5 = 0{,}061$
> - $p'(2{,}1) = 13{,}23 - 2 = 11{,}23$
> - $x_2 = 2{,}1 - \dfrac{0{,}061}{11{,}23} = 2{,}1 - 0{,}005432 = 2{,}094568$
>
> **Passo 5 — comparar com as alternativas.** Desta vez a resposta **está** entre elas : (b). "Outra resposta" não é sempre o gabarito. (a) é a primeira iteração ; cuidado com o sinal em $-\frac{-1}{10}$, que **soma**.

---

### Ver também
- [Lista de Exercícios 2026/2](./lista-2.md) — a lista longa, com casos reais e gabarito comentado.
- [Dicionário de conceitos — 2026/2](../IA/dicionario-2.md)
- [Material complementar — 2026/2](../IA/adicoes-2.md)
