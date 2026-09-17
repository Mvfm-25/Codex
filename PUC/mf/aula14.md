# Métdos Formais
## [17/09][mvfm]
---
### Seguindo com os exercícios
- Chegando na aula, Júlio já tinha começado a revisão no **Exercício n02** da [folha de revisão para prova](atividades/RevisaoP1.pdf)
    - Ela pede por uma definição indutiva para um conjunto de árvores binárias "**Natalinas**". 
    - ![Árvore binária natalina](assets/Natalinas.png)
- Pra isso, ele cria uma regra base & uma regra para encontrar o próximo elemento. Seguindo a formatação definida anteriormente.
    - Regra base :
        - **{Vazio} / $<<>, a, <>>$ e N**
    - Regra próximo elemento :
        - **$<<L, a, R>>$ e N / $<<L, a, <>>, a, <<>, a, R, >>$ e N**
- Ele segue de novo com aquela definição que uma árvore é a raíz e mais outras árvores qauisquer de baixo dela.
- "*Como que tu vai implementar isso não me importa. Essa é a definição simbólica.*"
    - "*Sei lá o que vou inventar até terça-feira que vem.*"
    - "*Não tem muito o que inventar com regras indutivas.*"

### Definição Equacional Recursiva para max: List($N$) -> $N$
- Primeira definição, especificação é : **Não funciona para listas vazias**. 
    - Manda o usuário ler a documentação direito e pra parar de reclamar.
    - ![Questão 3](assets/esp_max.png)
- O que ele já escreveu :
    1. **Max : List<$N$> -> $N$**
    2. Max(l) = m
    3. Pré : l != [], [l] > 0
- O que é $M$? Como podemos garantir que $M$ é o maior de todos.
    - Bom... Pelo menos Maior / Igual.
- Vamos usar indices como normalmente começaríamos em determinada línguagem de programação. 
- Tenho notado isso em muitas das aulas que tivemos, to tendo uma realização muito idiota que só estamos escrevendo Java (*Ou, genericamente qualquer outra linguagem mas o meu ponto segue*) de modo matemático.
    - Duh, esse é o ponto inteiro da cadeira. Por isso que é uma realização muito idiota, mas é algo que praticamente acontece em todas as aulas.
- "*A pós-condição tem que ser verdadeira até para índices que não fazem sentido.*"
- Segue a pós-condição escrita no quadro :
    1. **paratodoIpertencenteN ( $I$ < [$l$] ^ $l$[$i$] = $m$ )**
    - Retorna o maior elemento da lista, pois teve uma especificação anterior que não mencionava o fato que **$m$** teria que ser um elemento da lista.
- Acredito que o Júlio acabou de apresentar o uso de uma função auxiliar '*Maior*', sendo a função que de fato faz a comparação entre dois números naturais para ver quem é a mior. Deixando o trabalho de passar pela lista para o '*Max*'.
    - Questão deixava apresentar tais funções auxiliares, sem ter que criar sua estruturação.
    - Mesmo assim, Júlio foi especificar. Essencialmente, a especificação dele foi uma função recursiva que **corre** os dois números até o zero. Vendo quem chega mais cedo.
- De novo, não conseguindo escrever com letras Gregas aqui está me prejudicando um pouco. Claude, do your thing.

### Questões para Provar
- Questão n04 : 
    - ![Questão 4 para provar.](assets/prova_quest4.png)
    - "*Ela soma soma e eleva ao quadrado, apenas?*"
- Vamos provar pela variável $n$ que $f(n) = (n+1)^2$
    - Caso Base
        - Provar para 0. $f(0).
        - = 1   (por F1.)
        - = $(0+1)^2$   (por alguma regra aritmética qualquer, whatever.) -> Basicamente o que ele colocou no quadro. Já sabemos que vale assim de cabeça.
- "*Multiplicação é um inferno para provar.*"
    - Caso Indutivo
        - Seja $x$ e $N$ arbitrária
        - Assumir HI (hipótese de indução) $f(x) = (x+1)^2$
        - Provar $f(x+1) = (x+2)^2$
        - $f(x+1)$
        - = $f(x) + 2x(x + 1) + 1$  (por F2)
        - = $(x+1)^2 + 2x(x+1) + 1$     (por HI)
- "*Agora tudo por álgebra e aritmética, não vamos inventar nada.*"
        - = $x^2 + 4x + 4$
        - = $(x+2)^2
    - q.e.d
### Conclusões.
- **NENHUMA** dessas funções vão acabar caindo na prova justamente pois estamos vendo elas agora nessa aula, mas o comportamento geral de definir, especificar & provar segue.
- Por sorte, vamos poder trabalhar com tal gramática, não tendo que fazer uso da síntaxe do Isabelle que é chata & longa para caralho
- "*Não ignora o teste, pois ele mostra falhas na especificação.*"
    - "*Stop and think!*"
    - "*Oh fuck! The kitchen's on fire! Just get the fuck outta here!*"
