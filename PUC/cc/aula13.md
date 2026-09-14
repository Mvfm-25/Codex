# Construção de Compiladores
## [14/09/26][mvfm]
---
### Análise Sintática Ascendente
- Conceitos fundamentais incluem : **Shift-Reduce, Automatos LR & Geração de Tableas SLR(1) LR(1) LALR(1)
- Como funciona a Análsie Ascendente?
    - Do topo para a base, o fundamental contrário da descendente :
        - **Parte das folhas, reconhece handles e reduz até chegar em S**
    - Um parser ascendente parte da cadeia de tokens (folhas) e constrói a árvore de derivação de baixo para cima, até chergar no símbolo inicial.
    - '*A cada passo, procura na pilha uma sequência que corresponda ao lado direito de alguma produção e a substitui (reduz) pela não terminal do lado esquerdo*'
    - SLR reconhce pouca coisa muita ruim, mas o CLR é coisa demais muitos estados. LALR é o sweet spot descrito pelo Agustini.

### Exemplo Prático : Expressõe de uma calculadora.
    ```code
        S -> E
        E -> E + T
            | T
        T -> (E)
            | NUM
    ```
- ![Tabela Ascendente](assets/tabelaAscendente.png)
- Por que isso é ascendente?
    - Cada linha da tabela é um passo na pilha, árvore montada de baixo para cima.
    - 'shift' empurra o próximo token do léxico para a pilha
    - "*reduce X -> a" substitui *a* (topo da pilha) pelo não-terminal X.
    - Quando a pilha contém só o símbolo incial e a entrada acabou : sentença aceita

### Conflitos Shift-Reduce & Reduce-Reduce.
-  Gramática if/else (dangling else)
    ```code
        S -> if E then S
            | if E then S else S
    ```
- Ao chegar em "if E then if E then S" com else no lookaheadm, o parser pode reduzir (fechando of If interno) ou empilhar o else (shift)
- Ambas são válidas, mas geram árvores notavelmente diferentes. 
- Convenção usual : 
    - **O else se liga ao if** mais próximo. Usado em C, Java, Javascript
- Em linguagens lidamos com isso de maneiras um pouco diferentes :
    1. Python obriga blocos por identação
    2. Kotlin, Swift & Go exigem chaves sempre.
    3. Reduce-Reduce (mais raro) geralmente aponta um erro de projeto na gramática.

### Pontos, Closure & Go-To
- Um item LR(0) é uma produção da gramática com um ponto (●) marcando até onde já reconhecemos o lado direto.
- Tudo à esquerda já está na pilha, o pós-ponto é o que ainda esperamos ver na pilha.
    - Ponto no fim da produção significa que o handle inteiro tá na pilha. Reduzimos agora.
    - ![Por pontos](assets/pontos.png)
- '*closure*' adiciona, para cada não-terminal logo após o ponto, todas as suas produções com o ponto no início. "*O que pode vir a seguir*"
- goTo(I, X) avança o ponto sobre o símbolo X e fecha o resultado. Transição do automato LR ao ler X.
    - Cada conjunto de itens (fechado) corresponde a um estado do autmato de pilha que orienta o parser.
- Powerpoint está errado e é melhor simplesmente pedir pela foto de alguém.


