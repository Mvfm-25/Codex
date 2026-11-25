---
name: puc-guias
description: Cria guias de estudo por prova (materiais/P1.md, P2.md, P3.md…) para uma cadeira do vault Codex/PUC — conteúdo explicado passo a passo na notação do professor, prova-exemplo resolvida e atividades novas de preparo com gabarito — a partir do mapa de provas, do índice de materiais e do texto já extraído dos slides. Use quando o usuário pedir guia/resumo/material de estudo para uma prova, "atividades para treinar para a P2", simulado com gabarito, ou quiser regenerar um guia depois que chegou material novo.
---

# puc-guias

Gera **um guia por execução** (ex.: "cc P2"); se o usuário pedir todos, faça um de cada vez —
cada guia exige leitura própria do material e regenerar só um fica barato.

`<skill>` = diretório desta skill. As ferramentas de cálculo ficam na skill irmã:
`<skill>/../puc-verificar-guias/scripts/`.

## 1. Pré-requisitos

```bash
python -I <skill>/scripts/acha_puc.py [cadeira]
```
Precisa de, em `<cadeira>/materiais/`:
- `mapa-provas.json` → skill `puc-cronograma`;
- `materiais-index.md` e `.cache/manifest.json` → skill `puc-materiais-index`.
Se faltarem, rode essas skills antes (ou avise o usuário). Elas são o que garante que o guia
cubra exatamente o recorte da prova e use o material real do professor.

## 2. Ler o material (com economia)

Para a prova pedida, leia nesta ordem:
1. A seção da prova no `mapa-provas.md` (inclui as **observações das provas-exemplo**).
2. As notas `aulaNN.md` da prova — trazem o que o professor enfatizou ("isso cai", "vale 2,5").
3. A(s) prova(s)-exemplo, inteiras, do cache — definem o **formato** do guia.
4. **Todo** o material da prova, pelo cache, com
   `python -I <skill>/scripts/le_material.py <pasta_cadeira> "<trecho do nome>" [--max 150] [--de N]`
   — tira rodapés e linhas repetidas, pula cópias idênticas e casa nomes com ou sem acento/NFD.
   Leia em blocos (`--de` continua de onde parou) até o fim de cada deck: o fim dos slides costuma
   ter **perguntas** ("Perguntas (vale Candycoins)") que viram questão de prova.
5. Em `IA/` (resumos, simulados, adicoes.md): veja o que já existe para **remeter** em vez de
   duplicar.

Anote, enquanto lê, a **notação do professor**: nomes de funções (`verifica`, `geraCod`,
`pRot`), forma das gramáticas (Cocol/EBNF, `→`), mnemônicos da máquina, formato das tabelas.
O guia tem de usar a mesma notação — é a que aparece na prova e no gabarito dele.

## 3. Escrever o guia

**O objetivo é a maior cobertura possível do material entregue**: cada deck, cada lista, cada
prova e cada laboratório tem de aparecer explicado e linkado em algum guia. Consequências:
- **Prova cumulativa** (mapa com `cumulativa`) ou PS/G2 → o conteúdo das provas anteriores também
  cai; gere (ou atualize) os guias delas mesmo que a data já tenha passado.
- **Listas do professor sem gabarito** → resolva-as no guia (seção "Listas do professor
  resolvidas", em `<details>`), conferidas por ferramenta. Exercícios "use a ferramenta online"
  (AES, hash, RSA) também se resolvem: `cripto_calc.py aes|md|merkle|rsa-pem`.
- **Listas com gabarito oficial** → só confira e linke; não as repita como atividade nova.
- **Perguntas do fim dos slides** e **provas-exemplo** → respondidas, com o raciocínio.
- Slides em inglês → mantenha os termos originais entre parênteses (*pre-image resistance*).
- Escreva num modelo no scratchpad com links `{{atividades/arquivo.pdf|rótulo}}` e gere o guia com
  `python -I <skill>/scripts/resolve_links.py <modelo.md> <pasta_cadeira>/materiais/P<n>.md`.

Siga a estrutura de `references/estrutura-guia.md` (leia agora). Pontos que fazem diferença:
- **Passo a passo de verdade**: cada técnica como uma receita numerada e logo depois um exemplo
  executado (tabela de pilha, derivação, código gerado), não só a definição.
- **Prova-exemplo resolvida** com o raciocínio, inclusive as perguntas de "que erro aparece/
  em qual função".
- **Atividades novas**: 6–8 por guia, do básico ao "estilo prova", cobrindo cada tópico do recorte.
  O `manifest.json` lista onde há "Exercício/Gabarito" nos slides — leia esses trechos e **não
  repita** exercícios que o material já resolve (o aluno já tem esses gabaritos). Varie gramáticas,
  programas e valores.
- **Gabaritos calculados, não estimados**. Para cada resposta mecânica, use as ferramentas:
  - First/Follow, LL(1), estados e tabelas LR(0)/SLR/CLR/LALR, rastreamento da pilha:
    `python -I <skill>/../puc-verificar-guias/scripts/lr_tabela.py gram.txt --metodo clr --trace "a b c" [--ll1] [--ja-aumentada]`
  - Código de máquina de pilha (valores finais, saída, altura da pilha, quadro de ativação):
    `python -I <skill>/../puc-verificar-guias/scripts/maquina_pilha.py prog.pil --var a=5 -t`
  - Criptografia (modular, DH, RSA, curvas, assinatura, badHash, XOR):
    `python -I <skill>/../puc-verificar-guias/scripts/cripto_calc.py rsa 11 23 3 42` (veja `--help`)
  Grave os arquivos de teste no scratchpad. Se a ferramenta discordar do que você escreveu, a
  ferramenta costuma estar certa — investigue antes de publicar.
- Gabarito em blocos `<details><summary>A1</summary> … </details>` para o aluno tentar antes.
- Links relativos a `materiais/` (`../aula03.md`, `../atividades/x.pdf`); nomes com espaço ou
  parênteses entre `<…>`. Grave em UTF-8 com a ferramenta Write.

## 3½. Medir a cobertura e iterar

```bash
python -I <skill>/../puc-verificar-guias/scripts/cobertura.py <pasta_cadeira> --detalhe
```
Mostra, por material: se está linkado, quantos **títulos de slide** aparecem num mesmo parágrafo
do guia e quantos **termos-chave** (vocabulário distintivo do material) o guia contém. Use o
`--detalhe` para separar **lacuna real** (um laboratório resumido demais, uma lista faltando) de
**ruído** (fragmentos de diagrama, títulos de questão de prova, verbos de enunciado). Complete as
lacunas reais e meça de novo. Referência obtida em `ss`: todos os materiais linkados, ~70% dos
termos-chave e ~50% dos títulos — o restante era ruído. Não reescreva o guia só para repetir
títulos de seção do professor: isso infla a métrica sem melhorar o estudo.

## 4. Ligar e verificar

- Acrescente/atualize a linha do guia na seção "Guias de estudo" do `materiais-index.md`.
- Rode a skill `puc-verificar-guias` sobre o guia novo (ou ao menos
  `checa_md.py <guia> --mapa <materiais>/mapa-provas.json`) e corrija o que ela apontar.

Ao final, diga ao usuário o que o guia cobre, quantas atividades tem, quais gabaritos foram
conferidos por ferramenta e quais (dissertativos) não têm conferência automática.
