# Segurança de Sistemas — Simulado P1
## [21-09-26][mvfm]
---
### Prefácio
- Simulado montado sobre a estrutura anunciada na [aula13](../../aula13.md), com o conteúdo das [aulas 02 a 06](../../ss-index.md) e o aprofundamento de [IA/adicoes.md](../../IA/adicoes.md).
- **Estrutura espelhada da prova real** : objetivas espalhadas pelo conteúdo (**2,0 pts**) + 4 dissertativas (**2,0 pts cada**).
	- Cada dissertativa é ancorada num **caso real** — Enigma, VENONA & WEP, *Deep Crack* & 2DES, e um engajamento de pentest. O conceito cobrado é o mesmo dos quatro blocos; o cenário só força a aplicação em vez da recitação.
	- **Hash & MAC** aparecem nas objetivas, que é como o Henry sinalizou que cairiam.
- A **Parte III** é bônus e fora dos quatro blocos — treino de conteúdo, não previsão de prova.
- A **Parte IV** cobre o material de revisão depositado em [`provas/p1`](./) **depois** da aula13 : o deck de *Padding Oracle Attack* (Aula11), o deck de **funções resumo** (Merkle–Damgård, Davies–Meyer, oráculo aleatório, senhas) e o deck de **cifras clássicas** (confusão/difusão, método de Friedman). Inclui os **dois exercícios práticos entregues**, resolvidos passo a passo. Não estava nos quatro blocos anunciados — mas foi entregue como material de P1, então trate como cobrável.
- Gabarito comentado no fim, dentro de blocos recolhíveis. Responda antes de abrir.
- Tempo sugerido : **90 minutos** para as Partes I–III ; reserve **mais 60** para a Parte IV, que tem dois exercícios de cálculo.

---

## Parte I — Objetivas
> 10 questões × 0,2 = **2,0 pontos**. Marque **uma** alternativa.

**1.** O princípio de Kerckhoffs, na formulação de Shannon ("*o inimigo conhece o sistema*"), é sustentado por um argumento prático. Ele é :
- a) Algoritmos secretos são matematicamente mais fracos que algoritmos públicos.
- b) Uma **chave** é um segredo pequeno, trocável e individual; um **algoritmo** é um segredo grande, imutável e coletivo — quando a chave vaza, troca-se a chave; quando o algoritmo vaza, todos recomeçam do zero.
- c) A publicação do algoritmo impede a engenharia reversa do binário.
- d) Sistemas públicos podem dispensar o sigilo da chave, pois a revisão aberta os torna inquebráveis.
- e) O sigilo do algoritmo é dispensável apenas em criptografia assimétrica.

**2.** `A5/1` (GSM), `CSS` (DVD), `Mifare Classic` e `KeeLoq` (chaves de carro) compartilham a mesma história de quebra. Ela é :
- a) Todos usavam chaves de 56 bits, derrubadas por força bruta.
- b) Todos foram quebrados por análise de frequência sobre o tráfego capturado.
- c) Todos eram algoritmos **secretos**, quebrados depois de recuperados por engenharia reversa — e teriam caído antes se tivessem sido publicados.
- d) Todos reutilizavam nonce, caindo por *two-time pad*.
- e) Todos foram quebrados por canais laterais de consumo de energia.

**3.** Um criptograma ilegível apresenta **índice de coincidência ≈ 0,072**, praticamente igual ao do português. A triagem indica :
- a) Cifra polialfabética com chave longa, provavelmente Vigenère.
- b) One-Time Pad, pois o IC do texto aleatório é 0,0385.
- c) Substituição **monoalfabética** ou **transposição** — ambas preservam o IC do idioma.
- d) Cifra de bloco em modo CBC.
- e) O texto não está cifrado, apenas corrompido.

**4.** Seguindo a questão anterior : a contagem de letras do criptograma reproduz **exatamente** as frequências do texto claro. Conclui-se que a cifra é :
- a) Substituição monoalfabética, pois a permutação preserva as contagens.
- b) **Transposição**, pois ela reordena em vez de substituir — as letras são as mesmas, só mudaram de lugar.
- c) Playfair, que cifra digramas.
- d) Vigenère com chave de comprimento 1.
- e) Impossível decidir sem o comprimento da chave.

**5.** A substituição monoalfabética tem $26! \approx 4 \times 10^{26}$ chaves — mais que o AES-88 — e cai em segundos com 200 letras de criptograma. A lição é :
- a) Fatoriais crescem mais devagar que exponenciais.
- b) Análise de frequência é uma forma otimizada de força bruta.
- c) **Tamanho de chave é condição necessária e nunca suficiente** — ele só limita a força bruta; havendo estrutura explorável, o espaço de chaves é irrelevante.
- d) O espaço de chaves só importa para cifras de bloco.
- e) $26!$ é menor que $2^{56}$, portanto o DES é mais seguro.

**6.** Sobre o requisito $|K| \ge |M|$ do One-Time Pad :
- a) É uma recomendação de engenharia, relaxável com um PRNG de boa qualidade.
- b) É um **teorema de Shannon** — com menos chaves que mensagens, nem toda mensagem candidata seria alcançável a partir de $c$, e as descartadas teriam probabilidade menor, violando o sigilo perfeito.
- c) Vale apenas quando a chave é reutilizada.
- d) Decorre do custo computacional do XOR sobre mensagens longas.
- e) Aplica-se a cifras de bloco, não a cifras de fluxo.

**7.** Na hierarquia de modelos de ataque, o adversário **mais poderoso** é o que :
- a) Dispõe apenas do criptograma (COA).
- b) Observa pares $(m,c)$ produzidos por terceiros (KPA).
- c) Escolhe $m$ e recebe $c$ (CPA).
- d) Escolhe $c$ e recebe $m$ (**CCA**) — e é contra ele que uma cifra moderna precisa resistir, no nível **IND-CCA2**.
- e) Conhece o algoritmo, mas não a chave.

**8.** Uma função de hash criptográfica com saída de $n$ bits oferece, contra **colisões**, segurança da ordem de :
- a) $2^{n}$, igual à resistência à pré-imagem.
- b) $2^{n-1}$, pela média da busca exaustiva.
- c) $2^{n/2}$, por conta do **paradoxo do aniversário** — razão de o SHA-256 oferecer só 128 bits contra colisão.
- d) $n^2$, por conta da estrutura Merkle–Damgård.
- e) $2^{2n}$, pois é preciso encontrar duas mensagens.

**9.** Sobre **MAC** e **assinatura digital** :
- a) Ambos fornecem não-repúdio, diferindo apenas no desempenho.
- b) O MAC fornece integridade e autenticidade, mas **não** fornece não-repúdio, porque a chave é simétrica e ambas as partes poderiam ter gerado a tag.
- c) A assinatura digital não fornece integridade, apenas autoria.
- d) O HMAC usa construção aninhada por razões de desempenho em hardware.
- e) `MAC-then-Encrypt` é a ordem recomendada pelos padrões modernos.

**10.** O ataque ***meet-in-the-middle*** contra o **2DES** reduz o custo de quebra para aproximadamente :
- a) $2^{112}$ operações — metade do espaço nominal.
- b) $2^{56}$ operações, idêntico ao DES simples.
- c) $2^{57}$ operações, ao custo de $2^{56}$ de memória — **um bit a mais** que o DES simples.
- d) $2^{64}$ operações, limitado pelo tamanho do bloco.
- e) $2^{128}$ operações, equivalente ao AES-128.

---

## Parte II — Dissertativas
> 4 questões × 2,0 = **8,0 pontos**. Um ou dois parágrafos por item.

### Questão 1 — Caso Enigma : modelo de ataque, metas e Kerckhoffs *(2,0)*
> A Enigma militar alemã de 3 rotores tinha espaço de chaves de $\approx 1{,}59 \times 10^{20}$ (cerca de **67 bits**) e o alto-comando a considerou inquebrável até o fim da guerra. Os Aliados **possuíam** máquinas e conheciam o projeto completo. Ainda assim, o tráfego era lido diariamente em Bletchley Park.

**a)** Explique por que a posse do projeto pelos Aliados **não** é, em si, uma falha do sistema, e o que isso instancia do princípio de Kerckhoffs. Onde estava — corretamente — o segredo da Enigma? *(0,5)*

**b)** Descreva os quatro modelos de ataque em ordem crescente de poder do adversário, indicando o que o atacante possui em cada um, e **classifique o ataque à Enigma** nessa hierarquia, justificando com o insumo concreto que o viabilizava. *(0,6)*

**c)** O **refletor** foi adotado por conveniência operacional : tornava a máquina auto-recíproca, permitindo cifrar e decifrar com a mesma configuração. Enuncie a propriedade que ele impôs à cifra e explique **como ela reduz o espaço de busca** antes de qualquer cálculo. *(0,5)*

**d)** *Exercício de crib-dragging.* Sabe-se que o criptograma abaixo contém a palavra `WETTER`, transmitida diariamente nos boletins meteorológicos :

```
posição :  1  2  3  4  5  6  7  8  9 10 11 12
cifrado :  X  R  W  T  E  K  M  A  B  W  E  T
```

Arrastando o *crib* de 6 letras pelas 7 posições iniciais possíveis, **elimine os alinhamentos impossíveis** e aponte os que sobrevivem. Justifique a regra de eliminação. *(0,4)*

---

### Questão 2 — Casos VENONA e WEP : One-Time Pad e o custo do reuso *(2,0)*
> Entre os anos 1940 e 1980, o projeto **VENONA** decifrou tráfego diplomático soviético cifrado com One-Time Pad. Cinco décadas depois, o **WEP** — proteção padrão das redes Wi-Fi — caiu por um erro com a **mesma** estrutura, apesar de usar RC4 e não papel e lápis.

**a)** Enuncie a definição de **sigilo perfeito** de Shannon e explique, a partir dela, por que o OTP corretamente usado é incondicionalmente seguro — isto é, resiste a um adversário com poder computacional infinito. *(0,6)*

**b)** *Exercício.* Dois textos claros de 8 bits foram cifrados com a **mesma** chave $k$ :

$$c_1 = 11111101 \qquad c_2 = 11111100$$

Calcule $c_1 \oplus c_2$, mostre algebricamente a que valor esse resultado é igual em termos de $m_1$ e $m_2$, e explique por que isso compromete o sigilo **sem que $k$ seja conhecida**. Nomeie o modo de falha. *(0,6)*

**c)** O WEP usa um **IV de 24 bits** concatenado à chave para gerar o fluxo do RC4. Explique por que esse tamanho de IV reproduz, em poucas horas de tráfego, exatamente a falha do item anterior. Cite o modo AEAD moderno que também é catastrófico sob reuso de nonce e o modo projetado para sobreviver a esse erro. *(0,5)*

**d)** Cite os três motivos que inviabilizam o OTP na prática e explique por que o primeiro deles é **circular**. *(0,3)*

---

### Questão 3 — Caso *Deep Crack* : cifras de bloco e *meet-in-the-middle* *(2,0)*
> Em 1998 a EFF construiu o **Deep Crack** por cerca de US$ 250 mil e recuperou uma chave DES em **56 horas**. A resposta da indústria não foi dobrar a cifra — foi triplicá-la, e depois migrar para o AES.

**a)** Preencha e comente a tabela — bloco, chave e segurança efetiva — para **DES**, **2DES**, **3DES (EDE)** e **AES-128**. Explique por que se diz que o DES **não foi quebrado matematicamente**. *(0,6)*

**b)** Descreva o ataque *meet-in-the-middle* sobre o 2DES **passo a passo**, partindo da igualdade que ele explora, e apresente o custo em operações **e** em memória. Em que modelo de ataque ele se enquadra? *(0,8)*

**c)** Responda à pergunta que o caso coloca : **por que a indústria pulou o 2DES e foi direto ao 3DES?** Relacione sua resposta à mesma lição da Enigma (Questão 1c) e da substituição monoalfabética. *(0,4)*

**d)** No 3DES em modo EDE, a operação do meio é um **D** e não um **E**. Qual é a razão de engenharia dessa escolha? *(0,2)*

---

### Questão 4 — Caso de engajamento : pentest de rede *(2,0)*
> Uma empresa contrata um pentest de rede. O reconhecimento revela : um servidor web com formulário de login, uma API REST exposta, um serviço de administração numa porta alta com credencial padrão de fábrica, uma biblioteca de terceiros desatualizada e uma lista de funcionários publicada no site. O testador usa a credencial padrão, obtém acesso e alcança outro host da rede interna.

**a)** Defina **superfície de ataque** e **vetor de ataque**. Em seguida, **classifique cada item do cenário** em uma das duas categorias e explique a relação entre os conceitos. *(0,7)*

**b)** Qual é a estratégia defensiva primária associada à superfície de ataque? Dê dois exemplos concretos aplicáveis ao cenário. *(0,4)*

**c)** Liste as fases de um pentest na ordem correta, mapeando os eventos do cenário às fases correspondentes, e indique **qual é o entregável** que distingue um pentest de uma invasão. *(0,5)*

**d)** Associe pelo menos quatro ferramentas às respectivas fases. Em seguida, indique o **único** elemento que separa, juridicamente, esse engajamento de um crime — a atividade técnica sendo idêntica. *(0,4)*

---

## Parte III — Estudos de caso *(bônus, 1,0)*
> Fora dos quatro blocos anunciados. Aprofundamento com casos reais.

**A) Colisão de hash e assinatura de código.** *(0,5)*
Em 2017 o Google demonstrou a primeira colisão prática de **SHA-1** (ataque *SHAttered*), e o MD5 já produzia colisões em segundos. Explique por que uma colisão — e **não** uma quebra de pré-imagem — é suficiente para comprometer um esquema de assinatura de código, e por que o expoente relevante aqui é $n/2$ e não $n$. Indique o que se usa hoje para uso geral e o que se usa **para senhas**, justificando a diferença.

**B) Cadeia de confiança em boot verificado.** *(0,5)*
Celulares, consoles e a urna eletrônica implementam o mesmo padrão : uma **raiz de confiança em hardware** que verifica a assinatura de cada estágio antes de lhe passar o controle. Descreva a cadeia, explique por que a raiz precisa ser **imutável**, e distinga ***verified boot*** de ***measured boot***. Em seguida, explique o limite que **Ken Thompson** enunciou em *Reflections on Trusting Trust* (1984) e diga qual prática moderna o endereça.

---

## Parte IV — Material de revisão entregue em `provas/p1`

> Conteúdo que chegou **depois** da aula13 : o deck de *Padding Oracle Attack* (Aula11), o deck completo de **funções resumo** e os dois exercícios práticos. Fora dos quatro blocos anunciados, mas entregue explicitamente como material de P1 — trate como cobrável.

### IV.a — Objetivas
> 8 questões. Marque **uma** alternativa.

**11.** Uma mensagem é cifrada em **CBC** com IV aleatório e começa com `dest=80`. O atacante conhece esse trecho do texto claro e quer que o servidor leia `dest=25`. Ele deve enviar :
- a) $\mathrm{IV}' = \mathrm{IV} \oplus (\texttt{...25...})$
- b) $\mathrm{IV}' = \mathrm{IV} \oplus (\texttt{...80...})$
- c) $\mathrm{IV}' = \mathrm{IV} \oplus (\texttt{...80...}) \oplus (\texttt{...25...})$
- d) Não pode ser feito sem a chave $k$.
- e) $\mathrm{IV}' = D_k(c_0) \oplus (\texttt{...25...})$

**12.** O ataque da questão anterior é possível porque :
- a) O AES tem bloco de 128 bits, grande demais para um IV de 128 bits.
- b) No CBC, $m_i = D_k(c_i) \oplus c_{i-1}$ — o bloco anterior entra por **XOR depois da cifra**, então virar um bit dele vira o mesmo bit do texto claro. **Confidencialidade não implica integridade.**
- c) O IV é transmitido em claro, o que é uma falha do padrão.
- d) O gerador de IV do CBC é previsível na maioria das implementações.
- e) É um ataque de texto claro escolhido contra o *key schedule*.

**13.** Por que o ataque do slide altera **somente o IV**, e não um bloco cifrado intermediário?
- a) Porque o IV é o único campo não autenticado.
- b) Porque alterar $c_{i-1}$ com $i \ge 1$ também corromperia $m_{i-1}$ por inteiro, já que $D_k$ de um bloco alterado é imprevisível ; o **IV não é decifrado**, então mexer nele não destrói nada.
- c) Porque o primeiro bloco é o único que contém cabeçalho.
- d) Porque o CBC só permite modificação no primeiro bloco.
- e) Porque os blocos seguintes estão protegidos pelo *padding*.

**14.** No *padding oracle attack*, o atacante varre o último byte do bloco que controla e o oráculo aceita o padding. Ele conclui que $I[15] = R[15] \oplus \texttt{0x01}$, mas precisa **confirmar**. Por quê?
- a) Porque o oráculo pode ter respondido por atraso de rede.
- b) Porque `0x01` não é um padding PKCS#7 válido isoladamente.
- c) Porque o padding aceito pode ter sido `02 02` — caso $m[14]$ valesse `02` por acaso. Alterando $R[14]$ e repetindo, se ainda for aceito o padding era mesmo `01`.
- d) Porque é preciso testar os 256 valores antes de concluir.
- e) Porque o primeiro byte do bloco também precisa ser válido.

**15.** O custo do *padding oracle attack* contra um bloco AES de 16 bytes, e o que ele diz :
- a) $2^{128}$ operações — equivale a força bruta sobre a chave.
- b) $2^{64}$ operações, pelo paradoxo do aniversário sobre o bloco.
- c) No máximo **4096 consultas** ($256 \times 16$), cerca de 2048 em média — e **a chave nunca é atacada**. O ataque contorna a criptografia em vez de enfrentá-la.
- d) $2^{56}$ operações, herdadas do DES.
- e) 256 consultas por bloco, independentemente do tamanho do bloco.

**16.** Sobre a construção de **Merkle–Damgård** :
- a) Seu teorema garante que, se a **função de compressão** é resistente a colisão, o hash resultante também é.
- b) O bloco de padding contém apenas bits `1000...0` ; incluir o comprimento é opcional.
- c) Ela é imune ao ataque de extensão de comprimento, ao contrário da construção esponja.
- d) Ela exige que a função de compressão seja uma permutação.
- e) O SHA-3 a utiliza, assim como MD5, SHA-1 e SHA-2.

**17.** Na função de compressão **Davies–Meyer**, $h(H,m) = E(m,H) \oplus H$, o XOR final com $H$ existe porque :
- a) Melhora a difusão entre blocos consecutivos.
- b) Sem ele a função seria **invertível** — conhecendo $m$, bastaria calcular $D(m,\cdot)$ para caminhar para trás na cadeia e fabricar pré-imagens. O *feed-forward* é o que torna a compressão unidirecional.
- c) Compensa o fato de a mensagem ser usada como texto claro.
- d) Evita que o IV seja zero.
- e) Reduz o custo do *key schedule*, que de outro modo rodaria duas vezes.

**18.** Aplicando o **índice de coincidência** a um criptograma de Vigenère, as colunas dão IC alto ($\approx 0{,}065$) e **todas juntas** para $m = 5$, e também para $m = 10$. O comprimento da chave é :
- a) 10, pois quanto mais colunas, mais confiável a estatística.
- b) **5** — múltiplos do comprimento verdadeiro também sobem, então toma-se o **menor** $m$ em que todas as colunas sobem.
- c) 50, o mínimo múltiplo comum.
- d) Indeterminado sem aplicar também o exame de Kasiski.
- e) 2, a razão entre os dois candidatos.

---

### IV.b — Dissertativa 5 : o caso do *padding oracle* *(2,0)*
> Em 2002 **Serge Vaudenay** mostrou que implementações de SSL/TLS, IPsec e WTLS podiam ter seu tráfego decifrado sem que a chave fosse atacada. Em 2010 o mesmo defeito derrubou aplicações ASP.NET em produção. Em 2013 o **Lucky Thirteen** o ressuscitou depois de a indústria já ter "corrigido" o problema.

**a)** Defina o que é um **oráculo de padding** e cite as **três** formas pelas quais um sistema pode se tornar um sem que o programador perceba. *(0,4)*

**b)** Descreva o ataque **passo a passo** para recuperar os dois últimos bytes de um bloco. Use a notação $I = D_k(c)$ para o valor intermediário e $R$ para o bloco que o atacante controla, e mostre de onde sai cada igualdade. *(0,8)*

**c)** Apresente o custo em consultas por bloco de 16 bytes e compare com a força bruta sobre AES-128. Em que **modelo de ataque** (COA / KPA / CPA / CCA) o padding oracle se enquadra, e por quê? *(0,4)*

**d)** A primeira correção foi *"sempre gerar o mesmo erro"*. Explique por que ela **não bastou**, qual foi a segunda correção, e por que a correção **estrutural** — `Encrypt-then-MAC` ou AEAD — elimina o ataque em vez de apenas dificultá-lo. *(0,4)*

---

### IV.c — Exercício prático : criptoanálise de cifra de fluxo com reuso de chave
> Reprodução do exercício entregue. Mensagens cifradas com **a mesma chave** por XOR byte a byte. Objetivo : recuperar os textos claros e a chave.

**Tabela de apoio fornecida :**

| Par | XOR | | Letra | ASCII |
|---|---|---|---|---|
| `a`⊕`b` | `00000011` | | `a` | `01100001` |
| `a`⊕`c` | `00000010` | | `b` | `01100010` |
| `a`⊕`d` | `00000101` | | `c` | `01100011` |
| `b`⊕`c` | `00000001` | | `d` | `01100100` |
| `b`⊕`d` | `00000110` | | | |
| `c`⊕`d` | `00000111` | | | |
| iguais | `00000000` | | | |

**Primeiro :**
```
C1 : 00000000 00000001 00000000
C2 : 00000011 00000000 00000001
C3 : 00000010 00000011 00000010
```

**Segundo :**
```
C1 : 00000000 00000000 00000000 00000001
C2 : 00001111 00001111 00000010 00001110
C3 : 00001111 00000000 00001111 00000010
C4 : 00001110 00001110 00001110 00000000
```

**Terceiro :**
```
C1 : 00000011 00000011 00000001 00000001 00000010
C2 : 00000000 00000001 00000010 00000011 00000011
C3 : 00000001 00000000 00000011 00000000 00000001
C4 : 00000001 00000010 00000000 00000001 00000000
```

**Pede-se, para cada conjunto :** a matriz de diferenças $C_i \oplus C_j$ por posição, o que ela revela sobre os textos claros, e — quando possível — o texto claro e a chave.

---

### IV.d — Exercício prático : hash por Merkle–Damgård
> Reprodução do exercício entregue. Função de compressão **Davies–Meyer sobre AES** : $H_i = E(M_i,\, H_{i-1}) \oplus H_{i-1}$, isto é, **AES-128 sem padding, usando o bloco de mensagem como chave e o estado encadeado como texto claro**. Em todos os casos $H_0 = \texttt{00000000000000000000000000000000}$.

**Exercício 1 — 2 blocos.** Calcule $H_2$.
```
M1 = 00112233445566778899aabbccddeeff
M2 = ffeeddccbbaa99887766554433221100
```

**Exercício 2 — 3 blocos.** Calcule $H_3$.
```
M1 = 0123456789abcdef0123456789abcdef
M2 = fedcba9876543210fedcba9876543210
M3 = 00112233445566778899aabbccddeeff
```

**Exercício 3 — 3 blocos.** Calcule $H_3$.
```
M1 = aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
M2 = bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
M3 = cccccccccccccccccccccccccccccccc
```

---
---

## Gabarito comentado

> [!success]- **Parte I — Objetivas**
> **1 — (b).** O argumento é prático, não filosófico : algoritmos vazam, são extraídos por engenharia reversa e precisam ser auditados; chaves podem ser trocadas, algoritmos não. É a razão de os padrões saírem de competições públicas — DES (1977), AES/Rijndael (2001), SHA-3/Keccak (2012), ML-KEM e ML-DSA (2024).
>
> **2 — (c).** *Security through obscurity*, com falha documentada e repetida. A raridade do atacante capaz não é propriedade do sistema.
>
> **3 — (c).** O IC é a ferramenta de **triagem** : ele diz que tipo de cifra está na frente antes de qualquer tentativa de quebra. A permutação monoalfabética não altera o IC, e a transposição também não. IC ≈ 0,038 indicaria polialfabética ou texto aleatório.
>
> **4 — (b).** A transposição reordena, então as frequências ficam idênticas às do texto claro — o que torna a análise de frequência inútil e, por isso mesmo, é o teste que **identifica** uma transposição. Na monoalfabética o *formato* da distribuição se preserva, mas associado a outras letras.
>
> **5 — (c).** Mesma lição do refletor da Enigma e do 2DES contra MITM : três instâncias do mesmo princípio em escalas diferentes de sofisticação.
>
> **6 — (b).** É teorema, não inconveniência. Cuidado com (a) : trocar a chave verdadeiramente aleatória por um PRNG deixa de ser OTP e passa a ser uma cifra de fluxo com segurança **computacional**.
>
> **7 — (d).** COA → KPA → CPA → CCA. Um sistema é avaliado pelo modelo mais forte que resiste; o mínimo aceitável hoje é IND-CCA2, porque na prática o atacante frequentemente consegue escolher entradas e observar respostas — foi assim que o *padding oracle* de Vaudenay (2002) quebrou implementações de TLS sem tocar na chave.
>
> **8 — (c).** Paradoxo do aniversário. Pré-imagem e 2ª pré-imagem custam $2^{n}$.
>
> **9 — (b).** A chave do MAC é simétrica : qualquer tag que Alice gerou, Bob também poderia ter gerado. Sobre (d) : o HMAC é aninhado para resistir ao **ataque de extensão de comprimento**, ao qual $H(k \| m)$ é vulnerável em hashes Merkle–Damgård. Sobre (e) : o correto é **`Encrypt-then-MAC`** — `MAC-then-Encrypt` é o erro do SSL/TLS antigo.
>
> **10 — (c).** $\approx 2^{57}$ operações e $2^{56}$ de memória. Duplicar a cifra comprou **um bit**, ao custo de dobrar o tempo de execução.

> [!success]- **Questão 1 — Caso Enigma**
> **a)** Kerckhoffs, instanciado na prática : os Aliados tinham máquinas e conheciam o projeto completo, e a segurança dependia inteiramente da **chave diária** (ordem e escolha dos rotores, posições iniciais, anéis e a fiação do plugboard) — que é exatamente onde o segredo deve estar. O problema não foi o projeto ser conhecido; foi ele ter um **defeito estrutural**. Resposta que atribua a quebra à "divulgação do projeto" inverte o princípio da disciplina.
>
> **b)**
>
> | Modelo | Sigla | O que o atacante tem |
> |---|---|---|
> | Só criptograma | COA | apenas $c$ |
> | Texto claro conhecido | KPA | pares $(m,c)$ **observados** |
> | Texto claro escolhido | CPA | ele **escolhe** $m$ e recebe $c$ |
> | Criptograma escolhido | CCA | ele escolhe $c$ e recebe $m$ |
>
> A Enigma caiu em **KPA** — texto claro conhecido. O insumo eram os *cribs* : boletins meteorológicos transmitidos todo dia no mesmo horário e formato (`WETTERVORHERSAGE`), saudações padronizadas e o `HEILHITLER` ao fim das transmissões. Ponto extra por observar que nenhum desses vícios era falha da máquina — **o elo humano quebrou primeiro** : chaves de mensagem repetidas, operadores escolhendo `AAA` ou as iniciais da namorada como posição inicial.
>
> **c)** Como a corrente volta pelos rotores por caminho diferente do que foi, a saída nunca coincide com a entrada : **nenhuma letra jamais é cifrada como ela mesma**. A consequência é que, ao arrastar um *crib* pelo criptograma, **qualquer posição em que uma letra do crib coincida com a letra correspondente do cifrado está eliminada sem nenhum cálculo**. Isso descartava a grande maioria dos alinhamentos instantaneamente, e só os sobreviventes iam para a **Bombe** de Turing — que não testava $10^{20}$ chaves, mas derivava contradições lógicas a partir do *crib* e eliminava blocos inteiros do espaço de uma vez. A redução é de **espaço de busca**, não força bruta.
>
> **d)** Regra : elimina-se o alinhamento em que **alguma** letra do *crib* coincide com a letra do criptograma na mesma posição, porque a Enigma nunca cifra uma letra como ela mesma.
>
> | Posição inicial | Cifrado sobreposto | Colisão | Veredito |
> |---|---|---|---|
> | 1 | `X R W T E K` | `T`↔`T` (pos. 4) | **eliminado** |
> | 2 | `R W T E K M` | `T`↔`T` (pos. 3) | **eliminado** |
> | 3 | `W T E K M A` | `W`↔`W` (pos. 1) | **eliminado** |
> | 4 | `T E K M A B` | `E`↔`E` (pos. 2) | **eliminado** |
> | 5 | `E K M A B W` | — | **possível** |
> | 6 | `K M A B W E` | — | **possível** |
> | 7 | `M A B W E T` | `E`↔`E` (pos. 5) | **eliminado** |
>
> Sobrevivem as posições **5** e **6** : 5 dos 7 alinhamentos caem sem uma única operação criptográfica. É a redução que torna o problema tratável.

> [!success]- **Questão 2 — Casos VENONA e WEP**
> **a)** Sigilo perfeito : $\Pr[M{=}m \mid C{=}c] = \Pr[M{=}m]$ — observar o criptograma não altera em nada a distribuição de probabilidade sobre as mensagens. No OTP, para **qualquer** mensagem candidata $m'$ do mesmo tamanho existe exatamente uma chave $k' = c \oplus m'$ que a produziria, e todas são igualmente prováveis. O criptograma, portanto, não carrega informação sobre a mensagem — não há o que computar, e poder computacional infinito não ajuda. É a distinção entre segurança **perfeita** (OTP) e **computacional** (AES, RSA, ChaCha20 — tudo que se usa).
>
> **b)** $c_1 \oplus c_2 = 11111101 \oplus 11111100 = \mathbf{00000001}$. A chave se cancela :
>
> $$c_1 \oplus c_2 = (m_1 \oplus k) \oplus (m_2 \oplus k) = m_1 \oplus m_2$$
>
> O resultado é o XOR dos **textos claros**, obtido sem conhecer $k$. A partir dele, a redundância do idioma e o *crib-dragging* recuperam ambas as mensagens. O modo de falha é o **two-time pad**, e é exatamente o que VENONA explorou : os soviéticos reutilizaram páginas de bloco de chave. No exemplo, $m_1 \oplus m_2 = 00000001$ diz que as mensagens diferiam num único bit — por exemplo `H` (`01001000`) e `I` (`01001001`).
>
> **c)** Um IV de 24 bits tem apenas $2^{24} \approx 16{,}7$ milhões de valores. Numa rede movimentada isso se esgota em poucas horas, e dois pacotes com o mesmo IV e a mesma chave produzem o **mesmo fluxo** RC4 — literalmente o caso do item (b), com o XOR dos pacotes revelando o XOR dos textos claros. Modo moderno catastrófico sob reuso de nonce : **AES-GCM**. Projetado para sobreviver ao erro : **AES-GCM-SIV**. A lição de 1917 é a mesma de hoje.
>
> **d)** (i) **Distribuição** da chave; (ii) **aleatoriedade real**, não um PRNG; (iii) **não-reuso**, cada bit serve uma única vez. O primeiro é circular : é preciso transportar com segurança tanto material de chave quanto mensagem se pretende enviar — mas se já existe um canal seguro para isso, envie a mensagem por ele e dispense o OTP.

> [!success]- **Questão 3 — Caso *Deep Crack***
> **a)**
>
> | Cifra | Bloco | Chave | Segurança efetiva | Situação |
> |---|---|---|---|---|
> | **DES** (1977) | 64 bits | 56 bits | $2^{56}$ | **quebrada** — *Deep Crack*, 56 h, 1998; hoje horas em FPGA barata |
> | **2DES** | 64 bits | 112 bits | $\mathbf{2^{57}}$ | inútil |
> | **3DES** (EDE) | 64 bits | 168 bits | $\approx 2^{112}$ | obsoleta (NIST descontinuou em 2023) |
> | **AES-128** | 128 bits | 128 bits | $2^{128}$ | **padrão atual** |
>
> O DES não foi quebrado matematicamente : a estrutura Feistel resistiu bem, e sua resistência à criptoanálise diferencial mostrou que a NSA já conhecia a técnica nos anos 70. Ele caiu porque **a Lei de Moore alcançou o espaço de chaves** — e os 56 bits foram decisão política, contestada já na época.
>
> **b)** O 2DES calcula $c = E_{k_2}(E_{k_1}(m))$, aparentando 112 bits. O ataque explora
>
> $$E_{k_1}(m) = D_{k_2}(c)$$
>
> — o valor intermediário é alcançável pelos dois lados. Com **um** par conhecido $(m,c)$ :
> 1. Calcule $E_{k}(m)$ para todas as $2^{56}$ chaves e guarde numa tabela hash — $2^{56}$ operações, $2^{56}$ de memória.
> 2. Calcule $D_{k'}(c)$ para todas as $2^{56}$ chaves, buscando cada resultado na tabela.
> 3. Cada colisão é um candidato $(k_1,k_2)$; confirme com um **segundo** par conhecido.
>
> Custo $\approx 2^{57}$ operações. É um ataque de **texto-claro conhecido (KPA)** que troca memória por tempo.
>
> **c)** Porque o 2DES **não compra segurança**: 112 bits nominais entregam 57 bits reais, um único bit a mais que o DES, ao custo de dobrar o tempo de execução. O 3DES em EDE resiste com $\approx 2^{112}$, e foi essa a razão de pular a etapa intermediária. A lição é a mesma da Enigma ($10^{20}$ chaves que não protegeram nada, porque o ataque não era por força bruta) e da substituição monoalfabética ($26!$ chaves quebradas por frequência) : **contar bits de chave não é medir segurança**.
>
> **d)** Com $k_1 = k_2 = k_3$, o EDE $E_{k_3}(D_{k_2}(E_{k_1}(m)))$ colapsa em $E_k(m)$ — DES simples. A escolha garante **compatibilidade retroativa com equipamento legado**.

> [!success]- **Questão 4 — Caso de engajamento**
> **a)** **Superfície de ataque** é o **conjunto** de todos os pontos em que um atacante não autorizado pode tentar entrar ou extrair dados. **Vetor de ataque** é o caminho específico efetivamente usado numa tentativa concreta — um vetor é um **elemento da superfície, explorado**. Classificação do cenário :
>
> | Item | Categoria |
> |---|---|
> | Formulário de login | superfície |
> | API REST exposta | superfície |
> | Porta alta do serviço de administração | superfície |
> | Biblioteca de terceiros desatualizada | superfície |
> | Lista de funcionários publicada | superfície (**humana** — insumo de phishing) |
> | **Uso da credencial padrão de fábrica** | **vetor** |
>
> Só o último é vetor : é o que foi efetivamente percorrido. Tudo o mais permaneceu como possibilidade.
>
> **b)** A estratégia primária é **reduzir a superfície**. No cenário : desativar ou restringir por rede o serviço de administração e trocar a credencial padrão; atualizar ou remover a biblioteca de terceiros. Também valem : retirar a lista de funcionários do site público e limitar os endpoints expostos da API.
>
> **c)** Reconhecimento (passivo e ativo) → varredura e enumeração → exploração → pós-exploração e movimentação lateral → **relatório**. Mapeando : a lista de funcionários no site é reconhecimento **passivo**; a descoberta da porta alta e da versão da biblioteca é varredura e enumeração; o uso da credencial padrão é exploração; alcançar outro host interno é **movimentação lateral**. O **relatório** é o entregável, e é o que distingue o pentest de uma invasão — sem ele houve intrusão, não avaliação.
>
> **d)** `nmap` (varredura de portas e detecção de serviço), `Nessus`/`OpenVAS` (varredura de vulnerabilidade), `Burp Suite` (interceptação e teste web — o formulário e a API), `Metasploit` (exploração), `Wireshark` (análise de tráfego), `hashcat`/`John` (quebra de hash offline, na pós-exploração). O elemento que separa o engajamento de um crime é o **escopo autorizado por escrito** — as regras de engajamento, definindo alvos, janelas de tempo e técnicas permitidas. A atividade técnica é idêntica; só a autorização muda a classificação legal. Note que alcançar **outro host** é exatamente o ponto em que o escopo escrito decide se houve movimentação lateral autorizada ou invasão.

> [!success]- **Parte III — Estudos de caso**
> **A)** Num esquema de assinatura de código assina-se o **hash** do binário, não o binário. Se o atacante encontra $m \ne m'$ com $H(m) = H(m')$, basta submeter à assinatura o instalador legítimo $m$ e distribuir o malicioso $m'$ : **a assinatura é válida para os dois**, porque é a mesma. Não é preciso quebrar pré-imagem nem tocar na chave privada. O expoente relevante é $n/2$ pelo **paradoxo do aniversário** — o atacante escolhe **ambas** as mensagens, e encontrar um par qualquer que colida é quadraticamente mais barato que atingir um alvo fixo. Foi assim que MD5 e SHA-1 saíram de uso : colisões em segundos no MD5, colisão real demonstrada no SHA-1 pelo *SHAttered* em 2017. Hoje : **SHA-256 / SHA-3** para uso geral; **bcrypt, scrypt ou Argon2** para senhas. A diferença é que, para senhas, o que se quer é uma função deliberadamente **lenta** e com *salt* — um SHA puro é rápido demais, e rapidez é vantagem do atacante offline. Nota histórica : o malware **Flame** (2012) usou uma colisão de MD5 para forjar um certificado de assinatura de código, o que torna este cenário literal e não hipotético.
>
> **B)** A cadeia :
>
> $$\underbrace{\text{raiz de confiança}}_{\text{hardware, imutável}} \to \text{firmware} \to \text{bootloader} \to \text{kernel} \to \text{aplicação}$$
>
> Cada elo **verifica a assinatura digital do próximo antes de lhe passar o controle**. A raiz precisa ser imutável porque **a cadeia só é tão forte quanto ela** — daí ser hardware, com a chave pública gravada de fábrica e sem caminho de escrita. Exemplos : UEFI Secure Boot, Android Verified Boot e o MSE da urna.
>
> | | **Verified boot** | **Measured boot** |
> |---|---|---|
> | O que faz | verifica a assinatura e **recusa** executar se falhar | calcula o hash de cada estágio e **registra** num TPM |
> | Resultado da falha | a máquina não dá boot | dá boot, mas o registro denuncia |
> | Uso típico | dispositivo dedicado, urna, console, celular | atestação remota, BitLocker |
>
> **O limite de Thompson** : um compilador pode ser modificado para inserir uma porta dos fundos ao compilar um programa alvo **e** para se reinserir ao compilar a si mesmo. Após uma recompilação, o binário carrega o ataque e o código-fonte do compilador volta a ficar limpo — nenhuma auditoria de fonte encontra nada, porque não há nada no fonte. *"Você não pode confiar em código que não escreveu inteiramente você mesmo."* Consequência : auditar o fonte prova propriedades **do fonte**; ligar isso ao binário exige confiar também no compilador, nas bibliotecas, no sistema de build e na máquina que compilou. A prática moderna que endereça isso são as **compilações reprodutíveis** (*reproducible builds*) — processo determinístico em que mesmo fonte e mesmas ferramentas geram o mesmo binário bit a bit, permitindo que auditores independentes recompilem e **comparem hashes** em vez de confiar em quem compilou. Debian, Tails e o Bitcoin Core investem nisso há anos.

> [!success]- **Parte IV.a — Objetivas do material de revisão**
> **11 — (c).** $m_0 = D_k(c_0) \oplus \mathrm{IV}$. Para obter $m_0' = m_0 \oplus \Delta$ basta enviar $\mathrm{IV}' = \mathrm{IV} \oplus \Delta$, e $\Delta$ é a diferença entre o que está lá e o que se quer pôr : $(\texttt{...80...}) \oplus (\texttt{...25...})$. Note o pressuposto : o atacante **já conhece** aquele trecho do claro. O ataque é cirúrgico — ele reescreve, não descobre.
>
> **12 — (b).** A maleabilidade é do **modo**, não da primitiva : trocar DES por AES não muda nada. Esta é a questão que cobra a frase "confidencialidade não implica integridade", e a razão de existir AEAD.
>
> **13 — (b).** O IV não passa por $D_k$ — ele só entra no XOR. Alterar um bloco cifrado real destrói o bloco de texto claro correspondente, o que denuncia a adulteração ; alterar o IV é invisível.
>
> **14 — (c).** O falso positivo de `02 02`. É o detalhe de implementação que separa quem leu o ataque de quem o executou.
>
> **15 — (c).** $256 \times 16 = 4096$ consultas no pior caso por bloco, $\approx 2048$ em média, contra $2^{128}$ da força bruta. E o ponto conceitual : **a chave nunca é atacada**.
>
> **16 — (a).** É o teorema de Merkle–Damgård. Sobre (b) : o comprimento no bloco de padding é o *reforço* de Merkle–Damgård e é **obrigatório** — sem ele, mensagens de tamanhos diferentes colidem por construção. Sobre (c) : é o inverso — Merkle–Damgård **sofre** extensão de comprimento, e a esponja do SHA-3 é que é imune. Sobre (e) : o SHA-3 **não** usa Merkle–Damgård.
>
> **17 — (b).** Sem o *feed-forward*, $E(m,H)$ é invertível por $D(m,\cdot)$ e a cadeia se percorre para trás. Sobre (c) : cuidado com a inversão — no Davies–Meyer a **mensagem é a chave** e o estado encadeado é o texto claro, não o contrário.
>
> **18 — (b).** Múltiplos do comprimento verdadeiro também dão IC alto, com menos dados por coluna. Toma-se o **menor** $m$ em que **todas** as colunas sobem juntas — não a maior média.

> [!success]- **Parte IV.b — Dissertativa 5 : padding oracle**
> **a)** Um **oráculo de padding** é qualquer comportamento observável do sistema que revele se o padding de um criptograma submetido era **válido ou não** após a decifragem. Basta **um bit** de resposta por consulta. As três formas :
>
> 1. **Erro explícito distinguível** — o caso clássico do HTTPS antigo : `403` para padding inválido, `404` para padding válido mas mensagem inválida.
> 2. **Ausência de resposta** — o sistema simplesmente não devolve o que devolveria no caso válido.
> 3. **Tempo de resposta** — um caminho de código roda mais que o outro. É o oráculo que **sobra** depois de unificarem as mensagens de erro.
>
> **b)** Seja $c$ o bloco alvo, $I = D_k(c)$ o **valor intermediário** e $R$ o bloco que o atacante põe no lugar do bloco anterior. O sistema calcula
> $$m = I \oplus R$$
>
> *Último byte :*
> 1. Fixe $R$ arbitrário e varra $R[15]$ pelos 256 valores.
> 2. Quando o oráculo aceitar, o padding mais provável é `01`, ou seja $m[15] = \texttt{0x01}$. De $m[15] = I[15] \oplus R[15]$ :
> $$I[15] = R[15] \oplus \texttt{0x01}$$
> 3. **Confirme** alterando $R[14]$ e repetindo : se ainda for aceito, o padding era mesmo `01` e não um `02 02` acidental.
>
> *Penúltimo byte :*
> 4. Agora o alvo é o padding `02 02`. Force $m[15] = \texttt{0x02}$ fixando $R[15] = I[15] \oplus \texttt{0x02}$ — possível porque $I[15]$ já é conhecido.
> 5. Varra $R[14]$ até o oráculo aceitar. Então $m[14] = \texttt{0x02}$ e
> $$I[14] = R[14] \oplus \texttt{0x02}$$
>
> Repetindo com `03 03 03`, `04 04 04 04`, … recupera-se $I$ inteiro. O texto claro **verdadeiro** sai então do bloco anterior **real** : $m_i = I \oplus c_{i-1}$. Para o bloco seguinte, desliza-se a janela — o primeiro bloco cifrado passa a fazer o papel de IV.
>
> **c)** No máximo $256$ consultas por byte $\times\, 16$ bytes $= \mathbf{4096}$ por bloco, $\approx 2048$ em média. Contra $2^{128}$ da força bruta sobre AES-128 — alguns milhares de requisições HTTP contra um número que não cabe no universo. O modelo é **CCA** (texto cifrado escolhido) : o atacante **escolhe** os criptogramas que submete e observa a resposta do sistema. E é CCA **adaptativo** (CCA2), porque cada consulta depende do resultado da anterior. É a justificativa empírica de o padrão moderno ser IND-CCA2 : o adversário CCA não é uma abstração teórica, é um `curl` em laço.
>
> **d)** *"Sempre gerar o mesmo erro"* não bastou porque o oráculo não precisa ser uma **mensagem** — os dois caminhos de código continuavam levando **tempos** diferentes, e o **Lucky Thirteen** (2013) extraiu exatamente esse sinal. A segunda correção foi **tempo de resposta constante**, que é necessária mas frágil : depende de o compilador não otimizar, de o cache não variar e de ninguém quebrar a propriedade numa refatoração futura.
>
> A correção **estrutural** é `Encrypt-then-MAC` ou **AEAD** (AES-GCM, ChaCha20-Poly1305). Com o MAC calculado **sobre o criptograma**, a tag é verificada **antes** de qualquer decifragem : um criptograma adulterado é rejeitado sem que a chave seja usada e sem que o padding chegue a ser olhado. A diferença de natureza é o ponto da resposta — as duas primeiras correções tentam **esconder** o bit que vaza ; a terceira faz com que **não exista bit a vazar**, porque o caminho de código que o produzia nunca é alcançado.

> [!success]- **Parte IV.c — Criptoanálise de cifra de fluxo : resolução**
> **O método, antes dos números.** Com a chave reutilizada, $C_i \oplus C_j = P_i \oplus P_j$ : a chave se cancela e sobram as **diferenças entre os textos claros**. Isso é tudo o que o reuso vaza — e é também tudo o que ele *não* vaza, ponto ao qual voltamos no fim.
>
> Ler uma diferença é ler a tabela ao contrário : `00` ⇒ os dois caracteres são **iguais** ; `03` ⇒ são `a` e `b` (em alguma ordem) ; e assim por diante.
>
> ---
> **Primeiro conjunto** — matriz de diferenças :
>
> | | $C_1{\oplus}C_2$ | $C_1{\oplus}C_3$ | $C_2{\oplus}C_3$ | Leitura |
> |---|---|---|---|---|
> | pos. 1 | `03` | `02` | `01` | $\{a,b\}$, $\{a,c\}$, $\{b,c\}$ |
> | pos. 2 | `01` | `02` | `03` | $\{b,c\}$, $\{a,c\}$, $\{a,b\}$ |
> | pos. 3 | `01` | `02` | `03` | idem |
>
> **Posição 1.** Procura-se $(x,y,z)$ com $x{\oplus}y = \texttt{03}$, $x{\oplus}z = \texttt{02}$, $y{\oplus}z = \texttt{01}$. Testando as quatro letras : $x=a \Rightarrow y=b,\, z=c$, e $b \oplus c = \texttt{01}$ ✓. Nenhuma outra escolha de $x$ fecha (para $x=b$ não existe $z$ com $b{\oplus}z=\texttt{02}$ ; para $x=c$ ou $x=d$ não existe $y$ com diferença `03`). **Solução única : $(a, b, c)$.**
>
> **Posições 2 e 3.** Mesmo raciocínio com o padrão `01/02/03` : só $x=c$ fecha, dando $(c, b, a)$. Único.
>
> Portanto :
>
> $$P_1 = \texttt{acc} \qquad P_2 = \texttt{bbb} \qquad P_3 = \texttt{caa}$$
>
> **A chave** sai de $K = C_1 \oplus P_1$ :
>
> | | byte 1 | byte 2 | byte 3 |
> |---|---|---|---|
> | $C_1$ | `00000000` | `00000001` | `00000000` |
> | $P_1$ (`a`,`c`,`c`) | `01100001` | `01100011` | `01100011` |
> | $K$ | `01100001` | `01100010` | `01100011` |
> | | `a` | `b` | `c` |
>
> $$\boxed{K = \texttt{abc}}$$
>
> *Verificação :* $C_2 \oplus K = \texttt{bbb}$ ✓ e $C_3 \oplus K = \texttt{caa}$ ✓.
>
> ---
> **Segundo conjunto** — matriz de diferenças :
>
> | | $d_{12}$ | $d_{13}$ | $d_{14}$ | $d_{23}$ | $d_{24}$ | $d_{34}$ |
> |---|---|---|---|---|---|---|
> | pos. 1 | `0f` | `0f` | `0e` | **`00`** | `01` | `01` |
> | pos. 2 | `0f` | **`00`** | `0e` | `0f` | `01` | `0e` |
> | pos. 3 | `02` | `0f` | `0e` | `0d` | `0c` | `01` |
> | pos. 4 | `0f` | `03` | `01` | `0c` | `0e` | `02` |
>
> **O que a matriz entrega de graça**, sem nenhuma hipótese : os dois zeros. Na posição 1, $P_2$ e $P_3$ têm o **mesmo** caractere ; na posição 2, $P_1$ e $P_3$ têm o mesmo. Diferenças de `01` indicam letras adjacentes ; `0f` indica caracteres a 15 posições de distância no bloco.
>
> **A observação que o exercício exige.** As diferenças chegam a `0f` — mas a maior diferença possível dentro de $\{a,b,c,d\}$ é $c \oplus d = \texttt{07}$. **A tabela fornecida no enunciado não cobre este conjunto** : o alfabeto aqui é mais largo (uma faixa alinhada de 16 caracteres, do tipo `a`–`p`). É um descompasso do próprio material, e vale apontá-lo.
>
> Uma solução **consistente**, seguindo o padrão do primeiro conjunto ($K = \texttt{abc}$) :
>
> $$K = \texttt{abcd} \;\Rightarrow\; P_1 = \texttt{abce},\; P_2 = \texttt{nmaj},\; P_3 = \texttt{nblf},\; P_4 = \texttt{olmd}$$
>
> Confere com a estrutura : $P_2[1] = P_3[1] = \texttt{n}$ ✓ e $P_1[2] = P_3[2] = \texttt{b}$ ✓.
>
> ---
> **Terceiro conjunto** — matriz de diferenças :
>
> | | $d_{12}$ | $d_{13}$ | $d_{14}$ | $d_{23}$ | $d_{24}$ | $d_{34}$ |
> |---|---|---|---|---|---|---|
> | pos. 1 | `03` | `02` | `02` | `01` | `01` | **`00`** |
> | pos. 2 | `02` | `03` | `01` | `01` | `03` | `02` |
> | pos. 3 | `03` | `02` | `01` | `01` | `02` | `03` |
> | pos. 4 | `02` | `01` | **`00`** | `03` | `02` | `01` |
> | pos. 5 | `01` | `03` | `02` | `02` | `03` | `01` |
>
> De graça : $P_3 = P_4$ na posição 1, e $P_1 = P_4$ na posição 4.
>
> Aqui todas as diferenças estão em $\{\texttt{00},\texttt{01},\texttt{02},\texttt{03}\}$, o que confina os quatro caracteres de cada posição a um bloco **alinhado** de 4 símbolos. E de novo a tabela do enunciado não serve : $\{a,b,c,d\}$ cruza a fronteira de alinhamento (por isso $a \oplus d = \texttt{05}$, e não `03`). Na posição 2, por exemplo, seria preciso $x{\oplus}y=\texttt{02}$, $x{\oplus}z=\texttt{03}$ e $x{\oplus}w=\texttt{01}$ simultaneamente — **impossível** dentro de $\{a,b,c,d\}$, e imediato dentro de $\{d,e,f,g\}$, que é alinhado.
>
> Uma solução **consistente** sobre $\{d,e,f,g\}$ :
>
> $$K = \texttt{eeeee} \;\Rightarrow\; P_1 = \texttt{ffddg},\; P_2 = \texttt{edgff},\; P_3 = \texttt{defed},\; P_4 = \texttt{dgede}$$
>
> ---
> **A lição, e ela é o objetivo do exercício.** Repare no que aconteceu nos conjuntos 2 e 3 : as diferenças são **completamente** determinadas, e o texto claro **não é**. Qualquer chave produz um conjunto de textos claros igualmente consistente — os deslocados por um XOR constante.
>
> Isso não é defeito do exercício, é a estrutura do problema. O reuso de chave vaza $P_i \oplus P_j$, e **só isso** ; o que converte diferenças em texto é a **redundância do idioma** ou um **crib**. Com mensagens de 3 a 5 letras sem estrutura linguística, não há redundância a explorar, e o ataque para onde parou. Foi exatamente por isso que o **VENONA** levou décadas e não semanas : mesmo com o two-time pad estabelecido, decifrar exigiu acumular tráfego, cribs e cadernos de código capturados.
>
> O primeiro conjunto só fecha em solução única porque o enunciado restringe o alfabeto a quatro letras — a restrição de alfabeto está fazendo, ali, o papel que a redundância do idioma faz no mundo real.

> [!success]- **Parte IV.d — Hash por Merkle–Damgård : resolução**
> **A construção.** Davies–Meyer sobre AES-128, iterado à Merkle–Damgård :
> $$H_i = E(M_i,\, H_{i-1}) \oplus H_{i-1}, \qquad H_0 = \texttt{00…00}$$
>
> O erro mais comum é inverter os papéis : **o bloco de mensagem é a chave** do AES, e o estado encadeado $H_{i-1}$ é o bloco de entrada. Na ferramenta online : modo **ECB**, **sem padding**, chave = $M_i$, texto = $H_{i-1}$, tudo em hexadecimal. Depois, XOR do resultado com $H_{i-1}$ — esquecer esse XOR final é o segundo erro mais comum, e é o que tornaria a função invertível.
>
> ---
> **Exercício 1 — 2 blocos**
>
> | Passo | Valor |
> |---|---|
> | $H_0$ | `00000000000000000000000000000000` |
> | $E(M_1, H_0)$ | `fde4fbae4a09e020eff722969f83832b` |
> | $H_1 = E \oplus H_0$ | `fde4fbae4a09e020eff722969f83832b` |
> | $E(M_2, H_1)$ | `f93ac7d57ff32afb499b06a9d6825127` |
> | $H_2 = E \oplus H_1$ | **`04de3c7b35facadba66c243f4901d20c`** |
>
> Note o primeiro passo : como $H_0 = 0$, o XOR final não muda nada e $H_1 = E(M_1, 0)$. É uma boa conferência intermediária — se $H_1$ não for exatamente a saída do AES, algo foi digitado errado.
>
> ---
> **Exercício 2 — 3 blocos**
>
> | Passo | Valor |
> |---|---|
> | $H_0$ | `00000000000000000000000000000000` |
> | $E(M_1, H_0)$ | `79abc5c23868ad84d388ce61110a6274` |
> | $H_1$ | `79abc5c23868ad84d388ce61110a6274` |
> | $E(M_2, H_1)$ | `9da02846e575eb435bbfaa945586aa33` |
> | $H_2$ | `e40bed84dd1d46c7883764f5448cc847` |
> | $E(M_3, H_2)$ | `09802954521b205ac760d94a35dd7c9b` |
> | $H_3$ | **`ed8bc4d08f06669d4f57bdbf7151b4dc`** |
>
> ---
> **Exercício 3 — 3 blocos**
>
> | Passo | Valor |
> |---|---|
> | $H_0$ | `00000000000000000000000000000000` |
> | $E(M_1, H_0)$ | `baebc618a55c351f25cedf37bf70f390` |
> | $H_1$ | `baebc618a55c351f25cedf37bf70f390` |
> | $E(M_2, H_1)$ | `1436327d23ecb432fe2dd1aa67a61cfd` |
> | $H_2$ | `aeddf46586b0812ddbe30e9dd8d6ef6d` |
> | $E(M_3, H_2)$ | `32284c78ee19aaf5132334b334bbf5d4` |
> | $H_3$ | **`9cf5b81d68a92bd8c8c03a2eec6d1ab9`** |
>
> ---
> **O que o exercício está ensinando, além da aritmética.**
>
> 1. **Efeito avalanche.** Compare $M_1$ do Exercício 1 e do Exercício 3 : entradas com estrutura óbvia (`00112233…`, `aaaa…`) produzem saídas sem nenhuma. Nenhum padrão da entrada sobrevive.
> 2. **O encadeamento é serial.** $H_2$ depende de $H_1$, que depende de $H_0$. Não há como paralelizar, e um erro num passo contamina todos os seguintes — daí valer a pena anotar os intermediários.
> 3. **O que falta para ser um hash de verdade.** Falta o **bloco de padding** com o comprimento da mensagem. Aqui as mensagens são múltiplos exatos do bloco e ele foi dispensado ; num hash real ele é obrigatório, e é o que impede colisões triviais entre mensagens de tamanhos diferentes.
> 4. **A extensão de comprimento está à vista.** $H_2$ do Exercício 1 **é** o estado interno. Quem o conhece pode continuar a iteração e calcular o hash de $M_1 \| M_2 \| M_4$ para qualquer $M_4$, **sem conhecer $M_1$ nem $M_2$**. É o ataque que condena o MAC ingênuo $H(k \| m)$ e a razão de o HMAC ser aninhado.

---
### Ver também
- [aula13](../../aula13.md) — estrutura anunciada da prova.
- [IA/adicoes.md](../../IA/adicoes.md) — aprofundamento de todos os blocos cobrados, incluindo a **Aula 11** (maleabilidade do CBC e padding oracle) e as duas seções de **Material de Revisão P1** (funções resumo ; cifras clássicas).
- [aula03](../../aula03.md) & [aula04](../../aula04.md) — Enigma e cifras clássicas.
- [aula06](../../aula06.md) — One-Time Pad.

**Material de origem da Parte IV**, nesta pasta :
- [`Aula11_PaddingOracleAttack.pdf`](./Aula11_PaddingOracleAttack.pdf) — maleabilidade do CBC e o ataque completo.
- [`8-FuncoesResumo.pdf`](./8-FuncoesResumo.pdf) — funções resumo, Merkle–Damgård, Davies–Meyer, senhas.
- [`CifrasClassicas .pdf`](./CifrasClassicas%20.pdf) — confusão/difusão, Kasiski, índice de coincidência.
- [`Exercicio___Cryptoanalise_cifras_de_fluxo-2.pdf`](./Exercicio___Cryptoanalise_cifras_de_fluxo-2.pdf) — resolvido na **Parte IV.c**.
- [`SS___Exercício_Hash.pdf`](./SS___Exerc%C3%ADcio_Hash.pdf) — resolvido na **Parte IV.d**.
