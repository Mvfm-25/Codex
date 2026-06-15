# Métodos Numéricos
## [11-06-2026][mvfm]
--- 
### Otimização
- JB comenta que a '*otimização*' que vamos ver não é o mesmo conceito de '*otimização*' vista em [POA](PUC/poa/poa-index.md)
- Otimizar é : '*encontrar os valores mais baixos & altos de uma função?*`
	- é mencionado que ambas essas perguntas são a mesma, mas entregadas de sabores diferentes. '*-f(x)*'.
	- '*Me dá o valor específico naquela área específica da função.*'
- E se uma função tem **4** empates em o ponto mais baixo? Quatro pontos de mesma altura.
	- Só conseguimos ver que existem esses quatro pontos vendo pelo meio gráfico. Dada a função simplesmente, como eu tenho certeza que eles existem?
- Aparentemente é um problema que a Física enfrenta frequentemente.
- O método que vamos ver nos retorna uma única resposta. Se vira.
	- Vamos ver outro futuramente que o JB aparentemente gosta bem mais, nos retornando **todos** os mínimos. Computacionalmente mais pesado.
	- '*Quase desconhecido.*'
- '*Ótimo no sentido matemático é o MELHOR valor possível.*'
	- '*Dentro de dado escopo.*'

### Método que todo mundo usa
- **Método do Gradiente Descendente.**
	- O que é um gradiente?
		- '*Algo que tá amarrado à uma função. Toda função tem um gradiente.*' 
		- '*Ele é um vetor amarradinho à uma função.*'
- $f(x,y) = cos(sin(x) + 5 + x * y)$
	- Essa função tem duas variáveis e não retorna um vetor. Ela retorna um valor único.
	- O gradiente tem como símbolo um triângulo virado de cabeça pra baixo. **Ele** é um vetor.
	- Tendo **duas** variáveis, o vetor tem tamanho **dois**.
	- Ele é uma coleção de derivadas. A derivada de **x** e **y**.
	- $(df / dx, df / dy)$
- Um jeito infalível é derivar à mão e simplesmente usar no programa hardcoded.
	- Pode não ser divertido ou prático, mas é possível.
- E o que fazemos com um gradiente? JB comentou que IA's usam, mas como e porque?
- Ele mostra um gráfico mostrando ondinhas, montanhas e fala que é um Gradiente. Tri-dimensional.

### Pensa Que Aquilo É Uma Montanha.
- '*Sei que um jeito depressa de descer aquela montanha é rolar na montanha.*'
	- Tendo neve vai, tendo pedregulhos afiados nem tanto.
	- Schneider foi jogado à montanha.
- Não tendo a visão global da motanha como nós, Schneider tem um campo de visão limitado.
	- Caindo, sua derivada vai ser negativa. Alimentando seus pontos **x, y, z.**
	- Subindo, sua derivada é positiva. 
	- Em um vale, sua derivada seria 0. Não que não exista, mas seria 0.
- A gradiente descendente é simplesmente a gradiente, com o sinal contrário.
	- Ao invés de apontar para a direção em que ele sobe mais depressa, Schneider vai estar apontando para a direção que ele desce mais depressa.
- Schneider continua fazendo até as derivadas zerarem. Em um vale.
- Mas isso não garante que ele chegue no ponto **mais** baixo da montanha. 
	- É um ótimo local, não global.
- '*É muito ruim de desenhar isso*'
- Essencialmente, o que estamos descobrindo é :
	- **Schneider** é largado em um ponto **P1**.
	- Queremos mandá-lo para **P2**.
	- Descobrimos P2 por : **$p2 = p1 - gradiente$**
	- Mas a gradiente pode ser desconfortavelmente LONGO.
	- Para isso, multiplicamos o gradiente descendente para uma fração pequenina.
	- baby steps. A direção que o gradiente nos dá é o que realmente importa.
- '*Parece Newton*'
	- Deixo de ter a vontade de me mexer quando der zero.

### Para Criar o Caos

