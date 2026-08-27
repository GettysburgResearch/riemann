#!/usr/bin/env python3
"""Exact replay for cyclic-phase entropy collapse in the multicolor Witt model."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FROZEN_COMMIT = "2d4e06ccc65b337f05410219f366323c40a4a8d5"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FUNCTION_FIELD_MULTICOLOR_WITT_PHASE_DIAGRAM.md"
    ): "bb4610731c91951b10c11d7664c5d193b4fa1f3c",
    (
        "research/l-families/atlas/function_field/"
        "function_field_multicolor_witt_phase_diagram.py"
    ): "cc48422f9db42a6d759251671af76bba62a70cad",
    (
        "research/l-families/atlas/function_field/"
        "function_field_multicolor_witt_phase_diagram.json"
    ): "98fcbec7c51c56ace02c0f6bdca7307f076adb45",
    "tests/test_function_field_multicolor_witt_phase_diagram.py": (
        "2e06eac5b8f3fd35fdf0a6e0adad02be50396f3d"
    ),
}
CONTROL_ROWS = ((2, 3, 7), (3, 3, 5))

SOURCE_PATH = HERE / "function_field_multicolor_witt_phase_diagram.py"
IMPORTED_SOURCE_BLOB = "cc48422f9db42a6d759251671af76bba62a70cad"


def check_imported_source_blob() -> None:
    completed = subprocess.run(
        ["git", "hash-object", str(SOURCE_PATH)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=3,
    )
    if completed.stdout.strip() != IMPORTED_SOURCE_BLOB:
        raise RuntimeError("working-tree multicolor producer differs from frozen blob")


check_imported_source_blob()
SPEC = importlib.util.spec_from_file_location("multicolor_witt_source", SOURCE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load the frozen multicolor Witt producer")
source = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(source)


def check_source_blobs() -> None:
    check_imported_source_blob()
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


def cyclic_power_sum(colors: int, exponent: int) -> int:
    source.validate_color_count(colors)
    source.validate_nonnegative_integer(exponent, "phase exponent")
    return colors if exponent % colors == 0 else 0


def cyclic_necklace_value(colors: int, total: int) -> int:
    source.validate_color_count(colors)
    if isinstance(total, bool) or not isinstance(total, int) or total < 1:
        raise ValueError("word length must be positive")
    numerator = sum(
        int(sp.mobius(divisor))
        * cyclic_power_sum(colors, divisor) ** (total // divisor)
        for divisor in sp.divisors(total)
    )
    if numerator % total:
        raise ArithmeticError("cyclic necklace value lost integrality")
    return numerator // total


def cyclotomic_remainder(colors: int, coefficients: dict[int, int]) -> tuple[int, ...]:
    source.validate_color_count(colors)
    phase = sp.Symbol("phase")
    expression = sum(
        coefficient * phase ** (exponent % colors)
        for exponent, coefficient in coefficients.items()
    )
    modulus = sp.Poly(sp.cyclotomic_poly(colors, phase), phase, domain=sp.ZZ)
    remainder = sp.rem(
        sp.Poly(expression, phase, domain=sp.ZZ),
        modulus,
    )
    return tuple(int(remainder.nth(index)) for index in range(modulus.degree()))


def collapsed_coefficients(
    colors: int,
    polynomial: source.Polynomial,
    maximum_degree: int,
) -> tuple[tuple[int, ...], ...]:
    source.validate_color_count(colors)
    source.validate_nonnegative_integer(maximum_degree, "maximum degree")
    rows: list[dict[int, int]] = [{} for _ in range(maximum_degree + 1)]
    for (degree, color_phase), coefficient in polynomial.items():
        exponent = sum(index * value for index, value in enumerate(color_phase))
        rows[degree][exponent] = rows[degree].get(exponent, 0) + coefficient
    return tuple(cyclotomic_remainder(colors, row) for row in rows)


def multiply_univariate(
    left: list[int], right: list[int], maximum_degree: int
) -> list[int]:
    source.validate_nonnegative_integer(maximum_degree, "maximum degree")
    output = [0] * (maximum_degree + 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            degree = left_degree + right_degree
            if degree <= maximum_degree:
                output[degree] += left_coefficient * right_coefficient
    return output


def cyclic_direct_coefficients(
    colors: int, q: int, maximum_degree: int
) -> tuple[int, ...]:
    source.validate_color_count(colors)
    source.validate_nonnegative_integer(maximum_degree, "maximum degree")
    source.irreducible_count(q, 1)
    answer = [1] + [0] * maximum_degree
    for prime_degree in range(colors, maximum_degree + 1, colors):
        count = source.irreducible_count(q, prime_degree)
        factor = [0] * (maximum_degree + 1)
        for selected in range(min(count, maximum_degree // prime_degree) + 1):
            factor[selected * prime_degree] = (
                sp.binomial(count, selected) * (-colors) ** selected
            )
        answer = multiply_univariate(
            answer, [int(value) for value in factor], maximum_degree
        )
    return tuple(answer)


def control_panel(colors: int, q: int, maximum_degree: int) -> dict[str, object]:
    direct = source.direct_product(colors, q, maximum_degree)
    witt = source.witt_product(colors, q, maximum_degree)
    collapsed_direct = collapsed_coefficients(colors, direct, maximum_degree)
    collapsed_witt = collapsed_coefficients(colors, witt, maximum_degree)
    expected = cyclic_direct_coefficients(colors, q, maximum_degree)
    constant_rows = tuple(
        (value,) + (0,) * (sp.totient(colors) - 1) for value in expected
    )
    if collapsed_direct != constant_rows or collapsed_witt != constant_rows:
        raise ArithmeticError("cyclic phase collapse disagrees with its Euler adapter")
    necklace_rows = {
        str(total): cyclic_necklace_value(colors, total)
        for total in range(1, maximum_degree + 1)
    }
    return {
        "colors": colors,
        "q": q,
        "maximum_degree": maximum_degree,
        "critical_decay_exact_test": f"{q}^{colors}>{colors}^2",
        "critical_decay_regime": q**colors > colors**2,
        "cyclic_coefficients": list(expected),
        "cyclic_necklace_values": necklace_rows,
        "exact_direct_and_witt_collapse": True,
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
                "formal replay for integer q>=2; geometric theorem for prime-power q"
            ),
            "cyclic_phase_adapter": (
                "sum_(j=0)^(c-1) omega^(j*d)=c if c|d and 0 otherwise"
            ),
            "grouped_witt_radius": (
                "guaranteed open disk |u|<c^(-1/c) at the complete cyclic phase"
            ),
            "critical_decay_threshold": ("q>c^(2/c), equivalently q^c>c^2"),
            "uniform_multicolor_comparison": (
                "cyclic coherence improves the guaranteed disk from 1/c"
            ),
        },
        "controls": [
            control_panel(colors, q, maximum_degree)
            for colors, q, maximum_degree in CONTROL_ROWS
        ],
        "boundary_control": {
            "colors": 3,
            "q": 2,
            "q_power_colors": 8,
            "color_square": 9,
            "critical_decay_regime": False,
        },
        "proof_ledger": {
            "root_of_unity_local_adapter": "PROVED EXACT",
            "cyclic_necklace_specialization": "PROVED EXACT",
            "grouped_normal_convergence_to_c_inverse_c": "PROVED",
            "critical_decay_for_q_power_c_greater_than_c_square": "PROVED",
            "optimality_or_natural_boundary": "NOT CLAIMED",
            "native_cyclic_mask_or_sheaf_realization": "NOT INCLUDED",
            "number_field_transfer": "NOT INFERRED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "control_rows": [list(row) for row in CONTROL_ROWS],
            "largest_color_count_producer": 3,
            "largest_color_count_including_tests": 6,
            "largest_single_content_row_in_tests": 84,
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
