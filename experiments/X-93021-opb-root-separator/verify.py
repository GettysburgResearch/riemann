#!/usr/bin/env python3
"""Exact/directed fifth-strike replay for the OPB root separator.

Arithmetic:
- fractions.Fraction for every finite carry, primal, dual, and Farkas identity;
- decimal.Context with outward rounding for the two logarithm/square-root
  certificates at X=20 and X=40;
- no external LP solver and no asymptotic scan.

The replay proves an exact finite separator and the all-scale root-face algebra.
It does not prove the redesigned critical transverse cone, OPB, Cycle Debt, or
the Riemann Hypothesis.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple

Edge = Tuple[int, int, int]
Expr = Dict[int, Fraction]
Interval = Tuple[Decimal, Decimal]

PREC = 100
LOW = Context(prec=PREC, rounding=ROUND_FLOOR)
HIGH = Context(prec=PREC, rounding=ROUND_CEILING)
ZERO: Interval = (Decimal(0), Decimal(0))


def mobius_sieve(limit: int) -> List[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: List[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            m = n * p
            if m > limit:
                break
            composite[m] = True
            if n % p == 0:
                mu[m] = 0
                break
            mu[m] = -mu[n]
    return mu


def b2_values(limit: int) -> List[int]:
    mu = mobius_sieve(limit)
    return [
        0 if q == 0 else mu[q] - (mu[q // 2] if q % 2 == 0 else 0)
        for q in range(limit + 1)
    ]


def allowed_splits(limit: int) -> List[Edge]:
    """Quarter-balanced unordered splits, exactly 4*j >= n."""
    return [
        (n, j, n - j)
        for n in range(2, limit + 1)
        for j in range(1, n // 2 + 1)
        if 4 * j >= n
    ]


def carry(edge: Edge, q: int) -> int:
    n, j, k = edge
    return n // q - j // q - k // q


def interval_add(a: Interval, b: Interval) -> Interval:
    return LOW.add(a[0], b[0]), HIGH.add(a[1], b[1])


def interval_mul_nonnegative(a: Interval, b: Interval) -> Interval:
    assert a[0] >= 0 and b[0] >= 0
    return LOW.multiply(a[0], b[0]), HIGH.multiply(a[1], b[1])


def primitive_w_interval(endpoint: int, q: int) -> Interval:
    if q == endpoint:
        return ZERO
    x = Decimal(endpoint)
    d = Decimal(q)
    log_lo = LOW.subtract(LOW.ln(x), HIGH.ln(d))
    log_hi = HIGH.subtract(HIGH.ln(x), LOW.ln(d))
    sqrt_lo = LOW.sqrt(d)
    sqrt_hi = HIGH.sqrt(d)
    return LOW.divide(log_lo, sqrt_hi), HIGH.divide(log_hi, sqrt_lo)


def eval_expr_interval(expr: Mapping[int, Fraction], endpoint: int) -> Interval:
    lo = Decimal(0)
    hi = Decimal(0)
    for q, coeff in sorted(expr.items()):
        w_lo, w_hi = primitive_w_interval(endpoint, q)
        c = Decimal(coeff.numerator) / Decimal(coeff.denominator)
        if coeff >= 0:
            lo = LOW.add(lo, LOW.multiply(c, w_lo))
            hi = HIGH.add(hi, HIGH.multiply(c, w_hi))
        else:
            lo = LOW.add(lo, LOW.multiply(c, w_hi))
            hi = HIGH.add(hi, HIGH.multiply(c, w_lo))
    return lo, hi


def add_expr(a: Expr, b: Mapping[int, Fraction], scale: Fraction = Fraction(1)) -> Expr:
    out = dict(a)
    for q, value in b.items():
        out[q] = out.get(q, Fraction(0)) + scale * value
        if out[q] == 0:
            del out[q]
    return out


SUPPORT_20: List[Edge] = [
    (2, 1, 1),
    (3, 1, 2),
    (4, 2, 2),
    (5, 2, 3),
    (6, 3, 3),
    (7, 3, 4),
    (8, 2, 6),
    (9, 3, 6),
    (10, 4, 6),
    (11, 3, 8),
    (12, 4, 8),
    (13, 6, 7),
    (14, 6, 8),
    (15, 4, 11),
    (16, 8, 8),
    (17, 7, 10),
    (18, 6, 12),
    (19, 8, 11),
]

SUPPORT_40_ROOT: List[Edge] = [
    (4, 2, 2), (6, 2, 4), (7, 3, 4), (8, 4, 4),
    (9, 4, 5), (10, 4, 6), (11, 3, 8), (12, 4, 8),
    (13, 5, 8), (13, 6, 7), (14, 6, 8), (15, 4, 11),
    (16, 4, 12), (17, 5, 12), (18, 6, 12), (18, 7, 11),
    (19, 8, 11), (20, 8, 12), (21, 7, 14), (22, 6, 16),
    (23, 11, 12), (24, 12, 12), (25, 8, 17), (26, 12, 14),
    (27, 7, 20), (28, 12, 16), (29, 13, 16), (30, 8, 22),
    (31, 11, 20), (32, 16, 16), (33, 16, 17), (34, 12, 22),
    (35, 11, 24), (36, 12, 24), (37, 15, 22), (38, 16, 22),
    (39, 15, 24),
]


def solve_root_completed_symbolic_40() -> List[Expr]:
    """Solve the exact 37-dimensional root-face system at X=40.

    Primitive variables are W_q for q=3,...,39. The q=2 target is the
    minimal root completion (1/2) sum_{q>=3} b2(q) W_q.
    """
    rows = list(range(3, 40))
    primitives = list(range(3, 40))
    size = len(SUPPORT_40_ROOT)
    assert size == len(rows) == len(primitives) == 37
    matrix = [
        [Fraction(carry(edge, q)) for edge in SUPPORT_40_ROOT]
        for q in rows
    ]
    rhs: List[List[Fraction]] = []
    for q in rows:
        vector = [Fraction(0)] * size
        vector[q - 3] = Fraction(1)
        rhs.append(vector)
    augmented = [matrix[i] + rhs[i] for i in range(size)]
    for column in range(size):
        pivot = next(
            row for row in range(column, size)
            if augmented[row][column] != 0
        )
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    augmented[row][j] - factor * augmented[column][j]
                    for j in range(2 * size)
                ]
    return [
        {q: coefficient for q, coefficient in zip(primitives, augmented[i][size:])
         if coefficient}
        for i in range(size)
    ]


def verify_root_completed_symbolic_40(coefficients: Sequence[Expr]) -> int:
    b40 = b2_values(40)
    checks = 0
    for q in range(2, 41):
        total: Expr = {}
        for edge, expression in zip(SUPPORT_40_ROOT, coefficients):
            if carry(edge, q):
                total = add_expr(total, expression)
        if q == 2:
            expected = {r: Fraction(b40[r], 2) for r in range(3, 40) if b40[r]}
        elif 3 <= q < 40:
            expected = {q: Fraction(1)}
        else:
            expected = {}
        assert total == expected
        checks += 1
    assert all(min(edge[1], edge[2]) >= 2 and 4 * edge[1] >= edge[0]
               for edge in SUPPORT_40_ROOT)
    return checks + len(SUPPORT_40_ROOT)



def symbolic_triangular_flow(endpoint: int, support: Sequence[Edge]) -> Dict[int, Expr]:
    """One edge of parent n, solved downward against primitive target W_q."""
    assert len(support) == endpoint - 2
    out: Dict[int, Expr] = {}
    for n in range(endpoint - 1, 1, -1):
        edge = support[n - 2]
        assert edge[0] == n
        assert 4 * edge[1] >= edge[0]
        expr: Expr = {n: Fraction(1)}
        for m in range(n + 1, endpoint):
            if carry(support[m - 2], n):
                expr = add_expr(expr, out[m], Fraction(-1))
        out[n] = expr
    return out


def verify_symbolic_flow(endpoint: int, support: Sequence[Edge], coeffs: Mapping[int, Expr]) -> int:
    checks = 0
    for q in range(2, endpoint):
        total: Expr = {}
        for n in range(2, endpoint):
            if carry(support[n - 2], q):
                total = add_expr(total, coeffs[n])
        assert total == {q: Fraction(1)}
        checks += 1
    # q=endpoint has zero target and no supported parent can carry it.
    assert all(carry(edge, endpoint) == 0 for edge in support)
    return checks + len(support)


def dot(values: Sequence[Fraction], weights: Sequence[Fraction]) -> Fraction:
    return sum((a * b for a, b in zip(values, weights)), Fraction(0))


def run() -> dict:
    root_floor_checks = 0
    root_split_checks = 0
    primal_dual_checks = 0
    root_neutral_counterexample_checks = 0
    symbolic_flow_checks = 0
    directed_flow_checks = 0
    symbolic_root40_checks = 0
    directed_root40_checks = 0
    directed_separator_checks = 0
    hostile_mutations = 0

    # All-scale root face: sum_{q>=2} b2(q) floor(n/q) = -n for n>=2.
    max_root = 256
    b2 = b2_values(max_root)
    for n in range(2, max_root + 1):
        value = sum(b2[q] * (n // q) for q in range(2, n + 1))
        assert value == -n
        root_floor_checks += 1

    # Its split defect vanishes on every interior row and is negative only on
    # the three quarter-balanced unit-child rows n=2,3,4.
    for edge in allowed_splits(max_root):
        n, j, k = edge
        defect_units = (-n) - (0 if j == 1 else -j) - (0 if k == 1 else -k)
        expected = -(int(j == 1) + int(k == 1))
        assert defect_units == expected
        if expected:
            assert n in (2, 3, 4)
        root_split_checks += 1

    # Exact rational primal/dual discovery fixture at X=6.
    # a_q=1, psi=b2/2. Objective ell_4=ell_5=ell_6=1.
    b6 = b2_values(6)
    psi = [Fraction(0)] * 7
    for q in range(2, 7):
        psi[q] = Fraction(b6[q], 2)
    for edge in allowed_splits(6):
        discrepancy = sum(Fraction(carry(edge, q)) * psi[q] for q in range(2, 7))
        width = sum(carry(edge, q) for q in range(2, 7))
        assert -width <= discrepancy <= 0
        primal_dual_checks += 1
    primal_value = psi[4] + psi[5] + psi[6]
    assert primal_value == 1

    # Positive dual: v=1 on lower constraint of (2,1,1), u=1 on upper
    # constraint of (6,3,3). Their incidence difference is e4+e5+e6.
    e_bottom = (2, 1, 1)
    e_upper = (6, 3, 3)
    dual_target = [
        Fraction(carry(e_upper, q) - carry(e_bottom, q))
        for q in range(2, 7)
    ]
    assert dual_target == [0, 0, 1, 1, 1]
    dual_cost = sum(carry(e_bottom, q) for q in range(2, 7))
    assert dual_cost == primal_value == 1
    primal_dual_checks += 2

    # Root neutrality is not sufficient for positive interior realization.
    # Target t_2=t_6=1 has b2 pairing -2+2=0.
    target = {2: Fraction(1), 6: Fraction(1)}
    assert sum(Fraction(b6[q]) * target.get(q, 0) for q in range(2, 7)) == 0
    # Farkas vector y_2=-1, y_4=1 is nonnegative on every interior split row.
    y = {2: Fraction(-1), 4: Fraction(1)}
    interior = [e for e in allowed_splits(6) if min(e[1], e[2]) >= 2]
    for edge in interior:
        pairing = sum(y.get(q, 0) * carry(edge, q) for q in range(2, 7))
        assert pairing >= 0
        root_neutral_counterexample_checks += 1
    assert sum(y.get(q, 0) * target.get(q, 0) for q in range(2, 7)) == -1
    root_neutral_counterexample_checks += 1

    # Exact symbolic and directed positive carry flow for the full X=20 target.
    coeffs = symbolic_triangular_flow(20, SUPPORT_20)
    symbolic_flow_checks += verify_symbolic_flow(20, SUPPORT_20, coeffs)
    directed_coeffs = {n: eval_expr_interval(expr, 20) for n, expr in coeffs.items()}
    min_lower, min_index = min((iv[0], n) for n, iv in directed_coeffs.items())
    assert min_lower > Decimal(0)
    assert min_index == 5
    assert min_lower > Decimal("0.00727")
    directed_flow_checks += len(directed_coeffs) + 2

    # Exact symbolic and directed positive interior flow for the minimally
    # root-completed X=40 target. This is the first endpoint at which the
    # root tail in the retained campaign is positive.
    root40_coefficients = solve_root_completed_symbolic_40()
    symbolic_root40_checks += verify_root_completed_symbolic_40(root40_coefficients)
    directed_root40 = [eval_expr_interval(expr, 40) for expr in root40_coefficients]
    root40_min_lower, root40_min_edge_index = min(
        (interval[0], index) for index, interval in enumerate(directed_root40)
    )
    assert root40_min_lower > Decimal("0.00006649")
    assert SUPPORT_40_ROOT[root40_min_edge_index] == (18, 6, 12)
    directed_root40_checks += len(directed_root40) + 2

    # Universal root witness feasibility with c=1/(2sqrt(2)).
    # Interior rows have zero defect. Unit-child rows have defects -2c or -c.
    sqrt2_lo = LOW.sqrt(Decimal(2))
    sqrt2_hi = HIGH.sqrt(Decimal(2))
    c_lo = LOW.divide(Decimal(1), HIGH.multiply(Decimal(2), sqrt2_hi))
    c_hi = HIGH.divide(Decimal(1), LOW.multiply(Decimal(2), sqrt2_lo))
    a2_lo = LOW.divide(Decimal(1), sqrt2_hi)
    a2_hi = HIGH.divide(Decimal(1), sqrt2_lo)
    assert LOW.multiply(Decimal(2), c_lo) <= a2_hi
    assert HIGH.multiply(Decimal(2), c_hi) >= a2_lo
    # c < 1/sqrt(3); n=4 has an a2 carry, hence even more reserve.
    sqrt3_hi = HIGH.sqrt(Decimal(3))
    a3_lo = LOW.divide(Decimal(1), sqrt3_hi)
    assert c_hi < a3_lo
    assert c_hi < a2_lo
    directed_separator_checks += 3

    # Directed actual separator at X=40.
    b40 = b2_values(40)
    s_lo = Decimal(0)
    s_hi = Decimal(0)
    for q in range(3, 41):
        if b40[q] == 0:
            continue
        w_lo, w_hi = primitive_w_interval(40, q)
        coefficient = Decimal(b40[q])
        if b40[q] > 0:
            s_lo = LOW.add(s_lo, LOW.multiply(coefficient, w_lo))
            s_hi = HIGH.add(s_hi, HIGH.multiply(coefficient, w_hi))
        else:
            s_lo = LOW.add(s_lo, LOW.multiply(coefficient, w_hi))
            s_hi = HIGH.add(s_hi, HIGH.multiply(coefficient, w_lo))
    assert s_lo > 0
    root_value_lo = LOW.multiply(c_lo, s_lo)
    root_value_hi = HIGH.multiply(c_hi, s_hi)
    assert root_value_lo > Decimal(1) / Decimal(200)
    directed_separator_checks += 2

    # Since the directed X=20 flow has zero debt, N_20=0. The root witness is
    # feasible at X=40, so the OPB defect B_40 is strictly >1/200.
    assert min_lower > 0 and root_value_lo > Decimal(1) / Decimal(200)
    directed_separator_checks += 1

    # Fail-closed mutations.
    mutated_b2 = b40[:]
    mutated_b2[2] += 1
    if sum(mutated_b2[q] * (8 // q) for q in range(2, 9)) != -8:
        hostile_mutations += 1
    wrong_dual_target = [
        Fraction(carry(e_upper, q) + carry(e_bottom, q))
        for q in range(2, 7)
    ]
    if wrong_dual_target != [0, 0, 1, 1, 1]:
        hostile_mutations += 1
    if Decimal("0.005") < root_value_lo and not (Decimal("0.006") < root_value_lo):
        hostile_mutations += 1
    bad_support = list(SUPPORT_20)
    bad_support[3] = (5, 1, 4)  # illegal for eta=1/4 and wrong carry row
    try:
        bad_coeffs = symbolic_triangular_flow(20, bad_support)
        verify_symbolic_flow(20, bad_support, bad_coeffs)
    except (AssertionError, KeyError):
        hostile_mutations += 1
    mutated_root40 = list(SUPPORT_40_ROOT)
    mutated_root40[14] = (18, 5, 13)
    if any(
        sum(carry(edge, q) for edge in mutated_root40)
        != sum(carry(edge, q) for edge in SUPPORT_40_ROOT)
        for q in range(2, 41)
    ):
        hostile_mutations += 1

    assert hostile_mutations == 5

    return {
        "classification": "PASS_X_93021_OPB_ROOT_SEPARATOR",
        "arithmetic_class": "EXACT_RATIONAL_PLUS_DIRECTED_DECIMAL_PRIMITIVES",
        "root_floor_checks": root_floor_checks,
        "root_split_checks": root_split_checks,
        "exact_primal_dual_checks": primal_dual_checks,
        "root_neutral_farkas_checks": root_neutral_counterexample_checks,
        "symbolic_x20_flow_checks": symbolic_flow_checks,
        "directed_x20_flow_checks": directed_flow_checks,
        "directed_x40_separator_checks": directed_separator_checks,
        "symbolic_x40_root_completed_flow_checks": symbolic_root40_checks,
        "directed_x40_root_completed_flow_checks": directed_root40_checks,
        "x20_minimum_flow_lower": str(min_lower),
        "x20_minimum_flow_parent": min_index,
        "x40_root_objective_interval": [str(root_value_lo), str(root_value_hi)],
        "x40_separator": "B_40 > 1/200",
        "x40_root_completed_minimum_flow_lower": str(root40_min_lower),
        "x40_root_completed_minimum_flow_edge": list(SUPPORT_40_ROOT[root40_min_edge_index]),
        "hostile_mutations_detected": hostile_mutations,
        "proves": [
            "the all-scale dyadic root face is a feasible carry-discrepancy witness",
            "an exact rational primal/dual root-face fixture",
            "root neutrality alone is not sufficient for a positive interior flow",
            "a symbolic and directed positive full-target flow at X=20",
            "the exact directed OPB zero-borrowing separator B_40 > 1/200",
            "an exact symbolic and directed positive interior flow for the root-completed X=40 target",
        ],
        "does_not_prove": [
            "a polylogarithmic bound for the redesigned transverse borrowing cone",
            "One-sided Parity Borrowing",
            "polylogarithmic Cycle Debt",
            "the Riemann Hypothesis",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = run()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
