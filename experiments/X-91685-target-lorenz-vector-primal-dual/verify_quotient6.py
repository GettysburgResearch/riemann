#!/usr/bin/env python3
"""Directed exact endpoint replay for the quotient-five-to-six P5 row."""
from __future__ import annotations
from decimal import Decimal, localcontext, ROUND_HALF_EVEN
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import Path
import hashlib
import json

DEN = 10**70
LOG_EPS = Fraction(3, 10**110)


class I:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = Fraction(lo)
        self.hi = Fraction(lo if hi is None else hi)
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

    def __truediv__(self, other):
        other = as_i(other)
        assert not (other.lo <= 0 <= other.hi)
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return as_i(other) / self


def as_i(x):
    return x if isinstance(x, I) else I(x)


@lru_cache(None)
def sqrt_i(q):
    q = Fraction(q)
    a = q.numerator
    b = q.denominator
    lo = isqrt(a * DEN * DEN // b)
    while Fraction((lo + 1) ** 2, DEN**2) <= q:
        lo += 1
    while Fraction(lo**2, DEN**2) > q:
        lo -= 1
    hi = lo if Fraction(lo**2, DEN**2) == q else lo + 1
    return I(Fraction(lo, DEN), Fraction(hi, DEN))


@lru_cache(None)
def invsqrt_i(n):
    return 1 / sqrt_i(n)


@lru_cache(None)
def log_i(q):
    q = Fraction(q)
    with localcontext() as ctx:
        ctx.prec = 120
        ctx.rounding = ROUND_HALF_EVEN
        v = Decimal(q.numerator).ln() - Decimal(q.denominator).ln()
    f = Fraction(v)
    return I(f - LOG_EPS, f + LOG_EPS)


@lru_cache(None)
def gamma_i(j, m):
    if m == j:
        return Fraction(j + 1, j - 1) * invsqrt_i(j)
    if m == j + 1:
        return -Fraction((j + 1) * (j - 2), j * (j - 1)) * invsqrt_i(j + 1)
    if m >= j + 2:
        return Fraction(2, j * (j - 1)) * invsqrt_i(m)
    return I(0)


@lru_cache(None)
def q_i(Y, j):
    Y = Fraction(Y)
    N = Y.numerator // Y.denominator
    if N < j:
        return I(0)
    ans = I(0)
    for m in range(j, N + 1):
        ans += gamma_i(j, m) * log_i(Y / Fraction(m))
    return ans


def main():
    minimum = None
    count = 0
    for j in range(12, 67):
        lo = max(67, 5 * j)
        hi = 6 * j
        if lo > hi:
            continue
        for x in range(lo, hi + 1):
            value = q_i(Fraction(x), j)
            for d in (2, 3, 5):
                value -= invsqrt_i(d) * q_i(Fraction(x, d), j)
            assert value.lo > 0, (j, x, float(value.lo))
            rec = (value.lo, j, x)
            if minimum is None or rec < minimum:
                minimum = rec
            count += 1
    assert minimum is not None
    assert minimum[0] > Fraction(1, 10**6)
    payload = {
        "arithmetic_class": "DIRECTED_RATIONAL_INTERVAL",
        "classification": "PASS_P5_ROW_THROUGH_QUOTIENT_SIX",
        "domain": "max(67,5j)<=x<=6j; cell interiors follow from affine dependence on log x",
        "endpoint_tests": count,
        "minimum_endpoint": minimum[2],
        "minimum_lower_bound": ">1/1000000",
        "minimum_row": minimum[1],
        "rh_established_by_replay": False,
        "rows": "12<=j<=66",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    out = Path(__file__).resolve().parent / "results" / "quotient6.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["classification"])
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
