#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import Path
import json
import sys

sys.set_int_max_str_digits(1000000)


@dataclass(frozen=True)
class I:
    lo: Fraction
    hi: Fraction

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

    def __truediv__(self, other):
        other = as_i(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return as_i(other) / self


def as_i(x):
    if isinstance(x, I):
        return x
    if not isinstance(x, Fraction):
        x = Fraction(x)
    return I(x, x)


K = 4
X_LEFT = Fraction(1)
X_RIGHT = Fraction(67)
MAX_N = (4**K) * int(X_RIGHT)
SQRT_DEN = 10**55
LOG_TERMS = 90


@lru_cache(maxsize=None)
def sqrt_q(x: Fraction) -> I:
    x = Fraction(x)
    scaled = (x.numerator * SQRT_DEN * SQRT_DEN) // x.denominator
    r = isqrt(scaled)
    return I(Fraction(r, SQRT_DEN), Fraction(r + 1, SQRT_DEN))


@lru_cache(maxsize=None)
def log_two() -> I:
    z = Fraction(1, 3)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(LOG_TERMS):
        partial += power / Fraction(2 * j + 1)
        power *= z2
    partial *= 2
    tail = 2 * power / (Fraction(2 * LOG_TERMS + 1) * (1 - z2))
    return I(partial, partial + tail)


@lru_cache(maxsize=None)
def log_q(x: Fraction) -> I:
    x = Fraction(x)
    if x <= 0:
        raise ValueError("log argument must be positive")
    exponent = 0
    y = x
    while y >= 2:
        y /= 2
        exponent += 1
    while y < 1:
        y *= 2
        exponent -= 1
    if y == 1:
        base = I(Fraction(0), Fraction(0))
    else:
        z = (y - 1) / (y + 1)
        z2 = z * z
        power = z
        partial = Fraction(0)
        for j in range(LOG_TERMS):
            partial += power / Fraction(2 * j + 1)
            power *= z2
        partial *= 2
        tail = 2 * power / (Fraction(2 * LOG_TERMS + 1) * (1 - z2))
        base = I(partial, partial + tail)
    return base + exponent * log_two()


@lru_cache(maxsize=None)
def invsqrt(n: int) -> I:
    return 1 / sqrt_q(Fraction(n))


def linear_sieves(limit: int):
    mu = [0] * (limit + 1)
    spf = [0] * (limit + 1)
    primes: list[int] = []
    mu[1] = 1
    for n in range(2, limit + 1):
        if spf[n] == 0:
            spf[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if p > spf[n] or p * n > limit:
                break
            spf[p * n] = p
            if n % p == 0:
                mu[p * n] = 0
                break
            mu[p * n] = -mu[n]
    return mu, spf


def prime_power_base(n: int, spf: list[int]) -> tuple[int, int] | None:
    if n < 2:
        return None
    p = spf[n]
    m = n
    exponent = 0
    while m % p == 0:
        m //= p
        exponent += 1
    if m == 1:
        return p, exponent
    return None


def prefixes():
    mu, spf = linear_sieves(MAX_N)
    mobius_over_n = [Fraction(0)] * (MAX_N + 1)
    mobius_over_sqrt = [I(Fraction(0), Fraction(0)) for _ in range(MAX_N + 1)]
    theta_half = [I(Fraction(0), Fraction(0)) for _ in range(MAX_N + 1)]
    theta_log_half = [I(Fraction(0), Fraction(0)) for _ in range(MAX_N + 1)]

    a = Fraction(0)
    b = I(Fraction(0), Fraction(0))
    c = I(Fraction(0), Fraction(0))
    d = I(Fraction(0), Fraction(0))
    for n in range(1, MAX_N + 1):
        if mu[n]:
            a += Fraction(mu[n], n)
            b += mu[n] * invsqrt(n)
        pp = prime_power_base(n, spf)
        if pp is not None:
            p, exponent = pp
            lp = log_q(Fraction(p))
            lam_over_sqrt = lp * invsqrt(n)
            c += lam_over_sqrt
            d += exponent * lp * lp * invsqrt(n)
        mobius_over_n[n] = a
        mobius_over_sqrt[n] = b
        theta_half[n] = c
        theta_log_half[n] = d
    return mobius_over_n, mobius_over_sqrt, theta_half, theta_log_half


A_PREFIX, B_PREFIX, C_PREFIX, D_PREFIX = prefixes()
LOG4 = 2 * log_two()


def cell_coefficients(ns: tuple[int, ...]) -> tuple[I, I, I]:
    # On a common arithmetic cell,
    #   sum_j 2^-j D(4^j x) = alpha sqrt(x) + beta log(x) + gamma.
    alpha = I(Fraction(0), Fraction(0))
    beta = I(Fraction(0), Fraction(0))
    gamma = I(Fraction(0), Fraction(0))
    for j, n in enumerate(ns):
        weight = Fraction(1, 2**j)
        alpha += 5 * A_PREFIX[n]
        beta -= weight * C_PREFIX[n]
        gamma -= 3 * weight * B_PREFIX[n]
        gamma -= weight * j * C_PREFIX[n] * LOG4
        gamma += weight * D_PREFIX[n]
    return alpha, beta, gamma


def value_interval(a: Fraction, b: Fraction, ns: tuple[int, ...]) -> I:
    alpha, beta, gamma = cell_coefficients(ns)
    sx = I(sqrt_q(a).lo, sqrt_q(b).hi)
    lx = I(log_q(a).lo, log_q(b).hi)
    return alpha * sx + beta * lx + gamma


def interior_ns(a: Fraction, b: Fraction) -> tuple[int, ...]:
    mid = (a + b) / 2
    return tuple(int((4**j) * mid) for j in range(K + 1))


def point_ns(x: Fraction) -> tuple[int, ...]:
    return tuple(int((4**j) * x) for j in range(K + 1))


def certify_interval(a: Fraction, b: Fraction, depth: int = 0) -> tuple[Fraction, int]:
    ns = interior_ns(a, b)
    iv = value_interval(a, b, ns)
    if iv.hi < 0:
        return iv.hi, 1
    if depth >= 10:
        raise AssertionError(("unresolved cell", a, b, ns, float(iv.lo), float(iv.hi)))
    mid = (a + b) / 2
    left_hi, left_count = certify_interval(a, mid, depth + 1)
    right_hi, right_count = certify_interval(mid, b, depth + 1)
    return max(left_hi, right_hi), left_count + right_count


def certify():
    base_den = 4**K
    start = int(X_LEFT * base_den)
    stop = int(X_RIGHT * base_den)
    maximum_hi: Fraction | None = None
    maximum_where = None
    interval_boxes = 0
    point_checks = 0

    # One-sided values on every open common cell.
    for k in range(start, stop):
        a = Fraction(k, base_den)
        b = Fraction(k + 1, base_den)
        hi, count = certify_interval(a, b)
        interval_boxes += count
        if maximum_hi is None or hi > maximum_hi:
            maximum_hi = hi
            maximum_where = ("cell", str(a), str(b))

    # Activated point values at every common knot, including both endpoints.
    for k in range(start, stop + 1):
        x = Fraction(k, base_den)
        ns = point_ns(x)
        iv = value_interval(x, x, ns)
        assert iv.hi < 0, ("point", x, ns, float(iv.lo), float(iv.hi))
        point_checks += 1
        if maximum_hi is None or iv.hi > maximum_hi:
            maximum_hi = iv.hi
            maximum_where = ("point", str(x), str(x))

    assert maximum_hi is not None and maximum_hi < 0
    result = {
        "classification": "PASS_WEIGHTED_QUARTER_CASCADE_K4",
        "cascade": "sum_{j=0}^4 2^{-j} D(4^j x)",
        "frontier": "1 <= x <= 67",
        "largest_arithmetic_argument": MAX_N,
        "base_common_cells": stop - start,
        "directed_interval_boxes": interval_boxes,
        "activated_point_checks": point_checks,
        "maximum_upper_decimal": float(maximum_hi),
        "maximum_location": maximum_where,
        "strict_sign": "negative",
        "scope": (
            "Exact Mobius/von-Mangoldt prefix arithmetic. Square roots and "
            "logarithms use directed rational enclosures; every common arithmetic "
            "cell is bounded recursively and every activated knot is checked. "
            "This certifies the scalar cascade only, not its physical endpoint "
            "coupling or RH."
        ),
    }
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(out)


if __name__ == "__main__":
    certify()
