# Métodos Numéricos
## [12-05-2026][mvfm]
---
### Parquinhos
- Problema parecido com o enunciado do [Trabalho 1](./trabalhos/t1.pdf), envolvendo parquinhos de diversão e números de atendência.
- Traduz todo probleminha em :
	- $Ax = b$
- Agora pense em resolvê-lo múltiplas vezes.
- Para resolver um sistema, com o uso de **Gauss-normal** é ***cúbico***
- Temos um sistema para resolver : 
	- $Ax = b$
	- Existe alguma matriz que é bem fácil resolver o sistema dela?
	- Uma matriz com informação apenas acima da diagonal principal. Ou na própria diagonal em si.
		- "*Embora seja fácil de resolver, isso não é vida real.*"
		- Mas está perto.
	- O caso de "*Diagonal principal + acima*" é mais real. Mais honesto.
	- Simplesmente, os passos à frente de Gauss, Back-Substitution.
	- Caso tenhamos um sistema assim... Quanto custaria resolvê-lo assim? Com a diagonal principal + acima.
		- Max, Wide & Eu acreditamos que seria *N*, considerando que passamos por todas as linhas da matriz uma única vez. Porém, a quantidade de operações (somas, principalmente) vai aumentando a quantidade de somas para as linhas de cima.
	- De acordo com o JB, como estamos usando ${n^2}/2$, não tem como ser simplesmente **$n$**.
	- E como a teoria da complexidade desconsidera operações irrelevantes, a complexidade seria $n^2$
- Após isso, tendo da diagonal principal para cima, é uma **vantagem**.
- Assim, o espelhamento dele : **Diagonal principal, elementos abaixo** também ajuda bastante.

### A coisa legal de JB
- Ele vai mostrar um sistema não tão legal, e transforma-lôs nos últimos dois que vimos.
- O algoritmo se chama **Decomposição LU**.
	- "*Transforma um sistema complicado em sistemas fáceis.*"
- Pegamos o exemplo de $Ax = b$
	- A partir dela, vamos procurar duas matrizes **L** & **U** que, multiplicadas, resultem em **A**.
	- Queremos que elas tenham um formato especial. A **L** é : **Diagonal Principal + Números abaixo.** A **U** é o espelhamento.
- L & U significam Lower & Upper respectivamente.
- $Ax = b$ -> $A = L * U$ & $L * U * x = b$
- O que é resultado de uma matriz vezes um vetor? Um vetor.
- U, uma matriz, está multiplicando um vetor, x. Portanto $U * x$ é um vetor. Vamos chamá-lo de **$y$**
	- Caso a gente saiba quem é $y$, conseguimos dizer que : $L * y = b$
- "*Não parece que o problema acabou, mas ele acabou.*"
- $Ux = y$	\
	- $Ly = b$\
- O baixo de cima.
- Custou 3 preços :
	1. $n^2$
	2. $n^2$
	3. $L * U$
- Mas, resolvendo o sistema várias vezes, eu preciso encontrar o **LU** uma única vez!
	- O que já tira muito do custo anterior!
- Sempre achamos $LU$? E quanto custa achar $LU$?
	- Se dá pra resolver um sistema, sempre vamos achar um $LU$
	- Mas... Achar $LU$ custa $n^3$. O mesmo de Gauss. Mas eu só o encontro uma única vez! Não preciso resolver **Gauss** múltiplas vezes!

### Finding private L * U
- E agora?
- Sor resolve isso em um programinha **LU.awk**
- Na diagonal principal da Matriz **U**, temos apenas *1*, no exemplo do JB.
	- O que quer dizer que não precisariamos guardar a diagonal principal.
- Tu resolve Gauss para encontrar LU.
	- No programa do JB, resolvendo gauss a mesma matriz que ele descobriu a LU, os aux's que ele usou para resolvê-la são os elementos abaixo da diagonal principal em **L**.
	- E para a matriz U, são os elementos finais da execução de Gauss.
	- Como a diagonal principal da matriz L são apenas 1's, simplesmente ignorá-los. Tanto que na versão compactada de LU, a diagonal principal de L é simplesmente ignorada e por cima dela está a matriz principal de U.
- Bem legal.
- A parte chata, é ter um problema para resolver com esse método.
	- O que o JB implica é que : poucos problemas do tipo existem.
- Se para encontrar LU é simplesmente fazer Gauss uma única vez, o que pode incomodar é quando somos forçados a usar o Pivotamento. Que pode nos incomodar em descobrir que linhas são que linhas.

