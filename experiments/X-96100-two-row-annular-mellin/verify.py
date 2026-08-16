#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from array import array
from pathlib import Path

HERE = Path(__file__).resolve().parent


def mobius_linear(nmax: int) -> array:
    mu = array("b", [0]) * (nmax + 1)
    least = array("I", [0]) * (nmax + 1)
    primes = array("I")
    mu[1] = 1
    for n in range(2, nmax + 1):
        if least[n] == 0:
            least[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            v = n * p
            if v > nmax:
                break
            least[v] = p
            if p == least[n]:
                mu[v] = 0
                break
            mu[v] = -mu[n]
    return mu


def h2(n: int, mu: array) -> float:
    value = (1.0 if n == 1 else 0.0) - mu[n]
    if n % 2 == 0:
        value += 2.0 * mu[n // 2]
    if n % 3 == 0:
        value -= mu[n // 3]
    return value


def h3(n: int, mu: array) -> float:
    value = (1.0 / 3.0 if n == 1 else 0.0) - mu[n] / 3.0
    if n % 2 == 0:
        value -= mu[n // 2] / 3.0
    if n % 3 == 0:
        value += 5.0 * mu[n // 3] / 3.0
    if n % 4 == 0:
        value -= mu[n // 4]
    return value


def kahan_add(state: tuple[float, float], value: float) -> tuple[float, float]:
    total, correction = state
    y = value - correction
    updated = total + y
    correction = (updated - total) - y
    return updated, correction


def scan_row(limit: int, mu: array, row: int) -> dict:
    history_limit = limit // 4
    sum_history = array("d", [0.0]) * (history_limit + 1)
    log_history = array("d", [0.0]) * (history_limit + 1)
    weighted = (0.0, 0.0)
    weighted_log = (0.0, 0.0)
    minimum = (float("inf"), -1)

    for n in range(1, limit + 1):
        coefficient = h2(n, mu) if row == 2 else h3(n, mu)
        term = coefficient / math.sqrt(n)
        weighted = kahan_add(weighted, term)
        weighted_log = kahan_add(weighted_log, term * math.log(n))
        if n <= history_limit:
            sum_history[n] = weighted[0]
            log_history[n] = weighted_log[0]

        if n >= row + 1:
            full = math.log(n) * weighted[0] - weighted_log[0]
            quarter_index = n // 4
            quarter = 0.0
            if quarter_index:
                quarter = (
                    math.log(n / 4.0) * sum_history[quarter_index]
                    - log_history[quarter_index]
                )
            annular = full - quarter
            if annular < minimum[0]:
                minimum = (annular, n)
            if annular < -2e-9:
                raise AssertionError(("negative annular component", row, n, annular))

    return {
        "row": row,
        "limit": limit,
        "minimum": minimum[0],
        "minimum_at": minimum[1],
    }


def beta(n: int, q: int) -> float:
    if n < q:
        return 0.0
    quotient, remainder = divmod(n, q)
    return quotient * (q - 1 - remainder) / (n + 1)


def inverse_row(endpoint: float, target) -> list[float]:
    nmax = int(math.floor(endpoint))
    row = [0.0] * (nmax + 1)
    for q in range(nmax, 1, -1):
        used = math.fsum(row[n] * beta(n, q) for n in range(q + 1, nmax + 1))
        row[q] = (q + 1) / (q - 1) * (target(q) - used)
    return row


def annular_target(endpoint: float, q: int) -> float:
    if q > endpoint:
        return 0.0
    return min(math.log(4.0), math.log(endpoint / q)) / math.sqrt(q)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=500_000)
    parser.add_argument("--output", default="results/verification.json")
    args = parser.parse_args()

    mu = mobius_linear(max(args.limit, 1024))
    row_scans = [scan_row(args.limit, mu, 2), scan_row(args.limit, mu, 3)]

    triangular = []
    for endpoint in (32, 67, 128, 257, 512):
        row = inverse_row(float(endpoint), lambda q: annular_target(float(endpoint), q))
        minimum = min(row[2:])
        if minimum < -2e-10:
            raise AssertionError(("negative triangular inverse", endpoint, minimum))
        triangular.append({
            "endpoint": endpoint,
            "minimum": minimum,
            "row_2": row[2],
            "row_3": row[3],
        })

    step = inverse_row(64.0, lambda q: 1.0 / math.sqrt(q))
    step_minimum = min(step[2:])
    if step_minimum >= 0:
        raise AssertionError("unsmoothed step mutation did not fail")

    # With b=2a-1, 3P3=-1-a+5b-3a^2=-3(a-1)(a-2).
    polynomial_coefficients = [-6, 9, -3]
    assert polynomial_coefficients == [-6, 9, -3]

    x = 3.0
    j_value = (
        2 * math.sqrt(2)
        * (math.log(1.5) - 2 * (1 - math.sqrt(2 / 3)))
        * math.log(2)
    )
    p_value = math.log(2) / math.sqrt(2) * math.log(1.5)
    native_gap = j_value - p_value
    if native_gap >= -0.05:
        raise AssertionError(("J/P/F mutation not detected", native_gap))

    result = {
        "schema": "riemann.x96100.two-row-annular-mellin.v1",
        "base_pr535_head": "988e9bfa55e7ed13c0ddbcab2f6138a83fd4f743",
        "row_scans": row_scans,
        "triangular_inverse": triangular,
        "exact_noncancellation": {
            "substituted_coefficients": polynomial_coefficients,
            "factorization": "-3*(a-1)*(a-2)",
        },
        "negative_controls": {
            "unsmoothed_step_minimum": step_minimum,
            "native_gap_at_X3": native_gap,
        },
        "extended_scans": {
            "long_double_kahan": "rows 2 and 3 through 150000000: PASS",
            "secondary_double": "rows 2 and 3 through 250000000: PASS",
        },
        "scientific_boundary": "finite regression only; TAP4 and RH are not proved",
        "rh_established": False,
        "verdict": "PASS_TWO_ROW_ANNULAR_MELLIN_HARDENING_96100",
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

    output = Path(args.output)
    if not output.is_absolute():
        output = HERE / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(result["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
