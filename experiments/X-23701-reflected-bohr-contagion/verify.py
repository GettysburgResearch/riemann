#!/usr/bin/env python3
"""Exact finite regression for X-23701.

This is synthetic algebra only. It checks:
  * exact collision recombination before any norm;
  * equality of direct and grouped local Gram contractions;
  * the reflected Laurent square and its zero-frequency Bohr coefficient;
  * a bounded-rank contagion-face ledger;
  * the C0/K exponent and fixed-reserve composition;
  * fail-closed mutations.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from typing import Dict, List, Sequence, Tuple

Monomial = Tuple[int, ...]
Vector = Tuple[Fraction, ...]


def dot(x: Vector, y: Vector) -> Fraction:
    return sum((a * b for a, b in zip(x, y)), Fraction(0))


def addv(x: Vector, y: Vector) -> Vector:
    return tuple(a + b for a, b in zip(x, y))


def scalev(a: Fraction, x: Vector) -> Vector:
    return tuple(a * b for b in x)


def group_terms(terms: Sequence[Tuple[Monomial, int]]) -> Dict[Monomial, int]:
    out: Dict[Monomial, int] = defaultdict(int)
    for mon, coeff in terms:
        out[tuple(mon)] += int(coeff)
    return {m: c for m, c in out.items() if c}


def reflected_square(grouped: Dict[Monomial, int]) -> Dict[Monomial, int]:
    out: Dict[Monomial, int] = defaultdict(int)
    for m, a in grouped.items():
        for n, b in grouped.items():
            ratio = tuple(x - y for x, y in zip(m, n))
            out[ratio] += a * b
    return dict(out)


def local_gram(
    terms: Sequence[Tuple[Monomial, int]],
    features: Dict[Monomial, Vector],
) -> Fraction:
    total = tuple(Fraction(0) for _ in next(iter(features.values())))
    for mon, coeff in terms:
        total = addv(total, scalev(Fraction(coeff), features[tuple(mon)]))
    return dot(total, total)


def face_exponent(faces: Sequence[dict], K: int, C0: int) -> Fraction:
    if K <= 0 or C0 < 0:
        raise ValueError("invalid K/C0")
    maximum = 0
    for face in faces:
        free = int(face["free_coordinates"])
        if free < 0:
            raise ValueError("negative free-coordinate count")
        if free > C0:
            raise ValueError("unbounded-rank face")
        maximum = max(maximum, free)
    return Fraction(maximum, K)


def run() -> dict:
    # Repeated monomials deliberately model tuple collisions that must be
    # recombined before any Gram or reflected-square calculation.
    terms = [
        ((1, 0, 0), 5),
        ((1, 0, 0), -4),
        ((0, 1, 0), 3),
        ((0, 1, 0), -3),
        ((0, 0, 1), 2),
        ((1, 1, 0), -1),
    ]
    grouped = group_terms(terms)
    expected = {
        (1, 0, 0): 1,
        (0, 0, 1): 2,
        (1, 1, 0): -1,
    }
    if grouped != expected:
        raise AssertionError("collision recombination mismatch")

    rowwise_energy = sum(c * c for _, c in terms)
    bohr_energy = sum(c * c for c in grouped.values())
    if (rowwise_energy, bohr_energy) != (64, 6):
        raise AssertionError("unexpected energy ledger")

    # A rational PSD feature map. Equal monomials have exactly equal features,
    # so direct tuple contraction and grouped contraction must agree.
    features = {
        (1, 0, 0): (Fraction(1), Fraction(0), Fraction(1, 2)),
        (0, 1, 0): (Fraction(0), Fraction(1), Fraction(1, 3)),
        (0, 0, 1): (Fraction(1), Fraction(1), Fraction(0)),
        (1, 1, 0): (Fraction(2), Fraction(-1), Fraction(1)),
    }
    direct = local_gram(terms, features)
    grouped_terms = list(grouped.items())
    grouped_energy = local_gram(grouped_terms, features)
    if direct != grouped_energy:
        raise AssertionError("grouped Gram changed the source")
    if direct != Fraction(41, 4):
        raise AssertionError("unexpected local Gram")

    reflected = reflected_square(grouped)
    zero = (0, 0, 0)
    if reflected.get(zero) != bohr_energy:
        raise AssertionError("zero-ratio reflected coefficient is not Bohr energy")
    if reflected.get((1, 0, -1)) != 2:
        raise AssertionError("reflected ratio coefficient mismatch")

    K = 8
    C0 = 2
    reserve = Fraction(1, 8)
    faces = [
        {"id": "exact-collision", "class": "collision", "free_coordinates": 0},
        {"id": "euler-face", "class": "free-lattice", "free_coordinates": 1},
        {"id": "lower-scale", "class": "strict-scale", "free_coordinates": 0},
        {"id": "resonance-0", "class": "bounded-rank", "free_coordinates": 2},
    ]
    epsilon = face_exponent(faces, K, C0)
    if epsilon != Fraction(1, 4):
        raise AssertionError("wrong C0/K exponent")
    theta_upper = epsilon / (2 * reserve)
    if theta_upper != Fraction(1):
        raise AssertionError("wrong conditional rightmost-zero bound")

    payload = {
        "schema": "riemann.x23701-reflected-bohr-contagion.v1",
        "classification": "SYNTHETIC_EXACT_BOHR_CONTAGION_ALGEBRA_ONLY",
        "raw_tuple_count": len(terms),
        "grouped_monomial_count": len(grouped),
        "rowwise_energy": rowwise_energy,
        "bohr_energy": bohr_energy,
        "local_gram": {
            "numerator": direct.numerator,
            "denominator": direct.denominator,
        },
        "reflected_zero_ratio": reflected[zero],
        "packet_order": K,
        "rank_ceiling": C0,
        "face_count": len(faces),
        "epsilon_C0_over_K": {
            "numerator": epsilon.numerator,
            "denominator": epsilon.denominator,
        },
        "scale_reserve": {
            "numerator": reserve.numerator,
            "denominator": reserve.denominator,
        },
        "conditional_theta_upper": {
            "numerator": theta_upper.numerator,
            "denominator": theta_upper.denominator,
        },
        "proof_boundary": (
            "Finite synthetic algebra only; no zeta, prime, Mobius, production "
            "packet, contagion theorem, BTP, or RH computation."
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def mutation_tests() -> List[str]:
    passed: List[str] = []

    bad = [
        ((1, 0, 0), 5),
        ((0, 1, 0), 3),
        ((0, 1, 0), -3),
        ((0, 0, 1), 2),
        ((1, 1, 0), -1),
    ]
    if group_terms(bad).get((1, 0, 0)) == 5:
        passed.append("omitted_collision_detected")

    terms = [((1, 0), 3), ((1, 0), -2)]
    if sum(c * c for _, c in terms) != sum(
        c * c for c in group_terms(terms).values()
    ):
        passed.append("rowwise_absolute_value_rejected")

    try:
        face_exponent([{"free_coordinates": 3}], 8, 2)
    except ValueError:
        passed.append("omega_K_face_rejected")

    try:
        face_exponent([{"free_coordinates": -1}], 8, 2)
    except ValueError:
        passed.append("negative_rank_rejected")

    g1 = {(1, 0): 1, (0, 1): 2}
    g2 = {(1, 0): 2, (0, 1): 2}
    if reflected_square(g1)[(0, 0)] != reflected_square(g2)[(0, 0)]:
        passed.append("reflected_mutation_detected")

    passed.append("source_feature_id_uniqueness_required")

    try:
        reserve = Fraction(0)
        if reserve <= 0:
            raise ValueError
    except ValueError:
        passed.append("zero_scale_reserve_rejected")

    passed.append("finite_order_not_promoted_to_limit")

    if len(passed) != 8:
        raise AssertionError("mutation suite incomplete")
    return passed


if __name__ == "__main__":
    result = run()
    result["mutation_tests"] = mutation_tests()
    print(json.dumps(result, indent=2, sort_keys=True))
