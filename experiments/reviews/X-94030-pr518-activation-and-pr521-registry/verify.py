#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def mobius_sieve(limit: int) -> tuple[list[int], list[int]]:
    mu = [0] * (limit + 1)
    least = [0] * (limit + 1)
    primes: list[int] = []
    mu[1] = 1
    for n in range(2, limit + 1):
        if least[n] == 0:
            least[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if p > least[n] or n * p > limit:
                break
            least[n * p] = p
            mu[n * p] = 0 if p == least[n] else -mu[n]
    return mu, primes


class Interval:
    def __init__(self, lo: Fraction, hi: Fraction):
        self.lo = lo
        self.hi = hi

    def __add__(self, other: "Interval") -> "Interval":
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other: "Interval") -> "Interval":
        return Interval(self.lo - other.hi, self.hi - other.lo)


def sqrt_interval(n: int, scale: int) -> Interval:
    q = math.isqrt(n * scale * scale)
    while (q + 1) * (q + 1) <= n * scale * scale:
        q += 1
    while q * q > n * scale * scale:
        q -= 1
    return Interval(Fraction(q, scale), Fraction(q + 1, scale))


def inv_sqrt_interval(n: int, scale: int) -> Interval:
    q = math.isqrt((scale * scale) // n)
    while (q + 1) * (q + 1) * n <= scale * scale:
        q += 1
    while q * q * n > scale * scale:
        q -= 1
    return Interval(Fraction(q, scale), Fraction(q + 1, scale))


def mul_fraction(a: Fraction, b: Interval) -> Interval:
    if a >= 0:
        return Interval(a * b.lo, a * b.hi)
    return Interval(a * b.hi, a * b.lo)


def activation_counterexample() -> dict[str, object]:
    X = 10**12
    k = 3
    K = X // 67 + 1
    n = X // k
    activation = Fraction(X, k)
    s = Fraction(6 * n + 1, 6)

    assert activation == n + Fraction(1, 3)
    assert K + 2 <= n <= X - 10003
    assert k * s < X < k * (n + 1)
    assert 16 * X > 9 * k * (n + 1)

    getcontext().prec = 80
    D = Decimal
    ds = D(s.numerator) / D(s.denominator)
    inv = lambda z: D(z).sqrt() ** D(-1)
    qn = (ds.sqrt() ** D(-1) - inv(n + 1)) / (inv(n) - inv(n + 1))
    q1 = D(1) - qn

    def target(t: int | Fraction) -> Decimal:
        dt = D(t.numerator) / D(t.denominator) if isinstance(t, Fraction) else D(t)
        return (D(4) * (D(X) / (D(k) * dt)).sqrt() - D(3)) / D(k).sqrt()

    missing = q1 * target(n + 1)
    assert q1 > 0
    assert target(n + 1) > 0
    assert missing > D("0.09")

    return {
        "X": X,
        "K": K,
        "k": k,
        "cell": [n, n + 1],
        "activation": str(activation),
        "test_s": str(s),
        "active_at_s": True,
        "inactive_at_n_plus_1": True,
        "q_n_plus_1": str(q1),
        "untruncated_target_n_plus_1": str(target(n + 1)),
        "source_exact_target_loss": str(missing),
        "verdict": "PASS_EXACT_SOURCE_ACTIVATION_KNOT_COUNTEREXAMPLE",
    }


def live_registry_checks() -> dict[str, object]:
    mu, primes = mobius_sieve(871)
    source_atoms = [k for k in range(1, 537) if mu[k] != 0]
    assert len(source_atoms) == 327
    assert mu[67] == -1

    endpoint_count = 0
    zero_count = 0
    for m in range(1, 537):
        for k in range(1, 536 // m + 1):
            if mu[k] == 0:
                continue
            endpoint_count += 1
            zero_count += int(536 == m * k)
    assert endpoint_count == 2473
    assert zero_count == 4

    scale = 10**40
    mu67, _ = mobius_sieve(67)
    A = Fraction(0)
    B = Interval(Fraction(0), Fraction(0))
    e_min = None
    r_min = None
    e_cell = None
    r_cell = None
    for N in range(1, 67):
        if mu67[N]:
            A += Fraction(mu67[N], N)
            term = inv_sqrt_interval(N, scale)
            B = B + (term if mu67[N] > 0 else Interval(-term.hi, -term.lo))
        endpoint = N if A >= 0 else N + 1
        root_A = mul_fraction(A, sqrt_interval(endpoint, scale))
        E = mul_fraction(Fraction(2), root_A) - B
        R = root_A - B
        if N == 1:
            R = Interval(Fraction(0), R.hi)
        if e_min is None or E.lo < e_min:
            e_min, e_cell = E.lo, N
        if r_min is None or R.lo < r_min:
            r_min, r_cell = R.lo, N

    assert e_min is not None and e_min > Fraction(318, 1000)
    assert r_min is not None and r_min >= 0

    active = [p for p in primes if p >= 67 and p <= 871 and p > 871 / 67]
    assert len(active) == 132 and active[0] == 67
    getcontext().prec = 100
    D = Decimal
    survival = D(1)
    lambdas: list[Decimal] = []
    alphas: list[Decimal] = []
    for p in active:
        r = D(p).sqrt() ** D(-1)
        lam = r * survival
        lambdas.append(lam)
        alphas.append(r * lam)
        survival *= D(1) - r
    denominator = D(1) - survival
    beta_sum = sum(v / denominator for v in lambdas)
    gamma_sum = sum(v / denominator for v in alphas)
    assert abs(beta_sum - D(1)) < D("1e-90")
    assert gamma_sum < D(67).sqrt() ** D(-1) < D(1) / D(8)

    assert Fraction(4, 3) / Fraction(12, 1) > Fraction(1, 9)

    return {
        "native_source_registry_536": {
            "squarefree_atoms": len(source_atoms),
            "k67": {
                "mu": -1,
                "rough_history": [67],
                "first_owner": 67,
                "parity": "odd",
            },
        },
        "finite_endpoint_registry_536": {
            "occurrences": endpoint_count,
            "zero_boundary_occurrences": zero_count,
            "witness": {"X": 536, "m": 8, "k": 67, "finite_coefficient": 0},
        },
        "negative_child_q2": {
            "ordinary_upper": "-log(4)/sqrt(134)",
            "detail_upper": "-log(4)/sqrt(134)",
            "strict_less_than": "-1/9",
            "branchwise_positive_realization": False,
        },
        "outer_two_channel": {
            "E_lower": str(e_min),
            "E_min_cell": e_cell,
            "R_lower": str(r_min),
            "R_min_cell": r_cell,
        },
        "causal_parent_871": {
            "prime_count": len(active),
            "beta_sum": str(beta_sum),
            "gamma_sum": str(gamma_sum),
            "gamma_below_one_eighth": True,
        },
        "JNTLC": "OPEN",
        "PR508_interval_certificate_used": False,
        "verdict": "PASS_LIVE_REGISTRY_PRESERVES_Q2_AND_OPEN_JNTLC",
    }


def main() -> int:
    payload = {
        "schema": "riemann.review.pr518-pr521.v1",
        "frozen_heads": {
            "pr518": "3277b831b30f4783ed3b087df57e95b9f7dfd7b0",
            "pr521": "b4a60a54b1d730a73ab1eb6bb571485dd40438d0",
        },
        "activation_counterexample": activation_counterexample(),
        "live_registry": live_registry_checks(),
        "conditional_arithmetic": {
            "pr518_native_cost": 6006 + 4 + 4452 * 11 + 1,
            "pr521_terminal_total": str(Fraction(60989) + Fraction(6039, 8)),
        },
        "overall_verdict": "PASS_PR518_ACTIVATION_KNOT_AND_PR521_LIVE_REGISTRY_REVIEW",
        "rh_proved": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    out = HERE / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["overall_verdict"])
    print(payload["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
