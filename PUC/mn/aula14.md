# Métodos Numéricos
## [16-04-2026][mvfm]
---
### Método de Gauss
- Vamos ver o método mais simples "*dos três que veremos esse semestre.*"
	- O engraçado é que os outros dois também são com **Gauss** no nome.
	- *Gauss-Jacora* & *Gauss-Seidel*. 
- Iterativos : **saem procurando pela raíz**.
	- Caso o sistema seja mal-condicionado, erros se acumulam e pode estragar tudo.
- O que pode ser mal-condicionado?
	- Um pequeno erro de arredondamento?
		- Tendo um poquinho disso, a solução se **mexe** bastante no quadro.
		![[condicionado.excalidraw | 100%]]
	- Um sistema mal-condicionado em duas dimensões é bem ruim.
	- Em três piora, assim como em quatro, cinco, seis e por aí
- Vamos ver Gauss em um sistema $2x2$, do jeito mais boboca de todos.
- Exemplo dado : 
	$3x + 2y = 6$
	$2x - y = 4$
- Matriz $a$ = [3, 2][2, -1]
- Matriz $x$ = [$x, y$]
- Matriz $b$ = [6, 4]
- JB então faz uma pequena recapitulação do uso de **Gauss** de nossas aulas de **ALGA**.
	- "*Tu pode operar, mas os resultados não vão estar se alterando. Não te preocupa.*"
	- Eliminação de variáveis. Zeramos o $x$ da linha dois para simplficar e, eventualmente, encontrar o valor de $y$.
	- Uma matriz $3x3$ é na real $4x3$ para segurar a coluna que representa a matriz $b$
	- **Eliminação de Gauss**.
	- *Back-Susbstution*, lol okay.
- JB mostra um pequeno scriptzinho **.awk** para mostrar a eliminação de Gauss em execução.
	- Bem legal.
	- $if .equals(4) : = 0$
- Os valores das últimas colunas da matriz $a$ são os que mais demoram para serem encontrados.
	- E caso exista um erro antigo de colunas anteriores, poderiamos **contaminar** a tabela inteira.
- Isso é combatido com o uso de **Pivotamento**.
- *Trabalhar com números menores dá menos chance de dar cagada.*
	- O uso de números menores se dá pelo contexto de **IEEE**?
		- **SIM!**
	- FUCK YOU ZAUSS
- Subtração **CATASTRÓFICA**
