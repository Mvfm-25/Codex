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
