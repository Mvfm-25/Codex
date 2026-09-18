# Métodos Formais para Computação — Adições & Aprofundamentos
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas. Segue os tópicos na ordem em que apareceram nas notas, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---

## Aula 01 — V&V, os Limites do Teste e os Três Acidentes

### "Teste Não Garante Correção de Porcaria Nenhuma" — a Frase Tem Autor e Forma Precisa

A afirmação do Júlio é a formulação informal de uma das frases mais citadas da computação, de **Edsger Dijkstra** (1969):

> *"Program testing can be used to show the presence of bugs, but never to show their absence."*

O argumento por trás é de cardinalidade, e vale explicitar porque é o que **justifica a existência da disciplina inteira**. Considere a função da Aula 02:

```java
static int pontoMedio(int a, int b)
```

O domínio de entrada é $2^{32} \times 2^{32} = 2^{64}$ pares — cerca de $1{,}8 \times 10^{19}$ casos. A um bilhão de testes por segundo, testar exaustivamente levaria **~585 anos**. E essa é uma função de duas linhas com dois parâmetros inteiros; qualquer programa real tem domínio astronomicamente maior.

Testar é, portanto, **amostragem** de um espaço que não pode ser percorrido. Uma prova formal não amostra: ela raciocina sobre a estrutura do programa e cobre o domínio inteiro de uma vez. É a diferença entre verificar que $2+2=4$, $3+3=6$, $5+5=10$ e provar que a soma de dois pares é par.

Isso **não** torna o teste inútil — ele é barato, encontra defeitos reais, não exige especificação formal e detecta erros de premissa que uma prova sobre a especificação errada jamais pegaria. A relação é de complementaridade, não de substituição.

### Verificação vs. Validação — a Distinção Que Cai na Prova

As duas perguntas da aula são a definição padrão (Boehm, 1979), e a confusão entre elas é erro clássico:

| | **Verificação** | **Validação** |
|---|---|---|
| Pergunta | *"Estamos construindo o produto **corretamente**?"* | *"Estamos construindo o **produto correto**?"* |
| Compara com | A **especificação** | As **necessidades reais** do usuário |
| Se falha | O software não faz o que foi especificado | O software faz o que foi especificado — e o especificado estava errado |
| Exemplos | Testes unitários e funcionais, revisão de código, **prova formal** | Testes de aceitação, protótipos, homologação com o cliente |

A assimetria importante: **métodos formais só atacam a verificação**. Uma prova estabelece que a implementação satisfaz a especificação — se a especificação não corresponde ao que o cliente queria, a prova é impecável e o produto é inútil. É por isso que a Aula 02 gasta tanto tempo em *extrair a especificação do cliente* antes de qualquer prova: a parte formal é a metade fácil.

Encaixando as três técnicas da aula nesse quadro:

| Técnica | Executa o software? | Cobertura | Custo |
|---|---|---|---|
| **Estática** (revisão, análise estática, *linters*) | Não | Parcial, heurística | Baixo |
| **Dinâmica** (testes) | Sim | Só os casos executados | Médio |
| **Formal** (prova, *model checking*) | Não | **Todo o domínio** | Alto |

### Os Três Acidentes: o Que Realmente Aconteceu

Ariane 5, Therac-25 e Pentium FDIV são citados em toda introdução da área e quase nunca explicados. Os três têm causa técnica precisa, e cada um ilustra um tipo diferente de falha:

**Ariane 5, voo 501 (4 de junho de 1996) — falha de especificação reaproveitada.** 37 segundos após a decolagem, o foguete se autodestruiu; ~US$ 370 milhões. A causa: uma conversão de um `float` de 64 bits (velocidade horizontal) para um **inteiro com sinal de 16 bits** transbordou. O código era herdado do Ariane 4 e a rotina em questão — alinhamento inercial — **nem precisava rodar após a decolagem**; ficou ligada por conveniência de reuso. Como o Ariane 5 era mais rápido, o valor saiu da faixa. A exceção não tratada derrubou o computador inercial, o reserva executava o mesmo código e falhou identicamente 72 milissegundos antes, e o controle de voo interpretou o diagnóstico como dado válido. **Redundância não protege contra defeito de software: as duas cópias erram junto.**

**Therac-25 (1985–1987) — race condition mata.** Um acelerador linear de radioterapia entregou doses de radiação ~100× acima do prescrito; ao menos três mortes. Duas falhas combinadas: (1) uma **race condition** entre a tarefa de entrada de dados e a de posicionamento — se o operador editasse a prescrição rápido demais (em menos de 8 segundos), o magneto ficava fora de posição enquanto o feixe já estava configurado em alta potência; (2) um **contador de um byte** que transbordava, e quando o valor dava zero uma checagem de segurança era pulada. O agravante: os modelos anteriores tinham **travas eletromecânicas de hardware** removidas no Therac-25 sob o argumento de que "o software cuidava disso".

**Pentium FDIV (1994) — cinco células vazias.** A instrução de divisão em ponto flutuante usava o algoritmo SRT com uma tabela de consulta de 1066 entradas. Cinco entradas não foram copiadas para o silício, e a divisão retornava resultado errado a partir da 4ª casa decimal em certos operandos. A Intel argumentou que o erro atingiria um usuário típico "a cada 27 mil anos" e depois recolheu os chips: **prejuízo de US$ 475 milhões**. Não era erro de código — era erro de **dado numa tabela**, o tipo de defeito que teste por amostragem tem probabilidade quase nula de encontrar e que verificação formal do circuito encontra imediatamente. Não por acaso, a Intel se tornou uma das maiores usuárias de verificação formal de hardware depois disso.

O padrão comum: nos três, o teste convencional passou. É exatamente o argumento de Dijkstra em forma de fatura.

---

## Aula 02 — Contratos, o Ponto Médio e um Bug Famoso

### O `(a+b)/2` é Um dos Bugs Mais Famosos da Computação

A conclusão a que a aula chegou no final — "somando dois números int gigantes, dá overflow, voltando um número negativo" — não é uma hipótese de sala de aula. É um defeito real que ficou escondido por **duas décadas** na busca binária mais citada da literatura.

O algoritmo foi publicado por **Jon Bentley** em *Programming Pearls* (1986), com a observação de que a busca binária foi descrita pela primeira vez em 1946 e uma versão correta só apareceu em 1962. Em 2006, **Joshua Bloch** — que havia implementado `java.util.Arrays.binarySearch` — publicou o artigo *Extra, Extra — Read All About It: Nearly All Binary Searches and Mergesorts Are Broken*, mostrando que a linha

```java
int mid = (low + high) / 2;      // quebrado
```

transborda quando `low + high` excede $2^{31}-1$. Em Java, o overflow de `int` é silencioso e o resultado vira negativo, produzindo `ArrayIndexOutOfBoundsException`. O bug estava no JDK, em *Programming Pearls*, e em incontáveis livros e códigos derivados.

As correções:

```java
int mid = low + (high - low) / 2;   // portável; (high - low) não transborda se low <= high
int mid = (low + high) >>> 1;       // Java: deslocamento sem sinal trata os bits como unsigned
```

O ponto que interessa para a disciplina: **o programa satisfazia a especificação matemática e mesmo assim estava errado**, porque `int` não é $\mathbb{N}$ nem $\mathbb{Z}$ — é $\mathbb{Z}$ módulo $2^{32}$. Foi exatamente a conclusão do Júlio no final da aula. Uma prova de correção que ignore a representação da máquina prova a coisa errada; é por isso que ferramentas sérias de verificação modelam aritmética de largura fixa (*bitvectors*) em vez de inteiros ideais.

### A Tripla de Hoare — a Notação Por Trás de PRÉ e PÓS

O que a aula escreveu como PRÉ e PÓS tem notação formal, e ela é o objeto central da **lógica de Hoare** (C. A. R. Hoare, *An Axiomatic Basis for Computer Programming*, 1969):

$$\{P\}\; S \;\{Q\}$$

Leitura: *se* o predicado $P$ (pré-condição) vale antes de executar o comando $S$, *então* $Q$ (pós-condição) vale depois. Para o ponto médio:

$$\{\, a \ge 0 \land b \ge 0 \land a \le b \,\}\;\; r := \texttt{pontoMedio}(a,b) \;\;\{\, r = \lfloor (a+b)/2 \rfloor \,\}$$

Uma distinção que aparece cedo e confunde:

- **Correção parcial** — *se* $S$ terminar, $Q$ vale. É o que a tripla acima afirma.
- **Correção total** — $S$ **termina** e $Q$ vale. Exige uma prova adicional de terminação, normalmente por um **variante**: uma expressão que decresce a cada iteração e é limitada inferiormente (tipicamente em $\mathbb{N}$), o que impede laço infinito.

Essa é a razão de a ementa da Aula 01 listar *"assertivas, pré e pós-condições, invariantes e variantes"* como quatro coisas: **invariante** é o que se mantém verdadeiro a cada volta do laço (a alma da prova de correção), **variante** é o que garante que o laço acaba.

Vale notar que a tripla de Hoare é a formalização do que a aula chamou de "sempre útil pedir ao cliente um exemplo": os exemplos `[0,10] → 5` e `[3,10] → 6` são **instâncias** da pós-condição. Eles ajudam a *descobrir* $Q$ e servem para conferi-la, mas $Q$ é a afirmação universal que os exemplos apenas ilustram.

### Design by Contract: Por Que o Cliente é Quem Erra

A intuição da aula — "se o cliente passa [7,1], o programa continua correto, ele é que quebrou o contrato" — é literalmente a tese do **Design by Contract**, formulado por **Bertrand Meyer** para a linguagem **Eiffel**. A analogia é comercial e simétrica:

| | **Obrigação** | **Benefício** |
|---|---|---|
| **Cliente** (quem chama) | Garantir a **pré-condição** — só chamar com $a \ge 0 \land b \ge 0 \land a \le b$ | Recebe a **pós-condição** garantida |
| **Fornecedor** (a rotina) | Garantir a **pós-condição** | Pode **assumir** a pré-condição — não precisa validar nada |

O benefício do fornecedor é a parte contraintuitiva e a mais valiosa: como a pré-condição é obrigação do cliente, a rotina **não precisa de código defensivo**. Nada de `if (a > b) return -1;`. A verificação acontece uma vez, no ponto de chamada, e não em toda invocação em todo lugar.

Daí a regra prática que orienta o desenho:

- **Pré-condição forte** = contrato fácil para o fornecedor, difícil para o cliente.
- **Pré-condição fraca (no limite, $\top$)** = a rotina aceita tudo e precisa lidar com tudo.

E a diferença conceitual que costuma cair: **violação de pré-condição não é exceção de negócio, é bug**. Exceções tratam situações previstas e recuperáveis (arquivo ausente, rede caiu); a quebra de contrato indica que o *código chamador* está errado e precisa ser corrigido, não tratado. É por isso que em C isso vira `assert()`, que some no *build* de produção — asserções documentam e detectam bugs em desenvolvimento, não substituem validação de entrada externa.

Um adendo útil sobre herança, já que a Engenharia de Software II ronda o assunto: uma subclasse pode **enfraquecer** a pré-condição e **fortalecer** a pós-condição, nunca o contrário. Isso é exatamente o **Princípio da Substituição de Liskov** enunciado por contratos — o "L" do SOLID não é uma diretriz de estilo, é uma condição sobre pré e pós-condições.

### Da Pós-Condição para o Programa: a Pré-Condição Mais Fraca

A aula seguiu o caminho natural — escrever o programa, depois checar se está correto. A lógica de Hoare permite o caminho inverso, que é onde a disciplina costuma chegar: **Dijkstra** definiu $\mathrm{wp}(S, Q)$, a **pré-condição mais fraca** (*weakest precondition*) — o predicado mais permissivo que garante $Q$ após executar $S$.

A regra da atribuição é a mais simples e a mais surpreendente, porque funciona **de trás para frente**:

$$\mathrm{wp}(x := e,\; Q) \;=\; Q[x \backslash e]$$

Isto é: substitua toda ocorrência de $x$ em $Q$ pela expressão $e$. Aplicando ao ponto médio, com $Q \equiv (r = \lfloor (a+b)/2 \rfloor)$ e $S \equiv (r := (a+b)/2)$:

$$\mathrm{wp} = \big( (a+b)/2 = \lfloor (a+b)/2 \rfloor \big)$$

Sobre os inteiros, a divisão inteira **já é** o piso para operandos não-negativos, então isso reduz a $a + b \ge 0$ — e a pré-condição $a \ge 0 \land b \ge 0$ da aula é suficiente para garanti-la. A prova fecha, e note que ela nunca executou o programa nem escolheu um caso de teste.

A relação com a tripla: $\{P\}\,S\,\{Q\}$ é válida **se e somente se** $P \Rightarrow \mathrm{wp}(S, Q)$. Verificar um programa vira, então, gerar uma fórmula lógica e checar se ela é válida — que é precisamente o que ferramentas como **Dafny**, **Frama-C** e o **ESC/Java** fazem, despachando a fórmula para um provador SMT como o **Z3**.

---

### Referências para ir além

- **Hoare, *An Axiomatic Basis for Computer Programming* (CACM, 1969)** — o artigo fundador. Doze páginas, e a notação $\{P\}S\{Q\}$ nasce nele.
- **Bloch, *Extra, Extra — Read All About It: Nearly All Binary Searches and Mergesorts Are Broken* (2006)** — o relato do bug do `(low+high)/2`, direto de quem o encontrou no JDK.
- **Nancy Leveson & Clark Turner, *An Investigation of the Therac-25 Accidents* (IEEE Computer, 1993)** — a análise definitiva do caso; leitura obrigatória sobre software crítico.
- **Relatório da comissão Lions sobre o voo 501 do Ariane 5 (ESA, 1996)** — curto, público, e descreve a cadeia de falhas linha a linha.
- **Bertrand Meyer, *Object-Oriented Software Construction*, 2ª ed.** — Cap. 11, o texto canônico de Design by Contract, incluindo as regras de herança.
- **Dijkstra, *A Discipline of Programming* (1976)** — a fonte de $\mathrm{wp}$ e da ideia de derivar o programa a partir da especificação em vez de verificá-lo depois.
- **Rustan Leino, *Program Proofs* (MIT Press, 2023) / tutorial do Dafny** — a versão executável de tudo isso: escreve-se `requires`/`ensures`/`invariant` e a ferramenta prova ou aponta o contraexemplo.

---

## Aula 05 — Regras de Inferência, e Por Que a Cláusula de Fecho Não é Decorativa

### A notação, escrita direito

As notas pedem desculpa pela notação — "*o uso de $e$ é para representar o símbolo de pertence; vai ficar feio*" — e o pedido é justo, então vale registrar a forma padrão. Uma **regra de inferência** se escreve com as premissas acima da barra e a conclusão abaixo:

$$\frac{P_1 \quad P_2 \quad \cdots \quad P_n}{C}\;\text{(nome)}$$

Lê-se: "se $P_1, \dots, P_n$ valem, então $C$ vale". Um **axioma** é o caso $n = 0$ — uma regra sem premissas, cuja barra fica com o topo vazio:

$$\frac{\ }{\ 0 \in S\ }\;\text{(base)}$$

Essa notação é de **Gentzen** (1934), e o fato de axioma e regra terem a mesma forma não é economia de símbolos: é o ponto. Um sistema formal é apenas um conjunto de regras, e as que não têm premissa são os pontos de partida. É por isso que as notas puderam escrever o axioma como "$/\,b$" — a barra com nada em cima.

Reescrevendo os exercícios registrados nas notas na forma padrão. Para o conjunto $S_3$ da atividade **(e)**, cujas palavras válidas incluem `aba`, `aabaa`, `abba`, `aabbaa`:

$$\frac{\ }{\ \texttt{aba} \in S_3\ } \qquad\qquad \frac{w \in S_3}{\texttt{a}w\texttt{a} \in S_3}$$

E para a atividade **(h)**, o conjunto dos ímpares gerados a partir do zero:

$$\frac{\ }{\ 0 \in S\ } \qquad\qquad \frac{n \in S}{2n + 1 \in S}$$

Note que esse segundo conjunto **não** é o dos ímpares: partindo de $0$ obtém-se $1, 3, 7, 15, 31, \dots$ — os números da forma $2^k - 1$. A regra $2n+1$ aplicada repetidamente a partir de $0$ dobra e soma um, o que gera os *repunits* binários, não todos os ímpares. Conferir o conjunto gerado contra o conjunto pretendido enumerando os primeiros elementos é o hábito que evita o erro mais comum desse tipo de exercício.

Para de fato gerar os ímpares, a regra precisa ser $\frac{n \in S}{n + 2 \in S}$ com base $1 \in S$.

---

### A cláusula de fecho: o que ela realmente impede

As notas listam os três passos — base, indução, fecho — e definem o terceiro como "*declarar que $i$ consiste exatamente dos elementos produzidos pelos passos da base e da indução*". Essa é a definição correta, e ela costuma parecer burocrática. Não é: **sem ela, o conjunto não está definido**.

Considere a definição de $\mathbb{N}$ só com os dois primeiros passos:

- Base: $0 \in N$.
- Indução: se $n \in N$, então $n + 1 \in N$.

Pergunta: $-5$ pertence a $N$? As duas regras não dizem nada sobre isso. Elas dizem o que **está** em $N$, nunca o que **não está**. E o conjunto dos inteiros $\mathbb{Z}$ satisfaz as duas regras perfeitamente: contém o $0$, e é fechado sob sucessor. O conjunto dos racionais também. O conjunto dos reais também.

As duas primeiras cláusulas não determinam um conjunto — determinam uma **família** de conjuntos, todos os que as satisfazem. A cláusula de fecho escolhe um deles: o **menor**, aquele contido em todos os outros.

Formalmente, se $\mathcal{F}$ é a família de todos os conjuntos que satisfazem base e indução,

$$N = \bigcap_{X \in \mathcal{F}} X$$

e esse é o **menor ponto fixo** do operador definido pelas regras. É o mesmo conceito que aparece com outro nome em várias partes da computação: a semântica de programas recursivos, a análise de fluxo de dados em compiladores e o cálculo de FIRST/FOLLOW em gramáticas são todos menores pontos fixos.

**A consequência direta, e o motivo de a cláusula importar para o resto da disciplina:** é o fecho que autoriza a prova por **indução estrutural**. O raciocínio:

> Seja $P$ uma propriedade. Se $P$ vale para os elementos da base, e se $P$ se preserva por cada regra de inferência, então o conjunto $\{x : P(x)\}$ satisfaz base e indução. Logo ele pertence a $\mathcal{F}$. Como $N$ é o **menor** elemento de $\mathcal{F}$, tem-se $N \subseteq \{x : P(x)\}$ — ou seja, $P$ vale para **todo** elemento de $N$.

Sem "menor", esse último passo não existe: poderia haver elementos em $N$ que não foram produzidos por regra nenhuma, e sobre os quais o argumento indutivo nada diz. A cláusula de fecho é literalmente o que transforma a definição num **princípio de prova** — e esse princípio é a ferramenta central de todo o resto do semestre, em listas (Aula 08), árvores e em Isabelle (Aulas 11 e 13).

Uma forma curta de guardar: **base e indução dizem o que existe; o fecho diz que nada mais existe — e é a segunda metade que permite provar coisas.**

---

### O princípio de indução que cada definição gera

Vale explicitar a mecânica, porque ela é sempre a mesma e resolve metade dos exercícios de cara: **uma regra de inferência na definição vira um caso na prova**.

Para o conjunto $S_3$ acima, com um axioma e uma regra, o princípio é:

$$\frac{P(\texttt{aba}) \qquad \forall w \in S_3\ \big(P(w) \Rightarrow P(\texttt{a}w\texttt{a})\big)}{\forall w \in S_3\ P(w)}$$

Um caso base por axioma, um caso indutivo por regra. Se a definição tem três regras, a prova tem três casos indutivos — não há escolha nem criatividade nessa parte.

Aplicando: prove que toda palavra de $S_3$ tem comprimento **ímpar**.

- **Base.** $|\texttt{aba}| = 3$, ímpar. ✓
- **Indução.** Suponha $|w|$ ímpar. Então $|\texttt{a}w\texttt{a}| = |w| + 2$, e ímpar mais dois é ímpar. ✓
- Pelo princípio acima, toda palavra de $S_3$ tem comprimento ímpar. $\blacksquare$

O padrão é sempre esse. A parte difícil de uma prova por indução estrutural quase nunca é a estrutura — é **escolher a propriedade $P$ certa**, e às vezes fortalecê-la para que a hipótese indutiva sirva. Esse é exatamente o problema que aparece na Aula 13 com a comutatividade da soma.

---

## Aula 08 — Listas como Tipo Indutivo, e o Salto para Árvores

### `List<T>` é o mesmo esquema, com dois construtores

As notas trazem as duas regras corretamente. Escritas na notação padrão:

$$\frac{\ }{\ [\,] \in \mathsf{List}\langle T\rangle\ }\;\text{(nil)} \qquad\qquad \frac{E \in T \qquad L \in \mathsf{List}\langle T\rangle}{E : L \in \mathsf{List}\langle T\rangle}\;\text{(cons)}$$

E as notas também acertam a leitura da notação de ordem: `0 : 1 : 2 : []` é $[0,1,2]$ porque `:` associa à **direita**, ou seja, `0 : (1 : (2 : []))`. A dúvida registrada ("*a partir da lista vazia, colocaram 2, 1 e 0 — nessa ordem, eu acredito*") está certa: a **construção** acontece de trás para frente, do `[]` para fora, mas a **leitura** é da frente para trás. Vale fixar, porque essa inversão é a origem de metade dos erros em provas sobre listas.

A observação estrutural que amarra com a Aula 05: `nil` é o axioma, `cons` é a regra de inferência. É literalmente o mesmo esquema de $\mathbb{N}$ com `0`/`Suc`, só que `cons` carrega um dado extra ($E$) junto. Uma lista **é** um natural com carga: se apagar todos os elementos de `0 : 1 : 2 : []`, sobra `Suc(Suc(Suc(0)))`, que é $3$ — o comprimento.

Daí sai o princípio de indução, mecanicamente, um caso por construtor:

$$\frac{P([\,]) \qquad \forall e \in T,\ \forall l \in \mathsf{List}\langle T\rangle\ \big(P(l) \Rightarrow P(e : l)\big)}{\forall l \in \mathsf{List}\langle T\rangle\ P(l)}$$

---

### Funções recursivas sobre listas, e uma prova completa

A definição de uma função sobre um tipo indutivo segue a mesma forma: **uma equação por construtor**. É por isso que essas definições nunca precisam de prova de terminação — cada chamada recursiva recebe um argumento estruturalmente menor, e a estrutura é finita por construção (de novo, graças à cláusula de fecho).

$$\begin{aligned} \mathrm{comp}([\,]) &= 0 \\ \mathrm{comp}(e : l) &= 1 + \mathrm{comp}(l) \end{aligned} \qquad\qquad \begin{aligned} \mathrm{conc}([\,],\, ys) &= ys \\ \mathrm{conc}(e : l,\, ys) &= e : \mathrm{conc}(l,\, ys) \end{aligned}$$

A concatenação $\mathrm{conc}$ é a `@` do Isabelle e a `++` do Haskell, e é a função que o enunciado do trabalho mencionado na Aula 13 usa como base.

**Teorema.** $\mathrm{comp}(\mathrm{conc}(xs, ys)) = \mathrm{comp}(xs) + \mathrm{comp}(ys)$.

*Prova, por indução estrutural em $xs$.*

**Caso base** ($xs = [\,]$):
$$\mathrm{comp}(\mathrm{conc}([\,], ys)) = \mathrm{comp}(ys) = 0 + \mathrm{comp}(ys) = \mathrm{comp}([\,]) + \mathrm{comp}(ys)\ \checkmark$$

**Caso indutivo** ($xs = e : l$), com hipótese $\mathrm{comp}(\mathrm{conc}(l, ys)) = \mathrm{comp}(l) + \mathrm{comp}(ys)$:
$$\begin{aligned} \mathrm{comp}(\mathrm{conc}(e:l,\, ys)) &= \mathrm{comp}(e : \mathrm{conc}(l, ys)) && \text{(def. de conc)} \\ &= 1 + \mathrm{comp}(\mathrm{conc}(l, ys)) && \text{(def. de comp)} \\ &= 1 + \mathrm{comp}(l) + \mathrm{comp}(ys) && \textbf{(hipótese indutiva)} \\ &= \mathrm{comp}(e : l) + \mathrm{comp}(ys) && \text{(def. de comp, ao contrário)} \end{aligned}$$
$\blacksquare$

Duas coisas para reter desse esqueleto, porque elas se repetem em todas as provas do semestre:

1. **A indução é feita no argumento sobre o qual a função recorre.** $\mathrm{conc}$ recorre no primeiro argumento, então a indução é em $xs$. Tentar induzir em $ys$ trava no caso base, porque nenhuma equação de $\mathrm{conc}$ decompõe $ys$. Essa regra reaparece como o ponto central da Aula 13.
2. **Cada passo é justificado por uma equação da definição ou pela hipótese.** Nada de "é óbvio". Isabelle vai cobrar exatamente isso, com o nome de cada equação (`soma01`, `soma02`) na justificativa.

---

### Árvores: a generalização anunciada

As notas registram que o tópico do dia era "definições indutivas e recursivas sobre **árvores**". O esquema é o mesmo, com um construtor que tem **duas** sublistas em vez de uma:

$$\frac{\ }{\ \mathsf{Folha} \in \mathsf{Arv}\langle T\rangle\ } \qquad\qquad \frac{e \in T \qquad l \in \mathsf{Arv}\langle T\rangle \qquad r \in \mathsf{Arv}\langle T\rangle}{\mathsf{No}(l,\, e,\, r) \in \mathsf{Arv}\langle T\rangle}$$

O princípio de indução ganha **duas** hipóteses no caso do nó — uma para cada subárvore:

$$\frac{P(\mathsf{Folha}) \qquad \forall l, e, r\ \big(P(l) \wedge P(r) \Rightarrow P(\mathsf{No}(l,e,r))\big)}{\forall t \in \mathsf{Arv}\langle T\rangle\ P(t)}$$

Esse é o momento em que a indução estrutural deixa de ser "indução matemática disfarçada": não há mais um "anterior" único, há dois, e nenhuma ordem linear natural entre eles. A propriedade não está sendo provada sobre $n$ e $n-1$, e sim sobre uma estrutura e suas partes.

O exemplo canônico, e um bom exercício para conferir se o esquema foi entendido:

$$\begin{aligned} \mathrm{folhas}(\mathsf{Folha}) &= 1 \\ \mathrm{folhas}(\mathsf{No}(l,e,r)) &= \mathrm{folhas}(l) + \mathrm{folhas}(r) \end{aligned} \qquad \begin{aligned} \mathrm{nos}(\mathsf{Folha}) &= 0 \\ \mathrm{nos}(\mathsf{No}(l,e,r)) &= 1 + \mathrm{nos}(l) + \mathrm{nos}(r) \end{aligned}$$

**Teorema.** $\mathrm{folhas}(t) = \mathrm{nos}(t) + 1$ para toda árvore $t$.

O caso base é $1 = 0 + 1$. O caso indutivo, com hipóteses $\mathrm{folhas}(l) = \mathrm{nos}(l)+1$ e $\mathrm{folhas}(r) = \mathrm{nos}(r)+1$:

$$\mathrm{folhas}(\mathsf{No}(l,e,r)) = \mathrm{folhas}(l) + \mathrm{folhas}(r) = \big(\mathrm{nos}(l)+1\big) + \big(\mathrm{nos}(r)+1\big) = \mathrm{nos}(\mathsf{No}(l,e,r)) + 1$$

$\blacksquare$ — e note que as **duas** hipóteses foram usadas, o que é a assinatura de uma indução sobre árvore feita corretamente. Uma prova que usa só uma delas quase certamente está errada.

**Sobre o comentário de organização das notas** ("*os md's não escritos podem ser substituídos pelas folhas de atividades*"): para métodos formais isso funciona melhor do que na média das disciplinas, justamente porque o conteúdo é cumulativo e mecânico. Cada tipo indutivo novo traz o mesmo pacote — construtores, princípio de indução, funções por equação, provas por casos. Ter o esquema acima em mãos permite reconstruir uma aula perdida a partir apenas da lista de exercícios dela.

---

## Aula 11 — Isabelle: a Sintaxe Correta, Currying, e `primrec` × `fun`

### O arquivo que compila

As notas foram tomadas ao vivo e os trechos de código têm erros de transcrição que impedem o Isabelle de carregar a teoria. Como o trabalho da Aula 13 depende disso funcionar, vale a versão corrigida, com as diferenças marcadas.

```isabelle
theory Exemplos              (* nome deve casar com o arquivo: Exemplos.thy *)
  imports Main               (* Main, com M maiúsculo — não "main" *)
begin

(* nat já existe em Main; esta é a definição que o Isabelle usa: *)
(* datatype nat = 0 | Suc nat *)

definition quadrado :: "nat ⇒ nat" where   (* ⇒ (\<Rightarrow>), não -> *)
  "quadrado n = n * n"

primrec somar :: "nat ⇒ nat ⇒ nat" where   (* tipo COMPLETO: dois args, um resultado *)
  somar1: "somar x 0       = x" |
  somar2: "somar x (Suc y) = Suc (somar x y)"

fun par :: "nat ⇒ bool" where              (* fun, não primrec — ver adiante *)
  "par 0             = True"  |
  "par (Suc 0)       = False" |
  "par (Suc (Suc n)) = par n"

value "True ∧ False"        (* ∧ é conjunção; ^ é potência *)
value "quadrado 5"          (* devolve 25 *)

end                          (* end fecha a teoria; done fecha uma PROVA *)
```

As correções, uma a uma:

| Nas notas | Correto | Por quê |
|---|---|---|
| `imports main` | `imports Main` | nomes de teoria são sensíveis a maiúsculas |
| `nat->nat` | `nat ⇒ nat` (ou `nat => nat`) | `⇒` é o tipo função; `⟶` é implicação **entre proposições** |
| `nat -> nat ->` | `nat ⇒ nat ⇒ nat` | a assinatura precisa do tipo do resultado |
| `True ^ False` | `True ∧ False` | `^` é exponenciação |
| `datatype bool = True \| Flase` | `False` | — |
| `"part 0 = True"` | `"par 0 = True"` | o nome tem de casar com a assinatura |
| `done` no fim do arquivo | `end` | `done` encerra uma prova por método, não a teoria |

A confusão entre `⇒` e `⟶` é a que mais custa tempo, e a distinção vale ser guardada: `⇒` constrói **tipos** (`nat ⇒ bool` é o tipo dos predicados sobre naturais); `⟶` constrói **fórmulas** (`P ⟶ Q` é uma proposição). Escrever `nat ⟶ nat` produz um erro de tipo que o Isabelle reporta de forma pouco óbvia.

---

### O título que as notas nunca explicam: currying

A seção das notas se chama "*Thou Shall Curry Your Functions*" e o conceito não aparece. Ele está escondido na assinatura `nat ⇒ nat ⇒ nat`.

Essa assinatura parece dizer "função de dois naturais". Não é o que ela diz. A seta `⇒` associa à **direita**, então o que está escrito é

$$\texttt{nat} \Rightarrow (\texttt{nat} \Rightarrow \texttt{nat})$$

— uma função que recebe **um** natural e devolve **outra função**, que por sua vez recebe um natural e devolve um natural. Toda função em Isabelle/HOL tem exatamente um argumento. Isso é **currying**, nome em homenagem a Haskell Curry.

A aplicação acompanha: `somar 3 5` é `(somar 3) 5` — primeiro aplica-se `somar` a `3`, obtendo uma função, e depois essa função a `5`. É por isso que argumentos são separados por espaço e não por vírgulas entre parênteses.

O que se ganha com isso, e por que não é só notação:

1. **Aplicação parcial.** `somar 3` é um valor legítimo, de tipo `nat ⇒ nat` — a função "somar três". Pode ser nomeada, passada adiante, usada em `map`.
2. **Tudo é de primeira classe, sem caso especial.** Não é preciso distinguir "função de 1 argumento" de "função de 2"; a teoria de tipos tem uma regra só.
3. **Provas mais simples.** Regras sobre funções de um argumento cobrem todos os casos automaticamente.

O preço é o parênteses obrigatório em argumentos compostos: `somar x (Suc y)` está certo, e `somar x Suc y` é lido como `somar x Suc` aplicado a `y` — três argumentos, com `Suc` no lugar errado. É o erro de sintaxe mais frequente de quem está começando, e a mensagem de erro (uma incompatibilidade de tipos) não aponta para a causa real.

---

### `primrec` × `fun`: por que existem dois

As notas registram que "*o Isabelle permite a implementação de funções recursivas*" sem explicar por que há duas palavras-chave, e a escolha entre elas é justamente o que explica por que `par` não pôde ser escrita como `primrec`.

| | `primrec` | `fun` |
|---|---|---|
| Recursão permitida | **primitiva**: exatamente um construtor de profundidade, num argumento fixo | qualquer, desde que termine |
| Terminação | garantida por construção, **sem prova** | Isabelle tenta provar automaticamente |
| Equações exigidas | **uma por construtor**, nem mais nem menos | qualquer conjunto, com sobreposição resolvida por ordem |
| Regra de indução gerada | a do datatype | uma **sob medida**, seguindo a recursão da função |
| Falha quando | o padrão é mais fundo que um construtor | não consegue provar terminação |

`somar` é primitiva recursiva: seus padrões são `0` e `Suc y`, exatamente os dois construtores de `nat`, e a chamada recursiva é sobre `y` — um construtor abaixo. `primrec` aceita.

`par` **não** é: o padrão `Suc (Suc n)` tem profundidade **dois**, e a recursão pula de dois em dois. Isso é recursão bem-fundada, mas não primitiva. `primrec` rejeita; `fun` aceita, prova a terminação automaticamente (o argumento decresce na ordem usual de `nat`) e ainda gera uma regra de indução customizada — `par.induct`, com **três** casos, `0`, `Suc 0` e `Suc (Suc n)` — que é exatamente o que se precisa para provar coisas sobre `par`.

A regra prática: **use `primrec` quando couber, `fun` quando não couber.** `primrec` dá garantias mais fortes de graça e equações que casam melhor com o simplificador. Quando nem `fun` consegue provar a terminação, existe ainda `function`, que aceita a definição e deixa a obrigação de prova para você.

**Sobre nomear as equações.** O `somar1:` e `somar2:` das notas não são decoração: eles dão nome a cada equação para que uma prova possa citá-la, como em `by (simp only: somar1)`. Sem nome explícito, as equações ficam acessíveis em bloco como `somar.simps`, e o controle fino sobre qual passo de reescrita aplicar se perde. Em provas longas, esse controle é a diferença entre um passo que funciona e um `simp` que diverge.

---

### Por que `nat` é unário

As notas registram a definição — "*todo natural é sucessor de algum outro natural acima de 0*" — sem comentar o que parece um absurdo de engenharia: representar $1000$ como mil aplicações de `Suc`.

A razão é que `nat` não é um tipo para **computar**, é um tipo para **provar**. A definição unária é a formalização direta dos **axiomas de Peano**, e o que ela entrega é exatamente o princípio de indução da Aula 05 — dois construtores, dois casos na prova. Uma representação binária teria eficiência computacional e um princípio de indução horrível de usar.

Duas coisas tornam isso viável na prática:

- **Literais são notação.** Escrever `5` no Isabelle não constrói `Suc(Suc(Suc(Suc(Suc 0))))` na memória; o sistema usa uma representação numérica interna e as regras de simplificação para aritmética (`arith`, `simp`) operam sobre ela. A forma unária só aparece quando se faz *pattern matching* explícito em `Suc n`.
- **Geração de código.** Ao exportar para ML, Haskell ou Scala, o Isabelle substitui `nat` por inteiros de máquina com uma prova de que a substituição preserva a semântica. Prova-se sobre unário; executa-se sobre binário.

É o mesmo padrão que rege toda a ferramenta: escolher a representação que torna as **provas** fáceis, e recuperar a eficiência depois, com uma tradução justificada. O aviso registrado na Aula 13 — "*cuidado pois o Isabelle assume que `x+1` implica no uso de `Suc`*" — é esse mecanismo aparecendo: `x + 1` e `Suc x` são o mesmo valor, e o simplificador converte entre as formas conforme a regra que estiver tentando aplicar.

---

## Aula 13 — A Prova de `soma`, Corrigida, e a Armadilha da Comutatividade

### Por que a indução é em `b`, e não em `a`

As notas registram a escolha do Júlio — "*fazendo a indução na variável $b$, o segundo argumento da definição indutiva*" — como se fosse preferência. Não é: é **forçado**, e reconhecer isso resolve a maioria dos exercícios de prova do semestre.

A definição é

$$\mathrm{soma}(x, 0) = x \qquad\qquad \mathrm{soma}(x,\, \mathrm{Suc}\,y) = \mathrm{Suc}(\mathrm{soma}(x, y))$$

Olhe onde o *pattern matching* acontece: no **segundo** argumento. A primeira equação exige que o segundo argumento seja `0`; a segunda exige que seja `Suc y`. O primeiro argumento, `x`, atravessa as duas sem ser inspecionado.

Consequência: uma prova por indução em `b` tem, em cada caso, uma equação da definição pronta para aplicar. O caso base bate com `soma x 0 = x`; o caso indutivo bate com `soma x (Suc y) = Suc (soma x y)`. A prova anda.

Uma prova por indução em `a` trava imediatamente. No caso base seria preciso avaliar `soma 0 b` com `b` desconhecido — e **nenhuma** equação se aplica, porque nenhuma delas decompõe o primeiro argumento. Não há como dar o primeiro passo.

**A regra geral:** *induza sobre o argumento em que a função recorre*. Quando há várias funções envolvidas, induza sobre o argumento em que a função mais externa recorre. Quando as funções recorrem em argumentos diferentes, provavelmente vão ser necessários lemas auxiliares — que é exatamente o assunto da última seção.

---

### A prova em Isar, corrigida e comentada

As notas trazem o esqueleto da prova com alguns problemas de transcrição: `paratodoA::nat . ...` não é sintaxe de quantificador, o `fix y` aparece antes do `next`, e falta o `qed` final. A versão que compila:

```isabelle
theorem t2: "∀a::nat. soma a b = a + b"
proof (induction b)

  (* ---------- CASO BASE: b = 0 ---------- *)
  show "∀a::nat. soma a 0 = a + 0"
  proof (rule allI)                  (* allI: para provar ∀x. P x, fixe um x arbitrário *)
    fix x :: nat
    have "soma x 0 = x"       by (simp only: somar1)   (* pela 1ª equação *)
    also have "... = x + 0"   by arith                  (* aritmética trivial *)
    finally show "soma x 0 = x + 0" .                   (* encadeia as igualdades *)
  qed

next
  (* ---------- CASO INDUTIVO: b = Suc y ---------- *)
  fix y :: nat
  assume HI: "∀a::nat. soma a y = a + y"               (* hipótese indutiva *)
  show "∀a::nat. soma a (Suc y) = a + (Suc y)"
  proof (rule allI)
    fix x :: nat
    have "soma x (Suc y) = Suc (soma x y)"  by (simp only: somar2)
    also have "... = Suc (x + y)"           by (simp only: HI)
    also have "... = x + Suc y"             by arith
    finally show "soma x (Suc y) = x + Suc y" .
  qed
qed
```

O vocabulário Isar que esse esqueleto usa, e que se repete em toda prova da disciplina:

| Palavra | Papel |
|---|---|
| `proof (induction b)` | abre a prova e gera um subobjetivo por construtor de `b` |
| `fix x :: nat` | introduz um elemento **arbitrário mas fixo** — o "seja $X$ arbitrário" das notas |
| `assume HI: "..."` | introduz a hipótese e lhe dá nome, para citar depois |
| `have "..." by ...` | estabelece um passo intermediário |
| `also` / `finally` | encadeia igualdades transitivamente; `...` refere-se ao lado direito anterior |
| `next` | separa um subobjetivo do próximo |
| `show` | prova o objetivo corrente |
| `qed` | fecha o bloco |

E os três métodos que aparecem: `simp only: <regra>` reescreve usando **apenas** aquela regra (controle máximo, ideal para mostrar cada passo); `arith` resolve aritmética linear sobre naturais e inteiros; `rule allI` aplica a regra de introdução do quantificador universal.

O "**No subgoals!**" que as notas celebram é literalmente o estado do provador dizendo que a pilha de objetivos esvaziou. Enquanto houver subobjetivo aberto, o `qed` falha.

---

### A armadilha: o teorema 3 não sai com uma indução só

As notas listam quatro teoremas a provar, e o terceiro — $\mathrm{soma}(a,b) = \mathrm{soma}(b,a)$ — é de outra categoria. Vale o aviso, porque ele é a primeira parede real do semestre.

Tentar indução em `b` direto **não funciona**. No caso base seria preciso mostrar $\mathrm{soma}(a, 0) = \mathrm{soma}(0, a)$: o lado esquerdo simplifica para `a` pela primeira equação, mas o lado direito, $\mathrm{soma}(0, a)$, tem `a` na posição que não é inspecionada — nenhuma equação se aplica. Trava exatamente como a indução em `a` travava antes.

A saída são **dois lemas auxiliares**, cada um provado por sua própria indução:

```isabelle
lemma soma_zero_esq: "soma 0 b = b"
  by (induction b) simp_all

lemma soma_suc_esq: "soma (Suc a) b = Suc (soma a b)"
  by (induction b) simp_all

theorem soma_comutativa: "soma a b = soma b a"
  by (induction a) (simp_all add: soma_zero_esq soma_suc_esq)
```

O padrão é geral e vale guardar: a definição só sabe decompor **um** dos argumentos, então cada fato que precisa decompor o **outro** vira um lema. `soma_zero_esq` e `soma_suc_esq` são exatamente as duas equações que `soma` teria se fosse definida recorrendo no primeiro argumento — provadas, em vez de dadas.

Isso generaliza para praticamente tudo que a disciplina vai pedir:

- **Associatividade** de `soma` — indução em um argumento, direta.
- **Comutatividade** — precisa dos dois lemas acima.
- $\mathrm{comp}(\mathrm{conc}(xs,ys)) = \mathrm{comp}(xs)+\mathrm{comp}(ys)$ — direta, porque `conc` recorre em `xs` e a indução é em `xs`.
- $\mathrm{rev}(\mathrm{conc}(xs,ys)) = \mathrm{conc}(\mathrm{rev}\,ys, \mathrm{rev}\,xs)$ — **precisa** do lema $\mathrm{conc}(xs, [\,]) = xs$, pelo mesmo motivo: a lista vazia à direita é o caso que a definição não inspeciona.
- $\mathrm{rev}(\mathrm{rev}\,xs) = xs$ — precisa do anterior. É o exercício clássico de abertura do tutorial de Isabelle, e a razão de ele ser clássico é justamente essa cadeia de lemas.

**Quando `simp` falha, quase sempre é isto:** falta um lema sobre o argumento que a definição não decompõe. O reflexo certo não é procurar outro método de prova — é perguntar "qual fato sobre o outro argumento eu estou assumindo sem ter provado?".

Sobre o tom das notas ao fechar a aula — "*medo por nada*" — é uma leitura justa das provas do teorema 2, e otimista demais para o teorema 3. A sintaxe do Isabelle é de fato mecânica depois que a prova está feita à mão, como o Júlio disse. O que não é mecânico é **descobrir de quais lemas se precisa**, e essa parte não fica mais fácil por conhecer a ferramenta.

---
