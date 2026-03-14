# Engenharia de Software II - Aula02
## [13-03-2026][mvfm]

### Contador de né's : 30

### Arquitetura Orientada à Serviços
- Java, DotNet & Javascript seguindo a mesma solução
- Semana que vem, vamos fazer atividades práticas de monolitos -> Micro-serviços
- Júlio não parece seguir exatamente a orientação de seus próprios slides, ele já pulou alguns slides no terceiro arquivo

### Web Services
- "[...] Um componente de software independente e fracamente acoplado que engloba funcionalidades discretas que pode ser distribuída e acessada por meio de protocolos padrão. "
- Carcaterísticas 
	1. Objetos remotos
	2. Residem em um servidor WEB, possuíndo uma URL
	3. Protocolos que facilitam comunicação (**vamos ver bem mais http eu acredito**)

### Web & HTTP
![exemplo weather](assets/web_http.png)
- HTTP
	1. Protocolo de nível de aplicação
	2. Protocolo textual
	3. Baseado em mensagens de requisição.
- Júlio está mostrando atualmente o exemplo Spring Pet Clinic, dentro de um devspace do github.
- Bem como o Mangan nos meses iniciais do estágio.
- Rodando Java 25, lol lamo good luck pom.xml
- Estrutura HTTP 
	- Requisição
		1. Linha inicial
		2. Um ou mais campos de cabeçalho
		3. Uma linha em [?branco]
		4. Corpo de mensagem (**opcional**)
	- Resposta 
		1. [Linha de status com seu código](https://http.cat/)
		2. Uma ou mais linhas de cabeçalho (i know right)
		3. Uma linha em [?branco] (i know right)
		4. Corpo de mensagem (**I KNOW RIGHT**)

### REST
- Júlio continua com a memsa diretriz de deixar *bem claro* que escolha de arquitetura vai depender *MUITO* do que queremos.
- " Por que ele quis. "
- ' REST é um estilo arquitetural de aplicações WEB baseado em quatro princípios: '
	1. Identificação de recursos através de [URI's](https://learn.microsoft.com/pt-br/azure/architecture/best-practices/api-design)
	2. Interface uniforme de acesso para recursos baseada em HTTP.
	3. [?Mensagens Autodescritivas]
	4. Interação através de hyperlinks
- Okay. Whatever. 
- Exemplos disponibilizados :
	- [JSON-Placeholder](https://jsonplaceholder.typicode.com/)
	- [Random-User](https://randomuser.me/)
	- [Reqres](https://reqres.in/)
	- [Petstore](http://petstore.swagger.io/)
- As tarefas realmente relegadas para o desenvolvedor é : **Definir o que é exposto, formato de URI's, quais métodos do HTTP são utilizados, 'semântica de aplicação'.**
- Exemplo que ele está mostrando de uma aplicação Spring é monolítica, bem com o que estou fazendo da DB. Is it fucking over?

### Restante da aula
- Não vamos seguir os slides mesmo, hoje a aula foi na **309**, mas não para implementação de algo (o que é bem estranho)
- Estamos basicamente ocupando espaço.
- Sor fala de MVC, explicando que estamos casando tecnologia com framework o que não deixa clean.
- Olhando o cronograma, vamos estar na mesma sala o restante do semestre, basicamente. No NP.
- Modelo 'pipe and filter', de novo, o que já fazemos no estágio
- **blablabla.stream()**
		**.requestMatchers()**
		**.hasRole()**
- Sor continua a apresentar novos sistemas, tanto em java, .NET & JS mas acredito que todos sejam monolíticos.
- Imagina se fosse 4 créditos.
- Não parece que vou aprender muito nesta cadeira.
