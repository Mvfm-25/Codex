# Sistemas Operacionais
## [11-03-2026] [mvfm]

### Estado atual da cadeira
- Aula de novo na sala normal do 30
- Acontecendo justamente o que eu tinha previsto que aconteceria:
	1. Sor percebe que aulas práticas são uma necessidade à esse ponto
	2. Revisando o cronograma, percebe que não temos nenhuma aula de laboratório marcada
	3. Pós-começo-de-semestre tenta corrigir isso
	4. Falha miseravelmente
- Não sei como vão ser as atividades práticas.
- Lembrando FPPD, em que **não** aprendemos **Go**. A cadeira de **Go** btw.

### Definição de Processos
- Aula começa propriamente com o sor perguntando sobre processos : 
	 - "**Processos e programas... Iguais ou diferentes?**"
- Imediatamente ele comenta : 
	 - "**Btw... Não se existe uma definição acadêmica para 'programa', apenas aplicação.**"
- Okay.
- Então sabemos que não são iguais. Thanks bro.
- **Processos**
	- "*Um programa em execução; Execução do processo deve progredir de maneira sequencial.*"
	- Definição dada pelo slide. Sequência tendo trema.
- O que forma um processo?
	1. Contador de programa
		Conta para o registrador onde está a próxima instrução
	2. Pilha
		[?Serve apenas para futuras recursões]
	3. Seções de dados
		Bem direto. Onde os dados estão armazenados.
	![processos](assets/processo.png)

### Estados de Processo
1. Novo (new)
	O processo está sendo criado
2. Executando (running)
	Instruções estão sendo executadas
3. Esperando (waiting)
	O processo está esperando algum evento acontecer
4. Pronto (ready)
	O processo está esperando ser associado a um processador
5. Terminado (terminated)
	O processo terminou sua execução
![Diagrama](assets/eventos_processo.png)
- Tudo isso veio diretamente dos slides da aula.
- Não me lembro de nada que o sor estava comentando enquanto isso, alguma tangente provavelmente.

### Process Control Block (PCB)
- Pequena revisão de conceitos fundamentais de paralelização
- Exemplo dos pintores pintando as paredes
- "**GPU & CPU não conversam tanto.**" I know right. CUDA eat ya heart out!
- Aluna ao lado (Com o sor diretamente à sua frente btw) comprando maquiagem na web.
![omg](assets/omg_bruh.gif)
- O que um PCB faz?
	- "**PCB armazena informações associadas com cada processo.**"
	1. Estado do processo
	2. Contador de programas (**I KNOW RIGHT**)
	3. Registradores da CPU
	4. Informação de gerenciamento de memória
	5. Informação para contabilidade
	6. Informações do status E/S
	![PCB](assets/pcb.png)
