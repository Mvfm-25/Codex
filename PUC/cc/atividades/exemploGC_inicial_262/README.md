# exemploGC — código inicial 2026/2 (C-- → x86 32 bits)

Gerador de código em **uma passagem** (BYACC/J + JFlex) da linguagem C-- para
**x86 de 32 bits**, usando a pilha do processador como máquina de pilha.
Não usa bibliotecas externas: a mini biblioteca de E/S (`__read`, `__write`,
`__writeLit`, `__writeln`) é anexada a todo programa gerado.

Este é o **ponto de partida do trabalho**: a análise sintática e semântica da
linguagem está completa, e a geração de código cobre a parte "sem funções".
Os pontos a completar estão marcados com `TODO (alunos)` em `exemploGC.y`.

## A linguagem C-- desta versão

```c
int total;                      // globais: int e bool
bool achou;

int soma(int a, int b) {        // funções: parâmetros por valor, locais no início
    int s;                      //   do corpo (não há variáveis de bloco)
    s = a + b;
    return s;
}

void main() {
    total = 0;                  // atribuição é um COMANDO (como em Pascal)
    while (total < 10) {        // único laço: while
        if (total % 2 == 0) write("par: ", total);
        else                write(total);
        total = total + 1;
    }
    read(total);
}
```

| Construção | Situação |
|---|---|
| globais `int`, `bool`; `float` é reconhecido e rejeitado | gera código |
| `+ - * / %`, menos unário, `< > <= >= == !=`, `&& \|\| !`, `c ? a : b` | gera código |
| atribuição `x = e;` — **comando**, não expressão | gera código |
| `if` / `else`, `while`, bloco `{ }`, comando vazio `;` | gera código |
| `write("texto")`, `write(e)`, `write("texto", e)`, `read(x)` | gera código |
| `return;` na `main` (encerra o programa) | gera código |
| funções, parâmetros, variáveis locais, chamadas, `return` | **verificação semântica pronta; geração: TODO (alunos)** |
| `for`, `do-while`, `break`, `continue`, `++`, `--`, `+=`, atribuição em expressão | **não existem** (erro sintático) |

Quando o programa usa uma construção cuja geração ainda não existe, o compilador
informa, uma única vez por assunto:

```
Erro: geracao de codigo nao implementada: funcoes (prologo, epilogo, chamada e retorno)  linha: 3
Erro: geracao de codigo nao implementada: acesso a parametros e variaveis locais  linha: 3
```

## Organização

| Arquivo | Papel |
|---|---|
| `exemploGC.y` | gramática com ações curtas que chamam métodos; seção de código: 1 infraestrutura, 2 tabela de símbolos e verificações, 3 expressões, 4 comandos e controle, **5 funções e chamadas (TODO)**, 6 início/fim do `.s` |
| `exemploGC.flex` | analisador léxico (JFlex `%byaccj`) |
| `ClasseID.java` | `VarGlobal`, `VarLocal`, `NomeParam`, `NomeFuncao` |
| `TS_entry.java` | entrada da TS: tipo, classe, deslocamento; para funções, parâmetros e nº de locais. `getOperando()` devolve `_x` ou `d(%EBP)` |
| `TabSimb.java` | dois níveis: global e o da função em análise |
| `BibliotecaIO.java` | texto assembly da biblioteca de E/S e da finalização do programa |
| `testa.sh` | executa e compara os exemplos (usado pelo `Makefile`) |

## O que falta implementar (TODO alunos)

A tabela de símbolos **já calcula** os deslocamentos de parâmetros e locais
(`fixaDeslocParams`, `declaraVar`). Registro de ativação sugerido:

```
   8+4*(n-1-i)(%EBP)   parâmetro i (0..n-1) — empilhados da esquerda p/ a direita
   4(%EBP)             endereço de retorno (CALL)
   0(%EBP)             %EBP do chamador
  -4*k(%EBP)           variável local k (1..m)
```

1. **Prólogo** (`geraPrologo`): `PUSHL %EBP` · `MOVL %ESP, %EBP` · `SUBL $4m, %ESP`
   (na `main`, que é `_start`, basta `MOVL %ESP, %EBP` e reservar os locais).
2. **Epílogo** (`geraEpilogo`): `_fim_f:` · `MOVL %EBP, %ESP` · `POPL %EBP` · `RET`.
3. **Retorno** (`gcReturn`): `POPL %EAX` (se houver valor) · `JMP _fim_f`.
4. **Chamada** (`gcChamada`): argumentos já empilhados · `CALL _f` · `ADDL $4n, %ESP`
   · em expressão, `PUSHL %EAX`.
5. **Parâmetros e locais** (`acessoImplementado`, `gcRead`): usar `v.getOperando()`;
   no `read`, empilhar o endereço com `LEAL d(%EBP), %EAX` · `PUSHL %EAX`.

## Uso

```
make                         # gera Parser.java e Yylex.java e compila
./run.x exemplos/ok/t05_while.cmm
./run.x exemplos/ok/t07_leitura.cmm < exemplos/ok/t07_leitura.entrada
make teste                   # exemplos/ok      : executa e compara com .esperado
make teste-erros             # exemplos/erros   : mensagens de erro esperadas
make teste-funcoes           # exemplos/funcoes : objetivo do trabalho
make testes                  # os três
```
Montar e executar exige Linux x86 ou x86-64 (`as --32`, `ld -m elf_i386`).
No `Makefile`, troque `BYACCJ` para `./yacc.linux -tv -J` se não houver `byaccj` instalado.

## Exemplos

| Pasta | Conteúdo | Hoje |
|---|---|---|
| `exemplos/ok` | `t01` aritmética · `t02` relacionais e lógicos · `t03` atribuição como comando · `t04` if/else e else pendente · `t05` while simples/aninhado · `t06` write · `t07` read · `t08` `?:` · `t09` Collatz · `t10` primos e MDC | 10/10 ok |
| `exemplos/erros` | `e01`–`e09`: atribuição em expressão, atribuição encadeada, `++`, `+=`, `for`, `do-while`, `break`, `continue`, expressão como comando · `es01`: erros semânticos | 10/10 ok |
| `exemplos/funcoes` | `f01` fatorial · `f02` Fibonacci com locais · `f03` vários parâmetros e chamadas aninhadas · `f04` Hanói (void, chamada como comando) · `f05` locais na main com `read` | 0/5 — **objetivo** |

Cada `prog.cmm` tem `prog.esperado` (saída do programa, ou mensagens de erro do
compilador) e, se lê dados, `prog.entrada`. Os `.esperado` de `exemplos/funcoes`
são a saída correta depois de implementada a geração de funções.

Observação: `es01_semanticos.esperado` inclui hoje as duas linhas
"geracao de codigo nao implementada"; depois de implementar as funções, elas
deixam de aparecer e o arquivo esperado deve ser atualizado (`make teste-erros`
indicará a diferença).
