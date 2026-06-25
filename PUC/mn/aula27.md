# Métodos Numéricos
## [23-06-2026][mvfm]
---
### Intervalo
- Inventado por volta da década de **80**, com uma matemática que só foi inventanda em **1966**.
	- '*Essa matemática incrivelmente avançada é simples.*'
- Em '66, um americano inventou um tipo de número inteiramente novo.
	- Não muito conhecido, mas existe.
	- **O Intervalo.**
- '*Quero falar de um número, mas não tenho todas as informações dele. Mas tenho certeza que ele está por aqui.*'
	- Num exemplo bem exagerado : '*A temperatura dessa sala de aula está entre [16, 19] graus celsius.*'
	- '*O importante do intervalo é que ele não está fora dele mesmo. Tá dentro desse intervalo e não sai.*'
- E definindo esse novo tipo de número, o criador teve que também escrever como se opera neles.
- Por mais que tenhamos um começo e fim bem determinado, existem números infinitos dentro desse espaço. Estamos falando de **todos**.
	- '*O cosseno desse limite não vai retornar um valor. Vai retornar um intervalo também.*'

### Um Método, Tosco, Simples & Quase Perfeito.
- '*Todas as contas em intervalo garantem apenas que : O intervalo não está fora disso aqui.*'
- POr lidar com intervalos, não temos garantia que TODO o intervalo está dentro daquela função.
	- Trabalhando com intervalos leva a um certo grau de incerteza. Mas já é bem rápido.
- Pela explicação do JB, o algoritmo é simplesmente calcular funções do jeito que estávamos fazendo antes, só que agora com intervalos ao invés de um valor pronto fixo.
- Com esse método, não caímos naquele problema de cair no mínimo local ao invés do mínimo global.
- **Branch & Bound**. Vamos fazer **Branch & Bound**.
- Sor pegou uma função, pegou o seu intervalo e depois foi continuamente dividindo o intervalo em intervalos menorzinhos e menorzinhos.
	- A otimização já foi feita, mas ainda não conseguimos ver.
	- O que foi feito?
- Procurando pelo mínimo global, poderíamos desconsiderar os intervalos mais altos.
	- '*Pq lá todo mundo tá mais baixo.*'
	- Bem o que o Wide falou.
- **-0.379485**
