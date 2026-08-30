#!/usr/bin/env python3
"""Exact small extension-field scout of a COMPLETE degree-two owner fibre.

All unordered owner pairs, cross-owner disjointness, core exclusions and
quadratic classes are included. No floating character evaluations occur.
"""

from __future__ import annotations

import json
from collections import Counter
from itertools import combinations


class Field:
    def __init__(self, p: int, nonsquare: int):
        if (
            type(p) is not int
            or type(nonsquare) is not int
            or p not in (5, 7)
            or not 1 < nonsquare < p
            or pow(nonsquare, (p - 1) // 2, p) != p - 1
        ):
            raise ValueError("fixed small quadratic field required")
        self.p, self.nonsquare, self.q = p, nonsquare, p * p

    def add(self, x, y):
        return (x % self.p + y % self.p) % self.p + self.p * (
            (x // self.p + y // self.p) % self.p
        )

    def neg(self, x):
        return (-(x % self.p)) % self.p + self.p * ((-(x // self.p)) % self.p)

    def sub(self, x, y):
        return ((x % self.p - y % self.p) % self.p) + self.p * (
            (x // self.p - y // self.p) % self.p
        )

    def mul(self, x, y):
        a, b, c, d = x % self.p, x // self.p, y % self.p, y // self.p
        return (a * c + self.nonsquare * b * d) % self.p + self.p * (
            (a * d + b * c) % self.p
        )

    def power(self, x, exponent):
        if (
            type(x) is not int
            or not 0 <= x < self.q
            or type(exponent) is not int
            or not 0 <= exponent <= 5000
        ):
            raise ValueError("bounded finite-field exponent required")
        result = 1
        while exponent:
            if exponent & 1:
                result = self.mul(result, x)
            x = self.mul(x, x)
            exponent //= 2
        return result

    def quadratic(self, x):
        if not x:
            return 0
        result = self.power(x, (self.q - 1) // 2)
        if result not in (1, self.p - 1):
            raise ValueError("quadratic character image")
        return 1 if result == 1 else -1

    def trace(self, x):
        return 2 * (x % self.p) % self.p


def fibre(field, lam, rho, h, k, extra_excluded=(3,)):
    if not isinstance(field, Field) or any(
        type(x) is not int or not 0 <= x < field.q for x in (lam, rho, h, k)
    ):
        raise ValueError("finite-field parameter type/range")
    if not h or not k or type(extra_excluded) is not tuple or extra_excluded != (3,):
        raise ValueError("nonzero phase and fixed marked exclusion required")
    if lam == rho or len({0, 1, 2, lam, rho, *extra_excluded}) != 5 + len(
        extra_excluded
    ):
        raise ValueError("distinct core/marked roots required")
    excluded = {0, 1, 2, lam, rho, *extra_excluded}
    available = [x for x in range(field.q) if x not in excluded]
    d2 = field.mul(field.sub(rho, lam), field.sub(rho, lam))
    records = []
    for a, b in combinations(available, 2):
        x = field.mul(d2, field.mul(field.sub(rho, a), field.sub(rho, b)))
        y = field.mul(d2, field.mul(field.sub(lam, a), field.sub(lam, b)))
        records.append((1 << a | 1 << b, x, y, field.quadratic(x), field.quadratic(y)))
    counts = Counter()
    phases = {key: [0] * field.p for key in ((-1, -1), (-1, 1), (1, -1), (1, 1))}
    residues = {key: Counter() for key in phases}
    ktrace = [field.trace(field.mul(k, x)) for x in range(field.q)]
    htrace = [field.trace(field.mul(h, y)) for y in range(field.q)]
    for mask_p, x, _, tau, _ in records:
        for mask_q, _, y, _, sigma in records:
            if mask_p & mask_q:
                continue
            key = (sigma, tau)
            counts[key] += 1
            phases[key][(ktrace[x] - htrace[y]) % field.p] += 1
            residues[key][(x, y)] += 1
    expected = (
        len(available)
        * (len(available) - 1)
        * (len(available) - 2)
        * (len(available) - 3)
        // 4
    )
    if sum(counts.values()) != expected:
        raise ValueError("complete owner coverage")

    def cyclotomic(row):
        return [value - row[-1] for value in row[:-1]]

    current = sum(36 * 36 * count * count - 36 * count for count in counts.values())
    return {
        "parameters": {"lambda": lam, "rho": rho, "h": h, "k": k},
        "available_roots": len(available),
        "owner_pair_count": len(records),
        "complete_bilateral_count": expected,
        "quadratic_class_counts": {str(key): counts[key] for key in phases},
        "exact_additive_characters": {
            str(key): cyclotomic(phases[key]) for key in phases
        },
        "nonempty_residue_cells": {str(key): len(residues[key]) for key in phases},
        "integer_principal_literal_wick": current,
    }


def main():
    field = Field(5, 2)
    results = []
    for lam, rho in ((5, 6), (5, 7), (5, 12), (6, 12)):
        h, k = 1, 2
        original = fibre(field, lam, rho, h, k)
        left = fibre(field, field.power(lam, field.p), rho, field.power(h, field.p), k)
        total = fibre(
            field,
            field.power(lam, field.p),
            field.power(rho, field.p),
            field.power(h, field.p),
            field.power(k, field.p),
        )
        results.append(
            {
                "original": original,
                "left_partial": left,
                "total": total,
                "principal_partial_defect": left["integer_principal_literal_wick"]
                - original["integer_principal_literal_wick"],
                "principal_total_defect": total["integer_principal_literal_wick"]
                - original["integer_principal_literal_wick"],
            }
        )
    print(
        json.dumps(
            {
                "field": "F5[a]/(a^2-2)",
                "status": "EXACT_COMPLETE_OWNER_SCOUT",
                "results": results,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
