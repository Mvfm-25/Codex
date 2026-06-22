# Métodos Numéricos
## [18-06-2026][mvfm]
---
### Aula passda
- Acabei me esquecendo de salvar o arquivo da aula passada verdadeira e com os pulls do repositório fui perdendo ele.
- Ao menos tenhos os [slides](https://moodle.pucrs.br/pluginfile.php/5758285/mod_resource/content/1/apres.pdf) disponíveis pelo Moodle.
	- JB mostra o que compiladores de maneira bem inteligente
	- Ao invés de ter que realizar/calcular uma cálculo completo & complexo, dividimos em pequenas secçõeszinhas para resolvé-las individualmente. Bem rapidamente.
	![Gradiente Progressivo](assets/progressivo.png)
- Hoje, veremos :

### De Forma Regressiva
- Vamos fazer o mesmo, ao *contrário*.
- O que faziamos é : **calcular as derivadas com relação à cada passinho.** Sempre pensávamos de maneira individual.
- Vamos tirar esse vetor.
	- Temos as formulinhas e cada passinho. Mas o vetor agora é **um único vetor**. Um float. **Só**.
- O que é esse float?
	- Exemplo : $f(x, y) = cos(x^2 + y) / y$
	- Quanto vale a função em tal lugar? Qual o gradiente em tal lugar? As mesmas perguntas de antes.
- Continuamos quebrando em pedacinhos, dessa vez não tendo constantes :
	1. f1 = x = 4
	2. f2 = y = 2
	3. f3 = f1 * f1 = 16
	4. f4 = f2 + f3
	5. f5 = $cos$(f4)
	6. f6 = $f4 / f2$
- O float é : **A derivada da função com relação a um passo específico.**
![Método regressivo](assets/regressivo.png)
- Mas e como começamos tudo isso? Sabemos de algum número?
	- '*Só tem um cara possível*'
	- Quem?
	- $F6$. Ele seria $F6$ pela derivada de $F6$. 
	- Ou seja : **1**.
- Por isso que no gráfico, temos apenas $1$ no final da imagem.
	- Agora vamos ter que encontrar $F5$ & $F2$.
	- Jb só comenta que operações de divisões são chatinhas e ele errou um pouquinho em escolher incluir essa operação.

### $A = B / C$
- Como resolvemos isso?
	- Levando em conta que divisões são chatas, conseguimos traduzir para : $a = b * c^-1$.
	- Com isso, conseguimos : $Da / Db = c^-1$
	- E disso : $Da / Dc = -b / c^2$
- Para comentar : JB nos esperou derivar até escrever no quadro e continuar a aula. Praticamente a sala inteira esqueceu a derivar.
	- Acredito que ninguém teve que derivar desde o segundo semestre.
	- Lol.
- O que conseguimos, de fato é : 
	- $F6 = F5 * F6^-1$
	- $DF6 / DF5 = F2^-1$
	- $DF6 / DF2 = -F5 / F2^2$
- Agora, temos que propagar esse resultado para trás.
	- Schneider escolher calcular $y$ primeiro, $F2$.
	- '*Só que agora entra a regra da cadeia.*'
	- Isso é : $DF / DF2 = DF / DF6 * DF6 / DF2$
	- $DF / DF2 = 1 * DF6 / DF2$
	- $DF / DF2 = 1 * -F5 / F2^2$
- Mas esses resultados já existem, de acordo com o gráfico :
	- $F2 = 2$
	- $F5 = 0,6603$
- Ou seja : $-F5 / F2^2$ resulta em : $0,1650$.
- Agora fazemos isso com o $F5$ : 
	- $DF / DF5 = DF / DF6 * DF6 / DF5$
	- $DF / DF5 = 1 * DF6 / DF5$
	- $DF / DF5 = 1 * F2^-1$
	- $DF / DF5 = 0,5$
