# Construção de Compiladores
## [19-08-26][mvfm]
---
### Resultados 
- Gramática = {Terminais, Não-Terminais, Produção, }
- No caso do exercício da aula passada, em json :
	- Terminais -> '{', '}', STRING, ':', ',', '[', ']', NUMERO.
	- Não-Terminais -> JSON, OBJECT, MEMBER, ARRAY, ELEMENTOS, VALUE. 
- Léxico não diz se está faltando colchetes, chaves. Ele simplesmente retorna o que ele conseguiu ler.
	- Problema do movimento, automatos finitos não tem memória. Ele pode simplesmente andar.
	- Só preciso saber onde estou.
	- Vamos ver máquinas de pilha futuramente para lidar justamente com esse caso.
- \"[^\"]*\" {return STRING;}
	- Reconheci uma string!
- [0-9]+(\.[0-9]+)? {return NUMBER;}
	- Reconheci um número!
- Muita coisa do que eu estava me confundindo ser léxico é na verdade **sintático.**
	- Justamente pela limitação dos Automatos Finitos. Nada de memória.

### Análise Sintática
- "**Procedimento que verifica se um programa p pertence a uma gramática G(p E L(G))
	- Retorna simplesmente sim ou não se programa pertence a determinada linguagem.
	![Análise Sintática](assets/ansin.png)
	- Só sabemos se ele parou quando ele montou uma árvore de decisão. Máquina de pilha, sempre para.
- "**Se vocês colocarem apenas 'ERRO' ou 'ERRO SINTÁTICO', vão perder 1,5**"
![Abordagens da análise sintática](assets/abordagens.png)
![Restrições de tais abordagens](assets/restrictions.png)
- As duas respostas do semestre :
	- Vareia
	- Por Pilha
- "**Tem que ser rápido, se não... Não funciona.**"
- Ao invés de ter,em analisadores descendentes. :
	- CMD -> if(e) cmd fi
	-	|if (e) cmd else fi
	-	|o
- Por termos MUITA coisa em comum em caminhos diferentes, ele deixa de ser determinístico. Para resolver isso, 'fatoramos à esquerda'.
	- CMD -> if(e) cmd R
	-	|O

	- R -> ELSE CMD
	-	|E
