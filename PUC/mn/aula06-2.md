# Métodos Numéricos
## [20-08-26][mvfm]
---
### Seguindo com polinomios
- '*Polinômios são um mundo feliz*'
- A regra de Descartes também é bem +-, tanto nos casos de raízes positivas e negativas são incertezas.
- Primeiro tópico para encontrar raízes reais será especificado hoje
- Mas o JB está devendo duas coisas da aula passada
	- '*Uma delas tem filmezinhos e animaçõeszinhas para mostrar*'
- Ele mostra o polinômio $p(x) = x^4  + 6x + 10$ em que sabemos que ela possuí 4 raízes, mas o GNUPLOT não mostra nenhuma raíz.
	- Todas elas são complexas.
	- Vamos simplesmente subtrair $10$ para baixar o gráfico. Assim tornando evidente que ela possuí $2$ raízes reais. Deixando $2$ complexas.
- $p(x,a) = x^4 + 6x + a$
	- alpha sendo um parametro pra simplesmente regular o quão alto fica a função.
	- Com um laço que mandava o $a$ de -10 -> 10, as raízes se aproximavam aproximavam & depois sumiam.
- ELe mostra a mesma coisa depois no gráfico que visualiza tanto o eixo real quanto o complexo.
	- E é bem legal. Saíram do eixo real e entraram no eixo complexo.
	- O descer de dois em dois não é mágica... Bem, é, mas é algo que o Descartes viu as as raízes sumindo para uma dimensão que ele não conhecia ainda.
- '*As raízes complexas são espelhadas, mas não sempre. Só quando os coefieientes são reais.*'

### Assunto Pequeno
- '*Algum dia na vida vocês vão precisar avaliar um polinômio*'
	- é botar um x no polinomio e ver no que sai
- '*Tem jeitos bons & mals de fazer isso*'
- Polinômio de exemplo : **$p(x) = x^5 + 12x^4 - 6x^3 + 11x - 16$**
	- Traduzindo isso direto para código, usando *pow()* não é a melhor maneira de fazer isso. Só as chamadas de pow() quebra a performance.
	- mas também não vamos escrever **$x * x * x * x * x$** para mostrar $x^5$
- Forma de **Horner** simplifica bastante coisa.
	- Jeito mega-econômio de escrever um polinômio.
	- Mas... Tem que ser escrita de trás pra frente.
- O polinômio anterior escrito em forma de horner : 
	- **$-16 + x * ( 11 + x * ( 0 + x * ( -6 + x * ( 12 + x ) ) ) )$**
	- $0$ está ali pois ele é o coefiente do $x^2$.
- '*Certas coisas estão amarradas umas nas outras*'
- Jogar pessoas na montanha.

### Jogando pessoas na montanha.
- Método muito simples para as pessoas da TI. Inventado pela matématica, mas isso é uma pesquisa binária
- métodoResolve($a,b$)
	- entre a & b, sai e procura.
	- Tendo ambos, vou achar o m. Aplicando m, se ele for positivo $a$ conttinua & o novo $b$ é o antigo $m$.
	- A raíz fica cercando a raíz, tu não vai **ACHAR** a raiz, mas tu chega bem perto.
	- '*Aqui pra nós é chuver no molhado.*'
- Mas a divantagem é que as seçõesque cortamos podem até ter raízes, mas nunca vamos olhar lá.
	- E ela só encontra uma única raíz. POr mais que tenha milhões.
- JB escreve um pequeno pseudo-código que exemplifica justamente isso que estávamos discutindo.
	- O objetivo é deixar $a$ & $b$ bem pertinho, não necessariamente encontrar a raíz.
