#!/usr/bin/env python3
"""Exact replay for the rough-sieved function-field Witt frontier."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from fractions import Fraction
from pathlib import Path

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
    "tests/test_function_field_divisor_wavelet_witt_factorization.py": (
        "5fa7501c6bea03a9325d5056ecdd603eed5694b9"
    ),
}
PREDECESSOR_PATH = HERE / "function_field_divisor_wavelet_witt_factorization.py"
SPEC = importlib.util.spec_from_file_location(
    "divisor_wavelet_witt_source", PREDECESSOR_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load the frozen Witt producer")
source = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(source)

MAX_TOTAL_DEGREE = 8
CONTROL_Q = 5
CONTROL_CUTOFF = 2
CONTROL_RADIUS = Fraction(9, 20)


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


def validate_cutoff(maximum_degree: int, cutoff: int) -> None:
    source.validate_nonnegative_integer(maximum_degree, "maximum degree")
    source.validate_nonnegative_integer(cutoff, "rough cutoff")
    if cutoff > maximum_degree:
        raise ValueError("rough cutoff cannot exceed the replay degree")


def degree_range_product(
    q: int, minimum_prime_degree: int, maximum_prime_degree: int, truncation: int
) -> source.Polynomial:
    output: source.Polynomial = {(0, 0): 1}
    for prime_degree in range(minimum_prime_degree, maximum_prime_degree + 1):
        output = source.multiply_truncated(
            output,
            source.direct_prime_degree_factor(q, prime_degree, truncation),
            truncation,
        )
    return output


def removed_product(q: int, cutoff: int, maximum_degree: int) -> source.Polynomial:
    validate_cutoff(maximum_degree, cutoff)
    return degree_range_product(q, 1, cutoff, maximum_degree)


def rough_product(q: int, cutoff: int, maximum_degree: int) -> source.Polynomial:
    validate_cutoff(maximum_degree, cutoff)
    return degree_range_product(q, cutoff + 1, maximum_degree, maximum_degree)


def conditioning_inverse(q: int, cutoff: int, radius: Fraction) -> Fraction:
    source.validate_nonnegative_integer(cutoff, "rough cutoff")
    # Validate the formal field-size parameter even when cutoff == 0 and the
    # local-factor loop below is empty. Geometric use still requires q to be
    # a prime power, as fenced in the theorem packet.
    source.irreducible_count(q, 1)
    if not isinstance(radius, Fraction) or radius <= 0 or radius >= Fraction(1, 2):
        raise ValueError(
            "control radius must be a Fraction strictly between zero and one half"
        )
    answer = Fraction(1)
    for degree in range(1, cutoff + 1):
        local = 1 - 2 * radius**degree
        if local <= 0:
            raise ArithmeticError("deleted local factor ceased to be positive")
        answer *= local ** (-source.irreducible_count(q, degree))
    return answer


def control_panel() -> dict[str, object]:
    complete = source.direct_euler_product(CONTROL_Q, MAX_TOTAL_DEGREE)
    removed = removed_product(CONTROL_Q, CONTROL_CUTOFF, MAX_TOTAL_DEGREE)
    rough = rough_product(CONTROL_Q, CONTROL_CUTOFF, MAX_TOTAL_DEGREE)
    reassembled = source.multiply_truncated(removed, rough, MAX_TOTAL_DEGREE)
    if reassembled != complete:
        raise ArithmeticError("rough and removed Euler factors did not reassemble")
    condition = conditioning_inverse(CONTROL_Q, CONTROL_CUTOFF, CONTROL_RADIUS)
    if CONTROL_Q * CONTROL_RADIUS**2 <= 1:
        raise ArithmeticError("control radius is not above the critical radius")
    return {
        "q": CONTROL_Q,
        "rough_cutoff_degree": CONTROL_CUTOFF,
        "maximum_total_degree": MAX_TOTAL_DEGREE,
        "critical_radius_control": str(CONTROL_RADIUS),
        "q_times_radius_squared": str(CONTROL_Q * CONTROL_RADIUS**2),
        "removed_condition_inverse": str(condition),
        "removed_condition_numerator_digits": len(str(condition.numerator)),
        "rough_nonzero_laurent_monomials": len(rough),
        "rough_phase_one_coefficients": source.phase_one_coefficients(
            rough, MAX_TOTAL_DEGREE
        ),
        "exact_reassembly": True,
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
            "rough_quotient": (
                "F_(q,>y)(u,z)=F_q(u,z)/prod_(deg P<=y)(1-(uz)^degP-(u/z)^degP)"
            ),
            "conditioning_cost": ("log K_(q,y)(r)=O_(q,r)((q*r)^y/y), 0<r<1/2"),
            "critical_subfrontier": (
                "for q>=5 and every eta>0, y_n<=(2-eta)*log_q(n) "
                "retains exponential q^(-n/2)-normalized decay"
            ),
            "absolute_method_barrier": (
                "y_n>=(2+eta)*log_q(n) makes every critical-radius "
                "finite-deletion condition number superexponential in n"
            ),
            "fixed_core": (
                "every fixed squarefree core is a finite Laurent multiplier "
                "times a finite-deletion quotient and preserves |u|<1/2"
            ),
        },
        "bounded_control": control_panel(),
        "proof_ledger": {
            "finite_rough_quotient": "PROVED EXACT",
            "uniform_conditioning_bound": "PROVED",
            "exponent_two_subfrontier": "PROVED FOR THE COMPLETE DEGREE SHELL",
            "exponent_two_absolute_conditioning_barrier": "PROVED",
            "sharp_actual_rough_coefficient_frontier": "NOT CLAIMED",
            "fixed_core_stability": "PROVED",
            "growing_core_or_arbitrary_sieve": "NOT INCLUDED",
            "maximal_height_wavelet": "NOT PROVED",
            "number_field_transfer": "NOT INFERRED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "q": CONTROL_Q,
            "maximum_total_degree": MAX_TOTAL_DEGREE,
            "rough_cutoff_degree": CONTROL_CUTOFF,
            "finite_field_elements": 0,
            "polynomials_enumerated": 0,
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
