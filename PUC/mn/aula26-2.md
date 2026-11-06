# Métodos Numéricos
## [05-11][mvfm]
---
### Otimização
- "*A otimização que vamos falar nessa disciplina não é a otimização que se fala no prédio 32.*"
    - Otimização 32 é simplesmente deixar um algoritmo já escrito melhor. Seja em memória, armazenamento ou velocidade.
    - Vamos ver otmização **matemática** : achar o maior/menor valor de alguma coisa.
    - Depende da situação.
- Vamos começar a falar de pessoas sendo jogadas de montanhas. Ou, otimização para o lado do menor que existe.
- Ele já traz o problema de ótimo local & ótimo global.
    - Existem métodos burros o suficiente que se quebram em mínimos locais.
- No olhometro não conta, GNUPlot é '*Uma baita ferramenta*.'
- O que podemos fazer aqui? Só tendo a fórmula.
    - Só chutando X, escolhendo o melhor (menor nesse caso) e depois testa x's por perto. Por intervalos essencialmente.
- O outro método é jogar uma bolinha de gude. Literalmente o que ele falou.
- Ela vai cair em **algum** mínimo. Não se garante se local ou global.
- A função que ele tá mostrando agora tem apenas uma única variavel, um gráfico (x,y). Com duas variaveis temos um gráfico (x, y, z).
- Uma coisa com 3 variáveis, tem um gráfico 3D, mas o resultado leva a outra dimensão acima. Um coisa 4d.

### O Método que Vamos Ver...
- "*Só existe Gauss, masculino com G.*"
- Gradiente Descendente.
    - "*Trabalhoso, mas é mais ou menos simples.*"
    - Feito para resolver o problema na variante sem graça. Um mínimo ***qualquer***
- Mas : **Funciona pra uma caralhada de quantidade de variaveis**.
- O que é um gradiente?
    - "*Uma direção? Quase.*"
- Tendo uma função qualquer $f(x, y, z)$, realmente não importa
    - O que seria o gradiente dela? Gradiente é um vetor.
    - Gradiente se escreve : $\nabla$$f(x, y, z) =  [ -, -, - ]$. É um vetor 3D, então é feito, composto, por 3 partes. O que são os componentes? A derivada da função com relação à x, y & z de acordo.
- $\nabla$$f(x, y, z) = \frac{df}{dx}, \frac{df}{dy}, \frac{df}{dz}$
- Ficou MUITO feia a derivada da função.
- "*Derivar é chato, mas não é complicado.*"
- Por ser um vetor, o gradiente te informa uma direção correta.
    - Mas o que ele tá me falando mesmo? 
- Derivada é só o movimento previsto, andando para cima. Gradiente te conta isso nos dois mundos. $(x,y)$ & $(x,y,z)$
- Em um exemplo, vimos que $x$ tem um aumento bem grande & $y$ tem um aumento **AINDA MAIOR**.
    - O vetor do gradiente são essas duas informações **juntas**. Ele aponta para uma direção positiva, positiva no exemplo de $(x = 2, y = 7)$
    - Isso significa somar os dois vetores? **NÃO**. É uma combinação dos dois, mas não soma como era soma em álgebra linear.

### Aviso Dado
- O que o gradiente está tentando nos avisar? Ele mostra a direção que você deve ir em que você mais sobre rapidamente. Então tu só fala '*não não.*'. Matematicamente, tu ignora o gradiente.
![Exemplo de Gradiente](assets/gradiente_exemplo.png)
- Essencialmente, imitando o esquema da bolinha de gude especificado anteriormente
- Revisar BASTANTE esses conceitos em casa pq são bem dificeis de visualizar. Mesma coisa que me ferrou semestre passado.
- Overshooting : eu fui, mas me passei. Só a direção pode me deixar '*zanzando*', como uma bolinha de gude que fica descendo e subindo num vale.
- O gradiente não te diz exatamente quantos passinhos, então tu normalmente escolhe uma quantidade arbitrária de passos.
    - Uma quantidade $\gamma$ de passos.
    - Passinhos em fórmula : $V_0 = \vec{v} = \begin{bmatrix} X \\\ Y \\\ Z \end{bmatrix}$
    - Então : $V_1 = V_0 - \gamma$$\nabla$$f(V_0)$
- Genericamente : $V_{i+1} = V_i - \gamma$$\nabla$$f(V_i)$
    - Paramos quando a derivada ficar perto de 0. A bolinha de gude desiste.
- Se já temos isso... O que podem ser as futuras 2 aulas? Como melhoramos?
    - Pessoal da física já usa esse método do gradiente faz anos. É o que eles usam.
- O que são os problemas dessa função?
    - Derivadas tendem a ficarem mais compridas e complicadas & extremamente repetitivas.
- Diferenciação Automática.
    - O que te lembrar Diferenciar? Derivar.
    - Derivação automática. Vamos ver um método que precisa apenas da função para o gradiente funcionar. Não derivas.
- Bem mágico. Mas ainda melhora!
- Temos dois tipos de D.A. e o D.A. que vamos ver aula que vem (D.A. progressiva) é a mais fácil que vamos ver.
    - A regressiva é mais complicadinha, de acordo com o JB.
- Progressiva é bem tranquila, mas é chatinha. A regressiva é mais difícil de entender, e por ser mais dificil elea compensa em ser muito mais rápida que a outra.
