# Métodos Numéricos — Resolução de Exercícios de Laboratório
## [Gerado por IA][mvfm]

> Resolução passo a passo das questões dos ExLabs que têm relação direta com os tópicos expandidos em `adicoes.md`. O objetivo não é só dar a resposta — é mostrar **de onde vem** cada passo de raciocínio, conectando o exercício ao conteúdo formal que as aulas deixaram implícito.
>
> ExLab 4 (Interpolação) não é coberto aqui pois interpolação polinomial ainda não foi expandida em `adicoes.md`.

---

## ExLab 1 — Solução de Equações

---

### Q1 — O Algoritmo do Epsilon de Máquina

**Questão:** O algoritmo abaixo termina? Por quê? E o que significa o último valor impresso?

```
double aux = 1.0;
while 1 + aux > 1:
    print aux
    aux = aux / 2
```

**Conexão com `adicoes.md`:** Seção *IEEE 754 — O que ficou por baixo dos panos* e *Arredondamento*.

#### Raciocínio

O loop está testando se `1.0 + aux > 1.0` em aritmética de ponto flutuante. Matematicamente, qualquer `aux > 0` tornaria a condição verdadeira para sempre. Em IEEE 754, não.

O número `1.0` em double precision ocupa exatamente a casa binária $2^0$. A **mantissa tem 52 bits**, o que significa que o menor passo representável a partir de 1.0 é $2^{-52}$. Quando `aux` cai abaixo de $2^{-52}$, a soma `1.0 + aux` é arredondada de volta para `1.0` pelo modo *round to nearest* — a operação de adição perde `aux` inteiramente.

**Nesse momento:**
- A condição `1 + aux > 1` avalia como `1.0 > 1.0` → **falso**
- O loop termina

**(a) Sim, o algoritmo termina.** A aritmética IEEE 754 tem precisão finita, e `aux` eventualmente se torna indistinguível de zero na vizinhança de 1.0.

**(b) O último valor impresso** é o **epsilon de máquina** (ε_mach) — a menor potência de 2 tal que `1.0 + ε > 1.0` ainda é representável. Para `double` (64 bits):

$$\varepsilon_{mach} = 2^{-52} \approx 2{,}220 \times 10^{-16}$$

Este é o limite de precisão relativa de todos os cálculos em double precision. Qualquer resultado com erro relativo menor que ε_mach é indistinguível do valor exato para o computador.

**Conclusão:** O algoritmo é a definição executável do epsilon de máquina. A conexão direta com IEEE 754: os 52 bits da mantissa determinam o valor de ε. Um `float` de 32 bits (23 bits de mantissa) teria ε_mach ≈ 1,19 × 10⁻⁷ — muito mais grosseiro.

---

### Q2a — Regra de Descartes

**Questão:** Encontre o número de raízes positivas e negativas de $p(x) = 6x^5 + 18x^3 - 34x^2 - 493x + 1431$.

**Conexão com `adicoes.md`:** Seção *Regra de Descartes — O que "desce de dois em dois" quer dizer*.

#### Raciocínio

**Raízes positivas — aplicar a regra diretamente em $p(x)$:**

Listando os coeficientes em ordem decrescente de grau (zeros incluídos):

$$+6,\; 0,\; +18,\; -34,\; -493,\; +1431$$

Ignorando os zeros para contagem de trocas de sinal:

$$+6 \to +18 \to -34 \to -493 \to +1431$$

| Transição | Mudança? |
|---|---|
| $+6 \to +18$ | Não |
| $+18 \to -34$ | **Sim (1)** |
| $-34 \to -493$ | Não |
| $-493 \to +1431$ | **Sim (2)** |

→ **2 trocas de sinal** → **2 ou 0 raízes positivas reais.**

**Raízes negativas — avaliar $p(-x)$:**

$$p(-x) = 6(-x)^5 + 18(-x)^3 - 34(-x)^2 - 493(-x) + 1431$$
$$= -6x^5 - 18x^3 - 34x^2 + 493x + 1431$$

Coeficientes ignorando zeros:

$$-6 \to -18 \to -34 \to +493 \to +1431$$

| Transição | Mudança? |
|---|---|
| $-6 \to -18$ | Não |
| $-18 \to -34$ | Não |
| $-34 \to +493$ | **Sim (1)** |
| $+493 \to +1431$ | Não |

→ **1 troca de sinal** → **exatamente 1 raiz negativa real** (não pode "descer de dois" a partir de 1).

**Conclusão:** $p(x)$ tem **1 raiz negativa** e **2 ou 0 raízes positivas**. Como o polinômio é de grau 5 com coeficientes reais, raízes complexas vêm em pares conjugados. Os cenários possíveis são:

- 1 negativa + 2 positivas + 2 complexas conjugadas
- 1 negativa + 0 positivas + 4 complexas conjugadas

---

### Q2b/c — Cotas de Lagrange, Cauchy e Fujiwara

**Questão:** Calcule as cotas de Lagrange e Cauchy (e Fujiwara se corajoso) para as raízes de $p(x) = 6x^5 + 18x^3 - 34x^2 - 493x + 1431$.

**Conexão com `adicoes.md`:** Seção *Aula 06 — Cotas de Lagrange, Cauchy e Fujiwara*.

#### Raciocínio

O polinômio em forma completa: $6x^5 + 0x^4 + 18x^3 - 34x^2 - 493x + 1431$.
Coeficiente líder: $a_5 = 6$.

---

**Cota de Lagrange:** $M = \max\!\left\{1,\; \sum_{i=0}^{n-1}\left|\frac{a_i}{a_n}\right|\right\}$

$$M = \max\!\left\{1,\; \frac{|0|}{6} + \frac{|18|}{6} + \frac{|-34|}{6} + \frac{|-493|}{6} + \frac{|1431|}{6}\right\}$$
$$= \max\!\left\{1,\; 0 + 3 + 5{,}67 + 82{,}17 + 238{,}5\right\}$$
$$= \max\!\left\{1,\; 329{,}33\right\} = \boxed{329{,}33}$$

Todas as raízes estão em $[-329{,}33;\; 329{,}33]$.

---

**Cota de Cauchy:** $M = 1 + \max_{0 \le i < n}\!\left|\frac{a_i}{a_n}\right|$

$$M = 1 + \max\!\left\{0,\; 3,\; 5{,}67,\; 82{,}17,\; 238{,}5\right\} = 1 + 238{,}5 = \boxed{239{,}5}$$

O máximo é dominado pelo coeficiente $a_0 = 1431$ (o termo constante, com razão $1431/6 = 238{,}5$).

---

**Cota de Fujiwara:** $M = 2 \cdot \max_{1 \le i \le n}\!\left|\frac{a_{n-i}}{a_n}\right|^{1/i}$

Calculando cada termo — o expoente $1/i$ "suaviza" os coeficientes maiores:

| $i$ | Coef. $a_{n-i}$ | $\left|\frac{a_{n-i}}{a_5}\right|$ | Raiz $(\cdot)^{1/i}$ |
|---|---|---|---|
| 1 | $a_4 = 0$ | 0 | 0 |
| 2 | $a_3 = 18$ | $3$ | $\sqrt{3} \approx 1{,}732$ |
| 3 | $a_2 = -34$ | $5{,}67$ | $5{,}67^{1/3} \approx 1{,}782$ |
| 4 | $a_1 = -493$ | $82{,}17$ | $82{,}17^{1/4} \approx 3{,}011$ |
| 5 | $a_0 = 1431$ | $238{,}5$ | $238{,}5^{1/5} \approx 2{,}979$ |

$$M = 2 \times \max\!\{0,\; 1{,}732,\; 1{,}782,\; 3{,}011,\; 2{,}979\} = 2 \times 3{,}011 = \boxed{6{,}02}$$

**Conclusão:** As três cotas garantem que todas as raízes estão dentro do intervalo correspondente, mas com precisões radicalmente diferentes.

| Cota | Intervalo garantido |
|---|---|
| Lagrange | $[-329{,}3;\; 329{,}3]$ |
| Cauchy | $[-239{,}5;\; 239{,}5]$ |
| **Fujiwara** | $[-6{,}02;\; 6{,}02]$ |

Fujiwara é **54× mais precisa** que Cauchy aqui. O motivo: ela usa expoentes $1/i$ que penalizam coeficientes de baixo grau (distantes da raiz no sentido da recursão de Horner), enquanto Cauchy e Lagrange os tratam igualmente. O $1431$ que domina Lagrange e Cauchy vira $(1431/6)^{1/5} \approx 2{,}98$ em Fujiwara — bem mais modesto.

---

### Q3 — Método da Bisecção e Seus Limites

**Questão:** Crie $p(x)$ com raízes 2, 3 e 4. Use bisecção em $[1,\;5]$. Ele encontra raízes? Todas? Só uma? Sempre?

**Conexão com `adicoes.md`:** Seção *Bisecção — O Teorema que a justifica*.

#### Raciocínio

**Construindo o polinômio:**

$$p(x) = (x-2)(x-3)(x-4) = x^3 - 9x^2 + 26x - 24$$

**Verificando a condição de Bolzano no intervalo $[1,\;5]$:**

$$p(1) = (1-2)(1-3)(1-4) = (-1)(-2)(-3) = -6 < 0$$
$$p(5) = (5-2)(5-3)(5-4) = (3)(2)(1) = 6 > 0$$

Sinais opostos → Bolzano garante pelo menos uma raiz em $(1,\;5)$.

**Executando a bisecção:**

| Iter. | $[a, b]$ | $c = (a+b)/2$ | $p(c)$ | Novo intervalo |
|---|---|---|---|---|
| 1 | $[1, 5]$ | $3{,}0$ | $p(3) = 0$ | **Raiz encontrada!** |

$p(3) = 27 - 81 + 78 - 24 = 0$ exatamente. A bisecção encontra $x = 3$ na primeira iteração.

**Ela encontra as outras raízes (2 e 4)?** Não. Bisecção é um método para encontrar **uma** raiz por chamada — aquela que está dentro do intervalo com troca de sinal. Para encontrar $x = 2$ precisaria de $[1,\;2{,}5]$; para $x = 4$, de $[3{,}5,\;5]$.

**Ela sempre converge?** Sim, desde que a condição de Bolzano seja satisfeita e $p$ seja contínua no intervalo. A taxa de convergência é **linear**: a cada iteração o intervalo é dividido ao meio, então em $n$ passos o erro é $\leq \frac{b-a}{2^n}$.

---

### Q4 — Falha da Bisecção com Número Par de Raízes

**Questão:** Use bisecção em $[1,\;6]$ para $p(x) = (x-2)(x-3)(x-4)(x-5)$. O que acontece?

**Raciocínio:**

$$p(1) = (-1)(-2)(-3)(-4) = 24 > 0$$
$$p(6) = (4)(3)(2)(1) = 24 > 0$$

**Ambos os extremos têm o mesmo sinal.** A condição de Bolzano não é satisfeita — a bisecção não consegue sequer iniciar.

Por quê? O polinômio tem **4 raízes** no intervalo. Depois de cruzar o eixo em 2, 3, 4 e 5, o sinal volta a ser positivo em 6. Um número par de cruzamentos cancela a troca de sinal nos extremos.

**Como adaptar?** Avaliar $p$ em vários pontos intermediários e encontrar sub-intervalos onde o sinal muda:
- $p(1) = 24 > 0$, $p(2) = 0$: raiz em 2
- $p(2{,}5) = (0{,}5)(-0{,}5)(-1{,}5)(-2{,}5) = -0{,}9375 < 0$: troca de sinal entre 2 e 3
- $p(4{,}5) = (2{,}5)(1{,}5)(0{,}5)(-0{,}5) = -0{,}9375 < 0$: troca entre 4 e 5

Aplicar bisecção separadamente em $[2,\;3]$, $[3,\;4]$ e $[4,\;5]$.

**Conclusão:** Bisecção é cega a raízes "emparelhadas" — ela enxerga apenas troca de sinal, não a quantidade de raízes. Qualquer algoritmo robusto de busca de raízes precisa de uma fase de *bracketing* (varredura de sub-intervalos) antes de aplicar bisecção.

---

### Q7 — Método de Horner

**Questão:** Para $p(x) = x^5 + 18x^3 + 34x^2 - 493x + 1431$, o que o algoritmo abaixo imprime?

```
a[] = {1, 0, 18, 34, -493, 1431}
p = 0
para i = 0 a 5:
    p = x * p + a[i]
imprima x, p
```

**Conexão com `adicoes.md`:** Seção *Método de Horner — Por que funciona*.

#### Raciocínio

Traçando a execução passo a passo (variável `p` a cada iteração):

| $i$ | `a[i]` | Operação | `p` após |
|---|---|---|---|
| 0 | 1 | $p = x \cdot 0 + 1$ | $1$ |
| 1 | 0 | $p = x \cdot 1 + 0$ | $x$ |
| 2 | 18 | $p = x \cdot x + 18$ | $x^2 + 18$ |
| 3 | 34 | $p = x \cdot (x^2+18) + 34$ | $x^3 + 18x + 34$ |
| 4 | -493 | $p = x \cdot (x^3+18x+34) - 493$ | $x^4 + 18x^2 + 34x - 493$ |
| 5 | 1431 | $p = x \cdot (x^4+18x^2+34x-493) + 1431$ | $x^5 + 18x^3 + 34x^2 - 493x + 1431$ |

**O algoritmo imprime $(x,\; p(x))$ — o valor do polinômio avaliado em $x$.**

A forma aninhada equivalente é:

$$p(x) = (((((1)x + 0)x + 18)x + 34)x - 493)x + 1431$$

**Por que Horner é melhor?** A avaliação ingênua de um polinômio de grau 5 exigiria calcular $x^5, x^4, x^3, x^2$ separadamente — 4 potenciações custosas. Horner usa apenas multiplicações e somas sequenciais: **5 multiplicações e 5 adições**, custo $O(n)$ em vez de $O(n^2)$.

---

### Q9 — Horner Estendido: Avaliando $p(x)$ e $p'(x)$ Simultaneamente

**Questão:** O que o algoritmo modificado abaixo imprime?

```
p = 0, q = 0
para i = 0 a 5:
    q = x * q + p
    p = x * p + a[i]
imprima x, p, q
```

**Conexão com `adicoes.md`:** Seção *Método de Newton — Quando ele falha* (Newton precisa de $p'(x)$).

#### Raciocínio

Traçando a execução para `a[] = {1, 0, 18, 34, -493, 1431}`:

| $i$ | `q` após | `p` após |
|---|---|---|
| 0 | $x \cdot 0 + 0 = 0$ | $x \cdot 0 + 1 = 1$ |
| 1 | $x \cdot 0 + 1 = 1$ | $x \cdot 1 + 0 = x$ |
| 2 | $x \cdot 1 + x = 2x$ | $x \cdot x + 18 = x^2 + 18$ |
| 3 | $x \cdot 2x + (x^2+18) = 3x^2 + 18$ | $x(x^2+18) + 34 = x^3 + 18x + 34$ |
| 4 | $x(3x^2+18)+(x^3+18x+34) = 4x^3+36x+34$ | $x(x^3+18x+34)-493 = x^4+18x^2+34x-493$ |
| 5 | $x(4x^3+36x+34)+(x^4+18x^2+34x-493) = 5x^4+54x^2+68x-493$ | $x^5+18x^3+34x^2-493x+1431$ |

Resultado final:
- `p` = $x^5 + 18x^3 + 34x^2 - 493x + 1431 = p(x)$ ✓
- `q` = $5x^4 + 54x^2 + 68x - 493$

**Verificando:** $p'(x) = 5x^4 + 3 \cdot 18x^2 + 2 \cdot 34x - 493 = 5x^4 + 54x^2 + 68x - 493$ ✓

**O algoritmo imprime $(x,\; p(x),\; p'(x))$.** As duas quantidades calculadas são exatamente o que o **Método de Newton** precisa a cada iteração:

$$x_{k+1} = x_k - \frac{p(x_k)}{p'(x_k)}$$

Um único loop de Horner, com custo $O(n)$, fornece as duas quantidades — sem calcular derivadas simbolicamente. Esta é a implementação eficiente de Newton para polinômios.

**Conclusão:** O algoritmo modificado é o **Horner estendido**, também chamado de **deflação sintética**. A variável `q` acumula os coeficientes do polinômio quociente $q(x)$ tal que $p(x) = (x - x_0) \cdot q(x) + p(x_0)$, e $q(x_0) = p'(x_0)$ pelo teorema de Ruffini. Ele resolve o problema central de Newton para polinômios: calcular $f'$ de forma barata.

---

## ExLab 2 — Sistemas Lineares

---

### Q1 — O Parquinho como Sistema Linear

**Questão:** Um parque tem brinquedos A, B, C, D. 20 pessoas/hora entram por A, 10 por C. De A ou C: metade vai a B, o resto divide-se em três (sai, vai ao brinquedo extra 1, vai ao extra 2). De B ou D: divide-se igualmente entre A, C, D. Quantas pessoas brincam em cada brinquedo?

**Conexão com `adicoes.md`:** Seção *Aula 14 — Eliminação de Gauss* e *Sistemas Lineares como Novo Problema*.

#### Raciocínio

**Modelando o fluxo:**

Definindo $x_A, x_B, x_C, x_D$ como o fluxo total de pessoas/hora em cada brinquedo.

- De A: $\frac{1}{2}x_A \to B$, $\frac{1}{6}x_A \to C$, $\frac{1}{6}x_A \to D$, $\frac{1}{6}x_A$ saem
- De C: $\frac{1}{2}x_C \to B$, $\frac{1}{6}x_C \to A$, $\frac{1}{6}x_C \to D$, $\frac{1}{6}x_C$ saem
- De B: $\frac{1}{3}x_B \to A$, $\frac{1}{3}x_B \to C$, $\frac{1}{3}x_B \to D$
- De D: $\frac{1}{3}x_D \to A$, $\frac{1}{3}x_D \to C$, $\frac{1}{3}x_D \to D$

**Equações de balanço:**

$$x_A = 20 + \frac{1}{6}x_C + \frac{1}{3}x_B + \frac{1}{3}x_D \tag{1}$$
$$x_B = \frac{1}{2}x_A + \frac{1}{2}x_C \tag{2}$$
$$x_C = 10 + \frac{1}{6}x_A + \frac{1}{3}x_B + \frac{1}{3}x_D \tag{3}$$
$$x_D = \frac{1}{6}x_A + \frac{1}{6}x_C + \frac{1}{3}x_B + \frac{1}{3}x_D \tag{4}$$

**Resolvendo (simplificando D):**

De (4): $x_D - \frac{1}{3}x_D = \frac{1}{6}x_A + \frac{1}{6}x_C + \frac{1}{3}x_B$

$$\frac{2}{3}x_D = \frac{1}{6}(x_A + x_C) + \frac{1}{3}x_B$$

Substituindo (2) em D: $x_B = \frac{1}{2}(x_A + x_C)$, portanto:

$$\frac{2}{3}x_D = \frac{1}{6}(x_A+x_C) + \frac{1}{3}\cdot\frac{1}{2}(x_A+x_C) = \frac{1}{6}(x_A+x_C) + \frac{1}{6}(x_A+x_C) = \frac{1}{3}(x_A+x_C)$$

$$\boxed{x_D = \frac{1}{2}(x_A+x_C) = x_B}$$

B e D têm o mesmo fluxo. Substituindo em (1):

$$x_A = 20 + \frac{1}{6}x_C + \frac{1}{3}x_B + \frac{1}{3}x_D = 20 + \frac{1}{6}x_C + \frac{2}{3} \cdot \frac{1}{2}(x_A+x_C)$$
$$x_A = 20 + \frac{1}{6}x_C + \frac{1}{3}(x_A+x_C)$$
$$\frac{2}{3}x_A = 20 + \frac{1}{2}x_C \implies x_A = 30 + \frac{3}{4}x_C \tag{I}$$

Da mesma forma em (3):

$$\frac{2}{3}x_C = 10 + \frac{1}{2}x_A \implies x_C = 15 + \frac{3}{4}x_A \tag{II}$$

**Eliminação de Gauss — substituindo (II) em (I):**

$$x_A = 30 + \frac{3}{4}\!\left(15 + \frac{3}{4}x_A\right) = 30 + \frac{45}{4} + \frac{9}{16}x_A$$

$$x_A - \frac{9}{16}x_A = \frac{120 + 45}{4} \implies \frac{7}{16}x_A = \frac{165}{4}$$

$$x_A = \frac{165}{4} \cdot \frac{16}{7} = \frac{660}{7} \approx 94{,}3 \text{ pessoas/hora}$$

$$x_C = 15 + \frac{3}{4} \cdot \frac{660}{7} = \frac{105 + 495}{7} = \frac{600}{7} \approx 85{,}7 \text{ pessoas/hora}$$

$$x_B = x_D = \frac{1}{2}\left(\frac{660}{7} + \frac{600}{7}\right) = \frac{1260}{14} = 90 \text{ pessoas/hora}$$

**Verificação:** $x_A = 20 + \frac{600}{42} + 30 + 30 = 20 + \frac{100}{7} + 60 \approx 94{,}3$ ✓

**Conclusão:**

| Brinquedo | Pessoas/hora |
|---|---|
| A | $\approx 94{,}3$ |
| B | $90{,}0$ |
| C | $\approx 85{,}7$ |
| D | $90{,}0$ |

A maior afluência é em A (portão principal, 20 chegadas) e a menor em C (portão secundário, 10 chegadas). B e D são iguais porque são alimentados simetricamente por A e C. O modelo é um sistema linear $4 \times 4$ resolvido por substituição progressiva — Gauss reduzido ao caso mais simples.

---

### Q4 — Sistema Mal-Condicionado (Composto Químico)

**Questão:** Mesma mistura química do Q3, mas agora as proporções de X não somam 100%. Interprete com cuidado.

**Conexão com `adicoes.md`:** Seção *Sistemas Mal-Condicionados* e *Pivotamento e Subtração Catastrófica*.

#### Raciocínio

No Q3, a composição de X somava exatamente 100%, o que tornava o sistema exatamente determinado e a solução física (proporções somando 1). No Q4, a composição de X soma:

$$24{,}3\% + 15\% + 26{,}2\% + 21{,}5\% = 87\%$$

Os **13% restantes** são substâncias desconhecidas. O sistema que se monta é:

$$\begin{bmatrix} 0{,}15 & 0{,}36 & 0{,}20 & 0{,}31 \\ 0{,}28 & 0{,}11 & 0{,}15 & 0{,}22 \\ 0{,}27 & 0{,}36 & 0{,}33 & 0{,}24 \\ 0{,}30 & 0{,}17 & 0{,}32 & 0{,}23 \end{bmatrix} \begin{bmatrix} \alpha_A \\ \alpha_B \\ \alpha_C \\ \alpha_D \end{bmatrix} = \begin{bmatrix} 0{,}243 \\ 0{,}150 \\ 0{,}262 \\ 0{,}215 \end{bmatrix}$$

**Por que isso é problemático:**

1. **Inconsistência física:** As colunas da matriz (composição de A, B, C, D) somam 100% cada. O vetor b (composição de X) soma 87%. Não existe solução com $\alpha_A + \alpha_B + \alpha_C + \alpha_D = 1$ que satisfaça o sistema — há matéria "perdida" em X que A, B, C, D não explicam.

2. **Sensibilidade ao erro:** A pequena perturbação no vetor $b$ (13% faltando) vs. o Q3 (b exato) pode causar uma **grande mudança na solução** se o número de condicionamento $\kappa(A)$ for alto. Este é exatamente o mal-condicionamento descrito em `adicoes.md`.

3. **Resultado possível:** Gauss pode retornar proporções negativas ou maiores que 1 — fisicamente impossíveis. Isso não é erro do algoritmo; é o sistema dizendo que as 4 substâncias conhecidas não são suficientes para descrever X.

**Interpretação correta:** A solução $[\alpha_A, \alpha_B, \alpha_C, \alpha_D]$ encontrada representa a **melhor estimativa** das proporções das substâncias conhecidas na fração dos 87% explicados. Os valores devem ser interpretados como proporções parciais, e a soma deles deve ser $< 1$ (o complemento são as substâncias desconhecidas).

**Conclusão:** Este exercício é um caso clássico de sistema mal-condicionado gerado por dados reais imperfeitos. A lição de `adicoes.md` se aplica diretamente: quando os dados têm "ruído" (as % desconhecidas), um sistema que seria bem condicionado com dados limpos pode produzir soluções instáveis. A ferramenta correta é **mínimos quadrados** (minimizar $||Ax - b||^2$), não Gauss puro.

---

## ExLab 3 — Cadeias de Markov

---

### Q1 — Sorveteria: Estado Estacionário e Convergência

**Questão:** 1000 clientes respondem Sim ou Não sobre sorvete. Transições: Sim→Sim 70%, Sim→Não 30%, Não→Sim 60%, Não→Não 40%. Quantos dirão Sim na 4ª visita? E a longo prazo?

**Conexão com `adicoes.md`:** Seção *Aula 15 — Cadeias de Markov e o Problema dos Lemmings*, especialmente *Propriedade de Markov* e *Resolvendo com Eliminação de Gauss*.

#### Raciocínio

**Matriz de transição** (coluna = estado atual, linha = próximo estado):

$$T = \begin{bmatrix} 0{,}7 & 0{,}6 \\ 0{,}3 & 0{,}4 \end{bmatrix}$$

A propriedade de Markov garante que aplicar $T$ repetidamente converge a um estado independente da distribuição inicial.

**Calculando $T^4$ (4ª visita):**

$$T^2 = T \cdot T = \begin{bmatrix} 0{,}7 \cdot 0{,}7 + 0{,}6 \cdot 0{,}3 & 0{,}7 \cdot 0{,}6 + 0{,}6 \cdot 0{,}4 \\ 0{,}3 \cdot 0{,}7 + 0{,}4 \cdot 0{,}3 & 0{,}3 \cdot 0{,}6 + 0{,}4 \cdot 0{,}4 \end{bmatrix} = \begin{bmatrix} 0{,}67 & 0{,}66 \\ 0{,}33 & 0{,}34 \end{bmatrix}$$

$$T^4 = T^2 \cdot T^2 = \begin{bmatrix} 0{,}67^2 + 0{,}66 \cdot 0{,}33 & \cdots \\ \cdots & \cdots \end{bmatrix} \approx \begin{bmatrix} 0{,}6\overline{6} & 0{,}6\overline{6} \\ 0{,}3\overline{3} & 0{,}3\overline{3} \end{bmatrix}$$

$T^4$ já convergiu: **cada coluna é $[2/3,\; 1/3]$**, independente do estado inicial.

**Na 4ª visita:** $\approx 667$ clientes dizem Sim e $\approx 333$ dizem Não.

**Estado estacionário** — resolvendo $\pi = T\pi$ com $\pi_{Sim} + \pi_{N\tilde{a}o} = 1$:

$$\pi_{Sim} = 0{,}7\;\pi_{Sim} + 0{,}6\;\pi_{N\tilde{a}o}$$
$$0{,}3\;\pi_{Sim} = 0{,}6\;\pi_{N\tilde{a}o} \implies \pi_{Sim} = 2\;\pi_{N\tilde{a}o}$$

Com soma = 1: $3\;\pi_{N\tilde{a}o} = 1 \implies \pi_{N\tilde{a}o} = \frac{1}{3},\quad \pi_{Sim} = \frac{2}{3}$

**Conclusão:** A longo prazo, **667 clientes** (2/3) dirão que o sorvete é o melhor, **333** (1/3) discordarão — independentemente de quantos começaram em cada grupo. A cadeia converge geometricamente, e já em $T^4$ o estado estacionário é atingido. O estado estacionário é encontrado por um sistema linear de 2 equações — resolvido por substituição direta.

---

### Q4 — Mobilidade Social: Gauss para Encontrar o Equilíbrio

**Questão:** Ricos (R), Médios (M), Pobres (P) com transições geracionais. Calcule: (b) probabilidade de neto rico partindo de Pobre; (c) idem para bisneto; (d) proporção de longo prazo; (e) com redistribuição de renda.

**Conexão com `adicoes.md`:** Seções *Aula 14 — Eliminação de Gauss*, *Aula 15 — Cadeias de Markov* e especialmente *Resolvendo com Eliminação de Gauss*.

#### Raciocínio

**Matriz de transição** (linha = próxima geração):

$$T = \begin{bmatrix} 0{,}70 & 0{,}15 & 0{,}10 \\ 0{,}20 & 0{,}70 & 0{,}30 \\ 0{,}10 & 0{,}15 & 0{,}60 \end{bmatrix} \quad \begin{matrix} \leftarrow R' \\ \leftarrow M' \\ \leftarrow P' \end{matrix}$$

Colunas = estado atual (R, M, P). Ponto de partida: Pobre → $v_0 = [0,\; 0,\; 1]^T$.

---

**(b) Netos Ricos** — 2 gerações: $v_2 = T^2 v_0 = T(T v_0)$

$T v_0 = [0{,}10,\; 0{,}30,\; 0{,}60]^T$ (filhos)

$T \cdot [0{,}10,\; 0{,}30,\; 0{,}60]^T$:

$$R: 0{,}70 \times 0{,}10 + 0{,}15 \times 0{,}30 + 0{,}10 \times 0{,}60 = 0{,}07 + 0{,}045 + 0{,}06 = \mathbf{0{,}175}$$
$$M: 0{,}20 \times 0{,}10 + 0{,}70 \times 0{,}30 + 0{,}30 \times 0{,}60 = 0{,}02 + 0{,}21 + 0{,}18 = 0{,}41$$
$$P: 0{,}10 \times 0{,}10 + 0{,}15 \times 0{,}30 + 0{,}60 \times 0{,}60 = 0{,}01 + 0{,}045 + 0{,}36 = 0{,}415$$

**Probabilidade de neto Rico: 17,5%.**

---

**(c) Bisnetos Ricos** — 3 gerações: $T \cdot [0{,}175,\; 0{,}41,\; 0{,}415]^T$

$$R: 0{,}70 \times 0{,}175 + 0{,}15 \times 0{,}41 + 0{,}10 \times 0{,}415 = 0{,}1225 + 0{,}0615 + 0{,}0415 = \mathbf{0{,}2255}$$
$$M: 0{,}20 \times 0{,}175 + 0{,}70 \times 0{,}41 + 0{,}30 \times 0{,}415 = 0{,}035 + 0{,}287 + 0{,}1245 = 0{,}4465$$
$$P: 0{,}10 \times 0{,}175 + 0{,}15 \times 0{,}41 + 0{,}60 \times 0{,}415 = 0{,}0175 + 0{,}0615 + 0{,}249 = 0{,}328$$

**Probabilidade de bisneto Rico: 22,6%.** O crescimento de 17,5% → 22,6% mostra convergência em direção ao estado estacionário.

---

**(d) Estado estacionário** — resolvendo $\pi = T\pi$ com $\pi_R + \pi_M + \pi_P = 1$ via Gauss:

Das equações de equilíbrio:

$$0{,}30\,\pi_R = 0{,}15\,\pi_M + 0{,}10\,\pi_P \implies \pi_R = \frac{\pi_M}{2} + \frac{\pi_P}{3} \tag{1}$$
$$0{,}40\,\pi_P = 0{,}10\,\pi_R + 0{,}15\,\pi_M \tag{2}$$

Substituindo (1) em (2):

$$0{,}40\,\pi_P = 0{,}10\!\left(\frac{\pi_M}{2} + \frac{\pi_P}{3}\right) + 0{,}15\,\pi_M = 0{,}05\,\pi_M + \frac{\pi_P}{30} + 0{,}15\,\pi_M$$
$$\left(0{,}40 - \frac{1}{30}\right)\pi_P = 0{,}20\,\pi_M \implies \frac{11}{30}\,\pi_P = \frac{\pi_M}{5} \implies \pi_M = \frac{11\,\pi_P}{6}$$

$$\pi_R = \frac{1}{2} \cdot \frac{11\,\pi_P}{6} + \frac{\pi_P}{3} = \frac{11\,\pi_P}{12} + \frac{4\,\pi_P}{12} = \frac{15\,\pi_P}{12} = \frac{5\,\pi_P}{4}$$

Soma = 1:

$$\frac{5\,\pi_P}{4} + \frac{11\,\pi_P}{6} + \pi_P = 1 \implies \frac{15 + 22 + 12}{12}\,\pi_P = 1 \implies \pi_P = \frac{12}{49}$$

$$\boxed{\pi_R = \frac{15}{49} \approx 30{,}6\%} \qquad \boxed{\pi_M = \frac{22}{49} \approx 44{,}9\%} \qquad \boxed{\pi_P = \frac{12}{49} \approx 24{,}5\%}$$

---

**(e) Com redistribuição** — Pobres agora: P→P 50%, P→M 40%, P→R 10%. Novo $T$ idêntico exceto na coluna de P:

Nova coluna P: $[0{,}10,\; 0{,}40,\; 0{,}50]^T$.

Resolvendo novamente:

$$0{,}30\,\pi_R = 0{,}15\,\pi_M + 0{,}10\,\pi_P \implies \pi_R = \frac{\pi_M}{2} + \frac{\pi_P}{3} \tag{mesma eq. 1}$$
$$0{,}50\,\pi_P = 0{,}10\,\pi_R + 0{,}15\,\pi_M \tag{2'}$$

Substituindo (1) em (2'):

$$0{,}50\,\pi_P = 0{,}10\!\left(\frac{\pi_M}{2}+\frac{\pi_P}{3}\right) + 0{,}15\,\pi_M = 0{,}20\,\pi_M + \frac{\pi_P}{30}$$
$$\left(\frac{1}{2} - \frac{1}{30}\right)\pi_P = \frac{\pi_M}{5} \implies \frac{14}{30}\,\pi_P = \frac{\pi_M}{5} \implies \pi_M = \frac{14\,\pi_P}{6} = \frac{7\,\pi_P}{3}$$

$$\pi_R = \frac{7\,\pi_P}{6} + \frac{\pi_P}{3} = \frac{7\,\pi_P + 2\,\pi_P}{6} = \frac{9\,\pi_P}{6} = \frac{3\,\pi_P}{2}$$

Soma = 1: $\frac{3}{2}\pi_P + \frac{7}{3}\pi_P + \pi_P = 1 \implies \frac{9+14+6}{6}\pi_P = 1 \implies \pi_P = \frac{6}{29}$

$$\boxed{\pi_R = \frac{9}{29} \approx 31{,}0\%} \qquad \boxed{\pi_M = \frac{14}{29} \approx 48{,}3\%} \qquad \boxed{\pi_P = \frac{6}{29} \approx 20{,}7\%}$$

**Comparação:**

| | Sem redistribuição | Com redistribuição | Variação |
|---|---|---|---|
| Ricos | 30,6% | 31,0% | +0,4 p.p. |
| Médios | 44,9% | 48,3% | +3,4 p.p. |
| **Pobres** | **24,5%** | **20,7%** | **−3,8 p.p.** |

**Conclusão:** A redistribuição reduz a pobreza estrutural de 24,5% para 20,7% a longo prazo. O efeito é moderado porque as regras para Ricos e Médios não foram alteradas — a mobilidade descendente ainda existe. O estado estacionário é o ponto fixo de $T$, e encontrá-lo é literalmente resolver um sistema linear $3 \times 3$ via Gauss — a ligação direta entre Cadeias de Markov e Eliminação de Gauss que o JB demonstrou com os Lemmings.

---

## Nota sobre ExLab 4 — Interpolação

ExLab 4 cobre interpolação polinomial (Newton, Lagrange), extrapolação e mínimos quadrados. Esses tópicos **ainda não estão expandidos em `adicoes.md`**. As questões serão cobertas quando o conteúdo de interpolação for adicionado.
