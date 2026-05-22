# Métodos Numéricos
## [19-05-2026][mvfm]
---
### App de dieta do Joãozinho
- JB está desenvolvendo uma app para garantir a melhor forma para o verão ( que está por aí! )
- O app está recomendo 'as melhores refieções para o dia!'
	- No primeiro dia, Pizza. No segundo dia, XIS! No terceiro dia, lasanha! No próximo... Picadão. Então, Rúcula.
	- '*Uma app muito bem planejada.*'
- O app foi criteriosamente planejada para que : de um dia para o seguinte, não está pré-determinado, mas tem chances maiores e menores.
- Se baseia na decisão anterior, mas não garante uma resposta logo de cara pelo o que entendi.
- Muito parecido com o problema do parquinho, mas não é a mesma coisa.
- Perceba na falta de *entrada* & *saidas* como um exemplo.
![[assets/appjb.excalidraw | 100%]]
- Não resolvemos por um sistema, vamos utilizar **Cadeia de Markov**.
	- Outro matemático Russo, estudava estatística.
	- Ele descobriu uma série de fenômenos na própria língua russa. Uns 150 anos atrás.
	- Esse fundamentos desenvolvidos por Markov, consegue grosseiramente descrever LLM's.
		- Um cálculo para '*prever*' a palavra seguinte.
		- Muito, muito grosseiramente.
- Ele fez isso na língua russa.
- :^0

### Markov & JB
- '*Eu só tenho probabilidades, vamos ver para onde isso me leva.*'
- Não temos um início default, jogamos a pessoa no aplicativo e mandamos ela trafegando por aí.
- '*Eu gostaria de ter uma matriz para fazer isso.*'
	- JB agora está procurando por um programinha que ele lembra de ter para fazer isso.
- Legal que estamos estudando isso agora, queria me aprofundar em cadeias de Markov já faz um tempo agora. Quero implementar algo parecido no Thoth pro random humor generator da G.D.M.
- '*Se eu tivesse uma arma, esse projetor não estaria mais aí.*'
	- JB ameaçando a vida do projetor.
- JB fez a matriz e ele ficou bem bonitinha. Não consegui entender muito bem como ela funciona, mas ficou legal.
- Informações daqui para lá, essencialmente. Mesma coisa que os parâmetros do programa.
- '*de*' no eixo y, as colunas. E '*para*' no eixo x, as linhas.
	- Ou seja, as colunas tem que somar 1. As colunas são as origens.
	- Matriz markoviana o nome. Ela poderia ter sido escrita da direção contrária, mas a configuração atual é dada a preferência pessoal do JB.
- Eventualmente, teremos que multiplicar nossa matriz desenvolvida por um vetor. Ainda não sabemos porque.
	- Cool funky math games.
- Luísa escolhe começar na **Lasanha**. Ela só entra uma vez, não tem saída. Seguindo dia à dia para refeições diferentemente.
	- Uma das perguntas é que em dado intervalo, quais as comidas que ela mais comeu. Essencialmente, perguntas de analítica.
	- O ponto de início de fato mantem tamanha influência em larga escala? Meses, anos?
- JB agora está usando um exemplo de Cadeias de Markov para a previsão do tempo. Mesma coisa, bem útil para análise.
- Obrigado Markov.

### A execução.
- JB roda um programinha dele alimentando a matriz criada anteriormente e um vetor S = [1 0 0 0 0]
	- O que isso ajuda?
- Seguindo a ordem da matriz, o $1$ descrito no vetor é a **Lasanha** da matriz. Acredito que ela só determina o ponto de início.
- No dia seguinte, Luísa teve 0.3 prob de repetir a Lasanha, 0 & 0 para Rúcula e Pizza, 03 & 04 para Tudo e XIS respectivamente.
- As probabilidades meio que se estabilizam ao decorrer dos dias. Estão ficando cada vez mais e mais parecidas.
	- No longo prazo, isso significa um certo sentido de segurança de resultados. Ou seja, vou estar *provavelmente* correto.
	- Para decorrer os dias, JB fez o seguinte : $m^1 * s$ para o primeiro dia. $m^2 * s$ e segue assim. O expoente simbolizando os dias.
- Ao longo período, as colunas ficaram iguais.
	- Andando tempo suficiente, não importa de onde começaste.
	- Mas pode se tornar falso.
- O *Tudo* é a refeição mais provável, e a *Lasanha* menos provável. O *Tudo* tem praticamente 3x as probabilidades da *Lasanha*.
- Oh wow.
- JB mostra também, comprova sem dúvidas, que começando em outro lugar não importa na prática.
- '*Previsão de tempo através de cadeia de Markov.*'
	- JB julga isso como algo muito legal para um **TCC**.
- Outro exemplo usado também é o escalanador do processos do sistema operacional.
