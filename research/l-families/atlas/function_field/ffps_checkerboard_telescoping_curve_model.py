#!/usr/bin/env python3
"""Exact bounded replay for the telescoping checkerboard curve model."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_CHECKERBOARD_TELESCOPING_CURVE_MODEL.md"
SOURCE_BLOBS = {
    (
        "a33cf6e6d",
        "research/l-families/atlas/function_field/FFPS_FINITE_ABELIAN_SUBGROUP_MASK_COMPRESSION.md",
    ): "8fb67e8445a40b836703e92cdacc55e680dac500",
    (
        "464c3705f",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md",
    ): "ab16e6c0894e51303119692e67b2f2bf59ba73e4",
}

Q_FIXTURES = (3, 5, 7, 9)
MAX_D = 128
MAX_E = 64
MAX_ROWS = 512
MAX_BIT_OPERATIONS = 100_000
MAX_BOUNDARY_ROWS = 2_048
MAX_WALL_SECONDS = 3.0


def divisors(value: int) -> tuple[int, ...]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    return tuple(divisor for divisor in range(1, value + 1) if value % divisor == 0)


def mobius(value: int) -> int:
    value = int(value)
    if value < 1:
        raise ValueError("value must be positive")
    remaining = value
    prime_count = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            prime_count += 1
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def irreducible_count(field_size: int, degree: int) -> int:
    if (
        isinstance(field_size, bool)
        or not isinstance(field_size, int)
        or field_size < 2
    ):
        raise ValueError("field_size must be an integer at least two")
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 1:
        raise ValueError("degree must be positive")
    numerator = sum(
        mobius(divisor) * field_size ** (degree // divisor)
        for divisor in divisors(degree)
    )
    if numerator % degree:
        raise ArithmeticError("irreducible count is not integral")
    return numerator // degree


def minimal_closed_place_degree(field_size: int, path_length: int) -> int:
    if (
        isinstance(path_length, bool)
        or not isinstance(path_length, int)
        or path_length < 1
    ):
        raise ValueError("path_length must be positive")
    for degree in range(1, MAX_E + 1):
        if irreducible_count(field_size, degree) >= path_length + 1:
            return degree
    raise RuntimeError("closed-place degree cap exceeded")


def gf2_rank(vectors: tuple[int, ...]) -> tuple[int, int]:
    basis: dict[int, int] = {}
    bit_operations = 0
    for original in vectors:
        value = original
        while value:
            pivot = value.bit_length() - 1
            bit_operations += 1
            if pivot not in basis:
                basis[pivot] = value
                break
            value ^= basis[pivot]
    return len(basis), bit_operations


def path_model(field_size: int, path_length: int) -> tuple[dict[str, object], int]:
    degree = minimal_closed_place_degree(field_size, path_length)
    edges = tuple((1 << vertex) | (1 << (vertex + 1)) for vertex in range(path_length))
    rank, bit_operations = gf2_rank(edges)
    if rank != path_length:
        raise ArithmeticError("path squareclasses are not independent")
    top_divisor = 0
    for edge in edges:
        top_divisor ^= edge
        bit_operations += 1
    expected_top = 1 | (1 << path_length)
    if top_divisor != expected_top:
        raise ArithmeticError("top character did not telescope to endpoints")

    available_primes = irreducible_count(field_size, degree)
    common_punctures = (path_length + 1) * degree
    minimal_punctures = 2 * degree
    common_h1 = common_punctures - 2
    minimal_h1 = minimal_punctures - 2
    puncture_tax = (path_length - 1) * degree
    if common_h1 - minimal_h1 != puncture_tax:
        raise ArithmeticError("removable-puncture tax failed")
    return (
        {
            "q": field_size,
            "d": path_length,
            "e_q_d": degree,
            "available_degree_e_primes": available_primes,
            "geometric_torsor_rank": path_length,
            "geometric_torsor_degree": 1 << path_length,
            "top_character_rank": 1,
            "top_branch_points": minimal_punctures,
            "minimal_open_h1": minimal_h1,
            "common_open_punctures": common_punctures,
            "common_open_h1": common_h1,
            "removable_puncture_tax": puncture_tax,
            "top_invariants": 0,
            "deligne_constant_after_extension": minimal_h1,
        },
        bit_operations,
    )


def boundary_trace_difference(
    closed_place_degree: int, extension_degree: int, signs: tuple[int, ...]
) -> int:
    """Return the exact trace added by filling equal-degree middle places."""

    if (
        isinstance(closed_place_degree, bool)
        or not isinstance(closed_place_degree, int)
        or closed_place_degree < 1
    ):
        raise ValueError("closed_place_degree must be positive")
    if (
        isinstance(extension_degree, bool)
        or not isinstance(extension_degree, int)
        or extension_degree < 1
    ):
        raise ValueError("extension_degree must be positive")
    if any(sign not in (-1, 1) for sign in signs):
        raise ValueError("boundary signs must be plus or minus one")
    if extension_degree % closed_place_degree:
        return 0
    relative_degree = extension_degree // closed_place_degree
    return closed_place_degree * sum(sign**relative_degree for sign in signs)


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
    bit_operations = 0
    for field_size in Q_FIXTURES:
        for path_length in range(1, MAX_D + 1):
            row, cost = path_model(field_size, path_length)
            rows.append(row)
            bit_operations += cost
            if len(rows) > MAX_ROWS:
                raise RuntimeError("row cap exceeded")
            if bit_operations > MAX_BIT_OPERATIONS:
                raise RuntimeError("bit-operation cap exceeded")

    boundary_rows = 0
    for sign_count in range(7):
        for bit_mask in range(1 << sign_count):
            signs = tuple(
                -1 if bit_mask & (1 << index) else 1 for index in range(sign_count)
            )
            for degree in range(1, 5):
                for relative_degree in range(1, 5):
                    value = boundary_trace_difference(
                        degree, degree * relative_degree, signs
                    )
                    expected = degree * (
                        sum(signs) if relative_degree % 2 else sign_count
                    )
                    if value != expected:
                        raise ArithmeticError("boundary tower law failed")
                    boundary_rows += 1
                    if boundary_rows > MAX_BOUNDARY_ROWS:
                        raise RuntimeError("boundary row cap exceeded")

    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return {
        "schema": "riemann.function_field.ffps_checkerboard_telescoping_curve.v1",
        "status": "EXACT_TELESCOPING_TOP_CHARACTER_MODEL",
        "exact": {
            "squareclass_rank": "d",
            "top_character": "P_0/P_d",
            "minimal_h1": "2*e-2",
            "common_h1": "(d+1)*e-2",
            "puncture_tax": "(d-1)*e",
            "boundary_tower": ("e*sum epsilon_i^(m/e) if e divides m, otherwise zero"),
            "even_relative_degree": "e*(d-1)",
        },
        "imported": [
            "Grothendieck-Ogg-Shafarevich",
            "Grothendieck trace formula",
            "Deligne weight bound",
        ],
        "rows": len(rows),
        "boundary_rows": boundary_rows,
        "controls": {
            "q5_d4": next(row for row in rows if row["q"] == 5 and row["d"] == 4),
            "q3_d128": next(row for row in rows if row["q"] == 3 and row["d"] == 128),
        },
        "resource_ledger": {
            "bit_operations": bit_operations,
            "max_bit_operations": MAX_BIT_OPERATIONS,
            "boundary_rows": boundary_rows,
            "max_boundary_rows": MAX_BOUNDARY_ROWS,
            "finite_fields_enumerated": 0,
            "polynomials_enumerated": 0,
            "curves_enumerated": 0,
            "cohomology_groups_computed": 0,
            "l_function_zeros_enumerated": 0,
        },
        "open": [
            "many-place physical FFPS source adapter",
            "legal extension across source punctures",
            "varying-conductor selected trace estimate",
            "CYSEL, WCADD, WCKUM, RH, and GRH",
        ],
    }


def run_checks() -> dict[str, object]:
    check_source_blobs()
    report = build_report()
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "full-rank quadratic-torsor construction",
        "removable-puncture tax",
        "same-characteristic tower",
        "dim H_c^1=2e-2",
        "legal source extension across middle punctures",
        "not an FFPS source realization",
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
