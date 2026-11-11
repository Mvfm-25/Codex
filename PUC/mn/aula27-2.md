# Métodos Numéricos
## [10-11][mvfm]
---
### Continuando
- Quando $x = 3$, $y = 2$ calculue : $f(x, y$. Sendo : $f(x, y) = cos(sin(x) + 5 + xy)$
    - O processo é simples, é só substituir & ver o resultado. Coisa que fazemos desde de sempre.
    - A gradiente é outra coisa. $\nabla$$f = (\frac{df}{dx}, \frac{df}{dy}, \frac{df}{dz})$
- Funções são "*sequências de passos simples.*" Passamos de $f(x, y) = cos(sin(x) + 5 + xy)$
    - $f_i = a$
    - $f_i = x_j$
    - $f_i = f_j ◦ f_k ◦ ∈ {+, -, *, /}$
    - $f_i = g(f_j) g ∈ {sin, cos, exp}$
![Sequência de passos simples*](assets/mn_seq.png)
![Testando com valores 4 & 2](assets/mn_seq_func.png)
- "*Falta um pulinho para gradiente. Um pulinho besta.*"

### Modo Progressivo.
- Quebramos em pedaçinhos de novo a função. E, eu sei a gradiente dos primeiros 3 passinhos.
![Passinhos](assets/passinhos.png)
    - Como?
    - Depende das variações. No passinho 3, 5 não vareia, ele sempre vai ser 5.
    - Mas e o no passinho 1? Qual a derivada de X com relação à X? 1. E com relação a Y? 0.
- $f(x,y) = cos(sin(x) + 5 + x * y)$
    - $f_1 =    x -> (\frac{df_1}{dx}, \frac{df_1}{dy}, \frac{df_1}{dz})$ = (1, 0)$
    - $f_2 =    y -> (\frac{df_2}{dx}, \frac{df_2}{dy}, \frac{df_2}{dz})$ = (0, 1)$
    - $f_3 =    5 -> (\frac{df_3}{dx}, \frac{df_3}{dy}, \frac{df_3}{dz})$ = (0, 0)$
- Pro caso do $f_4$, foi recomendado o uso da regra da cadeia.
    - $f_4 = sin(f_1)$ = $\nabla$$f_4 = cos(f_1) * \nabla$$f_1$ Que no final, é : $f_4 = cos(f_1) * (1, 0) = (cos(x), 0)$
- E assim vai, até terminar todas as continhas pequenas. O último passo sendo o cumulativo de tudo que já fizemos.
![Passo](assets/passo_f5.png)
![Passo](assets/passo_f6.png)
![Passo](assets/passo_f7.png)
![Passo](assets/passo_f8.png)
![Passo](assets/passo_final_mesmo.png)
- "*Agora vai ficar mais simples ainda, por que não é assim que se faz.*"
    - Queremos saber na vida real. Sempre perguntando '*Quando é que vale em lugar tal?*'. Sempre use números, não Strings.
    - "*Quanto vale $f$ em $(3,2)$? E $\nabla$$f(3,2)$?*"
    - E tu sai fazendo as continhas. Usa os números e faz a conta.
- Computacionalmente é caro, mas também estamos pedindo bastante coisa para resolver. Não tem almoço de graça.
    - Quantidade de variáveis influencia diretamente na performance.
    - Resultado final vai ser um vetor btw, caso você tenha se esquecido.
![Arquetipos](assets/arquetipos.png)
