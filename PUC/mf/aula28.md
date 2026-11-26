# Métodos Formais
## [26-11][mvfm]
---
### Aula Revisão P2
- **Aplique o cálculo da pré-condição mais fraca da lógica Floyd-Hoare e apresente as implicações que necessitam ser provadas em uma prova de correção parcial para as seguintes triplas :**
    - a)  $[x > 2 ^ y > 3] x := x + 1; y := y + x [y > 6]$
    -   ^ Pré-condição.                         ^ Pós-condição.
    - b) $[x < 7] if (x >= 5) then$ $x := 1 [x < 5]$
- Técnica para resposta é de baixo para cima. A regra a ser aplica é a da composição. Temos que calcular a condição que junta a pré e a pós condição. Regra no final do arquivo.
- Respostas :
```code

^   (x > 2 ^ y > 3)
|   (y + x + 1 > 6)
|   x := x + 1
|   (y + x > 6)
|   y := y + x
|   (y > 6)

(x > 2 ^ y > 3) -> (y + x + 1 > 6

^   (x < 7))
|   (x >= 5 -> 1 < 5) ^ (> x >= 5 -> x < 5)
|   if (x >= 5){
|       (1 < 5)
|       x = 1
|       (x < 5)
|   }
|   (x < 5)

(x < 7) -> ( x >= 5 -> 5 ) ^( !x >= 5 -> x < 5 )
```

- **Considere o seguinte algoritmo para computar o quadrado de um inteiro positivo maior ou igual a 1** :
```code

int sqr(int x){
    int i = 1;
    int j = 1;
    while( i < x ){
        j = j + 2*i + 1;
        i = i + 1;
    }

    return j;

}

```
- **Responda as seguintes questões** :
    - a) **Defina uma estrutura adequada de representação de estado para a computação deste algoritmo e mostre pelo menos duas sequências finitas de computação.**
    - b) **Defina formalmente as pré-condições & pós-condições do algoritmo.**
    - c) **Defina formalmmente a invariante e a variante do laço de repetição.**
    - d) **Defina uma função recursiva na cauda 'tail_sqr' e explique como usar 'tail_sqr' para computar 'sqr'.**
- O que estava presente no quadro :
```code

SQR : Z -> Z
PRÉ : x > 1
PÓS : j = $$x^2$

    | x  | i  | j |
e0  | 3  | 1  | 1 |
e1  | 3  | 2  | 4 |
e2  | 3  | 3  | 9 |
```
- Estou assumindo que a tabela abaixo seria a resposta pra alternativa *a*. Como é simplesmente um for, uma tabelinha parece intuitivamente ser a estrutura ótima de representação. Faz sentido pra mim.
