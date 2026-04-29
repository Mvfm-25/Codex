# Métodos Numéricos
## [28-04-2026][mvfm]
---
### O que estamos fazendo agora
- Nesse ponto do semestre, estamos vendo **Sistemas-Lineares & como resolvê-los.**
- Por enquanto vimos apenas um único método para resolver Sistemas Lineares : **Gauss**
- Hoje veremos **Gauss-Jacobi** e, caso reste tempo, **Gauss-Seidel**. 
	- Principal problemas que vimos, além daqueles que usamos de exemplo para re-entender o uso de Gauss, foi aquele do planeta Zorg.
- JB aponta que tendo $0's$ na diagonal principal é desagradável em um contexto de informática e para isso, usamos pivotamento. 
	- Mesmo não tendo esse caso da diagonal principal, o pivotamento ainda é usado para lidar com números menores. Deixando o resultado final mais preciso levando em consideração de CPU's IEEE-754.
- **Gauss** é denominado como um *método direto*. Ele também avisa que ele vai ser o *único* direto que veremos.
	- A definição dele de direto é : 'Métodos que não tem passos pós o retorno da resposta, de correção ou alinhamento.'
	- Visto como o '*único lado negativo de Gauss*'
- **Gauss** também parece não ser muito econômico. Em um sistema $1k x 1k$, **Gauss** é bem caro. $O(n^3)$.
- JB comenta que o parque olímpico de Munique é simplesmente incrível.
	- O sistema para a criação do parque olímpico é visto como um *sistema enorme*. Leve em consideração também que nos anos 70's, os computadores eram **PÉSSIMOS** comparados com os atuais.
	- Os engenheiros simplesmente não resolveram o sistema. Usaram cabos **extra giga-enormes**.
	- Human ingenuity.
- Um [código awk](/home/mvfm_/penguosis/prog/awkCoisas/xx.awk) foi disponibilizado para a aula de hoje.

### Gauss-Jacobi
- Um método **iterativo**.
	- Assim como o método de Newton que vimos antes.
	- Ele 'sai por aí'. Poderíamos 'deixar rodando' para chegar cada vez mais do resultado *real*.
- Por que não simplesmente só usamos esse método? O outro não é simplesmente inútil?
	- Pois ele pode sair pulando por aí e não achar nada. Não se há garantia de resultado.
	- Obrigado Germano pela observação!
- Schneider sugere usar em conjunto ambos os métodos. Usar **Gauss** normal primeiro e depois o de **Gauss-Jacobi**.
	- JB comenta que parece razoável, mas **NÃO!**
	- Por mais que **Jacobi** inicia em um ponto agradável, ele ainda tem o potencial de simplesmente fugir da solução.
- Mas como?
	- Por meio de duas regras, aponta JB.
	- O sistema tem que ter uma certa *cara*. A outra é bem mais *enrolada*, pago caro de ver.
- Por mais que o sistema não cumpra as duas propriedades, ainda sim seria possível encontrar uma resposta agradável. Mas não me dá fé não seguir essas propriedades mágicas.

### Funcionamento de Gauss-Jacobi
- O que significa ser um sistema linear
	- Que as variáveis estão separadas de cada uma
	- Não tem log, cos, sin
	- E mais alguma outra coisa...
	- Que conseguimos isolar as variáveis.
- Dado o sistema : $3x - 4y + 7z = 8$ | $6x + y + 2z = 5$ | $x +2y - z = 4$, conseguimos isolar cada variável da seguinte maneira : 
	- $x = (8 + 4y - 7z) / 3$
	- $y = 5 - 6x - 2z$
	- $z = -4 + x - 2y$
- JB testa o sistema com **variáveis chutadas** por uma aluna.
	- Os números, de acordo, foram : $3, 8, 4$.
- Com eles, conseguimos os seguintes resultados : 
	- $x = 4, y = -5, z = 15$
- Após isso, corrigimos os números chutados baseando-se nos resultados dos das linhas em seus estados originais.
- Esse processo só se repete vez após vez com esses números novos.
	- Pós-correção : $x = 4, y = -5, z = 15$
- Qual pode ser a condição de parada? 
	- Caso consiga resolver o sistema original. Usa os números encontrados, e vê se fica muito perto do resultado original.
	- Outra condição de parada é quando os números encontrados não fiquem muito diferentes dos resultados anteriores.
- Rodando esse exmplo no código disponibilizado, os resultados eventualmente se tornaram $nan$.
- O método de **Gauss** normal funciona direitinho.
	- *Resolve rindo*.
- A propriedade simples mencionada anteriormente diz que :
	- *Se a matriz for diagonalmente dominante, o sistema converge.*
	- O número que está na diagonal, tem que ser um número grande.
	- Esse cara da diagonal A[i][i] tem que ser **MAIOR** que todo mundo da mesma linha, somados.
		- Posição tem que ser $i = j$ para o posicionamento do item.
- JB diz que conseguimos **DEIXAR** uma matriz diagonalmente dominante.
	- Wuh huh?
- Simplesmente movendo as incógnitas entre linhas.
- Esse *fazer* dominante explica bastante aquele negócio que o JB que a *estrutura* da Matriz que complicava as duas propriedades mágicas.

### A Segunda Propriedade Mágica
- Que suspense.
- Wide está comendo Mel de novo. Incrivelmente na aula do JB de novo.
- Na matriz do exemplo anterior, JB comenta que, amarrada à ela, vem **três** matriz secretas.
	- [x1, y1, z1], [x2, y2, z2], [x3, y3, z3]
	- E além disso, temos outros **três valores secretos** : $Alpha 1, Aplha 2, Alpha 3$.
- São chamados de **Auto-vetores & Auto-valores** respectivamente.
	- É comentado que eles são bem caros de se encontrar.
- Multiplicando a matriz normal, por uma das auto-vetores recebemos de volta uma **quase-cópia** das auto-vetores.
	- O que corrige o **quase** seria a multiplicação com o **valor Alpha** adequado.
	- Fazemos esse multiplicação pois essas **quasi-autovetores** podem voltar com o tamanho errado. Um poquinho pra cima, um pouquinho pra baixo.
	- Super-importante em outras áreas. Não na computação.
- A segunda propriedade mágica é :
	- **Encontrar o maior auto-valor**
	- Verificar se ele é menor que 1.
	- Caso seja, o sistema vai.
- Mas como comentado anteriormente, é muito, **MUITO** caro encontrar esses valores.
	- Esse valor muito, **MUITO** caro de se encontrar se chama $Raio Espectral$.
- O método que veremos na próxima aula é **Gauss-Seidel**, que trz muito do que já descobrimos de Jacobi. Com algunas à mais.

