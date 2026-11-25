#!/usr/bin/env python3
"""Localiza a raiz PUC do vault Codex e, se possível, a cadeira em foco.

Uso:  python acha_puc.py [cadeira]

Imprime JSON:
  {"raiz": ".../PUC", "cadeira": "cc" | null, "pasta_cadeira": ".../PUC/cc" | null,
   "indice_cadeira": ".../cc/cc-index.md" | null, "cadeiras": ["cc", "es2", ...]}

Como a raiz é encontrada (na ordem):
  1. variável de ambiente PUC_ROOT;
  2. o diretório atual ou um de seus ancestrais é a raiz PUC;
  3. um ancestral contém PUC/ ou Codex/PUC/;
  4. locais conhecidos (Windows e Linux) do vault.
Uma pasta é "raiz PUC" quando tem subpastas <x> com o arquivo <x>/<x>-index.md.
A cadeira vem do argumento ou, se o diretório atual está dentro de PUC/<x>/, de <x>.
"""
import json
import os
import sys
from pathlib import Path


def cadeiras_em(p: Path):
    try:
        return sorted(d.name for d in p.iterdir()
                      if d.is_dir() and (d / f"{d.name}-index.md").is_file())
    except OSError:
        return []


def eh_raiz(p: Path) -> bool:
    # uma pasta de cadeira também pode ter subpastas com <x>-index.md (ex.: cc/materiais/),
    # então só vale como raiz se chamar PUC ou tiver pelo menos duas cadeiras
    if not p.is_dir():
        return False
    n = len(cadeiras_em(p))
    return n >= 2 or (n >= 1 and p.name.upper() == "PUC")


def candidatos():
    env = os.environ.get("PUC_ROOT")
    if env:
        yield Path(env)
    cwd = Path.cwd().resolve()
    for a in [cwd, *cwd.parents]:
        yield a
        yield a / "PUC"
        yield a / "Codex" / "PUC"
    home = Path.home()
    yield Path("C:/GDM-05/Codex/PUC")
    yield home / "penguosis" / "Codex" / "PUC"
    yield home / "Codex" / "PUC"


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raiz = next((c.resolve() for c in candidatos() if eh_raiz(c)), None)
    if raiz is None:
        print(json.dumps({"erro": "raiz PUC não encontrada; defina PUC_ROOT"}, ensure_ascii=False))
        sys.exit(1)
    cads = cadeiras_em(raiz)
    cadeira = sys.argv[1].strip("/\\") if len(sys.argv) > 1 else None
    if cadeira is None:
        try:
            rel = Path.cwd().resolve().relative_to(raiz)
            if rel.parts and rel.parts[0] in cads:
                cadeira = rel.parts[0]
        except ValueError:
            pass
    if cadeira is not None and cadeira not in cads:
        print(json.dumps({"erro": f"cadeira '{cadeira}' não existe em {raiz}", "cadeiras": cads},
                         ensure_ascii=False))
        sys.exit(1)
    pasta = raiz / cadeira if cadeira else None
    print(json.dumps({
        "raiz": str(raiz),
        "cadeira": cadeira,
        "pasta_cadeira": str(pasta) if pasta else None,
        "indice_cadeira": str(pasta / f"{cadeira}-index.md") if pasta else None,
        "cadeiras": cads,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
