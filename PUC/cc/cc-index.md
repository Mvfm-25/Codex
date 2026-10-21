# Construção de Compiladores
## Professor : [Alexandre Agustini](https://www.inf.pucrs.br/agustini/)
---
### Avaliação
- **$G1 = (P1 + P2 + P3 + MT) / 4$** — 75% provas, 25% média dos exercícios práticos.
---
### Trabalhos :
- [T1 — ASDR para a linguagem C--](https://moodle.pucrs.br/mod/assign/view.php?id=3897322)
	- Analisador sintático descendente recursivo para a gramática **C--**, partindo do exemplo visto em aula. Grupos de até 3; entrega até **09/09, 19:15** (início da P1).
- [Tarefa — Verificação Semântica](https://moodle.pucrs.br/mod/assign/view.php?id=3924670)
	- Atividade prática sobre o código inicial de 2026/2 (variáveis globais). Grupos de até 4; entrega até **14/10, 23:59**.
- T2
	- ? — Apresentação prevista para 21/10.
- T3
	- ? — Apresentação prevista para 23/11.
---
### Provas
- P1 — 09/09
	- [Prova exemplo da parte inicial da matéria](https://moodle.pucrs.br/mod/resource/view.php?id=3887222)
- P2 — 19/10
	- [Prova P2 2023/1 (exemplo)](https://moodle.pucrs.br/mod/resource/view.php?id=3927646) — "alta probabilidade de ter semelhança com a P2, mas sem garantias".
- P3 — 25/11
---
### Aulas
- [Página da disciplina no Moodle](https://moodle.pucrs.br/course/view.php?id=96187)
	- Cards : Introdução à compilação, Análise Léxica, Análise Sintática Descendente, Análise Sintática Ascendente, Tradução Dirigida por Sintaxe e Verificação Semântica.
- [Cronograma do Semestre](https://sarc.pucrs.br/Default/Export.aspx?id=4f050267-4bbb-44a3-b507-18171b321f98&ano=2026&sem=2)
- [Aula01](./aula01.md)
	- Apresentação da disciplina, breve revisão em Línguagens & Automatos
- [Aula02](./aula02.md)
	- Continuação da revisão de Linguagens & Automatos.
- [Aula03](./aula03.md)
	- Introdução à análise léxica.
- [Aula04](./aula04.md)
	- Continuação de análise léxica. Atividades(?)
- [Aula05](./aula05.md)
	- Solução de atividades práticas, uso do Jflex.
- [Aula06](./aula06.md)
	- Introdução à análise Sintática.
- [Aula08](./aula08.md)
	- Re-introdução de conceitos fundamentais para análise Sintática, atividade prática. 
- [Aula13](./aula13.md)
	- Análise sintática ascendente — shift-reduce, itens LR(0), closure & go-to, e conflitos shift-reduce / reduce-reduce (dangling else).
- [Aula14](./aula14.md)
	- Tabelas **Action & GoTo**, limites do LR(0) e a adição de lookahead — SLR(1), LR(1) canônico e LALR(1).
- [Aula16](./aula16.md)
	- Correção de exercícios de **CLR(1)** com lookahead, raciocínio shift/reduce na pilha e por que a recursão à esquerda é preferível.
- [Aula17](./aula17.md)
	- **BYACC/J** na prática (módulo de análise ascendente) e aviso da **P2** em 19/10.
- [Aula18](./aula18.md)
	- **Tradução dirigida por sintaxe** — gramáticas de atributos, atributos sintetizados & herdados, SDD S/L-atribuídas e árvore sintática anotada.
- [Aula20](./aula20.md)
	- Introdução à **verificação semântica** — por que a gramática não basta, tabela de símbolos, escopos e sistemas de tipos; validade não é correção.
- [Aula21](./aula21.md)
	- Revisão pré-prova da **P2** e atividade preparatória.
---
### Resumos
- [Resumo — Análise Semântica](./IA/resumo-analise-semantica.md)
	- TDS (atributos, SDD/SDT, S/L-atribuídas), BYACC/J, tabela de símbolos, escopos e verificação de tipos.
---
### Adições IA
- [Material complementar gerado por IA](./IA/adicoes.md)

