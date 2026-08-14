# Métodos Numéricos
## [06-08-26][mvfm]
--- 
### Ventos 90km/h
- Primeira aula de métodos numéricos no novo semestre marcada por um alerta vermelho de tempora com ventos de 90km/h.
- Imagina ficar preso na universidade devido uma crise metereológica.
- '*Pessoal teve pitis e saiu correndo.*'
- IEE 754 novamente!
	- Saudade, na real.
	- Lida apenas com armazenamento em binário, criado em 1985.
- Seguido por IEEE854, para qualquer outra base. Multi-base.
	- Depois revisado em 2008 que deu uma ajeitada em algumas coisas.

### Como queremos guardar números no computador?
- BOm... Não sei.
- Mas precisamos tratar com vários tipos de números, grandes pequenos, negativos, positivos etc.
	- Para isso, vamos nos basear na notação científica.
	- Exemplo : $6,02214x10^23$
	- Nele, temos o número quebrado de fato na frente, vezes uma base em um expoente. Por isso, temos um número com 23 zeros depois da vírgula.
	- Ele é um número GIGANTE.
	- Simplesmente colocando o expoente como negativo, estariamos lidando com um número MINÚSCULO.
- No computador, temos tais elementos :
	- **Mantissa** : Parte quebrada do número.
	- **Expoente** : Pra ter sentido de escala
	- **SInal** : Se explica.
- Não vamos guardar a base pois, como estamos trabalhando em um computador, a base sempre vai ser **2**.
- O padrão se adapta para tipos diferentes, float, double etc.
	- No exemplo de float (32bits) ele é quebrado de tal maneira :
		- 1 de sinal
		- 8 de expoente
		- 24 de mantissa.
	- Estranho não? Bizarro, não?
- Não tem sinal no expoente, apenas para a mantissa. Bizarro, não?
- Tem um motivo para o expoente aparecer primeiro, diferente da notação científica.
	- Por que?
	- Pegando desse jeito, o float, tendo 4 bytes conseguimos olhar para ele como se fosse uma string de 4 char
	- Ordenar float é a mesma coisa de ordenar uma string de 4 char.

### O que o padrão fala
- Lidando com o IEEE 754, conseguimos ter +0 & -0.
- Obviamente, tratando ambos como um simples zero.
- O que acontece com $1 / 0$?
	- IEEE retorna com INFINITO. Ou 'inf' como ele escreve na tela.
	- Que também vem positivamente ou negativamente.
	- INFs chegam com todos os bits do expoente ligados.
- Temos NaN também. JB conseguiu um '-NaN' dividindo 0/0.
	- NaN também vem com os dois sabores.
	- NaN chega com todos os bits do expoente ligados também, e pelo menos um ligado na mantissa.
- '*Tem muita inteligência nesse padrão.*'

### Vamos fazer um resumo
- '*Pq no resumo realmente vamos aprender como esse negócio funciona.*'
- O que é um zero?
	- Tudo zerado, com a talvez exceção do bit do sinal.
- O que é um infinito?
	- Expoente todo ligado, mantissa toda zerada.
- O que é um NaN?
	- Expoente todo ligado, pelo menos um bit na mantissa ligada.
- Cara padrão :
	- Uma casa antes da vírgula, todo o resto depois da vírgula.
- O primeiro um do número sempre vai ficar antes da vírgula.
	- Pra não ficar com tantos zeros antes da parte verdadeiramente *importante* do número.

### Que surpresa?
- Sempre guardando com um '*1*' na frente, nem precisa guardá-lo!
	- Número normalizado, esse arrumadinho com o '1' escondido.
	- O que implica na existência dos números sub-normalizados. Aqueles que não conseguem ser normalizados.
- '*Muitas mais algumas coisas! Mal estamos começando com esse padrão!*'
- A subtração de 127 do expoente.
	- Antes de usar, tire 127. Quando guardar, adicione 127.
	- Por que? Por causa daquele negócio esquisito da ordenação bizarra por strings.
