#!/usr/bin/env python3
"""Exact bounded replay for the checkerboard phase-Gram Wick spectrum."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from collections import Counter
from fractions import Fraction
from itertools import product
from math import prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_CHECKERBOARD_PHASE_WICK_SPECTRUM.md"
SOURCE_BLOBS = {
    (
        "6e4609dfe",
        "research/l-families/atlas/function_field/FFPS_CORRELATED_MASK_AMPLIFIER.md",
    ): "4569c521e99e8c591f1694126605f8abee8a75f8",
    (
        "9e116ec41",
        "research/l-families/atlas/function_field/FFPS_FINITE_ABELIAN_SUBGROUP_MASK_COMPRESSION.md",
    ): "19d0ce572fcd70e68b1618462bea29a2958b7f9e",
    (
        "e2d8ded9e",
        "research/l-families/atlas/function_field/FFPS_WICK_CENTERED_DOMINATION_BOUNDARY.md",
    ): "47ff1430d4d0a55580ade3d36489ef3cd5cee7a7",
}

PRIME_PANEL = (5, 13, 17, 29, 37, 41, 53, 61)
MAX_SUBSET_ROWS = 1_024
MAX_CHARACTER_ROWS = 256
MAX_WALL_SECONDS = 3.0


def is_prime(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def validate_panel(primes: tuple[int, ...]) -> tuple[int, ...]:
    if not primes:
        raise ValueError("prime panel must be nonempty")
    if len(set(primes)) != len(primes):
        raise ValueError("prime panel must be distinct")
    if any(not is_prime(prime) or prime % 4 != 1 for prime in primes):
        raise ValueError("every panel entry must be prime and one modulo four")
    return primes


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def subset_minimum(primes: tuple[int, ...]) -> tuple[int, tuple[int, ...], int]:
    primes = validate_panel(primes)
    local_q = tuple((prime + 1) // 2 for prime in primes)
    minimum: int | None = None
    minimizers: list[int] = []
    rows = 0
    for mask in range(1 << len(primes)):
        left = prod(
            prime if mask & (1 << index) else local_q[index]
            for index, prime in enumerate(primes)
        )
        right = prod(
            local_q[index] if mask & (1 << index) else prime
            for index, prime in enumerate(primes)
        )
        if (left + right) % 2:
            raise ArithmeticError("restricted eigenvalue is not integral")
        eigenvalue = (left + right) // 2
        if minimum is None or eigenvalue < minimum:
            minimum = eigenvalue
            minimizers = [mask]
        elif eigenvalue == minimum:
            minimizers.append(mask)
        rows += 1
        if rows > MAX_SUBSET_ROWS:
            raise RuntimeError("subset-row cap exceeded")
    if minimum is None:
        raise ArithmeticError("empty subset scan")
    return minimum, tuple(minimizers), rows


def restricted_character_spectrum(primes: tuple[int, ...]) -> tuple[Counter[int], int]:
    """Explicitly pair complete characters by the global top character."""

    primes = validate_panel(primes)
    local_sizes = tuple((prime - 1) // 2 for prime in primes)
    character_rows = prod(local_sizes)
    if character_rows > MAX_CHARACTER_ROWS:
        raise RuntimeError("character-row cap exceeded")
    local_q = tuple((prime + 1) // 2 for prime in primes)
    spectrum: Counter[int] = Counter()
    seen: set[tuple[int, ...]] = set()
    for character in product(*(range(size) for size in local_sizes)):
        if character in seen:
            continue
        toggled = tuple(
            (entry + size // 2) % size
            for entry, size in zip(character, local_sizes, strict=True)
        )
        if toggled == character:
            raise ArithmeticError("top-character translation has a fixed point")
        seen.add(character)
        seen.add(toggled)
        eigenvalue = prod(
            local_q[index] if entry == 0 else primes[index]
            for index, entry in enumerate(character)
        )
        toggled_eigenvalue = prod(
            local_q[index] if entry == 0 else primes[index]
            for index, entry in enumerate(toggled)
        )
        if (eigenvalue + toggled_eigenvalue) % 2:
            raise ArithmeticError("paired eigenvalue is not integral")
        spectrum[(eigenvalue + toggled_eigenvalue) // 2] += 1
    if 2 * sum(spectrum.values()) != character_rows:
        raise ArithmeticError("restricted character-orbit count failed")
    return spectrum, character_rows


def panel_row(primes: tuple[int, ...]) -> tuple[dict[str, object], int]:
    primes = validate_panel(primes)
    dimension = len(primes)
    native_amplitude = prod((prime - 1) // 2 for prime in primes)
    principal_eigenvalue = prod((prime + 1) // 2 for prime in primes)
    top_eigenvalue = prod(primes)
    atomic_diagonal = prod(prime - 1 for prime in primes)
    restricted_row_sum = (principal_eigenvalue + top_eigenvalue) // 2
    minimum, minimizers, subset_rows = subset_minimum(primes)
    repair = max(0, atomic_diagonal - minimum)
    full_leverage = Fraction(native_amplitude, principal_eigenvalue)
    checkerboard_leverage = Fraction(
        4 * native_amplitude, principal_eigenvalue + top_eigenvalue
    )
    leverage_ratio = checkerboard_leverage / full_leverage
    leverage_upper = 4 * Fraction(3, 5) ** dimension
    repair_lower = Fraction(1) - Fraction(dimension + 2, 2) * Fraction(3, 5) ** (
        dimension // 2
    )
    repair_fraction = Fraction(repair, atomic_diagonal)
    if leverage_ratio > leverage_upper:
        raise ArithmeticError("leverage asymptotic bound failed")
    if repair_fraction < repair_lower:
        raise ArithmeticError("repair asymptotic bound failed")
    if restricted_row_sum != (principal_eigenvalue + top_eigenvalue) // 2:
        raise ArithmeticError("restricted row-sum identity failed")
    return (
        {
            "dimension": dimension,
            "primes": list(primes),
            "native_amplitude": native_amplitude,
            "principal_eigenvalue_Q": principal_eigenvalue,
            "top_eigenvalue_P": top_eigenvalue,
            "phase_atomic_diagonal": atomic_diagonal,
            "restricted_row_sum": restricted_row_sum,
            "minimum_restricted_eigenvalue": minimum,
            "minimizing_subset_masks": list(minimizers),
            "sharp_phase_wick_repair": repair,
            "phase_wick_repair_fraction": fraction_text(repair_fraction),
            "full_leverage": fraction_text(full_leverage),
            "checkerboard_leverage": fraction_text(checkerboard_leverage),
            "leverage_ratio": fraction_text(leverage_ratio),
            "leverage_ratio_upper_bound": fraction_text(leverage_upper),
            "repair_fraction_lower_bound": fraction_text(repair_lower),
            "selected_covariance_wick_repair": 1,
        },
        subset_rows,
    )


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2.0,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"source blob mismatch: {commit}:{path}")


def build_report() -> dict[str, object]:
    started = time.monotonic()
    rows: list[dict[str, object]] = []
    subset_rows = 0
    for length in range(1, len(PRIME_PANEL) + 1):
        row, cost = panel_row(PRIME_PANEL[:length])
        rows.append(row)
        subset_rows += cost
        if subset_rows > MAX_SUBSET_ROWS:
            raise RuntimeError("aggregate subset-row cap exceeded")

    spectrum_controls: dict[str, object] = {}
    character_rows = 0
    for length in (1, 2, 3):
        primes = PRIME_PANEL[:length]
        spectrum, cost = restricted_character_spectrum(primes)
        character_rows += cost
        minimum, _, _ = subset_minimum(primes)
        if min(spectrum) != minimum:
            raise ArithmeticError("full character spectrum missed the subset minimum")
        spectrum_controls[f"d{length}"] = {
            "primes": list(primes),
            "spectrum": {
                str(eigenvalue): multiplicity
                for eigenvalue, multiplicity in sorted(spectrum.items())
            },
            "restricted_dimension": sum(spectrum.values()),
        }

    two_prime = rows[1]
    if (
        two_prime["minimum_restricted_eigenvalue"] != 37
        or two_prime["restricted_row_sum"] != 43
        or two_prime["sharp_phase_wick_repair"] != 11
        or spectrum_controls["d2"]["spectrum"] != {"37": 1, "43": 1, "52": 4}
    ):
        raise ArithmeticError("(5,13) spectral control failed")
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return {
        "schema": "riemann.function_field.ffps_checkerboard_phase_wick_spectrum.v1",
        "status": "EXACT_WICK_LEVERAGE_SEPARATION",
        "exact": {
            "restricted_spectrum": "(lambda_chi+lambda_chi_top)/2",
            "minimum": "min over complementary principal/top subsets",
            "phase_wick_repair": "max(0,D0-mu_min)",
            "repair_fraction_limit": 1,
            "selected_covariance_wick_repair": 1,
        },
        "rows": rows,
        "spectrum_controls": spectrum_controls,
        "resource_ledger": {
            "subset_rows": subset_rows,
            "max_subset_rows": MAX_SUBSET_ROWS,
            "complete_character_rows": character_rows,
            "max_character_rows_per_control": MAX_CHARACTER_ROWS,
            "conductor_families_enumerated": 0,
            "curves_enumerated": 0,
            "l_function_zeros_enumerated": 0,
        },
        "open": [
            "growing-d physical FFPS source",
            "native cancellation of the phase-Wick repair",
            "WCADD, WCKUM, CYSEL, RH, and GRH",
        ],
    }


def run_checks() -> dict[str, object]:
    check_source_blobs()
    report = build_report()
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "Wick--leverage separation theorem",
        "smallest eigenvalue of the restricted Gram",
        "selected covariance identity",
        "not claims that a growing",
        "OPEN / CENTRAL",
        "No external novelty or priority claim",
    ):
        if marker not in note:
            raise RuntimeError(f"note contract marker missing: {marker}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = run_checks() if args.check else build_report()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
