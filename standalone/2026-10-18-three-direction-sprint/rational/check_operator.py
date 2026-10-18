#!/usr/bin/env python3
"""Exact Dirichlet-polynomial replay of the rejected global filter approach."""
import argparse
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path

import verify as v


COUNTS = Counter()


def need(ok, gate):
    COUNTS[gate] += 1
    if not ok:
        raise RuntimeError('REJECT:' + gate)


def add(a, b, scalar=F(1)):
    out = a.copy()
    for n, value in b.items():
        out[n] = out.get(n, F(0)) + scalar * value
        if not out[n]:
            del out[n]
    return out


def multiply(a, b):
    out = {}
    for n, x in a.items():
        for m, y in b.items():
            out[n*m] = out.get(n*m, F(0)) + x*y
    return {n: x for n, x in out.items() if x}


def source_incidence(c, p):
    out = {}
    for q, value in c.items():
        if q % p:
            continue
        for d in v.divisors(q):
            out[d] = out.get(d, F(0)) + value * v.mu_trial(q//d)
    return {n: x for n, x in out.items() if x}


def canonical(poly, q):
    return sum((value for n, value in poly.items() if n % q == 0), F(0))


def run():
    rows = []
    for y in (24, 32, 48, 64, 96):
        _, c = v.source(y)
        primes = [p for p in range(2, y+1) if v.factors(p) == ((p, 1),)]
        top = [p for p in primes if 2*p > y]
        middle = [p for p in primes if 3*p > y >= 2*p]
        py = {n: F(v.mu_trial(n), n) for n in range(1, y+1) if v.mu_trial(n)}
        h1, square, atop = {}, {}, {}
        for p in top:
            lp = {p: F(1, p), 1: F(-1, p)}
            h1 = add(h1, lp)
            square = add(square, multiply(lp, lp))
            literal = source_incidence(c, p)
            expected = add(multiply(lp, py), multiply(lp, lp), F(1, 2))
            expected = {n: -2*x for n, x in expected.items()}
            need(literal == expected, 'literal_top_incidence_polynomial')
            atop = add(atop, literal)
        for p0 in middle:
            p2 = {1: F(1), 2: F(-1, 2)}
            l0 = multiply({p0: F(1, p0), 1: F(-1, p0)}, p2)
            a0 = source_incidence(c, p0)
            need(a0 == add({n: -2*x for n, x in multiply(l0, py).items()},
                           multiply(l0, l0), F(-1)), 'literal_middle_incidence_polynomial')
            known = add(multiply(h1, l0), square, F(-1))
            cleared = add(multiply(l0, atop), multiply(h1, a0), F(-1))
            need(cleared == multiply(l0, known), 'cleared_global_filter_identity')
            filtered_middle = add(multiply(h1, py), multiply(h1, l0), F(1, 2))
            filtered_middle = {n: 2*x for n, x in filtered_middle.items()}
            need(add(atop, filtered_middle) == known, 'finite_filtered_middle_identity')
            for i, p in enumerate(top):
                for ell in top[i+1:]:
                    q = p*ell
                    need(canonical(atop, q) == F(4, q), 'unfiltered_target_response')
                    need(canonical(filtered_middle, q) == F(-4, q), 'filtered_target_cancellation')
                    need(canonical(known, q) == 0, 'global_target_response_zero')
            rows.append({'Y': y, 'middle_prime': p0, 'top_prime_count': len(top),
                         'surviving_dilation_count': len(known)})
    return {'status': 'PASS', 'arithmetic': 'EXACT_RATIONAL_DIRICHLET_POLYNOMIALS',
            'cases': rows, 'checks_by_gate': dict(sorted(COUNTS.items())),
            'total_checks_including_guards': sum(COUNTS.values()),
            'claim': 'The global filtered cancellation is exact and has zero response on every distinct top-prime pair.',
            'not_checked': ['operator series convergence', 'asymptotic PNT norm bound', 'RH']}


def main():
    a = argparse.ArgumentParser()
    a.add_argument('--report', type=Path)
    z = a.parse_args()
    report = run()
    encoded = json.dumps(report, sort_keys=True, indent=2) + '\n'
    if z.report:
        z.report.write_text(encoded, encoding='utf-8', newline='\n')
    print(encoded, end='')


if __name__ == '__main__':
    main()
