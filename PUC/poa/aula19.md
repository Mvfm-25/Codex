# Projeto & Otimização de Algoritmos
## [11-05-2026][mvfm]
---
### Problemão anterior
- Hoje a gente vai ser propriamente apresentado para o conceito de **Backtracking**, mas primeiramente vamos resolver o problema da aula anterior.
	- Da qual não participei.
- Acredito que ainda seja coisas de programação dinâmica.
- É problema de soma de **sub-conjuntos**. 
	- Tenho uma lista gigante de números, a soma já feita e o alvo que quero.
	- {...}, 0, 191
		- Caso demonstrado no quadro.
- Caso o algoritmo ultrapasse o limite que queremos, montamos um novo ramo da árvore, em que retiramos um número (arbritário?)
- Tendo uma lista de tamanho $n$, teremos uma quantidade de $2^n$ de subconjuntos.
	- O pior caso do algoritmo atual, é não ter nenhuma soma que alcance o alvo e tenha que passar por todas as $2^n$ possibilidades.
	- O que é muita coisa. Até para computadores.

### Aí entra o Backtracking
- "É algo mais fraco."
	- Um pouco mais parecido com força bruta, mas um pouco mais inteligente. Temos um certo sentido de directionamento, mas nada garantido. "Parece promissor."
- "*Assim que eu já tenha passado do meu alvo, impedindo a execução.*"
- Esse negócio de parecer razoável.
- Por mais que o Backtracking seja bem rápido, e bem inteligente, tem certos problemas em que o espaço de busca é tão absurdamente gigante que no mundo real : pouco importa.
- Uma lição parecida com as de algoritmos gulosos, em que existem certos problemas que nem ajudam.
- {$somaRestante + somaAtual$} < $alvo$ -> retorna
	- Foi um if que já ajudou bastante com tempo de execução.Aparentemente ajudando mais do que '*Se já passamos do limite, cai fora*'.

### Vamos ver Backtracking em outra coisa.
- O problema mais famoso de backtracking, de acordo com o JB.
- Um problema com o tabuleiro de xadrez.
	- De tamanho 8x8
- O problema das **n-rainhas**.
![8 queens](assets/eightq.png)
- Colocar **oito rainhas** em um tabuleiro de **8x8** de maneir com que nenhuma rainha ataque qualquer outra.
- A maneira mais idiota possível seria testar todas as **64** localizações possíveis.
	- Funciona, mas é muito idiota.
	- $(64 x 63 x 62 x 61 x 60 x 59 x 58 x 57 x 56) / 8!$, no total. Ou $3,14699x10^{84}$ caso queira ser muito chato.
- É claro que conseguimos ser mais inteligente.
- Primeira ideia do JB, simplesmente não colocar nenhuma rainha na mesma linha, coluna que uma que já tenha sido colocada.
	- Desse jeito temos, $8^8$ de possibilidades. Ou 16,777,216 caso seja muito chato.
- JB vai resolver, por mão, o problema de $4x4$. Que o reduz para *apenas* 256 possibilidades.
- Sempre andando de 1 em 1, testes por profundidade.
- JB conseguiu encontrar *uma* maneira de inserir 4 rainhas. Mas e se ele quisesse **TODAS** as maneiras?
	- Cadu sugere, espelhar &/ou rotacionar um dos quadros já finalizados.
	- Tu basicamente só testa metade do quadro.
	- Dos testes feitos pelo JB, ele só precisou colocar a primeira rainha no primeiro e segundo pilar.
	- Independente da rotação, tu ainda vai usar uma das soluções já encontradas.	
