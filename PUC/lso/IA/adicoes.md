# Laboratório de Sistemas Operacionais — Adições & Aprofundamentos
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas. Segue os tópicos na ordem em que apareceram nas notas, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---

## Aula 01 — O Que a Ementa Realmente Pede

### "Customização de Distribuições" — o Que Isso Significa em Embarcado

O primeiro tópico da ementa é o mais opaco escrito assim. Traduzido: em sistema embarcado você **não instala uma distro**, você **constrói uma**. Um roteador, um controlador industrial ou um dispositivo médico tem 64 MB de flash e nenhum espaço para os ~2 GB de um Ubuntu mínimo, então o sistema é montado peça por peça com exatamente o que aquele produto precisa.

As duas ferramentas que dominam esse espaço:

| | **Buildroot** | **Yocto / OpenEmbedded** |
|---|---|---|
| Modelo | Gera uma imagem completa do zero | Gera uma **distribuição** com receitas e camadas |
| Curva | Simples — um `make menuconfig` e pronto | Íngreme, muitos conceitos próprios |
| Reconstrução | Tende a refazer tudo | Cache incremental por pacote |
| Uso típico | Projetos pequenos, protótipos | Produto comercial de longa vida |

Os dois produzem as mesmas quatro peças: **bootloader** (U-Boot), **kernel** Linux, **rootfs** e a **toolchain**. E o conceito central que atravessa tudo é a **compilação cruzada**: você compila no PC x86-64 (*host*) um binário que roda no ARM do dispositivo (*target*). Daí a existência de compiladores com nome de prefixo — `arm-linux-gnueabihf-gcc`. É por isso que "conhecimentos básicos de Linux & C" está listado como requisito: sem os dois, nada disso é operável.

A libc também muda: no lugar da `glibc` (grande, completa) usa-se **musl** ou **uClibc-ng**, que cabem em centenas de KB. É a mesma troca de sempre — funcionalidade por espaço.

### Módulo de Kernel: o Segundo Tópico, e Por Que Não é "Recompilar o Linux"

"Projeto e implementação de módulos do sistema operacional" tem um significado técnico bem estreito. Um **módulo de kernel** (`.ko`) é código que é carregado no kernel **em execução**, sem reinicializar e sem recompilar o kernel inteiro:

```c
#include <linux/module.h>
#include <linux/kernel.h>

static int __init meu_init(void) {
    printk(KERN_INFO "modulo carregado\n");   // não existe printf aqui
    return 0;
}
static void __exit meu_exit(void) {
    printk(KERN_INFO "modulo removido\n");
}

module_init(meu_init);
module_exit(meu_exit);
MODULE_LICENSE("GPL");                         // sem isso, o kernel fica "tainted"
```

Carrega-se com `insmod`, remove-se com `rmmod`, inspeciona-se com `lsmod`. As diferenças em relação a programar em userspace são o que torna isso uma disciplina inteira:

- **Não existe libc.** Nada de `printf`, `malloc`, `stdio`. Usa-se `printk`, `kmalloc`, `vmalloc` — a API interna do kernel.
- **Não existe proteção de memória.** Um ponteiro inválido não gera *segfault* num processo; gera **kernel panic** e derruba a máquina. Por isso o desenvolvimento é feito em VM ou com placa de destino separada.
- **A pilha é minúscula** — tipicamente 8 KB ou 16 KB para toda a cadeia de chamadas. Recursão profunda ou arrays grandes na pilha corrompem memória silenciosamente.
- **Não há ABI estável.** Um módulo compilado para o kernel 6.1 não carrega no 6.2. É decisão deliberada do projeto Linux, e a razão de drivers proprietários (como o da NVIDIA) precisarem recompilar a cada atualização.

### Políticas de Escalonamento: o Que Existe Para Ser Modificado

O terceiro tópico da ementa fica concreto sabendo que o Linux não tem *um* escalonador — tem **classes de escalonamento**, consultadas em ordem estrita de prioridade:

| Classe | Política | Para quê |
|---|---|---|
| `stop_sched_class` | — | Interno, migração de tarefas. Sempre vence. |
| `dl_sched_class` | `SCHED_DEADLINE` | Tempo real com prazo (EDF + *Constant Bandwidth Server*) |
| `rt_sched_class` | `SCHED_FIFO`, `SCHED_RR` | Tempo real por prioridade fixa (1–99) |
| `fair_sched_class` | `SCHED_OTHER`, `SCHED_BATCH` | **Todo processo normal.** Era CFS; desde o kernel 6.6 é **EEVDF** |
| `idle_sched_class` | `SCHED_IDLE` | Só roda quando não há mais nada |

Um processo `SCHED_FIFO` **nunca** é preemptado por um `SCHED_OTHER`, por mais que este espere. Daí o risco clássico de travar a máquina com um laço infinito em prioridade de tempo real.

O detalhe que torna a ementa realizável: implementar uma política nova significa preencher a `struct sched_class` — um conjunto de ponteiros de função (`enqueue_task`, `dequeue_task`, `pick_next_task`, `task_tick`) que o núcleo chama nos momentos certos. É um ponto de extensão projetado para isso, não um remendo. E desde o kernel 6.12 existe o **`sched_ext`**, que permite escrever escalonadores em **eBPF** e carregá-los sem recompilar o kernel — exatamente o tipo de experimento que uma disciplina de laboratório quer fazer.

---

## Aula 02 — Revisão: o Que Está Por Trás do Overhead e do Syscall

### Overhead de Troca de Contexto — de Onde Vem o Custo

A definição da aula ("tempo gasto na tarefa de alternar a CPU entre dois processos") está certa, mas esconde que o custo **direto** é o menor dos dois componentes:

**Custo direto** (~1–3 µs): salvar registradores no PCB, carregar os do próximo, trocar a tabela de páginas (`CR3` no x86), atualizar contadores do escalonador.

**Custo indireto** (frequentemente 10× maior): o processo novo chega com **caches frios**. As linhas de cache L1/L2 e as entradas de TLB pertencem ao processo anterior e precisam ser reconquistadas *miss* a *miss*. Esse custo não aparece em nenhuma medição direta da troca — ele se espalha pelas milhares de instruções seguintes.

Duas otimizações de hardware existem só para reduzir isso: **ASID/PCID**, que etiqueta entradas de TLB por processo para evitar o *flush* completo a cada troca; e o fato de threads do mesmo processo **compartilharem tabela de páginas**, o que elimina a troca de `CR3` inteira. É por isso que trocar entre threads é substancialmente mais barato que trocar entre processos — mesma razão pela qual `pthread_create` é ordens de grandeza mais rápido que `fork`.

### "Como Poderíamos Burlar o Syscall?" — a Resposta é Não Dá, e o Que Existe no Lugar

A pergunta que ficou aberta na aula tem uma resposta precisa, e ela é arquitetural.

O processador tem **níveis de privilégio** (*rings*): userspace roda no **ring 3**, o kernel no **ring 0**. Instruções privilegiadas — E/S direta em portas, alterar a tabela de páginas, mascarar interrupções — simplesmente **falham** (`#GP`, *general protection fault*) se executadas no ring 3. Não é convenção nem checagem de software que se possa contornar: é o silício recusando a instrução.

A única passagem do ring 3 para o ring 0 é uma **transição controlada**: a instrução `syscall` (x86-64) salta para um endereço fixado pelo kernel no registrador `MSR_LSTAR` durante o boot. O userspace **não escolhe para onde salta** — só coloca o número da chamada em `%rax` e os argumentos nos registradores, e o kernel decide o resto. Burlar isso seria burlar o isolamento inteiro do sistema; quando alguém consegue, é uma vulnerabilidade de escalação de privilégio, não uma técnica.

O que existe são formas de **pagar menos** pela travessia:

- **vDSO** (*virtual dynamic shared object*): o kernel mapeia uma pequena biblioteca no espaço de cada processo. Chamadas que só leem dados que o kernel já mantém atualizados — `gettimeofday()`, `clock_gettime()` — são resolvidas **inteiramente em ring 3**, lendo uma página compartilhada. A syscall não é burlada; ela deixou de ser necessária.
- **io_uring**: em vez de uma syscall por operação de E/S, o processo e o kernel compartilham dois *ring buffers* em memória. Milhares de operações são enfileiradas com **zero** syscalls; o kernel as consome de forma assíncrona. É a resposta moderna ao custo de travessia em servidores de alta carga.
- **Batching clássico**: `readv`/`writev`, `sendmmsg`, `epoll` — uma syscall carregando muito trabalho em vez de muitas carregando pouco.

O padrão comum aos três: a fronteira continua intacta, o que muda é quantas vezes você a atravessa.

### Round-Robin: Formalizando a Fila do Banco

O exemplo do banco (uma conta por vez, volta pro fim da fila) é uma descrição exata de Round-Robin. O que ele não mostra é a decisão de projeto que define se o algoritmo presta: **o tamanho do quantum**.

Seja $q$ o quantum e $c$ o custo de uma troca de contexto. A fração de CPU efetivamente gasta em trabalho útil é:

$$\text{eficiência} = \frac{q}{q + c}$$

Os dois extremos:

- **$q$ muito pequeno** → o denominador é dominado por $c$. Com $q = 1$ ms e $c = 0{,}1$ ms, 9% da CPU é queimada só trocando. No limite, o banco passa mais tempo chamando gente ao balcão do que atendendo.
- **$q$ muito grande** → nenhum processo é preemptado antes de terminar e o Round-Robin **degenera em FCFS**, perdendo toda a interatividade que justificava usá-lo.

A regra prática clássica: escolher $q$ tal que **~80% dos surtos de CPU terminem antes do quantum expirar**. Assim processos interativos (surto curto, depois E/S) raramente são interrompidos, e só os processos longos pagam preempção.

O Linux moderno abandonou o quantum fixo justamente por isso. O CFS usava uma **latência-alvo** dividida entre as tarefas prontas, ponderada por peso derivado do *nice*; o EEVDF (kernel 6.6+) acrescenta um *deadline* virtual por tarefa, atendendo primeiro quem tem o prazo mais próximo. O efeito é um quantum que se adapta à carga — pequeno quando há muitas tarefas interativas, grande quando há poucas — em vez de um número escolhido na compilação.

---

### Referências para ir além

- **Corbet, Rubini & Kroah-Hartman, *Linux Device Drivers*, 3ª ed.** (gratuito em lwn.net/Kernel/LDD3) — a referência clássica de módulos de kernel. Datado em APIs, ainda insuperável em conceitos.
- **Documentação do kernel em `Documentation/scheduler/`** — `sched-design-CFS.rst` e `sched-ext.rst` descrevem as classes de escalonamento direto da fonte.
- **Bootlin — *Embedded Linux System Development* (slides gratuitos, bootlin.com/docs)** — o melhor material aberto sobre toolchain, Buildroot, Yocto e boot em embarcado.
- **Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (ostep.org)** — capítulos de escalonamento (MLFQ, RR) e de mecanismos de troca de contexto, com a melhor explicação intuitiva disponível.
- **`man 2 syscall`, `man 7 vdso`, `man 7 sched`** — a fronteira userspace/kernel documentada de forma normativa.
- **Axboe, *Efficient IO with io_uring*** — o artigo do autor explicando por que a syscall por operação virou gargalo e como o ring buffer resolve.
