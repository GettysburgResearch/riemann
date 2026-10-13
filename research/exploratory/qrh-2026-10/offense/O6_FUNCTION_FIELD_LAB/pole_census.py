"""pole_census.py -- which polar divisors occur in the y^k-coefficient of the 1/L 'multiple Dirichlet series'.
For every monic row u of exact degree k (lab_core per-row dump, exact 1/L coefficients), recover
L(x,psi_u) = 1/(1/L) mod x^k exactly (Z[omega]), take its inverse roots alpha_j numerically (float, labelled),
and record the angles of alpha_i conj(alpha_j)/q, i.e. the poles of sum_d |[x^d]1/L|^2 t^d at t = 1/(alpha_i conj alpha_j).
Prints the set of denominators N such that every such angle is in (1/N)Z (up to 1e-7), and the angle set
of the inverse roots themselves relative to the CM angle theta0.
Usage: python3 pole_census.py q dumpfile k [tol]
(tol: angle tolerance, default 1e-4; numpy roots of repeated roots are accurate only to ~eps^(1/mult))
"""
import sys, cmath, math
from fractions import Fraction
import numpy as np
q = int(sys.argv[1]); path = sys.argv[2]; K = int(sys.argv[3]); TOL = float(sys.argv[4]) if len(sys.argv) > 4 else 1e-4
W = cmath.exp(2j * cmath.pi / 3)
prod_angles = set(); root_angles = set(); bad = 0; nrows = 0
for line in open(path):
    t = line.split()
    if int(t[0]) != K or int(t[2]) == 1:
        continue
    co = [tuple(map(int, x.split(','))) for x in t[3:]]
    inv = [a + b * W for a, b in co]
    # L = 1/inv mod x^K
    Lc = [1 + 0j] + [0j] * (K - 1)
    for j in range(1, K):
        Lc[j] = -sum(inv[i] * Lc[j - i] for i in range(1, j + 1))
    while len(Lc) > 1 and abs(Lc[-1]) < 1e-9:
        Lc.pop()
    nrows += 1
    if len(Lc) == 1:
        continue
    r = np.roots(Lc[::-1]); al = 1 / r
    for a in al:
        if abs(abs(a) - math.sqrt(q)) > 1e-3 and abs(abs(a) - 1) > 1e-3:
            bad += 1
        root_angles.add(round(cmath.phase(a) / (2 * math.pi) % 1, 3))
    big = [a for a in al if abs(abs(a) - math.sqrt(q)) < 1e-3]   # pairs on |alpha|=sqrt(q) only
    for a in big:
        for b in big:
            ang = cmath.phase(a * b.conjugate()) / (2 * math.pi) % 1
            prod_angles.add(ang)
def denom(x):
    f = Fraction(x).limit_denominator(60)
    return f.denominator if abs(float(f) - x) < TOL else None
dens = sorted({denom(a) for a in prod_angles}, key=lambda z: (z is None, z or 0))
print(f'q={q} k={K} rows={nrows}; inverse roots off the circles |a|=sqrt(q),1: {bad}')
print(f'angles of alpha_i conj(alpha_j)/q, |alpha_i|=|alpha_j|=sqrt(q); their denominators (None = not rational with denom<=400): {dens}')
print(f'distinct inverse-root angles: {len(root_angles)}')
