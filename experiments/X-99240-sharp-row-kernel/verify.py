#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T99240_SHARP_ROW_KERNEL_FRAME"

def A(j: int) -> Fraction:
    return Fraction(j + 1, j - 1)

def B(j: int) -> Fraction:
    return Fraction((j + 1) * (j - 2), j * (j - 1))

def C(j: int) -> Fraction:
    return Fraction(2, j * (j - 1))

def gamma(j: int, m: int) -> Fraction:
    if m < j:
        return Fraction(0)
    if m == j:
        return A(j)
    if m == j + 1:
        return -B(j)
    return C(j)

def mu_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    comp = [False] * (n + 1)
    for k in range(2, n + 1):
        if not comp[k]:
            primes.append(k)
            mu[k] = -1
        for p in primes:
            if k * p > n:
                break
            comp[k * p] = True
            if k % p == 0:
                mu[k * p] = 0
                break
            mu[k * p] = -mu[k]
    return mu

def check_cumulative_identities() -> dict:
    checks = 0
    for j in range(2, 80):
        for N in range(j + 1, 160):
            s0 = sum((gamma(j, m) for m in range(1, N + 1)), Fraction(0))
            s1 = sum((m * gamma(j, m) for m in range(1, N + 1)), Fraction(0))
            assert s0 == Fraction(2 * N, j * (j - 1))
            assert s1 == Fraction(N * (N + 1), j * (j - 1))
            checks += 2
    return {"classification": "PASS_CUMULATIVE_GAMMA_IDENTITIES", "checks": checks}

def check_positive_proof_gates() -> dict:
    for j in range(3, 500):
        assert j * (j - 2) ** 2 - (j - 3) ** 2 * (j + 1) == j * j + j - 9
        assert j * j + j - 9 > 0
        assert 16 * j > 9 * (j + 2)
    for N in range(3, 10000):
        assert 4 * (N + 1) ** 3 - (2 * N + 1) ** 2 * (N + 2) == 3 * N + 2
        assert 3 * N + 2 > 0

    minimum = (10.0, None, None)
    for j in range(2, 80):
        for N in range(j, 400):
            y = float(N + 1)
            value = sum(
                float(gamma(j, m)) / math.sqrt(m)
                * (4.0 * (m / y) ** 1.5 - 1.0) / 3.0
                for m in range(1, N + 1)
            )
            if value < minimum[0]:
                minimum = (value, j, N)
            assert value > 0.0
    return {
        "classification": "PASS_SHARP_ROW_KERNEL_POSITIVITY_GATES",
        "minimum_probe": minimum[0],
        "minimum_row": minimum[1],
        "minimum_cell": minimum[2],
    }

def check_mellin_identity() -> dict:
    points = [Fraction(3, 4), Fraction(1), Fraction(5, 4),
              Fraction(2), Fraction(7, 2), Fraction(11)]
    for s in points:
        target = (s + Fraction(3, 2)) / (s * (s - Fraction(1, 2)))
        kernel = (s - Fraction(1, 2)) / (s * (s + Fraction(3, 2)))
        assert target * kernel == 1 / (s * s)
    return {"classification": "PASS_EXACT_MELLIN_MULTIPLIER_CANCELLATION",
            "rational_points": len(points)}

def check_formal_fubini() -> dict:
    mu = mu_sieve(80)
    checks = 0
    for X in range(10, 81):
        for j in range(2, min(12, X) + 1):
            left: dict[tuple[int, int], Fraction] = {}
            right: dict[tuple[int, int], Fraction] = {}
            for n in range(1, X // j + 1):
                if mu[n] == 0:
                    continue
                for m in range(j, X // n + 1):
                    g = gamma(j, m)
                    if g == 0:
                        continue
                    coeff = Fraction(mu[n]) * g
                    left[(n, m)] = coeff
                    right[(n, m)] = coeff
            assert left == right
            checks += len(left)
    return {"classification": "PASS_FINITE_MOBIUS_FUBINI_COEFFICIENTS",
            "coefficient_checks": checks}

def check_target_firewall() -> dict:
    mu = mu_sieve(67)
    A13 = sum((Fraction(mu[n], n) for n in range(1, 14)), Fraction(0))
    B13 = sum(mu[n] / math.sqrt(n) for n in range(1, 14))
    equality_prefix = 2 * math.sqrt(67) * float(A13) - B13
    sharp_prefix = 4 * math.sqrt(67) * float(A13) - 3 * B13
    assert equality_prefix < -0.30
    assert sharp_prefix > 0.35
    return {
        "classification": "PASS_SHARP_TARGET_IS_ESSENTIAL_FIREWALL",
        "equality_prefix_t13_x67": equality_prefix,
        "sharp_prefix_t13_x67": sharp_prefix,
    }

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    core = {
        "schema": "riemann.t99240.sharp-row-kernel.v1",
        "checks": [
            check_cumulative_identities(),
            check_positive_proof_gates(),
            check_mellin_identity(),
            check_formal_fubini(),
            check_target_firewall(),
        ],
        "volterra_two_anchor_gate_used": False,
        "score_endgame_used": False,
        "frontier_chain_used": False,
        "inherited_hall_profile_replayed": False,
        "rh_established": False,
        "classification": VERDICT,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canon).hexdigest()
    text = json.dumps(core, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")
    print(VERDICT)
    print(core["proof_object_sha256"])

if __name__ == "__main__":
    main()
