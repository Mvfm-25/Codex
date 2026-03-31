# Projeto & Otimização de Algoritmos
## [24-03-2026][mvfm]
---
### Camponeses Russos
- Algoritmo russo (**duh**)
- Caracterizado pelo **JB** como : 
	- "*Um algoritmo simples para pessoas simples e sem educação*"
	- Sem educação no sentido acadêmico mas puta que pariu quase morri.
- **Karatsuba** indiretamente mencionado mas como um preview do que a gente vai eventualmente conversar sobre.
- Nada muito claro, de novo só descrito como *Outro* algoritmo russo.
- O algoritmo funcionava, principalmente, para trocas. Multiplicação sendo seu principal foco.
![[assets/russo.excalidraw | 100%]]
- "**Fantástico pois se sustenta em operações bem simples**"
- Se é comentado que pra **assembly** é batata.
	- Como se sustenta em multiplicação e divisão por dois, essas operações são apenas um shift para lados diferentes.
- "**Talvez não seja o melhor no geral, mas é bem divertido!**"
- Mas e funciona?
	``` a = 2, b = 2 
	r = 0
		enquanto 2 > 0
			se 2 for impar
				(nao e)
			a = 2 * 2 (4)
			b = 2 / 2 (1)
	r = 0
		enquanto 1 > 0
			se 1 for impar
				r = 0 + 4
			a = 4 * 2  (8)
			b = 1 / 2  (0)
- Resultado volta $4$
- Então funciona!
- Mas porque funciona?
	- Muita gente da sala agora está mencionando que anda bem rápido
	- Tira logo de cara muitas multiplicações
	- 
