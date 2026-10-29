# Métodos Formais
## [29-10][mvfm]
---
 ### Classes & Objetos em Dafny
- Terça vimos princípios de Conjuntos & multi-conjuntos, tendo que inddicar a sequência de ordenação de determinada lista & permutações entre si.
    - Métodos *ghost* batendo com o tema de outubro.
    ```code 

    ghost predicate OrdenadoCrescente(s:seq<int>)
    {
        forall i :: 0 <= i < |s|-1 ==> s[i] <= s[i+1]
    }

    ghost predicate Permutacao(a:seq<int>, b:seq<int>)
    {
        multiset(a) == multiset(b)
    }

    ```
- Primeiro, algumas definições. De acordo com **[University of Strathclyde](https://personal.cis.strath.ac.uk/jan.de-muijnck-hughes/three-times/objects.html#dafny)**, universidade de Glasgow :
    - *Datatypes carry data and first-class pure functions, and are immutable; typically living on stacks.*
    - *Objects carry data, and methods that are impure; importantly they are mutable structures that live on heaps.*
- Exemplo genérico entregue pela mesma fonte : 
```code
class Contador
{
    var valor:int

    // Construtores aqui também seguem o 'normal' de maioria das linguagens.
    constructor ()
    // Pós-condição necessária. Garanto que qualquqer coisa que implementar aqui, o atributo 'valor' vai ser inicializado 0 por esse construtor.
    ensures valor == 0
    {
        valro := 0;
    }

    // Dois construtores?
    constructor Init(v:int)
    ensures valor == v
    {
        valor := v;
    }

    // Garanto que o método incrementa, de FATO incrementa o valor de valor.
    method Incrementa
    // Quem estou modificando? O próprio objeto.
    modifies this
    ensures valor == old(valor + 1)
    {
        valor := valor + 1;
    }
}

method Main()
{
    // Pelo menos 3 grandes maneiras de instanciar um novo objeto.
    // Esse é um deles, classe tendo construtor.
    var c := new Contador();

    // Chamando construtor pelo nome, agora que temos dois.
    var c2 := new Contador.Init(5);

    // Incrementando o valor & verificando que foi exatamente isso que ocorreu.
    c2.Incrementa();
    assert c2.valor == 6;

    // Não tem public ou private como no Java, então podemos pegar direto aqui a variável 'valor'.
    print(c.valor);
}
```
- Do jeito que o Dafny está escrito atualmente, o Júlio comenta que a estrutura interna do objeto é bem exposta. Ou seja, não segue muito bem o propósito & princípios da Programação Orientada à objetos.

### A Técnica
- Vamos deixar mais POO-Like
    - hehehehehehehehehe
- Júlio tá escrevendo em UML agora, coisa de boas práticas em engenharia de software.
```code
class Contador
{
    // Está especificado que o Contador vai ter um valor.
    // Especificando a interface pública de um contador. Literalmente uma interface do Java.
    ghost var valor:int 

    ghost predicate Valid()
    read this
    {
        valor >= 0
    }

    constructor ()
    ensures valor == 0

    method Incrementa()
    ensures valor == old(valor) + 1

    method Decrementa()
    ensures valor == old(valor) - 1

    function
}
```
- Fiquei com preguiça e não segui escrevendo a cada adição do Júlio no quadro.
- Tenho certeza que ele vá publicar o material no moodle daqui a pouco então não preciso me preocupar tanto.
