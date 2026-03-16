# Projeto de Desenvolvimento de Software
## [16-03-2026] [mvfm]

### O Diagrama Central
- Maneira de como sumarizar um jogo.
![onions](assets/core.png)
- Parece um pouco arbitrário
- Talvez para conseguir descrever rapidamente o principal método de interação do jogador com o jogo.
- Okay vro

### 30 Seconds of Fun
- "**That’s how we make games at Nintendo, though: we had the fundamentals solid first, them do as much with that core concept as our time and ambition will allow**"
	Shigeryu Miyamoto
![vro](assets/miyamoto.jpg)
- Pra explicar '**Game Feel', a 'alma do jogo', Cohen mostra um vídeo do Extra Credits.
- [Is it fucking over.](https://www.youtube.com/watch?v=UvCri1tqIxQ&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
- A ideia básica foi relacionar com o conceito [MVP](https://en.wikipedia.org/wiki/Minimum_viable_product)
- "**O mínimo possível de um jogo que ainda o torna interessante e divertido**."
- [Acho que seria mais legal mostrar alguma coisa dos vidocs da Bungie](https://www.bungie.net/en/Forums/Post/385583)
- Jogadores são chatos, e você também deveria ser.
- Lista de dificuldade :
	- **Corrida**
		- ![Racing](https://www.youtube.com/watch?v=DcyaLDAPVf4&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
	- **Tiro-Top-Down**
		- ![Top-Down](https://www.youtube.com/watch?v=j9HxpB_Z-4A&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
	- **Plataforma 2D**
		- ![Platform 2D](https://www.youtube.com/watch?v=rLl9XBg7wSs&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
	- **Puzzle 2D**
		- ![Puzzle](https://www.youtube.com/watch?time_continue=35&v=EwARSZEPie8&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
	- **Plataforma 2D + Puzzle**
		- ![Platform 2D + Puzzle](https://www.youtube.com/watch?v=UAO2urG23S4&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
	- **Plataforma 3D**
		- ![Platform](https://www.youtube.com/watch?time_continue=202&v=vT3AaQ77ges&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
	- **FPS**
		- ![FPS](https://www.youtube.com/watch?time_continue=8&v=4JVm3IF8Y2I&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
	- **JRPG**
		- ![JRPG](https://www.youtube.com/watch?time_continue=465&v=mz0g9hxq7L8&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
	- **Luta**
		- ![F](https://www.youtube.com/watch?time_continue=465&v=7hZSWtkYN_c&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
	- **Action & Adventure**
		- ![A&A](https://www.youtube.com/watch?time_continue=19&v=pUPJdWe-zVU&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
	- **WRPG**
		- ![wrpg](https://www.youtube.com/watch?time_continue=37&v=BpyibHImmzU&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
	- **RTS**
		- ![rts](https://www.youtube.com/watch?time_continue=261&v=YIL3vhrFSwM&embeds_referring_euri=https%3A%2F%2Fmflash.github.io%2F&source_ve_path=MjM4NTE)
### MVP
- Lista de gêneros de jogos representação da dificuldade de um MVP para cada tipo de jogo.
- Não necessariamente o tipo de jogo mais difícil de se fazer
- Mas o mais chato de perceber se é divertido ou não, de início.
- Várias técnicas :
	1. Papel & Caneta
	2. Wireframe
	3. Prototipação Digital
- Lembrete : **[Fail Faster](https://failfaster.ca/)**
- Protótipos De Papel & Caneta
	- Mais barato.
	- Mais rápido
	- Mais fácil
	- [?divertido fazer]
	- Iteração rápida
- Exemplo mostrado : **Protótipos à papel de Spore.**
![Spore](assets/spore1.jpg)
![Spore](assets/spore2.jpg)
![Spore](assets/spore3.jpg)

### Espaço de Possibilidades
- Define :
	1. Tudo que é possível em um jogo
	2. Tudo que os jogadores podem experimentar
	3. Todos os resultados possíveis
- Ou seja, tudo que é possível fazer dentro do jogo.
- **Muitas possibilidades :**
	- Pode gerar gameplay complexo/confuso
	![complexidade](assets/complexo-complexo.png)
- **Poucas possibilidades :**
	- Pode entendiar rápido demais
	![simplicidade](assets/simples-simples.png)
- O que queremos é algo que vai gradualmente se tornando mais difícil
- Isso se chama **Complexidade Emergente**
![emergente](assets/emergente.png)

### Complexidade Emergente
- Jogos de regras simples que podem gerar complexidade logo após.
- Exemplos : 
	- **Go**
	- Poucas regras, fácil de jogar
	- Possibilidades de jogos são tão grandes que desde sua criação, **Go** nunca teve dois jogos iguais.
	![go](assets/go.jpg)
	- **Portal**
	- Poucas regras, fácil de jogar
	- Eventualmente, cria situações complexas
	![portal](assets/portal.jpg)
- Como se gera tal complexidade?
	- "**Conexão de todos elementos, contexto modificando o resultado!**"
	- Contexto muda! Regras se mantêm.

### Dominância
- **Estratégia Dominante**
	- Uma opção tão boa, que as outras deixam de ser relevantes.
- **Estratégia Dominada**
	- Uma opção tão ruim que não se existe situação válida para usá-la.
- Com o exemplo dado de **O Dilema do Prisoneiro**, a **estratégia dominante** é confessar.
![fucking emojis](assets/dilema.png)
