#!/usr/bin/env python3
"""Simulador da máquina de pilha da disciplina de Compiladores (Prof. Agustini / MiniP).

Uso:
  python maquina_pilha.py <prog.pil | -> [--var a=5 b=2 ...] [--in 3 7 ...] [-t]

Aceita programas completos ou trechos de gabarito:
  - rótulos de código "R001:" / "_start:" (com ou sem NOP na mesma linha);
  - dados "_a  DS 4" / "_k  DC 10" (endereços em bytes a partir de 500, palavras de 4 bytes);
  - comentários com ";" ; várias instruções na mesma linha ("LDA _i  LDC 1  ADD" ou "LDA _i · LDC 1");
  - rótulos de dados usados sem DS (ex.: "LDA _a" num trecho) são alocados automaticamente (aviso).
  --var inicializa variáveis globais (a=5 ou _a=5); --in fornece a entrada do IN.
  -t imprime o rastreamento: instrução, pilha e BP após cada passo (como o MaquinaPilha.java -t).

Semântica (slides "Geração de Código" + tabela da P3): operações binárias desempilham RT1 (topo)
e RT2 e empilham RT2 op RT1; booleanos 0/1; JSR empilha o endereço de retorno; PUSHBP/SETBP/
POPBP encadeiam quadros; LDO/STO N acessam BP+N; AMEM/DMEM N alocam/liberam N palavras.
Termina em HALT/STOP ou ao passar da última instrução. Imprime saída, memória e altura máxima.
"""
import re
import sys

COM_ARG = {"LDC", "LDA", "STA", "JMP", "JZER", "JPOS", "JNEG", "JSR", "AMEM", "DMEM", "LDO", "STO",
           "DS", "DC"}
SEM_ARG = {"LDI", "STI", "ADD", "SUB", "MUL", "DIV", "MOD", "GRT", "LES", "EQ", "GREQ", "LEEQ",
           "DIF", "AND", "OR", "NOT", "NEG", "INCR", "DECR", "NOP", "HALT", "STOP", "RTS",
           "PUSHBP", "SETBP", "POPBP", "DUP", "DROP", "OUT", "IN", "OUTS"}
MNEM = COM_ARG | SEM_ARG
BASE_DADOS = 500


def monta(texto):
    codigo, rot_cod, dados, avisos = [], {}, {}, []
    prox_dado = BASE_DADOS
    for n_linha, linha in enumerate(texto.splitlines(), 1):
        linha = linha.split(";")[0].replace("·", " ").strip()
        if not linha or linha.startswith("#"):
            continue
        toks = linha.split()
        # dado: "_a DS 4"
        if len(toks) >= 3 and toks[0].upper() not in MNEM and toks[1].upper() in ("DS", "DC"):
            nome, op, val = toks[0].rstrip(":"), toks[1].upper(), int(toks[2])
            dados[nome] = {"end": prox_dado, "ini": val if op == "DC" else 0}
            prox_dado += val if op == "DS" else 4
            continue
        i = 0
        while i < len(toks):
            t = toks[i]
            if t.endswith(":"):
                rot_cod[t[:-1]] = len(codigo)
                i += 1
                continue
            op = t.upper()
            if op not in MNEM:
                raise SystemExit(f"linha {n_linha}: instrução desconhecida '{t}'")
            arg = None
            if op in COM_ARG:
                if i + 1 >= len(toks):
                    raise SystemExit(f"linha {n_linha}: {op} sem argumento")
                arg = toks[i + 1]
                i += 1
            codigo.append((op, arg, n_linha))
            i += 1
    # rótulos de dados usados mas não declarados
    for op, arg, _ in codigo:
        if arg and not re.fullmatch(r"-?\d+", arg) and arg not in rot_cod and arg not in dados:
            if op in ("LDA", "STA", "LDC"):
                dados[arg] = {"end": prox_dado, "ini": 0}
                prox_dado += 4
                avisos.append(f"'{arg}' sem DS: alocado em @{dados[arg]['end']}")
    return codigo, rot_cod, dados, avisos


def valor(arg, rot_cod, dados):
    if re.fullmatch(r"-?\d+", arg):
        return int(arg)
    if arg in dados:
        return dados[arg]["end"]
    if arg in rot_cod:
        return rot_cod[arg]
    raise SystemExit(f"rótulo '{arg}' indefinido")


def executa(codigo, rot_cod, dados, entrada, rastro, limite=200000):
    mem = {d["end"]: d["ini"] for d in dados.values()}
    pilha, bp, pc, saida, alt_max, passos = [], 0, 0, [], 0, 0
    pop = lambda: pilha.pop()
    while 0 <= pc < len(codigo):
        passos += 1
        if passos > limite:
            raise SystemExit("limite de passos excedido (laço infinito?)")
        op, arg, _ = codigo[pc]
        v = valor(arg, rot_cod, dados) if arg is not None and op not in ("DS", "DC") else None
        prox = pc + 1
        if op == "LDC":
            pilha.append(v)
        elif op == "LDA":
            pilha.append(mem.get(v, 0))
        elif op == "STA":
            mem[v] = pop()
        elif op == "LDI":
            pilha.append(mem.get(pop(), 0))
        elif op == "STI":
            rt1 = pop(); rt2 = pop(); mem[rt2] = rt1
        elif op in ("ADD", "SUB", "MUL", "DIV", "MOD", "GRT", "LES", "EQ", "GREQ", "LEEQ", "DIF", "AND", "OR"):
            rt1 = pop(); rt2 = pop()
            r = {"ADD": lambda: rt2 + rt1, "SUB": lambda: rt2 - rt1, "MUL": lambda: rt2 * rt1,
                 "DIV": lambda: int(rt2 / rt1), "MOD": lambda: rt2 - int(rt2 / rt1) * rt1,
                 "GRT": lambda: int(rt2 > rt1), "LES": lambda: int(rt2 < rt1), "EQ": lambda: int(rt2 == rt1),
                 "GREQ": lambda: int(rt2 >= rt1), "LEEQ": lambda: int(rt2 <= rt1), "DIF": lambda: int(rt2 != rt1),
                 "AND": lambda: int(rt1 != 0 and rt2 != 0), "OR": lambda: int(rt1 != 0 or rt2 != 0)}[op]()
            pilha.append(r)
        elif op == "NOT":
            pilha.append(int(pop() == 0))
        elif op == "NEG":
            pilha.append(-pop())
        elif op == "INCR":
            pilha.append(pop() + 1)
        elif op == "DECR":
            pilha.append(pop() - 1)
        elif op == "DUP":
            pilha.append(pilha[-1])
        elif op == "DROP":
            pop()
        elif op == "OUT":
            saida.append(pop())
        elif op == "IN":
            if not entrada:
                raise SystemExit("IN sem entrada (use --in)")
            pilha.append(entrada.pop(0))
        elif op == "JMP":
            prox = v
        elif op == "JZER":
            if pop() == 0:
                prox = v
        elif op == "JPOS":
            if pop() > 0:
                prox = v
        elif op == "JNEG":
            if pop() < 0:
                prox = v
        elif op == "JSR":
            pilha.append(pc + 1); prox = v
        elif op == "RTS":
            prox = pop()
        elif op == "AMEM":
            pilha.extend([0] * v)
        elif op == "DMEM":
            for _ in range(v):
                pop()
        elif op == "PUSHBP":
            pilha.append(bp)
        elif op == "SETBP":
            bp = len(pilha) - 1
        elif op == "POPBP":
            bp = pop()
        elif op == "LDO":
            pilha.append(pilha[bp + v])
        elif op == "STO":
            pilha[bp + v] = pop()
        elif op in ("HALT", "STOP"):
            alt_max = max(alt_max, len(pilha))
            if rastro:
                print(f"{op:<7}{'':<8} pilha:[ {' '.join(map(str, pilha))} ]  BP={bp}")
            break
        alt_max = max(alt_max, len(pilha))
        if rastro:
            print(f"{op:<7}{(arg or ''):<8} pilha:[ {' '.join(map(str, pilha))} ]  BP={bp}")
        pc = prox
    return mem, pilha, saida, alt_max, passos


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    texto = sys.stdin.read() if args[0] == "-" else open(args[0], encoding="utf-8").read()
    codigo, rot_cod, dados, avisos = monta(texto)

    def lista(flag):
        if flag not in args:
            return []
        out = []
        for a in args[args.index(flag) + 1:]:
            if a.startswith("-") and not re.fullmatch(r"-\d+", a):
                break
            out.append(a)
        return out

    for par in lista("--var"):
        nome, val = par.split("=")
        nome = nome if nome.startswith("_") else "_" + nome
        if nome not in dados:
            dados[nome] = {"end": max([d["end"] for d in dados.values()] + [BASE_DADOS - 4]) + 4, "ini": 0}
        dados[nome]["ini"] = int(val)
    entrada = [int(x) for x in lista("--in")]
    for a in avisos:
        print(f"aviso: {a}")
    mem, pilha, saida, alt, passos = executa(codigo, rot_cod, dados, entrada, "-t" in args)
    print(f"saída (OUT): {saida if saida else '—'}")
    print(f"pilha final: [ {' '.join(map(str, pilha))} ]   altura máxima: {alt}   passos: {passos}")
    print("memória:")
    for nome, d in sorted(dados.items(), key=lambda x: x[1]["end"]):
        print(f"   {nome:<8} @{d['end']} = {mem.get(d['end'], 0)}")


if __name__ == "__main__":
    main()
