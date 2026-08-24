#!/usr/bin/env python3
"""Exact replay for T-105510."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path
from typing import Sequence

VERDICT = "PASS_T105510_TRIANGULAR_WICK_FRONTIER"
ROOT = Path(__file__).resolve().parents[2]
CONTENT = (
    "README_105510.md",
    "PR_BODY_105510_ADDENDUM.md",
    "PACKET_METADATA_105510.json",
    "claims/lemmas/L-105510-triangular-polynomial-wick-congruence.md",
    "claims/lemmas/L-105511-polynomial-wick-density-reserve.md",
    "claims/refutations/R-105510-pointwise-polynomial-is-not-a-unit.md",
    "claims/theorems/T-105510-boundary-tame-ninety-two-percent-frontier.md",
    "claims/methodology/M-105510-hostile-review-contract.md",
    "reports/gpt56-pro/2026-08-24-triangular-wick-frontier.md",
    "experiments/X-105510-triangular-wick/README.md",
    "experiments/X-105510-triangular-wick/replay.sh",
    "experiments/X-105510-triangular-wick/verify.py",
    "experiments/X-105510-triangular-wick/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def identity(n: int) -> list[list[F]]:
    return [[F(i == j) for j in range(n)] for i in range(n)]


def matrix_add(a: Sequence[Sequence[F]], b: Sequence[Sequence[F]]) -> list[list[F]]:
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def matrix_scale(c: F, a: Sequence[Sequence[F]]) -> list[list[F]]:
    return [[c * value for value in row] for row in a]


def matrix_multiply(
    a: Sequence[Sequence[F]], b: Sequence[Sequence[F]]
) -> list[list[F]]:
    rows = len(a)
    inner = len(b)
    columns = len(b[0])
    return [
        [sum((a[i][k] * b[k][j] for k in range(inner)), F(0)) for j in range(columns)]
        for i in range(rows)
    ]


def matrix_power(x: Sequence[Sequence[F]], exponent: int) -> list[list[F]]:
    result = identity(len(x))
    for _ in range(exponent):
        result = matrix_multiply(result, x)
    return result


@lru_cache(maxsize=None)
def triangular_identity_checks() -> dict[str, int]:
    cases = 0
    for n in range(1, 11):
        for trial in range(100):
            generator = random.Random(105510 + 1000 * n + trial)
            x = [
                [F(generator.randint(-3, 3)) if j > i else F(0) for j in range(n)]
                for i in range(n)
            ]
            one = identity(n)
            x2 = matrix_multiply(x, x)
            p = matrix_add(
                matrix_add(one, matrix_scale(F(-1, 2), x)),
                matrix_scale(F(-1, 8), x2),
            )
            require(all(p[i][i] == 1 for i in range(n)), "unit diagonal")
            require(all(p[i][j] == 0 for i in range(n) for j in range(i)), "triangular")

            powers = [one]
            for _ in range(1, n):
                powers.append(matrix_multiply(powers[-1], x))
            resolvent = [[F(0) for _ in range(n)] for _ in range(n)]
            for power_matrix in powers:
                resolvent = matrix_add(resolvent, power_matrix)

            target = one
            if n > 3:
                target = matrix_add(target, matrix_scale(F(1, 8), powers[3]))
            for power in range(4, n):
                target = matrix_add(target, matrix_scale(F(9, 64), powers[power]))

            actual = matrix_multiply(matrix_multiply(p, p), resolvent)
            require(actual == target, "triangular Wick identity")
            cases += 1
    require(cases == 1000, "matrix case count")
    return {"exact_nilpotent_matrix_cases": cases, "maximum_dimension": 10}


@lru_cache(maxsize=None)
def coefficient_checks() -> dict[str, str]:
    # P(x)^2 = 1-x+x^3/8+x^4/64.
    p2 = [F(1), F(-1), F(0), F(1, 8), F(1, 64)]
    q: list[F] = []
    running = F(0)
    for m in range(16):
        if m < len(p2):
            running += p2[m]
        q.append(running)
    expected = [F(1), F(0), F(0), F(1, 8)] + [F(9, 64)] * 12
    require(q == expected, "polynomial quotient coefficients")
    return {
        "q0": str(q[0]),
        "q1": str(q[1]),
        "q2": str(q[2]),
        "q3": str(q[3]),
        "q_m_ge_4": str(q[4]),
    }


@lru_cache(maxsize=None)
def energy_and_record_checks() -> dict[str, str]:
    t3 = F(math.factorial(3), math.factorial(6))
    t4 = F(math.factorial(4), math.factorial(8))
    energy_bound = F(1, 64) * t3 + F(81, 4096) * F(18, 17) * t4
    require(energy_bound == F(1669, 11698176), "energy fraction")
    require(energy_bound < F(1, 7000), "energy target")

    reserve = F(3500, 3501)
    eta = reserve * F(99, 101) ** 2
    line = 2 * eta - 1
    margin90 = line - F(9, 10)
    margin92 = line - F(23, 25)
    require(eta == F(3811500, 3968189), "eta fraction")
    require(line == F(3654811, 3968189), "line fraction")
    require(margin90 == F(834409, 39681890) > 0, "ninety margin")
    require(margin92 > 0, "ninety-two margin")
    return {
        "one_sided_energy_upper": str(energy_bound),
        "energy_target": "1/7000",
        "model_reserve_lower": str(reserve),
        "eta_lower_under_99_101": str(eta),
        "conditional_line_fraction": str(line),
        "conditional_line_decimal": f"{float(line):.15f}",
        "margin_over_ninety_percent": str(margin90),
        "margin_over_ninety_two_percent": str(margin92),
    }


def content_hashes() -> dict[str, str]:
    result: dict[str, str] = {}
    for relative in CONTENT:
        data = (ROOT / relative).read_bytes().replace(b"\r\n", b"\n")
        result[relative] = hashlib.sha256(data).hexdigest()
    return result


def build_payload() -> dict[str, object]:
    payload: dict[str, object] = {
        "verdict": VERDICT,
        "triangular_identity": triangular_identity_checks(),
        "coefficients": coefficient_checks(),
        "energy_and_record": energy_and_record_checks(),
        "content_sha256": content_hashes(),
        "finite_source_congruence_machine_verified": True,
        "pnt_limit_machine_proved": False,
        "triwxfer105510_proved": False,
        "ninety_percent_established": False,
        "record_beaten": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    payload = build_payload()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(VERDICT)
    print(payload["proof_object_sha256"])
    print("EXACT_NILPOTENT_MATRIX_CASES=1000")
    print("CONDITIONAL_LINE_FRACTION=3654811/3968189")
    print("TRIWXFER105510_OPEN")
    print("NINETY_PERCENT_UNPROVED")
    print("RECORD_UNBEATEN")
    print("RH_UNPROVED")
