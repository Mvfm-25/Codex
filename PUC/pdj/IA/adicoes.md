# Projeto de Desenvolvimento de Jogos — Adições & Aprofundamentos
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas. Segue os tópicos na ordem em que apareceram, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---

### Pipeline de Produção — O que cada fase realmente entrega

As notas descrevem as fases mas não o que é o artefato concreto de saída de cada uma:

| Fase | Entrega concreta |
|---|---|
| Conceito | High-concept (1-2 frases), pitch document, análise de viabilidade |
| Pré-produção | GDD (Game Design Document), protótipo jogável, pipeline técnico validado, orçamento |
| Produção | Alpha, Beta, Gold Master |
| Pós-produção | Patches, DLCs, port para outras plataformas, post-mortem |

O **GDD** é o documento central da pré-produção — especifica mecânicas, narrativa, arte conceitual, sistemas de áudio, UI e metas de performance. Em estúdios modernos ele vive em wikis (Confluence, Notion) em vez de um PDF estático, pois muda constantemente.

---

### Bartle Taxonomy — O que as notas não explicam sobre cada tipo

As quatro categorias (Socializador, Matador, Explorador, Conquistador) têm uma relação com **dois eixos**:

```
                Agir
                 ↑
Matador          |          Conquistador
(Players)        |          (World)
-----------------+------------------→ Interagir
(Players)        |          (World)
Socializador     |          Explorador
                 |
              Interagir
```

- Eixo X: foco em **jogadores** vs. foco no **mundo**
- Eixo Y: **agir** vs. **interagir**

Nenhum jogador real é 100% de um tipo — são combinações. Um jogo bem balanceado oferece algo para cada tipo. Counter-Strike atende Matadores e Socializadores. Dark Souls atende Conquistadores e Exploradores.

---

### MDA Framework — A direção que designer e jogador percorrem

O ponto mais importante do MDA que ficou implícito nas notas:

- **Designer** pensa de M → D → A (cria mecânicas, antecipa dinâmicas, projeta estética desejada)
- **Jogador** experimenta de A → D → M (sente a estética primeiro, percebe as dinâmicas depois, só eventualmente "vê" as mecânicas)

Isso explica por que mecânicas bem documentadas no papel frequentemente criam experiências ruins: o designer estava pensando em M enquanto o jogador só vai chegar lá muito depois, se chegar.

**Exemplo com Portal:**
- Mecânica: portais que preservam momentum
- Dinâmica: puzzles emergentes de troca de perspectiva e momentum acumulado
- Estética: sensação de descoberta e engenhosidade

---

### Flow State — A fórmula de Csikszentmihalyi

O gráfico das notas mostra o conceito. O que ficou faltando é a estrutura: o estado de flow ocorre quando **desafio e habilidade estão equilibrados e elevados simultaneamente**:

```
Desafio
  ↑  Ansiedade | FLOW
     ----------|----------
     Tédio     |
               └──────────→ Habilidade
```

- Desafio >> Habilidade = ansiedade, frustração
- Habilidade >> Desafio = tédio
- Ambos baixos = apatia
- Ambos altos e próximos = **flow**

A curva de dificuldade de um jogo bem desenhado não é linear — ela sobe junto com a habilidade do jogador, mantendo o equilíbrio. Tutoriais bem feitos são a entrada no eixo antes do flow começar.

---

### Dominância e Equilíbrio — O Nash que estava escondido no Dilema do Prisioneiro

As notas mencionam estratégia dominante no contexto do Dilema do Prisioneiro. O conceito formal que estava por baixo é o **Equilíbrio de Nash**: um estado onde nenhum jogador tem incentivo para mudar de estratégia dado o que os outros estão fazendo.

No Dilema do Prisioneiro, o único equilíbrio de Nash é **ambos confessarem** — mesmo que ambos calarem seja melhor para o grupo. Isso é o problema central do game design competitivo: o equilíbrio individual e o equilíbrio coletivo raramente coincidem.

**Consequências práticas:**
- Uma estratégia dominante elimina escolha real → jogo fica chato
- Sem equilíbrio claro → jogo fica caótico e injusto
- O sweet spot é ter múltiplas estratégias viáveis com trade-offs reais (rock-paper-scissors é o exemplo mínimo)

---

### Complexidade Emergente — Por que Go nunca teve dois jogos iguais

As notas citam Go como exemplo. O número de posições possíveis em Go é aproximadamente $2.08 \times 10^{170}$ — maior que o número de átomos no universo observável ($10^{80}$). Com apenas duas regras principais:

1. Stones do mesmo time conectados formam grupos
2. Grupos sem liberdades são capturados

Isso é **emergência**: regras simples, espaço de possibilidades astronômico. O mesmo princípio do Tetris, xadrez, e Magic: The Gathering.

**Regras de ouro para gerar emergência:**
- Cada elemento interage com múltiplos outros (não apenas com o sistema central)
- Contexto muda o resultado de uma mesma ação
- Consequências têm alcance temporal (decisão agora afeta situação depois)

---

### Pacing — A Estrutura Narrativa que estava por baixo

As notas mencionam a **Jornada do Herói** de passagem. A estrutura de três atos é mais diretamente aplicável ao pacing de jogos:

```
Ato 1 (Setup)      →  Ato 2 (Confronto)     →  Ato 3 (Resolução)
Introdução         →  Complicações escalando  →  Clímax + Desfecho
~25% do jogo       →  ~50% do jogo           →  ~25% do jogo
```

A cena da girafa em The Last of Us que as notas mencionam é um **beat de alívio** no meio do Ato 2 — a teoria chama isso de "valley" antes do próximo "peak". Sem valleys, o jogador dessensibiliza. Sem peaks, entedia.

O **Diretor do Left 4 Dead** é um caso raro de pacing algorítmico: ele monitora métricas do time (HP, ammo, distância do objetivo) e ajusta spawns e itens em tempo real para manter a tensão no nível ideal — flow state aplicado sistemicamente.

---

### Protótipos — Os três tipos e quando usar cada um

As notas mencionam papel & caneta, wireframe e prototipação digital. A distinção importante é a **fidelidade**:

- **Baixa fidelidade (papel)**: testa conceito e regras. Custo: horas. Ideal para validar "isso é divertido?"
- **Média fidelidade (wireframe/grey-box)**: testa layout, fluxo e feel. Custo: dias. Ideal para validar "isso funciona?"
- **Alta fidelidade (vertical slice)**: testa experiência completa de uma seção. Custo: semanas. Ideal para validar "isso está polido?"

O protótipo de papel do Spore que as notas mostram testava apenas as **regras de evolução** — sem gráficos, sem áudio, sem engine. A pergunta era só "a progressão é satisfatória?". Levou dias. O jogo final levou anos.

---

### Game Loop — O conceito que une tudo

Não apareceu nas notas mas é o fundamento técnico de qualquer jogo:

```
enquanto jogo_está_rodando:
    processar_input()
    atualizar_estado()
    renderizar()
```

O **game loop** roda dezenas a centenas de vezes por segundo. Todo sistema de jogo (física, IA, animação, audio) é chamado dentro dele. A frequência determina os FPS. As mecânicas são o que acontece em `atualizar_estado()`. As dinâmicas emergem de como os sistemas interagem nessa função.

**Fixed timestep vs. variable timestep**: física precisa de timestep fixo para ser determinística (mesmo input, mesmo resultado). Rendering usa timestep variável para maximizar FPS. Jogos modernos separam os dois.

---

## Aula 04 — As 4 Chaves da Diversão e a Anatomia do Desafio

### As 4 Keys to Fun (Nicole Lazzaro)

O Bartle classifica *quem* são os jogadores. As **4 Keys to Fun** de Nicole Lazzaro classificam *que tipo de diversão* um jogo oferece — e um bom jogo oferece mais de uma:

| Chave | Nome | Motor emocional | Exemplo |
|---|---|---|---|
| Hard Fun | Diversão Desafiadora | **Fiero** — triunfo pessoal após superação | Dark Souls, I Wanna Be The Guy |
| Easy Fun | Diversão Exploratória | Curiosidade, mistério, surpresa | Breath of the Wild |
| Serious Fun | Diversão Significativa | Imersão, alteração de estado interno | Journey, Portal |
| People Fun | Diversão Social | Alegria de conexão, competição, cooperação | CS:GO, Among Us |

**Fiero** (do italiano *orgulho*) é a emoção específica do Hard Fun: a reação física de levantar os braços ao derrotar um chefe. Lazzaro pesquisou que é a emoção mais intensa que videogames produzem — das mais difíceis de alcançar em outros mídias.

Easy Fun não precisa de habilidade: exploração de mundo aberto sem objetivo claro, liberdade de "fazer bobagem". Serious Fun pode não ter vitória definida — o objetivo é *sentir* algo, não ganhar.

---

### A Definição de Jogo de Bernard Suits

> *"Tentativa voluntária de superar obstáculos desnecessários."* — Bernard Suits, *The Grasshopper* (1978)

Cada palavra carrega peso:
- **Voluntária**: coerção elimina o aspecto lúdico. Um prisioneiro obrigado a jogar não está "jogando" no sentido filosófico.
- **Obstáculos**: qualquer resistência ao objetivo (inimigos, física, outros jogadores).
- **Desnecessários**: isso separa jogo de trabalho. Você *poderia* pegar a bandeira com a mão — as regras proíbem. Você aceita a limitação porque quer. Isso é **lusory attitude** (atitude lúdica).

Essa definição explica por que remover obstáculos não torna um jogo melhor: sem obstáculos, não há jogo.

---

### Comunicação no Jogo: Sinais vs. Feedback

O jogo precisa de uma linguagem consistente com o jogador. A distinção fundamental:

- **Sinal**: evento que ocorre *independentemente* da ação do jogador. Alarme ao ser detectado; música mudando ao entrar em combate; cutscene disparada por timer.
- **Feedback**: resposta direta a uma ação do jogador. Som de hit confirmation ao acertar um golpe; número de dano flutuando; vibração do controle ao coletar item.

O erro mais comum: **feedback ausente ou ambíguo**. Se o jogador faz uma ação e nada acontece visivelmente, ele não sabe se a ação funcionou. Isso quebra o loop de agência — a sensação de que *eu* fiz algo e o mundo respondeu.

---

### Desafio = Obstáculo + Justiça

O desafio só funciona se o jogador **entende o que aconteceu e por quê**:

- **Sem compreensão**: o obstáculo vira frustração. Morrer sem entender o motivo não é diferente de morrer aleatoriamente.
- **Com compreensão**: o obstáculo vira aprendizado. "Errei o timing" → "Na próxima acerto" → motivação para tentar de novo.

O Dark Souls é frequentemente citado como "difícil" — mas a dificuldade é percebida como *justa* porque cada ataque telegrafará antes de acontecer. A *percepção* de justiça importa mais que a dificuldade objetiva. Jogos com hitboxes invisíveis e dano de fonte desconhecida criam percepção de injustiça mesmo que matematicamente corretos.

---

## Aula 05 — Core Loop, Game Feel e Espaço de Possibilidades

### O Diagrama Central (Core Mechanic)

O diagrama em cebola serve para responder: **qual é a interação fundamental mais repetida no jogo?** É chamado de *core mechanic* ou *core loop*:

- Mario: correr + pular
- Dark Souls: atacar + esquivar (gerenciando estamina)
- Tetris: rotacionar + posicionar

Tudo mais no jogo existe para criar variações contextuais desse núcleo. Progressão, narrativa, level design são *embalagens* ao redor do core.

A regra de Miyamoto — "fundamentos sólidos primeiro" — significa: se o core loop não é divertido em si mesmo, nenhuma quantidade de conteúdo extra conserta o jogo.

---

### 30 Seconds of Fun e Game Feel

O conceito vem do design do Halo: a Bungie isolou um loop de combate de ~30 segundos que era divertido de repetir indefinidamente. Toda a estrutura de encontros do jogo são variações desse loop.

**Game Feel** (ou *juice*) é a qualidade tátil das mecânicas — a soma de:
- Animações responsivas (sem input lag)
- Sons que confirmam cada ação
- Feedback visual (screenshake, hit-stop, partículas)
- Momentum e peso do personagem

Jogos com mau game feel parecem "plástico". A mesma mecânica com bom ou mau game feel cria experiências radicalmente diferentes. É o que o Extra Credits chama de "a alma do jogo": um jogo pode ter mecânicas brilhantes mas game feel ruim e ainda assim falhar.

---

### Espaço de Possibilidades: O Eixo Simplicidade-Emergência

O problema das três configurações:

```
Muitas regras → espaço grande → caótico e confuso
Poucas regras → espaço pequeno → entediante e previsível
Poucas regras + interações ricas → espaço emergente → ideal
```

A distinção crucial é entre **complexidade complicada** e **complexidade emergente**:
- **Complicada**: muitas regras independentes para memorizar. Alto esforço, baixa surpresa.
- **Emergente**: poucas regras que interagem entre si. O contexto muda o resultado da mesma ação.

Teste prático: se você remove uma regra, o jogo simplifica ou desmorona? Em sistemas emergentes, cada regra interage com as outras — remover qualquer uma colapsa o sistema.

---

## Aulas 14, 15, 16 — Godot Engine: Câmera, Nodos e Ciclo de Vida

### O Sistema de Cenas e Nodos do Godot

A arquitetura central do Godot é a **árvore de nodos**:
- Tudo no jogo é um **nodo** (Node) com propriedades e métodos
- Nodos se organizam em hierarquia pai-filho
- Uma **cena** é uma subárvore salva como arquivo `.tscn`, reutilizável e instanciável

Essa hierarquia tem implicações práticas: transformações (posição, rotação, escala) são relativas ao pai. Colocar a Camera2D como filho do sprite do personagem já é Camera Follow — o nodo herda a posição do pai sem uma linha de código.

---

### Camera2D — Viewport, Limites e Smoothing

O mapeamento entre mundo do jogo e tela envolve os mesmos conceitos de CG:
- **World Space**: coordenadas do mundo (SRU)
- **Screen Space**: pixels na tela (SRP)
- **Camera2D** faz essa transformação automaticamente — a mesma regra de três que víamos em CG, abstraída pelo Godot

Os **limites de câmera** (`limit_left`, `limit_right`, etc.) restringem a navegação da viewport — fundamental para não expor área além do nível.

O **smoothing** (delay de acompanhamento) simula um cameraman físico: o sprite se move, a câmera "tenta alcançar". Cria sensação de velocidade em personagens rápidos. **Viewports múltiplas** permitem minimaps e split-screen: cada Viewport renderiza a cena de uma perspectiva diferente.

---

### Ciclo de Vida de Nodos: free() vs queue_free()

```gdscript
nodo.free()        # Libera imediatamente. Perigoso se outro código ainda referencia o nodo.
nodo.queue_free()  # Agenda liberação para o fim do frame atual. Seguro, recomendado.
```

O risco do `free()` imediato: se qualquer outro nodo ainda segura referência e tenta acessá-la no mesmo frame, ocorre use-after-free. `queue_free()` espera o frame terminar, garantindo que ninguém mais usará o nodo.

**VisibleOnScreenNotifier2D** detecta quando um nodo sai da viewport. Combinado com `queue_free()`, é o padrão para destruir projéteis e decals fora de tela — economizando memória e processamento.

### Troca de Cenas

`get_tree().change_scene_to_file()` descarrega a cena atual e carrega uma nova — toda a árvore de nodos é destruída e reconstruída. Para transições suaves com efeitos (fade, preservação de estado), a alternativa é **instanciar cenas dentro de outra cena** ao invés de trocá-las — mais trabalho, mais controle.

---

## Aula 02 — Multidisciplinaridade e Controle de Versão em Jogos

### Por Que Jogos São o Produto Mais Complexo de Fazer

As notas capturam "multidisciplinar, muita gente". O dado concreto: um AAA moderno envolve 500-3000 pessoas e custa $200-500M. A razão é que jogos são simultaneamente software de tempo real (engine, networking, rendering), obra de arte (arte, música, narrativa), produto de entretenimento (game design, UX, monetização) e experiência performática (voice acting, motion capture). Cada área tem cultura, ferramentas e vocabulário diferentes — a integração é o principal desafio.

### Por Que Perforce Domina o Mercado AAA

Git foi projetado para código-fonte textual. Um projeto AAA tem terabytes de texturas, modelos 3D e áudios. Git armazena todo histórico de cada arquivo — inviável para assets que mudam frequentemente e pesam gigabytes cada.

**Git LFS** (Large File Storage) é a solução moderna para projetos menores: armazena ponteiros no git, arquivos grandes em servidor separado. Para projetos Godot de tamanho médio, Git + LFS é suficiente. Perforce (*Helix Core*) foi projetado desde o início para binários grandes — daí sua dominância em estúdios grandes.

---

## Aula 03 — Pitch de Jogo, High-Concept e Scope Creep

### O Que Torna um High-Concept Eficaz

"Uma boa ideia que cabe em duas linhas" (Cohen) tem estrutura formal:

> *[Gênero/referência conhecida] + [twist diferenciador]*

Exemplos:
- "Dark Souls mas cooperativo desde o início" → *It Takes Two*
- "Metroid mas com roguelike" → *Returnal*
- "GTA mas pirata" → *Skull and Bones* (vendeu mal — o twist não era interessante o suficiente)

O high-concept serve ao **pitch** (convencer um produtor), não ao design. O design real começa depois. O erro é tentar que o high-concept seja também um documento de design.

### Por Que "Não Dá Tempo" É a Frase Mais Importante

O conceito formal é **scope creep**: o escopo tende a crescer continuamente durante o desenvolvimento porque adicionar é sempre mais fácil que cortar. A solução é design **subtrativo**: começar com a ideia completa e cortar tudo que não é core. O que sobra após os cortes é o MVP do jogo.

---

## Aula 06 — Pacing Dinâmico e o Algoritmo do Diretor do Left 4 Dead

### O Que o Diretor Monitora

O Diretor do Left 4 Dead é um dos exemplos mais estudados de pacing dinâmico. Ele monitora continuamente: HP total do time, munição disponível, itens coletados, tempo sem evento de tensão, distância até o objetivo. Com esses inputs, ajusta: spawn de infectados, localização de itens (medkits, ammo) e ativação de eventos especiais (tank, witch).

O objetivo é manter a **curva de tensão** dentro de uma banda — nem muito fácil, nem impossível. Implementação prática do flow state de Csikszentmihalyi aplicado sistemicamente.

### Tension Graph: A Ferramenta por Trás do "Tempo X Tensão"

Um **tension graph** visualiza o arco emocional planejado:

```
Tensão
 ↑     /\      /\      /\/\
 |    /  \    /  \    /
 |   /    \  /    \  /
 └──/──────\/──────\/───────→ Tempo
```

Cada pico é confronto ou revelação; cada vale é alívio ou exploração. Sem alternância: dessensibilização (todos picos) ou tédio (todos vales). A cena da girafa de The Last of Us é um **valley** deliberado no Ato 2 — alívio emocional antes do próximo pico.

### Weenies: Guiar sem Dizer

Os exemplos de Disney que Cohen menciona são **weenies**: landmarks visuais que atraem o olhar e guiam o movimento sem instrução explícita. O Castelo da Cinderela no centro do Magic Kingdom é o exemplo original de Walt Disney. Em jogos: pilares de luz, janelas iluminadas, corredores com perspectiva convergente.

---

## Aula 09 — Acompanhamento do T1: O Que Juízes Avaliam em Pitches

### Critérios de Avaliação em Pitches de Jogo

Aula de acompanhamento sem conteúdo novo. O contexto: o T1 é um pitch de jogo. Em pitches formais na indústria os critérios são:

1. **Clareza do conceito**: o ouvinte entende o jogo em 30 segundos?
2. **Diferenciação**: por que este jogo e não outro que já existe?
3. **Viabilidade**: é realizável com os recursos disponíveis?
4. **Apresentação**: slides, linguagem, confiança do apresentador

Para pitches acadêmicos, clareza é o critério mais importante — juízes veem dezenas de pitches e penalizam os que demandam esforço para entender.

### O Documento por Trás do Pitch: GDD

O **GDD (Game Design Document)** é o artefato formal que segue o pitch aprovado. Especifica mecânicas, narrativa, arte conceitual, sistemas de áudio, UI e metas de performance. Em estúdios modernos ele vive em wikis (Confluence, Notion) em vez de PDF estático, pois muda constantemente durante o desenvolvimento.

---

## Aula 17 — Áudio em Godot: AudioStreamPlayer e Effects Chain

### AudioStreamPlayer vs. AudioStreamPlayer2D vs. AudioStreamPlayer3D

| Nodo | Quando usar |
|---|---|
| `AudioStreamPlayer` | Música, ambiance, UI sounds — sem posição no espaço |
| `AudioStreamPlayer2D` | Sons com posição no mundo 2D (passos, efeitos locais) |
| `AudioStreamPlayer3D` | Sons posicionais em 3D |

O `AudioStreamPlayer2D` ajusta volume e panning automaticamente com a distância entre o nodo e o `AudioListener2D` (geralmente a câmera). Um som de coleta de moeda sai diferente de cada lado da tela — sem nenhum código adicional.

### Audio Bus e Effects Chain

O painel de áudio do Godot funciona como DAW simplificado. Cada `AudioStreamPlayer` envia para um **bus** (Master por padrão). Effects são adicionados ao bus:

```
AudioStreamPlayer → Bus "SFX" → [Compressor] → [Reverb] → Master → Hardware
```

O **low-pass filter** que Cohen usou é um efeito de bus: corta frequências altas, dando sensação de distância ou de áudio chegando de trás de uma parede. Colocar no bus SFX afeta todos os sons do grupo; no bus específico, apenas aquele stream.

### Audacity para Game Audio

Casos de uso práticos:
- **Normalizar** volume de samples (todas ao mesmo peak para consistência de mixagem)
- **Loop points**: cortar samples para que início e fim casem perfeitamente em loop
- **Noise reduction**: remover ruído de fundo de gravações próprias
- **Export**: converter WAV para OGG (formato preferido do Godot por compressão)

---

## Aula 18 — Tilesets e Tilemaps: Arquitetura e Performance

### A Diferença entre Tileset e Tilemap

- **Tileset**: a *biblioteca* — textura grande (spritesheet) com todos os tiles organizados em grid. É o recurso (`.png` + metadados de colisão, animação, etc.).
- **Tilemap** (`TileMapLayer`): o *mapa* — especifica qual tile vai em cada posição da grade. Usa o tileset como referência.

Um único tileset pode ser reutilizado por múltiplos tilemaps (diferentes fases), e um tilemap pode ter múltiplas camadas (fundo, decoração, colisão, foreground) usando o mesmo tileset.

### Batching: Por Que Tilemap é Mais Performático que Sprites Individuais

Desenhar 1000 sprites individuais resulta em 1000 draw calls para a GPU. `TileMapLayer` agrupa todos os tiles em um **mesh** único e envia em **um único draw call**. Em mobile, a diferença é perceptível; em mundos grandes, é necessária.

Isso explica por que jogos 2D clássicos usavam tilemaps mesmo quando poderiam usar sprites individuais — o batching era obrigatório dadas as limitações de hardware.

### Tiles de Física: Collision Shapes por Tile

No editor de tileset do Godot, cada tile pode ter sua própria **collision shape**:
- Tiles de chão: retângulo full
- Tiles de rampa: triângulo
- Tiles decorativos: sem collision

O `TileMapLayer` gera automaticamente um corpo de física composto pela união das shapes de todos os tiles — o personagem colide com o mapa inteiro via um único `StaticBody2D`, eficiente e sem código manual.

---

## Aula 21 — Checkpoint T2: Level Editors, Data-Driven Design e Condições de Vitória

### Level Editor como Ferramenta de Desenvolvimento

Construir a ferramenta antes do jogo é decisão de design chamada **tool-first development**. O benefício: o jogo torna-se **data-driven** — os níveis são dados, não código. Alterações de nível não exigem recompilação. A estrutura descrita nas notas (editor que gera JSON com propriedades de entidades) é a base de todo engine profissional:

- **Unity**: cenas salvas como YAML/JSON interno
- **Godot**: cenas em `.tscn` (formato texto)
- **Unreal**: blueprints + assets `.uasset` binários com metadados

A diferença entre um jogo e um motor de jogo é exatamente isso: quando designers criam conteúdo sem tocar em código, o motor está pronto.

---

### JSON para Configuração de Entidades

O padrão de *entity config* em JSON é ubíquo na indústria:

```json
{
  "entities": [
    { "id": "goblin", "hp": 30, "damage": 5, "speed": 120, "ai": "patrol" }
  ]
}
```

**Vantagens sobre valores hard-coded**:
- Balanceamento sem recompilar: ajustar `damage` é editar um número
- Game designers sem código podem modificar
- Facilita testes A/B (carregar configs diferentes para testar variações)

**Limitação**: JSON não tem tipos complexos, referências circulares ou lógica. Para dados mais ricos, Godot usa **Recursos** (`.tres`) — arquivos texto com schema definido, diretamente integrados ao editor.

---

### Condições de Vitória e Derrota: Estrutura Formal

A exigência do Cohen ("jogador deve conseguir ganhar e perder") mapeia para o **game loop de estado**:

```gdscript
enum GameState { PLAYING, WIN, LOSE }
var state = GameState.PLAYING

func _process(delta):
    if state != GameState.PLAYING:
        return
    check_win_condition()
    check_lose_condition()
```

A separação entre **estado do jogo** e **lógica do jogo** é a arquitetura mínima necessária. Sem ela, as condições de vitória e derrota interferem com a atualização normal do jogo.

---

### Python → GDScript: As Diferenças que Importam

| Python | GDScript |
|---|---|
| `def func(self):` | `func nome():` |
| `self.variavel` | `variavel` (implícito no nodo) |
| `import modulo` | `preload()` / `load()` |
| `None` | `null` |
| `isinstance(x, Tipo)` | `x is Tipo` |

O que muda estruturalmente: GDScript é event-driven — lógica vive em `_ready()`, `_process()`, `_input()` em vez de um loop explícito. A lógica Python de simulação de jogo (estado, entidades, colisões) porta quase diretamente; input e rendering precisam ser adaptados para o paradigma de nodos e sinais do Godot.

---

## Aula 14 — A Godot e a Arquitetura de Nós

### O Modelo de Cena: Árvore de Nós

A Godot foi escolhida como engine do semestre, então vale fixar sua ideia central, que difere da Unity (GameObject + Components): na Godot, **tudo é um nó** (*Node*), e um jogo é uma **árvore de nós** (*SceneTree*). Cada nó é uma peça com uma responsabilidade — `Sprite2D` desenha, `CollisionShape2D` colide, `Camera2D` enquadra — e nós ganham comportamento composto por *aninhamento* e *herança*, não por anexar componentes. Uma **cena** é uma sub-árvore salva em arquivo (`.tscn`) que pode ser instanciada como peça reutilizável (um inimigo, uma bala). Essa composição por árvore é o que torna "mudar a hierarquia de nós" tão poderoso quanto se verá nas próximas aulas.

### Representação UTF do Mapa e Geração Procedural de Cavernas

A "geração de cavernas com representação UTF do mapa" das notas é **geração procedural de conteúdo** (PCG). A técnica clássica para cavernas orgânicas é **autômato celular**: parte-se de uma grade aleatória de paredes/vazios e aplica-se algumas iterações de uma regra de vizinhança (uma célula vira parede se a maioria dos 8 vizinhos é parede). Em poucos passos o ruído aleatório se "assenta" em cavernas conectadas e arredondadas. Manipular canais **RGB** do sprite para distinguir parede de chão (como nas notas) é uma forma de *debug* de PCG: visualizar a grade lógica antes de ter arte de verdade — separar a **representação de dados** do mapa da sua **renderização** é boa prática que paga depois.

---

## Aula 15 — Câmera 2D, Window e Viewport

### SRU, SRP e a "Regra de Três" da Câmera

Os termos resgatados de CG são o coração do que o `Camera2D` automatiza. **SRU** (Sistema de Referência do Universo / *world space*) são as coordenadas do mundo do jogo — onde os objetos "realmente" estão. **SRP** (Sistema de Referência do Dispositivo / *screen space*) são pixels na tela. A câmera define uma **window** (a região retangular do mundo que está sendo observada) e a engine a mapeia para o **viewport** (a região da tela onde isso é desenhado). A transformação é uma composição de translação + escala — a "regra de três" das notas:

$$x_{\text{tela}} = (x_{\text{mundo}} - x_{\text{window}})\cdot\frac{\text{largura}_{\text{viewport}}}{\text{largura}_{\text{window}}}$$

Quando o redimensionamento da janela "quebra a renderização" (o bug que o Cohen mostrou), é porque a razão de aspecto do viewport mudou sem ajustar a window — exatamente o problema de *aspect ratio* dos códigos OpenGL de CG. A Godot oferece modos de *stretch* (`viewport`, `canvas_items`) e *aspect* (`keep`, `expand`) justamente para resolver isso de forma declarativa.

### Camera Follow, Limites e Smoothing (o "delay")

Os três efeitos demonstrados são recursos prontos do `Camera2D`, e cada um tem um nome técnico:

- **Camera follow** = tornar a câmera filha do nó do jogador na árvore. Como filhos herdam a transformação do pai, a câmera segue de graça — daí "zero linhas de código". É a manifestação direta da herança de transformações da árvore de nós.
- **Limites de câmera** (*camera limits*) = *clamping* da posição da câmera a um retângulo, impedindo que ela mostre "fora do mapa". Útil para não revelar o vazio além das bordas da fase.
- **Smoothing / *position smoothing*** = o "delay de acompanhamento". Em vez de a câmera saltar para a posição alvo, ela **interpola** suavemente a cada frame (tipicamente um *lerp*: `pos += (alvo - pos) * fator`). É o "câmera-man físico" das notas, e a observação ao Cadu está certa: smoothing reforça a *sensação* de velocidade e peso do personagem.

### V-Sync — Por Que é Recomendado

A recomendação de **V-Sync** (sincronização vertical) merece o porquê: a GPU desenha quadros num ritmo independente do monitor; quando um novo quadro é trocado *no meio* da varredura da tela, vê-se **screen tearing** (uma "costura" horizontal onde metade da tela mostra o quadro novo e metade o antigo). V-Sync força a troca de buffer a acontecer só no *vertical blank* do monitor, eliminando o tearing — ao custo de prender o frame rate à taxa de atualização (60 Hz → 60 FPS) e adicionar um pouco de latência de entrada. É o trade-off padrão: imagem limpa vs latência mínima.

---

## Aula 16 — Ciclo de Vida de Nós e Troca de Cenas

### `free()` vs `queue_free()` — e Por Que a Diferença Importa

A regra do Cohen ("assim como criamos, destruímos") evita **vazamento de memória**: nós removidos da árvore mas nunca liberados continuam ocupando RAM. As duas formas têm semântica distinta e não-intercambiável na prática:

| | `free()` | `queue_free()` |
|---|---|---|
| Quando libera | **imediatamente**, na hora da chamada | no fim do frame atual, em fila |
| Risco | se o nó (ou um ancestral) ainda está sendo processado neste frame, gera *crash*/acesso inválido | seguro: espera todo o processamento do frame terminar |
| Uso recomendado | casos controlados, fora do ciclo de sinais | **o padrão** para destruir nós durante o jogo |

A razão de `queue_free()` existir: durante um frame, a engine percorre a árvore chamando `_process`/sinais; deletar um nó *no meio* dessa varredura corromperia a iteração. A fila adia a remoção para um momento seguro. Regra prática: na dúvida, `queue_free()`.

### Liberar o que Saiu da Tela — `VisibleOnScreenNotifier2D`

O exemplo dos **decals** de tiro e das "caixinhas liberadas ao sair da viewport" é uma técnica de gestão de recursos: objetos efêmeros (partículas, projéteis, marcas) acumulam-se e degradam a performance se nunca somem. O `VisibleOnScreenNotifier2D` emite o sinal `screen_exited` quando o nó deixa o campo de visão da câmera, e conectá-lo a `queue_free()` faz a limpeza automática. É o mesmo princípio do **limite de decals** do TF2 citado nas notas: jogos impõem um teto de objetos descartáveis para não esgotar memória/GPU — aqui, em vez de um teto fixo, libera-se por visibilidade.

### Troca de Cenas e a "Gambiarra" das Transições

A troca de cenas (`change_scene_to_file` / `change_scene_to_packed`) descarrega a cena atual e carrega outra — é o mecanismo para menu, game over e troca de fase. O motivo de transições "limpas" darem trabalho (a "gambiarra" das notas) é que a troca padrão é **abrupta e síncrona**: a cena antiga some e a nova aparece de uma vez, e durante o carregamento de cenas grandes o jogo *trava*. Fazer um *fade* suave exige manter um nó **persistente** *acima* da cena trocada (um *autoload*/singleton com um `CanvasLayer` por cima de tudo) para animar a transição enquanto a cena por baixo é substituída — e, para cenas pesadas, **carregamento em segundo plano** (`ResourceLoader` em *thread*) para não congelar. Daí a fama de "muita gambiarra": a engine dá o corte seco de graça, mas a transição polida você monta por cima.

---

### Referências para ir além

- **Documentação oficial da Godot — *Your first 2D game* e *Nodes and scenes*** (docs.godotengine.org) — a base da árvore de nós e do ciclo de vida.
- **Godot Docs — `Camera2D`, `Viewport` e *Multiple resolutions*** — window/viewport, limites, smoothing e modos de stretch.
- **Godot Docs — *Nodes and scene instances: freeing nodes*** — a distinção `free()` vs `queue_free()` e `VisibleOnScreenNotifier2D`.
- **Sebastian Lague — "Procedural Cave Generation" (série no YouTube)** — autômatos celulares para cavernas, exatamente a técnica das notas.
- **Robert Nystrom, *Game Programming Patterns* (gratuito em gameprogrammingpatterns.com)** — *Game Loop*, *Update Method* e *Object Pool* (alternativa a destruir/recriar nós o tempo todo).
