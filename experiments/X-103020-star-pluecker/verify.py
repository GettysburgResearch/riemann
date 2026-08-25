#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import random
from pathlib import Path


def main() -> None:
    rng = random.Random(103020)
    star_checks = 0
    gradient_checks = 0
    energy_checks = 0

    for k in range(4, 101):
        s = [1.0 / k, 1.0 / k] + [
            -2.0 / (k * (k - 2))
        ] * (k - 2)
        assert abs(sum(s)) < 1e-12
        assert all(s[i] >= s[i + 1] - 1e-15 for i in range(k - 1))
        star_checks += 1

        values = [rng.uniform(-2.0, 2.0) for _ in range(k)]
        lhs = sum(s[i] * values[i] for i in range(k))
        rhs = sum(
            (s[i] - s[j]) * (values[i] - values[j])
            for i in range(k)
            for j in range(i + 1, k)
        ) / k
        assert abs(lhs - rhs) < 1e-10
        gradient_checks += 1

        edge_count = k * (k - 1) // 2
        w = {}
        for i in range(k):
            for j in range(i + 1, k):
                w[i, j] = (
                    1.0 if (i, j) == (0, 1) else 0.0
                ) - 1.0 / edge_count

        row = [0.0] * k
        for (i, j), value in w.items():
            row[i] += value
            row[j] += value
        potential = [value / (k - 2) for value in row]
        star = {
            (i, j): potential[i] + potential[j]
            for i in range(k)
            for j in range(i + 1, k)
        }
        cycle = {
            edge: w[edge] - star[edge]
            for edge in w
        }

        assert max(
            abs(
                sum(
                    cycle[min(i, j), max(i, j)]
                    for j in range(k)
                    if j != i
                )
            )
            for i in range(k)
        ) < 1e-10

        star_energy = sum(value * value for value in star.values())
        cycle_energy = sum(value * value for value in cycle.values())
        assert abs(star_energy - 2.0 / k) < 1e-10
        assert abs(cycle_energy - (k - 3.0) / (k - 1.0)) < 1e-10
        energy_checks += 1

    payload = {
        "schema": "riemann.t103020.star-pluecker.v1",
        "star_monotonicity_checks": star_checks,
        "gradient_identity_checks": gradient_checks,
        "star_cycle_energy_checks": energy_checks,
        "star_current_closed_by_replay": False,
        "plc103020_proved": False,
        "rh_established": False,
        "verdict": "PASS_T103020_STAR_PLUECKER_REDUCTION",
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
