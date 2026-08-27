#!/usr/bin/env python3
"""Exact bounded replay for the four-place universal Tate notch."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections.abc import Callable
from math import isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "c94466e28a48ec429150f63de6d334d4c4f60110"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "QUADRATIC_FAMILY_MULTIPLACE_L_FUNCTION_IDENTITY.md"
    ): "56790383fc49fb2f9116bc7add90e19afd00d1c7",
    (
        "research/l-families/atlas/function_field/"
        "quadratic_family_multiplace_l_function_identity.py"
    ): "e96b8a653573e72966f2fa5069b322996854bec8",
    (
        "research/l-families/atlas/function_field/"
        "quadratic_family_multiplace_l_function_identity.json"
    ): "f6183be7e06b284f3cc2c3c4a6ffe5b970c0411e",
    "tests/test_quadratic_family_multiplace_l_function_identity.py": (
        "693b94467d4968b3b9af12a9e52a955e0ada2331"
    ),
}

CONTROL_TRACES = {
    5: (-3, -1, 1, 3),
    7: (-4, -1, 2, 4),
}
RECURRENCE_CHECKS = 8
MAX_RAW_EXTENSION = 14


def check_source_contract() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"source blob mismatch: {path}")


def validate_prime(prime: int) -> None:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 5:
        raise ValueError("base must be an odd prime at least five")
    if any(prime % divisor == 0 for divisor in range(2, isqrt(prime) + 1)):
        raise ValueError("base must be prime")


def validate_trace(prime: int, trace: int) -> None:
    validate_prime(prime)
    if isinstance(trace, bool) or not isinstance(trace, int):
        raise TypeError("trace must be an integer")
    if trace * trace > 4 * prime:
        raise ValueError("trace must satisfy the elliptic Hasse bound")


def polynomial_multiply(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    return tuple(output)


def polynomial_value(coefficients: tuple[int, ...], value: int) -> int:
    total = 0
    for coefficient in reversed(coefficients):
        total = total * value + coefficient
    return total


def notch_polynomial(prime: int) -> tuple[int, ...]:
    validate_prime(prime)
    return prime**2, -(1 + prime**2), 1


def untwisted_polynomial(prime: int, trace: int) -> tuple[int, ...]:
    validate_trace(prime, trace)
    return prime, -trace, 1


def twisted_polynomial(prime: int, trace: int) -> tuple[int, ...]:
    validate_trace(prime, trace)
    return prime**3, -prime * trace, 1


def geometric_recurrence_polynomial(prime: int, trace: int) -> tuple[int, ...]:
    return polynomial_multiply(
        untwisted_polynomial(prime, trace), twisted_polynomial(prime, trace)
    )


def trace_value(prime: int, trace: int, extension_degree: int) -> int:
    validate_trace(prime, trace)
    if extension_degree < 0:
        raise ValueError("extension degree must be nonnegative")
    if extension_degree == 0:
        return 2
    previous, current = 2, trace
    for _ in range(1, extension_degree):
        previous, current = current, trace * current - prime * previous
    return current


def raw_correlation(prime: int, trace: int, extension_degree: int) -> int:
    if extension_degree < 1:
        raise ValueError("raw family extension degree must be positive")
    q = prime**extension_degree
    return q**2 - 10 + (4 * q - 10) * trace_value(prime, trace, extension_degree)


def apply_filter(
    sequence: Callable[[int], int],
    coefficients: tuple[int, ...],
    extension_degree: int,
) -> int:
    if extension_degree < 1:
        raise ValueError("filtered extension degree must be positive")
    return sum(
        coefficient * sequence(extension_degree + offset)
        for offset, coefficient in enumerate(coefficients)
    )


def filtered_correlation(prime: int, trace: int, extension_degree: int) -> int:
    return apply_filter(
        lambda degree: raw_correlation(prime, trace, degree),
        notch_polynomial(prime),
        extension_degree,
    )


def verify_recurrence(
    sequence: Callable[[int], int],
    coefficients: tuple[int, ...],
    checks: int = RECURRENCE_CHECKS,
) -> bool:
    if checks < 1:
        raise ValueError("recurrence check count must be positive")
    return all(
        sum(
            coefficient * sequence(extension_degree + offset)
            for offset, coefficient in enumerate(coefficients)
        )
        == 0
        for extension_degree in range(1, checks + 1)
    )


def bareiss_determinant(matrix: tuple[tuple[int, ...], ...]) -> int:
    size = len(matrix)
    if not size or any(len(row) != size for row in matrix):
        raise ValueError("matrix must be nonempty and square")
    work = [list(row) for row in matrix]
    sign = 1
    previous_pivot = 1
    for column in range(size - 1):
        pivot_row = next(
            (row for row in range(column, size) if work[row][column]), None
        )
        if pivot_row is None:
            return 0
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            sign *= -1
        pivot = work[column][column]
        for row in range(column + 1, size):
            for other_column in range(column + 1, size):
                numerator = (
                    work[row][other_column] * pivot
                    - work[row][column] * work[column][other_column]
                )
                if numerator % previous_pivot:
                    raise ArithmeticError("Bareiss division ceased to be exact")
                work[row][other_column] = numerator // previous_pivot
        previous_pivot = pivot
    return sign * work[-1][-1]


def hankel_determinant(sequence: Callable[[int], int], rank: int) -> int:
    if rank < 1:
        raise ValueError("Hankel rank must be positive")
    matrix = tuple(
        tuple(sequence(1 + row + column) for column in range(rank))
        for row in range(rank)
    )
    return bareiss_determinant(matrix)


def control_panel(prime: int, trace: int) -> dict[str, object]:
    validate_trace(prime, trace)
    raw = lambda degree: raw_correlation(prime, trace, degree)
    filtered = lambda degree: filtered_correlation(prime, trace, degree)
    recurrence = geometric_recurrence_polynomial(prime, trace)
    if not verify_recurrence(filtered, recurrence):
        raise ArithmeticError("rank-four geometric recurrence failed")
    rank_four_determinant = hankel_determinant(filtered, 4)
    if rank_four_determinant == 0:
        raise ArithmeticError("rank-four Hankel determinant vanished")

    isolate_untwisted = polynomial_multiply(
        notch_polynomial(prime), twisted_polynomial(prime, trace)
    )
    isolate_twisted = polynomial_multiply(
        notch_polynomial(prime), untwisted_polynomial(prime, trace)
    )
    untwisted_residual = lambda degree: apply_filter(raw, isolate_untwisted, degree)
    twisted_residual = lambda degree: apply_filter(raw, isolate_twisted, degree)
    if not verify_recurrence(untwisted_residual, untwisted_polynomial(prime, trace)):
        raise ArithmeticError("adaptive untwisted recurrence failed")
    if not verify_recurrence(twisted_residual, twisted_polynomial(prime, trace)):
        raise ArithmeticError("adaptive twisted recurrence failed")
    untwisted_determinant = hankel_determinant(untwisted_residual, 2)
    twisted_determinant = hankel_determinant(twisted_residual, 2)
    if not untwisted_determinant or not twisted_determinant:
        raise ArithmeticError("adaptive rank-two Hankel determinant vanished")

    return {
        "adaptive_filters": {
            "isolate_twisted_degree": len(isolate_twisted) - 1,
            "isolate_twisted_hankel_2": str(twisted_determinant),
            "isolate_untwisted_degree": len(isolate_untwisted) - 1,
            "isolate_untwisted_hankel_2": str(untwisted_determinant),
        },
        "filtered_first_four": [str(filtered(degree)) for degree in range(1, 5)],
        "geometric_recurrence_low_to_high": list(recurrence),
        "hankel_rank_four_determinant": str(rank_four_determinant),
        "prime": prime,
        "raw_first_three": [str(raw(degree)) for degree in range(1, 4)],
        "trace": trace,
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    if MAX_RAW_EXTENSION != RECURRENCE_CHECKS + 6:
        raise ArithmeticError("declared raw extension cap no longer matches replay")
    controls = [
        control_panel(prime, trace)
        for prime, traces in CONTROL_TRACES.items()
        for trace in traces
    ]
    for prime in CONTROL_TRACES:
        notch = notch_polynomial(prime)
        if polynomial_value(notch, 1) or polynomial_value(notch, prime**2):
            raise ArithmeticError("universal Tate notch lost a nuisance root")
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "import": "exact all-field degree-five four-place row",
        },
        "theorem": {
            "raw_tower": (
                "S_n=p^(2n)-10+(4*p^n-10)*t_n, t_n=lambda^n+mu^n and lambda*mu=p"
            ),
            "universal_notch": "N_p(E)=(E-1)*(E-p^2)",
            "minimality": (
                "every configuration-independent scalar-nuisance filter is "
                "divisible by N_p; degree two is uniquely monic-minimal"
            ),
            "post_notch_roots": ["lambda", "mu", "p*lambda", "p*mu"],
            "post_notch_minimal_rank": 4,
            "post_notch_characteristic_polynomial": ("(T^2-t*T+p)*(T^2-p*t*T+p^3)"),
            "universal_rank_two_verdict": (
                "impossible for a nonzero finite-degree Q(p)-coefficient filter "
                "independent of the formal elliptic trace"
            ),
            "adaptive_rank_two": (
                "multiply N_p by the trace-dependent quadratic for the unwanted "
                "elliptic pair; total degree four is minimal"
            ),
        },
        "place_count_selection": {
            "four": "two scalar Tate nuisances; unique quadratic notch; exact rank four",
            "five": "raw row already has no scalar Tate nuisance",
            "six": (
                "trace and middle-coefficient spectra require a separate "
                "exceptional-stratum analysis"
            ),
        },
        "controls": controls,
        "proof_ledger": {
            "four_place_tower_identity": "IMPORTED EXACT",
            "nuisance_root_ledger": "PROVED EXACT",
            "unique_minimal_universal_notch": "PROVED EXACT",
            "rank_four_for_every_configuration": "PROVED BY WEIL MODULI AND VANDERMONDE",
            "universal_rank_two_filter": "REFUTED OVER THE FORMAL TRACE FAMILY",
            "adaptive_degree_four_filter": "PROVED EXACT",
            "sheaf_or_tate_class_realization": "NOT CLAIMED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "control_primes": list(CONTROL_TRACES),
            "control_rows": len(controls),
            "largest_exact_matrix": 4,
            "maximum_raw_extension_index": MAX_RAW_EXTENSION,
            "finite_field_elements": 0,
            "curves_enumerated": 0,
            "zeta_zeros": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if not args.check:
        print(rendered, end="")


if __name__ == "__main__":
    main()
