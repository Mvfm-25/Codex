# Projeto & Otimização de Algoritmos
## [08-04-2026]
---
### O que faremos hoje
- Retornamos para o prédio 32 hoje
- Não teremos mais programas de Divisão e Conquista, mas algo *na mesma família*.
- **Programação Dinâmica**
	- Nâo necessariamente acadêmicamente considerado como uma subdivisão de **DC**, mas o JB entende que sim.
	- Centrados em recursividade
	- JB explica que recursividade é basicamente um *Diminuição & Conquista*.
- Linha de pensamento de algoritmos de Programação Dinâmica.
![[dinamica.excalidraw | 100%]]

### Problema das Pedrinas
- Castelo da princesa Isadora, com um pequeno recantinho uns 75metros de distância do Castelo
- Ela vai construir uma pequena estradinha de ponto a ponto
	- Pedrinhas de 1 largura X 2 altura, podem ser posicionadas de pé ou duas deitadinhas, pra cobrir o buraco em cima.
- Bastante gente já pensando com as árvores que JB normalmente nos traz para as situações.
	- Cadu começou com as variações de 3 pedrinhas
		- Três seguidas de pé
		- Um conjunto de deitadas, uma de pé
		- Mesma situação, do lado contrário
	- Nisso, ele tem uma pequena continha de (**Tamanho disponível, Quantas pedrinhas eu coloquei**)
		- Ele desenha uma árvore exemplificando o que ele tinha mostrado.
- Sor continua com o raciocínio do Cadu, com árvorezinhas e quantidades **restantes de espaço**.
![[pedrinhas01.excalidraw | 100%]]
- Sor adota mais ou menos o raciocínio que eu estava tendo, de primeiro pensar no cenário final.
	- Estrada de tamanho **N**
	- Estrada de tamanho **N-1**, só nos resta montar a pedrinha de largura 1
	- Estrada de Tamanho **N-2**, nos resta montar duas pedrinhas de largura 1, ou uma de largura 2.
- JB faz isso para nos trazer o raciocínio recursivo primeiro.
- Uma recursão primitiva é montada
	- $Cm = (Cm - 1) + (Cm - 2)$
- O que se falta, agora são os casos bases.
	- Com os caso base de :
		- Caminhos de Espaço $0$ : **1**
		- Caminhos de Espaço $1$ : **1**
- Ao decorrer de cobrir os casos de Caminhos Espaço 2, 3, 4, 5,& 6 foi observado que os resultados são iguais à **Fibonacci**.
- Então a solução para o caminho de tamanho $75$ é Fibonacci de $75$.
	- *Btw : Fibonacci de $75$ é = $2,111,485,077,978,050$*
- Estamos atolados na situação de **encontramos a solução recursiva, mas ela é bem lenta.**
	- Aceleramos a solução recursiva **OU** removemos a recursividade.

### Pedrinhas Coloridas
- Agora as pedrinhas são coloridas. Estando de pé, são azuizinhas em cima e branquinhas em baixo.
- Cadu sugere que árvores ainda podem ajudar, mas vão ter que criar mais galhos para acomodar as novas situações possíveis.
- Com quadradinhos coloridos, ainda seguimos com o mesmo raciocínio, mas consideramos muito mais possibilidades.
	- Estradinha de espaço 1 : $2$
	- Estradinha de Espaço 2 : $8$
