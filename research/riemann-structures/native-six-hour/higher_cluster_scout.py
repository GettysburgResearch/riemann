#!/usr/bin/env python3
"""Exact active-set discovery for complete native cardinality-band limits."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1
from itertools import combinations, pairwise
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
SOURCES = {
    "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md": "6810bcece309b0c54ae6c8fc84b314990004549c",
    "claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md": "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
}
PANELS = (
    (0, 1),
    (0, 1, 2),
    (0, 1, 4),
    (0, 1, 2, 3),
    (0, 1, 2, 4),
    (0, 2, 3, 4),
    (0, 1, 3, 4),
    (0, 1, 4, 6),
    (0, 3, 4, 5),
    (0, 1, 2, 3, 4),
    (0, 1, 2, 3, 4, 5),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_shape(shape):
    require(type(shape) is tuple and 2 <= len(shape) <= 6, "bounded source arity")
    require(
        all(type(x) is int and 0 <= x <= 12 for x in shape),
        "exact shape coordinate cap",
    )
    require(all(a < b for a, b in pairwise(shape)), "strictly increasing source shape")


def matrices(shape):
    validate_shape(shape)
    r = len(shape)
    direct = [[0] * r for _ in range(r)]
    gaps = [[0] * r for _ in range(r)]
    bands, pair_count = [], 0
    for k in range(1, r + 1):
        supports = tuple(combinations(range(r), k))
        rows = tuple((sum(shape[j] for j in support), support) for support in supports)
        pair_count += len(rows) ** 2
        for x, S in rows:
            for y, T in rows:
                distance = abs(x - y)
                for i in S:
                    for j in T:
                        direct[i][j] += distance
        distinct = sorted({x for x, _ in rows})
        cumulative = [0] * r
        mass = comb(r - 1, k - 1)
        cuts = []
        for x, y in pairwise(distinct):
            for at, support in rows:
                if at == x:
                    for j in support:
                        cumulative[j] += 1
            distance = y - x
            cuts.append(
                {
                    "left_location": x,
                    "right_location": y,
                    "cumulative_coefficient_counts": cumulative.copy(),
                    "total_mass_on_simplex": mass,
                }
            )
            for i in range(r):
                for j in range(r):
                    gaps[i][j] += distance * (
                        cumulative[i] * (mass - cumulative[j])
                        + cumulative[j] * (mass - cumulative[i])
                    )
        bands.append(
            {
                "cardinality": k,
                "source_subset_count": len(rows),
                "distinct_subset_sum_count": len(distinct),
                "cuts": cuts,
            }
        )
    require(direct == gaps, "independent ordered-pair and cumulative-distance matrices")
    require(
        all(direct[i][j] == direct[j][i] for i in range(r) for j in range(r)),
        "exact symmetric source matrix",
    )
    require(pair_count == comb(2 * r, r) - 1, "all nonempty cardinality pair count")
    return tuple(tuple(row) for row in direct), bands, pair_count


def solve(matrix, target):
    n = len(matrix)
    require(
        1 <= n <= 7 and len(target) == n and all(len(row) == n for row in matrix),
        "bounded rational KKT system",
    )
    augmented = [
        [F(value) for value in row] + [F(target[i])] for i, row in enumerate(matrix)
    ]
    for j in range(n):
        pivot = next((i for i in range(j, n) if augmented[i][j]), None)
        require(pivot is not None, "strictly concave active-face KKT invertibility")
        augmented[j], augmented[pivot] = augmented[pivot], augmented[j]
        divisor = augmented[j][j]
        augmented[j] = [value / divisor for value in augmented[j]]
        for i in range(n):
            if i == j:
                continue
            multiplier = augmented[i][j]
            augmented[i] = [
                a - multiplier * b
                for a, b in zip(augmented[i], augmented[j], strict=True)
            ]
        require(
            all(
                max(value.numerator.bit_length(), value.denominator.bit_length()) <= 512
                for row in augmented
                for value in row
            ),
            "exact KKT bit cap",
        )
    return tuple(row[-1] for row in augmented)


def matrix_action(matrix, vector):
    return tuple(
        sum((F(value) * q for value, q in zip(row, vector, strict=True)), F())
        for row in matrix
    )


def objective(matrix, vector):
    return sum(
        (a * b for a, b in zip(vector, matrix_action(matrix, vector), strict=True)), F()
    )


def active_sets(matrix):
    r = len(matrix)
    require(2 <= r <= 6, "active support cap")
    accepted = []
    checked = 0
    for size in range(1, r + 1):
        for active in combinations(range(r), size):
            checked += 1
            block = [[F(matrix[i][j]) for j in active] + [F(-1)] for i in active]
            block.append([F(1)] * size + [F(0)])
            solved = solve(block, [F(0)] * size + [F(1)])
            if any(q <= 0 for q in solved[:-1]):
                continue
            vector = tuple(
                solved[active.index(i)] if i in active else F() for i in range(r)
            )
            gradient_half = matrix_action(matrix, vector)
            lagrange = solved[-1]
            if any(gradient_half[i] > lagrange for i in range(r) if i not in active):
                continue
            require(
                all(gradient_half[i] == lagrange for i in active),
                "exact active KKT equations",
            )
            accepted.append(
                {
                    "active": active,
                    "vector": vector,
                    "lambda": lagrange,
                    "inactive_slacks": tuple(
                        lagrange - gradient_half[i] for i in range(r)
                    ),
                }
            )
    require(
        checked == 2**r - 1 and len(accepted) == 1,
        "complete active-set census with unique optimizer",
    )
    return accepted[0], checked


def four_prediction(shape):
    validate_shape(shape)
    require(len(shape) == 4, "four-source analytical atlas")
    a, _, c = (b - a for a, b in pairwise(shape))
    if c >= a:
        v = F(c - a, 3 * (2 * c - a))
        u = v / 2
    else:
        u = F(a - c, 3 * (2 * a - c))
        v = u / 2
    return u, F(1, 2) - u, F(1, 2) - v, v


def discover(shape):
    matrix, bands, pair_count = matrices(shape)
    optimum, checked = active_sets(matrix)
    vector = optimum["vector"]
    r = len(shape)
    if r == 2:
        require(vector == (F(1, 2), F(1, 2)), "two-source control")
    elif r == 3:
        require(
            vector == (F(1, 4), F(1, 2), F(1, 4)),
            "three-source shape-independent control",
        )
    elif r == 4:
        require(
            vector == four_prediction(shape),
            "predeclared four-source piecewise KKT atlas",
        )
    uniform = (F(1, r),) * r
    value = objective(matrix, vector)
    baseline = objective(matrix, uniform)
    require(value >= baseline, "unique source-simplex improvement")
    return {
        "shape": shape,
        "arity": r,
        "all_source_subset_count": 2**r,
        "complete_same_cardinality_ordered_pair_count_excluding_empty": pair_count,
        "exact_leading_matrix": matrix,
        "bands": bands,
        "all_active_supports_checked": checked,
        "unique_active_support": optimum["active"],
        "unique_activation": [str(q) for q in vector],
        "inactive_KKT_slacks": [str(x) for x in optimum["inactive_slacks"]],
        "exact_objective": str(value),
        "uniform_objective": str(baseline),
        "objective_gain": str(value - baseline),
        "constant_kernel_band_mass": comb(2 * r - 2, r - 1),
        "physical_leading_improvement_prefactor": f"8*A*epsilon/(4^{r}*K)",
        "shape_wall_claimed_as_literal_prime_product_equality": False,
        "full_finite_kernel_optimized": False,
    }


def authenticate():
    for path, blob in SOURCES.items():
        raw = subprocess.run(
            ["git", "show", f"{OLD}:{path}"], cwd=ROOT, capture_output=True, check=True
        ).stdout
        require(
            0 < len(raw) < 65536
            and sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
            == blob,
            "original source/kernel authentication",
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    authenticate()
    result = {
        "schema": "riemann.native_six_hour.higher_cluster_discovery.v1",
        "sources": [
            {"commit": OLD, "path": path, "blob": blob}
            for path, blob in SOURCES.items()
        ],
        "models": [discover(shape) for shape in PANELS],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
