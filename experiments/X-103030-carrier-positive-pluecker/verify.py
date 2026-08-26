#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def main() -> None:
    values = [Fraction(i, 16) for i in range(1, 16)]
    survival = [
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(1, 1),
    ]

    checks = 0
    minimum = None
    for a in values:
        for b in values:
            if b > a:
                continue
            for c in values:
                if c > b:
                    continue
                for d in values:
                    if d > c:
                        continue
                    for middle_left in survival:
                        for middle_right in survival:
                            s = a + b - a * b
                            rectangle = (
                                2 * a * b
                                + 2 * c * d * middle_right
                                - s * middle_left * (
                                    c
                                    + d * (1 - c) * middle_right
                                )
                            )
                            assert rectangle > 0
                            checks += 1
                            if minimum is None or rectangle < minimum:
                                minimum = rectangle

    rectangle_checks = 0
    for k in range(4, 101):
        scale = Fraction(1, (k - 1) * (k - 2))
        coefficient = {
            (i, j): Fraction(0)
            for i in range(k)
            for j in range(i + 1, k)
        }
        for i in range(2, k - 1):
            for j in range(i + 1, k):
                updates = [
                    ((0, 1), 2),
                    ((i, j), 2),
                    ((0, i), -1),
                    ((0, j), -1),
                    ((1, i), -1),
                    ((1, j), -1),
                ]
                for edge, multiplier in updates:
                    coefficient[edge] += scale * multiplier

        assert coefficient[0, 1] == Fraction(k - 3, k - 1)
        for j in range(2, k):
            expected = -Fraction(k - 3, (k - 1) * (k - 2))
            assert coefficient[0, j] == expected
            assert coefficient[1, j] == expected
        for i in range(2, k - 1):
            for j in range(i + 1, k):
                assert coefficient[i, j] == Fraction(
                    2, (k - 1) * (k - 2)
                )
        rectangle_checks += 1

    payload = {
        "schema": "riemann.t103030.carrier-positive-pluecker.v1",
        "ordered_activity_checks": checks,
        "minimum_exact_activity": str(minimum),
        "rectangle_decomposition_checks": rectangle_checks,
        "ccpf103030_proved": False,
        "rh_established": False,
        "verdict": "PASS_T103030_CARRIER_POSITIVE_PLUECKER",
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["proof_object_sha256"] = hashlib.sha256(raw.encode()).hexdigest()

    output = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    target = Path(__file__).parent / "results" / "verification.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(output, encoding="utf-8")

    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
