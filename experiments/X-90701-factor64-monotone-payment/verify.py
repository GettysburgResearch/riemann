#!/usr/bin/env python3
"""Exact Q(sqrt(2)) regression for L-90701.

The checker reconstructs the factor-64 reward from the polynomial coefficients,
verifies the finite block sums and rational radical enclosures, checks the
uniform prefix bounds, and exercises the Abel payment on exact rational
nonincreasing occupations. It proves no arithmetic occupation theorem or RH.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import random
from pathlib import Path

STATUS = "PASS_X_90701_FACTOR64_MONOTONE_PAYMENT"

Pair = tuple[Fraction, Fraction]  # a + b sqrt(2)


def add(x: Pair, y: Pair) -> Pair:
    return x[0] + y[0], x[1] + y[1]


def scale(x: Pair, c: Fraction | int) -> Pair:
    c = Fraction(c)
    return x[0] * c, x[1] * c


def lower(x: Pair) -> Fraction:
    """Directed lower value using 707/500 < sqrt(2) < 283/200."""
    lo = Fraction(707, 500)
    hi = Fraction(283, 200)
    return x[0] + x[1] * (lo if x[1] >= 0 else hi)


def upper(x: Pair) -> Fraction:
    lo = Fraction(707, 500)
    hi = Fraction(283, 200)
    return x[0] + x[1] * (hi if x[1] >= 0 else lo)


def mul_pair_rational(x: Pair, q: Fraction) -> Pair:
    return x[0] * q, x[1] * q


Q: list[Pair] = [
    (Fraction(1), Fraction(0)),
    (Fraction(-1, 4), Fraction(-1, 2)),
    (Fraction(-3, 4), Fraction(1, 8)),
    (Fraction(-3, 4), Fraction(3, 8)),
    (Fraction(-1, 4), Fraction(3, 8)),
    (Fraction(1), Fraction(1, 8)),
    (Fraction(0), Fraction(-1, 2)),
]


def build_coordinates() -> tuple[list[Pair], list[Pair | None]]:
    S: list[Pair] = []
    running: Pair = (Fraction(0), Fraction(0))
    for q in Q:
        running = add(running, q)
        S.append(running)
    A: list[Pair | None] = [None]
    for j in range(1, 7):
        total: Pair = (Fraction(0), Fraction(0))
        for ell in range(j):
            total = add(total, scale(S[ell], 2**ell))
        A.append(scale(total, 2))
    return S, A


S, A = build_coordinates()


def reward(m: int) -> Pair:
    j = m.bit_length() - 1
    if j >= 6:
        j = 6
    assert A[j] is not None
    numerator = add(A[j], scale(S[j], m + 1 - 2 ** (j + 1)))
    return scale(numerator, Fraction(1, m * (m - 1)))


def pair_sum(start: int, end: int) -> Pair:
    total: Pair = (Fraction(0), Fraction(0))
    for m in range(start, end + 1):
        total = add(total, reward(m))
    return total


def exact_dot(weights: list[Fraction], occupation: list[Fraction]) -> Fraction:
    return sum((w * x for w, x in zip(weights, occupation)), Fraction())


def main() -> dict[str, object]:
    gates: dict[str, bool] = {}

    gates["radical_enclosure"] = Fraction(707, 500) ** 2 < 2 < Fraction(283, 200) ** 2
    gates["sum_coefficients_zero"] = S[6] == (Fraction(0), Fraction(0))

    signs = {}
    for m in range(2, 1001):
        value_lo, value_hi = lower(reward(m)), upper(reward(m))
        if 13 <= m <= 63:
            ok = value_hi < 0
            signs[m] = -1
        else:
            ok = value_lo > 0
            signs[m] = 1
        if not ok:
            raise AssertionError(("reward sign", m, reward(m), value_lo, value_hi))
    gates["reward_sign_classification"] = True

    blocks = {
        "positive_2_12": pair_sum(2, 12),
        "negative_13_15": pair_sum(13, 15),
        "negative_16_31": pair_sum(16, 31),
        "negative_32_63": pair_sum(32, 63),
    }
    gates["block_2_12_gt_2"] = lower(blocks["positive_2_12"]) > 2
    gates["block_13_15_gt_minus_1_40"] = lower(blocks["negative_13_15"]) > -Fraction(1, 40)
    gates["block_16_31_gt_minus_1_3"] = lower(blocks["negative_16_31"]) > -Fraction(1, 3)
    gates["block_32_63_gt_minus_7_10"] = lower(blocks["negative_32_63"]) > -Fraction(7, 10)

    prefixes: list[Pair] = []
    running: Pair = (Fraction(0), Fraction(0))
    min_lower = None
    min_index = None
    for m in range(2, 10001):
        running = add(running, reward(m))
        prefixes.append(running)
        this_lower = lower(running)
        if min_lower is None or this_lower < min_lower:
            min_lower = this_lower
            min_index = m
        if this_lower <= Fraction(9, 10):
            raise AssertionError(("prefix lower bound", m, running, this_lower))
        if upper(running) >= Fraction(21, 10):
            raise AssertionError(("prefix upper bound", m, running, upper(running)))
    gates["prefix_bounds_through_10000"] = True

    # Analytic tail control after 63.
    d63 = pair_sum(2, 63)
    tail_total = scale((Fraction(-39), Fraction(39)), Fraction(1, 63))
    dinfty = add(d63, tail_total)
    gates["tail_limit_below_21_10"] = upper(dinfty) < Fraction(21, 10)
    gates["d63_above_9_10"] = lower(d63) > Fraction(9, 10)

    rng = random.Random(90701)
    abel_trials = 0
    for _ in range(500):
        length = rng.randint(4, 90)
        current = Fraction(rng.randint(1, 40), rng.randint(1, 20))
        occ: list[Fraction] = []
        for _m in range(2, length + 1):
            occ.append(current)
            drop = Fraction(rng.randint(0, 4), 100) * current
            current = max(Fraction(0), current - drop)
        d_pairs = [reward(m) for m in range(2, length + 1)]
        # Directed lower dot product.
        dot_lo = sum(
            (lower(d) * x if lower(d) >= 0 else lower(d) * x)
            for d, x in zip(d_pairs, occ)
        )
        if dot_lo < Fraction(9, 10) * occ[0]:
            raise AssertionError(("Abel payment", dot_lo, occ[0]))
        abel_trials += 1
    gates["monotone_occupation_trials"] = True

    if not all(gates.values()):
        raise AssertionError([name for name, ok in gates.items() if not ok])

    def pair_json(x: Pair) -> dict[str, str]:
        return {"rational": str(x[0]), "sqrt2_coefficient": str(x[1])}

    result = {
        "status": STATUS,
        "gates": gates,
        "coordinates": {
            "S": [pair_json(x) for x in S],
            "A": [pair_json(x) for x in A[1:] if x is not None],
        },
        "block_sums": {name: pair_json(value) for name, value in blocks.items()},
        "D63": pair_json(d63),
        "D_infinity": pair_json(dinfty),
        "finite_prefix_scan": {
            "through": 10000,
            "minimum_directed_lower": str(min_lower),
            "minimum_index": min_index,
        },
        "monotone_occupation_trials": abel_trials,
        "scope": "exact factor-64 reward algebra only; critical occupation variation and RH remain open",
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    return result


if __name__ == "__main__":
    result = main()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(STATUS)
