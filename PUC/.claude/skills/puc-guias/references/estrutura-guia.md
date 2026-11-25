# Estrutura de um guia de prova (`materiais/P<n>.md`)

Modelo extraído dos guias de `cc` (2026/2), que o usuário aprovou. Adapte os títulos das seções
de conteúdo à cadeira; mantenha a ordem e os elementos fixos.

```markdown
# <Nome da Cadeira> — P<n> (dd/mm)
## <Temas da prova em uma linha>
[← P<n-1>](./P<n-1>.md) · [Materiais por Prova](./materiais-index.md) · [P<n+1> →](./P<n+1>.md)
---
### Conteúdo segundo o cronograma
| Data | Conteúdo | Notas | Material |
|---|---|---|---|
| dd/mm – dd/mm | <tema do cronograma> | [Aula13](../aula13.md), … | [<slide>](../atividades/x.pdf), … |

> **O formato da prova** (pelo exemplo [<prova antiga>](../provas/...)): <quantas questões, de que
> tipo, quantos pontos cada; o que vem anexo; desvios do cronograma (ex.: conteúdo de outra prova)>.
>
> Para aprofundar: <links para IA/resumo-*.md, simulados existentes>.

---
## 1. <Primeiro tópico>
### 1.1 <Conceito>
- Definição curta, na notação do professor.
- **Receita** numerada quando houver algoritmo (First, Follow, closure, esquema de tradução…).
- Exemplo **executado** logo em seguida: tabela de pilha | entrada | ação; derivação; código.
> Dica do professor (das notas): "<citação>" ([AulaNN](../aulaNN.md)).

## <k>. Exemplo resolvido — questão <x> da <prova-exemplo>
**Passo 1 — …** · **Passo 2 — …** · … (o raciocínio que o gabarito oficial esperaria)

---
## <k+1>. Atividades de preparo (novas)
> Tente sem olhar; o gabarito está na seção <k+2>.

**A1 — <tema>.** <enunciado>   ← prefixo por prova: A (P1), B (P2), G (P3)…, ou o que fizer sentido
...

---
## <k+2>. Gabarito
<details><summary>A1</summary>

<resposta completa, com o passo a passo; código em blocos ```code>
</details>
```

## Critérios de qualidade

- Cobertura: toda linha do recorte do `mapa-provas.json` aparece em alguma seção; toda nota
  `aulaNN.md` da prova está linkada (o `checa_md.py --mapa` confere).
- Proporção: a prova-exemplo indica o peso de cada tópico — tópicos de 4–6 pontos merecem
  exemplo resolvido completo e 2+ atividades; tópicos de 1 ponto, uma explicação curta.
- Atividades: misture (a) mecânicas com resposta única (tabelas, código, valores) — conferidas
  por script; (b) "estilo prova" dissertativas (V/F justificado, "explique quando e por quê");
  (c) pelo menos uma que combine dois tópicos.
- Não copie exercícios resolvidos do material do professor; pode partir da mesma *ideia* com
  outra gramática/programa.
- Tom: didático e direto, em português, frases curtas; termos técnicos como o professor usa.
