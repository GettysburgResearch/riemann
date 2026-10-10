#!/usr/bin/env python3
"""Directed SHARP certificate using exact used-label exclusion corrections.

Analytic scope: EXCLUSION_PAIRS.md and EXCLUSION_STITCH.md. No ordinary
floating acceptance conditions or Python assertions occur in this checker.
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
from exclusion_moments import ExclusionMoments
from exclusion_tail import numerator_polynomial, certify_positive_tail
from verify_four_label import prime_power_sum
from verify_horizon_stitch import require
from verify_weighted_stitch import nonnegative_lower, smaller_upper
from weighted_moments import normalized_level_bounds

PRODUCT_CUTOFF = 10000000
POWER_POINTS = tuple(map(Q, ('1.3', '1.3002', '1.3005', '1.301',
    '1.3018', '1.303', '1.3048', '1.3075', '1.3115', '1.3175', '1.32')))
ENDPOINTS = (1, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120,
             10240, 20480, 40960, 81920, 163840, 327680, 655360,
             1310720, 2621440, 5242880, PRODUCT_CUTOFF)
LEVELS = (2, 4, 6)


def build_power_data(power, mu, progress=False):
    weights = ExclusionMoments((power+1)/2, PRODUCT_CUTOFF)
    require(weights.prime_cap == 5000000 and len(weights.primes) == 348513
            and weights.primes[-1] == 4999999, 'complete prime sieve control')
    require(weights.labels.count(67) == 2, 'two distinct native 67 labels')
    infinite_one = prime_power_sum((power+1)/2, 1, mu)
    require(bool(infinite_one < 3), 'positive first-pair removal coefficient')
    finite = {}
    for endpoint in ENDPOINTS:
        single = weights.cumulative(1, min(endpoint, weights.prime_cap))
        _, odd = normalized_level_bounds(power, endpoint, single)
        if endpoint > weights.prime_cap:
            tail = infinite_one-single[0]
            require(bool(tail > 0), 'positive omitted single-label mass')
            odd += tail
        triple = weights.cumulative(3, endpoint)
        _, triple_upper = normalized_level_bounds(power, endpoint, triple)
        row = {'odd': smaller_upper(odd, infinite_one), 'triple': triple_upper.upper()}
        for level in LEVELS:
            selected = weights.marked_cumulative(level, endpoint)
            lower, _ = normalized_level_bounds(power, endpoint, selected.ordinary)
            marked, _ = normalized_level_bounds(power, endpoint, selected.marked)
            row[level] = (nonnegative_lower(lower), nonnegative_lower(marked))
        finite[endpoint] = row
    selected = {level: weights.marked_cumulative(level, PRODUCT_CUTOFF)
                for level in LEVELS}
    single = weights.cumulative(1, weights.prime_cap)
    if progress:
        print(f'Certified marked finite moments at m={power}', file=sys.stderr, flush=True)
    return {'power': power, 'finite': finite, 'selected': selected,
            'one': single, 'infinite_one': infinite_one}


def verify_slab(low_data, high_data):
    low, high = low_data['power'], high_data['power']
    removal = low_data['infinite_one'].upper()
    require(removal.is_exact() and bool(removal < 3), 'global pair removal domain')
    bounded = []
    for left, right in zip(ENDPOINTS[:-1], ENDPOINTS[1:]):
        odd = low_data['finite'][right]['odd']
        positive = arb(0)
        for level in LEVELS:
            even, marked = high_data['finite'][left][level]
            positive += (1-removal/(level+1))*even+marked/(level+1)
        pair_margin = 1-odd+positive
        even = high_data['finite'][left]
        four_margin = (1-odd+even[2][0]-low_data['finite'][right]['triple']
                       +(1-odd/5)*even[4][0])
        margin = pair_margin if bool(pair_margin > four_margin) else four_margin
        require(bool(margin > 0), f'exclusion bounded margin [{left},{right}], powers [{low},{high}]')
        bounded.append({'endpoint_interval': [left, right],
                        'one_label_upper': str(odd),
                        'even_pairs_lower': str(positive),
                        'exclusion_pair_margin_ball': str(pair_margin),
                        'complete_four_level_margin_ball': str(four_margin),
                        'margin_ball': str(margin),
                        'entire_margin_ball_positive': True})
    polynomial, constants = numerator_polynomial(low, high, low_data['one'],
                                                  high_data['selected'],
                                                  low_data['infinite_one'])
    tail = certify_positive_tail(polynomial, PRODUCT_CUTOFF)
    return {'power_interval': [str(low), str(high)],
            'bounded_endpoint_certificates': bounded,
            'tail_constants': constants,
            'tail_numerator_coefficient_balls': [str(c) for c in polynomial],
            'unbounded_tail_certificate': tail}


def run(progress=False, only_first=False):
    ctx.prec = 192
    require(POWER_POINTS[0] == Q('1.3') and POWER_POINTS[-1] == Q('1.32'),
            'power coverage endpoints')
    require(all(a < b for a,b in zip(POWER_POINTS[:-1],POWER_POINTS[1:])),
            'strict power endpoint order')
    require(ENDPOINTS[0] == 1 and ENDPOINTS[-1] == PRODUCT_CUTOFF
            and all(a < b for a,b in zip(ENDPOINTS[:-1],ENDPOINTS[1:])),
            'complete endpoint-chain coverage')
    mu = mobius_sieve(80)
    records = []
    low = build_power_data(POWER_POINTS[0], mu, progress)
    for high_power in POWER_POINTS[1:]:
        high = build_power_data(high_power, mu, progress)
        records.append(verify_slab(low, high))
        low = high
        if only_first: break
    return {'status': 'PASS_FIRST_SLAB_ONLY' if only_first else 'PASS_GLOBAL_SHARP_EXCLUSION_STITCH',
            'arithmetic': 'ARB_DIRECTED_BALLS_EXACT_RATIONAL_POWERS_AND_BERNSTEIN_TAILS',
            'precision_bits':ctx.prec, 'python_flint_version':importlib.metadata.version('python-flint'),
            'global_sufficient_power':None if only_first else '13/10',
            'covered_power_interval':['1.3',str(POWER_POINTS[1] if only_first else POWER_POINTS[-1])],
            'larger_power_input':'WEIGHTED_STITCH.md A-WM1, threshold 33/25',
            'power_slab_count':len(records),
            'bounded_endpoint_intervals_per_power_slab':len(ENDPOINTS)-1,
            'selected_product_cutoff':PRODUCT_CUTOFF, 'ordinary_prime_sieve_cap':PRODUCT_CUTOFF//2,
            'ordinary_prime_count':348513, 'duplicate_67_label_count':2,
            'retained_even_levels':list(LEVELS), 'moment_order':6,
            'power_slabs':records, 'critical_power_one_proved':False, 'rh_proved':False,
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependency_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                for name in ['exclusion_moments.py','exclusion_tail.py','weighted_moments.py',
                             'polynomial_tail.py','check_threshold_arb.py','verify_four_label.py',
                             'verify_horizon_stitch.py','verify_weighted_stitch.py','verify_two_label.py']}}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--progress',action='store_true')
    parser.add_argument('--only-first',action='store_true',help='reconnaissance guard; does not assert global coverage')
    args=parser.parse_args()
    result=run(args.progress,args.only_first)
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    print(text,end='')

if __name__=='__main__':main()
