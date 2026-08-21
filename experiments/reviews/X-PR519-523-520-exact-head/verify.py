#!/usr/bin/env python3
"""Deterministic exact-head regression for reviews of PRs #519, #523 and #520.

This checks exact finite algebra only:
- G1=3K and W1=3F;
- source and Type-II scalar normalization;
- Vaughan's +,+,-,+ identity and the strict d>U coefficient;
- cubic third-difference inversion;
- phase-lock/translation Laurent coefficients;
- the arbitrary-Delta compact-envelope counterexample;
- fixed-order exponent cancellation.

It does not prove balanced Type II, the analytic Hermite estimates, the
terminal-pair theorem or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
from fractions import Fraction as Q
from pathlib import Path

SCHEMA = "riemann.review.pr519-pr523-pr520.v1"
VERDICT = "PASS_PR519_PR523_PR520_EXACT_HEAD_REVIEW_ALGEBRA"


def trim(a: list[Q]) -> list[Q]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def scale(a: list[Q], c: Q) -> list[Q]:
    return trim([c * x for x in a])


def mul(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def eval_poly(a: list[Q], x: Q) -> Q:
    ans = Q(0)
    for c in reversed(a):
        ans = ans * x + c
    return ans


def compose_scale(a: list[Q], k: int) -> list[Q]:
    return [c * Q(k) ** i for i, c in enumerate(a)]


# K=(-x+3x^2-2x^3)/3 and G1=3K.
K = [Q(0), Q(-1, 3), Q(1), Q(-2, 3)]
G1 = [Q(0), Q(-1), Q(3), Q(-2)]
F_LEFT = add(K, scale(compose_scale(K, 4), Q(-4)))
W1_LEFT = add(G1, scale(compose_scale(G1, 4), Q(-4)))


def mobius(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def primes(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for k in range(p * p, n + 1, p):
                sieve[k] = False
    return [p for p in range(2, n + 1) if sieve[p]]


def formal_lambda(n: int) -> list[Q]:
    out = [Q(0)] * (n + 1)
    for p in primes(n):
        lp = Q((p % 17) + 2, (p % 11) + 3)
        q = p
        while q <= n:
            out[q] = lp
            if q > n // p:
                break
            q *= p
    return out


def conv(a: list[Q], b: list[Q], n: int) -> list[Q]:
    out = [Q(0)] * (n + 1)
    for d in range(1, n + 1):
        if a[d] == 0:
            continue
        for k in range(d, n + 1, d):
            out[k] += a[d] * b[k // d]
    return out


def vaughan_check(n: int, u: int, v: int) -> tuple[int, int]:
    mu_i = mobius(n)
    mu = [Q(x) for x in mu_i]
    lam = formal_lambda(n)
    one = [Q(0)] + [Q(1)] * n
    logseq = conv(lam, one, n)

    mu_small = [Q(0)] * (n + 1)
    mu_large = [Q(0)] * (n + 1)
    lam_small = [Q(0)] * (n + 1)
    lam_large = [Q(0)] * (n + 1)
    for k in range(1, n + 1):
        (mu_small if k <= u else mu_large)[k] = mu[k]
        (lam_small if k <= v else lam_large)[k] = lam[k]

    small_lam = lam_small
    mu_log = conv(mu_small, logseq, n)
    mu_lam_one = conv(conv(mu_small, lam_small, n), one, n)
    type_ii = conv(conv(mu_large, lam_large, n), one, n)

    reconstructed = [
        small_lam[k] + mu_log[k] - mu_lam_one[k] + type_ii[k]
        for k in range(n + 1)
    ]
    assert reconstructed == lam

    grouped_checks = 0
    for q in range(1, n + 1):
        a_u = sum((mu_i[d] for d in range(u + 1, q + 1) if q % d == 0), 0)
        direct = sum((mu_i[d] for d in range(1, q + 1)
                      if q % d == 0 and d > u), 0)
        assert a_u == direct
        grouped_checks += 1
    return n, grouped_checks


def K_value(x: Q) -> Q:
    return eval_poly(K, x)


def endpoint_P(c: list[Q], n: int) -> Q:
    if n <= 0:
        return Q(0)
    return 3 * Q(n) ** 3 * sum(
        (c[m] * K_value(Q(m, n)) for m in range(1, min(n, len(c) - 1) + 1)),
        Q(0),
    )


def endpoint_inversion_checks() -> int:
    rng = random.Random(519523520)
    checks = 0
    for length in range(8, 35):
        c = [Q(0)] + [Q(rng.randint(-9, 9), rng.randint(1, 9))
                       for _ in range(length + 4)]
        vals = [endpoint_P(c, n) for n in range(length + 5)]
        for n in range(1, length):
            lhs = vals[n + 3] - 3 * vals[n + 2] + 3 * vals[n + 1] - vals[n]
            rhs = Q((n + 1) * (n + 2)) * (c[n + 2] - c[n + 1])
            assert lhs == rhs
            checks += 1
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    assert G1 == scale(K, Q(3))
    assert W1_LEFT == scale(F_LEFT, Q(3))
    assert F_LEFT == [Q(0), Q(5), Q(-63), Q(170)]
    normalization_grid = 0
    for den in range(4, 101):
        for num in range(den + 1):
            x = Q(num, den)
            if x <= Q(1, 4):
                F = eval_poly(F_LEFT, x)
                W1 = eval_poly(W1_LEFT, x)
            else:
                F = eval_poly(K, x)
                W1 = eval_poly(G1, x)
            assert W1 == 3 * F
            normalization_grid += 1

    rng = random.Random(93300)
    source_checks = 0
    for n in range(2, 45):
        c = [Q(0)] + [Q(rng.randint(-7, 7), rng.randint(1, 7))
                       for _ in range(n)]
        A = sum((c[m] * K_value(Q(m, n)) for m in range(1, n + 1)), Q(0))
        A1 = sum((c[m] * eval_poly(G1, Q(m, n)) for m in range(1, n + 1)), Q(0))
        assert A1 == 3 * A
        source_checks += 1

    vaughan_records = []
    for n in (31, 48, 64, 81, 96):
        u = max(1, int(n ** (1 / 3)))
        while (u + 1) ** 3 <= n:
            u += 1
        while u**3 > n:
            u -= 1
        vaughan_records.append(vaughan_check(n, u, u))

    inversion = endpoint_inversion_checks()

    D = {-1: Q(-2), 0: Q(5), 1: Q(-2)}
    weighted = {-1: Q(-1), 0: Q(5), 1: Q(-4)}
    factor = {}
    for i, a in {0: Q(1), 1: Q(-1)}.items():
        for j, b in {0: Q(4), -1: Q(-1)}.items():
            factor[i + j] = factor.get(i + j, Q(0)) + a * b
    assert factor == weighted
    assert sum(D.values(), Q(0)) == 1

    delta_witnesses = []
    for M in (10, 100, 1000, 10000):
        t = Q(2) + Q(1, M)
        delta = 1 / abs(t - 2)
        assert delta == M
        delta_witnesses.append({"M": M, "t": str(t), "Delta_t": str(delta)})
    tail_ratios = []
    for T in (10, 100, 1000, 10000):
        ratio = (Q(1, T - 2)) / T
        assert ratio < Q(1, T)
        tail_ratios.append({"T": T, "Delta_over_t": str(ratio)})

    wedge_checks = 0
    for m in range(2, 30):
        for eps in (Q(1, 10), Q(1, 3), Q(1, 2)):
            lhs = Q(4 * m - 6, 4) - eps / 4 + Q(3, 2) - m
            assert lhs == -eps / 4
            wedge_checks += 1

    payload = {
        "schema": SCHEMA,
        "verdict": VERDICT,
        "frozen_heads": {
            "pr498": "6cc0da2fa5711017e260ebdcea4ba8c22e453288",
            "pr519": "fb15b598734546230aa51a16dda28488d214729f",
            "pr523": "f2e2e96c48285f59a8df807ba49122778cb10ff4",
            "pr520": "41db5f783c751e66c786f18fa7fbd6d9bf229a8d",
        },
        "normalization": {
            "G1_equals_3K": True,
            "W1_equals_3F": True,
            "A1_equals_3A": True,
            "grid_checks": normalization_grid,
            "source_checks": source_checks,
        },
        "vaughan": {
            "signs": ["+Lambda_small", "+mu_small*log",
                      "-mu_small*Lambda_small*1",
                      "+mu_large*Lambda_large*1"],
            "strict_divisor_cut": "d>U",
            "records": [{"N": n, "grouped_checks": g} for n, g in vaughan_records],
        },
        "endpoint_third_difference_checks": inversion,
        "phase_lock": {
            "D_coefficients": {str(k): str(v) for k, v in D.items()},
            "critical_conjugated_coefficients": {str(k): str(v) for k, v in weighted.items()},
            "factorization_verified": True,
        },
        "delta_counterexample": {
            "definition": "Delta(t)=1/|t-2| for t!=2; Delta(2)=0",
            "compact_supremum_unbounded": True,
            "witnesses": delta_witnesses,
            "tail_ratio_samples": tail_ratios,
            "repair": "use a tail supremum after a threshold",
        },
        "fixed_order_wedge_checks": wedge_checks,
        "proof_boundary": (
            "Exact finite algebra and the arbitrary-Delta logical counterexample. "
            "Does not prove balanced Type II, analytic growing-order Hermite bounds, "
            "the terminal-pair theorem, or RH."
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
