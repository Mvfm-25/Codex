# Como o sistema linear foi montado

## O ponto de partida

O enunciado define um sistema que, em algum momento, **estabiliza** — a quantidade esperada
de pedidos em cada processador para de mudar. É exatamente essa condição de estado
estacionário que vira o sistema linear.

Chame de $\pi_i$ o número esperado de pedidos no processador $i$ no estado estacionário
(indexando de $1$ a $n$, como no enunciado).

---

## A equação de balanço

Em cada milissegundo, todos os pedidos de todos os processadores são atendidos em paralelo.
Para o processador $i$, o que chega nele é:

- **1 pedido externo**, se $i = 1$ (o enunciado diz que o processador 1 recebe um pedido
  por ms);
- **pedidos repassados** por outros processadores.

Como cada pedido no processador $j$ é repassado para $j\!+\!1$ com probabilidade
$(n\!+\!1\!-\!j)/(n\!+\!1)$ e para $j\!+\!2$ com probabilidade $(j\!-\!1)/(n\!+\!1)$,
o fluxo esperado de $j$ para $i$ por milissegundo é $\pi_j \cdot P_{j \to i}$.

No estado estacionário, o que chega ao processador $i$ deve igualar o que já estava lá:

$$\pi_i = \delta_{i,1} + \sum_{j=1}^{n} \pi_j \cdot P_{j \to i}$$

Reorganizando para o lado esquerdo:

$$\pi_i - \sum_{j=1}^{n} \pi_j \cdot P_{j \to i} = \delta_{i,1}$$

Isso é uma equação por processador. Com $n$ processadores, temos $n$ equações — ou seja,
um sistema linear $n \times n$.

---

## A forma matricial

Empilhando as $n$ equações em notação matricial, o sistema fica:

$$\underbrace{(I - P^T)}_{A} \, \pi = \underbrace{e_1}_{b}$$

onde:

- $P$ é a **matriz de roteamento** — $P_{ij}$ é a probabilidade de um pedido no
  processador $i$ ser repassado ao processador $j$ (excluindo conclusões);
- $P^T$ é a transposta: a contribuição que cada processador $j$ manda para cada linha $i$;
- $e_1 = [1, 0, \ldots, 0]^T$ porque só o processador 1 recebe chegadas externas.

---

## Preenchendo P (na prática)

Usando indexação 0-baseada do código, o processador $j$ roteia para:

| destino | probabilidade |
|---------|---------------|
| $(j+1) \bmod n$ | $(n - j) \mathbin{/} (n+1)$ |
| $(j+2) \bmod n$ | $j \mathbin{/} (n+1)$ |

Cada entrada dessas subtrai da coluna $j$ de $A$ (daí o `-=` no código):

```java
A[(j + 1) % n][j] -= fwd;
A[(j + 2) % n][j] -= skip;
```

O $I$ já estava lá — a inicialização `A[i][i] = 1.0` monta a identidade antes de
subtrair $P^T$.

---

## Por que funciona (e por que dispensa simulação)

A simulação antiga aproximava $\pi$ jogando pedidos aleatórios por 250.000 passos e
tirando média. O sistema linear *define* $\pi$ diretamente, sem aleatoriedade. Gauss
encontra a solução exata em $O(n^3)$ — para qualquer $n$ razoável, isso é instantâneo.

Uma consequência curiosa: o total $\sum \pi_i = n + 1$ para todo $n$. Pela Lei de Little,
com 1 chegada por ms e probabilidade $1/(n+1)$ de conclusão a cada visita, a esperança
do tempo no sistema é $n+1$ ms — e por isso o total de pedidos em regime é sempre $n+1$.
