#!/usr/bin/env python3
"""EMPIRICAL reconnaissance of the fourth-moment dual off-diagonal (FOURTH_MOMENT_A2.md Sec. 4).
Dual column sum over squarefree r = de (d,e coprime squarefree primary, N in (X,2X]), coefficient
  c(r) = sum over ordered balanced factorizations of gamma_2(d) gamma_2(e) conj((e/d)_3)
(by cubic reciprocity the two orders agree).  Rows h: nonzero elements with N(h) <= HD.
Reports rho = (S_true - S_diag)/L^2, where S_diag = sum_h sum_r |c(r)|^2 1_{(r,h)=1} is the dual diagonal and
L = sum_r |c(r)|^2 / 4 counts unordered pairs (column 'length').  The fourth-moment target at H < L is
equivalent (schematically, ray phases ignored) to rho = O(1); generic dual behaviour gives rho ~ +-sqrt(HD*L)/L^2 * ...
Tiny scales only."""
import sys, math, itertools, json
from eis import *
def run(X, HD):
    P = primes_upto(2*X)
    G2 = {p: gamma(2, [p]) for p in P}
    cols = []
    def rec(start, cur, nrm):
        if X < nrm <= 2*X: cols.append(tuple(cur))
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
    coefs = {}
    for d in cols:
        for e in cols:
            if set(d) & set(e): continue
            k = sum(sym_prime(elem(e), p) for p in d)
            r = tuple(sorted(d + e, key=lambda p: (norm(p), p)))
            coefs[r] = coefs.get(r, 0) + g2(d)*g2(e)*ZETA[(-2*k) % 6]
    R = list(coefs.items())
    L = sum(abs(c)**2 for _, c in R)/4
    B = int(math.isqrt(int(4*HD/3)) + 2)
    rows = [(a, b) for a in range(-B, B + 1) for b in range(-B, B + 1) if 0 < a*a - a*b + b*b <= HD]
    cache = {}
    def chi_r(r, h):
        s = 0
        for p in r:
            if (p, h) not in cache: cache[(p, h)] = sym_prime(h, p)
            k = cache[(p, h)]
            if k is None: return None
            s += k
        return s % 6
    S_true = S_diag = 0.0
    for h in rows:
        acc = 0
        for r, c in R:
            k = chi_r(r, h)
            if k is None: continue
            acc += c*ZETA[k]; S_diag += abs(c)**2
        S_true += abs(acc)**2
    return dict(X=X, HD=HD, n_r=len(R), L=L, rows=len(rows), S_true=S_true, S_diag=S_diag,
                ratio=S_true/S_diag, rho=(S_true - S_diag)/L**2)
if __name__ == '__main__':
    for X, HD in [(int(a), int(b)) for a, b in (s.split(':') for s in sys.argv[1:])]:
        print(json.dumps(run(X, HD)), flush=True)
