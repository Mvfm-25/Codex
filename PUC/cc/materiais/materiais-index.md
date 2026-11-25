# Construção de Compiladores — Materiais por Prova
## Conteúdo de cada avaliação segundo o [Cronograma do Semestre](https://sarc.pucrs.br/Default/Export.aspx?id=4f050267-4bbb-44a3-b507-18171b321f98&ano=2026&sem=2)
---
### Avaliação
- **$G1 = (P1 + P2 + P3 + MT) / 4$** — 75% provas, 25% média dos exercícios práticos.
- **PS (30/11)** & **G2 (07/12)** — cobrem **todo** o conteúdo abaixo.
---
### Guias de estudo
- [P1](./P1.md) — Revisão LF, léxico (ER, AFD, JFlex), ASDR, First/Follow, LL(1), tratamento de erros. JSON da P1 2014/1 resolvido + 8 atividades com gabarito.
- [P2](./P2.md) — LR(0)/SLR/CLR/LALR, BYACC/J, TDS (SDD/SDT), tabela de símbolos, escopos & tipos. P2 2023/1 resolvida + 7 atividades com gabarito.
- [P3](./P3.md) — RI, ambiente de execução, máquina de pilha, geração de expressões/controle/subprogramas, x86 do exemploGC, semântica OO. Questões 3 & 4 da P3 2024/2 resolvidas + 8 atividades com gabarito.
---
### P1 — 09/09
**Introdução, Análise Léxica & Análise Sintática Descendente**
- Introdução à compilação & revisão de AF, ER e GLC (03/08 – 05/08)
	- [Aula01](../aula01.md) — Apresentação da disciplina, o que faz um compilador.
	- [Aula02](../aula02.md) — Revisão de Linguagens & Autômatos (alfabeto, sentença, linguagem, gramática).
	- [Lista de revisão LF](../atividades/ExercicioRevLF.pdf) · [Solução](../atividades/SolucaoDeAtividades.pdf)
- Análise Léxica & geradores de analisadores léxicos (10/08 – 17/08)
	- [Aula03](../aula03.md) — Histórico, por que estudar compiladores, introdução ao léxico.
	- [Aula04](../aula04.md) — Scanning, tokens, precedência & ambiguidade (dangling else).
	- [Aula05](../aula05.md) — Atividades práticas com JFlex.
	- [Scanning (slides)](../atividades/02_Scanning_Compiladores.pdf)
	- [Exercícios de Análise Léxica](../atividades/exerciciosLexico_e1.pdf)
	- [Geradores e Compiladores](../atividades/GeradoresECompiladores.pdf)
	- [Manual do JFlex](../atividades/jflex_manual.pdf)
	- [meuLexico](../atividades/meuLexico/meuLexico.flex) — Exemplo de especificação JFlex.
- Análise Sintática Ascendente × Descendente & Analisadores Descendentes (19/08 – 31/08)
	- [Aula06](../aula06.md) — Resultados do léxico (JSON), introdução à análise sintática.
	- [Aula08](../aula08.md) — Autômatos de pilha, GLC, notação EBNF.
	- [Parsing (slides)](../atividades/03.Parsing_pt_atualizado.pdf) · [Algoritmos — análise descendente](../atividades/algoritmos1.pdf)
	- *Aulas 07, 09 & 10 sem anotações.*
- Prova exemplo : [P1 2014/1](<../atividades/compil_p1_141 (1).pdf>) — JSON : gramática/LL(1), JFlex, ASDR & mensagens de erro.
- Trabalho **T1** — ASDR para a linguagem C-- (entrega no início da P1).
- **Dicas do Agustini :**
	- 2,5 pontos da prova : a segunda secção `%%` do JFlex. Não precisa usar as macros DIGIT, LETTER & LineTerminator.
	- **Saber os terminais da gramática.**
	- Responder apenas "ERRO" ou "ERRO SINTÁTICO" custa 1,5 ponto.
---
### P2 — 19/10
**Análise Sintática Ascendente, Tradução Dirigida por Sintaxe & Verificação Semântica**
- Análise Ascendente — shift-reduce, LR(0), SLR(1), CLR(1), LALR(1) (14/09 – 23/09)
	- [Aula13](../aula13.md) — Shift-reduce, itens LR(0), closure & go-to, conflitos.
	- [Aula14](../aula14.md) — Tabelas Action & GoTo, lookahead.
	- [Aula16](../aula16.md) — Correção de exercícios CLR(1).
	- [Exercícios de Tabela CLR](../Exercicios_Tabela_De_Análise_CLR.png) · [Exercícios CLR (resolvidos)](../atividades/exercicios_CLR.pdf) · [Algoritmos CLR](../atividades/algoritmos_CLR.pdf)
	- *Aula15 sem anotações.*
- Geradores de analisadores sintáticos — BYACC/J
	- [Aula17](../aula17.md) — BYACC/J na prática.
	- [ByaccJ na Prática](../atividades/08.2-ByaccJ-na-Pratica.pdf)
- Processamento dirigido à sintaxe — gramática de atributos (28/09 – 30/09)
	- [Aula18](../aula18.md) — Atributos sintetizados & herdados, SDD S/L-atribuídas, SDT.
	- [TDS & BYACC/J (slides)](../atividades/Traducao_Dirigida_por_Sintaxe_BYACCJ.pdf) · [Syntax Directed Translation (handout)](../atividades/13-Syntax-Directed-Translation_anotado.pdf)
- Verificação de Tipos & Verificação Semântica (05/10 – 14/10)
	- [Aula20](../aula20.md) — Tabela de símbolos, escopos, sistemas de tipos.
	- [Aula21](../aula21.md) — Revisão pré-prova.
	- [Tabela de Símbolos & Verificação Semântica (slides)](../atividades/Tabela_Simbolos_Verificacao_Semantica.pdf)
	- [Prática — mini (tabela de símbolos & escopos)](../atividades/pratica/README.md)
	- [Atividade Mini Simplificada](../atividades/Atividade_Mini_Simplificada.docx)
	- *Aula19 sem anotações.*
- Resumos & simulados
	- [Resumo — Análise Semântica](../IA/resumo-analise-semantica.md)
	- [Simulado — Análise Semântica](../IA/simulado-analise-semantica.md)
- Prova exemplo : [P2 2023/1](../provas/p2/compil_p2_2023-1.pdf)
	- V/F sobre ascendentes, YACC & semântica; itens & tabela CLR com passo a passo; especificação YACC de protótipos em C com ações semânticas na tabela de símbolos.
---
### P3 — 25/11
**Geração de Código** *(+ verificação semântica avançada)*
- Correção da P2 (26/10)
	- [Aula22](../aula22.md)
- Geração de código — máquina de pilha & x86 (26/10 – 09/11)
	- [Aula24](../aula24.md) — Etapas da geração de código, representação intermediária.
	- [Aula25](../aula25.md) — Atividade em grupo : tradução de `while`/`if` para máquina de pilha.
	- [Geração de Código — Máquina de Pilha](../atividades/Geracao_Codigo_Maquina_Pilha.pptx)
	- [Intermediate Representation](../atividades/16-Intermediate-Rep.pdf)
	- [x64 Cheatsheet](../atividades/x64_cheatsheet.pdf)
	- [Exemplo GC inicial 2026/2](../atividades/exemploGC_inicial_262/README.md)
	- *Aula23 & Aula26 sem anotações.*
- Geração de código — subprogramas & registro de ativação (11/11)
	- [Exemplos com funções](../atividades/exemploGC_inicial_262/exemplos/funcoes/)
	- *Aula27 sem anotações.*
- Trabalho prático em aula (16/11 – 18/11) & dúvidas para a P3 (23/11)
- Prova exemplo : [P3 2024/2](../provas/p3/compil_p3_2024-2.pdf)
	- **Atenção** : metade da prova (5 pts) foi **verificação semântica** — genéricos & "classe implementa interface".
	- Restante : geração de código para expressão condicional `?:` & registro de ativação.
