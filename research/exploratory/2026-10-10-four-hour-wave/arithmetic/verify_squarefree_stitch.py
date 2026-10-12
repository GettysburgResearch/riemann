#!/usr/bin/env python3
"""Directed certificate for the squarefree SHARP finite-horizon/tail stitch.

Requires python-flint 0.9.0. See SQUAREFREE_STITCH.md for the analytic
contracts and the all-real endpoint/power implication. No RH claim.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import importlib.metadata
import json
from pathlib import Path

from flint import arb, ctx

from verify_horizon_stitch import as_arb, primes_through, removal_mass, require

SLABS = (
    (Q('1.737'), Q('1.7372'), 4640),
    (Q('1.7372'), Q('1.738'), 4680),
    (Q('1.738'), Q('1.7395'), 4700),
    (Q('1.7395'), Q('1.742'), 5000),
    (Q('1.742'), Q('1.747'), 5500),
    (Q('1.747'), Q('1.756'), 6500),
    (Q('1.756'), Q('1.773'), 8500),
)


def power_ball(low: Q, high: Q) -> arb:
    require(low <= high, 'power interval order')
    return arb(as_arb((low+high)/2), as_arb((high-low)/2))


def core_error(m: Q) -> Q:
    require(Q(3, 2) <= m < 2, 'core monotonicity domain')
    return Q(68, 67)*(3*m/(2*(2-m))+2/(m-1))


def slab_constants(low: Q, high: Q, horizon: int):
    m = power_ball(low, high)
    b = m/2
    require(bool(b > arb('0.5')) and bool(b < 1), 'squarefree prefix domain')
    zeta_b = b.zeta()
    zeta_2b = (2*b).zeta()
    require(bool(zeta_b < 0) and bool(zeta_2b > 0), 'zeta prefix sign')
    favorable = -3*m/4*(1+arb(67)**(-b))*zeta_b/zeta_2b
    low_favorable = favorable.lower()
    require(low_favorable.is_exact() and bool(low_favorable > 0),
            'directed positive lower favorable coefficient')
    inverse_root_floor = 1/(arb(horizon)/67).sqrt()
    prefix_error = (1+(1+inverse_root_floor)/(1-b)
                    + abs(zeta_b)*(1/(2*b-1)+inverse_root_floor)).upper()
    require(prefix_error.is_exact() and bool(prefix_error > 0),
            'directed prefix error upper bound')
    total_error = ((1+1/arb(67).sqrt())
                   *(3*as_arb(high)/4*prefix_error+4+2/as_arb(low))).upper()
    require(total_error.is_exact() and bool(total_error > 0),
            'directed total error upper bound')
    return favorable, low_favorable, prefix_error, total_error


def verify_slab(low: Q, high: Q, horizon: int, primes):
    require(Q(3, 2) <= low <= high < 2 and horizon >= 67, 'slab domain')
    removal = removal_mass(low, horizon, primes)
    require(bool(removal < 1), 'finite removal mass is not below one')
    favorable, low_favorable, prefix_error, total_error = slab_constants(low, high, horizon)
    a0 = as_arb((low+1)/2)
    b0 = as_arb(low/2)
    beta_series = (1-arb(67)**(-a0))/a0.zeta()
    require(bool(beta_series > 0), 'positive beta Dirichlet series')
    density = 1/arb(2).zeta()
    root = arb(horizon).sqrt()
    derivative_guard = (beta_series*as_arb((low-1)/2)*root
                        -low_favorable*(1-b0))
    require(bool(derivative_guard > 0), 'uniform tail derivative guard')
    tail_margin = (beta_series*arb(horizon)**as_arb((low-1)/2)
                   -density*as_arb(core_error(high))
                   +low_favorable*arb(horizon)**(b0-1)
                   -total_error/root)
    require(bool(tail_margin > 0), 'uniform squarefree tail inequality')
    active = [p for p in primes if p <= horizon]
    return {
        'power_interval': [str(low), str(high)],
        'horizon': horizon,
        'ordinary_prime_count': len(active),
        'prime_list_sha256': hashlib.sha256(
            (','.join(map(str, active))+'\n').encode('ascii')).hexdigest(),
        'duplicate_67_labels': 1,
        'finite_removal_mass_ball': str(removal),
        'one_minus_removal_mass_ball': str(1-removal),
        'favorable_coefficient_interval_ball': str(favorable),
        'directed_favorable_coefficient_lower': str(low_favorable),
        'directed_prefix_error_upper': str(prefix_error),
        'directed_total_error_upper': str(total_error),
        'tail_margin_ball': str(tail_margin),
        'tail_derivative_guard_ball': str(derivative_guard),
        'all_three_strict_entire_ball_guards_passed': True,
    }


def finite_squarefree_controls():
    limit = 1000
    squarefree = bytearray(b'\x01')*(limit+1)
    squarefree[0] = 0
    for p in primes_through(limit):
        p2 = p*p
        if p2 > limit:
            break
        for n in range(p2, limit+1, p2):
            squarefree[n] = 0
    density = 1/arb(2).zeta()
    count = 0
    for n in range(1, limit+1):
        count += squarefree[n]
        require(bool(abs(arb(count)-density*n) < 2*arb(n).sqrt()),
                'finite squarefree density control')
    require(count == 608, 'independent squarefree count at 1000')
    cases = 0
    for x in [67, 100, 1000]:
        for bq in [Q(3, 5), Q(4, 5), Q(9, 10)]:
            b = as_arb(bq)
            direct = sum((arb(n)**(-b) for n in range(1, x+1)
                          if squarefree[n]), arb(0))
            center = density/(1-b)*arb(x)**(1-b)+b.zeta()/(2*b).zeta()
            inverse_root = 1/arb(x).sqrt()
            coefficient = (1+(1+inverse_root)/(1-b)
                           +abs(b.zeta())*(1/(2*b-1)+inverse_root))
            require(bool(abs(direct-center) < coefficient*arb(x)**(arb('0.5')-b)),
                    'finite weighted squarefree prefix control')
            cases += 1
    return {'density_endpoints_checked': limit,
            'weighted_prefix_independent_direct_sum_cases': cases,
            'squarefree_count_at_1000': count}


def run():
    ctx.prec = 192
    controls = finite_squarefree_controls()
    primes = primes_through(max(x for _, _, x in SLABS))
    require(len(primes) == 1059 and primes[-1] == 8467, 'complete sieve control')
    reach = SLABS[0][0]
    for low, high, _ in SLABS:
        require(low <= reach, 'gap in power interval coverage')
        reach = max(reach, high)
    require(reach >= Q('1.7725'), 'prior threshold overlap')
    records = [verify_slab(*slab, primes) for slab in SLABS]
    return {
        'status': 'PASS_GLOBAL_SHARP_SQUAREFREE_STITCH',
        'arithmetic': 'ARB_DIRECTED_BALLS_AND_EXACT_RATIONAL_COEFFICIENTS',
        'precision_bits': ctx.prec,
        'python_flint_version': importlib.metadata.version('python-flint'),
        'global_sufficient_power': str(SLABS[0][0]),
        'global_sufficient_power_decimal': '1.737',
        'covered_power_interval': ['1.737', '1.773'],
        'larger_power_input': 'HORIZON_STITCH.md A-HS1, threshold 1.7725',
        'slabs': records,
        'independent_finite_controls': controls,
        'all_real_endpoints_follow_from_manuscript': True,
        'critical_power_one_proved': False,
        'rh_proved': False,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependency_sha256': hashlib.sha256(
            Path(__file__).with_name('verify_horizon_stitch.py').read_bytes()).hexdigest(),
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
