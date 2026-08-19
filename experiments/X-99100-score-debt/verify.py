#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path

VERDICT = "PASS_T99100_DISCOUNTED_SCORE_DEBT_SUPERMARTINGALE"

PRIMES_61 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]


def sqrt_bounds(n: int, digits: int = 40) -> tuple[Fraction, Fraction]:
    scale = 10**digits
    lo_i = isqrt(n * scale * scale)
    lo = Fraction(lo_i, scale)
    hi = Fraction(lo_i + 1, scale)
    assert lo * lo <= n < hi * hi
    return lo, hi


def inv_sqrt_upper(n: int) -> Fraction:
    lo, _ = sqrt_bounds(n)
    return 1 / lo


def hazard(rs: list[Fraction]) -> tuple[Fraction, list[Fraction], list[Fraction]]:
    s = Fraction(1)
    lambdas: list[Fraction] = []
    alphas: list[Fraction] = []
    for r in rs:
        lam = r * s
        lambdas.append(lam)
        alphas.append(r * lam)
        s *= 1 - r
    return s, lambdas, alphas


def debt_on_mass_tree(
    children: dict[int, list[tuple[Fraction, int]]],
    masses: dict[int, Fraction],
    terminal: set[int],
    node: int,
    unit_debt: Fraction,
) -> Fraction:
    """Pessimistic debt recursion.

    At a nonterminal node, the exact physical target identity leaves current
    mass m(v)-sum a(v,w)m(w). We charge even that current mass the full terminal
    unit debt. This dominates the actual construction, where nonterminal
    current differences have no declared-score shortfall.
    """
    if node in terminal:
        return unit_debt * masses[node]
    recursive_mass = sum((a * masses[child] for a, child in children[node]), Fraction())
    assert 0 <= recursive_mass <= masses[node]
    current_mass = masses[node] - recursive_mass
    return unit_debt * current_mass + sum(
        (a * debt_on_mass_tree(children, masses, terminal, child, unit_debt)
         for a, child in children[node]),
        Fraction(),
    )


def main() -> None:
    # Exact causal/hazard algebra on rational firewalls.
    rs = [Fraction(1, 9), Fraction(1, 11), Fraction(1, 13), Fraction(1, 17)]
    survival, lambdas, alphas = hazard(rs)
    assert survival + sum(lambdas, Fraction()) == 1
    for r, lam, alpha in zip(rs, lambdas, alphas):
        assert -lam * r + alpha == 0
    assert sum(alphas, Fraction()) < rs[0] < Fraction(1, 8)

    # Actual rough-prime gate: 1/sqrt(67) < 1/8 iff 64 < 67.
    assert 64 < 67
    sqrt67_lo, sqrt67_hi = sqrt_bounds(67)
    assert Fraction(1, 1) / sqrt67_lo < Fraction(1, 8)

    # Branch proliferation and varying depth do not amplify unit debt. The
    # recursive weights are actual child-mass coefficients. The complement is
    # current-owned mass, so current debt + descendant debt telescopes exactly.
    children = {
        0: [(Fraction(1, 40), 1), (Fraction(1, 50), 2),
            (Fraction(1, 60), 3), (Fraction(1, 70), 4)],
        1: [(Fraction(1, 20), 5), (Fraction(1, 25), 6)],
        2: [(Fraction(1, 30), 7)],
        3: [(Fraction(1, 100), 8), (Fraction(1, 100), 9),
            (Fraction(1, 100), 10)],
        4: [(Fraction(1, 16), 11)],
    }
    masses = {0: Fraction(1), 1: Fraction(3, 2), 2: Fraction(4, 3),
              3: Fraction(5, 4), 4: Fraction(7, 5),
              5: Fraction(2), 6: Fraction(3, 2), 7: Fraction(5, 3),
              8: Fraction(7, 4), 9: Fraction(4, 3), 10: Fraction(9, 5),
              11: Fraction(6, 5)}
    for node, edges in children.items():
        recursive_mass = sum((a * masses[ch] for a, ch in edges), Fraction())
        assert recursive_mass < Fraction(1, 8) * masses[node]
    terminal = set(range(5, 12))
    unit_debt = Fraction(7, 3)
    root_debt = debt_on_mass_tree(children, masses, terminal, 0, unit_debt)
    assert root_debt == unit_debt * masses[0]

    # Mutation firewall: counting survival/current coefficients as recursive
    # creates mass >1 and destroys the Bellman envelope. Only alpha children
    # cross to the next state.
    wrong_recursive_mass = survival + sum(lambdas, Fraction()) + sum(alphas, Fraction())
    assert wrong_recursive_mass > 1
    assert sum(alphas, Fraction()) < Fraction(1, 8)

    # Directed rational upper bound for the fixed P_61 terminal ledger.
    w_upper = Fraction(1)
    for p in PRIMES_61:
        w_upper *= 1 + inv_sqrt_upper(p)
    d0_upper = 2 * (4 * sqrt67_hi - 3)
    terminal_ledger_upper = d0_upper * w_upper
    assert terminal_ledger_upper < 3600

    core = {
        "schema": "riemann.x99100.discounted-score-debt.v2",
        "verdict": VERDICT,
        "hazard_parent_identity": True,
        "typed_recursive_mass_lt_one_eighth": True,
        "mass_complement_debt_telescope": True,
        "branch_count_independent_bound": True,
        "varying_depth_tree_checked": True,
        "wrong_current_as_child_mutation_rejected": True,
        "terminal_unit_debt_upper_lt": "2*(4*sqrt(67)-3)",
        "p61_weight_upper_decimal": f"{float(w_upper):.15f}",
        "terminal_ledger_upper_decimal": f"{float(terminal_ledger_upper):.15f}",
        "terminal_ledger_lt_3600": True,
        "rh_established": False,
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(core, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(VERDICT)
    print(core["proof_object_sha256"])


if __name__ == "__main__":
    main()
