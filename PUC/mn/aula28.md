# Métodos Numéricos
## [25-06-26] [mvfm]
---
### Sitemas Dinâmicos 
- O nome é '*mais ou menos moderna. Mais ou menos 40 anos.*'
	- Engobla um monte de cenários/situações que não vamos conseguir ver tudo dado o restante do semestre.
	- Vamos falar algo mais simples, que possuem '*Razões históricas e bem profundas. Tendo aplicações na vida real.*'
- '*Equação Diferencial*'
	- O que é, de onde vieram, do que se alimentam?
	- '*É uma coisa até mais boba*' quando perguntado se envolve derivadas. 
	- '*Mas envolve derivadas*'.
- Eu queria encontrar uma função **f(x)**.
	- Que quando eu somar com a derivada dela, a resposta é **x**.
	- $f(x) + f'(x) = x$
	- Uma função de que alguma forma está amarrada com sua derivada.
	- A função em si é a incógnita.
- '*Esse tipo de equação é extremamente comum em situações de mundo real.*'
	- Não se é algo que é muito comum para o pessoal da computação.;
- Um outro exemplo dado é :
	- $g''(x) = cos(g'(x))$
- Sabendo a derivada, como encontramos a função? Integra. 
	- $f'(x) = cos(2x) - sin( tan(e^x) )
	- Mas e se for uma função que se é impossível integrar?
- Dado o exemplo anterior, sabemos que ela é impossível de integrar, o que podemos fazer sobre isso?
	- '*Roubamos no jogo.*' Obrigado Euler.

### $X = 6$
- A única coisa que eu sei sobre a função normal é :
	- $f(6) = 31$
	- Todo o resto, me escapa.
	- Ela concertezam passa ali, $(6,31)$.
- Com isso, eu também sei que eu consigo calcular a derivada dela em 6. Ou seja, sabemos $f'(6)$.
	- Portanto, vou saber a **velocidade de crescimento, movimentação dela**.
- '*Eu posso criar um mecanismo tosco de re-construir a função com isso*', comentou Euler quase cego.
- Andando pouquinho a pouquinho para conseguir perceber como e quando a função está mudando.
	- $x1 = x0 + delta$
	- $y1 = y0 + f'(x0) * (x1 - x0)
	- $y1 = y0 + f'(x0) * delta$
- A partir disso, repita as etapas como pequenos passos.
	- O delta sempre vai ser o mesmo, só para fazer esses baby steps.
- '*Ele não vai encontrar a função para mim. Encontrar ele não encontra, mas ele mais ou menos me entrega o 'shape' dessa função.*'
- É a derivada que me diz se subimos, descemos etc.
- '*Ele está literalmente integrando caso o delta seja pequenino.*'

### Use Your Imagination
- Como são apenas aproximações, $x1$ acumulam um errinho, $x2$ um poquinho mais, $x3$ mais, $x4$ ainda mais etc.
- Como Euler foi o primeiro, esses erros se adicionam drasticamente.
- Euler só redesenha a função, nunca tivemos a função.
- Mas é inevitável que esse tipo de método se perca da função original. É só uma questão de tempo.
	- Não existe almoço de graça.
- Mecânica orbital, equações diferenciais funcionam para prever o comportamento de corpos celestes.
	- Assim como decaímento radioativo, finance etc.
- Euler sendo de primeira ordem, dividindo seu delta por 10, seu **erro é dividido por $10$ também.**
	- De segunda ordem, **seu erro é dividido por $10^2$
	- De oitava ordem, $10^8$.
- Artigo de Yoshida. Método de Verlet.
