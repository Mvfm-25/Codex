# Projeto & Otimização de Algoritmos
## [22-06-26][mvfm]
---
### Alg. Genéticos
- "*Algortimos genéticos dispensam de algo que B&B e Backtracking consideram importante : Hierarquia de árvores(?)*"
- Foi apontado que a maior preocupação de B&B e Backtracking é a profundidade da árvore de escolhas, espaço de possibilidades.
- '*Seu intuito é de fato tentar imitar a natureza.* '
- '*Preciso de voluntários*'
	- Alunos com irmãos do mesmo sexo, do mesmo pai.
	- Mesma genética, mas não são iguais.
	- Por que?
- '*Porque a natureza criou um processo bem sofisticado para que os seres se reproduzam.*'
	- Primeiro : dois sexos.
	- É do interesse da natureza, introduzir uma diferençazinha.
- Vamos fazer com que nosso código se reproduza. SEXUALMENTE.
- '*Os filhos do Einstein são um bando de idiotas.*'
- No exemplo do problema de viagem ao redor do Brasil, a única coisa que o algoritmo genético está fazendo é fazer simplesmente uma '*troca*' das distâncias entre as cidades.
	- Se ao invés de fazer uma viagem da 3 -> 4 -> 5, a distância geral diminuiria sendo 3 -> 7 -> 5?
	- Alguém comenta que isso parece desorganizado, mas justamente por ser desorganizado, nossas decisões ruins não se acumulam como se acumulavam no B&B ou Backtracking.

### Pai & Mãe
- '*Em um processo imitando a natureza, eu tenho um estoque de pais & mães que poderiam ser : muitos pais e mães. A natureza escolhe um par de pai & mãe que geram um filho, ele tendo um código genético único. Que pode ajudar em certos aspectos, ou piorar em outros.*'
	- Isso é a natureza, não é necessariamente o que eu quero.
	- Um pai e uma mãe são uma **espécie** de solução. '*Uma solução mais ou menos isso e uma mais ou menos aquilo.*'
- Em termos de gerações, mata os piores da geração passada e coloca os melhores da nova geração nessa **genepool**.
- '*Só que isso ainda gera um monte de perguntas porque isso ainda é uma imitação da natureza.*'
	- Qual o número certo de uma população inicial? Sei lá, chuta aí bro.
	- Como se definem os cromossomos dos seres? E como fazemos essas alterações por geração? Como decidimos a qualidade de um cromossomo?
- Não precisamos nos preocupar com '*Pais & Mães*'. Tudo é uma solução. Pega duas e mistura. Ou nem duas, se quiser pode pegar mais e mais. 
	- '*Isso é um problema teu, dá teus pulos.*'
