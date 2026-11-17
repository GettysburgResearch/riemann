"""SKEPTIC independent brute-force point counts for C5-E2 (own F_{p^r} arithmetic; no shared code).
Curve y^2 = f(x), deg f odd => one point at infinity on the smooth model (when f squarefree)."""
import itertools, json, sys

def find_irred(p, r):
    # monic degree-r polynomial over F_p with no roots in F_{p^k}, k<=r/2: brute force via
    # checking it has no factor of degree <= r//2 (trial division by all monic polys)
    def polymod(a, b):
        a = a[:]
        while len(a) >= len(b):
            c = a[-1] * pow(b[-1], -1, p) % p
            sh = len(a) - len(b)
            for i in range(len(b)):
                a[sh + i] = (a[sh + i] - c * b[i]) % p
            while a and a[-1] == 0: a.pop()
        return a
    for coeffs in itertools.product(range(p), repeat=r):
        f = list(coeffs) + [1]
        if f[0] == 0: continue
        ok = True
        for d in range(1, r // 2 + 1):
            for cc in itertools.product(range(p), repeat=d):
                g = list(cc) + [1]
                if not polymod(f, g):
                    ok = False; break
            if not ok: break
        if ok: return f
    raise ValueError

def field(p, r):
    m = find_irred(p, r) if r > 1 else [0, 1]
    Q = p ** r
    def enc(v): return sum(c * p ** i for i, c in enumerate(v))
    def dec(n): return [(n // p ** i) % p for i in range(r)]
    def mul(a, b):
        A, B = dec(a), dec(b)
        prod = [0] * (2 * r - 1)
        for i, x in enumerate(A):
            if x:
                for j, y in enumerate(B):
                    prod[i + j] = (prod[i + j] + x * y) % p
        for k in range(2 * r - 2, r - 1, -1):
            c = prod[k]
            if c:
                prod[k] = 0
                for i in range(r):
                    prod[k - r + i] = (prod[k - r + i] - c * m[i]) % p
        return enc(prod[:r])
    def add(a, b):
        A, B = dec(a), dec(b)
        return enc([(x + y) % p for x, y in zip(A, B)])
    return Q, mul, add

def count(fcoef, p, r):
    Q, mul, add = field(p, r)
    sq = {}
    for y in range(Q):
        v = mul(y, y); sq[v] = sq.get(v, 0) + 1
    tot = 0
    for x in range(Q):
        v = 0
        for c in reversed(fcoef):  # Horner, fcoef ascending ints mod p (embedded as constants)
            v = add(mul(v, x), c % p)
        tot += sq.get(v, 0)
    return tot + 1

curves = [((1, 1, 0, 1), 5, 4), ((3, 2, 0, 1), 7, 4), ((1, -1, 0, 0, 0, 1), 3, 5),
          ((1, 0, 2, 0, 0, 1), 5, 4), ((2, 1, 0, 0, 0, 0, 0, 1), 3, 5), ((1, 1, 0, 0, 0, 1), 3, 5)]
out = []
for f, p, R in curves:
    Ns = [count(f, p, r) for r in range(1, R + 1)]
    print(f, p, Ns, flush=True)
    out.append(dict(f_asc=f, p=p, N=Ns))
json.dump(out, open(sys.argv[1], 'w'), indent=1)
