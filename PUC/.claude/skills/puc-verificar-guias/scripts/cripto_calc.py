#!/usr/bin/env python3
"""Calculadora para conferir gabaritos de Segurança de Sistemas (criptografia).

Uso:  python cripto_calc.py <comando> [args]

  mdc A B                 MDC por Euclides estendido, com a tabela dos passos e a, b tais que A·a + B·b = mdc
  inv X N                 inverso de X em Z_N (ou "não existe"), com os passos de Euclides
  pot B E N               B^E mod N por quadrados sucessivos (mostra a redução por Fermat/Euler quando cabe)
  phi N                   φ(N) e a fatoração de N
  zn N                    Z*_N (invertíveis) e a tabela de inversos
  ger P                   geradores de Z*_P (P primo) e a ordem de cada elemento
  dh P G A B              Diffie-Hellman: A = G^a, B = G^b, K (confere se G é gerador)
  rsa P Q E [M]           chaves RSA (N, φ, d = E⁻¹ mod φ) e, com M, C = M^E e M = C^d
  assina H D N  E         assinatura RSA s = H^D mod N e verificação s^E mod N == H
  ec A B P X Y [K]        curva y² = x³ + A·x + B (mod P), ponto (X,Y): ciclo k·P até O;
                          com K, calcula K·P por double-and-add (tabela bit a bit)
  ecdh A B P X Y a b      ECDH: aP, bP, a(bP), b(aP)
  badhash BYTES...        badHash da Candycoin (XOR de todos os bytes com 01010101); bytes em binário/hex/dec
  xor X Y ...             XOR byte a byte (mesmo formato), útil para OTP com chave reutilizada

Inteiros pequenos, como nas provas; tudo é exato (sem ponto flutuante).
"""
import sys
from math import gcd


def euclides(a, b):
    """Euclides estendido com os passos: devolve (g, x, y, passos) com a·x + b·y = g."""
    passos = []
    r0, r1, s0, s1, t0, t1 = a, b, 1, 0, 0, 1
    while r1:
        q = r0 // r1
        passos.append((r0, r1, q, r0 - q * r1))
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return r0, s0, t0, passos


def inv(x, n):
    g, s, _, _ = euclides(x % n, n)
    return s % n if g == 1 else None


def fatora(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def phi(n):
    r = n
    for p in fatora(n):
        r = r // p * (p - 1)
    return r


def ordem(x, p):
    k, v = 1, x % p
    while v != 1:
        v = v * x % p
        k += 1
        if k > p:
            return None
    return k


def num(s):
    s = s.strip().replace(" ", "")
    if s.startswith(("0x", "0X")):
        return int(s, 16)
    if set(s) <= {"0", "1"} and len(s) >= 4:
        return int(s, 2)
    return int(s)


# ---------- AES-128 (FIPS-197), puro Python — para os exercícios de "use o AES online" ----------
def _xt(a):
    return ((a << 1) ^ 0x1B) & 0xFF if a & 0x80 else a << 1


def _sbox():
    s, inv_ = [0] * 256, [0] * 256
    p = q = 1
    while True:                                   # gera a S-box pelo inverso em GF(2^8) + afim
        p = p ^ ((p << 1) & 0xFF) ^ (0x1B if p & 0x80 else 0)
        q ^= q << 1; q ^= q << 2; q ^= q << 4; q &= 0xFF
        if q & 0x80:
            q ^= 0x09
        x = q ^ (q << 1 | q >> 7) ^ (q << 2 | q >> 6) ^ (q << 3 | q >> 5) ^ (q << 4 | q >> 4)
        s[p] = (x ^ 0x63) & 0xFF
        if p == 1:
            break
    s[0] = 0x63
    for i, v in enumerate(s):
        inv_[v] = i
    return s, inv_


SBOX, INV_SBOX = _sbox()


def _expande(chave):
    w = [list(chave[i:i + 4]) for i in range(0, 16, 4)]
    rcon = 1
    for i in range(4, 44):
        t = list(w[i - 1])
        if i % 4 == 0:
            t = [SBOX[b] for b in t[1:] + t[:1]]
            t[0] ^= rcon
            rcon = _xt(rcon)
        w.append([a ^ b for a, b in zip(w[i - 4], t)])
    return [sum(w[4 * r:4 * r + 4], []) for r in range(11)]


def _mix(c):
    a = c
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    return [a[i] ^ t ^ _xt(a[i] ^ a[(i + 1) % 4]) for i in range(4)]


def aes_cifra(chave, bloco):
    k = _expande(chave)
    s = [b ^ k[0][i] for i, b in enumerate(bloco)]
    for r in range(1, 11):
        s = [SBOX[b] for b in s]
        s = [s[(i + 4 * (i % 4)) % 16] for i in range(16)]            # ShiftRows (coluna-major)
        if r < 10:
            s = sum((_mix(s[4 * c:4 * c + 4]) for c in range(4)), [])
        s = [b ^ k[r][i] for i, b in enumerate(s)]
    return bytes(s)


def aes_decifra(chave, bloco):
    k = _expande(chave)
    s = [b ^ k[10][i] for i, b in enumerate(bloco)]
    for r in range(9, -1, -1):
        s = [s[(i - 4 * (i % 4)) % 16] for i in range(16)]            # InvShiftRows
        s = [INV_SBOX[b] for b in s]
        s = [b ^ k[r][i] for i, b in enumerate(s)]
        if r > 0:                                                     # InvMixColumns = Mix³
            for _ in range(3):
                s = sum((_mix(s[4 * c:4 * c + 4]) for c in range(4)), [])
    return bytes(s)


# ---------- chaves RSA em PEM (PKCS#1 privada / SPKI pública) ----------
def _der_ints(b):
    """Percorre o DER e devolve todos os INTEGER, na ordem (basta para chaves RSA)."""
    out, i = [], 0

    def tam(j):
        n = b[j]
        if n < 0x80:
            return n, j + 1
        k = n & 0x7F
        return int.from_bytes(b[j + 1:j + 1 + k], "big"), j + 1 + k

    while i < len(b):
        tag = b[i]
        n, j = tam(i + 1)
        if tag == 0x02:
            out.append(int.from_bytes(b[j:j + n], "big"))
            i = j + n
        elif tag in (0x30, 0x03, 0x04):          # SEQUENCE / BIT STRING / OCTET STRING: entra
            i = j + (1 if tag == 0x03 else 0)
        else:
            i = j + n
    return out


def le_pem(caminho):
    import base64
    txt = open(caminho, encoding="utf-8").read()
    corpo = "".join(l for l in txt.splitlines() if l and not l.startswith("-----"))
    ints = _der_ints(base64.b64decode(corpo))
    if "PRIVATE" in txt:                          # version, n, e, d, p, q, ...
        return {"n": ints[1], "e": ints[2], "d": ints[3]}
    return {"n": ints[0], "e": ints[1]}


# ---------- curvas elípticas ----------
O = None


def ec_soma(Pt, Qt, a, p):
    if Pt is O:
        return Qt
    if Qt is O:
        return Pt
    (x1, y1), (x2, y2) = Pt, Qt
    if x1 == x2 and (y1 + y2) % p == 0:
        return O
    if Pt == Qt:
        s = (3 * x1 * x1 + a) * inv(2 * y1, p) % p
    else:
        s = (y2 - y1) * inv(x2 - x1, p) % p
    x3 = (s * s - x1 - x2) % p
    return (x3, (s * (x1 - x3) - y1) % p)


def ec_mul(k, Pt, a, p, rastro=None):
    R = O
    for i, bit in enumerate(bin(k)[2:]):
        if i == 0:
            R = Pt
            if rastro is not None:
                rastro.append((bit, "inicialização", R))
            continue
        R = ec_soma(R, R, a, p)
        op = "dobra"
        if bit == "1":
            R = ec_soma(R, Pt, a, p)
            op = "dobra + soma P"
        if rastro is not None:
            rastro.append((bit, op, R))
    return R


def fmt(Pt):
    return "O" if Pt is O else f"({Pt[0]}, {Pt[1]})"


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(2)
    c, v = a[0], a[1:]
    if c == "mdc":
        A, B = int(v[0]), int(v[1])
        g, x, y, passos = euclides(A, B)
        for r0, r1, q, r in passos:
            print(f"{r0} = {q}·{r1} + {r}")
        print(f"mdc({A}, {B}) = {g}   ({A}·{x} + {B}·{y} = {g})   {'coprimos' if g == 1 else 'não coprimos'}")
    elif c == "inv":
        X, N = int(v[0]), int(v[1])
        g, s, _, passos = euclides(X % N, N)
        for r0, r1, q, r in passos:
            print(f"{r0} = {q}·{r1} + {r}")
        print(f"inverso de {X} em Z_{N}: {s % N}   ({X}·{s % N} = {X * (s % N)} ≡ 1)" if g == 1
              else f"{X} não tem inverso em Z_{N} (mdc = {g})")
    elif c == "pot":
        B, E, N = map(int, v[:3])
        f = phi(N)
        if gcd(B, N) == 1 and E >= f:
            print(f"Euler/Fermat: φ({N}) = {f} → {B}^{E} = {B}^({E} mod {f}) = {B}^{E % f} em Z_{N}")
        print(f"{B}^{E} mod {N} = {pow(B, E, N)}")
    elif c == "phi":
        N = int(v[0])
        print(f"{N} = " + " · ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in fatora(N).items())
              + f"   φ({N}) = {phi(N)}")
    elif c == "zn":
        N = int(v[0])
        els = [x for x in range(1, N) if gcd(x, N) == 1]
        print(f"Z*_{N} = {{{', '.join(map(str, els))}}}  (|Z*| = φ = {len(els)})")
        print("inversos: " + ", ".join(f"{x}⁻¹={inv(x, N)}" for x in els))
        sem = [x for x in range(1, N) if gcd(x, N) != 1]
        if sem:
            print("sem inverso: " + ", ".join(map(str, sem)))
    elif c == "ger":
        P = int(v[0])
        ords = {x: ordem(x, P) for x in range(1, P) if gcd(x, P) == 1}
        n = len(ords)
        print("ordens: " + ", ".join(f"{x}:{o}" for x, o in ords.items()))
        print(f"geradores de Z*_{P}: {[x for x, o in ords.items() if o == n]}")
    elif c == "dh":
        P, G, A_, B_ = map(int, v[:4])
        o = ordem(G, P)
        print(f"ordem de g={G} em Z*_{P}: {o} ({'gerador' if o == phi(P) else 'NÃO é gerador'})")
        A, B = pow(G, A_, P), pow(G, B_, P)
        print(f"A = {G}^{A_} mod {P} = {A}   B = {G}^{B_} mod {P} = {B}")
        print(f"K = B^a = {B}^{A_} mod {P} = {pow(B, A_, P)}   K = A^b = {A}^{B_} mod {P} = {pow(A, B_, P)}")
    elif c == "rsa":
        P, Q, E = map(int, v[:3])
        N, f = P * Q, (P - 1) * (Q - 1)
        d = inv(E, f)
        print(f"N = {P}·{Q} = {N}   φ(N) = {P - 1}·{Q - 1} = {f}   mdc(e={E}, φ) = {gcd(E, f)}")
        if d is None:
            print("e não é inversível mod φ(N): escolha outro e")
            return
        print(f"d = e⁻¹ mod φ = {d}   (e·d = {E * d} = {E * d // f}·{f} + 1)")
        print(f"pública (e, N) = ({E}, {N})   privada (d, N) = ({d}, {N})")
        if len(v) > 3:
            M = num(v[3])
            C = pow(M, E, N)
            print(f"M = {M}: C = M^e mod N = {C}   decifra C^d mod N = {pow(C, d, N)}")
    elif c == "assina":
        H, D, N, E = map(int, v[:4])
        s = pow(H, D, N)
        print(f"s = H^d mod N = {H}^{D} mod {N} = {s}   verificação s^e mod N = {pow(s, E, N)} "
              f"({'confere' if pow(s, E, N) == H % N else 'NÃO confere'})")
    elif c in ("ec", "ecdh"):
        A, B, P, X, Y = map(int, v[:5])
        Pt = (X, Y)
        disc = (4 * A ** 3 + 27 * B ** 2) % P
        if (Y * Y - X ** 3 - A * X - B) % P:
            print(f"aviso: ({X},{Y}) não está na curva")
        print(f"E: y² = x³ + {A}x + {B} mod {P}   (4a³+27b² mod p = {disc}{'  ← singular!' if disc == 0 else ''})")
        if c == "ec":
            R, k = Pt, 1
            ciclo = []
            while R is not O:
                ciclo.append(f"{k}P = {fmt(R)}")
                R = ec_soma(R, Pt, A, P)
                k += 1
            ciclo.append(f"{k}P = O")
            print("  ".join(ciclo))
            print(f"ordem de P: {k}")
            if len(v) > 5:
                K = int(v[5])
                r = []
                Q = ec_mul(K, Pt, A, P, r)
                print(f"\n{K} = {bin(K)[2:]}₂ — double-and-add (esquerda → direita):")
                for bit, op, R in r:
                    print(f"  bit {bit}: {op:<15} → {fmt(R)}")
                print(f"{K}P = {fmt(Q)}   (= {K % k}P, pois a ordem é {k})")
        else:
            a_, b_ = int(v[5]), int(v[6])
            Ap, Bp = ec_mul(a_, Pt, A, P), ec_mul(b_, Pt, A, P)
            print(f"A = {a_}P = {fmt(Ap)}   B = {b_}P = {fmt(Bp)}")
            print(f"K_A = a·B = {fmt(ec_mul(a_, Bp, A, P))}   K_B = b·A = {fmt(ec_mul(b_, Ap, A, P))}")
    elif c == "badhash":
        bs = [num(x) for x in v]
        h = 0b01010101
        print(f"início: 01010101")
        for b in bs:
            h ^= b
            print(f"⊕ {b:08b} → {h:08b}")
        print(f"badHash = {h:08b} (0x{h:02X})")
    elif c == "aes":                      # aes cifra|decifra CHAVEHEX BLOCOHEX
        k, b = bytes.fromhex(v[1]), bytes.fromhex(v[2])
        f = aes_cifra if v[0].startswith("c") else aes_decifra
        print(f(k, b).hex())
    elif c == "md":                       # md IVHEX M1HEX M2HEX ... (Davies-Meyer: H = E(M, H) ⊕ H)
        H = bytes.fromhex(v[0])
        print(f"H0 = {H.hex()}")
        for i, m in enumerate(v[1:], 1):
            e = aes_cifra(bytes.fromhex(m), H)
            Hn = bytes(x ^ y for x, y in zip(e, H))
            print(f"H{i} = E(M{i}, H{i - 1}) ⊕ H{i - 1} = {e.hex()} ⊕ {H.hex()} = {Hn.hex()}")
            H = Hn
    elif c == "merkle":                   # merkle CIFRADO_BASE64 [prefixo_chave_hex]: testa os 256 últimos bytes
        import base64
        ct = base64.b64decode(v[0])
        pre = v[1] if len(v) > 1 else "00" * 15
        for x in range(256):
            k = bytes.fromhex(pre + f"{x:02x}")
            pt = b"".join(aes_decifra(k, ct[i:i + 16]) for i in range(0, len(ct), 16))
            n = pt[-1]
            if 1 <= n <= 16 and pt.endswith(bytes([n]) * n):
                txt = pt[:-n]
                if all(32 <= ch < 127 for ch in txt):
                    print(f"chave …{x:02x}: {txt.decode()}   (padding PKCS7 de {n} byte(s))")
    elif c == "rsa-pem":                  # rsa-pem CHAVE.pem HEX_OU_ARQUIVO [mensagem]
        import hashlib
        import os
        k = le_pem(v[0])
        bruto = open(v[1]).read().strip() if os.path.exists(v[1]) else v[1]
        x = int(bruto, 16)
        expo = k.get("d", k["e"])                 # privada: decifra; pública: "verifica"
        m = pow(x, expo, k["n"]).to_bytes((k["n"].bit_length() + 7) // 8, "big")
        print(f"chave de {k['n'].bit_length()} bits; bloco após a exponenciação: {m[:2].hex()}…")
        if m[:2] in (b"\x00\x02", b"\x00\x01"):
            corpo = m[m.index(b"\x00", 2) + 1:]   # remove o padding PKCS#1 v1.5
            print(f"conteúdo ({'tipo 2, cifragem' if m[1] == 2 else 'tipo 1, assinatura'}): {corpo!r}")
        else:
            corpo = m
            print("sem padding PKCS#1 reconhecível")
        if len(v) > 2:
            h = hashlib.sha256(v[2].encode("utf-8")).hexdigest()
            print(f"SHA-256('{v[2]}') = {h}")
            ok = h.encode() in corpo or bytes.fromhex(h) in corpo
            print("→ a etiqueta CONFERE com a mensagem" if ok else "→ a etiqueta NÃO confere com a mensagem")
    elif c == "xor":
        bs = [num(x) for x in v]
        r = 0
        for b in bs:
            r ^= b
        print(" ⊕ ".join(f"{b:08b}" for b in bs) + f" = {r:08b} (0x{r:02X})")
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
