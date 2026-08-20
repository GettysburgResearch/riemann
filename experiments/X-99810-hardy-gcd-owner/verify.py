#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

VERDICT = "PASS_T99810_HARDY_GCD_OWNER_SQUARE_INTEGRATORS"


def phi(n: int) -> int:
    x = n
    out = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            out = out // p * (p - 1)
        p += 1
    if x > 1:
        out = out // x * (x - 1)
    return out


def run() -> dict:
    # tau=1/2, hence the minimum kernel exponent is one.
    nodes = [2, 5, 9]
    coeff = [F(3), F(-1), F(2)]
    q_min = sum(
        coeff[i] * coeff[j] * min(nodes[i], nodes[j])
        for i in range(len(nodes)) for j in range(len(nodes))
    )

    q_tail = sum(coeff) ** 2
    previous = 1
    for i, n in enumerate(nodes):
        tail = sum(coeff[i:])
        q_tail += (n - previous) * tail * tail
        previous = n
    assert q_min == q_tail == 51

    q_gcd = sum(
        coeff[i] * coeff[j] * math.gcd(nodes[i], nodes[j])
        for i in range(len(nodes)) for j in range(len(nodes))
    )
    q_jordan = F(0)
    for d in range(1, max(nodes) + 1):
        divisor_tail = sum(c for n, c in zip(nodes, coeff) if n % d == 0)
        q_jordan += phi(d) * divisor_tail * divisor_tail
    assert q_gcd == q_jordan == 61

    # Exact hazard partition and Hilbert-space Jensen fixture.
    r1, r2 = F(1, 3), F(1, 5)
    weights = [(1 - r1) * (1 - r2), r1, r2 * (1 - r1)]
    assert sum(weights) == 1
    vectors = [[F(2), F(-1)], [F(-3), F(4)], [F(5), F(1)]]
    barycenter = [
        sum(weights[k] * vectors[k][j] for k in range(3))
        for j in range(2)
    ]
    lhs = sum(x * x for x in barycenter)
    rhs = sum(
        weights[k] * sum(x * x for x in vectors[k])
        for k in range(3)
    )
    assert lhs == F(317, 225)
    assert rhs == F(217, 15)
    assert lhs <= rhs

    # Distinct clustered integer frequencies: exact diagonal firewall.
    N = 64
    dense_nodes = [N ** 3 + j for j in range(1, N + 1)]
    dense_q = sum(min(m, n) for m in dense_nodes for n in dense_nodes)
    dense_diagonal = sum(dense_nodes)
    dense_ratio = F(dense_q, dense_diagonal)
    assert dense_ratio == F(33557227, 524353)
    assert dense_ratio > 63

    core = {
        "schema": "riemann.x99810.hardy-gcd-owner.v1",
        "classification": VERDICT,
        "base_pr": 659,
        "base_sha": "83c17b32a99ac9e1aa5aec3168535550eb286636",
        "imported_first_owner_pr": 660,
        "imported_first_owner_sha": "ca3c055307e6804ae904cb9105594dd3f2408ba3",
        "poisson_min_kernel": str(q_min),
        "hardy_tail_square": str(q_tail),
        "gcd_quadratic": str(q_gcd),
        "jordan_divisor_square": str(q_jordan),
        "hazard_weights": [str(w) for w in weights],
        "hazard_jensen_lhs": str(lhs),
        "hazard_jensen_rhs": str(rhs),
        "distinct_cluster_size": N,
        "dense_q_over_diagonal": str(dense_ratio),
        "dense_ratio_gt_63": True,
        "htoc99810_proved": False,
        "dgoc99810_proved": False,
        "gpmoc99800_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    return {**core, "proof_object_sha256": hashlib.sha256(canonical).hexdigest()}


def main() -> None:
    result = run()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
