#!/usr/bin/env python3
"""Discovery-only structured scan of the P61 Target-Lorenz row margins.

This script uses ordinary floating-point arithmetic.  It is reconnaissance and
must never be cited as an infinite sign certificate.
"""
from __future__ import annotations

from pathlib import Path
import bisect
import hashlib
import json
import math

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ROUGH = [67, 71, 83, 127]
Y_VALUES = range(1, 67)
ROWS = range(2, 67)


def divisors_mu() -> list[tuple[int, int]]:
    vals = [(1, 1)]
    for q in PRIMES:
        vals += [(d * q, -mu) for d, mu in list(vals)]
    return sorted(vals)


def build_prefix(limit: int) -> tuple[list[float], list[float]]:
    s1 = [0.0] * (limit + 1)
    sl = [0.0] * (limit + 1)
    for m in range(1, limit + 1):
        iv = 1.0 / math.sqrt(m)
        s1[m] = s1[m - 1] + iv
        sl[m] = sl[m - 1] + iv * math.log(m)
    return s1, sl


def q_row(Y: float, j: int, s1: list[float], sl: list[float]) -> float:
    if Y < j:
        return 0.0
    logY = math.log(Y)
    A = (j + 1) / (j - 1)
    B = -(j + 1) * (j - 2) / (j * (j - 1))
    C = 2 / (j * (j - 1))
    out = A / math.sqrt(j) * (logY - math.log(j))
    if Y >= j + 1:
        out += B / math.sqrt(j + 1) * (logY - math.log(j + 1))
    n = int(math.floor(Y + 1e-12))
    if n >= j + 2:
        out += C * (
            (s1[n] - s1[j + 1]) * logY - (sl[n] - sl[j + 1])
        )
    return out


def target(d: int, p: int, y: int) -> float:
    x = p * y
    out = 0.0
    if d <= x:
        out += (4 * math.sqrt(x / d) - 3) / math.sqrt(d)
    if d <= y:
        out -= (4 * math.sqrt(y / d) - 3) / math.sqrt(p * d)
    return out


def row(d: int, p: int, y: int, j: int, s1: list[float], sl: list[float]) -> float:
    return (
        q_row(p * y / d, j, s1, sl)
        - q_row(y / d, j, s1, sl) / math.sqrt(p)
    ) / math.sqrt(d)


def main() -> None:
    vals = divisors_mu()
    max_x = max(ROUGH) * max(Y_VALUES)
    s1, sl = build_prefix(max_x + 2)
    minimum = (float("inf"), None)
    determinant_minimum = (float("inf"), None)
    cases = 0
    negative = 0

    for p in ROUGH:
        for y in Y_VALUES:
            x = p * y
            active = vals[: bisect.bisect_right(vals, (x, 2))]
            even: list[tuple[int, float]] = []
            odd: list[tuple[int, float]] = []
            for d, mu in active:
                t = target(d, p, y)
                (even if mu == 1 else odd).append((d, t))

            odd_target = sum(t for _, t in odd)
            remaining = odd_target
            used: dict[int, float] = {}
            cutoff = None
            cutoff_fraction = None
            for d, t in even:
                take = min(t, remaining)
                used[d] = take / t
                remaining -= take
                if remaining <= 2e-12:
                    cutoff = d
                    cutoff_fraction = used[d]
                    break
            if cutoff is None:
                raise AssertionError((p, y, odd_target, remaining))

            for j in ROWS:
                margin = 0.0
                even_total_row = 0.0
                odd_total_row = 0.0
                support = x / j
                for d, mu in active:
                    if d >= support and d > y / j:
                        break
                    r = row(d, p, y, j, s1, sl)
                    if mu == 1:
                        even_total_row += r
                        margin += used.get(d, 0.0) * r
                    else:
                        odd_total_row += r
                        margin -= r
                cutoff_target = target(cutoff, p, y)
                cutoff_row = row(cutoff, p, y, j, s1, sl)
                signed_target = sum(t for _, t in even) - odd_target
                signed_row = even_total_row - odd_total_row
                determinant_lower = signed_row - (cutoff_row / cutoff_target) * signed_target
                if determinant_lower < determinant_minimum[0]:
                    determinant_minimum = (determinant_lower, {
                        "p": p, "y": y, "row": j, "cutoff": cutoff,
                        "quotient": x / j,
                    })
                cases += 1
                if margin < -1e-11:
                    negative += 1
                if margin < minimum[0]:
                    minimum = (
                        margin,
                        {
                            "p": p,
                            "y": y,
                            "row": j,
                            "cutoff": cutoff,
                            "cutoff_fraction": cutoff_fraction,
                            "quotient": x / j,
                        },
                    )

    payload = {
        "classification": "PASS_TARGET_LORENZ_STRUCTURED_RECONNAISSANCE",
        "scope": {
            "p": ROUGH,
            "integer_y": [1, 66],
            "rows": [2, 66],
            "cases": cases,
        },
        "negative_margin_count": negative,
        "minimum_margin_decimal": minimum[0],
        "minimum_case": minimum[1],
        "minimum_full_signed_determinant_lower_bound_decimal": determinant_minimum[0],
        "minimum_full_signed_determinant_case": determinant_minimum[1],
        "proof_status": "discovery only; binary64 signs do not certify real parameter cells",
        "rh_established_by_replay": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["record_sha256"] = hashlib.sha256(canonical).hexdigest()
    out = Path("results/reconnaissance.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
