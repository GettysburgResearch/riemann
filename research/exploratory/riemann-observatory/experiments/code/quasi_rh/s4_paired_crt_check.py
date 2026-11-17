# Level-2 audit, Section 4: explicit check of the CRT factorisation behind (eq:initial-paired-gauss)
#   gamma(conj(chi_z1) chi_z2) = conj(chi_z1(z2)) chi_z2(z1) gamma_{-1}(z1) gamma_1(z2),  |.| = 1,
# and of (eq:initial-paired-gauss) itself with a NONTRIVIAL nu (nu((t)) = psi(N t), psi of order 4 mod 5),
# using G evaluated on the class of z2 z1^{-1} mod 4.   Run: python3 -I s4_paired_crt_check.py
import sys, os, itertools, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from s4_zw import *
P = [p for p in eisenstein_primes(200) if p.q != 25]
cols = [c for c in squarefree_products(P, 200) if c]
psi = {1: 1, 2: 1j, 4: -1, 3: -1j}
nu = lambda ps: psi[nm(ps) % 5] if ps else 1
G_class = {}
for p in eisenstein_primes(600):
    G_class.setdefault(mod4(p.g), chi([p], (4, 0)).conjugate() * gamma([p], 3))
units4 = [(a, b) for a in range(4) for b in range(4) if norm((a, b)) % 2 == 1]
inv4 = lambda t: next(u for u in units4 if mod4(mul(u, t)) == (1, 0))
aco = lambda ps: alpha(elt(ps)).conjugate() * gamma(ps, 2)
f1 = f2 = n = 0
for z1, z2 in itertools.product(cols, cols):
    if set(p.g for p in z1) & set(p.g for p in z2): continue
    if nm(z1) * nm(z2) > 3000: continue
    m = mul(elt(z1), elt(z2))
    def chf(A, B): return np.conj(chi_arr(z1, A, B)) * chi_arr(z2, A, B)
    gam = gauss_general(m, chf)
    crt = np.conj(chi(z1, elt(z2))) * chi(z2, elt(z1)) * gamma(z1, -1) * gamma(z2, 1)
    n += 1
    if abs(gam - crt) > 1e-9 or abs(abs(gam) - 1) > 1e-9: f1 += 1
    mu1 = (-1) ** len(z1); mu2 = (-1) ** len(z2)
    lhs = mu1 * mu2 * np.conj(nu(z1)) * nu(z2) * gam
    t = mod4(mul(elt(z2), inv4(mod4(elt(z1)))))
    rhs = np.conj(nu(z1)) * nu(z2) * G_class[t] * aco(z1) * np.conj(aco(z2))
    if abs(lhs - rhs) > 1e-9: f2 += 1
print("pairs:", n, " CRT factorisation failures:", f1, "  (initial-paired-gauss) with nu != 1 failures:", f2)
