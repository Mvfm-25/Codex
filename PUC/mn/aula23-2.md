# Métodos Numéricos
## [29-10][mvfm]]
---
### Interpolação
- "*Para entender interpolação é bom entender junto duas outras palavras : Extrapolação & Aproximação((ajuste).*"
    - Alguma ideia do que significa essas palavras?
- Observatório da PUC aparentemente fica no prédio 8. Legal, não sabia isso.
- JB tá usando o exemplo de posições de corpos celestiais de novo.
    - Tendo uma coletania de pontos que correspondem ao angulo do corpo celestial de acordo com uma certa posição, mas com alguns gaps. Dados no dia 1, 3 & 18, bastante coisa faltando.
    - EU gostaria de saber os dados dos dias que perdi, e uma estimativa do futuro.
- Interpolação : Tentar achar uma função que passas nesses pontos definidos anteriormente. Passar EXATAMENTEi
    - *Ato de inserir, colocar entre ou calcular valores intermediários a partir de dados ou pontos já conhecidos.*
- Extrapolção : É algo que não queremos fazer. Usar a função que construimos antes para coisas **PRA FORA** do que conhecemos. No futuro, ou no passado anterior ao início de nossos dados.
    - *Ato de estimar ou prever um valor, comportamento ou fato além dos limites de um conjunto de dados ou informações conhecidas.*
- Aproximação : "**Coisa mais frouxa**." Achar uma função que passe **próximo** aos pontos que já temos.
    - *Não nos interessa nessa cadeira, mas vimos isso já na Computação Gráfica.*

### Dois Métodos de Interpolção
- **Interpolação de Newton** & **Interpolação de LaGrange**.
- Nossa primeira decisão é : **Que tipo de função que eu quero?** 
    - Vamos começar com polinômios. Eles são mais *fofinhos* de trabalhar com.
- Vamos estar procurando pelo melhor $p(x)$ que vamos conseguir encontrar.
- Se vamos encontrar **O MELHOR** polinômio, de que adianta ter dois métodos? Eles vão achar a mesma coisa no final. O preferido do JB é o de Newton, e ele não sabe a razão do porque pessoas usam LaGrange.

### Exemplinho
- Temos o ponto $(1,3)$. E só!
- Baseando-se unicamente nisso, o que seria o melhor polinômio que passa nesses pontos?
    - Tendo só isso, não tenho mais nada pra mudar de opinião. Vou continuar acreditando que $P(x) = 3$, pra sempre.
- Conseguimos um novo ponto : $(2,5)$. Com isso, conseguimos o polinomio : $P(x) = 2x + 1$, uma reta.
    - Mas, como conseguimos isso? No olhometro?
- Anecdote de alfinetes fixando a cada ponto do polinomio para determinar a '*velocidade para subir ou descer dependendo da direção o gráfico.*'. Um pouco difícil de traduzir a retórica da aula para a escrita agora, mas foi essa a ideia que ele trouxe.
    - Essa retórica levou à seguinte fórmula : $p(x) = 3 + \frac{2}{1} (x-1)$
- Aplicando Newton, ele 'mescla' os números.
    - $\frac{DeltaY}{DeltaX} = \frac{5 - 3}{2 - 1} = \frac{2}{1}$
- Mas isso com dois pontos só... E o que acontece quando as coisas ficarem extraordinariamente complicadas?
    - Recebemos o ponto : $(12,15)$
- Parece uma reta? Não. Temos três pontinhos, vamos ter uma função de grau 2. E é sempre assim. 10 pontinhos é um cara de grau 9.
- A melhor parábola, não duas retas.
- Primeiro : Medimos a inclinação da reta entre $(2,5)$ & $(12,15)$
    - $\frac{5-3}{2-1} = 2$
    - $\frac{15 - 15}{12 - 2} = 1$ 
    - $\frac{1 - 2}{12 - 1} = \frac{-1}{11}$, resultado das de cima.
- O que eu faço com isso?
- Com tudo isso, conseguimos a fórmula : $p(x) = 3 + 2(x - 1) - \frac{1}{11} (x - 1)(x - 2)$
    - Essa fórmula bate pra todos os pontos que já temos.
- Temos a seguinte evolução da fórumla, de acordo com os novos pontos que estamos acumulando :
    - $p(x) = 3$, 1 ponto : $(1,3)$
    - $p(x) = 3 + 2(x - 1)$, 2 pontos : $(1,3), (2,5)$
    - $p(x) = 3 + 2(x - 1) - \frac{1}{11} (x - 1)(x - 2)$, 3 pontos : $(1,3), (2,5), (12,15)$
- Não **PODEMOS** depender da ordem. Podemos receber pontos que são **ANTERIORES** à dado ponto.
- Pra exemplificar isso, o JB adicionou o ponto $(5,4)$ e seguiu pelo mesmo processo detalhado antes. Mas to com preguiça de escrever isso tudo de novo. LOL!
    - Mas a nova iteração da fórmula ficou : tudo o que tinhamos antes + $\frac{65}{924}(x - 1)(x - 2)(x - 12)$
