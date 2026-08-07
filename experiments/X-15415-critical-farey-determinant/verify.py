#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from typing import Dict, Tuple
import json
import math


def mobius(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    x = n
    p = 2
    parity = 0
    while p * p <= x:
        if x % p == 0:
            x //= p
            parity ^= 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        parity ^= 1
    return -1 if parity else 1


def frac_part(x: Fraction) -> Fraction:
    return x - (x.numerator // x.denominator)


def ceil_fraction(x: Fraction) -> int:
    return -((-x.numerator) // x.denominator)


def completed_packet_check(X: Fraction, x: Fraction, universe: int) -> dict:
    if not (X <= x <= 2 * X):
        raise ValueError("x outside dyadic block")
    D = ceil_fraction(2 * X)
    if universe <= D:
        raise ValueError("universe must exceed D")

    lhs = Fraction(1)
    for d in range(1, universe + 1):
        lhs += mobius(d) * frac_part(x / d) ** 2

    S = Fraction(0)
    M = 0
    for d in range(1, D + 1):
        mu = mobius(d)
        M += mu
        S += mu * (frac_part(x / d) ** 2 - Fraction(1, 3))

    tail = sum(
        (Fraction(mobius(d), d * d) for d in range(D + 1, universe + 1)),
        Fraction(0),
    )
    rhs = S + 1 + Fraction(M, 3) + x * x * tail
    return {
        "X": str(X),
        "x": str(x),
        "D": D,
        "universe": universe,
        "lhs": str(lhs),
        "rhs": str(rhs),
        "equal": lhs == rhs,
    }


# Formal Fourier coefficient in the basis
#   O = i/(2*pi), E = 1/(2*pi^2),
# so c_h = O/h + E/h^2.
FormalCoeff = Tuple[Fraction, Fraction]


def add_coeff(a: FormalCoeff, b: FormalCoeff) -> FormalCoeff:
    return a[0] + b[0], a[1] + b[1]


def scale_coeff(k: int, c: FormalCoeff) -> FormalCoeff:
    return k * c[0], k * c[1]


def c_h(h: int) -> FormalCoeff:
    if h == 0:
        raise ValueError("h must be nonzero")
    return Fraction(1, h), Fraction(1, h * h)


def reduce_frequency(h: int, d: int) -> Tuple[int, int, int]:
    # h/d = a/q and d=q*m, h=a*m.
    g = abs(math.gcd(h, d))
    a, q, m = h // g, d // g, g
    if q <= 0:
        a, q = -a, -q
    return a, q, m


def reduced_grouping_check(D: int, H: int) -> dict:
    direct: Dict[Fraction, FormalCoeff] = {}
    grouped: Dict[Fraction, FormalCoeff] = {}

    for d in range(1, D + 1):
        mu = mobius(d)
        for h in range(-H, H + 1):
            if h == 0:
                continue
            freq = Fraction(h, d)
            direct[freq] = add_coeff(
                direct.get(freq, (Fraction(0), Fraction(0))),
                scale_coeff(mu, c_h(h)),
            )

    for d in range(1, D + 1):
        mu = mobius(d)
        for h in range(-H, H + 1):
            if h == 0:
                continue
            a, q, m = reduce_frequency(h, d)
            if d != q * m or h != a * m:
                raise AssertionError("bad reduced decomposition")
            freq = Fraction(a, q)
            grouped[freq] = add_coeff(
                grouped.get(freq, (Fraction(0), Fraction(0))),
                scale_coeff(mu, c_h(h)),
            )

    return {
        "D": D,
        "H": H,
        "frequency_count": len(direct),
        "equal": direct == grouped,
    }


def determinant_check(a: int, q: int, b: int, v: int) -> dict:
    if a == 0 or b == 0 or q <= 0 or v <= 0:
        raise ValueError("invalid determinant row")
    r = a * v - b * q
    first_lhs = Fraction(v, b) - Fraction(q, a)
    first_rhs = Fraction(r, a * b)
    second_lhs = Fraction(v * v, b * b) - Fraction(q * q, a * a)
    second_rhs = Fraction(r, a * b) * (Fraction(v, b) + Fraction(q, a))
    return {
        "row": [a, q, b, v],
        "r": r,
        "first": first_lhs == first_rhs,
        "second": second_lhs == second_rhs,
    }


def main() -> None:
    packet_rows = [
        completed_packet_check(Fraction(5, 2), Fraction(3, 1), 17),
        completed_packet_check(Fraction(7, 3), Fraction(13, 4), 19),
        completed_packet_check(Fraction(11, 4), Fraction(21, 4), 23),
    ]
    grouping_rows = [
        reduced_grouping_check(6, 9),
        reduced_grouping_check(8, 12),
    ]
    determinant_rows = [
        determinant_check(1, 3, 2, 5),
        determinant_check(-2, 5, 3, 7),
        determinant_check(5, 8, -1, 3),
        determinant_check(7, 9, 4, 11),
    ]

    # Mutation: wrong determinant av-bq -> aq-bv must fail somewhere.
    mutation_rejected = False
    for row in determinant_rows:
        a, q, b, v = row["row"]
        wrong = a * q - b * v
        if Fraction(v, b) - Fraction(q, a) != Fraction(wrong, a * b):
            mutation_rejected = True
            break

    verdict = (
        all(r["equal"] for r in packet_rows)
        and all(r["equal"] for r in grouping_rows)
        and all(r["first"] and r["second"] for r in determinant_rows)
        and mutation_rejected
    )
    result = {
        "schema": "X-15415-v1",
        "packet_rows": packet_rows,
        "grouping_rows": grouping_rows,
        "determinant_rows": determinant_rows,
        "wrong_determinant_mutation_rejected": mutation_rejected,
        "verdict": (
            "SYNTHETIC_CRITICAL_FAREY_ALGEBRA_VERIFIED" if verdict else "FAIL"
        ),
        "scope": (
            "finite exact algebra only; does not verify the all-row "
            "summability theorem L-15448.29"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not verdict:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
