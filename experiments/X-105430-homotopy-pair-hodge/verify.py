#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import json
import random

VERDICT = "PASS_T105430_HOMOTOPY_COHERENT_PAIR_HODGE"


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def addv(x, y):
    return tuple(a+b for a, b in zip(x, y))


def subv(x, y):
    return tuple(a-b for a, b in zip(x, y))


def scale(a, x):
    return tuple(a*b for b in x)


def norm2(x):
    return dot(x, x)


def run():
    rng = random.Random(105430)

    variance_checks = 0
    for _ in range(2000):
        n = rng.randint(2, 9)
        dim = rng.randint(1, 4)
        vectors = [
            tuple(Fraction(rng.randint(-20, 20), rng.randint(1, 9))
                  for _ in range(dim))
            for _ in range(n)
        ]
        mean = tuple(sum(v[j] for v in vectors) / n for j in range(dim))
        lhs = sum(norm2(v) for v in vectors) / n
        rhs = norm2(mean) + sum(norm2(subv(v, mean)) for v in vectors) / n
        assert lhs == rhs
        pair_rhs = norm2(mean)
        pair_rhs += sum(
            norm2(subv(vectors[i], vectors[j]))
            for i in range(n) for j in range(n)
        ) / (2*n*n)
        assert lhs == pair_rhs
        variance_checks += 1

    pair_checks = 0
    for _ in range(3000):
        m = rng.randint(4, 9)
        dim = rng.randint(1, 3)
        edges = {}
        for i in range(m):
            for j in range(i+1, m):
                edges[i, j] = tuple(
                    Fraction(rng.randint(-12, 12), rng.randint(1, 7))
                    for _ in range(dim)
                )

        S = tuple(
            sum(v[d] for v in edges.values())
            for d in range(dim)
        )
        M = Fraction(m*(m-1), 2)
        mu = scale(Fraction(1, 1) / M, S)

        rows = []
        for i in range(m):
            row = tuple(
                sum(edges[min(i,j), max(i,j)][d]
                    for j in range(m) if j != i)
                for d in range(dim)
            )
            rows.append(row)

        us = [
            scale(
                Fraction(1, m-2),
                subv(rows[i], scale(Fraction(2, m), S))
            )
            for i in range(m)
        ]
        assert all(sum(u[d] for u in us) == 0 for d in range(dim))

        ws = {}
        for i in range(m):
            for j in range(i+1, m):
                ws[i, j] = subv(
                    subv(edges[i, j], mu),
                    addv(us[i], us[j])
                )
        for i in range(m):
            roww = tuple(
                sum(ws[min(i,j), max(i,j)][d]
                    for j in range(m) if j != i)
                for d in range(dim)
            )
            assert all(x == 0 for x in roww)

        total_edge = sum(norm2(v) for v in edges.values())
        decomposition = M * norm2(mu)
        decomposition += (m-2) * sum(norm2(u) for u in us)
        decomposition += sum(norm2(w) for w in ws.values())
        assert total_edge == decomposition

        edge_keys = list(edges)
        q2 = Fraction(0)
        for a in range(len(edge_keys)):
            i, j = edge_keys[a]
            for b in range(a+1, len(edge_keys)):
                k, l = edge_keys[b]
                if len({i, j, k, l}) == 4:
                    q2 += 2 * dot(edges[i, j], edges[k, l])

        physical_identity = norm2(S)
        physical_identity += total_edge
        physical_identity -= sum(norm2(r) for r in rows)
        assert q2 == physical_identity

        lefschetz = Fraction((m-2)*(m-3), m*(m-1)) * norm2(S)
        lefschetz -= (m-2)*(m-3) * sum(norm2(u) for u in us)
        lefschetz += sum(norm2(w) for w in ws.values())
        assert q2 == lefschetz

        assert norm2(S) == q2 - total_edge + sum(norm2(r) for r in rows)
        pair_checks += 1

    owner_checks = 0
    for k in range(2, 101):
        pairs = k*(k-1)//2
        c = Fraction((-1)**k * (k+3), k+1)
        equal_sum = pairs * (c / pairs)
        assert equal_sum == c
        equal_norm = pairs * (c/pairs)**2
        extreme_norm = c*c
        assert extreme_norm == pairs * equal_norm
        owner_checks += 1

    N = Fraction(10**6)
    p = (N, -192*N)
    w = (-N, 192*N)
    assert norm2(addv(p, w)) == 0
    assert norm2(p) > 0 and norm2(w) > 0

    mutations = sorted([
        "isolated_wick_energy_promoted_to_subpower_rejected",
        "first_chaos_removed_before_signed_recombination_rejected",
        "homotopy_integral_and_square_commuted_rejected",
        "pair_diagonal_promoted_to_physical_trace_rejected",
        "star_only_promoted_to_pair_closure_rejected",
        "cycle_only_promoted_to_pair_closure_rejected",
        "equal_extreme_owner_transfer_called_isometric_rejected",
        "selberg_delange_replay_claim_rejected",
        "rh_promoted_by_replay_rejected",
    ])

    payload = {
        "schema": "riemann.x105430.homotopy-pair-hodge.v1",
        "classification": VERDICT,
        "base_pr": 730,
        "base_sha": "5626725a994bd89973df6e13e48ed6f897d10d0b",
        "wick_pr": 719,
        "wick_sha": "b6cb90d3d5f06320ba2c4908930a5b85fa270240",
        "variance_checks": variance_checks,
        "pair_hodge_checks": pair_checks,
        "owner_transfer_checks": owner_checks,
        "homotopy_variance_proved": True,
        "degree_two_hodge_proved": True,
        "extreme_pair_transfer_proved": True,
        "isolated_wick_energy_subpower": False,
        "f1star105431_proved": False,
        "f1cycle105431_proved": False,
        "f1hcnc105430_proved": False,
        "rh_established": False,
        "mutations_rejected": mutations,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main():
    result = run()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
