# Construção de Compiladores — Adições & Aprofundamentos
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas. Segue os tópicos na ordem em que apareceram nas notas, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---

## Aula 01 — As Fases do Compilador e o Formalismo de Cada Uma

### Cada Fase Tem uma Máquina Formal Por Trás — e Não é a Mesma

As notas listam as quatro rotinas (léxica, sintática, semântica, geração/otimização) e mencionam que a análise léxica "é determinada por um **Autômato Finito**" com tempo $O(n)$. O que fica implícito é que **cada fase corresponde a um nível diferente da hierarquia de linguagens**, e é exatamente por isso que elas são fases separadas em vez de um passo só:

| Fase | Formalismo gerador | Reconhecedor | Complexidade |
|---|---|---|---|
| **Análise léxica** | Expressão regular / Gramática regular (tipo 3) | **Autômato finito** (AFD) | $O(n)$ |
| **Análise sintática** | Gramática livre de contexto (tipo 2) | **Autômato de pilha** | $O(n)$ para LL/LR; $O(n^3)$ no caso geral (CYK, Earley) |
| **Análise semântica** | — (nenhuma gramática captura) | Tabela de símbolos + travessia da árvore | $O(n)$ típico |
| **Geração de código** | — | Casamento de padrões na árvore | depende das otimizações |

**Por que a léxica é $O(n)$ de verdade.** Um AFD tem uma única transição possível por símbolo lido: nenhuma escolha, nenhum retrocesso, nenhuma memória além do estado atual. Cada caractere da entrada é consumido exatamente uma vez, com custo constante — daí o $O(n)$ exato, não amortizado.

**E por que a sintática precisa de mais.** Uma linguagem regular não consegue contar parênteses balanceados: o número de estados de um AFD é finito, e verificar `((((...))))` com aninhamento arbitrário exigiria estados infinitos. Formalmente é o **lema do bombeamento** que prova isso. É por isso que a fase seguinte usa **pilha** — e é por isso que a estrutura de blocos, chamadas aninhadas e expressões parentetizadas não podem ser tratadas com regex, por mais que a tentação exista.

### "Os menino bebeu o bolo" — o Exemplo Que Justifica a Fase Semântica

A frase da aula não é só uma piada: ela é a demonstração mais limpa de **por que semântica é uma fase separada da sintática**.

Sintaticamente, a frase está perfeita — a árvore que o Agustini montou (sintagma nominal + sintagma verbal) fecha sem erro. O que está errado é de outra natureza: **concordância** (`Os` no plural com `menino` no singular) e **compatibilidade de tipos** (`bolo` não é algo que se bebe). Nenhuma gramática livre de contexto captura isso de forma prática — concordância exige comparar dois pontos *distantes* da árvore, e uma GLC não tem como carregar essa informação de um ramo para outro.

O paralelo direto em compiladores:

```c
int x = "hello";     // sintaticamente impecável, semanticamente inválido
undeclared_var + 1;  // idem — a gramática não sabe o que foi declarado
foo(1, 2, 3);        // idem — a gramática não sabe a aridade de foo
```

Os três passam pelo parser sem uma reclamação e morrem na análise semântica, contra a **tabela de símbolos**. É a mesma distinção da frase do bolo. O exemplo canônico dessa separação na linguística é a frase de Chomsky, *"Colorless green ideas sleep furiously"* — gramaticalmente perfeita, semanticamente vazia, e cunhada justamente para argumentar que sintaxe é independente de significado.

### Por Que Gerar x86 "Sem Utilidade Prática" Ainda Vale a Pena

A observação das notas está certa quanto ao mercado e errada quanto ao motivo de existir. Compiladores completos são raros como emprego; **as técnicas são onipresentes**:

- **Validação de entrada** — o exemplo das URLs. Todo parser de JSON, YAML, CSV, protocolo de rede ou formato binário é análise léxica + sintática com outro nome.
- **DSLs e linguagens de configuração** — regras de negócio, queries, templates. Escrever uma gramática pequena e um parser é rotina.
- **Ferramentas de código** — linters, formatadores, *language servers*, migradores automáticos e refatoração de IDE operam sobre a árvore sintática abstrata (**AST**).
- **Transpiladores e front-ends** — TypeScript→JavaScript, Sass→CSS, ORMs que geram SQL.

E gerar x86 de verdade ensina o que nenhum nível acima ensina: convenção de chamada, *stack frame*, alocação de registradores e o que o hardware realmente faz com um `for`. É o elo entre a Organização de Computadores e a linguagem de alto nível.

---

## Aula 02 — Hierarquia de Chomsky, Derivação e Ambiguidade

### O Fecho de Kleene — o "Clinistar" das Notas

O símbolo é o **fecho de Kleene** (*Kleene star*), de **Stephen Kleene**, e a definição é mais precisa do que "representa o vazio":

Dado um alfabeto $A$, o fecho $A^*$ é o conjunto de **todas** as sentenças que podem ser formadas concatenando zero ou mais símbolos de $A$:

$$A^* = \bigcup_{i=0}^{\infty} A^i = A^0 \cup A^1 \cup A^2 \cup \cdots$$

O caso $A^0 = \{\varepsilon\}$ é onde entra o vazio: $\varepsilon$ é a **sentença vazia**, o elemento neutro da concatenação ($\varepsilon w = w \varepsilon = w$). Existe também o **fecho positivo** $A^+ = A^* \setminus \{\varepsilon\}$ — um ou mais símbolos.

Isso torna precisa a definição de linguagem que a aula deu: uma **linguagem sobre $A$ é qualquer subconjunto de $A^*$**. Note a consequência — como $A^*$ é infinito para qualquer $A$ não-vazio, o número de linguagens possíveis é incontável, enquanto o número de gramáticas (objetos finitos) é contável. Logo **existem linguagens que nenhuma gramática descreve**. É um resultado de cardinalidade, e vem antes de qualquer discussão sobre computabilidade.

### A Hierarquia de Chomsky: as Diferenças Que as Notas Não Detalharam

A aula estabeleceu o aninhamento correto e disse que as diferenças "aparecem na formatação das produções". Aqui está a formatação:

| Tipo | Nome | Forma das produções | Reconhecedor | Decidibilidade |
|---|---|---|---|---|
| **0** | Irrestrita | $\alpha \to \beta$, $\alpha$ contendo ao menos um não-terminal | Máquina de Turing | **Indecidível** (recursivamente enumerável) |
| **1** | Sensível ao contexto | $\alpha A \beta \to \alpha \gamma \beta$ — nunca encurta ($\lvert\text{esq}\rvert \le \lvert\text{dir}\rvert$) | Autômato linearmente limitado | Decidível, mas **PSPACE-completo** |
| **2** | **Livre de contexto** | $A \to \gamma$ — **um único não-terminal** à esquerda | Autômato de pilha | $O(n^3)$; $O(n)$ nas subclasses LL/LR |
| **3** | **Regular** | $A \to aB$ ou $A \to a$ | Autômato finito | $O(n)$ |

O nome **"livre de contexto"** fica óbvio olhando a tabela: $A \to \gamma$ pode ser aplicada **onde quer que $A$ apareça**, sem olhar o que está em volta. No tipo 1, a produção só vale se $A$ estiver cercado por $\alpha$ e $\beta$ — o *contexto*.

E isso responde o "não tem nada de importante nelas, obrigado problema da parada": para o **tipo 0**, decidir se $w \in L(G)$ é equivalente ao problema da parada — indecidível, então nenhum compilador pode ser construído. O **tipo 1** é decidível, mas o custo é exponencial em tempo na prática. Linguagens de programação vivem no tipo 2 porque é o ponto exato onde o poder expressivo ainda cobre estruturas aninhadas **e** o reconhecimento continua linear.

Um ajuste histórico: a hierarquia é de **Noam Chomsky** (1956), no artigo *Three Models for the Description of Language*. **Marvin Minsky** é figura central de autômatos e IA (*Computation: Finite and Infinite Machines*, 1967), mas a hierarquia não é dele.

### Ambiguidade: os Dois Lados da Mesma Aula

A aula deu a definição que cai na P1 — gramática ambígua é a que admite **mais de uma árvore de derivação** para a mesma sentença — e, sem anunciar, mostrou o exemplo e a cura na mesma aula.

**O exemplo** é a gramática da questão 7:

```
E → E + E | E * E | 1 | 2 | 3 | (E)
```

Para `1 + 2 * 3` existem duas árvores:

```
    +              *
   / \            / \
  1   *          +   3
     / \        / \
    2   3      1   2

  = 1+(2*3) = 7   = (1+2)*3 = 9
```

Duas árvores, dois valores. Um compilador teria que escolher arbitrariamente qual programa compilar — inaceitável.

**A cura** é a gramática da questão 4, que apareceu antes na mesma lista:

```
E → E + T | T
T → T * F | F
F → ( E ) | 1 | 2 | 3
```

Os três níveis $E$/$T$/$F$ (Expressão, Termo, Fator) não são decoração: eles **codificam a precedência na própria estrutura**. Como `*` só é alcançável descendo até $T$, a multiplicação fica obrigatoriamente mais funda na árvore, e árvore mais funda = avaliada primeiro. A recursão à esquerda (`E → E + T`) força **associatividade à esquerda**, resolvendo `1-2-3` como `(1-2)-3`. Uma única árvore por sentença — não-ambígua.

Dois resultados que fecham o assunto:

1. **Não existe algoritmo que decida se uma GLC arbitrária é ambígua.** O problema é indecidível (redução do Problema da Correspondência de Post). Por isso geradores de parser como o `yacc`/`bison` não *provam* que sua gramática é boa — eles reportam conflitos *shift/reduce* e *reduce/reduce*, que são sintomas de ambiguidade encontrados na construção da tabela.
2. **Existem linguagens inerentemente ambíguas** — para as quais *nenhuma* GLC não-ambígua existe. Felizmente nenhuma linguagem de programação real é assim; o clássico *dangling else* (`if a then if b then x else y`) é ambiguidade da gramática, não da linguagem, e se resolve com uma regra de desempate ou reescrevendo a gramática.

### Geradores vs. Reconhecedores — a Simetria Que Estrutura a Cadeira

A frase final da aula ("expressões regulares são geradoras, autômatos finitos são reconhecedores") é o eixo de toda a disciplina, e vale explicitar a dualidade completa:

| | **Gerador** (produz sentenças) | **Reconhecedor** (aceita/rejeita) |
|---|---|---|
| Tipo 3 | Expressão regular / gramática regular | Autômato finito |
| Tipo 2 | Gramática livre de contexto | Autômato de pilha |

A equivalência entre as duas colunas é um **teorema**, não uma definição — o **teorema de Kleene** garante que toda expressão regular tem um AFD equivalente e vice-versa. E ele é *construtivo*: existe um algoritmo que transforma um no outro (Thompson: regex → AFN; construção de subconjuntos: AFN → AFD; Hopcroft: minimização do AFD). Essa cadeia de construções é literalmente o que o `lex`/`flex` executa para transformar suas expressões regulares em código C — e é o motivo pelo qual se escreve o gerador e recebe o reconhecedor de graça.

---

### Referências para ir além

- **Aho, Lam, Sethi & Ullman, *Compilers: Principles, Techniques and Tools*, 2ª ed.** — o "Livro do Dragão". Cap. 3 (análise léxica), Cap. 4 (análise sintática, ambiguidade, eliminação de recursão à esquerda).
- **Hopcroft, Motwani & Ullman, *Introduction to Automata Theory, Languages and Computation*** — a referência formal para a hierarquia de Chomsky, lema do bombeamento e teorema de Kleene. É a cadeira de Linguagens & Autômatos que "ninguém lembra".
- **Chomsky, *Three Models for the Description of Language* (1956)** — o artigo original da hierarquia; curto e legível.
- **Terence Parr, *Language Implementation Patterns*** — a contraparte prática: como escrever parsers, ASTs e interpretadores de verdade, sem o peso teórico do Dragão.
- **`flex` & `bison` manuals (GNU)** — a documentação explica conflitos *shift/reduce* melhor do que a maioria dos livros, com exemplos reais de gramáticas ambíguas.
- **Nora Sandler, *Writing a C Compiler* (No Starch, 2024)** — implementa um compilador de C para **x86-64** incrementalmente; alinhado com a promessa de gerar código real da Aula 01.
