#!/usr/bin/env python3
"""Exact commensurability and endpoint-aliasing firewall for detector ports."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "canonical_detector_norm_lattice_obstruction.json"
NOTE_PATH = HERE / "CANONICAL_DETECTOR_NORM_LATTICE_OBSTRUCTION.md"
TEST_PATH = ROOT / "tests" / "test_canonical_detector_norm_lattice_obstruction.py"

SOURCE_LOCKS = {
    "research/integrated/wavelet_xd/README.md": "6a04ae3f85bcf00929079dd845f12175bb4e81e88eb20997ca7b38f17c67702f",
    "research/integrated/vaughan_half_divisor/HALF_DIVISOR_REDUCTION.md": "372956a4d7fe0da8ede50aad2601e469407debaa44124a2f2737c34814298ed6",
    "research/integrated/conjunctive/README.md": "3919171cc2fcc42c6a3b358e750a264747edd0e7dbc8ae4f618ca32508651351",
    "research/l-families/atlas/function_field/FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md": "6b3a0958422f01b44b7702b1088f4e13926d5d11a7725bde2582cd2d371b07e6",
}

CONTROL_BASES = (2, 3, 4, 5, 7, 8, 9, 11, 25)
CANONICAL_DILATIONS = (2, 4, 8)
SOURCE_ATOM_CAP = 256

# Exact coefficients a+b*sqrt(2), ordered by S_(2**j), j=0,1,2,3.
K1_COEFFICIENTS = ((1, 0), (-2, -1), (1, 2), (0, -1))


def sha256_lf(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def assert_sources() -> None:
    for relative, expected in SOURCE_LOCKS.items():
        path = ROOT / relative
        if not path.is_file() or sha256_lf(path) != expected:
            raise RuntimeError(f"locked canonical-detector source drifted: {relative}")


def factor_integer(value: int) -> dict[str, int]:
    if value < 1:
        raise ValueError("factorization input must be positive")
    integer_factors: dict[int, int] = {}
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            integer_factors[divisor] = integer_factors.get(divisor, 0) + 1
            remaining //= divisor
        divisor += 1
    if remaining > 1:
        integer_factors[remaining] = integer_factors.get(remaining, 0) + 1
    return {str(prime): exponent for prime, exponent in integer_factors.items()}


def native_integer_shift(base: int, dilation: int) -> int | None:
    """Return k>=0 with dilation=base**k, or None."""
    if base < 2 or dilation < 1:
        raise ValueError("base must exceed one and dilation must be positive")
    power = 1
    shift = 0
    while power < dilation:
        power *= base
        shift += 1
    return shift if power == dilation else None


def endpoint_shift(base: int, dilation: int) -> int:
    """Return ceil(log_base(dilation)) without numerical logarithms."""
    if base < 2 or dilation < 1:
        raise ValueError("base must exceed one and dilation must be positive")
    power = 1
    shift = 0
    while power < dilation:
        power *= base
        shift += 1
    return shift


def add_quadratic(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] + right[0], left[1] + right[1]


def scale_quadratic(value: tuple[int, int], scalar: int) -> tuple[int, int]:
    return value[0] * scalar, value[1] * scalar


def is_zero_quadratic(value: tuple[int, int]) -> bool:
    return value == (0, 0)


def collapsed_k1(base: int) -> dict[str, object]:
    shifts = tuple(endpoint_shift(base, 2**index) for index in range(4))
    grouped: dict[int, tuple[int, int]] = defaultdict(lambda: (0, 0))
    for shift, coefficient in zip(shifts, K1_COEFFICIENTS, strict=True):
        grouped[shift] = add_quadratic(grouped[shift], coefficient)

    coefficients = tuple(grouped.get(shift, (0, 0)) for shift in range(max(shifts) + 1))
    derivative_orders: list[tuple[int, int]] = []
    for order in range(len(coefficients) + 1):
        derivative = (0, 0)
        for exponent, coefficient in enumerate(coefficients):
            if exponent < order:
                continue
            falling = math.prod(range(exponent - order + 1, exponent + 1))
            derivative = add_quadratic(
                derivative, scale_quadratic(coefficient, falling)
            )
        derivative_orders.append(derivative)
        if not is_zero_quadratic(derivative):
            multiplicity = order
            break
    else:  # pragma: no cover - a nonzero finite polynomial cannot reach this branch
        raise ArithmeticError("collapsed wavelet vanished identically")

    return {
        "base_q": base,
        "endpoint_shifts_for_1_2_4_8": list(shifts),
        "coefficients_by_degree_shift_a_plus_b_sqrt2": [
            list(value) for value in coefficients
        ],
        "derivatives_at_one_until_first_nonzero": [
            list(value) for value in derivative_orders
        ],
        "constant_zero_multiplicity": multiplicity,
    }


def common_native_dilation(bases: tuple[int, ...], search_cap: int = 12) -> int | None:
    """Find the smallest common q_i**k_i>1 within a tiny exponent cap."""
    if not bases or any(base < 2 for base in bases):
        raise ValueError("at least one valid base is required")
    powers = [
        {base**exponent for exponent in range(1, search_cap + 1)} for base in bases
    ]
    intersection = set.intersection(*powers)
    return min(intersection) if intersection else None


def no_floats(value: object) -> None:
    if isinstance(value, float):
        raise TypeError("claim payload contains a float")
    if isinstance(value, dict):
        for key, item in value.items():
            no_floats(key)
            no_floats(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            no_floats(item)


def build_fixture() -> dict[str, object]:
    assert_sources()
    controls = []
    source_atoms = 0
    for base in CONTROL_BASES:
        dilation_rows = []
        for dilation in CANONICAL_DILATIONS:
            dilation_rows.append(
                {
                    "dilation": dilation,
                    "native_integer_shift": native_integer_shift(base, dilation),
                    "endpoint_step_shift": endpoint_shift(base, dilation),
                }
            )
            source_atoms += 1
        controls.append(
            {
                "base_q": base,
                "prime_factorization": factor_integer(base),
                "dilations": dilation_rows,
                "collapsed_k1": collapsed_k1(base),
            }
        )
    if source_atoms > SOURCE_ATOM_CAP:
        raise RuntimeError("source-atom cap exceeded")

    fixture: dict[str, object] = {
        "schema": "canonical-detector-norm-lattice-obstruction-v1",
        "theorem": {
            "native_translation": "lambda preserves q^Z iff lambda=q^k for an integer k",
            "step_extension": (
                "for lambda=q^(k+beta), S_lambda uses shift k+1 below log-phase "
                "beta and shift k above it"
            ),
            "endpoint_alias": "the sampled shift is ceil(log_q(lambda))",
            "minimal_wavelet_obstruction": (
                "the endpoint-sampled K1 constant zero has multiplicity one for every "
                "integer q>2, versus multiplicity two at q=2"
            ),
            "odd_q_consequence": (
                "2,4,8 are not native translations on q^Z for odd prime-power q"
            ),
        },
        "canonical_source_semantics": {
            "XD": "K1=(I-sqrt(2)S_2)(I-S_2)^2 with ratio-eight support",
            "HCNC": "oriented signed ratio-four near-collision",
            "BPOE": "physical observation on dyadic shell operators",
        },
        "controls": controls,
        "cross_base_controls": {
            "q_3_5_7_smallest_common_native_dilation": common_native_dilation(
                (3, 5, 7)
            ),
            "q_3_9_smallest_common_native_dilation": common_native_dilation((3, 9)),
            "q_3_27_smallest_common_native_dilation": common_native_dilation((3, 27)),
        },
        "scope": {
            "source_atoms_used": source_atoms,
            "source_atom_cap": SOURCE_ATOM_CAP,
            "continuous_phase_detector_evaluated": False,
            "q_adic_replacement_declared_canonical": False,
            "characteristic_two_family_constructed": False,
            "family_moment_or_sign_proved": False,
            "rh_or_grh_proved": False,
        },
        "provenance": {
            "source_locks_sha256_lf": SOURCE_LOCKS,
            "producer_sha256_lf": sha256_lf(Path(__file__)),
            "note_sha256_lf": sha256_lf(NOTE_PATH),
            "test_sha256_lf": sha256_lf(TEST_PATH),
        },
    }
    no_floats(fixture)
    return fixture


def render(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()
    rendered = render(build_fixture())
    if args.check:
        if (
            not OUTPUT_PATH.is_file()
            or OUTPUT_PATH.read_text(encoding="utf-8") != rendered
        ):
            raise SystemExit("canonical detector norm-lattice fixture drifted")
        print("PASS_CANONICAL_DETECTOR_NORM_LATTICE_OBSTRUCTION")
        return
    if args.stdout:
        print(rendered, end="")
        return
    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
