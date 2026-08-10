# Construção de Compiladores
## [10-08-26][mvfm]
---
### Histórico de Construção de Compiladores
- Pequena linha do tempo demonstrando acontecimentos importantes no contexto de compiladores
- Começando, quase que obviamente, com Fortran.
![Linha do tempo](assets/historico_compiladores.png)
- "*Programar com Go-To's é uma aberração, um atentado ao raciocínio das pessoas.*'
	- Ofensa DIRETA ao Basic.
- Agustini comenta que está faltando, claramente, a presença & impacto da linguagem C.
- Ele mostra na tela a árvore genealógica das linguagens de programação
	- Especificamente aquele que é a mais confusa com secções cortando áreas da árvore mostrando denominações como '*Imperative*', '*Hybrid*', '*Object-Oriented.*'
	- ![arvore feia](assets/arvore_feia.gif)

### Por que estudar compiladores?
- Base teórica da Computação
	1. Como compiladores & computadores funcionam ( conjunto de instruções, registradores, modos de endereçamento [ Relativo, Direto, Indireto] )
	2. Que código de máquina é gerado para cada construção da linguagem (considerações sobre eficiência)
	3. O que caracteriza um bom projeto de linguagem.
- Aplicações práticas em engenharia de Software
	1. Leitura de argumentos de linha de comando sintaticamente estruturados
	2. Leitura de dados estruturados (JSON, YAML, XML, Protocol Buffers)
	3. Pesquisa em nomes hierárquicos (namespaces, sistemas de arquivos)
	4. Interpretação de linguagens de comando e de consulta (DSL's, regex)
- Modelo estruturado -> Análise do model -> Gera alguma coisa na saída.
- O objetivo da disciplina é ver como a transformação é feita.

### Estrutura de um compilador
![Árvore sintática](assets/arvore_sintatica.png)
- '*Na dúvida, escolham pilha na prova.*'
	- Automatos de pilham diferem de automatos finitos por terem memória. Memória de pilha. Né?
![Demais fases front-end](assets/fases_front.png)
- **Compiladores de Passagem**
	- '*De forma sobre-posta, para cada token, o compilador analisa, verifica e já gera o código correspondente.*'
		- Busca token -> analisa -> Verifica -> Gera código -> Fim do código?
	- O programa de saída é gerado ao decorrer da leitura do programa-fonte, sem etapa intermediária.
	- Dificulta otimizações que dependem de contexto futuro.
		- ex: *Uso de uma variável declarada mais adiante.*
- ![Compiladores Multi-pass](assets/multi-pass.png)

### Arquitetura Duas-Passagens
- **Front-End** (dependente da linguagem)
	- Scanning, parsing, verificação semântica.
	- Produz uma representação intermediária. IR.
	- ex : Java, Pascal, C#.
- **Back-End** (dependente da máquina)
	- Otimização & geração de código baseado na IR.
	- ex de arquitetura alvo : **x86-64, ARM64, RISC-V**.
	- Historicamente : Pentium, PowerPC, SPARC.
- **Vantagens de Duas-Passagens**
	- Melhor portabilidade, um novo front-end ou back-end basta para suportar uma nova linguagem/máquina.
	- Muitas combinações possíveis entre front-end's & back-end's
	- Otimizações mais simples são mais simples sobre a reperesentação intermediária do que sobre o código fonte.
- **Desvantagens**
	- Compilação mais lenta devido sua quantidade de fases.
	- Necessária mais memória durante compilação.

### Compilador vs. Interpretador.
![Comp vs. Intr](assets/comp_v_intr.png)
![Estrutura estática de um compilador](assets/comp_estatica.png)

### Gramáticas
- O que é uma gramática?
``` code
	Comando = "if" "(" Condição ")" Comando ["else" Comando] .
```
- **Símbolos Terminais**
	- Símbolos Terminais (TS) - Átomos de linguagem (TS) : 'if', '>=', ident, number.
	- Símbolos Não-Terminais (NTS) - Derivados em unidades menores : Comando, Expr, Tipo, ...
	- Produções (P) - Regras de como não decompor não-terminais : Comando = Desig "=" Expr ";".
	- Símbolo Inicial (S) - Não-terminal raíz da gramática (ex : Programa)
