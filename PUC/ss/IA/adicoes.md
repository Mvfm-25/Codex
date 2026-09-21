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

## Aula 11 — Maleabilidade do CBC e o *Padding Oracle Attack*

Esta é a aula que fecha o argumento aberto na Aula 02 : **confidencialidade não é integridade**. O CBC esconde o conteúdo e, ainda assim, permite que um atacante o modifique cirurgicamente — e, com um oráculo de padding, permite decifrá-lo inteiro sem jamais tocar na chave.

### Primeiro : por que o CBC é maleável

A decifragem em CBC é

$$m_i = D_k(c_i) \oplus c_{i-1}, \qquad c_{-1} = \mathrm{IV}$$

O bloco anterior entra por **XOR**, depois da cifra. Isso tem uma consequência imediata e devastadora : alterar um bit de $c_{i-1}$ altera **exatamente o mesmo bit** de $m_i$. O atacante não precisa da chave — precisa só de aritmética.

O exemplo dos slides é o caso limpo. Um pacote cifrado começa com `dest=80`, e o atacante quer que o destino vire `25` :

$$m_0 = D_k(c_0) \oplus \mathrm{IV}$$

Se ele quer $m_0' = m_0 \oplus \Delta$, basta enviar $\mathrm{IV}' = \mathrm{IV} \oplus \Delta$. Como $\Delta$ é a diferença entre o texto que está lá e o que ele quer pôr no lugar :

$$\mathrm{IV}' = \mathrm{IV} \oplus (\texttt{...80...}) \oplus (\texttt{...25...})$$

É a alternativa correta da pergunta do slide, e note **o que ela exige** : que o atacante *conheça* o texto claro daquele trecho — por isso o slide classifica o ataque como "cirúrgico". Ele não descobre nada ; ele reescreve o que já sabe estar lá.

Duas observações que costumam cair em objetiva :

1. **Mexer no IV é gratuito.** Alterar $c_{i-1}$ para $i \ge 1$ corrompe irremediavelmente o bloco $m_{i-1}$ — ele vira lixo, porque $D_k$ de um bloco alterado é imprevisível. Mexer **só no IV** não corrompe nada, porque o IV não é decifrado : ele só entra no XOR. Por isso o ataque do slide é feito no primeiro bloco.
2. **Nenhuma cifra de bloco "melhor" resolve isso.** Trocar o DES pelo AES não muda nada : a maleabilidade é do **modo**, não da primitiva. A correção é autenticar o criptograma — `Encrypt-then-MAC` ou **AEAD**.

### O *padding oracle* : decifrar sem a chave

O ataque anterior modifica. Este **lê**, e essa é a diferença de grau que o torna notável.

**O padding.** Cifras de bloco operam sobre blocos completos (16 bytes no AES), então a última porção da mensagem é completada. No PKCS#7, completa-se com $p$ bytes cujo valor é o próprio $p$ : falta 1 byte ⇒ `01` ; faltam 2 ⇒ `02 02` ; faltam 5 ⇒ `05 05 05 05 05`. Ao decifrar, o sistema **valida** esse padding antes de entregar a mensagem.

**O oráculo.** Se o sistema reage de forma **distinguível** quando o padding está errado, ele virou um oráculo. Os slides listam as três formas em que isso acontece, e as três são reais :

- um **erro explícito** — o clássico `403` para padding inválido vs. `404` para padding válido mas mensagem inválida ;
- a **ausência** de uma resposta esperada ;
- uma **demora** diferente na resposta — o canal lateral de tempo, que é o que sobra depois que alguém "corrige" o bug unificando as mensagens de erro.

Um bit de resposta por consulta. É tudo de que o ataque precisa.

**A mecânica, byte a byte.** Seja $c$ o bloco alvo e $I = D_k(c)$ o **valor intermediário** — a saída da cifra, antes do XOR. O atacante controla integralmente o bloco que entra no XOR ; chame-o de $R$. O sistema decifra e obtém

$$m = I \oplus R$$

Para o **último byte** : o atacante fixa $R$ arbitrário e varre $R[15]$ pelos 256 valores possíveis. Quando o oráculo aceitar o padding, quase certamente é porque $m[15] = \texttt{0x01}$, logo

$$I[15] = R[15] \oplus \texttt{0x01}$$

Para o **penúltimo** : ele agora quer forçar o padding `02 02`. Já conhece $I[15]$, então fixa $R[15] = I[15] \oplus \texttt{0x02}$ — o que garante $m[15] = \texttt{0x02}$ — e varre $R[14]$ até o oráculo aceitar. Então $I[14] = R[14] \oplus \texttt{0x02}$. E assim por diante, com `03 03 03`, `04 04 04 04`, …

Descobertos os 16 bytes de $I$, o texto claro **verdadeiro** sai de graça, usando o bloco anterior **real** :

$$m_i = I \oplus c_{i-1}$$

Depois, como registram os slides, "*o primeiro bloco cifrado vira IV e o segundo vira o primeiro bloco*" : repete-se o procedimento deslizando a janela, até a mensagem inteira.

> **A armadilha do último byte.** A varredura de $R[15]$ pode acertar por acidente : se $m[14]$ por acaso valer `02`, o padding `02 02` também é válido. O falso positivo se elimina alterando $R[14]$ e repetindo a consulta — se ainda for aceito, o padding era mesmo `01`.

**O custo, e é aqui que o ataque se justifica.** No máximo 256 consultas por byte, 16 bytes por bloco :

| | Consultas |
|---|---|
| Por byte (pior caso / médio) | $256$ / $\approx 128$ |
| Por bloco de 16 bytes | $\le 4096$ / $\approx 2048$ |
| Força bruta sobre a chave AES-128 | $2^{128}$ |

Alguns milhares de requisições HTTP contra $2^{128}$. **A chave nunca é atacada** — o ataque contorna a criptografia em vez de enfrentá-la, e é o exemplo mais limpo da disciplina de que *implementação é superfície de ataque*.

**Em que modelo isso se enquadra.** Texto **cifrado escolhido** — CCA. O atacante submete criptogramas de sua escolha e observa a reação. É exatamente o cenário que a Aula 02 usa para justificar por que o padrão moderno é **IND-CCA2** e não algo mais fraco : o padding oracle é a prova empírica de que o adversário CCA não é uma abstração teórica.

### A história real, e por que a primeira correção não bastou

| Ano | Caso | O que era |
|---|---|---|
| 2002 | **Vaudenay** | o artigo original ; quebrou implementações de SSL/TLS, IPsec e WTLS |
| 2010 | **ASP.NET** (MS10-070) | padding oracle em produção ; permitia ler o `web.config` da aplicação |
| 2013 | **Lucky Thirteen** | o oráculo é **de tempo** — as mensagens de erro já eram iguais |
| 2014 | **POODLE** | força o *downgrade* para SSLv3, cujo padding CBC é inverificável por construção |

A sequência de correções descrita nos slides é a lição de engenharia :

1. *"Sempre gerar o mesmo erro."* — Insuficiente : sobra o tempo de resposta, e o **Lucky Thirteen** explorou exatamente isso.
2. *"Sempre levar o mesmo tempo de resposta."* — Necessário, mas é uma disciplina frágil de manter em código real, sujeita a otimizações de compilador e a efeitos de cache.
3. **A correção de verdade é estrutural** : `Encrypt-then-MAC` ou **AEAD** (AES-GCM, ChaCha20-Poly1305). Com o MAC sobre o criptograma, a tag é verificada **antes** de qualquer decifragem — um criptograma adulterado é rejeitado sem que o padding chegue a ser olhado, e o oráculo deixa de existir. Não há o que vazar porque não há o que computar.

Esse é o fecho do argumento de `Encrypt-then-MAC` que aparece na Aula 13 : a ordem das operações não é preferência de estilo, é o que apaga uma classe inteira de ataques.

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

## Material de Revisão P1 — Funções Resumo : Merkle–Damgård, Davies–Meyer e o Oráculo Aleatório

O material entregue em [provas/p1](../provas/p1/) inclui o deck completo de **funções resumo** e uma lista de exercícios de hash. A Aula 13 cobriu as três propriedades de segurança e o HMAC ; o que faltava era a **construção** — como um hash é montado, e por que montado assim.

### O oráculo aleatório : a ficção que define o alvo

O deck abre com a abstração de **caixa preta** : uma consulta nova recebe uma string aleatória de tamanho fixo, que fica anotada num caderno ; uma consulta repetida recebe a mesma resposta de antes. Esse é o **modelo do oráculo aleatório**, e é o comportamento ideal que um hash deveria ter.

Ele é **impossível**, e a razão é de contagem. O espaço de mensagens é infinito ; o de saídas tem $2^n$ elementos. Pelo **princípio da casa dos pombos**, colisões não apenas existem — existem em quantidade infinita, e nenhum projeto as elimina. Daí a reformulação prática que o deck enuncia :

> Não se exige que colisões não existam. Exige-se que seja **computacionalmente inviável** encontrá-las.

Vale saber que o modelo tem um limite conhecido : **Canetti, Goldreich e Halevi (1998)** construíram esquemas demonstravelmente seguros no modelo do oráculo aleatório e inseguros com **qualquer** função de hash concreta. Provas nesse modelo são, portanto, heurísticas fortes — não garantias. É a razão de a literatura distinguir "seguro no ROM" de "seguro no modelo padrão".

### O paradoxo do aniversário, com a fórmula

O deck de cifras clássicas traz a aproximação que a Aula 13 usou sem enunciar :

$$P_2(m, n) \approx 1 - e^{-n^2 / 2m}$$

onde $m$ é o número de valores possíveis e $n$ o de amostras. Com $m = 365$ :

| $n$ | $P_2$ |
|---|---|
| 23 | 0,507 |
| 30 | 0,706 |

A transposição para hash é direta : $m = 2^n$ saídas possíveis, e a probabilidade de colisão passa de $1/2$ quando o número de amostras chega a $\approx 1{,}18\sqrt{m} = 1{,}18 \cdot 2^{n/2}$. É **exatamente** de onde vem o expoente $n/2$ — não é convenção, é a mesma conta dos aniversários com outro $m$.

### Merkle–Damgård : do bloco para a mensagem

Uma **função de compressão** $h$ processa tamanho fixo : recebe $n + b$ bits (o estado encadeado mais um bloco de mensagem) e devolve $n$. Merkle–Damgård a estende para mensagens arbitrárias :

$$H_0 = \mathrm{IV}, \qquad H_i = h(H_{i-1}, m_i), \qquad H(m) = H_t$$

O último bloco é o **PB** (*padding block*) do diagrama, e sua estrutura importa :

$$\underbrace{1\,0\,0\,0\ldots0}_{\text{separador}} \;\|\; \underbrace{\text{comprimento da mensagem}}_{64 \text{ bits}}$$

Incluir o **comprimento** ali é o *reforço de Merkle–Damgård*, e não é decorativo : sem ele, mensagens de tamanhos diferentes colidem trivialmente por construção do padding. Com ele, vale o teorema que o deck enuncia :

> **Teorema (Merkle–Damgård).** Se a função de compressão $h$ é resistente a colisão, então $H$ é resistente a colisão.

A prova é uma indução para trás, e é curta o suficiente para valer a pena : dada uma colisão $H(m) = H(m')$ com $m \ne m'$, comparem-se os estados encadeados a partir do **último** bloco. Ou em algum ponto entradas diferentes de $h$ produziram a mesma saída — e essa é uma colisão de $h$, contradição — ou todas as entradas coincidem em todos os passos, e então $m = m'$, contradição. O reforço de comprimento é o que fecha o caso em que as mensagens têm tamanhos diferentes.

**O preço da construção.** $H(m)$ **é** o estado interno ao fim do processamento. Quem conhece $H(m)$ e $|m|$ pode continuar a iteração e calcular $H(m \,\|\, \text{padding} \,\|\, s)$ para $s$ arbitrário, **sem conhecer $m$**. Esse é o **ataque de extensão de comprimento**, e é precisamente por isso que o MAC ingênuo $H(k \,\|\, m)$ é quebrado e o HMAC precisa da construção aninhada — o ponto já registrado na Aula 13, agora com a causa estrutural visível.

O **SHA-3 / Keccak** não sofre disso : ele usa construção **esponja**, em que o estado interno é maior que a saída, e a truncagem final destrói a informação necessária para continuar. SHA-512/256 escapa pelo mesmo motivo.

### Davies–Meyer : da cifra de bloco para a função de compressão

Falta um andar : de onde vem $h$? Do **Davies–Meyer**, usado em MD5, SHA-1 e SHA-2 :

$$h(H, m) = E(m, H) \oplus H$$

O detalhe contraintuitivo, e o que mais confunde na hora do exercício : **a mensagem é a chave**, e o estado encadeado é o texto claro. Os tamanhos batem — entrada de $h$ = tamanho da chave + tamanho do bloco ; saída = tamanho do bloco.

**Por que o $\oplus H$ no fim.** Sem ele, $h(H,m) = E(m,H)$ seria **invertível** : conhecendo $m$, qualquer um calcula $D(m, \cdot)$ e caminha para trás na cadeia, construindo pré-imagens à vontade. O XOR de realimentação (*feed-forward*) é o que torna a função unidirecional. É um item de uma linha que decide uma questão de prova.

**Black, Rogaway e Shrimpton (2002)** analisaram as 64 construções possíveis desse tipo e mostraram que, no modelo da cifra ideal, Davies–Meyer atinge o ótimo : $\approx 2^n$ consultas para pré-imagem e $2^{n/2}$ para colisão.

Duas notas práticas : o *key schedule* roda **a cada bloco**, o que é caro — e é a razão de o SHA-2 usar uma cifra dedicada (SHACAL-2) em vez do AES. E, como o atacante controla a chave, o que importa aqui é a segurança da cifra sob **chaves relacionadas**, um requisito muito mais forte do que se pede numa cifra usada apenas para cifrar.

> Os três exercícios de hash do material estão resolvidos, com todos os estados intermediários, na **Parte IV** do [SIMULADO](../provas/p1/SIMULADO.md).

### Senhas : por que *salt* é boa prática e não solução

O deck fecha com um alerta que costuma ser lido rápido demais :

> *Hashear a senha com salt é apenas boa prática. Torna difícil recuperar a senha, não impossível.*

O **salt** resolve um problema específico e apenas ele : impede a **amortização** do ataque. Sem salt, uma tabela arco-íris calculada uma vez serve para todos os vazamentos do mundo, e senhas iguais produzem hashes iguais — o que denuncia quem repete senha. Com salt único por usuário, cada senha exige um ataque próprio.

O que o salt **não** resolve é o **ataque de dicionário**, e a razão é entropia. Dados $H(pw, salt)$ e o $salt$ — que é público e vaza junto —, o atacante testa candidatos até acertar. Isso é viável porque senhas humanas têm entropia baixíssima : seis letras minúsculas são $26^6 \approx 3 \times 10^8 \approx 2^{28}$, o que uma GPU varre em frações de segundo contra um SHA puro.

Daí a diferença já apontada na Aula 13, agora com o motivo completo : para senhas usa-se **bcrypt, scrypt ou Argon2**, funções de **derivação** deliberadamente lentas e com custo de memória ajustável. Elas não aumentam a entropia da senha — elas aumentam o custo de **cada** tentativa, deslocando $2^{28}$ tentativas baratas para $2^{28}$ tentativas caras. Velocidade é vantagem do atacante offline ; a defesa é tirá-la dele.

A lista de vazamentos do deck mostra o estado real da prática :

| Ano | Caso | Como as senhas estavam |
|---|---|---|
| 2010 | Gawker Media | 1,3 milhão em **texto claro** |
| 2012 | LinkedIn | 6,5 milhões em **hash sem salt** |
| 2012 | Yahoo Voices | meio milhão em **texto claro** |
| 2012 | IEEE | 100 mil em **texto claro** |

E a consequência que fecha o tema da Aula 13 : uma colisão em hash de assinatura de código não é hipótese. O **Flame** (2012) forjou um certificado que aparentava vir da Microsoft explorando uma colisão de MD5 no serviço de licenciamento do Terminal Server.

---

## Material de Revisão P1 — Cifras Clássicas : Confusão, Difusão e o Método de Friedman

O deck de cifras clássicas entregue para a P1 abre com um critério que a Aula 04 usou implicitamente sem nomear, e é o critério que organiza a disciplina inteira.

### Confusão e difusão : o critério de Shannon

| | **Confusão** | **Difusão** |
|---|---|---|
| Mecanismo | substituição | transposição / permutação |
| Objetivo | tornar a relação entre **chave** e criptograma o mais complexa possível | espalhar a **redundância** do texto claro por todo o criptograma |
| Sozinha, cai por | análise de frequência | frequências intactas denunciam a cifra |

O deck usa esse par para explicar cada fracasso clássico, e a leitura é a mesma em toda a linha :

- **Substituição monoalfabética** oferece confusão e **nenhuma** difusão. Cada letra guarda sua estatística ⇒ análise de frequência.
- **Transposição** oferece difusão e **nenhuma** confusão. As contagens de letras ficam idênticas às do texto claro ⇒ a própria preservação a denuncia.
- **Vigenère** tem um pouco dos dois, e é por isso que durou três séculos. Mas, nas palavras do deck, "*a transposição não distribui as informações de maneira aleatória*" — sobra padrão, e padrão é o que o Kasiski e o índice de coincidência exploram.

> **Lição :** uma cifra segura combina confusão **e** difusão, e produz criptograma indistinguível de aleatório.

É literalmente o critério que a Aula 02 enuncia como definição formal de segurança — o deck chega nele por outro caminho. E é o que as cifras modernas fazem, em rodadas :

| | Confusão | Difusão |
|---|---|---|
| **AES** (rede SP) | `SubBytes` (S-box não linear) | `ShiftRows` + `MixColumns` |
| **DES** (Feistel) | S-boxes | permutação `P` + estrutura Feistel |

Nenhuma rodada isolada é segura ; a segurança vem da **composição repetida** (10 rodadas no AES-128, 16 no DES). A métrica que se usa para verificar se a composição funcionou é o **efeito avalanche** : virar **um** bit da entrada deve virar aproximadamente **metade** dos bits da saída. É o mesmo critério que o deck de hash cita como propriedade de uma função resumo criptográfica.

### A taxonomia completa das substituições

A Aula 04 cobriu as duas primeiras ; o deck lista quatro :

| Tipo | Como funciona | Exemplo | Como cai |
|---|---|---|---|
| **Monoalfabética** | um alfabeto fixo | César, ROT13 | frequência de letras |
| **Polialfabética** | vários alfabetos alternados | Vigenère | Kasiski / IC, depois César $m$ vezes |
| **Homofônica** | um símbolo do claro ↦ **vários** possíveis | Zodiac Z408, cifras de Beale | frequências achatadas de propósito ⇒ exige digramas e contexto |
| **Poligrâmica** | substitui **grupos** de letras | Playfair, Hill | frequência de digramas / álgebra linear |

Duas notas de vocabulário. O slide escreve "*monofônicas*" para o terceiro tipo — o termo consagrado é **homofônica** (vários símbolos cifrados correspondem ao mesmo claro), e é assim que aparece na bibliografia ; vale escrever o nome certo na prova. E o ponto conceitual : a substituição homofônica é a primeira ideia clássica que ataca a análise de frequência **na raiz**, distribuindo as letras comuns por vários símbolos para achatar a distribuição. Não basta — resta a estrutura de digramas —, mas é o ancestral direto da exigência moderna de saída indistinguível de aleatório.

### ROT13, e a pergunta "por que não ROT14?"

A pergunta do slide tem resposta de uma linha : **13 = 26/2**, então ROT13 é uma **involução** — aplicá-la duas vezes devolve o original. Cifrar e decifrar são a mesma operação, o que permite uma única função, um único comando, nenhum parâmetro. Com ROT14 seria preciso ROT12 para desfazer.

E o ponto que a resposta deve conter : ROT13 **não é criptografia**, porque não tem chave. É ofuscação — esconder *spoilers* e piadas ofensivas na Usenet —, e a propriedade desejada era conveniência, não sigilo. Curiosamente, a mesma autorreciprocidade que torna o ROT13 conveniente é a que condenou a **Enigma** (Aula 03) : o refletor foi adotado pela mesma razão de comodidade operacional. A propriedade é a mesma ; o que muda é que uma delas pretendia ser segura.

### O método de Friedman, operacionalmente

A Aula 04 apresentou o índice de coincidência como ferramenta de **triagem** — que tipo de cifra está na frente. O deck mostra o segundo uso, que é mais fino : **determinar o comprimento da chave** de um Vigenère.

O procedimento :

1. Escolha um candidato $m$ para o comprimento da chave.
2. Reescreva o criptograma em $m$ colunas, tomando uma letra a cada $m$ :
   $$c^{(1)} = c_1 c_{m+1} c_{2m+1}\ldots \qquad c^{(2)} = c_2 c_{m+2} c_{2m+2}\ldots$$
3. Calcule o IC de **cada coluna** separadamente.
4. Se $m$ estiver certo, cada coluna foi cifrada por **uma única** César — logo todas devem dar $\mathrm{IC} \approx 0{,}065$ (inglês) ou $0{,}072$ (português). Se $m$ estiver errado, as colunas misturam deslocamentos diferentes e parecem aleatórias : $\mathrm{IC} \approx 0{,}038$.

O valor aleatório sai de uma conta de uma linha :

$$\mathrm{IC}_{\text{aleatório}} = \sum_{i=0}^{25}\left(\tfrac{1}{26}\right)^2 = 26 \cdot \tfrac{1}{676} = \tfrac{1}{26} \approx 0{,}0385$$

A tabela do deck é o método em ação :

| $m$ | IC por coluna | Veredito |
|---|---|---|
| 1 | 0,043 | baixo |
| 2 | 0,052 ; 0,051 | baixo |
| 3 | 0,050 ; 0,059 ; 0,045 | irregular |
| 4 | 0,049 ; 0,053 ; 0,052 ; 0,051 | baixo |
| **5** | **0,071 ; 0,063 ; 0,070 ; 0,083 ; 0,062** | **todas altas ⇒ $m = 5$** |
| 6 | 0,034 ; 0,050 ; 0,048 ; 0,038 ; 0,045 ; 0,048 | baixo |
| 7 | 0,033 ; 0,041 ; 0,038 ; 0,046 ; 0,041 ; 0,040 ; 0,047 | baixo |

O que se procura é a linha em que **todas** as colunas sobem juntas — não a maior média. Achado $m = 5$, cada coluna vira uma César isolada, e 26 tentativas por coluna encerram o problema.

> **Detalhe que decide questão :** **múltiplos** do comprimento verdadeiro também dão IC alto (com $m = 5$ correto, $m = 10$ e $m = 15$ igualmente funcionam, com metade e um terço dos dados por coluna). Toma-se sempre o **menor** $m$ que faz todas as colunas subirem.

Friedman ainda deixou uma estimativa fechada, útil quando se quer um chute inicial sem varrer $m$ :

$$m \approx \frac{0{,}027\,N}{(N-1)\cdot \mathrm{IC} - 0{,}038\,N + 0{,}065}$$

**Kasiski ou Friedman?** Os dois, e são complementares :

| | **Kasiski** (1863) | **Friedman** (década de 1920) |
|---|---|---|
| Natureza | combinatória — MDC das distâncias entre repetições | estatística — IC por coluna |
| Precisa de | repetições de 3+ letras no criptograma | volume de texto |
| Falha quando | o texto é curto ou há poucas repetições | o texto é curto demais para a estatística |
| Automatizável | sim, mas sensível a coincidências espúrias | sim, e é o método usado na prática |

Na prática roda-se Kasiski para obter candidatos e Friedman para confirmar.

### Os quatro modelos de ataque, com âncoras históricas

A Aula 02 lista a escada COA → KPA → CPA → CCA. O deck dá a cada degrau um caso concreto, e é isso que transforma a lista em resposta dissertativa :

| Modelo | Caso do deck | O que o torna aquele modelo |
|---|---|---|
| **COA** — só criptograma | Enigma : "elos e correntes" | análise puramente estrutural do tráfego, sem texto claro |
| **KPA** — claro conhecido | Enigma : os *cribs* | boletins meteorológicos previsíveis, **observados**, não escolhidos |
| **CPA** — claro escolhido | **Batalha de Midway** (1942) | ver abaixo |
| **CCA** — cifrado escolhido | "ataque na hora do almoço" | acesso temporário a um oráculo de decifragem |

**Midway** merece o parágrafo, porque é o exemplo canônico de CPA e raramente é contado direito. A inteligência americana lia parcialmente o código naval japonês **JN-25** e sabia que um grande ataque visava um alvo chamado `AF` — sem saber qual era. A hipótese era Midway. Para confirmar, ordenaram que Midway transmitisse **em texto claro**, por um canal que sabiam monitorado, que sua usina de dessalinização havia quebrado. Dias depois, o tráfego japonês cifrado informava que `AF` estava com falta de água. Confirmado o alvo, os porta-aviões americanos esperaram a frota japonesa na emboscada que virou a guerra no Pacífico.

Isso é exatamente a definição de **texto claro escolhido** : o atacante **injeta** um texto claro de sua escolha no sistema e observa o criptograma resultante. O detalhe que costuma ser cobrado é que a injeção não precisa ser direta — basta induzir o alvo a cifrar algo conhecido.

E o **"ataque na hora do almoço"** (*lunchtime attack*) é o apelido do **CCA1**, o modelo não-adaptativo : o atacante tem acesso à máquina de decifragem por um período limitado — enquanto o operador almoça — e depois precisa trabalhar só com o que coletou. Distingue-se do **CCA2** (adaptativo), em que o acesso ao oráculo continua depois de ver o criptograma alvo. É contra o CCA2 que se exige segurança hoje, e o **padding oracle** da Aula 11 é justamente um oráculo CCA2 na vida real : o servidor responde para sempre, não só na hora do almoço.

### Referências para ir além

- **Serge Vaudenay, "Security Flaws Induced by CBC Padding" (EUROCRYPT 2002)** — o artigo original do padding oracle. Curto e legível.
- **Ivan Damgård, "A Design Principle for Hash Functions"** e **Ralph Merkle, "One Way Hash Functions and DES"** (ambos CRYPTO 1989) — os dois artigos independentes que fundam a construção.
- **Black, Rogaway & Shrimpton, "Black-Box Analysis of the Block-Cipher-Based Hash-Function Constructions" (CRYPTO 2002)** — a análise das 64 variantes que justifica Davies–Meyer.
- **Cryptopals, conjuntos 2 e 3** — os desafios 16 (*bit-flipping* em CBC) e 17 (*padding oracle*) implementam exatamente esta aula. Fazer o 17 uma vez vale mais que ler o ataque cinco vezes.
- **Friedrich Kasiski, *Die Geheimschriften und die Dechiffrir-Kunst* (1863)** e **William Friedman, *The Index of Coincidence and Its Applications in Cryptography* (1922)** — as duas fontes primárias da criptanálise de Vigenère.
- **`hashcat` e `John the Ripper`** — rodar um ataque de dicionário contra SHA-256 e depois contra bcrypt, na mesma máquina, torna a diferença de custo por tentativa impossível de esquecer.

---
