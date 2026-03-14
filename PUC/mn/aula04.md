# Métodos Numérios
## [12-03-2026][mvfm]

### Recap de IEEE 754
- Recap da aula passada.
- Controle de exceções comentado por cima, elaborado depois.
- "**Se tiver divisão por '0' pula para uma certa seção de código, tipo jumpTo do visual basic** "

### Limites de representação
- Como passamos dos limites impostos de representação?
- A reoresentação do infinito foi escolhido para deixar bem claro que **algo deu errado.**
- ***Overflow!***
- Underflow comicamente definido como '**Número é pequeno demais e eu não sei mais o que fazer.**'
- E entre os gaps de representação de números? O que acontece caso eu queira um desses números?

### Arredondamento - Bits de guarda
- Bits de guarda são bits **além dos 32 especificados pelo padrão.**
- Servem propósito explícito de arredondamento para cima ou para baixo.
- JB esclarece depois que existem métodos variados, não só esses dois.
- Dependendo da linguagem, o usuário conseguiria determinar **manualmente** que modo de arredondamento ele quer usar, inclusive durante execução.
- Modos 
	1. +infinito
	2. -infinito
	3. Em direção ao [*infinito*] mais próximo
	4. Em direção ao [*zero*]

### Intervalos numéricos
- Incrivelmente, uma história pessoal do JB foi contada pela primeira vez
- Ele e um colega [?de laboratório supostamente] trabalhavam, [?eu chuto] com a representação digital de números irracionais, Pi sendo um exemplo.
- Um certo dia, ele conta, seu colega conseguiu fazer com que a rpesentação de Pi fosse alcançada utilizando intervalos numéricos
	- **Pi está entre : [3,14159 ; 3,141593]**
- Isso foi feito para fazer com que as limitações do padrão IEEE fossem *burladas* para conseguirmos representar *MAIS*.
- Ajuda também que muitos números ainda estamos descobrindo a *quantidades de casas*, então estamos armazenando um número de largura supostamente infinita em um contexto claramente finito.

### Fun fact : Soma de intervalos
[a1, a2] + [b1, b2] = [a1 + b1, a2 + b2]
- Na secção de menor importância (**a1 & b1**) arredondamos para baixo
- Na secção de maior importância (**a2 & b2**) arredondamos para cima.
- Meio que ajuda para '*Não perdemos nada.*'.	
- Mas... trocar o modo em execução parece ser bem custosa computacionalmente...
- '** Primeiro arredondamos todos os 1's para baixo e linhas após isso, arredondamos todos os 2's para cima.**"
- A resposta mais idiota funciona de vez em quando.

### FPU Status Word
- Um registrador escondido dentro do sistema com **5bits de tamanho** não associado à uma variável em específico.
- Um registrador de alerta basicamente.
- E o que o alerta?
	1. Divisão por 0.
	2. Overflow
	2. Underflow
	4. Operação Inválida
	5. Número inexato. (**Quase tudo no universo é inexato. Um número arredondado é um número inexato.**)
- O usuário (programador) só tem o dever de limpá-lo a cada execução, mais nada.

