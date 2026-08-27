#!/usr/bin/env python3
"""Bounded exact replay for the all-curve base-wave shadow extension."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from itertools import pairwise
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SHADOW_COMMIT = "e87f2392f"
SHADOW_BLOBS = {
    "research/l-families/atlas/function_field/FUNCTION_FIELD_BASEWAVE_SHADOW.md": (
        "e66606a8e06977b4ed54734942adf6c74cf82286"
    ),
    "research/l-families/atlas/function_field/function_field_basewave_shadow.py": (
        "e4896b7c8e59ba2f3a264d4e846e9ba821ec8116"
    ),
    "research/l-families/atlas/function_field/function_field_basewave_shadow.json": (
        "68a97c46036ca929ffcfd66ec78b70aaac3eb9a2"
    ),
    "tests/test_function_field_basewave_shadow.py": (
        "6de80f6a71f8531260228ab0a99bde0646e967d1"
    ),
}
FROZEN_ANCESTOR = "b870366141fe8d5f43d5b81f6e50a67d2a888070"
REPLAY_FIELD_SIZES = (2, 3, 4, 5)
REPLAY_RADIUS = Fraction(101, 100)
REPLAY_DELETED_DEGREES = (1, 2, 2, 5)
REPLAY_COEFFICIENT_CAP = 16


def check_shadow_blobs() -> None:
    """Pin the committed genus-zero predecessor which this theorem extends."""
    for path, expected in SHADOW_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SHADOW_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen shadow predecessor blob mismatch: {path}")


def validate_positive_integer(value: int, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{label} must be a positive integer")


def reciprocal_series(
    polynomial: tuple[Fraction, ...], coefficient_cap: int
) -> tuple[Fraction, ...]:
    """Coefficients through cap of 1/P(X), for P(0)=1."""
    if not polynomial or polynomial[0] != 1:
        raise ValueError("polynomial must have constant coefficient one")
    if isinstance(coefficient_cap, bool) or not isinstance(coefficient_cap, int):
        raise TypeError("coefficient cap must be an integer")
    if coefficient_cap < 0:
        raise ValueError("coefficient cap must be nonnegative")
    result = [Fraction(0)] * (coefficient_cap + 1)
    result[0] = Fraction(1)
    for degree in range(1, coefficient_cap + 1):
        result[degree] = -sum(
            (
                polynomial[index] * result[degree - index]
                for index in range(1, min(degree, len(polynomial) - 1) + 1)
            ),
            Fraction(0),
        )
    return tuple(result)


def repeated_unit_root_polynomial(multiplicity: int) -> tuple[Fraction, ...]:
    validate_positive_integer(multiplicity, "multiplicity")
    return tuple(
        Fraction((-1) ** degree * comb(multiplicity, degree))
        for degree in range(multiplicity + 1)
    )


def repeated_unit_root_coefficient(multiplicity: int, degree: int) -> int:
    validate_positive_integer(multiplicity, "multiplicity")
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 0:
        raise ValueError("degree must be a nonnegative integer")
    return comb(degree + multiplicity - 1, multiplicity - 1)


def finite_difference(values: tuple[int, ...]) -> tuple[int, ...]:
    if len(values) < 2:
        return ()
    return tuple(right - left for left, right in pairwise(values))


def polynomial_degree_certificate(multiplicity: int, cap: int) -> dict[str, object]:
    validate_positive_integer(multiplicity, "multiplicity")
    validate_positive_integer(cap, "cap")
    polynomial = repeated_unit_root_polynomial(multiplicity)
    coefficients = reciprocal_series(polynomial, cap)
    expected = tuple(
        Fraction(repeated_unit_root_coefficient(multiplicity, degree))
        for degree in range(cap + 1)
    )
    if coefficients != expected:
        raise ArithmeticError("repeated-pole reciprocal coefficients changed")
    differences = tuple(int(value) for value in coefficients)
    for _ in range(multiplicity):
        differences = finite_difference(differences)
    if any(differences):
        raise ArithmeticError("reciprocal coefficients exceed predicted degree")
    return {
        "multiplicity": multiplicity,
        "coefficient_polynomial_degree": multiplicity - 1,
        "coefficients": [int(value) for value in coefficients],
        "vanishing_difference_order": multiplicity,
    }


def local_cubic_certificate() -> dict[str, object]:
    checks = 0
    for left in (Fraction(1, 7), Fraction(-2, 11), Fraction(3, 13)):
        for right in (Fraction(2, 17), Fraction(-1, 19), Fraction(4, 23)):
            base = 1 - left - right
            denominator = (1 - left) * (1 - right) * (1 - left * right)
            defect = left * right * (left + right - left * right)
            if denominator - base != defect:
                raise ArithmeticError("local cubic factorization changed")
            checks += 1
    return {
        "checks": checks,
        "identity": "(1-a)(1-b)(1-ab)-(1-a-b)=ab(a+b-ab)",
    }


def deleted_modulus_panel(degrees: tuple[int, ...]) -> dict[str, object]:
    for degree in degrees:
        validate_positive_integer(degree, "deleted-place degree")
    multiplicities = {
        str(degree): degrees.count(degree) for degree in sorted(set(degrees))
    }
    replay_value = deleted_factor_value(2, degrees, Fraction(1, 7), Fraction(2, 11))
    return {
        "degrees": list(degrees),
        "degree_multiplicities": multiplicities,
        "support_only": True,
        "repeated_degrees_allowed": True,
        "interpretation": (
            "each list entry is one distinct deleted closed point; distinct points "
            "may have the same degree"
        ),
        "denominator": (
            "D_Sigma(X,Y)=prod_(v in Sigma)(1-q^(-deg(v)/2)X^deg(v))"
            "(1-q^(-deg(v)/2)Y^deg(v))(1-q^(-deg(v))(XY)^deg(v))"
        ),
        "axis_poles_have_modulus": "sqrt(q)",
        "mixed_poles_satisfy": "|XY|=q",
        "exact_q4_replay_value_at_X_1_7_Y_2_11": str(replay_value),
    }


def deleted_factor_value(
    field_size_sqrt: int,
    degrees: tuple[int, ...],
    left: Fraction,
    right: Fraction,
) -> Fraction:
    """Evaluate D_Sigma exactly when q is a square."""
    validate_positive_integer(field_size_sqrt, "square root of field size")
    result = Fraction(1)
    for degree in degrees:
        validate_positive_integer(degree, "deleted-place degree")
        axis_scale = Fraction(1, field_size_sqrt**degree)
        mixed_scale = Fraction(1, field_size_sqrt ** (2 * degree))
        result *= 1 - axis_scale * left**degree
        result *= 1 - axis_scale * right**degree
        result *= 1 - mixed_scale * (left * right) ** degree
    return result


def p1_affine_specialization(field_size: int, value: Fraction) -> dict[str, str]:
    validate_positive_integer(field_size, "field size")
    if value == 1:
        raise ValueError("deleted local factor vanishes")
    zeta_inverse = (1 - value) * (1 - field_size * value)
    outside_after_deleting_infinity = zeta_inverse / (1 - value)
    expected = 1 - field_size * value
    if outside_after_deleting_infinity != expected:
        raise ArithmeticError("P1 minus infinity did not recover A1")
    return {
        "u": str(value),
        "inverse_zeta_P1": str(zeta_inverse),
        "outside_product": str(outside_after_deleting_infinity),
        "expected_A1_product": str(expected),
    }


def convergence_panel() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for field_size in REPLAY_FIELD_SIZES:
        if REPLAY_RADIUS**6 >= field_size:
            raise ArithmeticError("replay radius left the residual convergence disc")
        rows.append(
            {
                "field_size": field_size,
                "radius": str(REPLAY_RADIUS),
                "r_to_the_sixth": str(REPLAY_RADIUS**6),
                "condition": "r^6<q, equivalently r^3<sqrt(q)",
            }
        )
    return {
        "rows": rows,
        "closed_point_input": "N_C(d)=O_C(q^d/d), derived from Weil",
        "residual_domain": "every closed bidisc |X|,|Y|<=r with r^3<sqrt(q)",
    }


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_shadow_blobs()
    pole_rows = [
        polynomial_degree_certificate(multiplicity, REPLAY_COEFFICIENT_CAP)
        for multiplicity in (1, 2, 3, 4)
    ]
    p1_rows = [
        p1_affine_specialization(field_size, Fraction(1, 4 * field_size))
        for field_size in REPLAY_FIELD_SIZES
    ]
    maximum_multiplicity = 4
    return {
        "source_contract": {
            "frozen_ancestor": FROZEN_ANCESTOR,
            "shadow_predecessor_commit": SHADOW_COMMIT,
            "shadow_predecessor_blobs": SHADOW_BLOBS,
            "dependency_scope": (
                "the committed genus-zero shadow quartet is pinned by commit blobs; "
                "the all-curve proof is symbolic and uses no curve instance"
            ),
        },
        "all_curve_factorization": {
            "orientation_product": (
                "F_C,Sigma=prod_(v notin Sigma)(1-q^(-deg(v)/2)X^deg(v)"
                "-q^(-deg(v)/2)Y^deg(v))"
            ),
            "formula": (
                "F_C,Sigma=J_C,Sigma/[Z_C(X/sqrt(q))Z_C(Y/sqrt(q))"
                "Z_C(XY/q)D_Sigma(X,Y)]"
            ),
            "regularized_function": (
                "P_C(X/sqrt(q))P_C(Y/sqrt(q))F_C,Sigma is analytic for |X|,|Y|<q^(1/6)"
            ),
            "local_certificate": local_cubic_certificate(),
            "deleted_modulus": deleted_modulus_panel(REPLAY_DELETED_DEGREES),
            "p1_minus_infinity_rows": p1_rows,
        },
        "frobenius_channels": {
            "normalized_polynomial": (
                "P_C(X/sqrt(q))=prod_j(1-lambda_j X), |lambda_j|=1"
            ),
            "maximum_root_multiplicity": "m_C",
            "axis_reciprocal_bound": "[X^n]1/P_C(X/sqrt(q))=O_C((n+1)^(m_C-1))",
            "bivariate_bound": ("c_(i,j)=O_C,Sigma((i+1)^(m_C-1)(j+1)^(m_C-1))"),
            "fixed_offset_expansion": (
                "c_(h+a,h+b)=sum_(lambda,mu)Q_(lambda,mu)^(a,b)(h)"
                "(lambda*mu)^h+O(R^(-h)), R>1"
            ),
            "fixed_offset_polynomial_degree": (
                "deg Q_(lambda,mu)^(a,b)<=m_lambda+m_mu-2"
            ),
            "repeated_pole_rows": pole_rows,
        },
        "shell_consequence": {
            "positive_genus": "S_h^alpha=O((1+h)^(2m_C-2)) for fixed finite ratio support",
            "simple_frobenius_roots": "S_h^alpha=O(1)",
            "coarse_genus_g_bound": "S_h^alpha=O((1+h)^(4g-2)) for g>=1",
            "genus_zero": (
                "the exponential q^(-(1/3-epsilon)h) theorem survives finite deletion"
            ),
            "norm_height_interpretation": (
                "polynomial degree growth is q^(o(h)), but no l2 shell summability follows"
            ),
        },
        "convergence": convergence_panel(),
        "scope": {
            "all_curve_factorization_proved": True,
            "polynomial_coefficient_bound_proved": True,
            "fixed_offset_unit_circle_expansion_proved": True,
            "exponential_decay_in_positive_genus_claimed": False,
            "shell_l2_summability_claimed": False,
            "point_enumeration": 0,
            "curve_enumeration": 0,
            "waveprimcar_proved": False,
            "rh_proved": False,
        },
        "resource_caps": {
            "abstract_pole_multiplicity": maximum_multiplicity,
            "coefficient_cap": REPLAY_COEFFICIENT_CAP,
            "deleted_place_degrees": list(REPLAY_DELETED_DEGREES),
            "point_counts": 0,
            "closed_points_enumerated": 0,
            "curves_enumerated": 0,
            "floating_point_operations": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    if not args.check and not args.write_json:
        print(rendered, end="")


if __name__ == "__main__":
    main()
