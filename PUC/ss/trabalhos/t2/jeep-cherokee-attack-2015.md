# Jeep Cherokee (2015): Análise de uma vulnerabilidade de segurança em veículos conectados

**Trabalho 2 – Análise de Falhas Famosas de Segurança**

**Tema:** Exploração remota de vulnerabilidades no sistema Uconnect do Jeep Cherokee (2014–2015).

**Pesquisadores responsáveis:** Charlie Miller e Chris Valasek.

**Período:** Julho e agosto de 2015.

**Duração estimada da apresentação:** 13 minutos.

---

# 1. Contextualização do caso

## Empresa, sistema e veículo afetado

O incidente envolve a Fiat Chrysler Automobiles (FCA), fabricante responsável pelos veículos Jeep, Dodge, Chrysler e Ram, entre outras marcas.

O principal veículo utilizado na demonstração foi um **Jeep Cherokee 2014**, equipado com o sistema multimídia Uconnect.

O Uconnect é um sistema de entretenimento e conectividade automotiva que oferece funcionalidades como:

- Navegação GPS;
- Reprodução de mídia e rádio;
- Conectividade Bluetooth;
- Comunicação celular;
- Ponto de acesso Wi-Fi.

O sistema possuía conectividade com redes externas e integração com componentes eletrônicos do automóvel, tornando-se uma possível superfície de ataque.

## Pesquisadores envolvidos

A pesquisa foi conduzida por **Charlie Miller e Chris Valasek**, pesquisadores especializados em segurança de sistemas automotivos.

Em julho de 2015, os pesquisadores demonstraram que era possível comprometer remotamente determinados sistemas do Jeep Cherokee, interferindo inclusive em componentes responsáveis pelo funcionamento do veículo.

A pesquisa foi apresentada publicamente durante a conferência **Black Hat USA 2015**, em agosto de 2015.

## Contextualização histórica

A pesquisa ganhou notoriedade por demonstrar que vulnerabilidades em sistemas de entretenimento automotivo poderiam ultrapassar os limites desses sistemas e alcançar componentes físicos essenciais à condução.

Anteriormente, pesquisas de segurança automotiva já haviam demonstrado a possibilidade de injetar mensagens na rede CAN de veículos, mas frequentemente exigiam acesso físico ao automóvel.

O trabalho de Miller e Valasek demonstrou uma possibilidade de exploração remota, sem necessidade de modificar fisicamente o veículo.

---

# 2. Descrição do problema

## O que aconteceu?

Charlie Miller e Chris Valasek demonstraram que poderiam comprometer remotamente o sistema Uconnect de um Jeep Cherokee e, posteriormente, interferir em diversos componentes eletrônicos do veículo.

Durante a demonstração, realizada com a participação do jornalista Andy Greenberg, os pesquisadores conseguiram controlar funcionalidades como:

- Sistema de ar-condicionado;
- Rádio e volume;
- Limpadores de para-brisa;
- Transmissão;
- Aceleração;
- Frenagem;
- Direção.

A demonstração evidenciou que um sistema multimídia conectado à internet poderia servir como ponto de entrada para alcançar componentes críticos do automóvel.

## Impacto imediato

O incidente demonstrou uma vulnerabilidade com consequências potencialmente graves para a segurança física de motoristas, passageiros e demais usuários das vias públicas.

A possibilidade de interferir remotamente em componentes de condução transformou o problema em uma questão de segurança física, e não apenas de privacidade ou segurança da informação.

É importante destacar que a demonstração foi conduzida pelos pesquisadores em condições controladas. Não há confirmação oficial de ataques criminosos que tenham reproduzido a demonstração e causado acidentes.

---

# 3. Consequências

## Recall de veículos

Após a divulgação da pesquisa, a Fiat Chrysler anunciou um recall voluntário envolvendo aproximadamente 1,4 milhão de veículos equipados com determinadas versões do sistema Uconnect.

Segundo a documentação da NHTSA, a investigação RQ 15-004 registrou uma população de 1.424.519 veículos.

O recall inicial, identificado como 15V-461, contemplou veículos dos anos-modelo 2013 a 2015 equipados com determinados sistemas Uconnect RA3 e RA4.

Entre os modelos envolvidos estavam:

- Jeep Cherokee;
- Jeep Grand Cherokee;
- Dodge Durango;
- Ram 1500, 2500 e outros modelos;
- Dodge Viper;
- Chrysler 200 e 300;
- Dodge Charger e Challenger.

Posteriormente, um segundo recall, identificado como 15V-508, acrescentou 7.810 unidades do Jeep Renegade.

## Principais consequências

1. **Segurança física:** demonstração de que sistemas eletrônicos de condução poderiam ser manipulados remotamente.
2. **Recall:** necessidade de corrigir os sistemas multimídia dos veículos afetados.
3. **Custos operacionais:** distribuição de atualizações e atendimento aos proprietários.
4. **Reputação:** exposição pública de falhas de segurança em veículos conectados.
5. **Indústria automotiva:** maior atenção à segurança cibernética durante o desenvolvimento de veículos conectados.

## Dados oficiais

A investigação da NHTSA registrou zero acidentes, ferimentos ou fatalidades associados aos registros analisados. Também não encontrou incidentes confirmados de invasão remota nos relatos examinados.

É importante diferenciar a quantidade de veículos contemplados pelo recall da quantidade de veículos efetivamente comprometidos: o recall foi uma medida preventiva, não uma confirmação de que todos os veículos haviam sido invadidos.

Fonte: NHTSA, investigação RQ 15-004.

---

# 4. Como a falha ocorreu

Esta seção representa o núcleo técnico da apresentação.

A pesquisa demonstrou que o comprometimento do veículo não dependia de uma única vulnerabilidade isolada, mas da combinação de falhas em diferentes componentes e mecanismos de comunicação.

## 4.1. Acesso inicial ao sistema Uconnect

Os pesquisadores começaram investigando a possibilidade de comprometer o sistema multimídia por meio de sua conexão Wi-Fi.

Durante essa investigação, identificaram problemas na geração automática de senhas da rede sem fio, que utilizava informações previsíveis relacionadas à inicialização do sistema.

Entretanto, o acesso por Wi-Fi exigia proximidade física com o veículo.

Os pesquisadores também investigaram a conectividade celular integrada ao sistema Uconnect, que permitia comunicação com a infraestrutura da operadora Sprint.

Essa segunda possibilidade foi fundamental para demonstrar a exploração remota do veículo.

A pesquisa utilizou uma femtocell, uma pequena estação-base celular, para investigar a comunicação com a rede da operadora e identificar sistemas vulneráveis.

## 4.2. Comprometimento do computador multimídia

Após estabelecer comunicação com a unidade Uconnect, os pesquisadores identificaram vulnerabilidades no software responsável pelo funcionamento do sistema multimídia.

O equipamento utilizava Linux como sistema operacional.

A exploração dessas vulnerabilidades permitiu obter controle sobre o computador multimídia, possibilitando manipular suas funcionalidades.

Nesse estágio, os pesquisadores já conseguiam interferir em funcionalidades como reprodução de música, rádio e navegação.

Entretanto, ainda não possuíam acesso direto à rede CAN do veículo.

## 4.3. Acesso ao controlador V850

O sistema multimídia não possuía uma conexão direta com a rede CAN.

Existia um controlador intermediário, identificado como V850, que participava da comunicação entre os componentes eletrônicos.

Esse controlador possuía restrições de comunicação: sua implementação permitia determinadas operações de leitura, mas não deveria permitir que o sistema multimídia enviasse comandos arbitrários à rede CAN.

Os pesquisadores descobriram uma maneira de alcançar o controlador por meio da comunicação com a unidade multimídia.

## 4.4. Modificação do firmware

Um dos pontos mais importantes da pesquisa foi a descoberta de que o mecanismo de atualização do firmware do controlador V850 não realizava as verificações de autorização e integridade necessárias.

Isso permitiu que os pesquisadores substituíssem o firmware original por uma versão modificada.

Com o controlador comprometido, conseguiram contornar as restrições existentes e enviar mensagens à rede CAN.

## 4.5. Acesso à rede CAN e controle do veículo

A rede CAN (Controller Area Network) é um protocolo de comunicação utilizado para permitir que diferentes módulos eletrônicos de um automóvel troquem informações.

Esses módulos podem ser responsáveis por funções como:

- Controle do motor;
- Transmissão;
- Sistema de frenagem;
- Direção;
- Sensores;
- Outros componentes eletrônicos.

Após comprometer o controlador intermediário, os pesquisadores conseguiram enviar mensagens à rede CAN e interferir em componentes físicos do veículo.

### Fluxo simplificado da exploração

1. Acesso remoto pela rede celular.
2. Comprometimento do sistema multimídia Uconnect.
3. Comunicação com o controlador V850.
4. Modificação do firmware do controlador.
5. Envio de mensagens à rede CAN.
6. Interferência nos componentes eletrônicos do veículo.

### Conceitos técnicos envolvidos

**Uconnect Head Unit:** computador responsável pelo sistema multimídia e conectividade do veículo.

**Linux embarcado:** sistema operacional utilizado pela unidade multimídia.

**Firmware:** software de baixo nível responsável pelo funcionamento de componentes eletrônicos.

**V850:** controlador intermediário envolvido na comunicação entre o sistema multimídia e a rede CAN.

**CAN Bus:** rede interna utilizada para comunicação entre os módulos eletrônicos do automóvel.

**Femtocell:** pequena estação-base celular utilizada pelos pesquisadores durante a investigação da conectividade do veículo.

---

# 5. Análise técnica da vulnerabilidade

## 5.1. Classificação das falhas

O incidente envolveu diferentes problemas de segurança que, combinados, permitiram o comprometimento remoto do veículo.

| Problema identificado | Classificação conceitual |
|---|---|
| Acesso remoto ao sistema multimídia | Exposição de superfície de ataque |
| Geração previsível de senhas Wi-Fi | Falha na geração de credenciais |
| Vulnerabilidades no software multimídia | Comprometimento de software |
| Atualização insegura do firmware | Falha de autenticação e integridade |
| Separação insuficiente entre sistemas | Falha de segmentação de rede |

Essas classificações descrevem os problemas identificados na pesquisa. Não representam necessariamente identificadores CVE ou CWE oficialmente atribuídos ao incidente.

## 5.2. Tecnologias envolvidas

- Linux embarcado;
- Sistema multimídia Uconnect;
- Redes celulares;
- Comunicação Wi-Fi;
- Microcontrolador V850;
- Firmware;
- CAN Bus;
- Sistemas eletrônicos automotivos.

## 5.3. Problemas arquiteturais

Um dos aspectos mais relevantes do incidente foi a insuficiência das medidas de isolamento entre o sistema multimídia e os componentes responsáveis pelo funcionamento físico do veículo.

Embora existissem restrições de comunicação entre os dois ambientes, o comprometimento do controlador intermediário permitiu contornar essas limitações.

O caso demonstra que a segurança de um sistema não depende apenas da proteção individual de seus componentes, mas também da segurança das interfaces e dos mecanismos de comunicação entre eles.

---

# 6. Medidas corretivas e preventivas

## 6.1. Medidas adotadas pela Fiat Chrysler

Após a divulgação da vulnerabilidade, a fabricante e a operadora Sprint adotaram medidas para impedir a exploração.

Entre elas:

- Bloqueio remoto da porta de comunicação utilizada na exploração pela rede celular;
- Bloqueio das vulnerabilidades relacionadas à comunicação sem fio de curto alcance;
- Distribuição de atualizações de software para os sistemas Uconnect;
- Disponibilização de atualizações por USB e atendimento em concessionárias.

As medidas foram registradas na investigação RQ 15-004 da NHTSA.

## 6.2. Medidas preventivas

Além das correções adotadas, algumas práticas poderiam ter evitado ou dificultado a exploração.

| Medida | Problema que procura resolver |
|---|---|
| Autenticação forte | Impedir acessos remotos não autorizados |
| Geração segura de senhas | Evitar credenciais previsíveis |
| Secure Boot | Impedir inicialização de firmware não confiável |
| Assinatura digital de firmware | Garantir autenticidade e integridade das atualizações |
| Segmentação de redes | Restringir a comunicação entre sistemas multimídia e componentes críticos |
| Princípio do menor privilégio | Limitar as permissões de cada componente |
| Auditorias de segurança | Identificar vulnerabilidades antes da comercialização |

Duas medidas merecem destaque especial:

**Assinatura digital de firmware:** garante que somente atualizações produzidas e autorizadas pelo fabricante sejam aceitas pelo controlador.

**Segmentação de redes:** impede que o comprometimento de um componente conectado à internet resulte automaticamente no acesso a sistemas responsáveis por funções críticas do veículo.

---

# 7. Conclusão

O caso do Jeep Cherokee demonstra como a crescente conectividade de dispositivos físicos amplia a superfície de ataque de sistemas computacionais.

Uma vulnerabilidade inicialmente localizada em um sistema multimídia permitiu que pesquisadores alcançassem componentes responsáveis por funções críticas do automóvel.

A pesquisa de Charlie Miller e Chris Valasek evidencia três aprendizados fundamentais:

1. **Conectividade também significa exposição:** sistemas conectados à internet precisam ser projetados considerando os riscos de acesso remoto não autorizado.
2. **Segurança precisa ser arquitetural:** não basta proteger componentes individualmente quando suas interfaces e mecanismos de comunicação podem ser explorados.
3. **Falhas digitais podem produzir consequências físicas:** em sistemas ciberfísicos, vulnerabilidades de software podem comprometer a segurança de pessoas.

O incidente também demonstra a importância da pesquisa independente em segurança da informação, da divulgação responsável de vulnerabilidades e da colaboração entre pesquisadores e fabricantes.

**Frase sugerida para encerramento:**

> Um automóvel moderno não é apenas uma máquina mecânica com computadores auxiliares. É também um sistema computacional distribuído, e precisa ser projetado com os mesmos cuidados de segurança de qualquer infraestrutura conectada.

---

# 8. Organização da apresentação

Embora não seja um tópico independente do enunciado, a seguinte organização permite distribuir o conteúdo dentro dos 10–15 minutos exigidos.

| Slide | Conteúdo | Tempo estimado |
|---|---|---:|
| 1 | Título e apresentação do caso | 30 segundos |
| 2 | Contextualização e sistema Uconnect | 1 minuto |
| 3 | Descrição do ataque e demonstração | 1 minuto |
| 4 | Consequências e recall | 1 minuto |
| 5 | Arquitetura eletrônica do veículo | 1 minuto |
| 6 | Acesso remoto e comprometimento do Uconnect | 1,5 minuto |
| 7 | V850, firmware e CAN Bus | 2 minutos |
| 8 | Classificação das vulnerabilidades | 1 minuto |
| 9 | Análise técnica e problemas arquiteturais | 1 minuto |
| 10 | Correções e medidas preventivas | 1,5 minuto |
| 11 | Conclusão | 30 segundos |
| | **Total** | **13 minutos** |

## Sugestões de materiais visuais

Para auxiliar a compreensão, recomenda-se utilizar:

1. Fotografias do Jeep Cherokee e do sistema multimídia Uconnect.
2. Trechos da demonstração original de Miller e Valasek.
3. Diagrama simplificado da arquitetura eletrônica do veículo.
4. Fluxograma da cadeia de exploração.
5. Representação da rede CAN e dos módulos eletrônicos conectados.
6. Comparação entre a arquitetura vulnerável e uma arquitetura com segmentação e validação de firmware.

## Distribuição entre integrantes

**Grupo com 3 integrantes:**
- Integrante 1: contextualização, descrição do problema e consequências.
- Integrante 2: cadeia de exploração e análise técnica.
- Integrante 3: classificação das falhas, medidas preventivas e conclusão.

**Grupo com 4 integrantes:**
- Integrante 1: contextualização.
- Integrante 2: descrição do problema e consequências.
- Integrante 3: exploração técnica.
- Integrante 4: análise técnica, medidas preventivas e conclusão.

**Grupo com 5 integrantes:**
- Integrante 1: contextualização.
- Integrante 2: descrição do problema e consequências.
- Integrante 3: acesso remoto e comprometimento do Uconnect.
- Integrante 4: controlador V850, firmware e CAN Bus.
- Integrante 5: classificação, medidas preventivas e conclusão.

Todos os integrantes devem compreender a cadeia completa da exploração para responder a possíveis perguntas.

---

# 9. Referências bibliográficas

As fontes abaixo possuem diferentes funções na pesquisa: algumas documentam diretamente a demonstração, outras contextualizam o incidente e outras oferecem explicações técnicas ou registros oficiais.

## 9.1. Fontes fornecidas inicialmente

### 1. Charlie Miller e Chris Valasek — Black Hat USA 2015

**Título:** Apresentação de Charlie Miller e Chris Valasek sobre a exploração remota do Jeep Cherokee.

**Tipo:** Apresentação técnica em vídeo.

**Link:** https://www.youtube.com/watch?v=MAcHkASmXEc

**Descrição:** Registro da apresentação dos próprios pesquisadores durante a conferência Black Hat USA 2015. É uma fonte primária para compreender como a pesquisa foi apresentada publicamente, quais vulnerabilidades foram discutidas e quais demonstrações foram realizadas.

**Utilização no trabalho:**
- Descrição do incidente;
- Demonstração das consequências práticas;
- Explicação da cadeia de exploração;
- Ilustrações e trechos audiovisuais.

### 2. Penn State — Hackers who remotely hijacked a Jeep to speak about cybersecurity threats

**Tipo:** Artigo institucional.

**Link:** https://www.psu.edu/news/campus-life/story/hackers-who-remotely-hijacked-jeep-speak-about-cybersecurity-threats

**Descrição:** Publicação da Universidade Estadual da Pensilvânia que contextualiza a pesquisa de Charlie Miller e Chris Valasek, apresenta informações sobre suas trajetórias profissionais e descreve a repercussão da demonstração.

O artigo destaca o recall de aproximadamente 1,4 milhão de veículos realizado pela Fiat Chrysler.

**Utilização no trabalho:**
- Contextualização dos pesquisadores;
- Descrição geral do incidente;
- Consequências e repercussão;
- Recall de veículos.

### 3. Kaspersky — Black Hat USA 2015: The full story of how that Jeep was hacked

**Autor:** Alex Drozhzhin.

**Data:** 6 de agosto de 2015.

**Tipo:** Artigo técnico e explicativo.

**Link:** https://www.kaspersky.com/blog/blackhat-jeep-cherokee-hack-explained/9493/

**Descrição:** Artigo publicado pela Kaspersky após a apresentação dos pesquisadores na Black Hat. Explica a investigação sobre a conectividade Wi-Fi e celular do veículo, o comprometimento do sistema multimídia, o acesso ao controlador V850 e a possibilidade de enviar mensagens à rede CAN.

É particularmente útil por transformar os detalhes da pesquisa em uma explicação mais acessível.

**Utilização no trabalho:**
- Explicação da cadeia de exploração;
- Funcionamento do Uconnect;
- Comunicação celular;
- Controlador V850;
- Firmware e CAN Bus.

## 9.2. Fontes complementares

### 4. Miller e Valasek — Remote Exploitation of an Unaltered Passenger Vehicle

**Data:** Agosto de 2015.

**Tipo:** Whitepaper técnico dos pesquisadores.

**Link:** https://www.ioactive.com/remote-exploitation-of-an-unaltered-passenger-vehicle/

**Descrição:** Documento técnico original da pesquisa, publicado pela IOActive. Apresenta a investigação realizada no Jeep Cherokee 2014, incluindo sua arquitetura de rede, os componentes eletrônicos envolvidos e os métodos utilizados para demonstrar a exploração remota.

É a principal referência técnica para aprofundar o funcionamento da vulnerabilidade.

**Utilização no trabalho:**
- Análise técnica;
- Arquitetura do veículo;
- Funcionamento dos componentes eletrônicos;
- Cadeia de exploração;
- Tecnologias envolvidas.

### 5. NHTSA — Investigation RQ 15-004

**Instituição:** National Highway Traffic Safety Administration.

**Tipo:** Documento governamental de investigação.

**Link:** https://static.nhtsa.gov/odi/inv/2015/INCLA-RQ15004-9129.PDF

**Descrição:** Documento oficial da investigação conduzida pela agência norte-americana responsável pela segurança no trânsito. Registra os veículos envolvidos, a população contemplada pelo recall, os riscos identificados e as medidas corretivas adotadas pela fabricante e pela operadora.

**Utilização no trabalho:**
- Consequências do incidente;
- Quantidade de veículos afetados;
- Recall;
- Medidas corretivas;
- Verificação dos registros de acidentes e incidentes.

### 6. IOActive — Harman-Kardon UConnect Vulnerability

**Data:** 28 de setembro de 2015.

**Tipo:** Comunicado técnico de segurança.

**Link:** https://ioactive.com/wp-content/uploads/2018/05/IOActive_Advisory_Harman-Kardon.pdf

**Descrição:** Comunicado de segurança que documenta os produtos Uconnect afetados, o impacto da vulnerabilidade e algumas informações técnicas relacionadas à exploração remota sem autenticação.

**Utilização no trabalho:**
- Classificação da vulnerabilidade;
- Sistemas afetados;
- Tecnologias envolvidas;
- Medidas de mitigação.

---

# 10. Observações e cuidados para a apresentação

- Não confundir o acesso inicial investigado por Wi-Fi com a demonstração de exploração remota pela rede celular.
- Não afirmar que todos os veículos contemplados pelo recall foram efetivamente invadidos.
- Não afirmar que a pesquisa causou acidentes ou vítimas.
- Não apresentar classificações CWE ou CVE como identificadores oficiais sem documentação que comprove essa atribuição.
- Diferenciar as vulnerabilidades originais das medidas corretivas adotadas posteriormente.
- Priorizar a explicação técnica da cadeia de exploração em vez de dedicar tempo excessivo à biografia dos pesquisadores.
- Utilizar os diagramas para demonstrar como o comprometimento de um sistema multimídia pôde alcançar componentes físicos do automóvel.

**Objetivo final:** demonstrar como falhas de segurança em sistemas embarcados e mecanismos de comunicação podem comprometer a integridade de um sistema ciberfísico, relacionando as causas técnicas do incidente às suas consequências e às medidas necessárias para evitar ocorrências semelhantes.