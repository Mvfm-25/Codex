# Métodos Numéricos — Adições & Aprofundamentos (Parte 2)
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas — arquivos `aulaXX-2.md`. Segue os tópicos na ordem em que apareceram nas notas, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---

## Aula 02 — IEEE 754: A Conta dos Bits, a Ordenação e os Casos Especiais

### A conta que não fecha: $1 + 8 + 24 = 33$

As notas registram a divisão do float como "1 de sinal, 8 de expoente, 24 de mantissa" — e marcam, corretamente, que aquilo é *estranho*. É estranho porque **não cabe**: são 33 bits num tipo de 32.

A resolução está numa distinção que o padrão faz e que os slides costumam atropelar: **bits armazenados** e **precisão** são coisas diferentes.

- O campo de mantissa (*trailing significand field*) tem **23 bits armazenados**.
- A precisão do formato, que o padrão chama de $p$, é **24 bits**.

O 24º bit é o **bit implícito** — aquele `1` da frente que as notas descobrem no final ("nem precisa guardá-lo!"). Ele existe no valor, participa de toda a aritmética, mas não ocupa espaço. É precisão de graça, e é por isso que os dois números aparecem em lugares diferentes da literatura. Quando o JB diz 24, está falando de $p$; quando o diagrama de bits diz 23, está falando do que vai para a memória. $1 + 8 + 23 = 32$.

Generalizando para os outros formatos binários do padrão:

| Formato | Sinal | Expoente ($k$) | Mantissa armazenada | Precisão $p$ | Bias ($2^{k-1}-1$) | Dígitos decimais ($p\log_{10}2$) |
|---|---|---|---|---|---|---|
| binary16 (*half*) | 1 | 5 | 10 | 11 | 15 | ≈ 3,3 |
| **binary32 (`float`)** | 1 | 8 | 23 | **24** | **127** | ≈ 7,2 |
| **binary64 (`double`)** | 1 | 11 | 52 | **53** | **1023** | ≈ 15,9 |
| binary128 (*quad*) | 1 | 15 | 112 | 113 | 16383 | ≈ 34,0 |

Note que o bias **não é uma constante mágica**: é sempre $2^{k-1}-1$, onde $k$ é o número de bits do expoente. O 127 do float e o 1023 do double são a mesma fórmula. Daí também sai a regra prática de que `float` dá ~7 casas decimais confiáveis e `double` dá ~16 — é literalmente $p$ convertido de base 2 para base 10.

**Sobre a linha do tempo que as notas mencionam:** o IEEE 754-1985 padronizou apenas binário; o **IEEE 854-1987** generalizou as mesmas ideias para qualquer base (a "multi-base" das notas), sem exigir base 2. A revisão de **2008** não foi só "uma ajeitada" — ela **fundiu os dois padrões** e acrescentou os formatos decimais (`decimal32/64/128`), o binary16, o binary128 e o **FMA** (*fused multiply-add*, que calcula $a \times b + c$ com um único arredondamento). A versão vigente é a **754-2019**. O arquiteto intelectual de tudo isso é **William Kahan**, que levou o Turing Award de 1989 exatamente por esse trabalho.

---

### "Ordenar float é ordenar uma string de 4 char" — por que funciona, e onde quebra

Essa é a pergunta que as notas deixam aberta duas vezes ("Por que?", "Tem um motivo"). A resposta completa tem uma parte bonita e uma pegadinha.

**A parte bonita.** O layout `[sinal][expoente][mantissa]` é deliberado, e a ordem dos campos é o segredo. Como o expoente é armazenado **com bias** — isto é, como um inteiro *sem sinal* que só cresce — e ocupa os bits **mais significativos** logo abaixo do sinal, a comparação numérica se alinha com a comparação binária:

- Expoente maior ⇒ padrão de bits maior ⇒ número maior. O expoente domina porque está mais à esquerda.
- Expoentes iguais ⇒ o desempate cai na mantissa, que também é *unsigned* e crescente.

Se o expoente guardasse o próprio sinal (complemento de dois, por exemplo), $2^{-1}$ teria o bit alto do expoente ligado e pareceria *maior* que $2^{+1}$ — a monotonicidade morreria. **É por isso que o bias existe**, e é a mesma razão pela qual o expoente vem antes da mantissa em vez de depois, ao contrário da notação científica escrita.

O resultado é que, para dois floats **positivos**, isto vale:

$$a < b \iff \text{bits}(a) < \text{bits}(b) \quad \text{(comparados como \texttt{uint32})}$$

**A pegadinha.** Isso só vale para positivos. O IEEE 754 usa **sinal-magnitude**, não complemento de dois: $-1{,}0$ é `0xBF800000` e $-2{,}0$ é `0xC0000000`. Como *unsigned*, $-2$ parece maior que $-1$ — a ordem dos negativos vem **invertida**, e todo negativo parece maior que todo positivo. A correção é um truque padrão de *radix sort* de floats:

```c
// transforma o padrão de bits numa chave de ordenação totalmente monotônica
uint32_t chave(float f) {
    uint32_t u;
    memcpy(&u, &f, sizeof u);          // type punning seguro; nada de cast de ponteiro
    return (u & 0x80000000u)
         ? ~u                          // negativo: inverte tudo (desfaz a inversão)
         : (u | 0x80000000u);          // positivo: liga o bit alto (joga acima dos negativos)
}
```

Com essa chave, `qsort` sobre inteiros ordena floats corretamente — sem uma única instrução de ponto flutuante. É assim que ordenações de alta performance sobre floats são implementadas na prática.

Três ressalvas que fecham o assunto:

1. **Literalmente comparar "4 chars" com `memcmp` não funciona em x86.** A equivalência é com o *inteiro* de 32 bits, e x86 é **little-endian** — os bytes estão na memória na ordem inversa, então `memcmp` compararia a mantissa baixa primeiro. Em big-endian (SPARC, redes) a comparação byte a byte funciona de verdade. E teria que ser `unsigned char`: com `char` assinado, qualquer byte $\ge$ 128 vira negativo e estraga tudo.
2. **$+0$ e $-0$ têm padrões de bits diferentes** (`0x00000000` e `0x80000000`), mas o padrão exige que $+0 = -0$ seja verdadeiro. Ordenação por bits os separa; a comparação em ponto flutuante não. É a primeira quebra de equivalência entre as duas.
3. **NaN não tem lugar nenhum nessa ordem.** Ele fica no topo dos padrões de bits mas não é maior nem menor que nada. O 754-2008 acabou definindo uma `totalOrder` justamente para dar um veredito a esses casos.

---

### Subnormais: o que "não conseguem ser normalizados" significa de fato

As notas chegam à conclusão certa por dedução — se o `1` implícito é obrigatório, tem que existir uma exceção — mas param aí. A mecânica é a seguinte.

Expoente armazenado igual a **zero** é o código de escape: nesse caso o bit implícito passa a valer **0** em vez de 1, e o expoente efetivo é **fixado** em $-126$ (não $-127$, que seria o resultado ingênuo de $0 - 127$). O valor lido vira:

$$(-1)^{s} \times 0{,}\text{mantissa} \times 2^{-126}$$

Isso abre a faixa entre zero e o menor normal:

| Quantidade | Valor (float) |
|---|---|
| Menor normal positivo | $2^{-126} \approx 1{,}18 \times 10^{-38}$ |
| Menor subnormal positivo | $2^{-149} \approx 1{,}40 \times 10^{-45}$ |

**Por que se dar a esse trabalho.** A propriedade que os subnormais compram chama-se **underflow gradual**, e o teorema que ela garante é curto e crítico:

$$x - y = 0 \iff x = y$$

Sem subnormais (com *flush to zero*), dois números **distintos** e muito próximos podem subtrair e dar exatamente zero. Aí um código perfeitamente razoável como

```c
if (x != y) z = 1.0 / (x - y);   // "protegido" contra divisão por zero
```

divide por zero mesmo assim. Kahan brigou por essa propriedade justamente porque ela é o que permite escrever código numérico defensivo que realmente funciona. O preço é a perda progressiva de precisão: um subnormal com só 3 bits significativos ainda é um número, mas com 3 bits de precisão.

**E o preço em performance.** Em boa parte do hardware x86, operar com subnormais dispara um caminho de microcódigo lento — desacelerações de 10× a 100× já foram medidas em código de DSP e áudio que deriva para valores minúsculos. Por isso as flags `FTZ` (*flush-to-zero*, zera resultados subnormais) e `DAZ` (*denormals-are-zero*, trata operandos subnormais como zero) do registrador `MXCSR`, ligadas automaticamente por `-ffast-math`. Elas trocam a garantia acima por velocidade — decisão consciente, não detalhe. O bit **`DE`** da FPU status word, que apareceu na Aula 04, é exatamente o sinalizador de que um operando subnormal entrou na conta.

---

### O `-NaN` que o JB conseguiu: quiet, signaling e um bit de sinal sem significado

As notas registram a curiosidade — $0/0$ produziu `-nan` — e param no "vem nos dois sabores". A explicação é mais interessante que isso.

**O bit de sinal de um NaN não significa nada.** O padrão não atribui interpretação a ele; NaN não é positivo nem negativo. Mas ele *está* lá no padrão de bits, e o `printf` o imprime obedientemente. O `-nan` não é um NaN "negativo": é um NaN cujo bit de sinal calhou de estar ligado.

E ele calha de estar ligado por um motivo bem concreto. Quando uma operação inválida como $0/0$ ou $\infty - \infty$ precisa devolver um NaN, o hardware x86 devolve um valor fixo que a Intel chama de **QNaN *real indefinite***, cujo padrão em float é `0xFFC00000` — sinal 1, expoente todo ligado, bit mais alto da mantissa ligado. Sinal 1 ⇒ imprime `-nan`. Não é acaso nem bug do compilador; é o valor canônico da arquitetura.

Isso introduz a divisão que realmente importa, e que as notas não alcançaram — não é entre NaN positivo e negativo, é entre:

| Tipo | Bit mais alto da mantissa | Comportamento |
|---|---|---|
| **qNaN** (*quiet*) | **1** | Propaga silenciosamente pelas contas. É o resultado padrão de $0/0$, $\sqrt{-1}$, $\infty - \infty$. |
| **sNaN** (*signaling*) | **0** (com pelo menos outro bit ligado) | Ao ser **usado** numa operação, levanta a exceção *invalid operation* — vira armadilha. Serve para marcar memória não-inicializada. |

Os bits restantes da mantissa são o **payload** do NaN: ~22 bits livres que sobrevivem à propagação aritmética. Isso é usado de verdade — a técnica de **NaN-boxing** empacota ponteiros e inteiros dentro de payloads de NaN de `double`, e é assim que motores JavaScript e o LuaJIT representam qualquer valor dinâmico num único registrador de 64 bits.

**A consequência prática que sobrevive à prova:** NaN é o **único** valor de ponto flutuante que não é igual a si mesmo.

```c
int eh_nan(double x) { return x != x; }   // funciona, e é a implementação clássica de isnan()
```

Isso quebra a **reflexividade** da igualdade, e com ela qualquer estrutura que assuma ordenação total: um NaN dentro de um `std::sort` viola a *strict weak ordering* e é **comportamento indefinido** — pode corromper memória, não só devolver uma ordem esquisita. É a razão pela qual código numérico sério filtra NaN *antes* de ordenar, não depois.

---

### Referências para ir além

- **David Goldberg, *What Every Computer Scientist Should Know About Floating-Point Arithmetic* (1991)** — o artigo canônico sobre o assunto; gratuito, e cobre bias, subnormais e underflow gradual com as provas.
- **IEEE 754-2019** — o padrão em si. A seção 3 (formatos) e a 6 (valores especiais) respondem quase tudo desta aula de forma normativa.
- **Kahan, *Lecture Notes on the Status of IEEE 754*** — o próprio autor explicando *por que* cada decisão foi tomada, incluindo a briga pelo underflow gradual. Disponível na página dele em Berkeley.
- **`float.exposed` e `h-schmidt.net/FloatConverter`** — conversores interativos que mostram os três campos ao vivo; a forma mais rápida de conferir os padrões de $\pm 0$, $\inf$ e NaN discutidos aqui.
- **Bruce Dawson, *Comparing Floating Point Numbers*** (blog *Random ASCII*) — a série que desenvolve o truque de ordenação por padrão de bits e a comparação por ULPs.

---

## Aula 04 — Exceções, Arredondamentos e o Laço do Epsilon

### As cinco exceções: por que são *flags grudentas* e não erros

As notas listam as cinco exceções corretamente e registram a frase-chave do JB — "*usuário só pode zerar, e depois perguntar se algum bit foi levantado*". Essa frase esconde uma decisão de projeto que vale explicitar: as exceções do IEEE 754 são **sticky flags**, não interrupções.

Uma flag grudenta é ligada quando o evento ocorre e **nunca é desligada pelo hardware**. Ela permanece ligada mesmo que mil operações corretas aconteçam depois. Isso permite o padrão de uso que o JB descreveu:

```c
#include <fenv.h>
#pragma STDC FENV_ACCESS ON

feclearexcept(FE_ALL_EXCEPT);        // zera tudo antes
double r = calcula_coisa_complicada(x);
if (fetestexcept(FE_OVERFLOW | FE_INVALID))
    fprintf(stderr, "resultado suspeito\n");   // pergunta depois
```

O ganho é performance: nenhuma verificação acontece *dentro* do laço quente. Um bloco inteiro de álgebra linear roda na velocidade máxima e só no final se pergunta se algo deu errado. Se cada operação tivesse que testar seu próprio resultado, o custo seria proibitivo.

| Exceção | Macro C99 | Resultado padrão entregue |
|---|---|---|
| Operação inválida | `FE_INVALID` | **qNaN** |
| Divisão por zero | `FE_DIVBYZERO` | $\pm\infty$ (com o sinal correto) |
| Overflow | `FE_OVERFLOW` | $\pm\infty$ ou o maior finito, conforme o arredondamento |
| Underflow | `FE_UNDERFLOW` | subnormal ou $\pm 0$ |
| Inexato | `FE_INEXACT` | o resultado arredondado |

Duas observações que as notas não alcançam:

**`FE_INEXACT` liga praticamente sempre.** Qualquer conta cujo resultado exato não caiba no formato — o que inclui `0.1 + 0.2` — levanta essa flag. Ela é inútil como detector de erro e útil apenas em contextos muito específicos (verificar se uma divisão foi exata, por exemplo). É a flag que todo mundo mascara.

**Underflow tem duas definições no padrão, e elas discordam.** O 754 permite sinalizar underflow *antes* do arredondamento (o resultado exato é minúsculo) ou *depois* (o resultado arredondado é subnormal). Implementações diferentes escolhem diferente, e há casos em que uma sinaliza e a outra não. É uma das poucas ambiguidades genuínas que sobraram no padrão.

---

### Os quatro arredondamentos: por que "para o mais próximo" empata no par

O padrão define quatro modos — e o JB só entregou metade da resposta sobre *por que* eles existem.

| Modo | Nome no padrão | $2{,}5 \to$ | $3{,}5 \to$ | $-2{,}5 \to$ |
|---|---|---|---|---|
| Mais próximo, empate no par | `roundTiesToEven` (**padrão**) | 2 | 4 | −2 |
| Para zero | `roundTowardZero` (truncar) | 2 | 3 | −2 |
| Para $+\infty$ | `roundTowardPositive` | 3 | 4 | −2 |
| Para $-\infty$ | `roundTowardNegative` | 2 | 3 | −3 |

**Por que o empate vai para o par.** A regra ingênua da escola — "meio arredonda pra cima" — introduz **viés estatístico**: metade dos empates sobe e nenhum desce, então somas longas derivam sistematicamente para cima. Somar um milhão de valores com empates enviesados acumula erro *linear* em $n$. Com o empate no par, metade dos casos sobe e metade desce (porque a paridade da mantissa é essencialmente aleatória), o erro vira um passeio aleatório e cresce com $\sqrt{n}$. Em contas grandes a diferença é de ordens de grandeza.

**Por que existem os arredondamentos direcionados.** Essa é a pergunta que as notas registram e respondem só pela metade — "intervalos, voltamos para intervalos". A resposta completa: numa aritmética intervalar, $[a, b]$ representa a garantia de que o valor verdadeiro está ali dentro. Se o computador arredondar $a$ para cima ou $b$ para baixo, o intervalo **encolhe** e a garantia se perde — o valor verdadeiro pode ficar de fora. Para preservar a inclusão, cada extremo tem que ser arredondado *para fora*:

$$[a,b] \cdot [c,d] = \big[\ \triangledown\!\min(ac, ad, bc, bd),\ \ \triangle\!\max(ac, ad, bc, bd)\ \big]$$

onde $\triangledown$ arredonda para $-\infty$ e $\triangle$ para $+\infty$. É exatamente o "menor com menor / maior com maior" das notas, mas com a sutileza que faltava: os quatro produtos precisam ser todos calculados porque **sinais negativos trocam qual extremo produz qual**. Se $a<0<b$, o menor produto pode vir de $b \cdot c$, não de $a \cdot c$.

Sem os modos direcionados no hardware, aritmética intervalar seria impossível de implementar com eficiência — e é por isso que eles estão no padrão. O assunto volta com força na **Aula 27** de 2026/1.

---

### Os 80 bits, e o *double rounding* que eles causam

As notas acertam o fato — "você PODE/DEVE fazer a conta num registrador com casas a mais, um número bizarro de **80 bits**" — mas o interessante é o problema que isso cria.

O formato é o **x87 double extended**: 1 bit de sinal, 15 de expoente, 64 de mantissa (aqui o bit da frente é **explícito**, diferente do binary32/64). Precisão $p = 64$, contra 53 do `double`.

O padrão recomenda calcular em precisão maior porque isso protege contra resultados intermediários que estouram ou perdem precisão. O problema é que arredondar **duas vezes** — primeiro para 80 bits, depois para 64 ao guardar na memória — nem sempre dá o mesmo resultado que arredondar uma vez direto para 64. Esse é o **double rounding**, e ele quebra a reprodutibilidade:

```c
double a = ..., b = ..., c = ...;
double x = a*b + c;            // pode ficar num registrador de 80 bits
printf("%d\n", x == a*b + c);  // pode imprimir 0 — em x87, sem otimizações agressivas
```

O mesmo programa, compilado com `-O0` e com `-O2`, podia dar respostas diferentes — porque a otimização mudava *quando* o valor era despejado da pilha do x87 para a memória. Isso gerou bugs históricos famosos e a variável `FLT_EVAL_METHOD` do C99, que documenta qual precisão intermediária a implementação usa.

**O assunto morreu na prática.** Em x86-64, ponto flutuante passou a usar **SSE2**, que opera diretamente em 32 e 64 bits sem registradores estendidos. Toda máquina moderna calcula `double` em exatamente 64 bits. O x87 ainda existe por compatibilidade e para `long double`, mas o caminho padrão não passa mais por ele — e a reprodutibilidade voltou.

---

### O laço do epsilon: resolvendo a pergunta que ficou aberta

As notas terminam com a pergunta certa e sem resposta: "*por que o que eu achava estar acontecendo com o 1 está acontecendo de fato com o EPS?*" — e com a hipótese errada de que "dividir um float é simplesmente remover um bit".

Começando pela hipótese. Dividir um float por 2 **não remove nada**: decrementa o expoente e deixa a mantissa intacta. `EPS` mantém todos os seus bits significativos o tempo todo — ele só fica menor. Se o laço fosse `enquanto EPS > 0`, `EPS` sobreviveria 149 divisões (até $2^{-149}$, o menor subnormal) antes de virar zero.

Quem perde bits é a **soma**, não o `EPS`. Em $1{,}0 + \text{EPS}$, o resultado precisa ser representado com o expoente do $1$ — e a mantissa do float só tem 23 bits abaixo dele. Conforme `EPS` encolhe, a soma exata precisa de mais e mais bits à direita, até que não sobre nenhum:

| `EPS` | $1 + \text{EPS}$ exato | Representável? | Arredonda para |
|---|---|---|---|
| $2^{-22}$ | $1{,}000000238\ldots$ | sim | ele mesmo |
| $2^{-23}$ | $1 + $ último bit da mantissa | **sim, no limite** | ele mesmo |
| $2^{-24}$ | exatamente no meio entre $1$ e $1+2^{-23}$ | não | **$1{,}0$** (empate → par) |

O laço para em `EPS` $= 2^{-24}$, depois de 24 iterações. Note que é o **empate no par** que decide: $1 + 2^{-24}$ está exatamente a meio caminho entre dois representáveis, e a regra manda escolher aquele com mantissa par — que é o próprio $1{,}0$.

O último `EPS` para o qual $1 + \text{EPS} > 1$ ainda valia é $2^{-23} \approx 1{,}19 \times 10^{-7}$, e **esse** é o número que se chama **epsilon de máquina** ($\varepsilon$): a distância de $1$ até o próximo float. Formalmente, $\varepsilon = 2^{1-p}$.

| Tipo | $p$ | $\varepsilon = 2^{1-p}$ | Constante em C |
|---|---|---|---|
| `float` | 24 | $2^{-23} \approx 1{,}19\times10^{-7}$ | `FLT_EPSILON` |
| `double` | 53 | $2^{-52} \approx 2{,}22\times10^{-16}$ | `DBL_EPSILON` |
| x87 `long double` | 64 | $2^{-63} \approx 1{,}08\times10^{-19}$ | `LDBL_EPSILON` |

Duas armadilhas para fechar:

1. **$\varepsilon$ não é "o menor float".** O menor subnormal é $2^{-149}$, treze ordens de grandeza menor. $\varepsilon$ é uma medida de **precisão relativa**, não de magnitude — é a resolução da régua, não o começo dela.
2. **Rodar esse laço em x87 dá a resposta errada.** Se `1.0 + EPS` for calculado num registrador de 80 bits e comparado antes de ser despejado para a memória, o laço só para em $2^{-64}$ — medindo o epsilon do *registrador*, não o do tipo. É o mesmo fenômeno da seção anterior, aparecendo num programa de cinco linhas.

O corolário prático é a regra que todo mundo já ouviu sem saber de onde vem: nunca compare floats com `==`; compare com tolerância **relativa**, escalada por $\varepsilon$.

```c
int quase_igual(double a, double b) {
    double escala = fmax(fabs(a), fabs(b));
    return fabs(a - b) <= 8 * DBL_EPSILON * escala;   // tolerância proporcional, não absoluta
}
```

---

## Aula 05 — Abel–Ruffini, Descartes Formalizado e o Resto de Taylor

### O que Galois provou (e o que ele *não* provou)

As notas registram "em 1830 se determinou: não se tem COMO criar uma fórmula para grau 5". A afirmação está certa, mas o enunciado preciso é mais forte e mais estranho do que parece.

O resultado é o **Teorema de Abel–Ruffini**: não existe fórmula geral, **por radicais**, para as raízes de polinômios de grau $\ge 5$. Cada palavra importa.

- **"Por radicais"** significa: uma expressão finita construída a partir dos coeficientes usando apenas $+$, $-$, $\times$, $\div$ e raízes $\sqrt[n]{\ }$. Essa é a restrição decisiva, e é por isso que o teorema não diz "não dá para resolver".
- **"Geral"** significa: uma única fórmula que sirva para *todo* polinômio daquele grau. Quínticas específicas podem perfeitamente ser resolvidas por radicais — $x^5 - 2 = 0$ tem raiz $\sqrt[5]{2}$. O que não existe é a fórmula universal.
- O teorema **não** diz que as raízes não existem. Pelo Teorema Fundamental da Álgebra elas existem, todas as $n$ delas, no plano complexo. Só não há como escrevê-las com aquele vocabulário limitado.

A crédito histórico: **Ruffini** publicou uma prova quase completa em 1799, **Abel** fechou o argumento em 1824. A contribuição de **Galois** (1832, escrita na véspera do duelo que o matou aos 20 anos) foi mais profunda: ele deu um **critério** dizendo exatamente *quais* polinômios são solúveis por radicais. A resposta é que a equação é solúvel se e somente se um certo grupo de simetrias de suas raízes — o **grupo de Galois** — é um *grupo solúvel*. Para grau $\le 4$, esses grupos ($S_2, S_3, S_4$) são todos solúveis; $S_5$ não é. A fronteira em 5 não é acidente de notação, é uma mudança na estrutura de grupos.

**A consequência prática, que é o ponto da disciplina:** como não há fórmula, a única saída para grau $\ge 5$ é **iteração numérica**. Bisecção, secante, Newton, Aberth — toda a segunda metade da matéria existe por causa de um teorema de álgebra abstrata. E mesmo para graus 3 e 4, onde a fórmula existe, ninguém a usa: a fórmula de Cardano envolve raízes cúbicas de números complexos mesmo quando as três raízes são reais (o *casus irreducibilis*), e é numericamente instável. Newton é mais rápido e mais preciso.

---

### A regra de Descartes, enunciada direito — e a queda "de 2 em 2"

As notas deixam duas coisas em aberto: "*esse número cai de 2 em 2. Por quê? No futuro vemos isso*" e "*e as negativas? Não do mesmo jeito, é claro*". As duas têm resposta curta.

**O enunciado.** Seja $v$ o número de trocas de sinal na sequência de coeficientes **não nulos** de $p(x)$, escritos em ordem decrescente de grau. Então o número de raízes reais positivas, contadas com multiplicidade, é $v$ ou $v-2$ ou $v-4$, …, até 0 ou 1.

**Por que cai de 2 em 2.** Porque raízes complexas de um polinômio de coeficientes **reais** aparecem sempre em **pares conjugados**. Se $z = a + bi$ é raiz, então $\bar z = a - bi$ também é. A prova é de uma linha: a conjugação preserva somas e produtos, então

$$p(\bar z) = \overline{p(z)} = \bar 0 = 0.$$

Logo as raízes reais só podem sumir aos pares — cada par que "sai do eixo real" leva duas raízes de uma vez. É exatamente a animação que o JB mostrou na aula seguinte, com as raízes se aproximando e desaparecendo juntas conforme o parâmetro variava. E é por isso que a ressalva das notas — "*as raízes complexas são espelhadas, mas só quando os coeficientes são reais*" — está correta e é essencial: com coeficientes complexos, o argumento acima desaba e uma raiz complexa pode ser solitária.

**As raízes negativas são, sim, "do mesmo jeito".** O truque é aplicar a regra idêntica a $p(-x)$: cada raiz negativa de $p$ vira raiz positiva de $p(-x)$. Concretamente, troque o sinal dos coeficientes de grau **ímpar** e conte as trocas de novo.

Com o exemplo das notas, $p(x) = 4x^5 - 6x^4 + 12x^3 - 17x + 9$:

| | Sequência de sinais | Trocas | Conclusão |
|---|---|---|---|
| $p(x)$ | $+\ -\ +\ -\ +$ | **4** | 4, 2 ou 0 raízes positivas |
| $p(-x) = -4x^5 - 6x^4 - 12x^3 + 17x + 9$ | $-\ -\ -\ +\ +$ | **1** | exatamente **1** raiz negativa |

Quando a contagem dá exatamente 1, não há ambiguidade — não dá para subtrair 2 e continuar não-negativo. É por isso que as notas puderam afirmar com certeza "está confirmada 1 negativa" enquanto as positivas continuaram ambíguas.

Juntando com o grau: são 5 raízes no total, 1 negativa garantida, $x=0$ não é raiz (o termo constante é 9), então o saldo é $4 = (\text{positivas}) + (\text{complexas})$, com as complexas em número par. Os cenários possíveis são $(4,0)$, $(2,2)$ ou $(0,4)$ — Descartes estreita o campo, mas não decide. Para decidir é preciso avaliar o polinômio, e é aí que entram as cotas e a bisecção.

---

### O preço da série de Taylor: o resto de Lagrange

As notas identificam corretamente o custo da aproximação — "*usar um ponto da função como âncora; ela não imita 100% a função*" — e param no qualitativo. O quantitativo é o que torna Taylor utilizável.

Truncando a série no grau $n$ em torno da âncora $a$, o erro tem forma fechada. Existe algum $\xi$ entre $a$ e $x$ tal que

$$\underbrace{f(x) - \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k}_{\text{erro de truncamento}} \;=\; \frac{f^{(n+1)}(\xi)}{(n+1)!}\,(x-a)^{n+1}.$$

Três leituras que essa fórmula entrega de graça:

1. **O erro morre com $(x-a)^{n+1}$.** Perto da âncora, dobrar o grau não melhora um pouco — melhora exponencialmente. Longe da âncora, o mesmo fator explode. É a formalização exata do "depende da âncora escolhida".
2. **O fatorial no denominador é quem faz a série funcionar.** Para $\sin$ e $\cos$, $|f^{(n+1)}| \le 1$ sempre, então o erro é limitado por $|x-a|^{n+1}/(n+1)!$ — que vai a zero para *qualquer* $x$. É por isso que essas séries convergem em toda a reta, enquanto $1/(1-x)$ só converge em $|x|<1$.
3. **Não se sabe quem é $\xi$** — só que existe. Na prática usa-se a cota $\max |f^{(n+1)}|$ no intervalo, o que dá um limite superior seguro para o erro. É assim que bibliotecas como a `libm` escolhem quantos termos usar.

**A ressalva que quase nunca é dita:** ter todas as derivadas não garante que a série represente a função. O contraexemplo canônico é

$$f(x) = \begin{cases} e^{-1/x^2}, & x \ne 0 \\ 0, & x = 0\end{cases}$$

que é infinitamente derivável e tem **todas** as derivadas nulas em $0$. Sua série de Taylor em torno de $0$ é identicamente zero, e portanto não se parece com $f$ em ponto nenhum exceto na âncora. Funções em que a série converge para a própria função são chamadas **analíticas**, e são uma subclasse estrita das infinitamente deriváveis. Sobre os complexos essa patologia desaparece — toda função derivável é analítica —, o que é uma das razões pelas quais análise complexa é mais bem-comportada que análise real.

---

## Aula 06 — Horner é Ótimo, Bisecção é Previsível

### Horner: a prova de que não dá para fazer melhor

As notas apresentam a forma de Horner como "jeito mega-econômico de escrever um polinômio" e mostram o padrão aninhado. Falta dizer o quanto se economiza e que isso é **comprovadamente ótimo**.

Para $p(x) = a_n x^n + \dots + a_1 x + a_0$, a reescrita é

$$p(x) = a_0 + x\big(a_1 + x\big(a_2 + \dots + x(a_{n-1} + x\,a_n)\dots\big)\big)$$

— exatamente o que as notas escreveram "de trás pra frente" (e a razão do $0$ explícito no lugar do $x^2$ ausente: a forma exige **todos** os coeficientes, inclusive os nulos).

| Estratégia | Multiplicações | Somas |
|---|---|---|
| Ingênua com `pow()` | $n$ chamadas a `pow` + $n$ | $n$ |
| Ingênua com potências repetidas | $\sim n(n+1)/2$ | $n$ |
| Potências acumuladas ($x^k = x^{k-1}\cdot x$) | $2n$ | $n$ |
| **Horner** | $\mathbf{n}$ | $\mathbf{n}$ |

E o resultado bonito: **Ostrowski** (1954) provou que $n$ somas são necessárias, e **Pan** (1966) provou que $n$ multiplicações são necessárias, para qualquer método que avalie um polinômio geral de grau $n$. Horner não é apenas bom — é **ótimo**, e o problema está fechado desde então.

A observação das notas sobre `pow()` merece precisão: o problema não é só a contagem de operações, é que `pow(x, k)` é uma função transcendental implementada com $\exp$ e $\log$. Ela custa dezenas de ciclos, não vetoriza bem, e **introduz erro de arredondamento próprio** — `pow(x,2)` pode não dar exatamente `x*x`. Horner usa apenas multiplicação e soma, ambas candidatas a **FMA** (`fused multiply-add`), que calcula `a*b+c` com um único arredondamento. Um laço de Horner com FMA é praticamente a operação ideal para um processador moderno:

```c
double horner(const double a[], int n, double x) {
    double r = a[n];
    for (int i = n - 1; i >= 0; i--)
        r = fma(r, x, a[i]);      // r*x + a[i], um arredondamento só
    return r;
}
```

**O bônus que ninguém conta:** o laço de Horner é literalmente a **divisão sintética** por $(x - x_0)$. Os valores intermediários de `r` são os coeficientes do quociente, e o valor final é o resto — que, pelo Teorema do Resto, vale $p(x_0)$. Isso significa que avaliar e **deflacionar** o polinômio são a mesma operação: achou uma raiz, aplique Horner, e o array de intermediários já é o polinômio de grau $n-1$ para continuar a busca. Aplicando Horner duas vezes obtém-se $p(x_0)$ e $p'(x_0)$ simultaneamente — exatamente os dois números de que o método de Newton precisa.

---

### Bisecção: quantas iterações, e o bug que ninguém vê

As notas capturam o método ("é uma pesquisa binária") e suas limitações reais — fica presa no intervalo, acha uma raiz só, pode pular pares de raízes. O que falta é o que torna a bisecção insubstituível: ela é o único método aqui com **garantia determinística**.

**A hipótese.** Exige-se $f$ contínua em $[a,b]$ com $f(a)\cdot f(b) < 0$. O **Teorema de Bolzano** (caso particular do Teorema do Valor Intermediário) garante então que existe pelo menos uma raiz dentro. Essa hipótese explica de uma vez as duas limitações das notas: o método pula raízes de multiplicidade par porque nelas o sinal **não troca**, e não sai do intervalo porque a garantia só vale ali dentro.

**A conta das iterações.** O intervalo tem largura $b-a$ e cada passo o corta pela metade, então após $n$ passos a incerteza é $(b-a)/2^n$. Para garantir erro $\le \epsilon$:

$$n \;\ge\; \log_2\!\left(\frac{b-a}{\epsilon}\right)$$

Isso é uma propriedade rara: dá para dizer **antes de rodar** quantos passos serão necessários. Nenhum dos métodos rápidos (secante, Newton) oferece isso — eles podem convergir em 4 iterações ou divergir para sempre. Em `double`, partindo de um intervalo de largura 1 e indo até a precisão da máquina, são cerca de **52 iterações**, sempre. Convergência **linear**, com fator exatamente $1/2$ — cerca de um bit de resposta por iteração, que é a leitura correta do "vai se fechando passinho a passinho" das notas.

**O bug clássico.** Escrever o ponto médio como

```c
double m = (a + b) / 2.0;      // errado em dois cenários distintos
```

falha quando `a + b` estoura para $\pm\infty$ (com valores grandes) e, em aritmética inteira, quando a soma estoura e o resultado vira negativo — foi exatamente esse o bug da busca binária do `java.util.Arrays.binarySearch`, que passou nove anos na biblioteca padrão do Java antes de ser encontrado em 2006. A forma segura:

```c
double m = a + (b - a) / 2.0;  // nunca sai do intervalo [a,b]
```

**O critério de parada também é sutil.** Parar quando $|f(m)| < \epsilon$ é tentador e errado: numa função de inclinação muito suave, $|f|$ pode ser minúsculo longe da raiz; numa função íngreme, pode ser grande já em cima dela. O critério confiável é o **do intervalo**, $|b-a| < \epsilon$, porque é sobre ele que há garantia. Na prática usa-se tolerância relativa, `|b-a| <= tol*|m|`, pelo mesmo motivo que se compara floats com tolerância relativa.

**Como isso é usado de verdade.** Ninguém usa bisecção pura em produção, e ninguém usa Newton puro: usa-se um **híbrido**. O **método de Brent** mantém um intervalo com sinais opostos (herdando a garantia da bisecção) e tenta a cada passo uma interpolação quadrática inversa — rápida como a secante. Se o passo rápido cai fora do intervalo ou não está encolhendo o suficiente, ele cai de volta na bisecção. O resultado tem a velocidade de um método superlinear e a garantia de terminação de um método linear. É o que está por trás de `scipy.optimize.brentq` e do `uniroot` do R.

---

## Aula 08 — Consolidação: o Bloco de Solução de Equações

As notas registram apenas "folinhas entregues" — aula inteira de exercícios. Vale, então, um mapa do que estava fechado a essa altura do semestre, porque é exatamente o recorte que cai em prova e o que os ExLabs cobram.

### O fluxo completo, do polinômio às raízes

Encontrar as raízes de um polinômio não é um método único, é um pipeline. Cada aula anterior entregou uma peça:

| Etapa | Pergunta | Ferramenta | Aula |
|---|---|---|---|
| 1 | Quantas raízes existem? | Grau do polinômio (TFA) | 05 |
| 2 | Quantas são reais, e de que sinal? | **Regra de Descartes** em $p(x)$ e $p(-x)$ | 05 |
| 3 | Onde elas podem estar? | Cotas de **Cauchy / Lagrange / Fujiwara** | 05 |
| 4 | Onde há troca de sinal? | Varredura avaliando com **Horner** | 06 |
| 5 | Refinar cada raiz | **Bisecção**, depois secante/Newton | 06, 09 |
| 6 | Continuar com o resto | **Deflação** (Horner de novo) | 06 |

O erro mais comum em prova é pular a etapa 3: sem cota, não há intervalo inicial, e sem intervalo inicial a bisecção não tem o que bisseccionar. A cota de **Cauchy**, $1 + \max_i |a_i/a_n|$, é a mais apertada das simples e vale a pena decorar — todas as raízes, **inclusive as complexas**, ficam dentro do disco de raio igual à cota. O detalhamento das três cotas está na **Aula 06** de 2026/1, em `adicoes.md`.

### Os três erros de conta que aparecem nas folhas

1. **Esquecer coeficientes nulos.** Tanto em Descartes quanto em Horner, o polinômio precisa estar escrito com **todos** os graus. $x^5 + 11x - 16$ tem coeficientes $[1, 0, 0, 0, 11, -16]$, e é o $0$ do $x^2$ que as notas destacam na forma aninhada.
2. **Confundir cota com raiz.** A cota diz "não olhe fora daqui". Ela é quase sempre folgada: para $p(x) = x^4 + 6x + 10$ a cota de Cauchy dá 11, e não há raiz real nenhuma. Cota grande não significa raiz grande.
3. **Aplicar Descartes ignorando multiplicidade.** A regra conta raízes **com multiplicidade**. Uma raiz dupla positiva consome duas unidades da contagem, não uma.

### Por que a deflação é perigosa

O passo 6 tem uma armadilha que raramente é mencionada: dividir o polinômio pela raiz encontrada propaga o **erro** dessa raiz para todos os coeficientes do quociente. Se a primeira raiz foi encontrada com erro na 6ª casa, a segunda sai com erro na 5ª, a terceira na 4ª, e assim por diante — a precisão degrada a cada deflação.

As duas mitigações padrão: deflacionar sempre **da menor raiz em magnitude para a maior** (é a ordem numericamente estável), e usar as raízes da deflação apenas como **chute inicial**, refinando cada uma com algumas iterações de Newton no polinômio **original**. Essa fragilidade é, aliás, o argumento a favor dos métodos simultâneos que aparecem na Aula 10 — Aberth acha todas de uma vez e nunca deflaciona.

---

## Aula 09 — Ordens de Convergência e o Índice de Eficiência

### Definindo "mais rápido" com precisão

As notas comparam bisecção, secante e Newton por adjetivos — "linear", "bem mais rápida", "quadrática" — e citam o expoente $1{,}618$ sem explicar de onde vem. A definição formal fecha tudo.

Seja $e_n = |x_n - r|$ o erro na iteração $n$. O método tem **ordem $p$** se

$$\lim_{n\to\infty} \frac{e_{n+1}}{e_n^{\,p}} = C, \qquad 0 < C < \infty.$$

| Método | Ordem $p$ | Leitura prática |
|---|---|---|
| Bisecção | $1$ ($C = 1/2$) | ganha $\approx 1$ bit por iteração |
| Secante | $\varphi \approx 1{,}618$ | os dígitos corretos são multiplicados por 1,6 |
| **Newton** | $2$ | os dígitos corretos **dobram** por iteração |

Convergência quadrática é espetacular em números: com 1 dígito correto, as iterações seguintes dão 2, 4, 8, 16 — de um chute grosseiro até a precisão de um `double` em cerca de 5 passos. É por isso que Newton domina apesar de todos os seus defeitos.

### De onde sai a razão áurea

Essa é a pergunta que as notas deixam no link da Wikipédia. A dedução é curta e bonita.

A análise de erro da secante produz a recorrência

$$e_{n+1} \approx C\, e_n\, e_{n-1}.$$

Procurando uma solução da forma $e_n \approx K e_{n-1}^{\,p}$ e comparando os expoentes dos dois lados, chega-se a

$$p = 1 + \frac{1}{p} \quad\Longrightarrow\quad p^2 - p - 1 = 0.$$

A raiz positiva é $p = \frac{1+\sqrt5}{2} = \varphi \approx 1{,}618$. A razão áurea não foi enfiada ali por estética: ela é a **raiz da equação característica** que descreve como o erro se propaga quando cada passo usa os *dois* passos anteriores. É o mesmo motivo pelo qual $\varphi$ governa Fibonacci — a mesma recorrência de dois termos, o mesmo polinômio característico.

### Newton: a derivação, e as quatro formas de quebrar

A fórmula $x_{n+1} = x_n - f(x_n)/f'(x_n)$ sai de truncar Taylor no primeiro grau: aproxima-se $f$ pela sua reta tangente em $x_n$ e toma-se a raiz da reta como próximo palpite. Isso torna exata a intuição registrada nas notas — "imagina a secante, mas trazendo $x_1$ tão perto de $x_2$ que a reta vira a derivada". A secante usa uma reta por **dois pontos**; Newton usa a reta **tangente**, que é o limite da anterior.

O que as notas chamam de "negócio que só tem vantagens" tem, na verdade, quatro modos de falha bem documentados:

1. **Derivada nula ou minúscula.** $f'(x_n) \approx 0$ atira o próximo ponto para o infinito. Geometricamente: a tangente é horizontal e não cruza o eixo.
2. **Ciclo.** Existem funções e chutes para os quais Newton oscila entre dois pontos para sempre, sem divergir nem convergir.
3. **Divergência garantida.** Para $f(x) = \sqrt[3]{x}$ com raiz em $0$, a iteração dá $x_{n+1} = -2x_n$ — o erro **triplica em módulo** a cada passo, a partir de qualquer chute. Newton diverge sistematicamente numa função contínua com raiz única.
4. **Raízes múltiplas destroem a ordem.** Se a raiz tem multiplicidade $m > 1$, $f$ e $f'$ se anulam juntas e a convergência cai para **linear** com fator $1 - 1/m$. A correção é o **Newton modificado**, $x_{n+1} = x_n - m\,f(x_n)/f'(x_n)$, que restaura a ordem 2 — se $m$ for conhecido.

O teorema que dá a garantia é local: se $r$ é raiz simples, $f$ é duas vezes derivável e $x_0$ está **suficientemente perto** de $r$, então a convergência é quadrática. "Suficientemente perto" é a letra miúda que a prática cobra — e é por isso que se usa bisecção para chegar perto e Newton para terminar.

### O resultado contraintuitivo: a secante ganha de Newton

As notas identificam o custo de Newton ("o que incomoda é o cálculo de derivadas") sem tirar a conclusão. A conclusão é que **a secante costuma ser mais eficiente**.

Comparar ordens de convergência é injusto se as iterações custam diferente. A medida correta é o **índice de eficiência**, $E = p^{1/m}$, onde $m$ é o número de avaliações de função por iteração.

| Método | Ordem $p$ | Avaliações por iteração | Índice $E = p^{1/m}$ |
|---|---|---|---|
| Newton | 2 | 2 ($f$ e $f'$) | $2^{1/2} \approx 1{,}414$ |
| **Secante** | 1,618 | **1** (reaproveita a anterior) | $\mathbf{1{,}618}$ |

Quando avaliar $f'$ custa aproximadamente o mesmo que avaliar $f$ — o caso comum — a secante entrega **mais precisão por unidade de trabalho**. Newton só ganha quando a derivada é barata: em polinômios, onde um único laço de Horner devolve $p$ e $p'$ de uma vez, ou quando se tem diferenciação automática (o assunto da Aula 26 de 2026/1, que calcula gradientes exatos a custo constante).

Some-se a isso que a secante não exige derivada nenhuma — o que a torna a única opção quando $f$ vem de uma simulação, de uma tabela ou de código de terceiros. É por isso que ela continua viva num mundo em que Newton é "teoricamente melhor".

---

## Aula 10 — Weierstrass, Ehrlich–Aberth e o Buraco na Teoria

### Durand–Kerner: a fórmula por trás dos "newtonzinhos"

As notas descrevem a ideia — vários Newtons correndo pelo plano, com o problema de caírem todos na mesma raiz — e a solução por "repulsão". Vale ver as fórmulas, porque elas são surpreendentemente simples.

O método de **Weierstrass–Durand–Kerner** parte de $n$ chutes $z_1, \dots, z_n$ simultâneos, um por raiz, e atualiza cada um por

$$z_i \;\leftarrow\; z_i - \frac{p(z_i)}{a_n \prod_{j \ne i} (z_i - z_j)}.$$

O denominador é a chave. Se todas as estimativas estivessem certas, $a_n\prod_{j\ne i}(z_i - z_j)$ seria exatamente $p'(z_i)$ — a fórmula viraria Newton puro. Como as estimativas ainda estão erradas, esse produto funciona como uma **derivada aproximada usando as outras raízes como referência**. É deflação sem deflacionar: cada estimativa divide fora a influência das outras, mas o polinômio original nunca é modificado, então o erro de uma raiz não contamina permanentemente as demais.

Cronologia, que as notas registram corretamente: **Weierstrass** (1891) como origem, redescoberto por **Durand** (1960) e **Kerner** (1966). A convergência é quadrática perto da solução.

### Ehrlich–Aberth: onde a repulsão aparece de fato

**Ehrlich** (1967) e **Aberth** (1973) melhoraram a ideia acrescentando explicitamente o termo de correção:

$$z_i \;\leftarrow\; z_i - \cfrac{\dfrac{p(z_i)}{p'(z_i)}}{1 - \dfrac{p(z_i)}{p'(z_i)}\displaystyle\sum_{j\ne i}\frac{1}{z_i - z_j}}$$

Leia por partes. O numerador é **exatamente o passo de Newton**. Todo o resto é um denominador corretivo, e nele mora o somatório $\sum_{j \ne i} 1/(z_i - z_j)$ — o **termo repulsor** que as notas descrevem como "cargas de elétrons".

A analogia do JB é melhor do que parece, e dá para torná-la precisa: $1/(z_i - z_j)$ é literalmente a forma do campo de uma carga pontual em duas dimensões. Quando $z_i$ se aproxima demais de $z_j$, esse termo explode, o denominador cresce, e o **passo encolhe** — a estimativa é freada antes de colidir com a vizinha. Quando as estimativas estão bem separadas, o somatório é pequeno, o denominador tende a 1, e o método volta a ser Newton com sua convergência quadrática. Repulsão forte de perto, Newton puro de longe.

Convergência cúbica para raízes simples, e todas as $n$ raízes — reais e complexas — saem de uma vez, sem deflação. É a resposta direta ao problema levantado na Aula 08.

**Um ajuste de crédito.** As notas dizem que "Aberth modifica a ideia inicial de Bini". A ordem é a inversa: Aberth publicou em 1973; **Dario Bini** (a partir de 1996, com Fiorentino em 2000) construiu o **MPSolve**, a implementação de referência em precisão múltipla *do* método de Ehrlich–Aberth. A contribuição de Bini foi resolver o problema que a fórmula acima não resolve — **a inicialização**. Chutes ruins fazem o método divergir ou convergir devagar; Bini usa o **polígono de Newton** dos coeficientes para posicionar os $n$ chutes iniciais em círculos concêntricos de raios estimados a partir das magnitudes dos coeficientes. É essa inicialização que faz o método funcionar em polinômios de grau alto.

### O buraco que o JB encontrou

A observação das notas — "*os métodos que funcionam muito bem não foram provados, e os provados não rodam muito bem*" — descreve com precisão o estado real da área, e é um caso raro de teoria atrasada em relação à prática.

**O lado sem prova.** Ehrlich–Aberth converge de forma confiável na prática, em milhares de polinômios de grau alto. Mas não existe teorema de **convergência global**: a garantia conhecida é local (perto da solução, converge cúbico). Ninguém provou que, a partir da inicialização de Bini, o método converge para **todo** polinômio. É conjectura amparada em evidência empírica massiva.

**O lado com prova.** O método de **Newton** aplicado ao plano complexo tem garantias demonstradas. Hubbard, Schleicher e Sutherland (2001) construíram conjuntos de pontos iniciais **provadamente suficientes** para achar todas as raízes, e trabalhos posteriores de Schleicher e Stoll levaram isso à prática, achando as raízes de polinômios de grau um milhão. A parte irônica, e que fecha o paradoxo das notas: por muito tempo essa abordagem provada era mais lenta que o Aberth sem prova — e a pesquisa recente consiste justamente em fechar essa distância pelos dois lados.

Vale registrar o que isso significa para a disciplina. Em análise numérica, "funciona" e "está provado que funciona" são propriedades independentes, e uma biblioteca séria é aquela que documenta qual das duas ela oferece. A bisecção da Aula 06, com sua fórmula $n \ge \log_2((b-a)/\epsilon)$, está no extremo oposto do espectro: lenta, limitada, e com garantia absoluta.

---

### Referências para ir além — Parte 2

- **Nick Higham, *Accuracy and Stability of Numerical Algorithms* (2ª ed., SIAM)** — a referência para erro de arredondamento, epsilon de máquina, double rounding e estabilidade de Horner.
- **Cleve Moler, *Numerical Computing with MATLAB*** — os capítulos de zeros e de raízes de polinômios trazem bisecção, secante, Newton e o método de Brent com o código lado a lado.
- **Brent, *Algorithms for Minimization Without Derivatives* (1973)** — o livro que define o método híbrido usado em `brentq`, `fzero` e `uniroot`.
- **MPSolve (Bini & Fiorentino) — `numpi.dm.unipi.it/mpsolve`** — a implementação de referência do Ehrlich–Aberth, com os artigos sobre a inicialização por polígono de Newton.
- **Ian Stewart, *Galois Theory* (4ª ed.)** — Abel–Ruffini e o critério de solubilidade explicados do zero, sem pressupor álgebra abstrata.
- **Hubbard, Schleicher & Sutherland, *How to find all roots of complex polynomials by Newton's method* (Invent. Math., 2001)** — o artigo do "lado provado" discutido na Aula 10.
