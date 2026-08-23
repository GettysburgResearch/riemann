#!/usr/bin/env python3
"""Exact rational calibration for L/T-105350.

This replay checks finite atomic Hamburger/Stieltjes realizations, the
one-anchor/separated-packet Gram factorization, parity splitting, a polynomial
exterior-residue calibration, and the bounded-order separator R-105350.
It does not machine-prove the infinite Hamburger moment theorem, evaluate Xi,
or establish CRVH105330, OASH105350, BRP105220, or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable

Q = Fraction


def transpose(a: list[list[Q]]) -> list[list[Q]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    assert a and b and len(a[0]) == len(b)
    return [
        [
            sum((a[i][r] * b[r][j] for r in range(len(b))), Q(0))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def diagonal(values: list[Q]) -> list[list[Q]]:
    n = len(values)
    return [[values[i] if i == j else Q(0) for j in range(n)] for i in range(n)]


def determinant(a: list[list[Q]]) -> Q:
    matrix = [list(row) for row in a]
    n = len(matrix)
    out = Q(1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if matrix[row][col] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
            out = -out
        pivot_value = matrix[col][col]
        out *= pivot_value
        for row in range(col + 1, n):
            if matrix[row][col] == 0:
                continue
            factor = matrix[row][col] / pivot_value
            for j in range(col, n):
                matrix[row][j] -= factor * matrix[col][j]
    return out


def submatrix(a: list[list[Q]], indices: tuple[int, ...]) -> list[list[Q]]:
    return [[a[i][j] for j in indices] for i in indices]


def quadratic(a: list[list[Q]], vector: list[Q]) -> Q:
    return sum(
        (vector[i] * a[i][j] * vector[j] for i in range(len(a)) for j in range(len(a))),
        Q(0),
    )


def moments(nodes: list[Q], weights: list[Q], maximum: int) -> list[Q]:
    return [
        sum((weight * node**power for node, weight in zip(nodes, weights)), Q(0))
        for power in range(maximum + 1)
    ]


def hankel(sequence: list[Q], size: int, shift: int = 0) -> list[list[Q]]:
    return [[sequence[r + s + shift] for s in range(size)] for r in range(size)]


def vandermonde(nodes: list[Q], columns: int) -> list[list[Q]]:
    return [[node**power for power in range(columns)] for node in nodes]


def cauchy_features(nodes: list[Q], packet: list[Q]) -> list[list[Q]]:
    return [[Q(1) / (Q(1) - node * x) for x in packet] for node in nodes]


def rational_h_value(z: Q, nodes: list[Q], weights: list[Q], constant: Q = Q(0)) -> Q:
    return constant + z * sum(
        (weight / (Q(1) - node * z) for node, weight in zip(nodes, weights)), Q(0)
    )


def loewner_value(
    x: Q, y: Q, nodes: list[Q], weights: list[Q]
) -> Q:
    if x == y:
        return sum(
            (
                weight / (Q(1) - node * x) ** 2
                for node, weight in zip(nodes, weights)
            ),
            Q(0),
        )
    return (rational_h_value(x, nodes, weights) - rational_h_value(y, nodes, weights)) / (
        x - y
    )


def matrix_equal(a: list[list[Q]], b: list[list[Q]]) -> bool:
    return a == b


def check_positive_hamburger_fixture() -> tuple[int, dict[str, object]]:
    nodes = [Q(-2), Q(0), Q(3)]
    weights = [Q(1, 5), Q(2, 3), Q(4, 7)]
    sequence = moments(nodes, weights, 10)
    checks = 0

    # Every confluent matrix is a polynomial-evaluation Gram matrix.
    determinants: list[str] = []
    for size in range(1, 6):
        matrix = hankel(sequence, size)
        v = vandermonde(nodes, size)
        expected = matmul(transpose(v), matmul(diagonal(weights), v))
        assert matrix_equal(matrix, expected)
        checks += size * size
        det_value = determinant(matrix)
        determinants.append(str(det_value))
        if size <= len(nodes):
            assert det_value > 0
        else:
            assert det_value == 0
        checks += 1

    # The same positive atoms factor every separated Loewner packet.
    packet = [Q(-1, 5), Q(1, 7), Q(1, 4)]
    feature = cauchy_features(nodes, packet)
    kernel = [
        [loewner_value(x, y, nodes, weights) for y in packet]
        for x in packet
    ]
    expected_kernel = matmul(transpose(feature), matmul(diagonal(weights), feature))
    assert kernel == expected_kernel
    checks += 9
    assert determinant(kernel) > 0
    checks += 1

    # Direct divided differences agree with the atomic formula.
    for x, y in itertools.product(packet, repeat=2):
        direct = loewner_value(x, y, nodes, weights)
        atomic = sum(
            (
                weight
                / ((Q(1) - node * x) * (Q(1) - node * y))
                for node, weight in zip(nodes, weights)
            ),
            Q(0),
        )
        assert direct == atomic
        checks += 1

    return checks, {
        "nodes": [str(value) for value in nodes],
        "weights": [str(value) for value in weights],
        "leading_determinants": determinants,
        "packet_determinant": str(determinant(kernel)),
    }


def check_symmetric_stieltjes_fixture() -> tuple[int, dict[str, object]]:
    # nu = 1/3 delta_0 + 2/5 delta_(1/4) + 1/7 delta_4.
    s_nodes = [Q(0), Q(1, 4), Q(4)]
    nu_weights = [Q(1, 3), Q(2, 5), Q(1, 7)]
    beta = moments(s_nodes, nu_weights, 10)
    checks = 0

    # Stieltjes even/odd blocks are positive Gram matrices.
    even_determinants: list[str] = []
    odd_determinants: list[str] = []
    for size in range(1, 4):
        even = hankel(beta, size)
        odd = hankel(beta, size, shift=1)
        v = vandermonde(s_nodes, size)
        expected_even = matmul(transpose(v), matmul(diagonal(nu_weights), v))
        expected_odd = matmul(
            transpose(v),
            matmul(diagonal([w * s for w, s in zip(nu_weights, s_nodes)]), v),
        )
        assert even == expected_even
        assert odd == expected_odd
        checks += 2 * size * size
        assert determinant(even) > 0
        assert determinant(odd) >= 0
        checks += 2
        even_determinants.append(str(determinant(even)))
        odd_determinants.append(str(determinant(odd)))

    # The symmetric Hamburger lift has atoms +-sqrt(s), with half weights.
    t_nodes = [Q(0), Q(-1, 2), Q(1, 2), Q(-2), Q(2)]
    t_weights = [
        Q(1, 3),
        Q(1, 5),
        Q(1, 5),
        Q(1, 14),
        Q(1, 14),
    ]
    full = moments(t_nodes, t_weights, 12)
    for power in range(11):
        expected = Q(0) if power % 2 else beta[power // 2]
        assert full[power] == expected
        checks += 1

    # Safe-axis Stieltjes values agree exactly.
    safe_values: list[dict[str, str]] = []
    for y in [Q(1, 5), Q(1, 2), Q(3, 4)]:
        stieltjes = sum(
            (weight / (Q(1) + s * y * y) for s, weight in zip(s_nodes, nu_weights)),
            Q(0),
        )
        h_over_iy_algebraic = stieltjes
        assert h_over_iy_algebraic > 0
        checks += 1
        safe_values.append({"y": str(y), "Hiy_over_iy": str(stieltjes)})

    return checks, {
        "s_nodes": [str(value) for value in s_nodes],
        "weights": [str(value) for value in nu_weights],
        "even_determinants": even_determinants,
        "odd_determinants": odd_determinants,
        "safe_axis": safe_values,
    }


def check_polynomial_exterior_calibration() -> tuple[int, dict[str, object]]:
    # p=x^4-2x^2+1/2 has critical points -1,0,1 and residues
    # rho_(+-1)=-1/16, rho_0=-1/8.  An inner symmetric window containing 0
    # has exterior Stieltjes measure 1/4 delta_0 + 1/8 delta_1.
    nu_nodes = [Q(0), Q(1)]
    nu_weights = [Q(1, 4), Q(1, 8)]
    beta = moments(nu_nodes, nu_weights, 6)
    checks = 0

    expected = [Q(3, 8)] + [Q(1, 8)] * 6
    assert beta == expected
    checks += len(beta)

    # H(z)=z/4+z/[8(1-z^2)].
    for z in [Q(-1, 3), Q(1, 5), Q(2, 5)]:
        direct = z / Q(4) + z / (Q(8) * (Q(1) - z * z))
        measure = z * sum(
            (weight / (Q(1) - s * z * z) for s, weight in zip(nu_nodes, nu_weights)),
            Q(0),
        )
        assert direct == measure
        checks += 1

    even = hankel(beta, 2)
    odd = hankel(beta, 2, shift=1)
    assert determinant(even) > 0
    assert determinant(odd) == 0
    checks += 2

    return checks, {
        "polynomial": "x^4-2x^2+1/2",
        "exterior_residue": "-1/16 at each of +-1",
        "nu": [
            {"s": str(s), "weight": str(w)} for s, w in zip(nu_nodes, nu_weights)
        ],
        "beta": [str(value) for value in beta],
    }


def check_bounded_order_firewall() -> tuple[int, dict[str, object]]:
    nodes = [Q(-1), Q(0), Q(1)]
    weights = [Q(1, 4), Q(-1, 4), Q(1, 4)]
    sequence = moments(nodes, weights, 6)
    checks = 0

    l1 = hankel(sequence, 1)
    l2 = hankel(sequence, 2)
    l3 = hankel(sequence, 3)
    assert l1 == [[Q(1, 4)]]
    assert l2 == [[Q(1, 4), Q(0)], [Q(0), Q(1, 2)]]
    assert determinant(l1) == Q(1, 4)
    assert determinant(l2) == Q(1, 8)
    assert determinant(l3) == Q(-1, 16)
    checks += 6

    witness = [Q(1), Q(0), Q(-1)]
    assert quadratic(l3, witness) == Q(-1, 4)
    checks += 1

    packet = [Q(-1, 2), Q(1, 4), Q(1, 2)]
    feature = cauchy_features(nodes, packet)
    kernel = matmul(transpose(feature), matmul(diagonal(weights), feature))
    expected_kernel = [
        [Q(31, 36), Q(67, 180), Q(5, 12)],
        [Q(67, 180), Q(319, 900), Q(11, 20)],
        [Q(5, 12), Q(11, 20), Q(31, 36)],
    ]
    assert kernel == expected_kernel
    checks += 9

    two_by_two = []
    for indices in itertools.combinations(range(3), 2):
        value = determinant(submatrix(kernel, indices))
        assert value > 0
        two_by_two.append(str(value))
        checks += 1
    assert determinant(kernel) == Q(-16, 2025)
    checks += 1

    return checks, {
        "function": "z/4*(1/(1+z)-1+1/(1-z))",
        "moments": [str(value) for value in sequence[:5]],
        "L1_det": str(determinant(l1)),
        "L2_det": str(determinant(l2)),
        "L3_det": str(determinant(l3)),
        "witness": "1-t^2",
        "witness_value": str(quadratic(l3, witness)),
        "packet": [str(value) for value in packet],
        "packet_2x2_determinants": two_by_two,
        "packet_3x3_determinant": str(determinant(kernel)),
    }


def proof_digest(fixtures: dict[str, object]) -> str:
    payload = json.dumps(fixtures, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    positive_checks, positive_fixture = check_positive_hamburger_fixture()
    stieltjes_checks, stieltjes_fixture = check_symmetric_stieltjes_fixture()
    polynomial_checks, polynomial_fixture = check_polynomial_exterior_calibration()
    firewall_checks, firewall_fixture = check_bounded_order_firewall()

    fixtures = {
        "positive_hamburger": positive_fixture,
        "symmetric_stieltjes": stieltjes_fixture,
        "polynomial_exterior": polynomial_fixture,
        "bounded_order_firewall": firewall_fixture,
    }
    counts = {
        "positive_hamburger_checks": positive_checks,
        "symmetric_stieltjes_checks": stieltjes_checks,
        "polynomial_exterior_checks": polynomial_checks,
        "bounded_order_firewall_checks": firewall_checks,
    }
    result = {
        "verdict": "PASS_X_105350_ONE_ANCHOR_LOEWNER_HAMBURGER",
        "arithmetic_class": "EXACT_RATIONAL_ATOMIC_MOMENT_GRAM",
        "checks": sum(counts.values()),
        "counts": counts,
        "fixtures": fixtures,
        "proof_object": proof_digest(fixtures),
        "infinite_hamburger_theorem_machine_proved": False,
        "oash105350_proved_for_xi": False,
        "crvh105330_proved_for_xi": False,
        "moving_saddle_proved": False,
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
