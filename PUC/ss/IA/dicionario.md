# Segurança de Sistemas — Dicionário de Conceitos
## [Gerado por IA][mvfm]

> Glossário dos conceitos que aparecem em [adicoes.md](./adicoes.md) e no [SIMULADO](../provas/p1/SIMULADO.md). Cada verbete traz o **conceito**, a **área** e, quando há, um **caso de uso** : um exemplo real, um ataque ou uma aplicação.
> Os verbetes estão em ordem alfabética. O índice por área logo abaixo serve para revisar um bloco da prova de cada vez.

---

### Áreas
| Sigla | Área |
|---|---|
| **FUN** | Fundamentos : metas, princípios, modelos de segurança |
| **CLA** | Criptografia clássica |
| **CAN** | Criptoanálise e modelos de ataque |
| **FLX** | One-Time Pad e cifras de fluxo |
| **BLO** | Cifras de bloco e modos de operação |
| **HSH** | Funções resumo, MAC e senhas |
| **CNF** | Assinatura digital e cadeia de confiança |
| **PEN** | Pentest e superfície de ataque |

### Índice por área
- **FUN** — [[#Autenticidade]] · [[#Confidencialidade]] · [[#Criptografia simétrica e assimétrica]] · [[#Espaço de chaves]] · [[#Indistinguibilidade (IND-CPA, IND-CCA2)]] · [[#Integridade]] · [[#Não-repúdio]] · [[#Princípio de Kerckhoffs]] · [[#Security through obscurity]] · [[#Segurança computacional]] · [[#Usabilidade em segurança]] · [[#Criptografia pós-quântica]] · [[#Algoritmo de Grover]] · [[#Algoritmo de Shor]] · [[#Harvest now, decrypt later]]
- **CLA** — [[#Cifra de César]] · [[#Confusão]] · [[#Difusão]] · [[#Enigma]] · [[#Refletor]] · [[#Playfair]] · [[#ROT13]] · [[#Substituição homofônica]] · [[#Substituição monoalfabética]] · [[#Substituição poligrâmica]] · [[#Substituição polialfabética]] · [[#Transposição]] · [[#Vigenère]]
- **CAN** — [[#Análise de frequência]] · [[#Bombe]] · [[#Canal lateral]] · [[#COA (só criptograma)]] · [[#CPA (texto claro escolhido)]] · [[#CCA (criptograma escolhido)]] · [[#Crib]] · [[#Crib-dragging]] · [[#Exame de Kasiski]] · [[#Força bruta]] · [[#Índice de coincidência]] · [[#KPA (texto claro conhecido)]] · [[#Método de Friedman]] · [[#Modelos de ataque]]
- **FLX** — [[#AES-GCM-SIV]] · [[#Cifra de fluxo]] · [[#Nonce]] · [[#One-Time Pad]] · [[#PRG]] · [[#Sigilo perfeito]] · [[#Two-time pad]] · [[#VENONA]] · [[#WEP]] · [[#XOR]]
- **BLO** — [[#2DES]] · [[#3DES (EDE)]] · [[#AEAD]] · [[#AES]] · [[#CBC]] · [[#Cifra de bloco]] · [[#DES]] · [[#ECB]] · [[#Encrypt-then-MAC]] · [[#Estrutura Feistel]] · [[#IV]] · [[#Maleabilidade]] · [[#Meet-in-the-middle]] · [[#Modo de operação]] · [[#Padding PKCS7]] · [[#Padding oracle attack]] · [[#Rede SP]] · [[#Valor intermediário]]
- **HSH** — [[#Ataque de dicionário]] · [[#Ataque de extensão de comprimento]] · [[#bcrypt, scrypt e Argon2]] · [[#Colisão]] · [[#Construção esponja]] · [[#Davies–Meyer]] · [[#Efeito avalanche]] · [[#Função de compressão]] · [[#Função resumo]] · [[#HMAC]] · [[#MAC]] · [[#MD5 e SHA-1]] · [[#Merkle–Damgård]] · [[#Oráculo aleatório]] · [[#Paradoxo do aniversário]] · [[#Pré-imagem e segunda pré-imagem]] · [[#Princípio da casa dos pombos]] · [[#Salt]] · [[#SHA-2 e SHA-3]] · [[#Tabela arco-íris]]
- **CNF** — [[#Assinatura digital]] · [[#Cadeia de confiança]] · [[#Compilações reprodutíveis]] · [[#Desafio-resposta]] · [[#Independência de software]] · [[#Measured boot]] · [[#Raiz de confiança]] · [[#Reflections on Trusting Trust]] · [[#Teste Público de Segurança]] · [[#Verified boot]]
- **PEN** — [[#Escopo autorizado]] · [[#Exploração]] · [[#Ferramentas de pentest]] · [[#Movimentação lateral]] · [[#Pentest]] · [[#Pós-exploração]] · [[#Reconhecimento]] · [[#Red teaming]] · [[#Relatório]] · [[#Superfície de ataque]] · [[#Varredura e enumeração]] · [[#Vetor de ataque]]

---

## 0–9

### 2DES
- **Área :** BLO
- **Conceito :** DES aplicado duas vezes com chaves independentes, $c = E_{k_2}(E_{k_1}(m))$. A chave nominal tem 112 bits, mas o *meet-in-the-middle* derruba a segurança efetiva para $\approx 2^{57}$ : **um bit** a mais que o DES simples.
- **Caso de uso :** é o exemplo que se usa para explicar por que, depois do *Deep Crack*, a indústria pulou direto para o 3DES. Mostra que contar bits de chave não é o mesmo que medir segurança.

### 3DES (EDE)
- **Área :** BLO
- **Conceito :** DES triplo no formato cifra–decifra–cifra, $E_{k_3}(D_{k_2}(E_{k_1}(m)))$, com 168 bits nominais e $\approx 2^{112}$ efetivos. O passo do meio é um **D** para que, com $k_1 = k_2 = k_3$, ele volte a ser DES simples.
- **Caso de uso :** transição entre o DES e o AES em sistemas bancários e de pagamento, mantendo **compatibilidade com equipamento legado**. O NIST o descontinuou em 2023.

---

## A

### AEAD
- **Área :** BLO
- **Conceito :** *Authenticated Encryption with Associated Data* : cifragem e autenticação feitas numa única operação. Garante confidencialidade e integridade, e ainda autentica dados que vão em claro (cabeçalhos, por exemplo).
- **Caso de uso :** AES-GCM e ChaCha20-Poly1305 no TLS 1.3. A tag é verificada **antes** de decifrar, o que elimina o *padding oracle* na raiz e tira do programador a chance de errar a ordem das operações.

### AES
- **Área :** BLO
- **Conceito :** *Advanced Encryption Standard* (Rijndael), padrão desde 2001. Bloco de 128 bits, chaves de 128, 192 ou 256 bits, estrutura de **rede SP** com 10, 12 ou 14 rodadas. Foi escolhido em competição pública.
- **Caso de uso :** a cifra de bloco padrão atual, presente em TLS, cifragem de disco (BitLocker, FileVault) e Wi-Fi WPA2/WPA3. Instancia o princípio de Kerckhoffs : é público e foi revisado por décadas.

### AES-GCM-SIV
- **Área :** FLX / BLO
- **Conceito :** variante do AES-GCM **resistente ao reuso de nonce**. Se um nonce se repete, ela vaza apenas se duas mensagens são idênticas, em vez de colapsar por completo como o GCM.
- **Caso de uso :** sistemas em que garantir a unicidade do nonce é difícil, como muitos dispositivos sem estado confiável ou nonces aleatórios em grande volume. É a resposta moderna à lição do WEP.

### Algoritmo de Grover
- **Área :** FUN
- **Conceito :** algoritmo quântico de busca com ganho **quadrático** : reduz a força bruta de $2^{n}$ para $2^{n/2}$.
- **Caso de uso :** é o motivo de a criptografia simétrica ser considerada segura contra computação quântica bastando **dobrar a chave**. O AES-256 mantém $2^{128}$ de margem.

### Algoritmo de Shor
- **Área :** FUN
- **Conceito :** algoritmo quântico que fatora inteiros e calcula logaritmos discretos em tempo polinomial, o que quebra RSA e curvas elípticas de forma essencialmente completa.
- **Caso de uso :** é a motivação da padronização pós-quântica do NIST em 2024. Diferente do Grover, contra ele não basta aumentar a chave : é preciso trocar a matemática.

### Análise de frequência
- **Área :** CAN
- **Conceito :** técnica que associa as letras mais frequentes do criptograma às mais frequentes do idioma (em português : `A` ≈ 14,6%, `E` ≈ 12,6%, `O` ≈ 10,7%). Funciona sempre que a cifra preserva a estatística de cada letra.
- **Caso de uso :** quebra uma **substituição monoalfabética** em segundos com cerca de 200 letras de criptograma, apesar das suas $26!$ chaves. Contra uma transposição é inútil, e é justamente essa inutilidade que identifica a transposição.

### Assinatura digital
- **Área :** CNF
- **Conceito :** primitiva **assimétrica** : o autor assina com a chave privada e qualquer pessoa verifica com a chave pública. Fornece integridade, autenticidade e **não-repúdio**. Na prática assina-se o **hash** da mensagem, não a mensagem.
- **Caso de uso :** assinatura de código (instaladores, atualizações de sistema), certificados TLS e cada elo de um *verified boot*. Exemplos de esquemas : RSA-PSS, Ed25519, ML-DSA.

### Ataque de dicionário
- **Área :** HSH
- **Conceito :** testar senhas candidatas (listas, variações, palavras comuns) contra um hash vazado até acertar. É viável porque senhas humanas têm entropia baixa : seis letras minúsculas somam $\approx 2^{28}$ possibilidades.
- **Caso de uso :** `hashcat` rodando contra o vazamento do LinkedIn (2012, SHA-1 sem salt). O salt **não** impede esse ataque ; só funções lentas como bcrypt ou Argon2 encarecem cada tentativa.

### Ataque de extensão de comprimento
- **Área :** HSH
- **Conceito :** em hashes Merkle–Damgård, a saída $H(m)$ **é** o estado interno final. Quem conhece $H(m)$ e $|m|$ consegue calcular $H(m \,\|\, \text{padding} \,\|\, s)$ para qualquer $s$ sem conhecer $m$.
- **Caso de uso :** quebra o MAC ingênuo $H(k \,\|\, m)$ : o atacante acrescenta parâmetros a uma requisição de API autenticada e produz uma tag válida. É o motivo de o HMAC ser aninhado. SHA-3 e SHA-512/256 são imunes.

### Autenticidade
- **Área :** FUN
- **Conceito :** meta de segurança que responde à pergunta *"veio de quem diz ter vindo?"*. Pode ser garantida por **MAC** (entre as partes que compartilham a chave) ou por **assinatura digital** (verificável por qualquer terceiro).
- **Caso de uso :** o cookie de sessão de um site assinado com HMAC. O servidor sabe que foi ele mesmo quem o emitiu.

---

## B

### bcrypt, scrypt e Argon2
- **Área :** HSH
- **Conceito :** funções de derivação para senhas **deliberadamente lentas**, com custo ajustável (e custo de memória no scrypt e no Argon2) e *salt* embutido. Não aumentam a entropia da senha ; aumentam o custo de **cada** tentativa.
- **Caso de uso :** armazenar senhas de usuários num banco de dados. Um SHA-256 puro é rápido demais, e rapidez é vantagem do atacante que tem o banco vazado em mãos (*offline*).

### Bombe
- **Área :** CAN
- **Conceito :** máquina eletromecânica de Turing em Bletchley Park. A partir de um *crib*, derivava contradições lógicas e eliminava blocos inteiros de configurações de rotor de uma vez. É **redução de espaço de busca**, não força bruta.
- **Caso de uso :** leitura diária do tráfego da Enigma na Segunda Guerra, alimentada pelos *cribs* dos boletins meteorológicos (`WETTER`).

---

## C

### Cadeia de confiança
- **Área :** CNF
- **Conceito :** sequência em que cada estágio **verifica a assinatura do próximo antes de lhe passar o controle** : raiz de confiança → firmware → bootloader → kernel → aplicação. A cadeia é tão forte quanto a sua raiz.
- **Caso de uso :** a urna eletrônica : o MSE verifica a BIOS, que verifica o carregador, que verifica o kernel, e só então os aplicativos de eleição são liberados. O mesmo padrão aparece em celulares e consoles.

### Canal lateral
- **Área :** CAN
- **Conceito :** vazamento de informação pela **implementação**, não pela matemática : tempo de resposta, consumo de energia, cache, radiação eletromagnética.
- **Caso de uso :** o **Lucky Thirteen** (2013) recuperou um *padding oracle* pelo **tempo** de resposta, depois de as mensagens de erro já terem sido unificadas.

### CBC
- **Área :** BLO
- **Conceito :** *Cipher Block Chaining* : cada bloco é combinado por XOR com o criptograma anterior antes de ser cifrado. Na decifragem, $m_i = D_k(c_i) \oplus c_{i-1}$, com $c_{-1} = \mathrm{IV}$. Esconde o conteúdo, mas é **maleável**.
- **Caso de uso :** modo usado no TLS até a versão 1.2. É a base do exemplo `dest=80` → `dest=25`, feito alterando só o IV, e do *padding oracle attack*.

### CCA (criptograma escolhido)
- **Área :** CAN
- **Conceito :** o modelo de ataque mais forte : o atacante **escolhe** criptogramas e recebe a decifragem, ou alguma reação a ela. O **CCA1** (*lunchtime attack*) dá acesso ao oráculo só por um período ; no **CCA2** (adaptativo) o acesso continua depois de ver o criptograma alvo.
- **Caso de uso :** o *padding oracle* é CCA2 na vida real : um servidor HTTPS que responde a qualquer requisição, para sempre. É por isso que se exige IND-CCA2 das cifras modernas.

### Cifra de bloco
- **Área :** BLO
- **Conceito :** primitiva que cifra blocos de **tamanho fixo** (64 bits no DES, 128 no AES) sob uma chave. Para mensagens maiores é preciso um **modo de operação**.
- **Caso de uso :** DES, 3DES e AES. Em modo CTR, uma cifra de bloco vira cifra de fluxo.

### Cifra de César
- **Área :** CLA
- **Conceito :** substituição monoalfabética por **deslocamento** fixo no alfabeto. Tem só 25 chaves úteis.
- **Caso de uso :** cai por força bruta em 25 tentativas. Serve de peça básica : cada coluna de um Vigenère é uma César.

### Cifra de fluxo
- **Área :** FLX
- **Conceito :** gera um fluxo pseudoaleatório a partir de uma chave curta e de um nonce, e faz XOR dele com a mensagem : $c = m \oplus \mathrm{PRG}(k, \text{nonce})$. É a estrutura do OTP com o fluxo **gerado** em vez de compartilhado, e troca sigilo perfeito por sigilo computacional.
- **Caso de uso :** ChaCha20 no TLS 1.3 e no WireGuard, e AES-CTR. RC4 foi a cifra de fluxo do WEP e hoje está proibida.

### COA (só criptograma)
- **Área :** CAN
- **Conceito :** modelo de ataque mais fraco : o atacante tem **apenas** criptogramas.
- **Caso de uso :** análise de frequência sobre uma monoalfabética interceptada e a análise estrutural de tráfego da Enigma ("elos e correntes").

### Colisão
- **Área :** HSH
- **Conceito :** duas entradas distintas $m \ne m'$ com $H(m) = H(m')$. Sempre existem, pela casa dos pombos ; a exigência é que seja **inviável encontrá-las**. Achar uma custa $\approx 2^{n/2}$ pelo paradoxo do aniversário.
- **Caso de uso :** assinatura de código : submete-se o instalador legítimo à assinatura e distribui-se o malicioso, que tem o mesmo hash, e a assinatura vale para os dois. O **Flame** (2012) forjou assim um certificado da Microsoft com uma colisão de MD5.

### Compilações reprodutíveis
- **Área :** CNF
- **Conceito :** processo de build **determinístico** : o mesmo fonte com as mesmas ferramentas gera o mesmo binário, bit a bit. Qualquer pessoa pode recompilar e **comparar hashes** em vez de confiar em quem compilou.
- **Caso de uso :** Debian, Tails e Bitcoin Core. É a resposta prática ao limite de *Trusting Trust*.

### Confidencialidade
- **Área :** FUN
- **Conceito :** meta que responde *"quem pode ler?"*, garantida por **cifragem**. Também chamada de privacidade. Não implica integridade.
- **Caso de uso :** HTTPS impede que alguém na mesma rede Wi-Fi leia o conteúdo de uma página. Sozinha, a cifragem não impede que o conteúdo seja **alterado** (ver [[#Maleabilidade]]).

### Confusão
- **Área :** CLA
- **Conceito :** critério de Shannon : tornar a relação entre a **chave** e o criptograma o mais complexa possível. Obtida por **substituição**.
- **Caso de uso :** a S-box (`SubBytes`) do AES e as S-boxes do DES. A monoalfabética tem confusão, mas nenhuma difusão, e por isso cai por frequência.

### Construção esponja
- **Área :** HSH
- **Conceito :** construção de hash em que o estado interno é **maior** que a saída. A mensagem é "absorvida" e a saída é "espremida" e truncada, o que destrói a informação necessária para continuar a iteração.
- **Caso de uso :** SHA-3 (Keccak), que é imune ao ataque de extensão de comprimento.

### CPA (texto claro escolhido)
- **Área :** CAN
- **Conceito :** o atacante **escolhe** textos claros e observa os criptogramas correspondentes. Não precisa injetar diretamente : basta induzir o alvo a cifrar algo conhecido.
- **Caso de uso :** a **Batalha de Midway** (1942). Os EUA fizeram Midway anunciar em claro que sua usina de dessalinização tinha quebrado ; o tráfego japonês cifrado passou a dizer que `AF` estava sem água, o que confirmou o alvo.

### Crib
- **Área :** CAN
- **Conceito :** trecho de texto claro **sabido ou provável** dentro de um criptograma. É o insumo de um ataque KPA.
- **Caso de uso :** `WETTERVORHERSAGE` nos boletins meteorológicos alemães e o `HEILHITLER` no fim das transmissões.

### Crib-dragging
- **Área :** CAN
- **Conceito :** arrastar o *crib* por todas as posições do criptograma e testar cada alinhamento. Na Enigma, elimina-se todo alinhamento em que alguma letra coincide com a letra do cifrado na mesma posição. No two-time pad, faz-se XOR do *crib* com $c_1 \oplus c_2$ e procura-se um trecho legível.
- **Caso de uso :** Simulado Q1d : `WETTER` sobre `XRWTEKMABWET` elimina 5 dos 7 alinhamentos sem cálculo nenhum. No VENONA, recuperou mensagens soviéticas a partir de páginas de pad reutilizadas.

### Criptografia pós-quântica
- **Área :** FUN
- **Conceito :** algoritmos assimétricos baseados em problemas que se acreditam resistentes a computadores quânticos (reticulados, entre outros). Padronizados pelo NIST em 2024 (FIPS 203/204/205).
- **Caso de uso :** ML-KEM (Kyber) para troca de chaves e ML-DSA (Dilithium) para assinatura, já em implantação em navegadores e no TLS.

### Criptografia simétrica e assimétrica
- **Área :** FUN
- **Conceito :** na **simétrica**, a mesma chave cifra e decifra (AES, ChaCha20, HMAC). Na **assimétrica**, há um par de chaves pública e privada (RSA, curvas elípticas, ML-KEM).
- **Caso de uso :** o TLS usa assimétrica para estabelecer uma chave de sessão e simétrica para cifrar o tráfego. Só a assimétrica dá não-repúdio.

---

## D

### Davies–Meyer
- **Área :** HSH
- **Conceito :** constrói uma função de compressão a partir de uma cifra de bloco : $h(H, m) = E(m, H) \oplus H$. **A mensagem é a chave** e o estado encadeado é o texto claro. O XOR final (*feed-forward*) impede a inversão : sem ele, bastaria calcular $D(m,\cdot)$ para andar para trás na cadeia.
- **Caso de uso :** a compressão de MD5, SHA-1 e SHA-2 (sobre a cifra dedicada SHACAL-2). Simulado IV.d : AES-128 com $M_i$ como chave e $H_{i-1}$ como bloco.

### DES
- **Área :** BLO
- **Conceito :** *Data Encryption Standard* (1977), estrutura Feistel, bloco de 64 bits e chave de **56 bits**. Nunca foi quebrado matematicamente : caiu porque a Lei de Moore alcançou o espaço de chaves.
- **Caso de uso :** o **Deep Crack** da EFF (1998, US$ 250 mil) recuperou uma chave em 56 horas. Hoje isso leva horas numa FPGA barata.

### Desafio-resposta
- **Área :** CNF
- **Conceito :** protocolo em que uma parte prova que **possui** uma chave respondendo a um desafio novo, sem transmitir a chave. O desafio novo a cada vez impede a repetição de uma resposta antiga.
- **Caso de uso :** a urna resolve um desafio criptografado antes de carregar os aplicativos. Cartões com chip, chaves FIDO2 e autenticação de controle remoto de carro usam o mesmo princípio.

### Difusão
- **Área :** CLA
- **Conceito :** critério de Shannon : **espalhar a redundância** do texto claro por todo o criptograma. Obtida por **transposição e permutação**.
- **Caso de uso :** `ShiftRows` e `MixColumns` no AES, e a permutação `P` no DES. A transposição pura tem difusão sem confusão, e suas frequências intactas a denunciam.

---

## E

### ECB
- **Área :** BLO
- **Conceito :** *Electronic Codebook* : cada bloco é cifrado de forma independente, com a mesma chave. É **determinístico** : blocos iguais geram criptogramas iguais, então nunca é IND-CPA.
- **Caso de uso :** o contraexemplo clássico. A imagem do pinguim do Linux cifrada em ECB continua mostrando o pinguim. No Simulado IV.d, o ECB aparece só como forma de calcular um único bloco de AES numa ferramenta online.

### Efeito avalanche
- **Área :** HSH / BLO
- **Conceito :** virar **um** bit da entrada deve virar cerca de **metade** dos bits da saída. É a métrica de que confusão e difusão estão funcionando em conjunto.
- **Caso de uso :** no Simulado IV.d, entradas cheias de padrão (`aaaa…`, `00112233…`) produzem hashes sem padrão algum. É também a forma de verificar que uma rodada de AES ou SHA está espalhando bem.

### Encrypt-then-MAC
- **Área :** BLO / HSH
- **Conceito :** a ordem correta : cifra-se primeiro e depois calcula-se o MAC **sobre o criptograma**. O receptor verifica a tag **antes** de decifrar. As alternativas, `MAC-then-Encrypt` e `Encrypt-and-MAC`, levaram a ataques reais.
- **Caso de uso :** a correção **estrutural** do *padding oracle* : um criptograma adulterado é rejeitado sem que o padding chegue a ser olhado, e o oráculo deixa de existir. `MAC-then-Encrypt` era o erro do SSL/TLS antigo.

### Enigma
- **Área :** CLA / CAN
- **Conceito :** máquina alemã de rotores. Tecla → plugboard → 3 rotores → refletor → rotores → plugboard → lâmpada. É polialfabética, com período de 16 900 e espaço de chaves de $\approx 1{,}59 \times 10^{20}$ (≈ 67 bits).
- **Caso de uso :** o estudo de caso que junta tudo : Kerckhoffs (os Aliados conheciam o projeto), KPA (os *cribs*), o defeito estrutural do refletor e o elo humano. Rejewski, Różycki e Zygalski a quebraram em 1932 ; Bletchley Park continuou o trabalho.

### Escopo autorizado
- **Área :** PEN
- **Conceito :** as **regras de engajamento** acordadas por escrito : alvos, janelas de tempo e técnicas permitidas. É o **único** elemento que separa juridicamente um pentest de um crime, já que a atividade técnica é idêntica.
- **Caso de uso :** Simulado Q4 : alcançar outro host da rede interna é movimentação lateral autorizada se estiver no escopo, e invasão se não estiver.

### Espaço de chaves
- **Área :** FUN
- **Conceito :** o número de chaves possíveis ; com $n$ bits, $2^n$. Limita **apenas** a força bruta. É condição necessária, nunca suficiente.
- **Caso de uso :** DES ($2^{56}$) caiu por força bruta. A monoalfabética ($26! \approx 4\times 10^{26}$) e a Enigma ($10^{20}$) caíram mesmo com espaços enormes, porque tinham estrutura explorável.

### Estrutura Feistel
- **Área :** BLO
- **Conceito :** divide o bloco em duas metades e, a cada rodada, aplica uma função à metade direita e combina o resultado por XOR com a esquerda, trocando as metades em seguida. Decifrar é a mesma estrutura com as subchaves em ordem inversa, e a função interna nem precisa ser invertível.
- **Caso de uso :** o DES, com 16 rodadas. Resistiu à criptoanálise diferencial, sinal de que a NSA já conhecia a técnica nos anos 70.

### Exame de Kasiski
- **Área :** CAN
- **Conceito :** método **combinatório** (1863) : sequências repetidas de 3 ou mais letras num criptograma de Vigenère aparecem a distâncias múltiplas do comprimento da chave. O MDC dessas distâncias dá o período $m$.
- **Caso de uso :** achar o comprimento da chave de um Vigenère. Na prática, usa-se para gerar candidatos e o Friedman para confirmar.

### Exploração
- **Área :** PEN
- **Conceito :** a fase do pentest em que uma vulnerabilidade encontrada é **efetivamente usada** para obter acesso.
- **Caso de uso :** Simulado Q4 : entrar no serviço de administração com a credencial padrão de fábrica. Ferramenta típica : `Metasploit`.

---

## F

### Ferramentas de pentest
- **Área :** PEN
- **Conceito :** as ferramentas associadas a cada fase :

| Ferramenta | Uso | Fase |
|---|---|---|
| `nmap` | varredura de portas, detecção de serviço | varredura |
| `Nessus` / `OpenVAS` | varredura de vulnerabilidades | varredura / enumeração |
| `Burp Suite` | interceptação e teste de aplicações web | enumeração / exploração |
| `Metasploit` | exploração | exploração |
| `Wireshark` | análise de tráfego | reconhecimento / pós-exploração |
| `hashcat` / `John` | quebra de hash *offline* | pós-exploração |

- **Caso de uso :** Simulado Q4d : `Burp` sobre o formulário de login e a API REST, `nmap` para descobrir a porta alta.

### Força bruta
- **Área :** CAN
- **Conceito :** testar todas as chaves : custo de $2^n$ no pior caso e $2^{n-1}$ em média. É o **pior caso do atacante**, nunca o caminho que ele escolhe.
- **Caso de uso :** o *Deep Crack* contra o DES. Contra o AES-128 ($3{,}4 \times 10^{38}$) está fora de alcance, então ataques reais procuram chaves fracas, reuso de nonce e canais laterais.

### Função de compressão
- **Área :** HSH
- **Conceito :** função de entrada de **tamanho fixo** ($n + b$ bits : estado encadeado mais bloco de mensagem) que devolve $n$ bits. É o bloco básico que Merkle–Damgård itera.
- **Caso de uso :** Davies–Meyer sobre AES no Simulado IV.d.

### Função resumo
- **Área :** HSH
- **Conceito :** hash criptográfico : mapeia entrada de tamanho arbitrário numa saída fixa de $n$ bits, com resistência à pré-imagem ($2^n$), à segunda pré-imagem ($2^n$) e à colisão ($2^{n/2}$). Sozinha, dá integridade apenas contra erros, não contra atacantes, porque o atacante também consegue recalcular o hash.
- **Caso de uso :** verificar o checksum SHA-256 de uma ISO baixada, fazer *commits* no Git, assinar o hash de um documento. Não serve sozinha para guardar senhas.

---

## H

### Harvest now, decrypt later
- **Área :** FUN
- **Conceito :** estratégia de **gravar hoje** tráfego cifrado com criptografia assimétrica clássica para decifrá-lo quando existir um computador quântico capaz de rodar o Shor.
- **Caso de uso :** é o que motiva migrar **já** para ML-KEM dados com vida útil longa : diplomáticos, médicos, segredos industriais.

### HMAC
- **Área :** HSH
- **Conceito :** MAC padrão baseado em hash, com construção **aninhada** : $H\big((k \oplus \text{opad}) \,\|\, H((k \oplus \text{ipad}) \,\|\, m)\big)$. O aninhamento existe para resistir ao ataque de extensão de comprimento.
- **Caso de uso :** autenticação de requisições em APIs (AWS SigV4), tokens JWT HS256, cookies de sessão e senhas de uso único (TOTP).

---

## I

### Independência de software
- **Área :** CNF
- **Conceito :** critério de **Ron Rivest** : um sistema de votação é *software-independent* se um erro ou alteração não detectado no software **não puder** causar uma mudança não detectável no resultado. Exige um registro fora do software, tipicamente o **VVPAT** (comprovante em papel conferido pelo eleitor).
- **Caso de uso :** a discussão acadêmica sobre urnas eletrônicas. Distingue *"é muito difícil fraudar"* de *"uma fraude seria necessariamente detectável"*.

### Indistinguibilidade (IND-CPA, IND-CCA2)
- **Área :** FUN
- **Conceito :** a definição moderna de segurança (Goldwasser & Micali, 1982). O adversário escolhe $m_0$ e $m_1$, recebe a cifragem de uma delas e precisa adivinhar qual foi ; a cifra é segura se ele não acerta com probabilidade significativamente maior que $1/2$. Consequência : **uma cifra determinística nunca é IND-CPA**. IND-CCA2 é a mesma exigência com acesso a um oráculo de decifragem.
- **Caso de uso :** o critério usado para aprovar modos e esquemas. Mostra por que o ECB é inseguro e por que todo modo sério exige IV ou nonce.

### Índice de coincidência
- **Área :** CAN
- **Conceito :** probabilidade de duas letras sorteadas do texto serem iguais : $\mathrm{IC} = \sum n_i(n_i-1) / N(N-1)$. Português ≈ 0,072, inglês ≈ 0,065–0,067, texto aleatório = $1/26 \approx 0{,}0385$.
- **Caso de uso :** **triagem** : IC alto num texto ilegível indica monoalfabética ou transposição ; IC baixo indica polialfabética. Em segundo uso, é a base do método de Friedman.

### Integridade
- **Área :** FUN
- **Conceito :** meta que responde *"foi alterado?"*. Contra atacantes exige **MAC** ou assinatura, porque um hash puro o próprio atacante recalcula.
- **Caso de uso :** o ponto central da Aula 11 : **confidencialidade não implica integridade**. O CBC esconde `saldo: 100` e ainda assim permite reescrevê-lo.

### IV
- **Área :** BLO
- **Conceito :** *Initialization Vector* : valor que entra no primeiro bloco para tornar a cifragem **não determinística**. Vai em claro junto com o criptograma. No CBC precisa ser imprevisível.
- **Caso de uso :** no CBC, alterar o IV altera exatamente os bits correspondentes do primeiro bloco de texto claro sem corromper nada, o que viabiliza o `dest=80` → `dest=25`. No WEP, o IV de 24 bits era curto demais e se repetia.

---

## K

### KPA (texto claro conhecido)
- **Área :** CAN
- **Conceito :** o atacante tem pares $(m, c)$ que **observou**, mas não escolheu.
- **Caso de uso :** a Enigma caiu em KPA, por meio dos *cribs*. O *meet-in-the-middle* sobre o 2DES também é KPA : precisa de um ou dois pares conhecidos.

---

## M

### MAC
- **Área :** HSH
- **Conceito :** *Message Authentication Code* : hash **com chave**, que dá integridade e autenticidade. Como a chave é **simétrica**, **não dá não-repúdio** : qualquer tag que Alice produziu, Bob também poderia ter produzido.
- **Caso de uso :** HMAC e Poly1305 autenticando pacotes no TLS e no WireGuard. Diante de um juiz, um MAC não prova quem gerou a mensagem.

### Maleabilidade
- **Área :** BLO
- **Conceito :** propriedade de um esquema em que o atacante altera o criptograma e produz uma alteração **previsível** no texto claro, sem conhecer a chave. No CBC, virar um bit de $c_{i-1}$ vira o mesmo bit de $m_i$. Em cifras de fluxo e CTR, virar um bit de $c$ vira o mesmo bit de $m$. A maleabilidade é do **modo**, não da primitiva.
- **Caso de uso :** $\mathrm{IV}' = \mathrm{IV} \oplus (\texttt{...80...}) \oplus (\texttt{...25...})$ redireciona um pacote. Trocar DES por AES não resolve ; autenticar o criptograma resolve.

### MD5 e SHA-1
- **Área :** HSH
- **Conceito :** hashes Merkle–Damgård de 128 e 160 bits, hoje **quebrados para colisão**. MD5 gera colisões em segundos ; o SHA-1 teve a primeira colisão prática demonstrada em 2017 (*SHAttered*, do Google).
- **Caso de uso :** o Flame forjou um certificado com colisão de MD5. O LinkedIn guardava senhas em SHA-1 sem salt. Hoje, só para usos não criptográficos.

### Measured boot
- **Área :** CNF
- **Conceito :** cada estágio do boot calcula o **hash** do próximo e o **registra** num TPM, sem impedir a execução. O boot acontece, mas o registro denuncia qualquer alteração.
- **Caso de uso :** atestação remota e BitLocker, que só libera a chave do disco se as medições baterem.

### Meet-in-the-middle
- **Área :** BLO / CAN
- **Conceito :** ataque ao 2DES que explora $E_{k_1}(m) = D_{k_2}(c)$ : cifra-se $m$ sob todas as $2^{56}$ chaves e guarda-se o resultado numa tabela ; decifra-se $c$ sob todas as $2^{56}$ chaves procurando coincidência ; confirma-se com um segundo par. Custa $\approx 2^{57}$ operações e $2^{56}$ de memória. **Troca memória por tempo.**
- **Caso de uso :** justifica a existência do 3DES e mostra, junto com a Enigma e a monoalfabética, que contar bits não é medir segurança.

### Merkle–Damgård
- **Área :** HSH
- **Conceito :** estende uma função de compressão a mensagens de qualquer tamanho : $H_0 = \mathrm{IV}$, $H_i = h(H_{i-1}, m_i)$. O último bloco leva `1000…0` e o **comprimento da mensagem**, o chamado *reforço*, que é obrigatório. **Teorema :** se $h$ resiste a colisão, $H$ também resiste. O preço é o ataque de extensão de comprimento.
- **Caso de uso :** a estrutura de MD5, SHA-1 e SHA-2. É iterada à mão no Simulado IV.d.

### Método de Friedman
- **Área :** CAN
- **Conceito :** método **estatístico** para achar o comprimento da chave de um Vigenère : para cada candidato $m$, divide-se o criptograma em $m$ colunas e calcula-se o IC de cada uma. O $m$ certo é o **menor** em que **todas** as colunas sobem para o IC do idioma, já que os múltiplos dele também sobem.
- **Caso de uso :** na tabela do deck, $m = 5$ dá todas as colunas entre 0,062 e 0,083 ; depois disso, cada coluna é uma César e cai em 26 tentativas. Simulado Q18.

### Modelos de ataque
- **Área :** CAN
- **Conceito :** a hierarquia do que o adversário pode obter, em ordem crescente de poder : **COA → KPA → CPA → CCA**. Um sistema é avaliado pelo modelo mais forte ao qual resiste.
- **Caso de uso :** ancorar uma dissertativa : Enigma (KPA), Midway (CPA), *padding oracle* (CCA2).

### Modo de operação
- **Área :** BLO
- **Conceito :** a regra que estende uma cifra de bloco a mensagens de vários blocos : ECB, CBC, CTR, GCM e outros. É no modo, e não na primitiva, que estão propriedades como determinismo, maleabilidade e autenticação.
- **Caso de uso :** o mesmo AES é inseguro em ECB, maleável em CBC e autenticado em GCM.

### Movimentação lateral
- **Área :** PEN
- **Conceito :** parte da pós-exploração em que, com acesso a um host, o atacante **avança para outros** dentro da rede.
- **Caso de uso :** Simulado Q4 : usar o serviço de administração comprometido para alcançar outro host interno. É o ponto em que o escopo escrito decide o que é permitido.

---

## N

### Não-repúdio
- **Área :** FUN
- **Conceito :** meta que responde *"o autor pode negar depois?"*. **Somente a assinatura digital** a fornece, porque a chave privada pertence a uma só parte.
- **Caso de uso :** contratos assinados com certificado ICP-Brasil e transações bancárias assinadas. Um MAC não serve para isso.

### Nonce
- **Área :** FLX / BLO
- **Conceito :** *number used once* : valor que **nunca pode se repetir** sob a mesma chave. Em cifras de fluxo e no GCM, repetir o par (chave, nonce) repete o fluxo gerado.
- **Caso de uso :** o AES-GCM é catastrófico sob reuso de nonce : vaza o XOR dos textos claros e permite forjar tags. Daí o AES-GCM-SIV.

---

## O

### One-Time Pad
- **Área :** FLX
- **Conceito :** $c = m \oplus k$, com $k$ verdadeiramente aleatório, **do tamanho da mensagem** e **usado uma única vez**. É o único sistema com **sigilo perfeito** demonstrado (Shannon, 1949). Na prática é inviável por três motivos : a distribuição da chave (que é circular), a aleatoriedade real e o não-reuso.
- **Caso de uso :** o "telefone vermelho" Washington–Moscou durante a Guerra Fria. O VENONA é o contraexemplo : o que quebrou ali foi o procedimento, não a matemática.

### Oráculo aleatório
- **Área :** HSH
- **Conceito :** a abstração do hash ideal : uma consulta nova recebe uma resposta aleatória, e uma consulta repetida recebe a mesma resposta de antes. Não é realizável. Canetti, Goldreich e Halevi (1998) mostraram esquemas seguros nesse modelo e inseguros com **qualquer** hash concreto.
- **Caso de uso :** modelo usado em provas de segurança de esquemas como RSA-OAEP e assinaturas de Schnorr. É uma heurística forte, não uma garantia.

---

## P

### Padding oracle attack
- **Área :** BLO / CAN
- **Conceito :** ataque de Vaudenay (2002) que **decifra** um criptograma CBC usando só um bit de resposta, *"o padding é válido?"*. Varrendo o bloco anterior $R$, obtém-se $I[15] = R[15] \oplus \texttt{01}$, depois $I[14] = R[14] \oplus \texttt{02}$, e assim por diante, com $m = I \oplus c_{i-1}$. O oráculo pode ser um erro distinguível, a ausência de resposta ou o tempo de resposta. Custa no máximo **4096 consultas** por bloco, e **a chave nunca é atacada**.
- **Caso de uso :** SSL/TLS e IPsec (2002), ASP.NET MS10-070 (2010, leitura do `web.config`), Lucky Thirteen (2013, oráculo de tempo) e POODLE (2014). A correção definitiva é Encrypt-then-MAC ou AEAD.

### Padding PKCS7
- **Área :** BLO
- **Conceito :** completa o último bloco com $p$ bytes de valor $p$ : `01`, `02 02`, `05 05 05 05 05`. É validado na decifragem.
- **Caso de uso :** é exatamente essa validação que vira oráculo. A armadilha do ataque é o falso positivo `02 02` na varredura do último byte, eliminado alterando $R[14]$ e repetindo (Simulado Q14).

### Paradoxo do aniversário
- **Área :** HSH
- **Conceito :** a probabilidade de colisão entre $n$ amostras de $m$ valores é $P \approx 1 - e^{-n^2/2m}$. Passa de 50% com $n \approx 1{,}18\sqrt{m}$ : 23 pessoas para 365 dias, e $\approx 2^{n/2}$ amostras para um hash de $n$ bits.
- **Caso de uso :** é o motivo de o SHA-256 ter só 128 bits de segurança contra colisão, e de um hash de assinatura precisar do dobro de bits da segurança desejada.

### Pentest
- **Área :** PEN
- **Conceito :** avaliação de segurança **autorizada** que simula um atacante real. Fases : reconhecimento → varredura e enumeração → exploração → pós-exploração e movimentação lateral → **relatório**.
- **Caso de uso :** uma empresa contrata o teste da sua rede antes de uma auditoria PCI-DSS. Simulado Q4.

### Playfair
- **Área :** CLA
- **Conceito :** substituição **poligrâmica** que cifra **pares** de letras usando uma grade 5×5 montada a partir da chave. Derruba a análise de frequência de letras isoladas, mas não a de digramas.
- **Caso de uso :** usada de verdade pelos britânicos na Primeira Guerra. Cai por frequência de digramas (`TH`, `HE`, `IN`).

### Pós-exploração
- **Área :** PEN
- **Conceito :** depois do acesso inicial : escalar privilégios, coletar credenciais, persistir e mover-se lateralmente.
- **Caso de uso :** extrair hashes de senha do host comprometido e quebrá-los *offline* com `hashcat`.

### Pré-imagem e segunda pré-imagem
- **Área :** HSH
- **Conceito :** **pré-imagem** : dado $h$, achar $m$ com $H(m) = h$. **Segunda pré-imagem** : dado $m$, achar $m' \ne m$ com o mesmo hash. As duas custam $2^n$, porque o alvo é fixo, ao contrário da colisão.
- **Caso de uso :** a resistência à pré-imagem é o que impede recuperar uma senha a partir do hash por inversão. A segunda pré-imagem é o que impede trocar um arquivo já publicado por outro com o mesmo checksum.

### Princípio da casa dos pombos
- **Área :** HSH
- **Conceito :** se há mais itens que caixas, alguma caixa recebe dois. Como há infinitas mensagens e só $2^n$ saídas, colisões **existem necessariamente**, e em quantidade infinita.
- **Caso de uso :** fundamenta a reformulação prática : não se exige que colisões não existam, exige-se que seja inviável **encontrá-las**.

### Princípio de Kerckhoffs
- **Área :** FUN
- **Conceito :** o sistema deve ser seguro mesmo que tudo sobre ele, **exceto a chave**, seja público. Na forma de Shannon : *"o inimigo conhece o sistema"*. A chave é um segredo pequeno, trocável e individual ; o algoritmo é grande, imutável e coletivo.
- **Caso de uso :** os padrões são escolhidos em competições públicas : DES (1977), AES (2001), SHA-3 (2012), ML-KEM e ML-DSA (2024). A Enigma o confirma : os Aliados conheciam o projeto, e o segredo estava, como deve estar, na chave diária.

### PRG
- **Área :** FLX
- **Conceito :** gerador pseudoaleatório criptográfico : expande uma chave curta num fluxo longo **indistinguível de aleatório** para um adversário eficiente. É diferente de um `rand()` comum.
- **Caso de uso :** o núcleo de toda cifra de fluxo (ChaCha20). Trocar a chave verdadeiramente aleatória do OTP por um PRG transforma o OTP numa cifra de fluxo, com segurança apenas computacional.

---

## R

### Raiz de confiança
- **Área :** CNF
- **Conceito :** o primeiro elo de uma cadeia de confiança, **imutável** e em hardware, com a chave pública gravada de fábrica e sem caminho de escrita. Tudo o que vem depois é tão confiável quanto ela.
- **Caso de uso :** o **MSE** da urna, o Secure Enclave da Apple, o chip Titan do Google e o TPM.

### Reconhecimento
- **Área :** PEN
- **Conceito :** primeira fase do pentest : coletar informação sobre o alvo. **Passivo**, sem tocar no alvo (OSINT, sites, registros DNS) ; **ativo**, interagindo com ele.
- **Caso de uso :** Simulado Q4 : a lista de funcionários publicada no site, colhida de forma passiva, serve de insumo para phishing.

### Red teaming
- **Área :** PEN / CNF
- **Conceito :** equipe que atua como adversário para testar defesas reais, com objetivos definidos. Um teste mostra a **presença** de defeitos, nunca a sua ausência (Dijkstra).
- **Caso de uso :** o **Teste Público de Segurança** do TSE.

### Rede SP
- **Área :** BLO
- **Conceito :** rede de substituição-permutação : rodadas que alternam camadas de **substituição** (confusão) e de **permutação** (difusão). Nenhuma rodada é segura sozinha ; a segurança vem da composição repetida.
- **Caso de uso :** o AES, com `SubBytes`, `ShiftRows`, `MixColumns` e `AddRoundKey`, repetidos por 10 rodadas no AES-128.

### Reflections on Trusting Trust
- **Área :** CNF
- **Conceito :** discurso de Ken Thompson no Turing Award de 1984. Um compilador pode inserir uma porta dos fundos num programa alvo **e** se reinserir ao compilar a si mesmo, deixando o código-fonte limpo. Auditar o fonte prova propriedades **do fonte**, não do binário.
- **Caso de uso :** é o limite da auditoria de código da urna. O ataque à cadeia de build da SolarWinds (2020) foi uma versão moderna. A resposta prática são as compilações reprodutíveis.

### Refletor
- **Área :** CLA / CAN
- **Conceito :** componente da Enigma que devolve a corrente pelos rotores por outro caminho, tornando a máquina **auto-recíproca** (a mesma configuração cifra e decifra). Consequência fatal : **nenhuma letra é cifrada como ela mesma**.
- **Caso de uso :** é o que torna possível o *crib-dragging* : todo alinhamento com uma letra coincidente é eliminado sem cálculo. É o exemplo de que conveniência operacional custa segurança.

### Relatório
- **Área :** PEN
- **Conceito :** o **entregável** do pentest : achados, evidências, risco e recomendações de correção. É o que distingue uma avaliação de uma intrusão.
- **Caso de uso :** Simulado Q4c : sem relatório houve invasão, não pentest.

### ROT13
- **Área :** CLA
- **Conceito :** César com deslocamento 13. Como $13 = 26/2$, é uma **involução** : aplicá-la duas vezes devolve o original. **Não é criptografia**, porque não tem chave ; é ofuscação.
- **Caso de uso :** esconder *spoilers* e piadas na Usenet. A autorreciprocidade que o torna conveniente é a mesma que condenou a Enigma.

---

## S

### Salt
- **Área :** HSH
- **Conceito :** valor aleatório, único por usuário e **público**, misturado à senha antes do hash. Impede a **amortização** : tabelas pré-calculadas deixam de servir, e senhas iguais deixam de ter hashes iguais. **Não** impede o ataque de dicionário.
- **Caso de uso :** o LinkedIn (2012) guardava senhas sem salt, e uma única tabela quebrava milhões de contas. Com salt, cada senha exige um ataque próprio.

### Security through obscurity
- **Área :** FUN
- **Conceito :** fazer a segurança depender do **sigilo do algoritmo**. É o que Kerckhoffs proíbe : a raridade do atacante capaz não é uma propriedade do sistema.
- **Caso de uso :** A5/1 (GSM), CSS (DVD), Mifare Classic e KeeLoq (chaves de carro) foram quebrados depois de o algoritmo secreto ser recuperado por engenharia reversa (Simulado Q2).

### Segurança computacional
- **Área :** FUN
- **Conceito :** garantia de que nenhum adversário **eficiente** obtém vantagem significativa. Opõe-se à segurança **perfeita**, que vale contra poder computacional infinito.
- **Caso de uso :** AES, RSA, ChaCha20 : tudo o que se usa na prática. A troca é aceitar um "inviável sem $2^{128}$ operações" em vez de um "impossível", em troca de chaves curtas.

### SHA-2 e SHA-3
- **Área :** HSH
- **Conceito :** **SHA-2** (SHA-256, SHA-512) usa Merkle–Damgård com Davies–Meyer sobre a cifra SHACAL-2. **SHA-3** (Keccak, 2012) usa construção esponja e é imune à extensão de comprimento. São o padrão atual para uso geral.
- **Caso de uso :** SHA-256 no Bitcoin, em certificados TLS e em *reproducible builds*. SHA-3 quando se quer uma estrutura independente do SHA-2.

### Sigilo perfeito
- **Área :** FLX / FUN
- **Conceito :** definição de Shannon : $\Pr[M{=}m \mid C{=}c] = \Pr[M{=}m]$, ou seja, ver o criptograma não altera nada do que se sabe sobre a mensagem. Exige $|K| \ge |M|$, e isso é **teorema**, não inconveniência.
- **Caso de uso :** no OTP, toda mensagem candidata tem exatamente uma chave compatível, $k' = c \oplus m'$. Interceptar `ATACAR AS 6` é o mesmo que interceptar `RECUAR AS 9`.

### Substituição homofônica
- **Área :** CLA
- **Conceito :** cada letra do claro corresponde a **vários** símbolos cifrados possíveis, o que achata a distribuição de frequências de propósito. O slide escreve "monofônica", mas o termo correto é **homofônica**. É a primeira ideia clássica que ataca a análise de frequência na raiz.
- **Caso de uso :** o Z408 do assassino do Zodíaco e as cifras de Beale. Cai por digramas e contexto.

### Substituição monoalfabética
- **Área :** CLA
- **Conceito :** um único alfabeto permutado para toda a mensagem. Tem $26! \approx 4 \times 10^{26}$ chaves, confusão sem difusão, e **preserva o IC** do idioma.
- **Caso de uso :** criptogramas de jornal e revistas de passatempo. É o exemplo de que um espaço de chaves enorme não protege nada : cai por frequência em segundos.

### Substituição poligrâmica
- **Área :** CLA
- **Conceito :** substitui **grupos** de letras de uma vez, em vez de letras isoladas.
- **Caso de uso :** Playfair (digramas) e Hill (álgebra linear sobre matrizes). Caem por frequência de digramas e por álgebra linear com texto claro conhecido.

### Substituição polialfabética
- **Área :** CLA
- **Conceito :** usa **vários** alfabetos, alternados segundo a chave ; a mesma letra do claro vira letras diferentes. Baixa o IC em direção a 0,038.
- **Caso de uso :** Vigenère e Enigma. Caem quando se descobre o período (Kasiski ou Friedman) ou por *cribs*.

### Superfície de ataque
- **Área :** PEN
- **Conceito :** o **conjunto** de todos os pontos em que um atacante pode tentar entrar ou extrair dados : portas, endpoints, formulários, bibliotecas de terceiros, pessoas. A defesa primária é **reduzi-la**.
- **Caso de uso :** Simulado Q4 : formulário de login, API REST, porta alta de administração, biblioteca desatualizada e a lista de funcionários (superfície humana). Reduzir significa fechar o serviço de administração, atualizar a biblioteca e tirar a lista do site.

---

## T

### Tabela arco-íris
- **Área :** HSH
- **Conceito :** estrutura **pré-calculada** que troca armazenamento por tempo para inverter hashes de senhas. É calculada uma vez e reaproveitada em qualquer vazamento sem salt.
- **Caso de uso :** quebrar em massa hashes MD5 ou NTLM sem salt. Um salt único por usuário a torna inútil.

### Teste Público de Segurança
- **Área :** CNF / PEN
- **Conceito :** o TPS do TSE : ciclos abertos de ataque à urna, realizados desde 2009 e obrigatórios desde 2017, com planos de teste, **reprodutibilidade exigida** e barreiras relaxadas de propósito para testar um mecanismo específico.
- **Caso de uso :** medir a resistência de mecanismos da urna sob condições concedidas. Não demonstra a ausência de vulnerabilidades, e por isso a formulação honesta é "suficientemente seguro".

### Transposição
- **Área :** CLA
- **Conceito :** **reordena** as letras em vez de substituí-las : difusão sem confusão. As frequências ficam **idênticas** às do texto claro.
- **Caso de uso :** a transposição colunar e a cítala espartana. Diagnóstico (Simulado Q3–Q4) : IC igual ao do idioma e contagem de letras igual à do claro indicam transposição.

### Two-time pad
- **Área :** FLX
- **Conceito :** reusar a chave de um OTP, ou o par (chave, nonce) de uma cifra de fluxo. A chave se cancela : $c_1 \oplus c_2 = m_1 \oplus m_2$. O que converte essa diferença em texto é a **redundância do idioma** ou um *crib*.
- **Caso de uso :** VENONA, WEP e AES-GCM com nonce repetido. Simulado Q2b : $11111101 \oplus 11111100 = 00000001$, as mensagens diferem num único bit. Simulado IV.c : recuperar textos e chave de mensagens cifradas com a mesma chave.

---

## U

### Usabilidade em segurança
- **Área :** FUN
- **Conceito :** herdeiro do sexto princípio de Kerckhoffs ("o sistema deve ser fácil de usar") : criptografia que ninguém consegue usar direito não protege ninguém.
- **Caso de uso :** *Why Johnny Can't Encrypt* (1999) mostrou que usuários competentes erravam com o PGP. É o motivo de Signal e WhatsApp cifrarem por padrão sem expor chave nenhuma.

---

## V

### Valor intermediário
- **Área :** BLO
- **Conceito :** no *padding oracle*, $I = D_k(c)$ : a saída da cifra **antes** do XOR com o bloco anterior. Recuperar $I$ byte a byte equivale a decifrar o bloco, porque $m_i = I \oplus c_{i-1}$.
- **Caso de uso :** a notação da Dissertativa 5b do Simulado.

### Varredura e enumeração
- **Área :** PEN
- **Conceito :** segunda fase do pentest : descobrir portas, serviços e versões, e listar usuários, diretórios e vulnerabilidades conhecidas.
- **Caso de uso :** `nmap -sV` revela o serviço na porta alta e a versão da biblioteca. `Nessus` associa essa versão a CVEs conhecidas.

### VENONA
- **Área :** FLX / CAN
- **Conceito :** projeto dos EUA (anos 1940–1980) que decifrou milhares de telegramas soviéticos cifrados com OTP, porque um fornecedor pressionado pela guerra **duplicou páginas** dos blocos de chave. Levou décadas, porque converter $m_1 \oplus m_2$ em texto exigiu acumular tráfego, *cribs* e livros de código capturados.
- **Caso de uso :** o caso histórico do two-time pad : a criptografia era perfeita, o procedimento não era.

### Verified boot
- **Área :** CNF
- **Conceito :** cada estágio verifica a **assinatura** do próximo e **se recusa** a executá-lo se a verificação falhar. A máquina não inicializa com código alterado.
- **Caso de uso :** a urna (MSE), o UEFI Secure Boot, o Android Verified Boot e consoles de videogame.

### Vetor de ataque
- **Área :** PEN
- **Conceito :** o **caminho específico** usado numa tentativa concreta. É um elemento da superfície de ataque que foi efetivamente explorado.
- **Caso de uso :** Simulado Q4 : entre todos os itens do cenário, só o uso da **credencial padrão** é vetor ; o resto é superfície. Outros exemplos : injeção de SQL num campo, e-mail de phishing.

### Vigenère
- **Área :** CLA
- **Conceito :** César com uma chave que se repete : cada letra da chave define um deslocamento, de forma cíclica. Tem $26^m$ chaves e achata as frequências, o que lhe valeu o apelido *le chiffre indéchiffrable* por três séculos.
- **Caso de uso :** usada pelos Confederados na Guerra Civil Americana. Cai com Kasiski ou Friedman para achar $m$, depois $m$ Césares isoladas.

---

## W

### WEP
- **Área :** FLX
- **Conceito :** proteção original do Wi-Fi : RC4 com um **IV de 24 bits** concatenado à chave. Com só $2^{24} \approx 16{,}7$ milhões de IVs, eles se repetem em poucas horas, e dois pacotes com o mesmo IV repetem o fluxo RC4.
- **Caso de uso :** a reencarnação do VENONA em software (Simulado Q2c). Ferramentas como o `aircrack-ng` recuperavam a chave em minutos, e o WEP foi substituído por WPA e WPA2.

---

## X

### XOR
- **Área :** FLX / FUN
- **Conceito :** OU exclusivo bit a bit ; é a sua própria inversa ($x \oplus x = 0$, $x \oplus 0 = x$). Os bits 1 do resultado marcam onde as entradas diferem.
- **Caso de uso :** faz cifrar e decifrar serem a mesma operação no OTP e nas cifras de fluxo, e pela mesma propriedade faz a chave se cancelar quando é reutilizada. Aparece também no CBC, no Davies–Meyer e no HMAC (`ipad`/`opad`).

---
### Ver também
- [adicoes.md](./adicoes.md) — o aprofundamento de onde sai a maior parte dos verbetes.
- [SIMULADO](../provas/p1/SIMULADO.md) — as questões citadas nos casos de uso (Q1–Q18, Dissertativas 1–5, Parte IV).
- [aula13](../aula13.md) — a estrutura da prova e os quatro blocos dissertativos.
