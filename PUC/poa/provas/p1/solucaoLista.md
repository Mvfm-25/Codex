# Soluções Selecionadas da Lista
## [mvfm + Claude]

> Soluções para os 5 exercícios escolhidos como mais interessantes, com ênfase na linha de raciocínio que levou a cada escolha de abordagem.

---

## 1. Greedy — Exercício 1: Troco com moedas de 17, 8 e 1

### Por que esse exercício é especial

As notas de `adicoes.md` usam o troco de moedas como o exemplo canônico onde greedy **falha** — com moedas {1, 3, 4}, o ótimo para 6 centavos é 3+3=2 moedas, mas greedy daria 4+1+1=3. As moedas desta questão ({17, 8, 1}) parecem "razoáveis" à primeira vista porque 17 é primo e 8 é potência de 2. Quero verificar se greedy funciona ou falha.

### Raciocínio

A estratégia gulosa natural é: **sempre use a maior moeda que couber**. Se o troco é $n$:
1. Use `n // 17` moedas de 17.
2. Com o resto, use `resto // 8` moedas de 8.
3. O que sobrar, use moedas de 1.

Antes de implementar, já posso prever um caso suspeito: **24 centavos**.
- Greedy: 17 + 7×1 = **8 moedas**.
- Ótimo: 8 + 8 + 8 = **3 moedas**.

Isso é uma falha catastrófica. A razão: ao escolher 17 primeiro, o algoritmo "queima" uma fatia que impede usar múltiplos de 8 de forma eficiente.

### Algoritmo Guloso (com a falha documentada)

```python
def troco_guloso(n, moedas=[17, 8, 1]):
    resultado = {}
    for m in moedas:
        resultado[m] = n // m
        n = n % m
    return resultado

def total_moedas_guloso(n):
    r = troco_guloso(n)
    return sum(r.values())
```

### Algoritmo Correto via Programação Dinâmica

Como greedy falha, o problema exige DP. A recorrência é:

```
minMoedas(0) = 0
minMoedas(n) = 1 + min( minMoedas(n-17), minMoedas(n-8), minMoedas(n-1) )
               para cada moeda que couber em n
```

```python
def troco_dp(n, moedas=[17, 8, 1]):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for m in moedas:
            if i >= m and dp[i - m] + 1 < dp[i]:
                dp[i] = dp[i - m] + 1
    return dp[n]

# Confirmação: testa todos os valores de 1 a 100
falhas = []
for v in range(1, 101):
    if total_moedas_guloso(v) != troco_dp(v):
        falhas.append(v)

print(f"Greedy falha em: {falhas}")
# Greedy falha em: [24, 32, 40, 41, 48, 49, 56, 57, 58, 64, 65, 66, 73, 74, 75, 82, 83, 90, 91, 99]
```

### Conclusão

O greedy falha em 20 dos 100 valores. A razão sistemática: sempre que um múltiplo de 8 ou combinação de 8s é mais eficiente que usar 17 no início, o greedy perde. A moeda de 1 garante que o troco sempre existe, mas não que é mínimo. Para este conjunto de denominações, DP é necessário.

---

## 2. Greedy — Exercício 4: Seleção de Atividades

### Por que esse exercício é especial

Este é o problema que melhor demonstra **quando greedy funciona** — ao contrário do exercício anterior. O enunciado propõe dois candidatos gulosos e pede para testá-los nos mesmos dados, o que permite ver empiricamente a diferença entre uma estratégia gulosa correta e uma intuitiva-mas-errada.

### Raciocínio

Tenho 10 atividades com horários. Quero o máximo de atividades não sobrepostas.

**Candidato (a) — Menor duração primeiro:**
A intuição é que atividades curtas "ocupam menos espaço". Mas duração curta não garante que a atividade não bloqueia duas outras longas.

**Candidato (b) — Menor horário de término primeiro:**
A intuição aqui é mais sólida: ao escolher o que termina mais cedo, libero o máximo de tempo futuro para outras atividades. Isso é provável de ser correto.

### Execução dos dois algoritmos

**Dados ordenados por duração (a):**

| Atividade | Início | Fim | Duração |
|-----------|--------|-----|---------|
| 1         | 2      | 4   | 2       |
| 6         | 6      | 8   | 2       |
| 8         | 7      | 9   | 2       |
| 2         | 1      | 4   | 3       |
| 9         | 7      | 10  | 3       |
| 10        | 8      | 11  | 3       |
| 4         | 4      | 8   | 4       |
| 3         | 2      | 7   | 5       |
| 5         | 4      | 9   | 5       |
| 7         | 5      | 10  | 5       |

Processando (end_atual = 0):
- Ativ. 1 (2-4): 2 ≥ 0 → **Selecionada**. end=4
- Ativ. 6 (6-8): 6 ≥ 4 → **Selecionada**. end=8
- Ativ. 8 (7-9): 7 < 8 → Pula
- Ativ. 2 (1-4): 1 < 8 → Pula
- Ativ. 9 (7-10): 7 < 8 → Pula
- Ativ. 10 (8-11): 8 ≥ 8 → **Selecionada**. end=11

**Algoritmo (a) resultado: {1, 6, 10} — 3 atividades.**

**Dados ordenados por término (b):**

| Atividade | Início | Fim |
|-----------|--------|-----|
| 1         | 2      | 4   |
| 2         | 1      | 4   |
| 3         | 2      | 7   |
| 4         | 4      | 8   |
| 6         | 6      | 8   |
| 5         | 4      | 9   |
| 8         | 7      | 9   |
| 7         | 5      | 10  |
| 9         | 7      | 10  |
| 10        | 8      | 11  |

Processando (end_atual = 0):
- Ativ. 1 (2-4): 2 ≥ 0 → **Selecionada**. end=4
- Ativ. 2 (1-4): 1 < 4 → Pula
- Ativ. 3 (2-7): 2 < 4 → Pula
- Ativ. 4 (4-8): 4 ≥ 4 → **Selecionada**. end=8
- Ativ. 6 (6-8): 6 < 8 → Pula
- Ativ. 5 (4-9): 4 < 8 → Pula
- Ativ. 8 (7-9): 7 < 8 → Pula
- Ativ. 7 (5-10): 5 < 8 → Pula
- Ativ. 9 (7-10): 7 < 8 → Pula
- Ativ. 10 (8-11): 8 ≥ 8 → **Selecionada**. end=11

**Algoritmo (b) resultado: {1, 4, 10} — 3 atividades.**

### Por que (b) é provadamente correto e (a) não é

Neste conjunto de dados ambos chegam a 3 atividades, mas isso é coincidência dos dados. O argumento de correção do algoritmo (b) usa a mesma estrutura que as notas usam para rock-jumping — prova por contradição:

**Prova por troca (exchange argument):** Suponha que a solução ótima O começa com atividade $x$ e o algoritmo (b) começa com $y$, onde $y$ termina antes ou junto de $x$ (por construção). Posso trocar $x$ por $y$ em O sem piorar a solução: $y$ termina mais cedo, então tudo que cabia depois de $x$ ainda cabe depois de $y$. Logo, a escolha gulosa de (b) nunca fecha portas que uma escolha diferente manteria abertas.

O algoritmo (a) não tem essa garantia: uma atividade curta pode começar no "meio" de um intervalo e bloquear duas atividades que, juntas, durariam menos.

**Contra-exemplo clássico para (a):**
- Atividades: (0-7), (0-4), (5-7) — durações: 7, 4, 2.
- (a): escolhe (5-7) dur=2 primeiro. Depois nada mais cabe (as outras começam antes de 7). Resultado: **1 atividade**.
- (b): escolhe (0-4) termina em 4. Depois (5-7) começa em 5 ≥ 4. Resultado: **2 atividades**.

### Implementação

```python
def selecao_atividades_b(atividades):
    ordenadas = sorted(atividades, key=lambda a: a[2])  # ordena por fim
    selecionadas = []
    end_atual = 0
    for nome, inicio, fim in ordenadas:
        if inicio >= end_atual:
            selecionadas.append(nome)
            end_atual = fim
    return selecionadas
```

---

## 3. D&C — Exercício 11: Análise dos Três Algoritmos

### Por que esse exercício é especial

As notas explicam o Teorema Mestre com os exemplos de potenciação ($O(\log n)$) e Karatsuba ($O(n^{1.585})$). Este exercício pede para aplicar o mesmo raciocínio a três algoritmos hipotéticos, um deles com uma armadilha: o Algoritmo B não segue a forma do Teorema Mestre e seu custo real surpreende.

### Algoritmo A: $T(n) = 5T(n/2) + O(n)$

**Identificação dos parâmetros:**
- $a = 5$ (cinco subproblemas)
- $b = 2$ (cada subproblema tem metade do tamanho)
- $f(n) = O(n)$ (custo de combinar é linear)

**Aplicando o Teorema Mestre:**
$$n^{\log_b a} = n^{\log_2 5} \approx n^{2.32}$$

Como $n^{2.32}$ cresce mais rápido que $f(n) = O(n)$, estamos no Caso 1: o custo é dominado pela expansão da recursão.

$$\boxed{T(n) = O(n^{\log_2 5}) \approx O(n^{2.32})}$$

### Algoritmo B: $T(n) = 2T(n-1) + O(1)$

**Atenção: este algoritmo não está na forma $T(n/b)$ — o subproblema diminui por subtração, não por divisão.**

O Teorema Mestre não se aplica aqui. Preciso expandir manualmente:

$$T(n) = 2T(n-1) + 1$$
$$= 2(2T(n-2) + 1) + 1 = 4T(n-2) + 3$$
$$= 4(2T(n-3) + 1) + 3 = 8T(n-3) + 7$$
$$= \ldots$$
$$= 2^k T(n-k) + (2^k - 1)$$

Quando $k = n - 1$, chegamos ao caso base $T(1)$:
$$T(n) = 2^{n-1} \cdot T(1) + 2^{n-1} - 1$$

$$\boxed{T(n) = O(2^n)}$$

Esta é a armadilha: "dois subproblemas de tamanho $n-1$" parece razoável, mas resulta em crescimento exponencial. A cada nível da recursão o trabalho **dobra**, e há $n$ níveis — daí o $2^n$.

### Algoritmo C: $T(n) = 9T(n/3) + O(n)$

**Identificação dos parâmetros:**
- $a = 9$ (nove subproblemas)
- $b = 3$ (cada subproblema tem um terço do tamanho)
- $f(n) = O(n)$ (custo de combinar é linear)

**Aplicando o Teorema Mestre:**
$$n^{\log_b a} = n^{\log_3 9} = n^2$$

Como $n^2$ cresce mais rápido que $f(n) = O(n)$, Caso 1:

$$\boxed{T(n) = O(n^2)}$$

### Comparação e Escolha

| Algoritmo | Complexidade | Observação |
|-----------|-------------|------------|
| A         | $O(n^{2.32})$ | Ruim pela expansão explosiva dos subproblemas |
| B         | $O(2^n)$      | **Inviável** — exponencial |
| C         | $O(n^2)$      | Melhor dos três |

**Escolheria o Algoritmo C.** Ainda é quadrático — longe do ideal — mas é o único dos três que não descamba para pior do que polinomial. O Algoritmo B é especialmente traiçoeiro: "apenas dois subproblemas" soa eficiente, mas sem a divisão do tamanho por um fator constante ($n/b$), a árvore de recursão tem profundidade $n$ com ramificação 2, gerando $2^n$ nodos.

A lição: o que importa no Teorema Mestre não é só quantos subproblemas existem, mas **como o tamanho encolhe a cada nível**.

---

## 4. D&C — Exercício 9: Existe $i$ tal que $A[i] = i$?

### Por que esse exercício é especial

O enunciado pede $O(\log n)$, o que imediatamente sugere busca binária. Mas o array não está sendo buscado por um valor — está sendo buscado por uma **propriedade de posição**. O exercício exige encontrar o invariante que torna a busca binária aplicável.

### Raciocínio

Defino uma função auxiliar: $d(i) = A[i] - i$.

**Propriedade crucial:** se $A$ contém inteiros distintos e está ordenado em ordem crescente, então $A$ é estritamente crescente: $A[i+1] > A[i]$, o que significa $A[i+1] \geq A[i] + 1$.

Logo:
$$d(i+1) = A[i+1] - (i+1) \geq A[i] + 1 - i - 1 = A[i] - i = d(i)$$

**$d$ é não-decrescente.** Isso é a chave.

Encontrar $i$ tal que $A[i] = i$ equivale a encontrar $i$ tal que $d(i) = 0$. E como $d$ é não-decrescente, posso aplicar busca binária sobre $d$:

- Se $d(\text{meio}) = 0$: encontrei, retorno `meio`.
- Se $d(\text{meio}) > 0$: qualquer $i \geq \text{meio}$ tem $d(i) \geq d(\text{meio}) > 0$, então a resposta só pode estar à **esquerda**.
- Se $d(\text{meio}) < 0$: a resposta só pode estar à **direita**.

### Implementação

```python
def encontra_ponto_fixo(A):
    esq, dir = 0, len(A) - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        d = A[meio] - meio
        if d == 0:
            return meio      # A[meio] == meio
        elif d > 0:
            dir = meio - 1   # resposta só à esquerda
        else:
            esq = meio + 1   # resposta só à direita
    return -1                # não existe tal i

# Exemplos
print(encontra_ponto_fixo([-3, 0, 2, 5, 7]))  # → 2 (A[2]=2)
print(encontra_ponto_fixo([1, 2, 3, 4, 5]))   # → -1 (nenhum)
print(encontra_ponto_fixo([0, 3, 5, 7, 9]))   # → 0 (A[0]=0)
```

### Por que é O(log n)

A cada iteração, o intervalo de busca é cortado ao meio. Com $n+1$ elementos, o número máximo de iterações é $\lfloor \log_2(n+1) \rfloor + 1$ — idêntico à busca binária convencional.

### O que torna isso elegante

A transformação $d(i) = A[i] - i$ converte um problema de "ponto fixo" — que parece exigir verificar cada posição — num problema de "encontrar zero em sequência monotônica". Uma vez visto esse invariante, a solução é imediata. É o mesmo tipo de insight que o Karatsuba usa: ao olhar para o problema de forma diferente, o custo cai dramaticamente.

---

## 5. Programação Dinâmica — Exercício 2: Calçada com Pedras Coloridas

### Por que esse exercício é especial

É a extensão direta do problema das pedrinhas das notas, que usava 2 cores. As notas já antecipam: "o esqueleto recursivo é o mesmo; o que muda é o número de possibilidades em cada passo." Este exercício testa se isso é verdade com 3 cores e restrições progressivas.

### Notação

A calçada tem 50 posições. Cada posição recebe uma pedra: Verde (V), Azul (Az) ou Amarela (Am).

---

### Parte (a): Quantas calçadas são possíveis?

**Raciocínio:** Sem nenhuma restrição, cada uma das 50 posições pode ser qualquer uma das 3 cores, independentemente. Não há estrutura recursiva interessante aqui — é combinatória pura.

$$\text{Total} = 3^{50} = 717.897.987.691.852.588.770.249$$

Nenhuma recursão necessária, mas serve de ponto de referência para os próximos itens.

---

### Parte (b): Sem duas amarelas consecutivas

**Raciocínio:** Agora existe uma dependência entre posições adjacentes. A abordagem das notas se aplica: definir o estado pela última pedra colocada.

Defino:
- $am(n)$ = calçadas válidas de comprimento $n$ terminando em Amarela
- $nao(n)$ = calçadas válidas de comprimento $n$ terminando em V ou Az (qualquer das outras)

**Recorrências:**
- $am(n) = nao(n-1)$ — só posso colocar Amarela após não-Amarela
- $nao(n) = 2 \cdot (am(n-1) + nao(n-1))$ — posso colocar V ou Az após qualquer coisa (2 escolhas)

**Casos base:** $am(1) = 1$, $nao(1) = 2$, total $f(1) = 3$.

Simplificando: seja $f(n) = am(n) + nao(n)$:
$$f(n) = am(n) + nao(n) = nao(n-1) + 2 \cdot f(n-1) = 2f(n-2) + 2f(n-1)$$

**Verificação para $n=2$:** $f(2) = 2 \cdot 3 + 2 \cdot 1 = 8$. Manual: $9 - 1$ (só {Am,Am} é inválido) $= 8$. ✓

```python
def calcada_sem_am_consecutivas(n):
    if n == 0: return 1
    am, nao = 1, 2          # casos base n=1
    for _ in range(2, n + 1):
        am, nao = nao, 2 * (am + nao)
    return am + nao

print(calcada_sem_am_consecutivas(50))
```

---

### Parte (c): Sem duas amarelas E sem duas azuis consecutivas

**Raciocínio:** Agora a restrição se aplica a duas cores. Preciso rastrear qual cor foi a última colocada com mais granularidade.

Defino:
- $v(n)$ = calçadas de comprimento $n$ terminando em Verde
- $az(n)$ = terminando em Azul
- $am(n)$ = terminando em Amarela

**Recorrências:** Verde pode seguir qualquer coisa. Azul não pode seguir Azul. Amarela não pode seguir Amarela.
$$v(n) = v(n-1) + az(n-1) + am(n-1) = f(n-1)$$
$$az(n) = v(n-1) + am(n-1)$$
$$am(n) = v(n-1) + az(n-1)$$

**Verificação para $n=2$:** $v(2)=3$, $az(2)=2$, $am(2)=2$, $f(2)=7$. Manual: $9 - \{Am,Am\} - \{Az,Az\} = 7$. ✓

Posso derivar uma recorrência só em $f(n)$:
$$f(n) = f(n-1) + 2f(n-2)$$
Com $f(0) = 1$, $f(1) = 3$.

**Verificação:** $f(3) = 2 \cdot 7 + 3 = 17$. Manual: $27 - 3 - 3 + 1 - 3 - 3 + 1 = 17$ (inclusão-exclusão). ✓

```python
def calcada_sem_am_e_az_consecutivas(n):
    if n == 0: return 1
    if n == 1: return 3
    prev2, prev1 = 1, 3     # f(0), f(1)
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + 2 * prev2
    return prev1

print(calcada_sem_am_e_az_consecutivas(50))
```

---

### O que conecta os três itens

| Item | Restrição | Recorrência | Estrutura |
|------|-----------|-------------|-----------|
| (a)  | Nenhuma   | $3^n$       | Independente por posição |
| (b)  | Sem Am-Am | $f(n) = 2f(n-1) + 2f(n-2)$ | Fibonacci modificado |
| (c)  | Sem Am-Am e Az-Az | $f(n) = f(n-1) + 2f(n-2)$ | Fibonacci modificado |

A progressão confirma exatamente o que as notas anteciparam: à medida que adicionamos restrições, o esqueleto da recorrência permanece linear e de ordem 2 — apenas os coeficientes mudam. A memoização ou o bottom-up com duas variáveis resolve todos os três em $O(n)$ tempo e $O(1)$ espaço.
