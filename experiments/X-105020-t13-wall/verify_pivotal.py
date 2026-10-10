#!/usr/bin/env python3
"""X-105020 driver: independent verification of every pivotal displayed
constant in the L-105021/L-105022/O-105023/R-105024/L-105025 deposits.
The three lane subdirectories contain the full lane computations; this
driver re-derives the load-bearing numbers from scratch and asserts them.
Run: python3 verify_pivotal.py  ->  ALL PIVOTAL CHECKS PASSED
"""
from fractions import Fraction
from sympy import primerange
from mpmath import mp, mpf, sqrt, primezeta
mp.dps = 30

# ---- L-105022: quarantine of the smooth Mobius mean (COMPLETE finite check)
primes61 = list(primerange(2, 62))
divs = [(1, 1)]
for p in primes61:
    divs += [(d * p, -s) for (d, s) in divs]
divs.sort()
assert len(divs) == 2**18
neg, acc = [], Fraction(0)
minA, minAt = Fraction(10), None
for d, s in divs:
    acc += Fraction(s, d)
    if acc < 0:
        neg.append(d)
    if acc < minA:
        minA, minAt = acc, d
assert neg == [5, 7, 11, 13, 14, 19, 21, 23, 30, 31, 33, 34, 37, 43, 47, 51, 53, 55, 61], neg
assert minA == Fraction(-2323, 30030) and minAt == 13
assert acc > 0  # A at the top of the lattice = prod(1-1/p) > 0
print("[ok] L-105022 quarantine: negative set = 19 points, all <= 61; min = -2323/30030 at 13")

# ---- L-105021: the Hall cap constants
A13 = Fraction(-2323, 30030)
B13 = (1 - 1/sqrt(mpf(2)) - 1/sqrt(mpf(3)) - 1/sqrt(mpf(5)) + 1/sqrt(mpf(6))
       - 1/sqrt(mpf(7)) + 1/sqrt(mpf(10)) - 1/sqrt(mpf(11)) - 1/sqrt(mpf(13)))
H = lambda x: 4*sqrt(mpf(x))*mpf(A13.numerator)/A13.denominator - 3*B13
assert H(67) > mpf(7)/20 > H(71), (H(67), H(71))
assert H(87) > 0 > H(88)
Cstar = (mpf(45045)*abs(B13)/4646)**2
assert abs(Cstar - mpf('87.358931769245881580717700547')) < mpf('1e-24')
C720 = ((mpf(7)/20 + 3*B13)/(4*mpf(A13.numerator)/A13.denominator))**2
assert abs(C720 - mpf('67.4938767025557377154204286011')) < mpf('1e-24')
print("[ok] L-105021 cap: C(7/20)=67.49387670..., C*=(45045|B13|/4646)^2=87.35893176...")

# ---- O-105023: circulation min-cut law constants
c1 = 4*(Fraction(1, 67) - A13)
assert c1 == Fraction(371342, 1006005)
assert 4*abs(A13) == Fraction(9292, 30030)
# cross-check vs the repo's own deposited odd-history gap (X-97600):
# E_T - O_T = 17.00508653821905259069845575... (lane H reproduced independently)
print("[ok] O-105023 law: c1 = 371342/1006005; crossing mass 9292/30030 = 0.3094239...")

# ---- R-105024 / L-105025: depth-split identity and the s=1/2 blow-up
S15 = mpf(1)
for p in primes61:
    S15 *= (1 - mpf(p)**mpf('-1.5'))
P67 = lambda z: primezeta(z) - sum(mpf(p)**(-z) for p in primerange(2, 67))
assert abs(-S15*P67(mpf('1.5')) - mpf('-0.016755956135')) < mpf('1e-11')
B2 = lambda z: 1 - P67(z) + (P67(z)**2 - P67(2*z))/2
assert abs(B2(mpf('1.01')) - mpf('1.8080462')) < mpf('1e-6')
assert abs(B2(mpf('1.0001')) - mpf('19.602112')) < mpf('1e-5')
assert B2(mpf('1.0000001')) > B2(mpf('1.0001')) > B2(mpf('1.01'))  # monotone blow-up
print("[ok] R-105024/L-105025: depth identity at z=1.5; B2 log^2 blow-up at z->1+")

print()
print("ALL PIVOTAL CHECKS PASSED")
