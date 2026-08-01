#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent


def q(obj: dict[str, str]) -> Fraction:
    return Fraction(int(obj["numerator"]), int(obj["denominator"]))


def matmul(
    A: list[list[Fraction]], B: list[list[Fraction]]
) -> list[list[Fraction]]:
    if not A or not B or len(A[0]) != len(B):
        raise ValueError("dimension mismatch")
    return [
        [
            sum(A[i][k] * B[k][j] for k in range(len(B)))
            for j in range(len(B[0]))
        ]
        for i in range(len(A))
    ]


def identity(n: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def main() -> None:
    path = ROOT / "certificates" / "synthetic.json"
    raw = path.read_bytes()
    data: dict[str, Any] = json.loads(raw)

    G = [q(x) for x in data["G_diag"]]
    D = [q(x) for x in data["D_diag"]]
    K = [q(x) for x in data["K_diag"]]
    M = q(data["M"])
    ell = q(data["ell"])
    n = len(G)

    if not (len(D) == len(K) == n and n > 0):
        raise AssertionError("diagonal lengths")
    if any(x <= 0 for x in G) or any(x < 0 for x in D + K):
        raise AssertionError("positivity")

    tau = Fraction(1, 1) / (ell * ell)
    B = M * ell

    if any(K[i] > M * M * G[i] for i in range(n)):
        raise AssertionError("unwhitened graph envelope")

    # K <= B^2 (D + tau G), using B^2 tau = M^2.
    if any(K[i] > B * B * (D[i] + tau * G[i]) for i in range(n)):
        raise AssertionError("regularized complete-frame envelope")

    core = set(int(i) for i in data["core_indices"])
    residual = [i for i in range(n) if i not in core]
    soft = [i for i in residual if D[i] <= tau * G[i]]
    good = [i for i in residual if D[i] > tau * G[i]]

    if not soft or not good:
        raise AssertionError("synthetic split must be nontrivial")
    if any(D[i] > tau * G[i] for i in soft):
        raise AssertionError("soft-tail absorption")
    if any(D[i] < tau * G[i] for i in good):
        raise AssertionError("good tail floor")
    if any(K[i] > B * B * D[i] for i in good):
        raise AssertionError("actual D-whitened good-frame envelope")

    L = [[q(x) for x in row] for row in data["localization_matrix"]]
    F = [[q(x) for x in row] for row in data["source_synthesis_matrix"]]
    if matmul(L, F) != identity(n):
        raise AssertionError("exact source right inverse")

    soft_trace = sum(D[i] / G[i] for i in soft)
    good_floor = min(D[i] / G[i] for i in good)
    good_envelope_sq = max(K[i] / D[i] for i in good)

    result = {
        "schema": "riemann.x15612-soft-tail-conditioning.result.v1",
        "classification": "EXACT_CORE_PLUS_SOFT_ABSORPTION_FRAME_PASSES",
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "dimension": n,
        "core_indices": sorted(core),
        "soft_indices": soft,
        "dangerous_complement_indices": good,
        "tau": {
            "numerator": str(tau.numerator),
            "denominator": str(tau.denominator),
        },
        "B": {
            "numerator": str(B.numerator),
            "denominator": str(B.denominator),
        },
        "soft_profile_trace": {
            "numerator": str(soft_trace.numerator),
            "denominator": str(soft_trace.denominator),
        },
        "dangerous_profile_floor": {
            "numerator": str(good_floor.numerator),
            "denominator": str(good_floor.denominator),
        },
        "dangerous_envelope_squared": {
            "numerator": str(good_envelope_sq.numerator),
            "denominator": str(good_envelope_sq.denominator),
        },
        "verdict": "PASS_EXACT_L15630_CONDITIONING_SPLIT",
    }

    out = ROOT / "results" / "synthetic-verification.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
