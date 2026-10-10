#!/usr/bin/env python3
"""EMPIRICAL (exact symbols, floating Gauss sums): the k = 3 pattern of the moment-ladder duals.

For pairwise coprime primary primes d, e, f:
    gamma_2(def) = gamma_2(d) gamma_2(e) gamma_2(f) * conj((e/d)_3 (f/d)_3 (f/e)_3),
i.e. every PAIR of factors carries a cubic symbol (the 'complete graph' K_3 pattern), with
(y/x)_3 = chi_x(y)^2.  Control: dropping one pair symbol must fail.
Run: python3 check_triple.py [prime_bound] [max_norm_product]
"""
import itertools, sys
from eis import *

B = int(sys.argv[1]) if len(sys.argv) > 1 else 60
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
P = primes_upto(B)
dev, dev_ctrl, n = 0.0, float('inf'), 0
for d, e, f in itertools.combinations(P, 3):
    if norm(d) * norm(e) * norm(f) > NMAX:
        continue
    g = gamma(2, [d, e, f])
    k_ed, k_fd, k_fe = sym_prime(e, d), sym_prime(f, d), sym_prime(f, e)   # chi_x(y) exponents mod 6
    pair = ZETA[(-2 * (k_ed + k_fd + k_fe)) % 6]
    pred = gamma(2, [d]) * gamma(2, [e]) * gamma(2, [f]) * pair
    ctrl = gamma(2, [d]) * gamma(2, [e]) * gamma(2, [f]) * ZETA[(-2 * (k_ed + k_fd)) % 6]
    dev = max(dev, abs(g - pred))
    dev_ctrl = min(dev_ctrl, abs(g - ctrl)) if (k_fe * 2) % 6 else dev_ctrl
    n += 1
print(f"triples tested: {n} (primes up to norm bound {B}, N(def) <= {NMAX})")
print(f"max |gamma_2(def) - prod gamma_2 * conj(all three pair symbols)| = {dev:.2e}")
print(f"control (one pair symbol dropped, nontrivial cases): min deviation = {dev_ctrl:.3f}  (should be >> 0)")
