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
