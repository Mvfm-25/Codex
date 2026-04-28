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
