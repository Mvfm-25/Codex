---
name: puc-cronograma
description: Lê o cronograma de uma cadeira da PUCRS (Moodle → Plano de Ensino → SARC, pelo browser do WMux) e monta o mapa "o que cai em cada prova" (P1, P2, P3, PS, G2), ligando cada aula do cronograma às notas aulaNN.md do vault Codex/PUC. Use sempre que o usuário quiser saber o conteúdo de uma prova, dividir a matéria por avaliação, "olhar o cronograma", associar aulas a provas, ou como primeiro passo antes de criar índices de materiais ou guias de estudo de uma cadeira — mesmo que ele só diga algo como "o que cai na P2 de cc?".
---

# puc-cronograma

Produz `<cadeira>/materiais/mapa-provas.md` (legível) e `mapa-provas.json` (lido pelas skills
`puc-materiais-index`, `puc-guias` e `puc-verificar-guias`). Cria a pasta `materiais/` se faltar.

Os scripts ficam em `scripts/` dentro do diretório desta skill (o "Base directory" mostrado ao
carregá-la). Abaixo, `<skill>` é esse diretório.

## 1. Localizar o vault e a cadeira

```bash
python -I <skill>/scripts/acha_puc.py [cadeira]
```
Devolve `raiz`, `cadeira`, `pasta_cadeira` e `indice_cadeira`. Sem argumento, a cadeira vem do
diretório atual (se estiver dentro de `PUC/<x>/`). Se `cadeira` vier `null` e o pedido não deixar
claro qual é, pergunte — a lista `cadeiras` mostra as opções. O caminho nunca é fixo: o mesmo vault
existe em Windows (`C:\GDM-05\Codex\PUC`) e Linux (`~/penguosis/Codex/PUC`).

## 2. Obter o texto do cronograma

Leia o `<cadeira>-index.md`: ele costuma ter o link "Página da disciplina no Moodle" e às vezes o
link direto "Cronograma do Semestre" (SARC). Prefira o link direto quando existir.

**Com WMux** (teste com `Test-Path '\\.\pipe\wmux'` no **PowerShell** — no Bash o caminho UNC é
mutilado e o teste dá falso):
```powershell
& "<skill>/scripts/wmux_cronograma.ps1" -CronogramaUrl '<link SARC>' -Saida '<scratchpad>/<cadeira>-cronograma.txt'
# ou, sem link direto:
& "<skill>/scripts/wmux_cronograma.ps1" -CursoUrl '<link do curso no Moodle>' -Saida '<scratchpad>/<cadeira>-cronograma.txt'
```
O script abre uma aba própria (`caller` único + `fresh`), segue curso → "Plano de Ensino" →
"Cronograma Previsto" → página externa do SARC, grava o texto e **fecha a aba**. Ele não mexe na
aba que o usuário está vendo. Saídas de erro e o que fazer:
- `wmux_indisponivel` → peça ao usuário o link do SARC, um PDF/print do cronograma, ou que abra o
  Claude dentro do WMux.
- `moodle_exige_login` → peça que faça login no Moodle no browser do WMux e rode de novo.
- `link_do_cronograma_nao_encontrado` → o professor organizou a página de outro jeito; use
  `browser.snapshot`/`get_text` com o mesmo `caller` para achar o link à mão, ou peça o link.

**Sem WMux**: aceite o texto colado, um PDF (extraia com `pdftotext -layout -enc UTF-8`) ou o link.
Não use Playwright/WebSearch quando o WMux estiver ativo (o usuário não vê essas janelas).

Se for a primeira vez que se obtém o link direto do SARC, ofereça acrescentá-lo ao
`<cadeira>-index.md` — da próxima vez o passo fica mais simples.

## 3. Gerar o mapa

```bash
python -I <skill>/scripts/mapa_provas.py <cronograma.txt> <pasta_cadeira> [--cumulativa P2[,P3]]
```
Antes de rodar, leia a regra de avaliação no `<cadeira>-index.md`: se ela disser que uma prova
"cobre todas"/"é cumulativa" (ex.: `ss`, "P2 cobre todas"), passe `--cumulativa` — o cronograma
sozinho só mostra o conteúdo *novo* desde a prova anterior. Linhas sem conteúdo (feriado,
dúvidas, correção de prova, apresentação de trabalhos) saem marcadas como `logistica`.
O script reconhece as linhas do SARC (`N  DIA  dd/mm/aaaa ...` + linha de descrição), atribui a
cada prova regular (P1, P2, P3…) as aulas desde a prova anterior, marca PS/G2 como "todo o
conteúdo" e casa as aulas com as notas pela data no cabeçalho `## [dd/mm/aa][...]`.

Confira o resumo impresso:
- `notas_sem_data`: notas sem data no cabeçalho (ex.: `ss/aula03.md`) — ficam fora do mapa;
  aponte ao usuário.
- `notas_sem_par`: notas cuja data não bate com nenhuma aula. Quase sempre é data errada no
  cabeçalho da nota (ex.: `aula08.md` com `16-08` quando a aula foi em 26/08). Aponte ao usuário;
  **não corrija a nota sozinho** — é o texto dele.
- Uma prova com 0 aulas, ou provas fora de ordem, indica cronograma num formato diferente:
  leia o texto e monte o mapa à mão no mesmo formato.

## 4. Completar com as provas-exemplo

O cronograma diz o que foi *dado* antes de cada prova; as provas-exemplo mostram o que é
*cobrado*. Procure provas antigas em `provas/`, `atividades/` (nomes como `compil_p1_*.pdf`,
`prova*`) e links "Prova exemplo" no índice. Para cada uma, extraia o texto e acrescente ao fim de
`mapa-provas.md` uma seção:

```markdown
### Observações das provas-exemplo
- **P3 (2024/2)**: metade da prova (5 pts) foi verificação semântica OO (genéricos, interfaces) —
  conteúdo da P2 no cronograma. Revisar semântica também para a P3.
```
Isso importa porque foi exatamente esse tipo de desvio que mudou o plano de estudo da P3 de `cc`.

## 5. Responder

Mostre ao usuário, por prova: data, temas (agrupe linhas repetidas como "Analisadores
descendentes ×3"), notas existentes e lacunas (aulas sem nota). Mencione as observações das
provas-exemplo e as notas com data suspeita. Os arquivos gerados ficam no vault — diga onde.
