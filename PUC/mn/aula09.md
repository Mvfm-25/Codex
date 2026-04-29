# Métodos Numéricos
## [31-03-2026][mvfm]
---
### Polinômios
- JB mostra em um gráfico psicodélico dele um polinômio de oito (8) raízes.
	- Com isso, uma pergunta surge.
	- O que pode ser tal pergunta?
	- *Como que ele sabe que região ele começa mostrando, para mostrar as 8 raízes?*
		- Ou seja, como determina a escala final do gráfico.
- Pelas cotas?
	- *Mais ou menos*.
- Aprendemos as cotas no mundo dos reais, não dos complexos ainda.
	- Posso usar de boas no mundo dos complexos?
- No mundo dos complexos, as **cotas** ajudam muito mais.
- Ao invés de serem apenas **dois pontos** para determinar um início e fim, no mundo dos complexos as cotas determinam um **raio** no gráfico.
	- Isso engloba muito mais, retornando o mesmo único número que antes retornava.
- Separar o mundo em dois mundos
	- Polinômios 
		- *Já sabemos bastante.*
	- Funções qualquer	
		- *Sabe-se muito pouco, mais difícil.*
- Para polinômios de **quinto grau** : é sair se procurando. Não se existe fórmula.
- Para **funções qualquer** : larga Newton e vê o que tu encontra.

### 1950-ish
- Temos computadores. Que podem fazer coisas legais.
- Força bruta? Com força bruta passamos a função de 8 raízes e faz esse *larga Newton* pra ver o que ele me encontra.
	- Esse plano tem um pequeno defeito : *Desse método, é possível encontrar a mesma raíz múltiplas vezes.*
	- **À medida que eu vou encontrando novas e novas raízes, MAIOR a chance de re-encontrar raízes passadas.**
		- É o processo que eu **sei**. Não o mais bonitinho.
- O que vemos na visualização do Newton?
	- Os coloridinhos estranhos representam **as raízes de cada região**, o raio que foi determinado anteriormente.
- O gráfico é **O Fractal De Newton**, cada regiãozinha colorida uma raíz diferente.
	- A mínima mudança de ponto pode levar para uma raíz diferente.
	- Por isso resulta em uma fractal?
	![Newton Fractal](assets/newtonfractal.png)
- Um problema foi resolvido em **1968**.

### Método Bini && Aberth
- São processos que encontram **TODAS** as raízes de **uma única vez**
	- Nenhuma raíz atrapalhando outra.
- **Método do Bini e de mais um fulano** Aberth e mais outro fulano. JB esqueceu de novo.
	![Método de Aberth](assets/aberth.png)
	*Método de Aberth*
- *Se eu sei que tenho 8 raízes, eu posso lançar 8 Newtons*
	- Mas nenhum deles pode ir para o mesmo lugar.
- Para isso, eles formularam um mecanismo para fazer com que isso não aconteça. Fazer com que os Newtons não se batam.
- Cargas elétricas? Positivo & Negativo se atream. Positivo e Positivo se repelem.
	- As raízes possuem cargas? A ideia princpial é jogada ao ar.
	- Raízes possuem carga positiva no exemplo do Sor.
	- Raízes não se mexem.
	- Newtons possuem **o sinal contrário**. Oito Newtons jogados ao redor do gráfico.
		- O Newton é atraído para uma raíz e ele **PODE** andar
	- Essa história não é necessariamente o que acontece no algoritmo, é só uma história.
	- Positivos são neutralizados por Negativos, fazendo com que outros negativos não sejam atraídos pra lá novamente.
	- Isso não muda o polinômio.
	- *É um mecanismo bem esperto.*
	- **Os oito Newtons não andam ao mesmo tempo.**
- Dois alunos são usados como cargas elétricas para mostrar que quando se movem ao mesmo tempo com o intuito de chegar em uma raíz, é possível (**ridiculamente improvável**) que eles sejam eternamente repelidos e nunca conseguindo chegar à raíz.
- [Artigo da Wikipédia sobre o método de Aberth, não acho que vou conseguir acompanhar o JB](https://en.wikipedia.org/wiki/Aberth_method)
- Basicamente, implementa-se um comportamente de **IA** nos Newtons.
	- I know right.
	- Valores resultados de uma formulona matemática representam a **vontade** de um Newton de querer seguir uma direção para achar uma raíz.
- *Como que tu pensou numa dessas?*
- Quase funcionaria para uma função qualquer, mas o que lhe resta é a garantia da quantidade de raízes em uma função.
