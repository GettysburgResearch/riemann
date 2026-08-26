#!/usr/bin/env python3
"""Bounded replay for the extra-notched signed-differential shell firewall."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

Quadratic = tuple[Fraction, Fraction]
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FROZEN_SOURCE_COMMIT = "49a5b4180d7c2ba582764750dc8178e2d5498b4c"
SOURCE_BLOBS = {
    "claims/lemmas/L-102701-common-mother-ratiofour-two-field-form.md": (
        "70eb455a3b2bb0398f8bba22dee82c39ef803156"
    ),
    (
        "claims/lemmas/"
        "L-102740-outer-ray-current-factors-through-the-first-order-critical-scale-current.md"
    ): "ec2f3aafe1b590a11a9967e298f5dfb0e2d59f55",
    (
        "claims/lemmas/"
        "L-106133-canonical-equal-pair-boolean-source-is-a-beta-half-source-square.md"
    ): "b988b14eb982504a799158eed4c76e7f033c96f0",
    (
        "claims/lemmas/L-106134-common-mother-is-a-differential-self-convolution.md"
    ): "cf40354ff8810a2d4bea9459cf142c300ba36237",
    (
        "claims/refutations/"
        "R-106150-boolean-source-square-is-wick-not-ordinary-mellin-convolution.md"
    ): "65352ffb46e0556c912c2494413c2a8b17b9a74f",
    (
        "claims/theorems/T-106150-same-half-source-analytic-square-frontier.md"
    ): "4f0b8b465b0396bfce07f4ead8f840157e34e8b5",
}


def check_source_blobs() -> None:
    """Authenticate the frozen formulas and the parent mismatch."""

    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{FROZEN_SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def qadd(left: Quadratic, right: Quadratic) -> Quadratic:
    """Add a+b*sqrt(2) pairs."""

    return left[0] + right[0], left[1] + right[1]


def qmul(left: Quadratic, right: Quadratic) -> Quadratic:
    """Multiply a+b*sqrt(2) pairs."""

    return (
        left[0] * right[0] + 2 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def qneg(value: Quadratic) -> Quadratic:
    return -value[0], -value[1]


def qscale(scale: Fraction, value: Quadratic) -> Quadratic:
    return scale * value[0], scale * value[1]


def qstr(value: Quadratic) -> str:
    a, b = value
    if b == 0:
        return str(a)
    sign = "+" if b > 0 else "-"
    magnitude = abs(b)
    b_text = "sqrt(2)" if magnitude == 1 else f"{magnitude}*sqrt(2)"
    if a == 0:
        return b_text if b > 0 else f"-{b_text}"
    return f"{a}{sign}{b_text}"


def poly_mul(left: list[Quadratic], right: list[Quadratic]) -> list[Quadratic]:
    result = [(Fraction(0), Fraction(0))] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = qadd(result[i + j], qmul(a, b))
    return result


def dyadic_numerator_coefficients() -> list[Quadratic]:
    """Coefficients of (1-z)^2(1-sqrt(2)z)^2."""

    rational_square: list[Quadratic] = [
        (Fraction(1), Fraction(0)),
        (Fraction(-2), Fraction(0)),
        (Fraction(1), Fraction(0)),
    ]
    quadratic_square: list[Quadratic] = [
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-2)),
        (Fraction(2), Fraction(0)),
    ]
    return poly_mul(rational_square, quadratic_square)


def atomic_coefficients() -> list[Quadratic]:
    """Atomic coefficients of D_out(A *_M A) at ratios 2^j."""

    return [qscale(Fraction(5), value) for value in dyadic_numerator_coefficients()]


def negative_atomic_mass() -> Quadratic:
    atoms = atomic_coefficients()
    total = (Fraction(0), Fraction(0))
    for index in (1, 3):
        total = qadd(total, qneg(atoms[index]))
    return total


def beta_weight(total_half_core_depth: int) -> Fraction:
    """Integral of (1-theta)*theta^depth on [0,1]."""

    if (
        isinstance(total_half_core_depth, bool)
        or not isinstance(total_half_core_depth, int)
        or total_half_core_depth < 0
    ):
        raise ValueError("total half-core depth must be a nonnegative integer")
    return Fraction(
        1,
        (total_half_core_depth + 1) * (total_half_core_depth + 2),
    )


def partial_fraction_check() -> bool:
    """Check R(s)=5+3/s-4/(s-1/2) coefficientwise."""

    # R(s)=(s-1)(5s+3/2)/(s(s-1/2)).  Multiplying the proposed
    # decomposition by s(s-1/2) gives
    # 5*s*(s-1/2)+3*(s-1/2)-4*s.
    proposed = [
        -Fraction(3, 2),
        -Fraction(5, 2) + 3 - 4,
        Fraction(5),
    ]
    # Directly multiply (s-1)(5s+3/2).
    target = [
        -Fraction(3, 2),
        Fraction(3, 2) - 5,
        Fraction(5),
    ]
    return proposed == target


def scale_ledger() -> dict[str, Fraction]:
    """Power exponents in Z for the prime-shell fixture."""

    atom_count = Fraction(3)
    coefficient_decay = Fraction(5, 2)
    coherent_wick_mass = 2 * (atom_count - coefficient_decay)
    free_diagonal = atom_count - 2 * coefficient_decay
    return {
        "atom_count": atom_count,
        "coefficient_decay": coefficient_decay,
        "free_diagonal": free_diagonal,
        "signed_negative_atomic_mass": coherent_wick_mass,
        "negative_mass_to_diagonal_gap": coherent_wick_mass - free_diagonal,
    }


def run() -> dict[str, object]:
    numerator = dyadic_numerator_coefficients()
    expected: list[Quadratic] = [
        (Fraction(1), Fraction(0)),
        (Fraction(-2), Fraction(-2)),
        (Fraction(3), Fraction(4)),
        (Fraction(-4), Fraction(-2)),
        (Fraction(2), Fraction(0)),
    ]
    if numerator != expected:
        raise AssertionError("dyadic numerator expansion changed")
    if not partial_fraction_check():
        raise AssertionError("partial fraction identity failed")
    atoms = atomic_coefficients()
    if qadd(qadd(qadd(qadd(atoms[0], atoms[1]), atoms[2]), atoms[3]), atoms[4]) != (
        Fraction(0),
        Fraction(0),
    ):
        raise AssertionError("atomic total must vanish")
    prime_singleton_pair_beta_weight = beta_weight(2)
    negative = negative_atomic_mass()
    weighted_negative = qscale(prime_singleton_pair_beta_weight, negative)
    ledger = scale_ledger()
    epsilon = Fraction(1, 100)
    horizon_multiplier = 16 * (1 + epsilon) ** 6
    return {
        "frozen_sources": {
            "commit": FROZEN_SOURCE_COMMIT,
            "blobs": SOURCE_BLOBS,
        },
        "exact_mellin_reduction": {
            "A_hat": "(1-2^(-s))*(1-sqrt(2)*2^(-s))/(s*(s-1/2))",
            "D_mellin_convention": "Mellin(D f)(s)=s*Mellin(f)(s)",
            "D_out": "(1/2)*D*(D-1)*(5*D+3/2)*(2*D-1)",
            "audited_object": "K_extra=D_out(A*_M A)",
            "L102740_outer_multiplier": "q(s)*r(s)^2*(s-1)*(5s+3/2)/(s^2*(s-1/2))",
            "L102740_derivative_outer_multiplier": (
                "q(s)*r(s)^2*(s-1)*(5s+3/2)/(s*(s-1/2))"
            ),
            "explicit_piecewise_derivative_multiplier": (
                "4*q(s)*r(s)^2*(s-1)/(s*(s-1/2))"
            ),
            "stable_filter_V": "(5*D+3/2)/4",
            "dyadic_shift_convention": "S_2 f(X)=f(X/2)",
            "exact_operator_relations": (
                "K_740=V*K_explicit; K_extra=Q*K_740=Q*V*K_explicit"
            ),
            "parent_adapter_status": (
                "three distinct frozen kernels were printed under one outer label"
            ),
            "reduced_rational_factor": "5+3/s-4/(s-1/2)",
            "continuous_base_density": "(3-4*exp(t/2))*1_{t>=0} dt",
            "base_atom": "5*delta_0",
        },
        "dyadic_atoms": [
            {
                "ratio": 2**index,
                "coefficient": qstr(value),
                "sign": "positive" if value[0] > 0 and value[1] >= 0 else "negative",
            }
            for index, value in enumerate(atoms)
        ],
        "negative_atomic_mass_per_unit_translate": qstr(negative),
        "prime_singleton_beta_weight": str(prime_singleton_pair_beta_weight),
        "beta_weighted_negative_atomic_mass": qstr(weighted_negative),
        "scale_fixture": {
            "horizon": "Y=16*(1+epsilon)^6*Z^10",
            "owner_primes": "p,q in [Z,(1+epsilon)Z]",
            "core_primes": "a,b in [Z^2,(1+epsilon)Z^2]",
            "all_physical_products_are_odd": True,
            "negative_atom_ratios": [2, 8],
            "negative_atoms_lie_below_horizon": True,
            "distinct_dyadic_layers_are_disjoint_by_2_adic_valuation": True,
            "epsilon": str(epsilon),
            "horizon_multiplier": str(horizon_multiplier),
        },
        "asymptotic_ledger_in_Z": {key: str(value) for key, value in ledger.items()},
        "asymptotic_ledger_in_Y": {
            key: str(value / 10) for key, value in ledger.items()
        },
        "conclusion": {
            "proved": (
                "the literal extra-notched signed differential has negative "
                "atomic variation of size Y^(1/10-o(1)) on the deleted "
                "Wick-disjoint prime shell"
            ),
            "rules_out": (
                "a deletion-stable or source-blind subpower negative-variation "
                "estimate based only on the literal extra-notched kernel"
            ),
            "does_not_rule_out": (
                "the explicit outer estimate, or cancellation after the complete "
                "undeleted Boolean source and all source sectors are recombined"
            ),
            "parent_blocker": (
                "the three-way explicit/constructed/D_out adapter must be repaired "
                "or retyped "
                "before any conclusion-facing use"
            ),
        },
        "resource_caps": {
            "prime_intervals_enumerated": 0,
            "source_atoms_enumerated": 0,
            "maximum_polynomial_degree": 4,
            "curves_enumerated": 0,
            "point_counts": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    if args.check:
        check_source_blobs()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
