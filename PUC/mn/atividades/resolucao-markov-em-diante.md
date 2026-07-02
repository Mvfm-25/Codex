# Resolução da lista — de "Cadeias de Markov" em diante

> Métodos Numéricos — Prof. João B. Oliveira
> Cobre: **Cadeias de Markov**, **Interpolação**, **Diferenciação automática** e **Sistemas dinâmicos**.
> Todos os valores numéricos foram conferidos computacionalmente (NumPy).

**Convenção usada em toda a seção de Markov:** trabalho com o vetor de estado como **vetor-linha** $v$ e matriz de transição $P$ com $P_{ij}=\Pr(\text{ir de } i \text{ para } j)$ (linhas somam 1). A evolução de um passo é $v' = vP$. A distribuição estacionária $\pi$ satisfaz $\pi = \pi P$ com $\sum_i \pi_i = 1$ (autovetor à esquerda de autovalor 1).

---

## Cadeias de Markov

### 1. Sorveteria (Sim/Não)

Estados: `Sim`, `Não`. Da tabela (linha = resposta atual, coluna = próxima):

$$P=\begin{bmatrix}0{,}7 & 0{,}3\\ 0{,}6 & 0{,}4\end{bmatrix}$$

**Longo prazo (estacionária).** Resolvo $\pi=\pi P$, com $\pi=(s,n)$, $s+n=1$:

$$s = 0{,}7s + 0{,}6n \;\Rightarrow\; 0{,}3s = 0{,}6n \;\Rightarrow\; s = 2n.$$

Com $s+n=1$: $n=\tfrac13,\; s=\tfrac23$. Logo, **a longo prazo $\approx 667$ dos 1000** clientes acham o chocolate o melhor (e 333 não).

**Quarta visita.** A pergunta depende da distribuição inicial (o enunciado não a fornece). O ponto importante é que a convergência é rápida — em 3–4 passos já se está praticamente no regime estacionário, **qualquer que seja o começo**:

| Visita | começando "todos Sim" | começando "todos Não" | começando 50/50 |
|---|---|---|---|
| 1 (inicial) | 1000 | 0 | 500 |
| 2 | 700 | 600 | 650 |
| 3 | 670 | 660 | 665 |
| 4 | 667 | 666 | 666{,}5 |
| 5 | 666{,}7 | 666{,}6 | 666{,}6 |

**Resposta:** na 4ª visita já são **≈ 667 clientes** (independentemente do início), e a longo prazo o valor se fixa em **2/3 ≈ 667 "Sim" / 333 "Não"**.

---

### 2. Times de futebol (Trêmio, Intencional, Cassis)

As probabilidades dadas são de *troca*; a probabilidade de ficar é o complemento. Ordem $[T,I,C]$:

- $T$ fica: $1-0{,}12-0{,}10=0{,}78$
- $I$ fica: $1-0{,}08-0{,}07=0{,}85$
- $C$ fica: $1-0{,}11-0{,}09=0{,}80$

$$P=\begin{bmatrix}0{,}78 & 0{,}12 & 0{,}10\\ 0{,}07 & 0{,}85 & 0{,}08\\ 0{,}11 & 0{,}09 & 0{,}80\end{bmatrix}$$

Estado inicial (ano 0): $T=10000,\ I=11000,\ C=6000$ (total $27000$, que se conserva pois as linhas somam 1).

Evolução ano a ano ($v'=vP$):

| Ano | Trêmio | Intencional | Cassis |
|---|---|---|---|
| 0 | 10000 | 11000 | 6000 |
| 1 | 9230 | 11090 | 6680 |
| 2 | 8711 | 11135 | 7154 |
| 3 | 8361 | 11154 | 7485 |
| 4 | 8126 | 11158 | 7717 |
| 5 | 7968 | 11154 | 7878 |
| 6 | 7862 | 11146 | 7992 |
| 8 | 7745 | 11128 | 8127 |
| 10 | 7694 | 11112 | 8194 |
| 12 | 7672 | 11101 | 8227 |

**Estabilização (estacionária $\pi$):** $\pi \approx (0{,}2836,\ 0{,}4104,\ 0{,}3060)$, ou seja

$$T \approx 7657,\quad I \approx 11082,\quad C \approx 8261.$$

Intencional se mantém líder; Cassis cresce à custa do Trêmio até as torcidas estabilizarem por volta desses valores.

---

### 3. Lobo-guará (regiões A, B, C)

Regras: 50% de repetir a região; de $A$ nunca vai para $B$; o restante das saídas se divide igualmente entre as duas outras regiões permitidas.

**(a) Matriz de transições.** Ordem $[A,B,C]$:

$$P=\begin{bmatrix}0{,}5 & 0 & 0{,}5\\ 0{,}25 & 0{,}5 & 0{,}25\\ 0{,}25 & 0{,}25 & 0{,}5\end{bmatrix}$$

- De $A$: repete 50%; a outra metade não pode ir a $B$, então vai toda para $C$.
- De $B$: repete 50%; a outra metade se divide igual entre $A$ e $C$ (25% cada).
- De $C$: repete 50%; a outra metade se divide igual entre $A$ e $B$ (25% cada).

> *Observação de leitura:* o enunciado é levemente ambíguo. Adotei a interpretação consistente com a regra geral "50% de repetir para qualquer região". Se, em vez disso, considerarmos que de $B$ e $C$ ele *nunca* repete (indo 50%/50% para as outras duas), a matriz muda e a resposta de (b) passa a 25% e a estacionária a $(1/2, 1/6, 1/3)$. Sigo com a interpretação principal abaixo.

**(b) Segunda-feira em A → quarta-feira em C (dois passos).**
Segunda: $v_0=(1,0,0)$. Terça: $v_1=v_0P=(0{,}5,\ 0,\ 0{,}5)$.
Quarta: $v_2=v_1P=(0{,}375,\ 0{,}125,\ 0{,}5)$.

$$\Pr(\text{quarta em } C) = \mathbf{0{,}5 = 50\%}.$$

**(c) Fração de longo prazo em B.** Resolvendo $\pi=\pi P$:

$$\pi=\left(\tfrac13,\ \tfrac29,\ \tfrac49\right)\approx(0{,}333,\ 0{,}222,\ 0{,}444).$$

Ele estará caçando em **B em 2/9 ≈ 22,2% das vezes**.

---

### 4. Ricos, Médios, Pobres

**(a) Matriz.** Ordem $[R,M,P]$ (Médios: 30% restante dividido igual = 15%/15%):

$$P=\begin{bmatrix}0{,}70 & 0{,}20 & 0{,}10\\ 0{,}15 & 0{,}70 & 0{,}15\\ 0{,}10 & 0{,}30 & 0{,}60\end{bmatrix}$$

**(b) Pobre → netos Ricos (2 gerações).** Começo $v_0=(0,0,1)$.
$v_1 = (0{,}10,\ 0{,}30,\ 0{,}60)$; $v_2 = v_1P = (0{,}175,\ 0{,}41,\ 0{,}415)$.

$$\Pr(\text{neto Rico}) = \mathbf{0{,}175 = 17{,}5\%}.$$

**(c) Bisnetos (3 gerações).** $v_3 = v_2P = (0{,}2255,\ 0{,}4465,\ 0{,}328)$.

$$\Pr(\text{bisneto Rico}) = \mathbf{0{,}2255 \approx 22{,}55\%}.$$

**(d) Proporção de longo prazo.** $\pi=\pi P$ dá

$$\pi \approx (0{,}3061,\ 0{,}4490,\ 0{,}2449) \;=\; (30{,}6\%\ R,\ 44{,}9\%\ M,\ 24{,}5\%\ P).$$

**(e) Com redistribuição** (Pobres: 50% P, 40% M, 10% R):

$$P_e=\begin{bmatrix}0{,}70 & 0{,}20 & 0{,}10\\ 0{,}15 & 0{,}70 & 0{,}15\\ 0{,}10 & 0{,}40 & 0{,}50\end{bmatrix}
\;\Rightarrow\; \pi_e \approx (0{,}3103,\ 0{,}4828,\ 0{,}2069).$$

Isto é, **31,0% Ricos, 48,3% Médios, 20,7% Pobres** — a fração de Pobres cai de ~24,5% para ~20,7% e a classe Média cresce.

---

### 5. Jogo de dados (Guilherme × Christian)

Cada jogador tem sua própria cadeia **absorvente** (o estado "venceu" é absorvente). Guilherme precisa do padrão **5–5**; Christian do padrão **5–6**. Como cada processo, isoladamente, atinge seu padrão com **probabilidade 1** se rolar para sempre, a grandeza que realmente distingue os jogadores — e que os diagramas de estados servem para calcular — é o **número esperado de rolagens até vencer** (tempo de absorção).

**Guilherme (5–5).** Estados: `N5` (sem 5 pendente) e `5a` (um 5 na mão). Seja $E_N,E_a$ o número esperado de rolagens até vencer.

$$E_N = 1 + \tfrac16 E_a + \tfrac56 E_N, \qquad E_a = 1 + \tfrac16\cdot 0 + \tfrac56 E_N.$$

Da 1ª: $E_N = 6 + E_a$. Substituindo na 2ª: $E_a = 1 + \tfrac56(6+E_a) \Rightarrow \tfrac16 E_a = 6 \Rightarrow E_a = 36$, e $E_N = \mathbf{42}$.

**Christian (5–6).** Estados: `N5` e `5` (um 5 na mão). Diferença crucial: se ele está com um 5 e tira **outro 5**, *permanece* no estado `5` (continua com um 5 na mão) — daí o auto-laço $1/6$ no diagrama.

$$E_N = 1 + \tfrac16 E_5 + \tfrac56 E_N, \qquad E_5 = 1 + \tfrac16\cdot 0 + \tfrac16 E_5 + \tfrac46 E_N.$$

Da 1ª: $E_N = 6 + E_5$. Na 2ª: $\tfrac56 E_5 = 1 + \tfrac46(6+E_5) \Rightarrow \tfrac16 E_5 = 5 \Rightarrow E_5 = 30$, e $E_N = \mathbf{36}$.

**Conclusão.** Guilherme espera **42** rolagens e Christian **36**. Embora ambos vençam com certeza se jogarem sozinhos indefinidamente, **Christian chega à vitória mais rápido, em média** — o padrão "56" (dois valores distintos) é mais fácil que "55" (par repetido). *(Nota: numa disputa cabeça-a-cabeça com a mesma sequência de dados, a partir do estado "um 5 na mão" as chances de 5 e de 6 são iguais, $1/6$ cada, o que daria 1/2 para cada um; mas os diagramas do enunciado são independentes por jogador, e por isso o resultado relevante é o tempo esperado.)*

---

### 6. Letras A–F em fila (passeio aleatório)

Saltos só para vizinhos: extremos ($A,F$) têm uma vizinha (100%); internas têm duas (50% cada). Ordem $[A,B,C,D,E,F]$:

$$P=\begin{bmatrix}
0 & 1 & 0 & 0 & 0 & 0\\
0{,}5 & 0 & 0{,}5 & 0 & 0 & 0\\
0 & 0{,}5 & 0 & 0{,}5 & 0 & 0\\
0 & 0 & 0{,}5 & 0 & 0{,}5 & 0\\
0 & 0 & 0 & 0{,}5 & 0 & 0{,}5\\
0 & 0 & 0 & 0 & 1 & 0
\end{bmatrix}$$

### 7. Distribuição de longo prazo e letra mais visitada

Para passeio aleatório em grafo, a estacionária é proporcional ao **grau** de cada nó. Graus: $A{=}1,B{=}2,C{=}2,D{=}2,E{=}2,F{=}1$ (soma 10):

$$\pi = \tfrac{1}{10}(1,2,2,2,2,1) = (0{,}1,\ 0{,}2,\ 0{,}2,\ 0{,}2,\ 0{,}2,\ 0{,}1).$$

**As mais visitadas são as quatro letras internas B, C, D, E** (empatadas em 20% cada); $A$ e $F$ são as menos visitadas (10%).

> *Cuidado:* essa cadeia é **periódica** (período 2 — grafo bipartido: a cada passo alterna entre posições pares e ímpares). Portanto $P^n$ **não converge**; quem converge é a **média temporal** das visitas, e é a ela que $\pi$ acima se refere.

### 8. Nova situação: vogais saltam +2 com 2%

Vogais em A–F: **A** e **E**. "Duas posições adiante": $A\to C$ (válido), $E\to G$ (**fora da fila**, não existe). Descontando o 2% das probabilidades já existentes da vogal viável:

- $A$: era $A\to B$ 100%; agora $A\to B$ **98%**, $A\to C$ **2%**.
- $E$: o salto +2 cairia em $G$, inexistente ⇒ $E$ permanece inalterada.

$$P'=\begin{bmatrix}
0 & 0{,}98 & 0{,}02 & 0 & 0 & 0\\
0{,}5 & 0 & 0{,}5 & 0 & 0 & 0\\
0 & 0{,}5 & 0 & 0{,}5 & 0 & 0\\
0 & 0 & 0{,}5 & 0 & 0{,}5 & 0\\
0 & 0 & 0 & 0{,}5 & 0 & 0{,}5\\
0 & 0 & 0 & 0 & 1 & 0
\end{bmatrix}$$

### 9. Nova distribuição e letra mais visitada

Resolvendo $\pi'=\pi'P'$:

$$\pi' \approx (0{,}0986,\ 0{,}1972,\ 0{,}2012,\ 0{,}2012,\ 0{,}2012,\ 0{,}1006).$$

A letra mais visitada **continua sendo uma das internas** — agora $C,D,E$ empatam ligeiramente à frente (≈20,1%) e $B$ cai um pouco (≈19,7%), porque parte do fluxo que ia de $A$ para $B$ passou a "pular" direto para $C$. A conclusão qualitativa (as internas dominam, os extremos são os menos visitados) **não se altera**.

---

## Interpolação

### 1. Parábola por (2,3), (3,5), (5,7)

$p(x)=ax^2+bx+c$ gera o sistema $\{4a+2b+c=3,\ 9a+3b+c=5,\ 25a+5b+c=7\}$, cuja solução é

$$\boxed{p(x) = -\tfrac13 x^2 + \tfrac{11}{3}x - 3.}$$

Raízes de $p(x)=0$: multiplicando por $-3$, $x^2-11x+9=0$, logo

$$x^* = \frac{11\pm\sqrt{85}}{2} \;\Rightarrow\; x^* \approx 0{,}8902 \ \text{ ou } \ 10{,}1098.$$

### 2. Interpolação de Newton — três ordenações

Os quatro pontos são os mesmos $\{(1,2),(3,5),(5,4),(7,8)\}$; só muda a ordem em que Ana, Beto e Carol os usam. **O polinômio interpolador de grau ≤3 por 4 pontos é único** — logo os três encontram o *mesmo* polinômio. O que muda são os coeficientes intermediários (diferenças divididas), não o resultado final.

Diferenças divididas na ordem de Ana:

$$p(x) = 2 + \tfrac32(x-1) - \tfrac12(x-1)(x-3) + \tfrac{3}{16}(x-1)(x-3)(x-5).$$

Expandindo (e o mesmo vale para Beto e Carol, que só têm coeficientes de Newton diferentes):

$$\boxed{p(x) = 0{,}1875\,x^3 - 2{,}1875\,x^2 + 7{,}8125\,x - 3{,}8125.}$$

| Ordenação | Coeficientes de Newton | Polinômio expandido |
|---|---|---|
| Ana $(1,3,5,7)$ | $2,\ 1{,}5,\ -0{,}5,\ 0{,}1875$ | idem |
| Beto $(7,5,3,1)$ | $8,\ 2,\ 0{,}625,\ 0{,}1875$ | idem |
| Carol $(5,1,7,3)$ | $4,\ 0{,}5,\ 0{,}25,\ 0{,}1875$ | idem |

Note que o **coeficiente de maior ordem (0,1875) é sempre o mesmo** — ele é a diferença dividida de todos os pontos, simétrica na ordem. **Explicação:** a unicidade do interpolador garante o mesmo polinômio; a forma de Newton apenas o "monta" em bases diferentes conforme a ordem.

### 3. Aço chinês (extrapolação com polinômio de grau alto)

Usando 1990–1995 (6 pontos → polinômio de **grau 5**) para prever 1996:

| Modelo | Previsão 1996 (real = 107,2) | Previsão 1997 |
|---|---|---|
| Grau 5 (interpola os 6 pontos) | **124,1** ❌ | **189,8** (absurdo) |
| Grau 3 (mín. quadrados) | 108,4 ✅ | 104,5 |
| Grau 2 | 117,6 | 129,4 |
| Grau 1 | 114,2 | 123,2 |

**Interpretação:** o interpolador de grau 5 passa exatamente pelos 6 pontos mas **oscila violentamente fora do intervalo** (fenômeno de Runge), errando o 1996 em ~16% e "explodindo" para 1997. Ajustes de grau baixo (2–3) extrapolam muito melhor. Moral do exercício: **extrapolação com polinômio de grau alto é perigosa**; grau baixo é mais robusto. (A produção real chinesa de ferro-gusa continuou subindo nos anos seguintes, próxima da tendência do grau 3.)

### 4. Ovos (previsão para 2022)

Dados 2016–2021 (mil dúzias). Como o crescimento é claramente suave e quase saturando, comparo modelos:

| Modelo | Previsão 2022 |
|---|---|
| Reta (grau 1) | ≈ 4 317 003 |
| Grau 2 | ≈ 4 063 009 |
| Grau 3 | ≈ 3 842 103 |

A série está **desacelerando** (2020→2021 cresceu pouco), então a reta superestima. Uma previsão razoável fica em torno de **4,0–4,1 milhões de mil dúzias**. Conferir no IBGE (o valor de 2022 ficou próximo de ~4,1 milhões), confirmando que extrapolar com grau baixo é o mais seguro.

### 5. Camarão cultivado (estimar 2017 e prever 2021)

Deixando 2017 de fora e interpolando os outros 7 pontos (grau 6):

| Modelo | Estimativa 2017 (real = 41 078) |
|---|---|
| Grau 6 (interpola os 7 pontos) | **39 930** (erro ~2,8%) |
| Grau 3 | 51 059 |
| Grau 2 | 54 540 |

Curiosamente, aqui o interpolador de grau alto acertou razoavelmente o **ponto interno** 2017 (interpolação, não extrapolação!). Mas para prever **2021** (ponto fora dos dados) o mesmo polinômio de grau alto oscila — por isso o item 6 pede um ajuste por mínimos quadrados, mais estável para extrapolar.

### 6. Mínimos quadrados no camarão (reta e grau 3)

Usando todos os 8 anos (2013–2020), $x=\text{ano}-2013$:

- **Melhor reta:** $y \approx -1301{,}0\,x + 62550{,}7$. Previsão 2021 ($x=8$): **≈ 52 142 ton**.
- **Melhor polinômio de grau 3:** $y \approx 632{,}7\,x^3 - 5329{,}4\,x^2 + 6898{,}2\,x + 65108{,}2$. Previsão 2021 ($x=8$): **≈ 103 180 ton**.

A reta dá uma extrapolação sóbria (~52 mil ton, coerente com a recuperação recente); o grau 3, embora ajuste melhor os dados históricos, **dispara** ao extrapolar (~103 mil ton, implausível). Reforça a lição: **para extrapolar, prefira o ajuste mais simples**.

---

## Diferenciação automática

### 1. $f(x,y,z)=\dfrac{3x^2y}{z} + x\,(y-z)$

#### (a) Decomposição em passos elementares (lista de Wengert)

Uma operação aritmética por passo:

| Passo | Expressão | em (2,3,5) |
|---|---|---|
| $w_1$ | $x$ | 2 |
| $w_2$ | $y$ | 3 |
| $w_3$ | $z$ | 5 |
| $w_4 = w_1 \cdot w_1$ | $x^2$ | 4 |
| $w_5 = 3 \cdot w_4$ | $3x^2$ | 12 |
| $w_6 = w_5 \cdot w_2$ | $3x^2y$ | 36 |
| $w_7 = w_6 / w_3$ | $3x^2y/z$ | 7,2 |
| $w_8 = w_2 - w_3$ | $y-z$ | −2 |
| $w_9 = w_1 \cdot w_8$ | $x(y-z)$ | −4 |
| $w_{10} = w_7 + w_9$ | $f$ | **3,2** |

#### (b) Avaliação

$$f(2,3,5) = \frac{3\cdot 4\cdot 3}{5} + 2\cdot(3-5) = 7{,}2 - 4 = \mathbf{3{,}2}.$$

#### (c) Derivadas parciais em (2,3,5)

**Regras de derivação elementares usadas** (a "tabela de derivadas" do grafo):

| Operação | Forma | Regra aplicada | Derivadas locais |
|---|---|---|---|
| $w_4=w_1\cdot w_1$ | $u\cdot u$ | **regra do produto / potência** | $\partial w_4/\partial w_1 = 2w_1$ |
| $w_5=3\cdot w_4$ | $c\cdot u$ | **múltiplo constante** | $\partial w_5/\partial w_4 = 3$ |
| $w_6=w_5\cdot w_2$ | $u\cdot v$ | **regra do produto** | $\partial/\partial w_5 = w_2,\ \partial/\partial w_2 = w_5$ |
| $w_7=w_6/w_3$ | $u/v$ | **regra do quociente** | $\partial/\partial w_6 = 1/w_3,\ \partial/\partial w_3 = -w_6/w_3^2$ |
| $w_8=w_2-w_3$ | $u-v$ | **regra da soma/diferença** | $\partial/\partial w_2 = 1,\ \partial/\partial w_3 = -1$ |
| $w_9=w_1\cdot w_8$ | $u\cdot v$ | **regra do produto** | $\partial/\partial w_1 = w_8,\ \partial/\partial w_8 = w_1$ |
| $w_{10}=w_7+w_9$ | $u+v$ | **regra da soma** | $\partial/\partial w_7 = 1,\ \partial/\partial w_9 = 1$ |

A **regra da cadeia** costura todas essas derivadas locais ao longo do grafo.

##### Modo reverso (adjuntos) — uma passada dá as três derivadas

Defino o adjunto $\bar w_i = \partial f/\partial w_i$ e propago de trás para frente a partir de $\bar w_{10}=1$, acumulando contribuições (regra da cadeia):

```
w̄10 = 1
w̄7  += w̄10·1                 = 1              (soma)
w̄9  += w̄10·1                 = 1              (soma)
w̄1  += w̄9·w8   = 1·(−2)      = −2             (produto: ∂w9/∂w1 = w8)
w̄8  += w̄9·w1   = 1·2         = 2              (produto: ∂w9/∂w8 = w1)
w̄6  += w̄7·(1/w3) = 1·(1/5)   = 0,2            (quociente)
w̄3  += w̄7·(−w6/w3²) = −36/25 = −1,44          (quociente)
w̄5  += w̄6·w2   = 0,2·3       = 0,6            (produto)
w̄2  += w̄6·w5   = 0,2·12      = 2,4            (produto)
w̄4  += w̄5·3    = 0,6·3       = 1,8            (múltiplo constante)
w̄1  += w̄4·2w1  = 1,8·4       = 7,2            (potência: ∂w4/∂w1 = 2w1)
w̄2  += w̄8·1                  += 2             (diferença)
w̄3  += w̄8·(−1)               += −2            (diferença)
```

Acumulando os adjuntos das entradas:

$$\frac{\partial f}{\partial x} = \bar w_1 = -2 + 7{,}2 = \mathbf{5{,}2}$$
$$\frac{\partial f}{\partial y} = \bar w_2 = 2{,}4 + 2 = \mathbf{4{,}4}$$
$$\frac{\partial f}{\partial z} = \bar w_3 = -1{,}44 - 2 = \mathbf{-3{,}44}$$

Note como as entradas $x,y,z$ recebem **duas contribuições cada** — uma por caminho no grafo (o termo $3x^2y/z$ e o termo $x(y-z)$) — exatamente a regra da cadeia multivariável. O modo reverso é o mais econômico aqui: **uma única passada** produz todas as parciais (por isso o enunciado diz que a regressiva "é mais econômica").

##### Modo progressivo (tangentes) — verificação de $\partial f/\partial x$

Semeando $\dot x=1,\ \dot y=0,\ \dot z=0$ e propagando para frente (cada operação com sua regra):

$$\dot w_4 = 2w_1\dot w_1 = 4,\quad \dot w_5 = 3\dot w_4 = 12,\quad \dot w_6 = \dot w_5 w_2 + w_5 \dot w_2 = 36,$$
$$\dot w_7 = \frac{\dot w_6 w_3 - w_6\dot w_3}{w_3^2} = \frac{180}{25}=7{,}2,\quad \dot w_8 = \dot w_2-\dot w_3 = 0,$$
$$\dot w_9 = \dot w_1 w_8 + w_1\dot w_8 = -2,\quad \dot w_{10} = \dot w_7 + \dot w_9 = \mathbf{5{,}2}.\ \checkmark$$

No modo progressivo, para obter as **três** parciais precisaríamos de três passadas (ou carregar um **vetor** de tangentes $(\dot x,\dot y,\dot z)$ simultaneamente) — daí a observação do enunciado de que "se preferir a progressiva, terá que usar um vetor".

**Conferência analítica** (fecha com a AD):
$$\partial f/\partial x = \tfrac{6xy}{z} + (y-z) = 7{,}2 - 2 = 5{,}2,$$
$$\partial f/\partial y = \tfrac{3x^2}{z} + x = 2{,}4 + 2 = 4{,}4,$$
$$\partial f/\partial z = -\tfrac{3x^2y}{z^2} - x = -1{,}44 - 2 = -3{,}44.\ \checkmark$$

---

## Sistemas dinâmicos

### 1. Função conhecida vs. integração da derivada (Euler)

Com $f(x)=\cos x$, $f'(x)=-\sin x$, $\Delta x=0{,}5$, comparo o valor exato com a reconstrução por Euler $f(x+\Delta x)\approx f(x)+f'(x)\Delta x$ partindo de $f(0)=1$:

| $x$ | $\cos x$ (exato) | Euler | erro |
|---|---|---|---|
| 0,0 | +1,0000 | +1,0000 | 0,0000 |
| 0,5 | +0,8776 | +1,0000 | −0,1224 |
| 1,0 | +0,5403 | +0,7603 | −0,2200 |
| 1,5 | +0,0707 | +0,3396 | −0,2688 |
| 2,0 | −0,4161 | −0,1592 | −0,2570 |
| 3,0 | −0,9900 | −0,9131 | −0,0769 |
| 4,0 | −0,6536 | −0,8082 | +0,1546 |
| 5,0 | +0,2837 | +0,0589 | +0,2247 |

A aproximação segue a **forma** da cossenoide mas **atrasa/defasa** e o erro se acumula. Reduzir $\Delta x$ diminui o erro proporcionalmente (Euler é de 1ª ordem, erro global $O(\Delta x)$).

Programa (Python):

```python
import numpy as np
dx = 0.5
xs = np.arange(0, 5 + 1e-9, dx)
verdadeira = np.cos(xs)
aprox = [1.0]
for i in range(1, len(xs)):
    aprox.append(aprox[-1] + (-np.sin(xs[i-1])) * dx)  # f += f'·dx
# plotar xs × verdadeira e xs × aprox
```

### 2. Decaimento radioativo

Solução exata $N(t)=N_0 e^{-t/\tau}$. A EDO correspondente é $\dfrac{dN}{dt} = -\dfrac{N}{\tau}$, logo o passo de Euler correto é

$$N(t+\Delta t) \approx N(t) - \frac{N(t)}{\tau}\,\Delta t.$$

> ⚠️ **Observação:** a fórmula impressa no enunciado, $N(t+\Delta t)\approx N(t)-\tau N(t)\Delta t$, é inconsistente com $N(t)=N_0e^{-t/\tau}$ (ela corresponderia a $N=N_0e^{-\tau t}$). Uso a versão dimensionalmente coerente $-N/\tau$.

Exemplo $N_0=1000$, $\tau=2$, $\Delta t=0{,}5$:

| $t$ | exato $N_0e^{-t/\tau}$ | Euler |
|---|---|---|
| 0,0 | 1000,00 | 1000,00 |
| 1,0 | 606,53 | 562,50 |
| 2,0 | 367,88 | 316,41 |
| 3,0 | 223,13 | 177,98 |
| 4,0 | 135,34 | 100,11 |
| 5,0 | 82,08 | 56,31 |

Euler **subestima** sistematicamente (a curva exata é convexa; Euler usa a inclinação do início de cada intervalo, "descendo" rápido demais). O erro encolhe ao diminuir $\Delta t$.

```python
import numpy as np
N0, tau, dt, T = 1000, 2.0, 0.5, 6.0
ts = np.arange(0, T + 1e-9, dt)
exato = N0 * np.exp(-ts / tau)
N = N0; euler = [N0]
for _ in ts[1:]:
    N = N - (N / tau) * dt
    euler.append(N)
```

### 3. Pêndulo (Euler para $\theta$ e $\omega$)

Sistema de duas variáveis acopladas:

$$\theta(t+\Delta t) = \theta(t) + \Delta t\,\omega(t), \qquad \omega(t+\Delta t) = \omega(t) - \Delta t\,\frac{g}{L}\sin\theta(t),$$
$$x = L\sin\theta, \qquad y = L(1-\cos\theta).$$

Exemplo $L=1$, $g=9{,}8$, $\theta(0)=0{,}3$ rad, $\omega(0)=0$, $\Delta t=0{,}05$:

| $t$ | $\theta$ | $\omega$ | $x$ | $y$ |
|---|---|---|---|---|
| 0,00 | +0,3000 | +0,0000 | +0,2955 | +0,0447 |
| 0,20 | +0,2567 | −0,5656 | +0,2539 | +0,0328 |
| 0,40 | +0,1091 | −0,9706 | +0,1089 | +0,0059 |
| 0,60 | −0,0962 | −1,0370 | −0,0960 | +0,0046 |
| 0,80 | −0,2845 | −0,7034 | −0,2807 | +0,0402 |
| 1,00 | −0,3808 | −0,0683 | −0,3717 | +0,0716 |

O pêndulo oscila em torno de $\theta=0$ (período $\approx 2\pi\sqrt{L/g}\approx 2{,}0$ s para pequenas amplitudes — coerente com o vaivém observado). Atenção: o **Euler explícito injeta energia** no sistema, então a amplitude cresce lentamente ao longo de muitos períodos; para simulações longas prefira Euler *semi-implícito* (usar $\omega$ já atualizado ao avançar $\theta$) ou Runge–Kutta.

```python
import numpy as np
L, g, dt, T = 1.0, 9.8, 0.05, 5.0
th, w = 0.3, 0.0
t = 0.0
while t <= T:
    x, y = L*np.sin(th), L*(1 - np.cos(th))
    # registrar (t, th, w, x, y)
    th, w = th + dt*w, w - dt*(g/L)*np.sin(th)   # Euler explícito
    t += dt
```

---

### Resumo dos resultados numéricos principais

| Item | Resultado |
|---|---|
| Markov 1 | 4ª visita ≈ 667 "Sim"; longo prazo 2/3 ≈ 667 / 1/3 ≈ 333 |
| Markov 2 | Estável ≈ T 7657, I 11082, C 8261 |
| Markov 3 | (b) 50%; (c) B em 2/9 ≈ 22,2% |
| Markov 4 | (b) 17,5%; (c) 22,55%; (d) 30,6/44,9/24,5%; (e) 31,0/48,3/20,7% |
| Markov 5 | Guilherme E=42 rolagens; Christian E=36 (mais rápido) |
| Markov 7/9 | Mais visitadas: letras internas (B–E ≈ 20%); extremos ≈ 10% |
| Interp 1 | $p(x)=-\tfrac13x^2+\tfrac{11}3x-3$; raízes $(11\pm\sqrt{85})/2$ |
| Interp 2 | Polinômio único $0{,}1875x^3-2{,}1875x^2+7{,}8125x-3{,}8125$ |
| Dif. autom. | $f(2,3,5)=3{,}2$; $\nabla f=(5{,}2,\ 4{,}4,\ -3{,}44)$ |
