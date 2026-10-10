#!/usr/bin/env python3
"""EMPIRICAL check (exact symbols, floating Gauss sums): orientation of Stickelberger gamma_2(p)^3 = -alpha(p) (or its
conjugate) in our conventions, and the consequent identity  mu(p) gamma_2(p) = -gamma_2(p) = alpha'(p) conj(gamma_2(p))^2,
which shows that after one GL(2) reflection the remaining variable carries mu*gamma_2, a conjugate-squared cubic Gauss
sum rather than a theta coefficient (FOURTH_MOMENT_A2.md, 'second-step obstruction')."""
import cmath, math
from eis import *
P = primes_upto(600)
d1 = d2 = 0; n = 0
for p in P:
    g2 = gamma(2, [p]); z = complex(p[0] - 0.5*p[1], p[1]*math.sqrt(3)/2); a = z/abs(z)
    d1 = max(d1, abs(g2**3 + a)); d2 = max(d2, abs(g2**3 + a.conjugate()))
    n += 1
print(f"{n} primes: max|g2^3 + alpha| = {d1:.2e}; max|g2^3 + conj(alpha)| = {d2:.2e}")
which = 'alpha' if d1 < d2 else 'conj(alpha)'
dev = 0
for p in P:
    g2 = gamma(2, [p]); z = complex(p[0] - 0.5*p[1], p[1]*math.sqrt(3)/2); a = z/abs(z)
    aa = a if which == 'alpha' else a.conjugate()
    dev = max(dev, abs(-g2 - aa*g2.conjugate()**2))
print(f"identity mu(p) gamma_2(p) = {which}(p) * conj(gamma_2(p))^2 : max dev {dev:.2e}")
# gamma_4 = conj(gamma_2): then the j=4 local unit omega_{p,4} = gamma_4(p) cancels the column Gauss sum gamma_2(p)
dev4 = max(abs(gamma(4, [p]) - gamma(2, [p]).conjugate()) for p in P)
print(f"max |gamma_4(p) - conj(gamma_2(p))| = {dev4:.2e}  (so gamma_2(p) * omega_(p,4) = |gamma_2(p)|^2 = 1)")
