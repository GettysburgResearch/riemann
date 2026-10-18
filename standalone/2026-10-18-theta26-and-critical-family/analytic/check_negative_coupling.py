#!/usr/bin/env python3
"""Exact finite algebra checks for NEGATIVE_COUPLING_STRIP.md.

These checks do not establish an infinite theta approximation or a zeta bound.
All acceptance conditions remain active under python -O.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def multiply(p, q):
    result = {}
    for left, a in p.items():
        for right, b in q.items():
            require(not left & right, "incidence variables must be disjoint")
            key = left | right
            result[key] = result.get(key, F(0)) + a * b
    return result


def contract(p, x, y, z):
    """A + Bx + Cy + Dxy -> A + Dz, with coefficients multiaffine."""
    result = {}
    for variables, coefficient in p.items():
        contains_x, contains_y = x in variables, y in variables
        if contains_x != contains_y:
            continue
        key = variables - {x, y}
        if contains_x:
            key = key | {z}
        result[key] = result.get(key, F(0)) + coefficient
    return result


def check_graph(n, edges):
    p = {frozenset(): F(1)}
    incidence = [[] for _ in range(n)]
    for k, (i, j, c) in enumerate(edges):
        x, y = ("edge", k, i), ("edge", k, j)
        incidence[i].append(x)
        incidence[j].append(y)
        p = multiply(p, {frozenset(): F(1), frozenset([x]): c,
                         frozenset([y]): c, frozenset([x, y]): F(1)})
    for i in range(n):
        variables = incidence[i]
        if not variables:
            x = ("isolated", i)
            variables.append(x)
            p = multiply(p, {frozenset(): F(1), frozenset([x]): F(1)})
        current = variables[0]
        for k, other in enumerate(variables[1:]):
            combined = ("contracted", i, k)
            p = contract(p, current, other, combined)
            current = combined
        vertex = ("vertex", i)
        p = {(key - {current}) | ({vertex} if current in key else set()): value
             for key, value in p.items()}
    direct = {}
    for mask in range(1 << n):
        subset = frozenset(("vertex", i) for i in range(n) if mask & (1 << i))
        coefficient = F(1)
        for i, j, c in edges:
            if bool(mask & (1 << i)) != bool(mask & (1 << j)):
                coefficient *= c
        direct[subset] = coefficient
    require(p == direct, "contracted incidence polynomial != complete partition")
    vertices = frozenset(("vertex", i) for i in range(n))
    require(all(p[key] == p[vertices - key] for key in p), "spin reversal failed")
    return {"vertices": n, "edges": len(edges), "configurations": len(direct),
            "contraction_and_reciprocity": "PASS"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    cases = [
        (2, [(0, 1, F(5, 4))]),
        (3, [(0, 1, F(1, 2)), (1, 2, F(5, 4)), (2, 0, F(1))]),
        (4, [(0, 1, F(5, 4)), (0, 2, F(1, 2)), (0, 3, F(1, 3)),
             (1, 2, F(7, 6)), (1, 3, F(2, 3)), (2, 3, F(1))]),
        (5, [(0, 1, F(5, 4)), (1, 2, F(1, 2)), (2, 0, F(1, 3))]),
    ]
    graphs = [check_graph(n, edges) for n, edges in cases]
    budgets = []
    for c, ri, rj in [(F(5, 4), F(1, 2), F(1, 2)),
                       (F(5, 4), F(1, 3), F(7, 11)),
                       (F(7, 6), F(1, 4), F(3, 5))]:
        margin = 1 + ri * rj - c * (ri + rj)
        require(margin >= 0 and 0 < ri < 1 / c and 0 < rj < 1 / c,
                "invalid edge disk budget")
        edge_product = (1 - ri) * (1 - rj) / ((1 + ri) * (1 + rj))
        require(edge_product >= (c - 1) / (c + 1), "tanh budget failed")
        minimum = (1 - c * ri) / (c - ri)
        require(minimum >= rj, "fractional-linear disk minimum failed")
        budgets.append({"c": str(c), "ri": str(ri), "rj": str(rj),
                        "disk_margin": str(margin), "minimum": str(minimum)})
    barrier, variance_upper = F(2323, 50000), F(4621, 100000)
    margin = barrier - barrier ** 2 / 9 - variance_upper
    require(margin == F(228671, 22500000000) and margin > 0,
            "theta variance barrier failed")
    here = Path(__file__).resolve().parent
    hashes = {name: hashlib.sha256((here / name).read_bytes()).hexdigest()
              for name in ["NEGATIVE_COUPLING_STRIP.md", Path(__file__).name]}
    report = {"status": "PASS", "scope": "finite exact algebra; no zeta bound",
              "graphs": graphs, "edge_budgets": budgets,
              "theta_variance_barrier": str(barrier), "barrier_margin": str(margin),
              "sha256": hashes}
    output = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
