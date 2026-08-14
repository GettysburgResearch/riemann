#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
from pathlib import Path


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    def __add__(self, other: object) -> "I":
        rhs = as_i(other)
        return I(self.lo + rhs.lo, self.hi + rhs.hi)

    __radd__ = __add__

    def __neg__(self) -> "I":
        return I(-self.hi, -self.lo)

    def __sub__(self, other: object) -> "I":
        return self + (-as_i(other))

    def __rsub__(self, other: object) -> "I":
        return as_i(other) - self

    def __mul__(self, other: object) -> "I":
        rhs = as_i(other)
        values = (
            self.lo * rhs.lo,
            self.lo * rhs.hi,
            self.hi * rhs.lo,
            self.hi * rhs.hi,
        )
        return I(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "I":
        rhs = as_i(other)
        if rhs.lo <= 0 <= rhs.hi:
            raise ZeroDivisionError("interval denominator crosses zero")
        return self * I(1 / rhs.hi, 1 / rhs.lo)

    def __rtruediv__(self, other: object) -> "I":
        return as_i(other) / self


def as_i(value: object) -> I:
    if isinstance(value, I):
        return value
    if isinstance(value, int):
        value = F(value)
    if not isinstance(value, F):
        raise TypeError(type(value))
    return I(value, value)


DEN = 10**90


def sqrt_i(n: int) -> I:
    root = isqrt(n * DEN * DEN)
    lo = F(root, DEN)
    if root * root == n * DEN * DEN:
        return I(lo, lo)
    return I(lo, F(root + 1, DEN))


def invsqrt_i(n: int) -> I:
    return 1 / sqrt_i(n)


def mobius_upto(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    least = [0] * (limit + 1)
    primes: list[int] = []
    mu[1] = 1
    for n in range(2, limit + 1):
        if least[n] == 0:
            least[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if p > least[n] or p * n > limit:
                break
            least[p * n] = p
            if n % p == 0:
                mu[p * n] = 0
                break
            mu[p * n] = -mu[n]
    return mu


def decimal(x: F, digits: int = 18) -> str:
    sign = "-" if x < 0 else ""
    x = abs(x)
    integer = x.numerator // x.denominator
    remainder = x.numerator % x.denominator
    out: list[str] = []
    for _ in range(digits):
        remainder *= 10
        out.append(str(remainder // x.denominator))
        remainder %= x.denominator
    return f"{sign}{integer}." + "".join(out)


def run() -> dict[str, object]:
    # PR #451 permits stopped leaves p >= 67 and 1 <= y < 67.
    p = 67
    y = 13
    parent_x = p * y
    threshold = 13

    mu = mobius_upto(threshold)
    a13 = sum((F(mu[n], n) for n in range(1, threshold + 1)), F(0))
    assert a13 == F(-2323, 30030)

    # B_13 = sum_{n <= 13} mu(n)/sqrt(n), enclosed directionally.
    b13 = I(F(0), F(0))
    for n in range(1, threshold + 1):
        b13 += mu[n] * invsqrt_i(n)

    r = invsqrt_i(p)
    alpha_s = 2 * (r + 2) / (r + 3)
    normalized_margin = alpha_s * sqrt_i(parent_x) * a13 - b13

    # The actual survival prefix has the additional positive factor
    # (1-r)(r+3), so its sign is the same.
    branch_prefactor = (1 - r) * (r + 3)
    physical_margin = branch_prefactor * normalized_margin

    assert branch_prefactor.lo > 0
    assert normalized_margin.lo > F(-2140, 1000)
    assert normalized_margin.hi < F(-2139, 1000)
    assert physical_margin.hi < 0

    # For fixed y=13, alpha_s(p)*sqrt(p) =
    # g(u)=2u(1+2u)/(1+3u), u=sqrt(p).
    # g'(u)=(2+8u+12u^2)/(1+3u)^2 > 0.
    # Since A_13<0, the normalized margin decreases with p.
    derivative_numerator_coefficients = [2, 8, 12]
    assert all(c > 0 for c in derivative_numerator_coefficients)
    assert a13 < 0

    result = {
        "classification": "PASS_PR451_STOPPED_LEAF_HALL_REFUTATION",
        "reviewed_pr": 451,
        "reviewed_head": "f41797c91497dc462f549a127d8494bbe4ccde2f",
        "counterexample": {
            "p": p,
            "y": y,
            "parent_parameter_x": parent_x,
            "negative_threshold": threshold,
            "A_13": f"{a13.numerator}/{a13.denominator}",
            "normalized_margin_lower": decimal(normalized_margin.lo),
            "normalized_margin_upper": decimal(normalized_margin.hi),
            "physical_survival_margin_lower": decimal(physical_margin.lo),
            "physical_survival_margin_upper": decimal(physical_margin.hi),
            "no_upward_hall_transport_exists": False,
        },
        "infinite_family": {
            "fixed_y": 13,
            "all_rough_primes_p_at_least_67": True,
            "reason": (
                "g(u)=2u(1+2u)/(1+3u) is strictly increasing for u>0, "
                "while A_13<0, so the prefix margin is decreasing in p."
            ),
        },
        "scope": (
            "Exact Fraction arithmetic and directed rational square-root "
            "enclosures. This refutes the universal stopped-leaf Hall assertion "
            "L-91621.12 and the resulting universal positive Hall row identity "
            "L-91663.9. It does not refute the native response identities or the "
            "conditional same-index child-replacement algebra."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)
    return result


if __name__ == "__main__":
    run()
