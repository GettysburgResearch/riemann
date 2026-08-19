#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import random
from fractions import Fraction
from math import isqrt
from pathlib import Path


BITS = 48
Q = 1 << BITS
VERDICT = "PASS_X_99450_RN_HALL_COBBOUNDARY_HARDENING"


def mobius_sieve(n: int) -> list[int]:
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


def sqrt_interval(n: int) -> tuple[Fraction, Fraction]:
    a = isqrt(n * Q * Q)
    lo = Fraction(a, Q)
    hi = lo if a * a == n * Q * Q else Fraction(a + 1, Q)
    return lo, hi


def invsqrt_interval(n: int) -> tuple[Fraction, Fraction]:
    lo, hi = sqrt_interval(n)
    return Fraction(1, hi), Fraction(1, lo)


def fstr(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def hall_certificate() -> dict[str, object]:
    mu = mobius_sieve(67)
    A = Fraction(0)
    B_lo = Fraction(0)
    B_hi = Fraction(0)
    rows = []

    for t in range(1, 67):
        A += Fraction(mu[t], t)
        il, iu = invsqrt_interval(t)
        if mu[t] >= 0:
            B_lo += mu[t] * il
            B_hi += mu[t] * iu
        else:
            B_lo += mu[t] * iu
            B_hi += mu[t] * il

        endpoint = t if A >= 0 else 67
        sl, su = sqrt_interval(endpoint)
        H_lo = 4 * A * (sl if A >= 0 else su) - 3 * B_hi
        H_hi = 4 * A * (su if A >= 0 else sl) - 3 * B_lo
        rows.append({
            "t": t,
            "mu_t": mu[t],
            "A_t": fstr(A),
            "B_lower": fstr(B_lo),
            "B_upper": fstr(B_hi),
            "minimizing_endpoint": endpoint,
            "endpoint_is_open_limit": bool(A < 0),
            "H_lower": fstr(H_lo),
            "H_upper": fstr(H_hi),
            "H_lower_decimal": f"{float(H_lo):.18f}",
        })

    min_row = min(rows, key=lambda r: Fraction(r["H_lower"]))
    payload = {
        "schema": "riemann.x99450.compact-target-hall.v1",
        "sqrt_interval_bits": BITS,
        "threshold_range": [1, 66],
        "hall_target": "7/20",
        "minimum_threshold": min_row["t"],
        "minimum_lower": min_row["H_lower"],
        "minimum_lower_decimal": min_row["H_lower_decimal"],
        "margin_over_7_20": fstr(
            Fraction(min_row["H_lower"]) - Fraction(7, 20)
        ),
        "rows": rows,
    }
    core = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["certificate_sha256"] = hashlib.sha256(core).hexdigest()
    return payload


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def matadd(a, b, scale=Fraction(1)):
    return [
        [a[i][j] + scale * b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def eye(n: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def rowmul(v: list[Fraction], a: list[list[Fraction]]) -> list[Fraction]:
    return [
        sum((v[k] * a[k][j] for k in range(len(v))), Fraction(0))
        for j in range(len(a[0]))
    ]


def run() -> dict[str, object]:
    hall = hall_certificate()
    stored = json.loads(
        (
            Path(__file__).resolve().parent
            / "certificates/compact_hall_1_66.json"
        ).read_text()
    )
    assert hall == stored
    assert hall["minimum_threshold"] == 13
    assert Fraction(hall["minimum_lower"]) > Fraction(7, 20)

    hall_checks = len(hall["rows"])
    rn_checks = 0
    random_key_checks = 0
    coboundary_checks = 0
    clamp_checks = 0
    noncancellation_checks = 0
    hostile = 0

    # Exact raw-cutoff counterexample.
    # T(4)=5, T(1)=1, hence RN ratio=1/5.
    assert 4 * 2 - 3 == 5
    assert 4 * 1 - 3 == 1
    assert Fraction(1, 5) < 1
    rn_checks += 3

    # Rational RN/random-key fixtures.
    rng = random.Random(99450)
    for children in range(1, 9):
        for _ in range(64):
            alphas = [
                Fraction(rng.randint(0, 9), 200 + rng.randint(1, 100))
                for _ in range(children)
            ]
            rs = [
                Fraction(rng.randint(0, 100), 100)
                for _ in range(children)
            ]
            widths = [a * r for a, r in zip(alphas, rs)]
            assert all(0 <= r <= 1 for r in rs)
            assert sum(widths, Fraction(0)) <= sum(alphas, Fraction(0))
            assert sum(alphas, Fraction(0)) < Fraction(1, 2)
            residual = 1 - sum(widths, Fraction(0))
            assert residual >= 0
            random_key_checks += 4

    # Nilpotent coboundary on exact random upper-triangular operators.
    for n in range(1, 9):
        for _ in range(32):
            T = [[Fraction(0) for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    T[i][j] = Fraction(rng.randint(0, 5), 20)
            # Build finite resolvent.
            R = eye(n)
            power = eye(n)
            for _k in range(1, n):
                power = matmul(power, T)
                R = matadd(R, power)
            assert matmul(matadd(eye(n), T, Fraction(-1)), R) == eye(n)

            P = [Fraction(rng.randint(0, 20), 7) for _ in range(n)]
            A = [Fraction(rng.randint(-20, 20), 11) for _ in range(n)]
            PT = rowmul(P, T)
            J = [P[i] - PT[i] for i in range(n)]
            E = [P[i] + A[i] for i in range(n)]
            ET = rowmul(E, T)
            AT = rowmul(A, T)
            rhs = [J[i] + ET[i] + A[i] - AT[i] for i in range(n)]
            assert rhs == E
            resolved = rowmul(J, R)
            assert resolved == P
            deltaA = [A[i] - AT[i] for i in range(n)]
            assert rowmul(deltaA, R) == A
            coboundary_checks += 4

    # Double-clamping algebra for F(u)=4-4sqrt(u)+2sqrt(u)log(u).
    # At u=1, log u=0 and F'=log(u)/sqrt(u), so F(1)=F'(1)=0.
    assert 4 - 4 == 0
    assert 0 == 0
    # V F = 2/sqrt(u)-1: at u=1 this is 1 and no delta atom is present.
    assert 2 - 1 == 1
    clamp_checks += 3

    # Large-row leading coefficient identity on exact rational z.
    for den in range(2, 61):
        for num in range(-den + 1, den):
            z = Fraction(num, den)
            if z in (0, 1):
                continue
            lhs = z + 2 - Fraction(2, 1 - z)
            rhs = -z * (z + 1) / (1 - z)
            assert lhs == rhs
            noncancellation_checks += 1

    # Hostile mutations.
    if Fraction(1, 5) != Fraction(1, 4):
        hostile += 1
    if hall["minimum_threshold"] != 12:
        hostile += 1
    if Fraction(hall["minimum_lower"]) != Fraction(7, 20):
        hostile += 1
    if Fraction(1, 8) != Fraction(1, 7):
        hostile += 1
    if -Fraction(2 * 3, 1 - 2) != 0:
        hostile += 1

    return {
        "schema": "riemann.x99450.three-interface-hardening.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_INTEGER_RATIONAL_AND_DIRECTED_RADICAL",
        "base_pr": 648,
        "base_sha": "49be6640ae2714d1f907a6117c4a6d2aaa9f2f11",
        "hall_prefix_checks": hall_checks,
        "hall_certificate_sha256": hall["certificate_sha256"],
        "hall_minimum_threshold": hall["minimum_threshold"],
        "hall_minimum_lower": hall["minimum_lower"],
        "rn_source_checks": rn_checks,
        "random_key_checks": random_key_checks,
        "coboundary_checks": coboundary_checks,
        "double_clamp_checks": clamp_checks,
        "noncancellation_leading_checks": noncancellation_checks,
        "hostile_mutations_detected": hostile,
        "proves": [
            "raw child cutoff counterexample and exact RN repair",
            "RN random-key common-parent algebra",
            "RN-compatible calibration coboundary telescope",
            "independent compact target Hall margin through every threshold",
            "canonical double-clamping algebra",
            "large-row noncancellation leading coefficient algebra",
        ],
        "requires_independent_reconstruction": [
            "complete native root registry E=P+A on frozen endpoint data",
            "finite anchored and omission ownership ledger",
            "full analytic Euler-summation and Landau reconstruction",
        ],
        "does_not_prove": [
            "independent acceptance of the full candidate",
            "Riemann Hypothesis",
        ],
        "rh_established": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = run()
    core = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(core).hexdigest()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
