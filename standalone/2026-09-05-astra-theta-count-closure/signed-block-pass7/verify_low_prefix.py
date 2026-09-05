#!/usr/bin/env python3
"""Six directed interval Xi signs, not a complete zero census.
mpmath 1.3.0 interval gamma is an explicit software trust dependency.
The analytic Euler-eta tail is strictly below the rational 2**(-120).
No ordinary floating point value is used for acceptance.
"""
from fractions import Fraction as F
from math import comb
import argparse
import json
from pathlib import Path
import mpmath
from mpmath import iv


def fail_unless(ok, message):
    if not ok:
        raise ArithmeticError(message)


def strict_load(path):
    def pairs(items):
        d = {}
        for k, v in items:
            if k in d:
                raise ValueError('duplicate JSON key')
            d[k] = v
        return d
    return json.loads(Path(path).read_text(), object_pairs_hook=pairs)


def encoded(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), allow_nan=False)


def compute():
    fail_unless(mpmath.__version__ == '1.3.0', 'requires mpmath 1.3.0')
    fail_unless(F(26*22, 14) < 41 and 3**41 < 2**66, 'tail constant')
    # Integral Euler transform remainder: sqrt(cosh(pi*t))*2**(-192)
    # < 3**41 * 2**(-192) < 2**(-126) < 2**(-120).
    iv.dps = 80
    n_terms = 192
    coeff = [sum((F(comb(k, n-1), 2**(k+1))
                  for k in range(n-1, n_terms)), F(0))
             for n in range(1, n_terms+1)]
    weights = [iv.mpf(c.numerator)/c.denominator for c in coeff]
    logs = [iv.log(n) for n in range(1, n_terms+1)]
    records = []
    signs = {14: 1, 15: -1, 21: -1, 22: 1, 25: 1, 26: -1}
    for t, sign in signs.items():
        s = iv.mpc(iv.mpf(1)/2, t)
        eta = sum(((-1)**n * weights[n] * iv.exp(-s*logs[n])
                   for n in range(n_terms)), iv.mpc(0))
        eps = iv.mpf(1)/2**120
        error = iv.mpc(iv.mpf([-eps, eps]), iv.mpf([-eps, eps]))
        zeta = (eta+error)/(1-iv.exp((1-s)*iv.log(2)))
        xi = s*(s-1)*iv.exp(-s*iv.log(iv.pi)/2)*iv.gamma(s/2)*zeta/2
        fail_unless(xi.imag.a <= 0 <= xi.imag.b, 'conjugation enclosure')
        fail_unless(xi.real.a > 0 if sign > 0 else xi.real.b < 0,
                    'endpoint sign not certified')
        records.append({'t': t, 'sign': sign, 'real': str(xi.real),
                        'imaginary': str(xi.imag)})
    return {'status': 'PASS_SIX_DIRECTED_ENDPOINT_SIGNS',
            'arithmetic': 'DIRECTED_INTERVAL_WITH_EXACT_ANALYTIC_TAIL',
            'mpmath': mpmath.__version__, 'decimal_precision': 80,
            'eta_terms': n_terms, 'tail_radius': '1/'+str(2**120),
            'interval_gamma_trust_dependency': True,
            'intervals_with_a_line_zero': [[14,15],[21,22],[25,26]],
            'complete_census': False, 'simplicity_proved': False,
            'rh_proved': False, 'enclosures': records}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--check', type=Path)
    args = p.parse_args()
    result = compute()
    if args.check:
        fail_unless(encoded(strict_load(args.check)) == encoded(result),
                    'saved result differs in value or numeric type')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
