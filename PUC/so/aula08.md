# Sistemas Operacionais
## [24-03-2026][mvfm]
---
### Escalonamento de Tarefas
- Planejamento, distribuição de recursos para tarefas ( aplicações, processos )
	- "*Um cinco ou sete pra vocês em termos de notas.*"
- De acordo com o sor, a definição mais direta da tarefa do escalonamento de tarefas é : 
	- "**Tentar fazer com que as tarefas sejam executadas efetivamente.**"
- A esse ponto, Filipo ainda não passou do primeiro slide dos disponíveis pelo moodle.
- Menciona que atividades práticas vão ser aquelas mais parecidas com as que vão aparecer em provas.
	- *Não necessariamente scriptzinhos em C*

### Passando pelos Slides
- Objetivos de escalonamento :
	1. Maximizar a taxa de utilização da CPU
	2. Maximizar **vazão** do sistema
		**Vazão** : Número de processos executados (Throughput)
	3. Minimizar tempo de execução (**Turnaround**)
	4. Minimizar tempo de espera
	5. Minimizar tempo de resposta
- **Obs : ** Enquanti isso, o professor continua no mesmo slide de antes.
- Rápida revisãozinha da arquitetura de **Von Neuman**
![[assets/neuman.excalidraw | 100% ]]
- Ajuda para lembrar fundamentos da blockchain?
- Honestamente, dá pra se perder mais fácil do que nas aulas do **JB**.
- Voltando aos slides...

### Algoritmos de Escalonamento
- Algoritmos que, considerando o contexto de escalonamento mencionado anteriormente, procuram atingir tempos médios bons.
	- "*Privelegiar a variância em relação à tempos médios.*"
- Políticas de escalonamento se encaixam em duas principais categorias : 
	1. **Preemptivas**
		*Processo de posse da CPU pode perdê-la a qualquer momento, na ocorrência de certos eventos. Como fim da sua fatia de tempo, processo mais prioritário tonra-se pronto para execução etc.*
		Obs : Como escrito no slide, algoritmos preemptivos **não permitem monopolização da CPU**
	2. **Não-Preemptivas**
		*O processo em execução só perde a posse da CPU caso termine ou a devolva deliberadamente. Isto é : uma vez no estado "running" ele só muda de estado caso conclua sua execução ou bloqueia a mesmo emitindo operação e/s.*
- Ou seja, aqueles que estão dispostos a compartilhar a CPU & aqueles que não estão.

### Exemplos de Algoritmos 
[Não classificados como Preemptivos ou não.]
1. FIFO / First-Come-First-Serve
2. Shortest-Job-First
3. Shortest-Remaining-Time-First
4. Highest-Response-Rate-Next
5. Round Robin
6. Priority
7. Multiple Queue
- **FIFO / FCFS**
	- Baixa complexidade
	- Não preemptivo
	- Primeiro da fila é executado primeiro
		- Executado até o término de sua execução. Ou quando ocorre uma chamada de sistema.
		- OBS : Filipo ainda não passou do primeiro slide. *I know right*.
	- Problemático para sistemas de tempo compartilhado.
	![[assets/fifoerrado.excalidraw | 100%]]
	![[assets/fifocorreto.excalidraw | 100%]]
	*Exemplo para como a ordenação inadequada pode causar problemas de atraso*
- **Shortest-Job-First**
	- "*Privelegiando processos menores permite tempo médio menor.*"
	- Considerado um algoritmo *ótimo* pelo Sor.
	- Ele possuí duas principais abordagens : 
		1. *Processo com menor expectativa de tempo ou processamento.*
		2. *Associado com cada processo está o tamanho de seu próximo burst. Priorize aqueles de burst menor.*
	- "*A real dificuldade do algoritmo é conhecer o tamnho da próxima requisição CPU.*"
- **Escalonamento de Prioridade**
	- Um número **inteiro** é associado a cada processo, refletindo suas propriedades.
	- Menor valor = Maior prioridade
	- Possuí um grande problema : **Starvation**
		- *Processos de baixa prioridade podem nunca ocorrer.*
	- Mas isso já foi resolvido com **aging**
		- Prioridade aumenta com o seu tempo de espera.
	- Prioridades podem ser definidas internamente ou externamente, depende da aplicação.
- **Round Robin**
	- Usado em sistemas de tempo compartilhado
		- Aqueles com fatias de tempo para cada processo, mencionado anteriormente.
	- Cada processo recebe uma pequena fatia de execução. Normalmente entre **10ms & 100ms**
	- Quando seu intervalo chega ao fim, ele é colocado ao final da fila de espera.
		- Acho que seja o mesmo usado no exemplo do **Jantar dos Filósofos**.	
	- Justo?
		- Quem se importa?
