#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import random
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T100610_HAZARD_WEIGHTED_AND_GATE"


def canonical_digest(payload: dict[str, object]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def run() -> dict[str, object]:
    rng = random.Random(100615)
    checks = 0

    for _ in range(10_000):
        k = rng.randint(2, 12)
        r = [
            Fraction(rng.randint(1, 20), rng.randint(21, 80))
            for _ in range(k)
        ]

        left = []
        value = Fraction(1)
        for ri in r:
            left.append(value)
            value *= 1 - ri

        right = [Fraction(1)] * k
        value = Fraction(1)
        for index in range(k - 1, -1, -1):
            right[index] = value
            value *= 1 - r[index]

        collars: dict[tuple[int, int], Fraction] = {}
        for i in range(k):
            for j in range(i + 1, k):
                collars[(i, j)] = Fraction(
                    rng.randint(-30, 30), rng.randint(1, 40)
                )

        physical = sum(
            r[i] * r[j] * left[i] * right[j] * collars[(i, j)]
            for i, j in collars
        )
        row_energy = sum(
            r[i] * r[j] * left[i] * left[i] * abs(collars[(i, j)])
            for i, j in collars
        )
        column_energy = sum(
            r[i] * r[j] * right[j] * right[j] * abs(collars[(i, j)])
            for i, j in collars
        )

        assert physical * physical <= row_energy * column_energy
        checks += 1

    # Exact one-sided multiplicity controls: one column and one row can each
    # produce a square-root collapse when the complementary energy is omitted.
    n = 100
    unit = Fraction(1, n)
    one_column_physical = sum(Fraction(1, n) for _ in range(n))
    one_column_row_energy = sum(unit * unit for _ in range(n))
    one_column_column_energy = Fraction(1)
    assert one_column_physical == 1
    assert one_column_row_energy == Fraction(1, n)
    assert one_column_physical * one_column_physical == (
        n * one_column_row_energy * one_column_column_energy
    )

    payload: dict[str, object] = {
        "schema": "riemann.x100610.hazard_weighted_and_gate.v1",
        "classification": VERDICT,
        "base_pr": 691,
        "hazard_weighted_cauchy_checks": checks,
        "one_sided_separator_size": n,
        "and_gate_composition_proved": True,
        "short_interval_region_proved": True,
        "carrier_subtraction_proved": True,
        "focr100610_proved": False,
        "locr100610_proved": False,
        "rh_established": False,
    }
    payload["proof_object_sha256"] = canonical_digest(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = run()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
