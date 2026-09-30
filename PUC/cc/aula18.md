# Construção de Compiladores
## [30-09][mvfm]
---
### Coisas para o Agustini se divertir
- Construção de "*Calculadoras*" de acordo com o conteúdo de **Syntax Directed Translation**.
    - Tradução & entendimento feito ao decorrer do tempo.
    - "*Method of compiler implementation where the source language translation is completely driven by the parser.*"
    - "*We augment a grammar by associating attributes with each grammar symbol that describes it''s properties.*"
- Yacc lê uma gramática livre de contexto, faz uma análise sintática e simplesmente responde :
    - Correto ou Incorreto.

### Material Agustini
- Vamos ver : **Gramáticas de atributos, esquemas de tradução e o modelo de ações semanticas do BYACC/j.**
    - Gramáticas de Atributos
        - Atributos sinetizados & herdados, regras semanticas, árvore anotada.
    - Ordem de avaliação e classes de SDD
        - Grafo de dependencias, SDD S-Atribuidas & L-Atribuidas
    - Esquemas de tradução (SDT)
        - Ações embutidas nas produções, SDT pós-fixos, ações no meio da regra.
- Gráfico de gramática associadas à ações semanticas.
    ```
    GRAM                |   AÇÕES SEMANTICAS
    E -> $E_1$ + $E_2$  |   E.val = $E_1$.val + $E_2$.val
    E -> $E_1$ * $E_2$  |   E.val = $E_1$.val * $E_2$.val
    E -> 1              |   E.val = 1
    E -> 2              |   E.val = 2
    E -> 3              |   E.val = 3
    ```
- Agustini desenha uma árvore de derivação padrão para representar o "*caminho*" disso tudo. Não vou conseguir fazer isso aqui, mas dá pra entender a ideia de como ficou.
- Atributos -> E : val : int 
- Ações Semanticas -> Como calcula o valor 
    - Tudo atribuido por **Knuth, 1968**. 
    - "*Ou algo por aí.*" Obrigado Agustini, preciso como sempre.
- Ordenção topológica, algo que já vimos em AEST II, mas não LEMBRO de nada.

### Onde entra a tradução dirigida por síntaxe?
- ![Exemplo gráfico do processo inteiro](assets/TDS.png)
- Faça uma árovre de derivação para as seguintes expressões :
    - $1 + 2 + 3$
    - $(1 + 2) * 3$
- Modo pós-fixada : 
    - $123*+$
    - $12+3*$
- Algoritmo é bem custoso, muita etapa lidando com muitos passos. Arovre de derivação por si só já é bem caro.
    - Excel. Qualquer aparelho de cálculo precisa disso. Por não poder calcular a arvore inteira todas as vezes que eu altero alguma coisa.
- Exemplo de árvore sintática anotada :
- ![Arvore](assets/arvore_sint.png)
- Agustini mostrou uma visualização dessas árvore feita no moodle.
