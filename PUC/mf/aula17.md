# Métodos Formais
## [29-09][mvfm]
---
### Lógica de Floyd-Hoare
- "*Método axiomático para provar que determinados programas são corretos*"
    - Parece que estamos entrando mais para especificação e verificação léxica de programação do que qualquer outra coisa agora.
    - Entrando em progrmaas de extensão *.dfy*, ou seja, uso do Dafny.
    ```
        method Triple(x: int) returns (r: int)
            requires true;
            ensures r == 3*x;
        {
            var y := 2*x;
            assert x + y == 3*x;
            r := x + y;
            assert r == 3*y;
        }
    ```
- raciocínio do porque estamos usando programas do Dafny foi a mesma que usavamos para a matéria anterior, então é simplesmente a justificação da cadeira como um todo regurgitada.
    - Para redução de falhas que são introduzidas durante a especificação do  sistema e, assim, reduzir o seu custo final
    - o Código bem especificado e verificado é mais fácil de reutilizar, uma vez que  temos um claro entendimento do que o sistema deve fazer;
    - o Para sistemas críticos (aviões, usinas nucleares, ...) isto se torna muito mais importante, pois se espera que os sistemas possam sofrer auditorias sobre o quanto eles garantem que irão funcionar conforme desejado;
    - o A especificação de um sistema auxilia na documentação do mesmo e, feita de  uma maneira formal, auxilia no processo de implementação final do sistema;
    - o Atualmente empresas enfrentam problemas com sistemas legados, pois os responsáveis pelo seu desenvolvimento não os documentam de uma maneira precisa e, na maioria das vezes, não se encontram mais na empresa;
    - o Sistemas de software têm um tempo de vida muitas vezes maior do que as pessoas - bug do milênio é apenas um exemplo.

### Triplas de Hoare
    ```
    (|P|) C (|Q|)
    ```
- Onde : 
    1. P & Q são asserções (formulas na lógica de predicados de primeira ordem com igualdade.)
    2. P : Pré-condição. Asserções sobre o estado inicial do programa, que denotam sob quais restrições o programa está preparado para funcionar.
    3. Q : Pós-Condição. Asserções sobre o estado final do programa, que denotam condições sobre os dados resultantes do programa.
    4. Comandos de uma linguagem de programação.
- Exemplo dado :
    ```
    (|x > 4|)   x:= x+1     (|x > 5)
    ```
![Exemplos de triplas](assets/exemplos_triplas.png)

### Linguagem de Programação Simplificada
- Vamos usar uma linguagem que não existe mas que vai nos ajudar a facilmente definir operações aritméticas & lógicas assim como certas operações fundamentais para programação como :
    ```
    Atribuição (:=)
    Sequência (;)
    Condição (if)
    Laço (while)
    
    EXPRESSÕES ARITMÉTICAS
    ---
    E : := n
    x
    E + E
    E - E
    E * E
    -E 

    EXPRESSÕES LÓGICAS
    ---
    B : := true
    false
    !B
    B&&B
    B||B
    E<E
    E==E
    E!=E 

    COMANDOS
    ---
    C : := x := E
    C ; C
    if B (C)
    if B (C) else (C)
    while B (C)
    ```
- "*Resistam programa imperativamente dentro de function*"
- Vendo o júlio desenhando fluxogramas é bem engraçado.

### Cálculo Floyd-Hoare
- A versão do cálculo demonstrada aqui irá obter a chamada "*pré-condição mais fraca*". Ou seja, de que qualquer outra pré-condição possível implicará nela.
![Cálculo Floyd-Hoare](assets/calculo_hoare.png)
- Restante do material pode ser encontrado [aqui](./atividades/LogicaDeHoare.pdf)
