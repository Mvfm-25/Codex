#!/usr/bin/env python3
"""Converte o texto de um cronograma SARC/PUCRS no recorte "o que cai em cada prova".

Uso:  python mapa_provas.py <cronograma.txt> <pasta_cadeira> [--saida <pasta>]

Lê as linhas do cronograma (formato do Export.aspx do SARC, copiado como texto), detecta
as provas, distribui as aulas entre elas e casa cada aula do cronograma com os arquivos
aulaNN.md da cadeira pela data do cabeçalho da nota.

Gera, em <pasta> (padrão: <pasta_cadeira>/materiais):
  mapa-provas.json  — dados para as skills seguintes
  mapa-provas.md    — versão legível (rascunho; a skill acrescenta as observações)
"""
import json
import re
import sys
from pathlib import Path

DIAS = r"(SEG|TER|QUA|QUI|SEX|SAB|SÁB|DOM)"
LINHA = re.compile(rf"(?m)^\s*(\d*)\s*{DIAS}\s+(\d{{2}})/(\d{{2}})/(\d{{4}})[^\n]*\n([^\n]*)")
NOME_PROVA = re.compile(r"\b(P\d|PS|G1|G2)\b")
DATA_NOTA = re.compile(r"(\d{1,2})[/-](\d{1,2})(?:[/-](\d{2,4}))?")


def le_cronograma(texto: str):
    linhas = []
    for m in LINHA.finditer(texto):
        num, _dia, d, mth, ano, resto = m.groups()
        partes = [p.strip() for p in resto.split("\t")]
        if partes and re.match(r"^\d{1,2}:\d{2}", partes[0]):
            partes = partes[1:]
        desc = partes[0] if partes else ""
        ativ = partes[1] if len(partes) > 1 else ""
        rec = partes[2] if len(partes) > 2 else ""
        linhas.append({
            "num": int(num) if num else None,
            "data": f"{d}/{mth}/{ano}",
            "dm": (int(d), int(mth)),
            "ano": int(ano),
            "descricao": desc,
            "atividade": ativ,
            "recursos": rec,
        })
    return linhas


def eh_prova(l):
    return "prova" in l["atividade"].lower() and NOME_PROVA.search(l["descricao"] + " " + l["atividade"])


def datas_das_notas(pasta: Path, ano_padrao: int):
    notas = {}
    for f in sorted(pasta.glob("aula*.md")):
        if not re.fullmatch(r"aula\d+(-\d+)?\.md", f.name):
            continue
        try:
            cabeca = f.read_text(encoding="utf-8", errors="replace").splitlines()[:6]
        except OSError:
            continue
        notas[f.name] = None          # sem data no cabeçalho, até prova em contrário
        for linha in cabeca:
            if linha.lstrip().startswith("##"):
                m = DATA_NOTA.search(linha)
                if m:
                    notas[f.name] = (int(m.group(1)), int(m.group(2)))
                    break
    return notas


LOGISTICA = re.compile(r"feriado|d[uú]vidas|corre[cç][aã]o|entrega de trabalho|apresenta[cç][aã]o dos trabalhos|"
                       r"semana acad[eê]mica|revis[aã]o de provas|^\s*$", re.I)


def tipo_linha(l):
    """'logistica' para linhas sem conteúdo novo (feriado, dúvidas, correção, apresentação de trabalhos)."""
    if LOGISTICA.search(l["descricao"]) or l["atividade"].lower().startswith("trabalho"):
        return "logistica"
    return "conteudo"


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        sys.exit(2)
    crono = Path(args[0])
    pasta = Path(args[1])
    saida = Path(args[args.index("--saida") + 1]) if "--saida" in args else pasta / "materiais"
    # provas que, pela regra de avaliação da cadeira, cobrem tudo desde o início (ex.: "P2 cobre todas")
    cumul = set(args[args.index("--cumulativa") + 1].split(",")) if "--cumulativa" in args else set()
    linhas = le_cronograma(crono.read_text(encoding="utf-8", errors="replace"))
    for l in linhas:
        l["tipo"] = tipo_linha(l)
    if not linhas:
        print(json.dumps({"erro": "nenhuma linha de cronograma reconhecida"}, ensure_ascii=False))
        sys.exit(1)

    # distribui as aulas entre as provas: tudo até uma prova "regular" (P1, P2, ...) é dela
    provas, atual = [], {"aulas": []}
    for l in linhas:
        if eh_prova(l):
            nome = NOME_PROVA.search(l["descricao"] + " " + l["atividade"]).group(1)
            regular = re.fullmatch(r"P\d", nome) is not None
            if regular:
                atual.update({"nome": nome, "data": l["data"], "local": l["recursos"]})
                if nome in cumul:
                    atual["cumulativa"] = True
                    atual["inclui_provas"] = [p["nome"] for p in provas if re.fullmatch(r"P\d", p["nome"])]
                provas.append(atual)
                atual = {"aulas": []}
            else:
                provas.append({"nome": nome, "data": l["data"], "local": l["recursos"],
                               "aulas": [], "cobre": "todo o conteúdo"})
        else:
            atual["aulas"].append(l)
    sobra = atual["aulas"]

    notas = datas_das_notas(pasta, linhas[0]["ano"])
    sem_data = sorted(n for n, dm in notas.items() if dm is None)
    notas = {n: dm for n, dm in notas.items() if dm is not None}
    por_data = {}
    for nome, dm in notas.items():
        por_data.setdefault(dm, []).append(nome)
    usadas = set()
    for p in provas:
        for a in p["aulas"]:
            a["notas"] = sorted(por_data.get(a["dm"], []))
            usadas.update(a["notas"])
    sem_par = sorted(set(notas) - usadas)

    saida.mkdir(parents=True, exist_ok=True)
    limpa = lambda a: {k: v for k, v in a.items() if k not in ("dm",)}
    dados = {
        "cadeira": pasta.name,
        "fonte": str(crono),
        "provas": [{**p, "aulas": [limpa(a) for a in p["aulas"]]} for p in provas],
        "apos_ultima_prova": [limpa(a) for a in sobra],
        "notas_sem_data_no_cronograma": sem_par,
        "notas_sem_data_no_cabecalho": sem_data,
    }
    (saida / "mapa-provas.json").write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [f"# {pasta.name} — Mapa de Provas", "## Gerado a partir do cronograma do semestre", "---"]
    for p in provas:
        md.append(f"### {p['nome']} — {p['data']}" + (f" ({p['local']})" if p.get("local") else ""))
        if p.get("cobre"):
            md.append(f"- Cobre **{p['cobre']}**.")
            md.append("---")
            continue
        if p.get("cumulativa"):
            md.append(f"- **Cumulativa**: cobre também o conteúdo de {', '.join(p['inclui_provas'])}. "
                      "Abaixo, só o conteúdo novo desde a prova anterior.")
        md.append("| # | Data | Conteúdo | Atividade | Notas |")
        md.append("|---|---|---|---|---|")
        for a in p["aulas"]:
            notas_md = ", ".join(f"[{n[:-3].capitalize()}](../{n})" for n in a["notas"]) or "—"
            desc = a['descricao'] or '—'
            if a["tipo"] == "logistica":
                desc = f"*{desc}*"
            md.append(f"| {a['num'] or ''} | {a['data']} | {desc} | {a['atividade']} | {notas_md} |")
        md.append("---")
    if sem_par or sem_data:
        md.append("### Notas a conferir")
        if sem_par:
            md.append("- Data do cabeçalho não bate com nenhuma aula: " + ", ".join(sem_par))
        if sem_data:
            md.append("- Sem data no cabeçalho (não entraram no mapa): " + ", ".join(sem_data))
    (saida / "mapa-provas.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps({
        "ok": True,
        "provas": [(p["nome"], p["data"], len(p["aulas"])) for p in provas],
        "notas_casadas": len(usadas),
        "notas_sem_par": sem_par,
        "notas_sem_data": sem_data,
        "aulas_de_conteudo_sem_nota": sum(1 for p in provas for a in p["aulas"]
                                          if a["tipo"] == "conteudo" and not a["notas"]),
        "saida": str(saida),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
