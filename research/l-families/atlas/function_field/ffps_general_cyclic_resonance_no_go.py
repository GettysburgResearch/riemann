#!/usr/bin/env python3
"""Bounded exact audit of the general cyclic hard-mask resonance.

The producer uses rational autocorrelation and exact cyclotomic-polynomial
reduction.  It audits masks in C_k only for k<=10; the accompanying note proves
the all-k statements algebraically.  No finite field, closed place, conductor,
curve, L-function, or zero is enumerated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_PATH = HERE / "ffps_general_cyclic_resonance_no_go.json"

SCHEMA = "riemann.function_field.ffps_general_cyclic_resonance_no_go.v1"
MAX_K = 10
MAX_EXACT_OPERATIONS = 2_000_000
MAX_SUBSETS = 4_096
MAX_OUTPUT_BYTES = 65_536
MAX_WALL_SECONDS = 5.0


@dataclass
class Guard:
    operations: int = 0
    subsets: int = 0

    def use(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        if self.operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.operations += amount

    def subset(self) -> None:
        if self.subsets + 1 > MAX_SUBSETS:
            raise RuntimeError("subset cap exceeded")
        self.subsets += 1


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def exact_division(dividend: list[int], divisor: list[int], guard: Guard) -> list[int]:
    dividend = trim(dividend.copy())
    divisor = trim(divisor.copy())
    if divisor[-1] != 1:
        raise ValueError("divisor must be monic")
    if len(dividend) < len(divisor):
        raise ArithmeticError("polynomial division is not exact")
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    remainder = dividend
    while len(remainder) >= len(divisor) and any(remainder):
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1]
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            remainder[index + shift] -= coefficient * value
        guard.use(len(divisor))
        trim(remainder)
    if any(remainder):
        raise ArithmeticError("cyclotomic factorization division left a remainder")
    return trim(quotient)


def polynomial_remainder(
    dividend: list[int], divisor: list[int], guard: Guard
) -> list[int]:
    dividend = trim(dividend.copy())
    divisor = trim(divisor.copy())
    if divisor[-1] != 1:
        raise ValueError("divisor must be monic")
    while len(dividend) >= len(divisor):
        shift = len(dividend) - len(divisor)
        coefficient = dividend[-1]
        for index, value in enumerate(divisor):
            dividend[index + shift] -= coefficient * value
        guard.use(len(divisor))
        trim(dividend)
    return trim(dividend)


def divisors(number: int) -> list[int]:
    return [divisor for divisor in range(1, number + 1) if number % divisor == 0]


def cyclotomic_polynomials(guard: Guard) -> dict[int, list[int]]:
    result: dict[int, list[int]] = {}
    for order in range(1, MAX_K + 1):
        polynomial = [-1] + [0] * (order - 1) + [1]
        for divisor in divisors(order):
            if divisor == order:
                continue
            polynomial = exact_division(polynomial, result[divisor], guard)
        result[order] = polynomial
    return result


def fourier_mode_is_zero(
    order: int,
    retained: frozenset[int],
    mode: int,
    cyclotomic: list[int],
    guard: Guard,
) -> bool:
    polynomial = [0] * order
    for exponent in retained:
        polynomial[(-mode * exponent) % order] += 1
        guard.use()
    remainder = polynomial_remainder(polynomial, cyclotomic, guard)
    return not any(remainder)


def selected_mode_count(
    order: int,
    retained: frozenset[int],
    cyclotomic: list[int],
    guard: Guard,
) -> int:
    return sum(
        not fourier_mode_is_zero(order, retained, mode, cyclotomic, guard)
        for mode in range(1, order)
    )


def rotate(retained: frozenset[int], shift: int, order: int) -> frozenset[int]:
    return frozenset((entry + shift) % order for entry in retained)


def intersection_count(
    retained: frozenset[int], shift: int, order: int, guard: Guard
) -> int:
    shifted = rotate(retained, shift, order)
    guard.use(len(retained))
    return len(retained & shifted)


def collision_coefficients(
    order: int, retained: frozenset[int], shift: int, guard: Guard
) -> dict[str, object]:
    size = len(retained)
    intersection = intersection_count(retained, shift, order, guard)
    hard = Fraction(order * intersection, size * size)
    selected = hard - 1
    return {
        "quotient_shift": shift % order,
        "intersection_size": intersection,
        "hard_kernel": str(hard),
        "selected_kernel": str(selected),
        "relative_kernel": str(hard - selected),
    }


def exhaustive_audit(
    cyclotomic: dict[int, list[int]], guard: Guard
) -> list[dict[str, object]]:
    summaries: list[dict[str, object]] = []
    primes = {2, 3, 5, 7}
    for order in range(2, MAX_K + 1):
        for size in range(1, order):
            counts: list[int] = []
            for entries in combinations(range(order), size):
                guard.subset()
                retained = frozenset(entries)
                modes = selected_mode_count(order, retained, cyclotomic[order], guard)
                lower_bound = math.ceil(Fraction(order, size)) - 1
                if modes < lower_bound:
                    raise ArithmeticError("finite Fourier uncertainty bound failed")
                if order in primes and modes != order - 1:
                    raise ArithmeticError("prime-order full-support theorem failed")
                rotated = rotate(retained, 1, order)
                rotated_modes = selected_mode_count(
                    order, rotated, cyclotomic[order], guard
                )
                if rotated_modes != modes:
                    raise ArithmeticError("rotation changed selected mode multiplicity")
                original_kernel = [
                    collision_coefficients(order, retained, shift, guard)
                    for shift in range(order)
                ]
                rotated_kernel = [
                    collision_coefficients(order, rotated, shift, guard)
                    for shift in range(order)
                ]
                if original_kernel != rotated_kernel:
                    raise ArithmeticError("rotation changed the correlation kernel")
                collision = original_kernel[0]
                expected = Fraction(order, size) - 1
                if Fraction(collision["selected_kernel"]) != expected:
                    raise ArithmeticError(
                        "orientation-preserving collision coefficient failed"
                    )
                if any(
                    Fraction(row["relative_kernel"]) != 1 for row in original_kernel
                ):
                    raise ArithmeticError("relative hard-minus-selected kernel failed")
                counts.append(modes)
            summaries.append(
                {
                    "order": order,
                    "retained_size": size,
                    "mask_count": len(counts),
                    "selected_mass": str(Fraction(order, size) - 1),
                    "uncertainty_lower_bound": math.ceil(Fraction(order, size)) - 1,
                    "minimum_mode_multiplicity": min(counts),
                    "maximum_mode_multiplicity": max(counts),
                }
            )
    return summaries


def subgroup_controls(
    cyclotomic: dict[int, list[int]], guard: Guard
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for order in range(2, MAX_K + 1):
        for size in divisors(order):
            if size in (order,):
                continue
            retained = frozenset(index * (order // size) for index in range(size))
            modes = selected_mode_count(order, retained, cyclotomic[order], guard)
            expected = order // size - 1
            if modes != expected:
                raise ArithmeticError(
                    "subgroup mask did not attain uncertainty equality"
                )
            rows.append(
                {
                    "order": order,
                    "retained_size": size,
                    "retained_exponents": sorted(retained),
                    "mode_multiplicity": modes,
                    "sharp_bound": expected,
                    "selected_mass": str(Fraction(order, size) - 1),
                }
            )
    return rows


def named_controls(guard: Guard) -> list[dict[str, object]]:
    masks = [
        ("ternary_two_fibre", 3, frozenset({0, 1})),
        ("quartic_adjacent_half", 4, frozenset({0, 1})),
        ("octic_sign_null", 8, frozenset({0, 1, 2, 4})),
    ]
    rows: list[dict[str, object]] = []
    for name, order, retained in masks:
        controls = [collision_coefficients(order, retained, 0, guard)]
        if order % 2 == 0:
            controls.append(collision_coefficients(order, retained, order // 2, guard))
        rows.append(
            {
                "name": name,
                "order": order,
                "retained_exponents": sorted(retained),
                "selected_mass": str(Fraction(order, len(retained)) - 1),
                "collision_components": controls,
            }
        )
    octic = next(row for row in rows if row["name"] == "octic_sign_null")
    sign_row = next(
        component
        for component in octic["collision_components"]
        if component["quotient_shift"] == 4
    )
    if sign_row["selected_kernel"] != "0":
        raise ArithmeticError("declared sign-flipped null control failed")
    return rows


def canonical_bytes(payload: dict[str, object]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def build_payload() -> dict[str, object]:
    started = time.monotonic()
    guard = Guard()
    cyclotomic = cyclotomic_polynomials(guard)
    exhaustive = exhaustive_audit(cyclotomic, guard)
    subgroup = subgroup_controls(cyclotomic, guard)
    controls = named_controls(guard)
    elapsed = time.monotonic() - started
    if elapsed > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return {
        "schema": SCHEMA,
        "scope": {
            "all_k_proof_location": "FFPS_GENERAL_CYCLIC_RESONANCE_NO_GO.md",
            "finite_audit": f"all nonempty proper subsets of C_k for 2<=k<={MAX_K}",
            "not_constructed": (
                "a common varying-conductor hard/selected derived complex or CYSEL"
            ),
            "enumeration": {
                "finite_fields": False,
                "closed_places": False,
                "conductors": False,
                "curves": False,
                "l_functions": False,
                "zeros": False,
            },
        },
        "exact_theorems": {
            "orientation_preserving_collision": (
                "selected coefficient is u=k/t-1>0 for every proper nonempty mask"
            ),
            "geometric_multiplicity": (
                "the number of nonzero selected Fourier labels; at least ceil(k/t)-1"
            ),
            "rotation_no_go": (
                "rotation preserves every |c_r|^2 and the full correlation kernel"
            ),
            "relative_projector": (
                "K_hard(g)-K_selected(g)=1 for every quotient value g"
            ),
            "wick_firewall": (
                "literal Wick subtraction removes omega_1=omega_2 only, not distinct "
                "atoms with the same oriented physical coordinates"
            ),
        },
        "exhaustive_summaries": exhaustive,
        "sharp_subgroup_controls": subgroup,
        "named_collision_controls": controls,
        "resource_ledger": {
            "exact_operations": guard.operations,
            "subsets": guard.subsets,
            "max_exact_operations": MAX_EXACT_OPERATIONS,
            "max_subsets": MAX_SUBSETS,
            "max_output_bytes": MAX_OUTPUT_BYTES,
            "max_wall_seconds": MAX_WALL_SECONDS,
        },
    }


def envelope(payload: dict[str, object]) -> dict[str, object]:
    return {
        "payload_sha256": hashlib.sha256(canonical_bytes(payload)).hexdigest(),
        "payload": payload,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    encoded = canonical_bytes(envelope(build_payload()))
    if len(encoded) > MAX_OUTPUT_BYTES:
        raise RuntimeError("output-byte cap exceeded")
    if args.check:
        if not OUTPUT_PATH.exists():
            raise SystemExit("canonical fixture is missing")
        if OUTPUT_PATH.read_bytes() != encoded:
            raise SystemExit("canonical fixture drifted")
        return
    OUTPUT_PATH.write_bytes(encoded)


if __name__ == "__main__":
    main()
