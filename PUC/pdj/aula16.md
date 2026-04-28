# Projeto Desenvolvimento de Jogos 
## [27-04-20260[mvfm]
---
### Destruindo Nodos
- Cohen determina que : assim como criamos, devemos destruír também.
- Exemplo dado para racicínio por trás de destruir nodos, Cohen menciona **decals** de tiros & projéteis.
	- Okay, pode ser.
	- Sprays do tf2 que ainda respeitam o limite de decals como esses também vale. Mas ninguém na real se importa. FUCK you.
- Em **Godot**, existem duas principais maneiras de deletar nodos :
	- **nodo.free()**
		- Libera imediatamente a memória ocupada.
	- **nodo.queue.free()**
		- Libera a memória ocupada quando não estiver mais em uso, espera em fila para liberação.
- Cada nodo herda os mesmos métodos, o uso de ambos pode ser aplicado para qualquer cenário desejado.
- Cohen mostra um exemplo prático do uso da função **VisibleOnScreenNotifier2d** para liberar caixinhas assim que elas deixam de ser visíveis pela viewport.

### Troca de Cenas
- "*Uma coisinha mais sofisticada.*"
- No básico básico mesmo, telas de início, opções, game over etc. Porém, essa troca pode ser usada também para transição de fases.
	- Mas não de maneira muito limpa. Muita gambiarra nesse caso.

