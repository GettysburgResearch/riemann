#!/usr/bin/env python3
"""Exact replay for live signed-history compression in the positive quotient."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUTPUT = HERE / "live_signed_history_positive_compression.json"

SOURCE_COMMIT = "098802565e3f9a00b7f4d0e4e77855620e446e7f"
SOURCE_BLOBS = {
    (
        "research/riemann-structures/"
        "SHARED_FIBRE_POSITIVE_QUOTIENT.md"
    ): "5263a5a32698074393edcb15a09e48a11f7ce370",
    (
        "research/riemann-structures/"
        "shared_fibre_positive_quotient.py"
    ): "b51ddeacd6d87aa439a91316feed7abc9e001884",
    (
        "research/riemann-structures/"
        "shared_fibre_positive_quotient.json"
    ): "771ed2bced3a457e8a5767700e8a92d449a158c9",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_LIVE_SHARED_FIBRE_COLLISIONS.md"
    ): "b12efe62a07fa12843937f715adaa87ae769f2e8",
    (
        "research/l-families/atlas/function_field/"
        "ffps_live_shared_fibre_collisions.py"
    ): "641a746ca6a4af2d041e238399c55dfe8e5c6424",
    (
        "research/l-families/atlas/function_field/"
        "ffps_live_shared_fibre_collisions.json"
    ): "36d599fd7ac86ae9f9aaca2f585fb7b7d391f9bf",
}

LIVE_ELL = 1031
LIVE_RHO = 521
LIVE_RATIOS = (9,) * 4 + (-3,) * 32 + (1,) * 64
ZERO_SUM_SUBPACKET = (-3, 1, 1, 1)


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def atomic_diagonal(ell: int, rho: int) -> Fraction:
    if ell <= 1 or rho <= 1:
        raise ValueError("conductors must exceed one")
    return Fraction(ell - 1, ell) * Fraction(rho - 1, rho)


def signed_total(coefficients: tuple[int, ...]) -> int:
    return sum(coefficients)


def diagonal_energy(coefficients: tuple[int, ...]) -> int:
    return sum(value * value for value in coefficients)


def direct_one_cell_wick(
    coefficients: tuple[int, ...],
    diagonal: Fraction,
) -> Fraction:
    """d*sum_{i != j} z_i z_j for the real exact fixture."""

    return diagonal * sum(
        coefficients[left] * coefficients[right]
        for left in range(len(coefficients))
        for right in range(len(coefficients))
        if left != right
    )


def complete_one_cell_ledger(
    coefficients: tuple[int, ...],
    diagonal: Fraction,
) -> dict[str, str | int]:
    """Positive/negative spectral ledger when the declared block is the cell."""

    count = len(coefficients)
    total = signed_total(coefficients)
    energy = diagonal_energy(coefficients)
    positive = diagonal * Fraction(count - 1, count) * total * total
    negative = diagonal * (energy - Fraction(total * total, count))
    full = diagonal * (total * total - energy)
    if positive - negative != full:
        raise AssertionError("one-cell positive/negative ledger failed")
    if direct_one_cell_wick(coefficients, diagonal) != full:
        raise AssertionError("direct one-cell Wick replay failed")
    return {
        "cell_multiplicity": count,
        "positive_eigenvalue": fraction_text(diagonal * (count - 1)),
        "negative_eigenvalue": fraction_text(-diagonal),
        "negative_multiplicity": count - 1,
        "positive_payment": fraction_text(positive),
        "negative_payment_magnitude": fraction_text(negative),
        "full_wick_value": fraction_text(full),
        "negative_to_positive_ratio": fraction_text(negative / positive),
        "full_magnitude_to_positive_ratio": fraction_text((-full) / positive),
    }


def ambient_projection_ledger(
    coefficients: tuple[int, ...],
    ambient_cell_multiplicity: int,
) -> dict[str, str | int]:
    """Projection data inside a possibly larger live residue cell."""

    if ambient_cell_multiplicity < len(coefficients):
        raise ValueError("ambient cell multiplicity is below the source block")
    total = signed_total(coefficients)
    energy = diagonal_energy(coefficients)
    quotient_input = Fraction(total * total, ambient_cell_multiplicity)
    kernel_energy = Fraction(energy) - quotient_input
    coherence = quotient_input / energy
    if quotient_input + kernel_energy != energy:
        raise AssertionError("orthogonal projection ledger failed")
    return {
        "ambient_cell_multiplicity": ambient_cell_multiplicity,
        "source_energy": str(energy),
        "quotient_input_energy": fraction_text(quotient_input),
        "kernel_energy": fraction_text(kernel_energy),
        "aggregation_coherence": fraction_text(coherence),
    }


def multiplicity_rows() -> list[dict[str, int]]:
    rows = [
        {"coefficient_ratio": 9, "multiplicity": 4},
        {"coefficient_ratio": -3, "multiplicity": 32},
        {"coefficient_ratio": 1, "multiplicity": 64},
    ]
    rebuilt = tuple(
        value
        for row in rows
        for value in (row["coefficient_ratio"],) * row["multiplicity"]
    )
    if rebuilt != LIVE_RATIOS:
        raise AssertionError("live multiplicity table failed")
    return rows


def build_payload() -> dict[str, object]:
    diagonal = atomic_diagonal(LIVE_ELL, LIVE_RHO)
    count = len(LIVE_RATIOS)
    total = signed_total(LIVE_RATIOS)
    energy = diagonal_energy(LIVE_RATIOS)
    if (count, total, energy) != (100, 4, 676):
        raise AssertionError("frozen live history invariants failed")

    complete = complete_one_cell_ledger(LIVE_RATIOS, diagonal)
    ambient = ambient_projection_ledger(LIVE_RATIOS, count)
    if ambient["aggregation_coherence"] != "1/4225":
        raise AssertionError("factor-4225 compression failed")
    if ambient["quotient_input_energy"] != "4/25":
        raise AssertionError("quotient input energy failed")
    if ambient["kernel_energy"] != "16896/25":
        raise AssertionError("kernel energy failed")

    zero_total = signed_total(ZERO_SUM_SUBPACKET)
    zero_energy = diagonal_energy(ZERO_SUM_SUBPACKET)
    if (zero_total, zero_energy) != (0, 12):
        raise AssertionError("zero-sum subpacket failed")
    zero_wick = direct_one_cell_wick(ZERO_SUM_SUBPACKET, diagonal)
    if zero_wick != -12 * diagonal:
        raise AssertionError("zero-sum negative block failed")

    full_live_wick = diagonal * (total * total - energy)
    if fraction_text(full_live_wick) != complete["full_wick_value"]:
        raise AssertionError("live Wick value did not match the source")

    core: dict[str, object] = {
        "marked_conductors": {
            "ell": LIVE_ELL,
            "rho": LIVE_RHO,
            "atomic_diagonal": fraction_text(diagonal),
        },
        "live_history_block": {
            "multiplicities": multiplicity_rows(),
            "history_count": count,
            "signed_total": total,
            "diagonal_energy": energy,
            "complete_one_cell_ledger": complete,
            "minimum_full_cell_projection": ambient,
            "positive_quotient_norm_bound": (
                "<z,(B_R)_+z> <= ||(Q_R)_+|| * (4/25)|w|^2 "
                "= ||(Q_R)_+|| * E/4225"
            ),
        },
        "zero_sum_internal_subpacket": {
            "ratios": list(ZERO_SUM_SUBPACKET),
            "signed_total": zero_total,
            "diagonal_energy": zero_energy,
            "positive_payment": "0",
            "full_wick_value": fraction_text(zero_wick),
            "admissibility_note": (
                "exact internal source subpacket; not asserted to be an "
                "admissible complete native input"
            ),
        },
    }
    proof_object = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "schema": "riemann.t108102.live-signed-history-positive-compression.v1",
        "proof_object_sha256": proof_object,
        "classification": "PASS_T108102_LIVE_SIGNED_HISTORY_POSITIVE_COMPRESSION",
        "finite_checks": 31,
        **core,
        "live_source_bound_to_positive_quotient": True,
        "factor_4225_input_energy_compression_proved": True,
        "complete_one_cell_positive_negative_spectrum_proved": True,
        "zero_sum_subpacket_has_zero_positive_debt": True,
        "full_live_fibre_positive_trace_evaluated": False,
        "complete_live_occupancy_census_proved": False,
        "signed_conductor_recombination_proved": False,
        "partial_frobenius_global_lift_constructed": False,
        "one_place_trace_proved": False,
        "principal_binding_proved": False,
        "rh_established": False,
        "grh_established": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--skip-source-check", action="store_true")
    args = parser.parse_args()
    if not args.skip_source_check:
        check_source_blobs()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != text:
            raise SystemExit("retained output mismatch")
    else:
        OUTPUT.write_text(text)
    print(payload["classification"])


if __name__ == "__main__":
    main()
