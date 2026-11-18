#!/usr/bin/env python3
"""SKEPTIC replay of C2-18 (Epstein part) from an INDEPENDENT coefficient source (no L-functions, no genus theory):
q = x^2/sqrt5 + sqrt5 y^2 (unimodular, Z_Q(s) = 5^{-s/2} Z_q(s) for Q = x^2+5y^2), so
xi_Q(s) := s(s-1)(sqrt20/2pi)^s Gamma(s) Z_Q(s) = s(s-1) pi^{-s} Gamma(s) Z_q(s), and Riemann's theta method gives
xi_Q(1/2+z) = 1 + (z^2 - 1/4) sum_m A_m z^{2m},  A_m = (2/(2m)!) int_1^inf (theta_q(t)-1) t^{-1/2} (log t)^{2m} dt,
theta_q(t) = theta3(e^{-pi t/sqrt5}) theta3(e^{-pi t sqrt5}).  (The pole terms -1/s - 1/(1-s) contribute exactly 1.)
Checks xi_Q(1/2) against Z_Q(1/2) = -2.2981771532167310042 (C2-12); Turan for k <= 78; Jensen J^{d,n}, d,n <= 40,
d+n <= 79, root isolation by FLINT on 60-digit-rounded integer polynomials.  NON-RIGOROUS.
Usage: python3 sk_jensen_epstein.py OUTDIR"""
import sys, os, json, time
import mpmath as mp
import sympy as sp
mp.mp.dps = 80
K = 81
r5 = mp.sqrt(5)
th = lambda t: mp.jtheta(3, 0, mp.exp(-mp.pi * t / r5)) * mp.jtheta(3, 0, mp.exp(-mp.pi * t * r5)) - 1
t0 = time.time()
A = [2 * mp.quad(lambda t: th(t) / mp.sqrt(t) * mp.log(t) ** (2 * m), [1, 2, 5, 10, 20, 40, 80, 160, 320, mp.inf]) / mp.factorial(2 * m) for m in range(K + 1)]
c = [1 - A[0] / 4] + [A[k - 1] - A[k] / 4 for k in range(1, K + 1)]
xi_half_expected = -mp.mpf(1) / 4 * mp.power(5, mp.mpf(1) / 4) * mp.mpf('-2.2981771532167310042')   # s(s-1)pi^{-1/2}Gamma(1/2)Z_q(1/2)
out = dict(xi_Q_half=[mp.nstr(c[0], 18), mp.nstr(xi_half_expected, 18)])
print(out, round(time.time() - t0, 1), flush=True)
g = [mp.factorial(k) * c[k] for k in range(K + 1)]
tur = [g[k] ** 2 - g[k - 1] * g[k + 1] for k in range(1, K)]
out['turan_k_1_to_80_all_positive'] = all(x > 0 for x in tur)
out['turan_min_rel'] = mp.nstr(min(tur[k - 1] / g[k] ** 2 for k in range(1, K)), 6)
# root isolation: FLINT fmpz_poly.complex_roots on the 60-digit-rounded integer polynomial (as the investigator,
# but with independently computed coefficients); sympy Sturm was too slow for ~1500 polynomials (killed at 15 min)
import fractions, math as _m
from flint import fmpq, fmpq_poly, fmpz
def qq(x):
    F = fractions.Fraction(mp.nstr(x, 60, strip_zeros=False))
    return fmpq(F.numerator, F.denominator)
gq = [qq(x) for x in g]
bad = []
for d in range(2, 41):
    for n in range(0, 41):
        if n + d > 79:
            break
        P = fmpq_poly([fmpz(_m.comb(d, j)) * gq[n + j] for j in range(d + 1)])
        nonreal = sum(m for r, m in P.numer().complex_roots() if not r.imag.contains(0))
        if nonreal:
            bad.append((d, n, nonreal))
out['nonhyperbolic_(d,n)'] = bad
out['runtime_s'] = round(time.time() - t0, 1)
print(out, flush=True)
os.makedirs(sys.argv[1], exist_ok=True)
json.dump(out, open(os.path.join(sys.argv[1], 'sk_jensen_epstein.json'), 'w'), indent=1, default=str)
