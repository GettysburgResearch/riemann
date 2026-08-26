#!/usr/bin/env python3
"""Exact, tiny replay for the Sym12 outer-S6 convention gate.

The calculation is pure character theory for S_6.  It performs no point
counts and imports no computer-algebra package.
"""

from __future__ import annotations

import argparse
import json
import math
from collections.abc import Iterable
from functools import cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANONICAL = HERE / "genus2_sym12_outer_s6_convention_gate.json"

Partition = tuple[int, ...]


def partitions(n: int, largest: int | None = None) -> tuple[Partition, ...]:
    """Return the partitions of ``n`` in reverse lexicographic order."""

    if n == 0:
        return ((),)
    if largest is None or largest > n:
        largest = n
    rows: list[Partition] = []
    for first in range(largest, 0, -1):
        for tail in partitions(n - first, first):
            rows.append((first, *tail))
    return tuple(rows)


def partition_label(partition: Partition) -> str:
    return "[" + ",".join(str(part) for part in partition) + "]"


def transpose(partition: Partition) -> Partition:
    return tuple(
        sum(row >= column for row in partition) for column in range(1, partition[0] + 1)
    )


def hook_dimension(partition: Partition) -> int:
    hooks = 1
    conjugate = transpose(partition)
    for row, length in enumerate(partition, start=1):
        for column in range(1, length + 1):
            hooks *= length - column + conjugate[column - 1] - row + 1
    return math.factorial(sum(partition)) // hooks


def class_size(cycle_type: Partition) -> int:
    multiplicities: dict[int, int] = {}
    for part in cycle_type:
        multiplicities[part] = multiplicities.get(part, 0) + 1
    centralizer = 1
    for length, multiplicity in multiplicities.items():
        centralizer *= length**multiplicity * math.factorial(multiplicity)
    return math.factorial(sum(cycle_type)) // centralizer


def permutation_sign(cycle_type: Partition) -> int:
    return -1 if (sum(cycle_type) - len(cycle_type)) % 2 else 1


def _is_border_strip(outer: Partition, inner: Partition, size: int) -> tuple[bool, int]:
    padded_inner = inner + (0,) * (len(outer) - len(inner))
    cells = {
        (row, column)
        for row, outer_length in enumerate(outer, start=1)
        for column in range(padded_inner[row - 1] + 1, outer_length + 1)
    }
    if len(cells) != size:
        return False, 0
    pending = {next(iter(cells))}
    seen: set[tuple[int, int]] = set()
    while pending:
        cell = pending.pop()
        if cell in seen:
            continue
        seen.add(cell)
        row, column = cell
        pending.update(
            neighbour
            for neighbour in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            )
            if neighbour in cells and neighbour not in seen
        )
    if seen != cells:
        return False, 0
    for row, column in cells:
        if {
            (row, column),
            (row + 1, column),
            (row, column + 1),
            (row + 1, column + 1),
        }.issubset(cells):
            return False, 0
    height = len({row for row, _ in cells}) - 1
    return True, height


@cache
def character(partition: Partition, cycle_type: Partition) -> int:
    """Irreducible symmetric-group character by Murnaghan--Nakayama."""

    if not cycle_type:
        return int(not partition)
    strip_size = cycle_type[0]
    remainder_size = sum(partition) - strip_size
    total = 0
    for inner in partitions(remainder_size):
        if len(inner) > len(partition):
            continue
        padded_inner = inner + (0,) * (len(partition) - len(inner))
        if any(
            left > right for left, right in zip(padded_inner, partition, strict=True)
        ):
            continue
        valid, height = _is_border_strip(partition, inner, strip_size)
        if valid:
            total += (-1) ** height * character(inner, cycle_type[1:])
    return total


S6_CLASSES = partitions(6)
S6_IRREPS = partitions(6)

# The exceptional outer automorphism is determined on conjugacy classes by
# the displayed swaps.  The identity, [2,2,1,1], and [5,1] are fixed.
OUTER_CLASS: dict[Partition, Partition] = {
    (6,): (3, 2, 1),
    (5, 1): (5, 1),
    (4, 2): (4, 2),
    (4, 1, 1): (4, 1, 1),
    (3, 3): (3, 1, 1, 1),
    (3, 2, 1): (6,),
    (3, 1, 1, 1): (3, 3),
    (2, 2, 2): (2, 1, 1, 1, 1),
    (2, 2, 1, 1): (2, 2, 1, 1),
    (2, 1, 1, 1, 1): (2, 2, 2),
    (1, 1, 1, 1, 1, 1): (1, 1, 1, 1, 1, 1),
}


def outer_irrep_map() -> dict[Partition, Partition]:
    vectors = {
        partition: tuple(character(partition, cls) for cls in S6_CLASSES)
        for partition in S6_IRREPS
    }
    result: dict[Partition, Partition] = {}
    for partition in S6_IRREPS:
        pulled_back = tuple(
            character(partition, OUTER_CLASS[cls]) for cls in S6_CLASSES
        )
        matches = [
            candidate for candidate, vector in vectors.items() if vector == pulled_back
        ]
        if len(matches) != 1:
            raise ArithmeticError(
                "outer pullback did not identify a unique irreducible"
            )
        result[partition] = matches[0]
    return result


def embedded_s5_class(cycle_type: Partition) -> Partition:
    return tuple(sorted((*cycle_type, 1), reverse=True))


def fixed_multiplicity(
    partition: Partition, *, outer: bool = False, sign_twist: bool = False
) -> int:
    numerator = 0
    for s5_class in partitions(5):
        embedded = embedded_s5_class(s5_class)
        evaluated = OUTER_CLASS[embedded] if outer else embedded
        value = character(partition, evaluated)
        if sign_twist:
            value *= permutation_sign(evaluated)
        numerator += class_size(s5_class) * value
    quotient, remainder = divmod(numerator, math.factorial(5))
    if remainder:
        raise ArithmeticError("subgroup character average was not integral")
    return quotient


def selector(*, outer: bool = False, sign_twist: bool = False) -> list[str]:
    selected = []
    for partition in S6_IRREPS:
        multiplicity = fixed_multiplicity(partition, outer=outer, sign_twist=sign_twist)
        if multiplicity not in (0, 1):
            raise ArithmeticError("unexpected S5 fixed multiplicity")
        if multiplicity:
            selected.append(partition_label(partition))
    return selected


OFFICIAL_GENERAL_ROWS = (
    (3, 1, 1, 1),
    (2, 2, 2),
    (2, 2, 1, 1),
    (2, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1),
)


def projection_on_official_rows(*, outer: bool, sign_twist: bool) -> int:
    return sum(
        fixed_multiplicity(row, outer=outer, sign_twist=sign_twist)
        for row in OFFICIAL_GENERAL_ROWS
    )


def _label_map(mapping: dict[Partition, Partition]) -> dict[str, str]:
    return {
        partition_label(source): partition_label(target)
        for source, target in mapping.items()
    }


def build_packet() -> dict[str, object]:
    outer_map = outer_irrep_map()
    class_rows = []
    for cls in S6_CLASSES:
        image = OUTER_CLASS[cls]
        class_rows.append(
            {
                "cycle_type": partition_label(cls),
                "class_size": class_size(cls),
                "sign": permutation_sign(cls),
                "outer_image": partition_label(image),
            }
        )

    alternatives = []
    for name, outer, sign_twist in (
        ("natural", False, False),
        ("outer", True, False),
        ("natural_plus_sign", False, True),
        ("outer_plus_sign", True, True),
    ):
        alternatives.append(
            {
                "convention": name,
                "selected_S6_irreps": selector(outer=outer, sign_twist=sign_twist),
                "fixed_dimension_on_frozen_general_rows": projection_on_official_rows(
                    outer=outer, sign_twist=sign_twist
                ),
            }
        )

    return {
        "packet": "GENUS2_SYM12_OUTER_S6_CONVENTION_GATE",
        "status": "EXACT_FINITE_CHARACTER_THEORY_AND_PRIMARY_SOURCE_CONVENTION_AUDIT",
        "resource_firewall": {
            "point_counts": 0,
            "largest_group": "S6",
            "computer_algebra_packages": 0,
        },
        "outer_automorphism": {
            "conjugacy_classes": class_rows,
            "irreducible_pullback": _label_map(outer_map),
            "sign_is_fixed": all(
                permutation_sign(cls) == permutation_sign(OUTER_CLASS[cls])
                for cls in S6_CLASSES
            ),
        },
        "S5_selectors": alternatives,
        "official_general_rows": {
            "weight_project_convention": "(j,k)=(12,3)",
            "partitions": [partition_label(row) for row in OFFICIAL_GENERAL_ROWS],
            "total_S6_dimension": sum(
                hook_dimension(row) for row in OFFICIAL_GENERAL_ROWS
            ),
            "source_grade": "CONDITIONAL_K3_FORMULA_DATABASE_ROWS",
        },
        "convention_reconciliation": {
            "split_root_M2_type": "[2,2,2]",
            "Bergstrom_Clery_2025_M2_type": "[2,2,2]",
            "deduction": (
                "The split-root and 2025 official identifications differ only by an "
                "inner automorphism: an outer automorphism sends [2,2,2] to [5,1]."
            ),
            "marked_subgroup": (
                "The official A2(w^1) subgroup is therefore conjugate to the natural "
                "point stabilizer S5, not the transitive outer S5."
            ),
            "character_twist": (
                "None in the regular covariant/form identification: mu is induced by the "
                "natural six-root quotient, nu o mu is the identity, and regular covariants "
                "are exactly the image.  The alternating chi5 maps to the alternating "
                "Vandermonde product, so the quadratic character is already represented "
                "inside the natural S6 module rather than added as an extra twist."
            ),
        },
        "exact_conclusion": {
            "official_selector": ["[6]", "[5,1]"],
            "official_general_fixed_dimension": 0,
            "outer_counterfactual_fixed_dimension": 1,
            "corrected_natural_marked_valuation_nullity": 0,
            "remaining_gate": (
                "Transport the exact natural marked modular zero through an independently "
                "justified cohomological/Galois adapter.  The former 15-dimensional "
                "one-orientation kernel is retracted, and outer-S6 relabelling is irrelevant."
            ),
        },
        "novelty_firewall": (
            "The S6 character facts are classical.  The project contribution is the exact "
            "convention reconciliation and its application to the frozen Sym12 rows; no "
            "claim of external novelty or of stable-channel nonvanishing is made."
        ),
        "primary_sources": [
            {
                "source": "Bergstrom-Faber-van der Geer, arXiv:0803.0917v2, Sections 2 and 5",
                "use": "A2(w^1) is the quotient by the point stabilizer of a labelled Weierstrass point.",
                "url": "https://arxiv.org/abs/0803.0917",
            },
            {
                "source": "Bergstrom-Clery, arXiv:2309.04388v2, Section 2 and Theorem 3.1",
                "use": "Fixes the official S6 action and identifies M2(Gamma[2]) with s[2^3].",
                "url": "https://arxiv.org/abs/2309.04388",
            },
            {
                "source": "Clery-van der Geer, arXiv:2605.13300v1, Sections 2, 6, and 8",
                "use": "Fixes the natural root action, gives M2 as s[2^3], and identifies regular covariants with modular forms.",
                "url": "https://arxiv.org/abs/2605.13300",
            },
        ],
    }


def _canonical_text(packet: dict[str, object]) -> str:
    return json.dumps(packet, indent=2, sort_keys=True) + "\n"


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check committed JSON")
    parser.add_argument("--write", action="store_true", help="rewrite committed JSON")
    args = parser.parse_args(list(argv) if argv is not None else None)
    packet = build_packet()
    text = _canonical_text(packet)
    if args.check:
        if not CANONICAL.exists() or CANONICAL.read_text(encoding="utf-8") != text:
            raise SystemExit("canonical outer-S6 packet is stale")
        print("outer-S6 convention gate: canonical packet verified")
        return 0
    if args.write:
        CANONICAL.write_text(text, encoding="utf-8")
        print(f"wrote {CANONICAL}")
        return 0
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
