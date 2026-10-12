#!/usr/bin/env python3
"""Certify global SHARP positivity from weighted moments and Bernstein tails.

The source and analytic scope are WEIGHTED_MOMENTS.md and
WEIGHTED_STITCH.md. Every acceptance comparison uses directed Arb balls.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import importlib.metadata
import json
from pathlib import Path
import sys

from flint import arb, ctx

from check_threshold_arb import mobius_sieve
from polynomial_tail import numerator_polynomial, certify_positive_tail
from verify_four_label import infinite_odd_masses
from verify_horizon_stitch import require
from weighted_moments import WeightedMoments, normalized_level_bounds

PRODUCT_CUTOFF = 10000000
POWER_POINTS = tuple(map(Q, (
    '1.32', '1.3202', '1.3205', '1.321', '1.3217', '1.3228',
    '1.3241', '1.3259', '1.3284', '1.3318', '1.3365', '1.3431',
    '1.3522', '1.3652', '1.385', '1.4',
)))
ENDPOINTS = (1, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120,
             10240, 20480, 40960, 81920, 163840, 327680, 655360,
             1310720, 2621440, 5242880, PRODUCT_CUTOFF)


def nonnegative_lower(ball):
    lower = ball.lower()
    require(lower.is_exact(), 'exact level lower endpoint')
    return arb(0) if bool(lower < 0) else lower


def smaller_upper(first, second):
    first = first.upper()
    second = second.upper()
    require(first.is_exact() and second.is_exact(), 'exact level upper endpoints')
    return first if bool(first < second) else second


def build_power_data(power: Q, mu, progress=False):
    weights = WeightedMoments((power+1)/2, PRODUCT_CUTOFF)
    require(weights.prime_cap == 5000000 and len(weights.primes) == 348513
            and weights.primes[-1] == 4999999, 'complete retained prime sieve control')
    require(weights.labels.count(67) == 2, 'two native 67 labels')
    sums, infinite_three = infinite_odd_masses(power, mu)
    infinite_one = sums[0]
    require(bool(infinite_one < 5), 'global later-level pairing domain')
    finite = {}
    for endpoint in ENDPOINTS:
        row = {}
        for level in range(1, 5):
            cap = weights.prime_cap if level == 1 else PRODUCT_CUTOFF
            selected = weights.cumulative(level, min(endpoint, cap))
            lower, upper = normalized_level_bounds(power, endpoint, selected)
            if level in [1, 3]:
                infinite = infinite_one if level == 1 else infinite_three
                if endpoint > cap:
                    tail = infinite-selected[0]
                    require(bool(tail > 0), 'positive omitted odd Euler mass')
                    upper += tail
                bound = smaller_upper(upper, infinite)
                require(bool(bound >= 0), 'nonnegative odd upper bound')
                row[level] = bound
            else:
                row[level] = nonnegative_lower(lower)
        finite[endpoint] = row
    selected = {level: weights.cumulative(
        level, weights.prime_cap if level == 1 else PRODUCT_CUTOFF)
        for level in range(1, 5)}
    if progress:
        print(f'Certified finite moment bounds at m={power}', file=sys.stderr, flush=True)
    return {'power': power, 'finite': finite, 'selected': selected,
            'infinite_one': infinite_one, 'infinite_three': infinite_three}


def verify_slab(low_data, high_data):
    low, high = low_data['power'], high_data['power']
    require(1 < low <= high < 2, 'power slab domain')
    bounded = []
    for left, right in zip(ENDPOINTS[:-1], ENDPOINTS[1:]):
        odd = low_data['finite'][right]
        even = high_data['finite'][left]
        removal = odd[1]
        require(bool(removal < 5), 'bounded removal domain')
        margin = 1-removal+even[2]-odd[3]+(1-removal/5)*even[4]
        require(bool(margin > 0), f'bounded weighted stitch margin at [{left},{right}]')
        bounded.append({'endpoint_interval': [left, right],
                        'odd_one_upper': str(removal),
                        'odd_three_upper': str(odd[3]),
                        'even_two_lower': str(even[2]),
                        'even_four_lower': str(even[4]),
                        'margin_ball': str(margin),
                        'entire_margin_ball_positive': True})
    selected_low = low_data['selected']
    selected_high = high_data['selected']
    polynomial, constants = numerator_polynomial(
        low, high, selected_low[1], selected_low[3],
        selected_high[2], selected_high[4], low_data['infinite_one'],
        low_data['infinite_three'])
    tail = certify_positive_tail(polynomial, PRODUCT_CUTOFF)
    return {'power_interval': [str(low), str(high)],
            'bounded_endpoint_certificates': bounded,
            'tail_constants': constants,
            'tail_numerator_coefficient_balls': [str(c) for c in polynomial],
            'unbounded_tail_certificate': tail}


def run(progress=False):
    ctx.prec = 192
    require(POWER_POINTS[0] == Q('1.32') and POWER_POINTS[-1] == Q('1.4'),
            'power coverage endpoints')
    require(all(a < b for a, b in zip(POWER_POINTS[:-1], POWER_POINTS[1:])),
            'strict power endpoint order')
    require(ENDPOINTS[0] == 1 and ENDPOINTS[-1] == PRODUCT_CUTOFF
            and all(a < b for a, b in zip(ENDPOINTS[:-1], ENDPOINTS[1:])),
            'complete endpoint-chain coverage')
    mu = mobius_sieve(80)
    records = []
    low_data = build_power_data(POWER_POINTS[0], mu, progress)
    for high in POWER_POINTS[1:]:
        high_data = build_power_data(high, mu, progress)
        records.append(verify_slab(low_data, high_data))
        low_data = high_data
    return {
        'status': 'PASS_GLOBAL_SHARP_WEIGHTED_MOMENT_STITCH',
        'arithmetic': 'ARB_DIRECTED_BALLS_EXACT_RATIONAL_POWERS_AND_BERNSTEIN_TAILS',
        'precision_bits': ctx.prec,
        'python_flint_version': importlib.metadata.version('python-flint'),
        'global_sufficient_power': '33/25',
        'covered_power_interval': ['1.32', '1.4'],
        'larger_power_input': 'FOUR_LABEL.md A-FL1, threshold 7/5',
        'power_slab_count': len(records),
        'bounded_endpoint_intervals_per_power_slab': len(ENDPOINTS)-1,
        'selected_product_cutoff': PRODUCT_CUTOFF,
        'ordinary_prime_sieve_cap': PRODUCT_CUTOFF//2,
        'ordinary_prime_count': 348513,
        'duplicate_67_label_count': 2,
        'weighted_moment_order': 6,
        'power_slabs': records,
        'all_real_endpoints_follow_from_manuscript': True,
        'critical_power_one_proved': False,
        'rh_proved': False,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependency_sha256': {name: hashlib.sha256(
            Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ['weighted_moments.py', 'polynomial_tail.py',
                         'check_threshold_arb.py', 'verify_four_label.py',
                         'verify_horizon_stitch.py', 'verify_two_label.py']},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--progress', action='store_true')
    args = parser.parse_args()
    result = run(args.progress)
    text = json.dumps(result, sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
