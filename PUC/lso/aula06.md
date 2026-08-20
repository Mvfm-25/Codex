# Laboratório de Sistenas Operacionais
## [20-08-2026][mvfm]
---
### As it goes down.
- [Tutorial inicial do BUILDROOT](https://moodle.pucrs.br/pluginfile.php/6110961/mod_resource/content/7/Tutorial%201.1_%20Buildroot%20e%20QEMU%20%28v1.2%29.html)
- Sempre se certficar do buildroot está '*íntegro*' como o sor colocou.
	- Ou seja, só chegar na pasta e rodar o MAKE.
- O que então me indica que aula passada foi simplesmenete para a configuração restante do ambiente.
- Passo o fim de semana agora configurando o que falta. Ou seja, praticamente tudo.
	- Último comando dele foi **make MAKEINFO=false**, imagino que simplesmente após o **make menu-config** que eu ainda estou rodando.
	- Desligar o buildroot com '*poweroff*'
	- '*Toda vez que eu altero, eu rodo simplesmente o 'make' de novo.*'
- Um erro típico é literal só se esquecer de rodar o make depois das alterações.
- Yeah no shit i have to compile my code.
- Muita coisa que ele tá fazendo aparece direto no manual, então não deve ser muito chato fazer isso
	- '*Tempo é dinheiro*' falando sobre decorando, copiando & colando o comando para rodar o QEMU
	- O que ele faz é um scriptzinho (uma sequência de comandos dentro de um arquivo). Um ponto sh?
- **start-qemu.sh**
	- '*Fazer isso pelo terminal, ou criar o arquivo manualmente caso sejam leigos. Mas eu sei que vocês não são leigos*'
	- $ qemu-system-i386 --kernel buildroot/output/images/bzImage --hda buildroot/output/images/rootfs.ext2 --nographic --append "console=ttyS0 root=/dev/sda" 
- Parece muito cursinho de linux essa parte da cadeira. Muito legal que temos isso, mas poderia ter sido um pouco mais cedo na graduação. Tive que aprender isso tudo sozinho algum tempo atrás.
	- Fuck my worthless chud life.

### Configurando a Rede
- [Tutorial de rede mencionado](https://moodle.pucrs.br/pluginfile.php/6110963/mod_resource/content/4/1.2%20-%20qemu-network.html)
- Tendo tudo isso feito, vamos só nos certificar que está tudo funcionando direitinho.
	- Seguir o tutorial pelo **1.2.** até o passo **Desafio**.
	- '*Até o passo 4, é literal só copiar & colar.*'
- Qual o endereçi IP de um docker que a recém foi levantado? O do host?
	- '*Não*'
	- Ah, okay, obrigado por explicar.
- Pela visão do **DHCP**, a máquina virtual é vista como outro endereço por si só.
	- Criando na máquina Host uma rede virtual, uma switch.
	- A switch criada na host vai ter a interface física do host & uma virtual que conecta a VM/Docker.
- '*O roteador que temos em casa é tanto um roteador quanto uma switch.*'
- O modo **NAT** é outra maneira de fazer isso, sem ter que gastar tanto I.P.
	- A gente está vendo bastante coisa de redes, mas como o Xavier é professor de redes isso já faz bastante sentido.
	- Uma rede local, um único IP
	- Pssando pelo IP(externo), temos IP's locais. Aqui tem o **NAT** - traduções de endereços.
	- É portforwading. Essencialmente... Define-se um port para o IP externo que re-direciona a conexão para um dos IP's locais.
- O tutorial vai mostrar como fazer pelo modo grid, não o modo NAT. Justamente porque não nos importamos tanto em quantos IPs vamos estar gastando, lol.
- Aula foi basicamente isso de novo, configuração das partes que faltava para o Buildroot com alguns fun facts de redes.
	- Visão bem geral do semestre essas aulas.
- Quem responde o PING?
	- O próprio sistema operacional.

### O que ficou faltando
- Rodar **make MAKEINFO=false** em casa.
