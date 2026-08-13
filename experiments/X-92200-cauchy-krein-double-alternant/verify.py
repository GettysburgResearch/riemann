#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction as Q


def determinant(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    out = Q(1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if a[row][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        value = a[col][col]
        out *= value
        for j in range(col, n):
            a[col][j] /= value
        for row in range(col + 1, n):
            factor = a[row][col]
            if factor:
                for j in range(col, n):
                    a[row][j] -= factor * a[col][j]
    return out


def alternants(x, p):
    n = len(x)
    t = [value * value for value in x]
    if n % 2 == 0:
        m = n // 2
        a0 = [
            [t[i] ** j for j in range(m)]
            + [p[i] * t[i] ** j for j in range(m)]
            for i in range(n)
        ]
        a1 = [
            [t[i] ** j for j in range(m)]
            + [p[i] * t[i] ** j for j in range(1, m + 1)]
            for i in range(n)
        ]
        sign = -1 if m % 2 else 1
    else:
        m = (n - 1) // 2
        a0 = [
            [t[i] ** j for j in range(m)]
            + [p[i] * t[i] ** j for j in range(m + 1)]
            for i in range(n)
        ]
        a1 = [
            [t[i] ** j for j in range(m + 1)]
            + [p[i] * t[i] ** j for j in range(1, m + 1)]
            for i in range(n)
        ]
        sign = 1
    return determinant(a0), determinant(a1), sign


def kernel_determinant(x, p):
    n = len(x)
    matrix = [
        [(x[i] * p[i] + x[j] * p[j]) / (x[i] + x[j]) for j in range(n)]
        for i in range(n)
    ]
    return determinant(matrix)


def denominator(x):
    out = Q(1)
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            out *= (x[i] + x[j]) ** 2
    return out


def divided_difference(nodes, values):
    work = list(values)
    for level in range(1, len(nodes)):
        work = [
            (work[i + 1] - work[i]) / (nodes[i + level] - nodes[i])
            for i in range(len(nodes) - level)
        ]
    return work[0]


def check_order_four():
    x = [Q(1), Q(2), Q(3), Q(4)]
    t = [value * value for value in x]
    p = [Q(2), Q(3), Q(5), Q(7)]

    a0, a1, sign = alternants(x, p)
    assert sign == 1

    delta = Q(1)
    for i in range(4):
        for j in range(i + 1, 4):
            delta *= t[j] - t[i]

    tp = [t[i] * p[i] for i in range(4)]
    t2p = [t[i] * tp[i] for i in range(4)]

    reduced0 = determinant(
        [
            [divided_difference(t[:3], p[:3]), divided_difference(t[:3], tp[:3])],
            [divided_difference(t, p), divided_difference(t, tp)],
        ]
    )
    reduced1 = determinant(
        [
            [divided_difference(t[:3], tp[:3]), divided_difference(t[:3], t2p[:3])],
            [divided_difference(t, tp), divided_difference(t, t2p)],
        ]
    )

    assert a0 == delta * reduced0
    assert a1 == delta * reduced1
    return {
        "first_alternant": str(a0),
        "second_alternant": str(a1),
        "first_reduced_determinant": str(reduced0),
        "second_reduced_determinant": str(reduced1),
    }


def stieltjes_value(t):
    return Q(2, t + 1) + Q(3, t + 4) + Q(5, t + 9)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", required=True)
    args = parser.parse_args()

    order_checks = {}
    for n in range(1, 9):
        x = [Q(i + 1) for i in range(n)]
        p = [Q((i + 2) * (i + 3), i + 5) for i in range(n)]
        a0, a1, sign = alternants(x, p)
        direct = kernel_determinant(x, p)
        factored = sign * a0 * a1 / denominator(x)
        assert direct == factored
        order_checks[str(n)] = {
            "direct": str(direct),
            "first_alternant": str(a0),
            "second_alternant": str(a1),
            "sign": sign,
        }

    x = [Q(1), Q(2), Q(3), Q(4)]
    p = [stieltjes_value(value * value) for value in x]
    st_a0, st_a1, _ = alternants(x, p)
    assert st_a0 < 0 and st_a1 < 0

    result = {
        "status": "PASS_CAUCHY_KREIN_DOUBLE_ALTERNANT",
        "orders": order_checks,
        "order_four": check_order_four(),
        "stieltjes_order_four": {
            "first_alternant": str(st_a0),
            "second_alternant": str(st_a1),
        },
        "scope": {"exact_finite_algebra": True, "rh_proved": False},
    }

    with open(args.json, "w", encoding="utf-8") as handle:
        json.dump(result, handle, sort_keys=True, separators=(",", ":"))
        handle.write("\n")

    print(result["status"])


if __name__ == "__main__":
    main()
