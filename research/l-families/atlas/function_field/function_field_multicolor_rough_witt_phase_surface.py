#!/usr/bin/env python3
"""Exact replay for the multicolor rough-Witt phase surface."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MULTICOLOR_COMMIT = "2d4e06ccc65b337f05410219f366323c40a4a8d5"
ROUGH_COMMIT = "11552aea89380809f45ff002eb0c6927c70ab1f2"
FROZEN_SOURCES = (
    (
        MULTICOLOR_COMMIT,
        (
            "research/l-families/atlas/function_field/"
            "FUNCTION_FIELD_MULTICOLOR_WITT_PHASE_DIAGRAM.md"
        ),
        "bb4610731c91951b10c11d7664c5d193b4fa1f3c",
    ),
    (
        MULTICOLOR_COMMIT,
        (
            "research/l-families/atlas/function_field/"
            "function_field_multicolor_witt_phase_diagram.py"
        ),
        "cc48422f9db42a6d759251671af76bba62a70cad",
    ),
    (
        MULTICOLOR_COMMIT,
        (
            "research/l-families/atlas/function_field/"
            "function_field_multicolor_witt_phase_diagram.json"
        ),
        "98fcbec7c51c56ace02c0f6bdca7307f076adb45",
    ),
    (
        MULTICOLOR_COMMIT,
        "tests/test_function_field_multicolor_witt_phase_diagram.py",
        "2e06eac5b8f3fd35fdf0a6e0adad02be50396f3d",
    ),
    (
        ROUGH_COMMIT,
        (
            "research/l-families/atlas/function_field/"
            "FUNCTION_FIELD_WITT_ROUGH_SIEVE_FRONTIER.md"
        ),
        "bd1dd0fb7b2400114ed78dddd5e36fa5d2984578",
    ),
    (
        ROUGH_COMMIT,
        (
            "research/l-families/atlas/function_field/"
            "function_field_witt_rough_sieve_frontier.py"
        ),
        "81eff0c25123e93baaec7c72daeda740ec7b4ff6",
    ),
    (
        ROUGH_COMMIT,
        (
            "research/l-families/atlas/function_field/"
            "function_field_witt_rough_sieve_frontier.json"
        ),
        "0bb8ff9b57ffd1844b8cd1708b2d809ffd81ae8c",
    ),
    (
        ROUGH_COMMIT,
        "tests/test_function_field_witt_rough_sieve_frontier.py",
        "7aca10c1a9e8d3079d0b915e92a644b7cad1a391",
    ),
)

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

CONTROL_COLORS = 3
CONTROL_Q = 11
CONTROL_CUTOFF = 2
CONTROL_MAXIMUM_DEGREE = 5
CONTROL_RADIUS = Fraction(8, 25)
LARGEST_TEST_CUTOFF = 3


def check_source_blobs() -> None:
    check_imported_source_blob()
    for commit, path, expected in FROZEN_SOURCES:
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def validate_cutoff(maximum_degree: int, cutoff: int) -> None:
    source.validate_nonnegative_integer(maximum_degree, "maximum degree")
    source.validate_nonnegative_integer(cutoff, "rough cutoff")
    if cutoff > maximum_degree:
        raise ValueError("rough cutoff cannot exceed the replay degree")


def degree_range_product(
    colors: int,
    q: int,
    minimum_prime_degree: int,
    maximum_prime_degree: int,
    truncation: int,
) -> source.Polynomial:
    source.validate_color_count(colors)
    if (
        isinstance(minimum_prime_degree, bool)
        or not isinstance(minimum_prime_degree, int)
        or minimum_prime_degree < 1
    ):
        raise ValueError("minimum prime degree must be a positive integer")
    source.validate_nonnegative_integer(maximum_prime_degree, "maximum prime degree")
    if minimum_prime_degree > maximum_prime_degree + 1:
        raise ValueError("prime-degree range may be empty only at adjacent endpoints")
    source.validate_nonnegative_integer(truncation, "maximum degree")
    source.irreducible_count(q, 1)
    output: source.Polynomial = {(0, (0,) * colors): 1}
    for prime_degree in range(minimum_prime_degree, maximum_prime_degree + 1):
        output = source.multiply_truncated(
            output,
            source.direct_prime_degree_factor(colors, q, prime_degree, truncation),
            truncation,
        )
    return output


def removed_product(
    colors: int, q: int, cutoff: int, maximum_degree: int
) -> source.Polynomial:
    validate_cutoff(maximum_degree, cutoff)
    return degree_range_product(colors, q, 1, cutoff, maximum_degree)


def rough_product(
    colors: int, q: int, cutoff: int, maximum_degree: int
) -> source.Polynomial:
    validate_cutoff(maximum_degree, cutoff)
    return degree_range_product(colors, q, cutoff + 1, maximum_degree, maximum_degree)


def conditioning_inverse(
    colors: int, q: int, cutoff: int, radius: Fraction
) -> Fraction:
    source.validate_color_count(colors)
    source.validate_nonnegative_integer(cutoff, "rough cutoff")
    source.irreducible_count(q, 1)
    if not isinstance(radius, Fraction) or radius <= 0 or colors * radius >= 1:
        raise ValueError("radius must be a Fraction strictly between 0 and 1/c")
    answer = Fraction(1)
    for degree in range(1, cutoff + 1):
        local = 1 - colors * radius**degree
        if local <= 0:
            raise ArithmeticError("deleted local factor ceased to be positive")
        answer *= local ** (-source.irreducible_count(q, degree))
    return answer


def phase_one_coefficients(
    polynomial: source.Polynomial, maximum_degree: int
) -> list[int]:
    source.validate_nonnegative_integer(maximum_degree, "maximum degree")
    answer = [0] * (maximum_degree + 1)
    for (degree, _phase), coefficient in polynomial.items():
        answer[degree] += coefficient
    return answer


def control_panel() -> dict[str, object]:
    complete = source.direct_product(CONTROL_COLORS, CONTROL_Q, CONTROL_MAXIMUM_DEGREE)
    removed = removed_product(
        CONTROL_COLORS,
        CONTROL_Q,
        CONTROL_CUTOFF,
        CONTROL_MAXIMUM_DEGREE,
    )
    rough = rough_product(
        CONTROL_COLORS,
        CONTROL_Q,
        CONTROL_CUTOFF,
        CONTROL_MAXIMUM_DEGREE,
    )
    reassembled = source.multiply_truncated(removed, rough, CONTROL_MAXIMUM_DEGREE)
    if reassembled != complete:
        raise ArithmeticError("removed and rough color factors did not reassemble")
    condition = conditioning_inverse(
        CONTROL_COLORS, CONTROL_Q, CONTROL_CUTOFF, CONTROL_RADIUS
    )
    if CONTROL_Q * CONTROL_RADIUS**2 <= 1:
        raise ArithmeticError("control radius is not above the critical radius")
    if CONTROL_COLORS * CONTROL_RADIUS >= 1:
        raise ArithmeticError("control radius is outside the color disk")
    return {
        "colors": CONTROL_COLORS,
        "q": CONTROL_Q,
        "rough_cutoff_degree": CONTROL_CUTOFF,
        "maximum_total_degree": CONTROL_MAXIMUM_DEGREE,
        "critical_radius_control": str(CONTROL_RADIUS),
        "q_times_radius_squared": str(CONTROL_Q * CONTROL_RADIUS**2),
        "color_times_radius": str(CONTROL_COLORS * CONTROL_RADIUS),
        "condition_inverse": str(condition),
        "condition_numerator_digits": len(str(condition.numerator)),
        "rough_nonzero_monomials": len(rough),
        "rough_phase_one_coefficients": phase_one_coefficients(
            rough, CONTROL_MAXIMUM_DEGREE
        ),
        "exact_reassembly": True,
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    largest_test_condition = conditioning_inverse(
        CONTROL_COLORS,
        CONTROL_Q,
        LARGEST_TEST_CUTOFF,
        CONTROL_RADIUS,
    )
    return {
        "source_contract": {
            "frozen_sources": [
                {"commit": commit, "path": path, "blob": blob}
                for commit, path, blob in FROZEN_SOURCES
            ]
        },
        "theorem": {
            "domain": (
                "formal replay for integer q>=2; geometric theorem for prime-power q"
            ),
            "rough_quotient": (
                "F_(q,c,>y)=F_(q,c)/prod_(deg P<=y)(1-sum_i (u*z_i)^degP)"
            ),
            "conditioning_cost": (
                "for y>=1, log K_(q,c,y)(r)=O_(q,c,r)((q*r)^y/y), 0<r<1/c; K_(q,c,0)=1"
            ),
            "two_axis_subfrontier": (
                "for fixed 0<eta<2, q>c^2 and "
                "y_n<=(2-eta)log_q(n) imply exponential "
                "critical-normalized complete-shell decay"
            ),
            "absolute_method_barrier": (
                "y_n>=(2+eta)log_q(n) makes every fixed critical-radius "
                "finite-deletion condition number superexponential"
            ),
            "fixed_colored_core": (
                "a fixed core divides by the union of low-degree and "
                "core-prime local factors and preserves |u|<1/c"
            ),
        },
        "control": control_panel(),
        "proof_ledger": {
            "multicolor_rough_quotient": "PROVED EXACT",
            "uniform_condition_number": "PROVED",
            "color_square_and_depth_two_subfrontier": "PROVED",
            "depth_two_absolute_conditioning_barrier": "PROVED",
            "fixed_colored_core_stability": "PROVED",
            "actual_sharp_rough_coefficient_frontier": "NOT CLAIMED",
            "behavior_for_q_at_or_below_color_square": "NOT CLAIMED",
            "native_ffps_or_sheaf_realization": "NOT INCLUDED",
            "number_field_transfer": "NOT INFERRED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "colors": CONTROL_COLORS,
            "q": CONTROL_Q,
            "rough_cutoff_degree": CONTROL_CUTOFF,
            "largest_test_rough_cutoff_degree": LARGEST_TEST_CUTOFF,
            "largest_test_condition_numerator_digits": len(
                str(largest_test_condition.numerator)
            ),
            "maximum_total_degree": CONTROL_MAXIMUM_DEGREE,
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
