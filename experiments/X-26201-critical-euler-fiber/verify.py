#!/usr/bin/env python3
"""Exact regression for the critical Euler-fiber carry/reflected-source bridge.

Standard library only. Arithmetic in Q(sqrt(2)) is exact.
This verifies finite algebra and source identities only; it proves no asymptotic
reflected reserve and no result about RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from typing import Iterable, List


@dataclass(frozen=True)
class Q2:
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @staticmethod
    def of(x: int | Fraction | "Q2") -> "Q2":
        if isinstance(x, Q2):
            return x
        return Q2(Fraction(x), Fraction(0))

    def __add__(self, other: int | Fraction | "Q2") -> "Q2":
        o = Q2.of(other)
        return Q2(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self) -> "Q2":
        return Q2(-self.a, -self.b)

    def __sub__(self, other: int | Fraction | "Q2") -> "Q2":
        return self + (-Q2.of(other))

    def __rsub__(self, other: int | Fraction | "Q2") -> "Q2":
        return Q2.of(other) - self

    def __mul__(self, other: int | Fraction | "Q2") -> "Q2":
        o = Q2.of(other)
        return Q2(
            self.a * o.a + 2 * self.b * o.b,
            self.a * o.b + self.b * o.a,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: int | Fraction | "Q2") -> "Q2":
        o = Q2.of(other)
        den = o.a * o.a - 2 * o.b * o.b
        if den == 0:
            raise ZeroDivisionError
        return Q2(
            (self.a * o.a - 2 * self.b * o.b) / den,
            (self.b * o.a - self.a * o.b) / den,
        )

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def positive_coefficient_cone(self) -> bool:
        # Sufficient exact positivity test for the inverse series in this file.
        return self.a >= 0 and self.b >= 0 and not self.is_zero()

    def as_pair(self) -> list[str]:
        return [str(self.a), str(self.b)]


ZERO = Q2()
ONE = Q2(Fraction(1), Fraction(0))
SQRT2 = Q2(Fraction(0), Fraction(1))


def poly_mul(p: List[Q2], q: List[Q2]) -> List[Q2]:
    out = [ZERO for _ in range(len(p) + len(q) - 1)]
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] = out[i + j] + x * y
    return out


def poly_eval(p: List[Q2], x: Q2) -> Q2:
    out = ZERO
    for coefficient in reversed(p):
        out = out * x + coefficient
    return out


def poly_derivative(p: List[Q2]) -> List[Q2]:
    return [p[i] * i for i in range(1, len(p))]


def inverse_series(p: List[Q2], order: int) -> List[Q2]:
    if p[0] != ONE:
        raise ValueError("constant coefficient must be one")
    answer = [ONE]
    for k in range(1, order + 1):
        total = ZERO
        for j in range(1, min(k, len(p) - 1) + 1):
            total = total + p[j] * answer[k - j]
        answer.append(-total)
    return answer


def formal_log_derivative_coeffs(p: List[Q2], order: int) -> List[Q2]:
    """Coefficients of -z p'(z)/p(z) = z d/dz log(1/p(z))."""
    inverse = inverse_series(p, order)
    z_derivative = [ZERO] + [p[i] * i for i in range(1, len(p))]
    product = poly_mul([-x for x in z_derivative], inverse)
    return product[: order + 1]


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            value = n * p
            if value > limit:
                break
            composite[value] = True
            if n % p == 0:
                mu[value] = 0
                break
            mu[value] = -mu[n]
    return mu


def q2_sum(values: Iterable[Q2]) -> Q2:
    total = ZERO
    for value in values:
        total = total + value
    return total


def main() -> None:
    mobius_local = [ONE, -ONE]
    pole = [ONE, -Q2(2)]
    half = [ONE, -SQRT2]
    filter_polynomial = poly_mul(pole, poly_mul(half, half))
    full_local = poly_mul(mobius_local, filter_polynomial)

    expected_filter = [
        ONE,
        -(Q2(2) + Q2(2) * SQRT2),
        Q2(2) + Q2(4) * SQRT2,
        Q2(-4),
    ]
    expected_full = [
        ONE,
        -(Q2(3) + Q2(2) * SQRT2),
        Q2(4) + Q2(6) * SQRT2,
        -(Q2(6) + Q2(4) * SQRT2),
        Q2(4),
    ]
    assert filter_polynomial == expected_filter
    assert full_local == expected_full

    half_root = SQRT2 / 2
    assert poly_eval(filter_polynomial, Q2(Fraction(1, 2))).is_zero()
    assert poly_eval(filter_polynomial, half_root).is_zero()
    assert poly_eval(poly_derivative(filter_polynomial), half_root).is_zero()
    assert poly_eval(full_local, ONE).is_zero()

    inverse = inverse_series(full_local, 64)
    assert all(value.positive_coefficient_cone() for value in inverse)

    log_derivative = formal_log_derivative_coeffs(full_local, 64)
    for k in range(1, 65):
        if k % 2 == 0:
            half_extra = Q2(2 * (2 ** (k // 2)))
        else:
            half_extra = Q2(0, 2 * (2 ** ((k - 1) // 2)))
        expected = Q2(1 + 2**k) + half_extra
        assert log_derivative[k] == expected

    limit = 512
    mu = mobius_sieve(limit)
    taps = {
        1: expected_filter[0],
        2: expected_filter[1],
        4: expected_filter[2],
        8: expected_filter[3],
    }
    source = [ZERO for _ in range(limit + 1)]
    for n in range(1, limit + 1):
        source[n] = q2_sum(
            Q2(mu[n // d]) * coefficient
            for d, coefficient in taps.items()
            if n % d == 0
        )

    mertens = [0] * (limit + 1)
    for n in range(1, limit + 1):
        mertens[n] = mertens[n - 1] + mu[n]
        if n % 2 == 1:
            assert source[n] == Q2(mu[n])
        cumulative = q2_sum(source[1 : n + 1])
        expected_cumulative = (
            Q2(mertens[n])
            + expected_filter[1] * mertens[n // 2]
            + expected_filter[2] * mertens[n // 4]
            + expected_filter[3] * mertens[n // 8]
        )
        assert cumulative == expected_cumulative

    fiber_rows = 0
    for odd in range(1, limit // 16 + 1, 2):
        if mu[odd] == 0:
            continue
        fiber = [source[(2**nu) * odd] for nu in range(5)]
        expected = [Q2(mu[odd]) * coefficient for coefficient in full_local]
        assert fiber == expected
        fiber_rows += 1

    # Mandatory mutations.
    no_pole_factor = poly_mul(half, half)
    assert not poly_eval(no_pole_factor, Q2(Fraction(1, 2))).is_zero()
    single_half_factor = poly_mul(pole, half)
    assert not poly_eval(
        poly_derivative(single_half_factor), half_root
    ).is_zero()
    assert not poly_eval(filter_polynomial, ONE).is_zero()

    result = {
        "verdict": "PASS_EXACT_CRITICAL_EULER_FIBER_ALGEBRA",
        "filter_coefficients_Q_sqrt2": [
            value.as_pair() for value in filter_polynomial
        ],
        "full_local_coefficients_Q_sqrt2": [
            value.as_pair() for value in full_local
        ],
        "inverse_coefficients_checked": len(inverse),
        "generalized_prime_coefficients_checked": len(log_derivative) - 1,
        "finite_source_rows_checked": limit,
        "odd_firewall_rows_checked": (limit + 1) // 2,
        "fiber_rows_checked": fiber_rows,
        "mutations": 3,
        "scope": (
            "Exact finite/filter/source algebra only. "
            "No reflected contraction, cofinal energy bound, or RH result."
        ),
    }
    payload = json.dumps(result, sort_keys=True, indent=2)
    result["proof_object_sha256_without_digest"] = hashlib.sha256(
        payload.encode("utf-8")
    ).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
