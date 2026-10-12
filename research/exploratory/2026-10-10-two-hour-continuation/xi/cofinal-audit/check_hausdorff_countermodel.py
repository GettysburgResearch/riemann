#!/usr/bin/env python3
"""Exact rational mixed-moment witness for a declared finite non-Xi source."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from math import comb, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent


def need(ok: bool, message: str) -> None:
    if not ok:
        raise SystemExit('FAIL: ' + message)


def mul(a: tuple[Q, Q], b: tuple[Q, Q]) -> tuple[Q, Q]:
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def power(a: tuple[Q, Q], n: int) -> tuple[Q, Q]:
    value = Q(1), Q(0)
    for _ in range(n):
        value = mul(value, a)
    return value


def inverse(a: tuple[Q, Q]) -> tuple[Q, Q]:
    norm = a[0]**2+a[1]**2
    need(norm > 0, 'nonzero exact Gaussian rational divisor')
    return a[0]/norm, -a[1]/norm


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=HERE/'hausdorff_countermodel_normal.json')
    args = parser.parse_args()
    root = Q(2), Q(1, 2)
    square = mul(root, root)
    beta = inverse(square)
    need(beta == (Q(60, 289), Q(-32, 289)), 'declared unshifted node')
    need(beta[0]**2+beta[1]**2 == Q(16, 289), 'exact unshifted node modulus square')
    need(Q(4, 17) < Q(1, 2), 'all-order scalar dominance margin')
    shifted = inverse((square[0]+1, square[1]))
    need(shifted == (Q(76, 425), Q(-32, 425)), 'declared shifted node')
    need(shifted[0]**2+shifted[1]**2 == Q(16, 425) < Q(1, 25),
         'all-order shifted scalar dominance margin')
    scale = Q(4, 3)
    real_node = Q(1, 2)
    a = [real_node**(n+1)+2*power(shifted, n+1)[0] for n in range(32)]
    b = [a[n]/scale**n for n in range(32)]
    need(all(x > 0 for x in a), 'displayed finite shifted moments positive')
    q = shifted[0]/scale, shifted[1]/scale
    one_minus_q = 1-q[0], -q[1]
    differences = []
    for m in range(32):
        combination = sum((Q((-1)**j*comb(m, j))*b[j] for j in range(m+1)), Q(0))
        direct = real_node*(1-real_node/scale)**m+2*mul(shifted, power(one_minus_q, m))[0]
        need(combination == direct, 'independent binomial/node mixed formula')
        differences.append(combination)
    need(all(x > 0 for x in differences[:31]) and differences[31] < 0,
         'first negative in the n=0 row is m=31')
    N = 31
    weights = []
    for ell in range(N+1):
        difference = sum((Q((-1)**j*comb(N-ell, j))*b[ell+j]
                          for j in range(N-ell+1)), Q(0))
        weights.append(comb(N, ell)*difference)
    need(sum(weights, Q(0)) == b[0], 'Bernstein partition total mass')
    for n in range(N+1):
        denominator = prod(range(N-n+1, N+1))
        value = sum((Q(prod(range(ell-n+1, ell+1)), denominator)*weights[ell]
                     for ell in range(N+1)), Q(0))
        need(value == b[n], 'exact Bernstein falling-factorial identity')
    need(weights[0] == differences[31] < 0, 'negative constructive measure weight')
    sources = [Path(__file__).resolve(), HERE/'HAUSDORFF_LOG_MOMENT_CRITERION.md',
               HERE/'COFINAL_MOMENT_OBSTRUCTION.md']
    result = {
        'status': 'PASS_EXACT_RATIONAL_HAUSDORFF_COUNTERMODEL',
        'arithmetic': 'Exact Python integer/Fraction Gaussian rational pairs; no floating predicate.',
        'source': 'Declared finite even polynomial with simple paired zeros +/-1, +/-(2+i/2), +/-(2-i/2).',
        'actual_Xi_or_theta_source_used': False,
        'positive_Fourier_kernel_claimed_for_this_polynomial': False,
        'complete_strip_half_width': '1/2', 'shift_t': '1', 'scale_L': str(scale),
        'all_order_unshifted_scalar_positivity_structural_modulus': '4/17',
        'all_order_shifted_scalar_positivity_structural_modulus_square': '16/425 < 1/25',
        'all_order_scalar_statements_supplied_by_the_analytic_norm_bound': True,
        'infinite_inequality_hierarchy_replayed': False,
        'finite_shifted_moments_replayed': 32,
        'mixed_node_and_binomial_formulas_compared': 32,
        'first_negative_index_in_n_zero_row': [0, 31],
        'exact_negative_witness': str(differences[31]),
        'witness_upper_endpoint_is_strictly_negative': True,
        'Bernstein_N31_partition_and_all_32_factorial_moments_replayed': True,
        'negative_N31_weight_at_zero': str(weights[0]),
        'rh_proved_or_refuted': False,
        'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(result['status'], 'WITNESS', 'D_0_31<0', flush=True)


if __name__ == '__main__':
    main()
