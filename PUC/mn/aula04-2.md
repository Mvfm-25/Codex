# Métodos Numéricos
## [13-08-26][mvfm]
---
### Back at it
- Continuamos com IEEE754, eu presumo.
- Tanto pelo o que eu lembro da [aula 02](./aula02-2.md), na qual o JB queria entrar mais em específicos do comportamento do protocolo.
	- Good on ya, for missing out on **aula03**.
- Wide ainda não apareceu. Talvez nem vá aparecer mais, acho que ele já conseguiu mudar de turma.

### O que aconteceu na aula passada
- Bits de exceção, 5 bits : 
- '*Usuário só pode zerar, e depois perguntar se algun bit foi levantado.*'
- Quatro arredondamentos :
	- Para o zero
	- Para o infinito positivo
	- Para o infinito negativo
	- Para o número mais próximo.
- As exceções que são os de fato 5 bits
	- Divisão por 0
	- Overflow - Responde infinito, e liga o bit de overflow.
	- Underflow
	- Operação inválida
	- Número inexato
- Tem um 'só que' :
	- Conta que resultava em um número abaixo do último número normalizado '*o último possível*'
	- Mas que ainda assim saiu um número. Como?
	- Qual o menor número de um float? $10^{-38}$
- Por que agora estamos lidando com números normalizados?
- Tendo um expoente todo zerado & uma mantissa toda zera : isso é apenas um zero.
	- Agora, com o expoente zerado, mas a mantissa não zerada ela é : **sub-normalizada**. Numeros sem o bit implícito.
	- Existem justamente para preencher aquele vazio que os números normalizados deixam quando perto do 0.

### Perguntas da Aula Passada :
- Como posso ter um resultado concreto no binário se tal espaço não é representado pelo IEEE?
	- Qual a resposta?
	- O número que não deveria existir, ele veio de alguma conta. Como que funciona com o processador de IEEE?
	- Ele vai fazer uma conta, ele recebe um float de 32 vezes um outro float de 32.
	- O resultado vai ser outro float de 32.
	- Sò que o padrão diz o seguinte : Você PODE/DEVE fazer a conta que te pediram num registrador com casas à mais. Um número bizarro de **80 bits**.
- Por que usamos os casos de arredondamento que usamos no IEEE?
	- '*Ter esses arredondamentos não é tão pavoroso assim.*'
	- Para o processador é relativamente tosco. Por mais que eu não saiba como fazer isso.
	- Mas qual a utilidade disso?
	- Intervalos. Voltamos para intervalos.
	- A multiplicação entre dois intervlos TEM que resultar em outro intervalo. Três incertezas.
	- Como se multiplica intervalos? Temos que pegar o MENOR POSSÌVEL e o MAIOR POSSÍVEL.
	- Menor com Menor dá em O MENOR POSSÍVEL & Maior com Maior dá em o MAIOR POSSÍVEL.
- '*O mundo float é bem desagradável*'

### Na minha linguagem preferida
- Acabei de criar um float : **EPS = 1.0**
	```code
		Enquanto 1.0 + EPS > 1.0 :
			print("Oi!")
			EPS = EPS/2
	```
- Roda para sempre? Ou para eventualmente?
- Eu acho que para, justamente pelo comportamento de 'shiftar para a direita'. Eventualmente vai ficar sem nada para shiftar.
	- E foi justamente isso,
	- Dividir um float pelo IEEE é simplesmente REMOVER um bit do expoente.
	- Por isso que eventualmente não temos mais nada para tirar.
- Mas o bit ainda tinha bastante coisa para tirar no número que o JB tava mostrando.
	- Então é outro motivo...
- Por que o que eu achava estar acontecendo com o 1, está acontecendo de  fato com o EPS?
	- É um pouco mais complicado...
