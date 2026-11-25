#!/usr/bin/env python3
"""Verificações mecânicas dos guias/índices em Markdown de uma cadeira.

Uso:  python checa_md.py <arquivo.md | pasta> [...] [--mapa mapa-provas.json]

Para cada .md:
  links     — todo link relativo [texto](alvo) aponta para um arquivo existente. Entende
              <alvo com espaços (e parênteses)>, ignora http(s)/mailto, âncoras puras e tudo que
              está dentro de blocos de código ou `código inline` (onde "[Ee](\\+|\\-)" não é link).
  codificação — UTF-8 válido, sem BOM, sem mojibake típico de leitura cp1252 ("Ã§", "Ã£", "â€").
  details   — quantidade de <details> igual à de </details>.
  cobertura (com --mapa e arquivo P<n>.md) — toda nota aulaNN.md que o mapa associa à prova P<n>
              aparece linkada no guia.
Sai com código 1 se houver problema. Imprime um relatório por arquivo.
"""
import json
import re
import sys
from pathlib import Path

MOJIBAKE = re.compile(r"Ã[\x80-\xbf§£¡©ª³µº]|â€|Â[ ·]")


def tira_codigo(texto):
    texto = re.sub(r"(?ms)^\s*(```|~~~).*?^\s*\1\s*$", lambda m: "\n" * m.group(0).count("\n"), texto)
    return re.sub(r"`[^`\n]*`", "", texto)


def links(texto):
    out = []
    for m in re.finditer(r"\]\(", texto):
        i = m.end()
        if i < len(texto) and texto[i] == "<":
            j = texto.find(">", i)
            if j == -1:
                continue
            alvo = texto[i + 1:j]
        else:
            prof, j = 1, i
            while j < len(texto) and prof:
                if texto[j] == "(":
                    prof += 1
                elif texto[j] == ")":
                    prof -= 1
                elif texto[j] in " \n":
                    break
                j += 1
            alvo = texto[i:j - 1] if prof == 0 else texto[i:j]
        linha = texto.count("\n", 0, m.start()) + 1
        out.append((linha, alvo.strip()))
    return out


def checa(arquivo: Path, mapa):
    probs = []
    bruto = arquivo.read_bytes()
    if bruto.startswith(b"\xef\xbb\xbf"):
        probs.append("BOM no início do arquivo (salvar como UTF-8 sem BOM)")
    try:
        texto = bruto.decode("utf-8-sig")
    except UnicodeDecodeError as e:
        return [f"não é UTF-8 válido: {e}"]
    for n, l in enumerate(texto.splitlines(), 1):
        if MOJIBAKE.search(l):
            probs.append(f"linha {n}: possível mojibake: {l.strip()[:70]}")
            break
    a, f = texto.count("<details"), texto.count("</details>")
    if a != f:
        probs.append(f"<details> desbalanceado: {a} abertos, {f} fechados")
    sem_cod = tira_codigo(texto)
    vistos = set()
    for linha, alvo in links(sem_cod):
        if not alvo or re.match(r"^(https?:|mailto:|obsidian:|#)", alvo):
            continue
        caminho = alvo.split("#")[0]
        if not caminho:
            continue
        p = (arquivo.parent / caminho)
        if not p.exists():
            probs.append(f"linha {linha}: link quebrado → {alvo}")
        vistos.add(p.resolve() if p.exists() else None)
    m = re.fullmatch(r"(P\d|PS|G\d)\.md", arquivo.name)
    if mapa and m:
        prova = next((p for p in mapa["provas"] if p["nome"] == m.group(1)), None)
        if prova:
            pasta = arquivo.resolve().parent.parent   # resolve: o argumento pode ser relativo ("." ou "P2.md")
            for aula in prova["aulas"]:
                if aula.get("tipo") == "logistica":       # correção de prova, feriado... não precisam estar no guia
                    continue
                for nota in aula.get("notas", []):
                    if (pasta / nota).resolve() not in vistos:
                        probs.append(f"cobertura: {nota} ({aula['data']}, {aula['descricao'][:40]}) não está linkada no guia")
    return probs


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    mapa = None
    if "--mapa" in args:
        k = args.index("--mapa")
        mapa = json.loads(Path(args[k + 1]).read_text(encoding="utf-8"))
        args = args[:k] + args[k + 2:]
    arquivos = []
    for a in args:
        p = Path(a)
        arquivos += sorted(p.glob("*.md")) if p.is_dir() else [p]
    total = 0
    for arq in arquivos:
        probs = checa(arq, mapa)
        total += len(probs)
        print(f"{'✔' if not probs else '✘'} {arq.name}" + ("" if not probs else f" — {len(probs)} problema(s)"))
        for pr in probs:
            print(f"    {pr}")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
