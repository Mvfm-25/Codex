# Métodos Formais para Computação
## [04/08/2026][mvfm]
---
### Introduções
- Professor é o **Júlio**, aula na 516.
	- Primeira vez que estou aqui extensivamente desde 2024/1.
- Disciplina do **Sexto Semestre** para CC, disciplina do **Sétimo Semestre** para ES.
- '**Essa disciplina acaba sendo um pouco mais difícil devido a sua distância de seus requisitos**'.
	- Cadeira de revisão? Teoria dos conjuntos?
	- Matemática discreta?
- Cadeira de testes unitários?
	- '**Teste não garane correção de porcaria nenhuma.**'
	- Testes servem para encontrar defeitos e corrigirem, nunca para mostrar a correção.
- Não necessariamente garantem qualidade.

### Ementa
- Conceitos essenciais de espeficação formal, verificação formal & métodos formais.
	- Análise de requisitos, modelagem e implementação de software.
	- Verificar e validar, duas coisas diferentes.
- Especificação e verificação de modelos e programas
- Estudo de lógica de Hoare;
	- Formalismo matemático? Retirada da ambiguidade.
- Especificação de assertivas, pré e pós-condições, invariantes e variantes.

### Software & Qualidade
- Requisitos de qualidade dependentes : 
	1. Do domínio da aplicação
	2. Ambiente de execução
	3. Público alvo
	4. etc.
	- '**Exigem técnicas sofisticadas e específica para cada produto desenvolvido.**'
- Acidentes da **Ariane 5, Therac-25 & Pentium FDIV** mencionados novamente, mesma coisa que o JB mostrou na introdução para métodos numéricos.
- Por que é tão difícil garantir a qualidade do software?
	1. Porque é algo tão dinâmico
	2. Porque envolve pessoas
	3. Porque é **CARO**
- **Verificação**
	- Estamos construindo o produto corretamente?
	- Estamos construindo certo o software?
	- Exemplo dado : testes funcionais.
- **Validação**
	- Construímos o produto correto?
	- Estamos construindo o software certo?
	- Exemplo dado : Testes de aceitação.

### Técnicas de V&V
- Estáticas
	- Não requerem que o sistema de software seja executado.
- Dinâmicas
	- Requerem trabalhar com uma representação executável do sistema de software.
- Formais
	- Requerem o uso de linguagens formais de especificação e fundamentos matemáticos sólidos.
- '**Formal methods are software engineering methods that apply rigorous, mathematically based notation and language to specify, develop and verify the software.**'
- '**Eu provo matemáticamente, não testo.**'
	- OOou shiii.
- Lógicas utilizadas na cadeira :
	1. Lógica de Predicados
	2. Lógica Equacional
	3. Lógicas de Segunda Ordem
	4. Lógicas de Programas
	5. Lógicas temporais
- Júlio deixou algumas folhinas de atividade & revisão para **Lógica** & **Matemática Discreta**.
	- [Matemática Discreta & Conjuntos](https://brpucrs-my.sharepoint.com/shared?listurl=https%3A%2F%2Fbrpucrs-my.sharepoint.com%2Fpersonal%2F10070245_pucrs_br%2FDocuments&id=%2Fpersonal%2F10070245_pucrs_br%2FDocuments%2FDocumentos%2Fmetodosformais%2Frevisao%2Frevisao.pdf&parent=%2Fpersonal%2F10070245_pucrs_br%2FDocuments%2FDocumentos%2Fmetodosformais%2Frevisao&shareLink=1&ga=1)
	- [Lógcia Propocional](https://brpucrs-my.sharepoint.com/shared?listurl=https%3A%2F%2Fbrpucrs-my.sharepoint.com%2Fpersonal%2F10070245_pucrs_br%2FDocuments&id=%2Fpersonal%2F10070245_pucrs_br%2FDocuments%2FDocumentos%2Fmetodosformais%2Frevisao%2FlogicaProposicional_sintaxe.pdf&parent=%2Fpersonal%2F10070245_pucrs_br%2FDocuments%2FDocumentos%2Fmetodosformais%2Frevisao&shareLink=1&ga=1)
	- [Lógica de Predicados](moodle.pucrs.br/mod/resource/view.php?id=3789237)
