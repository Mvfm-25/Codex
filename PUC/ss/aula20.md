# Segurança de Sistemas
## [07-10][mvfm]
---
### Um poquinho mais de matéria : Teoremas
- Ainda vendo aritmética modular que vimos [aula passada](./aula19.md)
- ![Resolvendo equações lineares](assets/eq_lineares.png)
- Continuamos com novos teoremas. Primeiramente : **Fermat**.
    - Seja *p* um número primo :
        - $∀ x ∈ (Z_p)^{*} : x^{p - 1} = 1$ em $Z_p$
    - Exemplo :
        - $Z_5 = { 1, 2, 3, 4 }$
        - $1^4$ |
            - $1$ em $Z_5$
        - $2^4$ |
            - $16$ em $Z_5$
            - $1$ em $Z_5$
        - $3^4$ |
            - $81$ em $Z_5$
            - $1$ em $Z_5$
        - $4^4$ |
            - $256$ em $Z_5$
            - $1$ em $Z_5$
- Fermat foi descrito como uma forma alternativa de calcular números inversos, mas que é considerado menos eficiente que Euclides. O algoritmo que foi introduzido aula passada.
- Esse teorema tem sem uso na geração aleatória de números primos. Peguei a imagem direto pra explicar, não conseguiria alterar muito sem ter certeza do que escrevi.
    = ![Aplicação de Fermat](assets/uso_fermat.png)
- **Teorema de Euler**
    - "*Um método terrível...*"
    - ($Z_p$) é um grupo cíclico, ou seja :
        - $∃g∈(Z_p) talque : {g^0, g^1, g^2, g^3, ..., g^{p-2}} = (Z_p)$
    - $g$ é chamado de gerador de $(Z_p)$
    - ![Geradores](assets/geradores.png)
