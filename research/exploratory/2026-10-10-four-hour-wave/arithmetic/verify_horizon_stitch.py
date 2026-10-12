#!/usr/bin/env python3
"""Certify all-endpoint SHARP positivity by finite-horizon/tail stitching.

Requires python-flint 0.9.0. Every prime through each integer horizon is
enumerated; all nonrational evaluations use Arb directed balls. The proof
in HORIZON_STITCH.md turns these finite inequalities into the all-real-
endpoint and all-real-power theorem. No critical-power or RH claim.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import importlib.metadata
import json
from pathlib import Path

from flint import arb, ctx

SLABS = (
    (Q('1.7725'), Q('1.773'), 29200),
    (Q('1.773'), Q('1.774'), 30000),
    (Q('1.774'), Q('1.778'), 32000),
    (Q('1.775'), Q('1.79'), 35000),
    (Q('1.78'), Q('1.81'), 40000),
)


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def as_arb(value) -> arb:
    value = Q(value)
    return arb(value.numerator)/value.denominator


def primes_through(limit: int):
    require(type(limit) is int and limit >= 2, 'sieve domain')
    sieve = bytearray(b'\x01')*(limit+1)
    sieve[0] = sieve[1] = 0
    p = 2
    while p*p <= limit:
        if sieve[p]:
            start = p*p
            sieve[start:limit+1:p] = b'\x00'*((limit-start)//p+1)
        p += 1
    return [p for p in range(2, limit+1) if sieve[p]]


def tail_error(m: Q) -> Q:
    require(Q(3, 2) <= m < 2, 'tail monotonicity domain')
    return Q(68, 67)*(3*m/(2*(2-m))+2/(m-1))+2


def removal_mass(m: Q, horizon: int, primes):
    root = arb(horizon).sqrt()
    denominator = 4*root-3
    power = as_arb(m)
    total = arb(0)
    for p in primes:
        if p > horizon:
            break
        p_ball = arb(p)
        ratio = (4*(arb(horizon)/p).sqrt()-3)/denominator
        require(bool(ratio > 0) and bool(ratio < 1), 'removal ratio domain')
        term = ratio**power/p_ball.sqrt()
        total += term
        if p == 67:
            total += term  # the second native source label
    return total


def verify_slab(low: Q, high: Q, horizon: int, primes):
    require(Q(3, 2) <= low <= high < 2, 'power slab domain')
    require(type(horizon) is int and horizon >= 67, 'horizon domain')
    mass = removal_mass(low, horizon, primes)
    require(bool(mass < 1), 'finite-horizon pairing mass is not below one')
    a = as_arb((low+1)/2)
    beta_series = (1-arb(67)**(-a))/a.zeta()
    require(bool(beta_series > 0), 'positive beta Dirichlet series')
    tail_left = beta_series * arb(horizon)**as_arb((low-1)/2)
    tail_right = as_arb(tail_error(high))
    margin = tail_left-tail_right
    require(bool(margin > 0), 'uniform tail inequality not proved')
    active = [p for p in primes if p <= horizon]
    prime_bytes = (','.join(map(str, active))+'\n').encode('ascii')
    return {
        'power_interval': [str(low), str(high)],
        'horizon': horizon,
        'ordinary_prime_count': len(active),
        'prime_list_sha256': hashlib.sha256(prime_bytes).hexdigest(),
        'duplicate_67_labels': 1,
        'finite_removal_mass': str(mass),
        'one_minus_removal_mass': str(1-mass),
        'pairing_mass_entire_ball_below_one': True,
        'tail_left_ball': str(tail_left),
        'tail_right_exact': str(tail_error(high)),
        'tail_margin_ball': str(margin),
        'tail_margin_entire_ball_positive': True,
    }


def run():
    ctx.prec = 192
    require(primes_through(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
            'prime sieve control')
    primes = primes_through(max(x for _, _, x in SLABS))
    require(len(primes) == 4203 and primes[-1] == 39989, 'complete prime count control')
    reach = SLABS[0][0]
    for low, high, _ in SLABS:
        require(low <= reach, 'gap in power interval coverage')
        reach = max(reach, high)
    require(reach == Q('1.81'), 'static-threshold overlap not covered')
    records = [verify_slab(*slab, primes) for slab in SLABS]
    # The exact rational checker separately proves the static threshold
    # 1.80206853774 < 1.81, hence covers every larger exponent.
    return {
        'status': 'PASS_GLOBAL_SHARP_FINITE_HORIZON_TAIL_STITCH',
        'arithmetic': 'ARB_DIRECTED_BALLS_AND_EXACT_RATIONAL_COEFFICIENTS',
        'precision_bits': ctx.prec,
        'python_flint_version': importlib.metadata.version('python-flint'),
        'global_sufficient_power': str(SLABS[0][0]),
        'global_sufficient_power_decimal': '1.7725',
        'covered_power_interval': ['1.7725', '1.81'],
        'larger_power_input': 'POWER_THRESHOLD.md A-SP1, threshold 1.80206853774',
        'slabs': records,
        'all_real_endpoints_follow_from_manuscript': True,
        'critical_power_one_proved': False,
        'rh_proved': False,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
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
