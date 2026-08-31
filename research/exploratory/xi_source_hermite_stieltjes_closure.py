#!/usr/bin/env python3
"""Exact bounded checks for XI_SOURCE_HERMITE_STIELTJES_CLOSURE.md.

The analytic equivalences in the note are written proofs.  This module checks
only finite algebraic identities over Fraction and Gaussian rational numbers.
It does not evaluate Xi, Phi, a continuum operator norm, or RH.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from typing import Any

Q = Fraction


@dataclass(frozen=True)
class GaussianRational:
    """A Gaussian rational a+b*i with exact Fraction coordinates."""

    re: Q
    im: Q = Q(0)

    def __add__(self, other: object) -> "GaussianRational":
        rhs = as_gaussian(other)
        return GaussianRational(self.re + rhs.re, self.im + rhs.im)

    __radd__ = __add__

    def __neg__(self) -> "GaussianRational":
        return GaussianRational(-self.re, -self.im)

    def __sub__(self, other: object) -> "GaussianRational":
        return self + (-as_gaussian(other))

    def __rsub__(self, other: object) -> "GaussianRational":
        return as_gaussian(other) - self

    def __mul__(self, other: object) -> "GaussianRational":
        rhs = as_gaussian(other)
        return GaussianRational(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "GaussianRational":
        rhs = as_gaussian(other)
        denominator = rhs.re * rhs.re + rhs.im * rhs.im
        if denominator == 0:
            raise ZeroDivisionError("division by zero Gaussian rational")
        return GaussianRational(
            (self.re * rhs.re + self.im * rhs.im) / denominator,
            (self.im * rhs.re - self.re * rhs.im) / denominator,
        )

    def __rtruediv__(self, other: object) -> "GaussianRational":
        return as_gaussian(other) / self

    def conjugate(self) -> "GaussianRational":
        return GaussianRational(self.re, -self.im)

    def squared_modulus(self) -> Q:
        return self.re * self.re + self.im * self.im

    def as_json(self) -> dict[str, str]:
        return {"re": fraction_text(self.re), "im": fraction_text(self.im)}


def as_gaussian(value: object) -> GaussianRational:
    if isinstance(value, GaussianRational):
        return value
    if isinstance(value, int):
        return GaussianRational(Q(value))
    if isinstance(value, Q):
        return GaussianRational(value)
    raise TypeError(f"unsupported Gaussian-rational operand: {type(value)!r}")


I = GaussianRational(Q(0), Q(1))


def fraction_text(value: Q) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def kappa(value: Q) -> Q:
    return (1 - value) / (1 + value)


def check_multiplier_defect() -> int:
    rows = 0
    r_values = (Q(0), Q(1, 7), Q(2, 3), Q(5, 4), Q(3))
    q_values = (Q(0), Q(1, 5), Q(4, 3), Q(2))
    for r in r_values:
        for q in q_values:
            left = 1 - kappa(r) * kappa(q)
            right = 2 * (r + q) / ((1 + r) * (1 + q))
            if left != right:
                raise AssertionError((r, q, left, right))
            rows += 1
    return rows


def check_stieltjes_two_channel() -> int:
    rows = 0
    x_values = (Q(1, 2), Q(3, 4), Q(2))
    y_values = (Q(2, 3), Q(5, 4), Q(3))
    r_values = (Q(0), Q(1, 7), Q(5, 2))
    for x in x_values:
        for y in y_values:
            for r in r_values:
                left = (x / (x * x + r) + y / (y * y + r)) / (x + y)
                middle = (r + x * y) / ((x * x + r) * (y * y + r))
                right = (
                    r / ((x * x + r) * (y * y + r))
                    + x * y / ((x * x + r) * (y * y + r))
                )
                if not (left == middle == right):
                    raise AssertionError((x, y, r, left, middle, right))
                rows += 1
    return rows


def check_source_factor_four() -> dict[str, str]:
    # In A_Phi, xi=2y and dxi=2dy:
    # (1/2) * xi * dxi = (1/2)*(2y)*(2dy) = 2y dy.
    # In K_0 the measure coefficient is (1/2)y dy.
    a_coefficient = Q(1, 2) * 2 * 2
    k0_coefficient = Q(1, 2)
    ratio = a_coefficient / k0_coefficient
    if ratio != 4:
        raise AssertionError((a_coefficient, k0_coefficient, ratio))
    return {
        "a_phi_coefficient_of_y_dy": fraction_text(a_coefficient),
        "k0_coefficient_of_y_dy": fraction_text(k0_coefficient),
        "ratio": fraction_text(ratio),
    }


def check_companion_congruence() -> int:
    """Check E2.2 with the common factor pi omitted.

    The variables B,Bp below represent X(bar(w)), X'(bar(w)); the variable
    wb represents bar(w).  No analytic relation is inferred from these
    independent exact samples.
    """

    samples = (
        (
            GaussianRational(Q(2), Q(1, 3)),
            GaussianRational(Q(3), Q(-1, 4)),
            GaussianRational(Q(1, 2), Q(2, 5)),
            GaussianRational(Q(-2, 3), Q(1, 7)),
            GaussianRational(Q(1), Q(1, 2)),
            GaussianRational(Q(5, 4), Q(2, 3)),
            Q(3, 5),
        ),
        (
            GaussianRational(Q(5, 3), Q(-2, 7)),
            GaussianRational(Q(7, 4), Q(1, 9)),
            GaussianRational(Q(-1, 3), Q(4, 5)),
            GaussianRational(Q(2, 5), Q(-3, 8)),
            GaussianRational(Q(4, 3), Q(1, 6)),
            GaussianRational(Q(3, 2), Q(-1, 5)),
            Q(7, 6),
        ),
    )

    rows = 0
    for z, wb, xz, xpz, xwb, xpwb, lam in samples:
        e_z = xz + I * lam * xpz
        e_w_conjugate = xwb - I * lam * xpwb
        theta_z = (xz - I * lam * xpz) / e_z
        theta_w_conjugate = (xwb + I * lam * xpwb) / e_w_conjugate

        left = (1 - theta_z * theta_w_conjugate) / (2 * I * (wb - z))
        bezout = (xpz * xwb - xz * xpwb) / (wb - z)
        right = lam * bezout / (e_z * e_w_conjugate)
        if left != right:
            raise AssertionError(
                {
                    "left": left.as_json(),
                    "right": right.as_json(),
                }
            )
        rows += 1
    return rows


def check_nonisometric_compression_counterexample() -> list[dict[str, int]]:
    """Verify the exact family C K E with C=diag(M,1), K=swap, E=C^-1.

    K is an isometry and C E=I.  Nevertheless C K E sends the second unit
    vector to M times the first unit vector, so its norm is at least M>1.
    """

    rows: list[dict[str, int]] = []
    for m in (2, 3, 5, 10):
        # Apply E, K, C to e_2=(0,1) exactly.
        after_e = (Q(0), Q(1))
        after_k = (after_e[1], after_e[0])
        after_c = (Q(m) * after_k[0], after_k[1])
        squared_norm = after_c[0] * after_c[0] + after_c[1] * after_c[1]
        if squared_norm != m * m:
            raise AssertionError((m, after_c, squared_norm))
        rows.append(
            {
                "M": m,
                "K_norm": 1,
                "CE_norm": 1,
                "CKE_lower_bound": m,
            }
        )
    return rows


def build_report() -> dict[str, Any]:
    return {
        "schema": "xi-source-hermite-stieltjes-closure-v1",
        "scope": (
            "finite exact algebra only; no Xi evaluation, continuum operator "
            "norm, source positivity, or RH conclusion"
        ),
        "checks": {
            "companion_congruence_rows": check_companion_congruence(),
            "multiplier_defect_rows": check_multiplier_defect(),
            "source_factor_four": check_source_factor_four(),
            "stieltjes_two_channel_rows": check_stieltjes_two_channel(),
            "nonisometric_compression_counterexamples": (
                check_nonisometric_compression_counterexample()
            ),
        },
        "all_passed": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="run all exact checks and emit the canonical JSON report",
    )
    args = parser.parse_args()
    if not args.check:
        parser.error("the only supported action is --check")
    print(json.dumps(build_report(), sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
