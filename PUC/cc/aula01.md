# Construção de Compiladores
## [03/08/26][mvfm]

### Brand New Day
- Primeira cadeira com o Augustini em alguns semestres, 2025/1?
	- Primeira cadeira também em uma sala re-montada, estamos na 401 que deixou de ser o laboratório de CG.
- "Ainda sou Coordenador, então imagino que todo me conheço."
- A aula vai terminar um pouquinho mais cedo pra podermos ir no auditório pro Decano esclarecer as mudanças di curso.
- "Vão explicar se a gente vai ser expulso do 32?"
	- BAH.
- Agustini mostrando a pirâmide etária do Brasil pra explicar que "Estamos perdendo alunos."
- "Vamos sair daqui semestre que vem? Não sei."

### O que faz um compilador?
- "Ele pega um programa fonte, compila e o transforma em 0's & 1's. Código objeto."
- Vamos gerar código real x86 nessa cadeira.
	- Praticamente nenhuma utilidade prática no mundo real profissional, mas parece legal.
- Validação de url's cai no trabalho de compiladores, de acordo com o Agustini.
	- "A não ser que vocês trabalhem numa empresa de modem."
- Compiladores parece bem mais expansos do que originalmente especulado.
- O maior problema dessa cadeira é : **Linguagens Automatos**
	- Ninguém, NINGUÉM lembra daquela cadeira.
- "Essas disciplinas online são uma vergonha."
- Elaboração de rotinas para :
	1. Análise Léxica
	2. Análise Sintática
	3. Verficação Semântica
	4. Geração & Otimização de Código.
- ^ Principais componentes de um compilador.

### Análise Sintática
- "Os menino bebeu o bolo."
- Como eu olho, analiso, esse todo vejo apenas como uma sequência de caracteres.
	- Letra, Letra, Espaço.
- A análise léxica vai reconhecer esses caracteres. (Léxico significa : conjunto total de palavras de um idioma. Um dicionário.)
	- Os : artigo determinante.
	- Menino : 'nome'
	- Bebeu : verbo
	- O : determinante
	- Bolo : nome.
- ^ O retorno da análise léxica retorna, ela transformou esses caracteres em um conjunto de símbolos. No caso da computação, esses símbolos vão ser frases reservadas, nossos If's While's etc.
- A análise léxica é determinada por um **Automato Finito**. Seu tempo de processamento é O(n). 
- Análise : decompor um todo em suas partes constituintes. Agora passamos para a Análise sintática.
- Sintaxe : transformar em um estrutura pra descobrir o relacionamento entre os elementos.
- Frase 
	- Sintáguima(?) Nominal
		- Det : Os
		- Nome : Menino
	- Sintáguima Verbal 
		- Verbo : Bebeu
		- Sintáguima Nominal 
			- Det : O
			- Nome : Bolo
- Essas estruturas vem da **Gramática Livre de Contexto**.
- Btw, Agustini trabalhava com linguagem natural e ELE foi absurdamente impactado pela IA.
	- A pesquisa dele em 2002.


