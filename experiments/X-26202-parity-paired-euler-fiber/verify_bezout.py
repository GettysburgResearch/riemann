#!/usr/bin/env python3
"""Exact Q(sqrt(2)) verification of the parity-paired Bezout filter bank."""
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json


@dataclass(frozen=True)
class Q2:
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @staticmethod
    def of(value):
        return value if isinstance(value, Q2) else Q2(Fraction(value), Fraction(0))

    def __add__(self, other):
        other = Q2.of(other)
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-Q2.of(other))

    def __rsub__(self, other):
        return Q2.of(other) - self

    def __mul__(self, other):
        other = Q2.of(other)
        return Q2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def square(self):
        return self * self

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def as_pair(self):
        return [str(self.a), str(self.b)]


ZERO = Q2()
ONE = Q2(1)
SQRT2 = Q2(0, 1)


def poly_mul(left, right):
    output = [ZERO for _ in range(len(left) + len(right) - 1)]
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            output[i + j] = output[i + j] + x * y
    return output


def sign_argument(polynomial):
    return [x if i % 2 == 0 else -x for i, x in enumerate(polynomial)]


def poly_add(left, right):
    length = max(len(left), len(right))
    return [
        (left[i] if i < len(left) else ZERO)
        + (right[i] if i < len(right) else ZERO)
        for i in range(length)
    ]


def main():
    source = poly_mul(
        [ONE, -ONE],
        poly_mul(
            [ONE, -Q2(2)],
            poly_mul([ONE, -SQRT2], [ONE, -SQRT2]),
        ),
    )
    expected_source = [
        ONE,
        -(Q2(3) + 2 * SQRT2),
        Q2(4) + 6 * SQRT2,
        -(Q2(6) + 4 * SQRT2),
        Q2(4),
    ]
    assert source == expected_source

    synthesis = [
        Q2(Fraction(1, 2)),
        Q2(Fraction(-11, 3), Fraction(7, 2)),
        Q2(1, Fraction(1, 6)),
        Q2(Fraction(14, 3), -3),
    ]

    bezout = poly_add(
        poly_mul(synthesis, source),
        poly_mul(sign_argument(synthesis), sign_argument(source)),
    )
    assert bezout[0] == ONE
    assert all(value.is_zero() for value in bezout[1:])

    # Exact positivity in Q(sqrt(2)).
    assert synthesis[0].a > 0 and synthesis[0].b == 0
    assert (
        synthesis[1].a < 0 < synthesis[1].b
        and 2 * synthesis[1].b**2 > synthesis[1].a**2
    )
    assert synthesis[2].a > 0 and synthesis[2].b > 0
    assert (
        synthesis[3].a > 0 > synthesis[3].b
        and synthesis[3].a**2 > 2 * synthesis[3].b**2
    )

    synthesis_budget = 2 * sum((value.square() for value in synthesis), ZERO)
    assert synthesis_budget == Q2(Fraction(2845, 18), Fraction(-320, 3))

    reserve_gap = Q2(Fraction(45, 4)) - synthesis_budget
    assert reserve_gap == Q2(Fraction(-5285, 36), Fraction(320, 3))
    assert 2 * 768**2 > 1057**2  # 768 sqrt(2)-1057 > 0.

    result = {
        "verdict": "PASS_EXACT_POSITIVE_BEZOUT_PARITY_RECONSTRUCTION",
        "source_polynomial_Q_sqrt2": [value.as_pair() for value in source],
        "synthesis_polynomial_Q_sqrt2": [
            value.as_pair() for value in synthesis
        ],
        "bezout_degree": len(bezout) - 1,
        "synthesis_square_budget_Q_sqrt2": synthesis_budget.as_pair(),
        "reserve_minus_budget_Q_sqrt2": reserve_gap.as_pair(),
        "scope": (
            "Exact local filter-bank algebra only. "
            "No physical-block contraction, cofinal estimate, or RH result."
        ),
    }
    payload = json.dumps(result, sort_keys=True, indent=2)
    result["proof_object_sha256_without_digest"] = hashlib.sha256(
        payload.encode("utf-8")
    ).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
