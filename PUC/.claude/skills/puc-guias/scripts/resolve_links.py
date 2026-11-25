#!/usr/bin/env python3
"""Troca {{caminho/do/arquivo}} pelo link Markdown com o nome EXATO do disco.

Uso:  python resolve_links.py <modelo.md> <saida.md>

<saida.md> deve ficar em <cadeira>/materiais/; os caminhos em {{…}} são relativos à pasta da
cadeira e podem ser escritos com acentos compostos (NFC) — o script encontra o arquivo mesmo que
o nome no disco esteja em NFD ("e" + acento combinante), comum em arquivos vindos do macOS ou do
Moodle, e que um link digitado à mão não acharia. Nomes com espaço ou parênteses saem entre <…>.
{{caminho|texto}} usa "texto" como rótulo; sem "|", o rótulo é o nome do arquivo sem extensão.
Sai com código 1 e lista o que não encontrou.
"""
import re
import sys
import unicodedata
from pathlib import Path


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    saida = Path(sys.argv[2]).resolve()
    base = saida.parent.parent
    disco = {unicodedata.normalize("NFC", p.relative_to(base).as_posix()): p.relative_to(base).as_posix()
             for p in base.rglob("*") if p.is_file() and ".cache" not in p.parts}
    faltou = []

    def troca(m):
        alvo, _, rot = m.group(1).partition("|")
        nfc = unicodedata.normalize("NFC", alvo.strip())
        real = disco.get(nfc)
        if not real:
            faltou.append(nfc)
            return m.group(0)
        rot = rot.strip() or Path(nfc).stem.replace("___", " — ").replace("_", " ").strip()
        link = "../" + real
        return f"[{rot}](<{link}>)" if re.search(r"[ ()]", link) else f"[{rot}]({link})"

    txt = Path(sys.argv[1]).read_text(encoding="utf-8")
    saida.write_text(re.sub(r"\{\{(.+?)\}\}", troca, txt), encoding="utf-8", newline="\n")
    if faltou:
        print("não encontrados:", *faltou, sep="\n  ")
        sys.exit(1)
    print("ok:", saida)


if __name__ == "__main__":
    main()
