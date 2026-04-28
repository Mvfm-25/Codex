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
