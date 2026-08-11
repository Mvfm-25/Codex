# Laboratório de Sistemas Operacionais
## [11-08-26][mvfm]
---
### Conceitos Fundamentais de Linux Embarcado
- Conceito de Linux embarcado de acordo com os slides do sor é basicamente o seguinte : 
	- '*Linux Embarcado é aquele Linux que é embarcado.*' 
	- Gee, thanks.
- Por ser de código aberto, aproveitamos de seu ecossistema para o uso de inúmeras bibliotecas ( De hardware, rede, gráficas, criptográficas etc. )
- Projetamos & desenvolvemos rápidamente com esse contexto.
- '*Se o sistema embarcado usa apenas software livre, o custo para o desenvolvimento de tal é praticamente zero.*'
	- O que nos permite gastar MAIS em coisas inúteis.
	- Call it WB thinking.

### Processadores & Arquiteturas
- Kernel Linux suporta nativamente uma ampla variedade de arquiteruras x64 & x32 bits.
	1. x86 & x86-64. Tanto em máquinas generalistas e embarcados.
	2. ARM ( Multimídia, industrial )
	3. PowerPC ( Aplicações industriais de tempo real )
	4. MIPS ( programas de rede )
	5. SuperH ( Decodificadores & aplicativos multimídia )
	6. Blackfin
	7. MicroBlaze
	8. Coldfire, Pontua¸c˜ao, Ladrilho, Xtensa, Cris, FRV, M32R.
- Tanto arquiteturas com e sem MMU são suportadas. 
- Além disso, o kernel suporta nativamente uma ampla variedade de barramentos de comunicação : 
	1. I2C
	2. SPI
	3. CAN
	4. 1-wire
	5. SDIO
	6. USB
- Rede também :
	- Ethernet, Wi-Fi, Bluetooth, CAN, etc.
	- IPv4, IPv6, TCP, UDP, SCTP, DCCP, etc.
	- Firewall, roteamento avan¸cado, multicast

### Plataformas de Hardware
- Plataforma de Avaliação do Fornecedor System-On-Chip (SoC)
	- Usualmente carom, mas muitos periféricos estão embutidos. Geralmente inadequado para produtos finais.
- Módulo de Componente
	- Pequena placa com apenas CPU/RAM/flash e alguns outros componentes principais com conectores para acessar todos os outros periféricos.
	- Pode ser usado para criar produtos finais em pequenas e médias quantidades.

