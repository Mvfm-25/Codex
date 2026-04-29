# Métodos Numéricos
## [23-04-2026][mvfm]
---
### Atividade
- Estamos voltando para a aula com a situação do **planeta Zorg** mencionada semana passada.
- Estamos controlando Lemmings basicamente em um labirinto perigoso & extremo.

### Lemmings
- Na situação mais simples : $%A*$, nosso Lemming infeliz tem 50% de se fuder muito ou de dar tudo certo. Considerando que :
	- Estamos no planeta Zorg, que se parece muito com uma matriz de caracteres
	- Nossos lemmings só se movem no **Norte, Sul, Lest & Oeste**.
	- Nos caracteres *.*, nossos lemmings podem passar o tempo. Nada acontece.
	- Nos caracteres *#*, *%* eles **MORREM**.
	- Nos caracteres *$*$* eles atingem felicidade eterna.
- Após a conclusão da passeada do Lemming (dada morte ou felicidade eterna), outro Lemming aparece nesse labirinto eterno da tortura.
	- Implicitamente, tendo as mesmas porcentagens.
- E se o Lemming for muito burro e repetir péssimas decisões
- **JB** anota que na situação específica **$%..A*$** ele menciona : 
	**75%** de felicidade total
	**25%** de morte.
- JB mostra em representação de máquino de estados, assim como Wide.
- JB rodando seu programa de fato utilizou da eliminiação de **Gauss**.
- Seguindo no cenário 02 %..A* temos as seguintes chances :
	- A = $%1 + B/2$
	- * = $A/2$
	- a = $b/2$
	- b = $A/2 + a/2$
	- % = $a/2$
