# Métodos Numéricos
## [01-09-26][mvfm]
---
### No tópico Solução de Equações
- Estamos preocupados em achar raízes de alguma coisa
	- Que pode ou não ser um polinômio.
	- Não tiro vantagem alguma caso seja um polinômio.
- **Bissecção** : Parece muito pesquisa binária
	- É fácil, natural e razoável.
	- Método '*limitado*' ao intervalo que tu deu ao início. Não sai procurando, fica preso dentro do intervalo entregue.
	- Raíz real, retorna apenas uma.
	- Convergência linear. Vai se '*fechando*' passinho a passinho.
- **Secante** : Também para raízes reais.
	- Não é limitado, sai andando.
	- Pega dois pontos x1, x2 na função e traça uma linha reta x3 que conecta ambas. Pega o ponto mais próximo à uma raiz para ser um x3.
	- Ele persegue uma raíz do lado que estiver. A convergência parece ser bem mais rápida. Expoente 1,618 para convergência.
	- O expoente é da **[razão aurea](https://pt.wikipedia.org/wiki/Propor%C3%A7%C3%A3o_%C3%A1urea)**. 


### Método mais sofisticado, mas não **O** mais sofisticado.
- Vantagem extra-plus ultra : Saí atrás de raíz, convergência quadrática & vai atrás de raíz complexas.
- Mais ou menos de **1600's**
- Também só consegue encontrar uma única raíz.
	- **Método de Newton**, mas existe bastante dúvida se Newton realmente trabalhou nele.
- Filho '*direto*' do método da Secante.
- Explicação é simplesmente '*Imagina a Secante, mas num mundo 3d*'
- Traz o X1 tão pra perto do X2 que todos os três (X1, X2, X3) são baaaaaaaaaasicamente a mesma coisa.
	- Essa reta vai se transformando no que? Da derivada
- Tu simplesmente encontra a dervidada de determinado ponto, que o JB está chamando de '*a*' agora em direção às raízes.
- É negócio que só tem vantagens.
	- O que incomoda é : o cálculo de derivadas.
- O nome tradicional de '*a*' é '*x0*', teu próximo passo é '*x1*'
- $Xi+1 = Xi - f(Xi) / f'(Xi)$
	- $f'(x)$ é a derivada.
