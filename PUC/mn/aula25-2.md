# Métodos Numéricos
## [03-11][mvfm]
---
### Interpolação de Lagrange
- O método que o JB tinha descrito como 'Fica batendo no carro todo amassado até consertar'.
- Ele mencionou que fica mais simpels usar os pontos na ordem correta, não tendo aquele cenário da interpolação de Newton de conseguir o ponto final intermediária a pontos já conhecidos.
    - Ainda daria pra fazer isso, mas fica mais chatinho de se trabalhar aparentemente.
- Temos $(x1, y1), (x2, y2), (x3, y3), (x4, y4)$. Então queremos um polinomio bonitinho e simples, de grau 3 sendo que temos quatro pontos.
    - Vamos encontrar o mesmo polinomio que Newton encontraria, mas de uma maneira diferente.
- Lagrange veio depois de newton, os métodos pelo que JB lembra. Ainda assim, ele parece ser muito mais trabalhos, mas possivelmente só para o JB.

### Eu Quero Encontrar um Polinomio
- Imagino que ele é de grau 3 já que estamos passando por 4 pontinhos.
- Genericamente, posso pensar em $p(x) = ax^3 + bx^2 + cx + d$ e ir testando os valores individualmente.
    - Mas nenhum dos dois métodos faz isso. Lagrange, especialmente, complica as coisas.
- "O polinomio que tu quer, é uma mistura desses $y$ que você já tem."
- O polinomio, passando pelos pontinhos que temos, tem que ser o mais próximo possível dos mesmos.
- Ele escreve no quadro : $p(x) = y_1 * P_1(x) + y_2 * P_2(x) + y_3 * P_3(x) + y_4 * P_4(x)$
    - Os polinomios individuais delcara importancia de cada pontinho.
    - $P_2(x) = (x - x_1) * (x - x_3) * (x - x_4)$
        - Queremos que $P_2$ seja $1$ quando $x$ for $x_2$
- Como?
- $P_2(x)$ em $x_2$ tem que dar $1$... Então...
    - $P_2(x) = 1 = (x_2 - x_1) * (x_2 - x_3) * (x_2 - x_4)$
    - Daí só juntamos tudo que fizemos :
    - $P_2(x) = \frac{(x - x_1) * (x - x_3) * (x - x_4)}{(x_2 - x_1) * (x_2 - x_3) * (x_2 - x_4)}$
- JB mostra tudo isso no GNUPlot de novo.
