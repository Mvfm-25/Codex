# Métodos Numéricos
## [17-03-2026][mvfm]

### O após o IEEE 754
- O que veremos agora é incerto.
- JB roda um pequeninho programa em C que roda uma renderização 3D de Voronoi?
- Parece um programa de POV-Ray
- É bem bonito.
- "*Sem nenhuma preocupação de erro de arredondamento.*"
	- "*A matemática está correta, mas ele leva em conta que os números não são perfeitamente análogos para o mundo real.*"
- A versão que ele roda, levando em consideração que **IEEE 754** é uma aproximação, o render fica bem mais bonito com bem menos *noise*.
- Como solucionar um problema que você não tem certeza que está errado?

### Polinômios
- Qual o motivo de falar de polinômios?
- "*Polinômios são amigos, são fofinhos.*"
- O que é um polinômio?
	- **$p(x) = a[m]^n$**
- Polinômios são fáceis de resolver, extremamente previsíveis.

### [Série De Taylor](https://pt.wikipedia.org/wiki/S%C3%A9rie_de_Taylor)
- Para pegar uma função que não é um polinômio e criar um *faux-polinômio* para deixá-la mais fácil de trabalhar
- Como se imita um polinômio?
	- *Onde quero imitar?*
	- *O quão bem quero imitá-la?*
- Gráfico está imitando bem no **$0$**.
![taylor series](assets/taylor.png)
- O gráfico também mostra o quanto matemáticos **GOSTAM** de polinômios.
- Integrar é bem fácil, derivar é bem fácil. *Quase* tudo com polinômios é bem fácil.
	- **Achar suas raízes(zeros) não é fácil.**
	- Mas eu sei de outras coisas!
- O grau de um polinômio é o elemento de maior expoente.
	- O que isso me ajuda?
	- **Isso determina quantas raízes ele vai ter**.

### [Évariste Galois](https://en.wikipedia.org/wiki/%C3%89variste_Galois) e o Quinto Grau
- Como aprendemos para encontrar as raízes no médio?
	- Max comenta que primeiro igualamos à zero e depois testamos certos valores para chegar à isso.
	- Outro aluno comentar que encontramos usando Baskhara.
- Então qual o problema de encontrar as raízes?
- $x^2$ é fácil. $x^3$ é um pouco mais difícil. Grau quatro piora, mas também temos fórmulas para resolver.
- Em meados de 1820, três ou quatro caras ao mesmo tempo ( que de acordo ao JB são mais ou menos iguais, que morreram de maneiras terríveis ) comprovam que para **grau 5** & acima, **uma fórmula não se é possível.**
	- Simplesmente impossível. You've gone adn busted my good man.
- [?Finni], [?Abbel], **Galois** e outro cara que JB se esquece.
	- Ele consegue ver o retrato, mas não consegue se lembrar do nome.
- **Galois** é um revolucionário francês na época pré-Napoleão.
	- Na prisão, ele se apaixona pela filha do diretor da prisão
	- Ela não se importa.
	- **Galois** é liberado, mas quando alguém comenta algo ruim da guria, **Galois** marca um duelo com o cara que fez isso.
	- Na noite anterior, ele anota todas suas descobertas matemáticas, por medo de morrer.
	- Nisso, ele **prova** a fórmula de quinto grau é impossível.
	- Ele morre no duelo.
	- O papel é perdido. Pois o cara que deveria entregar as anotações **simplesmente esquece.**
- A aula mais calma de JB.

### Brincando com Números
- JB mostra e visualiza a fórmula de um polinômio de quarto grau, cujas raízes são **imaginárias**.
	- **$p(x) + x^4 + 6x + 10$**
- Diminuindo o elemento **$10$**, você vai chegando cada vez mais próximo às raízes reais.
- Descendo, descendo e descendo é possível encontrar as quatro raízes?
- O que é um número complexo?
	- Raíz de número negativo
	- '**$z$**' é normalmente complexo
	- Formado por parte real e uma parte imaginária.
	- **$z = 3 + 5i$**
- Como se coloca isso num eixo?
- Não se coloca.
- Pra isso criaram o plano complexo : eixo $x$ é a parte real, eixo $y$ é a parte imaginária.
![[assets/complexo.excalidraw | 100%]]
- Contas com números complexos, resultam em números complexos?
- Cada pontinho no plano complexo, se é associado a outro pontinho. "*Isso é enlouquecedor*"
- "Enxergamos o plano complexo 'deitadinho"
	- Huh?
	- Tri-dimensionalidade? Simplesmente isso?
- Essa outra 'uma' nova direção, permite melhor representação disso?
- Tirando o módulo desse número complexo, vira um número único.
	- **$p(z) = 8 - 6i$ -> $\sqrt{64 + 36} = 10$**
	- **$10$** sempre será positivo ou será **$0$**.
	- Quando que ele pode ser zero? Quando ele é uma raíz. **Só** quando ele for uma raíz.

### E agora?
- JB comenta que na próxima aula, veremos como encontrar as raízes para números reais.
- Os programinhas de visualização desses números complexos são bem bonitos e divertidos.
	- O resultado de um deles parece um sapinho com as quatro raízes imaginárias.
- "**Sou um Deus né? Impressionante.**"
- A ideia do **Wide** de simplesmente 'baixar' como baixamos, reduzindo o elemento de menor grau, conseguimos encontrar as raízes reais. Passo a passo, lentamente.
	- Tínhamos 4 raízes imaginárias, passa a passo, conseguimos 2 reais e 2 imaginárias
	- Em um milonésimo de segundo, 2 raízes imaginárias se tornam '*uma*' real.
	- JB desenha o paralelo com as raízes $-x +x$ de Baskhara.
	- "**Zero duas vezes!**"
- "**O mundo complexo é muito mais descolado.**"
- Polinômio de grau ímpar, se garante uma raíz real. Par não se tem essa certeza.
- **Descartes** mencionado!!!	
	- Descartes e sua regra : $6x^8 - 4x^7 + 5x^5 + 4x^4 + 12x^3 - x$
	- Tendo esse polinômio, queremos quantas raízes positivas ele tem.
	- positivo, negativo, positivo, positivo, positivo & negativo.
	- Quantas trocas de sinal ocorreram? Três.
	- Então esse cara tem **três** raízes positivas... Ou esse número '**desce de duas em duas.**'
	- Tendo a segunda opção, ou ele tem apenas **uma**.
- Porque desce de dois em dois?
	- Quando duas raízes reais somem ( mergem ), vira uma complexa.
	- Quando tu não consegue ver os complexos, elas simplesmente somem.
- Descartes ainda não via os complexos.
