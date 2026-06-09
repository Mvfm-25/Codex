# Sistemas Operacionais
## [08-06-2026][mvfm]
---
### Interface do Sistema de Arquivos
- Hoje pelo menos o material tá localizado no card correto dessa semana.
- Apareceu uma entrega para o dia **09**, cujo card foi aparecer **ONTEM** no moodle. À meia-noite em ponto.
	- Uma atividade de gerência de arquivos também, justamente o conteúdo que a gente tá vendo agora.
	- Não ficou muito claro para mim se isso é simplesmente uma atividade prática, para exercitar, ou um trabalho de fato que vale 0.00000000000000001% da nota final.
	- Tenho certeza qual seria a alternativa mais engraçada.
- Ao menos, acho que a aula hoje vai ser aquelas em que o tempo simplesmente passa. 
	- One can only hope.
- Sumário da aula, entregue pelos slides : 
	1. Conceito & Atributos de Arquivos
	2. Operações & métodos de uso
	3. Estrutura de diretórios & Discos
	4. Montagem (Mounting) de Sistemas.
	5. Compartilhamento e Proteção
	6. Atividade prática
- Oh boy.

### Conceito de Arquivo
- O conceito básico pelos slides de um arquivo é simplesmente um '*espaço de endereçamento lógico contíguo mapeado pelo SO para dispositivos físicos.*'
	- Ou seja, espaço ocupado por certos atributos especificados pelo SO.
- Além disso, ele cita três características de um arquivo :
	1. Abstração
		O SO oculta as propriedades físicas do armazenamento.
	2. Persistência
		Dados gravados permanecem após reinicializações.
	3. Conteúdo
		POde ser texto, binário, imagem etc.
- Essas definições foram tiradas direto dos slides.
- É incrível como eu simplesmente não me importo.
- Aula infernal.
- Atributos adicionais : 
	1. Nome	
		Identificador legível por humanos.
	2. ID
		Identificador numérico interno.
	3. Tipo
		Extensão que sugere o uso do arquivo.
	4. Local
		Ponteiro para o dispositivo físico.
	5. Tamanho
		Tamanho atual & máximo previsto.
	6. Proteção
		Quem pode ler, escrever ou executar.
- Operações básicas disponíveis : 
	- **Criar** : Encontrar espaço e adicionar entrada no diretório
	- **Escrever/Ler** : Usa um ponteiro de posição atual
	- **Reposicionar** : Sor colocou a definição como '*O famoso seek*', mas acredito que seria simplesmente o '*buscar*'.
	- **Deletar** : Libera espaço e remove entrada.
	- **Truncar** : Apaga conteúdo mas mantém atributos.
