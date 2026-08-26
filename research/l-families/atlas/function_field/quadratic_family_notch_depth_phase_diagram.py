#!/usr/bin/env python3
"""Exact replay for the odd-notch factor-depth phase diagram.

The theorem is symbolic.  This producer evaluates only rational recurrences
for the cycle-index majorant and integer index identities; it enumerates no
finite fields, irreducibles, polynomials, curves, or zeros.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "QUADRATIC_FAMILY_NOTCH_DEPTH_PHASE_DIAGRAM.md"

FROZEN_BASE = "6e4609dfe1b073f1eb58445fdd1d7164dbc450d6"
FIXED_DEPTH_COMMIT = "1205d4bed"
SOURCE_BLOBS = {
    (
        FROZEN_BASE,
        "research/l-families/atlas/function_field/QUADRATIC_FAMILY_CLOSED_PLACE_WEIGHT_NOTCH.md",
    ): "a1b8476ddd3cad6f63ff205392426ae9c2d0829c",
    (
        FIXED_DEPTH_COMMIT,
        "research/l-families/atlas/function_field/QUADRATIC_FAMILY_FIRST_BOUNDARY_TRACE_ZERO_DENSITY.md",
    ): "f2a6be22e720be40aa19abb3405c5c8bf6b2ec63",
}

MAX_REPLAY_D = 16
MAX_REPLAY_N = 96
MAX_RATIONAL_STATES = 1_600
MAX_WALL_SECONDS = 4.0


def _strict_integer(value: object, name: str, minimum: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{name} must be an integer at least {minimum}")
    return value


def rough_majorant_coefficients(d_value: int, max_degree: int) -> list[Fraction]:
    """Return c_(N,d) for exp(sum_(e>=d) u^e/e), using its recurrence."""

    d_value = _strict_integer(d_value, "d", 1)
    max_degree = _strict_integer(max_degree, "max_degree", 0)
    coefficients = [Fraction(0) for _ in range(max_degree + 1)]
    coefficients[0] = Fraction(1)
    for degree in range(1, max_degree + 1):
        if degree < d_value:
            continue
        coefficients[degree] = (
            sum(coefficients[degree - part] for part in range(d_value, degree + 1))
            / degree
        )
    return coefficients


def rough_majorant_certificate(d_value: int, max_degree: int) -> dict[str, object]:
    """Check the exact finite recurrence shadow of c_(N,d)<=1/d."""

    coefficients = rough_majorant_coefficients(d_value, max_degree)
    checked = coefficients[d_value:]
    failures = [
        degree
        for degree, value in enumerate(coefficients)
        if degree >= d_value and value > Fraction(1, d_value)
    ]
    largest = max(checked, default=Fraction(0))
    return {
        "d": d_value,
        "max_degree": max_degree,
        "states": len(coefficients),
        "largest_coefficient": str(largest),
        "upper_bound": str(Fraction(1, d_value)),
        "failures": failures,
        "recurrence": "N*c_(N,d)=sum_(e=d)^N c_(N-e,d)",
    }


def notch_layer_certificate(n_value: int, depth: int) -> dict[str, object]:
    """Return the exact d=h-j and exterior-index scan for one notch layer."""

    n_value = _strict_integer(n_value, "n", 2)
    depth = _strict_integer(depth, "depth", 0)
    h_value = n_value // 2
    d_value = h_value - depth
    if d_value < 1:
        raise ValueError("depth must leave a positive minimum factor degree")
    epsilon = n_value % 2
    top_index = n_value - 2 * d_value
    expected_index = 2 * depth + epsilon
    if top_index != expected_index:
        raise RuntimeError("depth-to-exterior index identity failed")
    indices = list(range(top_index, epsilon - 1, -2))
    return {
        "n": n_value,
        "M": 2 * n_value - 1,
        "h": h_value,
        "depth_j": depth,
        "minimum_degree_d": d_value,
        "epsilon": epsilon,
        "top_exterior_index": top_index,
        "all_residual_indices": indices,
        "exact_residual": (
            f"m_{d_value}*D_{top_index} + "
            f"sum_(ell=1)^{depth} a_({d_value}+ell)*"
            f"D_({top_index}-2ell)"
        ),
    }


def layer_set_bound_certificate(
    q_value: int, M_value: int, degrees: list[int]
) -> dict[str, object]:
    """Return the exact harmonic-square upper-bound ledger."""

    q_value = _strict_integer(q_value, "q", 2)
    M_value = _strict_integer(M_value, "M", 1)
    if not isinstance(degrees, list) or not degrees:
        raise ValueError("degrees must be a nonempty list")
    normalized = sorted(set(degrees))
    if any(
        isinstance(degree, bool)
        or not isinstance(degree, int)
        or degree < 1
        or 2 * degree > M_value
        for degree in normalized
    ):
        raise ValueError("each degree must be positive with M-d>=d")
    budget = sum((Fraction(1, degree * degree) for degree in normalized), Fraction())
    return {
        "q": q_value,
        "M": M_value,
        "degrees": normalized,
        "layer_count": len(normalized),
        "harmonic_square_budget": str(budget),
        "normalized_count_upper_bound": str(budget),
        "count_upper_bound_formula": f"{q_value}^{M_value}*({budget})",
        "minimum_degree": min(normalized),
        "coarse_budget": str(Fraction(len(normalized), min(normalized) ** 2)),
    }


def _check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2.0,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"source blob mismatch: {commit}:{path}")


def build_report() -> dict[str, object]:
    started = time.monotonic()
    recurrence_rows = [
        rough_majorant_certificate(d_value, MAX_REPLAY_N)
        for d_value in range(1, MAX_REPLAY_D + 1)
    ]
    rational_states = sum(row["states"] for row in recurrence_rows)
    if rational_states > MAX_RATIONAL_STATES:
        raise RuntimeError("rational-state cap exceeded")
    if any(row["failures"] for row in recurrence_rows):
        raise RuntimeError("rough-majorant finite replay failed")

    depth_rows = [
        notch_layer_certificate(n_value, depth)
        for n_value in range(4, 17)
        for depth in range(n_value // 2)
    ]
    for row in depth_rows:
        if row["top_exterior_index"] != 2 * row["depth_j"] + row["epsilon"]:
            raise RuntimeError("exterior-index replay failed")

    report = {
        "schema": "riemann.function_field.quadratic_notch_depth_phase_diagram.v1",
        "status": "EXACT_UNIFORM_LAYER_BOUND_AND_EXTERIOR_DEPTH_SCAN",
        "sources": [
            {"commit": commit, "path": path, "blob": blob}
            for (commit, path), blob in SOURCE_BLOBS.items()
        ],
        "exact_theorem": {
            "rough_polynomials": "R_q(N,d)<=q^N/d for N>=d",
            "exact_layer": "B_q(M,d)<=q^M/d^2",
            "arbitrary_layers": "sum_(d in E) B_q(M,d)<=q^M sum_(d in E)d^-2",
            "proportional_band": ("d>=alpha*M and W=o(M) implies o(q^M/M) members"),
            "scale_sensitive_band": ("W=o(d_min^2/M) implies o(q^M/M) members"),
            "top_channel": "d=h-j exposes D_(2j+epsilon)",
        },
        "finite_exact_replay": {
            "rough_majorant_rows": recurrence_rows,
            "depth_index_rows": len(depth_rows),
            "sample_band": layer_set_bound_certificate(3, 65, [9, 10, 11, 12]),
        },
        "resource_contract": {
            "rational_recurrence_states": rational_states,
            "maximum_rational_states": MAX_RATIONAL_STATES,
            "finite_fields_enumerated": 0,
            "irreducibles_enumerated": 0,
            "polynomials_enumerated": 0,
            "curves_enumerated": 0,
            "zeros_enumerated": 0,
        },
        "firewalls": [
            "The bound counts conductor factor-degree layers, not L-function zeros.",
            "It does not prove that any deeper layer contains a raw correlation zero.",
            "The exterior scan is a formal character decomposition, not a sign law.",
            "The rough-polynomial inequality is treated as known or folklore.",
            "No external novelty or priority is claimed.",
        ],
    }
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return report


def run_checks() -> dict[str, object]:
    _check_source_blobs()
    report = build_report()
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "B_q(M,d)\\le {q^M\\over d^2}",
        "harmonic-square budget",
        "D_{2j+\\varepsilon}",
        "macroscopic number",
        "do not count zeros",
        "known or folklore",
    ):
        if marker not in note:
            raise RuntimeError(f"note contract marker missing: {marker}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="run source and exact replay checks"
    )
    args = parser.parse_args()
    report = run_checks() if args.check else build_report()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
