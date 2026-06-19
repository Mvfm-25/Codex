# Métodos Numéricos — Trabalho II

**Autor:** Marcus Vinicius Freitas Margarites Filho
**Data:** 18-06-2026

---

## 1. O problema

O enunciado forneceu sete medições parciais da altura de um projétil disparado pelo
obuseiro leve L117 (ângulo de 31°, carga propulsora média), obtidas por sensores
ao longo do voo:

| t (s) | 0 | 3 | 7 | 10 | 14 | 29 | 31 |
|------:|--:|--:|--:|---:|---:|---:|---:|
| h (m) | 1,5 | 1007 | 2075 | 2670 | 3190 | 2339 | 1892 |

O intervalo crítico — em que ocorre o ápice da trajetória — não foi amostrado:
há um salto de 14 s para 29 s, justamente onde a altura deixa de crescer (3190 m)
e passa a cair (2339 m). As duas perguntas a responder são:

- **Qual a altura máxima atingida pelo projétil?**
- **Quanto tempo após o disparo essa altura é atingida?**

Como os dados não cobrem o pico, ambas as respostas exigem **reconstruir a
trajetória entre as medições** e, sobre essa reconstrução, localizar o máximo.

---

## 2. Como obtive meu resultado

### 2.1. Estratégia

Adotei a **interpolação polinomial de Newton por diferenças divididas**. Com
sete pontos, o polinômio interpolador é único e de grau 6; a forma de Newton é
conveniente porque os coeficientes saem diretamente da tabela de diferenças
divididas e a avaliação pode ser feita de modo estável pelo esquema de Horner
aninhado, sem precisar expandir o polinômio na base canônica.

O resultado foi implementado em Java (`InterpolacaoNewton.java`) em três etapas:

1. **Construção dos coeficientes** — montagem da tabela de diferenças divididas
   `dd[i][j]` e extração da diagonal superior como vetor de coeficientes
   `c[0..6]`.
2. **Avaliação do polinômio** — método `avaliar(x)` usando Horner sobre a forma
   de Newton.
3. **Localização do máximo** — em vez de derivar o polinômio analiticamente e
   resolver `P'(t) = 0`, optei por uma busca numérica do máximo, mais robusta:
   uma varredura grosseira em todo o intervalo `[0, 31]` com passo de 0,001 s
   para isolar a região do pico, seguida de refinamento por **busca da seção
   áurea** (`secaoAurea`) com tolerância de 1×10⁻¹² s. Essa combinação evita os
   problemas de cancelamento numérico que surgiriam ao expandir o polinômio de
   grau 6 e procurar raízes da derivada.

### 2.2. Coeficientes obtidos (forma de Newton)

```
c[0] = 1,500000000
c[1] = 335,1666667
c[2] = -9,738095238
c[3] = -0,007142857143
c[4] = 0,0008194186766
c[5] = -3,798595321e-05
c[6] = 1,736562796e-06
```

O programa verifica que o polinômio reproduz exatamente os sete pontos de
entrada (`P(t_i) = h_i` para todo `i`), o que confirma a corretude da
interpolação.

### 2.3. Resultado

```
Altura máxima estimada : 3402,2360 m
Instante do máximo     : 18,6525 s
```

Ou seja, o projétil atinge cerca de **3402 m** aproximadamente **18,65 s** após
o disparo. O valor é fisicamente coerente: o instante cai dentro da janela não
amostrada (entre 14 s e 29 s) e a altura supera os 3190 m medidos aos 14 s, como
seria de esperar para um ponto que está acima da última medição ascendente e
ocorre antes do início da descida observada.

---

## 3. A experiência de extrair informação do ChatGPT

A consulta ao ChatGPT foi **rápida e direta**. Anexei o próprio `t2.pdf` e pedi,
em uma única mensagem, que ele resolvesse o problema pela interpolação de Newton
e explicasse o processo. Não foi necessário fragmentar a tarefa em vários passos,
nem reformular a pergunta: bastou um prompt para obter a solução completa.

Um ponto que considero relevante é que **o modelo trabalhou diretamente sobre o
arquivo entregue**. Por ter acesso ao enunciado original, ele extraiu sozinho os
sete pares (t, h) sem que eu precisasse transcrevê-los, o que reduz o risco de
erro de digitação na entrada e tende a produzir um desenvolvimento mais aderente
ao que de fato foi pedido. Em comparação com um cenário em que os dados são
copiados manualmente, partir do documento dá mais confiança de que o modelo está
resolvendo exatamente o problema proposto.

A resposta veio bem organizada: dados, tabela de diferenças divididas, montagem
do polinômio de Newton, expansão, derivação e, por fim, os pontos críticos com a
seleção do único fisicamente relevante. Houve ainda um comentário sobre a
plausibilidade física do resultado. **Em nenhum momento precisei corrigi-lo** —
não houve alucinação de dados, troca de método ou erro grosseiro de conta que me
obrigasse a intervir e refazer o raciocínio do modelo.

---

## 4. Comparação e conclusões

Ambas as soluções foram desenvolvidas pelo **mesmo método** — interpolação de
Newton por diferenças divididas — e chegaram a **resultados finais
praticamente idênticos**:

| Grandeza | Meu programa (Java) | ChatGPT |
|----------|--------------------:|--------:|
| Instante do máximo | 18,6525 s | ≈ 18,65 s |
| Altura máxima | 3402,236 m | ≈ 3402,24 m |

A concordância nas duas casas decimais relevantes é total. Vale notar que o
caminho até o resultado teve pequenas diferenças de forma: o ChatGPT optou por
**expandir o polinômio na base canônica e derivar analiticamente**, resolvendo
`P'(t) = 0` por via numérica e obtendo três raízes (≈ −25,48; ≈ 18,65; ≈ 52,04),
das quais apenas t ≈ 18,65 s está dentro do voo. Eu, por outro lado, mantive a
forma de Newton e localizei o máximo por **varredura + seção áurea**. Os
coeficientes intermediários reportados em cada abordagem aparecem em
representações diferentes (forma de Newton aninhada no meu caso; polinômio
expandido no caso do ChatGPT), mas isso é apenas uma questão de base: o
polinômio interpolador de grau 6 por sete pontos é único, então as duas
trajetórias coincidem e, com elas, o ponto de máximo.

### Conclusões

- O ChatGPT foi **adequado** para esta tarefa: resolveu corretamente, pelo
  método pedido, e chegou ao mesmo resultado obtido de forma independente pelo
  meu código — o que serve como validação cruzada das duas soluções.
- A experiência de consulta foi **eficiente**: uma única pergunta, baseada no
  PDF original, sem necessidade de correções.
- É preciso, ainda assim, manter a cautela que o próprio enunciado recomenda.
  A confiança no resultado não vem de o modelo "ter acertado", e sim de **dois
  métodos independentes convergirem para o mesmo valor**. Além disso, deve-se ter
  em mente que a interpolação é apenas um modelo matemático ajustado a pontos
  esparsos: ela reconstrói uma curva plausível, mas o pico real depende da
  física do voo, que não foi medida na janela crítica. Para uma aplicação em que
  "uma falha pode ter resultados devastadores", o número 3402 m / 18,65 s deve
  ser lido como a **melhor estimativa possível com os dados disponíveis**, e não
  como uma certeza — idealmente seria confirmado com medições adicionais entre
  14 s e 29 s.
