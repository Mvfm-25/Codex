# Segurança de Sistemas
##[05-10][mvfm]
---
### Artimética Modular
- Vamos começar a ver criptografia assimétrica, onde a chave que foi usada para codificar a mensagem não vai ser a mesma para decodificar a mesma.
- Lidando com "*Teoria dos números*" de acordo com o Henry.
    - Protocolos de troca de chaves
    - Assinaturas digitais
    - Criptografia assimétrica
- [Fonte listada pelos slides](http://shoup.net/ntb/ntb-v2.pdf)

### Notação
- **N** representa um número positivo inteiro
- **p** representa um número primo
    - Sor também comenta que vamos ver **números compostos**, que são **compostos** (heh?) por outros primos.
    - $4 = 2, 2$ | $6 = 3, 2$ | $8 = 2, 2, 2$ 
        - Só tem um jeito de compor o composto dessa particular maneira. É um problema NP, é um problema bem custoso.
- Notação : $Z_n = {0, 1, 2, ...,}$

### Aritmética Modular, especificamente...
- Exemplos :    Seja N = 12
                9   +   8   =   5   em $Z_{12}$
                5   *   7   =   11
                5   -   7   =   10
- Não é exatamente esse exemplo que o Henry passa na aula, ele passa o exemplo do relógio analógico. Ainda assim, segue o mesmo princípio de representação em faixas
- Divisão não foi incluída no exemplo pois é "*Bem mais complicada*"
- Re-passada uma explicação de **Maior divisor comum**.
    - ![MDC](assets/mdc.png)
- Co-Primos : Dois números em que o MDC entre eles é $1$

### Inverso Modular
- Nos números racionais, o inverso de $2$ é $1/2$.
    - Como se calcula isso genericamente?
- O inverso de x em $Z_n$ é um elemento y em $Z_n$ tal que x * y = 1 em $Z_n$.
    - $-y$ é representado por : $X^{-1}$
- ![Seja N um inteiro ímpar.](assets/inverso.png)
