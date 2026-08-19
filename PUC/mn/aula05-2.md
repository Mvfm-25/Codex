# Métodos Numéricos
## [18-08-26][mvfm]
---
### Algo além de IEEE
- Assunto interessante e legal de hoje : polinômios.
- Vamos mostrar um exemplo bem fofinho :
	- $p(x) = 3x^4 - 16x^3 + 9x -8$
- Mostramos o fofinho pq a cara genérica é bem chatinha :
	- $p(x) = amX^m + am-1X^{m-1} + ... + a1x^1 +a0$
- Um polinômio tem seu grau, especificado pelo expoente maior presente. E quantidade de coeficientes, a quantidade de *coisas* no polinômio.
- Por que estamos interessados neles?
	- Pois eles são fofinhos
	- São fáceis de se trabalhar com
	- Fáceis de se derivar, fáceis de se integrar.
	- Conseguimos transformar uma função qualquer e transforma-la em um polinomio fofinho.
		- Ou seja, uma série de taylor.
		- Um preço a pagar por isso : usar um ponto da função como âncora. Ela não traduz/imita corretamente 100% verdadeiramente a função. É apenas uma aproximação, baseando-se nessa âncora escolhida.**
	![Série de Taylor](assets/taylor.png)
- **-num era a dúvida do Wide.**
- '*Quase tudo é mais fácil com polinomios*'
	- O que não é?
- É mais difícil **achar raízes** de polinômios. Trabalhoso e complicado, tão quanto em funções normais.
	- E infelizmente você muitas vezes precisa encontrar tais raízes.
	- Pelo menos, no polinômios sempre vamos saber quantas raízes vamos ter. Olhando diretamente para o grau.
- Como achamos as raízes de um polnômio?
	- De grau dois : Baskhara / Formula Quadrática.
	- De grau 3 : Fórmula Cúbica.
	- Para grau 4 também temos fórmula.

### Lá em 1600
- Já tinhamos essas fórmulas, pelo menos até grau 4.
	- E para grau 5? Temos?
- Em 1830, se foi determinado :
	- **Não. Não se tem COMO criar uma fórmula para grau 5.**
- Corta para hoje, e ainda estamos encontrando maneiras *mais fáceis* de encontrar as raízes de outras maneiras.
- Vamos pegar um polinomio de exemplo :
	- **$4x^5 - 6x^4 + 12^3 - 17x + 9$**
- "*Um desses carinhas eu sei que tem uma raíz.*"
	- Qual o erro da frase?
	- Se um cara tem grau 5 ou 4, ele tem 4 ou 5 raízes. Não menos, não mais.
- Para o cara com grau 4, o grau é par. Quando temos um número negativo, positivo, elevados na quarta ficam como?
	- O negativo elevado à 4 fica positivo. O positivo se mantem positivo.
	- Ele vem do positivo e vai para o positivo.
- '*Um número negativo na 5 é BEEEEEEEEEEEEEM negativo*'
	- Mas o positivo se mantém positivo.
- Mas o bom é : o polinomio é contínuo. Ele é obrigado à pelo menos ter *uma* raíz.
- '*As raízes que te faltam podem ser números complexos*'
	- POr isso que tínhamos certeza que o de grau 4 não era evidente ONDE estavam as raízes.
	- Números complexos dependem de números **imaginários**.
- Na representação gráfica de um polinomio de grau 4 não vemos uma intersecção. Ou seja, **todas as raízes são números complexos**.
	- E como as enxergamos? Olhando para o plano complexo.
- Podemos pelo menos colocar o eixo real em uma direção e o eixo imaginário em outra. 
	- Isso pois os complexos são compostos por uma parte real & parte imaginária.
	- **$6,21 + 3,12i$** A partezinha com 'i' é a imaginária.
- Notações adicionais [aqui](./aula05.md)

### Onde estão as minhas raízes?
- Regra de Descartes nos ajuda nesse quesito. Ela nos diz **quantas raízes são positivas**
- Vamos com o exemplo : $4x^5 - 6x^4 + 12x^3 - 17x + 9$
	- Quantas vezes o sinal foi trocado?
	- Quatro vezes. De acordo com Descartes, temos **4 ou 2 ou NENHUMA** raíz(es) positivas.
	- Esse número caí de 2 em 2. Por que? No futuro vemos isso.
- E as negativas? Como usamos Descartes?
	- Não do mesmo jeito, é claro.
	- A gente começa a se preocupar com os expoentes sendo ímpares/pares & o sinal do coeficiente. Isso já muda como contamos a quantidade de trocas.
	- No exemplo de cima, está confirmada que temos **1 negativa**. 
- Mas agora... Temos certeza das negativas, mas ficou ambigua a quantidade de positivas & complexas.
- Quotas, para definir uma área de onde estão nossas raízes. Um '*está por aqui, não olha pra fora dessa caixinha.*'
	- Cauchy -> Vamos ver.
	- Lagrange -> Vamos ver.
	- Fujiwara

### Cauchy
- a MENOS simples das cotas simples.
- $1 + max {|a0/am|, |a1/am|, |a2/am|, ... , |am-1/am|}$
	- Os números '*a*' são os coeficientes do nosso polinomio.
- Exemplo com : $**p(x) = x^4 + 6x + 10**$
	- 1 + max {|10/1|, |6/1|} = 1 + max{10, 6} = 11.
	- Coeficiente da ponta não conta.

### Lagrange
- $max(1, soma(|ai/am|) )$
	- Soma tudo, que nesse caso vai dar 16, e encontra o maior entre '1' e o resultado da soma.
- Cauchy é mais informativo é o mais apertado.
