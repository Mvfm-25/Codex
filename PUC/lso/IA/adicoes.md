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

---

## Aula 03 — MMU, Barramentos e o Que Faz um Linux Ser "Embarcado"

### A frase circular do slide, e a definição que funciona

As notas registram a definição inútil — "*Linux embarcado é aquele Linux que é embarcado*" — e o sarcasmo é justo. Uma definição operacional: **Linux embarcado é Linux rodando num sistema em que o hardware foi escolhido para uma função específica, o software inteiro é montado pelo desenvolvedor, e não existe distribuição, gerenciador de pacotes ou usuário administrando a máquina.**

O que muda na prática, em relação a um Debian de desktop:

| | Distribuição de propósito geral | Linux embarcado |
|---|---|---|
| Rootfs | milhares de pacotes, `apt` | dezenas de binários, imagem única |
| Init | systemd | BusyBox `init` ou systemd enxuto |
| libc | glibc (~10 MB) | **musl** ou **uClibc-ng** (~1 MB) |
| Utilitários | GNU coreutils (um binário por comando) | **BusyBox** (um binário para tudo) |
| Atualização | pacote a pacote | imagem inteira, **A/B** com rollback |
| Boot | GRUB → initramfs → systemd | U-Boot → kernel → init, em segundos |

O **BusyBox** merece destaque porque é a peça mais característica do ecossistema: um único executável que implementa `ls`, `cp`, `sh`, `ping`, `tar` e mais de trezentos outros comandos, decidindo qual rodar pelo nome com que foi invocado (`argv[0]`, via links simbólicos). Trezentos comandos em menos de um megabyte. É por isso que ele é chamado de "o canivete suíço do Linux embarcado", e é o que vai aparecer dentro do rootfs gerado pelo Buildroot.

A observação das notas sobre custo — "*se o sistema usa apenas software livre, o custo de desenvolvimento é praticamente zero*" — merece uma ressalva que a disciplina inteira vai demonstrar: o custo de **licença** é zero; o custo de **engenharia** não é. As semanas gastas compilando toolchain, configurando rede e depurando boot são exatamente esse custo aparecendo. A troca é real e geralmente vale a pena, mas não é gratuita.

---

### MMU ou não-MMU: a maior bifurcação da lista

A lista de arquiteturas das notas termina com "*tanto arquiteturas com e sem MMU são suportadas*", em uma linha. Essa linha esconde a diferença mais profunda de todo o campo, porque **sem MMU o Linux deixa de ser o Linux que se aprende em Sistemas Operacionais**.

A **MMU** (*Memory Management Unit*) é o hardware que traduz endereços virtuais em físicos. Sem ela, todo processo enxerga a memória física crua, e desaparecem de uma vez:

| Recurso | Com MMU | Sem MMU (uClinux) |
|---|---|---|
| Espaço de endereçamento por processo | isolado | **compartilhado, físico** |
| Proteção entre processos | sim | **nenhuma** — um ponteiro errado corrompe o vizinho |
| `fork()` | copy-on-write | **não existe** — só `vfork()` |
| Memória virtual / swap | sim | não |
| Paginação sob demanda | sim | não — o binário inteiro vai para a RAM |
| Fragmentação de heap | irrelevante (páginas) | **problema real e fatal** |
| Formato de binário | ELF | **bFLT** / ELF-FDPIC |

A ausência de `fork()` é a que mais quebra código existente. `fork()` depende de duplicar a tabela de páginas e marcar tudo como copy-on-write — sem tabela de páginas, não há o que duplicar. O substituto é `vfork()`, que **suspende o pai** até o filho chamar `exec()` ou sair, e em que pai e filho compartilham a mesma memória. Qualquer programa que faça `fork()` e continue rodando nos dois ramos precisa ser reescrito.

A fragmentação também deixa de ser um detalhe: com MMU, a memória de um processo é contígua em endereços virtuais mesmo estando espalhada fisicamente. Sem MMU, uma alocação grande precisa de um bloco físico contíguo de verdade — e um sistema que rodou por semanas pode falhar em alocar 64 KB tendo 2 MB livres, espalhados.

Onde isso aparece: microcontroladores Cortex-M grandes, ColdFire, Blackfin, alguns ARM antigos. Na prática, hoje, é território cada vez menor — quando o hardware é pequeno a esse ponto, costuma ser mais sensato usar um RTOS (Zephyr, FreeRTOS) do que espremer um Linux mutilado. A existência do não-MMU é mais interessante como lição sobre o que a MMU realmente compra.

---

### Os barramentos, em uma tabela que serve de referência

As notas listam I2C, SPI, CAN, 1-Wire, SDIO e USB sem diferenciá-los. Como o semestre vai esbarrar neles, vale a comparação:

| Barramento | Fios | Velocidade típica | Topologia | Uso característico |
|---|---|---|---|---|
| **1-Wire** | **1** (+ terra) | 16 kbps | multiponto, endereçado | sensor de temperatura (DS18B20), EEPROM de identificação |
| **I²C** | **2** (SDA, SCL) | 100 k / 400 k / 3,4 M | multi-mestre, 7 bits de endereço | sensores, RTC, EEPROM, configuração de periféricos |
| **SPI** | **4** (MOSI, MISO, SCK, CS) | 1–100 Mbps | um mestre, um CS por escravo | flash NOR, displays, ADC rápido, rádio |
| **SDIO** | 4–8 de dados | até ~100 MB/s | ponto a ponto | cartão SD, eMMC, Wi-Fi em módulo |
| **CAN** | 2 (par diferencial) | 1 Mbps (5 Mbps no CAN-FD) | barramento, arbitragem por prioridade | automotivo, industrial — **tolerante a ruído** |
| **USB** | 4 | 12 Mbps – 10 Gbps | árvore, mestre único (host) | tudo |

Os dois eixos que explicam as escolhas:

- **Fios contra velocidade.** I²C usa dois fios para $N$ dispositivos porque endereça por software; SPI usa um fio de seleção por dispositivo e por isso é muito mais rápido (não há overhead de endereçamento) mas não escala em número. A regra prática: SPI quando importa throughput, I²C quando importa contagem de pinos.
- **CAN é o estranho, e é estranho de propósito.** Ele é o único projetado para ambiente eletricamente hostil: sinalização diferencial, arbitragem não-destrutiva por prioridade de mensagem (o nó de maior prioridade vence sem colisão e sem retransmitir), e detecção de erro com desligamento automático de nó defeituoso. É por isso que ele está dentro de todo carro — e por que o professor, sendo de redes, vai voltar ao assunto.

Um detalhe que costuma morder: no Linux, **CAN não é um barramento de periférico, é uma família de sockets**. Usa-se `socket(PF_CAN, SOCK_RAW, CAN_RAW)` e a interface aparece como `can0` ao lado de `eth0`. Isso alinha o CAN com a pilha de rede (`ip link set can0 up type can bitrate 500000`) em vez de com o modelo de driver de caractere dos outros barramentos.

---

### Sobre a lista de arquiteturas: quais realmente importam

A lista das notas é fiel ao slide, e o slide está datado. Vale o estado atual, porque isso afeta o que o Buildroot pode gerar:

- **ARM** é o padrão de fato do Linux embarcado. Cortex-A para Linux completo; a maior parte do mercado.
- **ARM64 (AArch64)** é o crescimento atual, inclusive em placas baratas.
- **RISC-V** é o entrante sério — arquitetura aberta, sem royalties, com suporte mainline no kernel e alvo válido no Buildroot.
- **x86/x86-64** aparece em embarcado industrial onde importa compatibilidade com software existente, e é o que a disciplina usa via **QEMU** (`qemu-system-i386`, na Aula 06) justamente para não exigir hardware real.
- **MIPS** perdeu relevância; a MIPS Technologies migrou para RISC-V em 2021.
- **PowerPC** sobrevive em nichos (aeroespacial, automação de alta confiabilidade).
- **SuperH, Blackfin, MicroBlaze, Cris, FRV, M32R** são história. Várias dessas arquiteturas foram **removidas do kernel mainline** ao longo dos últimos anos por falta de mantenedor — Blackfin, Cris, FRV, M32R saíram entre 4.17 e 5.x. A lista do slide é de uma época em que elas ainda eram suportadas.

A lição, para além dos nomes: o Linux suporta muitas arquiteturas porque **a camada `arch/` do kernel é uma interface bem definida** — a maior parte do kernel é independente de arquitetura, e portar significa implementar um conjunto conhecido de funções. É o mesmo argumento de *narrow waist* que aparece em compiladores, aplicado a um sistema operacional.

---

## Aula 04 — Buildroot: o Que Ele Constrói, e Por Que Demora Tanto

### Toolchain cruzada: o vocabulário que falta

As notas registram o fato central — "*o Buildroot também gera o compilador, assim como todas as ferramentas que vêm junto com a toolchain*" — e o "*yeah, no shit*" sobre a definição de build system. O que falta é por que gerar o compilador é necessário, e não uma extravagância.

**Compilação cruzada** é compilar num computador (o *host*) código que roda em outro (o *target*). Três máquinas entram na conversa, e os nomes são padronizados:

| Termo | O que é | No caso da disciplina |
|---|---|---|
| **build** | onde o compilador é compilado | seu Debian x86-64 |
| **host** | onde o compilador vai rodar | seu Debian x86-64 |
| **target** | para onde o compilador gera código | i386 dentro do QEMU |

Quando `host ≠ target`, a toolchain é **cruzada**. Ela é identificada por uma *tupla*, que é aquele nome longo que aparece em `output/host/bin/`:

```
arm      -   buildroot   -   linux   -   gnueabihf
 │             │              │              │
 arquitetura   vendor         SO             libc + ABI
```

E o compilador cruzado não é um programa isolado — é um conjunto:

1. **binutils** — o montador (`as`) e o ligador (`ld`) para a arquitetura alvo.
2. **GCC** — o compilador propriamente dito.
3. **libc** — glibc, musl ou uClibc-ng, **compilada para o alvo**.
4. **headers do kernel** — as definições de syscalls e `ioctl`s da versão de kernel que vai rodar.
5. **sysroot** — o diretório que imita a raiz do alvo, onde o compilador procura headers e bibliotecas em vez de olhar `/usr/include` do host.

O sysroot é a peça conceitualmente importante: sem ele, compilar um programa para ARM acabaria incluindo o `stdio.h` do seu x86-64 e ligando contra a glibc do seu Debian. O resultado compilaria e não rodaria. Todo erro clássico de compilação cruzada é, no fundo, um erro de sysroot.

**O que o Buildroot entrega no final**, em `output/images/`:

- `bzImage` ou `zImage` — o **kernel**, configurado e compilado para o alvo.
- `rootfs.ext2` / `rootfs.tar` / `rootfs.squashfs` — o **sistema de arquivos raiz** com BusyBox e o que mais foi selecionado.
- o **bootloader** (U-Boot, em hardware real; dispensável sob QEMU, que carrega o kernel direto).
- opcionalmente um *device tree blob* (`.dtb`), descrevendo o hardware para o kernel.

A Aula 06 usa exatamente os dois primeiros: `--kernel buildroot/output/images/bzImage --hda buildroot/output/images/rootfs.ext2`.

---

### Buildroot contra Yocto: a escolha que o professor já fez por vocês

Vale saber o que existe do outro lado, porque é a primeira pergunta em qualquer entrevista sobre embarcado.

| | **Buildroot** | **Yocto / OpenEmbedded** |
|---|---|---|
| Modelo | `make menuconfig` + Makefiles | receitas BitBake em Python/shell |
| Saída | **uma imagem**, monolítica | imagem **+ feed de pacotes** (`.ipk`/`.rpm`) |
| Curva de aprendizado | horas | semanas |
| Rebuild incremental | fraco — mudanças de config pedem rebuild do zero | forte, com cache de estado (`sstate`) |
| Atualização em campo | imagem inteira (A/B) | por pacote **ou** imagem |
| Tamanho do projeto | pequeno/médio, equipe pequena | produto de longa vida, várias placas |
| Quem usa | protótipos, dispositivos simples, ensino | automotivo (AGL), industrial, produtos com anos de suporte |

A escolha do Buildroot para uma disciplina é claramente a certa: em uma aula dá para chegar a um sistema que dá boot, o que com Yocto não aconteceria. O trade-off aparece quando o projeto cresce — e o sintoma é exatamente o que as notas vão registrar na Aula 06, "*toda vez que eu altero, eu rodo simplesmente o make de novo*".

---

### Por que a compilação consome uma aula inteira

A observação das notas — "*aula inteira foi consumida pelo tempo de compilar o Buildroot em ambientes de Codespaces*" — não é azar de infraestrutura. É estrutural, e entender por quê rende tempo economizado.

**O GCC é compilado três vezes.** Existe um problema de ovo e galinha: para compilar a libc do alvo é preciso de um compilador para o alvo; para compilar um compilador completo é preciso da libc. A saída é o *bootstrap* em estágios:

1. **GCC estágio 1** — compilador mínimo, sem suporte a libc, só o bastante para compilar o kernel e a própria libc.
2. **libc** — compilada com o estágio 1.
3. **GCC estágio 2 (final)** — compilador completo, agora ligado contra a libc recém-construída.

Some-se a isso binutils, o kernel inteiro, BusyBox e todos os pacotes selecionados — **tudo a partir do código-fonte**, como as notas corretamente destacam ("fontes, não binários pré-compilados"). Um build do zero razoavelmente configurado leva de 30 minutos a algumas horas, e é dominado por I/O e por processos de compilador de vida curta. Num Codespace com 2 vCPUs e disco de rede, é pior ainda.

**As quatro alavancas que realmente ajudam:**

```bash
# 1. Paralelismo — o padrão do Buildroot é conservador
make BR2_JLEVEL=$(nproc)

# 2. ccache — reaproveita objetos entre builds; ligar em Build options
#    BR2_CCACHE=y

# 3. Toolchain externa — pula todo o bootstrap do GCC (economia maior de todas)
#    Toolchain → Toolchain type → External toolchain

# 4. Baixar os fontes antes, para separar rede de CPU
make source
```

**E as três armadilhas**, que valem mais que as alavancas:

1. **Nunca rode `make clean`** para "resolver" um problema. Ele apaga `output/` inteiro, incluindo a toolchain, e recomeça do zero. Para reconstruir só um pacote, existe `make <pacote>-rebuild` (recompila) e `make <pacote>-reconfigure` (refaz o configure também).
2. **O Buildroot não reconstrói corretamente após mudanças de configuração.** Isso é documentado e assumido pelo projeto: remover um pacote do `menuconfig` não o remove do `output/` já construído. Mudanças significativas de config pedem, sim, um build limpo — é a fraqueza real da ferramenta frente ao Yocto.
3. **Não interrompa no meio.** Um `Ctrl-C` durante a extração ou o patch de um pacote deixa o diretório em estado inconsistente, e o erro que aparece depois é obscuro. Se acontecer, `make <pacote>-dirclean` conserta aquele pacote sem sacrificar o resto.

O comando que as notas anotam para a próxima sessão, `make linux-menuconfig`, encaixa exatamente nesse modelo: ele abre a configuração **do kernel** (diferente de `make menuconfig`, que é a do Buildroot). Depois de salvar, é preciso rodar `make` de novo para a mudança chegar ao `bzImage` — e é preciso `make linux-update-defconfig` para que a alteração seja **persistida** no defconfig do projeto em vez de viver apenas em `output/`.

---

## Aula 06 — Dissecando o QEMU e as Três Formas de Dar Rede a uma VM

### Cada flag do comando, e o que quebra sem ela

As notas registram o comando e a recomendação do professor de guardá-lo num script. Vale entender cada pedaço, porque quando o boot falha é sempre uma dessas flags.

```bash
qemu-system-i386 \
  --kernel buildroot/output/images/bzImage \
  --hda    buildroot/output/images/rootfs.ext2 \
  --nographic \
  --append "console=ttyS0 root=/dev/sda"
```

| Flag | O que faz | O que acontece sem ela |
|---|---|---|
| `qemu-system-i386` | emula uma máquina **i386 inteira** (CPU, chipset, periféricos) | — |
| `--kernel` | carrega o kernel **direto na memória**, pulando o bootloader | seria preciso U-Boot ou GRUB dentro de uma imagem de disco bootável |
| `--hda` | anexa o arquivo como o primeiro disco IDE do convidado | o kernel dá boot e entra em **kernel panic**: "unable to mount root fs" |
| `--nographic` | desliga a janela de vídeo e liga o console serial ao seu terminal | abre uma janela SDL e o terminal fica mudo |
| `--append` | passa a **linha de comando do kernel** | o kernel não sabe onde está a raiz nem para onde falar |

Os dois parâmetros dentro do `--append` são os que mais causam confusão:

- **`console=ttyS0`** diz ao kernel para mandar as mensagens de boot e abrir o console na **primeira porta serial**, não no vídeo. É o par obrigatório do `--nographic`: um sem o outro resulta em um sistema que dá boot perfeitamente e não mostra nada. Quase todo relato de "o QEMU trava sem imprimir nada" é esse par desalinhado.
- **`root=/dev/sda`** diz qual dispositivo montar como raiz. Note que é `sda` e não `sda1`: a imagem gerada pelo Buildroot é um sistema de arquivos **cru**, sem tabela de partições. Montar `/dev/sda1` falharia porque essa partição não existe.

**Sobre o "scriptzinho".** A observação do professor ("*um ponto sh?*") merece o complemento que torna o script robusto:

```bash
#!/bin/sh
# start-qemu.sh — chmod +x start-qemu.sh, depois ./start-qemu.sh
set -eu                                    # aborta em erro e em variável indefinida
IMG=buildroot/output/images
exec qemu-system-i386 \
  -kernel "$IMG/bzImage" \
  -hda    "$IMG/rootfs.ext2" \
  -nographic \
  -append "console=ttyS0 root=/dev/sda"
```

Duas coisas que economizam sofrimento: com `-nographic`, **`Ctrl-C` vai para o convidado**, não para o QEMU — para sair, use `Ctrl-A` seguido de `x`, ou desligue por dentro com `poweroff`, como as notas registram. E `Ctrl-A` depois `c` abre o monitor do QEMU, de onde dá para inspecionar o estado da máquina emulada.

---

### As três formas de dar rede, e por que o tutorial escolheu a difícil

As notas cobrem bem a distinção conceitual entre bridge e NAT e registram a escolha do tutorial ("*vai mostrar como fazer pelo modo grid, não o modo NAT*"). O QEMU oferece na verdade **três** modos, e o terceiro é o que quase todo mundo usa sem saber.

| Modo | Como funciona | IP do convidado | Ping de fora? | Precisa de root? |
|---|---|---|---|---|
| **User-mode (SLIRP)** — padrão | QEMU implementa uma pilha TCP/IP em espaço de usuário e faz NAT por software | `10.0.2.15`, sempre | **não** | não |
| **TAP + bridge** | interface virtual no host, ligada por uma switch virtual à placa física | do **DHCP da rede real** | **sim** | sim |
| **TAP + NAT/iptables** | interface virtual, com o host roteando e mascarando | sub-rede privada do host | só com port forwarding | sim |

**O user-mode é o padrão e é invisível.** Rodar `qemu-system-i386` sem nenhuma flag de rede já dá ao convidado uma placa de rede funcional, com DHCP, DNS e saída para a internet — tudo emulado pelo próprio processo do QEMU. Ele não precisa de privilégio nenhum porque nunca toca na rede real: as conexões do convidado viram chamadas `socket()` normais do processo QEMU no host.

E aqui está a resposta para uma pergunta que a aula deixa implícita: no user-mode, **o convidado não pode ser pingado de fora**, e frequentemente não consegue nem pingar para fora. O motivo é que ICMP não é TCP nem UDP — para traduzir um ping, o QEMU precisaria de um socket raw, que exige privilégio. "Rede funciona mas ping não funciona" é o sintoma canônico do SLIRP, e confunde todo mundo na primeira vez.

**Por que o tutorial usa bridge.** Porque é o único modo em que o convidado é um **cidadão de primeira classe da rede**: ele pega IP do mesmo DHCP que o host, é visível e pingável de qualquer máquina do laboratório, e pode receber conexões sem port forwarding. Isso é o que as notas descrevem — "*pela visão do DHCP, a máquina virtual é vista como outro endereço por si só*", com a switch virtual tendo "*a interface física do host e uma virtual que conecta a VM*". Para medir desempenho de rede entre duas máquinas, que é o assunto da Aula 07, o bridge é praticamente obrigatório: o SLIRP mediria a pilha emulada do QEMU, não a rede.

A justificativa registrada nas notas ("*não nos importamos tanto com quantos IPs vamos gastar*") é a correta para um laboratório. Em produção a conta inverte, e daí o NAT.

**A analogia do roteador doméstico está certa e vale formalizar.** A caixa de casa acumula três funções que são conceitualmente distintas:

- **Switch** (camada 2) — encaminha quadros entre as portas pelo endereço MAC. É o que a `br0` faz.
- **Roteador** (camada 3) — encaminha pacotes entre redes diferentes pelo endereço IP.
- **NAT** (camada 3/4) — reescreve endereços e portas para que várias máquinas compartilhem um IP público.

Bridge no QEMU usa só a primeira. NAT usa as três. É por isso que uma máquina em bridge aparece na rede como se fosse física, e uma em NAT some atrás do host.

---

### Quem responde ao ping — a resposta completa

As notas fecham com a pergunta e a resposta curta: "*o próprio sistema operacional*". Está certo, e o detalhe é instrutivo.

Um ping é um pacote **ICMP Echo Request**. Diferente de uma conexão TCP, não existe processo esperando por ele: não há `listen()`, não há porta, não há daemon de ping. O pacote sobe até a camada IP do kernel, o handler ICMP o reconhece, monta um **Echo Reply** copiando o payload e o devolve — tudo dentro do kernel, sem que nenhum programa em espaço de usuário saiba que aconteceu.

Três consequências práticas:

1. **Uma máquina responde a ping mesmo sem nenhum serviço rodando.** Um rootfs de BusyBox com só um shell responde. É por isso que ping é a primeira ferramenta de diagnóstico: ele testa a pilha de rede sem depender de nada acima dela.
2. **Dá para desligar a resposta**, e muita gente desliga: `sysctl net.ipv4.icmp_echo_ignore_all=1`, ou uma regra de firewall. Um host que não responde a ping não está necessariamente fora do ar — conclusão que custa horas a quem não sabe disso.
3. **Sob QEMU, quem responde depende do modo de rede.** Em bridge, quem responde é de fato o kernel do convidado, e o ping mede o caminho completo. Em user-mode, como visto acima, geralmente não há resposta alguma. Verificar isso é a forma mais rápida de descobrir em que modo a VM está.

---

## Aula 07 — iperf: o Que "Velocidade de Rede" Realmente Mede

As notas desta aula são três linhas — tutorial 1.3, `iperf`, e a constatação honesta de estar atrasado no anterior. Como a ferramenta vai ser usada de verdade, vale o material que o tutorial pressupõe.

### Throughput, largura de banda e goodput não são a mesma coisa

Três palavras usadas como sinônimos e que medem coisas diferentes:

| Termo | O que é | Exemplo num link de 1 Gbps |
|---|---|---|
| **Largura de banda** | capacidade **nominal** do meio | 1000 Mbps |
| **Throughput** | o que efetivamente trafega, incluindo cabeçalhos | ~941 Mbps |
| **Goodput** | só os dados úteis da aplicação | ~930 Mbps |

A diferença entre 1000 e 941 não é perda nem defeito: é **overhead de protocolo**. Cada quadro Ethernet de 1500 bytes de payload carrega 20 bytes de cabeçalho IP, 20 de TCP, 14 de Ethernet, 4 de FCS, mais preâmbulo e intervalo entre quadros. A eficiência teórica máxima do TCP sobre Ethernet com MTU padrão é de aproximadamente **94%** — então 941 Mbps num link gigabit é o **valor correto**, não um resultado ruim. Medir 941 e concluir que a rede está com problema é o erro número um de quem usa iperf pela primeira vez.

### O modelo cliente-servidor, e as flags que importam

O iperf sempre precisa de **dois lados**: um servidor que escuta e um cliente que gera tráfego.

```bash
# No host (ou na outra VM) — servidor
iperf3 -s

# No convidado QEMU — cliente, 10 segundos de TCP
iperf3 -c 192.168.1.10

# UDP a 100 Mbps, para medir perda e jitter
iperf3 -c 192.168.1.10 -u -b 100M

# Quatro fluxos paralelos — costuma ser o que satura o link
iperf3 -c 192.168.1.10 -P 4

# Sentido inverso: o servidor envia, o cliente recebe
iperf3 -c 192.168.1.10 -R
```

**TCP e UDP medem coisas diferentes, e essa é a distinção central.**

- Em **TCP**, o iperf mede quanto o controle de congestionamento consegue empurrar. Não há perda reportada, porque TCP retransmite — a perda aparece indiretamente, como throughput menor e retransmissões contadas.
- Em **UDP**, o iperf envia numa taxa **que você escolhe** (`-b`) e reporta o que chegou. É assim que se mede **perda de pacotes** e **jitter**, que TCP esconde. A pegadinha: sem `-b`, versões antigas do iperf usavam 1 Mbps por padrão, e o resultado parecia absurdamente baixo.

### Por que um fluxo TCP único pode não saturar o link

Esse é o resultado que mais surpreende, e ele tem fórmula. O throughput máximo de uma conexão TCP é limitado pela janela e pela latência:

$$\text{Throughput}_{\max} = \frac{\text{Janela}}{\text{RTT}}$$

A quantidade relacionada é o **produto banda-atraso** (*bandwidth-delay product*): quantos bytes cabem "em voo" no cabo.

$$\text{BDP} = \text{Banda} \times \text{RTT}$$

Num link de 1 Gbps com 50 ms de RTT, $\text{BDP} = 10^9 \times 0{,}05 / 8 \approx 6{,}25\ \text{MB}$. Se a janela do TCP for os clássicos 64 KB, o teto é

$$\frac{65536\ \text{bytes} \times 8}{0{,}05\ \text{s}} \approx 10{,}5\ \text{Mbps}$$

— **1% do link**, sem nenhuma perda de pacote, sem nenhum problema de rede. O gargalo é a janela. A correção é o *window scaling* (RFC 1323, ligado por padrão no Linux) e o autotuning de buffer do kernel; medir com `-w` diferentes é como se demonstra o efeito. E é por isso que `-P 4` costuma dar um número maior que um fluxo único: quatro janelas em paralelo somam quatro vezes o teto.

Num laboratório com QEMU na mesma máquina, o RTT é microssegundos e o efeito some — o que se mede ali é a capacidade da **emulação**, não do cabo. Vale ter isso em mente ao interpretar números altos demais: tráfego entre convidado e host em bridge nunca toca a placa física.

### Três cuidados na hora de medir

1. **O gargalo pode ser a CPU.** Em VM, gerar 1 Gbps de tráfego custa ciclos reais. Se o `iperf` está com um núcleo em 100%, o número medido é o do processador, não o da rede. Olhar `top` durante o teste é parte do método.
2. **Meça nos dois sentidos.** Links assimétricos e drivers com desempenho diferente em TX e RX são comuns. A flag `-R` existe exatamente para isso.
3. **`iperf` e `iperf3` não conversam entre si.** São implementações independentes com protocolos de controle incompatíveis, e a mensagem de erro não deixa isso claro. Se o servidor é `iperf3`, o cliente também precisa ser.

---
