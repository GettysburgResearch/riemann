#!/usr/bin/env python3
"""Exact combinatorial replay for L-26902.

The analytic variance estimate is proved in L-26902.  This verifier checks the
integer interval, slope, wavelet-run, and constant arithmetic used by that
proof over a large finite regression range.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


N_MIN = 210
N_MAX = 520
EXPECTED_SHA256 = "fe8287748e6c2e7320ca24e8db827044d77511dc2a72e401afb91a90e11365f0"


def wavelet_value(n: int, m: int, j: int) -> Fraction:
    def g(x: int) -> Fraction:
        if m <= x < 2 * m:
            return Fraction(1)
        if 2 * m <= x < 4 * m:
            return Fraction(-1, 2)
        return Fraction(0)

    return g(n) - g(j) - g(n - j)


def build_result() -> dict[str, object]:
    row_count = 0
    slope_cells = 0
    maximum_breaks = 0
    minimum_scaled_run = Fraction(10**9)

    for n in range(N_MIN, N_MAX + 1):
        left = (n + 3) // 4
        right = (n - 2) // 3
        points = list(range(left, right + 1))
        assert len(points) * 15 >= n, ("interval length", n, len(points))

        for j in range(left, right):
            assert n - j >= 2 * (j + 1), ("slope", n, j)
            slope_cells += 1

        for m in range(1, n + 1):
            values = [wavelet_value(n, m, j) for j in points]
            runs: list[int] = []
            current = 1
            for previous, value in zip(values, values[1:]):
                if value == previous:
                    current += 1
                else:
                    runs.append(current)
                    current = 1
            runs.append(current)

            assert len(runs) <= 7, ("too many runs", n, m, len(runs))
            maximum_breaks = max(maximum_breaks, len(runs) - 1)
            longest = max(runs)
            assert longest * 105 >= n, ("run too short", n, m, longest)
            minimum_scaled_run = min(
                minimum_scaled_run, Fraction(longest * 105, n)
            )
            row_count += 1

    exact_required = 48 * 105**3
    assert 60_000_000 >= exact_required

    return {
        "schema": "X-26902-uniform-carry-schur-structure-v1",
        "checks": {
            "rows": {
                "count": row_count,
                "n_min": N_MIN,
                "n_max": N_MAX,
            },
            "central_slope_cells": {"count": slope_cells},
            "maximum_wavelet_breaks": {"count": maximum_breaks},
            "minimum_scaled_run_ratio": {
                "numerator": minimum_scaled_run.numerator,
                "denominator": minimum_scaled_run.denominator,
            },
            "reserve_denominator": {"value": 60_000_000},
            "exact_required_denominator": {"value": exact_required},
        },
        "scope": (
            "exact combinatorial structure for L-26902; no logarithmic interval "
            "evaluation, physical transference, DSS, or RH"
        ),
    }


def main() -> None:
    result = build_result()
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    if digest != EXPECTED_SHA256:
        raise AssertionError(("proof-object digest mismatch", digest, EXPECTED_SHA256))
    result["sha256_without_digest"] = digest
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).with_name("results") / "schur-structure-verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
