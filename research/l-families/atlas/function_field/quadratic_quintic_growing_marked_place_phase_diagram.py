#!/usr/bin/env python3
"""Bounded replay for the growing marked-place character phase diagram."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

PANELS = ((101, 11), (101, 20), (101, 50), (101, 101), (1009, 31), (1009, 100))


def character_dimension(rank: int, index: int) -> int:
    """Dimension of the fundamental omega_index character of USp(2*rank)."""
    if rank < 1 or not 1 <= index <= rank:
        raise ValueError("require rank>=1 and 1<=index<=rank")
    lower = math.comb(2 * rank, index - 2) if index >= 2 else 0
    return math.comb(2 * rank, index) - lower


def stable_character_formula(mark_count: int) -> dict[str, object]:
    if mark_count < 11:
        raise ValueError("stable omega_5 formula requires at least 11 marks")
    rank = (mark_count - 1) // 2
    choose_two = mark_count * (mark_count + 1) // 2
    if mark_count % 2:
        return {
            "parity": "odd",
            "rank": rank,
            "formula": (
                "S_5,m=-q^(5/2)chi_omega5-m*q^(3/2)chi_omega3"
                "-binom(m+1,2)*q^(1/2)chi_omega1"
            ),
            "coefficients": {
                "omega_5": "-q^(5/2)",
                "omega_3": f"-{mark_count}*q^(3/2)",
                "omega_1": f"-{choose_two}*q^(1/2)",
            },
        }
    return {
        "parity": "even",
        "rank": rank,
        "formula": (
            "S_5,m=-q^(5/2)chi_omega5-q^2chi_omega4"
            "-m*q^(3/2)chi_omega3-m*q*chi_omega2"
            "-binom(m+1,2)*q^(1/2)chi_omega1-binom(m+1,2)"
        ),
        "coefficients": {
            "omega_5": "-q^(5/2)",
            "omega_4": "-q^2",
            "omega_3": f"-{mark_count}*q^(3/2)",
            "omega_2": f"-{mark_count}*q",
            "omega_1": f"-{choose_two}*q^(1/2)",
            "scalar": -choose_two,
        },
    }


def verify_stable_identity(mark_count: int, q: int, exterior: tuple[int, ...]) -> bool:
    """Check the stable decomposition after separating sqrt(q)-parity."""
    if len(exterior) != 5:
        raise ValueError("supply e_1 through e_5")
    e1, e2, e3, e4, e5 = exterior
    choose_two = mark_count * (mark_count + 1) // 2
    coefficient = choose_two - q * mark_count
    source_sqrt = -coefficient * e1 - q * (mark_count - q) * e3 - q * q * e5
    stable_sqrt = -q * q * (e5 - e3) - mark_count * q * (e3 - e1) - choose_two * e1
    if source_sqrt != stable_sqrt:
        return False
    if mark_count % 2:
        return True
    source_even = -coefficient - q * (mark_count - q) * e2 - q * q * e4
    stable_even = -q * q * (e4 - e2) - mark_count * q * (e2 - 1) - choose_two
    return source_even == stable_even


def normalized_envelope(q: int, mark_count: int) -> float:
    if q < 3 or q % 2 == 0 or not 11 <= mark_count <= q:
        raise ValueError("require odd q and 11<=m<=q")
    rank = (mark_count - 1) // 2
    choose_two = mark_count * (mark_count + 1) // 2
    numerator = q**2.5 * character_dimension(rank, 5)
    numerator += mark_count * q**1.5 * character_dimension(rank, 3)
    numerator += choose_two * q**0.5 * character_dimension(rank, 1)
    if mark_count % 2 == 0:
        numerator += q**2 * character_dimension(rank, 4)
        numerator += mark_count * q * character_dimension(rank, 2)
        numerator += choose_two
    family_size = q**4 * (q - 1)
    return min(1.0, numerator / family_size)


def panel(q: int, mark_count: int) -> dict[str, object]:
    envelope = normalized_envelope(q, mark_count)
    scale = mark_count / math.sqrt(q)
    return {
        "q": q,
        "mark_count": mark_count,
        "m_over_sqrt_q": f"{scale:.12f}",
        "normalized_character_envelope": f"{envelope:.12f}",
        "stable_formula": stable_character_formula(mark_count)["formula"],
        "full_aperture_exact_value": 0 if mark_count == q else None,
    }


def run() -> dict[str, object]:
    verification_rows = []
    exterior_rows = ((1, 3, -2, 5, 7), (4, -1, 6, 2, -3), (-2, 8, 1, -5, 9))
    for mark_count in range(11, 21):
        for q in (23, 29):
            for exterior in exterior_rows:
                verification_rows.append(
                    verify_stable_identity(mark_count, q, exterior)
                )
    return {
        "stable_selection_rules": {
            "odd_m_at_least_11": stable_character_formula(11)["formula"],
            "even_m_at_least_12": stable_character_formula(12)["formula"],
        },
        "growing_mark_phase": {
            "uniform_decay": "m=o(sqrt(q)) implies |S_(5,m)|/|H_5(q)|=o(1)",
            "envelope_scale": "O(min(1,m^5*q^(-5/2)))",
            "critical_scale": "m asymptotic to sqrt(q)",
            "full_aperture": (
                "m=q lies on the all-odd-exterior null stratum of y^2=x-x^q, "
                "so the exact correlation is zero"
            ),
        },
        "panels": [panel(q, mark_count) for q, mark_count in PANELS],
        "symbolic_verification": {
            "rows": len(verification_rows),
            "all_pass": all(verification_rows),
        },
        "firewalls": [
            "the character envelope is an upper bound, not an attained scale",
            "m and q must obey the rational-place feasibility m<=q",
            "the full-aperture zero is exceptional geometry, not generic cancellation",
            "no individual L-zero, RH, or GRH statement follows",
        ],
        "resource_caps": {
            "finite_fields_enumerated": 0,
            "curves_enumerated": 0,
            "symbolic_identity_rows": len(verification_rows),
            "floating_panels": len(PANELS),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
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
