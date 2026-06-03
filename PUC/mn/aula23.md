# Métodos Numéricos
## [02-06-2026][mvfm]
---
### Interpolação
- Tenho quatro pontinhos que os consegui rodando um experimento, não são tão parecidos meio aleatórios
	- Não consigo coletar mais desses pontinhos por $n$ razões.
- JB continua o exemplo com o contexto de 'movimento de corpos celestes'. Ele coletou a informação de tal maneira que vai ser muito difícil ou impossível de se replicar.
	- Mas o JB quer ter uma estimativa de quanto seria 'o valor correto adequado.'
- '*Interpolação é uma estimativa para uma coisa que não estão nesse conjunto de dados.*'
- O '*Inter*' de interpolação significa entre. Existe também '*Extrapolação*', dados que não tenho nem uma base matemática pra isso. Algo que o JB considera perigoso.
- "*Eu tenho um conjunto de informações, quero ter uma estimativa para algum outro valor que tenho por aí.*"
- JB menciona interpolação de Splines, um método que vimos em CG. Aqui em MN não vamos usar Splines, aqui vamos fazer matemática pura. O mesmo grau de dificuldade, não muda muito.
- Qual o meu problema? Eu queria ter estimativas para pontos que não estão contidos no dataset original.
- Vamos achar uma função que passa pelos pontinhos que já temos. Isso vai nos dar uma estrela do norte.

### North Star
- Temos que usar apenas o que temos.
- Queremos uma função que passe **exatamente** pelo que temos.
	- Que tipo de função gostaríamos encontrar? A mais fácil possível. **Polinomial.**
	- Podemos escolher o grau para tal função. Qual o grau? $3$. 
	- Não é muito claro que deveria ser três. Mas o JB escolheu.
- Caso tivéssemos dois pontos, usaríamos uma função de grau $1$. Caso três pontos, grau $2$. 
	- Para passar nos quatro pontos, teríamos que usar uma função de grau $3$. Isso é uma regra, não escolhemos ou decidimos isso.
- Caso um único ponto, teríamos um polinômio de grau 0. Uma constante.

### Matematizando com Newton.
- Para encontrar a fórmula de uma reta, a matemática tem uma maneira preferida desse maneira
	- Existe uma reta que conecta os pontos (2,3) & (4,5). Para criar a reta usamos a fórmula : $p(x) = 3 + a * 2$, onde as coordenadas (x,y) do primeiro ponto estão sendo usados como 'âncora' para os novos valores.
	- **Alpha** seria o ângulo de inclinação entre cada ponto. Neste caso, com apenas esses dois pontos, encontramos o **Alpha** da seguinte maneira :
		- $p(x) = 3 + (5-3)/(4-2) * (x-2)$ que retorna : $3 + 1(x - 2)$
- E agora, com três pontos, como encontramos a parábola que se encontra corretamente com os pontinhos que temos?
	- Conseguimos preservar o que já temos, a reta, simplesmente fazendo uma '*segunda reta*'. 
	- Isso não é uma parábola, mas é barato de se fazer e conecta todos os pontinhos.
		- O terceiro pontinho está em **(7,4)**.
	- Considerando as diferenças entre o primeiro e o segundo e o segundo e terceiro ponto, e depois disso a diferença entre diferenças o JB conseguiu :
		- **$p(x) = 3 +1 * (x-2) - 4/15 * (x-2) * (x-4)$**
- JB comenta que uma das vantagens do método de Newton é o não precisar de espaçamentos iguais assim como outros métodos.
- A cada novo ponto adicionado, repetir o processo.
	- O p(x) está ficando cada vez mais feio.
- O que o JB escondeu é que os pontos que nos foram dados eram contínuos. Ou seja, um '*seguia*' o anterior.
	- Mas o que ele comenta é que mesmo que esteja '*entre*' as informações anteriores, o método de Newton lida com isso.
