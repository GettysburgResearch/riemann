#!/usr/bin/env python3
"""Exact algebra replay for L-91702 and the R-91701 countermodel.

This checker deliberately does not claim to verify the arithmetic root Hall
identity.  It verifies, with Fraction arithmetic, that once positive post-Hall
sources and a literal parent-row identity are supplied, endpoint-monotone
component rows give a nonnegative current row, exact row/response/score
telescopes, and capacity-faithful child replacement.
"""
from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import random


def add(a: list[F], b: list[F]) -> list[F]:
    return [x + y for x, y in zip(a, b)]


def sub(a: list[F], b: list[F]) -> list[F]:
    return [x - y for x, y in zip(a, b)]


def scale(c: F, a: list[F]) -> list[F]:
    return [c * x for x in a]


def response(row: list[F], matrix: list[list[F]]) -> list[F]:
    return [sum(x * a for x, a in zip(row, col)) for col in matrix]


def score(row: list[F], g: list[F]) -> F:
    return sum(x * y for x, y in zip(row, g))


def run() -> dict[str, object]:
    # R-91701 exact countermodel.
    native = [F(1), F(1)]
    recursive = [F(2), F(0)]
    current = sub(native, recursive)
    assert add(current, recursive) == native
    assert sum(current) == 0
    assert current[0] < 0

    rng = random.Random(91702)
    trials = 2500
    rows = 17
    columns = 23
    checks = 4

    for _ in range(trials):
        # Build endpoint-monotone component rows Q_child <= Q_parent exactly.
        q_child = [F(rng.randint(0, 30), rng.randint(1, 11)) for _ in range(rows)]
        increment = [F(rng.randint(0, 30), rng.randint(1, 11)) for _ in range(rows)]
        q_parent = add(q_child, increment)

        coefficient = F(rng.randint(0, 30), rng.randint(1, 13))
        bonus = [F(rng.randint(0, 15), rng.randint(1, 13)) for _ in range(rows)]

        parent = add(scale(coefficient, q_parent), bonus)
        child = scale(coefficient, q_child)
        cur = sub(parent, child)

        assert all(x >= 0 for x in cur)
        assert add(cur, child) == parent
        checks += 2 * rows

        # Arbitrary exact linear ordinary/detail response maps.  Entries may be
        # signed, as a radix-four difference is a signed linear functional.
        ordinary = [
            [F(rng.randint(0, 15), rng.randint(1, 13)) for _ in range(rows)]
            for _ in range(columns)
        ]
        detail = [
            [F(rng.randint(-15, 15), rng.randint(1, 13)) for _ in range(rows)]
            for _ in range(columns)
        ]

        for matrix in (ordinary, detail):
            rp = response(parent, matrix)
            rc = response(cur, matrix)
            rh = response(child, matrix)
            assert add(rc, rh) == rp
            checks += columns

        # Capacity-faithful replacement is checked at the response-ledger level:
        # any child use below its exact child capacity leaves parent use below
        # the parent capacity after the exact current capacity is added.
        child_cap = response(child, ordinary)
        fractions = [F(rng.randint(0, 20), 20) for _ in range(columns)]
        child_use = [t * c for t, c in zip(fractions, child_cap)]
        cur_cap = response(cur, ordinary)
        parent_cap = response(parent, ordinary)
        assembled_use = add(cur_cap, child_use)
        assert all(u <= p for u, p in zip(assembled_use, parent_cap))
        checks += columns

        g = [F(rng.randint(0, 20), rng.randint(1, 13)) for _ in range(rows)]
        assert score(parent, g) == score(cur, g) + score(child, g)
        checks += 1

    result = {
        "classification": "PASS_POST_HALL_POSITIVE_SOURCE_CURRENT_LEDGER",
        "trials": trials,
        "exact_fraction_checks": checks,
        "countermodel_scalar_complement_row_negative": True,
        "current_row_nonnegative_from_endpoint_monotonicity": True,
        "ordinary_response_telescope": True,
        "radix_four_linear_telescope": True,
        "capacity_faithful_child_replacement": True,
        "literal_score_telescope": True,
        "scope": (
            "Exact Fraction replay of the algebra in R-91701/L-91702. "
            "The arithmetic root Hall identity O-91703.2 is a cited proof gate "
            "and is not replaced by these synthetic exact tests."
        ),
    }
    return result


def main() -> None:
    result = run()
    here = Path(__file__).resolve().parent
    out = here / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    print(result["classification"])
    print(f"result_sha256={digest}")
    print(out)


if __name__ == "__main__":
    main()
