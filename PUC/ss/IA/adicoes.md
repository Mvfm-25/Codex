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
