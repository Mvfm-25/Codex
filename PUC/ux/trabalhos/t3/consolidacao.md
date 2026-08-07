# Experiência do Usuário
## [23-06-26] - Grupo 07
---
### Consolidação
#### No que concordamos, no que discordamos. Principais 10.

##### Critérios de avaliação
- Cada tópico a seguir é associado a uma das **10 Heurísticas de Nielsen** e classificado segundo a **escala de severidade** (também de Nielsen) :
	- **0** — Não é um problema de usabilidade.
	- **1** — Cosmético : não precisa ser corrigido, a menos que haja tempo disponível.
	- **2** — Menor : correção de baixa prioridade.
	- **3** — Grave : importante corrigir, alta prioridade.
	- **4** — Catastrófico : imperativo corrigir antes do lançamento.
---

- 1. Ausência de preview da rota no convite.
	- Ao receber um convite para uma nova rota do motorista, o passageiro não tem acesso a uma visualização prévia do trajeto proposto.

	> **Heurística :** #1 — Visibilidade do status do sistema · **Severidade :** 3 (Grave)
	> O passageiro precisa decidir se aceita a rota sem dispor da informação central para essa decisão : o próprio trajeto.

- 2. Falta de termos de uso.
	- Na abertura do aplicativo, o usuário, independentemente de ser passageiro ou motorista, não é apresentado aos termos e condições de uso.

	> **Heurística :** #10 — Ajuda e documentação · **Severidade :** 3 (Grave)
	> Além do impacto sobre a confiança do usuário, a ausência de termos de uso é uma lacuna legal relevante para um aplicativo que lida com transporte de pessoas.

- 3. Pergunta inicial "**Você possui dependentes?**".
	- A formulação dá a impressão de que o usuário sem dependentes **não** estaria apto a utilizar o aplicativo.

	> **Heurística :** #2 — Correspondência entre o sistema e o mundo real · **Severidade :** 1 (Cosmético)
	> A formulação pode induzir um modelo mental equivocado, ainda que o usuário consiga prosseguir selecionando "Não".

- 4. Falta de auto-complete no cadastro do veículo.
	- A ausência de preenchimento assistido torna a adição e a atualização dos veículos do motorista uma tarefa repetitiva e propensa a erros.

	> **Heurística :** #7 — Flexibilidade e eficiência de uso · **Severidade :** 2 (Menor)
	> Não bloqueia a tarefa, mas a torna lenta e repetitiva, sobretudo para o motorista que atualiza seus dados com frequência.

- 5. Reutilização de dados já fornecidos.
	- O usuário não consegue salvar endereços favoritos ou recorrentes, como definir locais marcados como "casa" ou "trabalho".

	> **Heurística :** #6 — Reconhecimento em vez de memorização · **Severidade :** 2 (Menor)
	> O usuário é obrigado a redigitar endereços a cada uso, em vez de reconhecê-los e reaproveitá-los a partir de registros anteriores.

- 6. Adição de dependentes sem fluxo associado.
	- Nas configurações do passageiro, a tela "Meus Dependentes" exibe um botão "+ Adicionar" que não está vinculado a nenhum fluxo; apenas a remoção de um dependente está implementada, permitindo excluir, mas não cadastrar novos.

	> **Heurística :** #3 — Controle e liberdade do usuário · **Severidade :** 2 (Menor)
	> O usuário tem controle parcial sobre seus dependentes : consegue remover, mas não adicionar, o que limita o gerenciamento da própria conta.

- 7. Ausência de método de autenticação secundário.
	- O aplicativo não oferece uma forma alternativa de autenticação, deixando o acesso dependente de um único método.

	> **Heurística :** #7 — Flexibilidade e eficiência de uso · **Severidade :** 2 (Menor)
	> Sem um caminho alternativo de acesso, o usuário fica vulnerável a perder a entrada na conta caso o método único falhe.

- 8. Falta de validação da quantidade de assentos disponíveis.
	- Embora exista um teto de passageiros, não há nenhum mecanismo que comprove que o veículo realmente possui a quantidade de assentos informada pelo motorista.

	> **Heurística :** #5 — Prevenção de erros · **Severidade :** 3 (Grave)
	> A capacidade do veículo impacta diretamente a operação e a segurança das rotas; aceitar um valor não verificado abre margem para dados incorretos.

- 9. Ausência de uma tela dedicada a eventos.
	- Tanto o passageiro quanto o motorista não dispõem de uma janela própria para eventos recentes, apoiando-se inteiramente nas notificações.

	> **Heurística :** #1 — Visibilidade do status do sistema · **Severidade :** 3 (Grave)
	> Mudanças de estado relevantes só são visíveis no momento da notificação; uma vez perdida, o usuário não tem onde recuperar o histórico do que ocorreu.

- 10. Falta de priorização de rotas.
	- Não há destaque para rotas em andamento nem para aquelas previamente definidas como favoritas.

	> **Heurística :** #7 — Flexibilidade e eficiência de uso · **Severidade :** 2 (Menor)
	> A ausência de aceleradores e de hierarquia entre as rotas obriga o usuário a localizar manualmente o que deveria estar em evidência.
