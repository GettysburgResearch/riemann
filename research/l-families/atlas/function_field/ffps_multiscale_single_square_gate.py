#!/usr/bin/env python3
"""Exact bounded replay for the multiscale FFPS single-square gate."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

MAX_TOTAL_RANK = 8
MAX_BANDS = 4
MAX_BRANCH_DEGREE = 64
ELIGIBLE_PAIRS = (
    (5, 13),
    (17, 29),
    (37, 41),
    (53, 61),
    (73, 89),
    (97, 101),
    (109, 113),
    (137, 149),
)


def _validate_ranks(ranks: tuple[int, ...]) -> int:
    if not ranks or len(ranks) > MAX_BANDS:
        raise ValueError("the replay needs between one and four bands")
    if any(
        isinstance(rank, bool) or not isinstance(rank, int) or rank < 1
        for rank in ranks
    ):
        raise ValueError("every band rank must be a positive integer")
    total_rank = sum(ranks)
    if total_rank > MAX_TOTAL_RANK:
        raise ValueError("total rank is outside the replay range")
    return total_rank


def mode_census(ranks: tuple[int, ...]) -> dict[str, int]:
    total_rank = _validate_ranks(ranks)
    band_sizes = tuple(2**rank for rank in ranks)
    quotient_size = 2**total_rank
    pure_modes = sum(size - 1 for size in band_sizes)
    mixed_modes = quotient_size - 1 - pure_modes
    return {
        "bands": len(ranks),
        "total_rank": total_rank,
        "quotient_size": quotient_size,
        "selected_modes": quotient_size - 1,
        "band_pure_modes": pure_modes,
        "cross_band_modes": mixed_modes,
    }


def block_leverage(left_norm: int, right_norm: int) -> Fraction:
    if left_norm < 5 or right_norm < 5:
        raise ValueError("the replay uses eligible residue cardinalities at least five")
    return Fraction(
        4 * (left_norm - 1) * (right_norm - 1),
        5 * left_norm * right_norm + left_norm + right_norm + 1,
    )


def conductor_budget(branch_degrees: tuple[int, ...]) -> dict[str, object]:
    if not branch_degrees or len(branch_degrees) > MAX_TOTAL_RANK:
        raise ValueError("branch-degree tuple is outside the replay range")
    if any(
        isinstance(degree, bool)
        or not isinstance(degree, int)
        or degree < 2
        or degree > MAX_BRANCH_DEGREE
        for degree in branch_degrees
    ):
        raise ValueError("every paired branch degree must lie between 2 and 64")

    rank = len(branch_degrees)
    quotient_size = 2**rank
    total_degree = sum(branch_degrees)
    direct_total = sum(
        sum(branch_degrees[index] for index in range(rank) if mask & (1 << index)) - 2
        for mask in range(1, quotient_size)
    )
    closed_total = 2 ** (rank - 1) * total_degree - 2 * (quotient_size - 1)
    if direct_total != closed_total:
        raise AssertionError("selected-mode conductor formula failed")
    return {
        "paired_branch_degrees": list(branch_degrees),
        "total_selected_place_degree": total_degree,
        "largest_paired_branch_degree": max(branch_degrees),
        "total_modewise_hc1": closed_total,
        "average_modewise_hc1": str(Fraction(closed_total, quotient_size - 1)),
        "closed_average_formula": "H*T/(2*(H-1))-2",
    }


def _band_masks(ranks: tuple[int, ...]) -> tuple[list[int], int]:
    offsets: list[int] = []
    offset = 0
    for rank in ranks:
        masks = 0
        for index in range(offset, offset + rank):
            masks |= 1 << index
        offsets.append(masks)
        offset += rank
    return offsets, offset


def walsh_witness(
    ranks: tuple[int, ...],
    principal: Fraction = Fraction(3, 2),
    mixed: Fraction = Fraction(5, 3),
) -> dict[str, object]:
    """Exhibit a Fourier direction invisible to every separately squared band."""

    census = mode_census(ranks)
    if len(ranks) < 2:
        raise ValueError("a cross-band witness needs at least two bands")
    band_masks, total_rank = _band_masks(ranks)
    quotient_size = 2**total_rank
    chosen_mask = (band_masks[0] & -band_masks[0]) | (band_masks[1] & -band_masks[1])

    def character(mask: int, point: int) -> int:
        return -1 if (mask & point).bit_count() % 2 else 1

    amplitudes = [
        (principal + mixed * character(chosen_mask, point)) / quotient_size
        for point in range(quotient_size)
    ]
    transforms = [
        sum(
            (
                character(mask, point) * amplitudes[point]
                for point in range(quotient_size)
            ),
            start=Fraction(0),
        )
        for mask in range(quotient_size)
    ]
    pure_masks = [
        mask
        for band_mask in band_masks
        for mask in range(1, quotient_size)
        if mask & ~band_mask == 0
    ]
    if transforms[0] != principal or transforms[chosen_mask] != mixed:
        raise AssertionError("Walsh witness normalization failed")
    if any(transforms[mask] for mask in pure_masks):
        raise AssertionError("a band-pure mode detected the mixed witness")
    if any(
        value for mask, value in enumerate(transforms) if mask not in (0, chosen_mask)
    ):
        raise AssertionError("Walsh witness has an unexpected Fourier mode")

    principal_energy = principal * principal
    mixed_energy = mixed * mixed
    joint_interferometer = principal_energy - Fraction(
        mixed_energy, census["selected_modes"]
    )
    return {
        **census,
        "principal_transform": str(principal),
        "chosen_cross_band_transform": str(mixed),
        "all_band_pure_transforms": "0",
        "every_separate_band_interferometer": str(principal_energy),
        "joint_interferometer": str(joint_interferometer),
        "joint_minus_separate": str(joint_interferometer - principal_energy),
    }


def multiscale_panel(
    ranks: tuple[int, ...], branch_degrees: tuple[int, ...]
) -> dict[str, object]:
    total_rank = _validate_ranks(ranks)
    if len(branch_degrees) != total_rank:
        raise ValueError("one paired branch degree is required per block")
    factors = [block_leverage(*ELIGIBLE_PAIRS[index]) for index in range(total_rank)]
    band_products: list[Fraction] = []
    offset = 0
    for rank in ranks:
        band_products.append(
            math.prod(factors[offset : offset + rank], start=Fraction(1))
        )
        offset += rank
    joint = math.prod(band_products, start=Fraction(1))
    return {
        "ranks": list(ranks),
        **mode_census(ranks),
        "band_leverages": [str(value) for value in band_products],
        "joint_single_square_leverage": str(joint),
        "joint_equals_product_of_band_leverages": joint
        == math.prod(band_products, start=Fraction(1)),
        "separate_square_product_degree": 2 * len(ranks),
        "quadratic_recovery_root": f"1/{len(ranks)}",
        "separate_square_leverage_after_root": "(product_j L_j)^(1/J), not product_j L_j",
        "conductor": conductor_budget(branch_degrees),
    }


def run() -> dict[str, object]:
    panels = [
        multiscale_panel((1, 1), (2, 4)),
        multiscale_panel((2, 2), (2, 3, 8, 13)),
        multiscale_panel((2, 2, 2), (2, 3, 5, 8, 13, 21)),
        multiscale_panel((2, 2, 2, 2), (2, 3, 5, 8, 13, 21, 34, 55)),
    ]
    witnesses = [walsh_witness(ranks) for ranks in ((1, 1), (2, 2), (2, 1, 2))]
    return {
        "single_square_theorem": {
            "sequential_pre_square_restriction": "1_A=product_j 1_(A_j)",
            "joint_quotient": "K=product_j C2^(r_j)=C2^R",
            "joint_leverage": "L=product_j L_j",
            "joint_interferometer": "|P|^2-(2^R-1)^-1 sum_(chi!=1)|H_chi|^2",
            "cross_band_modes": "2^R-1-sum_j(2^(r_j)-1)",
        },
        "separate_square_gate": {
            "product_degree": "2J",
            "return_to_quadratic_scale": "take a J-th root",
            "retained_leverage": "geometric mean (product_j L_j)^(1/J)",
            "lost_information": "all Fourier modes nonprincipal in at least two bands",
        },
        "varying_place_firewall": {
            "paired_degree_total": "T=sum_i(deg ell_i+deg rho_i)",
            "average_modewise_hc1": "2^R*T/(2*(2^R-1))-2",
            "order_statistic_import": "D_max>=n^(alpha/delta-o(1)) with high probability",
            "consequence": "average hc1>=D_max/2-2",
            "leverage": "<(4/5)^R=n^(-alpha*log(5/4)+o(1))",
            "unchanged_conductor_threshold": "theta<delta*log(5/4)",
        },
        "panels": panels,
        "mixed_mode_witnesses": witnesses,
        "resource_caps": {
            "maximum_total_rank": MAX_TOTAL_RANK,
            "maximum_bands": MAX_BANDS,
            "maximum_quotient_points": 2**MAX_TOTAL_RANK,
            "largest_mode_sum": 2**MAX_TOTAL_RANK - 1,
            "source_atoms_enumerated": 0,
            "closed_places_enumerated": 0,
            "curves_or_l_functions_enumerated": 0,
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
