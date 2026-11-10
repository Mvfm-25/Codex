# Construção de Compiladores
## [09-11][mvfm]
---
### Atividade em Grupo para geração de código
- Traduzindo :
```code
while a > 0
    if (a % 2 == 0)
        a = a / 2
    else a = a -1
```
- É o mesmo (?) que está acontecendo aqui.
```code
R001 : NOP
    lda _a
    ldc 0

    les
    jzer R002
    |--------
    |E1
    |   LDC 2
    |   MOD
    |   LDC 0
    |   E2
    |--------
    |JZER R003
    |---------
    |   LDA _a
    |   LDC 2
    |   DIV
    |---------
    |   JMP R004
    |R003 : NOP
    |---------
    |   a = a 1
    |---------
    |R004 : NOP
        jmp R001
R002 : NOP
```
- "*O formato do código não depende do que está dentro de $E_1$, $C_1$ & $C_2$.*"
- "*A condição é testada no topo do laço; quando falsa, JZER salta para o rótulo de saída.*"
![Rótulos & Aninhamento](assets/rotulos_aninhamento.png)
- Estamos usando 4 rótulos pois estamos usando um compilador de passagem única, então ele tem que estar escrevendo o tempo todo.
- Exercício em grupo aparentemente foi movido para aula que vem, durante a aula agora.

### Ações no Meio da Regra & Conflitos
- "*Por que não escrever simplesmente duas produções para o if?*"
```code
cmd : IF exp THEN {A} cmd
    | IF exp THEN {A} cmd ELSE cmd
    ;
```
    - O BYACC/J transforma cada ação no meio em um não terminal não vazio $$n, $$1 & $$2 nesse caso.
    - Logo depois de 'THEN' ele precisa reduzir $$1 ou $$2, mas só saberia qual quando (e se) chegasse o ELSE.
- Solução :
    - Fatorar o prefixo comum : *IF exp THEN {A} cmd restoIF*
    - A decisão (else ou não) passa para o *restoIF*, depois de $C_1$.
    - Mesma técnica de fatoração à esquerda da análise descendente.
![Comandos de Controle](assets/comandos_controle.png)
- Material base está [aqui](atividades/Geracao_Codigo_Maquina_Pilha.pptx). Não vamos ver Subprogramas hoje, aparentemente.

### Lendo código do Claude
```
[...]
|TRUE       PUSHL $1
[...]
```
- Só estou 'empurrando' um Long constante 1 para representar o true.
- Em outro exemplo :
```code
exp     : NUM                              { gera("PUSHL $%s", $1); }       
```
- Eu estaria simplesmente empurrando o valor %s para $1.
    - Esse código é diretamente retirado desse [código](./atividades/exemploGC_inicial_262/exemploGC.y)
