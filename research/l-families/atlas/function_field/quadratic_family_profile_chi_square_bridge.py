#!/usr/bin/env python3
"""Bounded replay for the odd-notch profile chi-square bridge."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FUNCTION_FIELD_PATH = "research/l-families/atlas/function_field"
SOURCE_COMMIT = "9f439e623ccafc12ffe4d434e511fd41a415c12f"
DISCREPANCY_CONSTANT = 614_400
MAX_FACTORS = 5
MAX_PROFILE_COUNT = 5_000
PROFILE_INPUTS = ((3, 8, 1), (3, 12, 2), (5, 9, 1), (5, 14, 2))
BRIDGE_INPUTS = ((3, 1_613, 3), (3, 14_681, 4), (5, 48_733, 3))

SOURCE_BLOBS = {
    (
        SOURCE_COMMIT,
        f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_LOGARITHMIC_DEPTH_ZERO_FIREWALL.md",
    ): "0aa9cd103cc48aaf56a64f45a3902cca63a2d3c5",
    (
        SOURCE_COMMIT,
        f"{FUNCTION_FIELD_PATH}/quadratic_family_logarithmic_depth_zero_firewall.py",
    ): "2e6eb61536833ef924ed703099a11de42126ea24",
    (
        SOURCE_COMMIT,
        f"{FUNCTION_FIELD_PATH}/quadratic_family_logarithmic_depth_zero_firewall.json",
    ): "b4d56f8184734018422c35e84ef8d87bdf886872",
    (
        SOURCE_COMMIT,
        "tests/test_quadratic_family_logarithmic_depth_zero_firewall.py",
    ): "9286c3944f9de377e9ebecf1d3fc8aa538dc935a",
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


def _is_prime_power(value: int) -> bool:
    """Return whether the already-validated odd value is a prime power."""

    candidate = 3
    while candidate * candidate <= value and value % candidate != 0:
        candidate += 2
    if candidate * candidate > value:
        return True
    remaining = value
    while remaining % candidate == 0:
        remaining //= candidate
    return remaining == 1


def _validate_q(q_value: int) -> None:
    if (
        isinstance(q_value, bool)
        or not isinstance(q_value, int)
        or q_value < 3
        or q_value % 2 == 0
        or not _is_prime_power(q_value)
    ):
        raise ValueError("q must be an odd prime power")


def _validate_h_depth(h_value: int, depth: int) -> None:
    if isinstance(h_value, bool) or not isinstance(h_value, int) or h_value < 2:
        raise ValueError("h must be an integer at least two")
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 1:
        raise ValueError("depth must be a positive integer")
    if h_value - depth <= 2 * depth + 1:
        raise ValueError("the bridge requires d=h-j>r=2j+1")


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


def degree_profiles(h_value: int, depth: int) -> tuple[tuple[int, ...], ...]:
    """Small bounded degree-profile replay; no polynomial enumeration."""

    _validate_h_depth(h_value, depth)
    total_degree = 4 * h_value + 1
    minimum_degree = h_value - depth
    profiles: list[tuple[int, ...]] = []

    def extend(prefix: tuple[int, ...], remaining: int, slots: int) -> None:
        if len(profiles) > MAX_PROFILE_COUNT:
            raise RuntimeError("profile replay exceeded its cap")
        if slots == 1:
            if remaining >= prefix[-1]:
                profiles.append((*prefix, remaining))
            return
        lower = prefix[-1]
        upper = remaining // slots
        for next_degree in range(lower, upper + 1):
            extend((*prefix, next_degree), remaining - next_degree, slots - 1)

    for factor_count in range(2, MAX_FACTORS + 1):
        extend(
            (minimum_degree,),
            total_degree - minimum_degree,
            factor_count - 1,
        )
    if len(profiles) > MAX_PROFILE_COUNT:
        raise RuntimeError("profile replay exceeded its cap")
    return tuple(profiles)


def profile_multiplicities(profile: tuple[int, ...]) -> Counter[int]:
    if not profile or any(
        isinstance(degree, bool) or not isinstance(degree, int) or degree < 1
        for degree in profile
    ):
        raise ValueError("profile must contain positive integer degrees")
    if tuple(sorted(profile)) != profile:
        raise ValueError("profile degrees must be nondecreasing")
    return Counter(profile)


def profile_conductor_count(q_value: int, profile: tuple[int, ...]) -> int:
    multiplicities = profile_multiplicities(profile)
    count = 1
    for degree, multiplicity in multiplicities.items():
        count *= math.comb(irreducible_count(q_value, degree), multiplicity)
    return count


def profile_lower_bound_holds(q_value: int, profile: tuple[int, ...]) -> bool:
    total_degree = sum(profile)
    count = profile_conductor_count(q_value, profile)
    denominator = 4**MAX_FACTORS * math.factorial(MAX_FACTORS) * total_degree**5
    return denominator * count >= q_value**total_degree


def integer_partitions(value: int) -> tuple[tuple[int, ...], ...]:
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 5:
        raise ValueError("partition value must be an integer in [1,5]")
    partitions: list[tuple[int, ...]] = []

    def extend(prefix: tuple[int, ...], remaining: int, maximum: int) -> None:
        if remaining == 0:
            partitions.append(prefix)
            return
        for part in range(min(maximum, remaining), 0, -1):
            extend((*prefix, part), remaining - part, part)

    extend((), value, value)
    return tuple(partitions)


def newton_elementary(power_sums: tuple[int, ...], order: int) -> Fraction:
    """Newton recurrence from p_1,...,p_order to e_order."""

    if isinstance(order, bool) or not isinstance(order, int) or order < 0:
        raise ValueError("order must be a nonnegative integer")
    if len(power_sums) < order:
        raise ValueError("not enough power sums")
    elementary = [Fraction(1)]
    for current in range(1, order + 1):
        numerator = sum(
            (-1) ** (part - 1) * elementary[current - part] * power_sums[part - 1]
            for part in range(1, current + 1)
        )
        elementary.append(numerator / current)
    return elementary[order]


def chi_square_gate(
    counts_by_profile: tuple[tuple[int, ...], ...],
    zero_sets: tuple[tuple[int, ...], ...],
    beta: Fraction,
) -> dict[str, object]:
    """Exact finite check of Z/T <= beta+sqrt(beta*D^2)."""

    if not counts_by_profile or len(counts_by_profile) != len(zero_sets):
        raise ValueError("profiles and zero sets must be nonempty and aligned")
    residue_count = len(counts_by_profile[0])
    if residue_count < 1 or any(len(row) != residue_count for row in counts_by_profile):
        raise ValueError("all residue rows must have the same positive length")
    if beta < 0 or beta > 1:
        raise ValueError("beta must lie in [0,1]")

    profile_totals = tuple(sum(row) for row in counts_by_profile)
    if any(total <= 0 for total in profile_totals):
        raise ValueError("each profile must have positive total mass")
    for indices in zero_sets:
        if len(set(indices)) != len(indices) or any(
            index < 0 or index >= residue_count for index in indices
        ):
            raise ValueError("zero-set indices are invalid")
        if Fraction(len(indices), residue_count) > beta:
            raise ValueError("a zero set exceeds the beta density")

    total = sum(profile_totals)
    discrepancy_squared = Fraction(0)
    zero_total = 0
    for row, profile_total, indices in zip(
        counts_by_profile, profile_totals, zero_sets, strict=True
    ):
        uniform = Fraction(profile_total, residue_count)
        squared_norm = sum((Fraction(value) - uniform) ** 2 for value in row)
        discrepancy_squared += (
            Fraction(residue_count, total * profile_total) * squared_norm
        )
        zero_total += sum(row[index] for index in indices)

    normalized_zero = Fraction(zero_total, total)
    excess = max(Fraction(0), normalized_zero - beta)
    return {
        "residue_count": residue_count,
        "profile_count": len(counts_by_profile),
        "T": total,
        "Z": zero_total,
        "beta": str(beta),
        "normalized_zero": str(normalized_zero),
        "D_squared": str(discrepancy_squared),
        "squared_gate_holds": excess * excess <= beta * discrepancy_squared,
    }


def bridge_parameters(q_value: int, h_value: int, depth: int) -> dict[str, object]:
    _validate_q(q_value)
    _validate_h_depth(h_value, depth)
    total_degree = 4 * h_value + 1
    minimum_degree = h_value - depth
    top_degree = 2 * depth + 1
    ell = modulus_degree(q_value, top_degree)
    exponent_gap = total_degree - ell - top_degree
    polynomial_side = 2 * DISCREPANCY_CONSTANT * total_degree**11 * (ell + 1) ** 10
    safe = exponent_gap >= 0 and q_value**exponent_gap >= polynomial_side
    return {
        "q": q_value,
        "h": h_value,
        "M": total_degree,
        "j": depth,
        "d": minimum_degree,
        "r": top_degree,
        "ell_r": ell,
        "M_minus_ell_minus_r": exponent_gap,
        "ell_at_most_M_over_2": 2 * ell <= total_degree,
        "near_wall_safe": safe,
        "beta_lower_bound": str(Fraction(top_degree, q_value**top_degree + top_degree)),
        "factor_count_bound": MAX_FACTORS,
    }


def run() -> dict[str, object]:
    profile_panels = []
    generated_profiles = 0
    for q_value, h_value, depth in PROFILE_INPUTS:
        profiles = degree_profiles(h_value, depth)
        generated_profiles += len(profiles)
        if not profiles or len(profiles) > 5 * (4 * h_value + 1) ** 4:
            raise ArithmeticError("profile-count bound failed")
        if any(len(profile) > MAX_FACTORS for profile in profiles):
            raise ArithmeticError("factor-count bound failed")
        if not all(profile_lower_bound_holds(q_value, profile) for profile in profiles):
            raise ArithmeticError("uniform profile lower bound failed")
        total_degree = 4 * h_value + 1
        minimum_degree = h_value - depth
        two_factor = (minimum_degree, total_degree - minimum_degree)
        two_factor_count = profile_conductor_count(q_value, two_factor)
        if two_factor_count * total_degree**2 < q_value**total_degree:
            raise ArithmeticError("two-factor total-layer lower bound failed")
        profile_panels.append(
            {
                "q": q_value,
                "h": h_value,
                "j": depth,
                "M": total_degree,
                "d": minimum_degree,
                "profile_count": len(profiles),
                "maximum_factor_count": max(map(len, profiles)),
                "all_profile_lower_bounds_hold": True,
                "two_factor_layer_lower_bound_holds": True,
            }
        )

    cycle_panels = []
    for multiplicity in range(1, MAX_FACTORS + 1):
        partitions = integer_partitions(multiplicity)
        if any(sum(partition) != multiplicity for partition in partitions):
            raise ArithmeticError("cycle partition lost total multiplicity")
        cycle_panels.append(
            {
                "multiplicity": multiplicity,
                "cycle_partitions": [list(partition) for partition in partitions],
                "all_cycle_lengths_sum_to_multiplicity": True,
                "principal_power_requires_cycle_length_at_least_two": True,
            }
        )

    bridge_panels = [
        bridge_parameters(q_value, h_value, depth)
        for q_value, h_value, depth in BRIDGE_INPUTS
    ]
    if not all(
        panel["ell_at_most_M_over_2"] and panel["near_wall_safe"]
        for panel in bridge_panels
    ):
        raise ArithmeticError("half-modulus bridge panels are not safe")

    toy_gate = chi_square_gate(
        ((3, 1, 0, 0), (0, 2, 1, 1)),
        ((0, 1), (2, 3)),
        Fraction(1, 2),
    )
    if not toy_gate["squared_gate_holds"]:
        raise ArithmeticError("finite chi-square gate failed")

    return {
        "schema": "riemann.function_field.profile_chi_square_bridge.v1",
        "status": (
            "exact profile-weighted chi-square gate and unconditional bridge "
            "under an explicit logarithmic-gap criterion below the residue entropy wall"
        ),
        "frozen_sources": {
            f"{commit}:{path}": blob for (commit, path), blob in SOURCE_BLOBS.items()
        },
        "exact_gate": {
            "D_squared": (
                "Phi/T*sum_lambda T_lambda^-1*sum_a|N_lambda(a)-T_lambda/Phi|^2"
            ),
            "parseval": (
                "D_squared=T^-1*sum_lambda T_lambda^-1*"
                "sum_(chi!=1)|sum_(Q in lambda)chi(Q)|^2"
            ),
            "zero_bound": "Z<=T*(beta_r+sqrt(beta_r)*D)",
            "sufficient_spectral_gate": "D_squared<=beta_r",
            "toy_exact_panel": toy_gate,
        },
        "profile_bounds": {
            "maximum_factors": MAX_FACTORS,
            "profile_count": "at most 5M^4",
            "nonempty_profile_lower_bound": "T_lambda>=q^M/(122880M^5)",
            "total_layer_lower_bound": "T>=q^M/M^2",
            "total_layer_upper_bound": "T<=q^M/d^2",
            "bounded_panels": profile_panels,
        },
        "newton_repeated_degrees": {
            "nonprincipal_power": ("|sum_(deg P=e)chi(P)^b|<=(ell_r+1)q^(e/2)/e"),
            "principal_power": ("b>=2 and I_q(e)<=q^e/e<=q^(be/2)/e"),
            "profile_fourier_bound": ("|Nhat_lambda(chi)|<=(ell_r+1)^5q^(M/2)"),
            "cycle_panels": cycle_panels,
        },
        "discrepancy_bound": {
            "constant": DISCREPANCY_CONSTANT,
            "formula": "D^2<=614400M^11(ell_r+1)^10q^(ell_r-M)",
            "beta_lower_bound": "beta_r>=r/(q^r+r)>=1/(2q^r)",
            "near_wall_safe_condition": ("q^(M-ell_r-r)>=1228800M^11(ell_r+1)^10"),
            "conclusion": "Z/q^M<=2beta_r/d^2",
            "half_modulus_corollary": (
                "ell_r<=M/2 is safe for all sufficiently large M"
            ),
            "bridge_panels": bridge_panels,
        },
        "entropy_fence": {
            "support_bound": ("Phi*sum_a p_lambda(a)^2-1>=Phi/|supp p_lambda|-1"),
            "depth_scale": "J=(1/2)log_q(M)+O_q(1)",
            "breaks_logarithmic_depth": False,
        },
        "claim_boundary": {
            "raw_detector_zeros": True,
            "individual_L_function_zero": False,
            "integer_rh_or_grh": False,
            "number_field_transfer": False,
            "external_priority_claim": False,
        },
        "resource_caps": {
            "maximum_factor_count": MAX_FACTORS,
            "maximum_profile_count_per_panel": MAX_PROFILE_COUNT,
            "profiles_generated": generated_profiles,
            "polynomials_enumerated": 0,
            "irreducibles_enumerated": 0,
            "residue_classes_enumerated": 0,
            "characters_enumerated": 0,
            "finite_field_elements_enumerated": 0,
            "conductors_enumerated": 0,
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
