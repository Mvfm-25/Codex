# Sistemas Operacionais
## [10-06-2026][mvfm]

### Waste
- Hoje é uma aula não real
	- Alugado tempo no LabPro, supostamente para desenvolvimento do trabalho.
	- Esqueci de commitar de novo, todo trabalho tá local em casa. 
	- Nada que eu possa fazer.
- Vou trazer o máximo do conteúdo dos slides que eu conseguir. Não muita coisa além disso.
- Lembrando que a entrega para o T2 é dia **15**. 
	- Além disso, o F-16 tem que estar pelo menos montado até lá. 
	- As tintas aparentemente chegam só no dia 23, mas tenho os primers e finde compro o compressor de ar pro aerógrafo.
	- Fica com pouca coisa faltando

### File Locking
![Zero neurons.](assets/fillipoeseugato.png)
- Arquivo PDF da '*atividade prática*' que ninguém vai fazer mesmo começa com a definição de : **Concorrência Destrutiva.**
- Pra isso, ele re-lembra o que acontece em uma **Race Condition**
	- Múltiplos processos sendo executados concorrentemente 
	- Na execução de cada um, os processos tentam escrever em uma área crítica. Simultaneamente.
	- Sem nenhum tipo de sincronização isso, com certeza, dá errrado.
	- Consequentemente, o estado final desse dado escrito não pode ser confiado.
- O exemplo usa um cenário de banco, como normalmente se é demonstrado.

### Big League
- A solução, incrivelmente, é **File Locking**.
	- Pela explicação dada pelos slides, acho que isso é a mesma coisa que os **Semáforos** que vimos em **FPPD**, mas posso estar completamente errado.
- De vez em quando, a melhor solução é a mais burra idiota e simples de todas :
	1. Requisita a trava (**lock**)
	2. Executa operação crítica
	3. Destrava(**unlock**)
- Essa explicação sempre me incomodou um pouquinho pq isso essencialmente força os processos que estavam rodando concorrentemente à executarem de modo tradicional.
- Talvez a operação demore **ms** e a trava simplesmente pede para os outros processos que perderam na jogada de dados para **esperarem** um pouquinho. Talvez até en **ms** também.
	- Entendo que faz sentido e de fato funciona, mas ainda assim... Me incomoda.
- Pra complicar um pouquinho mais as coisas, Fillipo mostra que existem tipos de lock :

| Status atual | Requisição read | Requisição write |
| ............ | ............... | ................ |
| Livre        | **Permitido**   | **Permitido**    |
| Shared Lock  | **Permitido**   | *Bloqueado*      |
| Exclusive Lock| *Bloqueado*    | *Bloqueado*      |
