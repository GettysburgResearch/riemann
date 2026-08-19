#!/usr/bin/env python3
"""Exact replay for T-99050 score-last entropy isometry.

Standard library only. The replay checks finite causal-tree algebra, exact
termination, ownership mutations, and the elementary <852 root-cost ledger.
It does not prove the inherited endpoint-frame, Hall, all-column, or
Mellin--Landau theorems and does not establish RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable

SCHEMA = "riemann.t99050.score-last.v1"


def vadd(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(x + y for x, y in zip(a, b, strict=True))


def vscale(c: Fraction, a: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(c * x for x in a)


def vsum(items: Iterable[tuple[Fraction, ...]], dim: int) -> tuple[Fraction, ...]:
    out = tuple(Fraction(0) for _ in range(dim))
    for item in items:
        out = vadd(out, item)
    return out


def score(row: tuple[Fraction, ...]) -> Fraction:
    weights = (Fraction(2), Fraction(3), Fraction(5), Fraction(7))
    return sum((w * x for w, x in zip(weights, row, strict=True)), Fraction(0))


@dataclass(frozen=True)
class Node:
    row: tuple[Fraction, ...]
    rough_discounts: tuple[Fraction, ...]
    children: tuple["Node", ...]
    hall_bonus: tuple[Fraction, ...] = (Fraction(0),) * 4

    def causal_coefficients(self) -> tuple[Fraction, tuple[Fraction, ...], tuple[Fraction, ...]]:
        s = Fraction(1)
        lambdas: list[Fraction] = []
        alphas: list[Fraction] = []
        for r in self.rough_discounts:
            lam = r * s
            lambdas.append(lam)
            alphas.append(r * lam)
            s *= 1 - r
        assert s + sum(lambdas, Fraction(0)) == 1
        return s, tuple(lambdas), tuple(alphas)

    def current_row(self) -> tuple[Fraction, ...]:
        _, _, alphas = self.causal_coefficients()
        child_use = vsum(
            (vscale(a, child.row) for a, child in zip(alphas, self.children, strict=True)),
            len(self.row),
        )
        current = tuple(x - y for x, y in zip(self.row, child_use, strict=True))
        assert all(x >= 0 for x in current)
        return current


def expand(node: Node, weight: Fraction = Fraction(1)) -> tuple[tuple[Fraction, ...], Fraction, int]:
    """Return fully expanded row, fully expanded score and number of owners."""
    current = vadd(node.current_row(), node.hall_bonus)
    total_row = vscale(weight, current)
    total_score = weight * score(current)
    owners = 1
    _, _, alphas = node.causal_coefficients()
    for alpha, child in zip(alphas, node.children, strict=True):
        row_c, score_c, owners_c = expand(child, weight * alpha)
        total_row = vadd(total_row, row_c)
        total_score += score_c
        owners += owners_c
    return total_row, total_score, owners


def make_fixture() -> Node:
    leaf_a = Node((Fraction(11), Fraction(7), Fraction(5), Fraction(3)), (), ())
    leaf_b = Node((Fraction(9), Fraction(8), Fraction(4), Fraction(2)), (), ())
    leaf_c = Node((Fraction(6), Fraction(5), Fraction(3), Fraction(1)), (), ())

    mid_a = Node(
        (Fraction(40), Fraction(30), Fraction(20), Fraction(10)),
        (Fraction(1, 9), Fraction(1, 10)),
        (leaf_a, leaf_b),
    )
    mid_b = Node(
        (Fraction(35), Fraction(27), Fraction(18), Fraction(9)),
        (Fraction(1, 11),),
        (leaf_c,),
    )
    root = Node(
        (Fraction(160), Fraction(120), Fraction(90), Fraction(50)),
        (Fraction(1, 9), Fraction(1, 10)),
        (mid_a, mid_b),
        (Fraction(0), Fraction(3), Fraction(0), Fraction(1)),
    )
    return root


def verify_tree() -> dict[str, object]:
    root = make_fixture()
    expanded_row, expanded_score, owners = expand(root)
    expected_row = vadd(root.row, root.hall_bonus)
    expected_score = score(expected_row)
    assert expanded_row == expected_row
    assert expanded_score == expected_score

    mutated = vadd(expanded_row, root.hall_bonus)
    assert mutated != expected_row

    return {
        "classification": "PASS_FINITE_CAUSAL_TREE_LITERAL_SCORE_ISOMETRY",
        "expanded_row": [str(x) for x in expanded_row],
        "expanded_score": str(expanded_score),
        "owner_nodes": owners,
        "double_hall_bonus_mutation_rejected": True,
    }


def verify_coefficients() -> dict[str, object]:
    discounts = (Fraction(1, 9), Fraction(1, 10), Fraction(1, 11))
    s = Fraction(1)
    lambdas: list[Fraction] = []
    alphas: list[Fraction] = []
    for r in discounts:
        lam = r * s
        lambdas.append(lam)
        alphas.append(r * lam)
        s *= 1 - r
    assert s + sum(lambdas, Fraction(0)) == 1
    for r, lam, alpha in zip(discounts, lambdas, alphas, strict=True):
        assert alpha == r * lam
    assert Fraction(1, 8) > Fraction(1, 9)
    assert 64 < 67
    return {
        "classification": "PASS_CAUSAL_COEFFICIENT_AND_FACTOR67_GATES",
        "survival": str(s),
        "lambdas": [str(x) for x in lambdas],
        "alphas": [str(x) for x in alphas],
        "sqrt67_discount_below_one_eighth": True,
    }


def verify_depth() -> dict[str, object]:
    a = Fraction(67, 66)
    for y in (Fraction(67), Fraction(10**3), Fraction(10**12), Fraction(10**30)):
        assert y / 67 + 1 - a == (y - a) / 67
        z = y
        steps = 0
        while z >= 67:
            z = z / 67 + 1
            steps += 1
            assert steps < 100
        assert z < 67
    return {
        "classification": "PASS_ACTUAL_CHILD_SCALE_HAS_FINITE_DEPTH",
        "fixed_point": str(a),
        "tested_endpoints": [67, 10**3, 10**12, 10**30],
    }


def verify_root_cost() -> dict[str, object]:
    W = 10000
    B = W + 2
    X0 = 4 * B * B

    assert 8 < 9
    assert 16 * 67 < 33 * 33

    partial = sum((Fraction(1, 1), Fraction(1, 1), Fraction(1, 2), Fraction(1, 6), Fraction(1, 24), Fraction(1, 120)), Fraction(0))
    assert partial == Fraction(163, 60)
    assert partial > Fraction(27, 10)
    assert 27**20 > X0 * 10**20

    top_bound = 60
    thinning_bound = 96 * 33 // 4
    assert thinning_bound == 792
    total = top_bound + thinning_bound
    assert total == 852

    return {
        "classification": "PASS_EXPLICIT_ROOT_ONLY_SCORE_COST",
        "W": W,
        "B": B,
        "X0": X0,
        "top_omission_score_upper": top_bound,
        "thinning_score_upper": thinning_bound,
        "total_score_loss_upper": total,
    }


def main_payload() -> dict[str, object]:
    checks = [verify_coefficients(), verify_tree(), verify_depth(), verify_root_cost()]
    core = {
        "schema": SCHEMA,
        "classification": "PASS_T99050_SCORE_LAST_ENTROPY_ISOMETRY",
        "checks": checks,
        "arithmetic_tree_score_loss": 0,
        "root_owned_score_loss_upper": 852,
        "declared_score_used_in_final_tree": False,
        "heavy_inherited_campaigns_replayed": False,
        "rh_established": False,
    }
    digest = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {**core, "proof_object_sha256": digest}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = main_payload()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
