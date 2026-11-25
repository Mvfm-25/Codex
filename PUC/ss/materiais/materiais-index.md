# Segurança de Sistemas — Materiais por Prova
## Conteúdo de cada avaliação segundo o [Cronograma do Semestre](https://sarc.pucrs.br/Default/Export.aspx?id=fccef721-ee0a-4e61-a41c-074eb0fe9837&ano=2026&sem=2)
---
### Avaliação
- **$G1 = (P1 + P2 + MT) / 3$** — P1 cobre as unidades 1, 2 e 3; **P2 cobre todas** (cumulativa); MT pode ter pesos diferentes por trabalho.
- **PS (30/11)** & **G2 (07/12)** — cobrem **todo** o conteúdo abaixo.
- [Mapa de provas](./mapa-provas.md) — cronograma aula a aula & observações das provas-exemplo.
---
### Guias de estudo
- [P1](./P1.md) — **todo** o material até 21/09 (a P2 é cumulativa e a PS/G2 cobram tudo) : fundamentos, cifras clássicas & Vigenère, OTP, DES/AES/modos, MAC & HMAC, padding oracle, hash, pentest & laboratórios (Pickle Rick, Root Me), TSE. P1 2026/2 e P1-exemplo resolvidas, listas de OTP e de hash resolvidas, 8 atividades.
- [P2](./P2.md) — gestão de risco, aritmética modular, troca de chaves, RSA, curvas elípticas, assinatura digital, PQC, blockchain, WhatsApp e T2; questões que se repetem; P2-exemplo e as perguntas do fim dos slides de blockchain respondidas; **todas as listas do professor resolvidas** (modular, Fermat/Euler, Merkle/DH, RSA, assinatura); 10 atividades.
- Cobertura do material entregue (medida com `cobertura.py`) : todos os materiais de conteúdo linkados; 70% dos termos-chave e 48% dos títulos de slide presentes nos guias.
---
### P1 — 21/09 *(já realizada)*
**Fundamentos, cifras clássicas & de fluxo, cifras de bloco, integridade (hash/MAC) & pentest de rede**
- Fundamentos de segurança & criptografia (03/08 – 05/08)
	- [Aula02](../aula02.md) — Fundamentos de segurança, criptografia, cifras & chaves; atividade prática.
	- [Segurança de Sistemas Introdução Criptografia](<../atividades/Segurança de Sistemas Introdução Criptografia.pdf>) · [Atividade : áreas da cibersegurança](../atividades/Segurança_de_sistemas___Pesquisa_sobre_areas_da_seguraça_digital.pdf)
- Cifras clássicas & Enigma (10/08 – 12/08)
	- [Aula03](../aula03.md) — Apresentação do prof. Avelino sobre a **Enigma**. *(sem data no cabeçalho)*
	- [Aula04](../aula04.md) — Contexto histórico & funcionamento de múltiplas cifras clássicas.
	- [CifrasClassicas](<../atividades/CifrasClassicas .pdf>) · [T1 — Vigenère](../atividades/Segurança_de_Sistemas___T1_Venegre.pdf) · [Dom Casmurro (texto do T1)](../atividades/DomCasmurro.txt)
- Cifras de fluxo — One-Time Pad (17/08)
	- [Aula06](../aula06.md) — Introdução à cifra OTP, atividade prática.
	- [4 - CifraDeFluxo-OTP (45min)](<../atividades/4 - CifraDeFluxo-OTP (45min).pdf>) · [Exercicio — Cryptoanalise cifras de fluxo-2](../atividades/Exercicio___Cryptoanalise_cifras_de_fluxo-2.pdf)
- Cifras de bloco — DES, 3DES, AES & modos de operação (19/08)
	- [5 - CifraDeBloco - DES (45min)](<../atividades/5 - CifraDeBloco - DES (45min).pdf>) · [6 - CifraDeBloco - AES (45min)](<../atividades/6 - CifraDeBloco - AES (45min).pdf>) · [7 - Modos de Operação (45min) (Copy)](<../atividades/7 - Modos de Operação (45min) (Copy).pdf>)
- Funções resumo, MAC & *padding oracle* (24/08 – 26/08)
	- [8-FuncoesResumo](../atividades/8-FuncoesResumo.pdf) · [SS — Exercício Hash](../atividades/SS___Exercício_Hash.pdf) · [8 - CodigoAutenticacaoMensagem - MAC (45min)](<../atividades/8 - CodigoAutenticacaoMensagem - MAC (45min).pdf>) · [Aula11 PaddingOracleAttack](../atividades/Aula11_PaddingOracleAttack.pdf)
- Pentest de rede — planejamento, reconhecimento, varredura & laboratórios (31/08 – 09/09)
	- [Introdução ao Pentest de Rede-1](<../atividades/Introdução ao Pentest de Rede-1.pdf>) · [SS — Atividade Ferramentas de pentesting](../atividades/SS___Atividade_Ferramentas_de_pentesting.pdf) · [SS — Pickle Rick](../atividades/SS___Pickle_Rick.pdf) · [SS — Root Me](../atividades/SS___Root_Me.pdf)
- Dúvidas P1 & apresentação do TSE (14/09 – 16/09)
	- [Aula13](../aula13.md) — **Estrutura da prova** anunciada pelo professor.
	- [Aula14](../aula14.md) — Apresentação do **TSE** sobre a urna eletrônica.
- **Dicas do professor** ([Aula13](../aula13.md)) : 4 dissertativas de 2 pts (conceitos de criptografia; OTP; cifras de bloco + *meet-in-the-middle*; pentest conceitual) + objetivas; Hash & MAC são as objetivas "chatinhas".
- Provas : [P1-exemplo](<../provas/p1/SS___P1-exemplo.pdf>) · **[P1 2026/2](<../provas/p1/SS___P1___202602.pdf>)** (a prova real) · Correção na [Aula18](../aula18.md).
- Estudo próprio : [Simulado P1](../provas/p1/SIMULADO.md) · [Resolução](../provas/resolucao-simulado.md) · [Adições IA](../IA/adicoes.md) · [Dicionário](../IA/dicionario.md)
- *Cópias idênticas em `provas/p1/`* : CifrasClassicas, 8-FuncoesResumo, Aula11_PaddingOracleAttack, Exercício Hash e Criptoanálise de cifras de fluxo — mesmos arquivos de `atividades/`.
---
### P2 — 25/11 *(cumulativa : inclui P1)*
**Gestão de risco, aritmética modular, troca de chaves, RSA, curvas elípticas, assinatura digital, PQC, blockchain & WhatsApp**
- Gestão de risco (28/09)
	- [Aula17](../aula17.md) — Gestão de riscos com professor convidado; GRC; Risco = Probabilidade × Impacto.
- Aritmética modular (05/10 – 07/10)
	- [Aula19](../aula19.md) — Notação $Z_n$, MDC, co-primos e inverso modular.
	- [Aula20](../aula20.md) — Teoremas de **Fermat** e **Euler**, equações lineares em $Z_n$, geradores.
	- [9 - AritmeticaModular (60min)](<../atividades/9 - AritmeticaModular (60min).pdf>) · [SS — Exercicios Modular — Parte 1](../atividades/SS___Exercicios_Modular___Parte_1.pdf) · [SS — Exercicios Modular — Parte 2-1](../atividades/SS___Exercicios_Modular___Parte_2-1.pdf)
- Troca de chaves — Merkle & Diffie-Hellman (14/10)
	- [10 - TrocaDeChaves (60min)](<../atividades/10 - TrocaDeChaves (60min).pdf>) · [SS — Exercicio troca de chaves](../atividades/SS___Exercicio_troca_de_chaves.pdf)
	- *Aula de 14/10 sem anotações.*
- Estabelecimento de chaves — RSA (19/10)
	- [11 -CifraAssimétrica - RSA (60min)](<../atividades/11 -CifraAssimétrica - RSA (60min).pdf>) · [SS — RSA-1](../atividades/SS___RSA-1.pdf)
	- *Aula de 19/10 sem anotações.*
- Curvas elípticas (26/10)
	- [Aula22](../aula22.md) — Curvas elípticas : equação de Weierstraß, grupo de pontos, ponto identidade.
	- [Slides — Curvas elípticas](../atividades/Aula15_CurvasElipticas.pdf) · [SS — Exercicios Curva eliptica](../atividades/SS___Exercicios_Curva_eliptica.pdf) · [gabarito curvas elipticas](../atividades/gabarito_curvas_elipticas.pdf)
- Assinatura digital (28/10)
	- [Aula24](../aula24.md) — Por que assinar; vantagens e o custo de aumentar a mensagem.
	- [Aula16 AssinaturaDigital cortado](../atividades/Aula16_AssinaturaDigital_cortado.pdf) · [AssinaturaDigital](../atividades/AssinaturaDigital.pdf) · [AssinaturaDigital Exec1](../atividades/AssinaturaDigital_Exec1.txt) · [AssinaturaDigital Exec2](../atividades/AssinaturaDigital_Exec2.txt) · [Chave pública](<../atividades/Chave Publica.txt>) · [Chave privada](<../atividades/Chave Privada.txt>) · [Resolução própria](../atividades/resolucaoAssinaturaDigital.md)
- Criptografia pós-quântica (04/11)
	- [Palestra-PQC](../atividades/Palestra-PQC.pdf)
	- *Aula de 04/11 sem anotações.*
- Blockchain (09/11)
	- [Aula25](../aula25.md) — Bitcoin × blockchain, estrutura do bloco, Merkle tree, dinâmica do *badHash*.
	- [Blockchain apresentação](<../atividades/Blockchain apresentação.pdf>)
- Protocolo WhatsApp (16/11)
	- [Segurança no WhatsApp 25.2](<../atividades/Segurança no WhatsApp_25.2.pdf>) · [SS — Perguntas protocolo Whatsapp](../atividades/SS___Perguntas_protocolo_Whatsapp.pdf)
	- *Aula de 16/11 sem anotações.*
- Trabalho T2 — apresentações (18/11 – 23/11) : **cai na prova** (1 questão sobre um caso apresentado).
	- [Descrição do T2](<../trabalhos/t2/SS___T2___Descrição.pdf>) · [T2 do grupo — Jeep Cherokee](../trabalhos/t2/jeep-cherokee-attack-2015.md)
- Provas : [P2-exemplo](<../provas/p2/SS___P2-exemplo.pdf>) (outro semestre : forense e engenharia reversa, fora do cronograma 2026/2) · [PS 2026/1](<../provas/ps/SS___PS___202601.pdf>)
---
### PS — 30/11 & G2 — 07/12
- Todo o conteúdo. A [PS 2026/1](<../provas/ps/SS___PS___202601.pdf>) repete questões das P1/P2 anteriores (AES-ECB, Grover) — ver o [mapa](./mapa-provas.md#observações-das-provas-exemplo).
