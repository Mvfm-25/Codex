# Laboratório de Sistemas Operacionais
## [08-10][mvfm]
---
### Sala com 5 pessoas. Professor incluso.
- Parecendo aula do Filipo incrivelmente, conversando sobre o mercado & como colocar software no ar.
- Marcado hoje no cronograma como :
    - **Escalonamento no Linux. Classes de escalonamento.**
- Não sei porque veio tão pouca gente hoje.
- Ainda assim, materiais para o que seria o conteúdo dado está disponível no moodle :
    - [Digging into the Linux Scheduler](https://deepdives.medium.com/digging-into-linux-scheduler-47a32ad5a0a8)
    - [Documentação Oficial sobre o Linux Scheduler](https://www.kernel.org/doc/html/latest/scheduler/)
- "*Não aprendam framework. Não aprendam linguagem. Aprendam C, a única linguagem que vocês vão precisar.*"
- p.s. : Tutorial 3.0 foi disponibilizado pelo moodle também :
    - **[Criando a política de escalonamento SCHED_LOW_IDLE](https://moodle.pucrs.br/pluginfile.php/6111016/mod_resource/content/9/SCHED_LOW_IDLE.html)**
        - Já atualizei o repositório pra continuar o desenvolvimento dessa atividade, mas não acho que seria necessário criar uma nova branch.
- Lembrando :
    - $T_n$ -> Tarefas Normal. $T_i$ -> Tarefas Idle. $T_{li}$ -> Tarefas Low-Idle.
    - $T_n$ preemptam outras $T_n$
    - $T_n$ preemptam $T_i$
    - $T_n$ & $T_i$ preemptam $T_{li}$

### Artigo 01 - Princípios do Scheduler.
- Assuntos listados pelo autor :
    1. "*Some of the main problems that task scheduling has to deal with*"
    2. "*The linux scheduler Core in some details.*"
    3. "*A high-level overview of some the scheduling classes available*"
    4. "*How all the above is implemented in the source code.*"
- O que um scheduler precisa fazer? O que ele precisa se certificar que aconteça?
    1. De que todo processo rodando tenha sua chance de estar rodando na CPU.
    2. Alguns processos podem ter prioridade maior que outros.
    3. Que tais processos, de alta-prioridade, não sejam fominhas. Impedindo de outros rodarem na CPU também.
    4. Qualquer processo consiga ser interrompido a qualquer hora caso um processo de maior prioridade necessite rodar agora.
    5. Impedir ataques (até não-intencionais) de interfirirem seu equilíbrio.

### Artigo 01 - Anatomia do Scheduler.
- Artigo descreve a seguinte imagem como uma "*visão à 10mil pés dos componentes mais importantes do Scheduler*".
    - O autor fala que essa é uma visão bem, bem simplificada do que ele vai nos mostrar ao decorrer do artigo. Não entendi muito bem então o propósito então, caso ele realmente é tão simples quanto ele diz ser.
![Componentes principais.](assets/scheduler.webp)
- **RunQueue**
    - Essencialmente, o ponto de encontro de todas informações importantes para as estruturas de dados no scheduler. Existe apenas uma única runqueue por CPU, sempre.
![Runqueue](assets/runqueue.webp)
