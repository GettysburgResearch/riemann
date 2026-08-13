#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import json


@dataclass(frozen=True)
class Qr:
    """a+b*r in Q[r]/(r^2-1/p)."""

    a: Fraction
    b: Fraction
    p: int

    def __add__(self, other):
        other = as_qr(other, self.p)
        return Qr(self.a + other.a, self.b + other.b, self.p)

    __radd__ = __add__

    def __neg__(self):
        return Qr(-self.a, -self.b, self.p)

    def __sub__(self, other):
        return self + (-as_qr(other, self.p))

    def __rsub__(self, other):
        return as_qr(other, self.p) - self

    def __mul__(self, other):
        other = as_qr(other, self.p)
        return Qr(
            self.a * other.a + self.b * other.b / self.p,
            self.a * other.b + self.b * other.a,
            self.p,
        )

    __rmul__ = __mul__


def as_qr(value, p):
    if isinstance(value, Qr):
        assert value.p == p
        return value
    return Qr(Fraction(value), Fraction(0), p)


def matmul_row(row, matrix):
    return [
        row[0] * matrix[0][j] + row[1] * matrix[1][j]
        for j in range(2)
    ]


def main():
    primes = (5, 7, 11, 59, 61, 101, 1009)
    exact_identity_checks = 0
    minimum_lower_right = None

    for p in primes:
        one = Qr(Fraction(1), Fraction(0), p)
        r = Qr(Fraction(0), Fraction(1), p)
        factor = one - r

        M = [
            [factor * (one + 2 * r), factor * (-2 * r)],
            [factor * r, factor * factor],
        ]

        correction = [
            [Qr(Fraction(0), Fraction(0), p), 2 * r * factor],
            [Qr(Fraction(0), Fraction(0), p), -r * factor],
        ]

        N = [
            [M[i][j] + correction[i][j] for j in range(2)]
            for i in range(2)
        ]

        expected = [
            [factor * (one + 2 * r), Qr(Fraction(0), Fraction(0), p)],
            [factor * r, factor * (one - 2 * r)],
        ]
        assert N == expected
        exact_identity_checks += 4

        psi = [Qr(Fraction(1), Fraction(0), p), Qr(Fraction(2), Fraction(0), p)]
        score = [Qr(Fraction(2), Fraction(0), p), Qr(Fraction(1), Fraction(0), p)]

        assert matmul_row(psi, N) == matmul_row(psi, M)
        exact_identity_checks += 2

        score_delta = [
            matmul_row(score, N)[j] - matmul_row(score, M)[j]
            for j in range(2)
        ]
        assert score_delta[0] == Qr(Fraction(0), Fraction(0), p)
        assert score_delta[1] == 3 * r * factor
        exact_identity_checks += 2

        # Lower-right entry is (1-r)(1-2r)>0 for p>=5.
        numeric_lr = (1 - 1 / p**0.5) * (1 - 2 / p**0.5)
        assert numeric_lr > 0
        if minimum_lower_right is None:
            minimum_lower_right = numeric_lr
        else:
            minimum_lower_right = min(minimum_lower_right, numeric_lr)

    result = {
        "classification": "PASS_POSITIVE_SHARP_PRESERVING_ROUGH_STATE_COMPLETION",
        "tested_primes": list(primes),
        "exact_quadratic_field_identity_checks": exact_identity_checks,
        "minimum_tested_positive_lower_right_entry": minimum_lower_right,
        "scope": (
            "Exact arithmetic in Q[r]/(r^2-1/p) verifies the positive "
            "completion, exact preservation of (1,2), and the favorable "
            "(2,1) score increment. Positivity is analytic for every p>=5. "
            "The colored-to-physical column projection remains open."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
