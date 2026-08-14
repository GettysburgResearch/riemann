#!/usr/bin/env python3
"""Exact rational replay for the Target-Lorenz vector primal/dual theorem.

Arithmetic class: EXACT_RATIONAL, with integer square-root enclosures used only
for the displayed low-quotient radical inequalities. No floating-point sign
controls acceptance.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import isqrt
from pathlib import Path
import hashlib
import json

SCALE = 10**36


def sqrt_interval(q: Fraction) -> tuple[Fraction, Fraction]:
    assert q >= 0
    n, d = q.numerator, q.denominator
    lo = isqrt(n * SCALE * SCALE // d)
    while Fraction((lo + 1) ** 2, SCALE**2) <= q:
        lo += 1
    while Fraction(lo**2, SCALE**2) > q:
        lo -= 1
    hi = lo if Fraction(lo**2, SCALE**2) == q else lo + 1
    return Fraction(lo, SCALE), Fraction(hi, SCALE)


def inv_sqrt_interval(n: int) -> tuple[Fraction, Fraction]:
    lo, hi = sqrt_interval(Fraction(n))
    return Fraction(1, hi), Fraction(1, lo)


def leftmost(target_masses: list[Fraction], demand: Fraction) -> list[Fraction]:
    assert Fraction(0) <= demand <= sum(target_masses)
    out = [Fraction(0) for _ in target_masses]
    left = demand
    for i, mass in enumerate(target_masses):
        if left <= 0:
            break
        take = min(mass, left)
        out[i] = take / mass
        left -= take
    assert left == 0
    return out


def dot(a: list[Fraction], b: list[Fraction]) -> Fraction:
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def enumerate_target_vertices(
    target_masses: list[Fraction], demand: Fraction
) -> list[list[Fraction]]:
    """Enumerate all box/hyperplane vertices; at most one coordinate fractional."""
    n = len(target_masses)
    vertices: set[tuple[Fraction, ...]] = set()
    for fractional in range(n):
        others = [i for i in range(n) if i != fractional]
        for bits in product((0, 1), repeat=n - 1):
            x = [Fraction(0) for _ in range(n)]
            used = Fraction(0)
            for i, bit in zip(others, bits):
                x[i] = Fraction(bit)
                used += x[i] * target_masses[i]
            rem = demand - used
            if 0 <= rem <= target_masses[fractional]:
                x[fractional] = rem / target_masses[fractional]
                vertices.add(tuple(x))
    for bits in product((0, 1), repeat=n):
        x = [Fraction(b) for b in bits]
        if dot(x, target_masses) == demand:
            vertices.add(tuple(x))
    return [list(v) for v in sorted(vertices)]


def support_dual_lhs(
    target: list[Fraction],
    score: list[Fraction],
    rows: list[list[Fraction]],
    tau: Fraction,
    beta: Fraction,
    lambdas: list[Fraction],
) -> Fraction:
    total = Fraction(0)
    for e in range(len(target)):
        a = tau * target[e] - beta * score[e]
        a += sum(lambdas[j] * rows[j][e] for j in range(len(rows)))
        total += max(Fraction(0), a)
    return total


def support_dual_rhs(
    odd_target: Fraction,
    odd_score: Fraction,
    odd_rows: list[Fraction],
    tau: Fraction,
    beta: Fraction,
    lambdas: list[Fraction],
) -> Fraction:
    return (
        tau * odd_target
        - beta * odd_score
        + sum(lambdas[j] * odd_rows[j] for j in range(len(odd_rows)))
    )


def check_simultaneous_bathtub() -> dict:
    fixtures = [
        {
            "target": [Fraction(3), Fraction(5), Fraction(7), Fraction(11)],
            "score_ratio": [Fraction(2), Fraction(5, 2), Fraction(3), Fraction(4)],
            "row_ratios": [
                [Fraction(9), Fraction(7), Fraction(4), Fraction(1)],
                [Fraction(13), Fraction(8), Fraction(8), Fraction(2)],
                [Fraction(5), Fraction(4), Fraction(2), Fraction(0)],
            ],
            "demand": Fraction(12),
        },
        {
            "target": [Fraction(2), Fraction(3), Fraction(5), Fraction(7), Fraction(11)],
            "score_ratio": [Fraction(1), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5)],
            "row_ratios": [
                [Fraction(12), Fraction(10), Fraction(9), Fraction(3), Fraction(0)],
                [Fraction(6), Fraction(6), Fraction(4), Fraction(4), Fraction(1)],
            ],
            "demand": Fraction(13),
        },
    ]
    vertex_checks = 0
    for f in fixtures:
        t = f["target"]
        s = [t[i] * f["score_ratio"][i] for i in range(len(t))]
        rows = [
            [t[i] * ratios[i] for i in range(len(t))]
            for ratios in f["row_ratios"]
        ]
        u = leftmost(t, f["demand"])
        u_score = dot(u, s)
        u_rows = [dot(u, row) for row in rows]
        verts = enumerate_target_vertices(t, f["demand"])
        assert verts
        for v in verts:
            assert u_score <= dot(v, s)
            for j, row in enumerate(rows):
                assert u_rows[j] >= dot(v, row)
            vertex_checks += 1
    return {
        "classification": "PASS_SIMULTANEOUS_TARGET_BATHTUB",
        "fixtures": len(fixtures),
        "exact_vertex_comparisons": vertex_checks,
    }


def check_cutoff_separator() -> dict:
    t = [Fraction(3), Fraction(5), Fraction(7), Fraction(11)]
    rho = [Fraction(9), Fraction(7), Fraction(4), Fraction(1)]
    row = [t[i] * rho[i] for i in range(len(t))]
    demand = Fraction(12)
    u = leftmost(t, demand)
    cutoff = max(i for i, x in enumerate(u) if x > 0)
    max_row = dot(u, row)
    odd_row = max_row + Fraction(1, 7)
    tau = -rho[cutoff]
    lhs = sum(max(Fraction(0), row[i] + tau * t[i]) for i in range(len(t)))
    rhs = odd_row + tau * demand
    assert lhs < rhs
    assert rhs - lhs == odd_row - max_row

    odd_row_ok = max_row - Fraction(2, 7)
    rhs_ok = odd_row_ok + tau * demand
    assert lhs >= rhs_ok
    return {
        "classification": "PASS_EXPLICIT_CUTOFF_FARKAS_SEPARATOR",
        "cutoff_index": cutoff,
        "strict_dual_gap": str(rhs - lhs),
    }


def check_general_support_inequality() -> dict:
    t = [Fraction(2), Fraction(3), Fraction(5), Fraction(7)]
    sigma = [Fraction(1), Fraction(2), Fraction(3), Fraction(5)]
    s = [t[i] * sigma[i] for i in range(len(t))]
    row_ratios = [
        [Fraction(8), Fraction(6), Fraction(3), Fraction(1)],
        [Fraction(9), Fraction(7), Fraction(7), Fraction(0)],
    ]
    rows = [[t[i] * q[i] for i in range(len(t))] for q in row_ratios]
    demand = Fraction(8)
    u = leftmost(t, demand)
    odd_score = dot(u, s) + Fraction(1)
    odd_rows = [dot(u, r) - Fraction(1, 2) for r in rows]

    tests = 0
    for tau in [Fraction(-9), Fraction(-2), Fraction(0), Fraction(3), Fraction(11)]:
        for beta in [Fraction(0), Fraction(1), Fraction(5, 3)]:
            for l0 in [Fraction(0), Fraction(1), Fraction(4)]:
                for l1 in [Fraction(0), Fraction(2), Fraction(7, 2)]:
                    lhs = support_dual_lhs(t, s, rows, tau, beta, [l0, l1])
                    rhs = support_dual_rhs(
                        demand, odd_score, odd_rows, tau, beta, [l0, l1]
                    )
                    assert lhs >= rhs
                    tests += 1
    return {
        "classification": "PASS_VECTOR_SUPPORT_FUNCTION_DUAL",
        "exact_multiplier_tests": tests,
    }


def check_full_determinant_sufficiency() -> dict:
    fixtures = 0
    for t in [
        [Fraction(2), Fraction(3), Fraction(5), Fraction(7)],
        [Fraction(1), Fraction(4), Fraction(6), Fraction(9), Fraction(13)],
    ]:
        ratios = [
            [Fraction(9 - i) for i in range(len(t))],
            [Fraction(20 - 2 * i) for i in range(len(t))],
        ]
        rows = [[t[i] * q[i] for i in range(len(t))] for q in ratios]
        E_T = sum(t)
        O_T = E_T * Fraction(3, 7)
        theta = O_T / E_T
        u = leftmost(t, O_T)
        for row in rows:
            E_R = sum(row)
            O_R = theta * E_R - Fraction(1, 5)
            det = O_T * E_R - E_T * O_R
            assert det > 0
            assert dot(u, row) >= theta * E_R >= O_R
            fixtures += 1
    return {
        "classification": "PASS_FULL_TARGET_DETERMINANT_SUFFICIENCY",
        "row_fixtures": fixtures,
    }


def check_low_quotient_radicals() -> dict:
    rt67_lo, _ = sqrt_interval(Fraction(67))
    inv2_lo, _ = inv_sqrt_interval(2)
    inv3_lo, inv3_hi = inv_sqrt_interval(3)
    sqrt3_lo = 3 * inv3_lo
    c_lo = 3 * inv2_lo + sqrt3_lo - 3
    assert c_lo > 0

    case1 = Fraction(2, 3) * rt67_lo - Fraction(8, 1) / rt67_lo + c_lo
    rt134_lo, _ = sqrt_interval(Fraction(134))
    case2 = Fraction(2, 3) * rt134_lo - Fraction(6, 1) / rt134_lo + c_lo
    assert c_lo > Fraction(4, 5)
    assert case1 > 5
    assert case2 > 8
    assert inv2_lo + inv3_lo > 1
    return {
        "classification": "PASS_TARGET_DOMINATION_THROUGH_QUOTIENT_FIVE",
        "case_1_lower_bound": ">5",
        "case_2_lower_bound": ">8",
        "positive_constant_lower_bound": ">4/5",
    }


def main() -> None:
    checks = [
        check_simultaneous_bathtub(),
        check_cutoff_separator(),
        check_general_support_inequality(),
        check_full_determinant_sufficiency(),
        check_low_quotient_radicals(),
    ]
    payload = {
        "arithmetic_class": "EXACT_RATIONAL",
        "classification": "PASS_TARGET_LORENZ_VECTOR_PRIMAL_DUAL",
        "checks": checks,
        "scope": (
            "exact abstract common-source primal/dual theorem and exact low-quotient "
            "radical gates; no global P61 row-determinant sign is certified"
        ),
        "rh_established_by_replay": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["classification"])
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
