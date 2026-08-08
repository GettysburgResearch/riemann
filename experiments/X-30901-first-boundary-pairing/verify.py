#!/usr/bin/env python3
"""Exact symbolic replay for L-30901.

No transcendental values are evaluated.  A logarithmic coefficient is stored as
an integer vector on the formal basis

    log(X), log(2q-1), log(n).

The checker compares the original boundary formula with the paired `min(n,X)`
formula term by term and verifies the cutoff-interval combinatorics used in the
derivative proof.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path


@dataclass(frozen=True)
class LogCoeff:
    log_x: int = 0
    log_c: int = 0
    log_n: int = 0

    def __add__(self, other: "LogCoeff") -> "LogCoeff":
        return LogCoeff(
            self.log_x + other.log_x,
            self.log_c + other.log_c,
            self.log_n + other.log_n,
        )

    def scale(self, value: int) -> "LogCoeff":
        return LogCoeff(
            value * self.log_x,
            value * self.log_c,
            value * self.log_n,
        )


def direct_coefficient(sign: int, n: int, X: int) -> LogCoeff:
    # sign * [log(X)-log(c)-1_(n<=X)(log(X)-log(n))]
    result = LogCoeff(log_x=sign, log_c=-sign)
    if n <= X:
        result = result + LogCoeff(log_x=-sign, log_n=sign)
    return result


def paired_coefficient(sign: int, n: int, X: int) -> LogCoeff:
    # sign * [log(min(n,X))-log(c)]
    if n <= X:
        return LogCoeff(log_c=-sign, log_n=sign)
    return LogCoeff(log_x=sign, log_c=-sign)


def verify_cell(X: int, q: int, K: int) -> tuple[int, int]:
    comparisons = 0
    cutoff_intervals = 0
    previous_right = None
    for k in range(1, K + 1):
        even = 2 * k * q - 1
        odd = (2 * k + 1) * q

        assert direct_coefficient(+1, even, X) == paired_coefficient(+1, even, X)
        assert direct_coefficient(-1, odd, X) == paired_coefficient(-1, odd, X)
        comparisons += 2

        if previous_right is not None:
            assert previous_right < even
        previous_right = odd

        if even < X < odd:
            cutoff_intervals += 1

    assert cutoff_intervals <= 1
    return comparisons, cutoff_intervals


def main() -> None:
    total = 0
    crossing_cells = 0
    rows = []
    for X in (31, 64, 127, 256, 511, 1024):
        X_comparisons = 0
        X_crossings = 0
        for q in range(2, (X + 1) // 2 + 1):
            comparisons, crossings = verify_cell(X, q, 4 * X // q + 8)
            X_comparisons += comparisons
            X_crossings += crossings
        total += X_comparisons
        crossing_cells += X_crossings
        rows.append(
            {
                "X": X,
                "formal_coefficient_comparisons": X_comparisons,
                "cutoff_crossing_pairs": X_crossings,
            }
        )

    result = {
        "schema": "X-30901-first-boundary-pairing-v1",
        "classification": "PASS_EXACT_FIRST_BOUNDARY_PAIRED_LOG_IDENTITY",
        "rows": rows,
        "formal_coefficient_comparisons": total,
        "cutoff_crossing_pairs": crossing_cells,
        "checks": [
            "direct versus min-paired formal logarithm coefficients",
            "disjoint paired intervals",
            "at most one cutoff-crossing pair per output coordinate",
        ],
        "does_not_prove": [
            "the analytic derivative inequalities without the written proof",
            "CBVR",
            "Cycle Debt",
            "RH",
        ],
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    out = Path(__file__).with_name("results") / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
