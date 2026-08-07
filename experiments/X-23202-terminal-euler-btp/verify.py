#!/usr/bin/env python3
"""Exact finite regression for the corrected PR #233 proposal.

This checker verifies only rational scale geometry, finite complexity acyclicity,
signed source recombination, terminal exponents, and the fail-closed BTP schema.
It evaluates no primes, zeta values, or production packet estimate.
"""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict, deque
from fractions import Fraction
from typing import Iterable

SCHEMA = "riemann.x23202-terminal-euler-btp.v1"
REQUIRED_BTP_FIELDS = (
    "tuple_manifest",
    "signed_recombination",
    "factor_intervals",
    "cutoff_ledger",
    "normal_gram",
    "strict_scale_destinations",
    "epsilon_K",
)


class VerificationError(ValueError):
    pass


def classify_triplet(
    small: Fraction,
    left: Fraction,
    right: Fraction,
    delta: Fraction,
) -> str:
    """Check the normalized exponent version of L-23206's dichotomy."""
    if small + left + right != 1:
        raise VerificationError("exponents must sum to one")
    if small > delta:
        raise VerificationError("small prefix exceeds delta")

    if left > 1 - delta:
        if not small + right < delta:
            raise VerificationError("large-left complement is not small")
        return "reduce_b_large"

    if right > 1 - delta:
        if not small + left < delta:
            raise VerificationError("large-right complement is not small")
        return "reduce_c_large"

    if left >= delta:
        if left > 1 - delta or small + right > 1 - delta:
            raise VerificationError("left split is not balanced")
        return "balanced_b"

    if right >= delta:
        if right > 1 - delta or small + left > 1 - delta:
            raise VerificationError("right split is not balanced")
        return "balanced_c"

    raise VerificationError("internal gap: reserve is not below one third")


def grid_check(delta: Fraction, denominator: int = 60) -> tuple[int, dict[str, int]]:
    counts: dict[str, int] = defaultdict(int)
    total = 0
    for small_i in range(int(delta * denominator) + 1):
        small = Fraction(small_i, denominator)
        for left_i in range(denominator - small_i + 1):
            left = Fraction(left_i, denominator)
            right = 1 - small - left
            if right < 0:
                continue
            counts[classify_triplet(small, left, right, delta)] += 1
            total += 1
    return total, dict(sorted(counts.items()))


def topological_order(edges: dict[int, Iterable[int]]) -> list[int]:
    nodes = set(edges)
    for values in edges.values():
        nodes.update(values)
    indegree = {node: 0 for node in nodes}
    adjacency = {node: [] for node in nodes}
    for source, targets in edges.items():
        for target in targets:
            adjacency[source].append(target)
            indegree[target] += 1
    queue = deque(sorted(node for node, degree in indegree.items() if degree == 0))
    order: list[int] = []
    while queue:
        source = queue.popleft()
        order.append(source)
        for target in adjacency[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    if len(order) != len(nodes):
        raise VerificationError("same-scale complexity graph contains a cycle")
    return order


def recombine_signed(rows: list[list[Fraction]]) -> tuple[list[Fraction], Fraction, Fraction]:
    width = max(len(row) for row in rows)
    total = [
        sum((row[index] if index < len(row) else Fraction(0) for row in rows), Fraction(0))
        for index in range(width)
    ]
    direct_energy = sum(value * value for value in total)
    separated_energy = sum(sum(value * value for value in row) for row in rows)
    return total, direct_energy, separated_energy


def validate_btp_manifest(manifest: dict[str, object]) -> None:
    missing = [field for field in REQUIRED_BTP_FIELDS if field not in manifest]
    if missing:
        raise VerificationError("missing BTP fields: " + ", ".join(missing))
    if manifest["signed_recombination"] is not True:
        raise VerificationError("signed recombination must precede every norm")
    if manifest["normal_gram"] != "factor-ratio":
        raise VerificationError("wrong packet orientation")


def verify() -> dict[str, object]:
    delta = Fraction(1, 5)
    order = 6
    if not Fraction(1, order) < delta < Fraction(1, 3):
        raise VerificationError("canonical K/delta reserve failed")

    grid_cases, grid_counts = grid_check(delta)

    old_counterexample = (
        Fraction(37, 100),
        Fraction(77, 200),
        Fraction(49, 200),
    )
    old_rejected = False
    try:
        classify_triplet(*old_counterexample, Fraction(2, 5))
    except VerificationError:
        old_rejected = True
    if not old_rejected:
        raise VerificationError("the delta=2/5 counterexample was not rejected")

    complexity_order = topological_order({4: [3, 2], 3: [2], 2: [1], 1: []})

    signed_vector, signed_energy, separated_energy = recombine_signed(
        [
            [Fraction(3), Fraction(-2), Fraction(1)],
            [Fraction(-3), Fraction(2), Fraction(-1)],
            [Fraction(1), Fraction(1), Fraction(-1)],
        ]
    )
    if signed_vector != [Fraction(1), Fraction(1), Fraction(-1)]:
        raise VerificationError("signed source recombination changed")
    if signed_energy != 3 or separated_energy != 31:
        raise VerificationError("signed-energy control changed")

    manifest = {
        "tuple_manifest": "synthetic-bound",
        "signed_recombination": True,
        "factor_intervals": [[1, 5], [4, 5]],
        "cutoff_ledger": "complete",
        "normal_gram": "factor-ratio",
        "strict_scale_destinations": True,
        "epsilon_K": [1, order],
    }
    validate_btp_manifest(manifest)

    amplitude_decay = Fraction(1, 2) - delta
    energy_decay = 1 - 2 * delta
    epsilon_k = Fraction(1, order)
    two_theta_upper = epsilon_k / delta

    result: dict[str, object] = {
        "schema": SCHEMA,
        "classification": "EXACT_SYNTHETIC_TERMINAL_EULER_BTP_AUDIT",
        "delta": [delta.numerator, delta.denominator],
        "K": order,
        "truncated_exponent": [1, order],
        "grid_denominator": 60,
        "grid_cases": grid_cases,
        "grid_classification_counts": grid_counts,
        "old_delta_2_5_counterexample_rejected": old_rejected,
        "terminal_amplitude_decay_exponent": [
            amplitude_decay.numerator,
            amplitude_decay.denominator,
        ],
        "terminal_energy_decay_exponent": [
            energy_decay.numerator,
            energy_decay.denominator,
        ],
        "complexity_topological_order": complexity_order,
        "signed_recombined_vector": [str(value) for value in signed_vector],
        "signed_recombined_energy": str(signed_energy),
        "rowwise_separate_energy": str(separated_energy),
        "synthetic_epsilon_K": [epsilon_k.numerator, epsilon_k.denominator],
        "synthetic_two_theta_upper": [
            two_theta_upper.numerator,
            two_theta_upper.denominator,
        ],
        "required_btp_fields": list(REQUIRED_BTP_FIELDS),
        "proof_boundary": (
            "Exact finite geometry and schema only; no prime packet, BTP estimate, or RH result."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["exact_proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> int:
    print(json.dumps(verify(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
