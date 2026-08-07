#!/usr/bin/env python3
"""Exact checker for the eta triangular filter and reflection identities."""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15407-eta-reflection.synthetic.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def frac(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    n = integer(value.get("numerator"), f"{name}.numerator")
    d = integer(value.get("denominator"), f"{name}.denominator")
    if d <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n, d)


def fj(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


@dataclass(frozen=True)
class Qsqrt2:
    """Exact a+b*sqrt(2)."""

    a: Fraction
    b: Fraction

    @staticmethod
    def coerce(value: Qsqrt2 | Fraction | int) -> Qsqrt2:
        if isinstance(value, Qsqrt2):
            return value
        return Qsqrt2(Fraction(value), Fraction(0))

    def __add__(self, other: Qsqrt2 | Fraction | int) -> Qsqrt2:
        other = self.coerce(other)
        return Qsqrt2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self) -> Qsqrt2:
        return Qsqrt2(-self.a, -self.b)

    def __sub__(self, other: Qsqrt2 | Fraction | int) -> Qsqrt2:
        return self + (-self.coerce(other))

    def __rsub__(self, other: Qsqrt2 | Fraction | int) -> Qsqrt2:
        return self.coerce(other) - self

    def __mul__(self, other: Qsqrt2 | Fraction | int) -> Qsqrt2:
        other = self.coerce(other)
        return Qsqrt2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def inverse(self) -> Qsqrt2:
        denominator = self.a * self.a - 2 * self.b * self.b
        if denominator == 0:
            raise CertificateError("quadratic-field division by zero")
        return Qsqrt2(self.a / denominator, -self.b / denominator)

    def __truediv__(self, other: Qsqrt2 | Fraction | int) -> Qsqrt2:
        return self * self.coerce(other).inverse()

    def __pow__(self, exponent: int) -> Qsqrt2:
        if exponent < 0:
            return (self.inverse()) ** (-exponent)
        result = Qsqrt2(Fraction(1), Fraction(0))
        base = self
        n = exponent
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n >>= 1
        return result


def qj(x: Qsqrt2) -> dict[str, dict[str, str]]:
    return {"rational": fj(x.a), "sqrt2": fj(x.b)}


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")

    claimed = data.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError("claimed must be an object")

    zero = Qsqrt2(Fraction(0), Fraction(0))
    one = Qsqrt2(Fraction(1), Fraction(0))
    root2 = Qsqrt2(Fraction(0), Fraction(1))

    # h=log(2), c=sqrt(2): (1-r)^2(1-c r).
    coefficients = [
        one,
        -Qsqrt2(Fraction(2), Fraction(1)),
        Qsqrt2(Fraction(1), Fraction(2)),
        -root2,
    ]
    constant_moment = sum(coefficients, zero)
    linear_moment = sum((j * coefficient for j, coefficient in enumerate(coefficients)), zero)
    pole_ratio = root2 / 2
    pole_value = sum(
        (coefficient * (pole_ratio ** j) for j, coefficient in enumerate(coefficients)),
        zero,
    )
    energy_h_times_norm = Qsqrt2(Fraction(6), Fraction(-1)) / 3

    expected_energy = claimed.get("h_times_window_energy")
    if not isinstance(expected_energy, dict):
        raise CertificateError("claimed.h_times_window_energy must be an object")
    expected = Qsqrt2(
        frac(expected_energy.get("rational"), "claimed.energy.rational"),
        frac(expected_energy.get("sqrt2"), "claimed.energy.sqrt2"),
    )
    if expected != energy_h_times_norm:
        raise CertificateError("claimed eta-window energy mismatch")
    if constant_moment != zero or linear_moment != zero or pole_value != zero:
        raise CertificateError("eta hinge annihilation identity failed")

    reflection = data.get("reflection_control")
    if not isinstance(reflection, dict):
        raise CertificateError("reflection_control must be an object")
    F = frac(reflection.get("F"), "reflection_control.F")
    X = frac(reflection.get("X"), "reflection_control.X")
    Fprime = frac(reflection.get("Fprime"), "reflection_control.Fprime")
    zeta_second_ratio = frac(
        reflection.get("zeta_second_ratio"),
        "reflection_control.zeta_second_ratio",
    )
    Fref = frac(reflection.get("Fref"), "reflection_control.Fref")
    if Fref != -F - X:
        raise CertificateError("functional-equation reflection mismatch")
    if zeta_second_ratio != F * F - Fprime:
        raise CertificateError("zeta-second/log-derivative identity mismatch")
    reflected_product = F * Fref
    linearized_product = -Fprime - zeta_second_ratio - X * F
    if reflected_product != linearized_product:
        raise CertificateError("critical reflection linearization failed")

    selberg = data.get("selberg_control")
    if not isinstance(selberg, dict):
        raise CertificateError("selberg_control must be an object")
    raw_lambda = selberg.get("lambda")
    raw_log = selberg.get("log_weight")
    if not isinstance(raw_lambda, list) or not isinstance(raw_log, list):
        raise CertificateError("selberg arrays must be lists")
    if len(raw_lambda) != len(raw_log) or len(raw_lambda) < 2:
        raise CertificateError("selberg arrays must have equal length at least two")
    lam = [frac(value, f"selberg.lambda[{i}]") for i, value in enumerate(raw_lambda)]
    logs = [frac(value, f"selberg.log_weight[{i}]") for i, value in enumerate(raw_log)]
    if lam[0] != 0 or logs[0] != 0 or any(value < 0 for value in lam + logs):
        raise CertificateError("selberg arrays must be nonnegative and zero-indexed")
    coefficients_selberg: list[Fraction] = []
    for n in range(1, len(lam)):
        convolution = sum(
            lam[d] * lam[n // d]
            for d in range(1, n + 1)
            if n % d == 0
        )
        coefficient = lam[n] * logs[n] + convolution
        if coefficient < 0:
            raise CertificateError("Selberg coefficient is negative")
        coefficients_selberg.append(coefficient)

    return {
        "schema": SCHEMA,
        "status": "EXACT_ETA_REFLECTION_ALGEBRA",
        "quadratic_field_relation": "sqrt2^2=2",
        "eta_hinge_coefficients": [qj(value) for value in coefficients],
        "constant_moment": qj(constant_moment),
        "linear_moment": qj(linear_moment),
        "pole_ratio": qj(pole_ratio),
        "pole_polynomial_value": qj(pole_value),
        "h_times_window_energy": qj(energy_h_times_norm),
        "reflected_product": fj(reflected_product),
        "linearized_product": fj(linearized_product),
        "selberg_coefficients": [fj(value) for value in coefficients_selberg],
        "proof_boundary": (
            "exact quadratic-field and rational algebra only; no zeta value, "
            "critical Hardy estimate, or RH conclusion"
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        print(f"ERROR: {exc}")
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
