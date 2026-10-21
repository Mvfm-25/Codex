# Laboratório de Sistemas Operacionais
## Professor : [Miguel Xavier](https://setrem.edu.br/personnel/miguel-xavier-2/)
---
### Avaliação
- **$G1 = (TP1 + TP2 + TP3 + TP4) / 4$** — média 5.0, **sem G2**.
---
#### Trabalhos
- [TP1 — SystemInfo](https://moodle.pucrs.br/mod/assign/view.php?id=3863537)
	- Imagem Linux via **Buildroot** com servidor REST em Python (porta 8080, `GET /status`) que lê informações do sistema só de `/proc` e `/sys`. Entrega **03/09, 17:30**.
- TP2 — entrega **01/10, 17:30**, em três partes :
	- [Desafios 1 e 2 do Tutorial 2.2](https://moodle.pucrs.br/mod/assign/view.php?id=3863566) — nova **chamada de sistema** + programa de teste.
	- [Desafio do Tutorial 2.3](https://moodle.pucrs.br/mod/assign/view.php?id=3863567) — **driver de dispositivo** como módulo do kernel.
	- [Escalonador SSTF (disco)](https://moodle.pucrs.br/mod/assign/view.php?id=3863568) — IO-Scheduler do Tutorial 2.4.
- TP3
	- ? — Card "Depuração e Escalonamento da CPU" (SCHED_LOW_IDLE, Ftrace). Apresentação prevista para 03/11.
- TP4
	- ? — Apresentação prevista para 01/12.
---
### Aulas
- [Página da disciplina no Moodle](https://moodle.pucrs.br/course/view.php?id=95228)
	- Cards : Introdução à Linux Embarcado, Criando uma Distribuição Linux Embedded, Syscall e Device Drivers, Depuração e Escalonamento da CPU.
- [Cronograma do Semestre](https://sarc.pucrs.br/Default/Export.aspx?id=273a562b-a64f-4761-bbf0-39389692af89&ano=2026&sem=2)
- [Aula01](./aula01.md)
	- Aula introdutória da disciplina.
- [Aula02](./aula02.md)
	- Aula de revisão, conceitos fundamentais & iniciais de Sistemas Operacionais.
- [Aula03](./aula03.md)
	- Conceitos fundamentais de sistemas embarcados, kernel linux.
- [Aula04](./aula04.md)
	- Ambientes de desenvolvimento (Codespace, nativo, VM, Docker) e introdução ao **Buildroot** como build system de Linux embarcado.
- [Aula06](./aula06.md)
	- Build do Buildroot e execução no **QEMU** via `start-qemu.sh`; configuração de rede — switch virtual, **NAT** e port forwarding.
- [Aula07](./aula07.md)
	- Etapa 1.3 do tutorial — medição de desempenho de rede com **iperf**.
- [Aula16](./aula16.md)
	- Registro de progresso no repositório da disciplina — desafio 1 da etapa 2.2 resolvido.
- [Aula20](./aula20.md)
	- **Escalonamento no Linux** — classes de escalonamento, tutorial 3.0 (**SCHED_LOW_IDLE**), princípios do scheduler e a **runqueue**.
- [Aula22](./aula22.md)
	- Funcionamento de **debuggers** via *function tracing* e a arquitetura do **GDBServer**.
---
### Adições IA
- [Material complementar gerado por IA](./IA/adicoes.md)

