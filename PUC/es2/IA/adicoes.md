# Engenharia de Software II — Adições & Aprofundamentos
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas. Segue os tópicos na ordem em que apareceram, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---

### HTTP — Os métodos que a aula passou por cima

As notas descrevem a estrutura de requisição e resposta HTTP mas não nomeiam os **verbos**. São eles que dão semântica à operação:

| Método | Semântica | Idempotente? |
|---|---|---|
| `GET` | Lê um recurso. Sem efeito colateral. | Sim |
| `POST` | Cria um recurso novo. | Não |
| `PUT` | Substitui um recurso inteiro. | Sim |
| `PATCH` | Atualiza parcialmente um recurso. | Não (em geral) |
| `DELETE` | Remove um recurso. | Sim |

**Idempotência** significa que chamar o método N vezes produz o mesmo resultado que chamar uma vez. Isso importa para retries automáticos em caso de falha de rede.

#### Códigos de status — os principais

As notas linkam o `https.cat` mas não listam os mais usados na prática:

- `200 OK` / `201 Created` / `204 No Content` — sucesso
- `400 Bad Request` — requisição malformada (erro do cliente)
- `401 Unauthorized` — não autenticado
- `403 Forbidden` — autenticado mas sem permissão
- `404 Not Found` — recurso não existe
- `409 Conflict` — estado conflitante (ex: criando algo que já existe)
- `422 Unprocessable Entity` — corpo válido mas falha de validação de negócio
- `500 Internal Server Error` — o servidor quebrou
- `503 Service Unavailable` — serviço fora ou sobrecarregado

---

### REST — As seis restrições completas

As notas listam quatro princípios. O Roy Fielding definiu **seis restrições** em sua dissertação:

1. **Cliente-Servidor** — separação de responsabilidades. UI e armazenamento evoluem independentemente.
2. **Stateless** — cada requisição carrega toda informação necessária. O servidor não guarda estado de sessão entre requisições. *(Isso é o porquê de JWTs e tokens no header.)*
3. **Cacheable** — respostas devem indicar se podem ser cacheadas. `Cache-Control` header.
4. **Interface Uniforme** — URIs identificam recursos; representações (JSON/XML) são separadas do recurso em si.
5. **Sistema em Camadas** — o cliente não sabe se fala com o servidor final ou com um proxy/load balancer.
6. **Code on Demand** (opcional) — o servidor pode enviar código executável ao cliente (ex: JavaScript).

A restrição **Stateless** é a que mais impacta na prática: ela força autenticação via token a cada requisição e torna a escalabilidade horizontal trivial — qualquer instância pode atender qualquer requisição.

---

### Monolito vs. Microserviços — O que falta na comparação

As notas capturam bem as vantagens e desvantagens. Dois pontos que ficaram implícitos:

#### Quando monolito é a escolha certa

- Times pequenos (< 10 devs): o overhead de comunicação entre serviços não compensa.
- Domínio ainda não bem definido: microserviços com fronteiras erradas são piores que monolitos.
- Latência crítica: chamadas de rede somam milissegundos; dentro de um processo é nanosegundos.

A regra prática usada pela maioria: **comece monolítico, extraia serviços quando a dor de não ter for maior que o custo de criar.**

#### O problema que as notas nomeiam mas não resolvem: comunicação entre serviços

Existem dois padrões principais:
- **Síncrono (REST/gRPC)**: serviço A chama serviço B e espera resposta. Simples, mas cria acoplamento temporal — se B cair, A falha.
- **Assíncrono (mensageria — Kafka, RabbitMQ)**: A publica um evento, B consome quando puder. Mais resiliente, mais complexo.

---

### Escalabilidade — Horizontal vs. Vertical na prática

A dúvida das notas ("se são componentes de um servidor ou servidores em si") tem resposta clara:

- **Vertical**: é a mesma máquina ficando mais poderosa. Tem limite físico e geralmente exige downtime.
- **Horizontal**: são mais máquinas (ou containers) rodando a mesma aplicação em paralelo. Requer que a aplicação seja **stateless** para funcionar — daí a conexão direta com REST stateless acima.

**Auto-scaling** é o nome do mecanismo que faz escala horizontal automática em resposta à carga, disponível em AWS, GCP e Azure.

---

### API Gateway — O padrão que cola tudo

Em microserviços, o cliente normalmente não fala diretamente com cada serviço. Um **API Gateway** fica na frente:

```
Cliente --> API Gateway --> Serviço de Usuários
                       --> Serviço de Pedidos
                       --> Serviço de Pagamento
```

Ele centraliza: autenticação, rate limiting, logging, roteamento e transformação de respostas. O PetClinic do Júlio provavelmente tem um. Exemplos: Kong, AWS API Gateway, Nginx.

---

### Teorema CAP — A restrição fundamental de sistemas distribuídos

Todo sistema distribuído (microserviços incluídos) precisa escolher dois dos três:

- **C**onsistência: todos os nós veem os mesmos dados ao mesmo tempo.
- **A**vailability: o sistema sempre responde (mesmo que com dados desatualizados).
- **P**artition Tolerance: o sistema funciona mesmo que a rede entre nós falhe.

Como partições de rede são inevitáveis em sistemas reais, a escolha real é sempre entre **CP** (consistente mas pode ficar indisponível) e **AP** (disponível mas pode ter dados desatualizados). Bancos relacionais tradicionais são CP. Sistemas como Cassandra e DynamoDB são AP.

---

### Pipe and Filter — O modelo que o Júlio mostrou

O padrão mencionado nas notas (`stream().requestMatchers().hasRole()`) é **Pipe and Filter** de fato. Cada `.método()` é um filtro que transforma ou filtra o fluxo de dados passando pelo pipe.

É o mesmo modelo do shell Unix: `cat arquivo | grep "erro" | sort | uniq -c`

No Spring Security, cada `requestMatcher` é um filtro numa cadeia. A requisição HTTP passa por cada filtro em ordem. Se algum rejeitar, a cadeia para. Se todos aprovarem, chega ao controller.

---

### Versionamento de API — O que ninguém menciona até quebrar tudo

Quando uma API REST muda de forma que quebra clientes existentes, precisa de versionamento. As estratégias principais:

1. **URI**: `/api/v1/users` vs `/api/v2/users` — mais comum, mais visível.
2. **Header**: `Accept: application/vnd.api+json; version=2` — mais limpo mas menos óbvio.
3. **Query param**: `/users?version=2` — desencorajado.

A regra de ouro: **nunca remova ou renomeie campos de uma versão existente sem criar uma nova versão**. Adicionar campos novos geralmente é seguro (se clientes ignoram campos desconhecidos).

---

## Aula 07 — Backends For Frontends (BFF)

### O Problema que o BFF Resolve

Um API Gateway único para todos os clientes cria um problema: mobile, web e parceiros têm necessidades radicalmente diferentes:

- Mobile tem banda limitada — quer respostas compactas e poucas chamadas
- Web pode fazer múltiplas requisições paralelas — quer granularidade
- Parceiros externos têm contratos de API estáveis, diferentes dos internos

Tentar servir todos com um único gateway leva a: payloads grandes demais para mobile, endpoints acoplados a UI específica, ou contratos quebrados quando a UI evolui.

---

### A Solução: Um Gateway por Tipo de Cliente

O padrão **BFF** define um backend específico para cada tipo de frontend:

```
Mobile App    → BFF Mobile    ┐
Web App       → BFF Web       ├──→ Microserviços internos
Parceiros     → BFF Partners  ┘
```

Cada BFF:
- Agrega chamadas múltiplas a microserviços em uma única resposta otimizada para aquele cliente
- Implementa lógica de apresentação específica para aquele cliente (formatar datas, filtrar campos)
- Evolui independentemente dos outros BFFs — o time mobile muda o BFF mobile sem afetar web

---

### Diferença entre API Gateway e BFF

| | API Gateway | BFF |
|---|---|---|
| Responsabilidade | Infraestrutura transversal (auth, rate limit, routing) | Lógica específica de cliente |
| Escopo | Um para todos | Um por tipo de cliente |
| Quem mantém | Time de plataforma | Time do produto (junto com o frontend) |
| Ritmo de mudança | Raro, estável | Frequente, junto com o frontend |

Na prática podem coexistir: o API Gateway fica na frente (autenticação, TLS, logging), os BFFs ficam atrás servindo cada tipo de cliente.

---

### Quando BFF Faz Sentido

- **Múltiplos clientes com requisitos divergentes**: a alternativa é um gateway com lógica condicional crescente — anti-pattern chamado "fat gateway".
- **Times separados por produto**: autonomia sem acoplamento. O time mobile não espera o time web para evoluir sua API.

Quando **não** faz sentido: poucos clientes com necessidades similares — o overhead de manter múltiplos gateways não compensa.
