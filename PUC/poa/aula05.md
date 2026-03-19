# Projeto & Otimização de Algoritmos
## [18-03-2026][mvfm]
---
### Função da aula passada
- Potenciação de $x$ em $n$ vezes, uma operação linear.
- O que viram aula passada foi a maneira mais *linear* de fato
- Simplesmente um pequeno for que faz *cada operação individualmente uma de cada vez*.
- Sem dúvidas, a maneira mais lenta.
```
power(x, n):
	r = 1
	para i = 1 a n
		r = r * x
	ret r
```
*notando que o J.B. escreveu em notação matemática, fazendo com que o laço iniciasse em $1$ e não $0$*
- De acordo com sua promessa feita aula passada, **Wide** vai para o quadro defender o que ele acredita ser a prova que seu algoritmo funciona.

### Wide's Theorem
- Primeiramente, ele estabelece que :
	- "*Em caso de $0$, o algoritmo não funciona. Justamente por sempre retornar $1$.*"
- O que queremos fazer?
	- **Queremos diminuir a quantidade de operações necessárias para potenciação.**
	- Ou seja : de $2¹⁰$ -> $x²$
	- Tal limite foi imposto pois $x^2$ é o mínimo possível (dentro deste algoritmo) para potências.
- Re-utilização de reusltados também foi mencionado pela primeira vez nesse teorema.
![[assets/wide1.excalidraw | 100% ]]
- Sala surpreendentemente quieta para uma turma de 60
- Um real diálogo, J.B. deve estar adorando.
- Casos especiais determinados pelo **Wide** foram : **Ímpares, Pares & quando a divisão resulta em números menores que 2.**
- A ideia geral segue bem com os princípios de **Divisão & Conquista**.
	- Tarefona divida em mini tarefinhas.
	- Depois da divisão, resolve as pequeninhas
	- Monta tudo de volta depois.
![[assets/wide2.excalidraw | 100%]]

### Casos Especiais
- *Para quando $expo / 2 < 2$*
$(Xf^e) / Xi$
- *Para quando $expo / 2$ ímpar*
$(Xf^{e / 2}) * Xi$
- *Para quando $expo / 2 par$*
$(Xi * Xf)^e$
- J.B. passa um tempinho explicando que o **Wide** fez foi a própria ginástica mental que ele tanto menciona nas outras aulas.
- **Wide** menciona que passou 2h escrevendo o que ele escreveu.
- O que o J.B. adiciona é que : 
	- "*Isso não é uma ideia nova, esse problema já foi resolvido anos décadas séculos atrás.*"
	- "*Tenho uma pequena carta na manga que simplifica tudo isso.*"

### Formalização
- O que sabemos de potências?
	- Propriedade 1 : $a^b$
	- Propriedade 2 : $a^b * a^b = a^{2b}$
	- Propriedade 3 : $a^7 = a * a^6$
	- Propriedade 4 : $a^6 = a * a^3 * a^3$
- Mesma ideia que o **Wide**, mas um pouquinho mais organizado,
- Certo, agora sabemos que as propriedades existem, mas como podemos usá-las?
- J.B. escreve a propriedade recursiva no quadro :
![[jbr.excalidraw.png | 100%]]
- Computacionalmente, a **propriedade 3** está correta.
- Considerando apenas as propriedades matemáticas puras, estaria errado. 
