#!/usr/bin/env python3
"""Exact Fraction-only replay of L-15626 on a supplied eigenbasis."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


def F(value: object) -> Fraction:
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    if isinstance(value, dict):
        return Fraction(int(value["numerator"]), int(value["denominator"]))
    raise TypeError(f"unsupported rational: {value!r}")


def dot(x: list[Fraction], y: list[Fraction]) -> Fraction:
    return sum((a * b for a, b in zip(x, y)), Fraction(0))


def matvec(A: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    return [dot(row, x) for row in A]


def q(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def verify(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    A = [[F(x) for x in row] for row in data["A"]]
    n = len(A)
    if n == 0 or any(len(row) != n for row in A):
        raise ValueError("A must be a nonempty square matrix")
    if any(A[i][j] != A[j][i] for i in range(n) for j in range(n)):
        raise ValueError("A must be symmetric")

    p_indices = [int(i) for i in data["p_indices"]]
    q_indices = [i for i in range(n) if i not in p_indices]
    if len(set(p_indices)) != len(p_indices) or not p_indices or not q_indices:
        raise ValueError("P/Q split must be nontrivial")

    Gamma = F(data["Gamma"])
    gamma = F(data["gamma"])
    if not gamma > Gamma:
        raise ValueError("gamma must exceed Gamma")

    # Exact Q-compression floor.
    if len(q_indices) != 1:
        raise ValueError("retained checker uses a one-dimensional Q block")
    qi = q_indices[0]
    if A[qi][qi] < gamma:
        raise ValueError("Q compression floor fails")

    pairs = []
    for item in data["eigenpairs"]:
        lam = F(item["eigenvalue"])
        vec = [F(x) for x in item["vector"]]
        if len(vec) != n or dot(vec, vec) != 1:
            raise ValueError("eigenvector must be exactly normalized")
        if matvec(A, vec) != [lam * x for x in vec]:
            raise ValueError("invalid eigenpair")
        pairs.append((lam, vec))
    if len(pairs) != n:
        raise ValueError("complete eigenbasis required")
    for i in range(n):
        for j in range(i):
            if dot(pairs[i][1], pairs[j][1]) != 0:
                raise ValueError("eigenvectors are not orthogonal")

    lhs = Fraction(0)
    for lam, vec in pairs:
        if lam < Gamma:
            qnorm2 = sum((vec[i] * vec[i] for i in q_indices), Fraction(0))
            lhs += (Gamma - lam) * qnorm2

    cross_hs2 = sum(
        (A[i][j] * A[i][j] for i in q_indices for j in p_indices),
        Fraction(0),
    )
    rhs = cross_hs2 / (4 * (gamma - Gamma))
    if lhs > rhs:
        raise ValueError("L-15626 inequality fails")

    return {
        "schema": "riemann.x15611-spectral-tail-bridge.v1",
        "classification": "EXACT_L15626_BRIDGE_PASSES",
        "low_spectral_trace": q(lhs),
        "cross_hs_squared": q(cross_hs2),
        "compression_moat": q(gamma - Gamma),
        "bridge_upper": q(rhs),
        "strict_slack": q(rhs - lhs),
    }


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} certificate.json", file=sys.stderr)
        return 2
    result = verify(Path(sys.argv[1]))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
