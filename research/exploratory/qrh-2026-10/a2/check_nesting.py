#!/usr/bin/env python3
"""EMPIRICAL check (exact symbols, floating Gauss sums) of the nesting identity
   gamma_2(de) chi_de(h) = gamma_2(d) chi_d(h) * gamma_2(e) chi_e(h d^4)
for coprime primary primes d, e and random rows h, including the zero convention:
if e | d the right side vanishes through chi_e(d^4) = 0 (here d, e distinct primes so it is the coprime case),
and if e = d the left side gamma_2(d^2) is not defined for the squarefree family -- excluded)."""
import itertools, random, sys
from eis import *
random.seed(5)
P = primes_upto(int(sys.argv[1]) if len(sys.argv) > 1 else 120)
G2 = {p: gamma(2, [p]) for p in P}
dev = 0; n = 0; zero_ok = 0
for d, e in itertools.combinations(P, 2):
    if norm(d)*norm(e) > 3000: continue
    g2de = gamma(2, [d, e])
    for _ in range(6):
        h = (random.randint(-60, 60), random.randint(-60, 60))
        if h == (0, 0): continue
        kd, ke = sym_prime(h, d), sym_prime(h, e)
        lhs = 0 if (kd is None or ke is None) else g2de*ZETA[(2*(kd + ke)) % 6]   # chi_{de}(h)^? : family uses chi (sextic) itself
        # NOTE: the family twist is chi_n(h) (sextic, power 1); gamma_2 carries the cubic Gauss sum.
        lhs = 0 if (kd is None or ke is None) else g2de*ZETA[(kd + ke) % 6]
        d4 = mul(mul(d, d), mul(d, d))
        k_e_hd4 = sym_prime(mul(h, d4), e)
        rhs = 0 if (kd is None or k_e_hd4 is None) else G2[d]*ZETA[kd]*G2[e]*ZETA[k_e_hd4]
        dev = max(dev, abs(lhs - rhs)); n += 1
print(f"checked {n} (d, e, h) triples over {len(P)} primes; max |lhs - rhs| = {dev:.2e}")
