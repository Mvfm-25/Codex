# Segurança de Sistemas
## [16/09][mvfm]
---
### Apresentação do TSE sobre validade & confirmação da urna eletrônica.
- Perdemos quase meia hora da aparesentação, mas o representante fala que eles compartilham os dados brutos da coleta de votos para cada partido participante da eleição para evitar a divergência de cálculos.
- Máquinas standalone imitando 
- Código aberto para organizações como o Ministério Público, OAB, CNJ, Policia Federal, Sociedade Brasileira da Computação, Departmanetos de TI das universidades possuem acesso ao código da urna eletrônica **um ano antes da eleição** para a verificação & inspeção da urna.
	- Resolução TSE 23.673/2021.
	- Representantes das forças armadas verificam & comparam o código liberado com o de uma urna.
- Resumos digitais de todos os arquivos finais, Assinaturas digitais do TSE e entidades legitimadas.
	- Código fonte armazenada em mídia na regravavel
	- Possiblidade de auditoria futura.
- Garante que o software que vai para urna é o mesmo que foi auditado / inspecionado.
**Side note : material da apresentação não foi liberado, possível que eu erre algo**

### Atacante externo consegue fazer algo com a urna?
- Houve um teste público de segurança da URNA, ocorrendo desde 2009. Obrigatório desde 2017, ocorrendo por volta de outubro.
	- Qualquer um pode se candidatar para fazer o teste.
    - Teste é re-feito meses depois para comparação.
    - 112 planos de teste. 07 edições : 2009, 2012, 2016, 2017, 2019, 2021 & 2023.
    - Uma hackatona gigante, com a polícia federal presente. Apresentador aponta que a PF foi o crítico mais crítico.
    - Esses testes precisam ser reprodutíveis.
- "*Suficientemente seguro*"

### PLanos de ataque
- Com o plano de ataque especificado, certas barreiras são "*relaxadas*" para tornar o teste viável. Procurando testar certo mecanismo, não o processo inteiro.
- Foto com o Ariel Ril & Daniel Dalalana sendo parte de um desses eventos. Ambos doutores da PUCRS

### Dispositivo Interno de Segurança
- Praticamente ninguém sabe.
- Verificador da assinatura digital de arquivos.
- Componentes internos :
    - DDR3 4gb
    - Processador x86 Intel Atom
    - Pendrive removivel
    - 2gb SATA m@
    - MSE - Moduslo segurança embarcado. Primeiro equipamento energizado
- Ele le, verifca & executa a BIOS. Carrega e verifica o Loader do KErnel, depois o Sistema Operacional UENUX. Ele manda um desafio criptografado para a urna resolver em 4 min antes de carregar os aplicativos de eleição e os dados dos eleitores.
    - Impede a execução de aplicativos que não são do TSE.
- Saindo da fábrica, a urna não consegue fazer nada. Peso de papel.
    - Só após a atualização & ceritificação do Firmaware ela é considerada 'inicializada'.
    - Par de chaves para cada modo.

### Não existe perfeição, especialmente em segurança.
- Frases do representante :
    - Melhoria contínua é imperativa.
    - A urna original de '96 é IRRECONHECÍVEL com a urna atual.
    - Crise de confiça baseia-se essencialmente em mentiras & boatos sem o menor fundamento

