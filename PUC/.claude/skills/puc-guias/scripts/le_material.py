#!/usr/bin/env python3
"""Lê o texto já extraído (materiais/.cache) de um ou mais materiais, sem o ruído dos slides.

Uso:  python le_material.py <pasta_cadeira> <trecho do nome> [<trecho> ...] [--max 400]

Cada <trecho> casa com o caminho do material ignorando acentos e a forma Unicode (NFC/NFD) —
"TrocaDeChaves", "RSA (60min)", "Blockchain". Remove linhas repetidas (rodapés, cabeçalhos de
slide), números de página, autoria ("Prof.", "Escola Politécnica"). --max limita as linhas por
material. Imprime "##### <arquivo>" antes de cada um.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path


def chave(s):
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c))


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    a = sys.argv[1:]
    if len(a) < 2:
        print(__doc__)
        sys.exit(2)
    opts = {"--max": 400, "--de": 0}
    for o in opts:
        if o in a:
            i = a.index(o)
            opts[o] = int(a[i + 1])
            a = a[:i] + a[i + 2:]
    mx, de = opts["--max"], opts["--de"]
    cache = Path(a[0]) / "materiais" / ".cache"
    arquivos = sorted(cache.rglob("*.txt"))
    try:
        man = json.loads((cache / "manifest.json").read_text(encoding="utf-8"))
        sha = {chave(v["cache"]): v.get("sha1") for v in man.values()}
    except (OSError, ValueError):
        sha = {}
    ja = set()
    for trecho in a[1:]:
        achou = [p for p in arquivos if chave(trecho) in chave(p.relative_to(cache).as_posix())]
        if not achou:
            print(f"##### (nada casa com '{trecho}')")
        for p in achou:
            h = sha.get(chave("materiais/.cache/" + p.relative_to(cache).as_posix()))
            if h and h in ja:          # cópia idêntica (ex.: atividades/ e provas/p1/)
                continue
            ja.add(h)
            print("#####", unicodedata.normalize("NFC", p.relative_to(cache).as_posix())[:-4])
            vistos, n, k = set(), 0, 0
            for l in p.read_text(encoding="utf-8").splitlines():
                s = l.strip()
                # só números CURTOS são página/rodapé; "000…000" (IV, chave) é dado e fica
                if len(s) < 3 or (len(s) <= 7 and re.fullmatch(r"[\d\s/]+", s)) or s in vistos:
                    continue
                if re.search(r"(?i)\bprof\.|escola polit|cap[ií]tulo \d+ do livro", s):
                    continue
                vistos.add(s)
                k += 1
                if k <= de:
                    continue
                print(s[:120])
                n += 1
                if n >= mx:
                    print("… (cortado em --max)")
                    break


if __name__ == "__main__":
    main()
