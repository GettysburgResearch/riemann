#!/usr/bin/env python3
"""Exact rational-interval certificate for the finite margins in L-90005.

Only the Python standard library is used.  Algebraic square roots are enclosed
by rational intervals using integer square roots.  Logarithms are enclosed by
the positive atanh series

    log x = 2 * sum_{k>=0} y^(2k+1)/(2k+1),  y=(x-1)/(x+1),

with an exact geometric tail bound after power-of-two range reduction.

The cofinal/infinite inequalities in L-90005 remain analytic; this file certifies
the finite seed inequalities and displayed numerical margins used by that proof.
"""

from fractions import Fraction as F
from math import isqrt


class I:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_i(other))

    def __rsub__(self, other):
        return as_i(other) - self

    def __mul__(self, other):
        other = as_i(other)
        vals = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def inv(self):
        assert self.lo > 0 or self.hi < 0
        return I(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other):
        return self * as_i(other).inv()

    def __rtruediv__(self, other):
        return as_i(other) / self


def as_i(x):
    return x if isinstance(x, I) else I(x)


SCALE = 10**24


def sqrt_q(x):
    """Rigorous rational interval enclosing sqrt(x), x rational >= 0."""
    x = F(x)
    assert x >= 0
    a = isqrt((x.numerator * SCALE * SCALE) // x.denominator)
    while F((a + 1) ** 2, SCALE * SCALE) <= x:
        a += 1
    while F(a * a, SCALE * SCALE) > x:
        a -= 1
    lo = F(a, SCALE)
    if lo * lo == x:
        return I(lo)
    return I(lo, F(a + 1, SCALE))


def log_direct(x, terms=60):
    """Rigorous log interval from the atanh series; intended for 1<=x<=2."""
    x = F(x)
    assert x > 0
    if x < 1:
        return -log_direct(1 / x, terms)
    y = (x - 1) / (x + 1)
    y2 = y * y
    term = y
    partial = F(0)
    for k in range(terms):
        partial += term / F(2 * k + 1)
        term *= y2
    lo = 2 * partial
    # All terms are positive.  Bound every remaining denominator below by the
    # first omitted one and sum the geometric tail exactly.
    rem = 2 * term / F(2 * terms + 1) / (1 - y2)
    return I(lo, lo + rem)


LOG2 = log_direct(2)


def log_q(x):
    """Rigorous log interval with exact power-of-two range reduction."""
    x = F(x)
    assert x > 0
    m = 0
    while x >= 2:
        x /= 2
        m += 1
    while x < 1:
        x *= 2
        m -= 1
    return m * LOG2 + log_direct(x)


def log_i(x):
    assert x.lo > 0
    return I(log_q(x.lo).lo, log_q(x.hi).hi)


SQRT2 = sqrt_q(2)


def sums(n):
    s = I(0)
    a = I(0)
    for k in range(1, n + 1):
        inv_sqrt = sqrt_q(k).inv()
        s += inv_sqrt
        a += log_q(k) * inv_sqrt
    return s, a


def pars(n):
    m = n // 2
    s, a = sums(n)
    sm, am = sums(m)
    d = s - sm
    c = a - am + 4 * d - (sm + 1) * LOG2
    k = 4 * (I(n) - SQRT2 * m)
    return m, d, c, k


def q_value(n):
    _, d, c, k = pars(n)
    x = sqrt_q(F(1, n))
    logx = -log_q(n) / 2
    return c + 2 * d * logx - k * x


def x_crit(n):
    _, d, _, k = pars(n)
    return 2 * d / k


def p_at_x(n, x):
    _, d, c, k = pars(n)
    return c + 2 * d * log_i(x) - k * x


def p_at_theta(n, theta):
    theta = F(theta)
    _, d, c, k = pars(n)
    return c + d * log_q(theta) - k * sqrt_q(theta)


def inv_pow_3_2(x):
    x = F(x)
    return (I(x) * sqrt_q(x)).inv()


def nondiv_correction_lower(n):
    """Lower bound for C/h in L-90005.25."""
    m = n // 2
    pos = I(0)
    neg = I(0)
    for k in range(1, m + 1):
        pos += inv_pow_3_2(F(2 * k + 1, 2))
    for k in range(m + 1, n + 1):
        neg += inv_pow_3_2(k)
    return LOG2 * pos / 4 - neg / 2


def div_correction_lower(n):
    """Lower bound for C/h when q|Y and n=2m."""
    assert n % 2 == 0
    m = n // 2
    pos = I(0)
    neg = I(0)
    for k in range(1, m):
        pos += inv_pow_3_2(F(2 * k + 1, 2))
    for k in range(m, 2 * m):
        neg += inv_pow_3_2(k)
    return LOG2 * pos / 4 - neg / 2


def f_bound(m):
    """F(m) from L-90005.26."""
    return (
        LOG2
        * (sqrt_q(F(2, 3)) - sqrt_q(F(2, 2 * m + 3)))
        / 2
        - (sqrt_q(F(2, 2 * m + 1)) - sqrt_q(F(2, 4 * m + 3)))
    )


# ---------------------------------------------------------------------------
# Finite certificates used by L-90005.
# ---------------------------------------------------------------------------

# The three small even knot increments omitted from the cofinal analytic proof.
for n in (2, 4, 6):
    assert (q_value(n + 1) - q_value(n)).lo > 0

q7 = q_value(7)
q8 = q_value(8)
assert q7.lo > F(-4857, 10**6) and q7.hi < F(-4856, 10**6)
assert q8.lo > F(32916, 10**6) and q8.hi < F(32918, 10**6)

# Interior maxima in the only even cells whose negative endpoints require a
# concavity check.
for n, upper in (
    (2, F(-1960, 10**4)),
    (4, F(-684, 10**4)),
    (6, F(-43, 10**4)),
):
    xc = x_crit(n)
    assert p_at_x(n, xc).hi < upper

# For odd N=3,5,7 the concave critical point lies to the left of the cell, so
# P_N is decreasing across the whole cell.
for n in (3, 5, 7):
    assert x_crit(n).hi < sqrt_q(F(1, n + 1)).lo

# Rigorous bracket for the unique N=7 root.
root_lo = F(14085203501383, 10**14)
root_hi = F(14085203501385, 10**14)
assert p_at_theta(7, root_lo).lo > 0
assert p_at_theta(7, root_hi).hi < 0
assert root_lo > F(14, 100)  # also supplies the coarse c_*>0.14 bound.

# P_7'(theta) is decreasing throughout [1/8,1/7]: its second derivative has
# sign of -D + (K/4)sqrt(theta), and the latter is already negative at 1/7.
_, d7, _, k7 = pars(7)
assert (k7 * sqrt_q(F(1, 7))).hi < (4 * d7).lo
p7_prime_at_eighth = d7 / I(F(1, 8)) - k7 / (2 * sqrt_q(F(1, 8)))
assert p7_prime_at_eighth.hi < F(-17, 10)

# Transition-cell secant correction constants in L-90005.29.
upper_pos = I(0)
for k in range(1, 4):
    upper_pos += inv_pow_3_2(k)
upper_corr = LOG2 * upper_pos / 4

upper_neg = I(0)
for k in range(4, 8):
    upper_neg += inv_pow_3_2(k)
lower_corr = -upper_neg / 2

assert lower_corr.lo > F(-169, 1000)
assert upper_corr.hi < F(268, 1000)

# The scalar lower-bound function F(M) used for all cofinal nondivisible and
# divisible cases starts positive at M=5.  Its derivative is positive
# analytically (the positive second term alone dominates the negative term).
assert f_bound(5).lo > F(155, 10**4)

# Remaining direct secant cases.
assert nondiv_correction_lower(8).lo > 0
assert nondiv_correction_lower(9).lo > F(364, 10**4)
assert div_correction_lower(10).lo > 0
assert div_correction_lower(8).lo > F(-3612, 10**6)

print("PASS_X90005_EXACT_FINITE_CERTIFICATE")
print("Q7 enclosure:", float(q7.lo), float(q7.hi))
print("Q8 enclosure:", float(q8.lo), float(q8.hi))
print("root bracket:", float(root_lo), float(root_hi))
print("P7'(1/8) upper:", float(p7_prime_at_eighth.hi))
print("transition C/h lower:", float(lower_corr.lo))
print("transition C/h upper:", float(upper_corr.hi))
print("F(5) lower:", float(f_bound(5).lo))
print("q|Y, N=8 C/h lower:", float(div_correction_lower(8).lo))
