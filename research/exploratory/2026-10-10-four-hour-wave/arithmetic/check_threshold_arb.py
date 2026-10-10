#!/usr/bin/env python3
"""Independent Arb arithmetic replay of the labelled-prime bracket.

Requires python-flint. Arb's special-function algorithms are independent of
the rational Euler--Maclaurin implementation in verify_power_threshold.py.
The infinite prime-zeta tail uses the explicit bound P10 in the manuscript.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import importlib.metadata
import json
from pathlib import Path

from flint import arb, ctx


def mobius_sieve(limit: int):
    values = [1]*(limit+1)
    prime = [True]*(limit+1)
    for p in range(2, limit+1):
        if not prime[p]:
            continue
        for multiple in range(p, limit+1, p):
            values[multiple] *= -1
            if multiple > p:
                prime[multiple] = False
        for multiple in range(p*p, limit+1, p*p):
            values[multiple] = 0
    return values


def run():
    ctx.prec = 192
    cutoff = 40
    mu = mobius_sieve(cutoff)
    records = []
    for text in ('1.40103426886', '1.40103426887'):
        q = Q(text)
        s = arb(q.numerator)/q.denominator
        mass = sum((mu[k]*(k*s).zeta().log()/k for k in range(1, cutoff+1)), arb(0))
        tail = arb(2)**(-(cutoff+1)*s)/(cutoff+1)
        tail *= (1+2/((cutoff+1)*s-1))/(1-arb(2)**(-s))
        mass += arb(0, tail.upper())+arb(67)**(-s)
        above, below = bool(mass > 1), bool(mass < 1)
        if text.endswith('86') and not above:
            raise ValueError('Arb lower endpoint not proved above one')
        if text.endswith('87') and not below:
            raise ValueError('Arb upper endpoint not proved below one')
        records.append({'alpha': text, 'mass_ball': str(mass),
                        'mass_minus_one_ball': str(mass-1),
                        'entire_ball_above_one': above,
                        'entire_ball_below_one': below})
    return {
        'status': 'PASS_INDEPENDENT_ARB_THRESHOLD_BRACKET',
        'arithmetic': 'ARB_DIRECTED_BALLS',
        'python_flint_version': importlib.metadata.version('python-flint'),
        'precision_bits': ctx.prec,
        'prime_series_cutoff': cutoff,
        'records': records,
        'critical_power_one_proved': False,
        'rh_proved': False,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
