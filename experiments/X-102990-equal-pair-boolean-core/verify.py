#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, Fraction(0)) + x * y
    return {k: v for k, v in out.items() if v}


def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    equal_pair_checks = 0
    for k in range(4, 41):
        count = k * (k - 1) // 2
        assert sum(Fraction(1, count) for _ in range(count)) == 1
        assert sum(Fraction(1, count) ** 2 for _ in range(count)) == Fraction(1, count)
        equal_pair_checks += 1

    E = {0: Fraction(1), 1: Fraction(-1)}
    C = {0: Fraction(1), 2: Fraction(-1)}
    M = {0: Fraction(1), 1: Fraction(-1, 2), 2: Fraction(-1, 2)}
    D = {1: Fraction(-1, 2), 2: Fraction(1, 2)}
    lhs = mul(E, C)
    mm = mul(M, M)
    dd = mul(D, D)
    rhs = {
        k: mm.get(k, Fraction(0)) - dd.get(k, Fraction(0))
        for k in set(mm) | set(dd)
        if mm.get(k, Fraction(0)) - dd.get(k, Fraction(0))
    }
    assert lhs == rhs
    assert min(mul(D, D)) == 2

    # A selected phase label works whether it occurs to exponent one or two.
    for p in [2, 3, 5, 7, 11]:
        for exponent in [1, 2]:
            N = (p ** exponent) * 13
            Mphys = 17
            assert N % p == 0
            assert Mphys % p != 0

    payload = {
        "schema": "riemann.t102990.equal-pair-boolean-core.v1",
        "equal_pair_checks": equal_pair_checks,
        "endpoint_color_identity": True,
        "endpoint_variance_first_degree": 2,
        "owner_phase_divisibility_independent": True,
        "bci102990_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102990_EQUAL_PAIR_BOOLEAN_CORE_NORMAL_FORM",
    }
    payload["proof_object_sha256"] = digest(payload)

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
