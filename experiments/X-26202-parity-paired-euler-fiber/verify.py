#!/usr/bin/env python3
"""Exact regression for the parity-paired critical Euler-fiber source.

Standard library only. Arithmetic is exact in Q(sqrt(2)).
This verifies finite source/filter/frame algebra only. It proves no physical
block contraction, no cofinal estimate, and no result about RH.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json


@dataclass(frozen=True)
class Q2:
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @staticmethod
    def of(value: int | Fraction | "Q2") -> "Q2":
        if isinstance(value, Q2):
            return value
        return Q2(Fraction(value), Fraction(0))

    def __add__(self, other: int | Fraction | "Q2") -> "Q2":
        other = Q2.of(other)
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self) -> "Q2":
        return Q2(-self.a, -self.b)

    def __sub__(self, other: int | Fraction | "Q2") -> "Q2":
        return self + (-Q2.of(other))

    def __rsub__(self, other: int | Fraction | "Q2") -> "Q2":
        return Q2.of(other) - self

    def __mul__(self, other: int | Fraction | "Q2") -> "Q2":
        other = Q2.of(other)
        return Q2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: int | Fraction | "Q2") -> "Q2":
        other = Q2.of(other)
        denominator = other.a * other.a - 2 * other.b * other.b
        if denominator == 0:
            raise ZeroDivisionError
        return Q2(
            (self.a * other.a - 2 * self.b * other.b) / denominator,
            (self.b * other.a - self.a * other.b) / denominator,
        )

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def __pow__(self, exponent: int) -> "Q2":
        if exponent < 0:
            return (ONE / self) ** (-exponent)
        answer = ONE
        base = self
        value = exponent
        while value:
            if value & 1:
                answer = answer * base
            base = base * base
            value >>= 1
        return answer

    def as_pair(self) -> list[str]:
        return [str(self.a), str(self.b)]


ZERO = Q2()
ONE = Q2(Fraction(1))
SQRT2 = Q2(Fraction(0), Fraction(1))


def poly_mul(left: list[Q2], right: list[Q2]) -> list[Q2]:
    output = [ZERO for _ in range(len(left) + len(right) - 1)]
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            output[i + j] = output[i + j] + x * y
    return output


def poly_scale_argument(polynomial: list[Q2], scale: Q2) -> list[Q2]:
    output: list[Q2] = []
    power = ONE
    for coefficient in polynomial:
        output.append(coefficient * power)
        power = power * scale
    return output


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for prime in primes:
            value = n * prime
            if value > limit:
                break
            composite[value] = True
            if n % prime == 0:
                mu[value] = 0
                break
            mu[value] = -mu[n]
    return mu


def valuation_two(n: int) -> int:
    answer = 0
    while n % 2 == 0:
        n //= 2
        answer += 1
    return answer


def main() -> None:
    local = poly_mul(
        [ONE, -ONE],
        poly_mul([ONE, -Q2(2)], poly_mul([ONE, -SQRT2], [ONE, -SQRT2])),
    )
    expected_local = [
        ONE,
        -(Q2(3) + Q2(2) * SQRT2),
        Q2(4) + Q2(6) * SQRT2,
        -(Q2(6) + Q2(4) * SQRT2),
        Q2(4),
    ]
    assert local == expected_local

    normalized = poly_scale_argument(local, SQRT2 / 2)
    expected_normalized = [
        ONE,
        -(Q2(2) + Q2(Fraction(3, 2)) * SQRT2),
        Q2(2) + Q2(3) * SQRT2,
        -(Q2(2) + Q2(Fraction(3, 2)) * SQRT2),
        ONE,
    ]
    assert normalized == expected_normalized
    assert normalized == list(reversed(normalized))
    assert normalized[0].a > 0 and normalized[2].a > 0
    assert normalized[1].a < 0 and normalized[3].a < 0

    frame: dict[tuple[int, int], Q2] = defaultdict(lambda: ZERO)
    for k, coefficient in enumerate(local):
        frame[(k, 0)] = frame[(k, 0)] + 2 * coefficient * coefficient
    for lower in range(3):
        upper = lower + 2
        frame[(lower + 1, 1)] = (
            frame[(lower + 1, 1)]
            + 4 * local[upper] * local[lower]
        )
    frame[(2, 2)] = frame[(2, 2)] + 8 * local[4] * local[0]
    frame[(2, 0)] = frame[(2, 0)] - 4 * local[4] * local[0]

    expected_frame = {
        (0, 0): Q2(2),
        (1, 0): Q2(34, 24),
        (1, 1): Q2(16, 24),
        (2, 0): Q2(160, 96),
        (2, 1): Q2(136, 96),
        (2, 2): Q2(32),
        (3, 0): Q2(136, 96),
        (3, 1): Q2(64, 96),
        (4, 0): Q2(32),
    }
    assert dict(frame) == expected_frame

    at_minus_one = [Fraction(2), Fraction(18), Fraction(56),
                    Fraction(72), Fraction(32)]
    factorized = [Fraction(2)]
    for factor in (
        [Fraction(1), Fraction(1)],
        [Fraction(1), Fraction(4), Fraction(4)],
        [Fraction(1), Fraction(4)],
    ):
        out = [Fraction(0)] * (len(factorized) + len(factor) - 1)
        for i, x in enumerate(factorized):
            for j, y in enumerate(factor):
                out[i + j] += x * y
        factorized = out
    assert factorized == at_minus_one

    gap_left = at_minus_one[:]
    gap_left[0] -= Fraction(45, 4)
    first = [Fraction(-1), Fraction(4)]
    second = [Fraction(37, 4), Fraction(19), Fraction(20), Fraction(8)]
    gap_right = [Fraction(0)] * (len(first) + len(second) - 1)
    for i, x in enumerate(first):
        for j, y in enumerate(second):
            gap_right[i + j] += x * y
    assert gap_left == gap_right

    limit = 1024
    mu = mobius_sieve(limit)
    filter_polynomial = poly_mul(
        [ONE, -Q2(2)], poly_mul([ONE, -SQRT2], [ONE, -SQRT2])
    )
    taps = {
        1: filter_polynomial[0],
        2: filter_polynomial[1],
        4: filter_polynomial[2],
        8: filter_polynomial[3],
    }
    plus = [ZERO for _ in range(limit + 1)]
    minus = [ZERO for _ in range(limit + 1)]
    even_channel = [ZERO for _ in range(limit + 1)]
    odd_channel = [ZERO for _ in range(limit + 1)]
    for n in range(1, limit + 1):
        value = ZERO
        for divisor, coefficient in taps.items():
            if n % divisor == 0:
                value = value + Q2(mu[n // divisor]) * coefficient
        plus[n] = value
        character = -1 if valuation_two(n) % 2 else 1
        minus[n] = character * value
        even_channel[n] = (plus[n] + minus[n]) / 2
        odd_channel[n] = (plus[n] - minus[n]) / 2
        if valuation_two(n) % 2 == 0:
            assert even_channel[n] == plus[n]
            assert odd_channel[n].is_zero()
        else:
            assert odd_channel[n] == plus[n]
            assert even_channel[n].is_zero()

    fiber_rows = 0
    for odd in range(1, limit // 16 + 1, 2):
        if mu[odd] == 0:
            continue
        raw = [plus[(2**nu) * odd] for nu in range(5)]
        expected = [Q2(mu[odd]) * coefficient for coefficient in local]
        assert raw == expected
        normalized_row = [
            raw[nu] * (SQRT2 / 2) ** nu for nu in range(5)
        ]
        expected_row = [
            Q2(mu[odd]) * coefficient for coefficient in normalized
        ]
        assert normalized_row == expected_row
        fiber_rows += 1

    def poly_eval(polynomial: list[Q2], point: Q2) -> Q2:
        answer = ZERO
        for coefficient in reversed(polynomial):
            answer = answer * point + coefficient
        return answer

    assert poly_eval(local, Q2(Fraction(1, 2))).is_zero()
    assert not poly_eval(
        poly_scale_argument(local, -ONE), Q2(Fraction(1, 2))
    ).is_zero()

    result = {
        "verdict": "PASS_EXACT_PARITY_PAIRED_EULER_FIBER_ALGEBRA",
        "local_coefficients_Q_sqrt2": [x.as_pair() for x in local],
        "normalized_coefficients_Q_sqrt2": [
            x.as_pair() for x in normalized
        ],
        "frame_polynomial_terms": len(frame),
        "sharp_frame_lower_bound": "45/4",
        "source_rows_checked": limit,
        "complete_fiber_rows_checked": fiber_rows,
        "mutations": 1,
        "scope": (
            "Exact finite/filter/frame algebra only. "
            "No paired physical-block contraction, cofinal estimate, or RH result."
        ),
    }
    payload = json.dumps(result, sort_keys=True, indent=2)
    result["proof_object_sha256_without_digest"] = hashlib.sha256(
        payload.encode("utf-8")
    ).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
