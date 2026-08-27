#!/usr/bin/env python3
"""Bounded replay for the sharp rough single-harmonic RH normal form."""

from __future__ import annotations

import argparse
import cmath
import json
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

ROUGH_COMMIT = "d1af013130ae4004c629b916950e34545b0a65f1"
PHASE_COMMIT = "31c0e730ffe80683798d9cc830c26e9d451a8759"
SOURCE_BLOBS = {
    ROUGH_COMMIT: {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_PREFIX_TRUNCATED_ROUGH_RANKIN_FRONTIER.md"
        ): "fa63811afd3ecc23b2ea26089a7544f093023c4e",
        (
            "research/l-families/atlas/function_field/"
            "ffps_prefix_truncated_rough_rankin_frontier.py"
        ): "f004b2a418eba090899adb938337aff34cbb1ddb",
        (
            "research/l-families/atlas/function_field/"
            "ffps_prefix_truncated_rough_rankin_frontier.json"
        ): "ef899a0a37a25d56c94478943faa95894e27ff3d",
        "tests/test_ffps_prefix_truncated_rough_rankin_frontier.py": (
            "fb7f68fde6dbb0f75c498785e2d40b03ebfcb334"
        ),
    },
    PHASE_COMMIT: {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_SINGLE_HARMONIC_MAXIMAL_PHASE_TRANSPORT.md"
        ): "6c3b9487fe6bea2bc133c4d6283eb7e972797139",
        (
            "research/l-families/atlas/function_field/"
            "ffps_single_harmonic_maximal_phase_transport.py"
        ): "9662f1d429d4acf1c3e1b1f0968f163e5aa8eee9",
        (
            "research/l-families/atlas/function_field/"
            "ffps_single_harmonic_maximal_phase_transport.json"
        ): "8da26ca2b9ba3dc52b5620aeb5b02bcb44ffcca4",
        "tests/test_ffps_single_harmonic_maximal_phase_transport.py": (
            "23e7cbcbc7b25d1fb3e030ea26be8468ba594c4b"
        ),
    },
}

HORIZON = 840
ROUGH_BOUND = 13
FREQUENCY = 0.19
TOLERANCE = 3e-12


def check_source_contract() -> None:
    for commit, paths in SOURCE_BLOBS.items():
        for path, expected in paths.items():
            completed = subprocess.run(
                ["git", "rev-parse", f"{commit}:{path}"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=3,
            )
            if completed.stdout.strip() != expected:
                raise RuntimeError(f"source blob mismatch: {commit}:{path}")


def validate_positive_integer(value: int, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{label} must be a positive integer")


def primes_through(bound: int) -> tuple[int, ...]:
    validate_positive_integer(bound, "prime bound")
    primes: list[int] = []
    for candidate in range(2, bound + 1):
        if all(candidate % prime for prime in primes if prime * prime <= candidate):
            primes.append(candidate)
    return tuple(primes)


def mobius(value: int) -> int:
    validate_positive_integer(value, "Mobius argument")
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


def beta(value: int) -> int:
    validate_positive_integer(value, "beta argument")
    return mobius(value) - (mobius(value // 67) if value % 67 == 0 else 0)


def is_y_rough(value: int, bound: int) -> bool:
    validate_positive_integer(value, "roughness argument")
    return all(value % prime for prime in primes_through(bound))


def is_y_smooth(value: int, bound: int) -> bool:
    validate_positive_integer(value, "smoothness argument")
    remaining = value
    for prime in primes_through(bound):
        while remaining % prime == 0:
            remaining //= prime
    return remaining == 1


def squarefree_smooth_numbers(horizon: int, bound: int) -> tuple[int, ...]:
    return tuple(
        value
        for value in range(1, horizon + 1)
        if mobius(value) and is_y_smooth(value, bound)
    )


def smooth_numbers(horizon: int, bound: int) -> tuple[int, ...]:
    return tuple(value for value in range(1, horizon + 1) if is_y_smooth(value, bound))


def critical_phase(value: int, frequency: float) -> complex:
    validate_positive_integer(value, "critical phase argument")
    return value**-0.5 * cmath.exp(-1j * frequency * math.log(value))


def prefix(values: tuple[complex, ...]) -> tuple[complex, ...]:
    output = [0j]
    total = 0j
    for value in values:
        total += value
        output.append(total)
    return tuple(output)


def source_prefixes(
    horizon: int, bound: int, frequency: float
) -> dict[str, tuple[complex, ...]]:
    validate_positive_integer(horizon, "horizon")
    validate_positive_integer(bound, "roughness bound")
    ordinary = prefix(
        tuple(
            mobius(value) * critical_phase(value, frequency)
            for value in range(1, horizon + 1)
        )
    )
    rough = prefix(
        tuple(
            mobius(value) * critical_phase(value, frequency)
            if is_y_rough(value, bound)
            else 0j
            for value in range(1, horizon + 1)
        )
    )
    duplicate = prefix(
        tuple(
            beta(value) * critical_phase(value, frequency)
            for value in range(1, horizon + 1)
        )
    )
    return {"duplicate": duplicate, "ordinary": ordinary, "rough": rough}


def coefficient_masses(horizon: int, bound: int) -> tuple[float, float]:
    squarefree = squarefree_smooth_numbers(horizon, bound)
    smooth = smooth_numbers(horizon, bound)
    return (
        sum(value**-0.5 for value in squarefree),
        sum(value**-0.5 for value in smooth),
    )


def scale_identity_panel(
    horizon: int, bound: int, frequency: float
) -> dict[str, object]:
    rows = source_prefixes(horizon, bound, frequency)
    ordinary = rows["ordinary"]
    rough = rows["rough"]
    duplicate = rows["duplicate"]
    squarefree = squarefree_smooth_numbers(horizon, bound)
    smooth = smooth_numbers(horizon, bound)
    forward_errors: list[float] = []
    inverse_errors: list[float] = []
    duplicate_errors: list[float] = []
    duplicate_inverse_errors: list[float] = []
    for endpoint in range(1, horizon + 1):
        forward = sum(
            mobius(d) * critical_phase(d, frequency) * rough[endpoint // d]
            for d in squarefree
            if d <= endpoint
        )
        inverse = sum(
            critical_phase(d, frequency) * ordinary[endpoint // d]
            for d in smooth
            if d <= endpoint
        )
        duplicate_forward = ordinary[endpoint]
        if endpoint >= 67:
            duplicate_forward -= (
                critical_phase(67, frequency) * ordinary[endpoint // 67]
            )
        duplicate_inverse = 0j
        power = 1
        while power <= endpoint:
            duplicate_inverse += (
                critical_phase(power, frequency) * duplicate[endpoint // power]
            )
            power *= 67
        forward_errors.append(abs(forward - ordinary[endpoint]))
        inverse_errors.append(abs(inverse - rough[endpoint]))
        duplicate_errors.append(abs(duplicate_forward - duplicate[endpoint]))
        duplicate_inverse_errors.append(abs(duplicate_inverse - ordinary[endpoint]))
    errors = {
        "beta_forward": max(duplicate_errors),
        "beta_inverse": max(duplicate_inverse_errors),
        "rough_forward": max(forward_errors),
        "rough_inverse": max(inverse_errors),
    }
    if max(errors.values()) > TOLERANCE:
        raise ArithmeticError("finite scale identity exceeded tolerance")
    return {
        "errors": {key: render_float(value) for key, value in errors.items()},
        "frequency": render_float(frequency),
        "horizon": horizon,
        "rough_bound": bound,
    }


def phase_transport_panel(
    horizon: int, bound: int, frequency: float
) -> dict[str, object]:
    zero = source_prefixes(horizon, bound, 0.0)["rough"]
    twisted = source_prefixes(horizon, bound, frequency)["rough"]
    zero_max = max(abs(value) for value in zero[1:])
    twisted_max = max(abs(value) for value in twisted[1:])
    transport_cost = 1 + abs(frequency) * math.log(horizon)
    if twisted_max > transport_cost * zero_max + TOLERANCE:
        raise ArithmeticError("forward phase transport bound failed")
    if zero_max > transport_cost * twisted_max + TOLERANCE:
        raise ArithmeticError("reverse phase transport bound failed")

    multipliers = tuple(
        0j if value == 0 else cmath.exp(-1j * frequency * math.log(value))
        for value in range(horizon + 1)
    )
    forward_error = 0.0
    reverse_error = 0.0
    for endpoint in range(1, horizon + 1):
        forward = zero[endpoint] * multipliers[endpoint]
        reverse = twisted[endpoint] * multipliers[endpoint].conjugate()
        for value in range(1, endpoint):
            forward += zero[value] * (multipliers[value] - multipliers[value + 1])
            reverse += twisted[value] * (
                multipliers[value].conjugate() - multipliers[value + 1].conjugate()
            )
        forward_error = max(forward_error, abs(forward - twisted[endpoint]))
        reverse_error = max(reverse_error, abs(reverse - zero[endpoint]))
    if max(forward_error, reverse_error) > TOLERANCE:
        raise ArithmeticError("finite Abel reconstruction exceeded tolerance")
    return {
        "abel_forward_max_error": render_float(forward_error),
        "abel_reverse_max_error": render_float(reverse_error),
        "rough_twisted_max": render_float(twisted_max),
        "rough_zero_max": render_float(zero_max),
        "transport_cost": render_float(transport_cost),
        "two_sided_bound_verified": True,
    }


def partial_summation_panel(horizon: int, bound: int) -> dict[str, object]:
    zero = source_prefixes(horizon, bound, 0.0)["rough"]
    unweighted = [0]
    total = 0
    for value in range(1, horizon + 1):
        if is_y_rough(value, bound):
            total += mobius(value)
        unweighted.append(total)
    weighted_max = max(abs(value) for value in zero[1:])
    normalized_max = max(
        abs(unweighted[value]) / math.sqrt(value) for value in range(1, horizon + 1)
    )
    upper_cost = 1 + 0.5 * math.log(horizon)
    if normalized_max > 2 * weighted_max + TOLERANCE:
        raise ArithmeticError("normalized rough prefix exceeded Abel bound")
    if weighted_max > upper_cost * normalized_max + TOLERANCE:
        raise ArithmeticError("weighted rough prefix exceeded Abel bound")
    return {
        "normalization": "max_(N<=X)|Q_N|/sqrt(N)",
        "normalized_unweighted_max": render_float(normalized_max),
        "two_sided_bound": (
            "weighted_max/(1+log(X)/2)<=normalized_unweighted_max<=2*weighted_max"
        ),
        "verified": True,
        "weighted_zero_max": render_float(weighted_max),
    }


def composed_normal_form_panel(
    horizon: int, bound: int, frequency: float
) -> dict[str, object]:
    ordinary_zero = source_prefixes(horizon, bound, 0.0)["ordinary"]
    rough_twisted = source_prefixes(horizon, bound, frequency)["rough"]
    ordinary_max = max(abs(value) for value in ordinary_zero[1:])
    rough_max = max(abs(value) for value in rough_twisted[1:])
    squarefree_mass, smooth_mass = coefficient_masses(horizon, bound)
    transport_cost = 1 + abs(frequency) * math.log(horizon)
    lower = ordinary_max / (transport_cost * squarefree_mass)
    upper = transport_cost * smooth_mass * ordinary_max
    if not lower <= rough_max + TOLERANCE or not rough_max <= upper + TOLERANCE:
        raise ArithmeticError("composed normal-form comparison failed")
    return {
        "lower_bound": render_float(lower),
        "ordinary_zero_max": render_float(ordinary_max),
        "rough_twisted_max": render_float(rough_max),
        "smooth_mass": render_float(smooth_mass),
        "squarefree_mass": render_float(squarefree_mass),
        "upper_bound": render_float(upper),
        "verified": True,
    }


def render_float(value: float) -> str:
    return f"{value:.12g}"


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    return {
        "source_contract": {
            "commits": {
                "phase_transport": PHASE_COMMIT,
                "rough_frontier": ROUGH_COMMIT,
            },
            "git_blobs": SOURCE_BLOBS,
        },
        "theorem": {
            "cutoff_quantifier": (
                "choose y_X once at outer X and freeze it across every integer "
                "prefix 1<=N<=X"
            ),
            "range": ("y_X tends to infinity and limsup log(y_X)/log(log(X))<=2"),
            "raw_equivalences": (
                "RH iff rough weighted zero-frequency maximal prefix is X^o "
                "iff one fixed nonzero guarded harmonic is X^o"
            ),
            "weighted_equivalence": (
                "for fixed r>=1 and fixed nonzero h, RH iff "
                "w_(h,X)*rough_harmonic_max^2=X^o"
            ),
            "unweighted_equivalence": (
                "RH iff max_(N<=X)|sum_rough_(n<=N)mu(n)|/sqrt(N)=X^o"
            ),
        },
        "exact_comparisons": {
            "composed": (
                "M_zero_max/(H*C_sf)<=A_rough_harmonic_max<=H*C_sm*M_zero_max"
            ),
            "phase": ("A_rough_zero_max/H<=A_rough_harmonic_max<=H*A_rough_zero_max"),
            "rough_scale": ("A_rough_t_max/C_sm<=M_t_max<=C_sf*A_rough_t_max"),
            "unweighted": (
                "A_rough_zero_max/(1+log(X)/2)<=Q_normalized_max<=2*A_rough_zero_max"
            ),
        },
        "sharp_frontier": {
            "coefficient_mass_iff": (
                "C_sf,C_sm=X^o iff limsup log(y_X)/log(log(X))<=2"
            ),
            "fixed_A_beyond_two": (
                "for y_X=(log X)^A and fixed A>2, both positive masses are "
                "X^(1/2-1/A+o(1))"
            ),
            "scope": (
                "sharp for positive conditioning masses, not a no-go for signed "
                "cancellation or RH-equivalence beyond the frontier"
            ),
        },
        "kernel_weight": {
            "asymptotic": ("w_(h,X)~K_0^2*(2*pi*|h|)^(2r)*L_X^(-(2r+1))"),
            "fixed_h_and_r": True,
            "nonzero_h_required": True,
            "weight_and_inverse_are_subpower": True,
        },
        "scope_fences": {
            "dyadic_replacement_proved": False,
            "endpoint_only_proved": False,
            "moving_cutoff_inside_prefix_maximum": False,
            "moving_frequency_inside_prefix_maximum": False,
            "naive_unnormalized_moving_cutoff_mertens_equivalence": False,
            "rough_estimate_proved": False,
            "rh_or_grh_proved": False,
        },
        "bounded_replay": {
            "composed_normal_form": composed_normal_form_panel(
                HORIZON, ROUGH_BOUND, FREQUENCY
            ),
            "partial_summation": partial_summation_panel(HORIZON, ROUGH_BOUND),
            "phase_transport": phase_transport_panel(HORIZON, ROUGH_BOUND, FREQUENCY),
            "scale_identities": scale_identity_panel(HORIZON, ROUGH_BOUND, FREQUENCY),
        },
        "resource_caps": {
            "floating_point_tolerance": TOLERANCE,
            "integer_horizon": HORIZON,
            "largest_prime": ROUGH_BOUND,
            "large_matrices": 0,
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
