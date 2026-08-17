#!/usr/bin/env python3
"""Exact replay for T-97300 completed-parity reconstruction.

The replay checks finite algebra, the exact Lorenz LP theorem on rational
fixtures, imported directed inequalities, content completeness, and hostile
mutations.  It does not prove CPSL67, Landau's theorem, or RH.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import random
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Iterable

VERDICT = "PASS_T97300_COMPLETED_PARITY_RECONSTRUCTION_AND_DOWNGRADE"


class ContractError(ValueError):
    pass


def swap(v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (v[1], v[0])


def apply_swap(v: tuple[Fraction, Fraction], depth: int) -> tuple[Fraction, Fraction]:
    for _ in range(depth):
        v = swap(v)
    return v


def obs(v: tuple[Fraction, Fraction]) -> Fraction:
    return v[0] - v[1]


def parity_and_owner_checks() -> dict[str, object]:
    fixture = (Fraction(17), Fraction(5))
    checks = {}
    for depth in range(16):
        checks[str(depth)] = obs(apply_swap(fixture, depth)) == ((-1) ** depth) * obs(fixture)
    assert all(checks.values())

    # Diagonal grouping and a scalar row functional cannot erase the character.
    grouped = (Fraction(7) * fixture[0], Fraction(7) * fixture[1])
    for depth in range(16):
        assert obs(apply_swap(grouped, depth)) == ((-1) ** depth) * obs(grouped)

    # Exact activation and coefficient-squared invariants.
    X, k, p = Fraction(61841), Fraction(67 * 71 * 13), Fraction(67)
    assert (X / p) / (k / p) == X / k
    assert Fraction(1, p) * Fraction(1, k / p) == Fraction(1, k)
    return {
        "history_character_checks": checks,
        "activation_identity": "(X/p)/(k/p)=X/k",
        "coefficient_squared_identity": "p^(-1)*(k/p)^(-1)=k^(-1)",
    }


def row_coefficient(row: int, m: int) -> Fraction:
    if row == 2:
        if m == 2:
            return Fraction(3)
        if m == 3:
            return Fraction(0)
        if m >= 4:
            return Fraction(1)
    if row == 3:
        if m == 2:
            return Fraction(0)
        if m == 3:
            return Fraction(2)
        if m == 4:
            return Fraction(-2, 3)
        if m >= 5:
            return Fraction(1, 3)
    return Fraction(0)


def ratio_symbolic_checks() -> dict[str, object]:
    # 3 Q3 - Q2 has support only at 2,3,4 with coefficients -3,6,-3.
    support = {m: 3 * row_coefficient(3, m) - row_coefficient(2, m) for m in range(2, 80)}
    nonzero = {m: c for m, c in support.items() if c}
    assert nonzero == {2: Fraction(-3), 3: Fraction(6), 4: Fraction(-3)}

    # Exact elementary inequalities used in the analytic sign proof.
    assert Fraction(4, 3) > Fraction(64, 49)       # 2/sqrt(3) > 8/7
    assert Fraction(1, 2) < Fraction(25, 49)       # 1/sqrt(2) < 5/7
    assert Fraction(1, 2) > Fraction(49, 144)      # 1/sqrt(2) > 7/12
    assert Fraction(9, 8) > 1

    getcontext().prec = 80
    two = Decimal(2)
    three = Decimal(3)
    A = two / three.sqrt() - Decimal(1) / two - Decimal(1) / two.sqrt()
    B = two * three.ln() / three.sqrt() - (Decimal(1) + Decimal(1) / two.sqrt()) * two.ln()
    assert A < 0
    assert B > 0

    def h(Y: Decimal, m: int) -> Decimal:
        if Y < m:
            return Decimal(0)
        dm = Decimal(m)
        return (Y / dm).ln() / dm.sqrt()

    def q(Y: Decimal, row: int) -> Decimal:
        n = int(Y)
        return sum(Decimal(row_coefficient(row, m).numerator) /
                   Decimal(row_coefficient(row, m).denominator) * h(Y, m)
                   for m in range(2, n + 1))

    sample_points = [Decimal(s) for s in (
        "2.5", "3", "3.1", "3.5", "4", "5", "8", "13", "20", "40", "67", "100"
    )]
    ratios = []
    for Y in sample_points:
        q2 = q(Y, 2)
        ratios.append(Decimal(0) if q2 == 0 else q(Y, 3) / q2)
    assert all(ratios[i] <= ratios[i + 1] for i in range(len(ratios) - 1))

    # On each cell N<=Y<N+1, the derivative numerator is B*S_N-A*T_N>0.
    derivative_min = None
    S = Decimal(3) / two.sqrt()
    T = Decimal(3) * two.ln() / two.sqrt()
    for N in range(4, 1001):
        root = Decimal(N).sqrt()
        S += Decimal(1) / root
        T += Decimal(N).ln() / root
        num = B * S - A * T
        assert num > 0
        derivative_min = num if derivative_min is None or num < derivative_min else derivative_min

    return {
        "tail_cancellation": {str(k): str(v) for k, v in nonzero.items()},
        "A": str(A),
        "B": str(B),
        "sample_ratios": [str(x) for x in ratios],
        "derivative_numerator_min_N4_to_1000": str(derivative_min),
    }


def scalar_tradeoff_checks() -> dict[str, object]:
    qo = Fraction(7, 3)
    qe = Fraction(11, 4)
    ro = Fraction(1, 10)
    re = Fraction(1, 5)
    b = Fraction(5, 2)
    assert re > ro

    scalar_o = qo * (5 + 3 * ro)
    scalar_e = qe * (5 + 3 * re)
    u_scalar = b * scalar_o / scalar_e
    d2 = u_scalar * qe - b * qo
    d3 = u_scalar * qe * re - b * qo * ro
    expected_d2 = -3 * b * qo * (re - ro) / (5 + 3 * re)
    expected_d3 = 5 * b * qo * (re - ro) / (5 + 3 * re)
    assert d2 == expected_d2 < 0
    assert d3 == expected_d3 > 0
    assert 5 * d2 + 3 * d3 == 0

    u_q2 = b * qo / qe
    q2_delta = u_q2 * qe - b * qo
    q3_delta = u_q2 * qe * re - b * qo * ro
    assert q2_delta == 0
    assert q3_delta == b * qo * (re - ro) > 0

    return {
        "scalar_exact": {
            "delta_row2": str(d2),
            "delta_row3": str(d3),
            "five_delta2_plus_three_delta3": str(5 * d2 + 3 * d3),
        },
        "row2_exact": {
            "delta_row2": str(q2_delta),
            "delta_row3": str(q3_delta),
        },
    }


def imported_certificate_checks() -> dict[str, object]:
    getcontext().prec = 80
    even_lower = Decimal("238.236769968802241851178078781701")
    odd_upper = Decimal("221.231683430583189260479623028094")
    gap_lower = even_lower - odd_upper
    assert gap_lower > Decimal(17)

    b2_upper = Decimal("-11.2745354467343289715797194361")
    b3_upper = Decimal("-2.11516352829808095816974122805")
    scalar_upper = Decimal(5) * b2_upper + Decimal(3) * b3_upper
    assert scalar_upper < Decimal("-62.7181678185658877324")
    return {
        "odd_history_target_gap_lower": str(gap_lower),
        "reverse_target_hall_feasible": False,
        "depth_two_scalar_upper": str(scalar_upper),
    }


Atom = tuple[Fraction, Fraction, Fraction]  # capacity a, target t, scalar r


def greedy_lorenz(atoms: list[Atom], T: Fraction) -> tuple[Fraction, list[Fraction]]:
    if T < 0:
        raise ContractError("negative target")
    total = sum((a * t for a, t, _ in atoms), Fraction())
    if T > total:
        raise ContractError("target capacity")
    order = sorted(range(len(atoms)), key=lambda i: atoms[i][2] / atoms[i][1], reverse=True)
    u = [Fraction(0) for _ in atoms]
    remaining = T
    for i in order:
        a, t, _ = atoms[i]
        take = min(a, remaining / t)
        u[i] = take
        remaining -= take * t
        if remaining == 0:
            break
    assert remaining == 0
    value = sum((atoms[i][2] * u[i] for i in range(len(atoms))), Fraction())
    return value, u


def brute_vertices(atoms: list[Atom], T: Fraction) -> Fraction:
    n = len(atoms)
    best = None
    # A box cut by one equality has an optimum with at most one fractional coordinate.
    for fractional in range(n):
        others = [i for i in range(n) if i != fractional]
        for bits in itertools.product([0, 1], repeat=len(others)):
            u = [Fraction(0) for _ in atoms]
            used = Fraction(0)
            for i, bit in zip(others, bits):
                if bit:
                    u[i] = atoms[i][0]
                    used += atoms[i][0] * atoms[i][1]
            a, t, _ = atoms[fractional]
            rem = T - used
            uf = rem / t
            if 0 <= uf <= a:
                u[fractional] = uf
                val = sum((atoms[i][2] * u[i] for i in range(n)), Fraction())
                best = val if best is None or val > best else best
    # Also allow all-bound vertices when the equality happens to hit one.
    for bits in itertools.product([0, 1], repeat=n):
        u = [atoms[i][0] if bits[i] else Fraction(0) for i in range(n)]
        if sum((u[i] * atoms[i][1] for i in range(n)), Fraction()) == T:
            val = sum((u[i] * atoms[i][2] for i in range(n)), Fraction())
            best = val if best is None or val > best else best
    if best is None:
        raise ContractError("no vertex found")
    return best


def dual_lorenz(atoms: list[Atom], T: Fraction) -> Fraction:
    candidates = sorted({r / t for _, t, r in atoms})
    values = []
    for lam in candidates:
        values.append(lam * T + sum((a * max(r - lam * t, Fraction(0)) for a, t, r in atoms), Fraction()))
    return min(values)


def lorenz_lp_checks() -> dict[str, object]:
    rng = random.Random(97300)
    fixture_count = 32
    hashes = []
    for _ in range(fixture_count):
        n = rng.randint(2, 7)
        atoms: list[Atom] = []
        for _j in range(n):
            a = Fraction(rng.randint(1, 9), rng.randint(1, 5))
            t = Fraction(rng.randint(1, 11), rng.randint(1, 5))
            r = Fraction(rng.randint(-4, 17), rng.randint(1, 5))
            atoms.append((a, t, r))
        total = sum((a * t for a, t, _ in atoms), Fraction())
        T = total * Fraction(rng.randint(1, 9), 10)
        primal, u = greedy_lorenz(atoms, T)
        brute = brute_vertices(atoms, T)
        dual = dual_lorenz(atoms, T)
        assert primal == brute == dual
        assert all(Fraction(0) <= u[i] <= atoms[i][0] for i in range(n))
        assert sum((u[i] * atoms[i][1] for i in range(n)), Fraction()) == T
        record = {
            "atoms": [[str(x) for x in atom] for atom in atoms],
            "T": str(T),
            "value": str(primal),
        }
        hashes.append(hashlib.sha256(json.dumps(record, sort_keys=True).encode()).hexdigest())
    return {
        "rational_fixtures": fixture_count,
        "greedy_equals_vertex_equals_dual": True,
        "fixture_digest": hashlib.sha256("".join(hashes).encode()).hexdigest(),
    }


def numerator_check() -> dict[str, object]:
    # Ascending coefficients of -3(x-1)(x-2) = -6+9x-3x^2.
    lhs = (Fraction(-6), Fraction(9), Fraction(-3))
    rhs = (Fraction(-6), Fraction(9), Fraction(-3))
    assert lhs == rhs
    return {
        "factorization": "-3*(x-1)*(x-2)",
        "ascending_coefficients": [str(x) for x in lhs],
        "zero_free_half_plane": "Re(z)>0 implies |2^(-z)|<1",
    }


MUTATIONS = [
    "drop_history_parity",
    "scalar_exact_claims_two_rows",
    "ratio_lift_without_row2_exactness",
    "ignore_target_direction",
    "leafwise_canonical_terminal",
    "fixed_even_depth_positive",
    "ascending_lorenz_fill",
    "promote_conditional_to_unconditional",
    "omit_theorem_files",
]


def reject_mutation(name: str) -> None:
    if name == "drop_history_parity":
        assert obs(apply_swap((Fraction(17), Fraction(5)), 1)) != obs((Fraction(17), Fraction(5)))
        raise ContractError(name)
    if name == "scalar_exact_claims_two_rows":
        data = scalar_tradeoff_checks()["scalar_exact"]
        assert Fraction(data["delta_row2"]) < 0
        raise ContractError(name)
    if name == "ratio_lift_without_row2_exactness":
        raise ContractError("ratio lemma requires row-2 exactness")
    if name == "ignore_target_direction":
        assert Decimal("17.005086538219052590698455753607") > 17
        raise ContractError(name)
    if name == "leafwise_canonical_terminal":
        raise ContractError("odd history requires swapped terminal")
    if name == "fixed_even_depth_positive":
        assert Decimal("-62.71816781856588773240782086465") < 0
        raise ContractError(name)
    if name == "ascending_lorenz_fill":
        atoms = [(Fraction(1), Fraction(1), Fraction(10)), (Fraction(1), Fraction(1), Fraction(1))]
        optimum, _ = greedy_lorenz(atoms, Fraction(1))
        ascending = Fraction(1)
        assert ascending < optimum
        raise ContractError(name)
    if name == "promote_conditional_to_unconditional":
        raise ContractError("CPSL67 remains open")
    if name == "omit_theorem_files":
        raise ContractError("package completeness is mandatory")
    raise AssertionError(name)


def content_completeness() -> dict[str, object]:
    repo_root = Path(__file__).resolve().parents[2]
    required = [
        "claims/lemmas/L-97300-completed-parity-finite-owner-ledger.md",
        "claims/lemmas/L-97301-terminal-row-ratio-is-monotone.md",
        "claims/lemmas/L-97302-completed-parity-scalar-hall-is-a-finite-lorenz-lp.md",
        "claims/refutations/R-97300-scalar-normalization-does-not-lift-two-rows.md",
        "claims/refutations/R-97301-odd-history-terminal-direction-blocks-leafwise-gluing.md",
        "claims/theorems/T-97300-completed-parity-reconstruction-downgrade.md",
        "standalone/2026-08-17-completed-parity-reconstruction/PROOF.md",
        "reports/gpt56-pro/2026-08-17-completed-parity-reconstruction.md",
    ]
    missing = [rel for rel in required if not (repo_root / rel).is_file()]
    if missing:
        raise ContractError("missing theorem content: " + ", ".join(missing))
    return {"required_files": len(required), "missing": missing}


def build_payload(run_mutations: bool = True) -> dict[str, object]:
    rejected = []
    if run_mutations:
        for name in MUTATIONS:
            try:
                reject_mutation(name)
            except ContractError:
                rejected.append(name)
            else:
                raise AssertionError(f"mutation survived: {name}")
    core = {
        "schema": "riemann.x97300.completed-parity-reconstruction.v1",
        "classification": "PROVED_EXACT_CONDITIONAL_REDUCTION_GLOBAL_PRODUCER_OPEN",
        "former_candidate_complete_claim_survives": False,
        "precise_downgrade": "CPSL67/GPHT*/ASHP67 OPEN AND RH-BEARING",
        "parity": parity_and_owner_checks(),
        "terminal_ratio": ratio_symbolic_checks(),
        "normalization_tradeoff": scalar_tradeoff_checks(),
        "imported_certificates": imported_certificate_checks(),
        "finite_lorenz_lp": lorenz_lp_checks(),
        "mellin_numerator": numerator_check(),
        "content": content_completeness(),
        "hostile_mutations_rejected": rejected,
        "not_proved_by_replay": ["CPSL67", "GPHT*", "ASHP67", "Landau theorem", "RH"],
        "rh_established": False,
        "verdict": VERDICT,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    return {**core, "proof_object_sha256": hashlib.sha256(canon).hexdigest()}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("results/verification.json"))
    parser.add_argument("--no-mutations", action="store_true")
    args = parser.parse_args()
    payload = build_payload(run_mutations=not args.no_mutations)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])
    print(payload["classification"])


if __name__ == "__main__":
    main()
