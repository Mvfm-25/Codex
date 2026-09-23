# Métodos Numéricos
## [22-09][mvfm]
---
### Continuação das criaturas felpudinhas
- Chegamos a uma solução parecida, um sistema linear que tem vários 0's e -1's na diagonal principal.
- São simplesmente a representação das **chance** de um nodo chegar em outro nodo.
    - As chances sendo calculadas por somas ao invés de multiplicações, eu assumo.
    - Pelo menos foi assim que eu segui.

### A Aula de Hoje
- "*Método para resolver o sistema das criaturas felpudinhas escolhendo o ponto de início simplesmente alterando o vetor alimentado para a matriz de chances.*"
- $A * x = b$
    - trasforma a matriz única $A$ e as transforme em $A = L*U$
    - Como fazer isso?
- A matriz $L$ é diagonal inferior. Para cima, tudo é 0.
    - Não impede a existência de 0's em baixo.
- A matriz $U$ é diagonal superior.
- "*Sempre vai existir uma LU? Sempre vou conseguir encontrá-las?*"
    - Supondo que sim :
    ```code
        Ax  = b
        LUx = b
            Ux  = y -> Matriz * Vetor = Vetor. Sempre.
        Ly = b -> Com essa conta, especificamente a parte de L, você encontra 'y'. Com o 'y', voltamos o resultado para trás e conseguimos a matriz U.
    ```
- Forward substitution para L & Backward substitution par U.
    - Mas será que custa muito?
