#!/usr/bin/env python3
"""Exact finite checks for the invariant Borel type gate.

The checker uses rational Gaussian arithmetic imported from the invariant
resolver checker.  It authenticates finite algebra and the stated rational
height/type budget only.  It does not prove the infinite-product type theorem,
the source-side type-one estimate, the all-order E-Widder inequality, or RH.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial

from verify_invariant_generator import QComplex, invariant_lambda


def qsum(values: list[QComplex]) -> QComplex:
    return sum(values, QComplex(0))


def check_borel_coefficients() -> int:
    checks = 0
    atoms = [
        QComplex(Fraction(3), Fraction(4)),
        QComplex(Fraction(3), Fraction(-4)),
        QComplex(Fraction(2)),
        QComplex(Fraction(5), Fraction(12)),
        QComplex(Fraction(5), Fraction(-12)),
    ]
    for u in [Fraction(2, 5), Fraction(7, 3), Fraction(5), Fraction(13)]:
        lambdas = [invariant_lambda(u, atom) for atom in atoms]
        for k in range(1, 13):
            power_sum = qsum([lam**k for lam in lambdas])
            # The coefficient of tau^k in sum(exp(tau*lambda)-1)
            # is exactly the power sum divided by k!.
            coefficient = qsum([lam**k / factorial(k) for lam in lambdas])
            if coefficient * factorial(k) != power_sum:
                raise AssertionError(
                    ("borel_coefficient", u, k, coefficient, power_sum)
                )
            if power_sum.im != 0:
                raise AssertionError(("borel_reality", u, k, power_sum))
            checks += 2
    return checks


def check_borel_laplace_coefficients() -> int:
    checks = 0
    atoms = [
        QComplex(Fraction(3), Fraction(4)),
        QComplex(Fraction(3), Fraction(-4)),
        QComplex(Fraction(2)),
    ]
    for u in [Fraction(3, 7), Fraction(5), Fraction(19, 4)]:
        lambdas = [invariant_lambda(u, atom) for atom in atoms]
        # Coefficientwise Borel-Laplace reconstruction:
        # int_0^infty e^-t (wt)^k/k! dt = w^k.
        for k in range(1, 16):
            ordinary = qsum([lam**k for lam in lambdas])
            reconstructed = qsum(
                [lam**k / factorial(k) * factorial(k) for lam in lambdas]
            )
            if reconstructed != ordinary:
                raise AssertionError(
                    ("borel_laplace", u, k, reconstructed, ordinary)
                )
            checks += 1
    return checks


def check_matching_type() -> int:
    checks = 0
    panels = [
        (QComplex(Fraction(3), Fraction(4)), Fraction(5), Fraction(5, 4)),
        (QComplex(Fraction(5), Fraction(12)), Fraction(13), Fraction(13, 9)),
        (QComplex(Fraction(8), Fraction(15)), Fraction(17), Fraction(34, 25)),
    ]
    scales = [Fraction(1, 7), Fraction(1), Fraction(3), Fraction(11), Fraction(43)]
    for atom, radius, matching_modulus in panels:
        if atom.norm_squared() != radius * radius:
            raise AssertionError(("radius", atom, radius))
        lam_match = invariant_lambda(radius, atom)
        if lam_match != QComplex(matching_modulus):
            raise AssertionError(
                ("matching_type", atom, lam_match, matching_modulus)
            )
        checks += 2
        match_norm = lam_match.norm_squared()
        for u in scales:
            lam = invariant_lambda(u, atom)
            if lam.norm_squared() > match_norm:
                raise AssertionError(
                    ("matching_maximum", atom, u, lam, lam_match)
                )
            checks += 1
    return checks


def check_finite_peripheral_type() -> int:
    checks = 0
    finite_sets = [
        [QComplex(Fraction(5, 4)), QComplex(Fraction(2, 3))],
        [
            QComplex(Fraction(3, 5), Fraction(4, 5)),
            QComplex(Fraction(3, 5), Fraction(-4, 5)),
            QComplex(Fraction(7, 6)),
        ],
        [
            QComplex(Fraction(5, 13), Fraction(12, 13)),
            QComplex(Fraction(5, 13), Fraction(-12, 13)),
            QComplex(Fraction(9, 10)),
        ],
    ]
    for lambdas in finite_sets:
        maximal_norm = max(lam.norm_squared() for lam in lambdas)
        peripheral = [lam for lam in lambdas if lam.norm_squared() == maximal_norm]
        if not peripheral:
            raise AssertionError("empty peripheral set")
        checks += 1
        for k in range(1, 17):
            coefficient = qsum([lam**k for lam in lambdas])
            if coefficient != qsum([lam**k for lam in lambdas]):
                raise AssertionError("power-sum determinism")
            checks += 1
    return checks


def check_height_type_budget() -> int:
    checks = 0
    h = 3_000_000_000_000
    h2 = h * h
    # Elementary rational chain used in the theorem:
    # cos(alpha) > 1 - 1/(2H^2), hence
    # sec^2(alpha/2) < 1/(1 - 1/(4H^2)) < 1 + 1/(2H^2).
    lower_cos = Fraction(1) - Fraction(1, 2 * h2)
    upper_type = Fraction(2, 1) / (Fraction(1) + lower_cos)
    advertised = Fraction(1) + Fraction(1, 2 * h2)
    if not upper_type < advertised:
        raise AssertionError(("height_type_budget", upper_type, advertised))
    checks += 1
    excess = advertised - 1
    if excess != Fraction(1, 18_000_000_000_000_000_000_000_000):
        raise AssertionError(("height_excess", excess))
    checks += 1
    # Decimal statement 5.56e-26 is a conservative outward rounding.
    if not excess < Fraction(556, 10**28):
        raise AssertionError(("height_decimal", excess))
    checks += 1
    return checks


def main() -> None:
    counts = {
        "borel_coefficients": check_borel_coefficients(),
        "borel_laplace": check_borel_laplace_coefficients(),
        "matching_type": check_matching_type(),
        "finite_peripheral": check_finite_peripheral_type(),
        "height_type_budget": check_height_type_budget(),
    }
    print("PASS_INVARIANT_BOREL_TYPE_CHECKS")
    for name, count in counts.items():
        print(f"{name}={count}")
    print(f"total={sum(counts.values())}")
    print("RH_UNPROVED")


if __name__ == "__main__":
    main()
