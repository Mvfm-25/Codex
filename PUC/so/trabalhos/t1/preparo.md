# Preparo — Apresentação T1 (Processos vs. Threads)

---

## Fala de abertura

> "O trabalho implementa um benchmark de concorrência em C — quatro experimentos tentando incrementar um contador até 1 bilhão: threads sem sync (T1), threads com mutex (T2), processos sem sync em memória compartilhada (P1), e processos com semáforo nomeado (P2). O objetivo era observar na prática o custo de cada mecanismo de sincronização e o comportamento com N = 2, 4 e 8 workers."

---

## Perguntas e Respostas

---

**P: Por que T1 acertou exatamente 1 bilhão se não tem sincronização?**

> "Boa pergunta — isso é o x86 te enganando. O processador Intel usa um modelo de memória chamado TSO (Total Store Order), que é bem mais rígido do que o padrão C exige. Quando uma thread sobrescreve o incremento de outra, a perdedora relê o valor atualizado da cache e continua loopando até bater no target. Em ARM ou RISC-V isso quase certamente não aconteceria — o contador ficaria abaixo de 1 bilhão."

---

**P: Mas P1 também não tem sync e deu overshoot. Por que o comportamento é diferente?**

> "Porque threads compartilham a mesma cache L1/L2, então a coerência de cache já resolve grande parte das corridas. Processos não — a memória compartilhada trafega via RAM, a janela de inconsistência é bem maior, e aí o overshoot aparece de verdade: `+1` com N=2, `+4` com N=8."

---

**P: T2 com N=4 foi mais lento que N=8. Isso não deveria ser o contrário?**

> "Parece contra-intuitivo, mas faz sentido dado o hardware — essa máquina tem 2 cores físicos e 4 lógicos. Com 4 threads brigando por um único mutex em 2 cores físicos, cada lock que falha vira context switch, e a cache line do mutex fica sendo transferida entre cores o tempo todo. Com 8 threads o scheduler distribui melhor a espera, o overhead de chaveamento por incremento cai, e no fim agregado fica mais rápido."

---

**P: O que é data race? Por que T1 tem isso se funcionou?**

> "Data race é quando dois workers acessam a mesma memória simultaneamente e pelo menos um está escrevendo, sem nenhuma sincronização no meio. Em C11 isso é comportamento indefinido — o compilador pode fazer qualquer coisa, inclusive otimizar o loop inteiro pra fora. Funcionou aqui porque compilamos em `-O0` e no x86. Em `-O2` o compilador pode cachear o contador num registrador, nunca mais ler da memória, e travar em loop infinito."

---

**P: O que é `volatile` e vocês usaram?**

> "Não usamos, e isso é um dos pontos problemáticos. `volatile` força o compilador a sempre ler a variável da memória em vez de manter num registrador. Sem ele, com otimizações altas, a leitura do contador dentro do `while` pode virar uma constante. Para sync correto de verdade o certo seria `_Atomic` do C11, que garante atomicidade além de visibilidade."

---

**P: Por que P2 escala tão mal? 8 workers deveriam ser mais rápidos.**

> "P2 não tem paralelismo real nenhum — a seção crítica cobre o incremento inteiro. Cada incremento exige `sem_wait` + `sem_post`, que são duas syscalls completas passando pelo kernel. Com N=8 o sys time (14m37s) ficou maior que o user time (14m34s) — o sistema passa mais tempo no kernel gerenciando fila de semáforo do que executando código de usuário. Adicionar mais workers só aumenta a fila de espera."

---

**P: Por que vocês fizeram `sem_unlink` antes do `sem_open`?**

> "Defesa contra semáforo órfão. Se o processo morreu no meio de uma execução anterior sem fazer cleanup, o semáforo nomeado ainda existe no sistema com o mesmo nome. Se a gente tentar criar com `O_EXCL` sem o unlink antes, o `sem_open` falha. Fazendo o unlink primeiro, garante que começa com um semáforo limpo."

---

**P: Qual modelo foi mais eficiente no geral — processo ou thread?**

> "Para esse tipo de trabalho — counter compartilhado com muita contenção — threads ganham fácil. T1 e T2 ficam na mesma ordem de magnitude de P1 e P2 respectivamente, mas com menos overhead de criação e sem precisar de IPC. Processos têm overhead maior de criação e a comunicação via memória compartilhada tem latência maior. A vantagem de processo é isolamento — se um filho crasha, não derruba os outros."

---

**P: Vocês não chamaram `pthread_mutex_destroy`. Isso está errado?**

> "Tecnicamente, POSIX exige que todo mutex inicializado tenha um destroy correspondente pra liberar recursos associados. Na prática, em Linux com mutex de storage estático, o kernel limpa tudo no exit e não vaza nada. Mas é um anti-padrão — se o mutex fosse alocado dinamicamente ou em contexto de biblioteca, daria leak real."

---

**P: E o `sem_close` que os filhos não chamam em P2?**

> "Esse é mais sério em teoria. Cada processo que faz `sem_open` incrementa um reference count interno do kernel pro objeto nomeado. Se os filhos não chamam `sem_close` antes do `exit`, o count pode ficar inconsistente quando o pai faz `sem_unlink`. Em Linux o kernel fecha tudo no exit, então na prática não vaza — mas é um gap de conformidade POSIX real."

---

**P: Por que usar `IPC_PRIVATE` no shmget de P1?**

> "Com `IPC_PRIVATE` o kernel garante um segmento exclusivo — não tem como colidir com uma chave que outro processo esteja usando. Se usasse uma chave fixa, tipo `ftok`, corria o risco de pegar um segmento de uma execução anterior ou de outro processo no sistema."

---

**P: Por que o Makefile compila com `-O0`? Não é melhor otimizar?**

> "Foi uma escolha consciente pra não esconder a corrida de dados em T1. Com `-O2` o compilador pode perceber que `counter_t1` é lido no loop sem nenhuma proteção e cachear o valor num registrador — a thread nunca re-lê da memória e trava em loop infinito. Deixando em `-O0`, cada acesso vai de fato à memória e o experimento termina. É uma muleta, mas é intencional pra fins de observação."

---

**P: `pthread_t threads[n]` — isso é um array de tamanho variável. Tem algum problema nisso?**

> "É um VLA — Variable Length Array, feature do C99. Funciona bem aqui porque N é pequeno (2, 4 ou 8), então vai pro stack sem problema. Se N fosse grande e arbitrário, seria arriscado por stack overflow. C11 tornou VLA opcional, então em compiladores mais restritivos poderia dar warning. Pro escopo do trabalho é totalmente válido."

---

**P: Em T2, o check `if (counter_t2 >= limit)` está dentro do lock. Por que não deixar fora pra ser mais rápido?**

> "Porque aí seria TOCTOU — Time Of Check To Time Of Use. Se você checar fora do lock, pode ser que entre o check e o lock outra thread incremente o contador. Você entraria na seção crítica achando que ainda tem trabalho, incrementaria além do target, e o resultado final ficaria acima de 1 bilhão. O check dentro do lock garante que a decisão e a ação são atômicas."

---

**P: O `sem_unlink` antes do `sem_open` não verifica erro. E se a syscall falhar por outro motivo?**

> "O erro do `sem_unlink` é silenciado de propósito — se o semáforo não existia, `unlink` retorna -1 com ENOENT, e tá tudo bem, era exatamente o que queríamos. Se falhar por outro motivo, tipo permissão, aí sim seria um problema não tratado. Mas dado o contexto — processo rodando com suas próprias permissões e semáforo criado por ele mesmo — o único caso real é o ENOENT."

---

**P: Por que `worker_t1` e `worker_t2` recebem `void *arg` em vez de direto o `long`?**

> "É a assinatura que o POSIX exige para a função de thread — `void *(*start_routine)(void *)`. A API foi feita assim pra ser genérica: você passa qualquer estrutura de dados pelo ponteiro e converte dentro. No nosso caso é só um `long *` que a gente derreferencia pra pegar o `limit`. Não tem como passar o valor diretamente — teria que ser sempre por ponteiro."

---

**P: Os filhos em P2 saem com `exit(0)` sem chamar `sem_close`. Isso não é vazamento?**

> "Em Linux não vaza recurso em runtime — o kernel fecha o file descriptor no `exit`. O problema é mais teórico: o reference count do objeto nomeado no kernel pode ficar incorreto se o pai fizer `sem_unlink` enquanto os filhos ainda têm o fd aberto. Na prática, nesse programa funciona porque o pai só faz `sem_unlink` depois de `wait` de todos os filhos. Mas POSIX diz que cada `sem_open` deve ter um `sem_close` correspondente no mesmo processo — então é uma não-conformidade real, mesmo que inócua aqui."

---

**P: Por que usar `long` pra o contador e não `int`?**

> "`long` em x86-64 Linux é 64 bits — comporta até ~9.2 × 10¹⁸. O target de 1 bilhão cabe em `int` de 32 bits, mas `long` dá margem pra overshoot sem overflow. Em P1 com N=8 já vimos `+4` de overshoot — se usasse `int` e o overshoot fosse grande o suficiente, daria wraparound e o resultado seria inválido."

---

## Perguntas com maior chance de aparecer

1. Por que T1 acertou 1 bilhão sem sync? **(TSO do x86)**
2. Por que T2 com N=4 foi mais lento que N=8? **(contenção em 2 cores físicos)**
3. Por que P2 não escala? **(2 syscalls por incremento, sem paralelismo real)**
4. Por que `-O0` no Makefile? **(data race escondida por otimização)**
5. O check em T2 está dentro do lock — por quê? **(TOCTOU)**
6. `sem_close` nos filhos de P2 — por que não foi feito? **(gap POSIX confirmado no código)**
