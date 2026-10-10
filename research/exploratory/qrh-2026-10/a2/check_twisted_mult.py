#!/usr/bin/env python3
"""EMPIRICAL (exact symbols, floating Gauss sums): twisted multiplicativity of normalized Gauss sums
gamma_j(de) = chi_d(e)^j chi_e(d)^j gamma_j(d) gamma_j(e), and its cubic-reciprocity form
gamma_2(de) = gamma_2(d) gamma_2(e) * conj((e/d)_3)  [(e/d)_3 = chi_d(e)^2],  for coprime primary primes d,e."""
import itertools, sys
from eis import *
P = primes_upto(int(sys.argv[1]) if len(sys.argv) > 1 else 200)
maxdev = {'crt1': 0, 'crt2': 0, 'cubic_recip': 0, 'sextic_ratio_values': set()}
pairs = 0
for d, e in itertools.combinations(P, 2):
    if norm(d)*norm(e) > 4000: continue
    g2d, g2e, g2de = gamma(2, [d]), gamma(2, [e]), gamma(2, [d, e])
    g1d, g1e, g1de = gamma(1, [d]), gamma(1, [e]), gamma(1, [d, e])
    kde = sym_prime(e, d)   # chi_d(e) = (e/d)_6
    ked = sym_prime(d, e)   # chi_e(d) = (d/e)_6
    crt2 = g2de - ZETA[(2*(kde + ked)) % 6]*g2d*g2e
    crt1 = g1de - ZETA[(kde + ked) % 6]*g1d*g1e
    cub = g2de - ZETA[(-2*kde) % 6]*g2d*g2e
    maxdev['crt1'] = max(maxdev['crt1'], abs(crt1)); maxdev['crt2'] = max(maxdev['crt2'], abs(crt2))
    maxdev['cubic_recip'] = max(maxdev['cubic_recip'], abs(cub))
    maxdev['sextic_ratio_values'].add((kde - ked) % 6)   # sextic reciprocity: (e/d)_6 / (d/e)_6
    pairs += 1
print(f"primes: {len(P)}; coprime prime pairs with N(de) <= 4000: {pairs}")
print(f"max |gamma_1(de) - chi_d(e)chi_e(d) gamma_1(d)gamma_1(e)| = {maxdev['crt1']:.2e}")
print(f"max |gamma_2(de) - (chi_d(e)chi_e(d))^2 gamma_2(d)gamma_2(e)| = {maxdev['crt2']:.2e}")
print(f"max |gamma_2(de) - conj((e/d)_3) gamma_2(d)gamma_2(e)| = {maxdev['cubic_recip']:.2e}")
print(f"observed (e/d)_6/(d/e)_6 exponents mod 6: {sorted(maxdev['sextic_ratio_values'])} (expect subset of {{0,3}}: a sign)")
