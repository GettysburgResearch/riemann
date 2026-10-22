#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

EXPECTED_SHA256 = "395a7a89ea2267cfa5a3b805ead2646fa46a1761408f6ff048fed7b2e218757f"


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


MU = mobius_table(200)


def b2(n: int) -> int:
    return MU[n] - (MU[n // 2] if n % 2 == 0 else 0)


def divisor_gradient(X: int, coeff: list[Fraction], q: int) -> Fraction:
    return sum(
        coeff[m]
        * (
            (1 if m % q == 0 else 0)
            - (1 if (m - 1) % q == 0 else 0)
        )
        for m in range(2, X + 1)
    )


def flow_delta(X: int, flow: list[Fraction], q: int) -> Fraction:
    return sum(
        flow[j]
        * (
            (1 if (j + 1) % q == 0 else 0)
            - 2 * (1 if j % q == 0 else 0)
            + (1 if (j - 1) % q == 0 else 0)
        )
        for j in range(2, X)
    )


def fraction_json(value: Fraction) -> dict[str, int]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


def build_result() -> dict[str, object]:
    rows: list[dict[str, object]] = []

    for X in (17, 29, 43):
        coeff = [Fraction(0)] * (X + 1)
        for m in range(2, X + 1):
            coeff[m] = Fraction(
                (7 * m + 5) % 17 - 8,
                (m + 3) * (X + 2),
            )

        projection = sum(
            Fraction(b2(q)) * divisor_gradient(X, coeff, q)
            for q in range(2, X + 1)
        )
        expected_projection = -2 * coeff[2] + coeff[3]
        if projection != expected_projection:
            raise AssertionError(
                ("bottom charge projection", X, projection, expected_projection)
            )

        flow = [Fraction(0)] * (X + 1)
        for j in range(2, X):
            flow[j] = Fraction(
                (3 * j + 1) % 11 - 5,
                (j + 2) * (X + 5),
            )

        bottom_delta = sum(
            Fraction(b2(q)) * flow_delta(X, flow, q)
            for q in range(2, X + 1)
        )
        expected_bottom = 3 * flow[2] - flow[3]
        if bottom_delta != expected_bottom:
            raise AssertionError(
                ("bottom flow delta", X, bottom_delta, expected_bottom)
            )

        high_flow = [Fraction(0)] * (X + 1)
        for j in range(4, X):
            high_flow[j] = Fraction(
                (5 * j + 2) % 13 - 6,
                (j + 1) * (X + 7),
            )

        high_delta = sum(
            Fraction(b2(q)) * flow_delta(X, high_flow, q)
            for q in range(2, X + 1)
        )
        if high_delta != 0:
            raise AssertionError(("high-index flow is visible", X, high_delta))

        rows.append(
            {
                "X": X,
                "projection": fraction_json(projection),
                "bottom_flow_delta": fraction_json(bottom_delta),
                "high_index_flow_delta": fraction_json(high_delta),
            }
        )

    return {
        "schema": "X-26201-bottom-charge-v1",
        "classification": (
            "PASS_EXACT_DYADIC_BOTTOM_CHARGE_AND_FLOW_INVISIBILITY"
        ),
        "rows": rows,
        "scope": "finite exact algebra; no DSS, PBD, or RH conclusion",
    }


def main() -> None:
    result = build_result()
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    if digest != EXPECTED_SHA256:
        raise AssertionError(
            ("proof-object digest mismatch", digest, EXPECTED_SHA256)
        )

    result["sha256_without_digest"] = digest
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    result_path = Path(__file__).with_name("results") / "bottom-charge-verification.json"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
