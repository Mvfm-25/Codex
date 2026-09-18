# Segurança de Sistemas — Adições & Aprofundamentos
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas. Segue os tópicos na ordem em que apareceram nas notas, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---

## Aula 02 — Fundamentos: Kerckhoffs, as Quatro Metas e o Que "Aleatório" Significa

### "Indistinguível de um Texto Aleatório" é a Definição Formal de Segurança

A intuição registrada na aula — no mundo ideal não daria para distinguir texto cifrado de texto completamente aleatório — não é uma metáfora didática. É **literalmente** a definição moderna de segurança de uma cifra, e o nome dela é **indistinguibilidade** (Goldwasser & Micali, 1982).

A formalização é um jogo entre o adversário $\mathcal{A}$ e um desafiante:

1. $\mathcal{A}$ escolhe **duas** mensagens $m_0$ e $m_1$ do mesmo tamanho e as entrega.
2. O desafiante sorteia $b \in \{0,1\}$ e devolve $c = \text{Enc}_k(m_b)$.
3. $\mathcal{A}$ tenta adivinhar $b$.

A cifra é segura (**IND-CPA**) se nenhum adversário eficiente acerta com probabilidade significativamente melhor que $1/2$ — isto é, melhor que chutar. Note a consequência: **uma cifra determinística nunca pode ser IND-CPA**, porque $\mathcal{A}$ pode cifrar $m_0$ por conta própria e comparar. É exatamente por isso que todo modo de operação sério exige **IV** ou *nonce*, e por que o modo ECB (que cifra cada bloco independentemente) é o exemplo clássico de como não fazer — a famosa imagem do pinguim cifrada em ECB ainda mostra o pinguim.

O complemento da observação da aula ("dado poder computacional suficiente, conseguiríamos distinguir") também tem nome. A distinção é entre:

| | **Segurança perfeita** | **Segurança computacional** |
|---|---|---|
| Garantia | Nenhum adversário, nem com poder infinito, aprende nada | Nenhum adversário **eficiente** ganha vantagem significativa |
| Exemplo | *One-Time Pad* | AES, RSA, ChaCha20 — tudo que se usa |
| Preço | Chave do tamanho da mensagem, usada **uma única vez** | Chave de 128–256 bits |

O One-Time Pad é o único sistema **provadamente** inquebrável — Shannon provou isso em 1949, e provou também que a chave precisa ser tão longa quanto a mensagem, aleatória e nunca reutilizada. Reutilizar o pad destrói tudo: $c_1 \oplus c_2 = m_1 \oplus m_2$, e a chave desaparece da equação. Foi assim que o projeto **VENONA** quebrou tráfego soviético por décadas, explorando material de pad reaproveitado. É a diferença entre "matematicamente impossível" e "praticamente impossível" que abre a aula.

### O Princípio de Kerckhoffs e Por Que os Outros Cinco Envelheceram

Dos seis princípios de 1883, o segundo é o que sobreviveu como **o** princípio de Kerckhoffs, na formulação que **Claude Shannon** consolidou:

> *"O inimigo conhece o sistema."*

A justificativa é prática, não filosófica. Um algoritmo é usado por milhares de pessoas, está em binários que podem ser desmontados, em hardware que pode ser aberto, em documentação que vaza. **Uma chave é um segredo pequeno, trocável e individual**; um algoritmo é um segredo grande, imutável e coletivo. Quando o segredo do algoritmo vaza, todo mundo recomeça do zero — quando uma chave vaza, troca-se a chave.

Daí a razão de os padrões modernos serem escolhidos **em competições públicas**: DES (1977), AES (Rijndael, 2001), SHA-3 (Keccak, 2012) e os algoritmos pós-quânticos (ML-KEM/Kyber, ML-DSA/Dilithium, 2024) foram todos submetidos a anos de criptoanálise aberta antes da padronização. O oposto — *security through obscurity* — falha com regularidade documentada: A5/1 (GSM), CSS (DVD), Mifare Classic (crypto-1) e KeeLoq (chaves de carro) foram todos quebrados **depois** de o algoritmo secreto ser recuperado por engenharia reversa, e todos teriam sido quebrados antes se tivessem sido publicados.

Sobre os outros cinco: eles são de uma era em que cifrar era um ato manual e telegráfico. "A chave deve ser memorizável", "os criptogramas devem ser transmissíveis por telégrafo" e "o equipamento deve ser portável e operável por uma única pessoa" descrevem restrições de 1883 que a computação eliminou. Mas o sexto — **"o sistema deve ser fácil de usar"** — teve o percurso inverso: virou o campo de **usabilidade em segurança**, e é hoje uma das causas dominantes de falha real. O artigo *Why Johnny Can't Encrypt* (1999) mostrou que usuários competentes não conseguiam usar PGP corretamente, e é a razão de o Signal e o WhatsApp cifrarem por padrão sem expor chave nenhuma ao usuário. **Criptografia que ninguém consegue usar direito não protege ninguém.**

### As Quatro Metas Não Vêm da Mesma Primitiva

A aula lista privacidade, autenticação, integridade e não-repúdio como um bloco. Elas são **objetivos independentes**, atendidos por primitivas diferentes — e confundir isso é a origem de uma boa parte dos erros de projeto:

| Meta | Primitiva | Observação |
|---|---|---|
| **Privacidade** | Cifra (AES-GCM, ChaCha20) | Não garante integridade sozinha |
| **Integridade** | Hash + **MAC** (HMAC, Poly1305) | Hash puro não basta — o atacante recalcula o hash |
| **Autenticação** | MAC ou **assinatura digital** | MAC autentica *entre as partes que compartilham a chave* |
| **Não-repúdio** | **Somente assinatura digital** (RSA-PSS, Ed25519) | Exige chave **assimétrica** |

A linha do não-repúdio é a que carrega o conteúdo. Um **MAC não pode** fornecê-lo: Alice e Bob compartilham a mesma chave simétrica, então qualquer tag que Alice produziu, Bob também poderia ter produzido. Diante de um juiz, Alice diz "foi o Bob que forjou" e está tecnicamente coberta. Só a **assinatura digital** resolve, porque a chave privada é de uma parte só — o que Alice assinou, ninguém mais poderia ter assinado.

E a linha da privacidade contém a armadilha mais comum da prática: **cifrar não é proteger contra alteração**. Em modos de fluxo (ou em CTR/OFB), inverter um bit no texto cifrado inverte exatamente o bit correspondente no texto claro, sem detecção. Um atacante que sabe o formato da mensagem pode alterar `saldo: 100` sem conhecer a chave. É por isso que o padrão moderno é **AEAD** (*Authenticated Encryption with Associated Data*) — AES-GCM, ChaCha20-Poly1305 — que cifra **e** autentica numa operação só, e por isso que a regra de ouro é *"encrypt-then-MAC"*, nunca o contrário.

### Espaço de Chaves: Quando "Impossivelmente Impossível" Deixa de Valer

A afirmação que abre a aula — teoricamente quebráveis, praticamente não — depende inteiramente do tamanho do espaço de chaves, e a história mostra que essa fronteira **se move**.

Com chave de $n$ bits, a busca exaustiva custa $2^n$ tentativas (em média $2^{n-1}$):

| Chave | Espaço | Situação |
|---|---|---|
| 56 bits (DES) | $7{,}2 \times 10^{16}$ | **Quebrado em 1998** pelo *Deep Crack* da EFF em 56 horas, com US$ 250 mil em hardware. Hoje, horas em FPGA barata. |
| 128 bits (AES-128) | $3{,}4 \times 10^{38}$ | Fora de alcance por margem astronômica |
| 256 bits (AES-256) | $1{,}2 \times 10^{77}$ | Margem contra ataques quânticos |

O DES é o exemplo canônico de um algoritmo que **não foi quebrado matematicamente** — a estrutura Feistel resistiu bem, e a resistência do DES à criptoanálise diferencial mostrou que a NSA já a conhecia nos anos 70. Ele caiu porque a Lei de Moore alcançou o espaço de chaves. O tamanho de 56 bits foi uma decisão política, contestada na época.

Três ressalvas que separam a teoria da prática:

1. **Força bruta é o pior caso do atacante, nunca o caminho escolhido.** Ataques reais vão em chaves fracas, geradores de aleatoriedade defeituosos, reuso de nonce, canais laterais (tempo, consumo, cache) e no usuário. O modelo de ataques da aula descreve o que o adversário *pode* pedir; ele não obriga ninguém a atacar pela frente.
2. **A margem simétrica é confortável mesmo contra computação quântica.** O algoritmo de **Grover** dá ganho quadrático — reduz $2^{128}$ a $2^{64}$ operações — o que se resolve dobrando a chave. O problema real é a criptografia **assimétrica**: o algoritmo de **Shor** quebra RSA e curvas elípticas de forma essencialmente completa, o que é a razão da padronização pós-quântica do NIST em 2024 e da estratégia *"harvest now, decrypt later"* que já motiva migração hoje.
3. **A escada de modelos de ataque importa mais que o tamanho da chave.** Do mais fraco ao mais forte: *ciphertext-only* → *known-plaintext* → *chosen-plaintext* (CPA) → *chosen-ciphertext* (CCA). Uma cifra moderna é projetada para resistir ao **IND-CCA2**, o mais forte deles, porque na prática o atacante frequentemente *consegue* escolher entradas e observar respostas — foi assim que o **ataque de padding oracle** de Vaudenay (2002) quebrou implementações de TLS sem tocar na chave.

---

### Referências para ir além

- **Katz & Lindell, *Introduction to Modern Cryptography*, 3ª ed.** — o tratamento rigoroso de IND-CPA/CCA, segurança perfeita e provas por redução. É o livro que formaliza a intuição de "indistinguível de aleatório".
- **Ferguson, Schneier & Kohno, *Cryptography Engineering*** — a contraparte prática: como as coisas quebram na implementação, não na matemática.
- **Shannon, *Communication Theory of Secrecy Systems* (1949)** — a prova de segurança perfeita do One-Time Pad e a formulação da máxima de Shannon.
- **Cryptopals Crypto Challenges (cryptopals.com)** — exercícios progressivos de quebra: ECB, reuso de nonce, padding oracle. A forma mais rápida de tornar concreto o modelo de ataques.
- **Whitten & Tygar, *Why Johnny Can't Encrypt* (USENIX Security, 1999)** — o artigo que criou a área de usabilidade em segurança, e o sexto princípio de Kerckhoffs levado a sério.
- **NIST — *Post-Quantum Cryptography Standardization* (FIPS 203/204/205, 2024)** — os padrões ML-KEM e ML-DSA, e o processo público que instancia o princípio de Kerckhoffs em escala.

---

## Aula 03 — Enigma: Por Que a Aula "Inútil" é a Melhor Aula de Criptanálise do Semestre

As notas registram a aula como interessante mas "*não muito útil para a cadeira em si*". Vale contestar isso com cuidado, porque a Enigma é o estudo de caso que instancia praticamente todos os conceitos da disciplina: espaço de chaves, princípio de Kerckhoffs, modelo de ataque, ataque de texto-claro conhecido e falha humana de procedimento.

### A máquina, mecanicamente

A Enigma militar alemã era um circuito elétrico que mudava a cada tecla. O caminho da corrente:

$$\text{tecla} \to \text{plugboard} \to \text{rotor 1} \to \text{rotor 2} \to \text{rotor 3} \to \text{refletor} \to \text{rotores (volta)} \to \text{plugboard} \to \text{lâmpada}$$

Três componentes, com papéis distintos:

- **Rotores** (*Walzen*) — discos com 26 contatos de cada lado e uma fiação interna que permuta as letras. O rotor da direita avança uma posição a **cada** tecla; quando passa por um entalhe, empurra o do meio, e assim por diante — como um hodômetro. É isso que faz da Enigma uma cifra **polialfabética** com período $26 \times 25 \times 26 = 16\,900$: pressionar `A` cinco vezes produz cinco letras diferentes.
- **Refletor** (*Umkehrwalze*) — devolve a corrente pelos rotores por um caminho diferente. É o que torna a máquina **auto-recíproca**: cifrar e decifrar são a mesma operação, com a mesma configuração. Enorme conveniência operacional.
- **Plugboard** (*Steckerbrett*) — troca pares de letras antes e depois dos rotores. Contribui com a maior parte do espaço de chaves.

O espaço de chaves da Enigma de 3 rotores do Exército:

| Componente | Combinações |
|---|---|
| Escolha e ordem de 3 rotores entre 5 | $5 \times 4 \times 3 = 60$ |
| Posição inicial dos 3 rotores | $26^3 = 17\,576$ |
| Anéis (*Ringstellung*) | $26^2 = 676$ |
| Plugboard com 10 cabos | $\approx 1{,}507 \times 10^{14}$ |
| **Total** | $\approx \mathbf{1{,}59 \times 10^{20}}$ |

São cerca de **67 bits** de chave. Para 1940, um número esmagador — e a razão pela qual o alto-comando alemão considerou a máquina inquebrável até o fim da guerra.

### A falha que valeu a guerra: o refletor

E aqui está a lição que justifica a aula. O refletor, que dava a conveniência de cifrar e decifrar com a mesma configuração, impôs uma propriedade fatal:

> **Nenhuma letra jamais é cifrada como ela mesma.**

Como a corrente volta por um caminho diferente do que foi, a letra de saída nunca coincide com a de entrada. Parece inofensivo. É o oposto: transforma um espaço de $10^{20}$ chaves num problema tratável.

O ataque que isso habilita é o **crib-dragging**, um ataque de **texto-claro conhecido**. Suponha que se saiba que a mensagem contém `WETTERVORHERSAGE` ("previsão do tempo") — e sabia-se, porque os boletins meteorológicos eram transmitidos todo dia no mesmo horário e no mesmo formato. Arrasta-se essa palavra ao longo do criptograma; em qualquer posição em que alguma letra do *crib* coincida com a letra correspondente do criptograma, aquela posição está **eliminada**, sem nenhum cálculo. Na prática isso descartava a grande maioria dos alinhamentos instantaneamente.

Com um alinhamento plausível, a **Bombe** de Turing entrava: um dispositivo eletromecânico que percorria configurações de rotor procurando contradições lógicas na cadeia de implicações induzida pelo *crib*. Ela não testava as $10^{20}$ chaves — usava o *crib* para derivar contradições e eliminar blocos inteiros do espaço de uma vez. A redução é de espaço de busca, não de força bruta.

### Crédito, e o que a disciplina deve tirar disso

As notas mencionam "*matemáticos poloneses e uma equipe de especialistas britânicos*", e o crédito merece nome. **Marian Rejewski**, **Jerzy Różycki** e **Henryk Zygalski**, do *Biuro Szyfrów* polonês, quebraram a Enigma pela primeira vez em **1932** — sete anos antes da guerra —, reconstruindo a fiação dos rotores a partir de tráfego interceptado e explorando a repetição da chave de mensagem. Em julho de 1939, a semanas da invasão, entregaram tudo a franceses e britânicos. Sem essa transferência, Bletchley Park teria começado do zero.

Quatro lições que são exatamente o programa da cadeira:

1. **Kerckhoffs, na prática.** Os Aliados tinham máquinas Enigma e conheciam o projeto completo. A segurança dependia inteiramente da **chave diária**, que é onde deve estar. O problema não foi o projeto ser conhecido — foi ele ter um defeito estrutural.
2. **Conveniência operacional custa segurança.** O refletor foi escolhido para simplificar o uso. Toda escolha de usabilidade em criptografia tem esse risco, e reconhecê-lo é metade do trabalho de projeto.
3. **Tamanho de chave não é segurança.** $10^{20}$ chaves não protegeram nada, porque o ataque não era por força bruta. Esse ponto reaparece na Aula 04 com a substituição monoalfabética e na Aula 13 com o 2DES.
4. **O elo humano quebra primeiro.** Chaves de mensagem repetidas, saudações padronizadas, o `HEILHITLER` no fim das transmissões, operadores escolhendo `AAA` ou as iniciais da namorada como posição inicial — cada um desses vícios entregava *cribs*. Nenhum era falha da máquina.

---

## Aula 04 — As Cifras Clássicas e o Ferramental de Quebra

As notas registram a recapitulação por slides e admitem a lacuna: "*outras duas cifras que esqueci o nome*". Vale o panorama completo, porque essas cifras são o vocabulário de toda a primeira metade da disciplina.

### As cifras, em ordem de sofisticação

| Cifra | Chave | Espaço de chaves | Como cai |
|---|---|---|---|
| **César** | um deslocamento | **25** | força bruta em 25 tentativas |
| **Substituição monoalfabética** | uma permutação de 26 letras | $26! \approx 4\times10^{26}$ | **análise de frequência**, em minutos |
| **Vigenère** | uma palavra de $m$ letras | $26^m$ | **Kasiski** / índice de coincidência, depois César $m$ vezes |
| **Playfair** | uma grade $5\times5$ | $\approx 25!$ | frequência de **digramas** |
| **Transposição colunar** | uma permutação de colunas | $m!$ | anagramação; frequências ficam **inalteradas** |

As duas que as notas esqueceram são quase certamente **Vigenère** e **Playfair** — são as que sempre acompanham César numa aula de cifras clássicas.

**Vigenère** é César com uma chave que se repete: cada letra da chave define um deslocamento diferente, ciclicamente. Ficou conhecida como *le chiffre indéchiffrable* por três séculos, porque a repetição da chave achata as frequências.

**Playfair** cifra **pares** de letras usando uma grade $5\times5$, e foi usada de verdade pelos britânicos na Primeira Guerra. Cifrar digramas em vez de letras isoladas derruba a análise de frequência simples — mas não a de digramas, e `TH`, `HE`, `IN` continuam sendo os mais comuns do inglês.

**Transposição** é o caso conceitualmente distinto: ela **reordena** em vez de substituir. As frequências das letras ficam exatamente iguais às do texto claro, o que torna a análise de frequência inútil — e, por isso mesmo, é o teste que *identifica* uma transposição. Se as frequências parecem português normal mas o texto não faz sentido, é transposição, não substituição.

A observação registrada nas notas — que as cifras clássicas "*poderiam ser seguras se 75% da população não fosse alfabetizada*" — é historicamente aguda, e tem nome técnico: isso é **segurança por obscuridade**, e é precisamente o que Kerckhoffs proibiu. A raridade do atacante capaz não é uma propriedade do sistema.

### Análise de frequência, com números

A técnica aparece nas notas sem o ferramental. Ela se apoia em três estatísticas do idioma:

**1. Frequência de letras.** Em português, as mais comuns são `A` (~14,6%), `E` (~12,6%), `O` (~10,7%), `S` (~7,8%), `R` (~6,5%). Num criptograma monoalfabético longo, a letra mais frequente quase certamente corresponde a `A` ou `E`.

**2. Índice de coincidência.** A probabilidade de duas letras sorteadas ao acaso do texto serem iguais:

$$\mathrm{IC} = \frac{\sum_{i=1}^{26} n_i(n_i - 1)}{N(N-1)}$$

| Texto | IC aproximado |
|---|---|
| Português / inglês normal | $\approx 0{,}072$ / $0{,}067$ |
| Substituição monoalfabética | **igual ao do idioma** — a permutação não muda o IC |
| Vigenère com chave longa | $\to 0{,}038$ (uniforme) |
| Texto realmente aleatório | $0{,}0385$ |

O IC é a ferramenta de triagem: ele diz **que tipo** de cifra está na frente, antes de qualquer tentativa de quebra. IC alto e texto ilegível ⇒ monoalfabética ou transposição. IC baixo ⇒ polialfabética, e o próximo passo é achar o período.

**3. Exame de Kasiski.** Sequências repetidas de 3+ letras no criptograma de Vigenère tendem a aparecer a distâncias múltiplas do comprimento da chave. Calculando o MDC dessas distâncias obtém-se o período $m$; dividido o texto em $m$ colunas, cada coluna é uma César simples, e cai por frequência. É o método de 1863 que encerrou os três séculos de "indecifrável".

### A lição que atravessa a disciplina

A substituição monoalfabética tem $26! \approx 4 \times 10^{26}$ chaves — mais que o AES-88 — e cai em segundos num laptop. Um criptograma de 200 letras é suficiente.

> **Tamanho de chave é condição necessária e nunca suficiente.** Ele só limita o ataque de força bruta; se existe estrutura explorável, o espaço de chaves é irrelevante.

Esse é o mesmo argumento do refletor da Enigma (Aula 03) e do 2DES contra *meet-in-the-middle* (Aula 13). Três instâncias do mesmo princípio, em três escalas de sofisticação — e é por isso que a sequência de aulas está nessa ordem.

---

## Aula 06 — Sigilo Perfeito: a Resposta para "OTP é Decifrável?"

### A pergunta das notas tem resposta, e ela é "não"

As notas fecham com a pergunta em aberto e uma suspeita: "*OTP é decifrável? Acredito que pelo meu uso de 'segura' irônico algumas linhas acima, você conseguiria perceber que sim. Mas como?*"

A resposta direta, e ela contraria a expectativa: **o One-Time Pad usado corretamente é incondicionalmente seguro, e isso é um teorema provado.** O que é decifrável é o OTP usado **errado** — e como usá-lo corretamente é praticamente impossível, a ironia das notas acaba sendo justificada na prática, só que pelo motivo oposto ao suposto.

### O teorema de Shannon

**Shannon** (1949) definiu **sigilo perfeito** assim: um criptossistema tem sigilo perfeito se, para toda mensagem $m$ e todo criptograma $c$,

$$\Pr[M = m \mid C = c] \;=\; \Pr[M = m].$$

Em palavras: **observar o criptograma não muda em nada o que se sabe sobre a mensagem**. O atacante com poder computacional infinito e tempo infinito não ganha absolutamente nada — não é que quebrar seja difícil, é que não há informação ali para extrair.

**Por que o OTP tem essa propriedade.** Com $c = m \oplus k$ e $k$ uniformemente aleatório, para qualquer texto claro candidato $m'$ do mesmo comprimento existe **exatamente uma** chave $k' = c \oplus m'$ que produziria aquele mesmo $c$. Todas as mensagens possíveis são igualmente compatíveis com o criptograma observado. Interceptar 11 bits que decifram para `ATACAR AS 6` é interceptar algo que decifra igualmente bem para `RECUAR AS 9` — e nada no criptograma distingue os dois casos.

**O preço, que também é teorema.** Shannon provou que sigilo perfeito exige

$$H(K) \;\ge\; H(M) \qquad\text{e, no caso uniforme,}\qquad |K| \ge |M|.$$

A chave tem que ser **pelo menos tão longa quanto a mensagem**. Isso não é um defeito da construção do OTP — é um limite inferior que vale para **qualquer** sistema com sigilo perfeito. Não existe e não pode existir um esquema perfeito com chave curta. É a mesma estrutura de resultado que o Abel–Ruffini tem em álgebra: não é falta de engenhosidade, é impossibilidade demonstrada.

### O que de fato quebra o OTP: reuso de chave

Se o OTP é perfeito, o que é aquele "mas como?" das notas? É o **two-time pad** — a única forma de quebrá-lo, e ela é devastadora.

Cifrando duas mensagens com a mesma chave:

$$c_1 = m_1 \oplus k \qquad c_2 = m_2 \oplus k$$

O atacante calcula

$$c_1 \oplus c_2 = (m_1 \oplus k) \oplus (m_2 \oplus k) = m_1 \oplus m_2$$

**A chave sumiu.** O que sobra é o XOR de dois textos em língua natural — e isso é recuperável por *crib-dragging*: arrasta-se uma palavra provável ao longo do resultado e, quando ela está na posição certa, o XOR revela um fragmento legível da **outra** mensagem, que por sua vez serve de *crib* para continuar. Duas mensagens de algumas centenas de caracteres costumam cair inteiras.

Isso não é hipótese de sala de aula. O projeto **VENONA** decifrou milhares de telegramas soviéticos das décadas de 1940 e 1950 porque um fornecedor sob pressão de guerra duplicou páginas de blocos de uso único. A criptografia era perfeita; o procedimento não era.

A propriedade do XOR que as notas destacam — "*os 1's marcam quais bits eram diferentes*" — é exatamente o que torna o ataque possível: XOR é sua própria inversa ($x \oplus x = 0$, $x \oplus 0 = x$), e é isso que faz cifrar e decifrar serem a mesma operação, e que faz a chave cancelar quando reutilizada. A mesma propriedade que dá a conveniência dá o ataque, ecoando o refletor da Enigma.

### Por que ninguém usa OTP, e o que se usa no lugar

Três problemas práticos, todos consequência do teorema de Shannon:

1. **Distribuição da chave.** Para enviar 1 GB com sigilo, é preciso primeiro entregar 1 GB de chave por um canal já seguro. Se existe tal canal, mande a mensagem por ele.
2. **Aleatoriedade verdadeira.** A chave precisa ser genuinamente aleatória, não gerada por PRNG. Um OTP com chave de `rand()` é apenas uma cifra de fluxo ruim.
3. **Nunca reutilizar, jamais.** Isso exige controle de estado impecável entre as duas pontas — e é onde sistemas reais falham.

A solução prática é abrir mão do sigilo *perfeito* e aceitar o **sigilo computacional**: em vez de uma chave verdadeiramente aleatória do tamanho da mensagem, usa-se uma chave curta (128 ou 256 bits) expandida por um gerador pseudoaleatório criptográfico num fluxo tão longo quanto necessário. É exatamente a estrutura do OTP, com o fluxo gerado em vez de compartilhado:

$$c = m \oplus \mathrm{PRG}(k, \text{nonce})$$

É isso que são as **cifras de fluxo** do título da aula — RC4 (hoje quebrada e proibida), **ChaCha20** (o padrão atual, usado em TLS 1.3 e no WireGuard), e o AES em modo CTR, que transforma uma cifra de bloco em cifra de fluxo. A garantia cai de "impossível de quebrar" para "inviável de quebrar sem $2^{128}$ operações", o que é suficiente para todos os efeitos práticos.

**E o modo de falha é herdado inteiro.** Reutilizar o par (chave, nonce) numa cifra de fluxo é literalmente um two-time pad, com a mesma consequência. Foi assim que o **WEP** caiu — IV de 24 bits, que colide após poucas horas de tráfego —, e é por isso que o GCM do AES é catastroficamente inseguro sob reuso de nonce, a ponto de existirem modos específicos (AES-GCM-SIV) projetados para sobreviver a esse erro. A lição de 1917 continua sendo a mesma de hoje.

---

## Aula 13 — Consolidação para a P1: os Quatro Blocos Dissertativos

As notas registram a estrutura da prova e os quatro temas dissertativos, mais a lacuna que o professor apontou (Hash & MAC). Como é aula de revisão, o material complementar mais útil é o conteúdo de cada bloco, com os números que uma resposta boa precisa ter.

### Bloco 1 — Modelo de ataque, metas e Kerckhoffs

**Os modelos de ataque**, em ordem crescente de poder do adversário. É a hierarquia que organiza a resposta:

| Modelo | Sigla | O que o atacante tem |
|---|---|---|
| Só criptograma | COA | apenas $c$ |
| Texto claro conhecido | KPA | pares $(m, c)$ que ele **observou** |
| Texto claro escolhido | CPA | ele **escolhe** $m$ e recebe $c$ |
| Criptograma escolhido | CCA | ele escolhe $c$ e recebe $m$ |

Um sistema é avaliado pelo modelo mais forte que resiste. A Enigma caiu em **KPA** (os *cribs*); hoje o mínimo aceitável para uso geral é segurança **IND-CCA2**.

**As quatro metas** (que valem para segurança em geral, não só cifragem):

| Meta | Pergunta | Mecanismo |
|---|---|---|
| **Confidencialidade** | quem pode ler? | cifragem |
| **Integridade** | foi alterado? | hash, MAC |
| **Autenticidade** | veio de quem diz? | MAC, assinatura |
| **Não-repúdio** | pode negar depois? | **só** assinatura digital |

A distinção que mais cai: **MAC dá autenticidade mas não dá não-repúdio**, porque a chave é simétrica e as duas partes poderiam ter gerado a tag. Só a assinatura, com chave privada de um lado só, permite provar autoria a um terceiro.

**Kerckhoffs (1883)**, na formulação usável: *o sistema deve ser seguro mesmo que tudo sobre ele, exceto a chave, seja de conhecimento público.* A versão de Shannon é mais direta — "*o inimigo conhece o sistema*". O argumento é prático: algoritmos vazam, são extraídos por engenharia reversa e precisam ser auditados; chaves podem ser trocadas, algoritmos não. AES e RSA são públicos e revisados há décadas, e é isso que dá confiança neles — o inverso do que a intuição sugere.

### Bloco 2 — One-Time Pad

Cobrado na seção da **Aula 06** acima. O núcleo de uma boa resposta: a definição de sigilo perfeito de Shannon ($\Pr[M{=}m \mid C{=}c] = \Pr[M{=}m]$), o argumento de que toda mensagem candidata tem exatamente uma chave compatível, o requisito $|K| \ge |M|$ como **teorema** e não como inconveniente, e os três motivos de inviabilidade prática (distribuição, aleatoriedade real, não-reuso). Se couber, o two-time pad com $c_1 \oplus c_2 = m_1 \oplus m_2$ e VENONA como caso histórico.

### Bloco 3 — Cifras de bloco e o *meet-in-the-middle*

| Cifra | Bloco | Chave | Segurança efetiva | Situação |
|---|---|---|---|---|
| **DES** (1977) | 64 bits | 56 bits | $2^{56}$ | **quebrada** — força bruta em horas desde os anos 1990 |
| **2DES** | 64 bits | 112 bits | **$2^{57}$** | inútil (ver abaixo) |
| **3DES** (EDE) | 64 bits | 168 bits | $\approx 2^{112}$ | obsoleta (NIST descontinuou em 2023) |
| **AES-128/192/256** | 128 bits | 128/192/256 | $2^{128}$ / $2^{192}$ / $2^{256}$ | **padrão atual** |

**O ataque *meet-in-the-middle* sobre o 2DES** é o ponto que as notas destacam, e ele merece a conta completa porque é o argumento que explica a existência do 3DES.

Duplo DES calcula $c = E_{k_2}(E_{k_1}(m))$, aparentando 112 bits de chave. O ataque explora a igualdade

$$E_{k_1}(m) \;=\; D_{k_2}(c)$$

— o valor intermediário pode ser alcançado pelos dois lados. Com **um** par conhecido $(m,c)$:

1. Calcule $E_{k}(m)$ para todas as $2^{56}$ chaves $k$ e guarde numa tabela hash: $2^{56}$ operações, $2^{56}$ de memória.
2. Calcule $D_{k'}(c)$ para todas as $2^{56}$ chaves $k'$, procurando cada resultado na tabela.
3. Cada colisão é um candidato $(k_1, k_2)$. Confirme com um segundo par conhecido.

Custo total: $\approx 2^{57}$ operações. **Um bit a mais que o DES simples**, não 56. Duplicar a cifra comprou essencialmente nada, ao custo de dobrar o tempo de execução.

É por isso que se foi direto para o **triplo** DES, em modo EDE ($E_{k_3}(D_{k_2}(E_{k_1}(m)))$), que resiste com $\approx 2^{112}$. E note o motivo de o passo do meio ser um **D** e não um **E**: com $k_1 = k_2 = k_3$, o 3DES vira DES simples, garantindo compatibilidade com equipamento legado. Detalhe de engenharia que rende ponto numa dissertativa.

A moral, mais uma vez a mesma da Aula 04: **112 bits de chave nominais, 57 bits de segurança real.** Contar bits de chave não é medir segurança.

### Bloco 4 — Pentest e superfície de ataque

Os conceitos que as notas nomeiam, com definições utilizáveis:

- **Superfície de ataque** — o conjunto de todos os pontos em que um atacante não autorizado pode tentar entrar ou extrair dados: portas abertas, endpoints de API, formulários, arquivos enviados, bibliotecas de terceiros, pessoas. É um **conjunto**, e a estratégia defensiva primária é **reduzi-lo**.
- **Vetor de ataque** — o caminho específico usado numa tentativa concreta: uma injeção de SQL num campo, um e-mail de phishing, uma credencial padrão em um serviço exposto. Um vetor é um elemento da superfície, efetivamente explorado.
- **Fases de um pentest**: reconhecimento (passivo e ativo) → varredura e enumeração → exploração → pós-exploração e movimentação lateral → relatório. O **relatório** é o entregável, e é o que distingue um pentest de uma invasão.
- **Ferramentas por fase**: `nmap` (varredura de portas e detecção de serviço), `Nessus`/`OpenVAS` (varredura de vulnerabilidade), `Burp Suite` (interceptação e teste web), `Metasploit` (exploração), `Wireshark` (análise de tráfego), `hashcat`/`John` (quebra de hash offline).
- **A distinção que separa pentest de crime**: **escopo autorizado por escrito**. As "regras de engajamento" definem alvos, janelas de tempo e técnicas permitidas. Sem isso, a atividade técnica é idêntica e a classificação legal é outra.

O aviso das notas de que a prova cobra a parte **conceitual** e não o TryHackMe é coerente com isso: o que se avalia é o vocabulário e o método, não o uso da ferramenta.

### A lacuna apontada: Hash e MAC

O professor sinalizou que essas são as questões objetivas "chatinhas". O essencial:

**Função de hash criptográfica** — mapeia entrada de tamanho arbitrário em saída fixa, com três propriedades:

| Propriedade | Enunciado | Custo de quebrar (saída de $n$ bits) |
|---|---|---|
| Resistência à pré-imagem | dado $h$, achar $m$ com $H(m)=h$ | $2^{n}$ |
| Resistência à 2ª pré-imagem | dado $m$, achar $m' \ne m$ com $H(m')=H(m)$ | $2^{n}$ |
| **Resistência à colisão** | achar **quaisquer** $m \ne m'$ com $H(m)=H(m')$ | $\mathbf{2^{n/2}}$ |

O expoente $n/2$ é o **paradoxo do aniversário**, e é a razão de SHA-256 oferecer só 128 bits de segurança contra colisão. É também o que matou o **MD5** (colisões em segundos) e o **SHA-1** (colisão real demonstrada pelo ataque *SHAttered*, do Google, em 2017). Estado atual: **SHA-256/SHA-3** para uso geral; **bcrypt, scrypt ou Argon2** para senhas — nunca SHA puro, porque para senhas o que se quer é uma função deliberadamente **lenta** e com *salt*.

**MAC** (*Message Authentication Code*) — hash **com chave**, que dá integridade **e** autenticidade. O padrão é o **HMAC**:

$$\mathrm{HMAC}(k, m) = H\big((k \oplus \text{opad}) \,\|\, H((k \oplus \text{ipad}) \,\|\, m)\big)$$

A construção aninhada existe para resistir ao **ataque de extensão de comprimento**, ao qual construções ingênuas como $H(k \,\|\, m)$ são vulneráveis em hashes do tipo Merkle–Damgård (MD5, SHA-1, SHA-2). Esse é um detalhe clássico de prova objetiva.

E o ponto de ordem de operações: **sempre `Encrypt-then-MAC`** — cifre primeiro, autentique o criptograma. As alternativas (`MAC-then-Encrypt`, usada no SSL/TLS antigo, e `Encrypt-and-MAC`) levaram a ataques reais de *padding oracle*. Na prática moderna usa-se **AEAD** (AES-GCM, ChaCha20-Poly1305), que faz cifragem e autenticação numa operação só e elimina a chance de errar a ordem.

---

## Aula 14 — Cadeia de Confiança, e o Que uma Auditoria de Código Não Prova

As notas cobrem bem a apresentação do TSE. Vale extrair os dois conceitos de segurança que estão por trás dela, porque ambos são conteúdo de disciplina e não de palestra.

### Boot verificado: o MSE como raiz de confiança

A sequência descrita nas notas — o **MSE** (Módulo de Segurança Embarcado) é o primeiro componente energizado, lê e verifica a BIOS, carrega e verifica o carregador do kernel, depois o sistema operacional, e só então libera os aplicativos de eleição — é a implementação de um **verified boot** com **raiz de confiança em hardware**.

O princípio geral:

$$\underbrace{\text{Raiz de confiança}}_{\text{hardware, imutável}} \to \text{firmware} \to \text{bootloader} \to \text{kernel} \to \text{aplicação}$$

Cada elo **verifica a assinatura digital do próximo antes de lhe passar o controle**. A cadeia só é tão forte quanto sua raiz, e a raiz precisa ser imutável — daí ser hardware, com a chave pública gravada de fábrica e sem caminho de escrita.

Vale distinguir duas variantes que costumam ser confundidas:

| | **Verified boot** | **Measured boot** |
|---|---|---|
| O que faz | verifica a assinatura e **recusa** executar se falhar | calcula o hash de cada estágio e **registra** num TPM |
| Resultado da falha | a máquina não dá boot | dá boot, mas o registro denuncia |
| Uso típico | dispositivo dedicado, urna, console, celular | atestação remota, BitLocker |

A urna usa a primeira. O paralelo direto no mundo comum é o **UEFI Secure Boot** com chaves no firmware, e o **Android Verified Boot**; o desafio criptografado que as notas mencionam (a urna resolve em 4 minutos antes de carregar os aplicativos) é um protocolo **desafio-resposta**, que prova posse de uma chave sem transmiti-la.

A observação das notas de que "*saindo da fábrica a urna não consegue fazer nada — é peso de papel*" descreve um dispositivo com a raiz de confiança presente mas sem material criptográfico de operação. É o mesmo modelo de um HSM ou de um Secure Enclave recém-fabricado: o hardware existe, as chaves de operação são provisionadas depois, num ambiente controlado, e é esse provisionamento que constitui a "inicialização".

### O que uma auditoria de código-fonte garante — e o que não garante

Este é o ponto mais interessante da aula, e ele tem um artigo canônico.

O procedimento descrito é sólido: entidades legitimadas (Ministério Público, OAB, CNJ, Polícia Federal, SBC, universidades) acessam o código **um ano antes** da eleição; resumos digitais e assinaturas são gerados sobre os arquivos finais; representantes das forças armadas comparam o código liberado com o de uma urna; a mídia é não-regravável. Isso endereça diretamente a pergunta "*o software que vai para a urna é o mesmo que foi auditado?*".

Mas existe um limite que nenhum desse procedimento alcança, e ele foi enunciado por **Ken Thompson** no discurso do Turing Award de 1984, **"Reflections on Trusting Trust"**.

O argumento: suponha um compilador modificado para inserir uma porta dos fundos ao compilar um programa específico — digamos, o `login`. Alguém que leia o código-fonte do `login` não vê nada. Alguém que leia o código-fonte do **compilador** veria o ataque — então o compilador é modificado de novo para, ao compilar **a si mesmo**, reinserir as duas modificações. Recompilado uma vez, o compilador binário carrega o ataque, e o código-fonte do compilador volta a ficar **limpo**. Auditoria de fonte nenhuma encontra nada, porque não há nada no fonte.

A conclusão de Thompson: *"Você não pode confiar em código que não escreveu inteiramente você mesmo. Nenhuma quantidade de verificação em nível de fonte vai protegê-lo de usar código não confiável."*

Aplicado ao caso: auditar o código-fonte da urna prova propriedades **do código-fonte**. Para ligar isso ao binário que efetivamente roda, é preciso confiar também no compilador, nas bibliotecas, no sistema de build e na máquina que compilou.

**A resposta moderna a esse problema tem nome: *reproducible builds*.** A ideia é tornar o processo de compilação determinístico — mesmo fonte, mesmas ferramentas, mesmo binário, bit a bit — para que auditores independentes possam recompilar e **comparar hashes** em vez de confiar em quem compilou. Debian, Tails e o Bitcoin Core investem nisso há anos. O passo descrito nas notas, em que as forças armadas comparam o código liberado com o de uma urna, é uma versão manual e presencial dessa ideia; a versão forte seria qualquer auditor conseguir reproduzir o binário oficial a partir do fonte publicado.

### Testes públicos de segurança: o que um TPS mede

O **Teste Público de Segurança** que as notas descrevem — desde 2009, obrigatório desde 2017, sete edições, 112 planos de teste, refeito meses depois para comparação, com a PF como crítico mais duro — é **red teaming** institucionalizado, e o formato tem duas propriedades que merecem destaque:

1. **Reprodutibilidade exigida.** Um achado só conta se puder ser demonstrado de novo. Isso elimina relatos anedóticos e é o que permite a segunda rodada de confirmação.
2. **Barreiras relaxadas de propósito.** As notas registram isso corretamente: com um plano de ataque definido, certas proteções são afrouxadas para tornar o teste viável, porque o objetivo é testar **um mecanismo específico**, não o processo inteiro.

E é justamente essa segunda propriedade que define o limite da conclusão. Um TPS mede a resistência dos mecanismos testados sob as condições concedidas, com o tempo e o acesso concedidos. Ele **não** demonstra a ausência de vulnerabilidades — nenhum teste demonstra isso. É o mesmo princípio que abre a disciplina de Métodos Formais com Dijkstra: *testar mostra a presença de defeitos, nunca a sua ausência*. O "**suficientemente seguro**" que as notas citam é a formulação honesta disso.

### Independência de software: a crítica acadêmica, em termos técnicos

Vale conhecer o argumento central da literatura sobre urnas, porque ele não é sobre confiar ou desconfiar de ninguém — é uma propriedade formal. **Ron Rivest** (o `R` do RSA) formulou o critério de **independência de software**:

> Um sistema de votação é *software-independent* se uma alteração ou erro **não detectado** no software não puder causar uma mudança **não detectável** no resultado da eleição.

O ponto é que essa propriedade é difícil de obter sem um registro **fora do software** — tipicamente um comprovante em papel conferido pelo eleitor (**VVPAT**), que permita recontagem física independente do que o software fez. Com um registro assim, uma auditoria por amostragem pode confirmar o resultado **sem confiar no código**; sem ele, toda garantia se apoia na cadeia de confiança descrita acima, e essa cadeia tem o limite de Thompson.

Isso não é uma afirmação sobre a urna brasileira ser insegura — é uma afirmação sobre **que tipo de garantia** cada arquitetura consegue oferecer. A distinção entre "é muito difícil fraudar" e "uma fraude seria necessariamente detectável" é precisamente o tipo de precisão que uma disciplina de segurança deve treinar, e é a razão de a discussão acadêmica sobre voto eletrônico continuar viva mesmo onde os sistemas funcionam bem.

A frase final registrada nas notas — "*melhoria contínua é imperativa*", e a urna de 1996 ser irreconhecível frente à atual — é a postura correta, e é a mesma de qualquer sistema de segurança sério: a garantia nunca é um estado alcançado, é um processo mantido.

---
