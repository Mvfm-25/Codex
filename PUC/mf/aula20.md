# Métodos Formais
## [08-10][mvfm]
---
### Rápida correção da prova.
1. Aprsente uma definição indutiva para o conjunto de palavras formadas com os simbolos 0 & 1 tal que as palavras contenham a mesma quantidade de 0s & 1s em qualquer ordem.
    - Possível reposta :
        - Palavra vazia pertence. Nada / $e ∈ L$ | ${w ∈ L}/{OW1 ∈ L}$ | ${w ∈ L}/{1W0 ∈ L}$ | ${u, v ∈ L}/{uv ∈ L}$
2. Para cada um dos seguintes problemas, defina formalmente a assinatura de uma função associada a solução do respectivo problema, com seu domínio e contradominio, pré e pós-condições adequadas utilizando fórmulas em lógica de predicados. Não é necessário definir equações.
    - Computar o valor absoluto de um número inteiro.
        - Possível resposta : 
        - ABSOLUTO $Z$ -> $N$   PRÉ : $T$
        - ABSOLUTO(N) = R       PÓS : $R >= 0 ^ (N >= 0 -> R = N) ^ (N < 0 -> R = -N)$
    - Remover um elemento  de uma determinada posição de uma lista, deslocando os elementos subsequentes em uma posição e retornando a lista modificada.
        - Possível resposta :
        - REMOVER : LIST<T> x $N$ -> LIST<T>
        - REMOVER($l, p$) = $r$
        - PRÉ : $p < |l|$
        - PÓS : $|n| = |l| - 1$
            - ^ $∀i∈N( i < p -> r[i] = l[i] )$
            - ^ $∀i∈N( p <= i ^ i < |r| -> |r[i] = l[i + 1] )$
3. Defina, através de equações recursivas, a função solicitada nas seguintes questões. Utilize obrigatoriamente a definição indutiva de listas. Não esqueça de apresentar o domínio e contradomínio da função.
    - $nada/ {|nada|} ∈ List(T)$ || ${L ∈ List(T)   | h ∈ T}/h : L ∈ List(t)$
- Função que toma uma lista de números naturais como entrada e produz uma lista com o dobro do tamanho através da duplicação de cada elemnto. Ex : [1,2,3] -> [1,1,2,2,3,3]
    - Possível resposta : 
        - DOBRA : LIST<T> -> LIST<T>
        - DOBRA ([] = []
        - DOBRA($x:xs$) = $x:x:dobra(xs)$)
- Função que recebe um número natural $n$, uma lista de números naturais e retorna o elemento localizado na posição $n$ da lista.
    - Possível resposta :
        - GET : LIST<T> x $N$ -> T
        - GET($x:xs, 0$) = 0
        - GET($x:xs, n$) = GET($xs, n-1$)
4. Seja a seguinte função definida através de equações recursivas :
```code
f : N x N - > N
    
            { n + 1,                    m = 0
f(m,n)   -> | f(m-1, 1),                n = 0 & m > 0
            { f(m-1, f(m, n-1)),        n > 0 & m > 0

```
---
    - Possível resposta :
    - Provar por indução em $k$
    - P($k$) >= $f(1, k) = k + 2$
    - Caso base :
        - Provar $f(1,0) = 0 + 2$ 
        - $f(1,0)$
            - = $f(0,1)$
            - = $2$
            - $= 0 + 2$
            - $qed$
    - Caso indutivo :
        - Assumir $MI$ $f(1,l) = k + 2$
        - Provar $f(1, k + 1) = k + 1 + 2$
        - $f(1, k + 1)
            - = f(0, f(1, k))
            - = f(1,k) + 1)
            - = K + 2 + 1
            - K + 1 + 2
            - qed.
---
- Não vou escrever a questão 5. Foda-se.

### Arrays no Dafny.
- Continuação do material de *Programação & Verificação com Dafny*.
    - Material [aqui](https://brpucrs-my.sharepoint.com/shared?listurl=https%3A%2F%2Fbrpucrs%2Dmy%2Esharepoint%2Ecom%2Fpersonal%2F10070245%5Fpucrs%5Fbr%2FDocuments&id=%2Fpersonal%2F10070245%5Fpucrs%5Fbr%2FDocuments%2FDocumentos%2Fmetodosformais%2Fdafny%2FExerciciosDafny2%2Epdf&parent=%2Fpersonal%2F10070245%5Fpucrs%5Fbr%2FDocuments%2FDocumentos%2Fmetodosformais%2Fdafny&shareLink=1&ga=1), não sei se vou conseguir colocar tudo da aula aqui.
    - [Dafny Reference Manual](https://dafny.org/latest/DafnyRef/DafnyRef)
    - Disponibilizado também uma pasta zippada contendo exemplos de arrays na subpasta atividades.   
- O exemplo mais idiota possível de um array que o júlio deu foi uma "*sequência*"
```code
    var a := [1,2,3]
```
- Isso é conteúdo que vamos começar a ver semana que vem. Um array segue normalmente a síntaxe que estamos acostumados com maioria das linguagens.
```code
method Main(){
    // Criando
    var a := new nat[3]

    // Indexando manualmente.
    a[0] := 0
    print(a[2])

    // Inicialização pode também ser uma expressão que retorna uma função do tipo nat -> T
    a := new int[5]( i => i*i  )
}
```
