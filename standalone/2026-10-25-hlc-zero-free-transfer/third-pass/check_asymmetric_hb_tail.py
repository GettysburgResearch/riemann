#!/usr/bin/env python3
"""Exact algebra for ASYMMETRIC_HB_TAIL.md.

This does not certify an imported cap, analytic moment, or open middle band.
All predicates remain active under python -O.
"""

from decimal import Decimal, localcontext
from fractions import Fraction as F
from functools import lru_cache
from math import gcd


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


@lru_cache(None)
def mobius(n):
    out = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            out = -out
        p += 1
    return -out if n > 1 else out


def cutoff(x):
    if x <= 1:
        return F(1)
    if x >= 2:
        return F(0)
    z = x - 1
    return 1 - 10*z**3 + 15*z**4 - 6*z**5


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


hb_cases = 0
repeated_prime_cases = 0
repeated_negative_controls = 0
for y1 in [F(3, 2), F(2), F(5, 2), F(3), F(4), F(7)]:
    for y2 in [F(2), F(7, 2), F(5), F(8), F(11)]:
        nmax = int(y1*y2)
        m1 = {n: mobius(n)*cutoff(F(n)/y1) for n in range(1, nmax+1)}
        m2 = {n: mobius(n)*cutoff(F(n)/y2) for n in range(1, nmax+1)}
        outer, bad_outer = {}, {}
        for n in range(1, nmax+1):
            outer[n] = sum((m1[d]*m2[n//d] for d in divisors(n)), F(0))
            bad_outer[n] = sum(
                (m1[d]*m2[n//d] for d in divisors(n) if gcd(d, n//d) == 1),
                F(0),
            )
            repeated_prime_cases += any(
                gcd(d, n//d) > 1 and m1[d] and m2[n//d]
                for d in divisors(n)
            )
        for n in range(1, nmax+1):
            exact = m1[n]+m2[n]-sum((outer[d] for d in divisors(n)), F(0))
            wrong = m1[n]+m2[n]-sum((bad_outer[d] for d in divisors(n)), F(0))
            require(exact == mobius(n), "Unequal-cutoff convolution identity")
            repeated_negative_controls += wrong != mobius(n)
            hb_cases += 1
require(repeated_negative_controls > 0, "Repeated-prime mutation detected")

# Coefficients of affine polynomials in (1,r,b,alpha). These checks
# establish the endpoint identities generically, not just on a grid.
def add(x, y):
    return tuple(a+b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a-b for a, b in zip(x, y))


def scale(c, x):
    return tuple(c*a for a in x)


one = (F(1), F(0), F(0), F(0))
rr = (F(0), F(1), F(0), F(0))
bb = (F(0), F(0), F(1), F(0))
aa = (F(0), F(0), F(0), F(1))
e0 = add(scale(F(1, 6), one), scale(F(5, 6), rr))
eb_long = add(scale(F(1, 6), one), scale(F(5, 6), bb))
cap = scale(F(3, 4), sub(rr, bb))
gap_long = sub(e0, add(eb_long, cap))
gap_short = sub(e0, add(one, cap))
require(gap_long == scale(F(1, 12), sub(rr, bb)), "Generic long gap")
require(gap_short == (F(-5, 6), F(1, 12), F(3, 4), F(0)),
        "Generic short gap")
# Substitute b=1-alpha into the short gap.
short_endpoint = (
    gap_short[0]+gap_short[2], gap_short[1], F(0),
    gap_short[3]-gap_short[2],
)
require(short_endpoint == scale(F(1, 12),
        sub(sub(rr, one), scale(9, aa))), "Generic short endpoint")
require(
    sub(short_endpoint, scale(F(1, 12), aa))
    == scale(F(1, 12), sub(sub(rr, one), scale(10, aa))),
    "Generic condition r>=1+10alpha",
)


def old(r):
    return (1+5*r)/6


def energy(b):
    return max(F(1), old(b))


alpha = F(2, 125)
gain = alpha/12
require(1+10*alpha == F(29, 25), "Exact lower inverse length")
require(gain == F(1, 750) > F(1, 1000), "Exact usable far-tail gain")
require(gain-F(1, 1000) == F(1, 3000), "Exact margin beyond consumer gain")

range_cases = 0
for rmin in [F(29, 25), F(6, 5), F(3, 2)]:
    for i in range(31):
        r = rmin + F(i, 300)
        for j in range(101):
            b = (1-alpha) + F(j, 100)*(r-1)
            require(1-alpha <= b <= r-alpha, "Admitted longer inverse length")
            exp = energy(b)+F(3, 4)*(r-b)
            require(exp <= old(r)-gain, "Uniform coherent far-tail exponent")
            range_cases += 1

# The largest-b endpoint is exact, and forbids a stronger saving without
# a new estimate. The short endpoint is also exact at r=29/25.
r = F(29, 25)
for b in [1-alpha, r-alpha]:
    require(old(r)-energy(b)-F(3, 4)*(r-b) == gain, "Sharp scalar endpoint")
    require(not (energy(b)+F(3, 4)*(r-b) <= old(r)-F(1, 500)),
            "Negative control detects unsupported far-tail saving")

# Exact generic resource contacts at x=1/2. The kappa<3/4 examples
# are scalar/optimistic checks, not a new analytic field theorem.
def class_data(delta, kappa):
    cc = F(2, 3)/kappa
    C = delta*(4-cc)/(2*(5-cc))
    A = F(5, 6)-delta
    t = 1+C/(2*(A+C))
    R = 1-delta+A*C/(2*(A+C))
    g = delta/2
    b = (1-g-R)/(delta-g)
    c = (1-g/(3*kappa)-R)/(2*delta-2*g/(3*kappa))
    return g, t, R, b, c


def inverse_count(delta, g, ell):
    z = min((1-ell)/2, (3-2*ell)/8)
    return 1-delta*ell-2*g*z


def plain_count(delta, g, kappa, total_plain_length):
    return 1-delta*total_plain_length-g*(1-total_plain_length)/(3*kappa)


contact_cases = 0
individual_compatibility_cases = 0
for kappa in [F(7497, 10000), F(3, 4), F(4, 5), F(1)]:
    for i in range(1, 76):
        delta = F(i, 100)
        g, t, R, b, c = class_data(delta, kappa)
        require(F(1, 2) <= b <= 1 and 0 <= c <= F(1, 2), "Witness lengths")
        require(b+c == t, "Generic inverse/plain contact lengths")
        require(inverse_count(delta, g, b) == R, "Marked inverse contact")
        require(plain_count(delta, g, kappa, 2*c) == R, "Marked plain contact")
        require(R+delta*t == old(t), "Old complete inverse self-contact")
        plain_density = (15-16*delta)/(15-6*delta)
        require(R <= plain_density, "Inverse-power envelope permits class")
        require(R+delta/2 < 1, "Generic higher ordinary moments permit class")
        for j in range(21):
            ell = b*F(j, 20)
            nsum = 2*c*F(j, 20)
            require(inverse_count(delta, g, ell) >= R,
                    "Splitting inverse factors does not exclude class")
            require(plain_count(delta, g, kappa, nsum) >= R,
                    "Splitting plain factors does not exclude class")
            individual_compatibility_cases += 2
        contact_cases += 1

print("EXACT unequal-cutoff HB cases:", hb_cases, "PASS")
print("EXACT repeated-prime cases:", repeated_prime_cases, "PASS")
print("NEGATIVE repeated-prime failures detected:", repeated_negative_controls)
print("EXACT generic affine gap identities: 4 PASS")
print("EXACT far-tail range cases:", range_cases, "PASS")
print("EXACT saving:", gain, "; consumer margin:", gain-F(1, 1000))
print("NEGATIVE excessive-saving endpoint control: PASS")
print("EXACT generic critical-pair contacts:", contact_cases, "PASS")
print("EXACT individual resource compatibility cases:",
      individual_compatibility_cases, "PASS")


def bisect(fun, lo, hi, rounds=210):
    flo = fun(lo)
    require(flo*fun(hi) < 0, "Diagnostic sign bracket")
    for _ in range(rounds):
        mid = (lo+hi)/2
        fm = fun(mid)
        if fm == 0 or mid == lo or mid == hi:
            return mid
        if flo*fm < 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo+hi)/2


with localcontext() as ctx:
    ctx.prec = 60
    D = Decimal
    def quartic(k):
        return 16686*k**4-27405*k**3+9936*k**2+1290*k-275

    k = bisect(quartic, D(".749773294079928"), D(".749773294079929"))
    def critical(d):
        return ((3-324*k*k)*d*d+(756*k*k-54*k-5)*d+40*k-300*k*k)

    delta = bisect(critical, D(".469"), D(".47"))
    g = delta/2
    cc = 2/(3*k)
    C = delta*(4-cc)/(2*(5-cc))
    A = D(5)/6-delta
    t = 1+C/(2*(A+C))
    R = 1-delta+A*C/(2*(A+C))
    b = (1-g-R)/(delta-g)
    c = (1-g/(3*k)-R)/(2*delta-2*g/(3*k))
    require(abs(b+c-t) < D("1e-54"), "Diagnostic critical pair")
    require(D(".65") < b < 1 and b < t-D(2)/125,
            "Diagnostic middle-block placement")
    print("DECIMAL DIAGNOSTICS (resource comparison only):")
    for name, value in [
        ("critical r", t), ("critical inverse-product length", b),
        ("critical plain length", c), ("critical row count", R),
        ("old full inverse exponent", (1+5*t)/6),
        ("proved far-tail exponent", (1+5*t)/6-D(1)/750),
    ]:
        print(" ", name, "=", value)

print("No imported analytic theorem, open middle band, new region, or RH certified.")
