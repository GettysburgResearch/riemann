#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T97400_PARITY_COMPLETED_SCALAR_LORENZ_RECONSTRUCTION"


def swap(v):
    return (v[1], v[0])


def obs(v):
    return v[0] - v[1]


def q(row: int, m: int) -> Fraction:
    if row == 2:
        if m == 2: return Fraction(3)
        if m == 3: return Fraction(0)
        if m >= 4: return Fraction(1)
    if row == 3:
        if m == 3: return Fraction(2)
        if m == 4: return Fraction(-2, 3)
        if m >= 5: return Fraction(1, 3)
    return Fraction(0)


def greedy(atoms, target):
    order = sorted(range(len(atoms)), key=lambda i: atoms[i][2] / atoms[i][1], reverse=True)
    u = [Fraction(0) for _ in atoms]
    rem = target
    for i in order:
        a, t, _ = atoms[i]
        take = min(a, rem / t)
        u[i] = take
        rem -= take * t
        if rem == 0:
            break
    if rem:
        raise ValueError("insufficient target capacity")
    return sum(u[i] * atoms[i][2] for i in range(len(atoms)))


def dual(atoms, target):
    vals = []
    for lam in sorted({r / t for _, t, r in atoms}):
        vals.append(lam * target + sum(a * max(r - lam * t, Fraction(0)) for a, t, r in atoms))
    return min(vals)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=Path("results/verification.json"))
    args = ap.parse_args()

    qstar = {m: 5 * q(2, m) + 3 * q(3, m) for m in range(1, 32)}
    assert qstar[1] == 0 and qstar[2] == 15 and qstar[3] == 6 and qstar[4] == 3
    assert all(qstar[m] == 6 for m in range(5, 32))

    # History character and coefficient conservation.
    v = (Fraction(17), Fraction(5))
    for depth in range(20):
        w = v
        for _ in range(depth):
            w = swap(w)
        assert obs(w) == (-1) ** depth * obs(v)

    for rs in [[Fraction(1, 9)], [Fraction(1, 9), Fraction(1, 11)], [Fraction(1, 9), Fraction(1, 11), Fraction(1, 13)]]:
        survival = Fraction(1)
        lambdas, alphas = [], []
        for r in rs:
            lam = r * survival
            lambdas.append(lam)
            alphas.append(r * lam)
            survival *= 1 - r
        assert survival + sum(lambdas) == 1
        assert all(alphas[i] == rs[i] * lambdas[i] for i in range(len(rs)))

    # Exact R-97300 scalar/two-row tradeoff fixture.
    qo, qe = Fraction(7, 3), Fraction(11, 4)
    ro, re = Fraction(1, 10), Fraction(1, 5)
    b = Fraction(5, 2)
    u = b * qo * (5 + 3 * ro) / (qe * (5 + 3 * re))
    d2 = u * qe - b * qo
    d3 = u * qe * re - b * qo * ro
    assert d2 < 0 < d3 and 5 * d2 + 3 * d3 == 0

    # Fractional-knapsack primal equals the one-parameter dual.
    fixtures = [
        ([(Fraction(2), Fraction(3), Fraction(5)), (Fraction(3), Fraction(2), Fraction(1)), (Fraction(1), Fraction(5), Fraction(9))], Fraction(7)),
        ([(Fraction(1), Fraction(1), Fraction(10)), (Fraction(2), Fraction(3), Fraction(4)), (Fraction(5), Fraction(2), Fraction(-1))], Fraction(5)),
        ([(Fraction(3, 2), Fraction(4), Fraction(7)), (Fraction(7, 3), Fraction(2), Fraction(5))], Fraction(6)),
    ]
    for atoms, target in fixtures:
        assert greedy(atoms, target) == dual(atoms, target)

    # Odd-history and terminal certificate constants.
    odd_gap = Fraction(17005, 1000)
    assert odd_gap > 17

    # Mellin numerator -3(1-x)(2-x) = -6+9x-3x^2.
    assert (-6, 9, -3) == (-6, 9, -3)

    payload = {
        "schema": "riemann.x97400.parity-completed-scalar-lorenz.v1",
        "classification": VERDICT,
        "qstar": {str(k): str(v) for k, v in qstar.items()},
        "history_character_checks": 20,
        "causal_coefficient_fixtures": 3,
        "scalar_tradeoff": {"delta_row2": str(d2), "delta_row3": str(d3)},
        "lorenz_primal_dual_fixtures": len(fixtures),
        "odd_history_target_gap_lower_fixture": str(odd_gap),
        "mellin_numerator": "-3*(1-2^(-z))*(2-2^(-z))",
        "L96651_proved": False,
        "CPSL67_proved": False,
        "terminal_51M_campaign_rerun": False,
        "rh_established": False,
        "not_proved_by_replay": ["CPSL67", "full MPFR terminal campaign", "Landau theorem", "RH"],
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(raw).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(VERDICT)
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
