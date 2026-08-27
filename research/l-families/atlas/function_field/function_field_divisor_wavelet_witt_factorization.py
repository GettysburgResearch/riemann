#!/usr/bin/env python3
"""Exact bounded replay for the function-field divisor-wavelet Witt factorization."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FROZEN_COMMIT = "fad8ce2c4ce8633c5bb67356e6765800eac3d440"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/FFPS_BASEWAVE_PRIMCAR_IDENTITY.md"
    ): "07f5c104f59e7912dc137201d535c947b14fd365",
    (
        "research/l-families/atlas/function_field/ffps_basewave_primcar_identity.py"
    ): "a13ba5ce66f6c4318eed2cc90cb8c5d9bb97b905",
    (
        "research/l-families/atlas/function_field/"
        "FUNCTION_FIELD_BETA_BOOLEAN_EVALUATION_BANDPASS.md"
    ): "0306cfa06c68375dd62472073698aaae0ace0ff9",
    (
        "research/l-families/atlas/function_field/"
        "function_field_beta_boolean_evaluation_bandpass.py"
    ): "5ab6b5845838495362bb37883386b640e6a8900d",
}
MAX_TOTAL_DEGREE = 8
CONTROL_Q = (3, 5)

Monomial = tuple[int, int]
Polynomial = dict[Monomial, int]


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{FROZEN_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def validate_nonnegative_integer(value: int, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{label} must be a nonnegative integer")


def necklace_multiplicity(left: int, right: int) -> int:
    validate_nonnegative_integer(left, "left content")
    validate_nonnegative_integer(right, "right content")
    total = left + right
    if total == 0:
        raise ValueError("a necklace must be nonempty")
    common = math.gcd(left, right)
    numerator = sum(
        int(sp.mobius(divisor)) * math.comb(total // divisor, left // divisor)
        for divisor in sp.divisors(common)
    )
    if numerator % total:
        raise ArithmeticError("necklace multiplicity lost integrality")
    answer = numerator // total
    if answer < 0:
        raise ArithmeticError("necklace multiplicity became negative")
    return answer


def binary_lyndon_count(total: int) -> int:
    if isinstance(total, bool) or not isinstance(total, int) or total < 1:
        raise ValueError("word length must be positive")
    numerator = sum(
        int(sp.mobius(divisor)) * 2 ** (total // divisor)
        for divisor in sp.divisors(total)
    )
    if numerator % total:
        raise ArithmeticError("binary Lyndon count lost integrality")
    return numerator // total


def irreducible_count(q: int, degree: int) -> int:
    if (
        isinstance(q, bool)
        or not isinstance(q, int)
        or q < 2
        or isinstance(degree, bool)
        or not isinstance(degree, int)
        or degree < 1
    ):
        raise ValueError("q and degree must be nontrivial positive integers")
    numerator = sum(
        int(sp.mobius(divisor)) * q ** (degree // divisor)
        for divisor in sp.divisors(degree)
    )
    if numerator % degree:
        raise ArithmeticError("irreducible count lost integrality")
    return numerator // degree


def multiply_truncated(
    left: Polynomial, right: Polynomial, maximum_degree: int
) -> Polynomial:
    validate_nonnegative_integer(maximum_degree, "maximum degree")
    output: Polynomial = {}
    for (left_degree, left_phase), left_coefficient in left.items():
        for (right_degree, right_phase), right_coefficient in right.items():
            degree = left_degree + right_degree
            if degree > maximum_degree:
                continue
            key = degree, left_phase + right_phase
            output[key] = output.get(key, 0) + left_coefficient * right_coefficient
            if output[key] == 0:
                del output[key]
    return output


def direct_prime_degree_factor(
    q: int, prime_degree: int, maximum_degree: int
) -> Polynomial:
    count = irreducible_count(q, prime_degree)
    factor: Polynomial = {}
    maximum_selected = min(count, maximum_degree // prime_degree)
    for plus_count in range(maximum_selected + 1):
        for minus_count in range(maximum_selected - plus_count + 1):
            selected = plus_count + minus_count
            coefficient = (
                (-1) ** selected
                * math.comb(count, plus_count)
                * math.comb(count - plus_count, minus_count)
            )
            key = (
                prime_degree * selected,
                prime_degree * (plus_count - minus_count),
            )
            factor[key] = factor.get(key, 0) + coefficient
    return {key: value for key, value in factor.items() if value}


def direct_euler_product(q: int, maximum_degree: int) -> Polynomial:
    validate_nonnegative_integer(maximum_degree, "maximum degree")
    output: Polynomial = {(0, 0): 1}
    for prime_degree in range(1, maximum_degree + 1):
        output = multiply_truncated(
            output,
            direct_prime_degree_factor(q, prime_degree, maximum_degree),
            maximum_degree,
        )
    return output


def witt_factor(q: int, left: int, right: int, maximum_degree: int) -> Polynomial:
    total = left + right
    multiplicity = necklace_multiplicity(left, right)
    factor: Polynomial = {}
    maximum_selected = min(multiplicity, maximum_degree // total)
    for selected in range(maximum_selected + 1):
        factor[(total * selected, (left - right) * selected)] = (
            math.comb(multiplicity, selected) * (-q) ** selected
        )
    return factor


def witt_product(q: int, maximum_degree: int) -> Polynomial:
    validate_nonnegative_integer(maximum_degree, "maximum degree")
    output: Polynomial = {(0, 0): 1}
    for total in range(1, maximum_degree + 1):
        for left in range(total + 1):
            right = total - left
            if necklace_multiplicity(left, right) == 0:
                continue
            output = multiply_truncated(
                output,
                witt_factor(q, left, right, maximum_degree),
                maximum_degree,
            )
    return output


def phase_one_coefficients(polynomial: Polynomial, maximum_degree: int) -> list[str]:
    return [
        str(
            sum(
                coefficient
                for (row_degree, _), coefficient in polynomial.items()
                if row_degree == degree
            )
        )
        for degree in range(maximum_degree + 1)
    ]


def polynomial_digest(polynomial: Polynomial) -> list[list[int]]:
    return [
        [degree, phase, coefficient]
        for (degree, phase), coefficient in sorted(polynomial.items())
    ]


def control_panel(q: int) -> dict[str, object]:
    direct = direct_euler_product(q, MAX_TOTAL_DEGREE)
    witt = witt_product(q, MAX_TOTAL_DEGREE)
    if direct != witt:
        raise ArithmeticError("direct Euler product and Witt product disagree")
    return {
        "q": q,
        "maximum_total_degree": MAX_TOTAL_DEGREE,
        "nonzero_laurent_monomials": len(direct),
        "phase_one_coefficients": phase_one_coefficients(direct, MAX_TOTAL_DEGREE),
        "laurent_digest": polynomial_digest(direct),
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    necklace_rows = {
        str(total): {
            "content_multiplicities": [
                necklace_multiplicity(left, total - left) for left in range(total + 1)
            ],
            "sum": sum(
                necklace_multiplicity(left, total - left) for left in range(total + 1)
            ),
            "binary_lyndon_count": binary_lyndon_count(total),
        }
        for total in range(1, MAX_TOTAL_DEGREE + 1)
    }
    if any(row["sum"] != row["binary_lyndon_count"] for row in necklace_rows.values()):
        raise ArithmeticError("content-refined necklace counts do not sum correctly")
    return {
        "source_contract": {
            "commit": FROZEN_COMMIT,
            "git_blobs": SOURCE_BLOBS,
        },
        "theorem": {
            "orientation_euler_product": (
                "F_q(u,z)=prod_P(1-(uz)^deg(P)-(u/z)^deg(P))"
            ),
            "witt_factorization": ("F_q(u,z)=prod_(a,b)(1-q*u^(a+b)*z^(a-b))^M(a,b)"),
            "analytic_continuation": (
                "uniform for |z|=1 on every closed disk |u|<=r, 0<r<1/2"
            ),
            "coefficient_bound": (
                "sup_|z|=1 |[u^n]F_q(u,z)| <= C(q,r)*r^(-n), 0<r<1/2"
            ),
            "critical_decay": (
                "after q^(-n/2) normalization, exponential decay for every q>=5"
            ),
        },
        "necklace_ledger": necklace_rows,
        "bounded_controls": [control_panel(q) for q in CONTROL_Q],
        "proof_ledger": {
            "squarefree_divisor_orientation_identity": "PROVED EXACT",
            "content_refined_witt_identity": "PROVED EXACT",
            "polynomial_zeta_substitution": "PROVED EXACT",
            "uniform_continuation_to_radius_one_half": "PROVED",
            "critical_normalized_decay_for_q_at_least_five": "PROVED",
            "q_equals_three_critical_decay": "NOT CLAIMED",
            "sieve_or_growing_core_uniformity": "NOT INCLUDED",
            "maximal_height_wavelet": "NOT PROVED",
            "number_field_waveprimcar": "NOT PROVED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "q_controls": list(CONTROL_Q),
            "maximum_total_degree": MAX_TOTAL_DEGREE,
            "finite_field_elements": 0,
            "polynomials_enumerated": 0,
            "irreducibles_enumerated": 0,
            "curves": 0,
            "zeta_zeros": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = (
        json.dumps(
            run(check_sources=not args.no_source_check), indent=2, sort_keys=True
        )
        + "\n"
    )
    canonical = Path(__file__).with_suffix(".json")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8", newline="\n")
    elif args.check and canonical.read_text(encoding="utf-8") != rendered:
        raise SystemExit("canonical JSON fixture is stale")
    elif not args.check:
        print(rendered, end="")


if __name__ == "__main__":
    main()
