# Métodos Formais
## [10-11][mvfm]
---
### Quase Acabando
- Semestre acabando pra todo mundo agora, Júlio tá mostrando a solução para exercícios das aulas passadas. 
- Hoje está marcado no moodle como : "*Exercícios*" também.
    - Último arquivo disponível de exercícios no moodle é [Exercícios Dafny 5](./atividades/ExerciciosDafny5.pdf)- O que ele tá mostrando agora é uma arvore binária, especificando a estrutura.
```code
class Nodo<T>
{

    // Abstração
    ghost var Mapa:map<int, T>
    ghost var Repr:set<object>
    
    // Implementação
    var chave:int
    var valor:T
    var esq:Nodo?<T>
    var dir:Nodo?<T>

    [...]
}

class ArvoreBinariaBusca<T>
{
    // Abstração
    ghost var Repr:set<object>
    ghost var Mapa:map<int,T>

    // Implementação
    var raiz:Nodo?<T>

    [...]
}
```
- Arquivo inteiro está disponível [aqui](./atividades/classes_parte2/ArvoreBinariaBusca.dfy)
- Analisando o código, é util ter um predicato '*Menor*'?
```
    ghost predicate Menor(a:set<int>, b:set<int>)
    {
        forall x, y :: x in a && y in b ==> x < y
    }
```
    - Sim. Bem útil
    - Realmente, essa foi a conclusão.
- Restante do tempo da aula vai ser para tirar dúvidas das listinhas de atividade.

### Os 45 Minutos restantes.
- Na prova, as listinhas vão ser a base. Júlio só não vai cobrar a síntaxe do Dafny.
- Para isso, ele usa o seguinte exercício como base : 
    - "*Implemente & verifique em Dafny a correção de uma classe que represente uma ContaCorrente com operações de depósito, saque & consulta de saldo. Sabe-se que os objetos ContaCorrente possuem um valor máximo de saldo negativo garantido pelo banco e que jamais poderão extrapolar esse limite.*"
    ```code
        ---------------------
        | ContaCorrente     |
        ---------------------
        | saldo             |
        | limite            |
        ---------------------
        | ContaCorrente()   |
        | Depositar(valor)  |
        | Sacar(valor)      |
        | Saldo()           |
        ---------------------
    
        ---------------------
        | c:ContaCorrente   |
        ---------------------
        | saldo = -300      | Limite não sendo número negativo 
        | limite = 1000     |   permite isso. A invariante mudaria.
        --------------------- 


        Q : Quem é a invariante dessa classe?
        A : "*saldo >= limite"

        Q : Quais são as pré & pós condições de cada método da 'ContaCorrente'?
        A : ContaCorrente(L)
            pré : L < 0                         // Limite tem que ser negativo.
            pós : Limite = L ^ saldo = 0        // Garantir que Limite = L após a execução desse método.

            Sacar(valor)
            pré : saldo - valor >= limite ^ valor > 0
            pós : saldo = old(saldo) - valor
    ```
- Esse exemplo em específico não vai cair na prova, já que a recém fizemos, mas vai ser essencialmente isso.
    - O processo por si só parece bem simples, é só desenhar um UML & pensar 'logaicamente'. É um problema de Programação Orientada à Objetos.
- Exercício 3, da lista de sequencias é mencioando. Atividade 4, mais especificamente. 
    - Mesma ideia que o exercício anterior.
- "*O uso de sequencias é muito útil para simplificar especificações sobre outros tipos de coleções, tal como arrays. Estamos interessados em calcular o somatório de todos os elementos de um array de inteiros. Implemente e prove correta sua especificação, utilizando obrigatoriamente seq para facilitar a construção das especificações necessárias. Primeiro, especifique uma função recursiva adequada para representar o somatório de elementos de uma sequencia. Somente depois, implemente um método para calcular o somatório dos elementos do array."
    ```
        Somatorio : List<Z> -> Z
        Somatorio(l) : r
        ---
        Pré : T
    ```
        Pós : r = $\sum_{i=0}^{|l|-1}i$
    ```
        ---
        |
        | Somatorio([]) = $0$
        |
        | Somatorio($h:l$) = $h + Somatorio(l)$
        |
        ---

        Somatorio(array)
        {
            I = 0
            R = 0

            Enquanto ( I < |Array| )
            {
                R + R + Array[I]
                I = I + 1
            }
            Retorne R
        }
        Variante do Laço : |Array| - I
    ```
