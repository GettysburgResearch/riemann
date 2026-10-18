"""Exact monoid controls for SQUAREFREE_COLUMN_ADAPTER.md.

Integer ideals form a fixture monoid only: no sextic-symbol or asymptotic
mean claim is made. Complete coefficient equality implies equality for
every multiplicative character, including its nonunit zero extensions.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path
import hashlib
import json
import subprocess
import sys

COUNTS = Counter()
MUTATION = 'none'


def need(ok, gate):
    COUNTS[gate] += 1
    if not ok:
        raise RuntimeError('REJECT: ' + gate)


def mu(n):
    sign, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def weight(n, scale):
    x = F(n, scale)
    return (x-F(1, 2))**2*(1-x)**2 if F(1, 2) < x < 1 else F(0)


def clean(c):
    return {n: a for n, a in c.items() if a}


def direct(d, n):
    out = Counter()
    for a in range(1, d+1):
        for b in range(1, n+1):
            out[a*b] += mu(a)*weight(a, d)*weight(b, n)
    return clean(out)


def adapted(d, n):
    out = Counter()
    shared_h = 0
    for g in range(1, min(d, n)+1):
        if not mu(g):
            continue
        for h in range(1, isqrt(n//g)+1):
            for a in range(1, d//g+1):
                if not mu(a):
                    continue
                if MUTATION != 'drop_input_mask' and gcd(a, g) != 1:
                    continue
                for b in range(1, n//(g*h*h)+1):
                    if not mu(b) or gcd(a, b) != 1:
                        continue
                    if MUTATION != 'drop_input_mask' and gcd(b, g) != 1:
                        continue
                    w = mu(g)*mu(a)*weight(g*a, d)*weight(g*h*h*b, n)
                    if not w:
                        continue
                    if gcd(h, a*b) != 1:
                        shared_h += 1
                    if MUTATION == 'impose_h_coprime' and gcd(h, a*b) != 1:
                        continue
                    product = a*b if MUTATION == 'drop_row_power' else (g*h)**2*a*b
                    out[product] += w
                    need(F(d, g)*F(n, g*h*h)*(g*h)**2 == d*n,
                         'central_normalization')
                    need(mu(g*a) == mu(g)*mu(a) or MUTATION == 'drop_input_mask',
                         'mobius_factorization')
    return clean(out), shared_h


def b_direct(d, n, q):
    out = Counter()
    for a in range(1, d+1):
        for b in range(1, n+1):
            if mu(a) and mu(b) and gcd(a, b) == gcd(a*b, q) == 1:
                out[a*b] += mu(a)*weight(a, d)*weight(b, n)
    return clean(out)


def b_projected(d, n, q):
    out = Counter()
    for ell in range(1, min(d, n)+1):
        if not mu(ell) or gcd(ell, q) != 1:
            continue
        for a in range(1, d//ell+1):
            for b in range(1, n//ell+1):
                if not mu(a) or not mu(b) or gcd(a*b, q*ell) != 1:
                    continue
                coefficient = mu(a)
                if MUTATION == 'extra_mu_ell':
                    coefficient *= mu(ell)
                out[ell*ell*a*b] += coefficient*weight(ell*a, d)*weight(ell*b, n)
    return clean(out)


def q_smooth(n, q):
    while n > 1:
        g = gcd(n, q)
        if g == 1:
            return False
        n //= g
    return True


def run():
    shared = 0
    dig = hashlib.sha256()
    for d, n in ((24, 12), (40, 20), (64, 64), (128, 32)):
        old = direct(d, n)
        new, hits = adapted(d, n)
        shared += hits
        need(old == new, 'complete_old_product_polynomial')
        for a in sorted(old):
            need(1 <= a <= d*n, 'all_product_support')
            dig.update(f'{d},{n},{a},{old[a]}\n'.encode())
    need(shared > 0, 'genuine_h_shared_with_new_column')
    for d, n, q in ((24, 12, 1), (40, 20, 6), (64, 32, 5), (128, 32, 14)):
        need(b_direct(d, n, q) == b_projected(d, n, q),
             'positive_gcd_projector_coefficient')
    for q in (1, 2, 6, 30, 77):
        for n in range(1, 257):
            convolution = sum(mu(n//r) for r in range(1, n+1)
                              if n % r == 0 and q_smooth(r, q))
            need(convolution == mu(n)*(gcd(n, q) == 1),
                 'masked_inverse_euler_identity')
    return {'status': 'PASS', 'arithmetic': 'EXACT_RATIONAL_POLYNOMIALS',
            'shared_h_fixtures': shared, 'source_digest': dig.hexdigest(),
            'guards': dict(sorted(COUNTS.items())),
            'total_guards': sum(COUNTS.values()),
            'not_proved': ['asymptotic inverse moment input',
                           'full coherent mixed bound', 'RH']}


def main():
    global MUTATION
    a = argparse.ArgumentParser()
    modes = ('extra_mu_ell', 'impose_h_coprime', 'drop_row_power', 'drop_input_mask')
    a.add_argument('--mutation', choices=('none',)+modes, default='none')
    a.add_argument('--mutations', action='store_true')
    a.add_argument('--report', type=Path)
    args = a.parse_args()
    MUTATION = args.mutation
    report = run()
    if args.mutations:
        report['mutations'] = []
        for mode in modes:
            result = subprocess.run([sys.executable, '-B', '-O', __file__,
                                     '--mutation', mode], capture_output=True, text=True)
            need(result.returncode != 0 and 'REJECT:' in result.stderr,
                 'negative_control_rejected')
            report['mutations'].append({'mutation': mode, 'status': 'REJECTED',
                'gate': result.stderr.rsplit('REJECT:', 1)[-1].splitlines()[0].strip()})
    report['guards'] = dict(sorted(COUNTS.items()))
    report['total_guards'] = sum(COUNTS.values())
    if args.report:
        args.report.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
