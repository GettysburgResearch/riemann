#!/usr/bin/env python3
"""EMPIRICAL (exact sextic symbols, floating Gauss sums): dictionary between the fourth-moment dual
coefficient and the cubic A2 Weyl group multiple Dirichlet series (BBCFH 'WMDS I' eq. (5),(10),(13);
Chinta-Gunnells JAMS 2010 eqs. (2.1), (4.3)-(4.5)).

Conventions (BBF/CG): (a/c)_3 = cubic residue symbol, character in a, modulus c;
g(m, c) = sum_{a mod c} (a/c)_3 psi(m a / c), psi = e (trivial on O and on no larger ideal).
Our code: chi_c(a) = (a/c)_6, and (a/c)_3 = chi_c(a)^2; gamma_2(c) = g(1, c)/N(c)^{1/2}.

Checks, for coprime primary primes d, e (and products/powers where stated) and rows h prime to de:
 (R) cubic reciprocity orientation: (d/e)_3 == (e/d)_3          [so conj((e/d)_3) == (d/e)_3^{-1}]
 (N) nesting basis of BBCFH p.9:  g(1,d) (d/e)_3^{-1} == g(e, d)
 (T) twist split:  chi_d(h) chi_e(h) == (h/d)_3^{-1} (h/e)_3^{-1} * (h/de)_2,  (h/c)_2 := chi_c(h)^3
 (D) full dictionary:
       gamma_2(d) gamma_2(e) conj((e/d)_3) chi_d(h) chi_e(h)
         == N(de)^{-1/2} * H(d, e; h, h) * (h/de)_2,
     with H(d, e; h, h) = (h/d)_3^{-1} (h/e)_3^{-1} g(1,d) g(1,e) (d/e)_3^{-1}   [CG (4.3)-(4.5)]
 (P) stable p-parts for n = 3 (BBCFH (13)): g(1, p^2) = 0, H(p, p) = 0 is a definition, and
       g(p, p^2) == N(p) * conj(g(1, p)),  hence H(p^2, p) = H(p, p^2) = g(1,p) g(p,p^2) = N(p)^2,
       H(p^2, p^2) = g(1,p)^2 g(p,p^2) = N(p)^2 g(1,p).
"""
import itertools, random, sys, cmath, math
from eis import (mul, norm, sym_prime, primes_upto, residues, e_of, ZETA, gamma)

def cubic_sym(a, factors):
    """(a/c)_3 as k mod 3 (value omega^k = ZETA[2k]) for c = prod(factors) (repeats allowed), or None."""
    s = 0
    for p in factors:
        k = sym_prime(a, p)
        if k is None: return None
        s += 2*k
    return s % 6          # exponent of ZETA (even)

def g(m, factors):
    n = (1, 0)
    for p in factors: n = mul(n, p)
    R, N = residues(n)
    tot = 0
    for v in R:
        k = cubic_sym(v, factors)
        if k is None: continue
        tot += ZETA[k] * e_of(mul(m, v), n)
    return tot

random.seed(11)
P = primes_upto(int(sys.argv[1]) if len(sys.argv) > 1 else 160)
dev = {'R': 0.0, 'N': 0.0, 'T': 0.0, 'D': 0.0}
npairs = 0; nrows = 0
G1 = {p: g((1, 0), [p]) for p in P}
for d, e in itertools.combinations(P, 2):
    if norm(d)*norm(e) > 4000: continue
    npairs += 1
    kde, ked = sym_prime(e, d), sym_prime(d, e)       # chi_d(e), chi_e(d)
    dev['R'] = max(dev['R'], abs(ZETA[(2*kde) % 6] - ZETA[(2*ked) % 6]))
    # (N): g(e, d) == (e/d)^{-1} g(1,d) [CG Prop 2.1(3)] == (d/e)^{-1} g(1,d) [BBCFH p.9, via (R)]
    dev['N'] = max(dev['N'], abs(G1[d]*ZETA[(-2*ked) % 6] - g(e, [d])))
    g2d, g2e = gamma(2, [d]), gamma(2, [e])
    for _ in range(5):
        h = (random.randint(-80, 80), random.randint(-80, 80))
        kd, ke = sym_prime(h, d), sym_prime(h, e)
        if kd is None or ke is None: continue
        nrows += 1
        lhsT = ZETA[(kd + ke) % 6]
        rhsT = ZETA[(-2*kd - 2*ke) % 6] * ZETA[(3*kd + 3*ke) % 6]
        dev['T'] = max(dev['T'], abs(lhsT - rhsT))
        lhs = g2d * g2e * ZETA[(-2*kde) % 6] * ZETA[(kd + ke) % 6]
        H = ZETA[(-2*kd - 2*ke) % 6] * G1[d] * G1[e] * ZETA[(-2*ked) % 6]
        rhs = H / math.sqrt(norm(d)*norm(e)) * ZETA[(3*kd + 3*ke) % 6]
        dev['D'] = max(dev['D'], abs(lhs - rhs))
print(f"primes {len(P)}, coprime prime pairs {npairs}, (pair,row) tests {nrows}")
for k, v in dev.items(): print(f"  max dev ({k}) = {v:.2e}")
# NOTE on (N): BBCFH write g(1,c1)(c1/c2)^{-1} = g(c2,c1); by CG Prop 2.1(3), g(c2, c1) = (c2/c1)^{-1} g(1,c1),
# i.e. the symbol is mod c1 evaluated at c2; with cubic reciprocity the two readings coincide (check R).

# (P) stable p-parts
worst = {'g(1,p^2)': 0.0, 'g(p,p^2)-N conj g': 0.0}
small = [p for p in P if norm(p) <= 200]
for p in small:
    worst['g(1,p^2)'] = max(worst['g(1,p^2)'], abs(g((1, 0), [p, p])))
    worst['g(p,p^2)-N conj g'] = max(worst['g(p,p^2)-N conj g'],
                                     abs(g(p, [p, p]) - norm(p)*G1[p].conjugate()))
print(f"p-parts over {len(small)} primes (N p <= 200):")
for k, v in worst.items(): print(f"  max |{k}| = {v:.2e}")
p = small[0]
print(f"  e.g. p = {p}, N p = {norm(p)}: |g(1,p)|^2 = {abs(G1[p])**2:.6f};"
      f" H(p^2,p) = g(1,p) g(p,p^2) = {G1[p]*g(p,[p,p]):.6f} (expect N p^2 = {norm(p)**2})")
