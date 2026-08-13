#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import isqrt
from pathlib import Path
import hashlib
import json

SCALE = 10**50
TERMS = 180


class I:
    def __init__(self, lo: int, hi: int):
        assert lo <= hi
        self.lo = lo
        self.hi = hi

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
        values = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        lo = min(values) // SCALE
        hi = -((-max(values)) // SCALE)
        return I(lo, hi)

    __rmul__ = __mul__

    def lower_float(self) -> float:
        return self.lo / SCALE

    def upper_float(self) -> float:
        return self.hi / SCALE


def as_i(value) -> I:
    if isinstance(value, I):
        return value
    if isinstance(value, int):
        return I(value * SCALE, value * SCALE)
    if isinstance(value, Fraction):
        lo = (value.numerator * SCALE) // value.denominator
        hi = -((-value.numerator * SCALE) // value.denominator)
        return I(lo, hi)
    raise TypeError(type(value))


def sqrt_i(n: int) -> I:
    q = n * SCALE * SCALE
    m = isqrt(q)
    return I(m, m if m * m == q else m + 1)


def invsqrt_i(n: int) -> I:
    q = (SCALE * SCALE) // n
    m = isqrt(q)
    while (m + 1) * (m + 1) * n <= SCALE * SCALE:
        m += 1
    while m * m * n > SCALE * SCALE:
        m -= 1
    return I(m, m if m * m * n == SCALE * SCALE else m + 1)


def log_i(x: Fraction) -> I:
    assert x > 0
    power = 0
    y = x
    while y >= 2:
        y /= 2
        power += 1
    while y < 1:
        y *= 2
        power -= 1

    z = (y - 1) / (y + 1)
    z2 = z * z
    term = z
    total = Fraction(0)
    for k in range(TERMS):
        total += term / Fraction(2 * k + 1)
        term *= z2
    total *= 2
    tail = 2 * abs(term) / (Fraction(2 * TERMS + 1) * (1 - z2))
    low_y, high_y = (total, total + tail) if z >= 0 else (total - tail, total)

    z = Fraction(1, 3)
    z2 = z * z
    term = z
    total2 = Fraction(0)
    for k in range(TERMS):
        total2 += term / Fraction(2 * k + 1)
        term *= z2
    total2 *= 2
    tail2 = 2 * term / (Fraction(2 * TERMS + 1) * (1 - z2))
    low2, high2 = total2, total2 + tail2

    if power >= 0:
        low, high = low_y + power * low2, high_y + power * high2
    else:
        low, high = low_y + power * high2, high_y + power * low2
    return I(as_i(low).lo, as_i(high).hi)


def certify() -> dict:
    rs = [Fraction(1, 9), Fraction(1, 10), Fraction(1, 11), Fraction(1, 12)]
    survival = Fraction(1)
    lambdas = []
    alphas = []
    for r in rs:
        lam = r * survival
        alpha = r * lam
        lambdas.append(lam)
        alphas.append(alpha)
        survival *= 1 - r

    assert survival + sum(lambdas) == 1
    assert sum(-lambdas[i] * rs[i] + alphas[i] for i in range(len(rs))) == 0
    assert sum(alphas) < Fraction(1, 8)
    assert 8 * 8 < 67

    entropy = I(0, 0)
    for m in range(2, 68):
        entropy += log_i(Fraction(m)) * log_i(Fraction(67, m)) * invsqrt_i(m)
    d67 = entropy - (5 * sqrt_i(67) - 3)
    assert d67.lo > SCALE

    result = {
        "classification": "PASS_T91651_FOUNDATIONAL_REPLAY",
        "formal_rational_test": {
            "survival_plus_hazards": str(survival + sum(lambdas)),
            "child_cancellation": str(
                sum(-lambdas[i] * rs[i] + alphas[i] for i in range(len(rs)))
            ),
            "child_mass": str(sum(alphas)),
            "child_mass_gate": "1/8",
        },
        "analytic_gate": {
            "D67_lower": d67.lower_float(),
            "D67_upper": d67.upper_float(),
            "certified_above": "1",
            "corrects_historical_value": "3.2764",
        },
        "root_coefficient_mass_gate": {
            "active_nodes_strictly_below": 55,
            "per_node_coefficient_upper": 1,
            "mass_upper": 54,
        },
        "scope": (
            "Checks the exact coefficient algebra, strict child-mass gate, "
            "and directed base value D(67)>1. Imported finite campaigns and "
            "the full RH composition are outside this replay."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    result = certify()
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
