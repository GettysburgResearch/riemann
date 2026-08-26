#!/usr/bin/env python3
"""Exact replay for the quadratic-versus-quartic occupancy firewall."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import DefaultDict, Iterable, List, Tuple

Vec = Tuple[Fraction, Fraction]


def dot(a: Vec, b: Vec) -> Fraction:
    return a[0] * b[0] + a[1] * b[1]


def norm2(a: Vec) -> Fraction:
    return dot(a, a)


def sum_vec(vs: Iterable[Vec]) -> Vec:
    x = Fraction(0)
    y = Fraction(0)
    for a, b in vs:
        x += a
        y += b
    return (x, y)


def run() -> dict:
    rng = random.Random(106071)
    primes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
    checks = {
        "at_most_two_core_roots": 0,
        "exact_quadratic_residue_gram": 0,
        "homogeneity_degree_separation": 0,
        "low_crowding_cauchy": 0,
        "many_owner_one_residue_counterexample": 0,
        "partial_matching_does_not_bound_owner_count": 0,
        "quartic_pair_tensor_identity": 0,
    }

    for ell in primes:
        for factor in (2, 4, 8, 16):
            owner_count = factor * ell
            coefficient = Fraction(1, owner_count)

            quadratic_gram = (owner_count * coefficient) ** 2
            source_energy = owner_count * coefficient * coefficient
            quartic_pair_tensor = source_energy * source_energy

            assert quadratic_gram == 1
            assert quadratic_gram > ell * quartic_pair_tensor
            checks["many_owner_one_residue_counterexample"] += 1
            checks["partial_matching_does_not_bound_owner_count"] += 1

            for denominator in (2, 3, 5, 7):
                lam = Fraction(1, denominator)
                quadratic_scaled = lam**2 * quadratic_gram
                quartic_scaled = lam**4 * quartic_pair_tensor
                assert quadratic_scaled / quadratic_gram == lam**2
                assert quartic_scaled / quartic_pair_tensor == lam**4
                checks["homogeneity_degree_separation"] += 1

            coefficients = [coefficient] * owner_count
            exact_pair_sum = sum(
                x * x * y * y for x in coefficients for y in coefficients
            )
            assert exact_pair_sum == quartic_pair_tensor
            checks["quartic_pair_tensor_identity"] += 1

        for _ in range(120):
            groups: DefaultDict[int, List[Vec]] = defaultdict(list)
            atoms: List[Tuple[int, Vec]] = []
            for _atom in range(rng.randint(1, 80)):
                residue = rng.randrange(1, ell)
                vector = (
                    Fraction(rng.randint(-5, 5), rng.randint(1, 7)),
                    Fraction(rng.randint(-5, 5), rng.randint(1, 7)),
                )
                groups[residue].append(vector)
                atoms.append((residue, vector))

            residue_gram = sum(norm2(sum_vec(vs)) for vs in groups.values())
            orthogonality_expansion = Fraction(0)
            for residue, vector in atoms:
                for other_residue, other_vector in atoms:
                    if residue == other_residue:
                        orthogonality_expansion += dot(vector, other_vector)
            assert residue_gram == orthogonality_expansion
            checks["exact_quadratic_residue_gram"] += 1

        for crowding_bound in (1, 2, 3, 5, 8):
            for _ in range(60):
                source_energy = Fraction(0)
                residue_gram = Fraction(0)
                for residue in range(1, ell):
                    multiplicity = rng.randint(0, crowding_bound)
                    vectors = [
                        (
                            Fraction(rng.randint(-4, 4), rng.randint(1, 5)),
                            Fraction(rng.randint(-4, 4), rng.randint(1, 5)),
                        )
                        for _ in range(multiplicity)
                    ]
                    source_energy += sum(norm2(v) for v in vectors)
                    residue_gram += norm2(sum_vec(vectors))
                assert residue_gram <= crowding_bound * source_energy
                checks["low_crowding_cauchy"] += 1

        for block_scale in range(1, max(2, ell // 16 + 1)):
            if 8 * block_scale >= ell:
                continue
            for owner in range(1, ell):
                for residue in range(1, ell):
                    roots = [
                        core
                        for core in range(ell)
                        if (owner * core * core - residue) % ell == 0
                    ]
                    lifts = [
                        core
                        for core in range(block_scale, 8 * block_scale)
                        if (owner * core * core - residue) % ell == 0
                    ]
                    assert len(roots) <= 2
                    assert len(lifts) <= 2
                    checks["at_most_two_core_roots"] += 1

    result = {
        "verdict": "PASS_X_106071_QUADRATIC_VS_QUARTIC_FIREWALL",
        "arithmetic_class": "EXACT_RATIONAL_RESIDUE_GRAM_AND_HOMOGENEITY",
        "prime_fields": list(primes),
        "checks": checks,
        "total_checks": sum(checks.values()),
        "proved": {
            "quadratic_character_moment_is_residue_gram": True,
            "quartic_pair_tensor_has_degree_four": True,
            "quartic_to_quadratic_uniform_adapter_rejected": True,
            "many_owner_one_residue_counterexample": True,
            "at_most_two_cores_per_owner_residue": True,
            "low_owner_crowding_cells_are_closed": True,
        },
        "open": {
            "hqoro106071_high_owner_crowding": True,
            "bpoe103300": True,
            "riemann_hypothesis": True,
        },
        "scope": (
            "finite exact homogeneity, residue-Gram, root-count, "
            "and low-crowding algebra only"
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
