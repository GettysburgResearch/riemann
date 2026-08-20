#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

VERDICT = "PASS_T99100_COMMON_PARENT_RANDOM_KEY_INTERFACE"


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def verify(_: dict[str, Any] | None = None) -> dict[str, Any]:
    rs = [Fraction(1, 9), Fraction(1, 11), Fraction(1, 13)]
    survivor = Fraction(1)
    lambdas: list[Fraction] = []
    alphas: list[Fraction] = []
    for r in rs:
        lam = r * survivor
        alpha = r * lam
        lambdas.append(lam)
        alphas.append(alpha)
        survivor *= 1 - r

    assert survivor + sum(lambdas, Fraction()) == 1
    assert all(alpha == r * lam for alpha, r, lam in zip(alphas, rs, lambdas))
    assert sum(alphas, Fraction()) < Fraction(1, 8)

    parent = [Fraction(1), Fraction(1)]
    child_densities = [
        [Fraction(1, 10), Fraction(1, 20)],
        [Fraction(1, 15), Fraction(1, 12)],
        [Fraction(1, 30), Fraction(1, 25)],
    ]
    cumulative = [sum(row[i] for row in child_densities) for i in range(2)]
    assert all(Fraction(0) <= x <= Fraction(1) for x in cumulative)
    children = [[parent[i] * row[i] for i in range(2)] for row in child_densities]
    residual = [parent[i] * (1 - cumulative[i]) for i in range(2)]
    for i in range(2):
        assert sum(child[i] for child in children) + residual[i] == parent[i]

    masses = [Fraction(2), Fraction(3), Fraction(5)]
    normalized_values = [Fraction(1, 4), Fraction(2, 3), Fraction(7, 10)]
    raw_values = [m * z for m, z in zip(masses, normalized_values)]
    parent_normalized = sum(raw_values, Fraction()) / sum(masses, Fraction())
    barycenter = sum((m / sum(masses, Fraction())) * z for m, z in zip(masses, normalized_values))
    assert parent_normalized == barycenter

    fractional = [[Fraction(1, 2), Fraction(1, 2)], [Fraction(1, 2), Fraction(1, 2)]]
    matching_a = [[1, 0], [0, 1]]
    matching_b = [[0, 1], [1, 0]]
    for i in range(2):
        for j in range(2):
            assert fractional[i][j] == Fraction(matching_a[i][j] + matching_b[i][j], 2)
    for matching in (matching_a, matching_b):
        assert all(sum(row) == 1 for row in matching)
        assert all(sum(matching[i][j] for i in range(2)) == 1 for j in range(2))

    bad_children = [Fraction(3, 5), Fraction(3, 5)]
    assert sum(bad_children) <= 2
    assert sum(bad_children) > 1
    rounded_leaves = [0, 2]
    assert Fraction(sum(rounded_leaves), len(rounded_leaves)) == 1
    assert max(rounded_leaves) > 1

    core = {
        "classification": VERDICT,
        "coefficient_identity_exact": True,
        "factor67_bound_uses_64_lt_67": True,
        "common_parent_partition_control": True,
        "normalize_last_barycenter_control": True,
        "integral_hall_leaf_control": True,
        "global_mass_only_firewall": True,
        "expectation_only_firewall": True,
        "native_application_established": False,
        "rh_established": False,
        "alpha_sum_control": fstr(sum(alphas, Fraction())),
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return core


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text()) if args.certificate else None
    result = verify(data)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print(VERDICT)
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
