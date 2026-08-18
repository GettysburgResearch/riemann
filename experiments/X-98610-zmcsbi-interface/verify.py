#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from math import prod


def prime_factors(n: int) -> set[int]:
    out: set[int] = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def mobius(n: int) -> int:
    fs = prime_factors(n)
    if any(n % (p * p) == 0 for p in fs):
        return 0
    return -1 if len(fs) % 2 else 1


def in_semigroup(n: int, primes: set[int]) -> bool:
    return prime_factors(n) <= primes


def in_complement_semigroup(n: int, primes: set[int]) -> bool:
    return prime_factors(n).isdisjoint(primes)


def profiles(P: set[int], x: int) -> tuple[F, F, int, F, int]:
    A = sum((F(mobius(n), n) for n in range(1, x + 1) if in_semigroup(n, P)), F(0))
    N = sum(1 for n in range(1, x + 1) if in_semigroup(n, P))
    H = sum((F(1, n) for n in range(1, x + 1) if in_semigroup(n, P)), F(0))
    Nc = sum(1 for n in range(1, x + 1) if in_complement_semigroup(n, P))
    C = F(N + Nc, x) - H / x
    return A, C, N, H, Nc


def main() -> int:
    # R-98610: unconstrained contraction iff statewise ordering.
    states = [(F(5), F(3)), (F(7), F(0)), (F(9, 2), F(9, 2))]
    ratios = [F(0) if ep == 0 else em / ep for ep, em in states]
    assert all(F(0) <= q <= F(1) for q in ratios)

    # L-98610: exact Tao completion update on a nontrivial semigroup fixture.
    P = {2, 3}
    p = 5
    x = 60
    A, C, *_ = profiles(P, x)
    Ay, Cy, *_ = profiles(P, x // p)
    A2, C2, *_ = profiles(P | {p}, x)
    residual = C2 - C + F(1, p) * Cy
    assert residual >= 0
    assert A2 == A - F(1, p) * Ay
    assert (C2 + A2) - (C2 - A2) == (C + A - (C - A)) - F(1, p) * ((Cy + Ay) - (Cy - Ay))

    # L/R-98611: exact three-node countermodel.
    r = F(1, 2)
    d_v_plus = F(-1)
    d_w_minus = F(0)
    d_u_plus = F(8)
    D_u_plus = d_u_plus
    D_w_minus = d_w_minus + r * D_u_plus
    D_v_plus = d_v_plus + r * D_w_minus
    g_v_plus = d_v_plus + r * d_w_minus
    future = r * r * D_u_plus
    assert D_v_plus == F(1)
    assert g_v_plus == F(-1)
    assert future == F(2)
    assert D_v_plus == g_v_plus + future

    result = {
        "schema": "riemann.x98610.zmcsbi-interface.v1",
        "verdict": "PASS_X98610_ZMCSBI_INTERFACE_CORRECTION",
        "unconstrained_contraction_ratios": [str(q) for q in ratios],
        "tao_update": {
            "P": sorted(P), "p": p, "x": x,
            "A": str(A), "A_child": str(Ay), "A_new": str(A2),
            "C": str(C), "C_child": str(Cy), "C_new": str(C2),
            "reserve": str(residual),
        },
        "two_level_countermodel": {
            "completed_root": str(D_v_plus),
            "local_current": str(g_v_plus),
            "future_repair": str(future),
        },
        "rh_established": False,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
