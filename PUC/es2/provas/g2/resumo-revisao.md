# Engenharia de Software II — Resumo das Revisões (P1 e P2)

> Consolidação dos conteúdos abordados nos materiais `revisao_p1_respostas.pdf` e `revisao_p2_respostas.pdf` (Prof. Júlio Machado).

---

## Parte 1 — Arquitetura de Software (Revisão P1)

### Estilos e padrões arquiteturais

- **Orientação a objetos:** a comunicação entre componentes ocorre por **troca de mensagens**.
- **MVC (Modelo-Visão-Controle):** o **Modelo** representa os dados associados às interações feitas no **Controle**, que são posteriormente apresentados/manipulados na **Visão**.
- **Monolitos** ≠ microsserviços: a arquitetura monolítica **não** é dividida em pequenas partes com manutenção/evolução individual — essa característica é dos microsserviços.
- **Microsserviços** possuem componentes **fracamente acoplados** (baixo acoplamento), o que **facilita** a manutenção.

### Cenários de arquitetura

- Aplicações em **nuvem** que otimizam máquinas locais de poucos recursos, permitindo inserir novos *hosts* sem comprometer o sistema → arquitetura **cliente-servidor**.

### Microsserviços — características principais

- Padrão para criação de **aplicações distribuídas** com **alta escalabilidade**.
- Comunicação por **mecanismos-padrão** de tecnologia, como **REST** (*Representational State Transfer*).
- Cada serviço é **autônomo** e de **baixo acoplamento** — podem ser escritos em **linguagens diferentes** (aplicação poliglota).
- Princípio: **um banco de dados por microsserviço**.

### Monolitos × Microsserviços

**Monolitos — Benefícios**
- Testes completos facilitados (ex.: Selenium).
- Implantação simples: basta copiar para um servidor.
- Módulos compartilham memória, espaço e recursos → solução única para questões transversais (logging, cache, segurança).
- Vantagem de desempenho: módulos chamam uns aos outros diretamente (sem chamadas de rede).

**Monolitos — Desafios**
- Módulos fortemente acoplados dificultam mudanças conforme o app cresce.
- CI/CD complicado: qualquer alteração exige reimplantar o app inteiro.
- Escalonamento difícil quando módulos têm requisitos de recursos conflitantes.
- Um bug em um módulo (ex.: vazamento de memória) pode derrubar todo o sistema.
- Adotar novos frameworks/linguagens é caro (reescrever o app inteiro).

**Microsserviços — Benefícios**
- Serviços com **limites bem definidos** (API RPC ou orientada a mensagens): mais rápidos de desenvolver, entender e manter.
- **Equipes autônomas** organizadas por limites de negócio, responsáveis por todo o ciclo de vida do serviço.
- Aplicação **poliglota**: linguagem mais eficaz para cada serviço.
- **Ciclos de lançamento independentes** → maior velocidade e *time-to-market*.
- **Escalonamento independente** por serviço → maior disponibilidade e confiabilidade.

**Microsserviços — Desafios**
- Complexidade de **sistema distribuído**: mecanismo de comunicação, falhas parciais, indisponibilidade de dependências.
- **Transações distribuídas**: garantir atomicidade entre vários bancos é difícil; falhas na reversão geram **dados inconsistentes**.
- **Testes** mais complexos (vários serviços interagindo).
- **Implantação** mais complexa: muitas instâncias + mecanismo de **descoberta de serviços** (*service discovery*).
- **Sobrecarga operacional**: mais serviços para monitorar/alertar, mais pontos de falha; exige boa infra de operações e monitoramento.
- **Latência** introduzida por chamadas de rede entre serviços.
- Nem toda aplicação é grande o bastante para ser dividida; apps com forte integração/tempo real podem sofrer com a comunicação extra.

### Distribuição de bases de dados

Ao dividir um banco monolítico por microsserviço, além da separação nem sempre clara entre objetos, surgem outros problemas:
- **Sincronização de dados**
- **Integridade transacional**
- **Mesclagens (merges)**
- **Latência**

---

## Parte 2 — CD, Comunicação e Docker (Revisão P2)

*(Base: cap. 10 de VALENTE, Marco Tulio. **Engenharia de Software Moderna**, 2020.)*

### Continuous Deployment & Feature Flags

- **Feature Flags** (cap. 10.4.2): mecanismo associado ao **CD (continuous deployment)** que permite **ativar/desativar funcionalidades** sem reimplantar o código, desacoplando a **implantação** da **liberação** de uma feature.
- Prática de configuração de **CI/CD** com **GitHub Actions** (repositório de demonstração `aserg-ufmg/demo-ci`).

### Troca de mensagens em microsserviços

- **Message brokers**: em arquiteturas *cloud*, formam um **backbone de comunicação compartilhado** entre microsserviços.
- Suportam comunicação **assíncrona** (o remetente não precisa esperar a resposta) — a afirmação de que "não permitem assíncrona" é **falsa**.
- Oferecem **mais de um** padrão de distribuição de mensagens (não apenas ponto a ponto um-para-um).
- **APIs REST** **não** usam CORBA — essa associação é incorreta.
- ✅ Correta apenas a afirmação sobre *message brokers* como *backbone* compartilhado.

### Comunicação síncrona × assíncrona

- **HTTP** é um protocolo **síncrono**: o cliente envia uma solicitação e **espera a resposta**.
- Isso é **independente** da execução do código do cliente, que pode ser:
  - **Síncrona** → thread **bloqueado**;
  - **Assíncrona** → thread **não bloqueado**; a resposta alcança um *callback* (retorno de chamada).
- **AMQP** — protocolo compatível com vários SOs e ambientes de nuvem — usa **mensagens assíncronas**; o remetente geralmente **não espera** resposta.

### Docker

- **Container Docker** = **instância executável de uma imagem**.
- **Docker** é uma **plataforma de software livre** que empacota aplicativos em **contêineres** — componentes executáveis e padronizados que combinam o **código-fonte** com as **bibliotecas e dependências do S.O.** necessárias, permitindo executar o código em **qualquer ambiente**.

---

## Gabaritos de referência

| Revisão | Questão | Resposta |
|---------|---------|----------|
| P1 | 1 | A (I e III) |
| P1 | 2 | D (cliente-servidor) |
| P1 | 3 | B (comunicação via REST) |
| P2 | 2 | E (apenas I) |
| P2 | 4 | D (instância executável de uma imagem) |
| P2 | 5 | A (plataforma livre de contêineres) |

---

## Mapa de tópicos por prova

| Tema | P1 | P2 |
|------|:--:|:--:|
| Estilos/padrões arquiteturais (OO, MVC) | ✅ | |
| Monolitos × Microsserviços | ✅ | |
| Escalabilidade e bancos de dados distribuídos | ✅ | |
| CI/CD e Feature Flags | | ✅ |
| Message brokers e REST | | ✅ |
| Comunicação síncrona/assíncrona (HTTP/AMQP) | | ✅ |
| Docker e contêineres | | ✅ |
