# Projeto & Otimização de Algoritmos
## [13-05-2026][mvfm]
---
### O que fizemos aula passada?
- Aula passada fizemos a 'implementação' do problema de N-Rainhas.
	- JB comenta que não escrevemos o código pois ele já tinha escrito. A implementação parece ter **8 linhas** de tamanho.
- Agora JB está mostrando sua implementação do problema do T1.
	- A implementação durou **12s**.
	- Oh well.
- O algoritmo se baseia em divisão & conquista.
	- Como não se dá para dividir as minas, dividimos apenas o espaço que estamos procurando.
	- Ele segue mais ou menos com a lógica que eu tinha entendido também, que o espaço verdadeiro seria o espaço além da primeira mina. '*mina.x + 1*', mas ele leva em consideração também múltiplos quadrandtes, não só um único como eu fiz.
	- São quatro recursões por mina. *Cima, baixo, esquerda, direita*.
	- *Bem malandro.*
- Bem massa. Muito divertido.
- "*Vamos começar a aula hoje com alegria & descontração!*"
	- "*Belas garotas!*"

### Vênus de Milo
- JB começa com uma imagem da pintura de Vênus (por alguém que não me lembro de seu nome) e por cima, ele tem um algoritmo que está resolvendo um labirinto com o que parece ser **Depth-First-Search**. Que é de fato, um algoritmo de backtracking.
- Algo que já vimos em **Alest II**. Mas lá, vimos uma implementação em Grafos.
	- Mas o comportamento é o mesmo.
	- O que implica que vimos backtracking um pouquinho lá já.
- Mas em caminhamento em largura é diferente, pois ele nunca toma a decisão de voltar e melhorar. Ele se expande por todas as direções e tem a sorte de achar o final.

### Algo bem disruptivo & Legal
- Escolha um número inteiro. Só.
- Vamos somar todos os números de todas as pessoas & tentar quebrar em 2.
	- Caso a soma seja um número ímpar, não vamos conseguir fazer essa quebra.
- Carro usado de Wide foi vendido.
	- Grupo 1 tem a soma inteira, Grupo 2 tem 0.
		- Leva o maior integrante do grupo 1 e o leva para o grupo 2.
		- Fica movendo carinhas do Grupo 1 ao Grupo 2 até as somas de ambos os grupos seja igual. Mova de volta o elemento para o Grupo 1 caso estoure a soma.
