#!/usr/bin/env python3
"""Extrai texto de PDF/PPTX/DOCX de uma cadeira para um cache reutilizável.

Uso:  python extrai_texto.py <pasta_cadeira> [--forcar]

Percorre atividades/, provas/, trabalhos/ e a raiz da cadeira (não entra em materiais/, IA/,
assets/ nem pastas ocultas). Para cada .pdf/.pptx/.docx grava o texto compactado em
  <pasta_cadeira>/materiais/.cache/<caminho relativo>.txt
e mantém <pasta_cadeira>/materiais/.cache/manifest.json com, por arquivo:
  mtime, tamanho, linhas, titulo (1ª linha significativa), exercicios (linhas onde aparecem
  "Exercício", "Gabarito", "Lista de exercícios"...) e status (novo | atualizado | cache).
Só reextrai o que mudou desde a última execução (use --forcar para refazer tudo).

Imprime um resumo JSON com os arquivos novos/atualizados e os que falharam.
PDF usa o `pdftotext` (poppler); PPTX/DOCX são lidos como zip, sem dependências.
"""
import json
import re
import shutil
import hashlib
import subprocess
import sys
import unicodedata
import zipfile
from pathlib import Path

EXT = {".pdf", ".pptx", ".docx"}
PULAR = {"materiais", "IA", "assets", "node_modules"}
EXERC = re.compile(r"(exerc[ií]cio|gabarito|lista de exerc|quest[aã]o\s*\d|atividade)", re.I)
ENT = {"&lt;": "<", "&gt;": ">", "&amp;": "&", "&quot;": '"', "&apos;": "'"}


def desescapa(s):
    for k, v in ENT.items():
        s = s.replace(k, v)
    return s


# PDFs gerados por LaTeX saem do pdftotext com o acento antes da letra, como caractere solto:
# "Exerc´ıcio", "Seguran¸ca", "Gera¸c˜ao". Recompõe para "Exercício", "Segurança", "Geração".
ACENTOS = {"´": "́", "`": "̀", "˜": "̃", "ˆ": "̂", "¸": "̧", "¨": "̈"}
LATEX_ACENTO = re.compile(r"([A-Za-zı]?)([´`˜ˆ¸¨])\s?([A-Za-zı])")
VOGAL = set("aeiouAEIOUı")


def normaliza_latex(s: str) -> str:
    # o acento pode vir antes da letra ("N˜ao", "s´o") ou depois dela ("pu´blicos", "nu´mero"):
    # entre vogal e consoante ele pertence à vogal anterior; nos demais casos, à letra seguinte
    def junta(m):
        ant, ac, prox = m.groups()
        if ac == "¸":                       # cedilha só existe no c
            return ant + ("ç" if prox == "c" else "Ç" if prox == "C" else ac + prox)
        if ac == "`" and not (prox in "aA" or (ant and ant.isalpha() and prox in "eE")):
            return m.group(0)               # `x é aspa de abertura do LaTeX; crase só em à e "Vigenère"
        if ac == "˜" and ant in ("a", "o") and prox in ("o", "e"):
            return unicodedata.normalize("NFC", ant + ACENTOS[ac]) + prox   # "a˜o" → "ão", "o˜e" → "õe"
        if ant and ant in VOGAL and prox not in VOGAL:
            ant = "i" if ant == "ı" else ant
            return unicodedata.normalize("NFC", ant + ACENTOS[ac]) + prox
        prox = "i" if prox == "ı" else prox
        return ant + unicodedata.normalize("NFC", prox + ACENTOS[ac])
    s = re.sub(r"([cC])¸", lambda m: "ç" if m.group(1) == "c" else "Ç", s)   # cedilha depois do c
    return unicodedata.normalize("NFC", LATEX_ACENTO.sub(junta, s))


def compacta(texto: str) -> str:
    texto = normaliza_latex(texto)
    linhas = []
    for l in texto.replace("\r", "").split("\n"):
        l = re.sub(r"[ \t]{3,}", "  ", l.rstrip())
        if l.strip() == "" and (not linhas or linhas[-1] == ""):
            continue
        linhas.append(l)
    return "\n".join(linhas).strip() + "\n"


def de_pdf(p: Path) -> str:
    if not shutil.which("pdftotext"):
        raise RuntimeError("pdftotext não encontrado (instale poppler)")
    r = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(p), "-"],
                       capture_output=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode("utf-8", "replace")[:200])
    return r.stdout.decode("utf-8", "replace")


def de_pptx(p: Path) -> str:
    z = zipfile.ZipFile(p)
    slides = sorted((n for n in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
                    key=lambda n: int(re.findall(r"\d+", n)[0]))
    out = []
    for i, n in enumerate(slides, 1):
        x = z.read(n).decode("utf-8", "replace")
        out.append(f"--- slide {i}")
        for par in re.findall(r"<a:p>(.*?)</a:p>", x, re.S):
            t = "".join(re.findall(r"<a:t>(.*?)</a:t>", par))
            if t.strip():
                out.append(desescapa(t))
    return "\n".join(out)


def de_docx(p: Path) -> str:
    x = zipfile.ZipFile(p).read("word/document.xml").decode("utf-8", "replace")
    pars = re.findall(r"<w:p[ >].*?</w:p>", x, re.S)
    return "\n".join(desescapa("".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", par))) for par in pars)


LEITOR = {".pdf": de_pdf, ".pptx": de_pptx, ".docx": de_docx}


def arquivos(pasta: Path):
    for p in sorted(pasta.rglob("*")):
        rel = p.relative_to(pasta)
        if any(part in PULAR or part.startswith(".") for part in rel.parts[:-1]):
            continue
        if p.name.startswith((".", "~$")) or p.suffix.lower() not in EXT or not p.is_file():
            continue
        yield p, rel


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    pasta = Path(sys.argv[1]).resolve()
    forcar = "--forcar" in sys.argv
    cache = pasta / "materiais" / ".cache"
    cache.mkdir(parents=True, exist_ok=True)
    mpath = cache / "manifest.json"
    antigo = json.loads(mpath.read_text(encoding="utf-8")) if mpath.exists() else {}
    novo, mudou, falhas = {}, [], []
    for p, rel in arquivos(pasta):
        chave = rel.as_posix()
        st = p.stat()
        dest = cache / (chave + ".txt")
        ant = antigo.get(chave)
        if ant and not forcar and ant.get("mtime") == st.st_mtime and dest.exists():
            novo[chave] = {**ant, "status": "cache"}
            continue
        try:
            texto = compacta(LEITOR[p.suffix.lower()](p))
        except Exception as e:  # arquivo corrompido, protegido etc.
            falhas.append({"arquivo": chave, "erro": str(e)})
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(texto, encoding="utf-8")
        linhas = texto.splitlines()
        titulo = next((l.strip() for l in linhas if len(l.strip()) > 3 and not l.startswith("---")), "")
        exerc = [i + 1 for i, l in enumerate(linhas) if EXERC.search(l)]
        status = "atualizado" if ant else "novo"
        novo[chave] = {"mtime": st.st_mtime, "tamanho": st.st_size, "linhas": len(linhas),
                       "titulo": titulo[:120], "exercicios": exerc[:60], "cache": dest.relative_to(pasta).as_posix(),
                       "sha1": hashlib.sha1(p.read_bytes()).hexdigest(), "status": status}
        mudou.append({"arquivo": chave, "status": status, "linhas": len(linhas), "titulo": titulo[:80]})
    removidos = sorted(set(antigo) - set(novo))
    # o mesmo arquivo em duas pastas (ex.: atividades/ e provas/p1/) → indexar uma vez só
    por_hash = {}
    for k, v in novo.items():
        if v.get("sha1"):
            por_hash.setdefault(v["sha1"], []).append(k)
    duplicados = [sorted(ks) for ks in por_hash.values() if len(ks) > 1]
    mpath.write_text(json.dumps(novo, ensure_ascii=False, indent=2), encoding="utf-8")
    gi = pasta / "materiais" / ".gitignore"
    if not gi.exists():
        gi.write_text(".cache/\n", encoding="utf-8")
    # ensure_ascii: a saída é lida por outros processos, e o console do Windows (cp1252) quebra
    # nomes com acento — sobretudo os em NFD ("e" + acento combinante)
    print(json.dumps({"cadeira": pasta.name, "total": len(novo), "novos_ou_atualizados": mudou,
                      "removidos": removidos, "duplicados": duplicados, "falhas": falhas,
                      "manifest": str(mpath)}, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
