#!/usr/bin/env python3
"""Exact synthetic controls for L-4101 and L-4102.

The functions in this module operate on a *finite synthetic zero multiset*
through the rational resolvent model

    F_Z(s) = sum_{rho in Z} 1 / (s-rho).

They do not evaluate the Riemann xi function and cannot produce an RH
counterexample. Their purpose is to test every sign, factorial, power of two,
localizer orientation, and symmetry convention in the proposed certificate
kernels using exact Gaussian-rational arithmetic.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence


SCHEMA = "riemann.xi-stieltjes-synthetic.v1"
Gaussian = tuple[Fraction, Fraction]


class CertificateError(ValueError):
    """Raised for malformed or inconsistent synthetic certificates."""


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must be an integer, not bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def gscale(value: Gaussian, scalar: Fraction | int) -> Gaussian:
    scale = Fraction(scalar)
    return value[0] * scale, value[1] * scale


def ginv(value: Gaussian) -> Gaussian:
    a, b = value
    denominator = a * a + b * b
    if denominator == 0:
        raise CertificateError("synthetic evaluation point coincides with a zero")
    return a / denominator, -b / denominator


def gpow(value: Gaussian, exponent: int) -> Gaussian:
    if exponent < 0:
        raise CertificateError("Gaussian-rational exponent must be nonnegative")
    result: Gaussian = (Fraction(1), Fraction(0))
    base = value
    power = exponent
    while power:
        if power & 1:
            result = gmul(result, base)
        base = gmul(base, base)
        power >>= 1
    return result


def finite_logderivative_jet(
    zeros: Sequence[tuple[Fraction, Fraction]],
    x: Fraction,
    height: Fraction,
    order: int,
) -> list[Gaussian]:
    """Return F_Z^(k) for k=0,...,order at 1/2+x+i*height.

    Each zero is stored relative to the critical line as `(delta, gamma)`,
    meaning rho = 1/2 + delta + i*gamma.
    """
    if x <= 0:
        raise CertificateError("x must be positive")
    if order < 0:
        raise CertificateError("jet order must be nonnegative")
    if not zeros:
        raise CertificateError("synthetic zero multiset must be nonempty")

    inverse_resolvents: list[Gaussian] = []
    for delta, gamma in zeros:
        inverse_resolvents.append(ginv((x - delta, height - gamma)))

    jet: list[Gaussian] = []
    for derivative_order in range(order + 1):
        total: Gaussian = (Fraction(0), Fraction(0))
        for inverse in inverse_resolvents:
            total = gadd(total, gpow(inverse, derivative_order + 1))
        coefficient = (
            -math.factorial(derivative_order)
            if derivative_order % 2
            else math.factorial(derivative_order)
        )
        jet.append(gscale(total, coefficient))
    return jet


def moment_coefficient(n: int, k: int) -> Fraction:
    if not (0 <= k <= n):
        raise CertificateError("moment coefficient index out of range")
    numerator = math.factorial(2 * n - k)
    denominator = (
        2 ** (2 * n - k)
        * math.factorial(n)
        * math.factorial(k)
        * math.factorial(n - k)
    )
    coefficient = Fraction(numerator, denominator)
    return -coefficient if k % 2 else coefficient


def moments_from_jet(
    jet: Sequence[Gaussian], x: Fraction, highest_moment: int
) -> list[Fraction]:
    """Reconstruct m_n from exact F derivatives using L-4102."""
    if x <= 0:
        raise CertificateError("x must be positive")
    if highest_moment < 0:
        raise CertificateError("highest_moment must be nonnegative")
    if len(jet) <= highest_moment:
        raise CertificateError("jet is too short for requested moments")

    moments: list[Fraction] = []
    for n in range(highest_moment + 1):
        total = Fraction(0)
        for k in range(n + 1):
            total += (
                moment_coefficient(n, k)
                * jet[k][0]
                / x ** (2 * n - k + 1)
            )
        moments.append(total)
    return moments


def direct_on_line_moments(
    ordinates: Sequence[Fraction],
    x: Fraction,
    height: Fraction,
    highest_moment: int,
) -> list[Fraction]:
    """Direct Stieltjes moments for a finite critical-line zero multiset."""
    if x <= 0:
        raise CertificateError("x must be positive")
    u = x * x
    moments: list[Fraction] = []
    for n in range(highest_moment + 1):
        moments.append(
            sum(
                (
                    Fraction(1)
                    / (u + (height - gamma) ** 2) ** (n + 1)
                )
                for gamma in ordinates
            )
        )
    return moments


def hankel_matrix(moments: Sequence[Fraction], order: int) -> list[list[Fraction]]:
    if order < 0 or len(moments) <= 2 * order:
        raise CertificateError("insufficient moments for Hankel matrix")
    return [
        [moments[j + k] for k in range(order + 1)]
        for j in range(order + 1)
    ]


def localizing_matrix(
    moments: Sequence[Fraction], u: Fraction, order: int
) -> list[list[Fraction]]:
    if u <= 0:
        raise CertificateError("u must be positive")
    if order < 0 or len(moments) <= 2 * order + 1:
        raise CertificateError("insufficient moments for localizing matrix")
    return [
        [moments[j + k] - u * moments[j + k + 1] for k in range(order + 1)]
        for j in range(order + 1)
    ]


def quadratic_form(matrix: Sequence[Sequence[Fraction]], vector: Sequence[Fraction]) -> Fraction:
    size = len(vector)
    if len(matrix) != size or any(len(row) != size for row in matrix):
        raise CertificateError("matrix and vector dimensions do not match")
    return sum(
        vector[j] * matrix[j][k] * vector[k]
        for j in range(size)
        for k in range(size)
    )


def polynomial_value(vector: Sequence[Fraction], value: Fraction) -> Fraction:
    result = Fraction(0)
    power = Fraction(1)
    for coefficient in vector:
        result += coefficient * power
        power *= value
    return result


def direct_hankel_quadratic(
    ordinates: Sequence[Fraction],
    x: Fraction,
    height: Fraction,
    vector: Sequence[Fraction],
) -> Fraction:
    u = x * x
    total = Fraction(0)
    for gamma in ordinates:
        y = (height - gamma) ** 2
        a = Fraction(1, 1) / (u + y)
        total += a * polynomial_value(vector, a) ** 2
    return total


def direct_localizing_quadratic(
    ordinates: Sequence[Fraction],
    x: Fraction,
    height: Fraction,
    vector: Sequence[Fraction],
) -> Fraction:
    u = x * x
    total = Fraction(0)
    for gamma in ordinates:
        y = (height - gamma) ** 2
        a = Fraction(1, 1) / (u + y)
        total += y * a * a * polynomial_value(vector, a) ** 2
    return total


def differential_from_jet(jet: Sequence[Gaussian], x: Fraction) -> Fraction:
    if x <= 0:
        raise CertificateError("x must be positive")
    if len(jet) < 2:
        raise CertificateError("first derivative is required")
    return jet[1][0] + jet[0][0] / x


def parse_zero_multiset(value: Any) -> list[tuple[Fraction, Fraction]]:
    if not isinstance(value, list) or not value:
        raise CertificateError("zeros must be a nonempty array")
    zeros: list[tuple[Fraction, Fraction]] = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            raise CertificateError(f"zeros[{index}] must be an object")
        zeros.append(
            (
                parse_fraction(item.get("delta"), f"zeros[{index}].delta"),
                parse_fraction(item.get("gamma"), f"zeros[{index}].gamma"),
            )
        )
    return zeros


def verify_certificate(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    if data.get("kind") != "finite-zero-right-side-differential":
        raise CertificateError("unsupported synthetic certificate kind")

    zeros = parse_zero_multiset(data.get("zeros"))
    x = parse_fraction(data.get("x"), "x")
    height = parse_fraction(data.get("height"), "height")
    jet = finite_logderivative_jet(zeros, x, height, 1)
    re_f = jet[0][0]
    differential = differential_from_jet(jet, x)
    moments = moments_from_jet(jet, x, 1)
    localizer_b00 = moments[0] - x * x * moments[1]

    if localizer_b00 != differential / 2:
        raise AssertionError("B00 differential identity failed")

    claimed = data.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError("claimed must be an object")
    if parse_fraction(claimed.get("re_f"), "claimed.re_f") != re_f:
        raise CertificateError("claimed Re(F) mismatch")
    if parse_fraction(
        claimed.get("differential"), "claimed.differential"
    ) != differential:
        raise CertificateError("claimed differential mismatch")
    if parse_fraction(
        claimed.get("localizer_b00"), "claimed.localizer_b00"
    ) != localizer_b00:
        raise CertificateError("claimed localizer mismatch")

    status = (
        "SYNTHETIC_RIGHT_SIDE_DIFFERENTIAL_NEGATIVE"
        if re_f > 0 and differential < 0
        else "SYNTHETIC_CONTROL_NOT_SEPARATED"
    )
    if claimed.get("status") != status:
        raise CertificateError("claimed status mismatch")

    return {
        "schema": SCHEMA,
        "status": status,
        "re_f": fraction_json(re_f),
        "differential": fraction_json(differential),
        "localizer_b00": fraction_json(localizer_b00),
        "identity_b00_equals_half_differential": True,
        "proof_boundary": "finite synthetic zero model only; not an xi evaluation",
    }


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot read certificate: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args(argv)

    try:
        result = verify_certificate(load_json(args.certificate))
    except CertificateError as exc:
        print(
            json.dumps(
                {"schema": SCHEMA, "status": "REJECTED", "reason": str(exc)},
                sort_keys=True,
            )
        )
        return 2

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
