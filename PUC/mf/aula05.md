# Métodos Formais
## [18-08-26][mvfm]
---
### Aula como Sempre
- Terça-Feira que vem vamos ter uma aula magna, ou seja, NADA.
- Aparentemente a aula de hoje vai ser simplesmente uma aula de exercícios, focando especialmente para **Conjuntos Indutivos & **Equações Recursivas I**.
	- [Indutivos](./atividades/exind.pdf) : **(1e, 1h)**
	- [Recursivos](./atividades/exrec.pdf) : **(1d, 1e, 2)**
- ![Atividades Conjuntos Indutivos](assets/ind01.png)
	- Na atividades '**e**', palavras válidas poderiam ser : 
		1. aba
		2. aabaa
		3. abba
		4. aabbaa
	- Com isso, temos o seguinte axioma & regras :
		- **$/aba e S3$**
		- **$w e S3/ awa$**
		- **$wxw e S3 and w = a^m and x = b^m and m>0 and n>0 / wxbw e S3$**
	- Na atividade '**h**', construímos o seguinte axioma & regra de inferência :
	- O uso de $e$ é para simplesmente reprsentar o símbolo de '*pertence*'. Vai ficar feio.
		1. **$/ 0 e S$**
		2. **$n e S / 2 * n + 1 e S$**
- Regra de inferência :
	- **$a -> b = a / b$**
- Axioma :
	- **$t -> b = / b$$**
- Definição por indução necessita dos seguinte três passos para ser considerada válida :
	- Caso Base
		- Listar alguns elementos espcíficos de 'i'; pelo menos um elemento deve ser listado
	- Indução
		- Definir uma ou mais regras para a construção de novos elementos de 'i' a partir dos elementos já existentes
	- Fecho
		- Declarar que 'i' consiste exatamente dos elemento produzidos pelos passos da base e da indução.

### Atividades Recursivas
- ![Atividades Recursivas](assets/atrec.png)
