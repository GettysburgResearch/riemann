#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable

VERDICT = "PASS_T105200_POISSON_BEZOUT_RESIDUE_LOCALIZATION"


@dataclass(frozen=True)
class Gaussian:
    real: Fraction = Fraction(0)
    imag: Fraction = Fraction(0)

    def __add__(self, other: object) -> "Gaussian":
        rhs = as_gaussian(other)
        return Gaussian(self.real + rhs.real, self.imag + rhs.imag)

    __radd__ = __add__

    def __neg__(self) -> "Gaussian":
        return Gaussian(-self.real, -self.imag)

    def __sub__(self, other: object) -> "Gaussian":
        return self + (-as_gaussian(other))

    def __rsub__(self, other: object) -> "Gaussian":
        return as_gaussian(other) - self

    def __mul__(self, other: object) -> "Gaussian":
        rhs = as_gaussian(other)
        return Gaussian(
            self.real * rhs.real - self.imag * rhs.imag,
            self.real * rhs.imag + self.imag * rhs.real,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "Gaussian":
        rhs = as_gaussian(other)
        denominator = rhs.real * rhs.real + rhs.imag * rhs.imag
        if denominator == 0:
            raise ZeroDivisionError("Gaussian rational division by zero")
        return Gaussian(
            (self.real * rhs.real + self.imag * rhs.imag) / denominator,
            (self.imag * rhs.real - self.real * rhs.imag) / denominator,
        )

    def __rtruediv__(self, other: object) -> "Gaussian":
        return as_gaussian(other) / self

    def __pow__(self, exponent: int) -> "Gaussian":
        if exponent < 0:
            return Gaussian(1) / (self ** (-exponent))
        result = Gaussian(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power //= 2
        return result


def as_gaussian(value: object) -> Gaussian:
    if isinstance(value, Gaussian):
        return value
    if isinstance(value, Fraction):
        return Gaussian(value)
    if isinstance(value, int):
        return Gaussian(Fraction(value))
    raise TypeError(f"unsupported Gaussian operand: {type(value)!r}")


Polynomial = list[Fraction]


def trim(poly: Iterable[Fraction]) -> Polynomial:
    result = list(poly)
    if not result:
        return [Fraction(0)]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return trim(result)


def poly_neg(poly: Polynomial) -> Polynomial:
    return [-value for value in poly]


def poly_sub(left: Polynomial, right: Polynomial) -> Polynomial:
    return poly_add(left, poly_neg(right))


def poly_scale(poly: Polynomial, scalar: Fraction) -> Polynomial:
    return trim([scalar * value for value in poly])


def poly_mul(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return trim(result)


def poly_derivative(poly: Polynomial, order: int = 1) -> Polynomial:
    result = list(poly)
    for _ in range(order):
        result = [
            Fraction(index) * result[index]
            for index in range(1, len(result))
        ]
        if not result:
            result = [Fraction(0)]
    return trim(result)


def poly_integral(poly: Polynomial, constant: Fraction = Fraction(0)) -> Polynomial:
    return [constant] + [
        poly[index] / Fraction(index + 1)
        for index in range(len(poly))
    ]


def poly_eval(poly: Polynomial, value: Gaussian | Fraction | int) -> Gaussian:
    z = as_gaussian(value)
    result = Gaussian(0)
    for coefficient in reversed(poly):
        result = result * z + coefficient
    return result


def poly_divmod(dividend: Polynomial, divisor: Polynomial) -> tuple[Polynomial, Polynomial]:
    numerator = trim(dividend)
    denominator = trim(divisor)
    if denominator == [Fraction(0)]:
        raise ZeroDivisionError("polynomial division by zero")
    quotient = [Fraction(0)] * max(1, len(numerator) - len(denominator) + 1)
    remainder = list(numerator)
    while len(remainder) >= len(denominator) and remainder != [Fraction(0)]:
        degree = len(remainder) - len(denominator)
        coefficient = remainder[-1] / denominator[-1]
        quotient[degree] += coefficient
        shifted = [Fraction(0)] * degree + poly_scale(denominator, coefficient)
        remainder = poly_sub(remainder, shifted)
    return trim(quotient), trim(remainder)


def poly_extended_gcd(
    left: Polynomial, right: Polynomial
) -> tuple[Polynomial, Polynomial, Polynomial]:
    r0, r1 = trim(left), trim(right)
    s0, s1 = [Fraction(1)], [Fraction(0)]
    t0, t1 = [Fraction(0)], [Fraction(1)]
    while r1 != [Fraction(0)]:
        quotient, remainder = poly_divmod(r0, r1)
        r0, r1 = r1, remainder
        s0, s1 = s1, poly_sub(s0, poly_mul(quotient, s1))
        t0, t1 = t1, poly_sub(t0, poly_mul(quotient, t1))
    leading = r0[-1]
    return (
        poly_scale(r0, Fraction(1, 1) / leading),
        poly_scale(s0, Fraction(1, 1) / leading),
        poly_scale(t0, Fraction(1, 1) / leading),
    )


def rational_value_and_derivatives(
    numerator: Polynomial,
    denominator: Polynomial,
    point: Gaussian,
) -> tuple[Gaussian, Gaussian, Gaussian]:
    numerator_taylor = [
        poly_eval(poly_derivative(numerator, order), point)
        / Fraction(math.factorial(order))
        for order in range(3)
    ]
    denominator_taylor = [
        poly_eval(poly_derivative(denominator, order), point)
        / Fraction(math.factorial(order))
        for order in range(3)
    ]
    quotient_taylor: list[Gaussian] = []
    for order in range(3):
        value = numerator_taylor[order]
        for index in range(1, order + 1):
            value -= denominator_taylor[index] * quotient_taylor[order - index]
        quotient_taylor.append(value / denominator_taylor[0])
    return (
        quotient_taylor[0],
        quotient_taylor[1],
        Fraction(2) * quotient_taylor[2],
    )


def boundary_functional(
    numerator: Polynomial,
    denominator: Polynomial,
    scale: Fraction,
) -> Fraction:
    point = Gaussian(Fraction(0), scale)
    value, first, second = rational_value_and_derivatives(
        numerator, denominator, point
    )
    return (
        scale**3 * second.imag
        + 3 * scale**2 * first.real
        - 3 * scale * value.imag
    ) / 8


def omega(value: Fraction, scale: Fraction) -> Fraction:
    return scale**6 / (value * value + scale * scale) ** 3


def make_fixture(
    inner_root: int,
    outer_root: int,
    derivative_root: int,
    constant: int,
    scale: int,
) -> dict[str, object]:
    a = Fraction(inner_root)
    b = Fraction(outer_root)
    c = Fraction(derivative_root)
    C = Fraction(constant)
    T = Fraction(scale)

    if a * a + b * b != 2 * c * c:
        raise ValueError("fixture does not have rational p'' roots")

    q = poly_mul(
        [-a * a, Fraction(0), Fraction(1)],
        [-b * b, Fraction(0), Fraction(1)],
    )
    p = poly_integral(q, C)
    p1 = poly_derivative(p)
    p2 = poly_derivative(p, 2)
    p3 = poly_derivative(p, 3)

    critical_points = [-b, -a, a, b]
    second_points = [-c, Fraction(0), c]

    residues = [
        poly_eval(p, point).real / poly_eval(p2, point).real
        for point in critical_points
    ]
    debts = [
        poly_eval(p, point).real**2
        / (
            poly_eval(p1, point).real
            * poly_eval(p3, point).real
        )
        for point in second_points
    ]

    count_sum = sum(omega(point, T) for point in critical_points)
    first_sum = sum(
        omega(point, T) * residue
        for point, residue in zip(critical_points, residues)
    )
    second_sum = sum(
        omega(point, T) * residue * residue
        for point, residue in zip(critical_points, residues)
    )
    debt_sum = sum(
        omega(point, T) * debt
        for point, debt in zip(second_points, debts)
    )

    gcd, inverse, _ = poly_extended_gcd(p1, p2)
    if gcd != [Fraction(1)]:
        raise AssertionError("p' and p'' are not coprime")

    p_squared = poly_mul(p, p)
    interpolant = poly_divmod(poly_mul(p_squared, inverse), p2)[1]
    corrected_numerator, remainder = poly_divmod(
        poly_sub(p_squared, poly_mul(interpolant, p1)),
        p2,
    )
    if remainder != [Fraction(0)]:
        raise AssertionError("Bézout numerator is not divisible by p''")

    count_boundary = boundary_functional(p2, p1, T)
    first_boundary = boundary_functional(p, p1, T)
    second_boundary = boundary_functional(corrected_numerator, p1, T)
    original_boundary = boundary_functional(p_squared, poly_mul(p1, p2), T)
    debt_boundary = boundary_functional(interpolant, p2, T)

    assert count_sum == count_boundary
    assert first_sum == first_boundary
    assert second_sum == second_boundary
    assert second_sum + debt_sum == original_boundary
    assert debt_sum == debt_boundary
    assert original_boundary - debt_boundary == second_boundary

    for point in second_points:
        lhs = poly_eval(interpolant, point) * poly_eval(p1, point)
        rhs = poly_eval(p_squared, point)
        assert lhs == rhs

    assert debt_sum != 0
    assert original_boundary != second_boundary

    signed_first_mass = -first_sum
    coherence = signed_first_mass * signed_first_mass / (count_sum * second_sum)
    assert Fraction(0) < coherence <= Fraction(1)

    return {
        "parameters": {
            "inner_root": inner_root,
            "outer_root": outer_root,
            "p_double_prime_root": derivative_root,
            "antiderivative_constant": constant,
            "scale": scale,
        },
        "count": str(count_sum),
        "first_moment": str(first_sum),
        "second_moment": str(second_sum),
        "cross_residue_debt": str(debt_sum),
        "uncorrected_second_boundary": str(original_boundary),
        "coherence": str(coherence),
        "bezout_interpolant_degree": len(interpolant) - 1,
        "corrected_numerator_degree": len(corrected_numerator) - 1,
    }


def canonical_digest(payload: dict[str, object]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def run() -> dict[str, object]:
    fixtures = [
        make_fixture(1, 7, 5, 3, 2),
        make_fixture(7, 17, 13, -4, 3),
        make_fixture(1, 7, 5, -11, 5),
    ]

    for numerator in range(0, 9):
        epsilon = Fraction(numerator, 10)
        lower = ((1 - epsilon) / (1 + epsilon)) ** 2
        residues = [-(1 - epsilon), -1, -(1 + epsilon)]
        first = -sum(residues)
        second = sum(value * value for value in residues)
        coherence = first * first / (3 * second)
        assert coherence >= lower

    payload: dict[str, object] = {
        "schema": "riemann.x105200.poisson_bezout.v1",
        "classification": VERDICT,
        "arithmetic": "EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL",
        "fixtures": fixtures,
        "fixture_count": len(fixtures),
        "verified_identities": {
            "common_localizer_count": True,
            "common_localizer_first_moment": True,
            "uncorrected_second_moment_plus_debt": True,
            "bezout_interpolation": True,
            "bezout_debt_elimination": True,
            "debt_is_load_bearing": True,
            "smooth_coherence_bound": True,
            "monochromatic_coherence_lower_bound": True,
        },
        "entire_bezout_interpolation_proved": False,
        "nonreal_xi_correction_proved": False,
        "rh_established": False,
    }
    payload["proof_object_sha256"] = canonical_digest(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = run()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
