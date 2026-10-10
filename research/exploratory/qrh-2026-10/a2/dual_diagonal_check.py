#!/usr/bin/env python3
"""EMPIRICAL, finite (no asymptotic claim): is the positive dual mean square
      M(Hc) = sum_{0 < N(h) <= Hc} |C_h|^2,   C_h = sum_r c_r chi_r(h),
dominated by its diagonal  Diag(Hc) = sum_r |c_r|^2 #{h : N(h) <= Hc, (h, r) = 1}
once the number of rows exceeds the number of columns?  Coefficients: c_r = gamma_2(r) on squarefree
primary r (prime to 6) with N(r) <= R (the A2-type dual coefficient on its squarefree support; the
balanced-divisor weight and ray phases are omitted).  Prints M/Diag for several Hc.
Relevance: FOURTH_MOMENT_A2.md Sec. 4 asks for sum_h |C_h|^2 <~ L^2 with 𝓗 = L^2/H > L; if M ~ Diag ~ 𝓗 L
for 𝓗 > L, that positive target is unreachable and the needed saving cannot come from per-row structure."""
import sys, itertools
from eis import mul, norm, sym_prime, primes_upto, gamma, ZETA

R = int(sys.argv[1]) if len(sys.argv) > 1 else 400
P = [p for p in primes_upto(R)]
# squarefree products of distinct primary primes with norm <= R
rs = []
def build(start, cur, n):
    if cur: rs.append(list(cur))
    for i in range(start, len(P)):
        m = n*norm(P[i])
        if m > R: break
        cur.append(P[i]); build(i + 1, cur, m); cur.pop()
build(0, [], 1)
c = [gamma(2, f) for f in rs]
L = len(rs)
Hmax = int(sys.argv[2]) if len(sys.argv) > 2 else 12*L
hs = []
B = int((4*Hmax/3)**0.5) + 2
for a in range(-B, B + 1):
    for b in range(-B, B + 1):
        n = a*a - a*b + b*b
        if 0 < n <= Hmax: hs.append(((a, b), n))
hs.sort(key=lambda t: t[1])
sym = {}
for p in P:
    sym[p] = [sym_prime(h, p) for h, _ in hs]
cuts = sorted(set([L//2, L, 2*L, 4*L, 8*L, Hmax]))
M = 0.0; D = 0.0; j = 0
print(f"columns L = {len(rs)} squarefree r (N r <= {R}); rows h with N(h) <= {Hmax}: {len(hs)}")
out = []
for idx, (h, n) in enumerate(hs):
    Ch = 0
    for k, f in enumerate(rs):
        s = 0
        for p in f:
            v = sym[p][idx]
            if v is None: s = None; break
            s += v
        if s is None: continue
        Ch += c[k]*ZETA[s % 6]
        D += abs(c[k])**2
    M += abs(Ch)**2
    nrows = idx + 1
    if j < len(cuts) and (idx + 1 == len(hs) or hs[idx + 1][1] > cuts[j]) and n <= cuts[j]:
        pass
    while j < len(cuts) and (idx + 1 == len(hs) or hs[idx + 1][1] > cuts[j]):
        out.append((cuts[j], nrows, M, D)); j += 1
for Hc, nrows, Mv, Dv in out:
    print(f"  N(h) <= {Hc:6d}  rows {nrows:6d}  rows/L = {nrows/L:6.2f}   M/Diag = {Mv/Dv:.3f}")
