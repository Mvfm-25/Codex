# Projeto & Otimização de Algoritmos
## [11-03-2026][mvfm]

### Rock-Jumping
- Problema dos tijolinhos, mais ou menos
- **Wide** descrito como um explorador misterioso
- O explorador se depara com um caminho perigoso, um rio de corrente forte com pequenas pedras formando meio que uma ponte para o outro lado
- O explorador consegue determinar que consegue pular de pedrinha em pedrinha para atravessar o caminho.
![[assets/pedrinhas.excalidraw | 100%]]
- O problema foi dado : **Qual a menor quantidade de pulos para atravessar o caminho?**
	- Se fosse uma aula do semestre anterior, J.B iria de fato querer uma quantia certa.
	- *These youngsters...*
- Uma solução foi encontrada, relativamente rápido :
	- "***Quando possível, sempre dar o maior pulo possível... Caso contrário, dê um pulo menor.***"
- A solução foi fácil de encontrar, mas o ponto da aula foi mostrar que **provar** o algoritmo é a parte mais difícil.
- Como se provar isso?
	- Por **contradição.**	
	- "***Se não seguires minha receita, teu resultado sempre será pior.***"
- "*Prova depende de inspiração.*'

### Dados & Fitas
- Máquinas antigamente dependiam de fitas magnéticas para armazenamento de dados
- Mas isso traz dois pontos importantíssimos :
	- Fitas magnéticas não são infinitas
	- O aspecto físico de girar as fitas as deixa muito lentas
- Imagine que o dado que estás procurando foi, infelizmente, armazenado no final da fita
- O usuário teria que esperar uma rotação inteira da fita para conseguir ler o que foi armazenado

### Funcionamento da Máquina de Fitas
- "*Fita de 800m de largura, armazenando arquivos de tamanhos variados.*"
- Como armazená-los?
	- Um diretamente após o outro, nenhum gap entre cada arquivo.
- "*O cabeçote defeituoso lê um arquivo ponta-a-ponta.*"
	- "*Começando no início da fita, ele anda até o início do arquivo e o lê inteiro, após a leitura completa, o cabeçote volta para o início da fita.*"
- Então, além de tudo, a máquina é bem filha da puta mesmo.

### Máquina de Fitas - Problema #1
- Nessa situação, arquivos preferenciais não existem. 
- São todos visitados, acessados de mesma frequência. A única coisa que muda são seus tamanhos.
- De novo, a solução foi encontrada bem rápidamente : **Simplesmente ordenamos os arquivos de maneira crescente.**
![[assets/blocks.excalidraw | 100%]]
*Representação ainda não ordenada, só para ilustrar os tamnhos diferentes. Imagine em uma fila ordenada.*
- **Wide** sugere *ordem decrescente* como mais otimizado, isso pois ele leva em consideração que o cabeçote lê do início do arquivo, tendo que inevitavelmente voltar ao início.
- Contra-argumento de **Isadora** é que pelo custo, sempre piora ter que passar pelo pior caminho primeiro.
- **Wide** dessiste da ideia.

### Prova - Problema #1
- Temos dois arquivos : **A & B**
	- Sabemos que **B** é maior que **A** em espaço ocupado na fita.
- Imaginamos que eles se encontram *entre* duas grandes secções de dados da fita
![[assets/between.excalidraw | 100%]]
- A pergunta é : trocá-los de ordem importa?
- **SIM. SIM IMPORTA SIM.**
- Tendo 'a' colocado primeiro que 'b' :
	- x + (x+a) + (x+a) + b
- Tendo 'b' colocado primeiro que 'a' :
	- x + (x+b) + (x+b) + a
- Cortando tudo com tudo temos que :
	- O que resta na primeira situação é **a**.
	- O que resta na segunda situação é **b**.
- Como já sabemos que **a** é menor que **b**, podemos concluir que ordenando de forma crescente sempre nos leva para a situação desejada.	
