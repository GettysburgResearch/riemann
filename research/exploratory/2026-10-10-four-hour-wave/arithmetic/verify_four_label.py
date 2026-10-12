#!/usr/bin/env python3
"""Directed all-real SHARP certificate retaining the four-label level.

See FOUR_LABEL.md. Complete labelled subset levels through four are
enumerated at the bounded horizon. Whole tails use Euler elementary sums.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction as Q
import hashlib
import importlib.metadata
import json
from pathlib import Path

from flint import arb, ctx

from check_threshold_arb import mobius_sieve
from verify_horizon_stitch import as_arb, primes_through, require
from verify_two_label import two_label_products

POWERS = ((Q('1.4'), Q('1.405')), (Q('1.405'), Q('1.411')),
          (Q('1.411'), Q('1.420')), (Q('1.420'), Q('1.434')),
          (Q('1.434'), Q('1.454')), (Q('1.454'), Q('1.484')),
          (Q('1.484'), Q('1.5')))
ENDPOINTS = (1, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120,
             10240, 20480, 40960, 81920, 163840, 327680, 655360, 1000000)
PRIME_CUTOFF = 80


def labelled_levels(limit: int, primes):
    labels = sorted(primes+([67] if limit >= 67 else []))
    levels = {k: [] for k in range(1, 5)}

    def visit(start, product, level):
        if level:
            levels[level].append(product)
        if level == 4:
            return
        for j in range(start, bisect_right(labels, limit//product)):
            visit(j+1, product*labels[j], level+1)

    visit(0, 1, 0)
    return {k: sorted(v) for k, v in levels.items()}


def level_mass(m: Q, endpoint: int, products):
    require(m > 0 and endpoint >= 1, 'level mass domain')
    denominator = 4*arb(endpoint).sqrt()-3
    exponent = as_arb(m)
    total = arb(0)
    for n in products:
        if n > endpoint:
            break
        ratio = (4*(arb(endpoint)/n).sqrt()-3)/denominator
        require(bool(ratio > 0) and bool(ratio < 1), 'level ratio domain')
        total += ratio**exponent/arb(n).sqrt()
    return total


def prime_power_sum(a: Q, j: int, mu):
    s = as_arb(j*a)
    require(bool(s > 1), 'prime-power sum absolute convergence')
    total = sum((mu[k]*(k*s).zeta().log()/k
                 for k in range(1, PRIME_CUTOFF+1)), arb(0))
    tail = arb(2)**(-(PRIME_CUTOFF+1)*s)/(PRIME_CUTOFF+1)
    tail *= (1+2/((PRIME_CUTOFF+1)*s-1))/(1-arb(2)**(-s))
    return total+arb(0, tail.upper())+arb(67)**(-s)


def infinite_odd_masses(low: Q, mu):
    a = (low+1)/2
    sums = [prime_power_sum(a, j, mu) for j in range(1, 4)]
    third = (sums[0]**3-3*sums[0]*sums[1]+2*sums[2])/6
    require(bool(third > 0), 'positive infinite third elementary sum')
    return sums, third


def verify_slab(low: Q, high: Q, levels, mu):
    require(1 < low <= high, 'power slab domain')
    finite = []
    for left, right in zip(ENDPOINTS[:-1], ENDPOINTS[1:]):
        removal = level_mass(low, right, levels[1])
        third = level_mass(low, right, levels[3])
        second = level_mass(high, left, levels[2])
        fourth = level_mass(high, left, levels[4])
        require(bool(removal < 5), 'bounded later-level pairing guard')
        margin = 1-removal+second-third+(1-removal/5)*fourth
        require(bool(margin > 0), 'bounded four-label margin')
        finite.append({'endpoint_interval': [left, right],
                       'one_label_upper_ball': str(removal),
                       'two_label_lower_ball': str(second),
                       'three_label_upper_ball': str(third),
                       'four_label_lower_ball': str(fourth),
                       'positivity_margin_ball': str(margin),
                       'entire_margin_ball_positive': True})
    sums, third = infinite_odd_masses(low, mu)
    removal = sums[0]
    second = level_mass(high, ENDPOINTS[-1], levels[2])
    fourth = level_mass(high, ENDPOINTS[-1], levels[4])
    require(bool(removal < 5), 'unbounded later-level pairing guard')
    margin = 1-removal+second-third+(1-removal/5)*fourth
    require(bool(margin > 0), 'unbounded four-label margin')
    return {'power_interval': [str(low), str(high)],
            'bounded_endpoint_certificates': finite,
            'unbounded_endpoint_interval': [ENDPOINTS[-1], 'infinity'],
            'infinite_prime_power_sum_balls': [str(s) for s in sums],
            'infinite_three_label_upper_ball': str(third),
            'two_label_lower_at_last_endpoint_ball': str(second),
            'four_label_lower_at_last_endpoint_ball': str(fourth),
            'unbounded_positivity_margin_ball': str(margin),
            'unbounded_entire_margin_ball_positive': True}


def run():
    ctx.prec = 192
    primes = primes_through(ENDPOINTS[-1])
    require(len(primes) == 78498 and primes[-1] == 999983,
            'complete prime sieve control')
    levels = labelled_levels(ENDPOINTS[-1], primes)
    counts = {k: len(v) for k, v in levels.items()}
    require(counts == {1: 78499, 2: 211614, 3: 210777, 4: 95714},
            'complete labelled subset level counts')
    require(levels[2] == two_label_products(ENDPOINTS[-1], primes),
            'independent two-label enumeration control')
    require(levels[1].count(67) == 2 and levels[2].count(4489) == 1,
            'duplicate native label control')
    require([n for n in levels[3] if n <= 70] == [30, 42, 66, 70],
            'three-label activation control')
    require([n for n in levels[4] if n <= 330] == [210, 330],
            'four-label activation control')
    reach = POWERS[0][0]
    for low, high in POWERS:
        require(low <= reach, 'power interval coverage gap')
        reach = max(reach, high)
    require(reach == Q('1.5'), 'prior two-label threshold overlap')
    mu = mobius_sieve(PRIME_CUTOFF)
    records = [verify_slab(low, high, levels, mu) for low, high in POWERS]
    return {
        'status': 'PASS_GLOBAL_SHARP_FOUR_LABEL_POSITIVITY',
        'arithmetic': 'ARB_DIRECTED_BALLS_AND_EXACT_RATIONAL_POWERS',
        'precision_bits': ctx.prec,
        'python_flint_version': importlib.metadata.version('python-flint'),
        'global_sufficient_power': '7/5',
        'covered_power_interval': ['1.4', '1.5'],
        'larger_power_input': 'TWO_LABEL.md A-TL1, threshold 3/2',
        'power_slabs': records,
        'bounded_endpoint_interval_count_per_slab': len(ENDPOINTS)-1,
        'complete_labelled_level_counts': counts,
        'level_product_list_sha256': {k: hashlib.sha256(
            (','.join(map(str, v))+'\n').encode('ascii')).hexdigest()
            for k, v in levels.items()},
        'prime_series_cutoff': PRIME_CUTOFF,
        'all_real_endpoints_follow_from_manuscript': True,
        'critical_power_one_proved': False,
        'rh_proved': False,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependency_sha256': {name: hashlib.sha256(
            Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ['check_threshold_arb.py', 'verify_horizon_stitch.py',
                         'verify_two_label.py']},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
