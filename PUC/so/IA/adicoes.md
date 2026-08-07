# Sistemas Operacionais — Adições & Aprofundamentos
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas. Segue os tópicos na ordem em que apareceram, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---

### Processos — O que a pilha realmente é

As notas listam os componentes de um processo mas descrevem a pilha como "[?Serve apenas para futuras recursões]". A pilha (**stack**) faz mais:

- Armazena **variáveis locais** de cada função
- Armazena o **endereço de retorno** (para onde voltar quando a função terminar)
- Armazena os **parâmetros** passados para funções

Cada chamada de função empurra um **stack frame** no topo. Quando a função retorna, o frame é removido. Stack overflow ocorre quando frames se acumulam mais rápido do que retornam — recursão sem caso base.

**Comparação stack vs. heap:**

| | Stack | Heap |
|---|---|---|
| Alocação | Automática (entra/sai da função) | Manual (`malloc`/`free`) ou GC |
| Tamanho | Limitado (~1-8 MB típico) | Limitado pela RAM disponível |
| Velocidade | Muito rápida (só move ponteiro) | Mais lenta (busca bloco livre) |
| Lifetime | Escopo da função | Controlado pelo programador |

---

### Estados de Processo — As transições que faltaram

As notas listam os 5 estados mas não as **transições** entre eles:

```
                    ┌─── admitido ────┐
                    ↓                 │
                  Novo              Pronto ←── interrupt
                    │                 │             ↑
                    └─── criado ───→  │         Executando
                                      │             │
                                      └─ escalonado ┘
                                              │
                                           E/S ou evento
                                              ↓
                                          Esperando
                                              │
                                         E/S completa
                                              ↓
                                          Pronto (de novo)
```

O ponto crítico: **Pronto ≠ Executando**. Um processo em estado Pronto está na fila, esperando o escalonador dar-lhe a CPU. Em sistemas multicore, múltiplos processos podem estar Executando simultaneamente — um por núcleo.

---

### Troca de Contexto (Context Switch)

O mecanismo que permite múltiplos processos compartilharem uma CPU. Quando o SO precisa trocar de processo:

1. Salva o estado do processo atual no seu PCB (registradores, PC, stack pointer)
2. Carrega o estado do próximo processo do seu PCB
3. Continua a execução do novo processo de onde ele parou

**Custo**: context switches são **puros overhead** — durante a troca, nenhum trabalho útil é feito. O tempo de um switch varia de microsegundos a dezenas de microsegundos. Por isso threads são mais baratas: compartilham memória, então o switch salva/restaura menos estado.

---

### Fork() — Copy-on-Write

As notas descrevem que "o filho herda uma cópia do espaço de memória do pai". Na prática moderna, isso não é uma cópia imediata:

**Copy-on-Write (CoW)**: pai e filho inicialmente **compartilham as mesmas páginas de memória**, marcadas como read-only. Somente quando um dos dois tenta **escrever** em uma página, o SO copia aquela página específica e a modifica. Páginas não modificadas nunca são copiadas.

Consequência: `fork()` seguido imediatamente de `exec()` (que carrega um novo programa) é muito barato — quase nenhuma cópia acontece. Esse padrão fork+exec é como o shell cria processos.

---

### Algoritmos de Escalonamento — O que as notas não classificaram

As notas listam os algoritmos mas não dizem quais são preemptivos. A classificação:

| Algoritmo | Preemptivo? | Starvation? |
|---|---|---|
| FIFO/FCFS | Não | Não |
| Shortest-Job-First (não-preemptivo) | Não | Sim (jobs longos) |
| Shortest-Remaining-Time-First | Sim | Sim (jobs longos) |
| Round Robin | Sim | Não |
| Priority (estático) | Ambos | Sim (baixa prioridade) |
| Priority com Aging | Ambos | Não |

**HRRN (Highest Response Rate Next)** — mencionado na lista mas não explicado: prioriza o processo com maior razão de resposta $= (tempo\_espera + tempo\_serviço) / tempo\_serviço$. Quanto mais tempo um processo espera, maior sua prioridade. É não-preemptivo e previne starvation naturalmente.

---

### Round Robin — O quantum importa

As notas mencionam "entre 10ms e 100ms" sem explicar por quê o valor importa:

- **Quantum muito pequeno** (ex: 1ms): muitos context switches, overhead domina, eficiência cai.
- **Quantum muito grande** (ex: 1000ms): degrada para FIFO, tempo de resposta ruim para processos interativos.
- **Quantum típico** (10-100ms): balanceado. Com 10ms e 100 processos, cada um espera no máximo 1 segundo — aceitável para interatividade.

O Linux moderno usa um escalonador chamado **CFS (Completely Fair Scheduler)** que não usa quantum fixo — distribui CPU proporcionalmente ao peso de cada processo usando uma árvore rubro-negra para eficiência $O(\log n)$ nas operações de fila.

---

### Threads — Race Conditions e Exclusão Mútua

As notas descrevem threads e o que compartilham, mas não o problema central que o compartilhamento causa:

**Race condition**: quando duas threads acessam e modificam o mesmo dado simultaneamente e o resultado depende da ordem de execução.

Exemplo clássico: dois threads incrementando um contador

```c
// Thread 1 e Thread 2 executando isso simultaneamente:
contador = contador + 1;
```

Em assembly isso é 3 instruções: `LOAD`, `ADD`, `STORE`. Se Thread 1 faz LOAD antes de Thread 2 fazer STORE, um incremento é perdido. O contador deveria ser 2, mas fica 1.

**Solução**: Exclusão Mútua com **mutex** (mutual exclusion):

```c
pthread_mutex_lock(&mutex);
contador = contador + 1;   // seção crítica
pthread_mutex_unlock(&mutex);
```

Só uma thread por vez entra na seção crítica. O mutex é o mecanismo mais fundamental de sincronização, e aparece diretamente do uso de `pthread` que as notas mencionam.

---

### Deadlock — O pesadelo do escalonamento

Provavelmente vai aparecer nas próximas aulas. O **Deadlock** ocorre quando dois ou mais processos ficam esperando eternamente por recursos que o outro segura:

- Processo A segura recurso 1, espera recurso 2
- Processo B segura recurso 2, espera recurso 1
- Ambos bloqueados para sempre

As quatro condições necessárias para deadlock (Coffman, 1971):
1. **Exclusão mútua**: recurso só pode ser usado por um processo
2. **Hold and wait**: processo segura recurso enquanto espera outro
3. **Sem preempção**: recursos não podem ser forçosamente removidos
4. **Espera circular**: cadeia circular de dependências

Para prevenir deadlock, quebra-se pelo menos uma dessas condições. O **Jantar dos Filósofos** mencionado nas notas é o exemplo clássico que ilustra exatamente isso.

---

### `#define` vs `const` vs `int` — A diferença que importa

As notas mencionam `#define N 5` como diretiva de compilação. A distinção:

- `#define N 5`: substituição textual feita pelo **pré-processador**, antes da compilação. `N` não existe como variável — o compilador nunca vê `N`, só vê `5`. Sem tipo, sem verificação.
- `const int N = 5`: variável com tipo, verificada pelo compilador, pode ser inspecionada pelo debugger.
- `int N = 5`: variável modificável. Não serve como tamanho de array em C89.

Para tamanhos de buffer e constantes de sistema, `#define` ainda é comum em código C legado. Em C++ e C moderno (`c99+`), prefere-se `const` ou `constexpr` por segurança de tipos.

---

## Aula 04 — PCB em Detalhe e o Jantar dos Filósofos

### Process Control Block — Por que Cada Campo Existe

O PCB é a estrutura de dados no kernel que *representa* um processo. Cada campo tem razão de ser:

| Campo | Por que existe |
|---|---|
| Estado do processo | O escalonador precisa saber se pode (Pronto) ou não (Esperando) escalonar esse processo |
| Contador de programa (PC) | Para retomar exatamente de onde parou após um context switch |
| Registradores da CPU | Para restaurar o estado completo da CPU — sem isso o processo retomaria com valores errados |
| Informação de memória | Tabela de páginas e limites de segmento — o MMU precisa disso para traduzir endereços virtuais |
| Informações de E/S | Arquivos abertos, buffers, dispositivos em uso |
| Informações de contabilidade | CPU time usado, limites de recursos (`ulimit` no Linux) |

O PCB é criado no `fork()` e destruído no `exit()`. Em Linux, o PCB corresponde à estrutura `task_struct` — com ~500 campos. É uma das estruturas mais complexas do kernel.

---

### O Jantar dos Filósofos — O Exemplo Clássico de Deadlock

O Jantar dos Filósofos (Dijkstra, 1965) é o exemplo canônico de deadlock com recursos compartilhados:

**Cenário**: 5 filósofos em mesa circular, 5 garfos entre eles. Para comer, cada filósofo precisa dos **dois garfos adjacentes**.

**O deadlock**: se todos pegam o garfo esquerdo simultaneamente, ninguém consegue o garfo direito. Espera circular infinita — as quatro condições de Coffman todas satisfeitas.

**Soluções clássicas**:

1. **Ordenação de recursos**: garfos são numerados; filósofo sempre pega o de menor número primeiro. Quebra a espera circular (condição 4).
2. **Semáforo central**: no máximo 4 filósofos tentam comer ao mesmo tempo — sempre haverá pelo menos um que consegue os dois garfos.
3. **Solução do mordomo**: um árbitro controla quem pode tentar pegar garfos.

A conexão com `pthread_mutex`: cada garfo é um mutex. A regra prática mais usada para evitar deadlock em código real é **sempre travar mutexes na mesma ordem em todo o código** — é a solução de ordenação aplicada a sistemas reais.

---

## Aula 08 — Escalonamento: Preempção, Starvation e HRRN

### Classificação Formal dos Algoritmos

A tabela que as notas listam sem classificar:

| Algoritmo | Preemptivo | Starvation |
|---|---|---|
| FIFO/FCFS | Não | Não |
| SJF não-preemptivo | Não | Sim (jobs longos) |
| SRTF | Sim | Sim (jobs longos) |
| HRRN | Não | Não |
| Round Robin | Sim | Não |
| Priority estático | Ambos | Sim (baixa prioridade) |
| Priority com Aging | Ambos | Não |

### HRRN — Prevenção de Starvation sem Preempção

**Highest Response Ratio Next** seleciona o processo com maior razão:

$$\text{Response Ratio} = \frac{\text{tempo de espera} + \text{tempo de serviço esperado}}{\text{tempo de serviço esperado}}$$

Quanto mais tempo um processo espera, maior sua razão — e maior sua prioridade. **Aging** implícito sem mecanismo explícito: um processo de baixa prioridade nunca morre de starvation porque seu numerador cresce continuamente.

O Linux moderno usa o **CFS (Completely Fair Scheduler)**: distribui CPU proporcionalmente ao peso (*nice value*) de cada processo, usando árvore rubro-negra para eficiência $O(\log n)$ nas operações de fila.

---

## Aula 10 — Diretivas de Compilação e Armadilhas do `#define`

### `#define` vs. `const` vs. `enum`

```c
#define N 5       // substituição textual — sem tipo, sem escopo, invisível ao debugger
const int N = 5;  // variável tipada, visível ao debugger, ocupa memória
enum { N = 5 };   // constante inteira sem memória, com tipo
```

Para tamanhos de arrays em C89, apenas `#define` ou `enum` funcionam (VLAs — variable-length arrays — só existem a partir do C99). Em C11 e C++, `constexpr` é a opção preferida.

### Por Que `#define` é Perigoso em Expressões

```c
#define SQUARE(x) x * x        // perigoso
SQUARE(1 + 2)                  // expande para 1 + 2 * 1 + 2 = 5, não 9
#define SQUARE(x) ((x) * (x))  // correto: parênteses em tudo
```

Ou melhor: `static inline int square(int x) { return x * x; }` — função inline sem overhead e com segurança de tipos.

---

## Aula 11 — fork() em Profundidade e POSIX Threads

### Copy-on-Write: Por Que fork() é Barato

As notas dizem "o filho herda uma cópia do espaço de memória do pai". A implementação real:

**Copy-on-Write (CoW)**: após `fork()`, pai e filho compartilham as mesmas páginas físicas, marcadas como *read-only*. Somente quando um dos dois tenta **escrever** em uma página, o SO copia aquela página específica. Páginas nunca modificadas nunca são copiadas.

Consequência: `fork()` + `exec()` imediato é extremamente barato — o espaço do filho é descartado antes que qualquer escrita ocorra. É assim que shells criam processos.

### API POSIX Threads: Os Protótipos Essenciais

```c
int pthread_create(pthread_t *tid, const pthread_attr_t *attr,
                   void *(*func)(void *), void *arg);
int pthread_join(pthread_t tid, void **retval);
int pthread_mutex_lock(pthread_mutex_t *mutex);
int pthread_mutex_unlock(pthread_mutex_t *mutex);
```

O `NULL` como segundo argumento de `pthread_create` usa atributos padrão (stack de ~8MB, política SCHED_OTHER). A criação é "100× mais rápida que fork()" porque não aloca nova tabela de páginas — threads compartilham o espaço de endereçamento do processo.

---

## Aula 12 — Atividades de Múltipla Escolha: Padrões de Questão

### Como Abordar Questões de Escalonamento

Para questões que pedem tempo médio de espera: montar o **diagrama de Gantt** (linha do tempo de execução) antes de calcular. Exemplo para FIFO com processos chegando em $t=0$:

```
P1 (burst=4): [0----4]
P2 (burst=2):           [4--6]
P3 (burst=3):                  [6-----9]
Espera: P1=0, P2=4, P3=6 → média = (0+4+6)/3 = 3.33
```

Para SJF com os mesmos processos: P2 primeiro → tempo médio de espera menor.

### Como Contar Processos Criados por fork()

Cada `fork()` dobra o número de processos. Com $n$ `fork()` em série (sem condicionais): $2^n$ processos total.

Com condicional `if (fork() > 0)`: apenas o pai faz a próxima chamada → $n+1$ processos. Problemas de prova frequentemente pedem exatamente essa contagem.

---

## Aula 17 — Consolidação: Processos vs. Threads

Aula de contexto (P1 cancelada, entrega do T1). Boa oportunidade de consolidar os dois conceitos centrais do primeiro módulo:

**Processo**: unidade de isolamento. Espaço de endereçamento privado. Comunicação exige IPC explícita (pipes, shared memory, sockets). Criado via `fork()`.

**Thread**: unidade de concorrência. Compartilha código, dados e arquivos do processo pai. Comunicação é implícita (variáveis compartilhadas) mas exige sincronização (mutexes, semáforos). Criada via `pthread_create()`.

**Quando usar qual**:
- **Processos**: isolamento de falha (se um processo trava, os outros continuam), execução de programas diferentes (`exec()`).
- **Threads**: performance com dados compartilhados (sem overhead de IPC), paralelismo dentro de um mesmo programa.

---

## Aula 20 — Revisão P1: O Que Estudar e Como Usar a Colinha

### Escopo Confirmado da P1

Gerência de Memória foi explicitamente excluída. O foco é: processos, threads, sincronização POSIX — exatamente o que o T1 de benchmark exercitou.

### Hierarquia de Conteúdo para a Colinha (A4 frente única)

1. **Algoritmos de escalonamento**: diagrama de Gantt para FIFO, SJF e Round Robin com exemplos numéricos. Mais provável de aparecer em questão de cálculo.
2. **Condições de Coffman** para deadlock: exclusão mútua, hold and wait, sem preempção, espera circular.
3. **API POSIX**: protótipos de `fork()`, `pthread_create()`, `pthread_mutex_lock()`, `shmget()`, `sem_open()`.
4. **Estados de processo** e transições: diagrama dos 5 estados.
5. **Race condition e seção crítica**: definição, exemplo com contador, solução com mutex.

### O Que Colinha não Substitui

Colinha ajuda em fórmulas e protótipos de API. Não substitui entender **quando aplicar** cada conceito — questões de múltipla escolha frequentemente pedem raciocínio, não memorização.

---

## Aula 21 — Gerência de Memória: Hierarquia e Espaço Virtual

### Por Que a Memória Sempre Foi Escassa

As notas capturam a anedota histórica. O dado técnico por trás é a **hierarquia de memória**: não é possível ter grande quantidade de memória rápida a custo acessível:

| Nível | Velocidade | Capacidade típica |
|---|---|---|
| Registradores | ~1 ciclo | Dezenas de bytes |
| Cache L1 | 3-5 ciclos | 32-64 KB |
| Cache L2/L3 | 10-40 ciclos | 256 KB – 32 MB |
| RAM | 100-300 ciclos | 4-128 GB |
| SSD | ~100.000 ciclos | 256 GB – 4 TB |

Em microcontroladores modernos, 64 KB de RAM é comum — o "espaço escarso" da anedota histórica ainda existe em 2026, só que em contexto embarcado.

---

### Espaço de Endereçamento Virtual

Cada processo acredita ter acesso a toda a memória do sistema — isso é o **espaço de endereçamento virtual**. O SO mantém uma **tabela de páginas** por processo que mapeia endereços virtuais para físicos. Isso garante:

1. **Isolamento**: processo A não escreve no espaço de processo B — mesmo usando o mesmo endereço virtual
2. **Abstração**: o processo não sabe onde fisicamente está na RAM
3. **Capacidade além da RAM**: páginas não usadas podem estar no disco (*swap*)

O endereço `0x7fff...` do topo da stack é igual em todo processo Linux, mas mapeado para páginas físicas diferentes.

---

### Fragmentação: O Problema que a Paginação Resolve

- **Fragmentação interna**: o processo recebe mais memória que pediu (por alinhamento de página) — desperdiçada dentro do bloco
- **Fragmentação externa**: blocos livres suficientes no total, mas nenhum **contíguo** grande o suficiente

**Paginação** resolve fragmentação externa: o SO aloca páginas físicas não contíguas e as mapeia como contíguas no espaço virtual. O processo nunca sabe a diferença.

---

## Aula 22 — Substituição de Páginas: Os Algoritmos do T2

### Page Fault e o Ciclo de Vida de uma Página

Quando um processo acessa um endereço cuja página não está na RAM (**page fault**), o SO:

1. Bloqueia o processo (estado Esperando)
2. Seleciona uma **página vítima** para remover da RAM
3. Se modificada (*dirty bit* = 1), escreve no disco antes
4. Carrega a nova página; atualiza a tabela de páginas; retoma o processo

**Thrashing**: quando o sistema passa mais tempo tratando page faults do que executando código. Ocorre quando o working set do processo é maior que a RAM disponível.

---

### Os Algoritmos de Substituição

**FIFO**: remove a página que está na RAM há mais tempo. Simples; sofre da **Anomalia de Belady** — mais frames de RAM podem causar *mais* page faults. Único algoritmo com esse comportamento contra-intuitivo.

**LRU (Least Recently Used)**: remove a página usada há mais tempo ("mais fria"). Boa aproximação do ótimo. Implementação exata exige hardware especializado; na prática usa-se **Clock** como aproximação.

**Algoritmo Ótimo (Belady/OPT)**: remove a página que será usada **mais tarde no futuro**. Impossível de implementar em tempo real — serve como **lower bound** para comparação. Qualquer algoritmo real terá pelo menos tantos faults quanto OPT.

**Segunda Chance (Clock)**: cada página tem um *reference bit* setado ao ser acessada. Ao remover: percorre a fila; se bit é 1, zera e passa; se é 0, remove. Aproxima LRU com overhead mínimo.

O código Python do Filipo provavelmente fornece a estrutura do simulador (carga de sequência de referências, contagem de faults) — deixando os algoritmos para implementar.

---

## Aula 26 — Hardware de E/S: Polling, Interrupções e DMA

### Polling vs. Interrupções: O Trade-off Central

**Polling** (busy-wait): o host lê o bit *busy* repetidamente até ficar zero. Problema formal: **espera ocupada** — o processador gasta ciclos verificando status sem fazer trabalho útil.

**Interrupções** resolvem isso:
1. Host emite comando e continua executando outro processo
2. Dispositivo, ao terminar, envia **interrupção** para a CPU
3. CPU pausa, executa o **ISR (Interrupt Service Routine)**, retoma o processo anterior

| | Polling | Interrupção |
|---|---|---|
| CPU ocupada esperando? | **Sim** | Não |
| Latência de resposta | Muito baixa | Depende do overhead do ISR |
| Quando preferido | Dispositivos ultrarrápidos (< µs) | Disco, rede, teclado — qualquer coisa lenta |

Polling ainda é preferido para SSDs NVMe e redes de alta velocidade: a operação completa antes de ~20 iterações de polling, e o overhead de interrupção seria maior que o tempo economizado.

---

### DMA — Liberar a CPU do Trabalho Pesado

Para transferir 1 MB de disco, interrupção por byte geraria 1.048.576 interrupções. A solução é **DMA (Direct Memory Access)**:

1. CPU programa o controlador DMA: origem, destino, tamanho
2. DMA assume o barramento e transfere dados diretamente entre dispositivo e RAM
3. Ao terminar, DMA envia **uma única interrupção**

A CPU é liberada durante toda a transferência — tempo suficiente para executar centenas de milhares de instruções.

---

### Mapeamento de E/S: Port-Mapped vs. Memory-Mapped

Dois modelos para endereçar os registradores descritos nas notas (Data-In, Data-Out, Status, Control):

**Port-Mapped I/O**: dispositivos têm espaço de endereçamento separado da RAM; instruções especiais `IN`/`OUT` em x86 para acessar portas. Padrão histórico do IBM PC.

**Memory-Mapped I/O**: registradores de dispositivo mapeados em endereços RAM normais; CPU usa as mesmas instruções de leitura/escrita da memória. Domina em arquiteturas RISC (ARM) e em todo hardware moderno. Em Linux, `mmap()` sobre `/dev/mem` é a base dos drivers que acessam registradores — é MMIO exposto ao userspace.

---

## Aula 28 — Interface do Sistema de Arquivos

### O que "Espaço de Endereçamento Lógico Contíguo" Realmente Significa

A definição dos slides — arquivo como "espaço de endereçamento lógico contíguo mapeado pelo SO para dispositivos físicos" — é densa, mas o ponto é a palavra **lógico**. O arquivo *parece* uma sequência de bytes de 0 a $N$, contígua e sem buracos, para quem o lê. **Fisicamente**, esses bytes podem estar espalhados em blocos não-adjacentes no disco. O SO mantém a **abstração** (a 1ª característica citada) traduzindo o offset lógico em endereços físicos via estruturas como a tabela de blocos do inode. É a mesma ideia da memória virtual, aplicada ao armazenamento: o programa vê um espaço linear limpo; o SO esconde a bagunça física.

### Metadados, o Inode e Por Que Nome ≠ Arquivo

Os atributos listados (nome, ID, tipo, local, tamanho, proteção) são **metadados** — dados *sobre* o arquivo, guardados separadamente do conteúdo. Em sistemas Unix, eles vivem numa estrutura chamada **inode**, identificada pelo "ID numérico interno" das notas. Consequência crucial e contraintuitiva: **o nome não faz parte do arquivo**. O nome mora no *diretório*, que é apenas uma tabela `nome → número de inode`. Isso explica:

- **Hard links:** dois nomes podem apontar para o mesmo inode — o arquivo só some quando o último link é removido (por isso o inode guarda um *contador de links*).
- **Renomear é barato:** muda só a entrada de diretório, não toca no conteúdo.
- **O "tipo" pela extensão é só convenção:** em Unix o tipo real não está no `.txt`; o SO descobre o conteúdo por outros meios (*magic numbers*). A extensão é uma dica para humanos e para o shell, não uma verdade imposta.

### As Operações são Primitivas, e o "Seek" Move um Ponteiro

As operações (criar, ler/escrever, reposicionar, deletar, truncar) são as **chamadas de sistema** que toda linguagem embrulha. O detalhe que as notas tocaram — "reposicionar = o famoso seek" — é exatamente isso: cada arquivo aberto tem um **ponteiro de posição corrente** (*file offset*) na tabela de arquivos abertos do processo. `read`/`write` avançam esse ponteiro; `lseek` o move sem ler nada (permite **acesso aleatório**, pular direto ao byte 5000). E a distinção que os slides fizeram entre **truncar** (zera conteúdo, mantém o inode e os atributos) e **deletar** (remove a entrada de diretório e libera os blocos) é precisamente a diferença entre esvaziar o arquivo e fazê-lo deixar de existir.

---

## Aula 29 — File Locking e Concorrência Destrutiva

### Race Condition e Seção Crítica — a Formalização do "Dá Errado"

A "concorrência destrutiva" dos slides é a **race condition**: o resultado final depende da *ordem* não-determinística em que threads/processos intercalam acessos a um dado compartilhado. O exemplo do banco é canônico porque `saldo = saldo + 100` **não é atômico** — compila em três passos (ler, somar, gravar):

```
P1: lê saldo (100)            P2: lê saldo (100)
P1: soma 100 → 200            P2: soma 50 → 150
P1: grava 200                 P2: grava 150   ← os 100 de P1 sumiram (lost update)
```

A região de código que toca o recurso compartilhado é a **seção crítica**. A regra é que no máximo um fluxo pode estar nela por vez — **exclusão mútua**.

### A Intuição "Lock é igual a Semáforo" — Quase

A desconfiança das notas está certa em espírito: locks e semáforos resolvem o mesmo problema (exclusão mútua), mas não são a mesma coisa.

| | Lock / Mutex | Semáforo |
|---|---|---|
| Estado | binário (livre/ocupado) | contador $\ge 0$ |
| Dono | **tem dono** — só quem travou destrava | sem dono — qualquer um faz `signal` |
| Uso típico | proteger uma seção crítica | controlar acesso a $N$ recursos / sinalização entre processos |

O **file lock** é o mecanismo de exclusão aplicado a *arquivos*, mediado pelo SO (`flock`/`fcntl` em Unix), para coordenar **processos distintos** — não apenas threads dentro de um programa.

### Por Que "Forçar Execução Sequencial" Incomoda (e a Resposta: Locks de Leitura/Escrita)

O desconforto das notas — "o lock serializa quem rodava em paralelo" — é uma observação real sobre **contenção**: a seção crítica vira um gargalo, e o paralelismo vale só *fora* dela. A mitigação é exatamente a tabela de tipos de lock que o Fillipo mostrou — o **readers-writer lock**:

| Estado atual | Pedido de leitura | Pedido de escrita |
|---|---|---|
| Livre | permitido | permitido |
| **Shared (leitura)** | permitido | bloqueado |
| **Exclusive (escrita)** | bloqueado | bloqueado |

A ideia: **leituras não conflitam entre si** (ninguém altera o dado), então *muitos* leitores podem entrar ao mesmo tempo — só a escrita exige exclusividade total. Isso recupera paralelismo em cargas dominadas por leitura, que é o caso comum. O preço é a possibilidade de **starvation** (inanição): um fluxo contínuo de leitores pode adiar indefinidamente um escritor, problema que implementações justas resolvem dando prioridade ao escritor que está esperando.

### O Perigo que os Slides Não Mencionaram: Deadlock

Locks resolvem a race condition, mas introduzem um risco novo. Se P1 trava o arquivo A e espera B, enquanto P2 trava B e espera A, ninguém avança: **deadlock**. Ele exige quatro condições simultâneas (Coffman): exclusão mútua, posse-e-espera, não-preempção e espera circular. A prevenção mais simples e prática é impor uma **ordem global** de aquisição de locks (sempre travar A antes de B) — eliminando a espera circular. Vale lembrar disso sempre que um processo precise de mais de uma trava ao mesmo tempo.

---

## Aula 27 — O Subsistema de Software de E/S

Aula de atividade prática em grupo — as notas guardam só a logística. Vale usar o espaço para preencher o vão curricular exato em que ela cai: a Aula 26 terminou no **hardware** de E/S (polling, interrupções, DMA) e a Aula 28 começa na **interface** do sistema de arquivos (`open`, `read`, `lseek`). Entre as duas existe uma camada inteira de software — a menos ensinada e uma das mais cobradas da disciplina.

### As Quatro Camadas Entre o `read()` e o Prato do Disco

Um `read()` não conversa com o dispositivo. Ele atravessa uma pilha, e cada camada existe para esconder uma bagunça específica da camada de baixo:

| Camada | Onde roda | Responsabilidade |
|---|---|---|
| **Software de E/S no nível do usuário** | userspace | Bibliotecas (`stdio`, `fopen`/`fprintf`) e *spooling*. É quem faz o buffer de linha do `printf`. |
| **Software de E/S independente de dispositivo** | kernel | Nomeação uniforme (`/dev/sda`), proteção, tamanho de bloco unificado, **buffering**, **caching**, alocação. É a camada que faz disco e pendrive parecerem a mesma coisa. |
| **Device drivers** | kernel | O único código que conhece os registradores concretos daquele controlador. Traduz "ler bloco 4711" em escritas específicas de hardware. |
| **Tratadores de interrupção** | kernel | Acordam o driver quando o DMA da Aula 26 termina. Rodam em contexto de interrupção — não podem bloquear. |

A regra que organiza tudo: **o driver é a única parte que muda por dispositivo**. É por isso que adicionar hardware novo ao Linux significa escrever um driver, e não recompilar o kernel inteiro — e é por isso que drivers respondem pela maior parte do código-fonte de um SO moderno.

### Buffering, Caching e Spooling — Três Coisas que Parecem Uma

Confundir os três é erro clássico de prova. Os três guardam dados em memória, mas resolvem problemas diferentes:

| Técnica | Problema que resolve | Exemplo |
|---|---|---|
| **Buffering** | **Descompasso de velocidade e de tamanho** entre produtor e consumidor. Os dados vão passar de qualquer jeito; o buffer só suaviza o fluxo. | Placa de rede entrega pacotes de 1500 B; a aplicação quer 64 KB de uma vez. |
| **Caching** | **Latência de acesso repetido**. Guarda uma *cópia* de dado que já existe em outro lugar, apostando em **localidade**. | *Page cache* do Linux: o segundo `read()` do mesmo bloco não toca no disco. |
| **Spooling** | **Dispositivo não-compartilhável**. Serializa acessos concorrentes a um recurso que não pode ser intercalado. | Fila de impressão: duas páginas não podem sair intercaladas no papel. |

A distinção mais fina, e a que costuma cair: **buffer guarda a única cópia do dado; cache guarda uma cópia redundante**. Perder um cache custa performance; perder um buffer perde dado. É exatamente por isso que `sync()`/`fsync()` existem — o *page cache* funciona como buffer de escrita (*write-back*), e um desligamento abrupto com dados sujos ainda não descarregados perde escritas que a aplicação já considerava concluídas.

### Escalonamento de Disco: Por Que a Ordem dos Pedidos Importa

Num HDD, o custo dominante não é ler — é o **seek time**, mover o braço até a trilha certa. Como vários processos pedem blocos ao mesmo tempo, a fila pode ser reordenada. Usando o exemplo canônico (cabeça em 53, fila `98, 183, 37, 122, 14, 124, 65, 67`, disco de 0 a 199):

| Algoritmo | Ideia | Movimento total | Problema |
|---|---|---|---|
| **FCFS** | Atende na ordem de chegada. | **640** | Ignora a geometria; vai e volta à toa. |
| **SSTF** | Sempre o pedido mais próximo. | **236** | **Starvation**: um pedido distante pode nunca ser atendido. É o guloso e, como todo guloso, míope. |
| **SCAN** (*elevador*) | Varre até uma ponta, inverte, varre de volta. | **236** | Quem está logo atrás da cabeça espera uma varredura inteira. |
| **C-SCAN** | Varre só numa direção; ao chegar ao fim, volta ao início sem atender. | **382** | Movimento maior, mas **tempo de espera muito mais uniforme**. |

O nome *elevador* não é analogia solta: é literalmente a política de um elevador, e a intuição de que ele é "justo" é a mesma. C-SCAN parece pior pelo número, mas otimiza **variância**, não média — e em sistema interativo previsibilidade vale mais que throughput bruto.

**O detalhe moderno que inverte a conclusão:** em **SSD não existe seek**. Não há braço nem trilha; o custo de acesso é uniforme. Todo esse esforço vira desperdício de CPU, e por isso o escalonador padrão do Linux para NVMe é o `none` (fila simples). O gargalo migrou para outros lugares — *write amplification*, coleta de lixo do controlador e o `TRIM`, que avisa ao SSD quais blocos o sistema de arquivos já não usa. Um algoritmo pode estar formalmente correto e mesmo assim ser obsoleto porque a premissa de hardware evaporou.

---

## Aula 30 — Devolução da P2 e Consolidação do Módulo 2

### Por Que a Prova Sem Colinha Saiu Melhor

A observação das notas — 10,0 na prova sem colinha, 9,0 na prova com — está registrada como piada, mas é um resultado bem documentado e vale entender, porque muda como estudar para a PS.

O mecanismo é o **testing effect** (ou *retrieval practice*): **recuperar** uma informação da memória fortalece o traço mnemônico muito mais do que **revê-la**. Estudar sabendo que não haverá consulta força recuperação ativa durante o preparo; estudar sabendo que haverá colinha permite terceirizar a recuperação para o papel — e o preparo vira leitura, que é o modo mais fraco de estudar.

O agravante é a **ilusão de fluência**: reler material conhecido *parece* aprendizado porque o texto passa fácil e sem atrito. Essa facilidade é lida pelo cérebro como domínio, e é justamente por isso que a sensação "eu sei isso" e o desempenho real descolam — a impressão de ter errado a P1 apesar do 10,0 é a mesma ilusão operando na direção contrária. A linha de pesquisa de Robert Bjork sobre **dificuldades desejáveis** formaliza a ideia: condições que tornam o estudo mais difícil no curto prazo produzem retenção melhor no longo.

O que isso implica na prática: a colinha ajuda a **não travar** (protótipos de API, condições de Coffman, fórmulas), mas o preparo tem que ser feito **como se ela não existisse** — resolvendo questões antigas de memória antes de consultar qualquer coisa. A colinha é rede de segurança, não substituta de estudo, e escrevê-la é mais útil que consultá-la, porque escrever exige decidir o que importa.

### Escopo Consolidado do Módulo 2

A P1 cobriu processos, threads e sincronização (Aula 20). A P2 e a PS cobrem o que veio depois:

| Bloco | Conceitos centrais | Onde cai a conta |
|---|---|---|
| **Gerência de memória** (Aula 21) | Hierarquia, espaço de endereçamento virtual, tradução lógico→físico, MMU, fragmentação interna vs. externa | Cálculo de endereço: dividir em número de página + deslocamento |
| **Substituição de páginas** (Aula 22) | FIFO, LRU, ótimo (Belady), anomalia de Belady, *thrashing* | Simular a string de referência e **contar page faults** |
| **Hardware de E/S** (Aula 26) | Polling vs. interrupção vs. DMA, port-mapped vs. memory-mapped I/O | Comparação conceitual: quem consome CPU e por quê |
| **Software de E/S** (Aula 27) | Camadas, buffering/caching/spooling, escalonamento de disco | Movimento total da cabeça por algoritmo |
| **Sistemas de arquivos** (Aulas 28–29) | Arquivo como espaço lógico contíguo, inode, metadados, hard links, `lseek`, file locking, readers-writer | Distinguir truncar vs. deletar; identificar a seção crítica |

### Os Erros Clássicos deste Módulo

1. **Confundir fragmentação interna com externa.** Interna é espaço desperdiçado *dentro* de um bloco alocado (paginação sofre disso); externa é espaço livre *entre* blocos, grande no total mas fragmentado demais para servir (alocação contígua sofre disso).
2. **Achar que LRU sempre ganha de FIFO.** Não sempre — e a **anomalia de Belady** (mais quadros gerando *mais* page faults) atinge FIFO, não LRU. Saber *qual* algoritmo sofre a anomalia é a pergunta, não saber que ela existe.
3. **Tratar page fault como erro.** É evento normal de memória virtual: o SO carrega a página e reexecuta a instrução. O erro é *thrashing* — faltas tão frequentes que o sistema só pagina e não progride.
4. **Dizer que o nome é parte do arquivo.** O nome mora no diretório; o arquivo é o inode (Aula 28). Toda questão sobre hard link depende disso.
5. **Contar o retorno do C-SCAN como zero.** O movimento de volta ao início conta no total, e é exatamente por isso que o número dele é maior que o do SCAN.

---

### Referências para ir além

- **Silberschatz, Galvin & Gagne, *Operating System Concepts*, 10ª ed.** — Cap. 13–14 (interface e implementação de sistemas de arquivos) e Cap. 6–7 (sincronização, deadlocks).
- **Tanenbaum & Bos, *Modern Operating Systems*, 4ª ed.** — Cap. 4 (file systems) e Cap. 2 (mutual exclusion, semáforos).
- **`man 2 fcntl` e `man 2 flock`** (Linux) — a API real de file locking, com a distinção entre locks consultivos (*advisory*) e mandatórios.
- **Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (gratuito, ostep.org)** — capítulos de concorrência e de persistência, com a melhor explicação intuitiva de locks e inodes.
