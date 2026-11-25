#!/usr/bin/env python3
"""Mede quanto do material entregue pelo professor os guias de estudo cobrem.

Uso:  python cobertura.py <pasta_cadeira> [--guias P1.md,P2.md] [--min 0.6] [--detalhe]

Lê <pasta_cadeira>/materiais/.cache/manifest.json (da skill puc-materiais-index) e os guias
materiais/P*.md (ou os indicados). Para cada material (cópias idênticas contam uma vez):
  linkado   — algum guia tem link para o arquivo (ou para uma cópia idêntica);
  tópicos   — "títulos de slide" extraídos do texto (linhas curtas que abrem seção/slide e se
              repetem) e se cada um aparece num MESMO parágrafo de algum guia (≥ --min das
              palavras significativas, sem acento e sem diferenciar maiúsculas);
  exercícios — para listas (manifest com linhas de "Exercício/Questão"), quantos itens numerados
              existem e se o guia tem uma seção que a cita como resolvida ("lista ... resolvida").
Imprime uma tabela e, com --detalhe, os tópicos não cobertos de cada material. Termina com a
cobertura total (tópicos cobertos / tópicos) e a lista do que falta, para guiar a próxima versão.
Materiais de trabalho (trabalhos/) e textos de apoio sem tópicos são listados à parte.
"""
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

PARADAS = set("""a o e de da do das dos em no na nos nas um uma uns umas para por com sem que se como
mais menos ou ao aos à às é ser são foi the of and to in for on with by an is are be this that from
sobre entre seu sua seus suas ele ela eles elas isso esta este essa esse prof escola politécnica pucrs
capitulo capítulo livro understanding cryptography paar pelzl christof segurança sistemas""".split())


def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c))


def palavras(s):
    return [w for w in re.findall(r"[a-z0-9]+", norm(s)) if len(w) >= 3 and w not in PARADAS]


def ruido(t):
    """Linhas que parecem título mas não são tópico: autoria, dados de exemplo, células de tabela."""
    if re.search(r"(?i)\bprof\.?\b|escola polit|pucrs|elaborado a partir|cap[ií]tulo \d|http|www\.", t):
        return True
    sem = t.replace(" ", "")
    if re.fullmatch(r"[A-Z]{12,}", sem) or re.fullmatch(r"[01:C\d]{10,}", sem):   # texto cifrado, binário
        return True
    if re.search(r"[0-9a-f]{16,}", t):                                          # hex
        return True
    if sum(c.isdigit() for c in t) > len(t) * 0.3:                               # tabelas numéricas
        return True
    if len(re.findall(r"\s{2,}", t)) >= 2:                                       # 3+ células de tabela/diagrama
        return True
    return False


def titulos(texto, pptx):
    linhas = [l.strip() for l in texto.splitlines()]
    cand = Counter()
    for i, l in enumerate(linhas):
        if pptx:
            if i > 0 and linhas[i - 1].startswith("--- slide") and 3 < len(l) < 80:
                cand[l] += 1
            continue
        if not (4 <= len(l) <= 70) or l.endswith((".", ",", ";", ":")) or l.startswith(("•", "■", "–", "-", "●", "➔", "o ")):
            continue
        if not re.match(r"[A-ZÁÉÍÓÚÂÊÔÃÕÇ0-9]", l) or len(l.split()) > 9:
            continue
        if re.fullmatch(r"[\d\W]+", l) or len(palavras(l)) < 1:
            continue
        cand[l] += 1
    cand = Counter({t: n for t, n in cand.items() if not ruido(t)})
    # um título de slide em PDF costuma repetir (slides de continuação) ou abrir bloco
    out, vistos = [], set()
    for t, n in cand.most_common():
        chave = " ".join(palavras(t))
        if not chave or chave in vistos:
            continue
        if pptx or n >= 2 or len(palavras(t)) >= 2:
            vistos.add(chave)
            out.append(t)
    return out[:60]


def termos_chave(txt, df, n_docs, k=30):
    """Palavras distintivas do material: repetem nele (≥ 2×) e aparecem em poucos materiais."""
    from collections import Counter as C
    cont = C(w for w in palavras(txt) if len(w) >= 4 and not w.isdigit())
    limite = max(2, n_docs // 6)
    cand = [(n, w) for w, n in cont.items() if n >= 2 and df.get(w, 0) <= limite]
    return [w for _, w in sorted(cand, reverse=True)[:k]]


def paragrafos(md):
    md = re.sub(r"(?s)<details>.*?</details>", lambda m: m.group(0), md)
    blocos = re.split(r"\n\s*\n|\n(?=#)|\n(?=- )|\n(?=\t- )|\n(?=\|)", md)
    return [set(palavras(b)) for b in blocos if b.strip()]


def coberto(t, pars, minimo):
    ws = set(palavras(t))
    if not ws:
        return True
    return any(len(ws & p) / len(ws) >= minimo for p in pars)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(2)
    pasta = Path(a[0]).resolve()
    minimo = float(a[a.index("--min") + 1]) if "--min" in a else 0.6
    mat = pasta / "materiais"
    manifest = json.loads((mat / ".cache" / "manifest.json").read_text(encoding="utf-8"))
    nomes = a[a.index("--guias") + 1].split(",") if "--guias" in a else [p.name for p in sorted(mat.glob("P*.md"))] + \
        [p.name for p in sorted(mat.glob("PS*.md"))]
    guias = {n: (mat / n).read_text(encoding="utf-8") for n in nomes if (mat / n).exists()}
    if not guias:
        print("nenhum guia encontrado em", mat)
        sys.exit(1)
    pars = [p for g in guias.values() for p in paragrafos(g)]
    links = set()
    for g in guias.values():
        # <alvo com espaços e (parênteses)> ou alvo simples
        for ang, simples in re.findall(r"\]\(<([^>]+)>\)|\]\(([^)\s]+)\)", g):
            alvo = ang or simples
            links.add(norm(unicodedata.normalize("NFC", alvo.replace("../", "").split("#")[0])))

    grupos = {}
    for k, v in manifest.items():
        grupos.setdefault(v.get("sha1") or k, []).append(k)
    # frequência de documento de cada palavra (para achar termos distintivos)
    textos = {}
    for sha, ks in grupos.items():
        k0 = sorted(ks)[0]
        textos[sha] = (pasta / manifest[k0]["cache"]).read_text(encoding="utf-8")
    df = Counter()
    for t in textos.values():
        df.update(set(palavras(t)))
    vocab_guias = set(w for g in guias.values() for w in palavras(g))
    total_k = total_kc = 0

    total_t = total_c = 0
    linhas, falta, apoio = [], [], []
    for sha, ks in sorted(grupos.items(), key=lambda kv: kv[1][0]):
        k = sorted(ks, key=lambda x: (not x.startswith("atividades"), x))[0]
        v = manifest[k]
        txt = (pasta / v["cache"]).read_text(encoding="utf-8")
        lk = any(norm(unicodedata.normalize("NFC", x)) in links for x in ks)
        ts = titulos(txt, k.endswith(".pptx"))
        if k.startswith("trabalhos/") or not ts:
            apoio.append((k, lk))
            continue
        cob = [t for t in ts if coberto(t, pars, minimo)]
        nao = [t for t in ts if t not in cob]
        total_t += len(ts)
        total_c += len(cob)
        n_ex = len(set(re.findall(r"(?im)^\s*(?:exerc[ií]cio|quest[aã]o)\s*\d+", txt)))
        kws = termos_chave(txt, df, len(textos))
        kc = [w for w in kws if w in vocab_guias]
        total_k += len(kws)
        total_kc += len(kc)
        linhas.append((k, lk, len(cob), len(ts), n_ex, len(kc), len(kws)))
        if nao or len(kc) < len(kws):
            falta.append((k, nao, [w for w in kws if w not in vocab_guias]))

    print(f"Guias: {', '.join(guias)}   (parágrafo cobre um tópico com ≥ {int(minimo * 100)}% das palavras)\n")
    print("| Material | Linkado | Tópicos (títulos) | Termos-chave | Exercícios numerados |")
    print("|---|---|---|---|---|")
    for k, lk, c, t, ne, kc, kt in linhas:
        print(f"| {k} | {'✔' if lk else '✘'} | {c}/{t} ({100 * c // t}%) | {kc}/{kt} ({100 * kc // max(kt, 1)}%) | {ne or ''} |")
    if apoio:
        print("\nTrabalhos / textos de apoio (sem tópicos medidos): "
              + "; ".join(f"{k} {'✔' if lk else '✘'}" for k, lk in apoio))
    pct = 100 * total_c // max(total_t, 1)
    nao_link = [k for k, lk, *_ in linhas if not lk] + [k for k, lk in apoio if not lk]
    pk = 100 * total_kc // max(total_k, 1)
    print(f"\n**Cobertura de tópicos (títulos): {total_c}/{total_t} ({pct}%)** · "
          f"**termos-chave: {total_kc}/{total_k} ({pk}%)** · materiais não linkados: {len(nao_link)}")
    print("Títulos medem se os assuntos dos slides aparecem; termos-chave medem se o vocabulário técnico\n"
          "distintivo de cada material está no guia. Títulos de seção muito específicos (\"3.1 Localização do\n"
          "Arsenal Nativo\") e provas (\"Questão 1\") puxam a 1ª métrica para baixo — confira o --detalhe.")
    if "--detalhe" in a:
        for k, nao, kn in falta:
            print(f"\n- {k}" + (f"\n    títulos ({len(nao)}): " + " · ".join(nao[:20]) if nao else "")
                  + (f"\n    termos ausentes: " + ", ".join(kn) if kn else ""))
    if nao_link:
        print("\nNão linkados: " + "; ".join(nao_link))


if __name__ == "__main__":
    main()
