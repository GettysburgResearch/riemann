#!/usr/bin/env python3
"""Exact replay for the three-place signed-Tate notch."""

from __future__ import annotations

import argparse
import itertools
import json
import subprocess
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FROZEN_COMMIT = "4a9dc1bcc3fe57a2d6c883cdf4bb6079faa25db8"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "QUADRATIC_FAMILY_THREE_PLACE_ELLIPTIC_INTERFERENCE.md"
    ): "c3855545837643d63416b07e78e2f931b006a226",
    (
        "research/l-families/atlas/function_field/"
        "quadratic_family_three_place_elliptic_interference.py"
    ): "31018f73bf0afb91550f8240bfbc91e84e1c83d8",
}
TOWER_HORIZON = 20


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{FROZEN_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def validate_base(prime: int, trace: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 3
        or not sp.isprime(prime)
    ):
        raise ValueError("base must be an odd prime")
    if isinstance(trace, bool) or not isinstance(trace, int):
        raise TypeError("trace must be an integer")
    if trace * trace > 4 * prime:
        raise ValueError("trace violates the Hasse bound")


def validate_sign(value: int, label: str) -> None:
    if value not in (-1, 1):
        raise ValueError(f"{label} must be +1 or -1")


def elliptic_trace_tower(prime: int, trace: int, horizon: int) -> tuple[int, ...]:
    validate_base(prime, trace)
    if horizon < 1:
        raise ValueError("tower horizon must be positive")
    values = [2, trace]
    for _ in range(2, horizon + 1):
        values.append(trace * values[-1] - prime * values[-2])
    return tuple(values)


def orientation_sum(extension_degree: int, deltas: tuple[int, int, int]) -> int:
    if extension_degree < 0:
        raise ValueError("extension degree must be nonnegative")
    for delta in deltas:
        validate_sign(delta, "orientation sign")
    return sum(delta**extension_degree for delta in deltas)


def nuisance_value(
    extension_degree: int,
    prime: int,
    epsilon: int,
    deltas: tuple[int, int, int],
) -> int:
    validate_sign(epsilon, "minus-one sign")
    q = prime**extension_degree
    return (
        3
        * (1 + epsilon**extension_degree)
        * (2 * q - 3)
        * orientation_sum(extension_degree, deltas)
    )


def geometric_value(extension_degree: int, prime: int, traces: tuple[int, ...]) -> int:
    return 18 * (prime**extension_degree - 2) * traces[extension_degree]


def notch_value(values: tuple[int, ...], index: int, prime: int) -> int:
    if index < 0 or index + 4 >= len(values):
        raise ValueError("notch index requires rows n,n+2,n+4")
    return (
        values[index + 4]
        - (1 + prime**2) * values[index + 2]
        + prime**2 * values[index]
    )


def characteristic_polynomial(prime: int, trace: int) -> tuple[int, ...]:
    validate_base(prime, trace)
    return (
        prime**4,
        -(prime**2) * (prime + 1) * trace,
        prime**3 + prime + prime * trace**2,
        -(prime + 1) * trace,
        1,
    )


def recurrence_holds(values: tuple[int, ...], coefficients: tuple[int, ...]) -> bool:
    order = len(coefficients) - 1
    if len(values) < 2 * order:
        raise ValueError("need at least twice the recurrence order")
    return all(
        sum(
            coefficients[offset] * values[index + offset] for offset in range(order + 1)
        )
        == 0
        for index in range(len(values) - order)
    )


def hankel_rank(values: tuple[int, ...], size: int) -> int:
    if len(values) < 2 * size - 1:
        raise ValueError("not enough values for requested Hankel matrix")
    matrix = sp.Matrix(
        [[values[row + column] for column in range(size)] for row in range(size)]
    )
    return int(matrix.rank())


def control_panel(
    prime: int,
    trace: int,
    epsilon: int,
    deltas: tuple[int, int, int],
) -> dict[str, object]:
    validate_base(prime, trace)
    validate_sign(epsilon, "minus-one sign")
    maximum_extension_degree = TOWER_HORIZON + 8
    traces = elliptic_trace_tower(prime, trace, maximum_extension_degree)
    extension_degrees = tuple(range(1, maximum_extension_degree + 1))
    nuisance = tuple(
        nuisance_value(degree, prime, epsilon, deltas) for degree in extension_degrees
    )
    geometric = tuple(
        geometric_value(degree, prime, traces) for degree in extension_degrees
    )
    total = tuple(left + right for left, right in zip(nuisance, geometric, strict=True))
    notched_nuisance = tuple(
        notch_value(nuisance, index, prime) for index in range(len(nuisance) - 4)
    )
    if any(notched_nuisance):
        raise ArithmeticError("signed-Tate notch did not remove the nuisance channel")
    notched_total = tuple(
        notch_value(total, index, prime) for index in range(len(total) - 4)
    )
    notched_geometric = tuple(
        notch_value(geometric, index, prime) for index in range(len(geometric) - 4)
    )
    if notched_total != notched_geometric:
        raise ArithmeticError("notched total differs from notched geometric channel")
    characteristic = characteristic_polynomial(prime, trace)
    if not recurrence_holds(notched_total, characteristic):
        raise ArithmeticError("elliptic rank-four recurrence failed")
    if hankel_rank(notched_total, 4) != 4:
        raise ArithmeticError("notched sequence did not have minimal rank four")
    recovered_trace_numerator = -characteristic[3]
    if recovered_trace_numerator % (prime + 1):
        raise ArithmeticError("trace-recovery coefficient is not divisible")
    recovered_trace = recovered_trace_numerator // (prime + 1)
    if recovered_trace != trace:
        raise ArithmeticError("trace recovery failed")
    return {
        "characteristic_low_to_high": list(characteristic),
        "deltas": list(deltas),
        "epsilon": epsilon,
        "first_notched_extension_degree": 1,
        "first_six_notched_values": [str(value) for value in notched_total[:6]],
        "hankel_rank": 4,
        "nuisance_notch_zero": True,
        "prime": prime,
        "recovered_trace": recovered_trace,
        "trace": trace,
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    actual_controls = [
        control_panel(3, 0, -1, (1, -1, 1)),
        control_panel(5, -2, 1, (1, -1, 1)),
    ]
    formal_orientation_controls = [
        control_panel(3, 0, -1, deltas)
        for deltas in itertools.product((-1, 1), repeat=3)
    ]
    return {
        "source_contract": {
            "commit": FROZEN_COMMIT,
            "git_blobs": SOURCE_BLOBS,
        },
        "theorem": {
            "cleared_sequence": (
                "R_n=A(p^n)*Delta_n=3(1+epsilon^n)(2p^n-3)S_n+18(p^n-2)t_n"
            ),
            "universal_notch": "(E^2-1)(E^2-p^2)",
            "surviving_roots": "alpha,beta,p*alpha,p*beta",
            "minimal_characteristic": "(T^2-tT+p)(T^2-ptT+p^3)",
            "trace_recovery": "t=-[T^3]P/(p+1)",
        },
        "actual_frozen_controls": actual_controls,
        "formal_orientation_controls_p3": formal_orientation_controls,
        "proof_ledger": {
            "fixed_base_extension_adapter": "PROVED EXACT",
            "universal_nuisance_notch": "PROVED EXACT AND DEGREE-MINIMAL",
            "elliptic_isolation": "PROVED EXACT",
            "minimal_rank_four_recurrence": "PROVED EXACT",
            "trace_recovery": "PROVED EXACT",
            "new_sheaf_or_cohomology_class": "NOT CLAIMED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "base_primes": [3, 5],
            "maximum_extension_degree": TOWER_HORIZON + 8,
            "formal_orientation_profiles": len(formal_orientation_controls),
            "finite_field_elements": 0,
            "curves_enumerated": 0,
            "points_enumerated": 0,
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
