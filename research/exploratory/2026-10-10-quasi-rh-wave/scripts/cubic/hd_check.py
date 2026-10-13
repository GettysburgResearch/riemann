import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import eis, numpy as np
prs = [pr for pr in eis.primary_primes(200) if pr['p'] % 3 == 1]
print("p  p%12  chi(4)  |g1g2 + a*chi4*g3|  |g1g2 + a*conj(chi4)*g3|   (alpha := -gamma_2^3 from (4.7))")
for pr in prs:
    g1, g2, g3 = (eis.gauss_prime(pr, j) for j in (1, 2, 3))
    chi4 = eis.symbol_val((4, 0), pr, 1)
    alpha = -g2**3
    r1 = abs(g1*g2 + alpha*chi4*g3); r2 = abs(g1*g2 + alpha*np.conj(chi4)*g3)
    print(pr['p'], pr['p'] % 12, np.round(chi4, 3), round(r1, 6), round(r2, 6))
