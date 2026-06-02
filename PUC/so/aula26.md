# Sistemas Operacionais
## [01-06-2026][mvfm]
---
### Hardware de E/S : Conceitos básicos
- Conceitos básicos : 
	1. Porta
		Ponto de conexão para o dispositivo se comunicar com o computador
	2. Barramento
		Conjunto de fios e um protocolo rigidamente definido que especifica um conjunto de mensagens.
	3. Controlador
		Eletronica que opera a porta, barramento em dispositivo ( Hot Adapter )

### Estrutura típica de Barramento
![Estrutura típica](assets/barramento.png)
1. Barramento PCI
	Conecta os componentes de alta velocidade, especificados como a memória e a CPU.
2. Barramento de Expansão
	Disponível para os dipositivos mais lentos, como as entradas E/S. Tela, teclado etc.
3. SCSI
	Barramento especificamente para o armazenamento.
- Aula tá sendo o Filipo contando histórias de novo
- Nenhuma vontade de desenvolver o trabalho por enquanto, chegando em casa eu me viro
	- Mas que saco
	- Todas as aulas são assim, basicamente.
	- Chato
	- :[

### Registradores de Porta E/S
- Normalmente, uma porta E/S é composta por quatro registradores, cada um servindo seu propósito único :
![Exemplos](assets/reges.png)
	1. Data-In
		Lido pelo host para obter entrada.
	2. Data-Out
		Escrito pelo host para enviar saída.
	3. Status
		Indica estados atuais ( erro, comando pronto, ocupado )
	4. Control
		Escrito pelo host para iniciar comando ou mudar modo. 

### Polling ( Consulta )
- No início do slide, o conceito de **Handshaking* se é definido : 
	- "*  O host lê repidamente o bit $busy$ até que ele se torna zero. *"
- Isso por si só não ajuda muito.
- A imagem não melhora também.
![Polling](assets/polling.png)
