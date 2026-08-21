#!/usr/bin/env python3
from __future__ import annotations

from decimal import Decimal, getcontext
import hashlib
import json
from pathlib import Path

getcontext().prec = 60
ENDPOINTS = (100, 250, 500, 1000, 2000, 5000)
EXPECTED_SHA256 = "7a249c5a00cb1e5c6daa0434bcbdc40efef890f381f2ae1eb52091e8557f001e"


def mobius_table(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if n * p > limit:
                break
            composite[n * p] = True
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu


def carry_inverse(X: int) -> list[Decimal]:
    mu = mobius_table(X)
    prefix = [Decimal(0)] * (X + 1)
    prefix_log = [Decimal(0)] * (X + 1)

    for k in range(1, X + 1):
        term = Decimal(mu[k]) / Decimal(k).sqrt()
        prefix[k] = prefix[k - 1] + term
        prefix_log[k] = prefix_log[k - 1] + term * Decimal(k).ln()

    u = [Decimal(0)] * (X + 3)
    endpoint = Decimal(X)
    for m in range(1, X + 1):
        cutoff = X // m
        u[m] = (
            (endpoint / Decimal(m)).ln() * prefix[cutoff]
            - prefix_log[cutoff]
        ) / Decimal(m).sqrt()

    tail = [Decimal(0)] * (X + 4)
    for m in range(X, 0, -1):
        tail[m] = tail[m + 1] + u[m]

    profile = [Decimal(0)] * (X + 4)
    for j in range(2, X + 1):
        profile[j] = tail[j] / Decimal(j - 1)

    coeff = [Decimal(0)] * (X + 1)
    for j in range(2, X + 1):
        coeff[j] = Decimal(j + 1) * (
            profile[j] - 2 * profile[j + 1] + profile[j + 2]
        )
    return coeff


def beta(n: int, q: int) -> Decimal:
    k, r = divmod(n, q)
    return Decimal(k * (q - 1 - r)) / Decimal(n + 1)


def row_for_endpoint(X: int) -> dict[str, object]:
    coeff = carry_inverse(X)
    nonterminal = coeff[2:X]
    minimum = min(nonterminal)
    minimum_index = nonterminal.index(minimum) + 2
    negative = sum(value < 0 for value in nonterminal)

    selected = sorted({2, 3, 5, max(2, X // 4), max(2, X // 2), X - 1, X})
    endpoint = Decimal(X)
    residuals: list[Decimal] = []
    for q in selected:
        reconstructed = sum(
            coeff[n] * beta(n, q)
            for n in range(q, X + 1)
        )
        target = (endpoint / Decimal(q)).ln() / Decimal(q).sqrt()
        residuals.append(reconstructed - target)

    return {
        "X": X,
        "minimum_nonterminal_coefficient": str(minimum),
        "minimum_index": minimum_index,
        "negative_nonterminal_coefficients": negative,
        "selected_reconstruction_max_abs_residual": str(
            max(abs(value) for value in residuals)
        ),
        "c2": str(coeff[2]),
        "c3": str(coeff[3]),
    }


def build_result() -> dict[str, object]:
    return {
        "schema": "X-26201-carry-inverse-recon-v1",
        "precision_decimal_digits": 60,
        "rows": [row_for_endpoint(X) for X in ENDPOINTS],
        "classification": "DISCOVERY_ONLY_POSITIVE_CARRY_INVERSE_THROUGH_5000",
        "scope": (
            "high-precision finite reconnaissance; does not prove Carry "
            "Saturation, DSS, PBD, or RH"
        ),
    }


def main() -> None:
    result = build_result()
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    if digest != EXPECTED_SHA256:
        raise AssertionError(
            ("reconnaissance digest mismatch", digest, EXPECTED_SHA256)
        )

    result["sha256_without_digest"] = digest
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    result_path = Path(__file__).with_name("results") / "reconnaissance.json"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
