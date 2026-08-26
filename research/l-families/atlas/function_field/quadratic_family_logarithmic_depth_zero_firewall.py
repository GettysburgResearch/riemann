#!/usr/bin/env python3
"""Bounded replay for the odd-notch logarithmic-depth zero firewall."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FUNCTION_FIELD_PATH = "research/l-families/atlas/function_field"
FIXED_DEPTH_COMMIT = "d61323f8c269bdf114d958d6596d0d32bf793efb"
ANTICONCENTRATION_COMMIT = "cf7b10ef5e50693b9150996e3891da8debb6b180"
MAX_REPLAY_J = 8
MAX_WINDOW_SCAN = 64
MAX_CENTRAL_COUNT = 512
REPLAY_Q_VALUES = (3, 5, 7, 9)
CENTRAL_PANELS = ((3, 1), (3, 2), (5, 1))
WINDOW_INPUTS = (
    (3, 3**8),
    (3, 3**12),
    (3, 3**16),
    (3, 3**20),
    (5, 5**8),
    (5, 5**12),
)

SOURCE_BLOBS = {
    (
        "9716d2261e9e7843a6c1ffffd67ee8d6756060aa",
        f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_CLOSED_PLACE_WEIGHT_NOTCH.md",
    ): "a1b8476ddd3cad6f63ff205392426ae9c2d0829c",
    (
        "4fc8930e14eaa3863d3f3edc151c056d7d5aedce",
        f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_NOTCH_DEPTH_PHASE_DIAGRAM.md",
    ): "01cefa8a55c9b1ae1a0b5bed9c11fe323fb6764e",
    (
        FIXED_DEPTH_COMMIT,
        f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_FIXED_DEPTH_TRACE_ZERO_DENSITY.md",
    ): "1803cdf033710d2bbb53b83144cbf4b2ae324554",
    (
        FIXED_DEPTH_COMMIT,
        f"{FUNCTION_FIELD_PATH}/quadratic_family_fixed_depth_trace_zero_density.py",
    ): "935c3ddbef1550675384441daa679802d75636a6",
    (
        FIXED_DEPTH_COMMIT,
        f"{FUNCTION_FIELD_PATH}/quadratic_family_fixed_depth_trace_zero_density.json",
    ): "68e17b580208e12756cc3ed9f102407e07765dfd",
    (
        ANTICONCENTRATION_COMMIT,
        f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_LOCAL_DELTA_TOWER_ANTICONCENTRATION.md",
    ): "c6c9c27417ccf9521a2b777946e09b09d9184068",
    (
        ANTICONCENTRATION_COMMIT,
        f"{FUNCTION_FIELD_PATH}/quadratic_family_local_delta_tower_anticoncentration.py",
    ): "3938f64a81e33349e7e7c9b795a018597ec36f72",
    (
        ANTICONCENTRATION_COMMIT,
        f"{FUNCTION_FIELD_PATH}/quadratic_family_local_delta_tower_anticoncentration.json",
    ): "91086ee46dea9961cde6d740e424dcfd355761f0",
}


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"source blob mismatch: {commit}:{path}")


def _validate_q(q_value: int) -> None:
    if (
        isinstance(q_value, bool)
        or not isinstance(q_value, int)
        or q_value < 3
        or q_value % 2 == 0
    ):
        raise ValueError("q must be an odd integer at least three")


def _validate_depth(depth: int) -> None:
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 1:
        raise ValueError("depth must be a positive integer")


def _divisors(value: int) -> tuple[int, ...]:
    return tuple(divisor for divisor in range(1, value + 1) if value % divisor == 0)


def _mobius(value: int) -> int:
    remaining = value
    parity = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            parity += 1
            if remaining % prime == 0:
                return 0
        prime += 1
    if remaining > 1:
        parity += 1
    return -1 if parity % 2 else 1


def irreducible_count(q_value: int, degree: int) -> int:
    _validate_q(q_value)
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 1:
        raise ValueError("degree must be a positive integer")
    numerator = sum(
        _mobius(divisor) * q_value ** (degree // divisor)
        for divisor in _divisors(degree)
    )
    if numerator % degree:
        raise ArithmeticError("irreducible-count formula lost integrality")
    return numerator // degree


def modulus_degree(q_value: int, top_degree: int) -> int:
    """Degree of the product of all primes through ``top_degree``."""

    _validate_q(q_value)
    if (
        isinstance(top_degree, bool)
        or not isinstance(top_degree, int)
        or top_degree < 1
    ):
        raise ValueError("top_degree must be a positive integer")
    return sum(
        degree * irreducible_count(q_value, degree)
        for degree in range(1, top_degree + 1)
    )


def modulus_bounds_hold(q_value: int, depth: int) -> bool:
    """Check 2q^r/3 <= ell_r < q^(r+1)/(q-1), r=2j+1."""

    _validate_depth(depth)
    if depth > MAX_REPLAY_J:
        raise ValueError(f"depth exceeds replay cap {MAX_REPLAY_J}")
    top_degree = 2 * depth + 1
    ell = modulus_degree(q_value, top_degree)
    lower = 3 * ell >= 2 * q_value**top_degree
    upper = (q_value - 1) * ell < q_value ** (top_degree + 1)
    return lower and upper


def central_rademacher_atom(count: int) -> Fraction:
    if (
        isinstance(count, bool)
        or not isinstance(count, int)
        or not 1 <= count <= MAX_CENTRAL_COUNT
    ):
        raise ValueError(f"count must be an integer in [1,{MAX_CENTRAL_COUNT}]")
    return Fraction(math.comb(count, count // 2), 2**count)


def beta_squared_majorant(q_value: int, depth: int) -> Fraction:
    """Square of sqrt(3r/2) q^(-r/2)."""

    _validate_q(q_value)
    _validate_depth(depth)
    top_degree = 2 * depth + 1
    return Fraction(3 * top_degree, 2 * q_value**top_degree)


def layer_parameters(q_value: int, h_value: int, depth: int) -> dict[str, object]:
    _validate_q(q_value)
    _validate_depth(depth)
    if isinstance(h_value, bool) or not isinstance(h_value, int) or h_value < 2:
        raise ValueError("h must be an integer at least two")
    minimum_degree = h_value - depth
    top_degree = 2 * depth + 1
    ell = modulus_degree(q_value, top_degree)
    return {
        "q": q_value,
        "h": h_value,
        "M": 4 * h_value + 1,
        "j": depth,
        "d": minimum_degree,
        "r": top_degree,
        "ell_r": ell,
        "d_greater_than_r": minimum_degree > top_degree,
        "safe_modulus": 4 * ell <= minimum_degree,
        "twice_pnt_exponent": 2 * ell - minimum_degree,
        "rough_layer_weight": str(Fraction(1, minimum_degree**2))
        if minimum_degree > 0
        else None,
        "beta_squared_majorant": str(beta_squared_majorant(q_value, depth)),
    }


def safe_terminal_depth(q_value: int, h_value: int, depth: int) -> bool:
    panel = layer_parameters(q_value, h_value, depth)
    return bool(panel["d_greater_than_r"] and panel["safe_modulus"])


def maximum_safe_depth(q_value: int, h_value: int) -> int:
    _validate_q(q_value)
    if isinstance(h_value, bool) or not isinstance(h_value, int) or h_value < 2:
        raise ValueError("h must be an integer at least two")
    maximum = 0
    for depth in range(1, MAX_WINDOW_SCAN + 1):
        if not safe_terminal_depth(q_value, h_value, depth):
            break
        maximum = depth
    if maximum == MAX_WINDOW_SCAN and safe_terminal_depth(
        q_value, h_value, MAX_WINDOW_SCAN + 1
    ):
        raise RuntimeError("safe-window scan cap is too small")
    return maximum


def marked_prime_signature(
    h_value: int, depth: int, complement_multiplicity: int
) -> dict[str, object]:
    _validate_depth(depth)
    if isinstance(h_value, bool) or not isinstance(h_value, int) or h_value < 2:
        raise ValueError("h must be an integer at least two")
    if (
        isinstance(complement_multiplicity, bool)
        or not isinstance(complement_multiplicity, int)
        or complement_multiplicity < 0
    ):
        raise ValueError("complement multiplicity must be nonnegative")
    minimum_degree = h_value - depth
    top_degree = 2 * depth + 1
    return {
        "d": minimum_degree,
        "r": top_degree,
        "marked_factor_degree": minimum_degree,
        "a_d": complement_multiplicity + 1,
        "top_sign_sum": f"S_{top_degree}",
        "top_sign_coefficient": complement_multiplicity + 1,
        "other_channels_have_degree_below_r": True,
        "marked_pair_overcounts_by_m_d": True,
        "R_divides_C_is_dropped_only_to_enlarge_upper_bound": True,
    }


def run() -> dict[str, object]:
    modulus_panels = []
    for q_value in REPLAY_Q_VALUES:
        if not all(
            modulus_bounds_hold(q_value, depth) for depth in range(1, MAX_REPLAY_J + 1)
        ):
            raise ArithmeticError("modulus-degree bounds failed")
        modulus_panels.append(
            {
                "q": q_value,
                "maximum_depth": MAX_REPLAY_J,
                "all_exact_bounds_hold": True,
            }
        )

    central_panels = []
    for q_value, depth in CENTRAL_PANELS:
        top_degree = 2 * depth + 1
        count = irreducible_count(q_value, top_degree)
        atom = central_rademacher_atom(count)
        majorant = beta_squared_majorant(q_value, depth)
        if atom * atom > Fraction(1, count) or Fraction(1, count) > majorant:
            raise ArithmeticError("anti-concentration chain failed")
        central_panels.append(
            {
                "q": q_value,
                "j": depth,
                "r": top_degree,
                "I_q(r)": count,
                "beta_r": str(atom),
                "beta_r_squared": str(atom * atom),
                "simple_squared_majorant": str(majorant),
            }
        )

    window_panels = []
    for q_value, h_value in WINDOW_INPUTS:
        maximum = maximum_safe_depth(q_value, h_value)
        terminal = layer_parameters(q_value, h_value, maximum) if maximum else None
        first_failure = layer_parameters(q_value, h_value, maximum + 1)
        window_panels.append(
            {
                "q": q_value,
                "h": h_value,
                "maximum_safe_depth": maximum,
                "terminal_panel": terminal,
                "first_failure_panel": first_failure,
            }
        )

    return {
        "schema": "riemann.function_field.logarithmic_depth_zero_firewall.v1",
        "status": (
            "uniform marked-prime raw-zero bound and logarithmic growing-depth "
            "summation theorem"
        ),
        "frozen_sources": {
            f"{commit}:{path}": blob for (commit, path), blob in SOURCE_BLOBS.items()
        },
        "notation": {
            "n": "2h+1",
            "M": "4h+1",
            "d": "h-j",
            "r": "2j+1",
            "A_r": "product_(deg P<=r) P",
            "ell_r": "sum_(e<=r) e I_q(e)",
            "beta_r": "2^(-I_q(r))*binom(I_q(r),floor(I_q(r)/2))",
        },
        "marked_prime_reduction": {
            "factorization": "Q=R*C with deg R=d and C squarefree d-rough",
            "overcount": "each Q occurs m_d times, so marked pairs majorize Q",
            "fixed_complement": "all a_k and a_d=m_d(C)+1 are fixed",
            "detector": "S_(n,RC)=a_d*S_r+H_C(signs of degrees below r)",
            "residue_zero_fraction": "|E_C|/phi(A_r)<=beta_r",
            "R_divides_C": (
                "excluded for squarefreeness, then dropped only to enlarge the "
                "prime upper bound"
            ),
            "profile_remainder": None,
        },
        "pnt_ap": {
            "exact_normalization": ("pi_q(d;A,a)=I_q(d)/phi(A)+E_(d,A,a)"),
            "uniform_error": "|E_(d,A,a)|<=(deg(A)+1)q^(d/2)/d",
            "subset_bound": ("pi_q(d;A,E)<=beta*q^d/d*(1+(deg(A)+1)q^(deg(A)-d/2))"),
        },
        "whole_layer_bound": ("Z_(q,h,j)/q^M<=beta_r/d^2*(1+(ell_r+1)q^(ell_r-d/2))"),
        "safe_window": {
            "condition": "ell_(2J+1)<=(h-J)/4",
            "sum": "sum_(j=1)^J Z_(q,h,j)/q^M=O_q(h^-2)=O_q(M^-2)",
            "logarithmic_corollary": (
                "J<=(1/2-epsilon)log_q(h) is safe for sufficiently large h"
            ),
            "modulus_bounds": "2q^r/3<=ell_r<q^(r+1)/(q-1)",
            "panels": window_panels,
        },
        "bounded_replay": {
            "modulus_panels": modulus_panels,
            "central_panels": central_panels,
            "marked_prime_panels": [
                marked_prime_signature(100, 1, multiplicity)
                for multiplicity in range(3)
            ],
        },
        "barrier": {
            "scale": "ell_r=Theta_q(q^r), hence q^(2j)<<h",
            "k_wise_marginal_is_insufficient": True,
            "reason": (
                "the target H_C depends on all lower-degree signs from the same "
                "marked prime; conditioning it requires the exponential-degree "
                "lower-sign modulus"
            ),
            "beyond_logarithmic_window": False,
        },
        "claim_boundary": {
            "raw_detector_zeros": True,
            "individual_L_function_zero": False,
            "macroscopic_depth_bound": False,
            "rh_or_grh": False,
            "external_priority_claim": False,
        },
        "resource_caps": {
            "maximum_replay_depth": MAX_REPLAY_J,
            "maximum_window_scan": MAX_WINDOW_SCAN,
            "polynomials_enumerated": 0,
            "irreducibles_enumerated": 0,
            "residue_classes_enumerated": 0,
            "finite_field_elements_enumerated": 0,
            "curves_enumerated": 0,
            "conductors_enumerated": 0,
            "zeros_enumerated": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    if args.check:
        check_source_blobs()
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
