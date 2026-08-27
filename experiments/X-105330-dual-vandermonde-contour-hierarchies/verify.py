#!/usr/bin/env python3
"""Exact replay for the dual Vandermonde contour hierarchies.

The checker authenticates finite rational polynomial and atomic determinant
identities only.  It does not evaluate Xi, establish the cofinal contour
inequalities, prove PRES105220/BRP105220, or prove RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path

Q = Fraction


def trim(p: list[Q]) -> list[Q]:
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def poly_add(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return trim(out)


def poly_mul(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return trim(out)


def poly_scale(a: list[Q], scalar: Q) -> list[Q]:
    return trim([scalar * value for value in a])


def derivative(p: list[Q]) -> list[Q]:
    return trim([Q(i) * p[i] for i in range(1, len(p))] or [Q(0)])


def evaluate(p: list[Q], x: Q) -> Q:
    out = Q(0)
    for coefficient in reversed(p):
        out = out * x + coefficient
    return out


def polynomial_from_roots(roots: list[Q]) -> list[Q]:
    out = [Q(1)]
    for root in roots:
        out = poly_mul(out, [-root, Q(1)])
    return out


def transpose(matrix: list[list[Q]]) -> list[list[Q]]:
    return [list(row) for row in zip(*matrix)]


def matmul(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    assert len(a[0]) == len(b)
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def diagonal(values: list[Q]) -> list[list[Q]]:
    n = len(values)
    return [
        [values[i] if i == j else Q(0) for j in range(n)]
        for i in range(n)
    ]


def determinant(matrix: list[list[Q]]) -> Q:
    a = [list(row) for row in matrix]
    n = len(a)
    out = Q(1)
    for column in range(n):
        pivot = next(
            (row for row in range(column, n) if a[row][column] != 0),
            None,
        )
        if pivot is None:
            return Q(0)
        if pivot != column:
            a[column], a[pivot] = a[pivot], a[column]
            out = -out
        pivot_value = a[column][column]
        out *= pivot_value
        for row in range(column + 1, n):
            if a[row][column] == 0:
                continue
            factor = a[row][column] / pivot_value
            for j in range(column, n):
                a[row][j] -= factor * a[column][j]
    return out


def resultant(a: list[Q], b: list[Q]) -> Q:
    """Sylvester determinant with Res(a,b)=lc(a)^deg(b) prod b(alpha)."""
    a = trim(a)
    b = trim(b)
    m = len(a) - 1
    n = len(b) - 1
    if m == 0:
        return a[0] ** n
    if n == 0:
        return b[0] ** m
    a_desc = list(reversed(a))
    b_desc = list(reversed(b))
    size = m + n
    matrix: list[list[Q]] = []
    for shift in range(n):
        row = [Q(0)] * size
        row[shift : shift + m + 1] = a_desc
        matrix.append(row)
    for shift in range(m):
        row = [Q(0)] * size
        row[shift : shift + n + 1] = b_desc
        matrix.append(row)
    return determinant(matrix)


def quadratic(matrix: list[list[Q]], vector: list[Q]) -> Q:
    return sum(
        (
            vector[i] * matrix[i][j] * vector[j]
            for i in range(len(vector))
            for j in range(len(vector))
        ),
        Q(0),
    )


def vandermonde(nodes: list[Q], columns: int | None = None) -> list[list[Q]]:
    width = len(nodes) if columns is None else columns
    return [[node**power for power in range(width)] for node in nodes]


def vandermonde_square(nodes: list[Q]) -> Q:
    out = Q(1)
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            out *= (nodes[j] - nodes[i]) ** 2
    return out


def moments(nodes: list[Q], weights: list[Q], max_degree: int) -> list[Q]:
    return [
        sum(
            (weight * node**degree for node, weight in zip(nodes, weights)),
            Q(0),
        )
        for degree in range(max_degree + 1)
    ]


def hankel(moment_sequence: list[Q], size: int) -> list[list[Q]]:
    return [
        [moment_sequence[row + column] for column in range(size)]
        for row in range(size)
    ]


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        1
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
        if permutation[i] > permutation[j]
    )
    return -1 if inversions % 2 else 1


def pencil_determinant_polynomial(
    constant_matrix: list[list[Q]],
    linear_matrix: list[list[Q]],
) -> list[Q]:
    n = len(constant_matrix)
    out = [Q(0)]
    for permutation in permutations(range(n)):
        term = [Q(permutation_sign(permutation))]
        for row, column in enumerate(permutation):
            term = poly_mul(
                term,
                [
                    constant_matrix[row][column],
                    linear_matrix[row][column],
                ],
            )
        out = poly_add(out, term)
    return trim(out)


def product_t_minus(values: list[Q]) -> list[Q]:
    out = [Q(1)]
    for value in values:
        out = poly_mul(out, [-value, Q(1)])
    return out


def lagrange_cardinal(nodes: list[Q], target: int) -> list[Q]:
    roots = [node for index, node in enumerate(nodes) if index != target]
    numerator = polynomial_from_roots(roots)
    denominator = evaluate(numerator, nodes[target])
    assert denominator != 0
    return poly_scale(numerator, Q(1) / denominator)


def matrix_equal(a: list[list[Q]], b: list[list[Q]]) -> bool:
    return a == b


def fraction_text(value: Q) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def check_polynomial_hierarchies() -> tuple[dict[str, int], list[dict[str, object]]]:
    fixtures = [
        {
            "name": "five-real-root-coherence-firewall",
            "polynomial": [Q(8), Q(0), Q(-50), Q(-35), Q(0), Q(1)],
            "critical_points": [Q(-4), Q(-1), Q(0), Q(5)],
        },
        {
            "name": "quartic-wedge-two-separator",
            "polynomial": [Q(-1), Q(0), Q(-2), Q(0), Q(1)],
            "critical_points": [Q(-1), Q(0), Q(1)],
        },
        {
            "name": "good-cubic",
            "polynomial": [Q(3, 2), Q(-3), Q(0), Q(1)],
            "critical_points": [Q(-1), Q(1)],
        },
        {
            "name": "bad-cubic",
            "polynomial": [Q(4), Q(-3), Q(0), Q(1)],
            "critical_points": [Q(-1), Q(1)],
        },
    ]

    factorization_checks = 0
    pencil_checks = 0
    resultant_checks = 0
    partition_checks = 0
    cardinal_checks = 0
    summaries: list[dict[str, object]] = []

    for fixture in fixtures:
        polynomial = fixture["polynomial"]
        critical_points = fixture["critical_points"]
        dp = derivative(polynomial)
        ddp = derivative(dp)
        degree = len(polynomial) - 1
        assert len(critical_points) == degree - 1
        assert all(evaluate(dp, point) == 0 for point in critical_points)
        assert all(evaluate(ddp, point) != 0 for point in critical_points)

        residues = [
            evaluate(polynomial, point) / evaluate(ddp, point)
            for point in critical_points
        ]
        weights = [-residue for residue in residues]
        size = len(critical_points)

        count_moments = moments(
            critical_points,
            [Q(1)] * size,
            2 * size - 2,
        )
        residue_moments = moments(
            critical_points,
            weights,
            2 * size - 2,
        )
        h_matrix = hankel(count_moments, size)
        b_matrix = hankel(residue_moments, size)

        v_matrix = vandermonde(critical_points)
        expected_h = matmul(transpose(v_matrix), v_matrix)
        expected_b = matmul(
            matmul(transpose(v_matrix), diagonal(weights)),
            v_matrix,
        )
        assert matrix_equal(h_matrix, expected_h)
        assert matrix_equal(b_matrix, expected_b)
        factorization_checks += 2 * size * size

        det_h = determinant(h_matrix)
        assert det_h == vandermonde_square(critical_points)
        assert det_h != 0
        pencil = pencil_determinant_polynomial(b_matrix, h_matrix)
        expected_pencil = poly_scale(product_t_minus(residues), det_h)
        assert pencil == expected_pencil
        pencil_checks += len(pencil) + 1

        # Independent coefficient-side resultant evaluation at M+1 points.
        res_denominator = resultant(dp, ddp)
        assert res_denominator != 0
        for t_value in [Q(value) for value in range(size + 1)]:
            tp_minus_p = poly_add(poly_scale(ddp, t_value), poly_scale(polynomial, Q(-1)))
            normalized = resultant(dp, tp_minus_p) / (Q(degree * degree) * res_denominator)
            expected = evaluate(product_t_minus(residues), t_value)
            assert normalized == expected
            resultant_checks += 1

        leading_minors: list[Q] = []
        for k in range(1, size + 1):
            leading = [row[:k] for row in b_matrix[:k]]
            leading_value = determinant(leading)
            subset_value = Q(0)
            for subset in combinations(range(size), k):
                subset_nodes = [critical_points[index] for index in subset]
                subset_weight = Q(1)
                for index in subset:
                    subset_weight *= weights[index]
                subset_value += subset_weight * vandermonde_square(subset_nodes)
            assert leading_value == subset_value
            leading_minors.append(leading_value)
            partition_checks += 1 + len(list(combinations(range(size), k)))

        for target in range(size):
            cardinal = lagrange_cardinal(critical_points, target)
            padded = cardinal + [Q(0)] * (size - len(cardinal))
            assert [
                evaluate(cardinal, point) for point in critical_points
            ] == [
                Q(1) if index == target else Q(0)
                for index in range(size)
            ]
            assert quadratic(b_matrix, padded) == weights[target]
            cardinal_checks += size + 1

        summaries.append(
            {
                "name": fixture["name"],
                "residues": [fraction_text(value) for value in residues],
                "leading_minors": [
                    fraction_text(value) for value in leading_minors
                ],
                "pencil": [fraction_text(value / det_h) for value in pencil],
            }
        )

    return (
        {
            "vandermonde_factorization_checks": factorization_checks,
            "generalized_pencil_checks": pencil_checks,
            "resultant_evaluation_checks": resultant_checks,
            "andreief_partition_checks": partition_checks,
            "cardinal_sign_witness_checks": cardinal_checks,
        },
        summaries,
    )


def check_quartic_firewall() -> int:
    polynomial = [Q(-1), Q(0), Q(-2), Q(0), Q(1)]
    critical_points = [Q(-1), Q(0), Q(1)]
    dp = derivative(polynomial)
    ddp = derivative(dp)
    residues = [
        evaluate(polynomial, point) / evaluate(ddp, point)
        for point in critical_points
    ]
    assert residues == [Q(-1, 4), Q(1, 4), Q(-1, 4)]

    weights = [-value for value in residues]
    sequence = moments(critical_points, weights, 4)
    matrix = hankel(sequence, 3)
    assert determinant([[matrix[0][0]]]) == Q(1, 4)
    assert determinant([row[:2] for row in matrix[:2]]) == Q(1, 8)
    assert determinant(matrix) == Q(-1, 16)

    witness = [Q(1), Q(0), Q(-1)]  # 1-x^2 isolates c=0
    assert quadratic(matrix, witness) == Q(-1, 4)
    return 5


def cauchy_feature_matrix(
    x_nodes: list[Q],
    z_nodes: list[Q],
    scales: list[Q],
) -> list[list[Q]]:
    return [
        [scales[i] / (z_nodes[j] - x_nodes[i]) for j in range(len(z_nodes))]
        for i in range(len(x_nodes))
    ]


def check_cauchy_vandermonde_hierarchy() -> int:
    support_nodes = [Q(2), Q(3), Q(5), Q(7)]
    support_weights_sets = [
        [Q(1), Q(2), Q(3), Q(4)],
        [Q(1), Q(-1, 3), Q(5, 2), Q(7, 4)],
    ]
    packet_nodes = [Q(-2), Q(0), Q(1)]
    scales = [Q(2), Q(-1), Q(3)]
    checks = 0

    for support_weights in support_weights_sets:
        for size in range(1, len(packet_nodes) + 1):
            x_nodes = packet_nodes[:size]
            local_scales = scales[:size]
            features = cauchy_feature_matrix(
                x_nodes,
                support_nodes,
                local_scales,
            )
            weighted = matmul(
                matmul(features, diagonal(support_weights)),
                transpose(features),
            )
            direct_det = determinant(weighted)

            subset_sum = Q(0)
            for subset in combinations(range(len(support_nodes)), size):
                z_subset = [support_nodes[index] for index in subset]
                feature_subset = [
                    [features[i][index] for index in subset]
                    for i in range(size)
                ]
                feature_det = determinant(feature_subset)
                weight = Q(1)
                for index in subset:
                    weight *= support_weights[index]
                subset_sum += weight * feature_det**2

                numerator = (
                    vandermonde_square(x_nodes)
                    * vandermonde_square(z_subset)
                )
                for scalar in local_scales:
                    numerator *= scalar**2
                denominator = Q(1)
                for x_value in x_nodes:
                    for z_value in z_subset:
                        denominator *= (z_value - x_value) ** 2
                assert feature_det**2 == numerator / denominator
                checks += 1

            assert direct_det == subset_sum
            checks += 1

    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    counts, fixtures = check_polynomial_hierarchies()
    counts["quartic_wedge_two_firewall_checks"] = check_quartic_firewall()
    counts["cauchy_vandermonde_checks"] = check_cauchy_vandermonde_hierarchy()

    proof_payload = {
        "counts": counts,
        "fixtures": fixtures,
    }
    proof_object = hashlib.sha256(
        json.dumps(proof_payload, sort_keys=True).encode("utf-8")
    ).hexdigest()

    result = {
        "verdict": "PASS_X_105330_DUAL_VANDERMONDE_CONTOUR_HIERARCHIES",
        "arithmetic_class": "EXACT_RATIONAL",
        "counts": counts,
        "fixtures": fixtures,
        "proof_object": proof_object,
        "critical_hierarchy_proved_for_xi": False,
        "boundary_hierarchy_proved_for_xi": False,
        "pres105220_proved": False,
        "brp105220_proved": False,
        "rh_established": False,
    }

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
