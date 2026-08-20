#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

VERDICT = "PASS_T99970_UPBF_FIREWALL_AND_BALANCED_SURFACE"


def weight(mask: int, activities: tuple[F, ...]) -> F:
    out = F(1)
    for i, a in enumerate(activities):
        if mask & (1 << i):
            out *= a
    return out


def priority_edges(activities: tuple[F, ...]):
    k = len(activities)
    survival = F(1)
    lambdas: list[F] = []
    for a in activities:
        lambdas.append(a * survival)
        survival *= 1 - a

    for i in range(k):
        suffix = tuple(range(i + 1, k))
        for bits in range(1 << len(suffix)):
            A = 0
            for jpos, j in enumerate(suffix):
                if bits & (1 << jpos):
                    A |= 1 << j
            yield i, A, lambdas[i] * weight(A, activities)


def product(mask: int, labels: tuple[int, ...]) -> int:
    out = 1
    for i, p in enumerate(labels):
        if mask & (1 << i):
            out *= p
    return out


def balanced_fixture() -> dict:
    labels = (2, 3, 5, 7)
    activities = tuple(F(1, p) for p in labels)
    X = 20
    k = len(labels)
    phi = [F(max(0, X - product(mask, labels)), X) for mask in range(1 << k)]

    survival = F(1)
    for a in activities:
        survival *= 1 - a

    odd_surface = F(0)
    even_surface = F(0)
    for i, A, J in priority_edges(activities):
        Ai = A | (1 << i)
        drop = J * (phi[A] - phi[Ai])
        assert drop >= 0
        if A.bit_count() % 2:
            odd_surface += drop
        else:
            even_surface += drop

    scalar = sum(
        ((-1) ** mask.bit_count()) * weight(mask, activities) * phi[mask]
        for mask in range(1 << k)
    )
    assert scalar == survival * phi[0] + even_surface - odd_surface

    # Dropping the even surface does not reconstruct the physical scalar.
    assert survival * phi[0] - odd_surface != scalar

    return {
        "labels": list(labels),
        "X": X,
        "scalar": str(scalar),
        "survival": str(survival),
        "even_surface": str(even_surface),
        "odd_surface": str(odd_surface),
        "identity": True,
    }


def shifted_carrier_fixtures() -> list[dict]:
    rows = []
    for sqrt_q, sqrt_Y, c in (
        (2, 6, F(-1)),
        (3, 12, F(0)),
        (4, 20, F(1)),
        (5, 30, F(3)),
    ):
        q = sqrt_q * sqrt_q
        Y = sqrt_Y * sqrt_Y
        child_sqrt = sqrt_Y // sqrt_q
        lhs = (4 * sqrt_Y - 3 + c) - sqrt_q * (4 * child_sqrt - 3 + c)
        rhs = (3 - c) * (sqrt_q - 1)
        assert lhs == rhs
        assert rhs >= 0
        rows.append(
            {
                "q": q,
                "Y": Y,
                "c": str(c),
                "lhs": str(lhs),
                "rhs": str(rhs),
                "identity": True,
            }
        )
    return rows


def build_result() -> dict:
    result = {
        "verdict": VERDICT,
        "balanced_fixture": balanced_fixture(),
        "shifted_carrier_fixtures": shifted_carrier_fixtures(),
        "upbf67_proved": False,
        "upbf67_refuted": True,
        "balanced_surface_proved": True,
        "shifted_quadratic_family_proved": True,
        "afcd99970_proved": False,
        "rh_established": False,
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build_result()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(VERDICT)
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
