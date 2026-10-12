#!/usr/bin/env python3
"""Certify global all-real SHARP positivity for m>=3/2.

The complete proof is TWO_LABEL.md. Infinite prime masses use the proved
Möbius prime-zeta tail bound P10; all finite quantities use directed Arb.
No squarefree asymptotic, endpoint interpolation, or RH claim is used.
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
from verify_horizon_stitch import as_arb, primes_through, removal_mass, require

POWERS = ((Q('1.5'), Q('1.52')), (Q('1.52'), Q('1.56')),
          (Q('1.56'), Q('1.64')), (Q('1.64'), Q('1.81')))
ENDPOINTS = (1, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120,
             10240, 20480, 40960, 81920, 100000)
PRIME_CUTOFF = 80


def two_label_products(limit: int, primes):
    require(type(limit) is int and limit >= 1, 'pair product limit domain')
    products = []
    for i, p in enumerate(primes):
        if p*p >= limit:
            break
        stop = bisect_right(primes, limit//p)
        products.extend(p*q for q in primes[i+1:stop])
    products.extend(67*p for p in primes if 67*p <= limit)
    return sorted(products)


def two_label_mass(m: Q, endpoint: int, products):
    require(m > 0 and endpoint >= 1, 'two-label mass domain')
    denominator = 4*arb(endpoint).sqrt()-3
    exponent = as_arb(m)
    total = arb(0)
    for n in products:
        if n > endpoint:
            break
        ratio = (4*(arb(endpoint)/n).sqrt()-3)/denominator
        require(bool(ratio > 0) and bool(ratio < 1), 'pair removal ratio domain')
        total += ratio**exponent/arb(n).sqrt()
    return total


def infinite_removal_mass(m: Q, mu):
    a = as_arb((m+1)/2)
    require(bool(a > 1), 'prime-zeta absolute convergence')
    total = sum((mu[k]*(k*a).zeta().log()/k
                 for k in range(1, PRIME_CUTOFF+1)), arb(0))
    tail = arb(2)**(-(PRIME_CUTOFF+1)*a)/(PRIME_CUTOFF+1)
    tail *= (1+2/((PRIME_CUTOFF+1)*a-1))/(1-arb(2)**(-a))
    return total+arb(0, tail.upper())+arb(67)**(-a)


def certificate(low: Q, high: Q, primes, products, mu):
    require(1 < low <= high, 'power slab domain')
    intervals = []
    for left, right in zip(ENDPOINTS[:-1], ENDPOINTS[1:]):
        removal = removal_mass(low, right, primes)
        pairs = two_label_mass(high, left, products)
        require(bool(removal < 3), 'bounded later-level pairing guard')
        margin = 1-removal+(1-removal/3)*pairs
        require(bool(margin > 0), 'bounded two-label positivity margin')
        intervals.append({'endpoint_interval': [left, right],
                          'removal_mass_upper_ball': str(removal),
                          'two_label_mass_lower_ball': str(pairs),
                          'positivity_margin_ball': str(margin),
                          'entire_margin_ball_positive': True})
    infinite = infinite_removal_mass(low, mu)
    pairs = two_label_mass(high, ENDPOINTS[-1], products)
    require(bool(infinite < 3), 'unbounded later-level pairing guard')
    margin = 1-infinite+(1-infinite/3)*pairs
    require(bool(margin > 0), 'unbounded two-label positivity margin')
    return {'power_interval': [str(low), str(high)],
            'bounded_endpoint_certificates': intervals,
            'unbounded_endpoint_interval': [ENDPOINTS[-1], 'infinity'],
            'infinite_removal_mass_ball': str(infinite),
            'two_label_mass_at_last_endpoint_ball': str(pairs),
            'unbounded_positivity_margin_ball': str(margin),
            'unbounded_entire_margin_ball_positive': True}


def run():
    ctx.prec = 192
    primes = primes_through(ENDPOINTS[-1])
    require(len(primes) == 9592 and primes[-1] == 99991, 'complete prime sieve control')
    products = two_label_products(ENDPOINTS[-1], primes)
    require(len(products) == 23550, 'complete labelled pair product count')
    require(two_label_products(10, primes) == [6, 10], 'ordinary pair product control')
    require(products.count(134) == 2 and products.count(4489) == 1,
            'duplicate-67 pair multiplicity control')
    mu = mobius_sieve(PRIME_CUTOFF)
    require(mu[:11] == [1, 1, -1, -1, 0, -1, 1, -1, 0, 0, 1],
            'independent Möbius sieve control')
    reach = POWERS[0][0]
    for low, high in POWERS:
        require(low <= reach, 'power interval coverage gap')
        reach = max(reach, high)
    require(reach == Q('1.81'), 'static positivity threshold overlap')
    records = [certificate(low, high, primes, products, mu) for low, high in POWERS]
    return {
        'status': 'PASS_GLOBAL_SHARP_TWO_LABEL_POSITIVITY',
        'arithmetic': 'ARB_DIRECTED_BALLS_AND_EXACT_RATIONAL_POWERS',
        'precision_bits': ctx.prec,
        'python_flint_version': importlib.metadata.version('python-flint'),
        'global_sufficient_power': '3/2',
        'covered_power_interval': ['1.5', '1.81'],
        'larger_power_input': 'POWER_THRESHOLD.md A-SP1, threshold 1.80206853774',
        'power_slabs': records,
        'bounded_endpoint_interval_count_per_slab': len(ENDPOINTS)-1,
        'complete_labelled_two_product_count': len(products),
        'pair_product_list_sha256': hashlib.sha256(
            (','.join(map(str, products))+'\n').encode('ascii')).hexdigest(),
        'prime_series_cutoff': PRIME_CUTOFF,
        'all_real_endpoints_follow_from_manuscript': True,
        'critical_power_one_proved': False,
        'rh_proved': False,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependency_sha256': {name: hashlib.sha256(
            Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ['check_threshold_arb.py', 'verify_horizon_stitch.py']},
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
