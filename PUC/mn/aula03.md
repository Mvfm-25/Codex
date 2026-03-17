# Métodos Numéricos
## [10-03-2026][mvfm]

### IEEE 754
- Como se aramazenam números decimais em sistemas binários?
- Padrão formado em meados dos anos 80, disponibilizados em variados formatos
	1. Binário 16bits
	2. Binário 32bits
	3. Binário 64bits
- Formato binário é o equivalente ao **Float do Java**, JB comenta.
- Também temos em **Decimais*, algo que se é mais usado em processadores de calculadoras.
	1. Decimal 16bits
	2. Decimal 32bits
	3. Decimal 64bits
- Mas isso foi uma ideia completamente original? Se baseia em algo?

### [Notação Científica](https://www.calculatorsoup.com/calculators/math/scientific-notation-converter.php)
- Diretamente do artigo da Wikipédia sobre **Notação Científica** :
	- "Qualquer número real pode ser escrito no formato **m x $10^n$** de múltiplas maneiras. Por exemplo, **350** pode ser escrito como **3.5 x $10^2$** ou como **35 x $10^1$** ou até mesmo **350 x $10^0$**."
- Notação científica ajuda especialmente em casos de números muito pequenos ou muito grandes.
- A mesma ideia será transmitida para o padrão IEEE 754.
![[assets/nomeclatura.excalidraw | 100%]]
*Até mesmo as denominações de espaços*
*Leve em consideração também que, no contexto de processadores binários, a base acima sempre será 2.*
