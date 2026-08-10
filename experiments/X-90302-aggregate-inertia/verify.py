#!/usr/bin/env python3
"""Exact regression for L-90304 aggregate inertia elimination.

This verifies only the finite-dimensional Fraction algebra. It does not
certify any Q4 analytic estimate or RH.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
import random
from typing import Sequence

Row = tuple[Fraction, Fraction, Fraction, Fraction, Fraction]
# (weight, R, E, D, Theta)


def aggregate(rows: Sequence[Row]) -> dict[str, Fraction]:
    A = F = B = U = V = Fraction(0)
    for w, R, E, D, Theta in rows:
        if w < 0 or R < 0:
            raise ValueError("weights and R must be nonnegative")
        A += w * R
        F += w * E * E
        B += w * D * D
        U += w * Theta
        V += w * E * D
    C = U - 2 * V
    det = A * B - C * C / 4
    defect = max(Fraction(0), -det)
    if A <= F:
        raise ValueError("the theorem requires A > F")
    bound = A * U * U / (4 * (A - F))
    return {
        "A": A,
        "F": F,
        "B": B,
        "U": U,
        "V": V,
        "C": C,
        "det": det,
        "defect": defect,
        "bound": bound,
    }


def frac_string(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def main() -> None:
    rng = random.Random(90304)
    weights = [Fraction(1, 3), Fraction(1, 2), Fraction(1)]
    Rs = [Fraction(1), Fraction(2), Fraction(4), Fraction(7)]
    Es = [Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2)]
    Ds = [Fraction(-3), Fraction(-1), Fraction(0), Fraction(1), Fraction(3)]
    Ts = [Fraction(-4), Fraction(-1), Fraction(0), Fraction(1), Fraction(4)]

    checked = 0

    for _ in range(50_000):
        rows: list[Row] = []
        for _ in range(rng.choice([1, 2, 3, 4])):
            rows.append(
                (
                    rng.choice(weights),
                    rng.choice(Rs),
                    rng.choice(Es),
                    rng.choice(Ds),
                    rng.choice(Ts),
                )
            )

        A = sum((w * R for w, R, _, _, _ in rows), Fraction(0))
        F = sum((w * E * E for w, _, E, _, _ in rows), Fraction(0))
        if A <= F:
            continue

        data = aggregate(rows)
        if data["defect"] > data["bound"]:
            raise AssertionError((rows, data))
        checked += 1

    if checked < 30_000:
        raise AssertionError(f"too few admissible rows: {checked}")

    sharp_rows: list[Row] = [
        (Fraction(1), Fraction(4), Fraction(0), Fraction(0), Fraction(4))
    ]
    sharp = aggregate(sharp_rows)
    assert sharp["defect"] == sharp["bound"] == Fraction(4)

    mutation_rows: list[Row] = [
        (Fraction(1, 3), Fraction(4), Fraction(1), Fraction(3), Fraction(-4)),
        (Fraction(1, 3), Fraction(2), Fraction(2), Fraction(3), Fraction(-1)),
    ]
    mutation = aggregate(mutation_rows)
    false_bound = mutation["U"] * mutation["U"] / 4
    assert mutation["defect"] > false_bound
    assert mutation["defect"] <= mutation["bound"]

    proof_object = {
        "classification": "PASS_EXACT_AGGREGATE_INERTIA_ELIMINATION",
        "admissible_random_fraction_cases": checked,
        "sharp_equality": {k: frac_string(v) for k, v in sharp.items()},
        "mutation_firewall": {
            "defect": frac_string(mutation["defect"]),
            "false_bound_U2_over_4": frac_string(false_bound),
            "correct_bound": frac_string(mutation["bound"]),
        },
    }
    canonical = json.dumps(proof_object, sort_keys=True, separators=(",", ":"))
    proof_object["proof_object_sha256"] = sha256(canonical.encode()).hexdigest()
    print(json.dumps(proof_object, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
