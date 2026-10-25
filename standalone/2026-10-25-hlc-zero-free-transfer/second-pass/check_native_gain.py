#!/usr/bin/env python3
"""Exact finite control of the twisted Gauss-inverse decomposition.

This is a synthetic commutative sextic-symbol model over Z[zeta_6], not
an implementation of the actual Eisenstein Gauss sums or an analytic
estimate.  Its bilinear symbol has the same cocycle and natural-zero
identities used by NATIVE_GAIN.md.  All arithmetic is exact.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import gcd, isqrt
import json


class Z6:
    """a+b*z, z^2=z-1."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = Q(a), Q(b)

    def __add__(self, other):
        if not isinstance(other, Z6):
            other = Z6(other)
        return Z6(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Z6(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, Z6):
            other = Z6(other)
        return Z6(self.a * other.a - self.b * other.b,
                  self.a * other.b + self.b * other.a + self.b * other.b)

    __rmul__ = __mul__

    def __eq__(self, other):
        if not isinstance(other, Z6):
            other = Z6(other)
        return self.a == other.a and self.b == other.b


ZERO, ONE = Z6(), Z6(1)
ROOT = [ONE]
for _ in range(5):
    ROOT.append(ROOT[-1] * Z6(0, 1))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def factors(n):
    result = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        if e:
            result.append((p, e))
        p += 1
    if n > 1:
        result.append((n, 1))
    return tuple(result)


def mobius(n):
    f = factors(n)
    return 0 if any(e > 1 for _, e in f) else (-1) ** len(f)


def interaction(p, q):
    # Symmetric prime-pair phase; the true cubic Gauss cocycle is chi^4.
    return (p * q + p + q) % 6


def symbol(n, u):
    if gcd(n, u) != 1:
        return ZERO
    exponent = sum(en * eu * interaction(p, q)
                   for p, en in factors(n) for q, eu in factors(u))
    return ROOT[exponent % 6]


def twist(a, b):
    if gcd(a, b) != 1:
        return ZERO
    exponent = 4 * sum(ea * eb * interaction(p, q)
                       for p, ea in factors(a) for q, eb in factors(b))
    return ROOT[exponent % 6]


def gauss(n):
    if mobius(n) == 0:
        return ZERO
    primes = [p for p, _ in factors(n)]
    exponent = sum((p * p + 1) % 6 for p in primes)
    exponent += 4 * sum(interaction(p, q)
                        for i, p in enumerate(primes) for q in primes[i+1:])
    return ROOT[exponent % 6]


def unitary_convolve(a, b, limit):
    c = [ZERO for _ in range(limit + 1)]
    for d in range(1, limit + 1):
        if a[d] == ZERO:
            continue
        for e in range(1, limit // d + 1):
            if b[e] != ZERO and gcd(d, e) == 1:
                c[d * e] = c[d * e] + a[d] * b[e] * twist(d, e)
    return c


def divisor_count_y(n, y):
    return sum(1 for d in range(1, min(n, y) + 1)
               if n % d == 0 and n // d <= y and gcd(d, n // d) == 1)


def profile(n, D):
    return Q((n-D)*(2*D-n), D*D) if D < n < 2*D else Q(0)


def main():
    limit = 3000
    g = [ZERO] + [gauss(n) for n in range(1, limit + 1)]
    f = [ZERO] + [mobius(n) * g[n] for n in range(1, limit + 1)]
    inverse = unitary_convolve(g, f, limit)
    for n in range(1, limit + 1):
        require(inverse[n] == (ONE if n == 1 else ZERO), f"inverse at {n}")

    hb_counts = []
    for k, y in [(2, 17), (3, 7)]:
        gy = [g[n] if n <= y else ZERO for n in range(limit + 1)]
        gy2 = unitary_convolve(gy, gy, limit)
        gy2f = unitary_convolve(gy2, f, limit)
        if k == 2:
            hb = [2*gy[n] - gy2f[n] for n in range(limit + 1)]
        else:
            gy3 = unitary_convolve(gy2, gy, limit)
            f2 = unitary_convolve(f, f, limit)
            gy3f2 = unitary_convolve(gy3, f2, limit)
            hb = [3*gy[n] - 3*gy2f[n] + gy3f2[n]
                  for n in range(limit + 1)]
        for n in range(1, y**k + 1):
            require(hb[n] == g[n], f"Heath-Brown k={k}, n={n}")
        require(any(hb[n] != g[n] for n in range(y**k+1, limit+1)),
                "support restriction negative control failed")
        hb_counts.append({"k": k, "y": y, "checked": y**k})

    transport_cases = 0
    wrong_twist_failures = 0
    for D in [20, 35, 60]:
        y = isqrt(2*D)
        if y*y < 2*D:
            y += 1
        for u in range(1, 13):
            for mask in [1, 7]:
                lhs = sum((g[n] * symbol(n, u) * profile(n, D)
                           for n in range(D+1, 2*D) if gcd(n, mask) == 1), ZERO)
                rhs, wrong = ZERO, ZERO
                for r in range(1, 2*D):
                    if mobius(r) == 0 or gcd(r, mask) != 1:
                        continue
                    dy = divisor_count_y(r, y)
                    if not dy:
                        continue
                    outside = dy * g[r] * symbol(r, u)
                    for c in range(1, (2*D-1)//r + 1):
                        n = r*c
                        w = profile(n, D)
                        if not w or gcd(c, r*mask) != 1:
                            continue
                        inside = f[c] * w
                        rhs = rhs - outside * inside * symbol(c, u*r**4)
                        wrong = wrong - outside * inside * symbol(c, u*r**3)
                require(lhs == rhs, f"row transport D={D}, u={u}, mask={mask}")
                transport_cases += 1
                wrong_twist_failures += (lhs != wrong)
    require(wrong_twist_failures > 0, "twist-power mutation was not detected")

    # Deleting the cocycle changes at least one exact multiplicative identity.
    omitted_cocycle_failures = sum(
        gauss(a*b) != gauss(a)*gauss(b)
        for a in range(2, 20) for b in range(a+1, 20)
        if mobius(a*b) != 0)
    require(omitted_cocycle_failures > 0, "cocycle mutation was not detected")
    print(json.dumps({
        "arithmetic": "exact Q(zeta_6); synthetic bilinear symbol, not native Gauss data",
        "twisted_inverse_coefficients": limit,
        "finite_Heath_Brown": hb_counts,
        "exact_row_transport_cases": transport_cases,
        "wrong_row_twist_power_rejections": wrong_twist_failures,
        "omitted_cocycle_rejections": omitted_cocycle_failures,
        "analytic_claim": "none; no asymptotic cancellation tested"
    }, indent=2))


if __name__ == "__main__":
    main()
