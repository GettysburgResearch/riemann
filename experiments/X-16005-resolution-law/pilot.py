"""Pilot: correctness checks + cost estimate."""
import time, sys
import mpmath as mp
from mpmath import mpf
import core

print("=" * 72)
print("PILOT 1 -- Loewner closed form (L-16004) vs literal divided differences")
print("=" * 72)
for N in (4, 6):
    poles = [mpf('1.85') + mpf('3.7') * k for k in range(8)]
    w = [mpf(1)] * len(poles)
    core.set_dps(N)
    Q1 = core.build_Q_rank1(N, poles, w)
    Q2 = core.build_Q_divdiff(N, poles, w)
    n = 2 * N + 1
    num = max(abs(Q1[i, j] - Q2[i, j]) for i in range(n) for j in range(n))
    den = max(abs(Q1[i, j]) for i in range(n) for j in range(n))
    print(f"  N={N} dps={mp.mp.dps}  max rel entrywise difference = {mp.nstr(num/den,5)}")

print()
print("=" * 72)
print("PILOT 2 -- EXACT identity  P_xi(s) = Omega(s)*<xi,ell(s)>  (numeric spot check)")
print("=" * 72)
N = 5
core.set_dps(N)
lam = core.nodes(N)
mp.mp.dps = 60
xi = [mp.cos(mpf(j) * mpf('0.7')) + mpf(j) / 3 for j in range(-N, N + 1)]
c = core.P_coeffs(N, xi)
for s0 in ('0.3', '2.7', '-4.11'):
    s0 = mpf(s0)
    lhs = core.polyval_inc(c, s0)
    Om = mpf(1)
    for l in lam:
        Om *= (l - s0)
    rhs = Om * sum(xi[j] / (lam[j] - s0) for j in range(2 * N + 1))
    print(f"  s={mp.nstr(s0,4):>7}  |P - Omega*<xi,ell>| / |P| = {mp.nstr(abs(lhs-rhs)/abs(lhs),5)}")

print()
print("=" * 72)
print("PILOT 3 -- EXACT-recovery regime: K = N positive poles => Q singular,")
print("           kernel vector xi has P_xi roots exactly at the poles")
print("=" * 72)
for N in (4, 6, 8):
    core.set_dps(N)
    lam = core.nodes(N)
    poles = [mpf('1.85') + mpf('3.7') * k for k in range(N)]     # exactly N positive poles
    allp = [p for p in poles] + [-p for p in poles]
    w = [mpf(1)] * len(poles)
    Q = core.build_Q_rank1(N, poles, w)
    # xi from partial fractions of P(s)/Omega(s), P(s) = prod_m (mu_m - s) over all 2N poles
    xi = []
    for j in range(2 * N + 1):
        P = mpf(1)
        for m in allp:
            P *= (m - lam[j])
        D = mpf(1)
        for k in range(2 * N + 1):
            if k != j:
                D *= (lam[k] - lam[j])
        xi.append(P / D)
    Qxi = Q * mp.matrix(xi)
    nrm = max(abs(Qxi[i]) for i in range(2 * N + 1))
    scale = max(abs(Q[i, j]) for i in range(2 * N + 1) for j in range(2 * N + 1)) * max(abs(x) for x in xi)
    print(f"  N={N}: ||Q xi||_inf / scale = {mp.nstr(nrm/scale,5)}   (kernel confirmed)")
    # and its polynomial's roots
    c = core.P_coeffs(N, xi)
    R, odd = core.even_reduce(c)
    ur = core.poly_roots_increasing(R, extraprec=2000)
    got = sorted([mp.sqrt(u).real for u in ur])
    err = max(abs(g - p) / p for g, p in zip(got, sorted(poles)))
    print(f"        max rel error of recovered roots vs true poles = {mp.nstr(err,5)}")

print()
print("=" * 72)
print("PILOT 4 -- timing")
print("=" * 72)
for N in (4, 8, 12, 14):
    poles = [mpf('1.85') + mpf('3.7') * k for k in range(30)]
    w = [mpf(1)] * len(poles)
    t0 = time.time()
    info = core.detect(N, poles, w, extraprec=4000)
    dt = time.time() - t0
    mr = max(info['resid'])
    print(f"  N={N:>3} dps={info['dps']:>4} K=30  time={dt:6.2f}s  max root rel-residual={mp.nstr(mr,4)}"
          f"  even_res={mp.nstr(info['even_res'],3)}  odd_rel={mp.nstr(info['odd_rel'],3)}"
          f"  max|Im u|={mp.nstr(info['max_imag_u'],3)}")
    print("        recovered positive roots:", [mp.nstr(r, 10) for r in info['pos_roots']])
