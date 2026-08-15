#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "results" / "verification.json"


def sqrt_interval(n: int, digits: int = 24) -> tuple[Fraction, Fraction]:
    den = 10**digits
    lo_num = isqrt(n * den * den)
    lo = Fraction(lo_num, den)
    hi = Fraction(
        lo_num if lo_num * lo_num == n * den * den else lo_num + 1,
        den,
    )
    assert lo * lo <= n <= hi * hi
    return lo, hi


def add(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]):
    return a[0] + b[0], a[1] + b[1]


def neg(a: tuple[Fraction, Fraction]):
    return -a[1], -a[0]


def scale(c: Fraction, a: tuple[Fraction, Fraction]):
    return (c * a[0], c * a[1]) if c >= 0 else (c * a[1], c * a[0])


def mul(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]):
    values = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(values), max(values)


def reciprocal(a: tuple[Fraction, Fraction]):
    assert a[0] > 0
    return Fraction(1, a[1]), Fraction(1, a[0])


def divide(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]):
    return mul(a, reciprocal(b))


def decimal_string(x: Fraction, digits: int = 30) -> str:
    from decimal import Decimal, getcontext

    getcontext().prec = digits + 20
    value = Decimal(x.numerator) / Decimal(x.denominator)
    return f"{value:.{digits}f}"


def main() -> None:
    s14 = sqrt_interval(14)
    s15 = sqrt_interval(15)
    s67 = sqrt_interval(67)
    s1005 = sqrt_interval(1005)

    # D = p_1005(14) - 67^(-1/2) p_15(14).
    interval = (Fraction(4), Fraction(4))
    interval = add(interval, scale(Fraction(15, 13), s14))
    interval = add(interval, scale(Fraction(-15, 7), s15))
    interval = add(interval, scale(Fraction(-1, 91), reciprocal(s1005)))

    numerator = add(scale(Fraction(15), s14), scale(Fraction(-14), s15))
    child_term = divide(numerator, scale(Fraction(13), s67))
    interval = add(interval, neg(child_term))

    coarse_lo = Fraction(-184291, 10**9)
    coarse_hi = Fraction(-184290, 10**9)
    assert coarse_lo < interval[0] <= interval[1] < coarse_hi < 0

    payload = {
        "classification": "FAIL_L91763_INFINITESIMAL_CAUSAL_GENERATOR_POSITIVITY",
        "witness": {
            "p": 67,
            "child_endpoint": 15,
            "parent_endpoint": 1005,
            "row": 14,
        },
        "exact_expression": (
            "4 + 15*sqrt(14)/13 - 15*sqrt(15)/7 "
            "- 1/(91*sqrt(1005)) "
            "- (15*sqrt(14)-14*sqrt(15))/(13*sqrt(67))"
        ),
        "directed_interval": {
            "lower_fraction": f"{interval[0].numerator}/{interval[0].denominator}",
            "upper_fraction": f"{interval[1].numerator}/{interval[1].denominator}",
            "lower_decimal": decimal_string(interval[0]),
            "upper_decimal": decimal_string(interval[1]),
            "coarse_certificate": "-184291/10^9 < D < -184290/10^9 < 0",
            "sqrt_denominator": 10**24,
        },
        "scope": (
            "exact rational interval certificate for "
            "p_1005(14)-67^(-1/2)p_15(14); no large sweep"
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
