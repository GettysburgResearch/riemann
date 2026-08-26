#!/usr/bin/env python3
"""Exact finite replay for the Sym12 Eisenstein one-Tate no-go.

The source inputs are the constituent tables in BFG Theorem 4.4 and
Shmakov Theorems 4.6.6--4.6.8, specialized to (lambda_1, lambda_2)=(12, 0).
This script checks only finite S_6-to-S_5 projection and virtual Tate
polynomials.  It does not realize an l-adic Galois action.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANONICAL = HERE / "genus2_sym12_eisenstein_one_tate_no_go.json"

Partition = tuple[int, ...]
Polynomial = dict[int, int]

V6 = (6,)
V51 = (5, 1)
V42 = (4, 2)
V411 = (4, 1, 1)
V33 = (3, 3)
V321 = (3, 2, 1)
V222 = (2, 2, 2)
V21111 = (2, 1, 1, 1, 1)
V111111 = (1, 1, 1, 1, 1, 1)

SELECTORS: dict[str, frozenset[Partition]] = {
    "natural_trivial": frozenset((V6, V51)),
    "outer_trivial": frozenset((V6, V222)),
    "natural_sign": frozenset((V111111, V21111)),
    "outer_sign": frozenset((V111111, V33)),
}

B_PRIME = (V51, V42, V321)
C_PRIME = (V6, V42, V222)
BOREL_B = (V42, V222, V321)
BOREL_C = (V6, V42, V51)


@dataclass(frozen=True)
class Term:
    degree: int
    tate_power: int
    multiplicity: int
    carriers: tuple[Partition, ...]
    source: str


# Shmakov's nonzero terms at (12,0).  His printed elliptic dimension table has
# (new level 4, new level 2 plus, new level 2 minus, level 1) dimensions
# (1,1,1,0) at weight 14 and (1,1,0,1) at weight 16.
SHMAKOV_TERMS = (
    Term(2, 0, 1, (V33, V411), "Siegel weight-14 level-4 new"),
    Term(2, 0, 2, (V42, V51, V321), "Siegel weight-14 level-2 new"),
    Term(3, 1, 1, (V411, V33), "Siegel weight-16 level-4 new"),
    Term(3, 1, 1, (V321,), "Siegel weight-16 level-2 common"),
    Term(3, 1, 1, (V42,), "Siegel weight-16 Fricke-positive extra"),
    Term(3, 1, 1, B_PRIME, "Siegel weight-16 level-1 old, first block"),
    Term(3, 1, 1, C_PRIME, "Siegel weight-16 level-1 old, second block"),
    Term(2, 0, 1, BOREL_B, "Borel degree 2"),
    Term(3, 1, 1, BOREL_C, "Borel degree 3"),
)

# BFG's expected m=0 continuation differs only in the Fricke-positive block:
# Theorem 4.4 assigns B' rather than Shmakov's V_[3,2,1] + V_[4,2].
BFG_EXPECTED_TERMS = (
    Term(2, 0, 1, (V33, V411), "weight-14 level-4 new"),
    Term(2, 0, 2, (V42, V51, V321), "weight-14 level-2 new"),
    Term(3, 1, 1, (V411, V33), "weight-16 level-4 new"),
    Term(3, 1, 1, B_PRIME, "weight-16 Fricke-positive level-2 B-prime"),
    Term(3, 1, 1, B_PRIME, "weight-16 level-1 old, first block"),
    Term(3, 1, 1, C_PRIME, "weight-16 level-1 old, second block"),
    Term(2, 0, 1, BOREL_B, "formal weight-2/Borel degree 2"),
    Term(3, 1, 1, BOREL_C, "formal weight-2/Borel degree 3"),
)


def partition_label(partition: Partition) -> str:
    return "[" + ",".join(str(part) for part in partition) + "]"


def project(terms: Iterable[Term], selector: frozenset[Partition]) -> Polynomial:
    result: defaultdict[int, int] = defaultdict(int)
    for term in terms:
        fixed = sum(carrier in selector for carrier in term.carriers)
        result[term.tate_power] += (-1) ** term.degree * term.multiplicity * fixed
    return dict(
        sorted(
            (power, coefficient) for power, coefficient in result.items() if coefficient
        )
    )


def subtract(left: Mapping[int, int], right: Mapping[int, int]) -> Polynomial:
    powers = set(left) | set(right)
    return {
        power: left.get(power, 0) - right.get(power, 0)
        for power in sorted(powers)
        if left.get(power, 0) != right.get(power, 0)
    }


def virtual_rank(polynomial: Mapping[int, int]) -> int:
    return sum(polynomial.values())


def polynomial_label(polynomial: Mapping[int, int]) -> str:
    if not polynomial:
        return "0"
    pieces: list[str] = []
    for power, coefficient in sorted(polynomial.items()):
        monomial = "1" if power == 0 else ("L" if power == 1 else f"L^{power}")
        magnitude = "" if abs(coefficient) == 1 and power else str(abs(coefficient))
        body = magnitude if power == 0 else f"{magnitude}{monomial}"
        if not pieces:
            pieces.append(body if coefficient > 0 else f"-{body}")
        else:
            pieces.append(("+" if coefficient > 0 else "-") + body)
    return "".join(pieces)


def build_packet() -> dict[str, object]:
    projections = {
        name: project(SHMAKOV_TERMS, selector) for name, selector in SELECTORS.items()
    }
    expected = project(BFG_EXPECTED_TERMS, SELECTORS["natural_trivial"])
    natural = projections["natural_trivial"]
    defect = subtract(natural, expected)

    shmakov_positive = (V321, V42)
    bfg_positive = B_PRIME
    missing = tuple(
        carrier for carrier in bfg_positive if carrier not in shmakov_positive
    )
    epsilon_zero_compatible = not defect
    alternative_selector_matches = any(
        projection == expected
        for name, projection in projections.items()
        if name != "natural_trivial"
    )

    assert natural == {0: 2, 1: -4}
    assert expected == {0: 2, 1: -5}
    assert defect == {1: 1}
    assert projections == {
        "natural_trivial": {0: 2, 1: -4},
        "outer_trivial": {0: 1, 1: -3},
        "natural_sign": {},
        "outer_sign": {0: 1, 1: -1},
    }
    assert missing == (V51,)
    assert V51 in SELECTORS["natural_trivial"]
    assert not epsilon_zero_compatible
    assert not alternative_selector_matches

    return {
        "packet": "GENUS2_SYM12_EISENSTEIN_ONE_TATE_NO_GO",
        "status": "EXACT_FINITE_PROJECTION_AND_SOURCE_GRADED_NO_GO",
        "resource_firewall": {
            "point_counts": 0,
            "largest_linear_algebra_problem": "none",
            "calculation": "nine finite constituent rows and four S5 selectors",
        },
        "source_dimensions": {
            "weight_14": {
                "level_4_new": 1,
                "level_2_new_plus": 1,
                "level_2_new_minus": 1,
                "level_1": 0,
            },
            "weight_16": {
                "level_4_new": 1,
                "level_2_new_plus": 1,
                "level_2_new_minus": 0,
                "level_1": 1,
            },
        },
        "shmakov_projection_by_selector": {
            name: {
                "selected_irreps": [
                    partition_label(partition)
                    for partition in sorted(selector, reverse=True)
                ],
                "polynomial": polynomial_label(projections[name]),
                "virtual_rank": virtual_rank(projections[name]),
            }
            for name, selector in SELECTORS.items()
        },
        "BFG_expected_marked_continuation": {
            "polynomial": polynomial_label(expected),
            "virtual_rank": virtual_rank(expected),
            "source_grade": "EXPECTED_NONREGULAR_CONTINUATION",
        },
        "exact_localization": {
            "Shmakov_Fricke_positive_carriers": [
                partition_label(partition) for partition in shmakov_positive
            ],
            "BFG_Fricke_positive_carriers": [
                partition_label(partition) for partition in bfg_positive
            ],
            "unique_difference": partition_label(missing[0]) + " tensor L",
            "natural_S5_fixed_dimension_of_unique_difference": 1,
            "epsilon_formal": polynomial_label(defect),
        },
        "no_go": {
            "epsilon_zero_compatible_with_displayed_Shmakov_terms": (
                epsilon_zero_compatible
            ),
            "outer_or_sign_selector_reaches_BFG_2_minus_5L": (
                alternative_selector_matches
            ),
            "rank_specialization_already_distinguishes_branches": True,
            "rank_difference_Shmakov_minus_BFG": virtual_rank(natural)
            - virtual_rank(expected),
        },
        "proof_grade": {
            "exact": (
                "Given the displayed constituent tables, projection gives 2-4L, "
                "all four convention totals, and a unique [5,1] tensor L difference."
            ),
            "source_supported_topological": (
                "Shmakov states the relevant cohomology formulas and says Euler "
                "characteristics are unaffected by the connecting-map assumptions."
            ),
            "source_caveated_galois": (
                "Shmakov separately says the thesis does not give a satisfactory full "
                "justification of the Galois action on Eisenstein cohomology."
            ),
            "open": (
                "Independently realize the unique Fricke-positive local block in compactly "
                "supported l-adic Eisenstein cohomology on the natural marked quotient."
            ),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="compare with the committed JSON packet"
    )
    args = parser.parse_args()
    payload = build_packet()
    if args.check:
        stored = json.loads(CANONICAL.read_text(encoding="utf-8"))
        if payload != stored:
            raise SystemExit("canonical packet mismatch")
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
