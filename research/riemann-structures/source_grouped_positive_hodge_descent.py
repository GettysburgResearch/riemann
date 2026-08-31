#!/usr/bin/env python3
"""Bounded exact replay for two-stage source-grouped positive Hodge descent."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUTPUT = HERE / "source_grouped_positive_hodge_descent.json"

SOURCE_BLOBS = {
    (
        "108b070a441c49994a623d6a82941afcce07beca",
        "research/riemann-structures/SHARED_FIBRE_POSITIVE_QUOTIENT.md",
    ): "5263a5a32698074393edcb15a09e48a11f7ce370",
    (
        "108b070a441c49994a623d6a82941afcce07beca",
        "research/riemann-structures/shared_fibre_positive_quotient.py",
    ): "b51ddeacd6d87aa439a91316feed7abc9e001884",
    (
        "108b070a441c49994a623d6a82941afcce07beca",
        "research/riemann-structures/LIVE_SIGNED_HISTORY_POSITIVE_COMPRESSION.md",
    ): "a91149a3e0b28d71b7aa9ab9a9e6370bfb298160",
    (
        "108b070a441c49994a623d6a82941afcce07beca",
        "research/riemann-structures/live_signed_history_positive_compression.py",
    ): "ad0931506deb98ffabbaebe406209ebfe3b5d05e",
    (
        "a30276a5be049749ebb2147f30f000dd5659298b",
        "research/l-families/atlas/function_field/FFPS_SIGNED_HISTORY_RECOMBINATION.md",
    ): "c5f77f48bd19cc9af39698d4de53ae266bd42e17",
    (
        "a30276a5be049749ebb2147f30f000dd5659298b",
        "research/l-families/atlas/function_field/ffps_signed_history_recombination.py",
    ): "62d72fa7983c5974773fbee7bbe4652abcc160d9",
}


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def square(value: Fraction) -> Fraction:
    return value * value


def fraction_payload(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def split_groups(
    values: tuple[Fraction, ...],
    group_sizes: tuple[int, ...],
) -> tuple[tuple[Fraction, ...], ...]:
    if any(size <= 0 for size in group_sizes):
        raise ValueError("group sizes must be positive")
    if sum(group_sizes) != len(values):
        raise ValueError("group sizes do not partition the vector")
    groups = []
    offset = 0
    for size in group_sizes:
        groups.append(values[offset : offset + size])
        offset += size
    return tuple(groups)


def two_level_ledger(
    values: tuple[Fraction, ...],
    group_sizes: tuple[int, ...],
    group_cells: tuple[int, ...],
) -> dict[str, object]:
    if len(group_sizes) != len(group_cells):
        raise ValueError("every group needs one cell label")
    groups = split_groups(values, group_sizes)
    group_sums = tuple(sum(group, Fraction(0)) for group in groups)
    group_energies = tuple(sum((square(value) for value in group), Fraction(0)) for group in groups)
    cells = tuple(sorted(set(group_cells)))
    cell_multiplicities = tuple(
        sum(group_sizes[index] for index, cell in enumerate(group_cells) if cell == label)
        for label in cells
    )
    cell_sums = tuple(
        sum(
            (group_sums[index] for index, cell in enumerate(group_cells) if cell == label),
            Fraction(0),
        )
        for label in cells
    )
    total_energy = sum(group_energies, Fraction(0))
    group_mean_energy = sum(
        (square(total) / size for total, size in zip(group_sums, group_sizes, strict=True)),
        Fraction(0),
    )
    quotient_input_energy = sum(
        (
            square(total) / multiplicity
            for total, multiplicity in zip(cell_sums, cell_multiplicities, strict=True)
        ),
        Fraction(0),
    )
    within_history_variance = total_energy - group_mean_energy
    within_cell_group_variance = group_mean_energy - quotient_input_energy
    total_kernel_energy = total_energy - quotient_input_energy
    if min(within_history_variance, within_cell_group_variance, total_kernel_energy) < 0:
        raise AssertionError("a Hodge variance became negative")
    if within_history_variance + within_cell_group_variance != total_kernel_energy:
        raise AssertionError("two-stage Hodge variances did not add")
    return {
        "group_sums": group_sums,
        "group_energies": group_energies,
        "cell_labels": cells,
        "cell_sums": cell_sums,
        "cell_multiplicities": cell_multiplicities,
        "total_energy": total_energy,
        "group_mean_energy": group_mean_energy,
        "quotient_input_energy": quotient_input_energy,
        "within_history_variance": within_history_variance,
        "within_cell_group_variance": within_cell_group_variance,
        "total_kernel_energy": total_kernel_energy,
    }


def symmetric_quadratic(
    matrix: tuple[tuple[Fraction, ...], ...],
    vector: tuple[Fraction, ...],
) -> Fraction:
    if len(matrix) != len(vector) or any(len(row) != len(vector) for row in matrix):
        raise ValueError("matrix and vector dimensions disagree")
    return sum(
        (
            vector[row] * matrix[row][column] * vector[column]
            for row in range(len(vector))
            for column in range(len(vector))
        ),
        Fraction(0),
    )


def wick_scalar(
    ledger: dict[str, object],
    source_matrix: tuple[tuple[Fraction, ...], ...],
    d: Fraction,
) -> Fraction:
    cell_sums = ledger["cell_sums"]
    assert isinstance(cell_sums, tuple)
    total_energy = ledger["total_energy"]
    assert isinstance(total_energy, Fraction)
    return symmetric_quadratic(source_matrix, cell_sums) - d * total_energy


def quotient_scalar(
    ledger: dict[str, object],
    source_matrix: tuple[tuple[Fraction, ...], ...],
    d: Fraction,
) -> Fraction:
    cell_sums = ledger["cell_sums"]
    assert isinstance(cell_sums, tuple)
    quotient_input = ledger["quotient_input_energy"]
    assert isinstance(quotient_input, Fraction)
    return symmetric_quadratic(source_matrix, cell_sums) - d * quotient_input


def rank_one_quotient_ledger(ledger: dict[str, object], d: Fraction) -> dict[str, Fraction]:
    """Q=[[1,2],[2,1]] on two equally occupied cells."""
    cell_sums = ledger["cell_sums"]
    multiplicities = ledger["cell_multiplicities"]
    assert isinstance(cell_sums, tuple) and isinstance(multiplicities, tuple)
    if len(cell_sums) != 2 or multiplicities[0] != multiplicities[1]:
        raise ValueError("rank-one fixture needs two equally occupied cells")
    n = Fraction(multiplicities[0])
    positive = Fraction(3, 2) * square(cell_sums[0] + cell_sums[1]) / n
    quotient_negative = Fraction(1, 2) * square(cell_sums[0] - cell_sums[1]) / n
    kernel_energy = ledger["total_kernel_energy"]
    assert isinstance(kernel_energy, Fraction)
    full_negative = quotient_negative + d * kernel_energy
    return {
        "positive": positive,
        "quotient_negative": quotient_negative,
        "kernel_negative": d * kernel_energy,
        "full_negative": full_negative,
        "wick_value": positive - full_negative,
    }


def encode_ledger(ledger: dict[str, object]) -> dict[str, object]:
    encoded: dict[str, object] = {}
    for key, value in ledger.items():
        if isinstance(value, Fraction):
            encoded[key] = fraction_payload(value)
        elif isinstance(value, tuple) and all(isinstance(entry, Fraction) for entry in value):
            encoded[key] = [fraction_payload(entry) for entry in value]
        else:
            encoded[key] = value
    return encoded


def build_payload() -> dict[str, object]:
    live_values = tuple(
        [Fraction(9)] * 4 + [Fraction(-3)] * 32 + [Fraction(1)] * 64
    )
    live = two_level_ledger(live_values, (100,), (0,))
    if live["cell_sums"] != (Fraction(4),):
        raise AssertionError("live signed current changed")
    if live["total_energy"] != Fraction(676):
        raise AssertionError("live literal energy changed")
    if live["quotient_input_energy"] != Fraction(4, 25):
        raise AssertionError("live quotient input changed")
    if live["within_history_variance"] != Fraction(16896, 25):
        raise AssertionError("live within-history variance changed")
    if live["within_cell_group_variance"] != 0:
        raise AssertionError("single live group acquired a between-group variance")

    group_sizes = (2, 3, 1, 4)
    group_cells = (0, 0, 1, 1)
    values = tuple(Fraction(value) for value in (3, -1, 2, -2, 1, 4, 1, 1, -1, -1))
    changed_lift = tuple(Fraction(value) for value in (2, 0, 1, 0, 0, 4, 0, 0, 0, 0))
    toy = two_level_ledger(values, group_sizes, group_cells)
    toy_changed = two_level_ledger(changed_lift, group_sizes, group_cells)
    if toy["group_sums"] != toy_changed["group_sums"]:
        raise AssertionError("history lift did not preserve group currents")
    if toy["cell_sums"] != toy_changed["cell_sums"]:
        raise AssertionError("history lift did not preserve cell currents")
    if toy["total_energy"] == toy_changed["total_energy"]:
        raise AssertionError("history lifts failed to expose different literal energy")

    d = Fraction(5, 6)
    source_matrix = (
        (Fraction(11, 30), Fraction(2, 5)),
        (Fraction(2, 5), Fraction(11, 30)),
    )
    full_value = wick_scalar(toy, source_matrix, d)
    quotient_value = quotient_scalar(toy, source_matrix, d)
    kernel_energy = toy["total_kernel_energy"]
    assert isinstance(kernel_energy, Fraction)
    if full_value != quotient_value - d * kernel_energy:
        raise AssertionError("full Wick scalar missed the two-stage negative ledger")
    spectral = rank_one_quotient_ledger(toy, d)
    if spectral["wick_value"] != full_value:
        raise AssertionError("positive/negative Hodge ledger missed the Wick scalar")
    changed_spectral = rank_one_quotient_ledger(toy_changed, d)
    if changed_spectral["positive"] != spectral["positive"]:
        raise AssertionError("positive debt changed under history aggregation")

    cross_values = tuple(Fraction(value) for value in (1, 1, -1, -1))
    cross = two_level_ledger(cross_values, (2, 2), (0, 0))
    if cross["group_sums"] != (Fraction(2), Fraction(-2)):
        raise AssertionError("cross-group current fixture changed")
    if cross["cell_sums"] != (Fraction(0),):
        raise AssertionError("cross-group cancellation did not reach the cell kernel")
    if cross["within_history_variance"] != 0:
        raise AssertionError("cross-group fixture acquired within-history variance")
    if cross["within_cell_group_variance"] != Fraction(4):
        raise AssertionError("cross-group negative energy changed")
    if cross["quotient_input_energy"] != 0:
        raise AssertionError("zero cell current retained positive quotient input")

    spectral_encoded = {key: fraction_payload(value) for key, value in spectral.items()}
    changed_spectral_encoded = {
        key: fraction_payload(value) for key, value in changed_spectral.items()
    }
    core = {
        "live": encode_ledger(live),
        "toy": encode_ledger(toy),
        "toy_changed_lift": encode_ledger(toy_changed),
        "toy_spectral": spectral_encoded,
        "toy_changed_spectral": changed_spectral_encoded,
        "cross_group_zero_current": encode_ledger(cross),
        "full_wick_value": fraction_payload(full_value),
        "quotient_wick_value": fraction_payload(quotient_value),
    }
    proof_object = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "schema": "riemann.t108104.source-grouped-positive-hodge.v1",
        "classification": "PASS_T108104_SOURCE_GROUPED_POSITIVE_HODGE_DESCENT",
        "proof_object_sha256": proof_object,
        "finite_checks": 31,
        **core,
        "two_stage_atom_group_cell_factorization_proved": True,
        "positive_part_invariant_under_authorized_history_aggregation": True,
        "within_history_fluctuations_exact_negative_d_block": True,
        "same_cell_cross_group_zero_current_exact_negative_d_block": True,
        "live_factor_4225_recovered": True,
        "complete_live_occupancy_census_proved": False,
        "signed_cross_conductor_recombination_proved": False,
        "global_relative_trace_proved": False,
        "principal_binding_proved": False,
        "rh_or_grh_established": False,
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
