# Engenharia de Software II
## [17-04-2026][mvfm]
---
### Gateway API
- Seguimos com o roteiro especificado no início do semestre.
- Exemplos bem bobinhos de acordo com o Júlio
- Princípios de isolamento de nossos micro-serviços
	- Exemplos práticos disso incluem : 
		1. Evita grande troca de mensagens entre o cliente e *nossos* microserviços
		2. Tratamento de requisitos **transversais**. Pelo que entendi, requisitos que *atravessam* muitos de nossos microserviços.
		3. Retirado direto do slide : "*Implementa uma fachada com protocolos mais amigáveis para aplicativos cliente*"
![[assets/eureka.excalidraw | 100%]]
- Em geral, deu pra entender que o Gateway está lá para esconder muito do que está por dentro da aplicação do negócio.
	- **Thanks patriot act**.
- Slides descrevem tal abordagem como um *proxy reverso* : 
	- Roteando solicitações para o microserviço apropriado, lidando com tarefas como *autenticação*, *limitação de carga*, *armazenamento em cache* etc.
	- Um grande agregador.
	![Api Gateway](assets/gateway.png)

### Backends For Frontends - BFF
- Not so friendly now.
- Hoje é um Sexta-Feira, só lembrando.
- *Padrão de Integração & Comunicação.*
- Dado um cenário em que múltiplos clientes estão acessando um backend de serviços, cada um tendo pequenas ou grandes diferenças em seus requisitos de negócio (protocolos diferentes provavelmente) a solução foi :
	- **Definir API Gateways diferentes para cada tipo de cliente**
	- Justo **DO** more!
- Júlio tá fazendo a mesma coisa que ele faz todas as aulas
	- Ele entre na documentação de um repositório de exemplo dele
	- E só lê
	- Passando aqueles '**só se tu quiser né. legal. tá lá, funciona. gostei.**'
- I don't feel at home in this world anymore.
