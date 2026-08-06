# Métodos Formais 
## [06-08-2026][mvfm]
---
### Doing things Formally
- Cheguei um pouco atrasado à aula, mas o Júlio estava apenas fazendo uma pequena introduçãozinha ao que a gente vai estar fazendo no semestre : 
	- Provando *formalmente* (lol) que nossos algoritmos de fato funcionam, **em todos os casos**.
- Ou seja, aquele negócio que eu tinha comentando em alguma conversa qualquer que a gente da computação nunca precisaria fazer de fato.
- Deixando esse trabalho pros matemáticos que adoram tortura.
	- Oh well
- '*modelagem correção do sistema de ferrovias, especialmente na europa.*'
	- O mesmo exemplo da aula passada
	- Acho que vai ser aquele tipo de exemplo que ele vai trazer o semestre inteiro, bem como ele fez em ESII.
- Júlio também liberou certos exercícios de revisão, focando especificamente em lógica para computação.
- Seguem os dois principais :
	- [Lista 01](atividades/ExerciciosEspecificacao.pdf)
	- [Lista 02](atividades/RevisaoLogica.pdf)
- Primeira instância de '*exemplo bem bobinho*' do semestre.

### Exercícios
- Júlio coloca no quadro o seguinte slide :
	- '*Escrever uma função (em java) para calcular o ponto médio (um número natural) de um intervalo de valores naturais fechado em ambas extremidades.*'
- Tendo a especificação do cliente já validada anteriormente, como provamos formalmente que o tal algoritmo escrito funciona de fato mesmo?
- '*É sempre útil pedir ao cliente um exemplo do que ele quer de fato.*'
	- Ele nunca vai te dar uma explicação melhor.
- Para o exemplo anterior, os exemplos são os seguintes :
	- **Entrada [0,10]** | Saída [5]
	- **Entrada [3,10]** | Saída [6]
- Como passamos a especificação do cliente, de pt-Br para Matemátiquês?
	- Especificamos primeiro : **O domínio | contra-domínio** | D -> CD
	- Conjuntos de entrada & saída, para o programador leigo.
- Dado um valor $a$ & $b$, que definem as extremidades, ambos números naturais.	
	- $N$ x $N$ -> $N$
	- pontoMedio($a$,$b$) = $r$
	- De dois naturais, para um outro novo natural.
- '*Podemos ser um pouquinho mais claro nessa especficação.*'
	- '*Me descreva tudo que é verdadeiro para que essa computação dê certo. Me dê essas pré-condições.*'

### Sendo mais específico
- O que podemos considerar como pré-condições?
- Qual a forma lógica trivialmente verdadeira, tendo em vista que não temos restrições para $a$ & $b&?
	- Pré-Condições : **T**
	- **T** significa diretamente **TRUE**. Ainda não tenho o símbolozinho bonito para false, então em futuro uso **FALSE** vai ser simplesmente um **F**
- E se passarmos um intervalo como : [**7, 1**]. Funciona, ou não?
	- Isso depende inteiramente do cliente. 
- E o cliente, sendo o babaca que sempre é, esclarece : **NÃO**
- Então temos restrições. As pré-condições previamente estabelecidas estão incorretas. Como fica as précondições agora?
	- **PRE** : $a <= b$
	- **PÓS** : $r = [(a + b) / 2]$ Os colchetes nesse caso tentando representar o símbolo de arredondar para baixo.
	- '*Projeto baseado em contrato, Design by Contract*'
- '*Mesmo que eu tenha usado esse exemplo bobinho*'
- Testes unitários não exemplificam nada. Sò mostram que o programa funciona **NAQUELE** teste.
- Tendo isso, o programa está correto?
	```code
	public class Util {
		public static int pontoMedio(int a, int b){
			return (a + b) / 2;
		}
	}
	```
	- Sim! Por mais que o cliente use os parâmetros [**7, 1**], o programa está correto. Só quer dizer que o Cliente quebrou o contrato anteriormente estabelecido.
- Puramente mentira, o conjunto de entrada está completamente errado. '*int*' não é do conjunto **Natural**.
- Agora mexendo apenas com números negativos, temos que especificar que **não** trabalhamos com números negativos. Ou seja :
	- **PRÉ** : $ a >= 0 ^ b >= 0 ^ a <= b $
- A **PÓS** continua a mesma, o **PRÉ** já lida com as restrições que deveríamos lidar.
- Alerta Vermelho de tempestade severa tocou no meio da aula. Parecia o alarme dum amber alert.
	- Talvez a coisa mais engraçada que já acontecu na aula.
- Mesmo usando 'int', o programa está incorreto. Eles não são representações perfeitas de números inteiros. Somando dois números int gigantes, dá overflow. Voltando um número negativo.
	- Vamos à esse nível.
	- Software mata.
