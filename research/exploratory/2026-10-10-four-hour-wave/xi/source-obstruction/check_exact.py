#!/usr/bin/env python3
"""Exact finite-spectrum controls for SO-A/SO-B; no floating arithmetic."""

from fractions import Fraction as Q
from functools import reduce
from itertools import combinations
from math import gcd, lcm
import json
import hashlib
from pathlib import Path


if not __debug__:
    raise SystemExit("FAIL: Python optimization disables assertions; rerun without -O or -OO")


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q(0))


def transpose(a):
    return [list(col) for col in zip(*a)]


def rref(a):
    a = [list(row) for row in a]
    pivots = []
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = a[row][col]
        a[row] = [v / scale for v in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                scale = a[i][col]
                a[i] = [u - scale * v for u, v in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots


def null_vector(a):
    reduced, pivots = rref(a)
    free = next(j for j in range(len(a[0])) if j not in pivots)
    w = [Q(0)] * len(a[0])
    w[free] = Q(1)
    for row, pivot in enumerate(pivots):
        w[pivot] = -reduced[row][free]
    assert all(dot(row, w) == 0 for row in a)
    scale = lcm(*(v.denominator for v in w))
    integers = [v.numerator * (scale // v.denominator) for v in w]
    common = reduce(gcd, (abs(v) for v in integers))
    integers = [v // common for v in integers]
    if next(v for v in integers if v) < 0:
        integers = [-v for v in integers]
    return [Q(v) for v in integers]


def determinant(a):
    a = [list(row) for row in a]
    result = Q(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        value = a[j][j]
        result *= value
        for i in range(j + 1, len(a)):
            scale = a[i][j] / value
            for k in range(j + 1, len(a)):
                a[i][k] -= scale * a[j][k]
    return result


def inertia(a):
    """Rational symmetric elimination, including exact 2x2 pivots."""
    a = [list(row) for row in a]
    counts = [0, 0, 0]
    while a:
        n = len(a)
        diagonal = next((i for i in range(n) if a[i][i]), None)
        if diagonal is not None:
            order = [diagonal] + [i for i in range(n) if i != diagonal]
            a = [[a[i][j] for j in order] for i in order]
            pivot = a[0][0]
            counts[0 if pivot > 0 else 1] += 1
            a = [[a[i][j] - a[i][0] * a[0][j] / pivot
                  for j in range(1, n)] for i in range(1, n)]
            continue
        pair = next(((i, j) for i in range(n) for j in range(i + 1, n)
                     if a[i][j]), None)
        if pair is None:
            counts[2] += n
            break
        order = list(pair) + [i for i in range(n) if i not in pair]
        a = [[a[i][j] for j in order] for i in order]
        pivot = a[0][1]
        counts[0] += 1
        counts[1] += 1
        a = [[a[i][j] - (a[i][0] * a[1][j] + a[i][1] * a[0][j]) / pivot
              for j in range(2, n)] for i in range(2, n)]
    return counts


def value(x, critical, quartets):
    result = sum((2 * mult * x / (x * x + r)
                  for r, mult in critical), Q(0))
    for c, b, mult in quartets:
        u = x * x + c
        result += 4 * mult * x * u / (u * u + b * b)
    return result


def kernel(nodes, critical, quartets):
    f = [value(x, critical, quartets) for x in nodes]
    return [[(f[i] + f[j]) / (x + y) for j, y in enumerate(nodes)]
            for i, x in enumerate(nodes)]


def features(x, critical, quartets):
    positive, negative = [], []
    positive_weights, negative_weights = [], []
    for r, mult in critical:
        positive.extend([x / (x * x + r), 1 / (x * x + r)])
        positive_weights.extend([2 * mult, 2 * mult * r])
    for c, b, mult in quartets:
        u = x * x + c
        d = u * u + b * b
        positive.extend([x * u / d, (c * u + b * b) / d])
        positive_weights.extend([4 * mult, 4 * mult / c])
        negative.extend([x / d, 1 / d])
        negative_weights.extend([4 * mult * b * b,
                                 4 * mult * b * b * (c * c + b * b) / c])
    return positive, negative, positive_weights, negative_weights


def rational(q):
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def check_fixture(label, nodes, critical, quartets, check_low_order=False):
    nodes = list(map(Q, nodes))
    critical = [(Q(r), Q(m)) for r, m in critical]
    quartets = [(Q(c), Q(b), Q(m)) for c, b, m in quartets]
    assert len(nodes) == len(set(nodes)) and all(x > 0 for x in nodes)
    assert all(r > 0 and m > 0 for r, m in critical)
    assert all(c > 0 and b > 0 and m > 0 for c, b, m in quartets)
    assert len(set(r for r, _ in critical)) == len(critical)
    assert len(set((c, b) for c, b, _ in quartets)) == len(quartets)
    k = kernel(nodes, critical, quartets)
    records = [features(x, critical, quartets) for x in nodes]
    positive = [r[0] for r in records]
    negative = [r[1] for r in records]
    pw, nw = records[0][2:]
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            gram = sum((p * a * b for p, a, b in zip(pw, positive[i], positive[j])), Q(0))
            gram -= sum((p * a * b for p, a, b in zip(nw, negative[i], negative[j])), Q(0))
            assert gram == k[i][j], (label, "Gram identity", i, j)
    full_features = [p + n for p, n in zip(positive, negative)]
    _, pivots = rref(full_features)
    d = 2 * len(critical) + 4 * len(quartets)
    p = 2 * len(critical) + 2 * len(quartets)
    assert len(pivots) == min(len(nodes), d), (label, "feature rank")
    signature = inertia(k)
    assert signature[1] >= max(0, min(len(nodes), d) - p)
    if len(nodes) >= d:
        assert signature == [p, 2 * len(quartets), len(nodes) - d]
    low_counts = {}
    if check_low_order:
        for size in range(1, 4):
            minors = [determinant([[k[i][j] for j in inds] for i in inds])
                      for inds in combinations(range(len(nodes)), size)]
            assert all(q >= 0 for q in minors), (label, "low-order PSD", size)
            low_counts[str(size)] = {"positive": sum(q > 0 for q in minors),
                                     "zero": sum(q == 0 for q in minors)}
    record = {
        "label": label,
        "nodes": [str(x) for x in nodes],
        "critical_r_m": [[str(r), str(m)] for r, m in critical],
        "quartet_c_B_m": [[str(c), str(b), str(m)] for c, b, m in quartets],
        "feature_rank": len(pivots),
        "inertia_positive_negative_zero": signature,
        "low_order_principal_minors": low_counts,
    }
    if len(nodes) > p:
        w = null_vector(transpose(positive))
        ps = [dot(col, w) for col in transpose(positive)]
        ns = [dot(col, w) for col in transpose(negative)]
        assert not any(ps)
        assert any(ns)
        contraction = dot(w, [dot(row, w) for row in k])
        negative_squares = -sum((weight * v * v for weight, v in zip(nw, ns)), Q(0))
        assert contraction == negative_squares < 0
        record.update({"integer_witness": [str(x.numerator) for x in w],
                       "positive_feature_sums": [str(x) for x in ps],
                       "negative_feature_sums": [str(x) for x in ns],
                       "exact_negative_contraction": rational(contraction)})
        moment2 = dot(w, [x * x for x in nodes])
        if moment2:
            record["moment2_normalized_negative_contraction"] = rational(
                contraction / (moment2 * moment2))
    return record


def coefficient_determinant(r, c, B):
    h = B * B
    # Columns are the six numerators P(x)*phi(x) in (SO-3).
    columns = [
        [0, c * c + h, 0, 2 * c, 0, 1],
        [c * c + h, 0, 2 * c, 0, 1, 0],
        [0, c * r, 0, c + r, 0, 1],
        [0, r, 0, 1, 0, 0],
        [c * r, 0, c + r, 0, 1, 0],
        [r, 0, 1, 0, 0, 0],
    ]
    result = determinant(transpose([[Q(v) for v in col] for col in columns]))
    assert result == ((c - r) ** 2 + h) ** 2
    return result


def asymptotic_control(b):
    nodes = list(map(Q, range(1, 6)))
    r, a, m = Q(1), Q(1, 4), Q(1)
    c, B = b * b - a * a, 2 * a * b
    records = [features(x, [(r, Q(1))], [(c, B, m)]) for x in nodes]
    positive = [row[0] for row in records]
    w = null_vector(transpose(positive))
    moment = dot(w, [x * x for x in nodes])
    assert moment != 0
    w = [v / moment for v in w]
    assert dot(w, [x * x for x in nodes]) == 1
    assert all(dot(row, w) == 0 for row in transpose(positive))
    k = kernel(nodes, [(r, Q(1))], [(c, B, m)])
    contraction = dot(w, [dot(row, w) for row in k])
    assert contraction < 0
    w0 = []
    for i, x in enumerate(nodes):
        product = Q(1)
        for j, y in enumerate(nodes):
            if j != i:
                product *= x - y
        w0.append((x * x + r) / product)
    for power in range(2):
        assert dot(w0, [x ** power for x in nodes]) == 0
    assert dot(w0, [x * x for x in nodes]) == 1
    s, a2 = 1 / (b * b), a * a
    for x, record in zip(nodes, records):
        t = x * x
        ds = 1 + 2 * (t + a2) * s + (t - a2) ** 2 * s * s
        assert record[0][2] / s == x * (1 + (t - a2) * s) / ds
        assert record[0][3] == (1 + (t + 2 * a2) * s - a2 * (t - a2) * s * s) / ds
        assert record[1] == [x * s * s / ds, s * s / ds]
    return {"b": str(b), "exact_normalized_contraction": rational(contraction),
            "b8_times_contraction": rational(b ** 8 * contraction),
            "predicted_leading_coefficient": str(-16 * m * a * a),
            "exact_error_in_leading_coefficient": rational(
                b ** 8 * contraction + 16 * m * a * a),
            "max_error_from_barycentric_limit": rational(
                max(abs(u - v) for u, v in zip(w, w0)))}


def main():
    b, a = Q(1025), Q(1, 4)
    c, B = b * b - a * a, 2 * a * b
    assert 1 / (b * b) < Q(1, 9 * 1024)
    coefficient_det = coefficient_determinant(Q(1), c, B)
    reserve_share = 2 * B ** 2 / ((c - 1) ** 2 - B ** 2)
    assert 0 < reserve_share < 1
    fixtures = [
        ("X9_high_quartet_five_safe_nodes", range(1, 6), [(1, 1)], [(c, B, 1)], True),
        ("X9_high_quartet_five_mixed_nodes", [Q(1, 4), Q(1, 2), 1, 2, 4],
         [(1, 1)], [(c, B, 1)], True),
        ("X9_high_quartet_six_safe_nodes", range(1, 7), [(1, 1)], [(c, B, 1)], True),
        ("critical_multiplicity_1000", range(1, 6), [(1, 1000)], [(c, B, 1)], True),
        ("two_critical_pairs_one_quartet_seven_nodes", range(1, 8),
         [(1, 1), (9, 2)], [(c, B, 1)], False),
        ("two_critical_pairs_one_quartet_eight_nodes", range(1, 9),
         [(1, 1), (9, 2)], [(c, B, 1)], False),
        ("one_critical_pair_two_quartets_ten_nodes", range(1, 11),
         [(1, 3)], [(Q(63, 16), 1, 2), (Q(143, 16), Q(3, 2), 1)], False),
        ("one_critical_pair_two_quartets_eleven_nodes", range(1, 12),
         [(1, 3)], [(Q(63, 16), 1, 2), (Q(143, 16), Q(3, 2), 1)], False),
    ]
    records = [check_fixture(*fixture) for fixture in fixtures]
    report = {
        "status": "PASS exact rational synthetic controls; proof review pending",
        "arithmetic": "Python standard-library fractions.Fraction; no floating arithmetic",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "fixture_count": len(records),
        "X9_reserve_share": rational(reserve_share),
        "feature_coefficient_determinant_SO4": rational(coefficient_det),
        "fixtures": records,
        "SO_C_fixed_packet_asymptotic_controls": [
            asymptotic_control(Q(height)) for height in [1025, 2050, 4100, 8200]],
    }
    path = Path(__file__).with_name("exact_checks.json")
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(f"PASS: {len(records)} exact finite-spectrum fixtures; {path.name}")
    for record in records:
        print(record["label"], record["inertia_positive_negative_zero"])


if __name__ == "__main__":
    main()
