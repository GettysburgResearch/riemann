"""Exact complete arithmetic-shape activation discovery; no finite-kernel claim."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import defaultdict
from fractions import Fraction as F
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FREEZE = "755b27c2c9747f3db255238c59c2622dee6cad8b"
SOURCE = "research/riemann-structures/native-six-hour/HIGHER_NATIVE_CLUSTER_ATLAS.md"
BLOB = "13ddf1515da1913008290a75465f77cc137e7728"
MAX_ARITY = 16
MAX_BITS = 1024


def need(condition, message):
    if not condition:
        raise ValueError(message)


def bounded(value):
    value = F(value)
    need(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= MAX_BITS,
        "exact arithmetic cap",
    )
    return value


def authenticate():
    raw = subprocess.check_output(["git", "show", f"{FREEZE}:{SOURCE}"], cwd=ROOT)
    need(len(raw) < 1048576, "source size")
    actual = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    need(actual == BLOB, "exact primitive theorem pin")


def histogram(indices):
    data = {(0, 0): 1}
    for i in indices:
        new = defaultdict(int, data)
        for (k, s), count in data.items():
            new[k + 1, s + i] += count
        data = dict(new)
    return data


def incidence(r):
    need(type(r) is int and 2 <= r <= MAX_ARITY, "arity cap")
    total = histogram(range(r))
    data = []
    for i in range(r):
        others = histogram(j for j in range(r) if j != i)
        data.append({(k + 1, s + i): count for (k, s), count in others.items()})
    for (k, s), count in total.items():
        need(
            sum(row.get((k, s), 0) for row in data) == k * count,
            "complete incidence conservation",
        )
    for k in range(1, r + 1):
        need(
            sum(c for (j, _), c in total.items() if j == k) == comb(r, k),
            "unmarked full band coverage",
        )
        for row in data:
            need(
                sum(c for (j, _), c in row.items() if j == k) == comb(r - 1, k - 1),
                "marked full band coverage",
            )
    return total, data


def distance_matrix(r):
    total, data = incidence(r)
    matrix = [[0] * r for _ in range(r)]
    for k in range(1, r + 1):
        positions = sorted(s for j, s in total if j == k)
        for j in range(r):
            mass = comb(r - 1, k - 1)
            moment = sum(s * data[j].get((k, s), 0) for s in positions)
            left_mass = left_moment = 0
            for s in positions:
                distance = moment - s * mass + 2 * (s * left_mass - left_moment)
                need(distance >= 0, "distance positivity")
                for i in range(r):
                    matrix[i][j] += data[i].get((k, s), 0) * distance
                count = data[j].get((k, s), 0)
                left_mass += count
                left_moment += s * count
    need(
        all(
            matrix[i][j] == matrix[j][i] == matrix[r - 1 - i][r - 1 - j]
            for i in range(r)
            for j in range(r)
        ),
        "full symmetry and reflection",
    )
    for row in matrix:
        for value in row:
            bounded(value)
    return matrix


def enumerated_cut_matrix(r):
    need(2 <= r <= 8, "enumeration control cap")
    groups = defaultdict(lambda: [0] * r)
    for mask in range(1 << r):
        subset = [i for i in range(r) if (mask >> i) & 1]
        for i in subset:
            groups[len(subset), sum(subset)][i] += 1
    matrix = [[0] * r for _ in range(r)]
    for k in range(1, r + 1):
        locations = sorted(s for band, s in groups if band == k)
        prefix = [0] * r
        mass = comb(r - 1, k - 1)
        for index, s in enumerate(locations[:-1]):
            prefix = [a + b for a, b in zip(prefix, groups[k, s], strict=True)]
            gap = locations[index + 1] - s
            for i in range(r):
                for j in range(r):
                    matrix[i][j] += gap * (
                        mass * (prefix[i] + prefix[j]) - 2 * prefix[i] * prefix[j]
                    )
    return matrix


def solve(matrix, rhs):
    n = len(rhs)
    need(n <= 9 and all(len(row) == n for row in matrix), "linear size cap")
    rows = [
        [bounded(x) for x in row] + [bounded(y)]
        for row, y in zip(matrix, rhs, strict=True)
    ]
    for j in range(n):
        pivot = next((i for i in range(j, n) if rows[i][j]), None)
        if pivot is None:
            return None
        rows[j], rows[pivot] = rows[pivot], rows[j]
        scale = rows[j][j]
        rows[j] = [bounded(x / scale) for x in rows[j]]
        for i in range(n):
            if i != j and rows[i][j]:
                scale = rows[i][j]
                rows[i] = [
                    bounded(x - scale * y)
                    for x, y in zip(rows[i], rows[j], strict=True)
                ]
    return [row[-1] for row in rows]


def optimize(matrix):
    r = len(matrix)
    groups = [tuple(sorted({i, r - 1 - i})) for i in range((r + 1) // 2)]
    m = len(groups)
    reduced = [
        [
            F(sum(matrix[i][j] for i in left for j in right), len(left) * len(right))
            for right in groups
        ]
        for left in groups
    ]
    winners = []
    for mask in range(1, 1 << m):
        support = [i for i in range(m) if mask >> i & 1]
        system = [[reduced[i][j] for j in support] + [-1] for i in support]
        system.append([1] * len(support) + [0])
        answer = solve(system, [0] * len(support) + [1])
        if answer is None or any(value <= 0 for value in answer[:-1]):
            continue
        y = [F()] * m
        for i, value in zip(support, answer[:-1], strict=True):
            y[i] = value
        lam = answer[-1]
        if any(sum(reduced[i][j] * y[j] for j in range(m)) > lam for i in range(m)):
            continue
        q = [F()] * r
        for group, value in zip(groups, y, strict=True):
            for i in group:
                q[i] = value / len(group)
        action = [sum(F(matrix[i][j]) * q[j] for j in range(r)) for i in range(r)]
        need(sum(q) == 1 and all(value >= 0 for value in q), "full source simplex")
        need(
            all(action[i] == lam if q[i] else action[i] <= lam for i in range(r)),
            "all original-coordinate KKT inequalities",
        )
        winners.append((q, lam, [lam - value for value in action]))
    need(len(winners) == 1, "unique exact positive-support KKT solution")
    q, value, slacks = winners[0]
    uniform = F(sum(sum(row) for row in matrix), r * r)
    even_prediction = {r // 2 - 1, r // 2}
    odd_prediction = {r // 2 - 1, r // 2, r // 2 + 1}
    actual_support = {i for i, mass in enumerate(q) if mass > 0}
    return {
        "arity": r,
        "matrix": matrix,
        "all_reflection_supports_tested": (1 << m) - 1,
        "unique_activation": [str(x) for x in q],
        "objective": str(value),
        "gain_over_uniform": str(value - uniform),
        "inactive_slacks_Bq": [str(x) for x in slacks],
        "positive_support_zero_based": sorted(actual_support),
        "central_two_or_three_hypothesis": actual_support
        == (even_prediction if r % 2 == 0 else odd_prediction),
        "full_coordinate_KKT": True,
        "complete_subset_count": 1 << r,
        "physical_leading_multiplier_before_A_epsilon_over_K": str(F(8, 4**r)),
    }


def build():
    authenticate()
    panels = []
    for r in range(2, MAX_ARITY + 1):
        matrix = distance_matrix(r)
        if r <= 8:
            need(
                matrix == enumerated_cut_matrix(r),
                "independent enumerated cut equality",
            )
        panel = optimize(matrix)
        panel["independent_subset_enumeration_checked"] = r <= 8
        panels.append(panel)
    controls = {
        2: ["1/2", "1/2"],
        3: ["1/4", "1/2", "1/4"],
        4: ["0", "1/2", "1/2", "0"],
        5: ["0", "5/16", "3/8", "5/16", "0"],
        6: ["0", "0", "1/2", "1/2", "0", "0"],
    }
    need(
        all(
            row["unique_activation"] == controls[row["arity"]]
            for row in panels
            if row["arity"] in controls
        ),
        "frozen low-arity controls",
    )
    return {
        "schema": "riemann.native_six_hour.arithmetic_arity_discovery.v1",
        "source_commit": FREEZE,
        "source_path": SOURCE,
        "source_blob": BLOB,
        "coverage": list(range(2, MAX_ARITY + 1)),
        "exact_bit_cap": MAX_BITS,
        "finite_original_kernel_claim": False,
        "all_arity_theorem_claim": False,
        "panels": panels,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    print(json.dumps(build(), indent=2, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
