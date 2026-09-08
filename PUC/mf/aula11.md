# Métodos Formais
## [08-09][mvfm]
---

### Thou Shall Curry Your Functions
- Júlio tá mostrando agora o setup & utilidades do **Provador de Teoremas** Isabelle.
- Em arquivos que vamos usar, vamos estar descrevendo **Teorias**, um arquivo .thy
    - Segue mesma norma do Java, onde o nome da classe principal é o nome do arquivo em si.
        ```code
        theory exemplos
        imports main
        begin
        [...]
        where 
            [...]
            [...]
        done
        ```
- datatype bool = True | Flase
-   - Várias funções nativas já incorporadas, funções lógicas.
-   - Júlio descreveu como **Simpleszinho** ao invés de bobinho. Talvez evoluindo seu vasto vocabulário.
- Interpretado o Isabelle.
 ```code
    value "True ^ False"
   ```
- retorna ::"bool"

### datatype nat
- Definido simplesmente como 'nat = 0 | Suc nat'
    - Definido com o sucessor de si mesmo.
    - Todo natural é sucessor de algum outro natural acimda de 0.
- Função para retornar o quadrado de determinado número natural :
    ```code
    theory exemplo
        imports main
    begin

    definition quadrado::"nat->nat" where
    "quadrado n = n*n"
    ```
- Uma função não-recursiva, por mais que o Isabelle permita a implementação de funções recursivas. Foi só '*um exemplo bobinho*'.
- Vamos escrever uma função recursiva de soma de números naturais, seguindo certas determinações que o Júlio colocou - que em si utiliza uma estrutura única do Isabelle.
    ```code
    primrec somar::"nat -> nat ->" where
    somar1:"soma x 0 = x" |
    somar2:"somar x (Suc y) = Suc (somar x y)"

    ```
- Outra função escrita é a definição recursiva de números pares.
    ```code
    fun par::"nat -> bool" where
    "part 0 = True" |
    "par (Suc 0) = False" |
    "par (Suc (Suc n)) = par n"
    ```
