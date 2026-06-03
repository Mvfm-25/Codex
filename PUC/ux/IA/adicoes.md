# Experiência do Usuário — Adições & Aprofundamentos
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas. Segue os tópicos na ordem em que apareceram, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---

### Semiótica — Os três tipos de signo que Peirce definiu

As notas definem signo mas não distinguem os tipos. A taxonomia de Charles Sanders Peirce (a base da semiótica moderna) divide signos em:

- **Ícone**: relação de semelhança com o referente. Um ícone de lixeira *parece* uma lixeira.
- **Índice**: relação de causa/efeito ou contiguidade. Fumaça é índice de fogo. Um cursor de carregamento é índice de processamento.
- **Símbolo**: relação arbitrária, definida por convenção. A letra "A" não tem nada a ver com o som /a/ — é puramente convencional.

Em interfaces, ícones são mais universais (menos dependem de cultura), símbolos exigem aprendizado. O problema que as notas capturam ("não se consegue prever o que o usuário consegue interpretar") é exatamente a diferença entre ícone e símbolo: ícones bem escolhidos reduzem a carga de aprendizado.

---

### Meta-Comunicação — A teoria de Clarisse de Souza

O conceito de meta-comunicação nas notas vem da pesquisadora brasileira **Clarisse de Souza** e sua **Teoria da Engenharia Semiótica**. A ideia central:

> Uma interface é uma mensagem do designer para o usuário, explicando *quem o sistema acha que você é*, *o que você pode fazer*, e *como fazê-lo*.

Isso formaliza por que interfaces confusas são confusas: o designer comunicou algo diferente do que o usuário entendeu. A pesquisa de UX existe para fechar esse gap.

A imagem da "comunicabilidade" nas notas representa avaliações onde usuários são gravados enquanto usam um sistema — quando eles dizem frases como "Hmm, isso deveria funcionar..." ou ficam em silêncio confuso, o pesquisador está documentando falhas de meta-comunicação.

---

### DCU (Design Centrado no Usuário) — O que ISO 9241-210 formaliza

O DCU mencionado nas notas tem uma definição formal na norma **ISO 9241-210**. Os quatro princípios:

1. O design é baseado em compreensão explícita de usuários, tarefas e ambientes
2. Usuários estão envolvidos durante o design e o desenvolvimento
3. O design é guiado e refinado por avaliações centradas no usuário
4. O processo é iterativo

O ponto 3 é o mais frequentemente pulado na prática: **avaliação contínua**, não apenas ao final. A distinção entre "teste de usabilidade" (com usuários reais) e "avaliação heurística" (com especialistas) é importante — um complementa o outro.

---

### As 10 Heurísticas de Nielsen — O que toda avaliação de UX usa

Não apareceu nas aulas ainda mas é a ferramenta mais usada em avaliação de interfaces. Jakob Nielsen definiu 10 princípios em 1994 que continuam relevantes:

1. **Visibilidade do status do sistema** — o sistema sempre informa o que está fazendo. (Barras de progresso, indicadores de carregamento)
2. **Correspondência com o mundo real** — use linguagem e conceitos do usuário, não jargão técnico.
3. **Controle e liberdade do usuário** — "saída de emergência" clara para ações acidentais. (Desfazer, cancelar)
4. **Consistência e padrões** — mesma ação, mesmo resultado, sempre.
5. **Prevenção de erros** — melhor que boas mensagens de erro é não deixar o erro acontecer.
6. **Reconhecimento em vez de lembrança** — minimize o que o usuário precisa memorizar.
7. **Flexibilidade e eficiência** — atalhos para usuários experientes sem atrapalhar novatos.
8. **Design estético e minimalista** — cada elemento desnecessário compete com informação relevante.
9. **Ajuda a reconhecer, diagnosticar e se recuperar de erros** — mensagens de erro em linguagem simples + solução.
10. **Ajuda e documentação** — se necessário, fácil de encontrar e orientada a tarefas.

---

### Processos de Design — O que une todos os modelos

As notas listam vários modelos (simples, estrela, Mayhew, contextual, etc.) sem destacar o que é comum a todos: **iteração e feedback do usuário**. Todos os modelos são variações de:

```
Pesquisar → Definir → Idealizar → Prototipar → Testar → (repetir)
```

O nome moderno para isso é **Design Thinking** (Stanford d.school). As diferenças entre os modelos são principalmente de **ênfase** e **formalidade**:

- **Modelo simples**: ênfase em velocidade, menos formalidade
- **Engenharia de Usabilidade (Mayhew)**: ênfase em rigor e documentação
- **Design Contextual**: ênfase em pesquisa etnográfica (observar usuários no ambiente real)
- **Design Baseado em Cenários**: ênfase em narrativas de uso antes de wireframes

Para o trabalho prático da cadeira, o mais útil é entender que **nenhum modelo é seguido rigidamente** na prática — são vocabulários para justificar e comunicar decisões de design.

---

### Card Sorting — Dois tipos e quando usar cada um

As notas descrevem o card sorting da atividade mas não distinguem as variantes:

- **Card sorting aberto**: usuários criam as categorias. Usado quando você não sabe como organizar o conteúdo. Revela o modelo mental do usuário.
- **Card sorting fechado**: categorias são pré-definidas, usuários só alocam os cards. Usado para validar uma estrutura existente.
- **Híbrido**: categorias sugeridas, usuário pode criar novas.

A atividade da aula foi essencialmente um **card sorting aberto** — os grupos definiram as categorias (Pré-compra, Especificação, Compra, etc.). O resultado real de um card sorting é analisado estatisticamente: quais cards são consistentemente agrupados juntos revelam relações mentais entre conceitos.

Ferramentas digitais: **OptimalSort**, **Maze**, **Useberry** — permitem aplicar card sorting remotamente com dezenas de participantes.

---

### Pesquisa de Usuário — Os métodos além das entrevistas

As notas mencionam entrevistas, questionários e polling. O espectro completo:

| Método | Quando usar | O que revela |
|---|---|---|
| Entrevista | Exploração inicial | Motivações, contexto, histórias |
| Questionário | Validação em escala | Frequências, preferências |
| Observação contextual | Quando comportamento ≠ relato | O que usuários *fazem* vs. o que *dizem* |
| Teste de usabilidade | Protótipo existente | Pontos de fricção específicos |
| Análise de dados (analytics) | Produto em produção | O que usuários *realmente* fazem em escala |
| A/B testing | Decisões específicas | Qual variante performa melhor |

O princípio fundamental: **o que usuários dizem** e **o que usuários fazem** frequentemente divergem. Observação e analytics capturam comportamento real; entrevistas capturam percepção e motivação. Ambos são necessários.

---

### Personas e Jornadas — O que provavelmente vem a seguir

**Persona**: representação fictícia mas baseada em dados de um tipo de usuário. Não é um estereótipo — é uma síntese de padrões observados em pesquisa real.

Estrutura mínima de uma persona:
- Nome e foto (para humanizar)
- Perfil demográfico e contexto
- Objetivos e motivações
- Frustrações e dores
- Comportamentos relevantes ao produto

**Jornada do usuário (User Journey Map)**: visualização das etapas que um usuário percorre ao interagir com um produto — desde antes de usar (descoberta) até depois (resultado). Inclui ações, pensamentos, emoções e pontos de contato.

A combinação persona + jornada é o artefato mais comum de síntese de pesquisa. O trabalho T1 de "Pesquisa de Usuário, Espaço de Problema" provavelmente culmina nisso.

---

### Gestalt no Design de Interface

Princípios da Psicologia da Gestalt que explicam como humanos percebem agrupamentos visualmente — úteis para design de layouts:

- **Proximidade**: elementos próximos são percebidos como grupo. Explica por que margin e padding importam.
- **Similaridade**: elementos similares (cor, forma, tamanho) são percebidos como relacionados.
- **Fechamento**: o cérebro completa formas incompletas. Base de ícones minimalistas.
- **Continuidade**: o olho segue linhas e curvas além de onde terminam.
- **Figura-fundo**: o que é percebido como objeto vs. fundo pode ser ambíguo (usado intencionalmente em logos).

Esses princípios são a razão pela qual um design visualmente "limpo" funciona melhor cognitivamente — ele explora a tendência natural do cérebro de organizar e agrupar.

---

## Aula 12 — Personas: Da Pesquisa ao Arquétipo

### As Dimensões de Segmentação

Personas são construídas a partir de dados reais, não de suposições. As dimensões úteis para segmentação:

- **Experiência** com tecnologia ou domínio: iniciante, intermediário, avançado
- **Atitudes** em relação ao produto: entusiasta, cético, pragmático
- **Tarefas principais**: o que essa pessoa *realmente faz* com o sistema

**Por que idade não é recomendada como dimensão primária**: dois usuários de 25 e 55 anos podem ter comportamentos idênticos com o produto; dois usuários de 30 anos podem ter comportamentos opostos. Idade correlaciona fracamente com comportamento de uso em contextos de produto — é um atalho que frequentemente leva a estereótipos, não a personas úteis.

---

### O Corte 70/30 e Subgrupos

Quando os dados apresentam um corte 70/30 em alguma dimensão (ex: 70% usam o produto em desktop, 30% em mobile), isso indica dois contextos de uso distintos — possivelmente duas personas.

O ponto mais importante: o subgrupo de 70% frequentemente contém sub-segmentos adicionais. Personas não são simplesmente "maioria vs. minoria" — são padrões de comportamento distintos que justificam **decisões de design diferentes**.

Regra prática: se duas pessoas dentro de um subgrupo tomariam decisões de design opostas para a mesma feature, elas representam personas diferentes, independente do tamanho relativo dos grupos.

---

### Objetivos como Definição Central

A característica mais importante de uma persona bem construída são seus **objetivos** — não suas tarefas:

- **Tarefa**: "Fazer upload de uma foto de perfil"
- **Objetivo**: "Parecer profissional para recrutadores"

O objetivo explica *por que* a tarefa importa. Design centrado em tarefas otimiza o fluxo; design centrado em objetivos garante que o fluxo resolve o problema real.

O refinamento sucessivo de dados brutos: entrevista revela comportamentos → agrupamento identifica padrões → análise de padrões identifica motivações → motivações formam os objetivos da persona. É iterativo, não linear.

---

### Modelagem de Comportamento

A utilidade prática das personas é conseguir *prever* como uma persona reagiria a uma decisão de design antes de testar com usuários reais.

"A persona Carla usaria esse atalho de teclado?" — se os dados mostram que Carla é iniciante, provavelmente não. Essa pergunta direciona decisões de design sem precisar de novo teste.

Isso não substitui testes com usuários reais, mas reduz o custo de decisões óbvias e foca os testes nas questões genuinamente incertas — que são as mais valiosas de responder.

---

## Aula 04 — Engenharia Cognitiva e os Gulfs de Norman

### Os Dois Gulfs de Don Norman

As notas mencionam "engenharia cognitiva" como tema de continuação. O conceito central que fundamenta UX é o modelo de Donald Norman dos **dois gulfs** (*gulfs of execution and evaluation*):

- **Gulf of Execution**: distância entre o que o usuário *quer fazer* e as ações disponíveis no sistema. Interface confusa = gulf largo.
- **Gulf of Evaluation**: distância entre o estado real do sistema após uma ação e a *percepção* que o usuário tem desse estado. Feedback ausente = gulf largo.

Design de UX é, fundamentalmente, **encolher ambos os gulfs**. As notas descrevem exatamente esses problemas ("não se consegue prever o que o usuário consegue interpretar") — é o Gulf of Evaluation em palavras informais.

### Os 7 Estágios da Ação

Norman desdobra a interação em 7 estágios: formar o objetivo → planejar → especificar a ação → executar → perceber o estado → interpretar → avaliar se atingiu o objetivo. Estágios 1-4 pertencem ao Gulf of Execution; 5-7 ao Gulf of Evaluation. Interface "intuitiva" minimiza o esforço cognitivo em todos os 7.

---

## Aula 05 — Ciclos de Design e o Custo da Descoberta Tardia

### Por Que Todos os Modelos São Iterativos

Os modelos da aula (simples, estrela, Mayhew, contextual) compartilham iteração como princípio. A razão é econômica:

O custo de corrigir um problema cresce com o avanço do desenvolvimento:
- Descoberto em pesquisa: custo $1\times$
- Descoberto em prototipagem: custo $10\times$
- Descoberto em desenvolvimento: custo $100\times$
- Descoberto em produção: custo $1000\times$

Isso justifica todos os ciclos curtos e dinâmicas de aula: **descobrir cedo é barato**.

### Design Thinking (Stanford d.school)

O modelo mais influente atualmente:
1. **Empatizar** — pesquisa com usuários reais
2. **Definir** — enunciar o problema a partir dos dados
3. **Idealizar** — geração de ideias sem julgamento
4. **Prototipar** — construir para aprender
5. **Testar** — com usuários, voltar ao início

A diferença do modelo em cascata: não há fase "definir requisitos" que encerra antes de prototipar. Requisitos emergem através do processo.

---

## Aula 07 — Card Sorting: Análise e Dendrogramas

### O Que Se Faz com os Dados

Com múltiplos participantes, os resultados do card sorting são analisados estatisticamente:

- **Matriz de similaridade**: quantas vezes cada par de cards foi agrupado junto. Cards agrupados em 90%+ dos participantes têm relação forte no modelo mental.
- **Dendrograma**: árvore que mostra quais cards se agrupam mais fortemente. Cortar o dendrograma em diferentes alturas produz diferentes granularidades de organização.

A estrutura de informação final (menus, navegação) é derivada do dendrograma — não inventada pelo designer.

### Open vs. Closed Card Sorting

O que a aula fez foi **open card sorting** (grupos criados pelos alunos). A sequência típica:

1. **Open** (15-20 participantes): descobrir agrupamentos mentais dos usuários
2. **Closed** (20-30 participantes): validar a estrutura proposta — participantes só alocam cards em categorias pré-definidas

Ferramentas digitais: **OptimalSort**, **Maze**, **Useberry** — aplicam card sorting remotamente com dezenas de participantes.

---

## Aula 08 — Questionários de UX e o SUS

### O Que Torna um Questionário Útil

Um questionário para UX deve usar **escalas Likert** (1-5 ou 1-7) para intensidade de atitudes, perguntas neutras que não sugerem a resposta esperada, e um **teste piloto** com 3-5 pessoas antes da aplicação em larga escala.

O **SUS (System Usability Scale)** é o instrumento padronizado mais usado — 10 perguntas alternando afirmações positivas e negativas, pontuação de 0 a 100. Uma pontuação acima de 68 é considerada boa; abaixo de 51, crítica. Benchmarks bem estabelecidos permitem comparar produtos de domínios diferentes.

### Por Que Média Esconde Informação

Uma média de 3.0 em Likert pode vir de: 50% marcando 1 e 50% marcando 5 (bimodalidade — opiniões divididas) ou de 100% marcando 3 (neutralidade unânime). São situações radicalmente diferentes que exigem respostas de design opostas. Sempre inspecionar a **distribuição de frequências**, não só a média.

---

## Aula 09 — Brainstorming: Divergência Antes de Convergência

### As Quatro Regras do Brainstorming (Osborn, 1953)

1. **Sem crítica**: julgamento suspenso durante a geração. Avaliar vem depois.
2. **Quantidade sobre qualidade**: quanto mais ideias, maior a chance de uma boa aparecer.
3. **Ideias inusitadas são bem-vindas**: o improvável hoje pode ser o inovador amanhã.
4. **Combine e aprimore**: ideias dos outros são pontos de partida, não propriedade.

O erro mais comum: violar a regra 1 — alguém critica uma ideia ainda na fase de geração, silenciando os participantes menos assertivos.

### Brainstorming 6-3-5

Variante estruturada: 6 pessoas, cada uma escreve 3 ideias em 5 minutos, a folha passa para o próximo, que adiciona 3 mais. 30 minutos → até 108 ideias. Útil quando o grupo tende a convergir prematuramente em torno de uma ideia dominante.

---

## Aula 14 — Coleta de Dados: Análise Qualitativa e Quantitativa

### Análise de Dados de Questionário

Para dados quantitativos (Likert): calcular média e desvio padrão por item. Para respostas abertas:

- **Codificação temática**: ler todas as respostas e identificar temas recorrentes. Atribuir um código curto a cada tema ("dificuldade de navegação", "confusão com ícones").
- **Saturação**: quando novas respostas não produzem novos códigos, o modelo mental do grupo está mapeado — a coleta pode parar.

### O Problema da Interpretação Afirmada vs. Comportamento Real

O princípio fundamental de pesquisa com usuários: **o que usuários dizem** e **o que usuários fazem** frequentemente divergem. Questionários capturam percepção e motivação declaradas; testes de usabilidade e analytics capturam comportamento real.

Para o T2, os dados do formulário revelam *intenções e percepções* — úteis para design de conteúdo e hierarquia. O comportamento real dos mesmos usuários interagindo com protótipos revelaria *problemas de interação* — uma dimensão diferente, que questionários não capturam.

---

## Aula 17 — Prototipação: Tipos, Fidelidade e a Hipótese por Trás de Cada Protótipo

### A Pergunta que Define o Tipo de Protótipo

A questão central: **qual hipótese estou testando?**

| Hipótese | Tipo de protótipo | Fidelidade |
|---|---|---|
| "Esse fluxo faz sentido?" | Papel, wireframe | Baixa |
| "Essa mecânica de interação funciona?" | Protótipo clicável (Figma) | Média |
| "O visual comunica a identidade?" | Mockup de alta fidelidade | Alta |

Protótipo de papel antes de abrir o Figma poupa horas — falhas de fluxo são detectadas em 10 minutos com post-its. Alta fidelidade prematura desperdiça tempo em pixels que serão descartados.

### O Que Distingue Cada Tipo das Notas

- **Horizontal**: cobre toda a interface superficialmente. Avalia navegabilidade e arquitetura da informação. Não permite completar tarefas reais.
- **Vertical**: cobre um único fluxo completamente. Permite avaliar uma task end-to-end.
- **Alta fidelidade**: pixels corretos, tipografia final, interações reais. Necessário para validar visual e microinterações.
- **Baixa fidelidade**: velocidade máxima, feedback rápido. A perda de informação estética é vantagem em estágio inicial — não contamina o feedback com preferências visuais.

### Storyboard no UX vs. no Cinema

No cinema, storyboard mostra sequência de cenas. Em UX, mostra **a jornada do usuário**: a pessoa em contexto, usando o sistema, antes e depois. Inclui emoções e pensamentos, não apenas telas. O objetivo é humanizar o design — há uma pessoa real com contexto real do outro lado.

---

## Aula 19 — Sketches, Revisões de Design e o Ciclo de Feedback

### Sketches: Baixa Fidelidade com Alta Intenção

Um sketch de interface bem feito contém:
1. O **layout**: posição aproximada de elementos, hierarquia visual
2. **Anotações**: explicações do que não é evidente no desenho — intenção, comportamento, estado alternativo
3. **Flow**: setas mostrando transições entre estados

As anotações têm mais valor que o desenho em si. Um sketch sem anotações obriga o observador a inferir intenção — inferências erradas alimentam discussões improdutivas em reviews.

### Os Quatro Tipos de Revisão: Quando Usar Cada Um

| Tipo | Contexto | Duração |
|---|---|---|
| **Elevator Pitch** | Ideia muito inicial | 2-5 min |
| **Desktop Review** | Trabalho em andamento | 15-30 min |
| **Meeting** | Checkpoint periódico | ~1h |
| **Design Crit** | Entregável formal | 1-2h + preparação |

O **Design Crit** apresenta não só o que funcionou, mas o que *não* funcionou e por quê. O post-mortem de jogos mencionado nas notas é equivalente: honestidade sobre falhas é o que torna a revisão útil para o próximo projeto.

### Quando Simplificar o Storyboard Significa Simplificar a Interface

As notas citam: "se se embananam com storyboards ramificados, reconsiderem suas interfaces." A razão formal: cada ramificação é um ponto onde o usuário pode se perder.

A heurística de Nielsen n.3 (controle e liberdade) e n.5 (prevenção de erros) frequentemente conflitam com interfaces de múltiplos caminhos. Simplificar o storyboard geralmente é o mesmo que simplificar a interface — e ambos reduzem a carga cognitiva do usuário.

---

## Aula 20 — Padrões de Design em IHC

### O Que São Padrões de Design em IHC

O conceito de **padrão de design** em IHC tem origem no trabalho do arquiteto Christopher Alexander (*A Pattern Language*, 1977): capturar soluções recorrentes para problemas recorrentes em um formato reutilizável. Em IHC, um padrão documenta:

- **Problema**: a situação recorrente de design
- **Contexto**: quando o padrão se aplica
- **Solução**: a abordagem que funciona
- **Consequências**: trade-offs do uso

A diferença dos padrões GoF (software): padrões de IHC são sobre **interação e percepção do usuário**, não sobre estrutura de código.

---

### Padrões IHC Essenciais para o T2

O site [ui-patterns.com](https://ui-patterns.com/patterns) que as notas referenciam cataloga os mais usados. Os mais relevantes para uma interface de aplicativo:

| Padrão | Problema | Solução |
|---|---|---|
| **Progressive Disclosure** | Muita informação simultânea sobrecarrega | Mostrar só o necessário; revelar detalhes sob demanda |
| **Breadcrumb** | Usuário perdido em hierarquia profunda | Trilha mostrando o caminho percorrido |
| **Confirmation Dialog** | Ação destrutiva ou irreversível | Pedir confirmação explícita antes de executar |
| **Empty State** | Interface sem dados (primeira vez) | Explicar o estado + ação para populá-lo |
| **Skeleton Screen** | Conteúdo carregando cria sensação de quebrado | Placeholder visual durante carregamento |

O **critério 2.3 do enunciado** ("especificar quais padrões foram escolhidos, justificando a escolha") pede: nome do padrão + contexto onde aparece no design + por que foi escolhido em vez de alternativas.

---

### Diretrizes vs. Padrões: A Distinção que o Enunciado Mistura

**Diretriz**: princípio de design amplo e qualitativo. Ex: "use linguagem do usuário, não jargão técnico" (Nielsen #2).
**Padrão**: solução específica e instanciável. Ex: "use breadcrumb em hierarquias com mais de 2 níveis".

Para o relatório: diretrizes justificam decisões de alto nível; padrões descrevem como a interface é estruturada. Usá-los em seções separadas evita o relatório ficar vago demais.

---

## Aula 21 — Acompanhamento de T2: Validar Antes de Escrever

### Armadilha da Justificativa Circular

Aula sem conteúdo novo — mas o momento do ciclo é importante. Na fase de "fundamentações" (Módulo 02), o erro mais comum em relatórios de UX é a **justificativa circular**:

> "Escolhemos o padrão X porque nossa interface usa X."

O que o relatório deve mostrar:
1. **Dado de pesquisa** que revela o problema de design
2. **Padrão/diretriz** que resolve esse tipo de problema
3. **Aplicação específica**: como o padrão se manifesta nas telas do protótipo

A sequência correta é: dado → problema → solução. A sequência errada: solução → justificativa post-hoc.

---

### Critérios de Fundamentação de Protótipos

Fundamentar esboços não é descrever o que as telas fazem — é explicar **por que** cada decisão foi tomada em termos de princípios estabelecidos. Para cada componente relevante:

- Qual **heurística de Nielsen** ou diretriz se aplica?
- Qual **padrão de IHC** foi usado e por quê aqui especificamente?
- Qual dado da pesquisa do T1 motivou esta decisão?

Três perguntas, três parágrafos curtos por componente. O relatório fica mais coeso que uma descrição narrativa livre.

---

## Aula 24 — Avaliação de Interfaces: Métodos Formais

### Avaliação Heurística vs. Teste de Usabilidade

As notas introduzem o problema da avaliação. Dois métodos principais com trade-offs opostos:

**Avaliação Heurística (Nielsen, 1990)**:
- Realizada por **especialistas** (3-5 avaliadores), não usuários reais
- Cada avaliador analisa a interface solo contra as 10 heurísticas
- Resultados mesclados em lista de problemas com severidade (1-4)
- Detecta ~75% dos problemas com 5 avaliadores; custo baixo
- **Falha**: detecta problemas que usuários reais nunca teriam — e perde problemas que só aparecem em uso real

**Teste de Usabilidade**:
- Usuários reais realizam tarefas específicas enquanto são observados
- Métricas: taxa de conclusão, tempo na tarefa, número de erros, SUS
- **Regra dos 5 Usuários** de Nielsen: 5 participantes detectam ~85% dos problemas de usabilidade — mais que isso tem retorno decrescente

---

### O Gulf of Evaluation — Formalizando o Problema das Notas

O que as notas descrevem ("expectativas do desenvolvedor vs. o que o usuário tem de concreto") é o **Gulf of Evaluation** de Donald Norman:

> A distância entre o estado real do sistema e a percepção que o usuário forma desse estado.

O Gulf de Evaluation é por isso que developers não encontram os problemas testando o próprio software — sabem o que o sistema faz, então percepção e estado real coincidem. Um usuário novo não tem essa ancoragem. A imagem das notas é o Gulf de Evaluation puro. Avaliar é medir sistematicamente o tamanho desse gap.

---

### Escala de Severidade em Avaliação Heurística

| Nível | Descrição | Ação |
|---|---|---|
| 0 | Não é problema de usabilidade | Ignorar |
| 1 | Cosmético | Corrigir se houver tempo |
| 2 | Menor | Baixa prioridade |
| 3 | Maior | Alta prioridade — impede completar a tarefa |
| 4 | Catastrófico | Urgente — bloqueia completamente |

Para um protótipo acadêmico: focar em severidade 3-4 nas iterações iniciais. Severidade 1-2 é refinamento pós-validação de fluxo.
