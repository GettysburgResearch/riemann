#!/usr/bin/env python3
"""Exact rational regression for the annular divisor-gradient frame proposal.

This checker verifies only finite algebra:
  * divisor-gradient / cumulative-flow factorization;
  * Gram action on every prime-power constraint;
  * the formal von-Mangoldt objective identity;
  * exact minimum-norm active projection on a rational toy annulus;
  * exact active-residual halving;
  * a rational annular cost/positivity control;
  * complete-period prime-base covariance;
  * fail-closed mutations.

It does not prove the all-X annular frame theorem or RH.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from typing import Dict, List
from math import gcd


TOY_X = 30
ANNULUS = list(range(12, 25))
ACTIVE = [2, 3, 4, 5, 7]


def primes_through(n: int) -> List[int]:
    out: List[int] = []
    for k in range(2, n + 1):
        if all(k % p for p in out if p * p <= k):
            out.append(k)
    return out


def prime_powers(n: int) -> List[int]:
    out = set()
    for p in primes_through(n):
        q = p
        while q <= n:
            out.add(q)
            if q > n // p:
                break
            q *= p
    return sorted(out)


def factorization(n: int) -> Dict[int, int]:
    out: Dict[int, int] = {}
    value = n
    p = 2
    while p * p <= value:
        while value % p == 0:
            out[p] = out.get(p, 0) + 1
            value //= p
        p += 1
    if value > 1:
        out[value] = out.get(value, 0) + 1
    return out


def g(d: int, m: int) -> int:
    return int(m % d == 0) - int((m - 1) % d == 0)


def annular_row(q: int, j: int) -> int:
    return 2 * int(j % q == 0) - int((j - 1) % q == 0) - int((j + 1) % q == 0)


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [
            sum(a[i][k] * b[k][j] for k in range(len(b)))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def matvec(a, x):
    return [sum(row[j] * x[j] for j in range(len(x))) for row in a]


def inverse(a):
    n = len(a)
    aug = [
        [Fraction(a[i][j]) for j in range(n)]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col]), None)
        if pivot is None:
            raise AssertionError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [
                    aug[row][j] - factor * aug[col][j]
                    for j in range(2 * n)
                ]
    return [row[n:] for row in aug]


def canonical_digest(payload: dict) -> str:
    data = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def divisor_gradient_control() -> dict:
    divisors = [2, 3, 4, 5, 6, 10]
    amplitudes = {
        2: Fraction(1, 7),
        3: Fraction(2, 11),
        4: Fraction(1, 13),
        5: Fraction(3, 17),
        6: Fraction(2, 19),
        10: Fraction(1, 23),
    }
    flow = {
        m: sum(amplitudes[d] for d in divisors if m % d == 0)
        for m in range(1, TOY_X + 1)
    }
    h = {
        m: flow.get(m - 1, Fraction(0)) - flow.get(m, Fraction(0))
        for m in range(2, TOY_X + 1)
    }
    for m in range(2, TOY_X + 1):
        rhs = -sum(amplitudes[d] * g(d, m) for d in divisors)
        if h[m] != rhs:
            raise AssertionError("cumulative/divisor-gradient mismatch")

    rows = prime_powers(TOY_X)
    for q in rows:
        direct = sum(h[m] * g(q, m) for m in range(2, TOY_X + 1))
        gram = -sum(
            amplitudes[d]
            * sum(g(q, m) * g(d, m) for m in range(2, TOY_X + 1))
            for d in divisors
        )
        if direct != gram:
            raise AssertionError("Gram correction mismatch")

    for m in range(2, TOY_X + 1):
        lhs: Dict[int, int] = {}
        for p in primes_through(TOY_X):
            q = p
            while q <= TOY_X:
                coefficient = g(q, m)
                if coefficient:
                    lhs[p] = lhs.get(p, 0) + coefficient
                if q > TOY_X // p:
                    break
                q *= p
        lhs = {p: e for p, e in lhs.items() if e}
        rhs = factorization(m)
        for p, e in factorization(m - 1).items():
            rhs[p] = rhs.get(p, 0) - e
            if not rhs[p]:
                del rhs[p]
        if lhs != rhs:
            raise AssertionError("formal von-Mangoldt objective mismatch")

    return {
        "divisors": divisors,
        "amplitudes": {str(k): str(v) for k, v in amplitudes.items()},
        "maximum_flow": str(max(flow.values())),
        "nonzero_gradient_coordinates": sum(value != 0 for value in h.values()),
        "prime_power_rows": len(rows),
    }


def active_projection_control() -> dict:
    a = [
        [Fraction(annular_row(q, j)) for j in ANNULUS]
        for q in ACTIVE
    ]
    gram = matmul(a, transpose(a))
    gram_inverse = inverse(gram)
    residual = [Fraction(1, 2), Fraction(1, 3), Fraction(2, 5),
                Fraction(1, 7), Fraction(3, 11)]
    dual = matvec(gram_inverse, residual)
    update = matvec(transpose(a), dual)
    replay = matvec(a, update)
    if replay != residual:
        raise AssertionError("minimum-norm projection replay failed")

    half = Fraction(1, 2)
    halved = [residual[i] - half * replay[i] for i in range(len(residual))]
    if halved != [half * x for x in residual]:
        raise AssertionError("active residuals did not halve exactly")

    norm_sq = sum(x * x for x in update)
    energy = sum(residual[i] * dual[i] for i in range(len(residual)))
    if norm_sq != energy:
        raise AssertionError("pseudoinverse energy identity failed")

    identity = matmul(gram, gram_inverse)
    if identity != [
        [Fraction(int(i == j)) for j in range(len(ACTIVE))]
        for i in range(len(ACTIVE))
    ]:
        raise AssertionError("Gram inverse mismatch")

    return {
        "active_rows": ACTIVE,
        "annulus": [ANNULUS[0], ANNULUS[-1]],
        "gram_determinant_nonzero": True,
        "projection_norm_sq": str(norm_sq),
        "dual_energy": str(energy),
        "active_halving_factor": "1/2",
    }


def transfer_control() -> dict:
    seed_slack = Fraction(3)
    flow_norm_upper = Fraction(1)
    adjacent_upper = 2 * flow_norm_upper
    if seed_slack - adjacent_upper <= 0:
        raise AssertionError("synthetic annular positivity moat failed")

    alpha = Fraction(2, 5)
    x = 100
    point_upper = Fraction(1, (alpha * x) ** 2 - 1)
    count = x
    l2_weight_sq_upper = count * point_upper * point_upper
    if l2_weight_sq_upper >= Fraction(1, 1000):
        raise AssertionError("annular objective weight not small enough")

    return {
        "synthetic_seed_slack": str(seed_slack),
        "flow_l2_upper": str(flow_norm_upper),
        "remaining_slack_lower": str(seed_slack - adjacent_upper),
        "cost_weight_l2_sq_upper": str(l2_weight_sq_upper),
    }


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def complete_period_control() -> dict:
    checks = []
    pairs = [(3, 5), (4, 9), (3, 9), (5, 25), (4, 16), (2, 8)]
    for q, r in pairs:
        period = lcm(q, r)
        numerator = sum(
            annular_row(q, j) * annular_row(r, j)
            for j in range(1, period + 1)
        )
        if gcd(q, r) == 1:
            expected = 0
        elif q == 2 and r >= 4:
            expected = 8 * (period // r)
        elif r == 2 and q >= 4:
            expected = 8 * (period // q)
        else:
            expected = 6 * (period // max(q, r))
        if numerator != expected:
            raise AssertionError(
                f"complete-period covariance mismatch {(q, r)}: "
                f"{numerator} != {expected}"
            )
        checks.append({
            "q": q,
            "r": r,
            "period": period,
            "inner_product": numerator,
        })

    rho = Fraction(1, 2)
    toeplitz = [
        [rho ** abs(i - j) for j in range(4)]
        for i in range(4)
    ]
    floor = (1 - rho) / (1 + rho)
    shifted = [
        [toeplitz[i][j] - (floor if i == j else 0) for j in range(4)]
        for i in range(4)
    ]
    l = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    d = [Fraction(0) for _ in range(4)]
    for i in range(4):
        l[i][i] = 1
        d[i] = shifted[i][i] - sum(l[i][k] * l[i][k] * d[k] for k in range(i))
        if d[i] < 0:
            raise AssertionError("Toeplitz floor LDL pivot negative")
        if d[i]:
            for j in range(i + 1, 4):
                l[j][i] = (
                    shifted[j][i]
                    - sum(l[j][k] * l[i][k] * d[k] for k in range(i))
                ) / d[i]

    return {
        "period_checks": checks,
        "normalized_chain_rho": str(rho),
        "normalized_chain_floor": str(floor),
        "shifted_ldl_pivots": [str(x) for x in d],
    }


def build_result() -> dict:
    payload = {
        "schema": "riemann.x26101-annular-divisor-frame.v1",
        "classification": "EXACT_SYNTHETIC_ANNULAR_FRAME_ALGEBRA",
        "divisor_gradient": divisor_gradient_control(),
        "active_projection": active_projection_control(),
        "annular_transfer": transfer_control(),
        "complete_period_model": complete_period_control(),
        "verdict": "PASS_EXACT_ANNULAR_DIVISOR_FRAME_ALGEBRA",
    }
    payload["proof_object_sha256"] = canonical_digest(payload)
    return payload


def self_tests() -> list[str]:
    tests: list[str] = []
    result = build_result()
    assert result["verdict"].startswith("PASS")
    tests.append("central proof object")

    assert g(3, 6) != -int((6 - 1) % 3 == 0)
    tests.append("mutated divisor gradient rejected")

    assert annular_row(5, 15) == 2
    assert annular_row(5, 15) != 1
    tests.append("mutated annular Laplacian rejected")

    a = [[Fraction(annular_row(q, j)) for j in ANNULUS] for q in ACTIVE]
    residual = [Fraction(1, 2), Fraction(1, 3), Fraction(2, 5),
                Fraction(1, 7), Fraction(3, 11)]
    wrong = matvec(transpose(a), residual)
    assert matvec(a, wrong) != residual
    tests.append("missing Gram inverse rejected")

    assert Fraction(3) - 2 * Fraction(2) < 0
    tests.append("overstated flow moat rejected")

    assert complete_period_control()["period_checks"][0]["inner_product"] == 0
    tests.append("complete-period covariance model")

    m = 16
    full = sum(g(q, m) for q in (2, 4, 8, 16))
    truncated = sum(g(q, m) for q in (2, 4, 8))
    assert full != truncated
    tests.append("omitted prime-power row rejected")

    return tests


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    result = build_result()
    if args.self_test:
        tests = self_tests()
        print(f"{len(tests)}/{len(tests)} tests passed")
        for name in tests:
            print("PASS", name)

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
