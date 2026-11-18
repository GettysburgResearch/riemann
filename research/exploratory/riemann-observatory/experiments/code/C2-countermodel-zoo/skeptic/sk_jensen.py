#!/usr/bin/env python3
"""SKEPTIC replay of C2-17 (Turan / Jensen for xi~ = xi * P_quadruple) from an INDEPENDENT coefficient source:
Taylor coefficients of xi(1/2+z) from the Polya moments b_m = int_0^inf u^{2m} Phi(u) du (mpmath quad),
xi(1/2+w) = 8 sum_m 4^m b_m w^{2m}/(2m)!  (since H_0(z) = xi(1/2+iz/2)/8 = sum (-1)^m b_m z^{2m}/(2m)!),
then multiplication by (X-X0)(X-conj X0), X = z^2, X0 = (rho0-1/2)^2.  NON-RIGOROUS (mpmath, dps 110).
Real-root counts of the Jensen polynomials J^{d,0}(X) = sum_j C(d,j) g(j) X^j by sympy Sturm sequences on
the exactly-rational rounded polynomial (rounding to 100 digits; NOT propagated).
Usage: python3 sk_jensen.py OUTDIR"""
import sys, os, json, time, math
import mpmath as mp
import sympy as sp
mp.mp.dps = 110
M = 81


def Phi(u):
    return mp.fsum((2 * mp.pi ** 2 * n ** 4 * mp.exp(9 * u) - 3 * mp.pi * n ** 2 * mp.exp(5 * u)) * mp.exp(-mp.pi * n * n * mp.exp(4 * u)) for n in range(1, 12))


def main():
    t0 = time.time()
    b = [mp.quad(lambda u: u ** (2 * m) * Phi(u), [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.3, 1.7, 2.2]) for m in range(M + 1)]
    c = [8 * mp.mpf(4) ** m * b[m] / mp.factorial(2 * m) for m in range(M + 1)]   # xi(1/2+z) = sum c_m X^m
    out = dict(check_xi_half=[mp.nstr(c[0], 20), mp.nstr(mp.mpf(1) / 2 * (mp.mpf(1) / 2 - 1) * mp.pi ** (-mp.mpf(1) / 4) * mp.gamma(mp.mpf(1) / 4) * mp.zeta(mp.mpf(1) / 2), 20)])
    print('xi(1/2) from b_0 vs direct:', out['check_xi_half'], flush=True)
    res = {}
    for beta, gam in [(None, None), (0.6, 14.0), (0.9, 5.0), (0.6, 5.0)]:
        if beta is None:
            cc = c[:]
            lab = 'xi'
        else:
            X0 = (mp.mpc(beta, gam) - mp.mpf(1) / 2) ** 2
            A, B = -2 * mp.re(X0), abs(X0) ** 2          # (X - X0)(X - conj X0) = X^2 + A X + B
            cc = [B * c[m] + (A * c[m - 1] if m >= 1 else 0) + (c[m - 2] if m >= 2 else 0) for m in range(M + 1)]
            lab = f'xi~ beta={beta},gamma0={gam}'
        g = [mp.factorial(k) * cc[k] for k in range(M + 1)]
        tur = [g[k] ** 2 - g[k - 1] * g[k + 1] for k in range(1, M)]
        r = dict(turan_k_range=[1, M - 1], turan_all_positive=all(x > 0 for x in tur),
                 turan_min_rel=mp.nstr(min(tur[k - 1] / g[k] ** 2 for k in range(1, M)), 6))
        X = sp.Symbol('X')
        gq = [sp.Rational(mp.nstr(x, 100, strip_zeros=False)) if x != 0 else sp.Integer(0) for x in g]
        nonhyp = {}
        for d in list(range(2, 41)):
            poly = sp.Poly(sum(sp.binomial(d, j) * gq[j] * X ** j for j in range(d + 1)), X)
            nreal = poly.count_roots()            # real roots with multiplicity (Sturm, exact)
            if nreal < d:
                nonhyp[d] = d - nreal
        r['J_d0_nonhyperbolic_d<=40 (d: #nonreal)'] = nonhyp
        res[lab] = r
        print(lab, r, round(time.time() - t0, 1), flush=True)
    out['results'] = res
    out['runtime_s'] = round(time.time() - t0, 1)
    os.makedirs(sys.argv[1], exist_ok=True)
    json.dump(out, open(os.path.join(sys.argv[1], 'sk_jensen.json'), 'w'), indent=1, default=str)


if __name__ == '__main__':
    main()
