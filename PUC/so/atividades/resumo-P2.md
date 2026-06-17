# Resumo P2 — Sistemas Operacionais
## E/S + Gerência de Memória e Sistema de Arquivos
### [17-06-2026][Claude] · Fontes: `IO.pdf` e `exRevP2.pdf` · Ref.: Silberschatz, *Operating System Concepts* (9ª ed.)

---

# PARTE I — Sistemas de Entrada e Saída (E/S)

> **Ideia central:** o SO abstrai a enorme diversidade de hardware, permitindo que o software controle os periféricos de forma **segura, padronizada e eficiente**.

## 1. Hardware de E/S
- **Porta:** ponto físico/lógico de conexão do dispositivo.
- **Barramento (bus):** fios + protocolo que transportam as mensagens.
- **Controlador (adaptador):** circuito que opera e traduz os sinais da porta/barramento.
- **Hierarquia de barramentos:** CPU/RAM no topo (alta velocidade) → barramentos de expansão **PCI/PCIe** → periféricos lentos. **SCSI** para discos de alto desempenho.
- **4 registradores de porta:** `data-in` (entrada), `data-out` (saída), `status` (estado: ocupado/pronto/erro), `control` (comandos).

## 2. Como a CPU sabe que a E/S terminou
- **Polling (consulta ativa):** CPU lê o *busy bit* em loop. Simples, mas desperdiça ciclos em **busy-wait**. Aceitável só p/ dispositivos muito rápidos.
- **Interrupções (interrupt-driven):** o dispositivo **notifica** a CPU ao concluir → CPU faz *state save* e salta para o **interrupt handler**. Libera a CPU para outras tarefas.
- **Recursos avançados:** **vetor de interrupção** (tabela de ponteiros p/ a rotina certa), **mascaramento** (adiar interrupções não críticas), **níveis de prioridade**.
- **Vetores Intel (0–255):** 0–31 = exceções internas da CPU (divisão por zero, **page fault**); 32–255 = interrupções externas de periféricos.
- ⚠️ **Paradoxo (Polling > Interrupção):** em dispositivos *fenomenalmente rápidos* (NVMe, redes), o custo fixo do *context switch* da interrupção pode ser **maior** que a própria operação → a espera ativa dá **maior throughput**.

## 3. DMA — Direct Memory Access
- Evita a **E/S programada** (CPU movendo byte a byte).
- CPU configura o controlador DMA (**origem, destino, contador de bytes**); o DMA assume o barramento e transfere **blocos inteiros** direto p/ a RAM.
- Emite **uma única interrupção** ao final. CPU fica livre durante a transferência.

## 4. Interface de E/S de Aplicação
- O **kernel** encapsula o hardware em **classes genéricas**; o **device driver** esconde os detalhes do fabricante → aplicações **agnósticas**.
- **Camadas:** Aplicação (syscalls) → Subsistema de E/S do kernel → Drivers → Hardware.
- **Tipos de dispositivo:** **bloco** (`read`/`write`/`seek`) vs. **caractere** (`get`/`put`); **rede** (sockets, `select()`/`epoll()`). `ioctl()` = "escape" p/ comandos proprietários (ex.: ejetar mídia).
- **Dimensões de variação:** unidade (char vs. bloco), acesso (sequencial vs. aleatório), tempo (síncrono vs. assíncrono), compartilhável vs. dedicado.
- **Relógios/Timers:** hora atual, tempo decorrido e **timer programável** (interrupções periódicas p/ o escalonador preemptivo / *time-slice*).

## 5. Modelos de E/S (revisar p/ a prova!)
| Modelo | Comportamento |
|---|---|
| **Bloqueante** | Processo é suspenso (sai de prontos → fila de espera). Simples de programar. |
| **Não bloqueante** | Syscall retorna **imediatamente** com os bytes prontos (ou erro). Usa multithreading. |
| **Assíncrona** | Processo continua; a E/S ocorre em 2º plano; **sinal/evento** avisa ao concluir. |

## 6. Subsistema de E/S do Kernel
- **Escalonamento de E/S** (reordena a fila p/ maximizar vazão), **bufferização**, **caching**.
- **Por que bufferizar:** *mismatch* de **velocidade**, *mismatch* de **tamanho**, e **semântica de cópia** (garantir o dado exato do momento da chamada).
- **Spooling (SPOOL):** intercepta saídas em arquivos temporários quando o periférico não aceita fluxos intercalados (ex.: impressora). **Reserva de dispositivo:** acesso exclusivo → cuidado com **deadlock**.
- **Proteção:** instruções de E/S são **privilegiadas** (só via kernel). Erros expostos via `errno`.
- **STREAMS (Unix):** canal **full-duplex** modular = **Stream Head** + **Módulos** intercambiáveis + **Driver End**; comunicação por **mensagens em filas**.
- **Desempenho:** reduzir *context switches* e cópias; dosar interrupções vs. polling; maximizar o **DMA**.

---

# PARTE II — Gerência de Memória e Sistema de Arquivos

## 7. Memória Virtual e Paginação
- **Memória virtual:** programas podem **exceder a RAM física**; páginas ficam em RAM ou no **swap** (disco).
- **Page Fault:** a página referenciada **não está na RAM** → kernel a busca no disco, carrega em quadro livre, atualiza tabela de páginas e reexecuta a instrução. Evento **normal**, não erro.
- **TLB (Translation Lookaside Buffer):** cache de traduções p/ acelerar endereçamento.
  - **Fluxo TLB Miss → Page Fault:** (1) MMU não acha na TLB; (2) consulta tabela em RAM → bit de presença inválido = *page fault*; (3) desvia p/ o **handler** do kernel; (4) carrega página, atualiza tabela e **TLB**; (5) reexecuta a instrução.

## 8. Algoritmos de Substituição de Páginas
| Algoritmo | Característica |
|---|---|
| **OPT (Ótimo)** | Prevê o futuro → ideal, mas **impraticável**. Serve de balizador. |
| **LRU** | Remove a página **há mais tempo sem uso**. Ótimo na prática, mas o **LRU puro** exigiria *timestamp* por acesso → custo proibitivo no silício. |
| **FIFO** | Remove a mais antiga. Sofre da **Anomalia de Belady** (mais quadros → *mais* page faults). |
| **Clock/Second Chance, NRU** | Aproximam o LRU usando os **bits R (referência) e M (modificação)** da MMU — baratos. |

- **Algoritmos de pilha** (LRU, OPT) são **imunes** à Anomalia de Belady.

## 9. Thrashing e Localidade
- **Thrashing:** colapso de desempenho — o SO passa mais tempo fazendo *swap* de páginas do que computando.
- **Princípio da Localidade:** um processo acessa, em cada fatia de tempo, um **subconjunto concentrado** de páginas.
- **Working Set (conjunto residente):** o SO mede e **preserva** as páginas ativas de cada processo → reduz page faults e contém o thrashing.
- **VSWS (Variable-Interval Sampled Working Set):** em vez de janela fixa, opera por **amostragem** — zera o bit de referência no início do intervalo e, ao final, retém só as páginas usadas → **ajuste dinâmico** do tamanho.

## 10. Fragmentação · Paginação vs. Segmentação
- **Fragmentação Interna:** desperdício **dentro** de um bloco/partição de tamanho fixo (ex.: processo de 100 KB em partição de 256 KB → 156 KB ociosos presos). Típica de **partições estáticas** e **paginação**.
- **Fragmentação Externa:** memória livre total existe, mas **dispersa** em fragmentos não contíguos. Típica de **segmentação** e partições dinâmicas.
- **Segmentação:** divide o processo pela **lógica do programador** (código, heap, stack, dados) → tamanhos variáveis → **frag. externa**.
- **Paginação:** blocos de **tamanho fixo** → elimina frag. externa, mas gera **frag. interna** na última página de cada região.

## 11. Sistema de Arquivos
- **Acesso aos dados:**
  - **Sequencial:** percorre do início até o ponto desejado (fitas).
  - **Direto/Aleatório:** salta a qualquer bloco via índice (`seek`), em O(1) — sem ler os anteriores.
- **Estruturas de diretório:** evolução da **árvore pura** → **grafo acíclico** (hard/symbolic links).
  - **Benefício:** compartilhar o mesmo arquivo sob caminhos/nomes diferentes sem duplicar dados.
  - **Risco:** **ponteiros pendentes (dangling pointers)** ao excluir por um dos caminhos.
- **Alocação em disco (Unix/Linux — ext4): inode** com ponteiros **diretos, indiretos simples, duplos e triplos**.
  - **Vantagem sobre lista encadeada:** **acesso direto** a qualquer bloco (sem percorrer a cadeia) + metadados concentrados em estrutura compacta cacheável.

## 12. Concorrência em Arquivos
- **File Locking (contra *race conditions*):**
  - **Consultivo (advisory):** kernel só **registra** as travas; depende da **cooperação** do software — não impede acesso bruto de quem ignora a verificação. (POSIX `flock()`/`fcntl()`).
  - **Mandatório (mandatory):** kernel **intercepta e bloqueia** ativamente acessos conflitantes. *Deprecated* no Linux ≥ kernel 5.15.
- **Sistemas de Arquivos Distribuídos (NFS, CIFS, AFS) — Semânticas de Consistência:**
  - **Semântica UNIX:** escritas são **imediatamente visíveis** a todos que têm o arquivo aberto (consistência estrita).
  - **Semântica de Sessão (AFS):** alterações ficam em **cópia local** e só são propagadas ao servidor no **`close()`** (fim da sessão). Reduz tráfego de rede, mas atrasa a visibilidade.

---

### Palavras-chave para a prova
`polling` · `interrupção / vetor / handler` · `DMA` · `device driver` · `bloqueante/não bloqueante/assíncrono` · `buffering / caching / spooling` · `STREAMS` · `instrução privilegiada` · `página / quadro` · `page fault` · `TLB` · `LRU / FIFO / OPT / Clock / NRU` · `Anomalia de Belady` · `Working Set / VSWS` · `localidade` · `fragmentação interna vs. externa` · `paginação vs. segmentação` · `inode` · `acesso sequencial vs. direto` · `grafo acíclico / dangling pointer` · `advisory vs. mandatory locking` · `semântica UNIX vs. sessão`
