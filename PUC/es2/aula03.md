# Engenharia De Software II
## [20-03-2026][mvfm]

### Microserviços
- Continuação do uso do repositório do **PetClinic** como principal exemplo da cadeira
- Ele continua com a metodologia de "*Usaram x, mas isso é bom? Não sei... Mas tudo bem."
- Quando cheguei na cadeira, ele estava comentando sobre a quebra de serviços que é essencial para o conceito de Microserviços.
- **[Slides da aula](https://brpucrs-my.sharepoint.com/personal/10070245_pucrs_br/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F10070245%5Fpucrs%5Fbr%2FDocuments%2FDocumentos%2Fengenhariadesoftware2%2Fmicrosservicos%2Fmicrosservicos%2Epdf&parent=%2Fpersonal%2F10070245%5Fpucrs%5Fbr%2FDocuments%2FDocumentos%2Fengenhariadesoftware2%2Fmicrosservicos&ga=1)**

### Decomposição de Serviços - Nuvem
- Essencialmente, anterior a escrita de Stories, saber **o que** escrever como stories e logo após determinar o que vira issue.
	- Coisa que ainda não resolvemos na DB, incrivelmente.
- Paralelização de atarefas é citado como um ponto forte dessa metodologia.
- Mais pessoas trabalhando em menos coisas com resultados melhores ao mesmo tempo.
- Depois disso se coloca pontos fortes para se trabalhar com a nuvem
	1.**Escalabilidade**
	2.**Confiabilidade**
	3.**Elasticidade**

### Escalabilidade
- "*Capacidade de aumentar ou diminuir de modo rápido e fácil o tamanho ou a potência de uma solução TI ou de um recurso em específico.*"
- Um sistema é considerado escalável quando ele consegue lidar com cada vez mais trabalho ao decorrer do tempo.
- Podem ser escalados em duas direções
	- **Vertical**
		- *Scale up/down*
		- Capacidade de adicionar/remover poder computacional
		- RAM, GPU's
		- Exatamente o que tá acontecendo com **todos** os datacenters do mundo.
	- **Horizontal**
		- *Scale in/out*
		- Adiciona *nós de processamento*, ou remove de acordo com a carga de trabalho atual.
		- Não ficou muito claro pra mim se são necessariamente componentes de um servidor, ou os servidores em si.
		- Mas okay.

### Monolitos
- Aplicação que contém **toda** lógica de negócio em um grande bloco
	- Haha, get it.
- "**Apesar de divida em módulos, é implantada como um grande bloco.**"
![monolitos](assets/mono.png)

### Micro-Serviços
- O contrário essencialmente.
- Não se é entregue uma definição bonitinha como os monolitos anteriormente, mas é basicamente :
- **Além da divisão de módulos em si, também se é separado em bloquinhos diferentes de execução.**
![micro-serviços](assets/micro.png)
- Além disso, Sor nos mostra um pequenino gráfico para mostrar as principais caracteŕisticas de como um micro-serviço se comporta
![carmicro](assets/carmicro.png)
- Cadeira vai ser só isso, eu presumo.
- Ninguém está se divertindo, aparentemente nem o sor.

### Comparações
![Comparação](assets/c1.png)
![Comparação de novo](assets/c2.png)
- **Vantagens de Micro-Serviços**
	- Baixo acoplamento
	- Modularidade
	- Falha em um serviço não impacta os demais
	- Alta flexibilidade
	- Alto graude de flexibilidade
	- Facilidade de modificação
- **Desvantagens**
	- **Grande** chance de falha na comunicação entre os serviçoes
	- Dificuldade de gerenciar grande número de serviçoes
	- Necessidade de resolver problemas tais como latência de rede, balanceamento de carga e outros problemas de arquiteturas distribuídas
	- Teste mais complexo sob um ambiente distribuído
	- Implementação requer mais tempo
- Incrível que as desvantagens parecem mais críticas.
- Não me vendeu a ideia de *querer* implementar algo do gênero.
