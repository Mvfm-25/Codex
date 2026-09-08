# Métodos Numéricos
## [03-09-26][mvfm]
---
### Como tudo se resolveu
- Vamos encontrar um jeito que encontra todas, mas pra saber que são todas temos que saber quantas são. Com essa limitação, vamos trabalhar apenas com polinômios.
	- SÓ funciona com Polinômios
- Mais ou menos por 1968, mas começou em 1891. **Weierstrass**.
	- Na mão ele encontra um jeito que encontra TODAS AS RAÍZes de dado polinômio
- Os métodos de '60 '66 & '68 são apenas evoluções do método de Vierstraz.
- Mas um artigo que o JB encontrou, artigo de 2020, que mostra que os métodos que funcionam muito bem não foram provados. Mas os métodos provados não rodam muito bem.
	- Mas como?
	- JB vai pesquisar mais. Okay.

### O que eu vou contar hoje é tranquilo
- Vamos focar no método de '68.
- Funciona bem, tranquilo & sólido, mas é talvez sacana em algum ponto. Não se é certo.
- Mas vamos falar sobre : **Método de Aberth**.
	- Já nasce no mundo dos computadores, não parecido com Weierstrass.

### Método de Aberth
- Não vamos implementer ou ver a implementação. 
- Mais sofisticado de código, não simplesmente de fazer à mão.
- Só vários newtonzinhos correndo pelo mundo cartesiano para encontrar as raízes.
	- Mas é bem falho, pois ele pode continuamente encontrar a MESMA raíz múltipla vezes. Imagina um polinomio de 70 raízes.
- Aberth modifica a ideia inicial de **Bini**, para ter o próprio Método.
	- Ideia legal, mas difícil de explicar.
- Repulsores de newtons, essencialmente, foi a maneira de fazer com que os newtons NÃO caissem na mesma raíz.
- Cargas de elétrons foi a melhor maneira que o JB encontrou para explicar o que tá acontecendo por cima da matemática. Não vamos ver a matemática por baixo do método.
