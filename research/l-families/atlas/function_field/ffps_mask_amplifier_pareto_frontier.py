#!/usr/bin/env python3
"""Exact rational audit of the FFPS mask/sheaf amplifier Pareto frontier.

The module performs only constant-size integer and Fraction calculations.  It
does not enumerate a field, character family, conductor family, curve, or
L-function zero.
"""

from __future__ import annotations

import argparse
import json
import math
import subprocess
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md"
BASE_COMMIT = "6e4609dfe1b073f1eb58445fdd1d7164dbc450d6"

DEPENDENCY_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_CYCLIC_CHARACTER_MASKS.md": (
        "80a56f847a1d272c43e092164503ecdfdd4c4b5d"
    ),
    "research/l-families/atlas/function_field/FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md": (
        "9012f96b34a3ffe55b66282ba1e62bc02514b5c6"
    ),
    "research/l-families/atlas/function_field/FFPS_CYCLIC_CLOSURE_BUDGET.md": (
        "b576c8a114d7e502b9b474cfed0db7e4cf6e2475"
    ),
}

MAX_PRIMES = 8
MAX_PRIME = 10_000
MAX_EXACT_ROWS = 16
MAX_WALL_SECONDS = 3.0


def _pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _is_prime(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def _validate_primes(primes: tuple[int, ...]) -> tuple[int, ...]:
    if not primes or len(primes) > MAX_PRIMES:
        raise ValueError("prime panel size lies outside the declared cap")
    if len(set(primes)) != len(primes):
        raise ValueError("prime panel must contain distinct primes")
    for prime in primes:
        if (
            isinstance(prime, bool)
            or not isinstance(prime, int)
            or prime > MAX_PRIME
            or prime % 2 == 0
            or not _is_prime(prime)
        ):
            raise ValueError("panel entries must be capped odd primes")
    return primes


def panel_frontier(primes: tuple[int, ...]) -> dict[str, object]:
    """Return the exact continuous frontier for one local prime panel."""

    panel = _validate_primes(tuple(primes))
    dimensions = tuple((prime - 1) // 2 for prime in panel)
    native_size = math.prod(dimensions)
    constant_denominator = math.prod(value + 1 for value in dimensions)
    nonconstant_denominator = math.prod(panel)
    a_value = Fraction(constant_denominator, native_size)
    b_value = Fraction(nonconstant_denominator, native_size)

    result: dict[str, object] = {
        "primes": list(panel),
        "local_dimensions": list(dimensions),
        "N": native_size,
        "Q": constant_denominator,
        "P": nonconstant_denominator,
        "A": _pair(a_value),
        "B": _pair(b_value),
        "complete_leverage": _pair(1 / a_value),
        "available_order_divisor": math.gcd(*dimensions),
        "proper_continuous_improvement_exists": b_value > 2 * a_value,
    }
    if b_value > 2 * a_value:
        u_star = 1 - 2 * a_value / b_value
        rho_star = 1 / (1 + u_star)
        leverage_star = 4 * (b_value - a_value) / (b_value * b_value)
        result.update(
            {
                "u_star": _pair(u_star),
                "rho_star": _pair(rho_star),
                "leverage_star": _pair(leverage_star),
                "strict_improvement_u_endpoint": _pair(
                    (b_value - 2 * a_value) / a_value
                ),
                "unit_principal_cancellation_energy_at_u_star": _pair(1 / u_star),
            }
        )
    return result


def cyclic_design_point(
    primes: tuple[int, ...], order: int, retained_count: int
) -> dict[str, object]:
    """Return one exact feasible cyclic density and its joint costs."""

    panel = panel_frontier(tuple(primes))
    if isinstance(order, bool) or not isinstance(order, int) or order < 2:
        raise ValueError("character order must be an integer at least two")
    if (
        isinstance(retained_count, bool)
        or not isinstance(retained_count, int)
        or not 0 < retained_count < order
    ):
        raise ValueError("retained count must lie strictly between zero and order")
    if any(value % order for value in panel["local_dimensions"]):
        raise ValueError("character order must divide every quotient dimension")

    a_value = Fraction(*panel["A"])
    b_value = Fraction(*panel["B"])
    rho = Fraction(retained_count, order)
    selected_mass = (1 - rho) / rho
    leverage = 1 / (a_value * rho * rho + b_value * rho * (1 - rho))
    uncertainty_mode_lower_bound = (order + retained_count - 1) // retained_count - 1
    prime_order_mode_count = order - 1 if _is_prime(order) else None
    return {
        "primes": panel["primes"],
        "order": order,
        "retained_count": retained_count,
        "rho": _pair(rho),
        "u_selected_fourier_mass": _pair(selected_mass),
        "leverage": _pair(leverage),
        "unit_principal_minimum_cancellation_energy": _pair(1 / selected_mass),
        "uncertainty_nonconstant_mode_lower_bound": uncertainty_mode_lower_bound,
        "prime_order_exact_nonconstant_mode_count": prime_order_mode_count,
        "beats_complete_frame": leverage < Fraction(*panel["complete_leverage"]),
    }


def build_report() -> dict[str, object]:
    """Build the bounded exact report used by the focused tests."""

    rows = {
        "ternary_7_13": cyclic_design_point((7, 13), 3, 2),
        "quadratic_13_37": cyclic_design_point((13, 37), 2, 1),
        "ternary_13_37": cyclic_design_point((13, 37), 3, 2),
    }
    if len(rows) > MAX_EXACT_ROWS:
        raise RuntimeError("exact-row cap exceeded")
    return {
        "schema": "riemann.function_field.ffps_mask_amplifier_pareto_frontier.v1",
        "status": "EXACT_CYCLIC_PARETO_AND_FINITE_ANOMALY_CANCELLATION",
        "base_commit": BASE_COMMIT,
        "theorems": {
            "leverage_in_u": "L(u)=(1+u)^2/(A+B*u)",
            "selected_mass": "sum_{r=1}^{k-1}|gamma_r|^2=u=k/t-1",
            "continuous_optimum": "u_star=1-2*A/B; L_star=4*(B-A)/B^2",
            "pareto_interval": "0<=u<=u_star when B>2*A",
            "strict_improvement_interval": "0<u<(B-2*A)/A",
            "cancellation_energy": "min sum|H_r|^2=|P_0|^2/u",
            "uncertainty": "|S|*FourierSupport(1_S)>=k",
        },
        "panels": {
            "7_13": panel_frontier((7, 13)),
            "13_37": panel_frontier((13, 37)),
        },
        "design_points": rows,
        "resource_contract": {
            "prime_panels": 2,
            "design_rows": len(rows),
            "finite_fields_enumerated": 0,
            "characters_enumerated": 0,
            "conductors_enumerated": 0,
            "curves_enumerated": 0,
            "l_function_zeros_enumerated": 0,
        },
        "firewalls": [
            "The cancellation optimizer is finite amplitude algebra, not arithmetic realization.",
            "Fourier-label count is not a Betti-number or conductor theorem.",
            "No conductor-uniform CYSEL, individualization, RH, or GRH is proved.",
        ],
    }


def _check_dependency_blobs() -> None:
    for path, expected in DEPENDENCY_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{BASE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2.0,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"dependency blob mismatch: {path}")


def run_checks() -> dict[str, object]:
    """Fail closed unless every exact control and source lock agrees."""

    started = time.monotonic()
    report = build_report()
    _check_dependency_blobs()

    checks = {
        "7_13_u_star": ([5, 13], report["panels"]["7_13"]["u_star"]),
        "7_13_l_star": ([648, 1183], report["panels"]["7_13"]["leverage_star"]),
        "7_13_ternary_leverage": (
            [27, 49],
            report["design_points"]["ternary_7_13"]["leverage"],
        ),
        "13_37_u_star": ([215, 481], report["panels"]["13_37"]["u_star"]),
        "13_37_l_star": (
            [150336, 231361],
            report["panels"]["13_37"]["leverage_star"],
        ),
        "13_37_quadratic_leverage": (
            [216, 307],
            report["design_points"]["quadratic_13_37"]["leverage"],
        ),
        "13_37_ternary_leverage": (
            [54, 83],
            report["design_points"]["ternary_13_37"]["leverage"],
        ),
    }
    for label, (expected, actual) in checks.items():
        if actual != expected:
            raise RuntimeError(f"exact control failed: {label}")

    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "L(u)",
        "selected squared amplitude",
        "Fourier-label complexity",
        "individualize",
        "RH or GRH",
    ):
        if marker not in note:
            raise RuntimeError(f"note contract marker missing: {marker}")
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="run all fail-closed checks"
    )
    args = parser.parse_args()
    report = run_checks() if args.check else build_report()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
