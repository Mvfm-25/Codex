# Segurança de Sistemas
## [26-10][mvfm]
---
### Curvas Elípticas
- Continuando com criptografia assimétrica.
- Problema introduzído por esquemas assimétricos como **RSA**:
    - "*Exigem exponenciações inteiros com parametros de mais 1000bits*"
    - Ou seja, utiliza muita memória.
- Precisamos então sistemas equivalentes que não exigem tanto de seu ambiente. A criptografia da curva elíptica resolve isso.
    - "*Usa um grupo de pontos (em vez de números inteiros) para esquemas criptográficos*"
    - Tamanhos de coeficientes de 160-256bits. EXPONENCIALMENTE menor.

### Computação em Curvas Elípticas
- "*Curvas elípticas são polinômios que definem pontos com base na equação de Weierstraß*"
    - nem FUDENDO que vou conseguir pronunciar direito isso até o fim do semestre.
    - Segue o polinômio : $Y^2 = X^3 + aX + b$
    - ![Exemplo de curva](assets/exemplo_eliptica.png)
- Curvas elípticas podem ser sobre qualquer tipo de campo infinito.
- "*Não é qualquer curva que você pode utilizar.*"
    - ![Especificação de curvas elípticas](assets/esp_elipticas.png)
- Considerações para conversão de curvas em grupo de pontos : 
    - "*Num grupo qualquer, é necessário um elemento para operação identidade.*"
    - "*Este ponto identidade é incluído na definição do grupo.*"
    - "*Este ponto identidade é denomanidado 𝜃*"
- Esse tipo de curva é simétrica sobre o eixo X.
- Para cada ponto $T(x,y)$, seu ponto inverso é definido por $-T(x,-y)$𝜃
