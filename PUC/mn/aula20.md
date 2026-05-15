# Métodos Numéricos
## [14-05-2026][mvfm]
---
### Essa foi o Gauss mesmo
- **NÃO** é pra resolver Sistemas Lineares.
	- É pra usar os sistemas pra fazer uma coisa muito legal
- *Método dos mínimos Quadrados*
- Pelo menos dois número super-híper-mega famosos foram mencionados nessa cadeira : **Gauss** & **Newton**.
	- Ambos envolvidos com astronomia.
	- Astronomia é um bom exemplo do que vai acontecer aqui.
- Observando as estrelas, teríamos que anotar o posicionamento de estrelas escrevendo seus ângulos, azimuth.
	- Porém, temos certos dias que não as vemos, e em outros dias podemos estar em outro lugar. Que pode quebrar nossos pontos de referência.
- JB mostrou alguma coisa no GNUPlot, medidas de alguma coisa.
	- Uma curva bem bonita.
- No exemplo do JB, temos um caminho. E um caminho ruim.
	- Tem espaços repetidos, espaços vazios ou esparços.
	- É um gráfico bem literal, não uma fórmula bonitinha.
		- Acho que à partir desses dados, poderíamos *prever* o comportamento dos corpos celestiais.
- JB fala que poderíamos mudar o cenário para *temperaturas do banho*.
- Uma '*nuvem de pontinhos*'.
- Dá pra arranjar uma função que *mais ou menos* passa por essa curva aí?
	- A função não conseguiria passar por todos os pontinhos, mas algo que me indique o caminho. O melhor mais ou menos que puder.


### Método dos Mínimos Quadrados
- Como encontro essa função? O que é passar pelos pontinhos mais ou menos? Que tipo de função?
	- Muitas perguntas a partir de dados brutos.
- JB julga que a função tem meio que cara de parábola. No achismo, ele comenta.
- No achismo, JB escreve : $f(x) = ax^2 + bx + c$. A parábola genérica.
	- Na parábola, seus coeficientes a 'controlam'
- No achismo de novo, JB vai colocar uma coisinha à mais :
	- **$f(x) = $ax^2 + bx + c + d * cos(x)$**
- Com isso, queremos encontrar a função que chega mais perto da nuvem de pontos.
- '*$f(x1)$ deveria ser bem parecido com $y1$...'
	- Mas o que é parecido?
	- Que a diferença fosse a mínima possível. $|f(x1) - y1|$
	- Isso, JB vai testar para todos os $i$
- $Sigma|f(xi) - yi| = min!$
	- Pra conseguir os controlar esse cálculo do mal, temos knbos do $a, b, c, d$ da função.
- Mas trabalhar com módulo é chato. Então não vamos trabalhar com módulos. Vamos trabalhar com **exponencial**!
	- $Sigma( f(xi) - yi )^2 = min!$
- Regular o $a, b, c, d$ nos ajuda para deixar isso o mínimo possível.
- Como se descobre o valor mais baixo de uma função?
	- Onde a $derivada = 0$. Assim encontramos o máximo e o mínimo. Literalmente o mesmo método.
	- Mas nesse caso, queremos o mínimo mesmo. E ele vai ser maior que zero, considerando que é a soma de um monte de gente positiva.
- Derivada em relação à que? A derivada de $a, b, c$ & $d$.
- Vamos nos concentrar no 'a' por enquanto. Por isso o quadro é grande.

### Derivada em $a$
- Uh oh.
- É só comprido, não é complicado.
- $Derivada-a$ $Sigma( f(xi) - yi)^2 = min!$
	- Que pode ser re-escrito como : 
	- $Sigma$ $derivada-a$ $( f(xi) - yi)^2 = 0$
	- Que é igual a : 
	- $Sigma$ $2( f(xi) - yi) *$ $derivada$ $f(xi) / da = 0$
	- 
	- $2Sigma ( f(xi) - yi ) * x²i = 0$
	- Posso jogar aquele dois fora? Ora, se duas vezes aquele treco é igual a zero... Posso jogar fora.
	- $Sigma ( f(xi)*xi^2 - yi*xi^2 = 0$
	- Conseguimos quebrar a soma!
	- $Sigmaf(xi) * xi^2 - Sigma$ $yi * xi^2$
	- 
	- $Sigma f(xi) * x^2 =$ $Sigma yi * x^2$
	- Seja lá o que for... é o $f$! Vai parecer que ficou um horror, mas estamos bem próximos do fim.
	- $Sigma(axi^2 + bxi + c + d * cos(xi) ) * xi^2 =$ $Sigma yi * xi^2$
	- 
	- $Sigma axi^4 + bxi^3 + cx^2 + dcos(xi) * xi^2 =$ $Sigma yi * x^2$
	- '*Posso quebrar essa tralha toda em pequeninos.*'
	- $Sigma axi^4 +$ $Sigma bxi^3 +$ $Sigma cxi^2 +$ $d * cos(xi) * xi^2 =$ $Sigma yi * xi^2$
- Desse jeito, tendo cada um separado, consigo passar cada um como constante.
	- $a *$ $Sigma xi^4 +$ $b *$ $Sigma xi^3 +$ $c *$ $Sigma xi^2$ + $d *$ $Sigma cos(xi) * xi^2 =$ $Sigma yi * xi^2$
- Mas isso, tendo a derivada baseada em '$a$'.
- O mais legal é que : mesmo baseando a derivada nos outros coeficientes, nada muda.
	- Essencialmente.
- A cada coeficiente passado, diminui um grau.
- O processo é todo o mesmo. Exceto pelo $d$, por causa do cosseno colocado.
- Com tudo isso feito, de $a$ -> $d$, temos um sistema linear.
- Tendo ele, o que podemos com ele?
	- Resolvê-lo.
- Cosseno foi no achismo total. Foi exatamente o que o JB falou.

### No final
- Resolvendo com Gauss, JB recebe certas quantias para cada um dos coeficientes. Com esses valores, plottando pelo GNUPlot a curva ficou bem parecida com a nuvem de dados que tínhamos antes.
- Isso nunca foi uma parábola.
	- O programinha que gera os dados, ele é $x^3$
