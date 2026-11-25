---
name: puc-materiais-index
description: Inventaria o material de uma cadeira do vault Codex/PUC (slides, PDFs, pptx, docx, provas antigas, projetos em atividades/) e cria ou atualiza materiais/materiais-index.md, que diz que material serve para qual prova — criando a pasta materiais/ se preciso e mantendo um cache de texto extraído para as próximas skills. Use quando o usuário pedir um índice de materiais, "organizar o material por prova", disser que chegaram arquivos novos em atividades/, ou antes de gerar guias de estudo; também quando ele quiser saber "qual slide eu estudo para a P2".
---

# puc-materiais-index

Entrada: `<cadeira>/materiais/mapa-provas.json` (da skill `puc-cronograma`).
Saída: `<cadeira>/materiais/materiais-index.md`, o cache `<cadeira>/materiais/.cache/` e um link
no `<cadeira>-index.md`.

`<skill>` = diretório desta skill (o "Base directory" mostrado ao carregá-la).

## 1. Localizar e pré-requisitos

```bash
python -I <skill>/scripts/acha_puc.py [cadeira]
```
Se `materiais/mapa-provas.json` não existe, rode antes a skill `puc-cronograma` (ou, se o usuário
não quiser, peça a ele as datas das provas e monte o recorte à mão). Sem o recorte por prova o
índice vira só uma lista de arquivos, que não responde à pergunta "o que estudo para a P2".

## 1½. Trazer TODO o material do Moodle (antes de inventariar)

O vault costuma ter só parte do que o professor entregou — em `ss`, faltavam as **quatro provas**
e metade dos slides da P2. Guia bom depende de material completo, então sincronize primeiro
(precisa do WMux e da sessão do Moodle logada no browser dele):

```powershell
# 1º só lista (nada é gravado): status local | novo | grande | ignorado | nao_arquivo
& "<skill>/scripts/moodle_sync.ps1" -CursoUrl '<course/view.php?id=N>' -PastaCadeira '<pasta_cadeira>'
# depois baixa os novos (provas → provas/<p1|p2|ps>/, o resto → atividades/)
& "<skill>/scripts/moodle_sync.ps1" -CursoUrl '...' -PastaCadeira '...' -Baixar [-Ignorar 'regex']
```
- Reconhece por **SHA-1** arquivos que já existem com outro nome; nunca baixa executáveis
  (`.exe`, `.msi`…). Use `-Ignorar` para livros inteiros e textos de referência enormes.
- Recursos `nao_arquivo` (links externos, TryHackMe, vídeos) não são baixados — liste-os no índice.
- Mostre ao usuário a lista do que será baixado antes de usar `-Baixar` na primeira vez.

## 2. Extrair o texto (com cache)

```bash
python -I <skill>/scripts/extrai_texto.py <pasta_cadeira>
```
- Extrai PDF (`pdftotext`), PPTX e DOCX de `atividades/`, `provas/`, `trabalhos/` e da raiz da
  cadeira para `materiais/.cache/<caminho>.txt`, com espaços compactados. Só reprocessa o que
  mudou (por data de modificação) e cria `materiais/.gitignore` com `.cache/`.
- O `manifest.json` do cache guarda, por arquivo, o título, o nº de linhas e em que linhas há
  "Exercício"/"Gabarito"/"Questão" — a `puc-guias` usa isso para não repetir exercícios.
- O extrator recompõe acentos de PDFs gerados por LaTeX (`Exerc´ıcio` → `Exercício`), mas
  **expoentes viram texto corrido** (`2^10` aparece como `210`) — releia enunciados numéricos com
  esse cuidado. O resumo também lista `duplicados` (mesmo arquivo em duas pastas): indexe uma vez.
- **Leia o cache, não os PDFs originais.** Para classificar, normalmente bastam o título e as
  primeiras ~40 linhas (`head`) ou um `grep` por "Módulo", "Unidade", "Roteiro", "Agenda".
  Slides inteiros têm milhares de linhas; ler tudo só para classificar desperdiça contexto.
- Arquivos de código e Markdown (`.java`, `.y`, `.flex`, `README.md`) não vão para o cache: leia
  direto, pelo README primeiro.

## 3. Classificar cada material numa prova

Para cada arquivo (do manifest + projetos/pastas de `atividades/` + `IA/*.md`):
1. Compare título/roteiro com os temas do `mapa-provas.json` ("Análise ascendente" → a prova cujo
   recorte contém essas aulas).
2. Use a data de modificação/aparição só como desempate (material costuma chegar perto da aula).
3. Provas antigas: classifique pelo nome (`p1`, `p2`, `compil_p3_*`) e confira o conteúdo — a
   observação do mapa ("P3-exemplo cobra semântica") vale aqui também.
4. Material de referência geral (manuais, cheatsheets) vai junto da prova em que é usado.
5. Se ficar em dúvida entre duas provas, liste nas duas e diga por quê numa nota curta.

## 4. Escrever o índice

Escreva os links como `{{atividades/arquivo.pdf}}` (ou `{{caminho|rótulo}}`) num modelo no
scratchpad e gere o índice com
`python -I <skill>/../puc-guias/scripts/resolve_links.py <modelo.md> <pasta_cadeira>/materiais/materiais-index.md`
— ele usa o nome **exato** do disco (muitos vêm em Unicode NFD, que um link digitado não acha).

Formato (Obsidian, links relativos a `materiais/`, nomes com espaço/parênteses entre `<…>`):

```markdown
# <Nome da Cadeira> — Materiais por Prova
## Conteúdo de cada avaliação segundo o [Cronograma do Semestre](<link SARC>)
---
### Avaliação
- <fórmula da média, copiada do índice da cadeira>
- **PS (dd/mm)** & **G2 (dd/mm)** — cobrem **todo** o conteúdo abaixo.
---
### Guias de estudo            ← só se existirem P1.md/P2.md/P3.md
- [P1](./P1.md) — <uma linha>
---
### P1 — dd/mm
**<temas em uma linha>**
- <Tema> (dd/mm – dd/mm)
	- [Aula03](../aula03.md) — <descrição curta, reaproveitada do índice da cadeira>
	- [<Título do material>](../atividades/arquivo.pdf)
	- *Aulas 07, 09 & 10 sem anotações.*
- **Dicas do professor :** <o que as notas registram sobre a prova>
- Prova exemplo : [P1 2014/1](<../atividades/compil_p1_141 (1).pdf>) — <o que ela cobra>
---
```
- Se o índice já existe, **atualize** em vez de reescrever: acrescente o que é novo, preserve
  descrições e notas que o usuário editou.
- Descrições de aulas: reaproveite as do `<cadeira>-index.md` para manter a mesma voz.
- Aponte lacunas (aulas sem nota) — ajudam o usuário a saber o que pegar com colegas.

## 5. Ligar no índice da cadeira e verificar

- Em `<cadeira>-index.md`, na seção `### Provas`, garanta a linha
  `- [Materiais por Prova](./materiais/materiais-index.md)` (sem duplicar se já existir).
- Rode a verificação de links da skill `puc-verificar-guias`:
  `python -I <skill>/../puc-verificar-guias/scripts/checa_md.py <pasta_cadeira>/materiais`.
- Leia e grave sempre em UTF-8. No PowerShell, `Get-Content` sem `-Encoding utf8` mostra
  `ConstruÃ§Ã£o`, e `Set-Content` corrompe o arquivo; prefira as ferramentas Read/Write/Edit.

Termine dizendo ao usuário quantos materiais foram indexados, quais eram novos e o que ficou sem
classificação ou sem nota.
