# Projeto & Otimização de Algoritmos
## [29-04-2026][mvfm]
---
### Prefácio
- Este arquivo como fundamento teórico para a solução da lista de exercícios localizada [aqui](./lista.pdf). As soluções por si, estão [aqui](./solucaoLista.md). Nada muito complexo aqui, pois conhecendo o JB do jeito que o conheço, ele não vai se basear muito nas respostas teóricas.

### Algoritmos greedy
#### Principais exemplos : **Problema do Troco, Rock-Jumping, Codificação de Huffman, Escalonamento de Tarefas & Máquina de fitas**.
- Algoritmos greedy são consideravelmente simples de se entender & de se implementar em código.
- Requerem pequenas decisões locais que *devem* resultar em uma solução ótima geral.
- Os slides do Scopel definem algoritmos gulosos como : 
	'*É greedy se ele constrói uma solução com pequenos passos, fazendo uma escolha local (míope) a cada passo para otimizar um determinado critério ou função objetivo.*'
- O problema de algoritmos greedy é que eles não possuem **garantia** de uma solução ótima, por mais que tenhamos a escolha local bem determinada para a criação de uma sub-árvore ótima.
	- O exemplo que traz esse ponto à tona é justamente o problema do Troco. Por mais que o algoritmo se mantenha o mesmo, mudando os tipos de moedas disponíveis já podem quebrar com a sua funcionalidade.
- Descrito como sendo um algoritmo '*top-down*'
	- Isso significa que as escolhas míopes sempre vão depender de escolhas tomadas anteriormente, nunca vão depender de futuras escolhas.
	- Após uma decisão ter sido tomada, não conseguimos fazer um *back-track* dela.

### Divisão & Conquista
#### Principais exemplos : **Quicksort, Mergesort, Pesquisa Binária [em árvores], Camponeses Russos & Karatsuba**.
- Essencialmente, a divisão de um problemão gigante em vários probleminhas pequeninhos, recursivamente acumulando o resultados dos pequeninos para a resposta geral.
- Slides do Scopel focam bastante no uso do **Teorema Mestre**, mas nenhuma das aulas do JB fizeram uso dele. Por isso, assumo (com certo grau de confiança) de que o teorema não vai ser abordado na prova.
	- Porém, vou aproveitar um poquinho dos slides com certas definições bonitinhas que eles proporcionam.
- Algoritmos de divisão e conquista podem ser divididos (cool, huh?) em três etapas : 
	1. **Dividir** : Se a entrada é menor que um limite, resolve o problema utilizando um método direto e só retorna o resultado. Caso não seja, divide o problema em determinada fatia e os resolve recursivamente.
	2. **Conquista** : A parte recursiva, nele os pedacinhos menores tentam ser resolvidos diretamente. Caso não sejam, mesma coisa que a etapa anterior.
	3. **Combinar** : Combina as soluções da etapa anterior para gerar a solução final.
- Exemplo bem *visual* desses passos ocorrendo é Merge-Sort : 
	![Merge-sort em ação](assets/mergesort.webp)
