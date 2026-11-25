---
name: puc-verificar-guias
description: Verifica guias de estudo e índices de materiais do vault Codex/PUC (materiais/P1.md, P2.md, materiais-index.md…) — links quebrados, codificação/mojibake, blocos de gabarito, cobertura das aulas de cada prova — e recalcula de forma independente os gabaritos mecânicos (First/Follow, LL(1), tabelas LR(0)/SLR/CLR/LALR, rastreamento de pilha, código da máquina de pilha). Use depois de criar ou editar um guia, quando o usuário perguntar se um gabarito/tabela/código está certo, pedir para "conferir", "validar" ou "revisar" material de estudo, ou quiser só calcular uma tabela CLR ou simular código de pilha.
---

# puc-verificar-guias

Separada da criação de propósito: serve para guias gerados pela `puc-guias`, para guias que o
usuário editou à mão e para conferir uma resposta avulsa ("essa tabela CLR está certa?").

`<skill>` = diretório desta skill. Ferramentas em `<skill>/scripts/`:

| Script | Para quê |
|---|---|
| `acha_puc.py [cadeira]` | localiza o vault e a cadeira (caminho detectado, nunca fixo) |
| `checa_md.py <arq|pasta> [--mapa mapa-provas.json]` | links, UTF-8/BOM/mojibake, `<details>` balanceado, cobertura de notas por prova |
| `lr_tabela.py <gram.txt> [--metodo lr0\|slr\|clr\|lalr] [--trace "..."] [--ll1] [--ja-aumentada]` | First/Follow, LL(1), estados no formato do professor, tabela, conflitos, reconhecimento passo a passo |
| `maquina_pilha.py <prog.pil> [--var a=5] [--in 3] [-t]` | executa código da máquina de pilha (instruções dos slides e da tabela da prova): saída, memória, altura máxima, rastreamento com BP |
| `cripto_calc.py <comando> ...` | Segurança de Sistemas: MDC/Euclides estendido com passos, inverso, potência com Fermat/Euler, φ, Z*ₙ, geradores, Diffie-Hellman, RSA (chaves, cifra, assinatura), curvas elípticas (ciclo, double-and-add, ECDH), badHash, XOR; **AES-128** (`aes cifra|decifra`, validado com o FIPS-197), hash **Merkle–Damgård/Davies–Meyer** (`md`), quebra de **puzzles de Merkle** (`merkle`), RSA com chaves **PEM** e padding PKCS#1 (`rsa-pem`) |
| `cobertura.py <pasta_cadeira> [--detalhe]` | quanto do material entregue os guias cobrem: links, títulos de slide e termos-chave por material, com a lista do que falta |

As ferramentas são por disciplina (`lr_tabela`/`maquina_pilha` → Compiladores; `cripto_calc` →
Segurança). Para uma cadeira sem ferramenta, confira as contas com um script descartável no
scratchpad e, se o tipo de conta se repetir, proponha ao usuário acrescentar um script aqui.

Rode os scripts com `python -I` e grave entradas de teste no scratchpad, nunca no vault.

## 1. Verificação mecânica

```bash
python -I <skill>/scripts/acha_puc.py [cadeira]
python -I <skill>/scripts/checa_md.py <pasta_cadeira>/materiais --mapa <pasta_cadeira>/materiais/mapa-provas.json
```
Corrija (ou proponha corrigir) cada item. Observações:
- "link quebrado" com nome que tem parênteses: o link precisa estar entre `<…>`.
- "mojibake": o arquivo foi lido/gravado como cp1252 em algum momento; regrave em UTF-8 a partir
  de uma fonte boa (git, ou corrigindo as sequências `Ã§`→`ç`, `Ã£`→`ã`, `â€”`→`—`).
- "cobertura": a nota existe e é da prova mas o guia não a cita — acrescente na tabela do
  cronograma do guia ou na seção do tópico.

## 2. Recalcular os gabaritos

Percorra o gabarito do guia e, para cada resposta mecânica, recalcule **a partir do enunciado**,
sem copiar a resposta do guia para a ferramenta:

- **Gramáticas** (First/Follow, LL(1), itens, tabelas, traces): transcreva a gramática do
  enunciado para um `.txt` (uma produção por linha, `|` para alternativas, `ε` para vazio) e rode
  `lr_tabela.py` com o método pedido. Compare **pelo conteúdo** dos estados — a numeração pode
  diferir da do guia sem estar errada; diga ao usuário quando for só isso. Use `--ja-aumentada`
  quando a gramática do enunciado já começa com a produção `S → X` numerada como 0.
- **Código de pilha**: copie o código do gabarito para um `.pil`, rode com os valores do enunciado
  (`--var`) e confira valores finais, saída, altura máxima e, com `-t`, o quadro de ativação em
  pontos específicos ("pilha antes do STI"). Trechos sem `DS` são aceitos (o simulador aloca as
  variáveis e avisa). Se o enunciado pede para *gerar* o código, confira também se o código segue
  o esquema dos slides (ex.: endereço antes do valor no `STI`, `JZER` para o rótulo de saída).
- **x86 / outras máquinas**: não há simulador; confira à mão as convenções documentadas no
  material (deslocamentos `8+4*(n-1-i)(%EBP)`, prólogo/epílogo) e diga que foi conferência manual.
- **Dissertativas e V/F**: releia contra o material do professor (cache em `materiais/.cache/`);
  não há como automatizar, então seja explícito de que foi revisão de leitura.

## 3. Conferências de conteúdo

- Exercícios novos não podem ser cópia de exercícios resolvidos nos slides: use as linhas
  `exercicios` do `materiais/.cache/manifest.json` para achar e comparar.
- A notação deve ser a do professor (nomes de funções, mnemônicos, formato de tabela).
- O "formato da prova" no topo do guia deve bater com a prova-exemplo.

## 4. Relatório

Responda com uma lista curta por arquivo: ✔ o que passou (e por qual ferramenta), ✘ o que estava
errado e como foi corrigido (ou a correção proposta), e o que **não** pôde ser conferido
automaticamente. Não declare "tudo certo" para itens só revisados por leitura sem dizer isso.
Se corrigir algo no guia, rode o `checa_md.py` de novo no fim.
