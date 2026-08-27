#!/usr/bin/env python3
"""Bounded replay for the prefix-truncated rough Rankin frontier."""

from __future__ import annotations

import argparse
import cmath
import json
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FROZEN_COMMIT = "1e0c42aaf3f35a90af52380a32bbf7d8da0d5be5"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_SMALL_PRIME_ROUGH_CRITICAL_LATTICE_PRECONDITIONER.md"
    ): "7f909b9a474ef3418ef79ecf98170c8bdc7f7f90",
    (
        "research/l-families/atlas/function_field/"
        "ffps_small_prime_rough_critical_lattice_preconditioner.py"
    ): "2c9b40bc95dd090682449124c2873af9bcfebdbf",
}
HORIZON = 840
ROUGH_BOUND = 13
FREQUENCY = 0.271


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
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        parity += 1
    return -1 if parity % 2 else 1


def beta(value: int) -> int:
    validate_positive_integer(value, "beta argument")
    return mobius(value) - (mobius(value // 67) if value % 67 == 0 else 0)


def is_y_smooth(value: int, bound: int) -> bool:
    validate_positive_integer(value, "smoothness argument")
    validate_positive_integer(bound, "smoothness bound")
    remaining = value
    for prime in primes_through(bound):
        while remaining % prime == 0:
            remaining //= prime
    return remaining == 1


def is_y_rough(value: int, bound: int) -> bool:
    validate_positive_integer(value, "roughness argument")
    validate_positive_integer(bound, "roughness bound")
    return all(value % prime for prime in primes_through(bound))


def squarefree_smooth_divisors(horizon: int, bound: int) -> tuple[int, ...]:
    return tuple(
        value
        for value in range(1, horizon + 1)
        if mobius(value) and is_y_smooth(value, bound)
    )


def smooth_numbers(horizon: int, bound: int) -> tuple[int, ...]:
    return tuple(value for value in range(1, horizon + 1) if is_y_smooth(value, bound))


def critical_power(value: int, frequency: float) -> complex:
    return cmath.exp(-(0.5 + 1j * frequency) * math.log(value))


def prefix(values: tuple[complex, ...]) -> tuple[complex, ...]:
    output = [0j]
    total = 0j
    for value in values:
        total += value
        output.append(total)
    return tuple(output)


def source_prefixes(horizon: int, bound: int, frequency: float) -> dict[str, object]:
    validate_positive_integer(horizon, "horizon")
    validate_positive_integer(bound, "roughness bound")
    ordinary = prefix(
        tuple(
            mobius(value) * critical_power(value, frequency)
            for value in range(1, horizon + 1)
        )
    )
    duplicate = prefix(
        tuple(
            beta(value) * critical_power(value, frequency)
            for value in range(1, horizon + 1)
        )
    )
    rough = prefix(
        tuple(
            mobius(value) * critical_power(value, frequency)
            if is_y_rough(value, bound)
            else 0j
            for value in range(1, horizon + 1)
        )
    )
    sf_values = squarefree_smooth_divisors(horizon, bound)
    sm_values = smooth_numbers(horizon, bound)
    forward_errors: list[float] = []
    inverse_errors: list[float] = []
    duplicate_errors: list[float] = []
    duplicate_inverse_errors: list[float] = []
    for endpoint in range(1, horizon + 1):
        forward = sum(
            mobius(d) * critical_power(d, frequency) * rough[endpoint // d]
            for d in sf_values
            if d <= endpoint
        )
        inverse = sum(
            critical_power(d, frequency) * ordinary[endpoint // d]
            for d in sm_values
            if d <= endpoint
        )
        duplicate_forward = ordinary[endpoint]
        if endpoint >= 67:
            duplicate_forward -= (
                critical_power(67, frequency) * ordinary[endpoint // 67]
            )
        duplicate_inverse = 0j
        power = 1
        while power <= endpoint:
            duplicate_inverse += (
                critical_power(power, frequency) * duplicate[endpoint // power]
            )
            power *= 67
        forward_errors.append(abs(forward - ordinary[endpoint]))
        inverse_errors.append(abs(inverse - rough[endpoint]))
        duplicate_errors.append(abs(duplicate_forward - duplicate[endpoint]))
        duplicate_inverse_errors.append(abs(duplicate_inverse - ordinary[endpoint]))
    return {
        "duplicate_inverse_max_error": max(duplicate_inverse_errors),
        "duplicate_max_error": max(duplicate_errors),
        "forward_max_error": max(forward_errors),
        "inverse_max_error": max(inverse_errors),
        "ordinary_endpoint": ordinary[-1],
        "rough_endpoint": rough[-1],
    }


def coefficient_masses(horizon: int, bound: int, sigma: float) -> dict[str, float]:
    validate_positive_integer(horizon, "horizon")
    if not 0 < sigma < 0.5:
        raise ValueError("Rankin sigma must lie strictly between zero and one half")
    primes = primes_through(bound)
    sf_values = squarefree_smooth_divisors(horizon, bound)
    sm_values = smooth_numbers(horizon, bound)
    sf_mass = sum(value**-0.5 for value in sf_values)
    sm_mass = sum(value**-0.5 for value in sm_values)
    exponent = 0.5 + sigma
    sf_rankin = horizon**sigma * math.prod(1 + prime**-exponent for prime in primes)
    sm_rankin = (
        horizon**sigma * math.prod(1 - prime**-exponent for prime in primes) ** -1
    )
    sf_complete = math.prod(1 + prime**-0.5 for prime in primes)
    sm_complete = math.prod(1 - prime**-0.5 for prime in primes) ** -1
    subset_size = math.floor(math.log(horizon) / math.log(bound))
    subset_size = min(subset_size, len(primes))
    squarefree_binomial_lower = math.comb(len(primes), subset_size) / math.sqrt(horizon)
    if sf_mass > sf_rankin * (1 + 1e-12) or sm_mass > sm_rankin * (1 + 1e-12):
        raise ArithmeticError("Rankin product failed to dominate a truncated mass")
    if sf_mass > sf_complete * (1 + 1e-12) or sm_mass > sm_complete * (1 + 1e-12):
        raise ArithmeticError(
            "complete Euler product failed to dominate a truncated mass"
        )
    if squarefree_binomial_lower > sf_mass * (1 + 1e-12):
        raise ArithmeticError("squarefree binomial lower bound exceeded the mass")
    return {
        "rankin_sigma": sigma,
        "smooth_complete_product": sm_complete,
        "smooth_rankin_bound": sm_rankin,
        "smooth_truncated_mass": sm_mass,
        "squarefree_complete_product": sf_complete,
        "squarefree_binomial_lower_bound": squarefree_binomial_lower,
        "squarefree_binomial_subset_size": float(subset_size),
        "squarefree_rankin_bound": sf_rankin,
        "squarefree_truncated_mass": sf_mass,
    }


def polylog_phase_panel(
    log_x: float, powers: tuple[float, ...]
) -> list[dict[str, float]]:
    if log_x <= math.e:
        raise ValueError("log X must exceed e")
    ell = math.log(log_x)
    log_ell = math.log(ell)
    rows: list[dict[str, float]] = []
    for power in powers:
        log_y = 2 * ell + power * log_ell
        eta = log_y - 2 * ell
        sigma = max(0.0, (eta / 2 + 2 * log_ell) / log_y)
        rows.append(
            {
                "B": power,
                "log_y_over_loglog_x": log_y / ell,
                "rankin_sigma": sigma,
                "sigma_log_x_over_log_x": sigma,
                "suppressed_prime_scale_over_log_x": math.exp((0.5 - sigma) * log_y)
                / log_x,
            }
        )
    return rows


def fixed_power_certificate(
    log_x: float, powers: tuple[float, ...]
) -> list[dict[str, float]]:
    ell = math.log(log_x)
    log_ell = math.log(ell)
    rows: list[dict[str, float]] = []
    for power in powers:
        if power <= 2:
            raise ValueError("fixed-power certificate requires A>2")
        sigma = 0.5 - 1 / power + 2 * log_ell / (power * ell)
        rows.append(
            {
                "A": power,
                "certificate_power": 0.5 - 1 / power,
                "rankin_sigma": sigma,
                "suppressed_prime_scale_over_log_x": math.exp(
                    (0.5 - sigma) * power * ell
                )
                / log_x,
            }
        )
    return rows


def _render_complex(value: complex) -> dict[str, str]:
    return {"imag": f"{value.imag:.12g}", "real": f"{value.real:.12g}"}


def _render_float(value: float) -> str:
    return f"{value:.12g}"


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    source = source_prefixes(HORIZON, ROUGH_BOUND, FREQUENCY)
    if (
        max(
            source["forward_max_error"],
            source["inverse_max_error"],
            source["duplicate_max_error"],
            source["duplicate_inverse_max_error"],
        )
        > 2e-12
    ):
        raise ArithmeticError("finite prefix identities exceeded tolerance")
    mass_rows = [
        {
            "X": horizon,
            "y": bound,
            **{
                key: _render_float(value)
                for key, value in coefficient_masses(horizon, bound, 0.11).items()
            },
        }
        for horizon, bound in ((60, 5), (120, 7), (420, 13), (840, 13))
    ]
    phase_rows = [
        {key: _render_float(value) for key, value in row.items()}
        for row in polylog_phase_panel(10**6, (-2.0, 2.0, 6.0))
    ]
    certificate_rows = [
        {key: _render_float(value) for key, value in row.items()}
        for row in fixed_power_certificate(10**6, (3.0, 4.0, 6.0))
    ]
    return {
        "source_contract": {
            "commit": FROZEN_COMMIT,
            "git_blobs": SOURCE_BLOBS,
        },
        "theorem": {
            "prefix_conditioning": (
                "replace complete Euler products by the exact d<=X squarefree-smooth "
                "and smooth coefficient masses"
            ),
            "rankin_range": (
                "both truncated masses are X^o if and only if y tends to infinity "
                "with log y <= (2+o(1))*log log X"
            ),
            "critical_lattice": (
                "through that range, maximal rough retained-lattice energy is "
                "RH-equivalent; no rough estimate is proved"
            ),
        },
        "finite_prefix_control": {
            "frequency": FREQUENCY,
            "horizon": HORIZON,
            "rough_bound": ROUGH_BOUND,
            "duplicate_inverse_max_error": _render_float(
                source["duplicate_inverse_max_error"]
            ),
            "duplicate_max_error": _render_float(source["duplicate_max_error"]),
            "forward_max_error": _render_float(source["forward_max_error"]),
            "inverse_max_error": _render_float(source["inverse_max_error"]),
            "ordinary_endpoint": _render_complex(source["ordinary_endpoint"]),
            "rough_endpoint": _render_complex(source["rough_endpoint"]),
        },
        "truncated_mass_control": mass_rows,
        "asymptotic_parameter_controls": {
            "fixed_polylog_B": phase_rows,
            "fixed_power_A": certificate_rows,
            "scope": (
                "finite rows illustrate the analytic choices only; the asymptotic "
                "theorem uses Rankin plus the labelled PNT bound"
            ),
        },
        "proof_ledger": {
            "finite_prefix_factorizations": "IMPORTED EXACT AND REPLAYED",
            "truncated_maximal_conditioning": "PROVED EXACT",
            "rankin_product_bounds": "PROVED EXACT",
            "polylog_exponent_two_frontier": (
                "PROVED SHARP BY RANKIN-PNT UPPER AND SQUAREFREE-BINOMIAL LOWER BOUNDS"
            ),
            "fixed_A_mass_exponent": "PROVED WITH MATCHING UPPER AND LOWER BOUNDS",
            "rough_critical_lattice_equivalence": "PROVED EQUIVALENT TO RH",
            "rough_source_estimate": "OPEN",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "integer_horizon": HORIZON,
            "largest_prime": ROUGH_BOUND,
            "moduli": 0,
            "l_functions": 0,
            "zeta_zeros": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = run(check_sources=not args.no_source_check)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.write:
        canonical.write_text(rendered, encoding="utf-8", newline="\n")
    elif args.check and canonical.read_text(encoding="utf-8") != rendered:
        raise SystemExit("canonical JSON fixture is stale")
    elif not args.check:
        print(rendered, end="")


if __name__ == "__main__":
    main()
