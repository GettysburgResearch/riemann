# Level-2 audit, Section 4: bridge between the paper's gamma_2 (additive character e(z)=exp(4 pi i Im z/sqrt3))
# and the imported Hasse / Dunn-Radziwill normalisation (DR (1.7)-(1.8), (2.1)-(2.3), arXiv:2109.07463):
#   g~_DR(c) = |c|^{-1} sum_{x mod c} (x/c)_3 e_check(x/c),  e_check(z) = exp(2 pi i (z + conj z)).
# Claims tested:  gamma_2(n) = (lambda/n)_3 g~_DR(n);  g~_DR(n)^3 = mu(n) n/|n|  (DR (1.8));
#   g~_DR(ab) = conj((a/b)_3) g~_DR(a) g~_DR(b)  (DR (2.3), overline present in the rendered PDF,
#   dropped by pdftotext).                     Run: python3 -I s4_dr_bridge_check.py
import sys, os, itertools, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from s4_zw import *
LAM = (1, 2)
def gDR(ps):
    m = elt(ps); R = residues(m)
    A = np.array([r[0] for r in R]); B = np.array([r[1] for r in R])
    v = chi_arr(ps, A, B, 2)                    # chi_n^2 = cubic symbol (x/n)_3
    z = (A + B * OMEGA) / cv(m)
    return complex(np.sum(v * np.exp(2j * np.pi * 2 * z.real))) / abs(cv(m))
P = eisenstein_primes(300)
cols = [c for c in squarefree_products(P, 1200) if c and len(c) <= 2]
f = [0, 0, 0]; n = 0
for ps in cols:
    g2 = gamma(ps, 2); gd = gDR(ps); mu = (-1) ** len(ps)
    n += 1
    if abs(g2 - chi(ps, LAM, 2) * gd) > 1e-9: f[0] += 1
    if abs(gd ** 3 - mu * alpha(elt(ps))) > 1e-9: f[1] += 1
pr = [p for p in P if p.q < 120]
m = 0
for p, q in itertools.combinations(pr, 2):
    a, b = [p], [q]
    lhs = gDR(a + b); s = chi(b, p.g, 2)       # (a/b)_3
    m += 1
    if abs(lhs - np.conj(s) * gDR(a) * gDR(b)) > 1e-9: f[2] += 1
print("moduli:", n, " gamma_2 = (lambda/n)_3 g~_DR failures:", f[0], "  DR(1.8) failures:", f[1])
print("pairs:", m, " DR(2.3) with conj((a/b)_3) failures:", f[2])
