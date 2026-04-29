# Projeto Desenvolvimento de Jogos
## [24-04-2026][mvfm]
---
### Aula de Hoje
- re-vendo essencialmente, os conceitos de câmera em espaço digital
- Agora levando em consideração do contexto do **Godot**.
- Todos os nomes traduzidos de funcionalidades da engine para português ficaram horríveis
	- Acho que literalmente passaram o que queriam traduzir no translate para PT-BR, colaram e copiaram pro código.
- Cohen mostra alguns efeitos engraçados com a câmera, mostrando que o redimensionamento da janela godot quebrava a renderização da cena de jogo.
- Coisa bem parecida com o que a gente via nos nossos códigos OpenGL na cadeira de CG.
	- A **mesma** coisa que eu tava passando hoje com o *vim*.
- [Link para documentação oficial Godot para o conteúdo da aula de hoje](https://docs.godotengine.org/en/stable/classes/class_camera2d.html)
- Thanks Zack Snyder, you prick.
- Documentação oficial também disponibilizar um exemplo de [jogos isométricos](https://godotengine.org/asset-library/asset/2718) utilizando os métodos de distorção que eventualmente vamos ver.
- ![Godot nodes](assets/godotnodes.png)
- "*Em geral se é recomendado o uso de v-sync*"
	- Mas e o mix, e os frags.

### Vamos falar um poquinho sobre a câmera
- Window & Viewport
	- SRU & SRP mencionados!!!
	- Essencialmente uma regra de três, assim como vimos na cadeira de CG.
	- Godot já faz essas bugigangas pra nós pelo **Nodo Camera2D**.
- Cohen menciona que o uso de diferentes viewports na mesa cena é possível, mas dá um poquinho mais de trabalho
	- Exemplo que faz ele mencionar isso é a implementação de **mini-maps** em certos jogos.
- **Camera Follow** parece ser literalmente mover a viewport junto com o sprite do personagem.
	- It *is* that easy.
	- Zero linhas de código, o máximo que o Cohen teve que fazer foi alterar a hierarquia de nodos na árvore de nodos do Godot.
- Cohen mostra que também conseguimos alterar **limites de câmera**, restringindo o espaço de visualização da mesma.
	- Novamente, zero linhas de código, só o sliderzinho da engine.
- Após isso, ele mostra um efeito de *delay* de acompanhamento da câmera
	- Mais ou menos como se fosse um verdadeiro camera-man tendo que movimentar a câmera fisicamente para filmar o que o jogador está fazendo.
	- Comentei com o cadu que isso pode ser utilizado para aumentar a ilusão de um personagem muito rápido.
