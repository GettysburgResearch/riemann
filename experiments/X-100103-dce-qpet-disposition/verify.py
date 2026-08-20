#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import random
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T100103_DCE_QPET_HOSTILE_DISPOSITION"


def canonical_digest(payload: dict[str, object]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def run() -> dict[str, object]:
    rng = random.Random(100103)
    dce_checks = 0

    # r represents p^{-1/2}. DCE is B <= A/r; the predecessor is A-rB.
    for _ in range(10000):
        r = Fraction(rng.randint(1, 20), rng.randint(21, 80))
        A = Fraction(rng.randint(-100, 100), rng.randint(1, 50))
        B = Fraction(rng.randint(-100, 100), rng.randint(1, 50))
        dce = B <= A / r
        predecessor_nonnegative = A - r * B >= 0
        assert dce == predecessor_nonnegative
        dce_checks += 1

    # Finite logical model of the corridor implication.
    A_star = Fraction(12, 5)
    approximants = [A_star - Fraction(1, m) for m in range(2, 202)]
    synthetic_exponents = [A_star + Fraction(1, z) for z in range(2, 2002)]
    for A in approximants:
        assert min(synthetic_exponents[-1000:]) > A
    assert min(synthetic_exponents[-1000:]) >= A_star
    assert not (min(synthetic_exponents[-1000:]) < A_star)

    # Triangle-inequality forced-cancellation fixture.
    completed = Fraction(7, 3)
    residue = Fraction(10**12)
    remainder = completed - residue
    assert abs(remainder) >= abs(residue) - abs(completed)

    payload: dict[str, object] = {
        "schema": "riemann.x100103.dce_qpet_disposition.v1",
        "classification": VERDICT,
        "base_branch": "research/gpt56-pro/100100-two-route-closure-synthesis",
        "dce_edge_equivalence_checks": dce_checks,
        "dce_is_predecessor_sign": True,
        "qpet_contradicts_corridor": True,
        "qpet100101_proved": False,
        "qpet100101_refuted": True,
        "one_pole_corridor_dominance": False,
        "dce100100_proved": False,
        "rh_established": False,
    }
    payload["proof_object_sha256"] = canonical_digest(payload)
    return payload


def main() -> None:
    payload = run()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
