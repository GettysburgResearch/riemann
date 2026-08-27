#!/usr/bin/env python3
"""Exact bounded replay for the multicolor function-field Witt phase diagram."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from itertools import product
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FROZEN_COMMIT = "02555b216077a3cd3a1309eb530cd29b26c7f6a3"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FUNCTION_FIELD_DIVISOR_WAVELET_WITT_FACTORIZATION.md"
    ): "ad1ec29ec5678c4dfe356c29f1077de8e2dc868e",
    (
        "research/l-families/atlas/function_field/"
        "function_field_divisor_wavelet_witt_factorization.py"
    ): "af697bda209ef4e0f614a672d931e76bba94a83c",
    (
        "research/l-families/atlas/function_field/"
        "function_field_divisor_wavelet_witt_factorization.json"
    ): "41c8ae54f6edd556055fcadee8b6ca72581cbed8",
}
CONTROL_ROWS = ((2, 5, 7), (3, 11, 5))

Monomial = tuple[int, tuple[int, ...]]
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


def validate_color_count(colors: int) -> None:
    if isinstance(colors, bool) or not isinstance(colors, int) or colors < 2:
        raise ValueError("the multicolor replay needs at least two colors")


def validate_nonnegative_integer(value: int, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{label} must be a nonnegative integer")


def compositions(total: int, colors: int) -> tuple[tuple[int, ...], ...]:
    validate_color_count(colors)
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError("composition total must be a nonnegative integer")
    return tuple(
        row for row in product(range(total + 1), repeat=colors) if sum(row) == total
    )


def content_necklace_multiplicity(content: tuple[int, ...]) -> int:
    if (
        len(content) < 2
        or any(
            isinstance(value, bool) or not isinstance(value, int) or value < 0
            for value in content
        )
        or sum(content) == 0
    ):
        raise ValueError("content must be a nonzero tuple of nonnegative integers")
    total = sum(content)
    common = math.gcd(*content)
    numerator = 0
    for divisor in sp.divisors(common):
        reduced = tuple(value // divisor for value in content)
        multinomial = math.factorial(total // divisor)
        for value in reduced:
            multinomial //= math.factorial(value)
        numerator += int(sp.mobius(divisor)) * multinomial
    if numerator % total:
        raise ArithmeticError("content necklace multiplicity lost integrality")
    answer = numerator // total
    if answer < 0:
        raise ArithmeticError("content necklace multiplicity became negative")
    return answer


def lyndon_count(colors: int, total: int) -> int:
    validate_color_count(colors)
    if isinstance(total, bool) or not isinstance(total, int) or total < 1:
        raise ValueError("word length must be positive")
    numerator = sum(
        int(sp.mobius(divisor)) * colors ** (total // divisor)
        for divisor in sp.divisors(total)
    )
    if numerator % total:
        raise ArithmeticError("Lyndon count lost integrality")
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
            phase = tuple(
                left_value + right_value
                for left_value, right_value in zip(left_phase, right_phase, strict=True)
            )
            key = degree, phase
            output[key] = output.get(key, 0) + left_coefficient * right_coefficient
            if output[key] == 0:
                del output[key]
    return output


def multinomial_choice(population: int, counts: tuple[int, ...]) -> int:
    selected = sum(counts)
    if selected > population:
        return 0
    answer = math.factorial(population) // math.factorial(population - selected)
    for count in counts:
        answer //= math.factorial(count)
    return answer


def direct_prime_degree_factor(
    colors: int, q: int, prime_degree: int, maximum_degree: int
) -> Polynomial:
    validate_color_count(colors)
    validate_nonnegative_integer(maximum_degree, "maximum degree")
    count = irreducible_count(q, prime_degree)
    zero_phase = (0,) * colors
    factor: Polynomial = {(0, zero_phase): 1}
    maximum_selected = min(count, maximum_degree // prime_degree)
    for selected in range(1, maximum_selected + 1):
        for counts in compositions(selected, colors):
            phase = tuple(prime_degree * count_value for count_value in counts)
            key = prime_degree * selected, phase
            factor[key] = factor.get(key, 0) + (-1) ** selected * multinomial_choice(
                count, counts
            )
    return {key: value for key, value in factor.items() if value}


def direct_product(colors: int, q: int, maximum_degree: int) -> Polynomial:
    validate_color_count(colors)
    validate_nonnegative_integer(maximum_degree, "maximum degree")
    irreducible_count(q, 1)
    output: Polynomial = {(0, (0,) * colors): 1}
    for prime_degree in range(1, maximum_degree + 1):
        output = multiply_truncated(
            output,
            direct_prime_degree_factor(colors, q, prime_degree, maximum_degree),
            maximum_degree,
        )
    return output


def witt_content_factor(
    q: int, content: tuple[int, ...], maximum_degree: int
) -> Polynomial:
    validate_nonnegative_integer(maximum_degree, "maximum degree")
    irreducible_count(q, 1)
    total = sum(content)
    multiplicity = content_necklace_multiplicity(content)
    factor: Polynomial = {}
    for selected in range(min(multiplicity, maximum_degree // total) + 1):
        phase = tuple(selected * value for value in content)
        factor[(selected * total, phase)] = (
            math.comb(multiplicity, selected) * (-q) ** selected
        )
    return factor


def witt_product(colors: int, q: int, maximum_degree: int) -> Polynomial:
    validate_color_count(colors)
    validate_nonnegative_integer(maximum_degree, "maximum degree")
    irreducible_count(q, 1)
    output: Polynomial = {(0, (0,) * colors): 1}
    for total in range(1, maximum_degree + 1):
        for content in compositions(total, colors):
            if content_necklace_multiplicity(content) == 0:
                continue
            output = multiply_truncated(
                output,
                witt_content_factor(q, content, maximum_degree),
                maximum_degree,
            )
    return output


def digest(polynomial: Polynomial) -> list[list[object]]:
    return [
        [degree, list(phase), coefficient]
        for (degree, phase), coefficient in sorted(polynomial.items())
    ]


def control_panel(colors: int, q: int, maximum_degree: int) -> dict[str, object]:
    direct = direct_product(colors, q, maximum_degree)
    witt = witt_product(colors, q, maximum_degree)
    if direct != witt:
        raise ArithmeticError(
            "direct multicolor Euler product disagrees with Witt product"
        )
    necklace_rows = {
        str(total): {
            "content_sum": sum(
                content_necklace_multiplicity(content)
                for content in compositions(total, colors)
            ),
            "lyndon_count": lyndon_count(colors, total),
        }
        for total in range(1, maximum_degree + 1)
    }
    if any(row["content_sum"] != row["lyndon_count"] for row in necklace_rows.values()):
        raise ArithmeticError("content counts do not sum to the color Lyndon count")
    return {
        "colors": colors,
        "q": q,
        "maximum_degree": maximum_degree,
        "q_minus_color_square": q - colors**2,
        "critical_decay_regime": q > colors**2,
        "necklace_rows": necklace_rows,
        "nonzero_monomials": len(direct),
        "digest": digest(direct),
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    return {
        "source_contract": {
            "commit": FROZEN_COMMIT,
            "git_blobs": SOURCE_BLOBS,
        },
        "theorem": {
            "domain": (
                "formal replay for integer q>=2; geometric interpretation "
                "requires q to be a prime power"
            ),
            "multicolor_euler_product": ("F_(q,c)(u,z)=prod_P(1-sum_i (u*z_i)^degP)"),
            "multicolor_witt_product": (
                "F_(q,c)=prod_(content a!=0)(1-q*u^|a|*z^a)^M(a)"
            ),
            "uniform_continuation_radius": (
                "guaranteed open disk |u|<1/c for c colors"
            ),
            "critical_phase_transition": (
                "q>c^2 gives exponential q^(-n/2)-normalized decay"
            ),
        },
        "controls": [
            control_panel(colors, q, maximum_degree)
            for colors, q, maximum_degree in CONTROL_ROWS
        ],
        "proof_ledger": {
            "multicolor_local_adapter": "PROVED EXACT",
            "content_refined_witt_factorization": "PROVED EXACT",
            "uniform_radius_one_over_colors": "PROVED",
            "optimality_or_natural_boundary_at_one_over_colors": "NOT CLAIMED",
            "critical_decay_for_q_greater_than_color_square": "PROVED",
            "critical_decay_at_or_below_color_square": "NOT CLAIMED",
            "arithmetic_family_or_sheaf_realization": "NOT INCLUDED",
            "number_field_transfer": "NOT INFERRED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "control_rows": [list(row) for row in CONTROL_ROWS],
            "largest_control_color_count": 3,
            "largest_test_color_count": 4,
            "largest_total_degree": 7,
            "finite_field_elements": 0,
            "finite_field_polynomials_enumerated": 0,
            "irreducibles_enumerated": 0,
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
