# Construção de Compiladores
## [16/09][mvfm]
---
### Aula passada foi quase inútil
- Resumo de **Tabelas Action & GoTo**
    - Action[Estado, Terminal] : Determina se o parser empilha, reudz por produção, aceita ou retorna erro.
    - GoTo[Estado, Não-Terminal] : Mostra para onde ir após redução. Reconhece o não-terminal atual.
- "**Cada GoTo(I, X) sob um T vira shift. Cada item completo A->w* vira reduce.**"
    - ![Algoritmo de construção](assets/alg_const.png)
- Na prática, ferramentas como Bison & Yacc já geram essas tabelas automáticamente.
    - Também não vamos implementar em aula, Agustini determinou como inútil.
- "*Pra quem tá preocupado, vai piorar.*"
- Tabela completa gerada pelo processo anotado acima : 
    - ![Tabela completa](assets/tabela_completa.png)
- Trace do parser na frase **NUM + (NUM)**
    - ![Visão do Parser](assets/vis_parser.png)

### Limites do LR(O)
- LR(0) deduz o próximo shift olhando apenas para aquilo que está em sua pilha, não dando uma *espiada* no próximo token como tinhamos visto antes.
    - Isso é considerada frágil. Produções parecidas (como *id* podendo virar : **variável, elemento de array ou atributo**) geram conflito.
    - ![Exemplo de vulnerabilidade](assets/exemplo_vul.png)
    - A solução simples é : **simplesmente usar um token de lookahead.** Dando origem para **SLR(1), LR(1), LALR(1).**

### Adicionando LookAhead
- Ténicas :
    - SLR(1)
        1. Como decide reduzir : **reduz A->w se o próximo token E follow(A)**
        2. Poder de Reconhecimento : **Menor de todos Lookahead 1**
        3. Tamanho de tabela : **Igual ao LR(0)**
    - LR(1) [Canônico / CLR]
        1. Como decide Reduzir : **cada item carrega seu próprio lookahead específico do contexto**
        2. Poder de reconhecimento : **O maior. Reconhece toda gramática LR(1)**
        3. Tamanho da tabela : **Muito maior. Milhares de estados.**
    - LALR(1)
        1. Como decide reduzir : **mescla estados LR(1) com o mesmo núcleo (itens sem o lookahead)**
        2. Poder de reconhecimento : **Quase tão forte quanto LR(1)**
        3. Tamanho da tabela : **Praticamente igual ao LR(0)/SLR(1)**
- Exemplo da geração de tabela CLR(1)
    - ![Automato de Pilha & Tabela de transição de estados.](assets/exemplo_clr.png)
- Automato resultante :
    - ![Automato resultante](assets/exemplo_clr1.png)
