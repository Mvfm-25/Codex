# Métodos Numéricos
## [17/09][mvfm]]
---
### On With The Show
- Primeira aula do JB com a máquina nova semi-temporária. Vai saber quando pedirem de volta.
    - É possível que eu só exploda a Globante se me pedriem pela máquina.
- "*Tu não tá preparado para o que vai acontecer hoje*" ele conta pra um dos dois na fileira principal.
    - Favoritismo não é muito bem escondido nas aulas do JB.
- Pequena revisão para o métodod de **Gauss-Jacobi feita aula passada**, da qual eu não estava lá.

### What The Other Guy Said
- JB tá procurando por um sistema da aula passada que ele acabou não salvando.
    - Segue o sistema :
    ```code
        4x + y - z = 6
        3x - 4y +2z = 8
        x + 2y + 2z = 3 
    ```
- Qual a ideia pra  Gauss-Jacobi?
    1. Isola uma variável em cada uma. Nesse caso, isolando o $x$ no sistema acima.
    ```code
        x = 6 - y + 2 / 4
        y = 8 - 3x - 2z / -4
        z = 3 - x - 2y / 2
    ```
    2. Agora tu '*chuta*' a solução para cada uma. Chute dado pela turma :
    ```code 
        7
        5
        8
    ```
    3. Ajustando na fórmula do sistema.
    ```code
        x = 6 - 5 + 8 / 4 = 2.25
        y = 8 - 21 - 16 / -4 = 7.25
        z = 3 - 7 - 10 / 2 = -7
    ```
- Rodando em um programa escrito pelo JB, Gauss encontrou uma solução para o sistema proposto após *após* 226 passos.
    - "*Não existe um macete para começar com um chute melhor.*"
- Chutes consecutivos, indo para uma direção boa dependendo dos resultados, até encontrar a resposta.
    - Ou vai para um lugar e fica quieto, onde deve ser a solução... Ou vai para o infinito.
- O que garante que converge? A matriz ser a diagonalmente dominante.

### Gauss-Seidel
- "*Altamente complexo*"
- Mesmos primeiros 3 passos que **Gauss-Jacobi**. PORÉM.
    - Calcula o x com o primeiro chute, mas usa o resultado dessa conta como o x no chute do y. Pois estamos assumindo que ele vai ser melhorzinho
- "*A medida que tu aprende uma ideia melhor, use ela o mais cedo possível.*"
- Assumia-se que Seidel iria se dar melhor que Jacobi, rodando no mesmo programa com essas informações novas esperava-se um tempo menor para alcançar a resposta.
    - Infelizmente, o contrário ocorreu.
- A visão de um cara da matemática de Seidel é majoritariamente positiva. Mas para o cara da computação nem tanto.
    - O cara da computação tu pode rodar em paralelo, mas Seidel IMPEDE tal implementação. Possivelmnte piorando o tempo de execução do programa.
- JB menciona o método da Agatha, do qual eu mal lembro.

### Agathas'
- Matriz 1000x1000.
- "*Uma misttura de ambos métodos passados.*"
    - Pega 100 variáveis (100 linhas ) e as encontra em paralelo.
    - Nas próximas 100 linhas, utiliza essas 100 novas informações.
- Não necessariamente 100, o tamanho desse bloco fica a teu critério.
- "*Malandro.*"

### O que vamos fazer agora?
- "*Vamos brincar.*"
- Problema das criatiuras felpudas do semestre passado
![Criaturas](assets/felpudas.jpg)
![Felpudas](assets/felpudas1.jpg)
