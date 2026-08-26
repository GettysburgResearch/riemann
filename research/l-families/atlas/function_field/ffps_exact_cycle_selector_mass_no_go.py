#!/usr/bin/env python3
"""Bounded exact replay for the forced mass of an exact S_d cycle selector."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
MAX_CYCLE_DEGREE = 10
MAX_HOOK_DEGREE = 12
SOURCE_COMMIT = "2423b93de9d7822ddc92841549d5a7d904e571ca"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_RELATIVE_BOUNDARY_TRACE_TOWER_GATE.md": (
        "628854ef5be277572390bf298a070a9281af319b"
    ),
    "research/l-families/atlas/function_field/ffps_relative_boundary_trace_tower_gate.py": (
        "de8ff576b30014b7e554ddc25aee049b694f2667"
    ),
    "research/l-families/atlas/function_field/ffps_relative_boundary_trace_tower_gate.json": (
        "7d519a8f6c24b70a08c9e183e18d299b57348f5f"
    ),
    "tests/test_ffps_relative_boundary_trace_tower_gate.py": (
        "8631fc89be8dcd2bc1b3d21714cfef1c0271ee4c"
    ),
}


def validate_degree(degree: int) -> None:
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 1:
        raise ValueError("degree must be a positive integer")


def git_blob(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def check_source_blobs() -> None:
    for path, expected_blob in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "show", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            stdout=subprocess.PIPE,
        )
        if git_blob(completed.stdout) != expected_blob:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def partitions(total: int, largest: int | None = None) -> list[tuple[int, ...]]:
    """Integer partitions in decreasing order."""
    validate_degree(total)
    upper = total if largest is None else min(total, largest)
    rows: list[tuple[int, ...]] = []
    for first in range(upper, 0, -1):
        if first == total:
            rows.append((first,))
        else:
            for tail in partitions(total - first, first):
                rows.append((first, *tail))
    return rows


def multiply(left: list[int], right: list[int]) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] += a * b
    return product


def alternating_standard_exterior_trace(cycle_type: tuple[int, ...]) -> int:
    """Compute det(1-g | Std_d) from the cycle lengths of g."""
    if not cycle_type:
        raise ValueError("cycle type must be nonempty")
    for cycle_length in cycle_type:
        validate_degree(cycle_length)
    polynomial = [1]
    for cycle_length in cycle_type:
        polynomial = multiply(polynomial, [1, *([0] * (cycle_length - 1)), -1])
    quotient: list[int] = []
    previous = 0
    for coefficient in polynomial[:-1]:
        current = coefficient + previous
        quotient.append(current)
        previous = current
    if polynomial[-1] != -quotient[-1]:
        raise AssertionError("division by the invariant factor 1-t failed")
    return sum(quotient)


def cycle_selector_trace(cycle_type: tuple[int, ...]) -> Fraction:
    degree = sum(cycle_type)
    validate_degree(degree)
    return Fraction(alternating_standard_exterior_trace(cycle_type), degree)


def hook_rows(degree: int) -> list[dict[str, object]]:
    validate_degree(degree)
    return [
        {
            "k": k,
            "partition": [degree - k, *([1] * k)],
            "cycle_character": (-1) ** k,
            "selector_coefficient": str(Fraction((-1) ** k, degree)),
            "dimension": math.comb(degree - 1, k),
        }
        for k in range(degree)
    ]


def selector_rank_masses(degree: int) -> dict[str, Fraction]:
    validate_degree(degree)
    dimensions = [math.comb(degree - 1, k) for k in range(degree)]
    positive = sum(dimensions[::2], start=0)
    negative = sum(dimensions[1::2], start=0)
    return {
        "absolute": Fraction(positive + negative, degree),
        "positive": Fraction(positive, degree),
        "negative": Fraction(negative, degree),
        "integral_numerator_total": Fraction(positive + negative),
        "integral_numerator_even": Fraction(positive),
        "integral_numerator_odd": Fraction(negative),
    }


def product_selector_mass(degrees: tuple[int, ...]) -> Fraction:
    if not degrees:
        raise ValueError("degree tuple must be nonempty")
    mass = Fraction(1)
    for degree in degrees:
        mass *= selector_rank_masses(degree)["absolute"]
    return mass


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    cycle_panels: list[dict[str, object]] = []
    cycle_types_checked = 0
    for degree in range(1, MAX_CYCLE_DEGREE + 1):
        types = partitions(degree)
        cycle_types_checked += len(types)
        failures = [
            cycle_type
            for cycle_type in types
            if cycle_selector_trace(cycle_type)
            != Fraction(int(cycle_type == (degree,)))
        ]
        if failures:
            raise AssertionError(f"cycle-selector failure in degree {degree}")
        cycle_panels.append(
            {
                "degree": degree,
                "cycle_types_checked": len(types),
                "all_exact": True,
            }
        )

    hook_panels: list[dict[str, object]] = []
    for degree in range(1, MAX_HOOK_DEGREE + 1):
        masses = selector_rank_masses(degree)
        expected_absolute = Fraction(2 ** (degree - 1), degree)
        if masses["absolute"] != expected_absolute:
            raise AssertionError("absolute hook mass formula failed")
        if degree > 1:
            expected_side = Fraction(2 ** (degree - 2), degree)
            if (
                masses["positive"] != expected_side
                or masses["negative"] != expected_side
            ):
                raise AssertionError("positive/negative hook mass formula failed")
        hook_panels.append(
            {
                "degree": degree,
                "hooks": hook_rows(degree),
                "masses": {key: str(value) for key, value in masses.items()},
            }
        )

    product_degrees = ((2, 3), (3, 4), (2, 3, 5))
    products = [
        {
            "degrees": list(degrees),
            "forced_absolute_rank_mass": str(product_selector_mass(degrees)),
        }
        for degrees in product_degrees
    ]
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "role": "universal cycle selector and root-incidence cancellation",
        },
        "theorem": {
            "unique_expansion": (
                "1_(d-cycle)=d^-1*sum_(k=0)^(d-1) (-1)^k*chi_(d-k,1^k)"
            ),
            "coefficient_reason": (
                "orthogonality gives chi_lambda((d))/d; "
                "Murnaghan-Nakayama leaves only hooks"
            ),
            "forced_absolute_rank_mass": "2^(d-1)/d",
            "forced_positive_and_negative_mass_for_d_gt_1": "2^(d-2)/d each",
            "integral_numerator_complex_lower_bound": (
                "even rank >=2^(d-2), odd rank >=2^(d-2), total >=2^(d-1)"
            ),
            "product_rule": "multiply 2^(d_i-1)/d_i over independent factors",
            "scope": (
                "exact full-S_d characteristic-zero semisimple character category"
            ),
        },
        "cycle_panels": cycle_panels,
        "hook_panels": hook_panels,
        "product_panels": products,
        "ffps_consequence": {
            "closed_loophole": (
                "no cheaper exact d-cycle selector exists by changing the "
                "semisimple S_d character presentation"
            ),
            "remaining_escape": (
                "joint K_0 cancellation before termwise cost, a weaker or "
                "source-specific selector, or different geometry"
            ),
            "rh_proved": False,
        },
        "resource_caps": {
            "maximum_cycle_degree": MAX_CYCLE_DEGREE,
            "maximum_hook_degree": MAX_HOOK_DEGREE,
            "cycle_types_checked": cycle_types_checked,
            "product_panels": len(products),
            "finite_field_points": 0,
            "closed_places": 0,
            "curves_or_sheaves": 0,
            "l_functions_or_zeros": 0,
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
    print(rendered, end="")


if __name__ == "__main__":
    main()
