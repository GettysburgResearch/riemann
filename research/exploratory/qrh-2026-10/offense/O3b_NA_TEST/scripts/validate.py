# validation of na_model Gauss sums against brute-force a2/eis.py (imported read-only)
import sys, os, math, cmath, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../a2')))
import na_model as M
import eis
t=time.time()
P = M.make_primes(400)
sf = M.sf_elements(P, 400)
print('primes', len(P), 'sf', len(sf), time.time()-t)
bad = 0; cnt=0
for el, N, fac in sf[1:]:
    if N > 400: continue
    facs = [P[i].el for i in fac]
    for j in (1, 2):
        g1 = M.gamma_sf(P, fac, j)
        g0 = eis.gamma(j, facs)
        cnt += 1
        if abs(g1 - g0) > 1e-8: bad += 1; print('MISMATCH', el, N, j, g1, g0)
    # chi_s(m) check for a few m
    for m in [(2, 5), (-3, 7), (11, -4), (-1, 0)]:
        k = M.chi_exp_el(P, fac, m)
        k0 = eis.chi(facs, m)
        if (k if k >= 0 else None) != k0: bad += 1; print('CHI MISMATCH', el, m, k, k0)
print('checked', cnt, 'bad', bad)
# eq:signal check: gamma_2^3 = mu * alpha with |alpha| = 1; gamma_1 = G gamma_2^2 with |G|=1
import numpy as np
for el, N, fac in sf[1:8]:
    g1 = M.gamma_sf(P, fac, 1); g2 = M.gamma_sf(P, fac, 2)
    print(el, N, abs(g1), abs(g2), 'g1/g2^2=', g1/g2**2)
# direct check of q^{-1/2} g_{chi_s}(s,-m) = conj chi_s(-m) gamma_1(s) for one composite s
el, N, fac = [t for t in sf if len(t[2]) == 2][0]
facs = [P[i].el for i in fac]
R, NN = eis.residues(el)
for m in [(2,5),(3,-1)]:
    s = 0
    for v in R:
        k = eis.chi(facs, v)
        if k is None: continue
        s += M.ZETA[k] * eis.e_of(M.mul((-m[0], -m[1]), v), el)
    lhs = s / math.sqrt(NN)
    km = M.chi_exp_el(P, fac, (-m[0], -m[1]))
    rhs = np.conj(M.ZETA[km]) * M.gamma_sf(P, fac, 1)
    print('identity O3.1 check', el, m, abs(lhs - rhs))
