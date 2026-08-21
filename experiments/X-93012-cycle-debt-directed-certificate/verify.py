#!/usr/bin/env python3
"""Exact rational replay for L-93012.

Checks the directed primal/dual bracket, three-part gap decomposition, contact
localization, and mutations. The analytic rank-sparsity argument is not authenticated by this replay.
"""

from __future__ import annotations

import json
import random
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Mapping, MutableMapping, Tuple

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "results" / "verification.json"


@dataclass(frozen=True, order=True)
class Action:
    parent: int
    left: int

    @property
    def right(self) -> int:
        return self.parent - self.left


def actions_up_to(x: int) -> Dict[int, List[Action]]:
    out: Dict[int, List[Action]] = {}
    for n in range(2, x + 1):
        lo = (n + 3) // 4
        hi = n // 2
        out[n] = [Action(n, j) for j in range(lo, hi + 1)]
        assert out[n]
    return out


def add(dst: MutableMapping[int, Fraction], key: int, value: Fraction) -> None:
    dst[key] = dst.get(key, Fraction(0)) + value


def p_eval(e: Action, f: Mapping[int, Fraction]) -> Fraction:
    return Fraction(e.left, e.parent) * f[e.left] + Fraction(e.right, e.parent) * f[e.right]


def channel_source(mass: Mapping[Action, Fraction], x: int) -> Dict[int, Fraction]:
    out = {n: Fraction(0) for n in range(1, x + 1)}
    for e, value in mass.items():
        add(out, e.parent, value)
        add(out, e.left, -value * Fraction(e.left, e.parent))
        add(out, e.right, -value * Fraction(e.right, e.parent))
    return out


def pair_source(
    plus: Mapping[Action, Fraction], minus: Mapping[Action, Fraction], x: int
) -> Dict[int, Fraction]:
    a = channel_source(plus, x)
    b = channel_source(minus, x)
    return {n: a[n] - b[n] for n in range(1, x + 1)}


def build_superharmonic_potential(
    rng: random.Random, by_parent: Mapping[int, List[Action]], x: int
) -> Dict[int, Fraction]:
    f: Dict[int, Fraction] = {1: Fraction(0)}
    for n in range(2, x + 1):
        peak = max(p_eval(e, f) for e in by_parent[n])
        # Sometimes touch the lower envelope exactly, sometimes stay above it.
        lift = Fraction(0) if n % 3 == 0 else Fraction(rng.randint(1, 5), n + 7)
        f[n] = peak + lift
    return f


def run_cases(rng: random.Random, repetitions: int = 137) -> Tuple[int, int, int, Fraction]:
    identities = 0
    contact_checks = 0
    mutations = 0
    max_gap = Fraction(0)

    for case in range(repetitions):
        x = 9 + case % 13
        by_parent = actions_up_to(x)
        actions = [e for rows in by_parent.values() for e in rows]
        f = build_superharmonic_potential(rng, by_parent, x)

        plus: Dict[Action, Fraction] = {}
        minus: Dict[Action, Fraction] = {}
        c_lo: Dict[Action, Fraction] = {}
        c_hi: Dict[Action, Fraction] = {}
        delta: Dict[Action, Fraction] = {}

        for e in actions:
            delta[e] = f[e.parent] - p_eval(e, f)
            assert delta[e] >= 0
            lower_slack = Fraction(rng.randint(0, 5), e.parent + 11)
            width = Fraction(rng.randint(0, 4), 3 * e.parent + 17)
            c_lo[e] = delta[e] + lower_slack
            c_hi[e] = c_lo[e] + width
            plus[e] = Fraction(rng.randint(0, 7), rng.randint(1, 11))
            minus[e] = Fraction(rng.randint(0, 7), rng.randint(1, 11))

        source = pair_source(plus, minus, x)
        dual = -sum((source[n] * f[n] for n in range(1, x + 1)), Fraction(0))
        upper = sum((minus[e] * c_hi[e] for e in actions), Fraction(0))

        positive_defect = sum((plus[e] * delta[e] for e in actions), Fraction(0))
        negative_defect = sum(
            (minus[e] * (c_lo[e] - delta[e]) for e in actions), Fraction(0)
        )
        enclosure_debt = sum(
            (minus[e] * (c_hi[e] - c_lo[e]) for e in actions), Fraction(0)
        )
        gap = upper - dual
        assert gap == positive_defect + negative_defect + enclosure_debt
        assert gap >= 0
        identities += 4
        max_gap = max(max_gap, gap)

        # Exact dual feasibility against the lower directed enclosure.
        assert all(Fraction(0) <= delta[e] <= c_lo[e] for e in actions)
        identities += len(actions)

        # Contact localization for several exact thresholds.
        for eta in (Fraction(1, 100), Fraction(1, 20), Fraction(1, 5), Fraction(1, 2)):
            outside_plus = sum((plus[e] for e in actions if delta[e] >= eta), Fraction(0))
            outside_minus = sum(
                (minus[e] for e in actions if c_lo[e] - delta[e] >= eta), Fraction(0)
            )
            unresolved_minus = sum(
                (minus[e] for e in actions if c_hi[e] - c_lo[e] >= eta), Fraction(0)
            )
            assert outside_plus * eta <= gap
            assert outside_minus * eta <= gap
            assert unresolved_minus * eta <= gap
            contact_checks += 3

        # Mutation 1: an inner enclosure below a dual drift is rejected.
        chosen = max(actions, key=lambda e: delta[e])
        if delta[chosen] > 0:
            bad_lo = dict(c_lo)
            bad_lo[chosen] = delta[chosen] - Fraction(1, 997)
            assert not all(Fraction(0) <= delta[e] <= bad_lo[e] for e in actions)
            mutations += 1

        # Mutation 2: dropping interval uncertainty breaks the exact gap if present.
        if enclosure_debt > 0:
            assert gap != positive_defect + negative_defect
            mutations += 1

        # Mutation 3: changing one source coordinate breaks the pairing identity.
        changed_source = dict(source)
        changed_source[x] += Fraction(1, 991)
        changed_dual = -sum(
            (changed_source[n] * f[n] for n in range(1, x + 1)), Fraction(0)
        )
        assert upper - changed_dual != gap
        mutations += 1

    return identities, contact_checks, mutations, max_gap


def main() -> None:
    rng = random.Random(93012)
    identities, contact_checks, mutations, max_gap = run_cases(rng)
    payload = {
        "verdict": "PASS_X_93012_CYCLE_DEBT_DIRECTED_INTERVAL_CERTIFICATE",
        "arithmetic": "EXACT_RATIONAL",
        "gap_and_feasibility_identities": identities,
        "contact_localization_checks": contact_checks,
        "mutations_detected": mutations,
        "maximum_synthetic_gap": str(max_gap),
        "proves": [
            "finite directed primal-dual bracket algebra",
            "exact three-part gap decomposition",
            "finite contact-set localization inequalities",
        ],
        "analytic_steps_not_replayed": [
            "minimal-support rank-sparsity argument",
        ],
        "does_not_prove": [
            "actual critical Cycle-Debt certificate",
            "cofinal subpower debt",
            "Riemann Hypothesis",
        ],
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["verdict"])
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
