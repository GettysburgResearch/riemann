#!/usr/bin/env python3
"""Exact rational interval replay of a complete native congruence certificate."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys
from flint import arb, arb_mat, ctx

HERE = Path(__file__).resolve().parent
OPS = HERE.parent
sys.path.insert(0, str(OPS))
import physical_length_source
from directed_congruence_gate import gate

FROZEN = {
    'directed_congruence_gate.py': 'e4e34814942001d1576f1c5d8a798d1c0fd968790becf9b829503173a4bf1f54',
    'DIRECTED_CONGRUENCE_GATE.md': 'df7f7a68de4c6864b262653d73863921ba1c785c3c81d05f9706c76c22c85705',
    'enclose_length_robust_weighted.py': '9c774a1de5b0d0771764ffeeb7e56bfbf20620774f5a00466c3cd750a7f891d7',
    'enclose_length_robust_mixed.py': '38ef6a1f5125adf72f037d625222eccae509f4a146037361ca02dd20f1e1a6f3',
}


def need(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def endpoints(text):
    value = arb(text)
    need(value.is_finite(), 'finite serialized outward source ball')
    lo, hi = value.lower(), value.upper()
    need(lo.is_exact() and hi.is_exact(), 'exact dyadic endpoints')
    return Q(str(lo.fmpq())), Q(str(hi.fmpq()))


def run(receipt):
    for name, digest in FROZEN.items():
        need(sha(OPS / name) == digest, ('frozen reviewed producer', name))
    ctx.prec = 256
    data = json.loads(receipt.read_text())
    mixed = 'mixed_weighted_lower_matrix_balls' in data
    source = 'enclose_length_robust_mixed.py' if mixed else 'enclose_length_robust_weighted.py'
    need(data['producer_sha256'] == FROZEN[source], 'exact native producer identity')
    need(data['R_receipt_sha256'] == 'cede53ceb2e0543060c65bcd456e17983bb8197dc7127c361f918dcd5cca5191', 'complete physical R identity')
    rows = data['mixed_weighted_lower_matrix_balls'] if mixed else data['weighted_lower_matrix_balls']
    epsilon = Q(data['epsilon_exact']) if mixed else Q(data['certified_finite_lower_eigenvalue'])
    need(epsilon == (Q(1, 20000000000) if mixed else Q(1, 100000000000)), 'exact prescribed finite reserve')
    n = 10
    need(len(rows) == n and all(len(row) == n for row in rows), 'all native source matrix entries')
    A = [[endpoints(text) for text in row] for row in rows]
    need(all(A[i][j] == A[j][i] for i in range(n) for j in range(n)), 'complete symmetric source intervals')
    certificate = data['directed_congruence_certificate']
    P = [[Q(text) for text in row] for row in certificate['exact_dyadic_preconditioner']]
    need(len(P) == n and all(len(row) == n for row in P), 'complete exact preconditioner')
    need(all(x.denominator & (x.denominator - 1) == 0 for row in P for x in row), 'every preconditioner entry dyadic')
    # Full direct sum over original entry intervals; this does not call the
    # owner's native matrix multiplication or use its derived C balls.
    C = []
    for i in range(n):
        row = []
        for j in range(n):
            lo = hi = Q(0)
            for k in range(n):
                for ell in range(n):
                    a, b = A[k][ell]
                    if k == ell:
                        a -= epsilon
                        b -= epsilon
                    weight = P[k][i] * P[ell][j]
                    if weight >= 0:
                        lo += weight * a
                        hi += weight * b
                    else:
                        lo += weight * b
                        hi += weight * a
            row.append((lo, hi))
        C.append(row)
    margins = [C[i][i][0] - sum(
        (max(abs(C[i][j][0]), abs(C[i][j][1])) for j in range(n) if j != i), Q(0))
        for i in range(n)]
    need(all(x > 0 for x in margins), 'every complete exact interval congruence Gershgorin row positive')
    owner_C = [[endpoints(text) for text in row] for row in certificate['shifted_congruence_matrix_balls']]
    need(len(owner_C) == n and all(len(row) == n for row in owner_C), 'all owner congruence balls')
    need(all(max(C[i][j][0], owner_C[i][j][0]) <= min(C[i][j][1], owner_C[i][j][1])
             for i in range(n) for j in range(n)), 'every independent exact interval overlaps directed owner congruence')

    # Meaningful soundness controls: a positive-center input whose admitted
    # corner has determinant -.03 must not be accepted by the native gate.
    positive = arb_mat([[1, arb('0 +/- 0.0001')], [arb('0 +/- 0.0001'), arb('0.01')]])
    gate(positive, arb(0))
    bad = arb_mat([[1, arb('0 +/- 0.2')], [arb('0 +/- 0.2'), arb('0.01')]])
    need(Q(1, 100) - Q(1, 5) ** 2 == -Q(3, 100), 'exact negative admitted corner')
    try:
        gate(bad, arb(0))
    except ArithmeticError as error:
        need('Gershgorin row' in str(error), 'bad box rejected by full interval margin guard')
    else:
        raise ArithmeticError('native gate falsely accepted a box containing a negative matrix')
    return {
        'status': 'EXACT_FRACTION_FULL_CONGRUENCE_ORACLE_PASS',
        'native_matrix_class': 'mixed' if mixed else 'baseline',
        'source_receipt_sha256': sha(receipt), 'epsilon_exact': str(epsilon),
        'native_dimension': n, 'full_source_entries': 100, 'full_P_entries': 100,
        'all_original_interval_errors_retained': True,
        'independent_exact_interval_product_terms': n ** 4,
        'exact_positive_row_margins': [str(x) for x in margins],
        'minimum_row_margin_exact': str(min(margins)),
        'every_owner_congruence_ball_overlaps': True,
        'positive_box_control_passed': True,
        'negative_corner_box_control_rejected': True,
        'native_congruence_product_reused': False,
        'R_integration_performed': False,
        'producer_sha256': sha(Path(__file__)), 'frozen_sources': FROZEN,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('receipt', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run(args.receipt)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(result['status'], result['native_matrix_class'])
