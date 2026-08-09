#!/usr/bin/env python3
"""Regression checks for L-90005.

The theorem in L-90005 is analytic.  This script is deliberately only a
high-precision / floating regression harness: it checks the finite profile
brackets, the corrected N=7 root, direct exact-shell values, and searches for
transition anomalies near c_* X.  It is not used to justify the cofinal proof.
"""

from decimal import Decimal, getcontext
import math

getcontext().prec = 80
D = Decimal
SQRT2 = D(2).sqrt()
LOG2 = D(2).ln()


def dsqrt(x):
    return D(x).sqrt()


def dlog(x):
    return D(x).ln()


def sums(n):
    s = D(0)
    a = D(0)
    for k in range(1, n + 1):
        kd = D(k)
        s += 1 / dsqrt(kd)
        a += dlog(kd) / dsqrt(kd)
    return s, a


def pars(n):
    m = n // 2
    s, a = sums(n)
    sm, am = sums(m)
    dn = s - sm
    cn = a - am + 4 * dn - (sm + 1) * LOG2
    kn = 4 * (D(n) - SQRT2 * D(m))
    return m, dn, cn, kn


def profile(n, x):
    _, dn, cn, kn = pars(n)
    return cn + 2 * dn * dlog(x) - kn * x


def profile_theta(n, theta):
    return profile(n, dsqrt(theta))


def root7():
    lo = D(1) / 8
    hi = D(1) / 7
    for _ in range(300):
        mid = (lo + hi) / 2
        # P_7 is decreasing on this cell.
        if profile_theta(7, mid) > 0:
            lo = mid
        else:
            hi = mid
    return lo, hi


def b_float(X, m):
    if m < 2 or m > X:
        return 0.0
    return 2.0 * math.sqrt(m) * (
        math.log(X / m) - 2.0 * (1.0 - math.sqrt(m / X))
    )


def r_float(X, q):
    v = 0.0
    for k in range(1, X // q + 1):
        v += b_float(X, k * q) - b_float(X, k * q + 1)
    return v - math.log(X / q) / math.sqrt(q)


def shell_float(X, q):
    y = X // 2
    return r_float(X, q) - (r_float(y, q) if q <= y else 0.0)


lo, hi = root7()
assert D("0.14085203501383") < lo < hi < D("0.14085203501385")
cstar = float((lo + hi) / 2)

q7 = profile(7, D(1) / dsqrt(7))
q8 = profile(8, D(1) / dsqrt(8))
assert D("-0.004857") < q7 < D("-0.004856")
assert D("0.032916") < q8 < D("0.032918")

for n, limit in [(2, D("-0.1960")), (4, D("-0.0684")), (6, D("-0.0043"))]:
    _, dn, _, kn = pars(n)
    xc = 2 * dn / kn
    mx = max(
        profile(n, D(1) / dsqrt(n)),
        profile(n, D(1) / dsqrt(n + 1)),
        profile(n, xc),
    )
    assert mx < limit, (n, mx)

# Exact-definition spot checks, including the small-X sign reversals which
# motivate a bounded transition window rather than a literal finite-X root.
assert shell_float(12, 2) > 0.0
assert shell_float(232, 34) > 0.0
assert shell_float(234, 34) < 0.0

# Search the only dangerous area (near c_* X) at every even endpoint through
# 20,000.  The theorem uses width 158; the observed finite window is far tighter.
max_positive_overshoot = (-1.0, None)
for X in range(4, 20002, 2):
    center = cstar * X
    q0 = max(2, int(math.floor(center)) - 12)
    q1 = min(X // 2, int(math.floor(center)) + 13)
    for q in range(q0, q1 + 1):
        s = shell_float(X, q)
        disp = q - center
        if q <= center - 1.0:
            assert s > -2e-12, ("positive-side", X, q, s, disp)
        if q >= center + 3.0:
            assert s < 2e-12, ("negative-side empirical +3", X, q, s, disp)
        if disp > 0 and s > 0 and disp > max_positive_overshoot[0]:
            max_positive_overshoot = (disp, (X, q, s))

print("PASS_X90005")
print("cstar bracket:", lo, hi)
print("Q7:", q7)
print("Q8:", q8)
print("largest positive overshoot through X=20000:", max_positive_overshoot)
