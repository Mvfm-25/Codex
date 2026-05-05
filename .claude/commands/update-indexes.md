Update every index file across the Codex repository to reflect the current state of its folder. Follow the instructions below precisely.

## Context

The Codex repository lives at `C:\GDM-05\Codex\` and is an Obsidian vault. It has two main content sections:

- **PUC/** — university notes. Contains one `Index.md` at the top level, plus subject subfolders (`mn/`, `poa/`, `es2/`, `ux/`, `so/`, `pdj/`), each with its own `*-index.md`.
- **Informes/** — personal media log. Contains one `Index.md` at the top level, plus category subfolders (`Livros/`, `Gibis/`, `Filmes/`, `Vidya/`), each with its own `*-index.md`.

## Step 1 — Update each PUC subject index

For each subject folder inside `PUC/` (`mn`, `poa`, `es2`, `ux`, `so`, `pdj`):

1. List every `aula*.md` file directly inside the subject folder (not in subfolders).
2. Read the subject's `*-index.md` (e.g. `mn/mn-index.md`).
3. Compare: identify which aula files are **not yet listed** in the `### Aulas` section.
4. For each missing aula file, read it and extract **the key topics covered** — one or two short phrases, matching the terse style already in the index (e.g. `Padrão **IEEE 754**, notação científica e representação binária de decimais.`).
5. Insert the missing entries into the `### Aulas` section in **ascending numerical order**, using this exact format (tabs for indentation, matching the file):
   ```
   - [Aula XX](./aulXX.md)
   	- Key topic description.
   ```
6. Do not alter any other section (Trabalhos, Provas, Adições IA, headers, professor links, etc.).
7. Do not add entries for files inside subfolders (`trabalhos/`, `provas/`, `atividades/`, `IA/`).

## Step 2 — Update each Informes sub-index

For each category folder inside `Informes/` (`Livros/`, `Gibis/`, `Filmes/`, `Vidya/`):

1. List every `.md` file directly inside the category folder (excluding `*-index.md` itself and files inside `assets/`).
2. Read the category's `*-index.md` (e.g. `Livros/livros-index.md`).
3. Identify which item files are **not yet linked** in the index.
4. For each missing item, read it and extract its title and a one-sentence summary.
5. Add the missing entry in the appropriate section, following the link format already in use (e.g. `- [Title](./filename.md)`).
6. Do not alter the existing `Informes/Index.md` top-level file.

## Step 3 — Report

After all edits, print a concise summary:
- Which indexes were updated and what was added.
- Which indexes were already up to date (skip if none changed).
