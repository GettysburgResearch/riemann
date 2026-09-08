#!/usr/bin/env python3
"""Six directed endpoint signs, NOT a complete zero census.

Requires mpmath==1.3.0. The interval Gamma implementation is an explicit
software trust dependency. No non-directed special-function acceptance.
The Euler-transformed eta tail is bounded analytically by 2**(-127)
and enclosed in a rectangle of half-width 2**(-120).
"""
from fractions import Fraction
from math import comb
from pathlib import Path
import argparse
import json
import mpmath
from mpmath import iv

POINTS = ((14, 1), (15, -1), (21, -1), (22, 1), (25, 1), (26, -1))
TERMS = 192
PRECISION = 80


def rational_mpf(x):
    sign, man, exp, _ = x
    q = Fraction((-1 if sign else 1) * man)
    return str(q * 2**exp if exp >= 0 else q / 2**(-exp))


def result():
    if mpmath.__version__ != '1.3.0':
        raise RuntimeError('Requires mpmath==1.3.0')
    if not (Fraction(26*22, 2*7) < 41 and 3**41 < 2**65):
        raise ArithmeticError('Exact analytic tail budget failed')
    iv.dps = PRECISION
    weights = [sum((Fraction(comb(k, n-1), 2**(k+1))
                    for k in range(n-1, TERMS)), Fraction())
               for n in range(1, TERMS+1)]
    logs = [iv.log(n) for n in range(1, TERMS+1)]
    enclosures = []
    for t, sign in POINTS:
        s = iv.mpc(iv.mpf(1)/2, t)
        eta = iv.mpc(0)
        for n, (weight, logn) in enumerate(zip(weights, logs), start=1):
            w = iv.mpf(weight.numerator)/weight.denominator
            eta += (-1)**(n-1)*w*iv.exp(-s*logn)
        eps = iv.mpf(1)/2**120
        box = iv.mpf([-eps, eps])
        zeta = (eta+iv.mpc(box, box))/(1-iv.exp((1-s)*iv.log(2)))
        xi = s*(s-1)*iv.exp(-s/2*iv.log(iv.pi))*iv.gamma(s/2)*zeta/2
        if not xi.imag.a <= 0 <= xi.imag.b:
            raise ArithmeticError('Reality enclosure failed')
        if not (xi.real.a > 0 if sign == 1 else xi.real.b < 0):
            raise ArithmeticError(f'Endpoint sign failed at {t}')
        enclosures.append({'t': t, 'sign': sign,
            'real_bounds': [rational_mpf(v) for v in xi.real._mpi_],
            'imag_bounds': [rational_mpf(v) for v in xi.imag._mpi_]})
    return {'status': 'PASS_SIX_DIRECTED_ENDPOINT_SIGNS',
            'mpmath_version': mpmath.__version__, 'decimal_precision': PRECISION,
            'eta_terms': TERMS, 'tail_bound': '1/'+str(2**127),
            'error_box_half_width': '1/'+str(2**120),
            'intervals_with_at_least_one_line_zero': [[14,15], [21,22], [25,26]],
            'complete_zero_census': False, 'rh_proved': False,
            'gamma_interval_implementation_trusted': True,
            'enclosures': enclosures}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', type=Path)
    args = parser.parse_args()
    actual = result()
    if args.check:
        expected = args.check.read_text()
        # Canonical text comparison rejects floats, bool/int aliases and duplicate keys.
        if expected != json.dumps(actual, indent=2, sort_keys=True)+'\n':
            raise SystemExit('Saved endpoint record differs from fresh reconstruction')
    print(json.dumps(actual, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
