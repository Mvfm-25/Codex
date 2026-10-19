# Simulado — Análise Semântica
## Tradução Dirigida por Sintaxe · BYACC/J · Tabela de Símbolos · Escopos · Tipos
---
> Baseado em [resumo-analise-semantica](resumo-analise-semantica.md).
> **Estrutura:** 18 questões objetivas + 2 questões práticas.
> A resposta vem logo abaixo de cada questão. A alternativa correta está marcada com ✅ e explicada; as erradas têm o motivo do erro.

---

## Parte A — Questões objetivas

### Questão 1 — Papel da análise semântica

Qual das verificações abaixo **não** é responsabilidade da análise semântica?

- (a) Garantir que uma variável foi declarada antes de ser usada.
- (b) Garantir que uma função foi chamada com o número certo de argumentos.
- (c) Garantir que uma string literal foi fechada com aspas.
- (d) Garantir que os operandos de `*` têm tipos compatíveis.

> [!success] Resposta: ✅ (c)
> **Raciocínio:** cada fase garante uma coisa. O **léxico** cuida de identificadores válidos, **strings fechadas** e caracteres estranhos. O **sintático** cuida da forma. O **semântico** cuida de o programa *fazer sentido*.
> - (a), (b) e (d) são exemplos clássicos de checagem semântica (declarar antes de usar, aridade, tipos), e as duas primeiras **nem podem** ser expressas por uma GLC.
> - (c) é erro **léxico**: o scanner nem consegue formar o token.

---

### Questão 2 — Sintetizado × herdado

Na SDD abaixo, o atributo `L.inh` da produção `D → T L` é:

```
D → T L        { L.inh = T.type }
T → float      { T.type = float }
L → L₁ , id    { L₁.inh = L.inh; addType(id.entry, L.inh) }
L → id         { addType(id.entry, L.inh) }
```

- (a) Sintetizado, pois vem de um filho de `D`.
- (b) Herdado, pois é calculado a partir de um irmão à esquerda (`T`).
- (c) Sintetizado, pois `T.type` é sintetizado.
- (d) Herdado, pois é calculado a partir de um irmão à direita.

> [!success] Resposta: ✅ (b)
> **Raciocínio:** a pergunta é sempre *"quem calcula o atributo e de onde vem a informação?"*. `L.inh` é atribuído **na produção do pai** (`D → T L`) usando o valor do **irmão à esquerda** `T`. Informação que vem do pai ou de um irmão = **herdado**.
> - (a) e (c) erram: o fato de `T.type` ser sintetizado não torna `L.inh` sintetizado. Sintetizado seria um atributo de `D` calculado a partir dos filhos.
> - (d) erra a direção: `T` está à **esquerda** de `L`. Herdar de irmão à direita nem seria L-atribuído.

---

### Questão 3 — Classes de SDD

Assinale a afirmação **correta**:

- (a) Toda SDD L-atribuída também é S-atribuída.
- (b) Uma SDD S-atribuída pode ser avaliada por um percurso pós-ordem e casa naturalmente com parsers LR.
- (c) Em uma SDD L-atribuída, um herdado de `Xᵢ` pode depender de atributos de qualquer irmão, inclusive à direita.
- (d) SDDs S-atribuídas exigem marcadores `M → ε` para serem implementadas no yacc.

> [!success] Resposta: ✅ (b)
> **Raciocínio:** S-atribuída = só sintetizados. Num parser LR o pai é criado **na redução**, depois que todos os filhos já foram reconhecidos, ou seja, em **pós-ordem**. Por isso é o modelo nativo do yacc/BYACC/J.
> - (a) inverte a inclusão: **S ⊂ L**, não o contrário. A SDD do `T'` (com `inh`) é L e não S.
> - (c) é falsa: o "L" vem de *Left*. Só pai e irmãos **à esquerda** (`X₁…Xᵢ₋₁`) são permitidos.
> - (d) é falsa: S-atribuída vira **SDT pós-fixo** "de graça", com ações no fim da regra. Marcadores aparecem com ações **no meio** da regra.

---

### Questão 4 — Avaliando uma SDD L-atribuída

Considere a SDD sem recursão à esquerda:

```
T  → F T'        T'.inh = F.val          T.val  = T'.syn
T' → * F T'₁     T'₁.inh = T'.inh × F.val T'.syn = T'₁.syn
T' → ε           T'.syn = T'.inh
F  → digit       F.val = digit.lexval
```

Para a entrada `2 * 3 * 4`, qual é o valor de `inh` no `T'` que deriva `ε`?

- (a) 2
- (b) 6
- (c) 24
- (d) 4

> [!success] Resposta: ✅ (c)
> **Raciocínio:** o `inh` desce pela direita **acumulando** o produto parcial:
> 1. `F.val = 2` → primeiro `T'.inh = 2`.
> 2. Lê `* 3` → próximo `T'₁.inh = 2 × 3 = 6`.
> 3. Lê `* 4` → próximo `T'₁.inh = 6 × 4 = 24`.
> 4. Esse último `T'` deriva `ε` → `syn = inh = 24`, que sobe até `T.val = 24`.
>
> - (a) é o `inh` do primeiro `T'`; (b) é o do segundo. (d) é só o último dígito.

---

### Questão 5 — Esquema de tradução (SDT)

Com o SDT abaixo, qual é a saída para a entrada `1+2-3`?

```
E → E + T   { print('+') }
E → E - T   { print('-') }
E → T
T → 0 { print('0') } | ... | 9 { print('9') }
```

- (a) `+-123`
- (b) `12+3-`
- (c) `123+-`
- (d) `1+2-3`

> [!success] Resposta: ✅ (b)
> **Raciocínio:** a gramática é recursiva à esquerda, então agrupa `(1+2)-3`. A ação do operador está **no fim** da produção, logo só roda **depois** dos dois operandos (percurso pós-ordem):
> - `T→1` imprime `1`; `T→2` imprime `2`; reduz `E → E + T` imprime `+` → `12+`
> - `T→3` imprime `3`; reduz `E → E - T` imprime `-` → `12+3-`
>
> - (a) seria pré-fixa (ações no início). (c) agruparia `1+(2-3)` de forma errada. (d) é a própria infixa.

---

### Questão 6 — Pseudovariáveis do BYACC/J

Na regra `exp : exp '+' exp { $$ = $1 + $3; }`, o código Java gerado para `$1` é:

- (a) `val_peek(0)`
- (b) `val_peek(1)`
- (c) `val_peek(2)`
- (d) `val_peek(3)`

> [!success] Resposta: ✅ (c)
> **Raciocínio:** a fórmula é `$k → val_peek(n - k)`, onde `n` é o tamanho do corpo e `val_peek(i)` é `i` posições abaixo do topo. Aqui `n = 3` e `k = 1` → `val_peek(3 - 1) = val_peek(2)`.
> - (a) `val_peek(0)` é o topo = `$3`.
> - (b) `val_peek(1)` é o `'+'` = `$2`.
> - (d) `val_peek(3)` = `val_peek(n)` = **`$0`**, o símbolo logo **abaixo** do corpo.

---

### Questão 7 — Ação padrão

Um aluno escreveu a regra `exp : '(' exp ')' ;` **sem ação**. O que acontece ao avaliar `(5)`?

- (a) O valor de `exp` é 5, pois o BYACC/J propaga automaticamente o não-terminal do meio.
- (b) Erro de compilação no BYACC/J: toda regra precisa de ação.
- (c) O valor de `exp` passa a ser o valor associado ao `'('`, e não 5.
- (d) Conflito shift/reduce.

> [!success] Resposta: ✅ (c)
> **Raciocínio:** antes de qualquer ação, o gerador faz a **ação padrão `$$ = $1`**. O `$1` aqui é o token `'('`, cujo valor na pilha é "lixo" (sem valor útil). Por isso a regra **precisa** de `{ $$ = $2; }`.
> - (a) é exatamente o equívoco que a ação padrão causa: ela copia o **primeiro** símbolo, não o "mais importante".
> - (b) é falsa: regras sem ação são válidas (usam a padrão).
> - (d) não tem relação: a regra não cria conflito.

---

### Questão 8 — Precedência e associatividade

Com as declarações abaixo, quanto valem `2 ^ 3 ^ 2` e `-2 ^ 2`, respectivamente?

```
%left  '+' '-'
%left  '*' '/'
%left  NEG
%right '^'
%%
exp : '-' exp %prec NEG { $$ = -$2; } | exp '^' exp { $$ = Math.pow($1, $3); } | ...
```

- (a) 64 e 4
- (b) 512 e 4
- (c) 512 e −4
- (d) 64 e −4

> [!success] Resposta: ✅ (c)
> **Raciocínio:**
> - `^` é `%right` → `2^(3^2) = 2^9 = 512`. Se fosse `%left`, daria `(2^3)^2 = 64`.
> - `^` está declarado **depois** de `NEG`, então tem precedência **maior** → `-(2^2) = -4`. O menos unário só se aplica depois da potência.
>
> - (a) e (d) erram a associatividade (64). (a) e (b) erram a precedência entre `NEG` e `^` (fazendo `(-2)^2 = 4`).

---

### Questão 9 — Herdados em parsers LR

Por que atributos herdados são difíceis de implementar num parser LR (como o do BYACC/J)?

- (a) Porque o LR não possui pilha de valores.
- (b) Porque o nó pai só é criado na redução, depois que todos os filhos foram reconhecidos.
- (c) Porque o LR lê a entrada da direita para a esquerda.
- (d) Porque o yacc não permite variáveis globais no parser.

> [!success] Resposta: ✅ (b)
> **Raciocínio:** herdado = informação que vem do pai (ou de irmão). No LR, enquanto os filhos são processados o **pai ainda não existe**: ele nasce no *reduce*. As saídas práticas são: (1) reescrever como sintetizado (lista), (2) usar `$0`, (3) estado global.
> - (a) é falsa: existe a pilha de valores (`ParserVal[]`), andando junto com a de estados.
> - (c) é falsa: o LR lê da esquerda para a direita (o "L" de LR).
> - (d) é falsa: estado global é justamente uma das soluções (ex.: `tipoAtual`, `mem`).

---

### Questão 10 — O truque do `$0`

Na gramática abaixo, por que `$<sval>0` em `lista : lista ',' ID` sempre devolve o tipo declarado?

```
decl  : tipo lista ';' ;
tipo  : INT { $$ = "int"; } | FLOAT { $$ = "float"; } ;
lista : lista ',' ID  { addType($3, $<sval>0); }
      | ID            { addType($1, $<sval>0); } ;
```

- (a) Porque `$0` sempre aponta para o primeiro símbolo da pilha.
- (b) Porque `lista` sempre aparece logo depois de `tipo` na gramática, então `tipo` está sempre imediatamente abaixo do corpo sendo reduzido.
- (c) Porque o BYACC/J copia automaticamente atributos de `decl` para `lista`.
- (d) Porque `$0` é sinônimo de `$$`.

> [!success] Resposta: ✅ (b)
> **Raciocínio:** `$0 = val_peek(n)` = a entrada **logo abaixo** do handle. Como `lista` só aparece depois de `tipo`, não importa quantos `, ID` a lista acumule: ao reduzir `lista`, o que está imediatamente abaixo é sempre o `tipo`. O `<sval>` é obrigatório porque o BYACC/J não sabe o tipo de `$0` (ele não pertence à produção).
> - (a) é falsa: `$0` é relativo ao topo, não ao fundo da pilha.
> - (c) é falsa: não existe essa cópia automática; é só aritmética de posição.
> - (d) é falsa: `$$` é a **cabeça** sendo reduzida (`yyval`).
>
> ⚠️ Se `lista` aparecesse em outro contexto sem `tipo` antes, `$0` pegaria lixo.

---

### Questão 11 — Ação no meio da regra

O que o BYACC/J faz com `bloco : '{' { abreEscopo(); } comandos '}' ;`, e qual o risco?

- (a) Move a ação para o fim da regra; não há riscos.
- (b) Cria um marcador vazio `M → ε` com a ação; o marcador pode gerar conflitos que a gramática original não tinha.
- (c) Executa a ação durante o shift do `'{'`; pode gerar erro léxico.
- (d) Ignora a ação, pois o yacc só aceita ações no fim.

> [!success] Resposta: ✅ (b)
> **Raciocínio:** no LR, ações só rodam em **reduções**. Para executar algo no meio, o gerador transforma a regra em `bloco : '{' M comandos '}'` com `M → ε { abreEscopo(); }`. Esse marcador obriga o parser a decidir **mais cedo** se reduz `M`; se ainda houver caminhos alternativos naquele ponto, surge conflito. Atenção também à numeração: a ação conta como símbolo, então `comandos` vira `$3`.
> - (a) mudaria a semântica: o escopo seria aberto só depois dos comandos.
> - (c) é falsa: shift nunca executa ação semântica.
> - (d) é falsa: ações no meio são aceitas.

---

### Questão 12 — Dangling else

Para a gramática `C → if E C | if E C else C | o`, sem nenhuma declaração de precedência, o BYACC/J:

- (a) Rejeita a gramática por ser ambígua.
- (b) Reporta 1 conflito shift/reduce e escolhe **reduce**, associando o `else` ao `if` mais externo.
- (c) Reporta 1 conflito shift/reduce e escolhe **shift**, associando o `else` ao `if` mais próximo.
- (d) Reporta 1 conflito reduce/reduce.

> [!success] Resposta: ✅ (c)
> **Raciocínio:** no estado com `C → if E C .` e `C → if E C . else C`, com `else` à frente, a tabela tem duas opções: **shift** (o `else` é do `if` de dentro) ou **reduce** pela regra 1 (o `else` é do de fora). O padrão do yacc é **shift**, que é o comportamento de C/Java/Pascal. Para tirar o aviso: `%nonassoc IFX` antes de `%nonassoc ELSE` e `%prec IFX` na regra sem else; como `ELSE` tem precedência maior que a regra, ganha o shift.
> - (a) é falsa: yacc gera o parser mesmo com conflitos, só avisa.
> - (b) inverte o padrão.
> - (d) é falsa: o conflito é entre empilhar e reduzir, não entre duas reduções.

---

### Questão 13 — Escopo estático × dinâmico

```c
int a = 1;
void g() { print(a); }
void h() { int a = 5; g(); }
h();
```

O que é impresso com escopo **estático** e com escopo **dinâmico**, respectivamente?

- (a) 1 e 1
- (b) 5 e 5
- (c) 1 e 5
- (d) 5 e 1

> [!success] Resposta: ✅ (c)
> **Raciocínio:**
> - **Estático** olha o **texto**: `g` foi escrita no nível global, onde o único `a` visível é o global → **1**, independente de quem chamou.
> - **Dinâmico** olha a **pilha de chamadas**: `[global(a=1), h(a=5), g]`. Buscando `a` de cima para baixo: `g` não tem, `h` tem `a = 5` → **5**.
>
> - (d) troca os dois conceitos. (a) e (b) ignoram que os modelos dão resultados diferentes aqui.

---

### Questão 14 — `buscaLocal` × `busca`

No verificador Mini, ao declarar um nome, `declara()` chama `buscaLocal` e depois `busca`. Qual o resultado de cada caso?

- (a) `buscaLocal` achou → aviso; `busca` achou em escopo externo → erro.
- (b) `buscaLocal` achou → erro (redeclaração); `busca` achou em escopo externo → aviso (ocultação).
- (c) Ambos geram erro.
- (d) Ambos geram aviso.

> [!success] Resposta: ✅ (b)
> **Raciocínio:** `buscaLocal` procura **só no topo** (escopo corrente). Achar ali é declarar duas vezes no mesmo escopo → **erro**. `busca` procura do topo à base; achar só num escopo **externo** é *shadowing*, que é **legal** → apenas **aviso**.
> - (a) inverte os casos. (c) proibiria a ocultação, que a linguagem permite. (d) deixaria passar redeclaração.

---

### Questão 15 — Equivalência de tipos

```pascal
type curto = array[1..5] of integer;
var a : array[1..5] of integer;
    b : curto;
    c : array[1..10] of integer;
```

Quais pares são equivalentes por **nome** e por **estrutura**?

- (a) `a,b`: nome ✔, estrutura ✔ · `a,c`: nome ✘, estrutura ✔
- (b) `a,b`: nome ✘, estrutura ✔ · `a,c`: nome ✘, estrutura ✘
- (c) `a,b`: nome ✘, estrutura ✘ · `a,c`: nome ✘, estrutura ✔
- (d) `a,b`: nome ✔, estrutura ✘ · `a,c`: nome ✔, estrutura ✘

> [!success] Resposta: ✅ (b)
> **Raciocínio:**
> - `a` tem um tipo **anônimo** e `b` tem o tipo **`curto`**: nomes diferentes → por nome ✘. Mas as duas árvores de tipo são `array(1..5, integer)` → estrutural ✔.
> - `a` e `c` têm tamanhos diferentes (5 × 10) → as árvores **não** coincidem → estrutural ✘ (e por nome também ✘).
>
> - (a) e (c) dão `a,c` estruturalmente iguais, ignorando o tamanho do arranjo. (d) dá equivalência por nome a tipos distintos.

---

### Questão 16 — Tipo erro (⊥)

Qual é a função do tipo `⊥` (`Tipo.ERRO`) num verificador de tipos?

- (a) Representar o tipo de expressões `void`.
- (b) Evitar erros em cascata: como `⊥ ≤ A` para todo `A`, regras que recebem `⊥` não emitem novas mensagens.
- (c) Abortar a compilação no primeiro erro.
- (d) Indicar que a expressão precisa de coerção para `double`.

> [!success] Resposta: ✅ (b)
> **Raciocínio:** quando um erro é detectado, a expressão recebe `⊥`. Como `⊥` "cabe" em qualquer tipo, quem o recebe aceita em silêncio. Assim, `((x == y) > 5 && ...) || ...` gera **uma** mensagem, não três. No Mini, `atribuivelA` retorna `true` se algum lado é `ERRO`.
> - (a) é falsa: `void` é um tipo próprio (`Tipo.VOID`).
> - (c) é o oposto: a ideia é **reportar e continuar**.
> - (d) não tem relação: coerção é `int → double` via `≤`.

---

### Questão 17 — Sobrecarga

```java
void f(Base a, Base b);
void f(Derived a, Base b);
void f(Base a, Derived b);
f(new Derived(), new Derived());
```

Sendo `Derived ≤ Base`, qual é o resultado da resolução da chamada?

- (a) Escolhe `f(Base, Base)`, a mais geral.
- (b) Escolhe `f(Derived, Base)`, a primeira mais específica declarada.
- (c) Chamada ambígua.
- (d) Nenhuma candidata; erro de tipo.

> [!success] Resposta: ✅ (c)
> **Raciocínio:**
> 1. **Filtro:** as três aceitam `(Derived, Derived)` → três candidatas.
> 2. Procura-se uma que seja `<:` (mais específica que) **todas** as outras.
> 3. `(Derived, Base)` é mais específica no 1º parâmetro; `(Base, Derived)`, no 2º → **incomparáveis**. Nenhuma vence as duas → **ambígua**.
> 4. Correção: adicionar `f(Derived, Derived)`, que é `<:` todas.
>
> - (a) é o contrário da regra (busca-se a **mais específica**). (b) inventa um critério de ordem de declaração. (d) é falsa: há três candidatas.

---

### Questão 18 — Sobrescrita e variância

Qual sobrescrita é **segura** em termos de tipos?

- (a) `Base clone()` na superclasse sobrescrito por `Derived clone()` na subclasse.
- (b) `boolean equalTo(Base o)` sobrescrito por `boolean equalTo(Derived o)`.
- (c) Atribuir `A[] arr = new B[10]` e depois `arr[0] = new A()`, com `B extends A`.
- (d) `Derived make()` na superclasse sobrescrito por `Base make()` na subclasse.

> [!success] Resposta: ✅ (a)
> **Raciocínio:** regra de ouro: **covariante no que devolve, contravariante no que recebe**. Devolver um tipo mais específico (`Derived` onde se esperava `Base`) nunca quebra quem chama, pois `Derived ≤ Base`.
> - (b) torna o parâmetro mais específico (covariante): quem chama via `Base` pode passar um `Base` qualquer, que a versão sobrescrita não aceita.
> - (c) é a covariância de arranjos de Java: compila, mas lança `ArrayStoreException` em execução.
> - (d) generaliza o retorno: quem esperava `Derived` pode receber um `Base`.

---

## Parte B — Questões práticas

### Prática 1 — Calculadora em BYACC/J e a pilha de valores

Considere a calculadora:

```
%token NL
%token <dval> NUM
%type  <dval> exp
%left '+' '-'
%left '*' '/'
%left NEG
%%
linha : exp NL          { System.out.println(" = " + $1); } ;
exp : NUM               { $$ = $1; }
    | exp '+' exp       { $$ = $1 + $3; }
    | exp '-' exp       { $$ = $1 - $3; }
    | exp '*' exp       { $$ = $1 * $3; }
    | exp '/' exp       { $$ = $1 / $3; }
    | '-' exp %prec NEG { $$ = -$2; }
    | '(' exp ')'       { $$ = $2; }
    ;
```

**a)** Rastreie a **pilha de símbolos**, a **pilha de valores** e a **ação** (shift/reduce) para a entrada `8 - 2 * 3 NL`.

**b)** Explique o passo em que o parser tem `exp - exp` no topo e `*` na entrada. Que conflito existe ali, como ele é resolvido e qual seria o resultado errado?

**c)** Modifique a gramática para que as ações construam uma **AST** (`Num`, `Neg`, `BinOp`) em vez de calcular números. Indique a mudança no `%type`.

> [!success] Resposta
> **a) Rastreamento** ("–" = token sem valor útil):
>
> | # | Pilha de símbolos | Pilha de valores | Ação |
> |---|---|---|---|
> | 1 | `$` | | shift `NUM` (`yylval = 8`) |
> | 2 | `$ NUM` | `8` | reduce `exp → NUM` (`$$ = $1 = 8`) |
> | 3 | `$ exp` | `8` | shift `-` |
> | 4 | `$ exp - NUM` | `8 – 2` | reduce `exp → NUM` |
> | 5 | `$ exp - exp` | `8 – 2` | **shift `*`** (prec `*` > `-`) |
> | 6 | `$ exp - exp * NUM` | `8 – 2 – 3` | reduce `exp → NUM` |
> | 7 | `$ exp - exp * exp` | `8 – 2 – 3` | reduce `exp → exp * exp` (`$$ = 2 * 3 = 6`) |
> | 8 | `$ exp - exp` | `8 – 6` | reduce `exp → exp - exp` (`$$ = 8 - 6 = 2`) |
> | 9 | `$ exp` | `2` | shift `NL`; reduce `linha → exp NL` → imprime ` = 2.0` |
>
> **Raciocínio:**
> - **Shift** só empilha estado + `yylval`; **nenhuma ação semântica roda**. As ações rodam apenas nos **reduces**.
> - Em cada reduce, as `n` entradas do handle saem e uma entra com o `$$`. No passo 7: `$1 = 2`, `$3 = 3`, três entradas saem e `exp(6)` entra.
> - A ordem das reduções (`8`, `2`, `3`, `*`, `-`) é um **percurso pós-ordem** da árvore → a SDD é S-atribuída e o LR a avalia naturalmente.
>
> **b) O momento crítico (passo 5):** o topo `exp - exp` **já casa** com `exp → exp - exp`, então o parser poderia reduzir. Mas o próximo token é `*`, que também pode ser empilhado. É um **conflito shift/reduce** na tabela Action. O BYACC/J compara a precedência da **regra** (a de `-`, linha `%left '+' '-'`) com a do **token** (`*`, linha `%left '*' '/'`). Como `*` foi declarado **depois**, tem precedência maior → **shift**. Se reduzisse, calcularia `(8 - 2) * 3 = 18`, resultado errado. O correto é `8 - (2 * 3) = 2`.
>
> **c) Construindo AST:**
> ```
> %type <obj> exp                       /* antes era <dval>: agora o atributo é um nó */
> %%
> linha : exp NL          { raiz = (Expr) $1; } ;
> exp : NUM               { $$ = new Num($1); }                         // folha
>     | exp '+' exp       { $$ = new BinOp('+', (Expr)$1, (Expr)$3); }
>     | exp '-' exp       { $$ = new BinOp('-', (Expr)$1, (Expr)$3); }
>     | exp '*' exp       { $$ = new BinOp('*', (Expr)$1, (Expr)$3); }
>     | exp '/' exp       { $$ = new BinOp('/', (Expr)$1, (Expr)$3); }
>     | '-' exp %prec NEG { $$ = new Neg((Expr)$2); }
>     | '(' exp ')'       { $$ = $2; }                                  // parênteses somem
>     ;
> ```
> **Raciocínio:**
> - O campo muda de `dval` para `obj` porque o valor sintetizado agora é um **nó**, não um número. Como `obj` é `Object`, é preciso **cast** `(Expr)`. Alternativa sem casts: `byaccj -J -Jsemantic=Expr`.
> - `NUM` vira folha `Num`; os parênteses **não geram nó** (`$$ = $2`), porque a precedência já fica codificada na forma da árvore.
> - A sequência de reduções é a mesma de (a). Para `8 - 2 * 3`, o resultado é `BinOp('-', Num(8), BinOp('*', Num(2), Num(3)))`.
> - Continua sendo **S-atribuída**: o atributo de cada `exp` só depende dos filhos.

---

### Prática 2 — Verificador Mini: tabela de símbolos, escopos e tipos

Considere o programa abaixo, analisado pelo verificador Mini (pilha de `LinkedHashMap`, coerção implícita só `int → double`, `corpo` de função no **mesmo** escopo dos parâmetros, `bloco` abre escopo novo). A versão do verificador **não** tem a melhoria C5.

```c
 1  int x;
 2  bool flag;
 3  int dobro(int n) {
 4      return n * 2;
 5  }
 6  void main() {
 7      double x;
 8      int k;
 9      k = 0;
10      x = k;
11      k = x;
12      flag = dobro(k) > 3;
13      while (k) {
14          int k;
15          k = dobro(1, 2);
16      }
17      z = z + 1;
18      if (flag) return 1;
19      break;
20  }
```

**a)** Liste, linha por linha, os **erros** e **avisos** emitidos e explique cada um usando as funções do verificador (`declara`, `usaVar`, `atribuivelA`, `chama`, `checaCond`, `checaReturn`, contador `laco`).

**b)** Desenhe a **pilha de escopos** no momento em que a linha 15 é analisada e diga a qual declaração cada nome dessa linha se refere.

**c)** Na linha 17, quantas mensagens são emitidas? Escreva a alteração em `usaVar` (melhoria C5) que reduz isso e explique por que funciona.

> [!success] Resposta
> **a) Mensagens:**
>
> | Linha | Código | Mensagem | Por quê |
> |---|---|---|---|
> | 7 | `double x;` | **aviso:** `'x' oculta a declaração da linha 1` | `buscaLocal("x")` no escopo de `main` não acha nada → não é redeclaração. `busca("x")` acha o global e `nivel() > 0` → só aviso (ocultação é legal). |
> | 10 | `x = k;` | *(nenhuma)* ✔ | `x` agora é o `double` da linha 7; `INT.atribuivelA(DOUBLE)` → coerção `int → double` permitida. |
> | 11 | `k = x;` | **erro:** `tipos incompatíveis na atribuição a 'k': esperado int, encontrado double` | `DOUBLE ≤ INT`? Não. Seria **estreitamento**, que não é implícito. |
> | 12 | `flag = dobro(k) > 3;` | *(nenhuma)* ✔ | `dobro(k) : int` (aridade e argumento OK); `int > int` → `bool`; `flag : bool`. |
> | 13 | `while (k)` | **erro:** `condição deve ser bool, encontrado int` | `checaCond(INT)`: não é `ERRO` e não é `BOOL`. Em seguida `laco++` (vira 1). |
> | 14 | `int k;` | **aviso:** `'k' oculta a declaração da linha 8` | O `bloco` abriu escopo novo (nível 2): `buscaLocal` falha, `busca` acha o `k` de `main`. |
> | 15 | `k = dobro(1, 2);` | **erro:** `'dobro' espera 1 argumento(s), recebeu 2` | `chama`: existe ✔, é função ✔, aridade ✘. Mas **devolve `f.tipo = INT`** (a assinatura é conhecida), então a atribuição `int = int` **não** gera segunda mensagem. |
> | 16 | `}` | *(fecha bloco; `laco--` → 0)* | O símbolo `k@14` é descartado. |
> | 17 | `z = z + 1;` | **erro (2×):** `identificador 'z' não declarado` | Ver item (c). |
> | 18 | `return 1;` | **erro:** `função void não pode retornar valor` | `checaReturn(INT)` com `funcAtual.tipo == VOID` e `t != null`. |
> | 19 | `break;` | **erro:** `'break' fora de um laço` | O `while` terminou na linha 16 e fez `laco--` → `laco == 0`. |
>
> **Total:** 7 erros (linhas 11, 13, 15, 17 duas vezes, 18, 19) e 2 avisos (linhas 7 e 14).
>
> **b) Pilha na linha 15:**
> ```
>   topo → │ bloco (nível 2)          k : int @14             │  ← k resolve aqui
>          │ função main (nível 1)    x : double @7           │
>          │                          k : int @8   (oculto)   │
>          │ global (nível 0)         x : int @1   (oculto)   │
>          │                          flag : bool @2          │
>          │                          dobro : [int] -> int    │  ← dobro resolve aqui
>          │                          main : [] -> void       │
> ```
> - `k` → **`k@14`**: `busca` começa no topo e para na primeira ocorrência (regra do aninhamento mais próximo). O `k@8` está oculto.
> - `dobro` → **declaração da linha 3**, no escopo global. A função foi inserida no global **antes** do corpo (`abreFuncao`), por isso também é visível em `main` e permitiria recursão dentro de `dobro`.
> - Observação: o escopo da função `dobro` (com `n`) **já foi fechado** na linha 5; ele não está na pilha. A pilha contém exatamente os escopos **abertos**.
>
> **c) Linha 17 — duas mensagens.** A expressão do lado direito é reduzida primeiro: `usaVar("z")` → `busca` retorna `null` → **erro 1** e devolve `ERRO`. `aritmetico(ERRO, INT)` devolve `ERRO` em silêncio. Depois, `atribui` chama `usaVar("z")` de novo para o alvo → **erro 2**. A checagem final `ERRO.atribuivelA(ERRO)` é `true`, então não vem uma terceira.
>
> **Melhoria C5:** ao encontrar um nome não declarado, inseri-lo na tabela com tipo `ERRO`:
> ```java
> Tipo usaVar(String nome) {
>     Simbolo s = ts.busca(nome);
>     if (s == null) {
>         erro("identificador '" + nome + "' não declarado");
>         ts.insere(new Simbolo(nome, VAR_LOCAL, Tipo.ERRO, ts.nivel(), linha()));  // ★
>         return Tipo.ERRO;
>     }
>     return s.tipo;
> }
> ```
> **Por que funciona:** no segundo uso de `z` (o alvo da atribuição, ou qualquer uso posterior no mesmo escopo), `busca("z")` encontra o símbolo "falso" com tipo `ERRO`. Como `⊥ ≤ tudo`, nenhuma regra reclama → **uma mensagem só por nome não declarado**. Quando o escopo fecha, o símbolo falso é descartado junto, sem contaminar outras funções. Com a melhoria, o total cai para **6 erros**.
