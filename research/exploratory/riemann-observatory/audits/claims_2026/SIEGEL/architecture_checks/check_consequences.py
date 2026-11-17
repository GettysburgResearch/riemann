"""Numerical sanity checks of consequences (our own code; nothing from the source repositories).

(1) Guo Prop. 3.1 (unconditional): S_-(x,chi) <= (11/20) log x + (29/60) log q + 6, tested for every
    fundamental discriminant |D| <= DMAX at every prime x <= XMAX; also the Barreto/van Dijk shape
    S_- - (1/2)log x - (1/4)log q - loglog(3x) is tabulated (should stay O(1)).
(2) L(1,chi) log q and class numbers for small |D|, versus the auditor-derived effective consequence
    of Guo's Theorem 1.1 (c=1/100):  L(1,chi) >= 0.0076/log q for q >= 10   (derivation in ARCHITECTURE.md),
    hence h(D) >= 0.0024 sqrt|D|/log|D| for D < -4.
Run: python3 -I check_consequences.py
"""
import math, numpy as np

DMAX, XMAX = 4000, 2 * 10**6

def sieve(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

def is_fund(D):
    if D in (0, 1): return False
    if D % 4 == 1:
        m = abs(D)
    elif D % 4 == 0:
        m = abs(D) // 4
        if m % 4 not in (2, 3) and not (D // 4) % 4 in (2, 3): return False
        if (D // 4) % 4 not in (2, 3): return False
    else:
        return False
    k = 2
    while k * k <= m:
        if m % (k * k) == 0: return False
        k += 1
    return True

P = sieve(XMAX).astype(np.int64)
oddP = P[P > 2]
logp_p = np.log(oddP) / oddP
loglog = np.log(np.log(3.0 * oddP))

def legendre_vec(D):
    b = np.mod(D, oddP).astype(np.int64)
    e = (oddP - 1) // 2
    res = np.ones_like(b)
    base = b.copy()
    while np.any(e > 0):
        mask = (e & 1) == 1
        res[mask] = (res[mask] * base[mask]) % oddP[mask]
        base = (base * base) % oddP
        e >>= 1
    out = np.where(res == 0, 0, np.where(res == 1, 1, -1))
    return out

def chi2(D):
    if D % 2 == 0: return 0
    return 1 if D % 8 in (1, 7) else -1

worst31 = (-1e9, None); worst_bar = (-1e9, None); n_disc = 0; fails31 = 0
for D in list(range(-DMAX, -2)) + list(range(5, DMAX + 1)):
    if not is_fund(D): continue
    n_disc += 1; q = abs(D)
    chi = legendre_vec(D)
    inert = (chi == -1)
    s0 = (math.log(2) / 2) if chi2(D) == -1 else 0.0
    S = s0 + np.cumsum(np.where(inert, logp_p, 0.0))
    idx = np.nonzero(inert)[0]
    if len(idx) == 0: continue
    x = oddP[idx].astype(float); Sx = S[idx]
    g = Sx - (0.55 * np.log(x) + (29 / 60) * math.log(q) + 6)
    k = int(np.argmax(g))
    if g[k] > worst31[0]: worst31 = (float(g[k]), (D, int(x[k])))
    if g[k] > 0: fails31 += 1
    bar = Sx - (0.5 * np.log(x) + 0.25 * math.log(q) + loglog[idx])
    k = int(np.argmax(bar))
    if bar[k] > worst_bar[0]: worst_bar = (float(bar[k]), (D, int(x[k])))
print('(1) discriminants tested:', n_disc, ' primes x <=', XMAX)
print('    max over D,x of S_-(x) - [(11/20)log x + (29/60)log q + 6] =', round(worst31[0], 4), 'at (D,x) =', worst31[1], ' violations:', fails31)
print('    max over D,x of S_-(x) - [(1/2)log x + (1/4)log q + loglog 3x] =', round(worst_bar[0], 4), 'at', worst_bar[1])

# (2) class numbers of imaginary quadratic fields by reduced forms, |D| <= HMAX
HMAX = 20000
def classno(D):
    m = -D; h = 0; a = 1
    while 3 * a * a <= m:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a): continue
            c = (b * b - D) // (4 * a)
            if c < a: continue
            if b < 0 and (a == c): continue
            h += 1
        a += 1
    return h
rows = []
for D in range(-3, -HMAX - 1, -1):
    if not is_fund(D): continue
    h = classno(D)
    w = 6 if D == -3 else (4 if D == -4 else 2)
    L1 = 2 * math.pi * h / (w * math.sqrt(-D))
    rows.append((D, h, L1, L1 * math.log(-D)))
mn = min(rows, key=lambda r: r[3])
print('(2) imaginary fundamental D with |D| <=', HMAX, ':', len(rows), 'fields; known h=1 list check:',
      sorted(-r[0] for r in rows if r[1] == 1))
print('    min L(1,chi) log q =', round(mn[3], 4), 'at D =', mn[0], '(h=%d)' % mn[1])
big = [r for r in rows if -r[0] >= 10]
mn10 = min(big, key=lambda r: r[3])
print('    min over |D|>=10 of L(1,chi) log q =', round(mn10[3], 4), 'at D =', mn10[0], ' vs implied 0.0076: ratio', round(mn10[3] / 0.0076, 1))
viol = [r for r in big if r[1] < 0.0076 * math.sqrt(-r[0]) / (math.pi * math.log(-r[0]))]
print('    violations of implied h >= 0.0076 sqrt|D|/(pi log|D|):', len(viol))
# where does the implied bound first force h >= 2, 3 ?
for target in (1, 2, 10, 100):
    lo, hi = 10.0, 1e30
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if 0.0076 * math.sqrt(mid) / (math.pi * math.log(mid)) >= target: hi = mid
        else: lo = mid
    print('    implied bound gives h >= %d only for |D| >= %.3g' % (target, hi))
# real fields: L(1,chi) via -(1/sqrt D) sum chi(a) log sin(pi a/D), D <= RMAX
RMAX = 2000
def kron(D, n):
    # Kronecker symbol (D/n), n >= 1
    res = 1
    while n % 2 == 0:
        n //= 2; res *= chi2(D)
    a, m, t = D % n, n, 1
    if m == 1: return res
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5): t = -t
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3: t = -t
        a %= m
    return res * (t if m == 1 else 0)
rrows = []
for D in range(5, RMAX + 1):
    if not is_fund(D): continue
    L1 = -sum(kron(D, a) * math.log(math.sin(math.pi * a / D)) for a in range(1, D)) / math.sqrt(D)
    rrows.append((D, L1, L1 * math.log(D)))
mnr = min(rrows, key=lambda r: r[2])
print('    real fundamental D <=', RMAX, ':', len(rrows), 'fields; min L(1,chi) log q =', round(mnr[2], 4), 'at D =', mnr[0],
      '; all positive:', all(r[1] > 0 for r in rrows))

# (3) the auditor-derived constant: with c=1/100, eps=c/log q, t=q^4, u=q^2 (see ARCHITECTURE.md sec. 11)
#     1 <= L(1,chi) e^{4c}/eps + [(1.505 + e^c log q) e^{2c} + (q + 1 + 2 log q) e^{4c}] q^{-2}
c = 0.01
def bracket(q):
    return ((1 + math.exp(c) / 2 + math.exp(c) * math.log(q)) * math.exp(2 * c) + (q + 1 + 2 * math.log(q)) * math.exp(4 * c)) / q**2
mono = all(bracket(q) >= bracket(q + 1) for q in range(10, 10**5))
const = c * math.exp(-4 * c) * (1 - bracket(10))
print('(3) error bracket at q=10: %.4f (decreasing in q: %s); implied L(1,chi) log q >= %.5f for q >= 10' % (bracket(10), mono, const))
