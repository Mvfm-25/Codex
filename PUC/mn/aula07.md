# Métodos Numéricos
## [24-03-2026][mvfm]
---
### E o que agora
- Vamos ver dois outros métodos
	- E pq dois?
	- "*Pois os dois tem uma conexão bem forte.*"
- O primeiro também começa com dois pontos, não precisando que eles tenham sinais diferentes.
	- Em compensação : *eles saem por aí.*
	- A caixinha do método de bissecção pode ter uma caixinha bonitinha, esse aqui não.
	- Talvez encontre uma raíz que você não queria.
	- Talvez tenha milênios, JB não acredita tanto isso.
		- Justamente por ser bonitinho em gráficos.

### [Método da Secante](https://en.wikipedia.org/wiki/Secant_method)
- O que é uma secante?
	- **"Você sabé o que é uma corda? Não é a que você está pensando.**
![[assets/secantes.excalidraw | 100%]]
- Achar uma reta que passa por esses dois pontinhos
	- Vamos achar essa reta, e achar onde ela toca no eixo.
- Pontos $f(b) f(a)$ são os pontinhos da curva. O pontinho $c$, que está no eixo, deve estar mais perto da raíz.
- Paramos de usar o $f(b)$ para usar o $c$ e encontramos o ponto mais próximo do eixo, o $d$.
	- Repeat ad infinitum achando novos pontinhos.
![[assets/pontinhos.excalidraw | 100%]]
- A função vai andando por aí pois se você escolher que ponto desconsiderar após encontrar o novo ponto, é possível que tu vá lá longe.
- **Nele, não se é garantido encontrar uma raíz.**- 
- Se ele sair passeando, como posso ter confiança para parar?
- Além disso, como encontro o novo pontinho? Como funcionam as contas das retas?
	- Tendo $a$ & $b$, vamos achar a equação da reta se **ancorando** em um dos pontos.
	- $f(x) = f(a)$
		- Parando aqui, o que sabemos?
		- Para todos os valores de $x$, temos um $f(a)$
		- Então não é isso, é só válido para $f(a)$
		- Inclinação toda errada.
		- Sua inclinação deveria ser **o quanto ela muda em y / o quanto ela muda em x**
		- $f(b) - f(a) / b - a$
	- De onde vem essa informação?
	- O quanto mais perto e o quanto mais longe estou de $a$.
	- **$f(x) = f(a) + (f(b) - f(a)) / b - a * (x - a)$**
	- Pra verificar, usa o valor direto do pontos $a$ e $b$. E funciona.
	- Para encontrar **onde bate no eixo x**, vamos ter que achar como fazer $f(x) = 0$. É só uma maneira mais bonitinha de se escrever o $c$ que apareceu no gráfico mais cedo.
	- Ih fudeu.
	- $f(a) (a-b) = (f(b) - f(a)) * -(f(b) - f(a)) * a$
	- Que vira...
	- $x = (f(a) * (a-b) + ((f(b) - f(a)) * a) / f(b) - f(a)$
	- Que vira...
	- $(bf(a) - af(b)) / f(a) - f(b)$
- O programa do JB faz esses encontros de novos pontos umas 20 vezes.
	- Pq 20 vezes? **Pq sim**
	- Poderia funcionar com 500 passos.
- A parte de escolha de qual ponto desconsiderar, $a$ ou $b$, JB escolheu seguir com o de menor função. Assumindo que está mais perto da raíz.
- Como que eu paro com felicidade?
- **Achando uma raíz.** E como eu sei que descobri uma raíz?
	- Quando a $f$ desse novo pontinho chegou numa distância bem pequenina do zero, retornamos como resultado.
	- E esse pequenino? O módulo dessa função menos $10^{-6}$
	- Isso pois ele está levando em consideração os limites do **IEE-754**
- Esse método só acha **uma única raíz**.

### Máquina do Tempo de JB
- Em meados de 1600, se nasce **Cálculo**
	- Punk, altamente disruptivo.
- Com ele, as derivadas vem à vida.
- **Trazendo o pontinho $a$ bem, bem bem pertinho do $b$, o pontinho é praticamente a derivada de $b$, que é praticamente o $b$**
- Ou seja, vamos estar precisando apenas de $b$.
- Com a ideia nova de derivadas, estamos caminhando com apenas um pontinho.
- $f(x) = f(x1) + f'(x1) + (x - x1)$
- Ainda queremos encontrar o $x$ que deixa $f(x) = 0$
- "*Pega, trabalha, faz a festa conseguimos a seguinte fórmula : *"
	- $x2 = x1 - f(x1) / f'(x1)$
- Esse método é melhor que o método antigo? Vantajoso ou desvantajoso?
	- *Normalmente é.*
- Esse método é chamado **Método de Newton**
	- "*Newton nem passou perto desse método.*"
- Caminha na diração das raízes mais rapidinho do que o método das secantes.
- *Costuma* ser veloz.
- Continua saindo à caminhar como o anterior. 
