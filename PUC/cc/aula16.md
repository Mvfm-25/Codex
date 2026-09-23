# Construção de Compiladores
## [23-09][mvfm]
---
### Continuação da Derivação à partir do Ponto
- Agustini está fazendo a correção de um exercício que não fiz, mas não parece muito diferente daquilo desenvolvido / praticado na [Aula14](./aula14.md) 
- O uso do LookAhead está se demonstrado extremamente prático, reduzindo significativamente a ambiguidade de algoritmos sem ele. Estamos vendo **CLR(1)** especificamente
- Mesmo uso de grafos como na aula passada, torna claro o uso do autmato de pilha & da tabela de tradução durante a realização da atividade.
    - Tabela de transições, mas "*Tabela de Tradução*" fica muito mais legal.
    - É bem divertido criar nomes aleatórios & alternativos para coisas já conhecidas. É bem legal usar nomes que ninguém além de mim conhece pra me fuder na prova.
        - :^)

### Quem sabe fazer de cabeça a árvore de derivação?
- Ninguém.
- "*Daqui 3 aulas vai acaber a análise sintpatica, graças a Deus.*"
    - Momentos Júlio nessa cadeira, bem engraçado.
- Material das atividades que o Agustini tá corrigindo agora ainda não estão disponíveis no Moddle.
    - Oops, não vou conseguir copiar o que tá no quadro direito. Uma merda
- O raciocínio padrão é: 
    1. Verificar o que está na pilha
    2. Checar regra de shift ou redução. Caso shift, andar para próximo estado. Caso reduce, retora ps símbolos do lado direito da regra e os substitui pelo lado esquerdo.
    3. Continuar, recursivamente.
- Bem legal, e extremamente intuitivo para minha felicidade.
- Verificando o cronograma agora, Agustini possivelmente se confundiu.
    - Tá marcado para aula que vem : **Processamento dirigido à sintaxe** JÁ.
    - Era o previsto para uma cadeira do Agustini, a troca repentina do cronograma por nenhuma razão aparente
- Agustini reclamando de HashSet & HashTree. Bem engraçado

### Por que estamos vendo isso?
- "*Porque esse algoritmo é útil para coisas extremamente rápidas. Pelo menos, eu pessoalmente acredito nisso.*"
- Recursão está na esquerda & ele é extremamente melhor do que a recursão na direita
    - Justificativa do Agustini é que na redução à esquerda ele consegue começar a reduzir bem mais cedo, onde à redução à direita demoraria muito.
    - Exemplo dele foi a escrita de um método qualquer em java
- Vamos ver Yacc aula que vem. Exercícios provavelmente também. 
