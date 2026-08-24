#!/usr/bin/env python3
"""Small deterministic quadrature for the Haar sign of the USp(4) toy minor.

This is deliberately a discovery-only numerical companion to the exact range
and moment certificate.  It uses at most 1,376,256 two-dimensional cells, no
randomness, no numerical roots, and a five-second global wall guard.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path
from typing import Callable, Sequence


HERE = Path(__file__).resolve().parent
Q_SCAN_FIXTURE = HERE / "genus2_q_scan.json"
GRID_SIZES = (128, 256, 512)
PHASE_SHIFTS = (
    (Fraction(1, 2), Fraction(1, 2)),
    (Fraction(1, 4), Fraction(3, 4)),
    (Fraction(1, 8), Fraction(3, 8)),
    (Fraction(3, 4), Fraction(1, 4)),
)
MAX_TOTAL_CELLS = 1_400_000
MAX_WALL_SECONDS = 5.0
BOUNDARY_TOLERANCE = 1e-12
CONTROL_TOLERANCE = 1e-10


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _guard(clock: Callable[[], float], deadline: float) -> None:
    if clock() > deadline:
        raise TimeoutError("USp(4) sign quadrature exceeded its monotonic wall deadline")


def _phase_quadrature(
    grid_size: int,
    phase: tuple[Fraction, Fraction],
    *,
    clock: Callable[[], float],
    deadline: float,
) -> dict[str, object]:
    if grid_size not in GRID_SIZES:
        raise ValueError(f"grid size must be one of the frozen values {GRID_SIZES}")
    _guard(clock, deadline)
    phase_one, phase_two = (float(value) for value in phase)
    angles_one = [
        2.0 * math.pi * (index + phase_one) / grid_size
        for index in range(grid_size)
    ]
    angles_two = [
        2.0 * math.pi * (index + phase_two) / grid_size
        for index in range(grid_size)
    ]
    cos_one = [math.cos(angle) for angle in angles_one]
    sin_one = [math.sin(angle) for angle in angles_one]
    cos_two = [math.cos(angle) for angle in angles_two]
    sin_two = [math.sin(angle) for angle in angles_two]
    denominator_rows: list[float] = []
    negative_rows: list[float] = []
    boundary_rows: list[float] = []
    first_moment_rows: list[float] = []
    second_moment_rows: list[float] = []
    for row_index, (cos_theta, sin_theta) in enumerate(zip(cos_one, sin_one, strict=True)):
        if row_index % 16 == 0:
            _guard(clock, deadline)
        x = 2.0 * cos_theta
        row_denominator: list[float] = []
        row_negative: list[float] = []
        row_boundary: list[float] = []
        row_first: list[float] = []
        row_second: list[float] = []
        for cos_phi, sin_phi in zip(cos_two, sin_two, strict=True):
            cos_sum = cos_theta * cos_phi - sin_theta * sin_phi
            cos_difference = cos_theta * cos_phi + sin_theta * sin_phi
            weight = (
                (4.0 * sin_theta * sin_theta)
                * (4.0 * sin_phi * sin_phi)
                * max(0.0, 2.0 - 2.0 * cos_sum)
                * max(0.0, 2.0 - 2.0 * cos_difference)
            )
            y = 2.0 * cos_phi
            statistic = (x - y) ** 2 - 4.0 - x * x * y * y
            row_denominator.append(weight)
            row_negative.append(weight if statistic < -BOUNDARY_TOLERANCE else 0.0)
            row_boundary.append(weight if abs(statistic) <= BOUNDARY_TOLERANCE else 0.0)
            row_first.append(weight * statistic)
            row_second.append(weight * statistic * statistic)
        denominator_rows.append(math.fsum(row_denominator))
        negative_rows.append(math.fsum(row_negative))
        boundary_rows.append(math.fsum(row_boundary))
        first_moment_rows.append(math.fsum(row_first))
        second_moment_rows.append(math.fsum(row_second))
    denominator = math.fsum(denominator_rows)
    probability = math.fsum(negative_rows) / denominator
    boundary_weight = math.fsum(boundary_rows) / denominator
    density_average = denominator / (grid_size * grid_size)
    first_moment = math.fsum(first_moment_rows) / denominator
    second_moment = math.fsum(second_moment_rows) / denominator
    return {
        "phase": [
            f"{phase[0].numerator}/{phase[0].denominator}",
            f"{phase[1].numerator}/{phase[1].denominator}",
        ],
        "negative_probability_display": f"{probability:.12f}",
        "boundary_grid_weight_display": f"{boundary_weight:.12f}",
        "exact_moment_controls_pass": (
            abs(density_average - 8.0) < CONTROL_TOLERANCE
            and abs(first_moment + 1.0) < CONTROL_TOLERANCE
            and abs(second_moment - 3.0) < CONTROL_TOLERANCE
        ),
    }


def build_fixture(
    *,
    clock: Callable[[], float] = time.monotonic,
    maximum_wall_seconds: float = MAX_WALL_SECONDS,
) -> dict[str, object]:
    if maximum_wall_seconds <= 0 or maximum_wall_seconds > MAX_WALL_SECONDS:
        raise ValueError(f"wall limit must lie in (0,{MAX_WALL_SECONDS}]")
    total_cells = sum(
        grid_size * grid_size * len(PHASE_SHIFTS) for grid_size in GRID_SIZES
    )
    if total_cells > MAX_TOTAL_CELLS:
        raise ValueError("frozen quadrature exceeds its total cell cap")
    deadline = clock() + maximum_wall_seconds
    q_scan = json.loads(Q_SCAN_FIXTURE.read_text(encoding="utf-8"))
    claimed_payload_hash = q_scan["payload_sha256"]
    q_scan_payload = dict(q_scan)
    q_scan_payload.pop("payload_sha256")
    if claimed_payload_hash != _canonical_sha256(q_scan_payload):
        raise ValueError("bound genus-two q-scan payload hash mismatch")

    grid_rows: list[dict[str, object]] = []
    for grid_size in GRID_SIZES:
        phases = [
            _phase_quadrature(
                grid_size,
                phase,
                clock=clock,
                deadline=deadline,
            )
            for phase in PHASE_SHIFTS
        ]
        estimates = [float(row["negative_probability_display"]) for row in phases]
        grid_rows.append(
            {
                "grid_size": grid_size,
                "phase_count": len(phases),
                "cell_count": grid_size * grid_size * len(phases),
                "phase_estimates": phases,
                "phase_mean_display": f"{math.fsum(estimates) / len(estimates):.12f}",
                "phase_spread_display": f"{max(estimates) - min(estimates):.12f}",
            }
        )
    _guard(clock, deadline)
    final_estimate = float(grid_rows[-1]["phase_mean_display"])
    finite_comparisons: list[dict[str, object]] = []
    expected_q = (3, 5, 7)
    for expected, family in zip(expected_q, q_scan["families"], strict=True):
        q = int(family["q"])
        if q != expected:
            raise ValueError("bound q-scan families lost their frozen 3,5,7 order")
        negative = int(family["sign_counts"]["negative"])
        members = int(family["member_count"])
        finite_probability = Fraction(negative, members)
        finite_comparisons.append(
            {
                "q": q,
                "negative_count": negative,
                "member_count": members,
                "negative_proportion": [
                    finite_probability.numerator,
                    finite_probability.denominator,
                ],
                "negative_proportion_display": f"{float(finite_probability):.12f}",
                "quadrature_minus_finite_display": (
                    f"{final_estimate - float(finite_probability):.12f}"
                ),
            }
        )
    payload: dict[str, object] = {
        "schema": "riemann.atlas.function_field.usp4_sign_probability.v1",
        "status": "DISCOVERY_ONLY_NUMERICAL_QUADRATURE",
        "statistic": "F=(Tr U)^2-e_2(U)^2=(X-Y)^2-4-X^2*Y^2",
        "measure": {
            "domain": "full two-torus [0,2*pi)^2",
            "C2_positive_roots": [[2, 0], [0, 2], [1, 1], [1, -1]],
            "weyl_density": "product_{alpha>0}(2-2*cos(alpha dot theta))",
            "density_constant_term": 8,
        },
        "boundary_certificate": {
            "status": "PROVED_HAAR_MEASURE_ZERO",
            "statement": (
                "F=(X-Y)^2-4-X^2*Y^2 is a nonzero polynomial, so F=0 is an "
                "algebraic curve of two-dimensional Lebesgue measure zero; the USp(4) Weyl "
                "measure is absolutely continuous in the trace-coordinate square."
            ),
            "weak_convergence_consequence": (
                "Any proved weak convergence of the genus-two Frobenius class measures to Haar "
                "would imply convergence of the negative proportions because {F<0} is a Haar "
                "continuity set."
            ),
        },
        "resource_contract": {
            "grid_sizes": list(GRID_SIZES),
            "phase_shifts": [
                [
                    [phase[0].numerator, phase[0].denominator],
                    [phase[1].numerator, phase[1].denominator],
                ]
                for phase in PHASE_SHIFTS
            ],
            "total_cell_count": total_cells,
            "maximum_total_cells": MAX_TOTAL_CELLS,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "randomness": "NONE",
        },
        "q_scan_source_lock": {
            "path": "research/l-families/atlas/function_field/genus2_q_scan.json",
            "canonical_sha256": _canonical_sha256(q_scan),
            "payload_sha256": claimed_payload_hash,
        },
        "grid_refinement": grid_rows,
        "display_estimate": grid_rows[-1]["phase_mean_display"],
        "finite_comparisons": finite_comparisons,
        "interpretation": (
            "The shifted-grid calculation nominates a Haar negative mass near 0.738. The exact "
            "q=3,5,7 negative proportions rise toward it, but three fields and numerical "
            "quadrature do not prove convergence, a rate, or a limiting sign law."
        ),
        "firewall": (
            "The exact range, Haar moments, Haar-null boundary, and all-q 1/20 liminf floor are "
            "separate certified results. This display-only probability quadrature is not an "
            "interval proof and must not be used as a theorem or number-field transfer."
        ),
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        if json.loads(args.check.read_text(encoding="utf-8")) != fixture:
            raise SystemExit(f"USp(4) sign-probability fixture mismatch: {args.check}")
        print(f"OK: USp(4) sign-probability fixture matches {args.check}")
        return 0
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(
            json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        print(f"OK: wrote USp(4) sign-probability fixture {args.write}")
        return 0
    print(json.dumps(fixture, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
