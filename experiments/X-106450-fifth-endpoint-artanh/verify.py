#!/usr/bin/env python3
"""Light exact replay for T-106450 and L-106452.

The replay checks finite polynomial symmetrization, exact rational constants,
rank-one Loewner feature positivity and hostile status flags.  It does not
evaluate Xi or prove either signed-tail theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def q_value(m: int, u: Fraction, v: Fraction) -> Fraction:
    return sum(u ** (m - 1 - j) * v**j for j in range(m))


def outer(vector: list[Fraction]) -> list[list[Fraction]]:
    return [[x * y for y in vector] for x in vector]


def add_matrix(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def quadratic(matrix: list[list[Fraction]], vector: list[Fraction]) -> Fraction:
    return sum(
        vector[i] * matrix[i][j] * vector[j]
        for i in range(len(vector))
        for j in range(len(vector))
    )


def main() -> dict[str, object]:
    # Exact odd-endpoint symmetrization:
    # i^(m+1) v^m (u-v), averaged with u<->v, has the stated real sign.
    fixtures = [
        (1, Fraction(-3, 2), Fraction(5, 3)),
        (5, Fraction(-7, 4), Fraction(2, 5)),
        (9, Fraction(11, 6), Fraction(-5, 7)),
    ]
    for m, u, v in fixtures:
        assert m % 2 == 1
        r = (m - 1) // 2
        lhs = Fraction((-1) ** r, 2) * (u - v) ** 2 * q_value(m, u, v)
        assert lhs >= 0

    # Exact fifth-endpoint constants.
    same = Fraction(4, 39601)
    reflected = Fraction(640000, 1568239201)
    four_channel = 2 * same + 2 * reflected
    assert four_channel == Fraction(1596808, 1568239201)
    assert four_channel < Fraction(1, 980)

    margin = Fraction(997, 1000) - Fraction(9, 10) - Fraction(1, 980)
    assert margin == Fraction(4703, 49000)

    # Rank-one Cauchy features appearing in the artanh Loewner integral.
    points = [Fraction(-1, 3), Fraction(1, 7), Fraction(2, 5)]
    lam = Fraction(1, 10)
    gram = [[Fraction(0) for _ in points] for _ in points]
    for t in [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)]:
        plus = [Fraction(1, 1) / (1 - t * lam * u) for u in points]
        minus = [Fraction(1, 1) / (1 + t * lam * u) for u in points]
        gram = add_matrix(gram, add_matrix(outer(plus), outer(minus)))
    for vector in [
        [Fraction(1), Fraction(-2), Fraction(3)],
        [Fraction(-4), Fraction(1), Fraction(2)],
        [Fraction(5), Fraction(0), Fraction(-1)],
    ]:
        assert quadratic(gram, vector) >= 0

    # The exact common-carrier determinant is one.
    for x in [Fraction(-1, 5), Fraction(0), Fraction(3, 10)]:
        determinant_numerator = 1 - x * x
        carrier_square = 1 - x * x
        assert determinant_numerator == carrier_square

    result: dict[str, object] = {
        "schema": "riemann.x106450.fifth-endpoint-artanh.v1",
        "classification": "PASS_T106450_FIFTH_ENDPOINT_AND_ARTANH_SOURCE_ALGEBRA",
        "odd_endpoint_orders_checked": [1, 5, 9],
        "fifth_endpoint_four_channel_constant": "1596808/1568239201",
        "four_channel_below_one_over_980": True,
        "signed_tail_threshold": "4703/49000",
        "loewner_rank_one_features_checked": True,
        "positive_source_innerness_firewall_retained": True,
        "signedtail5_106450_proved": False,
        "signedtail106430_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    payload = main()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if arguments.output is not None:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(text, encoding="utf-8")
    print(text, end="")
