# Projeto & Otimização de Algoritmos
## [06-04-2026][mvfm]
---
### Karatsuba e o Fim de Divide-And-Conquer
- Não seguimos o problema da aula passada pois o JB quer aproveitar que estamos um pouquinho adiantados.
- Karatsuba vai ser o último algoritmo de **Divide-And-Conquer** que vamos ver esse semestre.
- Descrito como "*Algoritmo Lindo*" pelo JB.
	- É o outro algoritmo russo que ele tinha mencionado algumas aulas atrás.
	- Também serve para a multiplicação de dois números inteiros.
- Meados 1960
	- Matemático Komudgorov menciona em uma palestra que ele dá para o instituo de matemática em Moscow a "nova tecnologia"
	- **Computadores**
	- Primeiro ele levanto o ponto para o pessoal na palestra que o custo médio da **soma de dois números inteiros** é **O(n)**
	- Um problema linear pois se passa por cada casinha de ambos os números uma única vez. Nada de pulos
	- Ele faz isso para exemplificar o quão demorado a **multiplicação de dois inteiros** pode chegar a ser
	- "*Um de baixo multiplicando cada uma das casinhas do número de cima*" Repete isso por cada casinha do número de baixo.
	- Um problema quadrático O($n^2$)
- Após a palestra, Karatsuba vai para sua casa e reflete no que ele aprendeu. Nisso ele percebe que o algoritmo que aprendemos quando pequenos para multiplicações e divisões são **terríveis implementações** de um algoritmo de divisão e conquista.
- "*E se eu podesse dividir mais igualmente?*"
