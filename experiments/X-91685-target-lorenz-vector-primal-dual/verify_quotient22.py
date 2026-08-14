#!/usr/bin/env python3
"""Directed endpoint certificate for the P19 odd-row prefix through quotient 22."""
from __future__ import annotations

from decimal import Decimal, ROUND_HALF_EVEN, localcontext
from functools import lru_cache
from pathlib import Path
import hashlib
import json

PREC = 100
EPS = Decimal("1e-78")
MAX_X = 1452
ODD_SOURCES = (2, 3, 5, 7, 11, 13, 17, 19)


class Interval:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = lo if isinstance(lo, Decimal) else Decimal(lo)
        self.hi = self.lo if hi is None else (
            hi if isinstance(hi, Decimal) else Decimal(hi)
        )
        assert self.lo <= self.hi

    def __add__(self, other):
        other = as_interval(other)
        return Interval(self.lo + other.lo - EPS, self.hi + other.hi + EPS)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_interval(other))

    def __rsub__(self, other):
        return as_interval(other) - self

    def __mul__(self, other):
        other = as_interval(other)
        values = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return Interval(min(values) - EPS, max(values) + EPS)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_interval(other)
        assert not (other.lo <= 0 <= other.hi)
        values = (
            self.lo / other.lo,
            self.lo / other.hi,
            self.hi / other.lo,
            self.hi / other.hi,
        )
        return Interval(min(values) - EPS, max(values) + EPS)

    def __rtruediv__(self, other):
        return as_interval(other) / self


def as_interval(value):
    return value if isinstance(value, Interval) else Interval(value)


@lru_cache(None)
def sqrt_interval(n: int) -> Interval:
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = ROUND_HALF_EVEN
        value = Decimal(n).sqrt()
    return Interval(value - EPS, value + EPS)


@lru_cache(None)
def invsqrt_interval(n: int) -> Interval:
    return Interval(1) / sqrt_interval(n)


@lru_cache(None)
def log_interval(n: int) -> Interval:
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = ROUND_HALF_EVEN
        value = Decimal(n).ln()
    return Interval(value - EPS, value + EPS)


@lru_cache(None)
def gamma_interval(j: int, m: int) -> Interval:
    if m == j:
        return (
            Interval(Decimal(j + 1) / Decimal(j - 1))
            * invsqrt_interval(j)
        )
    if m == j + 1:
        return (
            -Interval(Decimal((j + 1) * (j - 2)) / Decimal(j * (j - 1)))
            * invsqrt_interval(j + 1)
        )
    if m >= j + 2:
        return (
            Interval(Decimal(2) / Decimal(j * (j - 1)))
            * invsqrt_interval(m)
        )
    return Interval(0)


def build_coefficients(j: int) -> tuple[list[Interval], list[Interval]]:
    c_values = [Interval(0) for _ in range(MAX_X + 1)]
    d_values = [Interval(0) for _ in range(MAX_X + 1)]
    c_sum = Interval(0)
    d_sum = Interval(0)
    for n in range(j, MAX_X + 1):
        gamma = gamma_interval(j, n)
        c_sum += gamma
        d_sum += gamma * log_interval(n)
        c_values[n] = c_sum
        d_values[n] = d_sum
    return c_values, d_values


def q_interval(
    x: int,
    divisor: int,
    j: int,
    c_values: list[Interval],
    d_values: list[Interval],
) -> Interval:
    activation = x // divisor
    if activation < j:
        return Interval(0)
    return (
        c_values[activation]
        * (log_interval(x) - log_interval(divisor))
        - d_values[activation]
    )


def main() -> None:
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = ROUND_HALF_EVEN
        inverse_roots = {
            d: invsqrt_interval(d) for d in ODD_SOURCES
        }
        minimum = None
        endpoint_tests = 0
        for j in range(4, 67):
            c_values, d_values = build_coefficients(j)
            lower = max(67, 5 * j)
            upper = 22 * j
            for x in range(lower, upper + 1):
                value = q_interval(x, 1, j, c_values, d_values)
                for divisor in ODD_SOURCES:
                    value -= inverse_roots[divisor] * q_interval(
                        x, divisor, j, c_values, d_values
                    )
                assert value.lo > 0, (j, x, str(value.lo))
                record = (value.lo, j, x)
                if minimum is None or record < minimum:
                    minimum = record
                endpoint_tests += 1

        assert minimum is not None
        payload = {
            "arithmetic_class": "DIRECTED_DECIMAL_INTERVAL",
            "classification": (
                "PASS_P19_ODD_ROW_PREFIX_THROUGH_QUOTIENT_TWENTY_TWO"
            ),
            "domain": (
                "max(67,5j)<=x<=22j; all activation walls are integer "
                "and cell interiors are affine in log x"
            ),
            "endpoint_tests": endpoint_tests,
            "minimum_endpoint": minimum[2],
            "minimum_lower_decimal": str(minimum[0]),
            "minimum_row": minimum[1],
            "odd_sources": list(ODD_SOURCES),
            "rounding_contract": (
                "100-digit Decimal sqrt/ln with 1e-78 outward padding "
                "after every operation"
            ),
            "rh_established_by_replay": False,
            "rows": "4<=j<=66",
        }
        canonical = json.dumps(
            payload, sort_keys=True, separators=(",", ":")
        ).encode()
        payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
        out = Path(__file__).resolve().parent / "results" / "quotient22.json"
        out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        print(payload["classification"])
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
