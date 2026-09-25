# Métodos Numéricos
## [24-09][[mvfm]
---
### A Aula Mais Difícil da Cadeira
- Outro método de Gauss.
- JB coloca no quadro um gráfico com uma coletania de vários pontos que vieram :
    - "*De sei lá. Não importa, mas já nos veio pronto.*"
- O que queremos?
    - Ao invés de uma numvem de pontinhos aleatórios, queremos uma função que prevê *mais ou menos* o comportamento dos pontinhos.
    - Não uma função que siga **EXATAMENTE** cada pontinho, mas uma média. No geral, ela vai estar um pouco errada.
- Método dos mínimos quadrados. Fuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuck.

### Aula de Cálculo.
- Primeira coisa : Um achismo. Que tipo de função a nossa nuvem você acha que parece ser?
- No exemplo do quadro : pensamos que é uma quadrática.
    - Vamos procurar A MELHOR QUADRÁTICA para nosso gráfico. É possível errarmos
- Começamos com : $F(x) = ax^2 + bx + c + dcos(x)$
    - JB colocou o $cos$ pelo achismo estar valendo por agora.
- O que temos que fazer para encontrar a melhor quadrática?
- Regular as variaveis até encontrar. Gira uma válvula aqui, outra lá etc.
- O que significa o melhor?
    - O mais perto dos nossos pontinhos.
    - O mais próximo em geral. A diferença mínima entre os y's para qualquer $f(x)$. 
    - Tira o módulo.
- Num mundo feliz, isso tá perto de 0. Mas para **TODOS** os pontos y.
- Soma tudo e vê se tá tudo pequeno.
    - $\sum(f(x_i) - y_i)^2$ = min!
        - Usado o elevado ao quadrado pra não usar o módulo.
- Como regulamos para ser o menor possível?
    - Derivada tem que ser igual à $0$. Derivada à relação à $a, b, c,$ & $d$.
    - Quatro derivadas.
- $d / da  = \sum(f(x_i) - y_i)^2 = 0$
    - Derivada da soma é a mesma que somar as derivadas

### Seguindo com o Cálculo
- Secção só pra mostrar a evolução da fórmula de acordo com o ritmo do JB.
- $\sum d / da  = (f(x_i) - y_i)^2 = 0$
- $\sum 2 * (f(x_i) - y_i) * (d(f(x_i)) / da) = 0$
- $2 * \sum (f(x_i) - y_i) * (d(f(x_i)) / da) = 0$
- $\sum (f(x_i) - y_i) * (d(f(x_i)) / da) = 0$
- $\sum (f(x_i) - y_i) * x_i^2 = 0$
    - *Chuveirinho...*
- $\sum f(x_i) * x_i^2 - \sum y_i * x_i^2 = 0$
- $\sum f(x_i) * x_i^2 = \sum y_i * x_i^2$
    - Só vamos piorar a fórmula a partir desse ponto.
- $\sum (ax_i^2 + bx_i + c + d * cos(x_i))x_i^2 = \sum y_i * x_i^2$
    - *Chuveirinho...*
- $\sum (ax_i^4 + bx_i^3 + cx_i^2 + dx_i^2 * cos(x_i)) = \sum y_i * x_i^2$
- $\sum ax_i^4 + \sum bx_i^3 + \sum cx_i^2 + \sum dx_i^2 * cos(x_i) = \sum y_i * x_i^2$
- $a \sum x_i^4 + b\sum x_i^3 + c\sum x_i^2 + d\sum x_i^2 * cos(x_i) = \sum y_i * x_i^2$
- **DEU. ISSO AQUI É O ACABAR.**

### Largados no mato. O que precisamos fazer agora?
- Agora só precisa fazer isso mais três vezes. 
- O que fizemos agora foi simplesmente para o modular o valor de $a$. Temos que procurar a derivada em relação ao $b$, ao $c$ & ao $d$.
- JB continuou por um tempo mostrando como a fórmula foi montada para cada variavel ( que, até certo ponto eram bem parecidas com a que descrevi aqui.  ) e enfim mostrou o script AWK que ele já tinha para tal cenário.
- *Gauss Recursivo* ele comenta para encontrar cada variável.
- Notícia ruim : *Não é vezes $x$... É o número $e * x*$
    - É regular ali dentro.
    - Sistema no final não vai ser mais linear. Tornando inúteis os métodos que vimos até agora.
