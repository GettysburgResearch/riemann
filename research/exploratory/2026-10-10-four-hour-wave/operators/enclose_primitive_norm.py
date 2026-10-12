#!/usr/bin/env python3
"""Extract exact primitive-norm constants after replaying a frozen weighted bound.

This requires a completed directed continuum receipt. It does not integrate R
again or certify a new source adapter. See QUANTITATIVE_PRIMITIVE_COMPLETION.md.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

from flint import arb
from enclose_analytic_upper import require

HERE = Path(__file__).resolve().parent
CHECKERS = {
    'cc96f85d80d348bc3e2f11ab37e2b7f4c9d4eedfcda16b5a8533b32c1f1ce236':
        'enclose_weighted_lower.py',
    '0ba57657eef0ea728134e846c2861f778793715c5d091c3c47090cc87f003f25':
        'enclose_weighted_lower_taylor.py',
}


def exact_upper(x):
    y = x.upper()
    require(y.is_finite() and y.is_exact(), 'finite exact directed upper endpoint')
    mantissa, exponent = y.man_exp()
    return Q(int(mantissa)) * Q(2) ** int(exponent)


def positive_integer_upper(x):
    y = exact_upper(x)
    return max(1, -(-y.numerator // y.denominator))


def semantic(data):
    if isinstance(data, dict):
        return {k: semantic(v) for k, v in data.items()
                if k not in ('elapsed_seconds', 'R_receipt_path')}
    if isinstance(data, list):
        return [semantic(v) for v in data]
    return data


def enclose(weighted_path, residual_path):
    data = json.loads(weighted_path.read_text())
    producer = data['producer_sha256']
    require(producer in CHECKERS, 'frozen independently reviewed weighted checker')
    name = CHECKERS[producer]
    require(hashlib.sha256((HERE / name).read_bytes()).hexdigest() == producer,
            'current weighted checker matches frozen review')
    require(data['R_receipt_sha256'] == hashlib.sha256(residual_path.read_bytes()).hexdigest(),
            'exact completed residual receipt')
    if name == 'enclose_weighted_lower.py':
        from enclose_weighted_lower import enclose as replay
    else:
        from enclose_weighted_lower_taylor import enclose as replay
    fresh = replay(residual_path, last=128, bits=256)
    require(semantic(data) == semantic(fresh), 'full fresh mathematical weighted replay')
    require(fresh['status'] == 'DIRECTED_WEIGHTED_SINGLE_WINDOW_LOWER_ACCEPT',
            'completed directed weighted lower acceptance')
    require(fresh['certified_lower_eigenvalue'] == '1e-11', 'frozen positive reserve')
    removed = fresh['removed_sine_modes']
    require(removed in (5, 11), 'reviewed primitive complement')
    dimension = removed + 3
    source = fresh['fresh_source_moment_receipt']['source_U_receipt']
    u = source['U_matrix_balls']
    lower = fresh['weighted_lower_matrix_balls']
    trace_cost = sum((arb(u[i][i]) - arb(lower[i][i])
                      for i in range(dimension)), arb(0))
    m = positive_integer_upper(trace_cost)
    coeffs = source['exact_trial_z_coefficients_balls']
    require(len(coeffs) == dimension + 100 and all(len(row) == dimension for row in coeffs),
            'complete exact high-sine trial coefficient inventory')
    k_ball = arb(0)
    for i in range(dimension):
        column_sum = sum((arb(row[i]).abs_upper() for row in coeffs[dimension:]), arb(0))
        k_ball += 1 + column_sum * column_sum
    k_ball *= arb(18) / 25
    k = positive_integer_upper(k_ball)
    epsilon = Q(1, 10 ** 11)
    kappa = Q(1, 6) if removed == 5 else Q(6, 5)
    theta = epsilon / (2 * m + epsilon)
    delta = min(epsilon / (2 * (1 + 2 * k)), theta * kappa / 2)
    require(theta > 0 and delta > 0, 'strict exact primitive norm constant')
    return {
        'status': 'DIRECTED_NATIVE_PRIMITIVE_NORM_ACCEPT',
        'scope': 'native complex L2 tests on every 0<L<=1, conditional inherited O1-O4',
        'weighted_receipt_sha256': hashlib.sha256(weighted_path.read_bytes()).hexdigest(),
        'residual_receipt_sha256': hashlib.sha256(residual_path.read_bytes()).hexdigest(),
        'reviewed_weighted_checker_sha256': producer,
        'removed_sine_modes': removed,
        'complement_dimension': dimension,
        'epsilon_exact': str(epsilon),
        'primitive_gap_exact': str(kappa),
        'residual_trace_upper_integer': m,
        'trial_primitive_synthesis_upper_integer': k,
        'theta_exact': str(theta),
        'delta_exact': str(delta),
        'delta_decimal_for_display_only': float(delta),
        'bound': 'q_1(h)>=delta*(||Pi_E h||_2^2+||G_1 h||_2^2); q_L(h)>=delta*||G_L h||_2^2',
        'G_definition': 'G_L h(t)=integral_0^t cosh((t-u)/2)*h(u) du',
        'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_sha256': hashlib.sha256((HERE / 'QUANTITATIVE_PRIMITIVE_COMPLETION.md').read_bytes()).hexdigest(),
        'limitations': ['no uniform L2 spectral gap', 'no independent second full R integration',
                        'xi/Weil terminal identification remains separate', 'RH remains open'],
    }


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('weighted_receipt', type=Path)
    p.add_argument('residual_receipt', type=Path)
    p.add_argument('--out', required=True, type=Path)
    args = p.parse_args()
    result = enclose(args.weighted_receipt, args.residual_receipt)
    args.out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
