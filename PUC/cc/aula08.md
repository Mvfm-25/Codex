# Construção de Compiladores
## [16-08-26][mvfm]
---
### Ninguém fez o tema de casa.
- Ainda estmos vendo **Análiste Sintática**, que em qualquer outra fonte a gente vai encontrar com o nome de **parsing**.
- A principal diferença que o Agustini está reinforçando nas aulas é que com análise sintática, estamos trabalhando diretamente com **Autômatos de Pilha** & **Gramáticas Livres de Contexto**.
	- Ou seja, onde estavamos apenas *reconhecendo* trechos de texto na análise léxica, vamos estar vendo coportamento também.
	- Principal exemplo disso seria a continuidade do '{' para o '}'.
- E é justamente por isso que estamos usando das GLC's (Gramáticas Livre de Contexto)
	- Onde um AFD (Automato Finito Deterministico) não consegue lembrar do estado anterior, ele não consegue contar quantas chaves se abriram e quantas se fecharam.
	- Automatos de pilha já resolvem esse impasse facilmente.
- ![Situação de vantagem das AP's](assets/uso_glc.png)

### Livre de Contexto
- Agustini escolheu usar de uma definição mais abrangente de uma GLC, não diretamente a de Chomsky, mas a notação **Cocol/EBNF de Mössenböck**.
	``` code
		A -> α
	```
- Onde alpha é uma : **Sequência não-vazia de T & NT**.
	- O lado esquerdi é sempre para um único NT.
	- Principal fator que diferencia as GLC das Gramáticas Sensíveis ao Contexto.
- Exemplo :
	``` code
		Expr =	Expr "+" Term
			| Term
		Term =	Term "*" Factor
			| Factor
		Factor =	ident
			| "(" Expr ")" .
	```
- ![Funcionamento de um Automato de Pilhas](assets/em_pilhas.png)

### Some Dust in your Eye
- Nada é perfeito, nada é sem limitações.
- As GLC's possuem limitações que podem paracer bem familiares para qualquer um que já programou em alguma linguagem decente :
	1. Todo nome deve ser declarado antes do seu uso.
		- A declaração pertence ao contexto de uso; 'X = ' pode estar correto ou incorreto caso ele tenha sido declarado anteriormente.
	2. Os operandos de uma expressão devem ter tipos compatíveis
		- Fuck you in specific JS.

### Análise Top-Down
- Funcionamento direto de um AP passando por código GLC.
- A árvore criada pela AP é construída començando pelo símbolo incial (duh) em direção à sentença de entrada.
	- A cada não terminal, a AP decide que alternativa expandir olhando para a entrada que ainda falta processar ( o Look-Ahead que já vamos explicar )
- Gramática de exemplo :
	``` code
		A = "a" A "c" | "b" "b" .
	```
	- A alternativa correta leva em consideração :
		- O look-ahead da entrada.
		- O conjunto de símbolos 'iniciais' de cada alternativa.
- ![Exemplo com a entrada de **a b b c**](assets/uso_top-down.png)
- ![Uso do token look-ahead](assets/uso_la.png)

### Atividade de aula
- Resto da aula foi apenas a solução de uma atividade disponibilizada pelo moodle.
	- Schneider rodou tudo na máquina dele, mas com uso de um codespaces. Só pedir para ele o link depois e rodar por lá.	
	- Mas ajuda também já ter o ambiente do Jflex aqui.
	- Entrega dele ficou para **09/09**, mas não entendi se é marcado como T1.
