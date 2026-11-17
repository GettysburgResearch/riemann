#!/usr/bin/env python3
"""SKEPTIC replay of C2-21 (continuous Beurling toy), NON-RIGOROUS mpmath:
(1) Mellin identity int_1^inf x^{-s} dPi = log(s/(s-1)) - E1((s-rho)L) - E1((s-conj rho)L) by direct quadrature in x
    (not in v = log x as the investigator did), with the x0-cut handled by splitting at x0;
(2) A = exp(-2 Re E1((1-rho)L));  (3) N(x) = x * int_{[1,x]} y^{-1} dG(y) check is analytic (see review);
(4) monotonicity h(x) = 1 - 1/x - 2 x^{beta-1} increasing => positivity for all x >= x0 (checked on a grid)."""
import sys, os, json
import mpmath as mp
mp.mp.dps = 30
out = {}
for beta, gam, x0 in [(mp.mpf('0.75'), mp.mpf(10), 32), (mp.mpf('0.6'), mp.mpf(25), 16)]:
    rho = mp.mpc(beta, gam); L = mp.log(x0)
    rec = {}
    for s in [mp.mpc(2, 0), mp.mpc(1.5, 3)]:
        f1 = lambda x: x ** (-s) * (1 - 1 / x) / mp.log(x)
        f2 = lambda x: -2 * mp.re(x ** (rho - 1)) * x ** (-s) / mp.log(x)
        I1 = mp.quad(f1, [1, 2, x0, 10 * x0, 1000 * x0, mp.inf])
        I2 = mp.quad(f2, mp.linspace(x0, 50 * x0, 400) + [mp.inf])
        closed = mp.log(s / (s - 1)) - mp.e1((s - rho) * L) - mp.e1((s - mp.conj(rho)) * L)
        rec[str(s)] = mp.nstr(abs(I1 + I2 - closed), 3)
    rec['A'] = mp.nstr(mp.exp(-2 * mp.re(mp.e1((1 - rho) * L))), 20)
    rec['zeta_at_2'] = mp.nstr(mp.mpf(2) * mp.exp(-2 * mp.re(mp.e1((2 - rho) * L))), 20)
    h = lambda x: 1 - 1 / x - 2 * x ** (beta - 1)
    rec['h(x0)'] = mp.nstr(h(x0), 10)
    rec['h_increasing_on_grid'] = all(h(x0 * 1.1 ** (k + 1)) > h(x0 * 1.1 ** k) for k in range(200))
    out[f'beta={beta},gamma={gam},x0={x0}'] = rec
print(json.dumps(out, indent=1))
os.makedirs(sys.argv[1], exist_ok=True)
json.dump(out, open(os.path.join(sys.argv[1], 'sk_beurling.json'), 'w'), indent=1)
