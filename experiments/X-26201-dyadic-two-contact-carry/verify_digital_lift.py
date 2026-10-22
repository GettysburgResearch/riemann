#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

EXPECTED_SHA256 = "17e23d1e2ebc01cc7283d125c15c721d4743e69f906b17b715294f60b0e09b23"


def beta(n: int, q: int) -> Fraction:
    if q < 1 or q > n:
        return Fraction(0)
    k, r = divmod(n, q)
    return Fraction(k * (q - 1 - r), n + 1)


def carry(n: int, j: int, q: int) -> int:
    return int((j % q) > (n % q))


def build_result() -> dict[str, object]:
    pointwise_cases = 0
    average_cells = 0
    hermitian_rows = 0

    for n in range(1, 61):
        coeff = [Fraction(0)] * (n + 1)
        for q in range(1, n + 1):
            coeff[q] = Fraction((5 * q + 3) % 17 - 8, q + 3)

        lower_row: list[Fraction] = []
        parent_row: list[Fraction] = []
        for j in range(n + 1):
            lower = sum(
                coeff[q] * carry(n, j, q)
                for q in range(1, n + 1)
            )
            lower_row.append(lower)

            for epsilon in (0, 1):
                parent = sum(
                    coeff[q] * carry(2 * n + 1, 2 * j + epsilon, 2 * q)
                    for q in range(1, n + 1)
                )
                if parent != lower:
                    raise AssertionError(
                        ("pointwise digital lift", n, j, epsilon, parent, lower)
                    )
                parent_row.append(parent)
                pointwise_cases += 1

        for q in range(1, n + 1):
            if beta(2 * n + 1, 2 * q) != beta(n, q):
                raise AssertionError(("average digital lift", n, q))
            average_cells += 1

        lower_energy = sum(value * value for value in lower_row) / (n + 1)
        parent_energy = sum(value * value for value in parent_row) / (2 * n + 2)
        if lower_energy != parent_energy:
            raise AssertionError(
                ("Hermitian digital lift", n, lower_energy, parent_energy)
            )
        hermitian_rows += 1

    lift_cells = 0
    for Y in (8, 13, 21, 34):
        coeff = [Fraction(0)] * (Y + 1)
        for n in range(2, Y + 1):
            coeff[n] = Fraction((7 * n + 1) % 19, n + 5)

        for q in range(2, Y + 1):
            parent = sum(
                coeff[n] * beta(2 * n + 1, 2 * q)
                for n in range(q, Y + 1)
            )
            lower = sum(
                coeff[n] * beta(n, q)
                for n in range(q, Y + 1)
            )
            if parent != lower:
                raise AssertionError(("lifted packing column", Y, q, parent, lower))
            lift_cells += 1

    even_row_mutation_rejected = any(
        beta(2 * n, 2 * q) != beta(n, q)
        for n in range(2, 30)
        for q in range(1, n + 1)
    )
    if not even_row_mutation_rejected:
        raise AssertionError("even-row mutation unexpectedly passed")

    return {
        "schema": "X-26201-digital-lift-v1",
        "classification": "PASS_EXACT_ODD_ROW_EVEN_COLUMN_CARRY_ISOMETRY",
        "pointwise_duplicate_cases": pointwise_cases,
        "average_cells": average_cells,
        "hermitian_rows": hermitian_rows,
        "lift_cells": lift_cells,
        "even_row_mutation_rejected": even_row_mutation_rejected,
        "scope": (
            "finite exact digital algebra; no odd-leakage estimate, "
            "PBD, DSS, or RH conclusion"
        ),
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
    result_path = Path(__file__).with_name("results") / "digital-lift-verification.json"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
