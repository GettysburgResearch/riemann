#!/usr/bin/env python3
"""Exact finite sextic moments; sharp test, nu=1, S consists of primes over 6.

This is a finite arithmetic experiment, not a smooth all-scale moment theorem.
The residue-field conventions agree with PR914's check_local_structure.py at
0cc0428fedbbfc340044c7451b3d392c1da9a103. The computation here independently
builds every squarefree ideal and every row in the requested norm ball.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path

ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
UNITS = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))


def need(ok, message):
    if not ok:
        raise ArithmeticError(message)


def mul(x, y, modulus=None):
    a, b = x
    c, d = y
    result = (a*c-b*d, a*d+b*c-b*d)
    return result if modulus is None else tuple(t % modulus for t in result)


def ring_power(x, exponent, modulus=None):
    out = (1, 0)
    while exponent:
        if exponent & 1:
            out = mul(out, x, modulus)
        x = mul(x, x, modulus)
        exponent //= 2
    return out


def norm(x):
    a, b = x
    return a*a-a*b+b*b


def complex_square(x):
    """Square in the epsilon=zeta6 basis, epsilon²=epsilon-1."""
    a, b = x
    return a*a-b*b, 2*a*b+b*b


def complex_norm(x):
    a, b = x
    return a*a+a*b+b*b


def rows(height):
    cap = isqrt(4*height//3)+2
    return [(a, b) for a in range(-cap, cap+1) for b in range(-cap, cap+1)
            if 0 < norm((a, b)) <= height]


def primes(limit):
    sieve = bytearray(b'\x01')*(limit+1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit)+1):
        if sieve[p]:
            sieve[p*p::p] = b'\x00'*((limit-p*p)//p+1)
    return [p for p in range(5, limit+1) if sieve[p]]


def prime_ideals(limit):
    result = []
    for p in primes(limit):
        if p % 3 == 1:
            roots = [r for r in range(p) if (r*r+r+1) % p == 0]
            need(len(roots) == 2, 'both split prime ideals retained')
            result.extend((p, p, r) for r in roots)
        elif p*p <= limit:
            result.append((p*p, p, None))
    return sorted(result, key=lambda q: (q[0], -1 if q[2] is None else q[2]))


def symbol(prime, row):
    order, p, root = prime
    a, b = row
    if root is None:
        residue = a % p, b % p
        if residue == (0, 0):
            return -1
        value = ring_power(residue, (order-1)//6, p)
        roots = [(x % p, y % p) for x, y in UNITS]
    else:
        residue = (a+root*b) % p
        if residue == 0:
            return -1
        value = pow(residue, (order-1)//6, p)
        roots = [(x+root*y) % p for x, y in UNITS]
    need(value in roots, 'sextic Euler residue belongs to mu6')
    return roots.index(value)


def columns(ideals, scale):
    result = []
    def visit(start, size, factors):
        if scale//2 < size <= scale:
            result.append((size, (-1)**len(factors), factors))
        for index in range(start, len(ideals)):
            new_size = size*ideals[index][0]
            if new_size > scale:
                break
            visit(index+1, new_size, factors+(index,))
    visit(0, 1, ())
    return result


def summarize(values, max_k):
    count = len(values)
    need(count > 0, 'nonempty complete row sample')
    mean = tuple(F(sum(v[j] for v in values), count) for j in range(2))
    centered = [(v[0]-mean[0], v[1]-mean[1]) for v in values]
    variance = sum((complex_norm(v) for v in centered), F(0))/count
    pseudo = tuple(sum((complex_square(v)[j] for v in centered), F(0))/count
                   for j in range(2))
    centered_fourth = sum((complex_norm(v)**2 for v in centered), F(0))/count
    cumulant = centered_fourth-2*variance**2-complex_norm(pseudo)
    powers = [sum(complex_norm(v)**k for v in values) for k in range(1, max_k+1)]
    return {'rows': count, 'exact_moments_2k': powers,
            'mean_epsilon_coordinates': [str(v) for v in mean],
            'centered_variance': str(variance),
            'centered_pseudovariance': [str(v) for v in pseudo],
            'centered_fourth_moment': str(centered_fourth),
            'fourth_connected_cumulant': str(cumulant),
            'fourth_cumulant_sign': (cumulant > 0)-(cumulant < 0),
            'maximum_row_squared_modulus': max(complex_norm(v) for v in values)}


def panel(scale, height, max_k):
    ideals = prime_ideals(scale)
    cols = columns(ideals, scale)
    all_rows = rows(height)
    signed, positive = [], []
    for row in all_rows:
        local = [symbol(q, row) for q in ideals]
        sa = sb = pa = pb = 0
        for _, mu, indices in cols:
            if any(local[j] < 0 for j in indices):
                continue
            x, y = ROOTS[sum(local[j] for j in indices) % 6]
            sa += mu*x
            sb += mu*y
            pa += x
            pb += y
        signed.append((sa, sb))
        positive.append((pa, pb))
    base_cap = isqrt(4*isqrt(isqrt(height))//3)+3
    sixth = set()
    for a in range(-base_cap, base_cap+1):
        for b in range(-base_cap, base_cap+1):
            base = (a, b)
            if 0 < norm(base)**6 <= height:
                sixth.add(ring_power(base, 6))
    need(sixth <= set(all_rows), 'all sixth-power replicas occur in the complete ball')
    signed_report = summarize(signed, max_k)
    positive_report = summarize(positive, max_k)
    selected = [value for row, value in zip(all_rows, signed) if row in sixth]
    sixth_report = summarize(selected, max_k)
    normalized = [str(F(moment, len(all_rows)*scale**k))
                  for k, moment in enumerate(signed_report['exact_moments_2k'], start=1)]
    return {'D': scale, 'H': height, 'prime_ideals': len(ideals),
            'squarefree_columns': len(cols), 'signed_source': signed_report,
            'positive_coefficient_comparison': positive_report,
            'exact_sixth_power_rows': sorted(sixth), 'sixth_power_source': sixth_report,
            'signed_moment_over_rows_D_power': normalized,
            'fourth_signed_over_positive': str(F(signed_report['exact_moments_2k'][1],
                                                 positive_report['exact_moments_2k'][1]))}


def controls():
    for p, root in [(7, 2), (7, 4), (13, 3), (13, 9)]:
        prime = p, p, root
        for a in range(p):
            for b in range(p):
                row = a, b
                j = symbol(prime, row)
                for unit in UNITS:
                    ju = symbol(prime, unit)
                    product = symbol(prime, mul(row, unit))
                    need(product == (-1 if j < 0 else (j+ju) % 6),
                         'actual split-field multiplicativity including local zero')
    for p in (5, 11):
        prime = p*p, p, None
        for a in range(p):
            for b in range(p):
                row = a, b
                j = symbol(prime, row)
                need(symbol(prime, ring_power(row, 6)) == (-1 if j < 0 else 0),
                     'actual inert-field sixth power retains zero mask')
    need(summarize([(0, 0), (1, 0)], 2)['fourth_connected_cumulant'] == '-1/8',
         'independent centered Bernoulli cumulant control')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scales', nargs='+', type=int, default=[16, 32, 64, 128, 256, 512])
    parser.add_argument('--k', type=int, default=4)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    need(args.k >= 2 and all(d >= 2 for d in args.scales), 'valid experiment parameters')
    controls()
    records = []
    for d in args.scales:
        record = panel(d, d, args.k)
        records.append(record)
        print('EXACT_SEXTIC_PANEL', d, 'columns', record['squarefree_columns'],
              'rows', record['signed_source']['rows'], 'cumulant_sign',
              record['signed_source']['fourth_cumulant_sign'], flush=True)
    result = {'status': 'PASS_EXACT_FINITE_SEXTIC_EXPERIMENT',
              'scope': 'nu=1, fixed excluded primes over6, sharp column D/2<Nn<=D, full sharp row ball Nu<=D',
              'arithmetic': 'integer mu6 coordinates and rational centered moments',
              'panels': records, 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'reference_pr': 914, 'reference_commit': '0cc0428fedbbfc340044c7451b3d392c1da9a103',
              'smooth_all_scale_moment_proved': False, 'rh_proved': False}
    content = json.dumps(result, sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end='')


if __name__ == '__main__':
    main()
