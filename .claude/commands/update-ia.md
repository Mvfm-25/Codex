Update each PUC subject's `IA/adicoes.md` file with complementary educational content for any aula not yet covered. Follow the instructions below precisely.

## Context

The Codex repository lives at `C:\GDM-05\Codex\`. Inside `PUC/`, there are six subject folders: `mn/`, `poa/`, `es2/`, `ux/`, `so/`, `pdj/`. Each has an `IA/adicoes.md` file — a document of AI-generated supplementary material that expands on the student's lecture notes.

### Style reference for `adicoes.md`

The file opens with:
```
# <Subject Name> — Adições & Aprofundamentos
## [Gerado por IA][mvfm]

> Material complementar às aulas anotadas. Segue os tópicos na ordem em que apareceram nas notas, preenchendo lacunas e expandindo o que foi mencionado brevemente.

---
```

Each aula's section follows this pattern:
```
## Aula XX — <Short descriptive title>

### <Topic Name>

<Substantive explanation that fills the gap between brief lecture notes and deeper understanding. Uses LaTeX math (`$...$` inline, `$$...$$` display), code blocks when relevant, comparison tables, and concrete examples. Formal theorem names, proofs, or historical context are added where the notes only gesture at them. Tone is direct, written for a CS undergraduate.>

---
```

The writing style:
- Portuguese (Brazilian), same register as existing entries.
- Bold key terms on first use.
- Fills in *what the notes omit* — formal definitions, proofs, complexity analysis, concrete failure cases, real-world applications — not a re-statement of what the notes already say.
- Ends each subject's file with a `### Referências para ir além` section listing 3–6 concrete resources, if not already present.

## Instructions

For each subject folder (`mn`, `poa`, `es2`, `ux`, `so`, `pdj`):

1. List all `aula*.md` files directly inside the subject folder (not in subfolders).
2. Read the subject's `IA/adicoes.md`.
3. Identify which aulas are **not yet covered** in `adicoes.md`. An aula is "covered" if there is an `## Aula XX` heading for it anywhere in the file.
4. For each uncovered aula:
   a. Read the aula file completely.
   b. Identify 2–4 concepts that the notes mention but leave underexplained — formal names, theorems, complexity, failure cases, historical context, or applications.
   c. Write a new section (or multiple sections) following the style reference above.
   d. Append the new section(s) to the end of `adicoes.md`, preceded by `---`.
5. Do not alter any existing content in `adicoes.md`.
6. Do not add sections for aulas whose files do not yet exist.

## Report

After all edits, print one line per subject:
- `<subject>: added Aula XX, Aula YY` — if new content was added.
- `<subject>: up to date` — if nothing was missing.
