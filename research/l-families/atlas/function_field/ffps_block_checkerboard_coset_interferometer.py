#!/usr/bin/env python3
"""Exact bounded replay for the block-checkerboard coset interferometer."""

from __future__ import annotations

import argparse
import ast
import json
import subprocess
import time
from collections import Counter
from fractions import Fraction
from itertools import product
from math import prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_BLOCK_CHECKERBOARD_COSET_INTERFEROMETER.md"

SOURCE_BLOBS = {
    (
        "12f52a2235cdcda5c3c6b43a82bfcadbbb08f73c",
        "research/l-families/atlas/function_field/FFPS_CORRELATED_MASK_AMPLIFIER.md",
    ): "4569c521e99e8c591f1694126605f8abee8a75f8",
    (
        "9e116ec41ecfee60d7e853bef6c9196053a2f206",
        "research/l-families/atlas/function_field/FFPS_FINITE_ABELIAN_SUBGROUP_MASK_COMPRESSION.md",
    ): "19d0ce572fcd70e68b1618462bea29a2958b7f9e",
    (
        "2e06d1561168fa2da94f0502661ae2d32a9ed101",
        "research/l-families/atlas/function_field/FFPS_GRAPH_KUMMER_CHARACTER_SPECTRUM.md",
    ): "a981ff9f50bc2b5e434f83a2023dd0b298a84e4a",
    (
        "cb45027c1114da2b66738fc44f9587bca738c600",
        "research/l-families/atlas/function_field/FFPS_CHECKERBOARD_TELESCOPING_CURVE_MODEL.md",
    ): "7d478fa212d39f9d222b05e1d94e266415e8d641",
}

MAX_PHASE_COORDINATES = 128
MAX_DIRECT_GRAM_CELLS = 4_096
MAX_QUOTIENT_ORDER = 64
MAX_SELECTED_GRAPH_MODES = 127
MAX_WALL_SECONDS = 3.0

Gaussian = tuple[int, int]
Blocks = tuple[tuple[int, ...], ...]


def is_prime(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def validate_panel(primes: tuple[int, ...], blocks: Blocks) -> None:
    if not primes or not blocks:
        raise ValueError("prime panel and block partition must be nonempty")
    if len(set(primes)) != len(primes):
        raise ValueError("phase primes must be distinct")
    if any(not is_prime(prime) or prime % 4 != 1 for prime in primes):
        raise ValueError("every phase prime must be prime and one modulo four")
    if any(not block for block in blocks):
        raise ValueError("blocks must be nonempty")
    flattened = tuple(index for block in blocks for index in block)
    if sorted(flattened) != list(range(len(primes))):
        raise ValueError("blocks must partition the phase-factor indices")
    if (1 << len(blocks)) > MAX_QUOTIENT_ORDER:
        raise RuntimeError("quotient-order cap exceeded")


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def block_panel(primes: tuple[int, ...], blocks: Blocks) -> dict[str, object]:
    validate_panel(primes, blocks)
    block_rows: list[dict[str, object]] = []
    for block in blocks:
        block_primes = tuple(primes[index] for index in block)
        amplitude = prod((prime - 1) // 2 for prime in block_primes)
        principal = prod((prime + 1) // 2 for prime in block_primes)
        top = prod(block_primes)
        leverage = Fraction(4 * amplitude, principal + top)
        block_rows.append(
            {
                "indices": list(block),
                "primes": list(block_primes),
                "M_j": amplitude,
                "Q_j": principal,
                "P_j": top,
                "block_leverage": fraction_text(leverage),
            }
        )

    block_count = len(blocks)
    quotient_order = 1 << block_count
    amplitude = prod(int(row["M_j"]) for row in block_rows)
    eigenvalue_numerator = prod(int(row["P_j"]) + int(row["Q_j"]) for row in block_rows)
    if eigenvalue_numerator % quotient_order:
        raise ArithmeticError("restricted constant eigenvalue is not integral")
    restricted_eigenvalue = eigenvalue_numerator // quotient_order
    if amplitude % quotient_order:
        raise ArithmeticError("checkerboard coset does not have integral size")
    coset_size = amplitude // quotient_order
    gram_energy = coset_size * restricted_eigenvalue
    leverage = Fraction(amplitude * amplitude, gram_energy)
    closed_leverage = Fraction((4**block_count) * amplitude, eigenvalue_numerator)
    full_leverage = Fraction(amplitude, prod(int(row["Q_j"]) for row in block_rows))
    product_leverage = prod(
        (Fraction(str(row["block_leverage"])) for row in block_rows),
        start=Fraction(1),
    )
    if leverage != closed_leverage or leverage != product_leverage:
        raise ArithmeticError("block leverage factorization failed")

    return {
        "primes": list(primes),
        "blocks": [list(block) for block in blocks],
        "block_count_r": block_count,
        "quotient_order_h": quotient_order,
        "native_amplitude_M": amplitude,
        "coset_size": coset_size,
        "restricted_constant_eigenvalue": restricted_eigenvalue,
        "indicator_gram_energy": gram_energy,
        "sharp_uniform_weight": quotient_order,
        "sharp_hard_leverage": fraction_text(leverage),
        "complete_frame_leverage": fraction_text(full_leverage),
        "strictly_improves_complete_frame": leverage < full_leverage,
        "product_of_block_leverages": fraction_text(product_leverage),
        "block_rows": block_rows,
    }


def quotient_signature(coordinate: tuple[int, ...], blocks: Blocks) -> int:
    signature = 0
    for block_index, block in enumerate(blocks):
        parity = sum(coordinate[index] for index in block) % 2
        signature |= parity << block_index
    return signature


def gram_entry(
    left: tuple[int, ...], right: tuple[int, ...], primes: tuple[int, ...]
) -> int:
    return prod(
        prime - 1 if left[index] == right[index] else -1
        for index, prime in enumerate(primes)
    )


def direct_coset_gram_control(
    primes: tuple[int, ...], blocks: Blocks
) -> dict[str, int]:
    panel = block_panel(primes, blocks)
    local_sizes = tuple((prime - 1) // 2 for prime in primes)
    coordinate_count = prod(local_sizes)
    if coordinate_count > MAX_PHASE_COORDINATES:
        raise RuntimeError("phase-coordinate cap exceeded")
    coordinates = tuple(product(*(range(size) for size in local_sizes)))
    quotient_order = int(panel["quotient_order_h"])
    cosets: dict[int, list[tuple[int, ...]]] = {
        label: [] for label in range(quotient_order)
    }
    for coordinate in coordinates:
        cosets[quotient_signature(coordinate, blocks)].append(coordinate)

    cell_count = sum(len(coset) ** 2 for coset in cosets.values())
    if cell_count > MAX_DIRECT_GRAM_CELLS:
        raise RuntimeError("direct Gram-cell cap exceeded")
    expected_size = int(panel["coset_size"])
    expected_row_sum = int(panel["restricted_constant_eigenvalue"])
    for coset in cosets.values():
        if len(coset) != expected_size:
            raise ArithmeticError("quotient cosets are not equicardinal")
        row_sums = {
            sum(gram_entry(left, right, primes) for right in coset) for left in coset
        }
        if row_sums != {expected_row_sum}:
            raise ArithmeticError("direct restricted row sum failed")
    return {
        "phase_coordinates": coordinate_count,
        "cosets": quotient_order,
        "coset_size": expected_size,
        "direct_gram_cells": cell_count,
        "common_row_sum": expected_row_sum,
    }


def character(character: int, phase: int) -> int:
    return -1 if (character & phase).bit_count() % 2 else 1


def gaussian_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gaussian_scale(scalar: int, value: Gaussian) -> Gaussian:
    return scalar * value[0], scalar * value[1]


def gaussian_norm(value: Gaussian) -> int:
    return value[0] * value[0] + value[1] * value[1]


def gaussian_times_conjugate(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] + left[1] * right[1],
        left[1] * right[0] - left[0] * right[1],
    )


def gaussian_sum(values: list[Gaussian] | tuple[Gaussian, ...]) -> Gaussian:
    total = (0, 0)
    for value in values:
        total = gaussian_add(total, value)
    return total


def interferometer_control(
    block_count: int, atoms: tuple[tuple[int, Gaussian], ...]
) -> dict[str, object]:
    if block_count < 1:
        raise ValueError("block count must be positive")
    quotient_order = 1 << block_count
    if quotient_order > MAX_QUOTIENT_ORDER:
        raise RuntimeError("quotient-order cap exceeded")
    if any(phase < 0 or phase >= quotient_order for phase, _ in atoms):
        raise ValueError("atom phase lies outside the quotient")

    principal = gaussian_sum([value for _, value in atoms])
    modes: list[Gaussian] = []
    for chi in range(quotient_order):
        modes.append(
            gaussian_sum(
                [gaussian_scale(character(chi, phase), value) for phase, value in atoms]
            )
        )
    if modes[0] != principal:
        raise ArithmeticError("principal Fourier mode mismatch")

    observations: list[Gaussian] = []
    for label in range(quotient_order):
        observations.append(
            gaussian_scale(
                quotient_order,
                gaussian_sum([value for phase, value in atoms if phase == label]),
            )
        )
    if gaussian_sum(observations) != gaussian_scale(quotient_order, principal):
        raise ArithmeticError("normalized coset sum failed")
    for label, observation in enumerate(observations):
        reconstructed = gaussian_sum(
            [
                gaussian_scale(character(chi, label), modes[chi])
                for chi in range(quotient_order)
            ]
        )
        if reconstructed != observation:
            raise ArithmeticError("coset Fourier inversion failed")

    off_coset_numerator = (0, 0)
    for left in range(quotient_order):
        for right in range(quotient_order):
            if left != right:
                off_coset_numerator = gaussian_add(
                    off_coset_numerator,
                    gaussian_times_conjugate(observations[left], observations[right]),
                )
    if off_coset_numerator[1] != 0:
        raise ArithmeticError("ordered off-coset interferometer is not real")
    denominator = quotient_order * (quotient_order - 1)
    direct_value = Fraction(off_coset_numerator[0], denominator)
    selected_energy = sum(gaussian_norm(mode) for mode in modes[1:])
    fourier_value = Fraction(gaussian_norm(principal)) - Fraction(
        selected_energy, quotient_order - 1
    )
    if direct_value != fourier_value:
        raise ArithmeticError("off-coset Fourier identity failed")

    for left in range(quotient_order):
        for right in range(quotient_order):
            selected_kernel = sum(
                character(chi, left) * character(chi, right)
                for chi in range(1, quotient_order)
            )
            kernel = Fraction(1) - Fraction(selected_kernel, quotient_order - 1)
            expected = (
                Fraction(0)
                if left == right
                else Fraction(quotient_order, quotient_order - 1)
            )
            if kernel != expected:
                raise ArithmeticError("interferometer kernel control failed")

    atomic_diagonal = Fraction(
        sum(character(chi, 0) ** 2 for chi in range(1, quotient_order)),
        quotient_order - 1,
    )
    if atomic_diagonal != 1:
        raise ArithmeticError("averaged selected atomic diagonal is not one")
    return {
        "block_count_r": block_count,
        "quotient_order_h": quotient_order,
        "atoms": len(atoms),
        "principal_energy": gaussian_norm(principal),
        "total_selected_energy": selected_energy,
        "off_coset_zero_target": (quotient_order - 1) * gaussian_norm(principal),
        "interferometer": fraction_text(direct_value),
        "averaged_selected_atomic_diagonal": 1,
        "same_coset_kernel": 0,
        "different_coset_kernel": fraction_text(
            Fraction(quotient_order, quotient_order - 1)
        ),
    }


def gf2_rank(vectors: tuple[int, ...]) -> int:
    pivots: dict[int, int] = {}
    for original in vectors:
        value = original
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def path_block_control(lengths: tuple[int, ...], degree: int) -> dict[str, object]:
    if not lengths or any(
        not isinstance(length, int) or isinstance(length, bool) or length < 1
        for length in lengths
    ):
        raise ValueError("every path block must have positive edge length")
    if not isinstance(degree, int) or isinstance(degree, bool) or degree < 1:
        raise ValueError("closed-place degree must be positive")
    block_count = len(lengths)
    quotient_order = 1 << block_count
    if quotient_order - 1 > MAX_SELECTED_GRAPH_MODES:
        raise RuntimeError("selected graph-mode cap exceeded")

    edge_offset = 0
    vertex_offset = 0
    generator_boundaries: list[int] = []
    generator_edges: list[int] = []
    for length in lengths:
        edge_mask = ((1 << length) - 1) << edge_offset
        endpoint_boundary = (1 << vertex_offset) | (1 << (vertex_offset + length))
        generator_edges.append(edge_mask)
        generator_boundaries.append(endpoint_boundary)
        edge_offset += length
        vertex_offset += length + 1

    edge_count = sum(lengths)
    vertex_count = edge_count + block_count
    component_count = block_count
    cycle_dimension = edge_count - vertex_count + component_count
    boundary_rank = gf2_rank(tuple(generator_boundaries))
    if cycle_dimension != 0 or boundary_rank != block_count:
        raise ArithmeticError("path-block transversality failed")

    multiplicities: Counter[int] = Counter()
    hc1_sum = 0
    for selected in range(1, quotient_order):
        boundary = 0
        edge_mode = 0
        for index in range(block_count):
            if selected & (1 << index):
                boundary ^= generator_boundaries[index]
                edge_mode ^= generator_edges[index]
        if edge_mode == 0 or boundary == 0:
            raise ArithmeticError("nonzero selected path mode became invariant")
        branch_vertices = boundary.bit_count()
        expected_vertices = 2 * selected.bit_count()
        if branch_vertices != expected_vertices:
            raise ArithmeticError("endpoint-disjoint branch count failed")
        multiplicities[branch_vertices] += 1
        hc1_sum += degree * branch_vertices - 2

    selected_modes = quotient_order - 1
    average_hc1 = Fraction(hc1_sum, selected_modes)
    closed_average = Fraction(
        2 * degree * block_count * (1 << (block_count - 1)) - 2 * selected_modes,
        selected_modes,
    )
    if average_hc1 != closed_average:
        raise ArithmeticError("average maximal-extension Hc1 formula failed")
    common_open_hc1 = degree * vertex_count - 2
    average_puncture_tax = Fraction(common_open_hc1) - average_hc1

    return {
        "path_lengths": list(lengths),
        "closed_place_degree_e": degree,
        "block_count_r": block_count,
        "edge_count": edge_count,
        "vertex_count": vertex_count,
        "component_count": component_count,
        "ambient_cycle_dimension": cycle_dimension,
        "selected_boundary_rank": boundary_rank,
        "nonzero_invariant_selected_modes": 0,
        "selected_modes": selected_modes,
        "branch_vertex_multiplicities": {
            str(branch_vertices): count
            for branch_vertices, count in sorted(multiplicities.items())
        },
        "maximally_extended_hc1_sum": hc1_sum,
        "average_maximally_extended_hc1": fraction_text(average_hc1),
        "average_hc1_closed_form": fraction_text(closed_average),
        "average_hc1_asymptotic_main": f"{degree}*r-2",
        "average_hc1_exact_excess": fraction_text(
            Fraction(degree * block_count, selected_modes)
        ),
        "common_open_hc1_per_nontrivial_mode": common_open_hc1,
        "average_removable_puncture_tax": fraction_text(average_puncture_tax),
    }


def deterministic_atoms(block_count: int) -> tuple[tuple[int, Gaussian], ...]:
    quotient_order = 1 << block_count
    atoms: list[tuple[int, Gaussian]] = []
    for phase in range(quotient_order):
        atoms.append((phase, (phase + 1, 1 - 2 * phase)))
        if phase % 2 == 0:
            atoms.append((phase, (2 - phase, phase + 3)))
    return tuple(atoms)


def check_source_blobs() -> None:
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
    panel = block_panel((5, 13, 17), ((0, 1), (2,)))
    amplifying_panel = block_panel((5, 13, 17, 29), ((0, 1), (2, 3)))
    if not amplifying_panel["strictly_improves_complete_frame"]:
        raise ArithmeticError("formula amplification control failed")
    direct_gram = direct_coset_gram_control((5, 13, 17), ((0, 1), (2,)))

    interferometers = [
        interferometer_control(block_count, deterministic_atoms(block_count))
        for block_count in range(1, 6)
    ]
    single_atom = interferometer_control(4, ((0, (3, -2)),))
    if single_atom["interferometer"] != "0":
        raise ArithmeticError("single-atom cancellation control failed")

    graph_controls = [
        path_block_control(
            tuple((index % 3) + 1 for index in range(block_count)), degree=2
        )
        for block_count in range(1, 7)
    ]
    selected_modes = sum(int(row["selected_modes"]) for row in graph_controls)
    quotient_kernel_cells = sum(
        int(row["quotient_order_h"]) ** 2 for row in interferometers
    )
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return {
        "schema": "riemann.function_field.ffps_block_checkerboard_coset_interferometer.v1",
        "status": "EXACT_FORMAL_BLOCK_INTERFEROMETER_AND_TRANSVERSE_PATH_MODEL",
        "formal_block_panel": panel,
        "formal_amplifying_panel": amplifying_panel,
        "direct_gram_control": direct_gram,
        "interferometer_controls": interferometers,
        "single_atom_zero_control": single_atom,
        "path_block_controls": graph_controls,
        "resource_ledger": {
            "direct_gram_cells": direct_gram["direct_gram_cells"],
            "quotient_kernel_cells": quotient_kernel_cells,
            "selected_graph_modes": selected_modes,
            "phase_coordinate_cap": MAX_PHASE_COORDINATES,
            "direct_gram_cell_cap": MAX_DIRECT_GRAM_CELLS,
            "quotient_order_cap": MAX_QUOTIENT_ORDER,
            "selected_graph_mode_cap_per_control": MAX_SELECTED_GRAPH_MODES,
            "finite_fields_enumerated": 0,
            "polynomials_enumerated": 0,
            "curves_enumerated": 0,
            "l_function_zeros_enumerated": 0,
        },
        "open": [
            "one native source simultaneously realizing the block Gram and path torsors",
            "legal maximal extension across every cancelled source puncture",
            "varying-conductor estimates and principal-member individualization",
            "CYSEL, WCADD, WCKUM, RH, and GRH",
        ],
    }


def run_checks() -> dict[str, object]:
    check_source_blobs()
    report = build_report()
    note = NOTE_PATH.read_text(encoding="utf-8")
    normalized_note = " ".join(note.split())
    for marker in (
        "block-leverage factorization theorem",
        "off-coset interferometer",
        "averaged selected atomic diagonal",
        "Endpoint-disjoint path blocks",
        "maximal-extension firewall",
        "coupled candidate, not a native-source theorem",
        "No external novelty or priority claim",
    ):
        if marker not in normalized_note:
            raise RuntimeError(f"note contract marker missing: {marker}")
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    if any(isinstance(node, ast.Assert) for node in ast.walk(tree)):
        raise RuntimeError("producer must not rely on assert statements")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = run_checks() if args.check else build_report()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
