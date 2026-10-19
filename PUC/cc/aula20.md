# Construção de Compiladores
## [07-10][mvfm]
----
### Verificação Semantica
- "*Escopos, sistemas de tipos, regras de inferencia e um verificador completo com JFLEX + BYACC/J*"
    - Resumo pequininho que o Agustini colocou foi : **Analise Semantica : Por que a gramática não basta; o que a análise semantica verifica.**
    - **Tabela de Simbolos : Responsabilidades, atributos, estruturas de dados e o "universo".**
    - **Escopos : Estático X Dinamico, pilha de tabelas, ocultação de nomes.**
    - **Sistemas de tipos e verificação : Expressões de tipo, regras S ⊢ e T; equivalencia, coerção, ⊥.

### Analise Sintática
- Onde estamos atualmente no compilador?
- ![Posição atual do compilador](assets/onde_no_compilador.png)
    - **Léxico** : Identificadores válidos, strings fechadas, nenhum caractere estranho.
    - **Sintático** : Declarações e expressões com a estrutura correta.
    - **Semantico** : O programa tem um significado bem definido? Variaveis declaradas antes do uso, tipos corretos, chamadas com as argumentos certos.
    - **Além de verificar** : Coleta informação para as fases seguintes : a qual declaração cada nome se refere, tipos, tamanhos.

### Por que não verificar tudo na gramática?
- BEM resumidamente : "*A gramática aceita um superconjunto da linguagem; análise semantica filtra os programas sem significado.*"
- Ferramentas : "*Tradução dirigida por sintaxe {atributos + ações semanticas, Unidade 4.2} e uma tabela de símbolos que ''lembra' o contexto que a GLC não consegue lembrar.*"
- **Validade não é correção.**
    - Rejeitar o maior número possível de programas incorretos.
    - Aceitar o maior numero possível de programas corretos.
    - Fazer isso rápidos.
    - As duas primeiras metas conflitam : uma análise estática sempre é conservadora.
    - ![Validade](assets/validade.png)


