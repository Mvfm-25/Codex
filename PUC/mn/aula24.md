# Métodos Numéricos
## [09-06-2026][mvfm]
---
### Interpolação de Lagrange
- '*Na base da porrada até ficar do jeito que eu quero.*'
- Justamente o que o JB tinha comentado na aula passada em que ele vai tratar da função de polinômio como um mecânico.
- Lagrange vai estar tratando do exato mesmo problema que a interpolação do Newton.
	- Vamos estar encontrando exatamente o mesmo resultado, mas vamos estar passando por caminhos diferentes.
	- Na opinião do JB, o processo do Newton é bem mais elegante. Ele não vê **NENHUM** ponto positivo na metodologia do Lagrange.
- Yipee
- Bem como na última aula, JB cria pontinhos aleatórios justamente para exemplificar a execução do método.
	- Seguem os pontos : (2,1) (3,4) (6,5) (8,2)
	- Tendo quatro pontos, já sabemos que o polinômio é de grau **três**, baseando-se no **número de pontos - 1**.
- '* Posso enxergar o p(x) como uma mistura dos quatro pontos mencionados anteriormente.*'
	- Mas pontos tem graus diferentes de importância, estando mais perto do p(x) etc.
- JB comenta que ele vai criar uma função que '*Dá uma importância para esse 1*', comentando sobre o ponto *(2,1)* e o relacionamento mencionando faz pouco.
	- Ele escreve : **$p(x) = 1*P2(x)$**
	- Essa importância é forte perto do $1$, mas bem fraquinha longe dele.
	- Cada um dos elementos do polinômios vão ter esse grau de importância.
	- $P(x) = 1*P2(x) + 4*P3(x) + 5*P6(x) + 2*P8(x)$
- Agora, vamos ter que encontrar essas quatro funções. JB comenta que é bem fácil encontrar essas quatro, mas menciona de novo a cena do mecânico batendo em teoremas matemáticos com um martelo descuidadamente.

### Marteladas
- Escolhido o $P6$ como a função exemplar. JB diz que a lógica de como encontrar a função de $P6$ é igual para todas as outras.
- Várias ideias sendo jogadas na parede e o JB julgando bastante.
	- Como uma aula normal de POA.
- Como forçamos que essa função '*se destrua*' nos outros pontos? Queremos que ela dê $1$ quando em $6$, mas que dê $0$ em qualquer outro ponto.
	- Para isso, JB escreve $P6 = (x-2)*(x-3)*(x-8)$
	- Escrevendo as raízes, ele faz com que $P6$ vale $zero$ em todos os outros pontos além de $(6,5)$.
- E agora? Sabemos o que ele não pode ser nos outros, mas o que ele tem que ser no ponto que tem que ser?
- Em $x = 6$, o resultado deu $-24$. Mas queremos que dê $1$.
	- Para isso, JB simplesmente escreveu : $(x-2)(x-3)(x-8) / -24$
	- Mas isso é hardcoded. Não é assim. Não podemos conjurar um $-24$ do nada.
- JB escreveu um pouquinho melhor :
	- $(x-2)(x-3)(x-8) / (6-2)(6-3)(6-8)$
- O método de Lagrange é simplesmente uma soma de 4 caras de grau três, nesse caso.
- Abrindo todas as contas, vamos conseguir um polinômio bonitinho que, supostamente, será igual ao polinômio que conseguimos por Newton.
- Expandindo as continhas, JB mostra que Lagrange & Newton resultam na mesma coisa.
	- Everything works!
- E porque queremos Lagrange? Quem usaria Lagrange?
	- JB comenta que tem a ver com o aspecto computacional. Mas não sabemos **O QUE**.
	- Lagrange tem muita conta, comparado com o Newton. Por que queremos algo mais enrolado?
- Pq a conta de Lagrange é hyper-repetitiva, muitas multiplicações são exatamente iguais.

### O Que Aconteceu Agora?
- Com isso, podemos argumentar que o método de Lagrange é pelo menos viável no aspecto computacional.
 
