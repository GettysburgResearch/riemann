#!/usr/bin/env python3
"""Exact regression for cycle-optimized fragmentation capacity debt."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parent
Edge = Tuple[int, int]
Flow = Dict[Edge, Fraction]


def mobius_table(n: int) -> List[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: List[int] = []
    lp = [0] * (n + 1)
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            lp[i * p] = p
            if p == lp[i]:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def edge(n: int, j: int) -> Edge:
    return (n, min(j, n - j))


def balanced_edges(x: int) -> List[Edge]:
    return [
        (n, j)
        for n in range(2, x + 1)
        for j in range((n + 3) // 4, n // 2 + 1)
    ]


def chi(e: Edge, q: int) -> int:
    n, j = e
    return n // q - j // q - (n - j) // q


def add(flow: Flow, e: Edge, value: Fraction) -> None:
    if value:
        flow[e] = flow.get(e, Fraction(0)) + value
        if flow[e] == 0:
            del flow[e]


def add_flows(*terms: Tuple[Fraction, Flow]) -> Flow:
    out: Flow = {}
    for scale, flow in terms:
        for e, value in flow.items():
            add(out, e, scale * value)
    return out


def tree(n: int, memo: Dict[int, Flow]) -> Flow:
    if n <= 1:
        return {}
    if n not in memo:
        j = n // 2
        memo[n] = add_flows(
            (Fraction(1), {edge(n, j): Fraction(1)}),
            (Fraction(1), tree(j, memo)),
            (Fraction(1), tree(n - j, memo)),
        )
    return dict(memo[n])


def fundamental_cycle(n: int, j: int, memo: Dict[int, Flow]) -> Flow:
    return add_flows(
        (Fraction(1), {edge(n, j): Fraction(1)}),
        (Fraction(1), tree(j, memo)),
        (Fraction(1), tree(n - j, memo)),
        (Fraction(-1), tree(n, memo)),
    )


def divergence(flow: Flow, x: int) -> List[Fraction]:
    r = [Fraction(0)] * (x + 1)
    for (n, j), value in flow.items():
        r[n] += value
        r[j] -= value
        r[n - j] -= value
    return r


def target(x: int) -> List[Fraction]:
    # Rational decreasing control with w(x)=0.
    w = [Fraction(0)] * (x + 1)
    for q in range(2, x + 1):
        w[q] = Fraction(x - q, x * q)
    return w


def target_divergence(w: List[Fraction]) -> List[Fraction]:
    x = len(w) - 1
    mu = mobius_table(x)
    u = [Fraction(0)] * (x + 2)
    for m in range(2, x + 1):
        u[m] = sum(
            Fraction(mu[k]) * w[m * k]
            for k in range(1, x // m + 1)
        )
    r = [Fraction(0)] * (x + 1)
    for m in range(2, x + 1):
        r[m] = u[m] - u[m + 1]
    r[1] = -sum(Fraction(m) * r[m] for m in range(2, x + 1))
    return r


def canonical_flow(r: List[Fraction]) -> Flow:
    x = len(r) - 1
    memo: Dict[int, Flow] = {}
    out: Flow = {}
    for m in range(2, x + 1):
        out = add_flows((Fraction(1), out), (r[m], tree(m, memo)))
    return out


def loads(flow: Flow, x: int) -> List[Fraction]:
    out = [Fraction(0)] * (x + 1)
    for q in range(2, x + 1):
        out[q] = sum(value * chi(e, q) for e, value in flow.items())
    return out


def capacities(edges: List[Edge], x: int) -> Dict[Edge, Fraction]:
    # Rational surrogate y_q=1/q. The algebra in L-27205 is valid for every
    # positive column weight; its RH consumer uses y_q=q^(-1/2).
    return {
        e: sum(Fraction(chi(e, q), q) for q in range(2, x + 1))
        for e in edges
    }


def negative_debt(flow: Flow, omega: Dict[Edge, Fraction]) -> Fraction:
    return sum(
        omega[e] * max(-flow.get(e, Fraction(0)), Fraction(0))
        for e in omega
    )


def proof_object() -> Dict[str, object]:
    divergence_checks = 0
    load_checks = 0
    baseline_checks = 0
    variation_checks = 0
    cycle_checks = 0
    dual_checks = 0
    mutation_checks = 0

    for x in range(6, 19):
        edges = balanced_edges(x)
        edge_set = set(edges)
        w = target(x)
        r = target_divergence(w)
        d0 = canonical_flow(r)
        assert set(d0).issubset(edge_set)
        assert divergence(d0, x) == r
        divergence_checks += 1
        assert loads(d0, x) == w
        load_checks += x - 1

        memo: Dict[int, Flow] = {}
        noncanonical = [
            e for e in edges if e != edge(e[0], e[0] // 2)
        ]
        d = dict(d0)
        for idx, (n, j) in enumerate(noncanonical):
            if idx % 5 == 0:
                cycle = fundamental_cycle(n, j, memo)
                assert divergence(cycle, x) == [Fraction(0)] * (x + 1)
                cycle_checks += 1
                d = add_flows(
                    (Fraction(1), d),
                    (Fraction((idx % 3) - 1, 3), cycle),
                )

        assert divergence(d, x) == r
        assert loads(d, x) == w

        omega = capacities(edges, x)
        signed = sum(d.get(e, Fraction(0)) * omega[e] for e in edges)
        baseline = sum(Fraction(1, q) * w[q] for q in range(2, x + 1))
        assert signed == baseline
        baseline_checks += 1

        total_variation = sum(
            abs(d.get(e, Fraction(0))) * omega[e] for e in edges
        )
        debt = negative_debt(d, omega)
        assert total_variation == baseline + 2 * debt
        variation_checks += 1

        positive_omega = [value for value in omega.values() if value > 0]
        assert positive_omega
        scale = min(positive_omega) / 2
        potential = [Fraction(0)] * (x + 1)
        for n in range(1, x + 1):
            potential[n] = scale * (n - 1)
        for n, j in edges:
            defect = potential[n] - potential[j] - potential[n - j]
            assert 0 <= defect <= omega[(n, j)]
        dual_value = -sum(r[n] * potential[n] for n in range(1, x + 1))
        assert dual_value <= debt
        dual_checks += 1

        if noncanonical:
            cycle = fundamental_cycle(*noncanonical[0], memo)
            mutated = dict(cycle)
            first = next(iter(mutated))
            mutated[first] += 1
            assert divergence(mutated, x) != [Fraction(0)] * (x + 1)
            mutation_checks += 1

    result = {
        "classification": "EXACT_CYCLE_CAPACITY_DEBT_IDENTITIES_VERIFIED",
        "maximum_X": 18,
        "divergence_checks": divergence_checks,
        "load_checks": load_checks,
        "baseline_checks": baseline_checks,
        "variation_checks": variation_checks,
        "cycle_checks": cycle_checks,
        "dual_weak_checks": dual_checks,
        "mutation_checks": mutation_checks,
        "weight_scope": "rational surrogate y_q=1/q",
        "scope": (
            "Exact finite linear algebra for arbitrary positive column weights. "
            "This checker does not prove the square-root-weight asymptotic CDT, "
            "MFT, or RH."
        ),
    }
    canonical = (
        json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    result = proof_object()
    out = ROOT / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
