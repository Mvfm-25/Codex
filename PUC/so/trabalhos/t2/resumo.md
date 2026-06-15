# Simulador de Memória — FIFO vs. LRU

## Visão geral da implementação

O arquivo `simulador_memoria.py` simula a **paginação por demanda** de um sistema operacional, comparando dois algoritmos de substituição de página: **FIFO** e **LRU**. A arquitetura é dividida em três classes:

| Classe | Responsabilidade |
|---|---|
| `Frame` | Representa um quadro da memória física: guarda a página alocada e um `timestamp` (relógio lógico). |
| `TabelaPaginas` | Coração da simulação: processa cada acesso, detecta *hit*/*page fault*, escolhe a vítima e imprime o mapa de memória. |
| `Simulador` | Lê e faz o *parsing* do arquivo de entrada, orquestra a execução e imprime as estatísticas finais. |

O fluxo de cada acesso (`acessar_pagina`) é:
1. Incrementa o relógio lógico e procura a página nos frames → se achar, é **Hit**.
2. Se não achar, é **Page Fault**: usa um frame vazio se houver.
3. Memória cheia → chama `substituir_pagina`, que escolhe a vítima.

A entrada segue o formato do enunciado (1ª linha = nº de frames; demais = páginas), mas o parser é **tolerante**: aceita vários números por linha, espaçamento irregular, comentários `#` e BOM do Windows (`utf-8-sig`).

## A diferença central entre FIFO e LRU

O detalhe mais elegante da implementação é que **os dois algoritmos compartilham exatamente o mesmo critério de escolha da vítima**: o frame de **menor `timestamp`** (`min(self.frames, key=...)`). A única diferença está em **quando o `timestamp` é atualizado**:

- **FIFO** — o `timestamp` é gravado **apenas na entrada** da página no frame. Em um *hit* nada muda. Logo, sai sempre a página que entrou **há mais tempo** (a "mais velha da fila").
- **LRU** — o `timestamp` é atualizado **também a cada hit** (linha 41-42). Assim, sai a página **usada há mais tempo** (a "menos recentemente usada").

Essa única linha condicional (`if self.algoritmo == "LRU"`) é o que separa os dois comportamentos — uma forma muito enxuta de unificar a lógica.

## Como os resultados da subpasta foram alcançados

A pasta `casos_teste/` contém 8 arquivos de entrada projetados para exercitar comportamentos teóricos distintos, e um `README.md` com a tabela de resultados de referência. Os valores foram validados contra a execução real do simulador. Os casos mais ilustrativos:

- **Anomalia de Belády (casos 02 e 03):** a *mesma* cadeia de referência rodada com 3 e depois 4 frames. No FIFO, **aumentar** de 3→4 frames **aumenta** os faults (9 → 10) — contraintuitivo, é a anomalia de Belády. O LRU, por ser um *algoritmo de pilha*, não sofre o efeito e melhora (10 → 8). Isso comprova uma propriedade teórica conhecida diretamente no código.
- **Localidade temporal (caso 04):** a página `4` é reacessada com frequência. O LRU a mantém (renova o timestamp a cada hit); o FIFO a expulsa só por ser antiga na fila. Resultado: **LRU 5 faults vs. FIFO 8** — a vantagem prática do LRU.
- **Thrashing (caso 05):** *working set* (4 páginas) maior que a memória (3 frames) em laço → 100% de faults em ambos. Limite teórico.
- **Casos 06/07:** *working set* que cabe na memória e memória de 1 frame (borda) → FIFO == LRU.
- **Caso 08:** mesma cadeia do gabarito, mas em formato "bagunçado", provando que o parser robusto produz resultado idêntico.

**Implicação:** os resultados não foram apenas "rodados e anotados" — cada caso isola uma propriedade conceitual (anomalia de Belády, localidade, thrashing, robustez do parser) e os números servem como **suíte de regressão**. Se uma alteração futura quebrar a lógica, a tabela do README denuncia.

## Pontos fortes

- **Unificação elegante** de FIFO e LRU por um único critério (`min` por timestamp), reduzindo duplicação e tornando a diferença conceitual explícita.
- **Parser robusto e tolerante** a formatos diversos, comentários e BOM.
- **Tratamento de erros** adequado (arquivo inexistente, vazio, não-numérico, frames ≤ 0).
- **Saída didática**: imprime o mapa de memória passo a passo, marcando o frame alterado — ideal para fins acadêmicos.
- **Cobertura de testes conceitual**, com resultados de referência validados contra o gabarito oficial.

## Pontos fracos

- **Eficiência:** tanto a busca de hit quanto a escolha da vítima são **O(n) por acesso** (varrem todos os frames). Para muitos frames seria melhor um dicionário `página→frame` + estrutura ordenada (ex.: `OrderedDict`/heap). Para o porte acadêmico, porém, é irrelevante.
- **Verbosidade da saída:** imprime o mapa completo a cada passo, sem modo "silencioso". Em cadeias longas o terminal fica poluído e dificulta ver só as estatísticas.
- **Ausência de testes automatizados:** os resultados de referência estão em uma tabela Markdown conferida manualmente; não há um script `assert`/`pytest` que falhe sozinho numa regressão.
- **Risco teórico de empate de timestamp:** como FIFO e LRU usam o mesmo relógio e nunca há empates reais (relógio sempre incrementa), funciona — mas o desempate do `min` depende implicitamente da ordem dos frames, o que não está documentado como garantia.
- **Sem validação de páginas negativas/limites:** valida `num_frames > 0`, mas não restringe os números de página (qualquer inteiro é aceito).
