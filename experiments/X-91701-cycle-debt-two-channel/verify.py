#!/usr/bin/env python3
"""Exact finite replay for L-93010 and L-93011.

This checker authenticates only the finite algebraic identities:
- signed split flows <-> two nonnegative Markov channels;
- exact negative-channel cost;
- Bellman-envelope dual feasibility;
- bang-bang complementary slackness and primal/dual equality.

It does not evaluate the repository's irrational carry capacities, construct the
critical Möbius source, prove a cofinal bound, or prove RH.
"""

from __future__ import annotations

import json
import random
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, MutableMapping, Tuple

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
    """Quarter-balanced unordered actions, including the central action."""
    out: Dict[int, List[Action]] = {}
    for n in range(2, x + 1):
        lo = (n + 3) // 4
        hi = n // 2
        out[n] = [Action(n, j) for j in range(lo, hi + 1)]
        assert out[n], n
    return out


def add(dst: MutableMapping[int, Fraction], key: int, value: Fraction) -> None:
    dst[key] = dst.get(key, Fraction(0)) + value


def split_divergence(flow: Mapping[Action, Fraction], x: int) -> Dict[int, Fraction]:
    r = {n: Fraction(0) for n in range(1, x + 1)}
    for e, value in flow.items():
        add(r, e.parent, value)
        add(r, e.left, -value)
        add(r, e.right, -value)
    return r


def channel_divergence(mass: Mapping[Action, Fraction], x: int) -> Dict[int, Fraction]:
    """Return M(I-P), directly from action mass x_e = parent * d_e."""
    out = {n: Fraction(0) for n in range(1, x + 1)}
    for e, value in mass.items():
        add(out, e.parent, value)
        add(out, e.left, -value * Fraction(e.left, e.parent))
        add(out, e.right, -value * Fraction(e.right, e.parent))
    return out


def size_weight(r: Mapping[int, Fraction]) -> Dict[int, Fraction]:
    return {n: n * r.get(n, Fraction(0)) for n in r}


def reconstruct_flow(
    plus: Mapping[Action, Fraction], minus: Mapping[Action, Fraction]
) -> Dict[Action, Fraction]:
    keys = set(plus) | set(minus)
    return {
        e: (plus.get(e, Fraction(0)) - minus.get(e, Fraction(0))) / e.parent
        for e in keys
    }


def channel_cost(minus: Mapping[Action, Fraction], cost: Mapping[Action, Fraction]) -> Fraction:
    return sum((minus.get(e, Fraction(0)) * cost[e] for e in cost), Fraction(0))


def flow_cost(flow: Mapping[Action, Fraction], cost: Mapping[Action, Fraction]) -> Fraction:
    return sum(
        (e.parent * cost[e] * max(-flow.get(e, Fraction(0)), Fraction(0)) for e in cost),
        Fraction(0),
    )


def p_eval(e: Action, f: Mapping[int, Fraction]) -> Fraction:
    return Fraction(e.left, e.parent) * f[e.left] + Fraction(e.right, e.parent) * f[e.right]


def run_signed_flow_cases(rng: random.Random, x: int, repetitions: int) -> Tuple[int, int]:
    by_parent = actions_up_to(x)
    actions = [e for rows in by_parent.values() for e in rows]
    identities = 0
    mutations = 0

    for _ in range(repetitions):
        flow: Dict[Action, Fraction] = {}
        costs: Dict[Action, Fraction] = {}
        for e in actions:
            numerator = rng.randint(-5, 5)
            denominator = rng.randint(1, 7)
            flow[e] = Fraction(numerator, denominator)
            costs[e] = Fraction(rng.randint(1, 13), rng.randint(1, 11))

        r = split_divergence(flow, x)
        s = size_weight(r)
        plus = {e: e.parent * max(flow[e], Fraction(0)) for e in actions}
        minus = {e: e.parent * max(-flow[e], Fraction(0)) for e in actions}

        d_plus = channel_divergence(plus, x)
        d_minus = channel_divergence(minus, x)
        assert all(s[n] == d_plus[n] - d_minus[n] for n in range(1, x + 1))
        identities += x

        rebuilt = reconstruct_flow(plus, minus)
        assert all(rebuilt[e] == flow[e] for e in actions)
        identities += len(actions)

        assert channel_cost(minus, costs) == flow_cost(flow, costs)
        identities += 1

        # A sign mutation must be visible in the source equation.
        chosen = next(e for e in actions if flow[e] != 0)
        mutated_plus = dict(plus)
        mutated_plus[chosen] += Fraction(1, 17)
        mutated_div = channel_divergence(mutated_plus, x)
        assert any(s[n] != mutated_div[n] - d_minus[n] for n in range(1, x + 1))
        mutations += 1

    return identities, mutations


def run_overlap_cases(rng: random.Random, x: int, repetitions: int) -> Tuple[int, int]:
    by_parent = actions_up_to(x)
    actions = [e for rows in by_parent.values() for e in rows]
    identities = 0
    strict_cancellations = 0

    for _ in range(repetitions):
        plus: Dict[Action, Fraction] = {}
        minus: Dict[Action, Fraction] = {}
        costs: Dict[Action, Fraction] = {}
        for e in actions:
            plus[e] = Fraction(rng.randint(0, 7), rng.randint(1, 9))
            minus[e] = Fraction(rng.randint(0, 7), rng.randint(1, 9))
            costs[e] = Fraction(rng.randint(1, 17), rng.randint(1, 13))

        source = {
            n: channel_divergence(plus, x)[n] - channel_divergence(minus, x)[n]
            for n in range(1, x + 1)
        }
        flow = reconstruct_flow(plus, minus)
        r = split_divergence(flow, x)
        assert all(source[n] == n * r[n] for n in range(1, x + 1))
        identities += x

        original_channel_cost = channel_cost(minus, costs)
        assert flow_cost(flow, costs) <= original_channel_cost
        identities += 1

        cancelled_plus: Dict[Action, Fraction] = {}
        cancelled_minus: Dict[Action, Fraction] = {}
        removed = Fraction(0)
        for e in actions:
            common = min(plus[e], minus[e])
            cancelled_plus[e] = plus[e] - common
            cancelled_minus[e] = minus[e] - common
            removed += common * costs[e]
            assert cancelled_plus[e] == 0 or cancelled_minus[e] == 0

        new_source = {
            n: channel_divergence(cancelled_plus, x)[n]
            - channel_divergence(cancelled_minus, x)[n]
            for n in range(1, x + 1)
        }
        assert new_source == source
        assert channel_cost(cancelled_minus, costs) == original_channel_cost - removed
        identities += x + 1
        if removed > 0:
            strict_cancellations += 1

    return identities, strict_cancellations


def build_exact_certificate(x: int) -> Tuple[
    Dict[int, List[Action]],
    Dict[int, Fraction],
    Dict[Action, Fraction],
    Dict[Action, Fraction],
    Dict[Action, Fraction],
]:
    """Construct a nontrivial exact primal-dual certificate synthetically."""
    by_parent = actions_up_to(x)
    f: Dict[int, Fraction] = {1: Fraction(0), 2: Fraction(1, 2)}

    for n in range(3, x + 1):
        f[n] = max(p_eval(e, f) for e in by_parent[n])

    cost: Dict[Action, Fraction] = {}
    plus: Dict[Action, Fraction] = {}
    minus: Dict[Action, Fraction] = {}

    # Parent two seeds a nonzero potential and carries only negative mass.
    e2 = by_parent[2][0]
    delta2 = f[2] - p_eval(e2, f)
    assert delta2 > 0
    cost[e2] = delta2
    plus[e2] = Fraction(0)
    minus[e2] = Fraction(2, 3)

    for n in range(3, x + 1):
        rows = by_parent[n]
        deltas = {e: f[n] - p_eval(e, f) for e in rows}
        assert min(deltas.values()) == 0

        lower = min((e for e in rows if deltas[e] == 0), key=lambda e: e.left)
        upper_candidates = [e for e in rows if deltas[e] > 0]
        upper = max(upper_candidates, key=lambda e: deltas[e]) if upper_candidates else None

        for e in rows:
            if e == upper:
                cost[e] = deltas[e]
            else:
                cost[e] = deltas[e] + Fraction(1, n + 5)
            plus[e] = Fraction(0)
            minus[e] = Fraction(0)

        plus[lower] = Fraction(n + 1, n + 3)
        if upper is not None:
            minus[upper] = Fraction(n + 2, 2 * n + 5)

    return by_parent, f, cost, plus, minus


def run_certificate_case(x: int) -> Tuple[int, int, Dict[str, str]]:
    by_parent, f, cost, plus, minus = build_exact_certificate(x)
    identities = 0
    mutations = 0

    # Complete Bellman feasibility and envelopes.
    for n, rows in by_parent.items():
        pvals = [p_eval(e, f) for e in rows]
        upper_vals = [p_eval(e, f) + cost[e] for e in rows]
        lower_envelope = max(pvals)
        upper_envelope = min(upper_vals)
        assert lower_envelope <= f[n] <= upper_envelope
        identities += 1
        for e in rows:
            delta = f[n] - p_eval(e, f)
            assert Fraction(0) <= delta <= cost[e]
            identities += 1
            if plus[e] > 0:
                assert delta == 0
                identities += 1
            if minus[e] > 0:
                assert delta == cost[e]
                identities += 1
        if any(plus[e] > 0 for e in rows):
            assert f[n] == lower_envelope
            identities += 1
        if any(minus[e] > 0 for e in rows):
            assert f[n] == upper_envelope
            identities += 1

    d_plus = channel_divergence(plus, x)
    d_minus = channel_divergence(minus, x)
    source = {n: d_plus[n] - d_minus[n] for n in range(1, x + 1)}
    primal = channel_cost(minus, cost)
    dual = -sum((source[n] * f[n] for n in range(1, x + 1)), Fraction(0))
    assert primal == dual
    identities += x + 1

    # The reconstructed signed flow is a feasible original primal with the same cost.
    flow = reconstruct_flow(plus, minus)
    r = split_divergence(flow, x)
    assert all(source[n] == n * r[n] for n in range(1, x + 1))
    assert flow_cost(flow, cost) == primal
    identities += x + 1

    # Mutating one occupied upper-tight capacity destroys equality but not feasibility.
    occupied_negative = next(e for e, value in minus.items() if value > 0)
    mutated_cost = dict(cost)
    mutated_cost[occupied_negative] += Fraction(1, 101)
    mutated_primal = channel_cost(minus, mutated_cost)
    assert mutated_primal > dual
    mutations += 1

    # Mutating one lower-tight support to a non-tight action creates a positive gap.
    candidate_parent = next(
        n
        for n, rows in by_parent.items()
        if any(plus[e] > 0 for e in rows)
        and any(f[n] - p_eval(e, f) > 0 for e in rows)
    )
    rows = by_parent[candidate_parent]
    old = next(e for e in rows if plus[e] > 0)
    new = next(e for e in rows if f[candidate_parent] - p_eval(e, f) > 0)
    mutated_plus = dict(plus)
    moved = mutated_plus[old]
    mutated_plus[old] = Fraction(0)
    mutated_plus[new] += moved
    mutated_source = {
        n: channel_divergence(mutated_plus, x)[n] - d_minus[n]
        for n in range(1, x + 1)
    }
    mutated_dual = -sum(
        (mutated_source[n] * f[n] for n in range(1, x + 1)), Fraction(0)
    )
    assert mutated_dual < primal
    mutations += 1

    details = {
        "primal_value": str(primal),
        "dual_value": str(dual),
        "states": str(x),
        "actions": str(sum(len(v) for v in by_parent.values())),
    }
    return identities, mutations, details


def main() -> None:
    rng = random.Random(91701)
    signed_identities, signed_mutations = run_signed_flow_cases(rng, x=18, repetitions=113)
    overlap_identities, strict_cancellations = run_overlap_cases(rng, x=16, repetitions=89)
    cert_identities, cert_mutations, cert_details = run_certificate_case(x=24)

    payload = {
        "verdict": "PASS_X_91701_CYCLE_DEBT_TWO_CHANNEL_MARKOV_CONTROL",
        "arithmetic": "EXACT_RATIONAL",
        "signed_flow_identities": signed_identities,
        "signed_flow_mutations_detected": signed_mutations,
        "overlap_identities": overlap_identities,
        "overlap_cases_with_strict_cost_reduction": strict_cancellations,
        "certificate_identities": cert_identities,
        "certificate_mutations_detected": cert_mutations,
        "certificate": cert_details,
        "proves": [
            "finite two-channel source identity",
            "finite cost identity and overlap cancellation",
            "finite Bellman-envelope feasibility",
            "finite bang-bang primal-dual equality",
        ],
        "does_not_prove": [
            "actual irrational carry-capacity evaluation",
            "critical Mobius source estimate",
            "cofinal subpower Cycle Debt",
            "Riemann Hypothesis",
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["verdict"])
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
