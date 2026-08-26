#!/usr/bin/env python3
"""Bounded exact replay for the complete-beta atomic-variation firewall."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ANALYTIC_SOURCE_COMMIT = "3f10a6be2009f8e499b1bd421fd97b2095a82b06"
ADAPTER_CONTEXT_COMMIT = "a970a55a11adc3d30bd98be90be12055984056ef"
SOURCE_BLOBS = {
    ANALYTIC_SOURCE_COMMIT: {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_SIGNED_DIFFERENTIAL_ATOMIC_SHELL_FIREWALL.md"
        ): "8dff1025fd7d794497b71c2ba2920a51ff9095f2",
        (
            "research/l-families/atlas/function_field/"
            "FFPS_EXTRA_NOTCHED_MELLIN_LANDAU_CONSUMER.md"
        ): "4a9aaf8bef6150bf054d6b6d4a873379db091b14",
    },
    ADAPTER_CONTEXT_COMMIT: {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_MOLLIFIED_COMPLETE_SOURCE_ADAPTER.md"
        ): "73f2bc0aa968ce8f9a60ed51c8261951ed8525b8",
    },
}

Quadratic = tuple[Fraction, Fraction]


def check_source_blobs() -> None:
    for commit, rows in SOURCE_BLOBS.items():
        for path, expected in rows.items():
            completed = subprocess.run(
                ["git", "rev-parse", f"{commit}:{path}"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=2,
            )
            if completed.stdout.strip() != expected:
                raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def qadd(left: Quadratic, right: Quadratic) -> Quadratic:
    return left[0] + right[0], left[1] + right[1]


def qneg(value: Quadratic) -> Quadratic:
    return -value[0], -value[1]


def qdivsqrt2(value: Quadratic) -> Quadratic:
    """Return (a+b*sqrt(2))/sqrt(2)."""

    return value[1], value[0] / 2


def qmulsqrt2(value: Quadratic) -> Quadratic:
    """Return sqrt(2)*(a+b*sqrt(2))."""

    return 2 * value[1], value[0]


def qsign(value: Quadratic) -> int:
    """Return the exact sign of a+b*sqrt(2)."""

    a, b = value
    if a == 0:
        return (b > 0) - (b < 0)
    if b == 0 or (a > 0) == (b > 0):
        return (a > 0) - (a < 0)
    square_comparison = a * a - 2 * b * b
    if square_comparison == 0:
        raise ArithmeticError("nonzero rational coefficients represented sqrt(2)")
    sign_of_larger_rational_part = (square_comparison > 0) - (
        square_comparison < 0
    )
    return sign_of_larger_rational_part if a > 0 else -sign_of_larger_rational_part


def qstr(value: Quadratic) -> str:
    a, b = value
    if b == 0:
        return str(a)
    sign = "+" if b > 0 else "-"
    magnitude = abs(b)
    b_text = "sqrt(2)" if magnitude == 1 else f"{magnitude}*sqrt(2)"
    if a == 0:
        return b_text if b > 0 else f"-{b_text}"
    return f"{a}{sign}{b_text}"


def kernel_atomic_coefficients() -> list[Quadratic]:
    return [
        (Fraction(5), Fraction(0)),
        (Fraction(-10), Fraction(-10)),
        (Fraction(15), Fraction(20)),
        (Fraction(-20), Fraction(-10)),
        (Fraction(10), Fraction(0)),
    ]


def complete_beta_atomic_coefficients() -> list[Quadratic]:
    kernel = kernel_atomic_coefficients()
    effective: list[Quadratic] = []
    for index in range(6):
        current = kernel[index] if index < len(kernel) else (Fraction(0), Fraction(0))
        previous = (
            qdivsqrt2(kernel[index - 1]) if index > 0 else (Fraction(0), Fraction(0))
        )
        effective.append(qadd(current, qneg(previous)))
    return effective


def positive_and_negative_mass() -> tuple[Quadratic, Quadratic]:
    effective = complete_beta_atomic_coefficients()
    positive = (Fraction(0), Fraction(0))
    negative = (Fraction(0), Fraction(0))
    for value in effective:
        sign = qsign(value)
        if sign > 0:
            positive = qadd(positive, value)
        elif sign < 0:
            negative = qadd(negative, qneg(value))
    return positive, negative


def total_atomic_variation() -> Quadratic:
    positive, negative = positive_and_negative_mass()
    return qadd(positive, negative)


def complete_group_positions(odd_part: int) -> tuple[int, ...]:
    if (
        isinstance(odd_part, bool)
        or not isinstance(odd_part, int)
        or odd_part < 1
        or odd_part % 2 == 0
    ):
        raise ValueError("odd_part must be a positive odd integer")
    return tuple(odd_part * 2**layer for layer in range(6))


def complete_group_fits_horizon(odd_part: int, horizon: int) -> bool:
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 1:
        raise ValueError("horizon must be a positive integer")
    return complete_group_positions(odd_part)[-1] <= horizon


def mobius(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    value = n
    parity = 0
    prime = 2
    while prime * prime <= value:
        if value % prime == 0:
            value //= prime
            parity += 1
            if value % prime == 0:
                return 0
            while value % prime == 0:
                value //= prime
        prime += 1
    if value > 1:
        parity += 1
    return -1 if parity % 2 else 1


def beta(n: int) -> int:
    return mobius(n) - (mobius(n // 67) if n % 67 == 0 else 0)


def check_two_adic_source_relation(limit: int = 999) -> bool:
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise ValueError("limit must be a positive integer")
    for m in range(1, limit + 1, 2):
        if beta(2 * m) != -beta(m):
            return False
        if beta(4 * m) != 0:
            return False
    return True


def run() -> dict[str, object]:
    effective = complete_beta_atomic_coefficients()
    expected = [
        (Fraction(5), Fraction(0)),
        (Fraction(-10), Fraction(-25, 2)),
        (Fraction(25), Fraction(25)),
        (Fraction(-40), Fraction(-35, 2)),
        (Fraction(20), Fraction(10)),
        (Fraction(0), Fraction(-5)),
    ]
    if effective != expected:
        raise AssertionError("complete-beta atomic coefficients changed")
    positive, negative = positive_and_negative_mass()
    if positive != negative or positive != (Fraction(50), Fraction(35)):
        raise AssertionError("positive/negative atomic masses do not balance")
    total_variation = total_atomic_variation()
    if total_variation != (Fraction(100), Fraction(70)):
        raise AssertionError("complete-group atomic total variation changed")
    if not check_two_adic_source_relation():
        raise AssertionError("two-adic beta relation failed")

    position_owners: dict[int, tuple[int, int]] = {}
    odd_parts = range(1, 64, 2)
    for odd_part in odd_parts:
        for layer, position in enumerate(complete_group_positions(odd_part)):
            if position in position_owners:
                raise AssertionError("distinct two-adic groups collided")
            position_owners[position] = (odd_part, layer)
    if not complete_group_fits_horizon(31, 32 * 31):
        raise AssertionError("endpoint-inclusive horizon lost its final atom")
    if complete_group_fits_horizon(31, 32 * 31 - 1):
        raise AssertionError("incomplete atomic group passed the horizon fence")

    odd_squarefree_density = Fraction(4, 1)
    partial_sum_leading_coefficient = Fraction(8, 1)
    squarefree_lower_lead = qmulsqrt2(positive)
    return {
        "frozen_sources": SOURCE_BLOBS,
        "kernel_atomic_coefficients": [
            {"ratio": 2**index, "coefficient": qstr(value)}
            for index, value in enumerate(kernel_atomic_coefficients())
        ],
        "complete_beta_atomic_coefficients": [
            {"ratio": 2**index, "coefficient": qstr(value)}
            for index, value in enumerate(effective)
        ],
        "grouping_identity": "B(z)=C(z)*(1-z/sqrt(2))",
        "two_adic_source": {
            "beta_2m": "-beta_m for odd m",
            "beta_4m": "0 for odd m",
            "checked_odd_m_through": 999,
        },
        "atomic_mass_per_odd_source": {
            "positive": qstr(positive),
            "negative": qstr(negative),
            "total_variation": qstr(total_variation),
        },
        "complete_group_support": {
            "ratios": [2**layer for layer in range(6)],
            "largest_ratio": 32,
            "full_group_condition": "32*m<=Y",
            "endpoint_inclusive_sample": {
                "m": 31,
                "Y": 32 * 31,
                "fits": complete_group_fits_horizon(31, 32 * 31),
            },
        },
        "lower_bound": {
            "exact": ("(50+35*sqrt(2))*sum_{m<=Y/32,m odd}|beta(m)|/sqrt(m)"),
            "odd_squarefree_density": f"{odd_squarefree_density}/pi^2",
            "weighted_partial_sum_lead": (
                f"{partial_sum_leading_coefficient}/pi^2*sqrt(x)"
            ),
            "squarefree_subsum_lead_at_x=Y/32": (
                f"({qstr(squarefree_lower_lead)})/pi^2*sqrt(Y)"
            ),
            "growth": "Omega(sqrt(Y))",
        },
        "disposition": {
            "raw_complete_jordan_premise": "refuted",
            "raw_landau_implication": "logically true but arithmetically vacuous",
            "fixed_mollified_density_premise": "still analytically sufficient",
            "rh_proved": False,
            "grh_proved": False,
        },
        "resource_caps": {
            "two_adic_relation_checks": (999 + 1) // 2,
            "collision_free_group_positions_checked": len(position_owners),
            "source_families_enumerated": 0,
            "conductors_enumerated": 0,
            "curves_enumerated": 0,
            "point_counts": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
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
