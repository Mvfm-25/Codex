# Métodos Formais
## [15-09][mvfm]
---
### Aula de Atividades
- Enunciado do trabalho entregue supostamente aula passada, mas faltando ainda 2 semanas para entega.
    - Ele vai se basear na atividade de '*concatenção*' que ele já tinha entregue como arquivo Isabelle. Não parece ser tão difícil, considerando que seria só seguir a base até sua conclusão lógica.
- Também já tenho um resumo escrito, *pelo menos para o arquivo de introdução ao Isabelle*, caso eu me perca. 
- Ainda não entendi como vai ser a aula hoje, mas acredito que o Júlio vai nos acompanhar com a resolução de outros arquivos de atividades presentes no Moodle.
    - Primeira aula de MF com o novo note btw.
- Prova ainda está para **Terça-feira que vem dia 22/09**. Prova vai ser aplicada na sala **314**

### Solucionando Questão 1.
![Questão 1](assets/quetao1.png)
- Função Letra a :
    - Modo Normal
    ``` code
        POT2 : N -> N
            POT2 (0) = 1
            POT2 (x+1) = 2 * POT2(x)

        FAT : N -> N
            FAT (0) = 1
            FAT (x+1) = (x+1) * FAT(x)

        FIB : N -> N
            FIB(0) = 0
            FIB(1) = 1
            FIB(x+2) = FIB(x) + FIB(x+1)

        SOMA N x N -> N
            SOMA(x, 0) = x
            SOMA(x, y+1) = SOMA(x,y) + 1

        MULT : N x N -> N
            MULT(x,0) = 0 
            MULT(x, y+1) = SOMA(x, MULT(x,y))
    ```
    - Em Isabelle :
    ```code
        primrec pot2 :: "nat -> nat" where
        pot2eq1:"pot2 0 = 1" |
        pot2eq2:"pot2 (Suc x) = 2 * pot2 x"

        primrec fat::"nat -> nat" where
        fateq1:"fat 0 = 1" |
        fateq2:"fat (Suc x) = (Suc x) * fat x"

        fun fib::"nat -> nat" where
        fibeq1:"fib 0 = 0" |
        fibeq2:"fib (Suc 0) = 1" |
        fibeq2 : "fib (Suc (Suc x)) = fib x + fib (Suc x)"
    ```
- Para o Isaballe os números naturais, uma estrutura indutiva, ou ele é 0 ou o sucessor de outro
- Teoremas a serem provados : 
    1. paratodoApertencenteN(POT2(a) = $2^a$)
    2. paratodoABpetencenteN(SOMA(A,B) = $a + b$)
    3. paratodoABpertencenteN(SOMA(A,B) = SOMA(B,A))
    4. paratodoApertencenteN(MULT(A,0) = 0)
- Júlio vai provar o segundo teorema, fazendo a indução na variável **b**, o segundo argumento da definição indutiva.
    - Provar por indução em : **B**.
    - P(B) = paratodaApertenceN(SOMA(A,B) = a + b)
- Agora : montar caso **base** & **indutivo**. Ver se ela é aceita por Isabelle.
```code
    theorem t2:"paratodoA::nat . soma a b = a + b"
    proof (induction b)
```
- Síntaxe do Isabelle vai só servir para os trabalhos. Escrevemos menos fazendo à mão mesmo.
- Provar **paratodoApertencenteN**(Soma(a,0) = a+0)
    - seja X pertencente N arbitrária.
    - PROVAR Soma(X,0) = X + 0
    - SOMA(X,0)
        - = X (por esq1)
        - = X + 0
        - qed
- Em Isabelle, provando caso base :
```code
    theorem t2:"paratodoA::nat . soma a b = a + b"
    proof (induction b)
        show "paratodoA::nat . soma a 0 = a + 0"
        proof (rule allI)
            fix x::nat
            have "soma x 0 = x" by (simp only:soma01) 
            also have ". . . = x + 0" by (arith)
            finally show "soma x 0 = x + 0" by (simp)
        qed
    next
```
- Caso indutivo
```code
    fix y::nat
    assume HI:"paratodoA::nat . soma a y = a + y"
    show "paratodaA::nat . soma a (Suc y) = a + (Suc y)"
    proof (rule allI)
        fix x::nat
        have "soma x (Suc y) = Suc( soma x y ) by (simp only:soma02)"
        also have ". . . = Suc (x + y)" by (simp only:HI)
        also have ". . . = x + Suc y" by (arith)
    qed
```
- 'No Subgoals!' mostra que não resta mais nada para ser provado no estado da prova.
    - Só tomar cuidado no Isabelle pois ele assume que 'x+1' implica no uso do Suc.
    - Mas é essencialmente '*passar*' o que a gente fez à mão para o programa.
- Medo por nada.
