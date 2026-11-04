# Construção de Compiladores
## [04-11][mvfm]
---
### Continuando
- Agustini mostrando as críticas da graduação presencial, muitas se não TODAS mencionando pelo menos uma vez o uso de LLM's. 
- Ele mencionou de novo a palestra da Dell no qual maior parte dos dev's nem programa mais.
    - Reunião início de dezembro num sábado pra discutir como LIDAR com as LLM's
- Reclamaram, comentaram? Que o Agustini tá falando demais & muito rápido.

### Geração de Código
- Estamos na parte final do compilador, pulamos o Código intermediário & a Otimização.
- Vamos gerar código assembler real, processador intel com Linux.
- "*Gerar um programa equivalente ao programa fonte em linguagem de máquina de acordo com a arquitetura onde ele será executado.*"
    - Entra com árvore + tabela de símbolos
    - Sai com código objeto (montagem da máquina de pilha)
- Para conseguirmos o que queremos, primeiro temos nos certificar de :
    1. Reservar espaço para variaveis e regristros de ativação
    2. Selecionar instruções para cada construçaõ da linguagem
    3. Alocar registradores... O problema mais dificil em máquinas reais 
    4. Ordenar a avaliação das expressões.
- "*Sem estrutura interna, não conseguimos fazer essa etapa de alocar registradores.*"
    - Máquina de pilha não tem registradores.
- POr que uma representação intermediária?
    - Facilita o transporte entre máquinas
    - Permite otimizadores independentes da máquina
    - Separa responsabilidades
    - Didática : não exige o estudo de uma arquitetura específica.
- Mostra um gráfico de códigos de linguagens diferntes (Java, C, PAscal) passa por RI & saí para ramos de x86-64, ARM & RISC-V.
    - Agustini mencionou Esperanto. "*Ouço desde os 5-6 anos de idade, mas ninguém fala.*" Suposta crítica da RI pois não vamos chegar a construír isso esse semestre

### Modelos de RI
- Tem distinção entre níveis de abstração
    - Alto nível : t1 = a[i, j+2].
    - Médio nível : t1 = j + 2; t2 = i * 2-; t3 = t1 + t2; t4 = 4 * t3;
    - Baixo nível : r1 = [fp - 4]; r2 = [r1 + 2]; r3 = [fp - 8]; r4 = r3 * 20;
- Cada vez mais próximas às instruções da máquina.
- Temos formas comuns de representação intermediária :
    - Árvore sintática abstrata
        - Percorrida pelo gerador
    - Código de 3 Endereços
        - Temporários explícitos
    - Máquina de Pilha
        - Temporários implícitos
    - Bytecode JVM
        - Que também é uma pilha
- PUC nos anos 90 comprou um IBM 3090, Mainframe. Processador vetorial, refrigerada à água.
    - "*Ninguém reclamou que eu divago, vou divagar.*"
- No final, vamos acabar usando uma máquina de pilha.
```code
Máquina de Pilha Agustini

LDA _a
LDA _b
LDA _C
MUL
ADD
STA _x
```
- Se não tivessemos isso, não teriamos Java ou C#.

### Quantos endereços por instrução?
- Acumulador : 1 endreço
- Registrador : 2 ou 3 endreço
- Pilha : **0 endreços**
    - OPerandos implicitos no topo da pilha.

### Por que uma máquina de pilha?
- Código pós-fixo = pós-ordem
    - Cada ação emite seu código quando a produção é reduzida.
- Composicional 
    - O código $E_1 + E_2$ é código($E_1$) * código($E_2$)  * ADD, sem saber contexto
- Sem alocação de registradores e sem temporários sem nome.
- Uma passagem
    - Não é preciso construir a arvore, a pilha do analisador faz o papel dela.
- Fácil de executar
    - Um simulador cabe em uma página Java.
- Representação de dados é rapidamente desconsiderada, "*Hoje em dia é tudo unicode.*""
- Quais são os tipos de endereçamento em Java?
    - É tudo relativo, tá tudo na heap.
- Registro de ativação cai na prova, mas... "*Ainda nem pensei na prova.*". Prova é dia 21.
    - Quadro, Stack frame. Um registro por chamada ativa, empilhado na pilha de execução.
    - Pilha != Heap

### Modelo da Máquina de Pilha
- Três memorias, tres registradores & nenhum registrador de dados.
```code
JMP _start
MOP
LDC 3
LDC 4
LDC 5
MUL
ETA _a
HALT

Dados Globais
_a =        23     #500
_v =        0      #504
            0      #508
                    -
_v+16 =     0

Conjunto de Instruções
DS N    - Reserva N bytes a partir do endereço atual
DC N    - Armazena a constante N e reserva posição
LDC N   - Empilha a constante N
LDA N   - Empilha o conteúdo do endereço N
STA N   - Desempilha & armazena no endereço N.
```
- "*Toda operação é feita na pilha pois não temos registradores.*"
- Numa comparação, desempilhamos 2 de pilha e empilhamos o resultado.
- Imagem do quadro tava bem ruim, é bem provável que eu tenha errado maioria dos comandos escritos
    - O que eu tenho real certeza é a primeira linha e as últimas três.
