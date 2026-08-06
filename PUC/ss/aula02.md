# Segurança De Sistemas
## [05-08-26][mvfm]
---
### Na Teoria
- Na teoria, todos os algoritmos criptográficos que vamos ver são quebráveis, mas praticamente, é impossivelmente impossível ter um computador poderoso o suficiente para quebrá-los.
- Definições de Criptografia :
	- **A arte e ciência de manter informações seguras.**
	- **Criptografia envolve a projeção de confiança: levar confiança de onde existe para onde é necessária.**
- '*Cifra e criptografia são intercambeáveis**'
- E como tudo isso funciona?
	- Tendo um enviador e receptor. Mensagens à cifrar.
	- Texto Claro -> Cifrar -> Texto Cifrado -> Decifrar -> Texto Claro Original.
- No mundo ideal, não seria possível distinguir o texto cifrado de um texto completamente aleatório.
- Tudo que vamos ver, tem um pequeno *sinalzinho* do texto original no texto cifrado.
	- Dado poder computacional suficiente, conseguiriamos distinguir do aleatorio verdadeiro.
- Metas
	1. Privacidade : Sem vazar dados confidenciais
	2. Autenticação : Sem se passar por outro
	3. Integridade : Sem alteração
	4. Não-Repúdio : Não ser capaz de negar

### Algoritmos Chave
- **Cifra**
	- Um algoritmo criptográfico para criar (criptografar) e decifrar (decriptografar).
- **Chave**
	- Usada para cifrar e decifrar.
- **Espaço da Chave**
	- Quantia de chaves possíveis.
- '*O segredo deve estar totalmente na chave e não na cifra.*'
	- Princípio de Kerckhoff (1883)
- Kerckhoff e seus seis princípios
	1. O sistema deveria ser inquebrável na prática, se não teoricamente inquebrável.
	2. O projeto de um sistema não deve necessitar do segredo do sistema.
	3. A chave deve ser memorizável e fácil de alterar.
	4. Os criptogramas devem ser transmissíveis por telégrafo.
	5. O equipamento deve ser portável e operável por uma única pessoa.
	6. O sistema deve ser fácil de usar. 
- Chaves e funcionalidade assimétricas.
![Diferentes chaves para diferentes coisas](assets/cifras.png)
- Tendo todo esse conhecimento, é completamente previsível que pessoas vão tentar quebrar tais sistemas. 
![ATAQUE](assets/modelos_ataque.png)

### Atividade Prática
[Análise de Malware] - Virus Dissection, Ransomware, Trojans
- O que é?
	- Estudo dos recrurso, objetivo, fontes e efeitos potenciais exclusivos de sfotware e código prejudiciais. - Fortinet
	- Ele analisa o código de malware para entender como ele varia de outros tipos. - Fortinet
	- '*Cat-and-mouse game.*' - TryHackMe
	- '*While malware analysts keep finding ways to identify and neutralize these techniques*' - TryHackMe
	- '*Malware analysis dissects malware to gather information about the malware functionality, how the system was compromised so that you can defend against future attacks*' - IBM.
- Perfil do Profissional
	- Coursera :  https://coursera.org/learn/malware-analysis-and-assembly | **IBM**
		- **Linux, Windows Powershell, Virtual Machines.**
	- EDX :  https://www.edx.org/course/malware-analysis-and-assembly-language-introduction | **IBM**
		- **C, C++. Assembly, Machine Assembly.**
