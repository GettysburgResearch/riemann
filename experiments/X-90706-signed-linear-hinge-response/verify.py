#!/usr/bin/env python3
"""Exact replay for L-90705 and R-90704.

Checks the linear-hinge basis decomposition of decreasing-convex sequences,
solves the E=60 average-carry inverse exactly, and certifies c(11)=-2/55 while
all target reconstruction identities hold.

It proves no square-root weighted cancellation, CHS, or RH.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import random
from pathlib import Path

STATUS = "PASS_X_90706_SIGNED_LINEAR_HINGE_RESPONSE"


def beta(n: int, q: int) -> Fraction:
    if q > n:
        return Fraction(0)
    a, r = divmod(n, q)
    return Fraction(a * (q - 1 - r), n + 1)


def inverse(target: list[Fraction], endpoint: int) -> list[Fraction]:
    c = [Fraction(0) for _ in range(endpoint + 1)]
    for q in range(endpoint, 1, -1):
        rhs = target[q]
        for n in range(q + 1, endpoint + 1):
            rhs -= c[n] * beta(n, q)
        c[q] = rhs / beta(q, q)
    return c


def reconstruct(c: list[Fraction], endpoint: int, q: int) -> Fraction:
    return sum((c[n] * beta(n, q) for n in range(q, endpoint + 1)), Fraction())


def hinge(endpoint: int) -> list[Fraction]:
    h = [Fraction(0) for _ in range(endpoint + 2)]
    for q in range(2, endpoint + 1):
        h[q] = Fraction(endpoint + 1 - q)
    return h


def decomposition_checks() -> int:
    rng = random.Random(90706)
    checks = 0
    for endpoint in range(4, 100):
        for _ in range(20):
            # Build an arbitrary decreasing-convex sequence from nonnegative
            # second-difference weights on the linear-hinge rays.
            weights = [Fraction(0) for _ in range(endpoint)]
            for K in range(2, endpoint):
                weights[K] = Fraction(rng.randint(0, 30), rng.randint(1, 19))
            h = [Fraction(0) for _ in range(endpoint + 2)]
            for q in range(2, endpoint + 1):
                h[q] = sum(
                    (
                        weights[K] * max(K + 1 - q, 0)
                        for K in range(2, endpoint)
                    ),
                    Fraction(),
                )
            # Recover weights from second differences.
            for K in range(2, endpoint):
                recovered = h[K] - 2 * h[K + 1] + h[K + 2]
                if recovered != weights[K]:
                    raise AssertionError(("hinge weight", endpoint, K))
            checks += endpoint - 2
    return checks


def main() -> dict[str, object]:
    endpoint = 60
    h = hinge(endpoint)
    c = inverse(h, endpoint)
    row_checks = 0
    for q in range(2, endpoint + 1):
        value = reconstruct(c, endpoint, q)
        if value != h[q]:
            raise AssertionError(("row reconstruction", q, value, h[q]))
        row_checks += 1

    gates = {
        "exact_negative_hinge_response": c[11] == Fraction(-2, 55),
        "left_neighbour_positive": c[10] == Fraction(53, 45),
        "right_neighbour_positive": c[12] == Fraction(131, 33),
        "all_rows_reconstruct_exactly": row_checks == 59,
    }
    decomposition_rows = decomposition_checks()
    gates["positive_hinge_basis_decomposition"] = decomposition_rows > 50000

    if not all(gates.values()):
        raise AssertionError([name for name, ok in gates.items() if not ok])

    serialized = ";".join(
        f"{q}:{c[q].numerator}/{c[q].denominator}"
        for q in range(2, endpoint + 1)
    )
    result = {
        "status": STATUS,
        "gates": gates,
        "endpoint": endpoint,
        "witness": {
            "coefficient_index": 11,
            "coefficient": "-2/55",
            "left_neighbour": "53/45",
            "right_neighbour": "131/33",
            "inverse_vector_sha256": hashlib.sha256(serialized.encode()).hexdigest(),
        },
        "exact_reconstruction_rows": row_checks,
        "hinge_decomposition_rows": decomposition_rows,
        "scope": (
            "exact generic convex-cone counterexample and decomposition only; "
            "square-root weighted cancellation, CHS and RH remain open"
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    return result


if __name__ == "__main__":
    result = main()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(STATUS)
