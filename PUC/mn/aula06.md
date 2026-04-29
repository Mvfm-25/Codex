# Métodos Numéricos
## [19-03-2026][mvfm]

### Recap aula anterior
- Começando lembrando o JB do polinômio da aula passada 
	- $p(x) = 6x^8 - 4x^7 + 5x^5 + 4x^4 + 12x^3 + x$
	- Raízes positivas : **3, 1**
	- Raízes negativas : **4, 2, 0**
- Isso se descobre usando a regra de **[Descartes](https://pt.wikipedia.org/wiki/Regra_dos_sinais_de_Descartes)**.
- Lembrando que ele só está seguindo o mundo de *reais*. Os complexos ainda não faziam parte do contexto dele.
- JB comenta que encontrar as **raízes em específico** é difícil.
- Muito se é incerto com os polinômio de acordo com Descartes.
- Mais alguma pergunta sobre as raízes?
	- **Intervalo**?
		- "*Mais ou menos estão aqui dentro.*"
		- Por fora não estão.
		- Denominadas *Cotas*. Em inglês *Bounds*.

### Cotas / Bounds
- Vamos ver específicamente **duas** cotas.
- Pois são calculadas de meio diferentes que resultam em números diferentes.
- Existem meios mais modernos, mas são bem complexos.
- O que eles usam?
	- **Os próprios números do Polinômio.**

### [Cota De Lagrange](https://wp.ufpel.edu.br/nucleomatceng/files/2012/08/Calculo_Numerico_vol1.pdf)
- "*O maior desses números*"
- $max { 1, Soma{ n - 1 i = 0 |Ai / An|$
	- $n$ é o grau. 
	- Quem é $a$? Quem é &An&? Se $n$ é o grau... $An$ seria seu coeficiente : $6$.
	- $Ai$ seria o coeficiente de todos os outros, de acordo com a etapa.
- No nosso exemplo : **$|1/6| + |12/6| + |4/6| + |5/6| + |4/6|$**
		- $26 / 6 =  4,3$
- O que ela nos entregou?
	- Um float.
	- O que fazemos com ele?
		- Temos ele positivo e sua versão negativa.
		- As tuas raízes vão estar entre esse intervalo. No exemplo $-4,3$ & $+4,3$
- Ele **tem muito mais poder**, como JB descreve.
- Esse polinômio tem suas raízes, *todas elas*, dentro desse intervalo.
- JB não sabe se importa se os intervalos são abertos ou fechados.

### [Cota de Cauchy](https://amatematicapura.blogspot.com/2014/08/equacoes-funcionais-equacao-de-cauchy.html)
- Outro matemático francês.
- Ele também usa os mesmos coeficientes, mas resulta em algo diferente.
- Ambos continuam corretos, incrivelmente.
$1 + $ max { $|1/6|, |12/6|, |4/6|, |5/6|, |4/6|$ } $ = 3$
- Com isso, temos um **3 direto**, redondinho. Foi coincidência, só por acaso.
- "**Cauchy entrega um número mais apertado**".
- Não se é garantido que Cauchy sempre entregará um intervalo menor.
	- "**Tem boas chances, mas não se tem garantia.**"
- Cota de **Fujiwara** é mencionada.
	- Os ingredientes do bolo são os mesmos.
	- Mas cada número tem um expoente diferentes, algumas etapas à mais adicionadas. Outra cota apertada, bem preciso.

### Rodando no Note do JB
- **Fujiwara** voltou $2,29$.
	- Fechou **BEM** mais.
- JB não faz a mínima ideia de como o matemático conseguiu isso.
- E agora? Como encontramos propriamente as raízes?
- **O método mais bobalhão de todos**
	- Já aprendemos ele em outro lugar.	
	- Bem antigo, mas é fácil, tranquilo. Relativamente **vagaroso**.
	- Serve apenas para encontrar as raízes reais, não as complexas. Mais ou menos devagar.
	- Ainda tem uma dificuldade extra : **Só é capaz de achar raízes que um lado da raíz tem um sinal, do outro o contrário.**.
	- Ainda tem que ter informações iniciais. Um início tem que ser lhe entregue.
	- Só não sabemos que sabemos. 
	- Serve para outras coisas além de polinômios.
- Colega informa que ele vai simplesmente encontrar por meio de **busca binária**, levando em consideração que o retorno é simplesmente uma ** única raíz.**
- Funciona bem como busca binária, a única coisa que ele vai perguntando é o sinal.

### Busca Binária
- JB exemplifica rodando o seu código C que esse método de selecionar pontos $a$ & $b$ subjetivamente para ir cortando no meio, leva é meio que um *bias* para o quão longe ir para encontrar a raíz.
- Pontos $a$ & $b$ já devem ser previamente encontrados.
- "**Cada um tem seu próprio conceito de bem apertado.**"
- Ridiculamente simples, calcular o meio é literal $(a + b) / 2$
- Se o meio tiver o mesmo sinal que um dos dois limites, um novo limite foi encontrado para encontrar um futuro meio.
- Em computação, e seus propósitos, ele é super eficiente. Mas pra matemática ele é bem lento.
	- **I know right**.
- A notícia ruim é que **precisamos dessa informaçãozinha à mais** de encontrar o $a$ & $b$ respectivamente.

### Jeito mais inteligente de se escrever um polinômio
- Continuando com o exemplo anterior, mas agora com um termo independente adicionado.
	- $p(x) = 6x^8 - 4x^7 + 5x^5 + 4x^4 + 12x^3 - x + 10$
	- **Horner** : $p(x) = 10 + x(-1 + x(0 + x(12 + x(4 + x(5 + x(0 + x(-4 + x(6))))))))$
	- Coloca o $x$ em evidência, escrevendo ao contrário. 
- [Briot-Ruffini](https://mundoeducacao.uol.com.br/matematica/dispositivo-pratico-briotruffini.htm) envolve divisão de expoentes, cortando raíz à raíz para não tropeçar na raíz anterior. 
- Resumindo, tu sempre vai encontrar uma nova raíz à cada vez.
- Não necessariamente implica em simplesmente encontrar *sempre* raízes reais
	- Caso tu encontre uma raíz complexa, tu só não vai conseguir ver.
- Tem acúmulo de erros de acordo com as divisões erradinhas para encontrar as novas raízes.
- O que pode trazer um pouuquinho de maior segurança, re-avaliando se a nova raíz encontrada **ainda é** raíz do cara lá de cima.
- Bem intuitivo.
- Infelizmente, só serve para polinômios. Mesmo o JB tendo o denominado como bem legal.
