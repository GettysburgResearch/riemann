#!/usr/bin/env python3
"""EMPIRICAL (exact symbols, floating Gauss sums): does the fourth-moment dual double sum
   C_h(X) = sum_{d,e} gamma_2(d) gamma_2(e) conj((e/d)_3) chi_d(h) chi_e(h)   [coprime, squarefree, primary, N in (X,2X]]
cancel better than a random-phase control with the same support?  By Poisson duality (FOURTH_MOMENT_A2.md Sec. 4)
the fourth-moment target at column length L=#pairs > H needs sum_{N h <= Hd} |C_h|^2 << L^2, whereas generic
(square-root) behaviour gives Hd * L.  Tiny scales only: reconnaissance, not evidence of any asymptotic."""
import sys, math, random, cmath, itertools, json
from eis import *
random.seed(11)
X = int(sys.argv[1]) if len(sys.argv) > 1 else 40
HD = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
P = primes_upto(2*X)
G2 = {p: gamma(2, [p]) for p in P}
# squarefree primary n with N(n) in (X, 2X], as prime-factor lists (products of distinct primes)
cols = []
def rec(start, cur, nrm):
    if X < nrm <= 2*X: cols.append(list(cur))
    for i in range(start, len(P)):
        q = P[i]
        if nrm*norm(q) > 2*X: break
        rec(i + 1, cur + [q], nrm*norm(q))
rec(0, [], 1)
def g2(fac):
    v = 1
    for p in fac: v *= G2[p]
    for p, q in itertools.combinations(fac, 2):
        v *= ZETA[(2*(sym_prime(q, p) + sym_prime(p, q))) % 6]
    return v
def elem(fac):
    n = (1, 0)
    for p in fac: n = mul(n, p)
    return n
coef = []
for d in cols:
    for e in cols:
        if set(d) & set(e): continue
        ne = elem(e)
        # conj((e/d)_3) = chi_d(e)^{-2}
        k = sum(sym_prime(ne, p) for p in d)
        coef.append((d, e, g2(d)*g2(e)*ZETA[(-2*k) % 6]))
L = len(coef)
# rows h: nonzero elements with N(h) <= HD, one per ideal up to units is NOT required: use all elements in a box
rows = [(a, b) for a in range(-70, 71) for b in range(-70, 71) if 0 < a*a - a*b + b*b <= HD]
symcache = {}
def chi_fac(fac, h):
    s = 0
    for p in fac:
        key = (p, h)
        if key not in symcache: symcache[key] = sym_prime(h, p)
        k = symcache[key]
        if k is None: return None
        s += k
    return s % 6
rand_phase = [cmath.exp(2j*math.pi*random.random()) for _ in coef]
S_true = S_rand = 0.0
for h in rows:
    ct = cr = 0
    for (d, e, c), rp in zip(coef, rand_phase):
        kd = chi_fac(d, h); ke = chi_fac(e, h)
        if kd is None or ke is None: continue
        z = ZETA[(kd + ke) % 6]
        ct += c*z; cr += rp*z
    S_true += abs(ct)**2; S_rand += abs(cr)**2
out = dict(X=X, HD=HD, columns=len(cols), pairs_L=L, rows=len(rows), S_true=S_true, S_rand=S_rand,
           ratio_true_over_rand=S_true/S_rand, generic_rowsxL=len(rows)*L, L_squared=L*L)
print(json.dumps(out))
