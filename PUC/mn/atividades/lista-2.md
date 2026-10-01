# Métodos Numéricos — Lista de Exercícios 2026/2
## [30-09-26][mvfm]
---
### Prefácio
- Lista montada sobre as aulas **2026/2** — [aula02-2](../aula02-2.md) a [aula16-2](../aula16-2.md) — e o aprofundamento de [IA/adicoes-2.md](../IA/adicoes-2.md). Os termos em negrito estão todos no [dicionário](../IA/dicionario-2.md).
- Incorpora os exercícios das folhas do professor : a [lista geral](./lista.pdf) e os [ExLab 1](./exlab1.pdf) e [ExLab 2](./exlab2.pdf). Cada item que veio de uma folha leva a origem entre parênteses — *(Lista · PF 2)* é o exercício 2 de "Sistemas de ponto flutuante" da lista geral ; *(ExLab 1 · 7)* é o 7 do ExLab 1. A lista geral vai além da aula16 (Markov, interpolação, diferenciação automática, sistemas dinâmicos) ; esses blocos **ficaram de fora**, porque a matéria de 2026/2 ainda não chegou neles.
- **Estrutura** : objetivas espalhadas pelo conteúdo + 5 questões de cálculo, uma por bloco da matéria :
	- **IEEE 754** (aulas 02 e 04) · **Polinômios** (05 e 06) · **Solução de equações** (06, 09 e 10) · **Sistemas lineares** (14 e 15) · **Mínimos quadrados** (16).
	- Cada questão de cálculo é ancorada num **caso real** — a Bolsa de Vancouver, o *Quake III*, o sistema em que o Seidel perdeu para o Jacobi na aula14, e a redescoberta de Ceres por Gauss. O caso só obriga a aplicar o conceito em vez de recitá-lo.
	- A **Questão 2** (polinômios) não tem caso : é o pipeline completo de achar raízes, do grau à deflação, num polinômio só.
- A **Parte III** é o laboratório : três questões feitas dos exercícios das folhas que não cabiam nas questões da Parte II — **cancelamento catastrófico**, o **polinômio do JB** do começo ao fim, e **modelagem** com sistemas lineares. São pensadas para resolver com um programa ao lado ; o gabarito traz os números para conferir.
- A **Parte IV** é bônus : três desastres históricos de ponto flutuante, para treinar diagnóstico.
- Todas as contas foram conferidas numericamente. Onde o valor é aproximado, o gabarito diz.
- Gabarito comentado no fim, dentro de blocos recolhíveis. Resolva antes de abrir.
- Tempo sugerido : **50 minutos** para a Parte I ; **2h30** para a Parte II, que é quase toda de conta ; **2 horas** para a Parte III, com computador.

---

## Parte I — Objetivas
> 20 questões. Marque **uma** alternativa. As questões 17 a 20 vêm dos exercícios das folhas de laboratório.

**1.** As notas da aula02 dividem o `float` em "1 de sinal, 8 de expoente, 24 de mantissa", o que soma 33 bits num tipo de 32. A explicação é :
- a) O IEEE 754 usa 33 bits internamente e descarta um ao armazenar.
- b) O bit de sinal é compartilhado com o expoente.
- c) A mantissa **armazena** 23 bits ; a **precisão** $p$ é 24 porque o `1` da frente dos números normalizados é **implícito** e não ocupa memória.
- d) O expoente tem só 7 bits efetivos, porque o oitavo guarda o sinal do expoente.
- e) O 24º bit é o bit de guarda usado nos arredondamentos.

**2.** O padrão de bits `0x7F800000` num `float` representa :
- a) O maior número finito representável.
- b) Um NaN silencioso.
- c) $+\infty$ — expoente todo ligado, mantissa toda zerada, sinal 0.
- d) O menor subnormal positivo.
- e) $-0$.

**3.** Para uma variável `double x`, a expressão `x != x` é verdadeira :
- a) Nunca, porque a igualdade é reflexiva.
- b) Somente quando `x` é $\pm\infty$.
- c) Somente quando `x` é **NaN**.
- d) Somente quando `x` é subnormal.
- e) Quando `x` é $-0$, pois $-0 \ne +0$ em bits.

**4.** O expoente é armazenado com **bias** (soma-se 127 ao guardar) em vez de em complemento de dois. O motivo principal é :
- a) Economizar um bit de expoente.
- b) Permitir expoentes maiores que 127.
- c) Fazer o padrão de bits crescer junto com o número, de modo que floats positivos se comparem como **inteiros sem sinal** — a "ordenação por string" da aula02.
- d) Evitar o *double rounding* dos registradores de 80 bits.
- e) Tornar a divisão por 2 uma operação só de mantissa.

**5.** No modo padrão do IEEE 754, $2{,}5$ arredonda para $2$ e $3{,}5$ para $4$. A regra existe porque :
- a) É mais barata em hardware que "meio arredonda para cima".
- b) Evita **viés** : metade dos empates sobe e metade desce, então o erro de somas longas cresce como $\sqrt{n}$ em vez de $n$.
- c) Números pares têm representação exata em binário e ímpares não.
- d) É exigida pela aritmética intervalar.
- e) Garante que o resultado nunca seja subnormal.

**6.** A propriedade garantida pela existência dos **subnormais** (underflow gradual) é :
- a) $x \cdot 1 = x$ para todo $x$.
- b) $x - y = 0 \iff x = y$.
- c) Nenhuma conta produz $\pm\infty$.
- d) O epsilon de máquina fica menor.
- e) A soma passa a ser associativa.

**7.** Sobre o **epsilon de máquina** do `float`, $\varepsilon = 2^{-23} \approx 1{,}19 \times 10^{-7}$ :
- a) É o menor `float` positivo.
- b) É o menor `float` normal positivo.
- c) É a distância de $1$ até o próximo `float` — uma medida de **precisão relativa**, não de magnitude.
- d) É o erro máximo de qualquer operação, em valor absoluto.
- e) Vale o mesmo para `float` e `double`.

**8.** Pela regra de Descartes, $p(x)$ tem 4 trocas de sinal. As raízes positivas são 4, 2 ou 0 — caem **de 2 em 2** porque :
- a) Todo polinômio de grau par tem um número par de raízes reais.
- b) Com coeficientes **reais**, raízes complexas aparecem em **pares conjugados** ; raízes reais só podem sair do eixo real aos pares.
- c) Descartes conta cada raiz duas vezes.
- d) As raízes positivas e negativas se anulam aos pares.
- e) É uma convenção, sem justificativa matemática.

**9.** O teorema de **Abel–Ruffini** (a "não existe fórmula para grau 5" da aula05) afirma que :
- a) Polinômios de grau $\ge 5$ não têm raízes complexas.
- b) Nenhuma quíntica pode ser resolvida exatamente.
- c) Não existe fórmula **geral** que expresse as raízes de todo polinômio de grau $\ge 5$ **por radicais** ($+, -, \times, \div, \sqrt[n]{\ }$) — as raízes existem, só não se escrevem assim.
- d) Métodos iterativos não convergem para grau $\ge 5$.
- e) As fórmulas de grau 3 e 4 são numericamente estáveis.

**10.** Avaliar um polinômio geral de grau $n$ pela **forma de Horner** custa :
- a) $n$ chamadas a `pow` e $n$ somas.
- b) $n(n+1)/2$ multiplicações e $n$ somas.
- c) $2n$ multiplicações e $n$ somas.
- d) $n$ multiplicações e $n$ somas — e está provado que não dá para fazer com menos.
- e) $\log_2 n$ multiplicações.

**11.** Bisecção em $[0, 1]$ com tolerância $10^{-6}$ no tamanho do intervalo. O número de iterações :
- a) Depende da função e não pode ser previsto.
- b) É **20**, sabido antes de rodar : $n \ge \log_2(1/10^{-6}) \approx 19{,}93$.
- c) É 6, uma iteração por casa decimal.
- d) É 10, porque a bisecção dobra os dígitos corretos por iteração.
- e) É 1.000.000.

**12.** Newton aplicado a $f(x) = (x-1)^2$, que tem raiz **dupla** em $x = 1$ :
- a) Converge quadraticamente, como sempre.
- b) Diverge, porque $f'(1) = 0$.
- c) Converge **linearmente**, com o erro caindo pela metade a cada passo ; o Newton modificado, $x_{n+1} = x_n - 2\,f(x_n)/f'(x_n)$, recupera a ordem 2.
- d) Converge em um passo a partir de qualquer chute.
- e) Entra em ciclo entre dois pontos.

**13.** Newton tem ordem 2 e a secante tem ordem $\varphi \approx 1{,}618$. Quando avaliar $f'$ custa o mesmo que avaliar $f$ :
- a) Newton é sempre mais eficiente, porque sua ordem é maior.
- b) A **secante** é mais eficiente : faz uma avaliação por iteração contra duas de Newton, e seu índice de eficiência $1{,}618$ supera o $\sqrt{2} \approx 1{,}414$ de Newton.
- c) Os dois são equivalentes.
- d) A bisecção supera os dois.
- e) A secante não converge sem derivada.

**14.** Sobre **Gauss-Jacobi** e **Gauss-Seidel** :
- a) Seidel sempre converge em menos iterações que Jacobi.
- b) Jacobi usa cada valor novo assim que ele é calculado.
- c) Jacobi calcula todas as variáveis de uma iteração só com valores da iteração anterior, e por isso **paraleliza** ; Seidel usa o valor novo imediatamente, o que cria dependência em série.
- d) Os dois exigem inverter a matriz $A$.
- e) Dominância diagonal é **necessária** para que qualquer um deles convirja.

**15.** A vantagem da **decomposição LU** sobre repetir a eliminação de Gauss é :
- a) Ela funciona para matrizes singulares.
- b) Ela dispensa a substituição regressiva.
- c) A fatoração, cara ($\sim\tfrac23 n^3$), é feita **uma vez** ; cada novo vetor $b$ custa só duas substituições triangulares ($\sim 2n^2$).
- d) Ela sempre é mais precisa numericamente.
- e) Ela transforma o sistema num problema iterativo.

**16.** No método dos mínimos quadrados, qual dos modelos leva a um **sistema linear** nas incógnitas?
- a) $F(x) = a\,e^{bx}$
- b) $F(x) = \sin(ax + b)$
- c) $F(x) = a x^2 + b x + c + d\cos(x)$ — é **linear nos parâmetros**, ainda que não seja linear em $x$.
- d) $F(x) = a / (x + b)$
- e) Nenhum : mínimos quadrados sempre gera sistema não linear.

**17.** *(Lista · RE 1)* Em `double`, `sqrt(x*x + 1) - 1` dá exatamente `0` para $x = 10^{-8}$, enquanto `x*x / (sqrt(x*x + 1) + 1)` dá $5 \times 10^{-17}$. As duas expressões são algebricamente iguais. O que aconteceu?
- a) A função `sqrt` tem um bug perto de 1.
- b) $x^2 = 10^{-16}$ é subnormal em `double`, e foi zerado.
- c) $x^2 + 1$ arredonda para exatamente $1$, porque $10^{-16}$ é menor que meio $\varepsilon$ ; a subtração de dois números quase iguais expõe esse erro — **cancelamento catastrófico**. A segunda forma não subtrai nada e por isso não sofre.
- d) A segunda forma está errada e dá um valor espúrio.
- e) A divisão da segunda forma introduz um erro que por acaso compensa o da raiz.

**18.** *(Lista · RE 3 ; ExLab 1 · 5)* O **método de Heron** para $\sqrt{p}$, $x_{n+1} = \frac12\left(x_n + \frac{p}{x_n}\right)$, é :
- a) Uma variante da bisecção com ponto médio ponderado.
- b) O método de **Newton** aplicado a $f(x) = x^2 - p$.
- c) O método da secante aplicado a $f(x) = \sqrt{x} - p$.
- d) Uma série de Taylor de $\sqrt{x}$ truncada no termo linear.
- e) Um método de ordem 1, que ganha uma casa por iteração.

**19.** *(Lista · RE 5 ; ExLab 1 · 4)* O polinômio $p(x) = (x-2)(x-3)(x-4)(x-5)$ tem $p(1) = 24$ e $p(6) = 24$. Sobre a bisecção em $[1, 6]$ :
- a) Ela prova que $p$ não tem raiz em $[1, 6]$.
- b) Ela converge para a raiz mais próxima do ponto médio.
- c) Ela converge para $x = 3{,}5$, o ponto de mínimo.
- d) Ela **não pode começar** : com $p(1)\,p(6) > 0$, Bolzano não garante nada — pode haver zero raízes ou um número **par** delas. É preciso subdividir o intervalo até achar trocas de sinal.
- e) Ela funciona se a tolerância for pequena o bastante.

**20.** *(Lista · RE 2)* Um programa só consegue plotar em $[-1, 1]$. Plotando $x^4 f(1/x)$ para um polinômio $f$ de grau 4 :
- a) Aparecem as mesmas raízes de $f$, só que comprimidas.
- b) Aparecem as raízes de $f$ multiplicadas por $-1$.
- c) Cada raiz $r \ne 0$ de $f$ vira uma raiz $1/r$ ; as raízes de $f$ com $|r| > 1$, invisíveis na janela, aparecem **dentro** dela. E $x^4 f(1/x)$ é só $f$ com os coeficientes em **ordem inversa**.
- d) Aparecem as raízes da derivada de $f$.
- e) Nada muda, porque $f(1/x)$ não é polinômio.

---

## Parte II — Exercícios
> 5 questões de cálculo. Mostre as contas intermediárias.

### Questão 1 — Caso Bolsa de Vancouver : representação e arredondamento
> Em janeiro de 1982 a Bolsa de Valores de Vancouver lançou um índice com valor inicial **1000,000**. Ele era recalculado a cada negociação — cerca de 3 mil vezes por dia — e o resultado era **truncado** para três casas decimais. Em novembro de 1983 o índice marcava **524,811**. Recalculado corretamente, o valor era **1098,892**.

**a)** *Decodificação.* Converta para decimal os floats `0xC1480000` e `0x3F400000`. Depois, codifique $-6{,}25$ em hexadecimal. Mostre sinal, expoente armazenado, expoente real e mantissa.

**b)** Classifique cada padrão de `float` abaixo (zero, infinito, NaN, normal, subnormal) e dê o valor quando houver :

```
0x00000000   0x80000000   0x7F800000   0xFFC00000   0x00800000   0x00000001
```

**c)** O índice de Vancouver foi recalculado da ordem de **1,4 milhão** de vezes em 22 meses. Truncar é o modo `roundTowardZero` do IEEE 754. Explique por que esse modo perde, em média, **0,0005 ponto por operação**, e estime a ordem de grandeza da perda acumulada. Compare com o que aconteceria em `roundTiesToEven`.

**d)** *O laço do epsilon.* *(Lista · PF 1 ; ExLab 1 · 1)* Quantas vezes o laço abaixo imprime `"Oi!"` com `EPS` do tipo `float`? E com `double`? Qual é o último valor impresso em cada caso, e que nome ele tem?

```
EPS = 1.0
Enquanto 1.0 + EPS > 1.0 :
    print("Oi!")
    EPS = EPS / 2
```

**e)** *Intervalos.* A aula04 justificou os arredondamentos direcionados pela aritmética intervalar, com a regra "menor com menor dá o menor, maior com maior dá o maior". Calcule $[-2, 3] \cdot [1, 4]$ e mostre que a regra, aplicada literalmente, **erra**. Qual é a regra correta, e onde entram os modos para $-\infty$ e $+\infty$?

**f)** *O calculeitor.* *(Lista · PF 2)* Um programa lê `val1 op val2` em `float`, **limpa** o registrador de exceções, faz a conta e mostra o resultado, os bits e as flags `FE_INEXACT`, `FE_DIVBYZERO`, `FE_UNDERFLOW`, `FE_OVERFLOW` e `FE_INVALID`. O exemplo do enunciado :
```
> calculeitor 21 / -0
val1 = 0 10000011 01010000000000000000000 = 21
val2 = 1 00000000 00000000000000000000000 = -0
res  = 1 11111111 00000000000000000000000 = -inf
FE_DIVBYZERO: 1   (as outras : 0)
```
Preveja resultado e flags levantadas para cada operação abaixo, e dê o padrão de bits de `1e-40` como `float`. Depois explique : por que o enunciado manda **ler o registrador de status** em vez de prever as exceções no próprio código? E por que as flags têm de ser limpas **depois** de ler as entradas, e não antes?

```
0/0      1e35 * 1e35      1/inf      0 * inf      1e-40 / 1e-40      1e-30 * 1e-30      1/3
```

---

### Questão 2 — O pipeline das raízes, do grau à deflação
> Seja $p(x) = x^4 - 2x^3 - 7x^2 + 8x + 12$. Siga as etapas na ordem da aula08 : **quantas** raízes, **de que sinal**, **onde**, **refinar**, **deflacionar**.

**a)** Aplique a regra de Descartes a $p(x)$ e a $p(-x)$. O que se pode afirmar sobre o número de raízes positivas, negativas e complexas?

**b)** Calcule as cotas de **Cauchy**, $1 + \max_i |a_i / a_m|$, e de **Lagrange**, $\max\left(1, \sum_i |a_i / a_m|\right)$. Qual é mais apertada? O que as cotas garantem sobre as raízes complexas?

**c)** Escreva $p$ na forma de Horner e avalie $p(1)$, $p(2{,}5)$ e $p(4)$, mostrando os valores intermediários. Onde há troca de sinal? O que isso resolve da ambiguidade de Descartes?

**d)** Sabendo que $x = 3$ é raiz, faça a **deflação** por Horner (divisão sintética) e encontre as outras três raízes.

**e)** A aula06 mostrou $p(x) = x^4 + 6x + 10$ no GNUPLOT sem nenhuma raiz real, e depois $x^4 + 6x$ com duas. Aplique Descartes aos dois polinômios e explique, com o argumento dos pares conjugados, o que aconteceu com as raízes quando o termo constante caiu de 10 para 0.

**f)** *Taylor.* Aproxime $e^{0{,}5}$ pelo polinômio de Taylor de grau 3 em torno de $a = 0$. Use o resto de Lagrange para dar uma **cota** do erro e compare com o erro real ($e^{0{,}5} = 1{,}6487213\ldots$).

**g)** *O plotador quebrado.* *(Lista · RE 2)* Seu programa de gráficos só plota em $x \in [-1, 1]$, e você precisa das **quatro** raízes reais de
$$f(x) = 8x^4 - 238x^3 + 1047x^2 - 953x + 154 .$$
Use Descartes para confirmar que todas são positivas. Mostre que $x^4 f(1/x)$ é o polinômio de coeficientes invertidos, $g(x) = 154x^4 - 953x^3 + 1047x^2 - 238x + 8$, e que suas raízes são os inversos das de $f$. Avaliando $f$ e $g$ só em pontos de $[-1, 1]$ (por Horner), isole as quatro raízes de $f$ em intervalos. Por fim, calcule a cota de Cauchy de $f$ e a de $g$ : o que a cota de $g$ diz sobre as raízes de $f$?

---

### Questão 3 — Caso *Quake III* : bisecção, secante e Newton
> O código-fonte de *Quake III Arena* (1999), liberado em 2005, contém a função abaixo. Ela calcula $1/\sqrt{x}$ — usada para normalizar vetores de iluminação milhões de vezes por segundo — sem nenhuma divisão e sem chamar `sqrt` :
>
> ```c
> float Q_rsqrt(float number) {
>     long i; float x2, y;
>     x2 = number * 0.5F;
>     y  = number;
>     i  = *(long *) &y;                    // lê os bits do float como inteiro
>     i  = 0x5f3759df - (i >> 1);           // chute inicial "mágico"
>     y  = *(float *) &i;
>     y  = y * (1.5F - (x2 * y * y));       // 1ª iteração
>     return y;
> }
> ```
>
> A última linha é **uma iteração do método de Newton**.

Os itens **a** a **c** usam $f(x) = x^3 - x - 2$, cuja raiz real é $r = 1{,}5213797\ldots$

**a)** Mostre, por Bolzano e por Descartes, que $f$ tem **exatamente uma** raiz positiva e que ela está em $[1, 2]$. Faça **4 iterações de bisecção** nesse intervalo, em tabela ($a$, $b$, $m$, $f(m)$). Quantas iterações seriam necessárias para largura $\le 10^{-6}$?

**b)** Faça **3 iterações de Newton** a partir de $x_0 = 1{,}5$ e anote o erro $|x_n - r|$ em cada uma. O que acontece com o número de casas corretas?

**c)** Faça iterações da **secante** a partir de $x_0 = 1$, $x_1 = 2$ até o erro ficar abaixo de $10^{-5}$. Quantas foram? Compare com Newton **por avaliação de função**, não por iteração.

**d)** Mostre que a linha `y = y * (1.5F - (x2 * y * y))` é Newton aplicado a $g(y) = \dfrac{1}{y^2} - x$. Por que escolher essa $g$, e não $h(y) = y^2 - \dfrac{1}{x}$, que tem a mesma raiz?

**e)** O chute do número mágico erra no máximo **≈ 3,4%**, e depois da iteração de Newton o erro máximo cai para **≈ 0,17%**. Explique esse número pela convergência quadrática. Por fim : a linha `i = *(long *) &y` só funciona porque o padrão de bits de um float positivo **cresce junto com o número**. Que decisão de projeto do IEEE 754, vista na aula02, garante isso?

**f)** *Heron e a raiz cúbica.* *(Lista · RE 3 ; ExLab 1 · 5 e 6)* O **método de Heron** calcula $\sqrt{p}$ por $x_{n+1} = \frac12\left(x_n + \frac{p}{x_n}\right)$. Mostre que é Newton aplicado a $h(x) = x^2 - p$ — a função que o *Quake III* recusou no item **d**. Faça 4 iterações para $p = 2$ a partir de $x_0 = 1$, com o erro. Depois deduza a iteração de Newton para $\sqrt[3]{p}$ e faça 3 iterações para $p = 10$ a partir de $x_0 = 2$.

**g)** *Bisecção e raízes múltiplas.* *(Lista · RE 4 e 5 ; ExLab 1 · 3 e 4)* Monte $p_3(x)$ com raízes $2, 3, 4$ e aplique a bisecção em $[1, 5]$. Que raiz ela acha, e em quantos passos? Ela acha as três? Mudando o intervalo inicial, dá para escolher qual raiz sai? Agora monte $p_4(x)$ com raízes $2, 3, 4, 5$ e tente $[1, 6]$. O que acontece, e como adaptar o algoritmo? Que cuidado a adaptação exige?

---

### Questão 4 — Caso da aula14 : o sistema em que o Seidel perdeu
> Na aula14, o JB resolveu o sistema abaixo com o programa dele : o **Gauss-Jacobi** achou a solução em **226 passos**. Esperava-se que o **Gauss-Seidel**, que usa cada valor novo o quanto antes, fosse mais rápido. *"Infelizmente, o contrário ocorreu."*
>
> $$\begin{cases} 4x + y - z = 6 \\ 3x - 4y + 2z = 8 \\ x + 2y + 2z = 3 \end{cases}$$

**a)** Isole $x$, $y$ e $z$ (as notas escreveram $x = 6 - y + 2/4$ ; corrija os parênteses). A partir de $(0, 0, 0)$, faça **2 iterações de Jacobi** e **2 de Seidel**.

**b)** Verifique se a matriz é **diagonalmente dominante** por linhas. As notas dizem que é isso que garante a convergência — então por que o Jacobi convergiu?

**c)** A matriz de iteração do Seidel, $T_S = -(D + L)^{-1} U$, é

$$T_S = \begin{pmatrix} 0 & -\tfrac14 & \tfrac14 \\[2pt] 0 & -\tfrac{3}{16} & \tfrac{11}{16} \\[2pt] 0 & \tfrac{5}{16} & -\tfrac{13}{16} \end{pmatrix}$$

Calcule seus autovalores e o **raio espectral** $\rho(T_S)$. Sabendo que $\rho(T_J) \approx 0{,}914$ para o Jacobi, explique o resultado do JB — inclusive a ordem de grandeza dos 226 passos.

**d)** *LU.* *(Lista · SL 4)* Fatore $A = \begin{pmatrix} 1 & 2 & 3 \\ 7 & 11 & 8 \\ 4 & 9 & 3 \end{pmatrix}$ em $L \cdot U$ (com $L$ de diagonal unitária) e **multiplique** $L \cdot U$ para verificar que $A$ é reconstruída. Resolva $Ax = b$ para $b_1 = (6, 26, 16)$ e $b_2 = (-1, 6, 5)$ por substituição **progressiva** ($Ly = b$) e **regressiva** ($Ux = y$), sem refatorar. O primeiro pivô vale $1$ e há um $7$ embaixo dele : o que o pivoteamento parcial faria aqui, e por quê?

**e)** No problema das criaturas felpudas, mudar o nodo de partida é só mudar $b$. Para uma matriz $1000 \times 1000$ e **100** pontos de partida diferentes, estime o custo de refazer Gauss cada vez contra fatorar uma vez e substituir 100 vezes.

**f)** *O sistema em que o Seidel ganhou.* *(Lista · SL 2)* A lista do professor traz o sistema abaixo e diz : *"agora resolva usando Gauss-Seidel e veja como a resposta é encontrada mais depressa"*.
$$\begin{cases} -8x + 2y + 4z + 5w = 7 \\ -x - 4y + 3z + w = 10 \\ 3x + y + 2z - w = 4 \\ -2x - 3y - z + 3w = -3 \end{cases}$$
A partir de $(1, 1, 1, 1)$, faça **2 iterações** de Jacobi e **2** de Seidel. Verifique a dominância diagonal. Sabendo que $\rho(T_J) \approx 0{,}843$ e $\rho(T_S) \approx 0{,}593$, estime quantas iterações cada um precisa para que a diferença entre iterações fique abaixo de $10^{-6}$. O que este sistema e o do enunciado têm em comum, e o que decide quem ganha?

---

### Questão 5 — Caso Ceres : mínimos quadrados
> Em 1º de janeiro de 1801, Giuseppe Piazzi descobriu Ceres. Acompanhou-o por cerca de 40 dias — uma fração pequena da órbita — até perdê-lo no brilho do Sol. Os astrônomos precisavam saber onde procurá-lo meses depois, a partir de poucas observações com erro. **Gauss**, então com 24 anos, ajustou uma órbita a essas observações minimizando a soma dos quadrados dos erros. Ceres foi reencontrado em 31 de dezembro de 1801, praticamente onde ele indicou. É o "outro método de Gauss" da aula16.

**a)** A aula16 minimiza $\sum (f(x_i) - y_i)^2$ e não $\sum |f(x_i) - y_i|$. Dê o motivo que as notas registram e explique por que ele importa para o passo seguinte — derivar e igualar a zero.

**b)** Ajuste uma reta $F(x) = ax + b$ aos pontos $(0, 1), (1, 2), (2, 4), (3, 4), (4, 6)$. Monte as **equações normais**, resolva, e calcule os resíduos e a soma dos quadrados dos resíduos. Quanto vale a **soma** dos resíduos, e por que isso não é coincidência?

**c)** Para o modelo da aula16, $F(x) = ax^2 + bx + c + d\cos(x)$, a derivada em relação a $a$ deu

$$a \sum x_i^4 + b \sum x_i^3 + c \sum x_i^2 + d \sum x_i^2 \cos(x_i) = \sum y_i\, x_i^2 .$$

Escreva as outras **três** equações (derivadas em relação a $b$, $c$ e $d$) e monte o sistema $4 \times 4$ na forma matricial. Que padrão a matriz tem?

**d)** Por que um polinômio de grau 4 passando **exatamente** pelos 5 pontos do item **b** (soma dos quadrados igual a zero) seria uma resposta pior, e não melhor?

**e)** A "notícia ruim" do fim da aula16 : o modelo com $e^{bx}$ não gera sistema linear. Para $F(x) = a\,e^{bx}$, mostre por que, e descreva a **linearização** por logaritmo. O que ela muda no problema que está sendo minimizado?

**f)** *Camarão.* *(Lista · Interpolação 6)* A produção brasileira de camarão cultivado, em toneladas :

| Ano | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 |
|---|---|---|---|---|---|---|---|---|
| Produção | 64.678 | 65.028 | 70.521 | 52.127 | 41.078 | 47.316 | 56.667 | 66.561 |

Com $t = \text{ano} - 2013$, ajuste por mínimos quadrados a **melhor reta** e o **melhor polinômio de grau 3**. Dê a soma dos quadrados dos resíduos de cada um e a previsão de cada um para 2021. Qual dos dois você usaria para prever, e por quê? (Depois, confira o valor real de 2021 na Pesquisa da Pecuária Municipal do IBGE.)

---

## Parte III — Laboratório
> 3 questões montadas com os exercícios das folhas que pedem programa. Faça as contas com o computador e use o gabarito para conferir os números — o que vale é a **interpretação**.

### Questão 6 — Cancelamento catastrófico
> Três exercícios da lista geral com o mesmo vilão : a **subtração de dois números quase iguais**. A subtração em si é exata (dois floats a menos de um fator 2 um do outro se subtraem sem erro) ; o que ela faz é **expor** os erros de arredondamento que já estavam nos operandos, trocando os dígitos corretos que se cancelaram por lixo.

**a)** *(Lista · PF 3)* Plote $f(x) = x^3 - 3x^2 + 3x - 1$ em torno de $x = 1$, primeiro em $[0{,}99;\ 1{,}01]$, depois em $[0{,}999975;\ 1{,}000025]$ e em intervalos menores. Descreva o gráfico e explique o que aparece. Repita com $g(x) = x^3$ e diga se o problema acontece. Por que avaliar $f$ por Horner não resolve, e o que resolve?

**b)** *(Lista · PF 4)* Você calcula $e^x$ pela série truncada
$$\text{meuexp}(x) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \frac{x^5}{5!}$$
Compare $\text{meuexp}(x)$ com $e^x$ para $x = 1, 2, 3, 5$ e para $x = -1, -2, -3, -5$. O que dá errado nos negativos? Aumente o número de termos : o problema some em $x = -5$? E em $x = -20$, com 100 termos, em `double` e em `float`? Separe os **dois** erros em jogo.

**c)** *(Lista · PF 4c)* Teste a ideia de calcular, para $x < 0$, $\text{meuexp}(x) = 1 / \text{meuexp}(-x)$. Por que ela funciona? Qual dos dois erros do item **b** ela resolve, e qual ela **não** resolve?

**d)** *(Lista · RE 1)* Mostre no papel que $f(x) = \sqrt{x^2 + 1} - 1$ e $g(x) = \dfrac{x^2}{\sqrt{x^2 + 1} + 1}$ são idênticas. Avalie as duas em `double` para $x = 10^{-3}, 10^{-5}, 10^{-7}, 10^{-8}$. Qual está certa? A partir de que $|x|$ a errada devolve exatamente zero, e por quê?

---

### Questão 7 — O polinômio do JB, do começo ao fim
> A lista geral e o ExLab 1 usam o mesmo polinômio em vários exercícios seguidos, cada um com uma peça do pipeline :
> $$p(x) = x^5 + 18x^3 + 34x^2 - 493x + 1431, \qquad \texttt{a[] = \{1, 0, 18, 34, -493, 1431\}}$$
> (O enunciado da questão 2 do ExLab 1 imprime esse polinômio de forma ambígua ; aqui vale a versão do vetor `a[]`, que é a mesma da lista geral.)

**a)** *(ExLab 1 · 2a)* Aplique Descartes a $p(x)$ e $p(-x)$. Liste os cenários possíveis de raízes positivas, negativas e complexas.

**b)** *(Lista · RE 9a–c ; ExLab 1 · 2b–c)* Calcule as cotas de Lagrange e de Cauchy e decida qual é melhor. Depois calcule a cota de **Fujiwara**,
$$|z| \le 2 \max\left\{ \left|\frac{a_{n-1}}{a_n}\right|,\ \left|\frac{a_{n-2}}{a_n}\right|^{1/2},\ \ldots,\ \left|\frac{a_1}{a_n}\right|^{1/(n-1)},\ \left|\frac{a_0}{2a_n}\right|^{1/n} \right\}$$
e compare as três com o maior módulo de raiz, $5{,}758$. Por que Lagrange e Cauchy são tão ruins neste polinômio?

**c)** *(Lista · RE 6 ; ExLab 1 · 7)* O que o algoritmo abaixo imprime? Execute-o à mão para $x = 2$, $x = -4$ e $x = -5$ (anote $p$ a cada volta do laço). O que as duas últimas execuções revelam?
```
void metodo( double x ) :
   double a[] = {1, 0, 18, 34, -493, 1431};
   double p = 0;
   para i = 0 a tamanho(a)-1 faça
       p = x * p + a[i];
   imprima x, p;
```

**d)** *(Lista · RE 8 ; ExLab 1 · 9)* O algoritmo foi "mudado misteriosamente" : antes de atualizar `p`, ele faz `q = x * q + p`. O que `q` guarda no fim? Execute para $x = -5$ e confira contra a derivada calculada à mão.

**e)** *(Lista · RE 7 e 9d ; ExLab 1 · 8)* Usando **c** e **d**, ache a raiz real negativa por **Newton** a partir de $x_0 = -5$ e pela **secante** a partir de $x_0 = -6$, $x_1 = -5$. Quantas iterações cada um leva até estabilizar em `double`? Depois rode Newton **real** a partir de $x_0 = 2$ e descreva o que acontece. O que isso diz sobre o cenário de Descartes?

**f)** *(Lista · RE 9e ; ExLab 1 · 10 e 11)* Com números complexos, o mesmo código de **d** faz Newton no plano. Ache as quatro raízes complexas. O enunciado pergunta : *por que "tentar"?* Dê pelo menos três motivos pelos quais Newton complexo pode não achar todas as raízes, e diga como a deflação ajuda.

**g)** *(Lista · RE 10)* O plano da deflação : achar uma raiz, dividir $p$ por $(x - r)$, repetir. Teste com
$$p(x) = x^5 - 20x^4 + 155x^3 - 580x^2 + 1044x - 720, \qquad \text{raízes } 2, 3, 4, 5, 6 .$$
Faça a divisão sintética por $x = 6$ e depois por $x = 5$. Agora suponha que o método achou $6{,}0001$ em vez de $6$ : qual é o resto da divisão, e onde ficam as raízes do quociente? Que problemas o plano tem, e como contorná-los?

---

### Questão 8 — Modelagem com sistemas lineares
> Os problemas do ExLab 2 não dão o sistema : dão uma situação. Metade do trabalho é montar $Ax = b$ ; a outra metade é **ler** a solução.

**a)** *O parquinho.* *(Lista · SL 1 ; ExLab 2 · 1)* Um parquinho tem 4 brinquedos, A, B, C e D. Pelo portão principal, perto de A, chegam 20 pessoas por hora ; pelo secundário, perto de C, chegam 10. Todos vão primeiro ao brinquedo do seu portão. Depois de A (ou de C), **metade** vai para B, e o resto se divide em **três** partes iguais : uma vai embora e as outras duas vão, uma cada, para os dois brinquedos restantes. Depois de B ou de D, as pessoas se dividem igualmente entre **A, C e D**. Monte o sistema de balanço (quem entra em cada brinquedo por hora) e resolva. Confira a resposta por conservação : quantas pessoas saem do parque por hora?

**b)** *(Lista · SL 3 ; ExLab 2 · 2)* Ache o polinômio de grau 3 que passa por $(-1, -3)$, $(0, -1)$, $(1, 2)$ e $(2, -2)$ montando o sistema linear (a matriz de **Vandermonde**). Qual incógnita sai de graça, e por quê?

**c)** *O químico, versão 1.* *(Lista · SL 5 ; ExLab 2 · 3)* Um composto $X$ é mistura das substâncias $A, B, C, D$, em proporções desconhecidas. O cromatógrafo mede a proporção dos componentes $a, b, c, d$ :

| Componente | em $X$ | em $A$ | em $B$ | em $C$ | em $D$ |
|---|---|---|---|---|---|
| $a$ | 26% | 15% | 36% | 20% | 31% |
| $b$ | 19% | 28% | 11% | 15% | 22% |
| $c$ | 31% | 27% | 36% | 33% | 24% |
| $d$ | 24% | 30% | 17% | 32% | 23% |

Monte e resolva o sistema. Mostre, **antes** de resolver, que as proporções encontradas vão somar exatamente 1.

**d)** *Versão 2.* *(Lista · SL 6 ; ExLab 2 · 4)* Os exames mostram outras substâncias desconhecidas em $X$, e a coluna de $X$ passa a ser $(24{,}3\%;\ 15\%;\ 26{,}2\%;\ 21{,}5\%)$ — soma 87%. As colunas de $A$ a $D$ não mudam. Resolva de novo e **interprete com cuidado** : quanto somam as proporções, o que isso significa, e o que aconteceu com a proporção de $A$ em relação à versão 1?

**e)** *Versão 3.* *(Lista · SL 7)* Agora há componentes desconhecidos também em $A, B, C, D$ :

| Componente | em $X$ | em $A$ | em $B$ | em $C$ | em $D$ |
|---|---|---|---|---|---|
| $a$ | 8% | 5% | 6% | 11% | 17% |
| $b$ | 7% | 8% | 11% | 5% | 6% |
| $c$ | 12% | 7% | 16% | 13% | 14% |
| $d$ | 12% | 11% | 12% | 14% | 2% |

Resolva e interprete. Depois some $0{,}1$ ponto percentual a **uma** entrada da coluna de $X$ de cada vez e resolva de novo : o que acontece com a proporção de $D$? Dá para afirmar que $D$ está na mistura?

---

## Parte IV — Estudos de caso *(bônus)*
> Para cada caso, diga **qual conceito da matéria** explica a falha e **qual teria sido a correção**. Um parágrafo cada.

**1. Míssil Patriot, Dhahran, 25/02/1991.** O sistema contava o tempo em décimos de segundo num registrador de ponto fixo de 24 bits, multiplicando o contador por $0{,}1$. A bateria estava ligada havia **100 horas**. Um míssil Scud não foi interceptado e 28 soldados morreram.

**2. Ariane 5, voo 501, 04/06/1996.** 37 segundos depois do lançamento, o software de navegação converteu um valor de velocidade horizontal de `double` (64 bits) para **inteiro de 16 bits com sinal**. O código tinha sido herdado do Ariane 4, mais lento. O foguete se autodestruiu.

**3. Pentium FDIV, 1994.** O Pentium calculava `4195835 / 3145727` como $1{,}33373\ldots$ em vez de $1{,}33382\ldots$. A divisão usava uma tabela de consulta com 1066 entradas, das quais **5** estavam vazias. A Intel gastou cerca de US\$ 475 milhões num recall.

---

## Gabarito comentado

> [!success]- **Parte I — Objetivas**
> **1 — (c).** 23 bits **armazenados**, precisão $p = 24$. O bit implícito existe no valor e participa das contas, mas não vai para a memória : $1 + 8 + 23 = 32$. Em `double` : 52 armazenados, $p = 53$.
>
> **2 — (c).** Expoente `0xFF` (todo ligado) e mantissa zero é infinito ; o sinal é 0, então $+\infty$. Com qualquer bit da mantissa ligado seria NaN.
>
> **3 — (c).** NaN é o único valor que não é igual a si mesmo — `x != x` é a implementação clássica de `isnan`. Sobre (e) : $-0$ e $+0$ têm bits diferentes, mas o padrão exige $-0 = +0$.
>
> **4 — (c).** Com bias, o expoente é um inteiro sem sinal crescente, e está nos bits mais significativos logo abaixo do sinal. Expoente maior ⇒ bits maiores ⇒ número maior. Em complemento de dois, $2^{-1}$ teria o bit alto do expoente ligado e pareceria maior que $2^{+1}$. Ressalva : só vale para positivos, porque o sinal é sinal-magnitude.
>
> **5 — (b).** "Meio para cima" empurra todos os empates no mesmo sentido, e o erro acumula **linearmente**. Com empate no par, o erro vira um passeio aleatório. É exatamente o que a Questão 1c mede em Vancouver.
>
> **6 — (b).** Sem subnormais, dois números distintos e minúsculos podem subtrair e dar exatamente zero — e um `if (x != y) z = 1/(x-y)` dividiria por zero mesmo "protegido".
>
> **7 — (c).** $\varepsilon = 2^{1-p}$ é a resolução da régua perto de 1. O menor float positivo é o subnormal $2^{-149} \approx 1{,}4 \times 10^{-45}$, 38 ordens de grandeza menor.
>
> **8 — (b).** $p(\bar z) = \overline{p(z)} = 0$ quando os coeficientes são reais. Duas raízes reais se aproximam, colidem e saem do eixo como um par conjugado — a animação da aula06. Com coeficientes complexos o argumento não vale.
>
> **9 — (c).** "Geral" e "por radicais" são as palavras que importam. $x^5 - 2 = 0$ tem raiz $\sqrt[5]{2}$ ; o que não existe é a fórmula universal. Consequência para a disciplina : acima do grau 4, só iteração numérica.
>
> **10 — (d).** Ostrowski (1954) provou que $n$ somas são necessárias e Pan (1966) que $n$ multiplicações são necessárias. Horner é **ótimo**.
>
> **11 — (b).** A cada passo a largura cai pela metade : $1/2^n \le 10^{-6} \Rightarrow n \ge 19{,}93$. Nenhum método rápido permite dizer isso antes de rodar.
>
> **12 — (c).** Para $f = (x-1)^2$ : $x_{n+1} = x_n - \frac{(x_n-1)^2}{2(x_n-1)} = x_n - \frac{x_n - 1}{2}$, e o erro cai pela metade — linear, com fator $1 - 1/m = 1/2$. Com o fator $m = 2$, o passo vira $x_{n+1} = x_n - (x_n - 1) = 1$ : chega na raiz em um passo. Sobre (b) : $f'$ só zera **na** raiz, não nos iterados.
>
> **13 — (b).** Índice de eficiência $E = p^{1/m}$, com $m$ avaliações por iteração : Newton $2^{1/2} \approx 1{,}414$, secante $1{,}618^{1/1}$. Newton só ganha quando $f'$ sai quase de graça — em polinômios, onde Horner devolve $p$ e $p'$ no mesmo laço.
>
> **14 — (c).** É o argumento do JB : "para o cara da computação" Jacobi paraleliza e Seidel não. O PageRank do Google, um sistema com bilhões de incógnitas, é resolvido com iterações do tipo Jacobi justamente por isso. Sobre (e) : dominância diagonal é **suficiente**, não necessária — veja a Questão 4b.
>
> **15 — (c).** É o ponto da aula15 : trocar o ponto de partida das criaturas felpudas é trocar $b$, e a fatoração já feita serve para todos. Sobre (d) : sem pivoteamento, LU pode ser **instável** — precisão não é a vantagem.
>
> **16 — (c).** O $\cos(x)$ é só um número conhecido para cada $x_i$ ; a incógnita $d$ entra multiplicando. Em (a), $b$ está dentro da exponencial e a derivada em relação a $b$ não é linear em $b$.
>
> **17 — (c).** $\varepsilon/2 = 2^{-53} \approx 1{,}11 \times 10^{-16}$, e $10^{-16}$ é menor : $1 + 10^{-16}$ fica mais perto de $1$ que do próximo `double`, então $x^2 + 1 = 1$ e $\sqrt{1} - 1 = 0$. A subtração foi exata ; o estrago estava no arredondamento anterior, e ela só o deixou à vista. Sobre (b) : $10^{-16}$ está muito longe dos subnormais do `double`, que começam em $\approx 2{,}2 \times 10^{-308}$. Veja a Questão 6d.
>
> **18 — (b).** $h(x) = x^2 - p$, $h'(x) = 2x$ : $x - \frac{x^2 - p}{2x} = \frac{x^2 + p}{2x} = \frac12\left(x + \frac{p}{x}\right)$. Por ser Newton numa raiz simples, tem **ordem 2** — o que exclui (e). Heron usava isso no século I, 1600 anos antes de Newton.
>
> **19 — (d).** $p(1)\,p(6) > 0$ é compatível com nenhuma raiz ou com um número par delas — aqui são quatro. Bolzano só dá uma implicação : troca de sinal ⇒ raiz. A volta não vale. Veja a Questão 3g.
>
> **20 — (c).** $x^4 f(1/x) = x^4\left(a_4 x^{-4} + a_3 x^{-3} + a_2 x^{-2} + a_1 x^{-1} + a_0\right) = a_4 + a_3 x + a_2 x^2 + a_1 x^3 + a_0 x^4$. Se $f(r) = 0$ com $r \ne 0$, então o polinômio invertido zera em $1/r$. A janela $[-1, 1]$ passa a mostrar as raízes com $|r| \ge 1$ ; as de $|r| \le 1$ já apareciam em $f$. Juntas, as duas plotagens cobrem a reta inteira. Veja a Questão 2g.

> [!success]- **Questão 1 — Bolsa de Vancouver**
> **a)**
>
> | Padrão | Sinal | Expoente armazenado | Expoente real | Mantissa (com o `1` implícito) | Valor |
> |---|---|---|---|---|---|
> | `0xC1480000` | 1 | `10000010` = 130 | $130 - 127 = 3$ | $1{,}1001_2 = 1{,}5625$ | $-1{,}5625 \times 2^3 = \mathbf{-12{,}5}$ |
> | `0x3F400000` | 0 | `01111110` = 126 | $-1$ | $1{,}1_2 = 1{,}5$ | $1{,}5 \times 2^{-1} = \mathbf{0{,}75}$ |
>
> Codificando $-6{,}25$ : $6{,}25 = 110{,}01_2 = 1{,}1001_2 \times 2^2$. Sinal 1, expoente $2 + 127 = 129 =$ `10000001`, mantissa armazenada `1001` seguida de zeros (o `1` da frente some).
>
> `1 10000001 10010000000000000000000` = **`0xC0C80000`**
>
> **b)**
>
> | Padrão | Classe | Valor |
> |---|---|---|
> | `0x00000000` | zero | $+0$ |
> | `0x80000000` | zero | $-0$ (compara igual a $+0$) |
> | `0x7F800000` | infinito | $+\infty$ |
> | `0xFFC00000` | NaN (quiet) | o `-nan` da aula02 : é o *real indefinite* que o x86 devolve em $0/0$ |
> | `0x00800000` | normal | $2^{-126} \approx 1{,}18 \times 10^{-38}$, o **menor normal** |
> | `0x00000001` | subnormal | $2^{-149} \approx 1{,}40 \times 10^{-45}$, o **menor positivo** |
>
> **c)** Truncar para três casas descarta tudo depois da terceira casa, sempre para baixo (o índice é positivo). O dígito descartado é, na prática, uniforme entre $0$ e $0{,}001$, então a perda média é **$0{,}0005$ por operação**, sempre com o mesmo sinal. Em $\approx 1{,}4 \times 10^6$ operações : $1{,}4 \times 10^6 \times 0{,}0005 \approx 700$ pontos. A perda real foi $1098{,}892 - 524{,}811 \approx 574$ — a mesma ordem de grandeza (a estimativa ignora que o índice mudou de valor ao longo do período).
>
> Com `roundTiesToEven` o erro de cada operação tem média **zero** e desvio de $\approx 0{,}0003$ ; acumulado, cresce como $\sqrt{n}$ : $\sqrt{1{,}4 \times 10^6} \times 0{,}0003 \approx 0{,}35$ ponto. **Setecentos pontos contra um terço de ponto** : é a diferença entre erro linear e passeio aleatório, e é o motivo de o modo padrão ser o que é.
>
> **d)** Em `float`, imprime **24 vezes**, para `EPS` $= 1, 2^{-1}, \ldots, 2^{-23}$. O último valor impresso, $2^{-23} \approx 1{,}19 \times 10^{-7}$, é o **epsilon de máquina** do `float`. Em `double`, **53 vezes**, e o último é $2^{-52} \approx 2{,}22 \times 10^{-16}$.
>
> O laço para porque $1 + 2^{-24}$ fica exatamente no meio entre $1$ e $1 + 2^{-23}$, e o empate vai para o par — que é o próprio $1{,}0$. Quem perde bits é a **soma**, não o `EPS` : dividir por 2 só decrementa o expoente. (Em x87 com registradores de 80 bits, o laço pode ir até $2^{-63}$ e medir o epsilon do registrador.)
>
> **e)** Os quatro produtos : $(-2)(1) = -2$, $(-2)(4) = -8$, $3 \cdot 1 = 3$, $3 \cdot 4 = 12$. O resultado é $[-8, 12]$. "Menor com menor" daria $(-2)(1) = -2$ como extremo inferior — **errado**, porque o sinal negativo troca qual par produz o mínimo. Regra correta : calcular os quatro produtos e tomar o mínimo e o máximo. O mínimo é arredondado para $-\infty$ e o máximo para $+\infty$, para o intervalo **nunca encolher** — se encolher, o valor verdadeiro pode ficar de fora e a garantia morre.
>
> **f)** Em x86 (SSE), `float` :
>
> | Operação | Resultado | Bits | Flags levantadas |
> |---|---|---|---|
> | `21 / -0` | $-\infty$ | `0xFF800000` | `DIVBYZERO` |
> | `0 / 0` | NaN | `0xFFC00000` (o *real indefinite*) | `INVALID` |
> | `1e35 * 1e35` | $+\infty$ | `0x7F800000` | `OVERFLOW`, `INEXACT` |
> | `1 / inf` | $+0$ | `0x00000000` | nenhuma |
> | `0 * inf` | NaN | `0xFFC00000` | `INVALID` |
> | `1e-40 / 1e-40` | $1$ | `0x3F800000` | nenhuma |
> | `1e-30 * 1e-30` | $+0$ | `0x00000000` | `UNDERFLOW`, `INEXACT` |
> | `1 / 3` | $0{,}33333334$ | `0x3EAAAAAB` | `INEXACT` |
>
> `1e-40` em `float` : `0 00000000 00000010001011011000010` = **`0x000116C2`**, um **subnormal** (expoente todo zerado, sem o `1` implícito), que vale $9{,}99995 \times 10^{-41}$ — não é exatamente $10^{-40}$. Duas pegadinhas : `1e-40 / 1e-40` **não** levanta underflow, porque as entradas já eram subnormais e o quociente, $1$, é exato ; e `1/inf` dá zero **sem** underflow, porque o zero é exato. Underflow é "resultado minúsculo **e** inexato", como em `1e-30 * 1e-30` : o exato, $10^{-60}$, está abaixo do menor subnormal ($1{,}4 \times 10^{-45}$).
>
> **Por que ler o registrador** : as flags são efeito colateral da operação, definidas pelo hardware em casos que o programador erra fácil — as duas pegadinhas acima, ou o fato de o padrão deixar à implementação detectar o underflow antes ou depois do arredondamento. Prever no código é reescrever a FPU e errar onde ela não erra. **Por que limpar depois de ler** : converter o texto `"1e-40"` para `float` já é uma operação inexata que produz um subnormal, e pode levantar `INEXACT` e `UNDERFLOW` por conta própria. Limpando antes, essas flags da **leitura** apareceriam como se fossem da conta.

> [!success]- **Questão 2 — Pipeline das raízes**
> **a)** $p(x)$ : sinais $+\ -\ -\ +\ +$ → **2 trocas** → 2 ou 0 positivas.
> $p(-x) = x^4 + 2x^3 - 7x^2 - 8x + 12$ : sinais $+\ +\ -\ -\ +$ → **2 trocas** → 2 ou 0 negativas.
> Grau 4, e $x = 0$ não é raiz (termo constante 12). Cenários possíveis (positivas, negativas, complexas) : $(2,2,0)$, $(2,0,2)$, $(0,2,2)$, $(0,0,4)$. Descartes sozinho **não decide**.
>
> **b)** Cauchy : $1 + \max\{2, 7, 8, 12\} = \mathbf{13}$. Lagrange : $\max(1,\ 2 + 7 + 8 + 12) = \mathbf{29}$. Cauchy é mais apertada. As cotas valem para o **módulo** de todas as raízes, inclusive as complexas : todas estão no disco $|z| \le 13$. Na reta real, procura-se em $[-13, 13]$.
>
> **c)** Forma de Horner : $p(x) = 12 + x\,(8 + x\,(-7 + x\,(-2 + x)))$. Coeficientes $[1, -2, -7, 8, 12]$ :
>
> | $x$ | Intermediários | $p(x)$ |
> |---|---|---|
> | 1 | $1,\ -1,\ -8,\ 0,\ 12$ | **12** |
> | 2,5 | $1,\ 0{,}5,\ -5{,}75,\ -6{,}375,\ -3{,}9375$ | **−3,9375** |
> | 4 | $1,\ 2,\ 1,\ 12,\ 60$ | **60** |
>
> Duas trocas de sinal : em $(1;\ 2{,}5)$ e em $(2{,}5;\ 4)$. Pelo Bolzano há pelo menos uma raiz em cada, logo **pelo menos 2 positivas** — e Descartes diz "2 ou 0", então são **exatamente 2**. É o casamento das etapas : Descartes dá as possibilidades, a varredura com Horner decide.
>
> **d)** Horner em $x = 3$ : intermediários $1,\ 1,\ -4,\ -4\ |\ 0$. O resto $0$ confirma a raiz, e os intermediários são o quociente :
> $$q(x) = x^3 + x^2 - 4x - 4 = x^2(x + 1) - 4(x + 1) = (x + 1)(x^2 - 4)$$
> Raízes : $\mathbf{-2,\ -1,\ 2,\ 3}$. Cenário $(2, 2, 0)$. Note que avaliar e deflacionar foram **a mesma conta**.
>
> **e)** $x^4 + 6x + 10$ : sinais $+\ +\ +$, 0 trocas → **nenhuma positiva** ; $p(-x) = x^4 - 6x + 10$ : 2 trocas → 2 ou 0 negativas. O gráfico não cruza o eixo : são 0 negativas e as 4 raízes são complexas, em **dois pares conjugados** ($\approx 1{,}297 \pm 1{,}685i$ e $-1{,}297 \pm 0{,}726i$).
> $x^4 + 6x = x(x^3 + 6)$ : raízes reais $0$ e $-\sqrt[3]{6} \approx -1{,}817$, mais um par conjugado. Baixar o termo constante de 10 para 0 desceu o gráfico até ele cortar o eixo : o par $-1{,}297 \pm 0{,}726i$ **colidiu no eixo real e se separou** em duas raízes reais. As raízes entram e saem do eixo **aos pares** — é o "de 2 em 2" de Descartes visto acontecer.
>
> **f)** $P_3(0{,}5) = 1 + 0{,}5 + \frac{0{,}25}{2} + \frac{0{,}125}{6} = 1{,}6458333$.
> Resto de Lagrange : $R_3 = \frac{e^{\xi}}{4!}(0{,}5)^4$ com $\xi \in (0;\ 0{,}5)$. Como $e^{\xi} < e^{0{,}5} < 1{,}65$ : $|R_3| < \frac{1{,}65}{24} \times 0{,}0625 \approx \mathbf{0{,}0043}$.
> Erro real : $1{,}6487213 - 1{,}6458333 = \mathbf{0{,}0028879}$, dentro da cota. A cota é segura porque usa o pior $\xi$ possível ; o $\xi$ verdadeiro está mais perto de 0.
>
> **g)** Descartes : $f$ tem sinais $+\ -\ +\ -\ +$, **4 trocas** ; $f(-x) = 8x^4 + 238x^3 + 1047x^2 + 953x + 154$ não tem nenhuma. Logo nenhuma raiz negativa, e as quatro reais que o enunciado promete são **positivas**.
> Os pontos da janela, por Horner :
>
> | $x$ | 0 | 0,2 | 0,3 | 0,5 | 0,9 | 1 |
> |---|---|---|---|---|---|---|
> | $f(x)$ | 154 | 3,39 | −44,0 | −90 | −23,9 | 18 |
> | $g(x)$ | 8 | −5,10 | 6,35 | 41,3 | — | 18 |
>
> e ainda $g(0{,}03) = 1{,}78$, $g(0{,}05) = -1{,}40$. Trocas de sinal :
> - em $f$ : $(0{,}2;\ 0{,}3)$ e $(0{,}9;\ 1)$ — as duas raízes pequenas, $\mathbf{0{,}2061}$ e $\mathbf{0{,}9594}$ ;
> - em $g$ : $(0{,}03;\ 0{,}05)$ e $(0{,}2;\ 0{,}3)$ — invertendo, raízes de $f$ em $(20;\ 33{,}3)$ e $(3{,}33;\ 5)$ : $\mathbf{24{,}632}$ e $\mathbf{3{,}953}$.
>
> Invertendo o intervalo, a ordem troca : $1/0{,}05 = 20$ é o extremo **inferior**. Refinar pode ser feito também dentro da janela, na raiz de $g$, e inverter no fim.
> Cauchy de $f$ : $1 + 953/8 \approx 120{,}1$ — todas as raízes têm $|r| \le 120{,}1$ (a maior é $24{,}6$). Cauchy de $g$ : $1 + 953/154 \approx 7{,}19$, logo as raízes de $g$ têm módulo $\le 7{,}19$ e as de $f$ têm módulo $\ge 1/7{,}19 \approx 0{,}139$. A cota do polinômio invertido dá uma **cota inferior** para as raízes do original : nenhuma raiz de $f$ está em $(-0{,}139;\ 0{,}139)$ — a menor é $0{,}206$.

> [!success]- **Questão 3 — Quake III**
> **a)** $f(1) = -2 < 0$ e $f(2) = 4 > 0$ : $f$ é contínua, então há raiz em $[1, 2]$ (Bolzano). Sinais de $f$ : $+\ -\ -$, **1 troca** → exatamente 1 raiz positiva (1 não permite descer de 2 em 2).
>
> | $n$ | $a$ | $b$ | $m$ | $f(m)$ |
> |---|---|---|---|---|
> | 1 | 1 | 2 | 1,5 | −0,125 |
> | 2 | 1,5 | 2 | 1,75 | 1,609 |
> | 3 | 1,5 | 1,75 | 1,625 | 0,666 |
> | 4 | 1,5 | 1,625 | 1,5625 | 0,252 |
>
> Após 4 iterações a raiz está em $[1{,}5;\ 1{,}5625]$, de largura $1/16$. Para largura $\le 10^{-6}$ : $n \ge \log_2(10^6) \approx 19{,}93$, logo **20 iterações**.
>
> **b)** $f'(x) = 3x^2 - 1$ ; $x_{n+1} = x_n - \dfrac{x_n^3 - x_n - 2}{3x_n^2 - 1}$.
>
> | $n$ | $x_n$ | Erro $\lvert x_n - r \rvert$ |
> |---|---|---|
> | 0 | 1,5 | $2{,}1 \times 10^{-2}$ |
> | 1 | 1,5217391 | $3{,}6 \times 10^{-4}$ |
> | 2 | 1,5213798060 | $9{,}9 \times 10^{-8}$ |
> | 3 | 1,52137970680457 | $7{,}5 \times 10^{-15}$ |
>
> As casas corretas vão de ~2 para ~4, ~7 e ~14 : **dobram** a cada passo. Na 4ª iteração já é a raiz em precisão de `double`.
>
> **c)** $x_{n+1} = x_n - f(x_n)\dfrac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$ :
>
> | $n$ | $x_n$ | Erro |
> |---|---|---|
> | 2 | 1,3333333 | $1{,}9 \times 10^{-1}$ |
> | 3 | 1,4626866 | $5{,}9 \times 10^{-2}$ |
> | 4 | 1,5311694 | $9{,}8 \times 10^{-3}$ |
> | 5 | 1,5209264 | $4{,}5 \times 10^{-4}$ |
> | 6 | 1,5213763 | $3{,}4 \times 10^{-6}$ |
> | 7 | 1,5213797080 | $1{,}2 \times 10^{-9}$ |
>
> **5 iterações** até ficar abaixo de $10^{-5}$ ($x_6$). Por avaliação : a secante gasta **uma** avaliação nova por iteração (reaproveita a anterior), Newton gasta **duas** ($f$ e $f'$). Newton chegou a $10^{-7}$ com 4 avaliações ; a secante chegou a $3{,}4 \times 10^{-6}$ com 7 (5 iterações + 2 pontos iniciais). A comparação direta é injusta com a secante : ela partiu de um erro de $0{,}5$, Newton de $0{,}02$. Da iteração 4 em diante, quando os dois já estão perto da raiz, os dígitos corretos da secante são multiplicados por ~1,6 a cada avaliação ($\approx 3{,}3 \to 5{,}5 \to 8{,}9$ casas, de $x_5$ a $x_7$) ; os de Newton dobram a cada **duas** avaliações, ou seja, $\sqrt2 \approx 1{,}41$ por avaliação. É o índice de eficiência da objetiva 13.
>
> **d)** $g(y) = y^{-2} - x$ ⇒ $g'(y) = -2y^{-3}$.
> $$y_{n+1} = y_n - \frac{y_n^{-2} - x}{-2y_n^{-3}} = y_n + \frac{y_n - x\,y_n^{3}}{2} = y_n\left(\frac32 - \frac{x}{2}\,y_n^{2}\right)$$
> Com `x2 = x/2`, é exatamente `y * (1.5F - x2*y*y)`. A escolha de $g$ é o truque todo : a iteração resultante **não tem divisão nem raiz**, só multiplicações — e em 1999 dividir e tirar raiz eram as operações caras. Com $h(y) = y^2 - 1/x$ a iteração seria $y - \frac{y^2 - 1/x}{2y}$, com duas divisões. **Mesma raiz, funções diferentes, custos diferentes** : escolher a $f$ também é parte do método.
>
> **e)** Para essa iteração, o erro relativo evolui como $e_{n+1} \approx \frac32 e_n^2$. Com $e_0 \approx 0{,}034$ : $\frac32 (0{,}034)^2 \approx 0{,}0017$ — os **0,17%**. Uma iteração transformou 1,5 casa correta em quase 3. Para um jogo, bastava.
>
> Quanto aos bits : é o **bias** do expoente, na ordem `[sinal][expoente][mantissa]`. O expoente com bias é um inteiro sem sinal crescente nos bits altos, então o inteiro lido de `y` é, a menos de escala e deslocamento, uma aproximação de $\log_2 y$. Deslocar para a direita divide o log por 2 (raiz quadrada) e subtrair de uma constante troca o sinal (inverso) : $\log_2(1/\sqrt{y}) = -\tfrac12 \log_2 y$. O número mágico é o deslocamento que corrige a escala. É a "ordenação de float como string" da aula02, usada como calculadora de logaritmo.
>
> **f)** $h(x) = x^2 - p$, $h'(x) = 2x$ : $x_{n+1} = x_n - \dfrac{x_n^2 - p}{2x_n} = \dfrac12\left(x_n + \dfrac{p}{x_n}\right)$. É Heron.
>
> | $n$ | $x_n$ ($\sqrt2$) | Erro |
> |---|---|---|
> | 1 | 1,5 | $8{,}6 \times 10^{-2}$ |
> | 2 | 1,4166667 | $2{,}5 \times 10^{-3}$ |
> | 3 | 1,4142157 | $2{,}1 \times 10^{-6}$ |
> | 4 | 1,414213562374690 | $1{,}6 \times 10^{-12}$ |
>
> Raiz cúbica : $h(x) = x^3 - p$, $h'(x) = 3x^2$ ⇒ $x_{n+1} = x_n - \dfrac{x_n^3 - p}{3x_n^2} = \dfrac13\left(2x_n + \dfrac{p}{x_n^2}\right)$. Para $p = 10$, $x_0 = 2$ : $2{,}1666667$ (erro $1{,}2 \times 10^{-2}$), $2{,}1545036$ ($6{,}9 \times 10^{-5}$), $2{,}1544347$ ($2{,}2 \times 10^{-9}$) ; a 4ª já é $\sqrt[3]{10} = 2{,}154434690031884$ em `double`. Ordem 2 nos dois : o erro é aproximadamente o quadrado do anterior vezes uma constante.
> O contraste com o *Quake* : Heron **divide** a cada passo, e é por isso que a iteração da $h$ era cara em 1999. Em hardware moderno, com divisão rápida, Heron é o jeito natural — e é como muitas bibliotecas refinam `sqrt` em software.
>
> **g)** $p_3(x) = (x-2)(x-3)(x-4) = x^3 - 9x^2 + 26x - 24$. Em $[1, 5]$ : $p_3(1) = -6$, $p_3(5) = 6$, e o primeiro ponto médio é $m = 3$, com $p_3(3) = 0$ **exatamente** : acha a raiz 3 em **1 passo**. Sorte da simetria — e mostra que o código precisa testar $f(m) = 0$, senão segue cortando à toa.
> Ela acha **uma** raiz por execução, nunca todas. Qual sai depende do intervalo : $[1;\ 4{,}5]$ converge para **2**, $[3{,}5;\ 5]$ para **4**. **Sempre** que $f(a)\,f(b) < 0$ ela acha **alguma** raiz de multiplicidade ímpar lá dentro — é a garantia de Bolzano, e é a única que ela dá.
> $p_4(x) = (x-2)(x-3)(x-4)(x-5) = x^4 - 14x^3 + 71x^2 - 154x + 120$ : $p_4(1) = p_4(6) = 24$, mesmo sinal, e a bisecção **nem começa**. Adaptação : varrer $[1, 6]$ com passo $h$, procurar trocas de sinal entre pontos vizinhos e rodar a bisecção em cada subintervalo que trocar. Cuidados :
> - $h$ menor que a **menor distância** entre raízes (aqui 1) ; se duas raízes caem no mesmo subintervalo, os sinais se cancelam e as duas somem ;
> - ponto da varredura caindo **em cima** da raiz — com $h = 0{,}5$ a partir de 1, os pontos $2, 3, 4, 5$ são as próprias raízes : testar $f = 0$ também ali ;
> - raízes de multiplicidade **par**, como em $(x-2)^2$, não trocam de sinal e são invisíveis a qualquer método de sinal — para elas, Newton (com o cuidado da objetiva 12).

> [!success]- **Questão 4 — O sistema da aula14**
> **a)** Isolando :
> $$x = \frac{6 - y + z}{4}, \qquad y = \frac{8 - 3x - 2z}{-4}, \qquad z = \frac{3 - x - 2y}{2}$$
> (As notas escreveram $x = 6 - y + 2/4$ ; o certo é $(6 - y + z)/4$. As contas das notas com o chute $(7, 5, 8)$ — $2{,}25$, $7{,}25$, $-7$ — estão corretas, então foi só a transcrição.)
>
> | Iteração | Jacobi $(x, y, z)$ | Seidel $(x, y, z)$ |
> |---|---|---|
> | 0 | $(0,\ 0,\ 0)$ | $(0,\ 0,\ 0)$ |
> | 1 | $(1{,}5;\ -2;\ 1{,}5)$ | $(1{,}5;\ -0{,}875;\ 1{,}625)$ |
> | 2 | $(2{,}375;\ -0{,}125;\ 2{,}75)$ | $(2{,}125;\ 0{,}40625;\ 0{,}03125)$ |
>
> No Seidel, o $y$ da iteração 1 já usa $x = 1{,}5$ : $y = (8 - 4{,}5 - 0)/(-4) = -0{,}875$. Solução exata : $\left(\frac{55}{31},\ -\frac{15}{62},\ \frac{53}{62}\right) \approx (1{,}774;\ -0{,}242;\ 0{,}855)$.
>
> **b)** Linha 1 : $|4| > |1| + |-1| = 2$ ✓. Linha 2 : $|-4| > |3| + |2| = 5$ ✗. Linha 3 : $|2| > |1| + |2| = 3$ ✗. **Não é diagonalmente dominante** — e nenhuma troca de linhas resolve, porque só a linha 1 tem um coeficiente maior que a soma dos outros. O Jacobi convergiu mesmo assim porque dominância diagonal é condição **suficiente**, não necessária. A condição **necessária e suficiente** é o raio espectral da matriz de iteração ser menor que 1 — e $\rho(T_J) \approx 0{,}914 < 1$.
>
> **c)** A primeira coluna de $T_S$ é nula, então $\lambda_1 = 0$ e os outros dois vêm do bloco $2 \times 2$ :
> $$\operatorname{tr} = -\tfrac{3}{16} - \tfrac{13}{16} = -1, \qquad \det = \tfrac{(-3)(-13) - (11)(5)}{256} = -\tfrac{16}{256} = -\tfrac{1}{16}$$
> $$\lambda^2 + \lambda - \tfrac{1}{16} = 0 \ \Rightarrow\ \lambda = \frac{-1 \pm \sqrt{5}/2}{2} \ \Rightarrow\ \lambda_2 \approx 0{,}059,\quad \lambda_3 = -\frac{2 + \sqrt5}{4} \approx -1{,}059$$
> $\rho(T_S) \approx \mathbf{1{,}059 > 1}$ : **o Seidel diverge** neste sistema. Não era lentidão, era divergência — cada iteração multiplica a componente do erro na direção de $\lambda_3$ por $-1{,}059$, trocando de sinal e crescendo.
>
> O Jacobi, com $\rho \approx 0{,}914$, reduz o erro cerca de 9% por passo. Partindo de um erro da ordem de 10 (o chute $(7, 5, 8)$) até $10^{-9}$ : $n \approx \dfrac{\ln(10^{-10})}{\ln 0{,}914} \approx \dfrac{-23{,}0}{-0{,}090} \approx 255$ passos — a ordem de grandeza dos **226** do JB (o número exato depende do critério de parada dele). O Seidel tem convergência **garantida** para matrizes estritamente diagonalmente dominantes ou simétricas definidas positivas — e é nelas que a intuição "usar o valor novo cedo ajuda" costuma se confirmar. Esta matriz não é nenhuma das duas, e aí não há regra : existem sistemas em que só o Jacobi converge, e outros em que só o Seidel.
>
> **d)** Eliminação guardando os multiplicadores :
> - $\ell_{21} = 7/1 = 7$, $\ell_{31} = 4/1 = 4$ → linhas 2 e 3 viram $(7, 11, 8) - 7(1, 2, 3) = (0, -3, -13)$ e $(4, 9, 3) - 4(1, 2, 3) = (0, 1, -9)$.
> - $\ell_{32} = 1/(-3) = -\tfrac13$ → linha 3 vira $(0, 1, -9) + \tfrac13(0, -3, -13) = \left(0,\ 0,\ -\tfrac{40}{3}\right)$.
> $$L = \begin{pmatrix} 1 & 0 & 0 \\ 7 & 1 & 0 \\ 4 & -\tfrac13 & 1 \end{pmatrix}, \qquad U = \begin{pmatrix} 1 & 2 & 3 \\ 0 & -3 & -13 \\ 0 & 0 & -\tfrac{40}{3} \end{pmatrix}$$
> Reconstrução, linha a linha de $L \cdot U$ : a 1ª é $(1, 2, 3)$ ; a 2ª é $7(1, 2, 3) + (0, -3, -13) = (7, 11, 8)$ ; a 3ª é $4(1, 2, 3) - \tfrac13(0, -3, -13) + \left(0, 0, -\tfrac{40}{3}\right) = \left(4,\ 9,\ 12 + \tfrac{13}{3} - \tfrac{40}{3}\right) = (4, 9, 3)$ ✓.
>
> | $b$ | $Ly = b$ (progressiva) | $Ux = y$ (regressiva) |
> |---|---|---|
> | $(6, 26, 16)$ | $y = \left(6,\ 26 - 42,\ 16 - 24 - \tfrac{16}{3}\right) = \left(6, -16, -\tfrac{40}{3}\right)$ | $x = (1, 1, 1)$ |
> | $(-1, 6, 5)$ | $y = \left(-1,\ 6 + 7,\ 5 + 4 + \tfrac{13}{3}\right) = \left(-1, 13, \tfrac{40}{3}\right)$ | $x = (2, 0, -1)$ |
>
> Na regressiva do $b_2$ : $x_3 = \frac{40/3}{-40/3} = -1$ ; $-3x_2 - 13(-1) = 13 \Rightarrow x_2 = 0$ ; $x_1 = -1 - 2 \cdot 0 - 3(-1) = 2$. Confira : $A \cdot (2, 0, -1) = (2 - 3,\ 14 - 8,\ 8 - 3) = (-1, 6, 5)$ ✓.
> **Pivoteamento** : o parcial trocaria as linhas 1 e 2 para usar o $7$ como pivô, o maior em módulo da coluna. Com pivô $1$, o multiplicador vale $7$ e cada erro de arredondamento da linha 1 entra **multiplicado por 7** na linha 2 ; com pivô $7$, todo multiplicador fica com $|\ell| \le 1$ e os erros não crescem nessa etapa. Em aritmética exata tanto faz — por isso a conta acima fecha. Com a troca, a fatoração vira $PA = LU$, e $P$ (a permutação) também é guardada e reaplicada a cada $b$ novo.
>
> **e)** Gauss a cada vez : $100 \times \tfrac23 (1000)^3 \approx 6{,}7 \times 10^{10}$ operações.
> LU : $\tfrac23 (1000)^3 \approx 6{,}7 \times 10^{8}$ uma vez, mais $100 \times 2(1000)^2 = 2 \times 10^{8}$ nas substituições — total $\approx 8{,}7 \times 10^{8}$. **Cerca de 77 vezes menos.** É a resposta ao "*mas será que custa muito?*" da aula15 : a fatoração custa o mesmo que um Gauss, e cada $b$ novo sai quase de graça.
>
> **f)** Isolando : $x = \frac{7 - 2y - 4z - 5w}{-8}$, $y = \frac{10 + x - 3z - w}{-4}$, $z = \frac{4 - 3x - y + w}{2}$, $w = \frac{-3 + 2x + 3y + z}{3}$.
>
> | Iteração | Jacobi $(x, y, z, w)$ | Seidel $(x, y, z, w)$ |
> |---|---|---|
> | 0 | $(1,\ 1,\ 1,\ 1)$ | $(1,\ 1,\ 1,\ 1)$ |
> | 1 | $(0{,}5;\ -1{,}75;\ 0{,}5;\ 1)$ | $(0{,}5;\ -1{,}625;\ 2{,}5625;\ -1{,}4375)$ |
> | 2 | $(-0{,}4375;\ -2;\ 2{,}625;\ -2{,}25)$ | $(-0{,}8984;\ -0{,}7129;\ 2{,}9854;\ -1{,}3167)$ |
>
> Solução exata : $\left(-\frac{101}{182},\ -\frac{135}{182},\ \frac{67}{26},\ -\frac{114}{91}\right) \approx (-0{,}5549;\ -0{,}7418;\ 2{,}5769;\ -1{,}2527)$. Depois de 2 iterações o Seidel já está a menos de $0{,}41$ da solução em todas as coordenadas ; o Jacobi ainda erra $w$ por $1$.
> **Dominância diagonal** : linha 1, $8$ contra $2 + 4 + 5 = 11$ ✗ ; linha 2, $4$ contra $5$ ✗ ; linha 3, $2$ contra $5$ ✗ ; linha 4, $3$ contra $6$ ✗. **Nenhuma** linha domina — e os dois convergem mesmo assim.
> Estimativa : o erro cai por $\rho$ a cada passo, então $n \approx \ln(10^{-6}) / \ln \rho$. Jacobi : $-13{,}8 / \ln 0{,}843 \approx -13{,}8 / -0{,}171 \approx 81$ ; Seidel : $-13{,}8 / \ln 0{,}593 \approx -13{,}8 / -0{,}523 \approx 26$. Rodando de verdade, com o critério "maior diferença entre iterações $< 10^{-6}$" : **85** e **30** — o Seidel quase **3 vezes** mais rápido, como o professor prometeu.
> O que os dois sistemas têm em comum : **nenhum é diagonalmente dominante**, então nenhuma regra garante coisa alguma de antemão. O que decide é só o raio espectral de cada matriz de iteração : aqui $\rho(T_S) = 0{,}593 < \rho(T_J) = 0{,}843$, e o Seidel ganha ; no sistema da aula14, $\rho(T_S) = 1{,}059 > 1$, e ele diverge. Mesmos métodos, resultados opostos — a "intuição" do valor novo só vale quando a matriz ajuda.

> [!success]- **Questão 5 — Ceres**
> **a)** As notas : "*usado o elevado ao quadrado pra não usar o módulo*". O motivo de fundo é que $|u|$ **não é derivável** em $u = 0$, e o método inteiro consiste em derivar e igualar a zero. O quadrado é derivável em toda parte, e a derivada de $(f(x_i) - y_i)^2$ é linear nos parâmetros quando $f$ é — é isso que transforma o problema num sistema **linear**. Efeito colateral : o quadrado pune muito os erros grandes, então o ajuste é sensível a pontos fora da curva.
>
> **b)** $n = 5$, $\sum x = 10$, $\sum x^2 = 30$, $\sum y = 17$, $\sum xy = 0 + 2 + 8 + 12 + 24 = 46$.
> $$\begin{cases} 30a + 10b = 46 \\ 10a + 5b = 17 \end{cases} \ \Rightarrow\ a = 1{,}2,\quad b = 1 \qquad F(x) = 1{,}2x + 1$$
>
> | $x_i$ | $y_i$ | $F(x_i)$ | Resíduo $y_i - F(x_i)$ |
> |---|---|---|---|
> | 0 | 1 | 1,0 | 0 |
> | 1 | 2 | 2,2 | −0,2 |
> | 2 | 4 | 3,4 | 0,6 |
> | 3 | 4 | 4,6 | −0,6 |
> | 4 | 6 | 5,8 | 0,2 |
>
> Soma dos quadrados : $0 + 0{,}04 + 0{,}36 + 0{,}36 + 0{,}04 = \mathbf{0{,}8}$. Soma dos resíduos : **exatamente 0**. Não é coincidência : a equação normal da derivada em relação a $b$ é $\sum (F(x_i) - y_i) \cdot 1 = 0$, que é literalmente "a soma dos resíduos é zero". Todo modelo com termo constante tem essa propriedade.
>
> **c)** Cada equação vem de multiplicar pela derivada de $F$ em relação ao parâmetro : $\partial F/\partial b = x$, $\partial F/\partial c = 1$, $\partial F/\partial d = \cos x$.
> $$\begin{pmatrix} \sum x^4 & \sum x^3 & \sum x^2 & \sum x^2\cos x \\ \sum x^3 & \sum x^2 & \sum x & \sum x\cos x \\ \sum x^2 & \sum x & n & \sum \cos x \\ \sum x^2\cos x & \sum x\cos x & \sum \cos x & \sum \cos^2 x \end{pmatrix} \begin{pmatrix} a \\ b \\ c \\ d \end{pmatrix} = \begin{pmatrix} \sum y\,x^2 \\ \sum y\,x \\ \sum y \\ \sum y\cos x \end{pmatrix}$$
> (somas sobre $i$, índices omitidos.) O padrão : a entrada $(j, k)$ é $\sum \varphi_j(x_i)\,\varphi_k(x_i)$, com funções-base $\varphi = (x^2, x, 1, \cos x)$. A matriz é **simétrica** — e, se as funções-base forem independentes nos pontos, **definida positiva**. O lado direito é $\sum y_i\,\varphi_j(x_i)$. Resolve-se por Gauss, ou pelo "Gauss recursivo" que o JB mencionou.
>
> **d)** Os dados têm **ruído** : medições reais, como as posições de Ceres, carregam erro. Um polinômio de grau 4 passa exatamente pelos 5 pontos, ou seja, ajusta o ruído junto com a tendência — é **interpolação**, não ajuste. Entre os pontos ele oscila, e fora deles (extrapolação, o que Gauss precisava fazer) diverge. A reta erra um pouco em cada ponto e acerta a tendência. "Não uma função que siga **EXATAMENTE** cada pontinho, mas uma média" — as notas já disseram.
>
> **e)** $\partial F/\partial b = a\,x\,e^{bx}$ : a incógnita $b$ fica dentro da exponencial, e as equações normais passam a ter termos como $\sum x_i e^{2bx_i}$, que não são lineares em $b$. Gauss não serve mais.
> Linearização : $\ln F = \ln a + b\,x$. Com $Y_i = \ln y_i$ e $A = \ln a$, ajusta-se a **reta** $Y = A + bx$ pelas equações normais do item **b**, e depois $a = e^{A}$.
> O que muda : passa-se a minimizar $\sum (\ln F(x_i) - \ln y_i)^2$, que é aproximadamente o erro **relativo**, não o absoluto. Os pontos de $y$ pequeno ganham peso. O resultado costuma ser bom, mas **não é** o ajuste de mínimos quadrados original — para esse, é preciso um método iterativo não linear (Gauss–Newton), com o resultado linearizado como chute inicial.
>
> **f)** Somas com $t = 0, \ldots, 7$ : $n = 8$, $\sum t = 28$, $\sum t^2 = 140$, $\sum y = 463\,976$, $\sum t\,y = 1\,569\,272$.
> $$\begin{cases} 140a + 28b = 1\,569\,272 \\ 28a + 8b = 463\,976 \end{cases} \ \Rightarrow\ a = -\tfrac{27322}{21} \approx -1301{,}05, \quad b = \tfrac{187652}{3} \approx 62\,550{,}67$$
> Reta : $F(t) \approx -1301{,}05\,t + 62\,550{,}67$. Soma dos quadrados dos resíduos $\approx 6{,}90 \times 10^{8}$. Previsão para 2021 ($t = 8$) : $\approx$ **52 142 t**.
> Cúbica : as equações normais usam $\sum t^3 = 784$, $\sum t^4 = 4676$, $\sum t^5 = 29\,008$, $\sum t^6 = 184\,820$ — é a matriz simétrica da Questão 5c com base $(t^3, t^2, t, 1)$. Resultado : $F(t) \approx 632{,}75\,t^3 - 5329{,}37\,t^2 + 6898{,}17\,t + 65\,108{,}15$, soma dos quadrados $\approx 1{,}62 \times 10^{8}$ (quatro vezes menor). Previsão para 2021 : $\approx$ **103 180 t**.
> Nenhuma das duas merece confiança para prever. A reta erra a **forma** : os dados caem até 2017 e sobem desde então, e ela prevê queda justamente quando a série se recupera. A cúbica pega o "V", mas fora dos dados o termo $t^3$ domina e a previsão salta 55% acima de 2020 — é a extrapolação que o enunciado chama de "atividade perigosa". Ajuste melhor **dentro** dos dados não quer dizer previsão melhor **fora** deles (mesmo argumento da Questão 5d). Se for para usar uma, a cúbica com desconfiança, ou uma reta só dos anos de recuperação.

> [!success]- **Questão 6 — Cancelamento catastrófico**
> **a)** Em $[0{,}99;\ 1{,}01]$ o gráfico é a cúbica lisa esperada, com o ponto de inflexão achatado em $x = 1$. Apertando a janela, a curva vira uma **escada** de degraus aleatórios. Em `double`, na janela $[0{,}999975;\ 1{,}000025]$, os valores calculados (avaliando da esquerda para a direita) saem todos múltiplos de $2^{-51} \approx 4{,}44 \times 10^{-16}$ :
>
> | $x - 1$ | $f(x)$ expandida | $(x - 1)^3$ exato | Erro relativo |
> |---|---|---|---|
> | $10^{-2}$ | $1{,}0000000006 \times 10^{-6}$ | $10^{-6}$ | $6 \times 10^{-10}$ |
> | $10^{-4}$ | $1{,}0000889 \times 10^{-12}$ | $10^{-12}$ | $9 \times 10^{-5}$ |
> | $2{,}5 \times 10^{-5}$ | $1{,}554 \times 10^{-14}$ | $1{,}5625 \times 10^{-14}$ | $0{,}5\%$ |
> | $10^{-5}$ | $8{,}88 \times 10^{-16}$ | $1{,}0 \times 10^{-15}$ | $11\%$ |
> | $3 \times 10^{-6}$ | $4{,}44 \times 10^{-16}$ | $2{,}7 \times 10^{-17}$ | $1500\%$ |
>
> Os termos $x^3$, $3x^2$, $3x$ e $1$ valem cerca de $1$, $3$, $3$ e $1$, e cada um carrega um erro de arredondamento da ordem de $\varepsilon$ vezes seu tamanho — uns $10^{-15}$ no total. A soma é quase zero : os dígitos corretos se cancelam e sobra o erro, que tem **tamanho absoluto fixo**. Quando o valor verdadeiro, $(x-1)^3$, cai abaixo desses $10^{-15}$, o gráfico passa a mostrar **só** o erro.
> $g(x) = x^3$ não sofre : duas multiplicações, sem subtração, com erro **relativo** de no máximo $\approx 2\varepsilon$ em qualquer janela. O gráfico dela continua liso em qualquer zoom (até a própria resolução dos $x$).
> Horner **não** resolve : $((x - 3)x + 3)x - 1$ ainda subtrai números perto de 1 e cancela do mesmo jeito. O que resolve é calcular $(x - 1)^3$ na forma **fatorada** : $x - 1$ é exato perto de 1 (Sterbenz), e o cubo só tem multiplicações. A forma de avaliar importa tanto quanto a fórmula.
>
> **b)** Com 5 termos :
>
> | $x$ | meuexp | $e^x$ | | $x$ | meuexp | $e^x$ |
> |---|---|---|---|---|---|---|
> | 1 | 2,71667 | 2,71828 | | −1 | 0,36667 | 0,36788 |
> | 2 | 7,26667 | 7,38906 | | −2 | 0,06667 | 0,13534 |
> | 3 | 18,4 | 20,0855 | | −3 | **−0,65** | 0,04979 |
> | 5 | 91,4167 | 148,413 | | −5 | **−12,333** | 0,00674 |
>
> Os positivos erram razoavelmente (38% em $x = 5$, e melhoram com mais termos). Os negativos viram **lixo** : exponencial negativa não existe. Há **dois** erros :
> 1. **Truncamento** — o erro de parar a série no 5º termo. Para $x = -5$, os termos são $1, -5, 12{,}5, -20{,}8, 26{,}0, -26{,}0, 21{,}7, \ldots$ : alternam e crescem até $n \approx |x|$, e parar em qualquer ponto deixa um erro do tamanho do próximo termo, perto de 20, contra uma resposta de $0{,}007$. Mais termos resolvem : com 20 termos, $\text{meuexp}(-5) = 0{,}0067455$ ; com 30, bate com $e^{-5}$ em 10 casas.
> 2. **Cancelamento** — mesmo com termos de sobra, a soma alterna parcelas enormes para dar um resultado minúsculo. Em $x = -20$, o maior termo é $20^{20}/20! \approx 4{,}3 \times 10^{7}$ ; o erro de arredondamento é $\approx \varepsilon \times 4{,}3 \times 10^7 \approx 10^{-8}$, **maior** que a resposta $e^{-20} = 2{,}06 \times 10^{-9}$. Com 100 termos, `double` dá $7{,}17 \times 10^{-10}$ (erra por um fator 3) e `float` dá $-2{,}76$.
>
> **c)** Para $x < 0$, $\text{meuexp}(-x) = \text{meuexp}(|x|)$ soma só parcelas **positivas** : não há cancelamento, e o erro relativo fica perto de $\varepsilon$. Inverter um número preserva o erro relativo. Em $x = -20$, com 100 termos, até em `float` : $1/\text{meuexp}(20) = 2{,}0611535 \times 10^{-9}$, contra $e^{-20} = 2{,}0611536 \times 10^{-9}$.
> Ela resolve o **cancelamento**, não o **truncamento** : com os 5 termos originais, $1/\text{meuexp}(5) = 0{,}01094$, contra $0{,}00674$ — positivo e com cara de exponencial, mas ainda 62% errado, porque $\text{meuexp}(5) = 91{,}4$ já estava longe de $148{,}4$. A ideia de última hora conserta o método, e o número de termos continua sendo problema seu.
>
> **d)** Multiplicando pelo conjugado : $\left(\sqrt{x^2 + 1} - 1\right)\dfrac{\sqrt{x^2 + 1} + 1}{\sqrt{x^2 + 1} + 1} = \dfrac{(x^2 + 1) - 1}{\sqrt{x^2 + 1} + 1} = \dfrac{x^2}{\sqrt{x^2 + 1} + 1}$.
>
> | $x$ | $f(x)$ | $g(x)$ |
> |---|---|---|
> | $10^{-3}$ | $4{,}99999875059 \times 10^{-7}$ | $4{,}99999875000 \times 10^{-7}$ |
> | $10^{-5}$ | $5{,}0000004 \times 10^{-11}$ | $4{,}9999999999 \times 10^{-11}$ |
> | $10^{-7}$ | $4{,}885 \times 10^{-15}$ | $5{,}000 \times 10^{-15}$ |
> | $10^{-8}$ | $\mathbf{0}$ | $5{,}000 \times 10^{-17}$ |
>
> $g$ é a certa : não subtrai nada, e o valor é $\approx x^2/2$, como a série de Taylor manda. $f$ perde dígitos progressivamente — cada vez que $x$ cai por 10, $x^2 + 1$ fica 100 vezes mais perto de 1 e $f$ perde duas casas. Zera de vez quando $x^2 < \varepsilon/2 = 2^{-53}$, isto é, $|x| \lesssim 1{,}05 \times 10^{-8}$ : aí $x^2 + 1$ arredonda para exatamente $1$ (objetiva 17). No gráfico perto de zero, $g$ desenha a parábola $x^2/2$ e $f$ desenha uma escada que termina num patamar em zero.

> [!success]- **Questão 7 — O polinômio do JB**
> **a)** $p(x)$ : coeficientes não nulos $+1,\ +18,\ +34,\ -493,\ +1431$ → **2 trocas** → 2 ou 0 positivas.
> $p(-x) = -x^5 - 18x^3 + 34x^2 + 493x + 1431$ : $-,\ -,\ +,\ +,\ +$ → **1 troca** → **exatamente 1** negativa.
> Cenários (positivas, negativas, complexas) : $(2, 1, 2)$ ou $(0, 1, 4)$.
>
> **b)** Lagrange : $\max(1,\ 0 + 18 + 34 + 493 + 1431) = \mathbf{1976}$. Cauchy : $1 + 1431 = \mathbf{1432}$. Cauchy é a melhor das duas.
> Fujiwara : $2 \max\left\{0,\ \sqrt{18},\ \sqrt[3]{34},\ \sqrt[4]{493},\ \sqrt[5]{1431/2}\right\} = 2 \max\{0;\ 4{,}243;\ 3{,}240;\ 4{,}712;\ 3{,}720\} = \mathbf{9{,}42}$.
> O maior módulo de raiz é $5{,}758$. Cauchy exagera **250 vezes**, Fujiwara menos de 2. Lagrange e Cauchy usam $|a_i/a_n|$ **sem raiz** : com $a_n = 1$ e $a_0 = 1431$, a cota fica do tamanho do termo constante. Mas uma raiz $z$ só "sente" $a_0$ através de $|z|^5$ — é o que Fujiwara modela tirando a raiz $k$-ésima de cada razão. Na prática, a cota de Cauchy manda procurar em $[-1432, 1432]$ ; a de Fujiwara, em $[-9{,}42;\ 9{,}42]$.
>
> **c)** É o método de **Horner** : imprime $x$ e $p(x)$. Os valores de `p` a cada volta :
>
> | $x$ | Voltas do laço | $p(x)$ |
> |---|---|---|
> | 2 | $1,\ 2,\ 22,\ 78,\ -337,\ 757$ | **757** |
> | −4 | $1,\ -4,\ 34,\ -102,\ -85,\ 1771$ | **1771** |
> | −5 | $1,\ -5,\ 43,\ -181,\ 412,\ -629$ | **−629** |
>
> $p(-5) < 0 < p(-4)$ : a raiz negativa que Descartes garantiu está em $(-5, -4)$. Os valores intermediários são também os coeficientes do quociente de $p$ por $(x - x_0)$ — a deflação da Questão 2d, de graça.
>
> **d)** `q` é a derivada : o laço aplica Horner, ao mesmo tempo, a $p$ e ao quociente que vai se formando, e a derivada de $p$ em $x_0$ é esse quociente avaliado em $x_0$. Imprime $x$, $p(x)$ e $p'(x)$. Para $x = -5$, os pares (`p`, `q`) são $(1, 0)$, $(-5, 1)$, $(43, -10)$, $(-181, 93)$, $(412, -646)$, $(-629, 3642)$ : $p(-5) = -629$ e $p'(-5) = 3642$.
> À mão : $p'(x) = 5x^4 + 54x^2 + 68x - 493$ ; $p'(-5) = 3125 + 1350 - 340 - 493 = 3642$ ✓. Um laço, $2n$ multiplicações, e sai tudo o que Newton precisa.
>
> **e)** Newton, $x_0 = -5$ : $-4{,}8272927$ ; $-4{,}8136623$ ; $-4{,}81358187463$ ; $-4{,}813581871848786$, e a 5ª repete. **4 iterações**. Secante, $x_0 = -6$, $x_1 = -5$ : $-4{,}88399$ ; $-4{,}81890$ ; $-4{,}813740$ ; $-4{,}8135822335$ ; $-4{,}81358187187$ ; $-4{,}813581871848786$. **6 iterações**, com uma avaliação cada (contra duas de Newton) — de novo a objetiva 13.
> Newton real a partir de $x_0 = 2$ : $14{,}41$ ; $11{,}43$ ; $9{,}03$ ; $7{,}10$ ; $5{,}53$ ; $4{,}25$ ; $3{,}12$ ; $1{,}64$ ; $5{,}65$ ; $4{,}35$ ; … — vaga pelo semieixo positivo **sem convergir**. Não há o que achar : no semieixo positivo o mínimo de $p$ é $\approx 753$, perto de $x = 2{,}13$. O cenário de Descartes é o $(0, 1, 4)$ : as 2 "possíveis" positivas são um par complexo.
>
> **f)** As raízes : $\mathbf{-4{,}813582}$, $\mathbf{2{,}501703 \pm 1{,}645720\,i}$ e $\mathbf{-0{,}094912 \pm 5{,}757119\,i}$ (módulos $4{,}81$, $2{,}99$ e $5{,}76$ — todas dentro da cota de Fujiwara). Partindo de $1 + i$ ou de $2i$, Newton complexo cai em $2{,}5017 + 1{,}6457i$ ; de $5i$ ou $6i$, em $-0{,}0949 + 5{,}7571i$. As conjugadas vêm de graça : $p(\bar z) = \overline{p(z)}$.
> Por que "**tentar**" :
> 1. Com coeficientes reais e **chute real**, toda a iteração fica real — Newton nunca sai do eixo e nunca acha raiz complexa. É preciso chutar fora do eixo.
> 2. **Qual** raiz sai depende do chute, e as fronteiras entre as bacias de atração são **fractais** (as imagens do ExLab 1 · 11) : chutes vizinhos podem ir para raízes diferentes, e nada garante que algum chute seu caia na bacia de cada raiz.
> 3. Pode **não convergir** : passar perto de um ponto com $p'(z) \approx 0$ joga o iterado longe, e existem ciclos (o item **e** mostra uma dança parecida no eixo real).
> 4. Raízes **múltiplas** ou muito próximas fazem a convergência cair para linear (objetiva 12).
>
> A **deflação** ataca 2 : depois de achar $r$, divide-se $p$ por $(x - r)$ — ou, para um par complexo, por $x^2 - 2\,\text{Re}(r)\,x + |r|^2$, mantendo os coeficientes reais — e a raiz achada deixa de existir para os próximos chutes. Deflacionando pela negativa, sobra a quártica $x^4 - 4{,}8136x^3 + 41{,}171x^2 - 164{,}178x + 297{,}284$, com resto $\approx 9 \times 10^{-13}$.
>
> **g)** Divisão sintética :
> - por $x = 6$ : $1,\ -14,\ 71,\ -154,\ 120\ |\ 0$ → $p'(x) = x^4 - 14x^3 + 71x^2 - 154x + 120$ ;
> - por $x = 5$ : $1,\ -9,\ 26,\ -24\ |\ 0$ → $p''(x) = x^3 - 9x^2 + 26x - 24$, com raízes $2, 3, 4$ (é o $p_3$ da Questão 3g).
>
> Com $6{,}0001$ no lugar de $6$, o resto é $\approx 0{,}0024$, e o quociente — que o plano manda usar como se o resto fosse zero — tem raízes $2{,}0001$ ; $2{,}9996$ ; $4{,}0006$ ; $4{,}9996$. Um erro de $10^{-4}$ na raiz achada virou erro de até $6 \times 10^{-4}$ nas outras.
> Problemas do plano :
> 1. Toda raiz achada é **aproximada**, e o quociente tem os coeficientes errados por isso. Cada raiz nova sai de um polinômio **perturbado**, e os erros se **acumulam** de etapa em etapa.
> 2. Raízes de polinômios com raízes próximas são **sensíveis** aos coeficientes : mudar só o coeficiente de $x^4$ por $10^{-6}$ (de $-20$ para $-19{,}999999$) desloca a raiz 5 em $1{,}04 \times 10^{-4}$ — cem vezes mais. É o fenômeno do polinômio de **Wilkinson**, com raízes $1, 2, \ldots, 20$.
> 3. Com raízes complexas, a divisão por $(x - r)$ gera coeficientes complexos, a não ser que se divida pelo par.
>
> Como contornar :
> - **Polir** cada raiz : usar a raiz do polinômio deflacionado só como chute e rodar Newton no $p$ **original**, que não tem erro acumulado.
> - Deflacionar começando pelas raízes de **menor módulo**, que é a ordem numericamente estável para a divisão sintética progressiva.
> - Conferir cada raiz final no $p$ original : $|p(r)|$ tem de ser pequeno.

> [!success]- **Questão 8 — Modelagem com sistemas lineares**
> **a)** Seja $x_A, x_B, x_C, x_D$ o número de pessoas por hora que brincam em cada um. De A saem $\tfrac12 x_A$ para B e $\tfrac16 x_A$ para cada um de C, D e "embora" ; de C, $\tfrac12 x_C$ para B e $\tfrac16 x_C$ para A, D e "embora" ; de B e de D, $\tfrac13$ para cada um de A, C e D. Balanço (entra = brinca) :
> $$\begin{cases} x_A = 20 + \tfrac13 x_B + \tfrac16 x_C + \tfrac13 x_D \\ x_B = \tfrac12 x_A + \tfrac12 x_C \\ x_C = 10 + \tfrac16 x_A + \tfrac13 x_B + \tfrac13 x_D \\ x_D = \tfrac16 x_A + \tfrac13 x_B + \tfrac16 x_C + \tfrac13 x_D \end{cases} \iff \begin{pmatrix} 1 & -\tfrac13 & -\tfrac16 & -\tfrac13 \\ -\tfrac12 & 1 & -\tfrac12 & 0 \\ -\tfrac16 & -\tfrac13 & 1 & -\tfrac13 \\ -\tfrac16 & -\tfrac13 & -\tfrac16 & \tfrac23 \end{pmatrix} \begin{pmatrix} x_A \\ x_B \\ x_C \\ x_D \end{pmatrix} = \begin{pmatrix} 20 \\ 0 \\ 10 \\ 0 \end{pmatrix}$$
> (O $\tfrac23$ é porque um terço de quem sai de D volta para D.) Da 4ª equação com a 2ª sai $x_D = x_B$ ; substituindo, $x_A = 30 + \tfrac34 x_C$ e $x_C = 15 + \tfrac34 x_A$. Resultado :
> $$x_A = \tfrac{660}{7} \approx 94{,}3, \qquad x_B = 90, \qquad x_C = \tfrac{600}{7} \approx 85{,}7, \qquad x_D = 90$$
> Conservação : só se sai do parque a partir de A e de C, com $\tfrac16$ de cada — $\tfrac16\left(\tfrac{660}{7} + \tfrac{600}{7}\right) = \tfrac{1260}{42} = \mathbf{30}$ por hora, exatamente as $20 + 10$ que entram ✓. Cada visitante brinca em média $360/30 = 12$ vezes.
>
> **b)** $p(x) = ax^3 + bx^2 + cx + d$, uma equação por ponto :
> $$\begin{pmatrix} -1 & 1 & -1 & 1 \\ 0 & 0 & 0 & 1 \\ 1 & 1 & 1 & 1 \\ 8 & 4 & 2 & 1 \end{pmatrix} \begin{pmatrix} a \\ b \\ c \\ d \end{pmatrix} = \begin{pmatrix} -3 \\ -1 \\ 2 \\ -2 \end{pmatrix}$$
> $d = -1$ sai de graça, porque $x = 0$ zera todos os outros termos. Sobram : $-a + b - c = -2$ ; $a + b + c = 3$ ; $8a + 4b + 2c = -1$. Somando as duas primeiras, $b = \tfrac12$ ; daí $a + c = \tfrac52$ e $8a + 2c = -3$, logo $a = -\tfrac43$, $c = \tfrac{23}{6}$.
> $$p(x) = -\tfrac43 x^3 + \tfrac12 x^2 + \tfrac{23}{6} x - 1$$
> Confira : $p(2) = -\tfrac{32}{3} + 2 + \tfrac{23}{3} - 1 = -2$ ✓. A matriz de Vandermonde é o jeito "força bruta" de interpolar : funciona, mas fica **mal condicionada** rapidamente com mais pontos — um dos motivos para existirem as formas de Lagrange e de Newton.
>
> **c)** Com $\alpha_A, \ldots, \alpha_D$ as frações de cada substância em $X$, cada componente dá uma equação : $0{,}15\alpha_A + 0{,}36\alpha_B + 0{,}20\alpha_C + 0{,}31\alpha_D = 0{,}26$, e assim por diante. Solução :
> $$\alpha = \left(\tfrac{81}{215},\ \tfrac{269}{645},\ \tfrac{62}{645},\ \tfrac{71}{645}\right) \approx (37{,}67\%;\ 41{,}71\%;\ 9{,}61\%;\ 11{,}01\%)$$
> Soma 1 **antes** de resolver : somando as quatro equações, cada $\alpha_j$ aparece multiplicado pela soma da sua coluna, que é $100\%$ ; o lado direito soma $100\%$. Logo $\alpha_A + \alpha_B + \alpha_C + \alpha_D = 1$ — não é uma equação a mais, é consequência das quatro.
>
> **d)** Mesma matriz, lado direito $(0{,}243;\ 0{,}15;\ 0{,}262;\ 0{,}215)$ :
> $$\alpha \approx (4{,}43\%;\ 22{,}26\%;\ 27{,}95\%;\ 32{,}36\%), \qquad \textstyle\sum \alpha = 87\%$$
> Pelo mesmo argumento de **c**, a soma é obrigatoriamente $87\%$ : $A$ a $D$ formam $87\%$ da massa de $X$, e os outros $13\%$ são as substâncias desconhecidas — **supondo** que elas não contenham nenhum dos componentes $a$ a $d$. Entre as conhecidas, a proporção relativa é $\alpha / 0{,}87 \approx (5{,}1\%;\ 25{,}6\%;\ 32{,}1\%;\ 37{,}2\%)$.
> O "cuidado" : a coluna de $X$ mudou no máximo 4,8 pontos percentuais, e a proporção de $A$ despencou de $37{,}7\%$ para $4{,}4\%$. O número de condição da matriz é $\kappa \approx 22$ : erros relativos no lado direito podem sair multiplicados por até 22 na solução. Se as medições do cromatógrafo têm erro de um ponto, o $4{,}4\%$ de $A$ não é confiável nem no sinal.
>
> **e)** Solução :
> $$\alpha \approx (19{,}97\%;\ 27{,}14\%;\ 46{,}54\%;\ 1{,}49\%), \qquad \textstyle\sum \alpha \approx 95{,}1\%$$
> Agora as colunas de $A$ a $D$ somam só $31\%$, $45\%$, $43\%$ e $39\%$, e o argumento da soma não vale mais : a soma dos $\alpha$ **não precisa** ser 1, nem 87%, nem nada. O que ela diz : $X$ é $\approx 95\%$ mistura de $A$ a $D$, e o resto é algo sem nenhum dos componentes $a$ a $d$. $\kappa \approx 13$.
> Somando $0{,}1$ ponto a uma entrada da coluna de $X$ por vez, $\alpha_D$ vira $2{,}11\%$, $1{,}92\%$, $1{,}33\%$ ou $0{,}99\%$. Uma mudança de $0{,}1$ ponto na medida — menos que a precisão típica de um cromatógrafo — mexe **até 40%** na proporção de $D$, em qualquer dos dois sentidos. Não dá para afirmar que $D$ está na mistura : $1{,}5\%$ é compatível com zero dentro do erro de medida. Se os dados fossem um pouco piores, o sistema poderia até devolver uma proporção **negativa**, fisicamente impossível ; nesse caso o problema certo é mínimos quadrados **com restrição** $\alpha \ge 0$, e não Gauss.

> [!success]- **Parte IV — Estudos de caso**
> **1. Patriot.** $0{,}1$ não tem representação finita em binário : $0{,}1 = 0{,}0\overline{0011}_2$. Truncado no registrador de 24 bits, cada décimo de segundo carregava um erro de $\approx 9{,}5 \times 10^{-8}$ s. Em 100 horas são $3{,}6 \times 10^6$ décimos : $3{,}6 \times 10^6 \times 9{,}5 \times 10^{-8} \approx 0{,}34$ s de atraso no relógio. Um Scud viaja a ~1,7 km/s, então a janela de rastreamento foi posicionada a mais de meio quilômetro do alvo. É o **erro de representação** acumulado **linearmente** por truncamento — o mesmo mecanismo de Vancouver, com consequências piores. Correções : contar o tempo em inteiros (décimos) e converter só no fim ; ou reiniciar o sistema periodicamente, que foi a instrução operacional emitida — o patch chegou a Dhahran um dia depois do ataque.
>
> **2. Ariane 5.** **Overflow** na conversão : o valor de velocidade horizontal do Ariane 5, mais rápido que o Ariane 4, passava de $32\,767$, o maior inteiro de 16 bits com sinal. A conversão levantou uma exceção não tratada, o sistema de navegação desligou, e o de reserva — rodando o **mesmo** código — já tinha falhado da mesma forma. Não foi erro de ponto flutuante, foi erro de **faixa** : um valor representável num formato e não no outro. Correção : checar a faixa antes de converter (saturar em vez de estourar), ou revalidar as premissas do código herdado para a nova trajetória. O módulo que falhou nem era necessário depois da decolagem.
>
> **3. Pentium FDIV.** A divisão usava o algoritmo **SRT**, que obtém vários bits do quociente por passo consultando uma tabela ; 5 entradas deveriam valer 2 e estavam em 0. O erro aparecia em cerca de 1 divisão aleatória em 9 bilhões, e chegava à 5ª casa significativa — muito acima de $\varepsilon$. É uma violação do requisito central do IEEE 754 : toda operação básica deve dar o resultado **exato arredondado** (*correctly rounded*). Correção : a tabela corrigida no hardware ; como paliativo, compiladores passaram a detectar os operandos perigosos e reescalar a divisão. Foi descoberto por Thomas Nicely calculando somas de recíprocos de primos gêmeos — trabalho numérico que exigia divisões exatas.

---
### Ver também
- [IA/dicionario-2.md](../IA/dicionario-2.md) — os conceitos cobrados aqui, em ordem alfabética e por bloco.
- [IA/adicoes-2.md](../IA/adicoes-2.md) — o aprofundamento das aulas 02 a 10 de 2026/2 (IEEE 754, polinômios, solução de equações).
- [IA/adicoes.md](../IA/adicoes.md) — 2026/1 : Gauss-Jacobi, decomposição LU e mínimos quadrados aparecem aprofundados nas aulas 16, 19 e 20.
- [exlab-resolucao.md](./exlab-resolucao.md) — resolução dos ExLabs 1–3, com o mesmo conteúdo em outra ordem.
- [ExLab 1](./exlab1.pdf) & [ExLab 2](./exlab2.pdf) — folhas de laboratório de solução de equações e sistemas lineares.
- [lista.pdf](./lista.pdf) — lista geral do professor ; os blocos de ponto flutuante, equações, sistemas lineares e o exercício 6 de interpolação estão incorporados aqui.
