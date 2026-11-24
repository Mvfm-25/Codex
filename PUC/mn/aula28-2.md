# Métodos Numéricos
## [17-11][mvfm]
---
### Sabemos como fazer diferenciação automática regressiva
- Sor faz uma recapitulação de como fizemos a diferenciação automática progressiva & regressiva. São cálculos bem legais e divertidos.
    - Mas temos que lembrar a fazer derivadas.
- Temos materiais tanto desse semestre, quanto do anterior
- No exemplo seguinte :
![Regressivo](assets/regressivo_1.png)
    - Faríamos : $\frac{df}{df_5} = \frac{df}{df_6} * \frac{df_6}{df_5}$
    - Ou seja, regra da cadeia.
- Como já sabemos quem é $\frac{df}{df_6} = 1$, só precisamos saber quem é $\frac{d(f_5/f_2)}{df_5}$
    - Conseguimos re-escrever $\frac{f_5}{f_2}$ como : $f_5 * \frac{1}{f_2}$.
    - Logo, temos $\frac{1}{f_2}$ = $\frac{1}{2}$. Pois $f_2 = y = 2$
- Então $f_5$ está recebendo $\frac{1}{2}$ de $f_6$
