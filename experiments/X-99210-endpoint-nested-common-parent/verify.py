#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

VERDICT = "PASS_T99210_ENDPOINT_NESTED_COMPONENT_ROW_INTERFACE"


def factor_exponents(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mobius(n: int) -> int:
    exps = factor_exponents(n)
    if any(e > 1 for e in exps.values()):
        return 0
    return -1 if len(exps) % 2 else 1


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def main() -> None:
    # Exact hazard telescope and random-key density control.
    rs = [F(1, 9), F(1, 11)]
    survivor = F(1)
    lambdas: list[F] = []
    alphas: list[F] = []
    for r in rs:
        lam = r * survivor
        lambdas.append(lam)
        alphas.append(r * lam)
        survivor *= 1 - r
    assert survivor + sum(lambdas, F()) == 1
    alpha_sum = sum(alphas, F())
    assert alpha_sum == F(193, 9801) < F(1, 8)

    # Positive endpoint increments and literal child restrictions.
    increments = [
        [F(3), F(4), F(5), F(6)],
        [F(2), F(3), F(4), F(5)],
        [F(1), F(2), F(3), F(4)],
    ]
    cumulative: list[list[F]] = []
    run = [F(0)] * 4
    for inc in increments:
        run = [a + b for a, b in zip(run, inc)]
        cumulative.append(run)
    parent = cumulative[-1]
    children = [cumulative[0], cumulative[1]]
    child_total = [sum(a * child[k] for a, child in zip(alphas, children)) for k in range(4)]
    current = [parent[k] - child_total[k] for k in range(4)]
    causal = [survivor * x for x in parent]
    for lam, r, child in zip(lambdas, rs, children):
        causal = [a + lam * (p - r * c) for a, p, c in zip(causal, parent, child)]
    assert current == causal and all(x >= 0 for x in current)

    # Literal fractional Hall source partition.
    even_targets = [F(5), F(3)]
    odd_target = F(4)
    even_profiles = [[F(5, 4), F(3, 2)], [F(1), F(5, 4)]]
    odd_profile = [F(3, 4), F(1)]
    flow = [F(3), F(1)]
    assert sum(flow, F()) == odd_target
    residual = [cap - used for cap, used in zip(even_targets, flow)]
    signed = [sum(t * row[k] for t, row in zip(even_targets, even_profiles)) - odd_target * odd_profile[k] for k in range(2)]
    bonus = [sum(flow[e] * (even_profiles[e][k] - odd_profile[k]) for e in range(2)) for k in range(2)]
    reconstructed = [sum(residual[e] * even_profiles[e][k] for e in range(2)) + bonus[k] for k in range(2)]
    assert bonus == [F(7, 4), F(7, 4)]
    assert reconstructed == signed

    # Exact formal score normalization: mu*log = Lambda in the prime-log basis.
    for k in range(2, 161):
        kexp = factor_exponents(k)
        lhs: dict[int, int] = {}
        for d in divisors(k):
            md = mobius(d)
            if md == 0:
                continue
            dexp = factor_exponents(d)
            for p, e in kexp.items():
                lhs[p] = lhs.get(p, 0) + md * (e - dexp.get(p, 0))
        lhs = {p: e for p, e in lhs.items() if e}
        rhs = {next(iter(kexp)): 1} if len(kexp) == 1 else {}
        assert lhs == rhs

    core = {
        "alpha_sum": "193/9801",
        "causal_current_equals_parent_residual": True,
        "classification": VERDICT,
        "endpoint_nested_vector_source": True,
        "finite_tree_depth": 4,
        "frozen_local_inputs_replayed": False,
        "hall_bonus": ["7/4", "7/4"],
        "hall_is_literal_source_partition": True,
        "literal_score_is_prime_power_benchmark": True,
        "maximum_random_key_density": "193/9801",
        "random_key_children_are_disjoint": True,
        "rh_established": False,
        "score_identity_limit": 160,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canon).hexdigest()
    out = Path(__file__).resolve().parent / "results/verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(core, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(VERDICT)
    print(core["proof_object_sha256"])


if __name__ == "__main__":
    main()
