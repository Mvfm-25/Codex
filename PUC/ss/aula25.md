# Segurança de Sistemas
## [09-11][[mvfm]
---
### Blockchain
- Penúltima aula de conteúdo.
- Modo histórinha
    - Cypherpunk queria ter uma moeda separada para não depender do Governo.
    - Bitgold sendo enviado por e-mail. Mas era bem limitado.
    - Em 2008, o Bitcoin foi proposto por um paper com a ideia de implementação.
        - A peer-to-peer electronic
    - Jeffrey Epstein como Satoshi Nakamoto, seguiu no desnvolvimento ate dezembro de 2010. Sua carteira guardada por uma criptografia assimetrica, fraca á computações quanticas.
- Não vamos ter uma aula do Fillipo, então vamos ver outras coisas além do Bitcoin.

### Bitcoin x Blockchain
- Bitcoin funciona ***por meio*** de uma Blockchain.
- Blockchain possuí outras aplicações além da criptomoeda, mas maior parte dos exemplos envolvem transações monetárias.
- O que uma blockchain precisa?
    - Criptografia Assimétrica
    - Lista Encadeada
    - Função Hash
    - Assinatura Digital
    - Rede P2P
    - ![Merkle Tree](assets/merkle_tree.png)
- O conceito geral se baseia em todas essas tecnologias mencionadas, sempre procurando a decentrelização & garantia da privacidade de seus usuários :
    - "*Um sistema de armazenamento de dados distribuído em vários nodos e que pode ser expandido, mas que possui a característica de que estes nodos não necessariamente confiam uns nos outros.*"

### Problemas Resolvidos
- Redes centralizadas possuem um único ponto de falha. Cai o servidor centralizado &
- Redes de-centralizadas melhoram um pouco, mas pontos de falhas locais ainda podem levar $n$ nodos junto na queda.
- Redes distribuídas melhoram ainda mais, os pontos de falha locais afetam apenas à si mesmos.

### A Rede
- Um nodo possuí uma cópa da Blockchain. Podendo enviar pela rede P2P solicitações de transações para adicionar nas redes.
- O nodo minerador também possuí a cópia da blockchain. Ele faz a criação de novos blocos com as transações enviadas por outros nodos, garantindo integridade de novos blocos gerados por outros mineiros.
    - Recebem premiações monetárias pelos serviços prestados na rede.

### O Bloco
- Separado em :
    - Header
        - Meta informações sobre o bloco.
        ```code
            Block version
            Parent block Hash
            Merkle tree root
            Timestamp
            nBits
                A dificuldade de um quebra-cabeça computacional que os mineradores completam para criar um novo bloco.
            Nonce
                Resposta do quebra-cabeça, número único
        ```
    - Data
        - Informações sobre as transações
        ```code
            Transação #1
            Transação #2
            .
            .
            .
            Transação #n
        ```
- "*Funciona como um livro-razão de contabilidade.*"
- Logo os dados armazenados são transações entre os usuários.
    - Cada usuário é identificado por uma chave pública.
- ![Transação Bitcoin](assets/transacao_bitcoin.png)

### Dinamica : Bitcoin
- "*Vamos fazer uma block aqui & vcs vão ser meus nodos.*"
    - Recompensa é docinho.
- Função BadHash
   - badHash{sequencia de Bytes} -> Hash com 1 byte.
1. Coloca os bytes da sequencia em pilha colocando os menos significativos primeiro.
2. Retira o primeiro byte e faz XOR com o valor binário ($01010101$) guarda o valor.
3. Retira da pilha o próximo byte e faz o XOR com o valor guardado
4. Caso a pilha esteja vazia, retorna o valor guardado. Caso contrário repete o passo 3.
- ![Resultado badHash](assets/resultado_badHash.png)
- ![Candycoin bloco](assets/candycoin_bloco.png)
- Mineradores que conseguirem blocos vão ganhar 0.5 na prova & bombom.
- Resultado supostamente encontrado :
```code
1101 1110

0100 0000 -> Criado a partir do merkle_tree de : 1101 0000 & 1001 0000

0000 0011

1100 0000
```
