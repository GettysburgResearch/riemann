#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path

VERDICT = "PASS_T99160_SAME_ROW_DEFECT_RESOLVENT_AND_OVERTHINNING_FIREWALL"


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matadd(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def matpow(a, n):
    out = eye(len(a))
    for _ in range(n):
        out = matmul(out, a)
    return out


def mobius(n):
    mu = [0] * (n + 1)
    mu[1] = 1
    primes = []
    composite = [False] * (n + 1)
    for x in range(2, n + 1):
        if not composite[x]:
            primes.append(x)
            mu[x] = -1
        for p in primes:
            if x * p > n:
                break
            composite[x * p] = True
            if x % p == 0:
                mu[x * p] = 0
                break
            mu[x * p] = -mu[x]
    return mu


def hall_gate() -> bool:
    # Directed 2^-32 enclosures for H_13(67).
    bits = 32
    scale = 1 << bits
    mu = mobius(67)

    def sqrt_interval(n):
        lo_num = isqrt(n * scale * scale)
        return Fraction(lo_num, scale), Fraction(lo_num + 1, scale)

    def invsqrt_interval(n):
        lo, hi = sqrt_interval(n)
        return 1 / hi, 1 / lo

    a = sum(Fraction(mu[k], k) for k in range(1, 14))
    b_lo = Fraction(0)
    b_hi = Fraction(0)
    for k in range(1, 14):
        if mu[k] == 0:
            continue
        lo, hi = invsqrt_interval(k)
        if mu[k] > 0:
            b_lo += lo
            b_hi += hi
        else:
            b_lo -= hi
            b_hi -= lo

    sqrt_lo, sqrt_hi = sqrt_interval(67)
    # a<0, so the lower endpoint uses sqrt_hi.
    h_lo = 4 * a * sqrt_hi - 3 * b_hi
    return h_lo > Fraction(7, 20)


def build_result():
    # Child operator on a three-state well-founded source DAG.
    t = [
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(1, 4), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1, 5), Fraction(0)],
    ]
    assert matpow(t, 3) == [[Fraction(0)] * 3 for _ in range(3)]
    assert matpow(t, 2) != [[Fraction(0)] * 3 for _ in range(3)]

    equality = [
        [Fraction(10), Fraction(4), Fraction(1)],
        [Fraction(6), Fraction(3), Fraction(1)],
    ]
    defect = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(1, 2), Fraction(0), Fraction(0)],
    ]
    current = matsub(matsub(equality, matmul(equality, t)), defect)
    assert all(x >= 0 for row in current for x in row)

    resolvent = matadd(matadd(eye(3), t), matpow(t, 2))
    source = [[Fraction(1)], [Fraction(0)], [Fraction(0)]]
    physical = matmul(matmul(current, resolvent), source)
    calibration = matmul(matmul(defect, resolvent), source)
    equality_root = matmul(equality, source)
    assert matadd(physical, calibration) == equality_root

    equality_score = 2 * equality_root[0][0] + equality_root[1][0]
    physical_score = 2 * physical[0][0] + physical[1][0]
    defect_score = 2 * calibration[0][0] + calibration[1][0]
    assert equality_score == physical_score + defect_score
    assert equality_score == 26
    assert physical_score == Fraction(47, 2)
    assert defect_score == Fraction(5, 2)

    # Voluntary overthinning creates a second row but does not erase the first.
    row_score = Fraction(100)
    capacity = Fraction(99)
    tau_constant = Fraction(99, 100)
    tau_logarithmic = Fraction(9, 10)
    assert tau_logarithmic < tau_constant
    assert tau_constant * row_score == capacity
    assert tau_logarithmic * row_score < capacity

    assert hall_gate()

    core = {
        "schema": "riemann.x99160.same-row-defect-resolvent.v1",
        "verdict": VERDICT,
        "augmented_resolvent_exact": True,
        "nilpotence_index": 3,
        "equality_score": str(equality_score),
        "physical_score": str(physical_score),
        "defect_score": str(defect_score),
        "hall_t13_x67_lower_gt": "7/20",
        "voluntary_overthinning_repairs_inherited_stronger_row": False,
        "constant_thinning_claim_must_be_withdrawn_or_defected": True,
        "same_row_lock_required": True,
        "rh_established": False,
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return core


def main():
    result = build_result()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
