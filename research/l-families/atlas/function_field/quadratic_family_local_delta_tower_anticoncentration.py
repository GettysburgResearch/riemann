#!/usr/bin/env python3
"""Exact bounded replay for local delta-tower anti-concentration."""

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
MAX_REPLAY_J = 12
MAX_CENTRAL_COUNT = 512
REPLAY_Q_VALUES = (3, 5, 7, 9)
CENTRAL_PANELS = ((3, 1), (3, 2), (5, 1))
CHANNEL_DEPTHS = (1, 2, 4, 8)

SOURCE_BLOBS = {
    (
        "9716d2261e9e7843a6c1ffffd67ee8d6756060aa",
        f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_CLOSED_PLACE_WEIGHT_NOTCH.md",
    ): "a1b8476ddd3cad6f63ff205392426ae9c2d0829c",
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


def _validate_q(q_value: int) -> None:
    if (
        isinstance(q_value, bool)
        or not isinstance(q_value, int)
        or q_value < 3
        or q_value % 2 == 0
    ):
        raise ValueError("q must be an odd integer at least three")


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


def central_rademacher_atom(count: int) -> Fraction:
    """Largest atom of a sum of ``count`` independent signs."""

    if (
        isinstance(count, bool)
        or not isinstance(count, int)
        or not 1 <= count <= MAX_CENTRAL_COUNT
    ):
        raise ValueError(f"count must be an integer in [1,{MAX_CENTRAL_COUNT}]")
    return Fraction(math.comb(count, count // 2), 2**count)


def central_atom_bound_holds(count: int) -> bool:
    """Exact rational form of max_atom <= count^(-1/2)."""

    atom = central_rademacher_atom(count)
    return count * atom * atom <= 1


def wallis_induction_bound_holds(index: int) -> bool:
    """Exact check of C(2m,m)/4^m <= (3m+1)^(-1/2)."""

    if (
        isinstance(index, bool)
        or not isinstance(index, int)
        or not 0 <= index <= MAX_CENTRAL_COUNT // 2
    ):
        raise ValueError("index is outside the bounded Wallis replay")
    atom = Fraction(math.comb(2 * index, index), 4**index)
    return (3 * index + 1) * atom * atom <= 1


def channel_signature(depth: int, shift: int) -> dict[str, object]:
    """Top-sign coefficient and lower-degree dependency of one delta event."""

    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 1:
        raise ValueError("depth must be a positive integer")
    if isinstance(shift, bool) or not isinstance(shift, int) or not 0 <= shift <= depth:
        raise ValueError("shift must be an integer in [0,depth]")
    top_degree = 2 * depth + 1
    return {
        "depth": depth,
        "shift": shift,
        "event": (
            f"D_{top_degree}=0"
            if shift == 0
            else f"D_{top_degree}+D_{top_degree - 2 * shift}=0"
        ),
        "top_sign_sum": f"S_{top_degree}",
        "top_sign_coefficient": 1,
        "all_other_terms_use_degrees_below": top_degree,
        "parity_forced_zero": shift == depth,
        "s_zero_is_single_D": shift == 0,
    }


def irreducible_lower_bound_holds(q_value: int, depth: int) -> bool:
    """Exact integer check of I_q(r) >= 2q^r/(3r), r=2j+1."""

    if (
        isinstance(depth, bool)
        or not isinstance(depth, int)
        or not 1 <= depth <= MAX_REPLAY_J
    ):
        raise ValueError(f"depth must be an integer in [1,{MAX_REPLAY_J}]")
    degree = 2 * depth + 1
    count = irreducible_count(q_value, degree)
    return 3 * degree * count >= 2 * q_value**degree


def simple_delta_squared_majorant(q_value: int, depth: int) -> Fraction:
    """Square of sqrt(3r/2) q^(-r/2), an upper bound for delta."""

    _validate_q(q_value)
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 1:
        raise ValueError("depth must be a positive integer")
    degree = 2 * depth + 1
    return Fraction(3 * degree, 2 * q_value**degree)


def run() -> dict[str, object]:
    if not all(
        wallis_induction_bound_holds(index)
        for index in range(MAX_CENTRAL_COUNT // 2 + 1)
    ):
        raise ArithmeticError("central-binomial induction bound failed")
    if not all(
        central_atom_bound_holds(count) for count in range(1, MAX_CENTRAL_COUNT + 1)
    ):
        raise ArithmeticError("Rademacher max-atom bound failed")

    irreducible_checks = []
    for q_value in REPLAY_Q_VALUES:
        for depth in range(1, MAX_REPLAY_J + 1):
            if not irreducible_lower_bound_holds(q_value, depth):
                raise ArithmeticError("irreducible-count lower bound failed")
        irreducible_checks.append(
            {
                "q": q_value,
                "maximum_depth": MAX_REPLAY_J,
                "all_lower_bounds_hold": True,
            }
        )

    central_panels = []
    for q_value, depth in CENTRAL_PANELS:
        degree = 2 * depth + 1
        count = irreducible_count(q_value, degree)
        atom = central_rademacher_atom(count)
        central_panels.append(
            {
                "q": q_value,
                "depth": depth,
                "r": degree,
                "I_q(r)": count,
                "max_atom": str(atom),
                "N_times_max_atom_squared": str(count * atom * atom),
                "at_most_N^-1/2": central_atom_bound_holds(count),
            }
        )

    channel_panels = [
        channel_signature(depth, shift)
        for depth in CHANNEL_DEPTHS
        for shift in sorted({0, max(1, depth // 2), depth})
    ]

    return {
        "schema": "riemann.function_field.local_delta_tower_anticoncentration.v1",
        "status": (
            "exact conditional anti-concentration and absolutely summable "
            "fixed-depth coefficient tower"
        ),
        "frozen_sources": {
            f"{commit}:{path}": blob for (commit, path), blob in SOURCE_BLOBS.items()
        },
        "top_degree_isolation": {
            "r": "2j+1",
            "S_r": "sum_(deg P=r) epsilon_P",
            "D_r": "S_r+A_r(epsilon_P:deg P<r)",
            "s_zero_event": "D_r=0, not a doubled random variable",
            "positive_shift_event": ("D_r+D_(r-2s)=S_r+B_(r,s)(lower-degree signs)"),
            "top_sign_coefficient": 1,
            "conditional_bound": "delta_(j,s,q)<=max_x Prob(S_r=x)",
            "terminal_parity": "delta_(j,j,q)=0",
        },
        "central_binomial_bound": {
            "exact_max_atom": "2^-N*binom(N,floor(N/2))",
            "wallis_bound": "binom(2m,m)/4^m<=(3m+1)^(-1/2)",
            "conclusion": "max_x Prob(S_N=x)<=N^(-1/2)",
            "counts_checked": MAX_CENTRAL_COUNT,
            "panels": central_panels,
        },
        "irreducible_count_bound": {
            "degree": "r=2j+1",
            "bound": "I_q(r)>=2q^r/(3r)",
            "delta_bound": "delta_(j,s,q)<=sqrt(3r/2)*q^(-r/2)",
            "fixed_q_form": "delta_(j,s,q)=O_q(sqrt(j)*q^-j), uniformly in s",
            "sum_over_s": "sum_(s=0)^j delta_(j,s,q)=O_q(j^(3/2)*q^-j)",
            "bounded_checks": irreducible_checks,
        },
        "coefficient_tower": {
            "M_minus_2": "O_q(sqrt(j)*q^-j)",
            "M_minus_3": "O_q(j^(3/2)*q^-j)",
            "absolute_summability": True,
        },
        "claim_boundary": {
            "sums_displayed_fixed_depth_coefficients": True,
            "sums_full_conductor_layers": False,
            "reason": (
                "O_(q,j)(M^-4) errors and the fixed-depth profile regime "
                "are not uniform when j grows with M"
            ),
            "individual_L_function_zero": False,
            "rh_or_grh": False,
            "external_priority_claim": False,
        },
        "bounded_replay": {
            "channel_panels": channel_panels,
            "maximum_central_count": MAX_CENTRAL_COUNT,
            "maximum_irreducible_depth": MAX_REPLAY_J,
            "q_values": list(REPLAY_Q_VALUES),
        },
        "resource_caps": {
            "maximum_central_count": MAX_CENTRAL_COUNT,
            "maximum_irreducible_depth": MAX_REPLAY_J,
            "polynomials_enumerated": 0,
            "irreducibles_enumerated": 0,
            "residue_classes_enumerated": 0,
            "finite_field_elements_enumerated": 0,
            "curves_enumerated": 0,
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
