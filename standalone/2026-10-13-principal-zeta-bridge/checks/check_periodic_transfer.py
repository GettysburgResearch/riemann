#!/usr/bin/env python3
"""Exact finite controls for the periodic Abel identity and its sign.

The primitive inputs are piecewise linear rational functions. Direct
finite dilation sums and independently partitioned integrals must agree.
This checks endpoint/sign bookkeeping, not the infinite analytic theorems.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def chi(n):
    return (0, 1, -1)[n % 3]


def prefix(t):
    return int((t.numerator // t.denominator) % 3 == 1)


def value(nodes, x):
    if x <= nodes[0][0] or x >= nodes[-1][0]:
        return F(0)
    for (a, fa), (b, fb) in zip(nodes, nodes[1:]):
        if a <= x <= b:
            return fa + (fb - fa) * (x - a) / (b - a)
    raise RuntimeError("uncovered source interval")


def slope(nodes, x):
    for (a, fa), (b, fb) in zip(nodes, nodes[1:]):
        if a < x < b:
            return (fb - fa) / (b - a)
    return F(0)


def direct(nodes, d):
    return sum((chi(m) * value(nodes, d / m)
                for m in range(1, int(d / nodes[0][0]) + 1)), F(0))


def integral(nodes, d):
    # These breaks come from the full prefix-step function, independently
    # of whether an individual chi(m) happens to be zero.
    points = {F(0), d}
    points.update(x for x, _ in nodes if 0 < x < d)
    points.update(d / m for m in range(1, int(d / nodes[0][0]) + 2)
                  if 0 < d / m < d)
    signed, negative, absolute = F(0), F(0), F(0)
    points = sorted(points)
    for a, b in zip(points, points[1:]):
        mid = (a + b) / 2
        deriv = slope(nodes, mid)
        c = prefix(d / mid)
        signed += (b - a) * c * deriv
        negative += (b - a) * c * max(-deriv, F(0))
        absolute += (b - a) * abs(deriv)
    return signed, negative, absolute


def main():
    nodesets = [
        [(1, 0), (2, 3), (3, -2), (4, 1), (6, 0)],
        [(1, 0), (F(3, 2), -4), (F(5, 2), 2), (5, 0)],
        [(F(1, 2), 0), (F(4, 3), 1), (2, 0)],
        [(1, 0), (2, -1), (3, 0), (4, 5), (7, 0)],
    ]
    nodesets = [[(F(x), F(y)) for x, y in nodes] for nodes in nodesets]
    scales = sorted({F(j, q) for q in (1, 2, 3, 7, 11)
                     for j in range(1, 181) if F(j, q) <= 40})
    rows = []
    negative_outputs = positive_outputs = 0
    for source_id, nodes in enumerate(nodesets):
        for d in scales:
            a = direct(nodes, d)
            b, n, v = integral(nodes, d)
            if a != b:
                raise RuntimeError(f"Abel identity failure: {source_id}, {d}")
            if max(-a, F(0)) > n or abs(a) > v:
                raise RuntimeError(f"positive-kernel inequality failure: {source_id}, {d}")
            negative_outputs += a < 0
            positive_outputs += a > 0
            rows.append([source_id, str(d), str(a), str(n), str(v)])
    total = 0
    for n in range(1, 10001):
        total += chi(n)
        if total != prefix(F(n)) or total not in (0, 1):
            raise RuntimeError("periodic prefix sign failure")
    if not negative_outputs or not positive_outputs:
        raise RuntimeError("finite sources did not exercise both signs")
    data = json.dumps(rows, separators=(",", ":"), ensure_ascii=True).encode()
    print(json.dumps({
        "status": "PASS",
        "arithmetic": "exact fractions; no floating-point tolerance",
        "primitive_sources": len(nodesets),
        "distinct_scales": len(scales),
        "abel_and_inequality_cases": len(rows),
        "negative_outputs": negative_outputs,
        "positive_outputs": positive_outputs,
        "prefix_cases": 10000,
        "case_sha256": hashlib.sha256(data).hexdigest(),
        "scope": "finite endpoint/sign control; not a proof of a native moment or infinite transfer theorem",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
