import sys
def album(n, metas=(0.50, 0.75, 0.95)):
    p = [0.0]*(n+1); p[0] = 1.0
    res = []; k = 0; i = 0
    while i < len(metas):
        k += 1
        for j in range(n, 0, -1):
            p[j] = p[j]*(j/n) + p[j-1]*((n-j+1)/n)
        p[0] = 0.0
        while i < len(metas) and p[n] > metas[i]:
            res.append(k); i += 1
    return res

n = int(sys.argv[1])
for m, k in zip((50, 75, 95), album(n)):
    print(f"{m}% : {k} figurinhas")
