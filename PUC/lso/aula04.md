# Laboratório de Sistemas Operacionais
## [13-08-26][mvfm]
---
### Sunday, Bloody Sunday
- '*Primeiro vamos ter que falar de ambientes de desenvolvimento.*'
	1. Codespace
		- Essa é a disciplina que mais estressa o Codespaces. Não fiquem surpresos em terem gasto todos os seus tokens de uso.
	2. Nativa (LINUX)
		- NENHUM COMENTÁRIO
		- Thank you professor, i'll think about NOTHING
	3. Máquina Virtual
		- NENHUM COMENTÁRIO
	4. Docker
- Aula vai focar na configuração do ambiente por meio do Codespace.
	- Vou aproveitar que é Debian aqui & tentar seguir por onde estou.
- '*Criação de uma distribuição*'
	- Whatever that means.

### O que é o Buildroot?
- '*is an Embedded Linux Build System*'
	- Yeah no shit
- '*Seu objetivo é simplificar e automatizar o processo de construção de uma distribuição Linux embarcado.*'
![Visão geral do BuildRoot](assets/buildroot_geral.png)
	- Fontes, não arquivos binários pré-compilados.
	- Buildroot também gera o compilador, assim como todas as ferramentas que estão vindo junto com a toolchain.
- Aula intiera foi consumida pelo tempo de compilar o buildroot em ambientes de codespaces. 
- Estou meio que trapaceando pois aproveitei que meu ambiente local já é Debian, então é possível que esteja um pouquinho avançado comparado aos meus colegas.
	- SUCKS TO SUCK LOSERS BLEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEh

### Fucking Thing Sucks
- Não acho que vou conseguir buildar tudo de uma única vez, entçao para a próxima vez que eu abrir esse note, rode o seguinte comando na pasta 'penguosis/buildroot' :
	- **make linux-menuconfig**
- That's all folks!
