# Segurança de Sistemas
## [19-08-26][mvfm]
---
### Cifras de Fluxo
- Definido bem resumidamente, nem por minha parte mas sim pelo Henry.
	- **Cifrar caracteres individuais, um de cada vez.**
- Principal exexmplo de tal tipo de cifra é : **One Time Pad** de 1917.
	- Marcado como '*Primeiro exemplo de cifra 'segura'*
	- Mas ainda acho muito engraçado que as cifras clássicas (De césar) ainda poderiam ser seguras caso 75% da população não fosse alfabetizado.
		- Oh, it isn't?

### One-Time-Pad
- '*Algoritmo em que o purotexto é combinado, caractere por caractere, a uma chave secreta aleatória que para isso deve ter, no mínimo, o mesmo número de caracteres do purotexto.*'
	- M=C={0,1}$^n$
	- K={0,1}$^n$
- Uso bem extensivo da operação XOR - 'Exclusive Or'.
	- Lembrando da tabela verdade :
	- 0 XOR 0 = 0
	- 1 XOR 1 = 0
	- 0 XOR 1 = 1
	- 1 XOR 0 = 1
- Olhando para um exemplo um pouco mais completo também ajuda :
	- 10100 XOR 10100 = 00000
	- 10101 XOR 00000 = 10101
- Ou seja, os 1's marcados no segundo exemplo prático demonstram apenas quais os bits que eram **diferentes** entre ambas strings.
- Uso do OTP :	
- ![One-Time-Pad in use.](assets/one-time-pad.png)
- Agora... Tendo tudo isso, OTP é decifrável? Acredito que pelo meu uso de '*segura*' algumas linhas acima sendo um claramente irônico, que você conseguiria perceber que sim. 
	- Mas como?
- Depois disso, atividade prática também disponível no moodle. Feita no caderno. 
