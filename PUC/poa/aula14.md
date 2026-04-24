# Projeto & Otimização de Algoritmos
## [15-04-2026][mvfm]
---
### Aula passada
- Aula passada foi continuação de de programação dinâmica
- JB passou já pelo problema de construir uma estrada de tamanho $n$ usando :
	- Bloquinhos de **1m de largura, 2m de altura**
	- Tais bloquinhos poderiam ser posicionados de pé, ou dois deitadinhos um em cima do outro para compensar pelo 1m não coberto.**
	- Solução foi uma recursão bem simples. Literalmente Fibonacci.
- Depois disso, ele mostra o mesmo problema, agora com as lajotinhas sendo pintadinhas na parte de cima com a cor azul.	
	- Problema era descobrir a quantidade de **variações**
	- Resolvido novamente por uma recursão bem simples, bem parecida com fibonacci.
- Úlitmo problema foi um problema em que agora as lajotinhas eram completamente pintadas de uma única cor sólida
	- Elas sendo **Azul, Verde, Roxo & Marrom.**
	- Mesmo problema, tentando encontrar total quantidade de variações
	- Mas agora com uma restrição que duas lajotinhas marrons não podiam estar lado à lado
	- Novamente, uma recursão bem simples.
- Com o final disso, JB mostra que com o uso de **Memoização**, conseguiriamos podar esssa árvore *gigantérrima* para evitar o re-cálculo de valores que já descobrimos.

### Nova aula.
- Ainda esperando JB aparecer na sala.
- Gente aparcendo lentamente pra aula, coisa de faltando 4min ainda falta metade da turma basicamente.
	- As fileiras centrais praticamente vazias.
	- Mais ou menos o que acontecia nas cadeiras tipo Cálculo II.

### Recursões & Porque as odeio
- JB comenta coisa que ele tinha comentado ontem que chegou um certo ponto que a recursão não era tão obviamente sobre seu problema.
	- Basicamente um gerador mágico de números.
- Ele adiciona também que as três etapas que ele tinha estabelecido antes de :
	- **Recursão -> Aceleração / Sem Recursão**
- Simplesmente complica cada vez mais a complexidade.
- Wide vai ao quadro tentar seu peixe.
	- $(k) resto$
	- Wide determina que $k$ é a quantidade de rosquinhas, uma possibilidade de entrega. $resto$ é o restante de $(n - k)$, ou seja, qualquer um que não tenha recebido uma rosquinha.
	- Tira uma de $k$ e manda para $resto$. De acordo com o Wide, isso conta como outra possibilidade.
- É parecido com a ideia que eu tive com as **árvores**, que eu e outro colega pensamos.
- JB '*formaliza*' um pouco o problema.
	- Estamos procurando $Rn, k$. $R$ vindo de *rosquinhas*.
	- $R2, 1 = 2$. Tendo uma única rosquinha, com duas pessoas posso dar uma rosquinha para cada um individualmente.
	- $R1, 1 = 1$ | $R1, 0 = 1$ | $R2, 2 = 1$
- Tentamos procurar todas as maneiras possíveis de encontrar todos aqueles que **não conseguem** as rosquinhas.
- Criamos certas verdades : 
	- $Rx, x = 1$ | $Rx, 0 = 1$ | $Rx, 1 = x$ | $Rx, x-1 = x$
	- A última verdade foi introduzida pelo **Cadu**.
- Pensando um poquinho de maneira recursiva, criamos dois casos base : 
	- $n - 1, k - 1$ Percebo a pessoa e, ela recebe uma rosquinha.
	- $n - 1, k$ Percebo a pessoa e, ela não recebe uma rosquinha.

### Eu odeio ele
- é só um problema de combinatória, JB **ODEIA** o aluno que sugeriu o uso da formula combinatória
	- Queremos o caminho de lágrimas e recursão, não algo simples & verdadeiro.
- O que importa é ** o porque e o daonde.**
