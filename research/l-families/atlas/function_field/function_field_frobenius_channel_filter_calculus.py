#!/usr/bin/env python3
"""Bounded exact replay for curve-adapted Frobenius channel filters."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PREDECESSOR_COMMIT = "18056756f6fdf36c5d7d88f3cc3d5f442878da80"
PREDECESSOR_BLOBS = {
    "research/l-families/atlas/function_field/FUNCTION_FIELD_BASEWAVE_CURVE_EXTENSION.md": (
        "fd8f0c7659b5d5d3e00ff7b1d6b720b77cce2afc"
    ),
    "research/l-families/atlas/function_field/function_field_basewave_curve_extension.py": (
        "d2db36d21823d5a28dd4dd3207469e9c9d9edbc7"
    ),
    "research/l-families/atlas/function_field/function_field_basewave_curve_extension.json": (
        "d364a9e459c87abb27d19eb7de62509fb19e0e79"
    ),
    "tests/test_function_field_basewave_curve_extension.py": (
        "67a939a5dc9792f340a72205fbbbfa7d1d732937"
    ),
}

SERIES_CAP = 10
SQRT_Q = Fraction(3)
Q = SQRT_Q * SQRT_Q

Uni = tuple[Fraction, ...]
Bivar = dict[tuple[int, int], Fraction]


def check_source_contract() -> None:
    for path, expected in PREDECESSOR_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{PREDECESSOR_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"predecessor blob mismatch: {path}")


def trim(poly: Uni) -> Uni:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def uni_mul(left: Uni, right: Uni) -> Uni:
    if not left or not right:
        raise ValueError("univariate factors must be nonempty")
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    return trim(tuple(output))


def uni_div_exact(dividend: Uni, divisor: Uni) -> Uni:
    dividend = trim(dividend)
    divisor = trim(divisor)
    if divisor == (Fraction(0),):
        raise ValueError("division by the zero polynomial")
    if len(dividend) < len(divisor):
        raise ValueError("divisor does not divide dividend")
    remainder = list(dividend)
    quotient = [Fraction(0)] * (len(dividend) - len(divisor) + 1)
    lead = divisor[-1]
    for degree in range(len(quotient) - 1, -1, -1):
        coefficient = remainder[degree + len(divisor) - 1] / lead
        quotient[degree] = coefficient
        for index, value in enumerate(divisor):
            remainder[degree + index] -= coefficient * value
    if any(remainder):
        raise ValueError("divisor does not divide dividend")
    return trim(tuple(quotient))


def uni_divmod(dividend: Uni, divisor: Uni) -> tuple[Uni, Uni]:
    dividend = trim(dividend)
    divisor = trim(divisor)
    if divisor == (Fraction(0),):
        raise ValueError("division by the zero polynomial")
    if len(dividend) < len(divisor):
        return (Fraction(0),), dividend
    remainder = list(dividend)
    quotient = [Fraction(0)] * (len(dividend) - len(divisor) + 1)
    lead = divisor[-1]
    for degree in range(len(quotient) - 1, -1, -1):
        coefficient = remainder[degree + len(divisor) - 1] / lead
        quotient[degree] = coefficient
        for index, value in enumerate(divisor):
            remainder[degree + index] -= coefficient * value
    return trim(tuple(quotient)), trim(tuple(remainder))


def monic(poly: Uni) -> Uni:
    poly = trim(poly)
    if poly == (Fraction(0),):
        raise ValueError("the zero polynomial has no monic normalization")
    return tuple(value / poly[-1] for value in poly)


def uni_gcd(left: Uni, right: Uni) -> Uni:
    left = trim(left)
    right = trim(right)
    while right != (Fraction(0),):
        _, remainder = uni_divmod(left, right)
        left, right = right, remainder
    return monic(left)


def uni_lcm(left: Uni, right: Uni) -> Uni:
    gcd = uni_gcd(left, right)
    return monic(uni_mul(uni_div_exact(left, gcd), right))


def reciprocal_series(denominator: Uni, cap: int = SERIES_CAP) -> Uni:
    if not denominator or denominator[0] == 0:
        raise ValueError("denominator must have nonzero constant term")
    if isinstance(cap, bool) or not isinstance(cap, int) or cap < 0:
        raise ValueError("cap must be a nonnegative integer")
    output = [Fraction(0)] * (cap + 1)
    output[0] = 1 / denominator[0]
    for degree in range(1, cap + 1):
        output[degree] = (
            -sum(
                (
                    denominator[index] * output[degree - index]
                    for index in range(1, min(degree, len(denominator) - 1) + 1)
                ),
                Fraction(0),
            )
            / denominator[0]
        )
    return tuple(output)


def scale_poly(poly: Uni, scale: Fraction) -> Uni:
    """Return coefficients of ``poly(scale*x)``."""
    if scale == 0:
        raise ValueError("scale must be nonzero")
    return tuple(value * scale**degree for degree, value in enumerate(poly))


def lift_axis(poly: Uni, axis: int) -> Bivar:
    if axis not in (0, 1):
        raise ValueError("axis must be zero or one")
    return {
        ((degree, 0) if axis == 0 else (0, degree)): value
        for degree, value in enumerate(poly)
        if value
    }


def lift_mixed(poly: Uni) -> Bivar:
    return {(degree, degree): value for degree, value in enumerate(poly) if value}


def clean(poly: Bivar) -> Bivar:
    return {key: value for key, value in poly.items() if value}


def bivar_mul(left: Bivar, right: Bivar, cap: int = SERIES_CAP) -> Bivar:
    if not left or not right:
        raise ValueError("bivariate factors must be nonempty")
    output: Bivar = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            if i + k <= cap and j + ell <= cap:
                key = (i + k, j + ell)
                output[key] = output.get(key, Fraction(0)) + a * b
    return clean(output)


def bivar_product(*factors: Bivar, cap: int = SERIES_CAP) -> Bivar:
    result: Bivar = {(0, 0): Fraction(1)}
    for factor in factors:
        result = bivar_mul(result, factor, cap)
    return result


def replay_polynomials() -> dict[str, Uni]:
    # P(u)=(1+9u^2)^2 is a reciprocal degree-four Weil-shaped polynomial
    # at q=9.  Q(u)=R(u)=1+9u^2 gives a nontrivial stable factor split.
    stable_factor = (Fraction(1), Fraction(0), Q)
    numerator = uni_mul(stable_factor, stable_factor)
    quotient = uni_div_exact(numerator, stable_factor)
    if quotient != stable_factor:
        raise ArithmeticError("stable factor split changed")
    normalized = scale_poly(numerator, 1 / SQRT_Q)
    normalized_factor = scale_poly(stable_factor, 1 / SQRT_Q)
    mixed = scale_poly(numerator, 1 / Q)
    mixed_factor = scale_poly(stable_factor, 1 / Q)
    return {
        "P": numerator,
        "Q_factor": stable_factor,
        "R_factor": quotient,
        "P_axis": normalized,
        "Q_axis": normalized_factor,
        "P_mixed": mixed,
        "Q_mixed": mixed_factor,
    }


def universal_factors() -> dict[str, Uni]:
    axis = (Fraction(1), -(SQRT_Q + 1 / SQRT_Q), Fraction(1))
    mixed = (Fraction(1), -(Fraction(1) + 1 / Q), 1 / Q)
    return {"axis": axis, "mixed": mixed}


def selector_replay() -> dict[str, object]:
    polys = replay_polynomials()
    universal = universal_factors()
    p_axis = polys["P_axis"]
    p_mixed = polys["P_mixed"]
    q_axis = polys["Q_axis"]
    r_axis = scale_poly(polys["R_factor"], 1 / SQRT_Q)

    # A tiny nontrivial analytic residual; no finite field is enumerated.
    residual: Bivar = {
        (0, 0): Fraction(1),
        (2, 1): Fraction(2, 9),
        (1, 2): Fraction(-1, 9),
        (3, 3): Fraction(1, 27),
    }
    u_x = lift_axis(universal["axis"], 0)
    u_y = lift_axis(universal["axis"], 1)
    u_m = lift_mixed(universal["mixed"])
    analytic_core = bivar_product(residual, u_x, u_y, u_m)

    reciprocal_x = lift_axis(reciprocal_series(p_axis), 0)
    reciprocal_y = lift_axis(reciprocal_series(p_axis), 1)
    reciprocal_m = lift_mixed(reciprocal_series(p_mixed))
    original = bivar_product(analytic_core, reciprocal_x, reciprocal_y, reciprocal_m)

    axis_filter = bivar_product(lift_axis(p_axis, 0), lift_axis(p_axis, 1))
    axis_filtered = bivar_mul(original, axis_filter)
    expected_axis_filtered = bivar_mul(analytic_core, reciprocal_m)
    if axis_filtered != expected_axis_filtered:
        raise ArithmeticError("axis Frobenius deflation identity changed")

    total_filter = bivar_mul(axis_filter, lift_mixed(p_mixed))
    total_filtered = bivar_mul(original, total_filter)
    if total_filtered != analytic_core:
        raise ArithmeticError("three-channel Frobenius deflation changed")

    selected_series = reciprocal_series(p_axis)
    selected_series = tuple(
        sum(
            (
                r_axis[index] * selected_series[degree - index]
                for index in range(min(degree, len(r_axis) - 1) + 1)
            ),
            Fraction(0),
        )
        for degree in range(SERIES_CAP + 1)
    )
    expected_selected = reciprocal_series(q_axis)
    if selected_series != expected_selected:
        raise ArithmeticError("stable channel selector identity changed")

    return {
        "q": int(Q),
        "sqrt_q": int(SQRT_Q),
        "series_cap": SERIES_CAP,
        "curve_numerator_degree": len(polys["P"]) - 1,
        "selected_factor_degree": len(polys["Q_factor"]) - 1,
        "axis_filter_bidegree": [len(p_axis) - 1, len(p_axis) - 1],
        "mixed_filter_degree": len(p_mixed) - 1,
        "original_nonzero_coefficients": len(original),
        "axis_filtered_nonzero_coefficients": len(axis_filtered),
        "total_filtered_nonzero_coefficients": len(total_filtered),
        "stable_selector_verified": True,
        "axis_deflation_verified": True,
        "total_deflation_verified": True,
    }


def minimal_degree_panel(max_genus: int = 8) -> dict[str, object]:
    if isinstance(max_genus, bool) or not isinstance(max_genus, int) or max_genus < 1:
        raise ValueError("max_genus must be a positive integer")
    rows = []
    for genus in range(1, max_genus + 1):
        degree = 2 * genus
        rows.append(
            {
                "genus": genus,
                "generic_numerator_degree": degree,
                "two_axis_null_bidegree": [degree, degree],
                "three_channel_depth_sum": 3 * degree,
                "dense_two_axis_stencil_upper_bound": (degree + 1) ** 2,
            }
        )
    return {
        "rows": rows,
        "scope": (
            "formal denominator selection without accidental cancellation; "
            "degree lower bound, not a lower bound on nonzero coefficients"
        ),
    }


def family_uniform_panel() -> dict[str, object]:
    stable_factors = (
        (Fraction(1), Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(-1), Fraction(1)),
        (Fraction(1), Fraction(1), Fraction(1)),
    )
    numerators = tuple(uni_mul(factor, factor) for factor in stable_factors)
    running = (Fraction(1),)
    rows = []
    for family_size, numerator in enumerate(numerators, start=1):
        running = uni_lcm(running, numerator)
        if any(
            uni_divmod(running, member)[1] != (Fraction(0),)
            for member in numerators[:family_size]
        ):
            raise ArithmeticError("family least-common-multiple filter changed")
        rows.append(
            {
                "family_size": family_size,
                "member_degree": len(numerator) - 1,
                "universal_axis_depth": len(running) - 1,
                "two_axis_bidegree": [len(running) - 1, len(running) - 1],
            }
        )
    return {
        "rows": rows,
        "formal_rule": "the primitive family-uniform null filter is lcm_i(P_i)",
        "shared_factors_reduce_depth": True,
        "generic_pairwise_coprime_depth": "sum_i degree(P_i)",
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    return {
        "source_contract": {
            "commit": PREDECESSOR_COMMIT,
            "git_blobs": PREDECESSOR_BLOBS,
            "imported": "all-curve three-zeta factorization and residual domain",
            "source_line_endings": "irrelevant because Git object IDs are pinned",
        },
        "filter_calculus": {
            "curve_zeta_numerator": "P_C(u)=product_(nu=1)^(2g)(1-alpha_nu*u)",
            "stable_factorization": "P_C=Q_x R_x=Q_y R_y=Q_m R_m",
            "filter": ("R_x(X/sqrt(q))*R_y(Y/sqrt(q))*R_m(XY/q)"),
            "selected_denominators": ("Q_x(X/sqrt(q))*Q_y(Y/sqrt(q))*Q_m(XY/q)"),
            "coefficient_field": "chosen K contains sqrt(q) and coefficients of P_C",
            "galois_stability_required_over_chosen_K": True,
            "smaller_field_descent": (
                "over K_0 not containing sqrt(q), the scaled filter "
                "Q(X/sqrt(q)) itself must descend to K_0[X]"
            ),
            "formal_minimal_multiplier": "R_x*R_y*R_m up to a scalar",
        },
        "axis_null": {
            "filter": "P_C(X/sqrt(q))*P_C(Y/sqrt(q))",
            "remaining_frobenius_denominator": "P_C(XY/q)",
            "analytic_bidisc": "every closed |X|,|Y|<=r with r^3<sqrt(q)",
            "fixed_offset_shell": "O_(C,Sigma,epsilon)(q^(-(1/3-epsilon)*h))",
        },
        "full_null": {
            "filter": ("P_C(X/sqrt(q))*P_C(Y/sqrt(q))*P_C(XY/q)"),
            "remaining_frobenius_denominator": "none",
            "analytic_limit": "residual Euler product still limits r^3<sqrt(q)",
        },
        "selector_replay": selector_replay(),
        "minimal_degree": minimal_degree_panel(),
        "family_uniform_filter": family_uniform_panel(),
        "scope": {
            "fixed_curve": True,
            "growing_genus_fixed_depth_filter": False,
            "accidental_residual_cancellation_excluded_from_minimality": True,
            "incomplete_family_theorem": False,
            "number_field_transfer": False,
            "rh_or_grh_proved": False,
        },
        "resource_caps": {
            "formal_series_bidegree": SERIES_CAP,
            "minimal_degree_genus": 8,
            "finite_fields_enumerated": 0,
            "curves_enumerated": 0,
            "points_enumerated": 0,
            "l_functions_enumerated": 0,
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
