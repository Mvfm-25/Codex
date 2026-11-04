# Métodos Formais
## [03-11][mvfm]
---
### Continuação de Classes & Objetos
- Seguindo da aula passada em que um contador foi implementado.
```code
class Contador
{
    ghost var valor:int 
    var incs:int 
    var decs:int

    [...]
}
```
- Júlio desenha um pequeno esquema de classes em que o contador agora é um agrupamento de dois novos objetos, uma nova classes 'Célula' que simplesmente armazena um valor integer dentro de si.
- Incs & Decs recebendo seus valores dessas classes.
```code

class Celula
{
    var valor:int

    constructor (v:int) 
    ensures valor == v
    {
        valor := v;
    }
}

```
- Com isso ele atualiza os métodos internos para corresponderem à mudança imposta.
- Referências não podem ser feitas diretamente mais pois o objeto não permite.
- 'Gerencia de Frames Dinamicos' -> Conjunto de referencias.
    - Whatever you say bro.
---
### Implementação de Fila em Dafny, com gerencia de frames dinamicos
- Primeiro especifica, só depois pensa na implementação
    - Implementação tem inúmeras, mas a especificação é a mesma. Devem, ao final das contas, fazerem as mesmas coisas.
- "Coleção linear de elementos que segue o protocolo FIFO."
```code
class Fila
{
    ghost var Conteudo:seq<int>
    ghost const TamanhoMaximo:int
    ghost var Repr:set<object>

    ghost predicate Valid()

    constructor (max:nat)
    requires max > 0
    ensures Conteudo == []
    ensures TamanhoMaximo == max
    ensures fresh(Repr)
    ensures Valid()

    method Enfileirar(e:int)
    requires |Conteudo| < TamanhoMaximo
    modifies Repr
    // Concatenação de duas sequências
    ensures Conteudo == old(Conteudo) + [e]
    ensures fresh(Repr - old(Repr))
    ensures Valid()

     method Desinfileirar() returns (e:imt)
    requires |Conteudo| > 0
    modifies Repr
    ensures e == old(Conteudo[0])
    ensures Conteudo == old(Conteudo[1..])

    function Tamanho():nat
    reads Repr
    ensures Tamanho() == |Conteudo|
}
```
