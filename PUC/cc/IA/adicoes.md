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

---

## Aula 03 — Duas Passagens, o Problema $M \times N$ e o Custo de Uma Passagem Só

### Por que separar front-end de back-end: a conta que justifica tudo

As notas listam as vantagens da arquitetura de duas passagens — portabilidade, combinações possíveis, otimização mais simples sobre a IR. A justificativa fica muito mais forte quando escrita como aritmética.

Suponha $M$ linguagens que se quer compilar e $N$ arquiteturas-alvo. Sem representação intermediária, é preciso escrever um compilador para cada par: **$M \times N$** implementações. Com uma IR no meio, escreve-se $M$ front-ends e $N$ back-ends: **$M + N$**.

| | Sem IR | Com IR |
|---|---|---|
| 3 linguagens, 3 alvos | 9 | 6 |
| 10 linguagens, 10 alvos | 100 | **20** |
| 30 linguagens, 15 alvos | 450 | **45** |

Acrescentar uma linguagem nova custa **um** front-end e ela imediatamente compila para todos os alvos existentes. Acrescentar um processador novo custa **um** back-end e todas as linguagens existentes passam a rodar nele.

Isso não é teoria: é literalmente o modelo de negócio do **LLVM**. Clang (C/C++/Objective-C), Rust, Swift, Julia e Zig são todos front-ends diferentes que emitem **LLVM IR**; o mesmo conjunto de back-ends gera x86-64, ARM64, RISC-V, WebAssembly e GPU. Quando a Apple migrou de x86 para ARM, as linguagens que usavam LLVM ganharam o novo alvo praticamente de graça. O **GCC** faz o mesmo com o **GIMPLE**.

O nome dessa forma arquitetural é **narrow waist** — cintura estreita. Uma interface no meio, escolhida para ser simples e estável, com muitas implementações de cada lado. É o mesmo padrão do IP nas redes e do POSIX nos sistemas operacionais, e reconhecê-lo é mais útil que decorar a lista de vantagens.

**A desvantagem que as notas registram merece nuance.** "Compilação mais lenta devido à quantidade de fases" é verdade para uma compilação isolada, mas a IR é justamente o que permite que otimizações caras sejam escritas **uma vez** em vez de $N$ vezes — e otimizações melhores compensam de longe o tempo extra do compilador. O trade-off real não é velocidade contra portabilidade: é tempo de compilação contra qualidade do código gerado.

---

### Compiladores de uma passagem: o que a restrição realmente custa

As notas descrevem o modelo — "para cada token, analisa, verifica e já gera o código" — e apontam a limitação: "*dificulta otimizações que dependem de contexto futuro, ex: uso de uma variável declarada mais adiante*". Esse exemplo é mais importante do que parece, porque ele **moldou a sintaxe de linguagens inteiras**.

Se o compilador só pode ver o que já leu, então tudo precisa ser declarado antes de ser usado. E daí saem, diretamente:

- **`forward` do Pascal.** Para escrever duas funções mutuamente recursivas, Wirth teve que inventar uma palavra-chave que dissesse "esta função existe, o corpo vem depois". Isso é sintaxe existindo puramente para acomodar uma limitação do compilador.
- **Os arquivos `.h` do C.** Um header é, em essência, uma declaração antecipada em massa. C foi projetado para ser compilável em uma passagem numa máquina com memória minúscula — e o mundo ainda paga por essa decisão com dependências de header, guardas de inclusão e tempos de compilação longos.
- **A ausência disso em Java e C#.** Nessas linguagens um método pode chamar outro definido 300 linhas abaixo, e uma classe pode referenciar outra de outro arquivo sem declaração prévia. Isso só é possível porque o compilador faz **múltiplas passagens**: uma para coletar todas as assinaturas numa tabela de símbolos, outra para verificar os corpos.

**A anedota que vale conhecer.** C não é nem sequer compilável em uma passagem de verdade, por causa do **lexer hack**: em `A * B;`, o analisador não consegue decidir se isso é uma multiplicação ou a declaração de um ponteiro sem saber se `A` é um tipo — informação que vive na tabela de símbolos, que é fase *semântica*. A solução real, em compiladores C de verdade, é o analisador léxico consultar a tabela de símbolos para decidir se devolve `IDENTIFIER` ou `TYPEDEF_NAME`, quebrando a separação limpa entre as fases que o resto da disciplina ensina. É um bom lembrete de que a arquitetura em camadas do slide é um ideal, e linguagens reais vazam entre elas.

---

### Sobre o `GOTO`: a citação e o teorema

A frase registrada nas notas — "*programar com go-to's é uma aberração*" — não é opinião solta do Agustini, é um dos artigos mais famosos da computação: **Edsger Dijkstra, "Go To Statement Considered Harmful"**, *Communications of the ACM*, março de 1968. (O título foi escolhido pelo editor Niklaus Wirth; Dijkstra havia chamado o texto de "A Case Against the Go To Statement".)

O argumento de Dijkstra é preciso e vale mais do que a caricatura: com `goto`, a posição no texto do programa deixa de ser suficiente para descrever o estado da execução. Sem `goto`, para saber "onde estou", bastam o ponto no código e a pilha de chamadas. Com `goto`, é preciso saber o **histórico** de como se chegou ali — e raciocinar sobre o programa vira raciocinar sobre todas as trajetórias possíveis.

O que dá fundamento formal à briga é o **Teorema do Programa Estruturado**, de **Böhm e Jacopini** (1966): qualquer função computável pode ser escrita usando apenas três construções — **sequência**, **seleção** (`if/else`) e **iteração** (`while`). O `goto` nunca é *necessário*. Isso transformou a discussão de "dá para viver sem?" em "por que manter?".

Um adendo honesto que raramente acompanha a citação: o `goto` sobreviveu em nichos onde as três construções ficam desajeitadas. O kernel do Linux usa `goto` extensivamente para tratamento de erro — o padrão `goto cleanup` que desfaz alocações na ordem inversa — porque a alternativa em C é aninhamento profundo ou repetição de código. A objeção de Dijkstra era ao **salto irrestrito**, não a saltos para a frente, locais e disciplinados.

---

## Aula 04 — Por Que o Léxico Não é Sintático: a Resposta Formal

### A hierarquia de Chomsky como resposta à pergunta

As notas fazem a pergunta certa ("Por que a análise léxica não é parte da sintática?") e a respondem com o material de expressões regulares. A resposta completa tem duas metades: uma teórica, sobre o que *pode* ser feito, e uma prática, sobre o que *convém* fazer.

**A metade teórica.** Tokens e estruturas sintáticas vivem em níveis diferentes da hierarquia de Chomsky (já vista na Aula 02).

| Nível | Gramática | Reconhecedor | O que se descreve |
|---|---|---|---|
| Tipo 3 | Regular | **AFD** (memória fixa) | identificadores, números, palavras-chave, comentários |
| Tipo 2 | Livre de contexto | **Autômato de pilha** | expressões aninhadas, blocos, parênteses balanceados |

A inclusão é **estrita**: toda linguagem regular é livre de contexto, mas não o contrário. Um autômato de pilha poderia, em princípio, reconhecer os tokens também — a separação não é uma necessidade lógica. Mas a recíproca é falsa e é isso que importa: **nenhum AFD reconhece parênteses balanceados**, então a análise sintática *não pode* ser feita com as ferramentas da léxica. A hierarquia força a existência da segunda fase; ela apenas *permite* a primeira.

**A metade prática — por que separar mesmo assim.** Quatro razões concretas:

1. **Velocidade.** Um AFD gasta tempo constante por caractere, sem pilha, sem alocação: um laço com uma tabela de transições. O scanner processa a maior parte dos caracteres do arquivo, e fazer isso com a maquinaria de um parser custaria caro.
2. **Simplicidade da gramática.** Se o parser tivesse que lidar com espaços em branco e comentários, **cada** produção precisaria permitir espaços entre os símbolos. A gramática incharia sem ganhar poder expressivo. Descartar o que não tem significado é a maior contribuição do scanner.
3. **Modularidade.** Trocar a codificação de entrada, aceitar identificadores Unicode, mudar a sintaxe de comentários — tudo isso é alteração local no scanner e não toca no parser.
4. **A regra da maior munch.** Decidir que `>=` é um token só e não `>` seguido de `=` é natural num AFD e desajeitado numa gramática.

---

### De expressão regular a analisador: o pipeline que o JFlex executa

As notas registram o fundamento — "cada letra do ASCII é uma expressão regular; a concatenação também é; a string vazia também" — que é a definição **indutiva** de ER: casos base ($\varepsilon$, $\emptyset$, cada símbolo) e três operadores (concatenação, união `|`, fecho de Kleene `*`). O que fica implícito é como esse texto vira um programa.

$$\text{ER} \xrightarrow[\text{Thompson}]{\text{construção}} \text{AFN} \xrightarrow[\text{subconjuntos}]{\text{determinização}} \text{AFD} \xrightarrow[\text{Hopcroft}]{\text{minimização}} \text{AFD mínimo} \longrightarrow \text{tabela}$$

- **Construção de Thompson.** Cada operador da ER vira um bloquinho de AFN com uma entrada e uma saída, colados por transições-$\varepsilon$. O resultado tem tamanho linear na ER e é mecânico de construir.
- **Construção de subconjuntos.** Cada estado do AFD passa a ser um *conjunto* de estados do AFN — a ideia de "todos os lugares onde eu poderia estar agora". No pior caso isso é exponencial ($2^n$ estados), mas em expressões de tokens reais o crescimento é modesto.
- **Minimização de Hopcroft.** Funde estados indistinguíveis, em $O(n \log n)$. O AFD mínimo é **único** a menos de renomeação — um resultado bonito que não tem análogo em autômatos de pilha.

O que o JFlex faz é exatamente isso, uma vez, em tempo de geração — e o que ele emite é a tabela de transições mais um laço. É por isso que o analisador gerado é rápido: todo o trabalho pesado aconteceu antes de o programa rodar.

**Um detalhe que explica o tamanho do arquivo gerado.** O scanner não constrói um AFD por token; ele une todas as regras com `|` num único autômato gigante e anexa a cada estado de aceitação a informação de qual regra casou. Por isso um `.flex` de 40 linhas gera um `.java` de milhares — é a tabela de transições escrita como um array.

---

### Dangling else: a ambiguidade é da gramática, não da linguagem

As notas registram a regra do C — "*o else sempre pertence ao if mais próximo*" — e a explicação "ifs e elses são inerentemente ambíguos". A segunda parte precisa de correção, e a correção é conceitualmente importante.

**Ambiguidade é propriedade de uma gramática, não de uma linguagem.** Dizer que a construção é "inerentemente ambígua" é impreciso: a *gramática ingênua* é ambígua; a **linguagem** não é. Dá para escrever uma gramática não-ambígua para exatamente o mesmo conjunto de programas, e ela é instrutiva:

```code
Cmd         = CmdCasado | CmdSolto .

CmdCasado   = "if" "(" Expr ")" CmdCasado "else" CmdCasado
            | outroComando .

CmdSolto    = "if" "(" Expr ")" Cmd
            | "if" "(" Expr ")" CmdCasado "else" CmdSolto .
```

A ideia: um **comando casado** é aquele em que todo `if` já tem seu `else`. A regra força que o ramo *then* de um `if-else` seja sempre casado — e é isso que impede um `if` sem `else` de se esconder ali dentro e capturar o `else` de fora. O resultado é uma derivação única para cada programa, com o `else` ligado ao `if` mais próximo por construção.

Ninguém escreve isso na prática — a gramática dobra de tamanho e fica ilegível. O que se faz é manter a gramática ambígua e resolver o conflito na ferramenta, o que reaparece na **Aula 13** como conflito *shift-reduce* e na **Aula 14** como regra de desempate da tabela. Mas saber que a gramática não-ambígua existe muda o entendimento do problema: o conflito do parser não é um defeito da linguagem, é uma escolha deliberada de trocar clareza da gramática por uma regra de desempate.

**Vale registrar como outras linguagens escaparam.** O problema desaparece quando a sintaxe delimita blocos: Python usa indentação, Go e Rust exigem chaves sempre, e Ada/Modula fecham com `end if`/`fi` — que é exatamente o `fi` da gramática de exemplo da Aula 06. Wirth, que projetou Pascal com esse defeito, o consertou em Modula-2.

---

## Aula 05 — Anatomia de um `.flex` e a Regra da Maior Munch

### As três seções, e o que vai em cada uma

As notas apontam o que cai na P1 — "a segunda seção `%%` do código, 2,5 pontos" — sem registrar a estrutura completa. Um arquivo JFlex tem três blocos separados por `%%`:

```java
// ---- 1. Código de usuário: copiado literalmente para o topo do .java gerado
package meucompilador;
import java.util.*;

%%
// ---- 2. Opções, declarações e macros
%class MeuLexico          // nome da classe gerada
%unicode                  // conjunto de caracteres
%type  int                // o que yylex() devolve
%line                     // habilita yyline (número da linha)
%column                   // habilita yycolumn

DIGITO      = [0-9]
LETRA       = [a-zA-Z_]
FIMDELINHA  = \r|\n|\r\n
BRANCO      = {FIMDELINHA}|[ \t\f]

%%
// ---- 3. Regras: padrão { ação em Java }
"if"                        { return IF; }
"else"                      { return ELSE; }
{LETRA}({LETRA}|{DIGITO})*  { return IDENT; }
{DIGITO}+                   { return NUMBER; }
{BRANCO}+                   { /* descartado: nenhum return */ }
"//" [^\r\n]*               { /* comentário de linha, descartado */ }
.                           { throw new Error("caractere ilegal: " + yytext()); }
```

O aviso das notas sobre não usar as macros de `DIGIT`, `LETTER` e `LineTerminator` na prova faz sentido: elas são a segunda seção, que é "receita de bolo", e o que está sendo avaliado é a **terceira**. Escrever as classes de caracteres direto nas regras (`[0-9]+` em vez de `{DIGITO}+`) resolve e evita perder tempo.

Dois detalhes que costumam custar pontos:

- **Ação sem `return` significa "ignore e continue".** É assim que espaços e comentários somem — não é um caso especial do gerador, é só uma ação que não devolve nada.
- **A regra `.` no final é uma rede de segurança.** Sem ela, um caractere inesperado faz o scanner falhar de forma obscura. Com ela, vem uma mensagem de erro com posição.

---

### "Casou a regra, executa" — o que acontece quando duas regras casam

A frase do Agustini registrada nas notas esconde a única regra que realmente precisa ser decorada, porque ela decide os casos ambíguos. O scanner aplica, nesta ordem:

1. **Maior munch** (*longest match*): entre todas as regras que casam na posição atual, vence a que consome **mais caracteres**.
2. **Ordem no arquivo**: em caso de empate no comprimento, vence a regra que aparece **primeiro**.

Daí saem as consequências práticas:

**Palavras-chave têm que vir antes de identificadores.** `if` casa com `"if"` (2 caracteres) e com `{LETRA}+` (2 caracteres) — empate. A regra 2 decide, e quem estiver escrito primeiro ganha. Invertida a ordem, toda palavra-chave da linguagem vira identificador e o parser nunca funciona. É o bug número um de quem escreve o primeiro `.flex`.

**Mas `ifx` vira identificador, corretamente.** Aqui a regra 1 decide antes: `{LETRA}+` consome 3 caracteres contra 2 de `"if"`. A maior munch protege identificadores que *começam* com palavra-chave, sem que seja preciso escrever nada especial.

**E `>=` sai inteiro.** Com as regras `">"` e `">="` declaradas, a entrada `>=` casa as duas; a maior munch escolhe a de 2 caracteres, independentemente da ordem no arquivo.

**O caso em que a maior munch atrapalha.** Em `1..10` (um intervalo, em Pascal ou Rust), a regra de número real `{DIGITO}+\.{DIGITO}*` casaria `1.` e depois sobraria `.10` — quebrando o intervalo. Linguagens com esse construto resolvem com *lookahead* (`{DIGITO}+ / [^.]`) ou proibindo a forma `1.` sem dígitos depois. É o exemplo canônico de que a maior munch é uma heurística, não uma verdade.

---

### Os terminais de uma gramática JSON

O aviso em caixa alta das notas — "**SABER OS TERMINAIS DE DETERMINADA GRAMÁTICA**" — merece a lista completa, porque JSON é o exemplo que reaparece na Aula 06.

| Terminal | Padrão no scanner | Categoria |
|---|---|---|
| `{` `}` `[` `]` `:` `,` | literais de 1 caractere | pontuação estrutural |
| `STRING` | `\"([^\"\\]\|\\.)*\"` | literal |
| `NUMBER` | `-?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?` | literal |
| `TRUE` `FALSE` `NULL` | `"true"` `"false"` `"null"` | palavras reservadas |

São **seis** símbolos de pontuação, não quatro — as notas listam `" { , [` e faltam o fechamento e os dois-pontos. E note o que **não** é terminal: espaços em branco (descartados) e as chaves de abertura/fechamento **não são pareadas** pelo scanner. Ele devolve `{` e `}` como tokens independentes; quem conta se abrem e fecham na ordem certa é o parser, pelo motivo desenvolvido na Aula 06.

Note também que `STRING` e `NUMBER` carregam **valor**, não só categoria. O parser precisa não só saber "veio um número" mas qual número — o que na prática significa que a ação da regra guarda `yytext()` num campo além de devolver o código do token. Essa distinção entre **token** (a categoria) e **lexema** (o texto que casou) é a que mais confunde no começo, e é o que o `yytext()` existe para resolver.

---

## Aula 06 — Por Que o AFD Não Conta Chaves, e o Que FIRST/FOLLOW Decidem

### A prova de que autômato finito não conta

As notas chegam à conclusão certa por intuição — "*problema do movimento, autômatos finitos não têm memória; só preciso saber onde estou*" — e essa intuição tem uma prova formal curta que vale conhecer, porque ela é o argumento que **obriga** a existência da análise sintática.

Considere $L = \{\texttt{\{}^n \texttt{\}}^n \mid n \ge 1\}$ — chaves balanceadas. Suponha que exista um AFD com $k$ estados que reconheça $L$. Alimente-o com $\texttt{\{}^{k+1}$. Ao ler $k+1$ símbolos, o autômato visitou $k+2$ estados; como só existem $k$ estados distintos, pelo **princípio da casa dos pombos** algum estado se repetiu. Sejam $i < j$ as posições em que isso ocorreu: o autômato está no mesmo estado depois de ler $i$ chaves e depois de ler $j$ chaves.

Mas então ele não consegue mais distinguir os dois casos — qualquer coisa que venha depois será processada de forma idêntica. Em particular, se ele aceita $\texttt{\{}^j\texttt{\}}^j$, ele **também aceita** $\texttt{\{}^i\texttt{\}}^j$, que não está em $L$. Contradição. Nenhum AFD reconhece $L$.

Esse é o **lema do bombeamento para linguagens regulares** aplicado ao caso concreto, e ele formaliza exatamente o "não tem memória" das notas: um AFD tem uma quantidade **fixa e finita** de informação de estado, então não consegue contar sem limite. A pilha do autômato de pilha é precisamente a memória ilimitada que falta.

**O corolário que organiza a disciplina inteira:** a observação das notas — "*muita coisa que eu achava ser léxico é na verdade sintático*" — tem um critério mecânico. Se a regra envolve **contar** ou **parear** coisas separadas por uma distância arbitrária, ela não é léxica. Chaves, parênteses, `begin`/`end`, tags de abertura e fechamento: tudo isso é sintático. Se a regra é sobre a forma de um pedaço contíguo e limitado de texto, é léxica.

---

### Recursão à esquerda e fatoração à esquerda: as duas cirurgias

As notas mostram a fatoração à esquerda no exemplo do `if/else` e a razão ("por termos muita coisa em comum em caminhos diferentes, ele deixa de ser determinístico"). Há na verdade **duas** transformações obrigatórias antes de um parser descendente funcionar, e vale ter as duas com o algoritmo.

**1. Fatoração à esquerda** — resolve alternativas com prefixo comum.

Se a gramática tem $A \to \alpha\beta_1 \mid \alpha\beta_2$, o parser olhando o lookahead vê $\alpha$ nos dois lados e não sabe qual escolher. A transformação extrai o prefixo:

$$A \to \alpha A' \qquad A' \to \beta_1 \mid \beta_2$$

Adiar a decisão até depois de consumir $\alpha$ é exatamente o que as notas fizeram ao criar o não-terminal `R`. Generalizando o exemplo:

```code
CMD -> "if" "(" e ")" CMD R
R   -> "else" CMD
     | ε
```

**2. Eliminação da recursão à esquerda** — resolve o laço infinito.

Essa é a que as notas não mencionam, e é a mais letal. Uma produção como $A \to A\alpha \mid \beta$ faz um parser descendente chamar `A()` como primeira coisa dentro de `A()`, sem consumir nenhum token: **estouro de pilha imediato**, sem nem olhar a entrada. E ela aparece na gramática mais natural que existe, a de expressões aritméticas:

```code
Expr -> Expr "+" Term | Term          // recursiva à esquerda: quebra descida recursiva
```

A transformação padrão troca a recursão à esquerda por recursão à direita com um não-terminal auxiliar:

$$A \to A\alpha \mid \beta \qquad\Longrightarrow\qquad A \to \beta A' \qquad A' \to \alpha A' \mid \varepsilon$$

```code
Expr  -> Term Expr'
Expr' -> "+" Term Expr' | ε
```

**O preço, e por que ninguém se importa.** A gramática transformada não é mais recursiva à esquerda, mas também perdeu a **associatividade à esquerda** na estrutura da árvore — `a - b - c` precisa ser $(a-b)-c$, e a nova gramática sugere $a-(b-c)$. Na prática isso se resolve na *ação semântica*: em notação EBNF a mesma coisa se escreve como um laço,

```code
Expr = Term { ("+" | "-") Term } .
```

e o código correspondente é um `while` que vai acumulando à esquerda, recuperando a associatividade correta. É por isso que gramáticas de compilador são escritas em EBNF com `{ }` e `[ ]` em vez da forma pura de Chomsky — e é a mesma notação Cocol/EBNF de Mössenböck que a Aula 08 adota.

Vale notar que essa é uma **assimetria entre descendente e ascendente**: parsers LR, da Aula 13, lidam com recursão à esquerda sem transformação nenhuma — na verdade *preferem* recursão à esquerda, porque ela consome pilha constante. A cirurgia acima existe só para o lado descendente.

---

### FIRST e FOLLOW: o que "conjunto de símbolos iniciais" significa

As notas registram que a alternativa correta é escolhida olhando "o conjunto de símbolos iniciais de cada alternativa". Esse conjunto tem nome, definição precisa, e um irmão sem o qual a coisa não fecha.

**FIRST($\alpha$)** é o conjunto de terminais que podem **começar** uma cadeia derivada de $\alpha$. Se $\alpha$ pode derivar a cadeia vazia, então $\varepsilon \in \text{FIRST}(\alpha)$.

**FOLLOW($A$)** é o conjunto de terminais que podem aparecer **imediatamente depois** de $A$ em alguma derivação. É necessário exatamente por causa do $\varepsilon$: se o parser está em $A$ e $A$ pode sumir, a decisão de "sumir" tem que ser tomada olhando o que vem *depois* de $A$ — informação que FIRST não tem.

A condição que uma gramática precisa satisfazer para ser **LL(1)** — analisável descendentemente com 1 token de lookahead — é: para cada par de alternativas $A \to \alpha \mid \beta$,

1. $\text{FIRST}(\alpha) \cap \text{FIRST}(\beta) = \emptyset$ — nenhum token inicia as duas;
2. se $\beta \Rightarrow^* \varepsilon$, então $\text{FIRST}(\alpha) \cap \text{FOLLOW}(A) = \emptyset$.

Conferindo nos exemplos das notas:

- A gramática original do `if/else` viola (1): as duas alternativas começam com `if`. É a fatoração que conserta.
- `Expr -> Expr "+" Term | Term` viola (1) de forma mais insidiosa: $\text{FIRST}$ das duas alternativas é o mesmo conjunto, porque a primeira começa com o próprio `Expr`. Recursão à esquerda é sempre uma violação de LL(1).
- A gramática fatorada, `R -> "else" CMD | ε`, satisfaz (1) trivialmente, mas cai exatamente na condição (2): `else` pertence a $\text{FOLLOW}(R)$, porque um `if` externo pode ter seu próprio `else` logo depois. **O dangling else é um conflito LL(1) genuíno** — e a resolução padrão (escolher a alternativa `"else" CMD` em vez de $\varepsilon$) é, mais uma vez, a regra do "else mais próximo", agora expressa como uma preferência na tabela.

O ponto que fecha as três aulas: o mesmo problema aparece como ambiguidade na gramática (Aula 04), como conflito LL(1) aqui, e como conflito *shift-reduce* na Aula 13. É um só fenômeno visto de três lugares.

---

## Aula 08 — Os Limites da GLC e a Descida Recursiva na Prática

### O que "não é livre de contexto" quer dizer, com prova

As notas listam duas limitações — declaração antes do uso, e compatibilidade de tipos — e as apresentam como fatos. A primeira tem prova, e a prova ilumina por que existe uma fase semântica separada.

A linguagem-modelo é $L = \{wcw \mid w \in \{a,b\}^*\}$: uma cadeia, um separador, e **a mesma cadeia** repetida. Ela **não é livre de contexto**, pelo lema do bombeamento para GLCs. A intuição: uma pilha é LIFO, então ao empilhar $w$ e desempilhar para comparar, a comparação sai **ao contrário** — uma pilha reconhece $wcw^R$ (palíndromos) com facilidade e $wcw$ de jeito nenhum.

Agora mapeie: "todo nome deve ser declarado antes do uso" é exatamente exigir que o identificador em `int contador;` e o identificador em `contador = 5;` sejam **a mesma cadeia**, separados por uma quantidade arbitrária de texto. É o problema $wcw$ disfarçado, e nenhuma GLC o resolve.

A consequência é arquitetural e é a razão de existir da terceira fase:

| Fase | Formalismo | Pergunta que responde |
|---|---|---|
| Léxica | ER / AFD | Isto é um token válido? |
| Sintática | GLC / Autômato de pilha | A estrutura está bem-formada? |
| **Semântica** | **Tabela de símbolos + regras** | Isto **faz sentido**? |

A **tabela de símbolos** é exatamente a memória extra que a GLC não tem — um dicionário associando nomes a tipos, escopos e posições. O formalismo acadêmico que descreve isso são as **gramáticas de atributos** de Knuth (1968), que anexam atributos sintetizados e herdados aos nós da árvore; na prática, compiladores fazem uma passagem sobre a AST com uma tabela de símbolos em mãos.

**E sobre o `Fuck you in specific JS` das notas.** A observação é justa e vale formalizar: compatibilidade de tipos também não é livre de contexto, porque exige lembrar o tipo declarado de cada nome. A diferença entre linguagens não está na gramática — está em **quando** essa verificação roda. Java e C# a fazem em tempo de compilação (tipagem estática); JavaScript e Python a fazem em tempo de execução, ou simplesmente coagem os valores. `[] + {}` em JS é sintaticamente impecável; o que falta é a fase que diria que aquilo não significa nada.

---

### Descida recursiva: a gramática vira código, quase literalmente

As notas descrevem a análise top-down em abstrato ("a AP decide que alternativa expandir olhando para a entrada que ainda falta"). O que torna isso concreto é que a implementação é quase uma transcrição: **cada não-terminal vira uma função**, e cada produção vira o corpo dela.

Com a gramática das notas, já convertida para EBNF para evitar a recursão à esquerda:

```code
Expr   = Term { "+" Term } .
Term   = Factor { "*" Factor } .
Factor = ident | "(" Expr ")" .
```

o parser inteiro é isto:

```java
Token la;                                  // o token de lookahead

void consome(int esperado) {
    if (la.tipo != esperado) erro(esperado, la);
    la = lexico.proximo();                 // avança
}

void Expr() {
    Term();
    while (la.tipo == PLUS) { consome(PLUS); Term(); }
}

void Term() {
    Factor();
    while (la.tipo == STAR) { consome(STAR); Factor(); }
}

void Factor() {
    if (la.tipo == IDENT) {
        consome(IDENT);
    } else if (la.tipo == LPAR) {
        consome(LPAR); Expr(); consome(RPAR);
    } else {
        erro("esperava identificador ou '('", la);
    }
}
```

Três coisas que esse código torna visíveis e que os slides não mostram:

1. **A "pilha" do autômato é a pilha de chamadas do Java.** Não há estrutura de dados explícita: o aninhamento de `(` `)` vira aninhamento de chamadas de `Expr` e `Factor`. É a implementação mais direta possível de um autômato de pilha, e explica por que o formalismo e a prática se encaixam tão bem aqui.
2. **O `if` dentro de `Factor` é literalmente o teste de FIRST.** `IDENT` e `LPAR` são $\text{FIRST}$ das duas alternativas; a disjunção dos conjuntos é o que garante que o `if` decide corretamente. A teoria da Aula 06 vira uma linha de código.
3. **Onde entram as ações semânticas.** Para construir uma AST em vez de só validar, cada função passa a devolver um nó: `Expr()` vira `No Expr()` e o `while` acumula `no = new NoSoma(no, Term())`. É aí que a associatividade à esquerda perdida na transformação EBNF é recuperada — no acúmulo, não na gramática.

**Por que isso importa apesar de LR ser "mais poderoso".** A descida recursiva é escrita à mão, então dá para colocar mensagens de erro específicas, recuperação de erro sob medida e casos especiais onde a linguagem exige. Não é coincidência que **GCC, Clang e o compilador de Rust** tenham todos abandonado geradores LR em favor de descida recursiva manual — a qualidade das mensagens de erro venceu a elegância do gerador. O assunto volta no fim da Aula 14.

---

### Determinismo: a diferença que faz um parser existir

Há uma distinção escondida em "autômato de pilha" que as notas não separam e que é o divisor de águas de toda a teoria de parsing.

**APs não-determinísticos** reconhecem exatamente as linguagens livres de contexto. **APs determinísticos** (APD) reconhecem um subconjunto **estritamente menor**, as *linguagens livres de contexto determinísticas*. Diferente do caso finito — onde AFN e AFD têm o mesmo poder, via construção de subconjuntos — aqui o não-determinismo **acrescenta poder de verdade**, e não há como determinizar.

Isso é o que dá sentido à frase registrada nas notas, "**tem que ser rápido, se não... não funciona**". Um parser precisa ser determinístico porque simular não-determinismo significa explorar alternativas e retroceder, o que custa tempo exponencial no pior caso. Toda a taxonomia da disciplina é, na verdade, um mapa de **quais fatias das LLC são determinísticas o suficiente**:

| Classe | Autômato | Decide olhando |
|---|---|---|
| LL($k$) | APD, top-down | $k$ tokens à frente, antes de expandir |
| LR($k$) | APD, bottom-up | $k$ tokens à frente, mais o estado da pilha |
| LLC determinísticas | APD | (o limite teórico) |
| LLC | AP não-determinístico | (fora de alcance de parser linear) |

E a inclusão **LL($k$) $\subsetneq$ LR($k$)** é estrita — toda gramática LL(1) é LR(1), mas existem gramáticas LR(1) que nenhum $k$ torna LL. A razão é intuitiva: o parser descendente tem que escolher a produção **antes** de ver seus filhos, enquanto o ascendente decide **depois** de já ter reconhecido o lado direito inteiro. Decidir mais tarde com mais informação é estritamente melhor — e é exatamente o argumento que abre a Aula 13.

Uma nota final sobre a "**Vareia**" das duas respostas do semestre: gramáticas ambíguas correspondem a APs genuinamente não-determinísticos, e é por isso que ferramentas como Bison precisam de uma regra de desempate (Aula 14) ou de um parser **GLR**, que explora todas as alternativas em paralelo e devolve uma floresta de árvores. É o que se usa para C++ e para linguagem natural, onde a ambiguidade é irredutível.

---

## Aula 13 — Handles, Prefixos Viáveis e o Teorema que Faz o LR Funcionar

### O que é um *handle*, e o fato surpreendente sobre ele

As notas descrevem o mecanismo corretamente — "*a cada passo, procura na pilha uma sequência que corresponda ao lado direito de alguma produção e a substitui*" — e usam a palavra *handle* sem defini-la. A definição precisa, e o teorema que vem depois dela, são a parte bonita da teoria LR.

**Definição.** Numa derivação mais à direita, um **handle** é a ocorrência do lado direito de uma produção que, ao ser reduzida, dá o passo anterior da derivação. Não basta que uma sequência *pareça* o lado direito de alguma produção — ela tem que estar na posição certa. É por isso que o parser não pode simplesmente reduzir qualquer coisa que encontre: reduzir fora de um handle leva a um beco sem saída.

A sequência de símbolos da pilha em qualquer ponto de um parse correto chama-se **prefixo viável** — um prefixo de alguma forma sentencial à direita que não ultrapassa o fim do handle.

**O teorema.** Para qualquer gramática livre de contexto, o conjunto de todos os prefixos viáveis é uma **linguagem regular**.

Vale parar nisso. A linguagem sendo analisada não é regular — se fosse, não precisaríamos de pilha nenhuma. Mas o conjunto de *estados de pilha alcançáveis* é. E linguagens regulares são reconhecidas por autômatos finitos. Portanto:

> Um **autômato finito** consegue rastrear em que ponto da análise a pilha está, e dizer quando há um handle no topo.

É esse o autômato LR que as notas constroem com itens, *closure* e *go-to* sem que o motivo apareça. Cada conjunto fechado de itens é um estado desse AFD; a entrada dele não é o programa, é o **conteúdo da pilha**. O parser é a soma de duas máquinas: uma pilha que guarda o que já foi reconhecido, e um AFD que olha para essa pilha e decide o que fazer. Knuth descobriu isso em 1965, e é a razão pela qual parsers LR são lineares no tamanho da entrada.

Isso também explica por que a pilha guarda **estados** e não apenas símbolos — nas notas da Aula 14, cada linha do trace tem um número de estado. O estado no topo é a resposta do AFD para "o que a pilha inteira significa", memorizada para não precisar reprocessá-la a cada passo.

### Itens, *closure* e *go-to*, com o significado de cada um

As notas definem os três corretamente. Vale amarrar cada um ao papel que desempenha no AFD:

| Conceito | Definição operacional | Papel no autômato |
|---|---|---|
| **Item LR(0)** $A \to \alpha \bullet \beta$ | Já reconheci $\alpha$, espero $\beta$ | uma hipótese em aberto |
| **Estado** | um conjunto fechado de itens | todas as hipóteses simultaneamente vivas |
| **closure($I$)** | para cada $\bullet B$, acrescenta $B \to \bullet\gamma$ | "se espero um $B$, então posso estar começando qualquer produção de $B$" |
| **goto($I$, $X$)** | avança o $\bullet$ sobre $X$ e fecha | a função de transição |
| Item **completo** $A \to \alpha\bullet$ | o handle inteiro está na pilha | candidato a **reduce** |

O ponto que a tabela torna óbvio: um estado conter **vários** itens não é um defeito, é o funcionamento normal — é o mesmo "conjunto de estados onde eu poderia estar" da construção de subconjuntos da Aula 04. O não-determinismo é resolvido carregando todas as possibilidades ao mesmo tempo, e a decisão só é tomada quando os itens divergem sobre o que fazer. **Quando eles divergem de forma irreconciliável, isso é um conflito.**

---

### Conflitos na prática: o que Yacc/Bison realmente faz

As notas explicam bem o *dangling else* como conflito shift-reduce e registram a convenção ("o else se liga ao if mais próximo"). O que falta é como essa convenção é **implementada**, e o que fazer quando ela não basta.

**A regra padrão: na dúvida, `shift`.** Diante de um conflito shift-reduce, Bison escolhe `shift` e emite um aviso. E aqui está a elegância: fazer `shift` do `else` significa continuar a produção do `if` **interno**, que é exatamente "o else se liga ao if mais próximo". A convenção das linguagens C-like cai fora da resolução padrão do gerador, de graça. É por isso que praticamente toda linguagem tem essa semântica — não foi tanto um projeto quanto uma consequência da ferramenta.

Um parser Bison para uma gramática C típica reporta **um** conflito shift-reduce do `if/else`, e é tradicional deixá-lo lá, documentado com `%expect 1`.

**Precedência: resolvendo conflitos sem inchar a gramática.** A gramática natural de expressões,

```code
E -> E "+" E | E "*" E | "(" E ")" | NUM
```

é ambígua e gera conflitos em todo operador — ao ver `E + E` com `*` no lookahead, reduzir dá $(a+b)\cdot c$ e empilhar dá $a+(b\cdot c)$. Em vez de reescrever a gramática em camadas (`Expr`/`Term`/`Factor`, como na Aula 08), declara-se:

```code
%left  '+' '-'          // menor precedência, associativo à esquerda
%left  '*' '/'          // maior precedência
%right '^'              // exponenciação associa à direita
%nonassoc '<' '>'       // a < b < c é erro de sintaxe, não expressão
```

A ordem das linhas dá a precedência (de baixo para cima), e a palavra-chave dá a associatividade. Com isso a gramática fica curta e legível, e o gerador resolve cada conflito comparando a precedência da produção a reduzir com a do token de lookahead. `%nonassoc` é o caso interessante: ele torna a construção um **erro**, que é como Python evita a armadilha de `a < b < c` significar `(a<b) < c`.

**Reduce-reduce é outra história.** As notas acertam ao dizer que é "mais raro" e "geralmente aponta um erro de projeto". Vale a precisão: um conflito reduce-reduce significa que o parser chegou a um ponto em que dois itens estão completos e ele não sabe por qual não-terminal reduzir — duas interpretações estruturalmente diferentes da mesma sequência. O padrão de Bison é reduzir pela produção que aparece **primeiro** no arquivo, o que quase sempre é arbitrário e quase sempre está errado. A causa típica é duplicação:

```code
lista_params -> ε
lista_args   -> ε          // ao ver "()", qual reduzir?
```

A correção é unificar os dois não-terminais e distinguir depois, na fase semântica — não mexer na ordem das regras. Um conflito reduce-reduce é sinal de refatorar a gramática; um shift-reduce muitas vezes pode ser deixado à resolução padrão de forma consciente.

---

## Aula 14 — A Hierarquia LR, o Mistério do LALR e o Que Se Usa Hoje

### O algoritmo da tabela, e o tamanho que ela tem

As notas trazem o algoritmo em imagem e a frase que o resume — "*cada goto(I, X) sob um T vira shift; cada item completo $A \to w\bullet$ vira reduce*". Escrito por extenso, para a tabela LR(0)/SLR(1):

Para cada estado $I_i$:
1. Se $A \to \alpha \bullet a\beta \in I_i$ com $a$ **terminal** e $\text{goto}(I_i, a) = I_j$, então $\text{Action}[i, a] = \textbf{shift } j$.
2. Se $A \to \alpha \bullet \in I_i$ e $A \ne S'$, então $\text{Action}[i, a] = \textbf{reduce } A \to \alpha$ — para quais $a$, é a pergunta que separa SLR de LR(1).
3. Se $S' \to S \bullet \in I_i$, então $\text{Action}[i, \$] = \textbf{accept}$.
4. Se $\text{goto}(I_i, A) = I_j$ com $A$ **não-terminal**, então $\text{GoTo}[i, A] = j$.
5. Toda célula não preenchida é **erro**.

O passo 5 é o mais subestimado: as células vazias não são desperdício, são o detector de erro sintático — e a razão pela qual um parser LR detecta erro **na primeira posição possível** (propriedade do prefixo viável), o que dá mensagens de erro com localização precisa.

A distinção Action/GoTo é a que mais confunde, e a regra é simples: **Action é indexada por terminal, GoTo por não-terminal**. Fazer `shift` consome entrada; fazer `goto` não consome nada — é apenas o estado para onde ir depois de uma redução ter empilhado um não-terminal.

Sobre o aviso das notas de que "*na prática, Bison e Yacc já geram essas tabelas*": os números explicam por quê. A gramática de C em Bison gera algo na ordem de **350 estados**; a de C++ passa de mil. Uma tabela LR(1) canônica para C++ chegaria à casa das dezenas de milhares de estados. Construir isso à mão é inviável, e é por isso que a construção manual é exercício de entendimento, não de prática.

---

### A hierarquia, com o que exatamente separa cada nível

As notas trazem a tabela comparativa correta. O que falta é **o que muda** entre os níveis, que é uma coisa só: a resposta à pergunta "para quais tokens de lookahead eu reduzo?".

| Técnica | Reduz $A \to \alpha$ quando o lookahead está em… | Estados | Poder |
|---|---|---|---|
| **LR(0)** | qualquer token (reduz sempre) | $n$ | mínimo |
| **SLR(1)** | $\text{FOLLOW}(A)$ — global, o mesmo em todo estado | $n$ | pouco maior |
| **LALR(1)** | lookaheads do LR(1), com estados de mesmo núcleo fundidos | $n$ | quase LR(1) |
| **LR(1)** | lookahead carregado em cada item, específico do contexto | $\gg n$ | máximo |

As inclusões são **estritas**: LR(0) $\subsetneq$ SLR(1) $\subsetneq$ LALR(1) $\subsetneq$ LR(1).

O problema do SLR fica claro assim: $\text{FOLLOW}(A)$ é calculado sobre a gramática inteira e reúne tudo que pode seguir $A$ em **qualquer** contexto. Num estado específico, só um subconjunto disso é realmente possível — mas o SLR não sabe distinguir, então reduz em casos onde deveria empilhar. É a "reconhece pouca coisa, muito ruim" das notas, agora com o mecanismo: lookahead **global** em vez de **contextual**.

O LR(1) resolve carregando o lookahead dentro de cada item — o item vira $[A \to \alpha\bullet\beta,\ a]$, e a mesma produção pode aparecer em estados diferentes com lookaheads diferentes. O preço é a explosão de estados, porque agora dois estados com os mesmos itens mas lookaheads diferentes são estados **distintos**.

**O truque do LALR, e a consequência estranha.** LALR funde estados LR(1) que têm o mesmo **núcleo** (mesmos itens ignorando os lookaheads), unindo seus conjuntos de lookahead. Isso devolve a contagem de estados ao nível do LR(0) mantendo quase todo o poder — o "sweet spot" das notas.

O detalhe que quase nunca é dito, e que é o resultado mais elegante da aula: essa fusão **nunca introduz conflito shift-reduce**, mas **pode introduzir conflito reduce-reduce**.

A intuição vale: decidir entre shift e reduce depende do lookahead confrontado com a parte *à direita do ponto*, que é idêntica nos estados fundidos — então nada muda. Já decidir entre **duas** reduções depende de os conjuntos de lookahead serem disjuntos, e unir conjuntos pode fazê-los se sobrepor.

É exatamente por isso que existem gramáticas LR(1) que não são LALR(1), e é a origem do bug mais frustrante de quem usa Bison: um conflito reduce-reduce que não corresponde a nenhuma ambiguidade real da linguagem, e que some se a ferramenta for trocada para um gerador LR(1) canônico (como o `%define lr.type canonical-lr` do Bison moderno, ou o algoritmo IELR).

---

### O que se usa hoje — e por que a descida recursiva voltou

O aviso das notas ("*não vamos implementar em aula, Agustini determinou como inútil*") é defensável e merece contexto: a prática divergiu bastante do que a teoria clássica sugere.

| Abordagem | Onde está | Por quê |
|---|---|---|
| **LALR(1)** gerado | Bison/Yacc, Ruby, PHP (historicamente), Go (até 2016) | tabelas compactas, teoria madura |
| **Descida recursiva à mão** | **GCC, Clang, Rust, Go (hoje), TypeScript, C#** | mensagens de erro, recuperação, casos especiais |
| **PEG / packrat** | pest, ANTLR (parcial) | ordem das alternativas resolve a ambiguidade por decreto |
| **ALL(\*)** | ANTLR 4 | lookahead adaptativo e ilimitado, aceita recursão à esquerda direta |
| **GLR** | Elsa, Bison `%glr-parser`, linguagem natural | explora todas as derivações em paralelo, devolve floresta |

A grande virada: **GCC abandonou seu parser Bison para C++ em 2004 e para C em 2006**, migrando para descida recursiva escrita à mão. Clang nunca usou gerador. Rust e Go também são descida recursiva manual.

O motivo não é performance — parsers LR são rápidos — e não é poder expressivo. É **diagnóstico**. Quando um parser gerado encontra uma célula vazia na tabela, tudo o que ele sabe dizer é "erro de sintaxe no estado 247". Um parser à mão sabe que estava no meio de uma lista de argumentos, pode sugerir a vírgula faltante, apontar o parêntese que abriu 30 linhas acima e **continuar** analisando para reportar os erros seguintes. Numa linguagem moderna, a qualidade das mensagens de erro é um recurso de produto, e ela venceu a elegância da geração automática.

O aviso das notas sobre a prova — "**se vocês colocarem apenas 'ERRO' ou 'ERRO SINTÁTICO', vão perder 1,5**" (Aula 06) — é o mesmo princípio aplicado à avaliação, e agora com justificativa: dizer *o que* se esperava e *onde* é a parte difícil e a parte que vale.

Isso não torna a teoria LR inútil. Ela continua sendo o que permite provar que uma gramática é não-ambígua, continua sendo a base de Bison e dos geradores que rodam em produção, e o vocabulário de *shift*, *reduce* e conflito é como todo mundo discute sintaxe. Mas é honesto saber que o compilador que compila este texto foi escrito à mão.

---
