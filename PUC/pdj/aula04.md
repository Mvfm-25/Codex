# Projeto de Desenvolvimento de Jogos
## [13-03-2026] [mvfm]

### Game Design
- Jogo de exemplo : **[Bartok](https://en.wikipedia.org/wiki/Bartok_(card_game))**
- parecido com Uno, 3-5 jogadores sem os coringas
- Objetivo é ser o primeiro sem nenhuma cartas
- O que o sor queria mostrar é que jogos de sorte não tem bom game design
- Uma das questões é ter *momentos interessantes quando não é sua vez*.
- Que jogo é divertido quando você não está fazendo nada?

### Iteração
- *Repetir, refinar.*
- 1% inspiração, 99% iteração.
- **" Tentativa voluntária de ultrapassar obstáculos desnecessários "** -*[Bernard Suits (The Grasshopper, 1978)](https://periodicos.sbu.unicamp.br/ojs/index.php/conexoes/article/view/8674955)*
- Flow state lmao
- lhe falta miques, aberta.

### Flow state
- Transe, distração em relação ao mundo real, suspenção de descrença.
![are you gaming](assets/flow_state.png)

### Os jogadores
- Quem são essas pessoas estranhas
- ![mud players](assets/mud_players.png)
1. Socializador : forma relacionamentos com outros jogadores
2. Matador : interfere com outros jogadores, quer ser o melhor
3. Explorador : quer descobrir o mundo, explora mecânicas
4. Conquistador : procura tokens de vitória, bater as regras do jogo, atingir 100%
- [Teste de personalidade para jogadores de mud](https://matthewbarr.co.uk/bartle/)
![resultados](assets/mmo_test.png)

### E Como aplicar isso
-  Hard Fun
	- Diversão desafiadora
	- [Fiero](https://www.nicolelazzaro.com/the4-keys-to-fun/), triunfo pessoal.
	- Não foca em sorte.
	- I wanna be the guy
	- ![VÍDEO DE VIDEOGAMEDUNKEY DE TODOS OS CARAS POSSÍVEIS](https://www.youtube.com/watch?v=_nW9k6k1I3k&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
- Easy Fun
	- Mistério, curiosidade, surpresa.
	- Foco no puro prazer de testar as mecânicas jogo, liberdade de bobagens
	- Exemplo principal é **Breath Of The Wild**.
	- ![Game Maker's Tool Kit oh thank god](https://www.youtube.com/watch?time_continue=139&v=vmIgjAM0uh0&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
	- See that mountain? You can climb there.
- Serious Fun
	- [?Jogos de terapia]
	- Mais interesse sobre suas sensações internas
	- Isso pode ser significar literalmente qualquer coisa que você quiser.
	- Exemplo é Portal.
	- ![Inertia dampners](https://www.youtube.com/watch?v=ninRkHZ7WOg&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
- People Fun
	- Jogos de multijogador basicamente
	- Divertido tanto por competitividade quanto por cooperação.
	- Jogar futebol com a gurizada no churrasco, é mais divertido com os amigos do que sem.
	- Exemplo principal é **Journey**.
	- ![Journey](https://www.youtube.com/watch?v=L-h5pNAteUQ&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)

### Elementos de jogo
- Jogo é um sistema : Regras, objetivos, condições de vitória e derrota.
- Linguagem com o jogador
	- Algo aconteceu?
	- Atingiu um objetivo?
	- Deve se manter a mesma com o jogador, mas o sor comenta que não necessariamente. Ligeiramente confuso.

### Tipos de Comunicação
- Sinais
	- Algo aconteceu, independentemente do jogador
	- Avisos
- Feedback
	- Confirmação audiovisual de uma ação do jogador.
	- Se foi ação dele, deixar claro que foi dele.

### Desafio
![tough shit, n00b](dif_curve.png)
- **Whatever doesn't kill, makes you stronger.**
- Desafio = **Obstáculo + Justiça**
- O Jogador precisa compreender o que aconteceu o o porquê
	- Objetivos claros
	- Jogador pode se sentir trapaceado, injustiçado. *Não queremos isso*.
	- Pacing importa, dificuldade não normalmente se mantém a mesma para fazer com que o jogador não se desgaste demais.
- Vários vídeos hoje na aula. 

### MDA Framework
- Como formalizar o game design?
- Regras
	- Definem o mundo, o que está disponível nele, o que se pode fazer nele.
- Sistema 
	- Execução do softwate, efeito das regras influenciadas pela interação do jogador
- Diversão
	- Resultado final esperado

Ou...

- Mechanics
	- Regras, descrição de componentes do jogo, o que é programado.
- Dynamics
	- Comportamento em tempo real das mecânicas agindo através do que o jogador faz
- Aesthetics
	- Respostas emocionais que são despertadas no jogador quando ele interage com o jogo, ou seja, interage com as dinâmicas
![to do what a game designer does](assets/mda.png)
