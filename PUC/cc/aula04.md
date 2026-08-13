# Construção de Compiladores
## [12-08-26][mvfm]
---
### Scanning
- Material de atividades, diponível [aqui.](./atividades/GeradoresECompiladores.pdf)
- '*Essa é a pior aula do semestre. Vai ser muito chato.*'
- Tareafas do analisador léxico
	```code
		entrada : if(x == 3) ...
		saída : IF LPAR IDENT EQ NUMBER RPAR ... EOF
	```
	1. Retorna símbolos terminais (tokens) : A cadeia de tokens deve sempre terminar com **EOF**.
	2. Despreza símbolos sem significado : espaços em branco, tabulações, fim de linha (CR/LF) & comentários.
	- Tokens têm estrutura sintática própria, descrita por gramáticas simples.
- Essencialmente mesmo material que foi entregue aula passada.
- Agustini tá escrevendo árvores de gramátiaca & precedência de operadores, mas não to conseguindo acompanhar. 
	- Porém, o material **da aula anterior** mostra exatamente o que ele está falando :
	![Gramática de Expressões Aritméticas](assets/Grams.png)
	![Precedência de Operadores](assets/Prec.png)
- A regra no C :
	- '*O else sempre pertence do if mais próximo.*'
	- Isso pois If's & Else's são inerentemente ambígua.
- Exemplo disso :
	![Arvore](assets/arvore1.png)
	![Arvore](assets/arvore2.png)
- '*Sem essas coisas de obsessão na disciplina.*'

### Por que a Análise Léxica não é parte da Sintática?
![Pq](assets/Pq.png)
- Cada letra do alfabeto ASCII por si só é uma expressão regular. A concatenação de pelo menos dois caracteres também é uma expressão regular.
	- **STRING VAZIA** também é uma expressão regular.
	![ER](assets/er.png)

