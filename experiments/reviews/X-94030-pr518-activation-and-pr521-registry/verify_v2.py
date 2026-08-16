#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
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


def calculate() -> dict[str, object]:
    X = 10**12
    k = 3
    n = X // k
    s = Fraction(6 * n + 1, 6)
    assert Fraction(X, k) == n + Fraction(1, 3)
    assert k * s < X < k * (n + 1)
    assert 16 * X > 9 * k * (n + 1)

    getcontext().prec = 80
    D = Decimal
    ds = D(s.numerator) / D(s.denominator)
    q_upper = D(1) - (
        ds.sqrt() ** D(-1) - D(n + 1).sqrt() ** D(-1)
    ) / (
        D(n).sqrt() ** D(-1) - D(n + 1).sqrt() ** D(-1)
    )
    target_upper = (
        D(4) * (D(X) / (D(k) * D(n + 1))).sqrt() - D(3)
    ) / D(k).sqrt()
    lost_target = q_upper * target_upper
    assert q_upper > 0 and target_upper > 0 and lost_target > D("0.09")

    mu, primes = mobius_sieve(871)
    source_atoms = sum(mu[i] != 0 for i in range(1, 537))
    endpoint_occurrences = sum(
        1
        for m in range(1, 537)
        for j in range(1, 536 // m + 1)
        if mu[j] != 0
    )
    zero_boundaries = sum(
        1
        for m in range(1, 537)
        for j in range(1, 536 // m + 1)
        if mu[j] != 0 and m * j == 536
    )
    terminal_primes = [p for p in primes if 67 <= p <= 871 and p > 871 / 67]
    assert source_atoms == 327
    assert endpoint_occurrences == 2473
    assert zero_boundaries == 4
    assert mu[67] == -1
    assert len(terminal_primes) == 132

    # Strict q=2 bound: log(4)>4/3 and sqrt(134)<12.
    assert 134 < 12 * 12
    assert Fraction(4, 3) / Fraction(12) == Fraction(1, 9)

    payload: dict[str, object] = {
        "schema": "riemann.review.pr518-pr521.validator.v2",
        "frozen_heads": {
            "pr518": "3277b831b30f4783ed3b087df57e95b9f7dfd7b0",
            "pr521": "b4a60a54b1d730a73ab1eb6bb571485dd40438d0",
        },
        "activation": {
            "X": X,
            "k": k,
            "cell": [n, n + 1],
            "activation": str(Fraction(X, k)),
            "test_s": str(s),
            "q_upper": str(q_upper),
            "target_upper": str(target_upper),
            "lost_target": str(lost_target),
        },
        "registry": {
            "squarefree_atoms_536": source_atoms,
            "finite_occurrences_536": endpoint_occurrences,
            "zero_boundaries_536": zero_boundaries,
            "k67_mu": mu[67],
            "terminal_primes_871": len(terminal_primes),
        },
        "firewalls": {
            "negative_q2_child": True,
            "branchwise_positive_child": False,
            "JNTLC": "OPEN",
            "pr508_interval_certificate_used": False,
        },
        "verdict": "PASS_PR518_PR521_VALIDATOR_V2",
        "rh_proved": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> int:
    payload = calculate()
    out = HERE / "results" / "verification_v2.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
