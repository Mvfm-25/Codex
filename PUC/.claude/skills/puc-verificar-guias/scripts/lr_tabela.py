#!/usr/bin/env python3
"""First/Follow, estados LR e tabela Action/GoTo — para conferir gabaritos de análise sintática.

Uso:
  python lr_tabela.py <gramatica.txt | -> [--metodo lr0|slr|clr|lalr] [--trace "a b c"] [--ll1]
                      [--ja-aumentada]   (a 1ª produção, S → X, já é a aumentada: não cria S')

Formato da gramática (uma produção ou várias alternativas por linha; a 1ª linha define o
símbolo inicial; símbolos separados por espaço; vazio = ε, eps, ou alternativa em branco):
    L -> A B
    A -> a A | ε
    B -> b B | c
Também aceita "→", "::=", ":" e "=" como seta. Terminal = qualquer símbolo que não aparece à
esquerda. Aspas são removidas ("+" vira +). Linhas começando com # são ignoradas.

Saída (Markdown): produções numeradas (0 = aumentada), First/Follow, estados no formato do
professor ("A → • a A, b/c"), tabela, conflitos e, com --trace, o reconhecimento passo a passo.
A numeração dos estados segue a ordem em que aparecem (BFS, símbolos na ordem dos itens), que é
a mesma usada à mão; se o gabarito numerar diferente, compare pelo conteúdo dos estados.
Com --ll1, verifica a condição LL(1) de cada não-terminal.
"""
import re
import sys
from collections import OrderedDict

EPS = "ε"
FIM = "$"


def le_gramatica(texto):
    prods, inicial = [], None
    for linha in texto.splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        m = re.match(r"^(\S+)\s*(?:->|→|::=|:|=)\s*(.*?)\s*;?\s*$", linha)
        if not m:
            raise SystemExit(f"linha não reconhecida: {linha}")
        esq, dir_ = m.group(1), m.group(2)
        inicial = inicial or esq
        for alt in dir_.split("|"):
            simbs = [s.strip("\"'") for s in alt.split()]
            simbs = [s for s in simbs if s not in (EPS, "eps", "epsilon", "vazio", "λ")]
            prods.append((esq, tuple(simbs)))
    return inicial, prods


class Gramatica:
    def __init__(self, inicial, prods, ja_aumentada=False):
        if ja_aumentada:
            # a 1ª produção (S → X) já é a aumentada; ela vira a produção 0
            self.ini, self.orig = inicial, prods[0][1][0]
            self.prods = list(prods)
        else:
            self.orig = inicial
            self.ini = inicial + "'"
            self.prods = [(self.ini, (inicial,))] + prods
        self.nts = list(OrderedDict.fromkeys(p[0] for p in self.prods))
        simbs = OrderedDict()
        for _, d in self.prods:
            for s in d:
                simbs[s] = 1
        self.ts = [s for s in simbs if s not in self.nts] + [FIM]
        self._first()
        self._follow()

    def _first(self):
        self.first = {n: set() for n in self.nts}
        mudou = True
        while mudou:
            mudou = False
            for a, d in self.prods:
                f = self.first_seq(d)
                if not f <= self.first[a]:
                    self.first[a] |= f
                    mudou = True

    def first_seq(self, seq):
        out = set()
        for s in seq:
            if s not in self.nts:
                out.add(s)
                return out
            out |= self.first[s] - {EPS}
            if EPS not in self.first[s]:
                return out
        out.add(EPS)
        return out

    def _follow(self):
        self.follow = {n: set() for n in self.nts}
        self.follow[self.ini].add(FIM)
        self.follow[self.orig].add(FIM)
        mudou = True
        while mudou:
            mudou = False
            for a, d in self.prods:
                for i, s in enumerate(d):
                    if s not in self.nts:
                        continue
                    f = self.first_seq(d[i + 1:])
                    novo = (f - {EPS}) | (self.follow[a] if EPS in f else set())
                    if not novo <= self.follow[s]:
                        self.follow[s] |= novo
                        mudou = True


def fmt_prod(g, i):
    a, d = g.prods[i]
    return f"{a} → {' '.join(d) if d else EPS}"


def closure(g, itens, lr1):
    itens = list(OrderedDict.fromkeys(itens))
    k = 0
    while k < len(itens):
        p, dot, la = itens[k]
        k += 1
        d = g.prods[p][1]
        if dot < len(d) and d[dot] in g.nts:
            B = d[dot]
            las = [None]
            if lr1:
                f = g.first_seq(d[dot + 1:])
                las = sorted(f - {EPS}) + ([la] if EPS in f else [])
                las = list(OrderedDict.fromkeys(las))
            for q, (esq, _) in enumerate(g.prods):
                if esq == B:
                    for b in las:
                        it = (q, 0, b)
                        if it not in itens:
                            itens.append(it)
    return tuple(itens)


def goto(g, I, X, lr1):
    mov = [(p, dot + 1, la) for p, dot, la in I
           if dot < len(g.prods[p][1]) and g.prods[p][1][dot] == X]
    return closure(g, mov, lr1) if mov else None


def colecao(g, lr1):
    estados = [closure(g, [(0, 0, FIM if lr1 else None)], lr1)]
    trans = {}
    i = 0
    while i < len(estados):
        I = estados[i]
        simbs = OrderedDict()
        for p, dot, _ in I:
            d = g.prods[p][1]
            if dot < len(d):
                simbs[d[dot]] = 1
        for X in simbs:
            J = goto(g, I, X, lr1)
            chave = frozenset(J)
            idx = next((k for k, E in enumerate(estados) if frozenset(E) == chave), None)
            if idx is None:
                estados.append(J)
                idx = len(estados) - 1
            trans[(i, X)] = idx
        i += 1
    return estados, trans


def funde_lalr(estados, trans):
    nucleo = lambda E: frozenset((p, d) for p, d, _ in E)
    grupos, mapa = OrderedDict(), {}
    for i, E in enumerate(estados):
        grupos.setdefault(nucleo(E), []).append(i)
    novos = []
    for k, (_, membros) in enumerate(grupos.items()):
        itens = []
        for m in membros:
            mapa[m] = k
            itens += [it for it in estados[m] if it not in itens]
        novos.append(tuple(itens))
    t2 = {(mapa[i], X): mapa[j] for (i, X), j in trans.items()}
    origem = [membros for membros in grupos.values()]
    return novos, t2, origem


def fmt_estado(g, E):
    agrup = OrderedDict()
    for p, dot, la in E:
        agrup.setdefault((p, dot), []).append(la)
    linhas = []
    for (p, dot), las in agrup.items():
        a, d = g.prods[p]
        corpo = list(d)
        corpo.insert(dot, "•")
        s = f"{a} → {' '.join(corpo)}"
        if las[0] is not None:
            s += ", " + "/".join(las)
        linhas.append(s)
    return linhas


def tabela(g, estados, trans, metodo):
    act = [{t: [] for t in g.ts} for _ in estados]
    gt = [{} for _ in estados]
    for (i, X), j in trans.items():
        if X in g.nts:
            gt[i][X] = j
        else:
            act[i][X].append(f"s{j}")
    for i, E in enumerate(estados):
        for p, dot, la in E:
            d = g.prods[p][1]
            if dot != len(d):
                continue
            if p == 0:
                act[i][FIM].append("acc")
                continue
            if metodo == "lr0":
                cols = g.ts
            elif metodo == "slr":
                cols = [t for t in g.ts if t in g.follow[g.prods[p][0]]]
            else:
                cols = [la]
            for t in cols:
                if f"r{p}" not in act[i][t]:
                    act[i][t].append(f"r{p}")
    conflitos = [(i, t, v) for i, linha in enumerate(act) for t, v in linha.items() if len(v) > 1]
    return act, gt, conflitos


def tipo_conflito(v):
    return "shift/reduce" if any(x.startswith("s") for x in v) else "reduce/reduce"


def trace(g, act, gt, tokens):
    entrada = tokens + [FIM]
    pilha = [0]
    simb = []
    pos = 0
    passos = []
    for _ in range(1000):
        s, a = pilha[-1], entrada[pos]
        pil = " ".join([str(pilha[0])] + [f"{simb[k]} {pilha[k + 1]}" for k in range(len(simb))])
        resto = "".join(entrada[pos:]) if all(len(x) == 1 for x in entrada[pos:]) else " ".join(entrada[pos:])
        if a not in act[s]:
            passos.append((pil, resto, f"**erro**: '{a}' não é terminal da gramática"))
            return passos, False
        v = act[s][a]
        if not v:
            passos.append((pil, resto, f"**erro** (Action[{s}, {a}] vazia)"))
            return passos, False
        acao = v[0]
        nota = f" ⚠ conflito {'/'.join(v)}, usado {acao}" if len(v) > 1 else ""
        if acao == "acc":
            passos.append((pil, resto, "**accept**"))
            return passos, True
        if acao.startswith("s"):
            j = int(acao[1:])
            passos.append((pil, resto, f"s{j}{nota}"))
            pilha.append(j)
            simb.append(a)
            pos += 1
        else:
            p = int(acao[1:])
            esq, d = g.prods[p]
            for _ in d:
                pilha.pop()
                simb.pop()
            j = gt[pilha[-1]].get(esq)
            passos.append((pil, resto, f"r{p} `{fmt_prod(g, p)}` ; goto({pilha[-1]},{esq})={j}{nota}"))
            if j is None:
                return passos, False
            pilha.append(j)
            simb.append(esq)
    return passos, False


def ll1(g):
    out = []
    for n in g.nts[1:]:
        alts = [d for a, d in g.prods[1:] if a == n]
        fs = [g.first_seq(d) for d in alts]
        problemas = []
        for i in range(len(alts)):
            for j in range(i + 1, len(alts)):
                x = (fs[i] & fs[j]) - {EPS}
                if x:
                    problemas.append(f"First({' '.join(alts[i]) or EPS}) ∩ First({' '.join(alts[j]) or EPS}) = {sorted(x)}")
            if EPS in fs[i]:
                for j in range(len(alts)):
                    if j != i:
                        x = (fs[j] - {EPS}) & g.follow[n]
                        if x:
                            problemas.append(f"{' '.join(alts[i]) or EPS} anulável e First({' '.join(alts[j]) or EPS}) ∩ Follow({n}) = {sorted(x)}")
        if any(d and d[0] == n for d in alts):
            problemas.append("recursão à esquerda direta")
        out.append((n, problemas))
    return out


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    fonte = args[0]
    texto = sys.stdin.read() if fonte == "-" else open(fonte, encoding="utf-8").read()
    metodo = args[args.index("--metodo") + 1] if "--metodo" in args else "clr"
    tr = args[args.index("--trace") + 1].split() if "--trace" in args else None
    g = Gramatica(*le_gramatica(texto), ja_aumentada="--ja-aumentada" in args)
    lr1 = metodo in ("clr", "lalr")

    print(f"## Gramática ({metodo.upper()})\n")
    for i in range(len(g.prods)):
        print(f"{i}  {fmt_prod(g, i)}  ")
    print("\n| NT | First | Follow |\n|---|---|---|")
    for n in g.nts[1:]:
        print(f"| {n} | {', '.join(sorted(g.first[n]))} | {', '.join(sorted(g.follow[n]))} |")
    if "--ll1" in args:
        print("\n### LL(1)")
        res = ll1(g)
        for n, probs in res:
            print(f"- {n}: " + ("ok" if not probs else "; ".join(probs)))
        print(f"\n**{'É' if all(not p for _, p in res) else 'NÃO é'} LL(1).**")

    estados, trans = colecao(g, lr1)
    origem = None
    if metodo == "lalr":
        estados, trans, origem = funde_lalr(estados, trans)
    print("\n### Estados\n```")
    for i, E in enumerate(estados):
        extra = f"   (funde CLR {', '.join('I' + str(m) for m in origem[i])})" if origem and len(origem[i]) > 1 else ""
        linhas = fmt_estado(g, E)
        print(f"I{i}:{extra}")
        for l in linhas:
            print(f"    {l}")
    print("```")
    print("\n### Transições\n" + "  ".join(f"goto(I{i},{X})=I{j}" for (i, X), j in trans.items()))

    act, gt, conf = tabela(g, estados, trans, metodo)
    nts = g.nts[1:]
    print("\n### Tabela\n")
    print("| | " + " | ".join(g.ts + nts) + " |")
    print("|---" * (1 + len(g.ts) + len(nts)) + "|")
    for i in range(len(estados)):
        cel = ["/".join(act[i][t]) for t in g.ts] + [str(gt[i].get(n, "")) for n in nts]
        print(f"| {i} | " + " | ".join(cel) + " |")
    print()
    if conf:
        for i, t, v in conf:
            print(f"- ⚠ **conflito {tipo_conflito(v)}** no estado {i}, coluna `{t}`: {' / '.join(v)}")
    else:
        print("Sem conflitos.")

    if tr is not None:
        passos, ok = trace(g, act, gt, tr)
        print(f"\n### Reconhecimento de `{' '.join(tr)}`\n\n| Pilha | Entrada | Ação |\n|---|---|---|")
        for p in passos:
            print(f"| {p[0]} | {p[1]} | {p[2]} |")
        print(f"\n**{'aceita' if ok else 'rejeitada'}**")


if __name__ == "__main__":
    main()
