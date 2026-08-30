#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
from typing import Iterable, List

CLASSIFICATION = "PASS_T108300_DIRECT_FIFTH_COMPANION_PHASE"

def trim(p: List[Fraction]) -> List[Fraction]:
    q = p[:]
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return q

def deriv(p: List[Fraction], k: int = 1) -> List[Fraction]:
    q = p[:]
    for _ in range(k):
        if len(q) <= 1:
            q = [Fraction(0)]
        else:
            q = [Fraction(i) * q[i] for i in range(1, len(q))]
    return trim(q)

def add(a: List[Fraction], b: List[Fraction], sign: int = 1) -> List[Fraction]:
    n = max(len(a), len(b))
    q = [Fraction(0)] * n
    for i in range(n):
        if i < len(a):
            q[i] += a[i]
        if i < len(b):
            q[i] += sign * b[i]
    return trim(q)

def mul(a: List[Fraction], b: List[Fraction]) -> List[Fraction]:
    q = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            q[i+j] += x*y
    return trim(q)

def scalar(a: List[Fraction], c: Fraction) -> List[Fraction]:
    return trim([c*x for x in a])

def transitions(signs: Iterable[int]) -> int:
    s = list(signs)
    return sum(1 for a, b in zip(s, s[1:]) if a != b)

def phase_negative_variation(increments: Iterable[Fraction]) -> Fraction:
    inc = list(increments)
    tv = sum(abs(x) for x in inc)
    delta = sum(inc)
    return (tv - delta) / 2

def run_checks() -> dict:
    checks = 0
    fixtures = [
        [Fraction(3), Fraction(-2), Fraction(5), Fraction(0), Fraction(-7),
         Fraction(4), Fraction(1), Fraction(-3), Fraction(2)],
        [Fraction(-1), Fraction(4), Fraction(0), Fraction(2), Fraction(-5),
         Fraction(1), Fraction(6), Fraction(0), Fraction(1), Fraction(2)],
        [Fraction(2), Fraction(0), Fraction(-3), Fraction(1), Fraction(0),
         Fraction(5), Fraction(-2), Fraction(4), Fraction(-1), Fraction(1), Fraction(1)]
    ]
    for f in fixtures:
        f1 = deriv(f, 1)
        f5 = deriv(f, 5)
        f6 = deriv(f, 6)
        W = add(mul(f1, f5), mul(f, f6), sign=-1)
        quotient_numerator = add(mul(f6, f), mul(f5, f1), sign=-1)
        assert quotient_numerator == scalar(W, Fraction(-1))
        checks += 1

    increment_fixtures = [
        [Fraction(1), Fraction(-2), Fraction(3), Fraction(-4)],
        [Fraction(-1), Fraction(-1), Fraction(2), Fraction(5, 2)],
        [Fraction(0), Fraction(7, 3), Fraction(-5, 3)]
    ]
    for inc in increment_fixtures:
        lhs = sum((-x if x < 0 else Fraction(0)) for x in inc)
        assert lhs == phase_negative_variation(inc)
        checks += 1

    seq_checks = 0
    for n in range(1, 13):
        for signs in itertools.product((-1, 1), repeat=n):
            v = transitions(signs)
            up = sum(1 for s in signs if s > 0)
            um = n - up
            assert v <= 2 * min(up, um)
            seq_checks += 1
    checks += seq_checks

    assert Fraction(9863, 10000) - Fraction(9, 10) == Fraction(863, 10000)
    assert (Fraction(9863, 10000) - Fraction(9, 10)) / 2 == Fraction(863, 20000)
    assert Fraction(997, 1000) - Fraction(9, 10) == Fraction(97, 1000)
    assert (Fraction(997, 1000) - Fraction(9, 10)) / 2 == Fraction(97, 2000)
    assert (Fraction(49, 50) - Fraction(9, 10)) / 2 == Fraction(1, 25)
    checks += 5

    c = Fraction(2)
    signs = []
    for j in range(12):
        parity = 1 if j % 2 == 0 else -1
        rho = Fraction(c + parity, -parity)
        signs.append(1 if rho > 0 else -1)
    assert signs == [-1, 1] * 6
    assert transitions(signs) == 11
    assert min(signs) == -1 and max(signs) == 1
    assert Fraction(1) + c * Fraction(-1) == Fraction(-1)
    checks += 5

    payload = {
        "schema": "riemann.x108300.direct-fifth-companion-phase.v1",
        "classification": CLASSIFICATION,
        "exact_checks": checks,
        "sign_sequences_checked": seq_checks,
        "direct_quotient_algebra_checked": True,
        "phase_negative_variation_identity_checked": True,
        "minority_transition_bound_checked": True,
        "threshold_9863": "863/20000",
        "threshold_997": "97/2000",
        "positive_fourier_countermodel_checked": True,
        "xi5minority108300_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload

def main() -> None:
    payload = run_checks()
    out = Path(__file__).parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    print(f"exact_checks={payload['exact_checks']}")

if __name__ == "__main__":
    main()
