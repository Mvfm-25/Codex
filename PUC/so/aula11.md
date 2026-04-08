# Sistemas Operacionais
## [06-04-2026][mvfm]
---
### Te digo que não lembro nada
- Essa aula foi aboslutamente infernal de acompanhar
- Me esqueci de trazer minha caneta e acabei ficando com um lugar bem na frente do quadro
- Revisão novamente de threads e processos
	- De saco cheio já, 11 aulas do mesmo conteúdo basicamente
	- E o conteúdo em si, sendo apenas revisão brevíssima de uma cadeira anterior
- Eu não me importo e o professor parece não se importar também.

### Processos
*Unidade fundamental do processamento*
- Re-vemos ( *i know right* ) a definiçaõ essencial de um processo : 
	- **Programa em execução, entidade dinâmica.**
- Gráficozinho bonitinho que não dá pra ler.
	- Simplesmente impossível, e olha que eu estava ali na frente.
	![folk im crine](assets/crine.png)
- Todo processo tem o seguinte : 
	1. Código (text)
	2. Dados (variáveis globais e estáticas)
	3. Pilha (variáveis e funções locais)
	4. Heap (memória alocada dinamicamente)
- Se é aprofundado um poquinho mais a chamada **fork()**
- Em sistemas UNIX ou UNIX-like, todos os processos (com exceção do primeiro) são criados via chamada de **fork()**.
	- "*O filho herda uma cópia do espaço de memória do pai. Espaço contíguo*"
	- Retorno da chamda **fork()**
		- **Pai **: PID do filho
		- **Filho **: Zero (0)
		- **Erro **: -1
	![they jumping me](assets/exemplo_fork.png)
- "*No momento do fork(), o SO duplica o processo. Agora existem dois Program Counters apontando para a próxima linha.*"

### Threads
*Concorrência dentro do mesmo espaço*
- Uma thread é um fluxo de execução dentro de um processo. Enquanto processos são isolados, threads compartilham a mesma memória.
- Mas e o que é compartilhado?
	- Segmento de Código e Dados (globais)
	- Arquivos abertos e sinais
- Ainda assim, cada thread tem sua stack & registradores.
- Em Linux & macOS, threads são criadas pela chamada da função **pthread_create()** da biblioteca **POSIX Threads**
- A criação não duplica o processo, apenas cria uma nova função paralelamente.
![threads](assets/pthreads.png)
- Criar uma nova thread é cerca de **100x** mais rápido que a criação de um novo processo.
	- Isso pois a criação de uma nova thread não requer alocação de nova tabela de páginas de memória.
![cria threads](assets/cria_threads.png)
