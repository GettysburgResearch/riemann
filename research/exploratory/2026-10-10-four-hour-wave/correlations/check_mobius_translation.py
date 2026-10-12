#!/usr/bin/env python3
"""Exact actual CRT translation; no infinite moment estimate is checked."""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
from itertools import combinations
import json
from pathlib import Path
from probe_sextic_cumulants import ROOTS, complex_norm, need, symbol


def polynomial(u, coefficients, translator=False):
    local = [symbol((7, 7, 2), (u, 0)), symbol((13, 13, 3), (u, 0))]
    a = b = 0
    for support, coefficient in coefficients:
        if any(local[j] < 0 for j in support):
            continue
        x, y = ROOTS[sum(local[j] for j in support) % 6]
        factor = (-1)**len(support) if translator else 1
        a += factor*coefficient*x
        b += factor*coefficient*y
    return a, b


def run():
    candidates = [u for u in range(91)
                  if symbol((7, 7, 2), (u, 0)) == 3 and
                     symbol((13, 13, 3), (u, 0)) == 3]
    need(candidates, 'actual CRT translator exists')
    t = candidates[0]
    need(len({t*u % 91 for u in range(91)}) == 91, 'translator is a permutation')
    supports = [s for r in range(3) for s in combinations(range(2), r)]
    profiles = [[(s, (-1)**j*(j+1)*(profile+1)+profile*j*j)
                 for j, s in enumerate(supports)] for profile in range(5)]
    checks = 0
    moments = []
    for profile in profiles:
        signed, unsigned = [], []
        for u in range(91):
            a = polynomial(u, profile, True)
            c = polynomial(t*u % 91, profile)
            need(a == c, 'literal joint-profile identity including local zeros')
            checks += 1
            signed.append(complex_norm(a))
            unsigned.append(complex_norm(polynomial(u, profile)))
        need(sorted(signed) == sorted(unsigned), 'complete exact distribution identity')
        checks += 1
        record = []
        for k in range(1, 9):
            left, right = sum(v**k for v in signed), sum(v**k for v in unsigned)
            need(left == right, 'complete 2k-th moment identity')
            checks += 1
            record.append({'k': k, 'unnormalized_exact_moment': left})
        moments.append(record)
    profile = profiles[0]
    weighted = [((u*u+3*u+1) % 17) for u in range(91)]
    inverse = pow(t, -1, 91)
    left = sum(weighted[u]*complex_norm(polynomial(u, profile, True))**2 for u in range(91))
    right = sum(weighted[inverse*v % 91]*complex_norm(polynomial(v, profile))**2 for v in range(91))
    need(left == right, 'exact nonuniform-measure transport')
    checks += 1
    return {'status': 'PASS_EXACT_MOBIUS_CRT_TRANSLATION', 'checks': checks,
            'prime_ideal_norms': [7, 13], 'modulus_norm': 91,
            'translator': t, 'translator_inverse': inverse,
            'profiles': len(profiles), 'moments': moments,
            'weighted_fourth_moment_transport': left,
            'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'helper_sha256': hashlib.sha256(Path(__file__).with_name('probe_sextic_cumulants.py').read_bytes()).hexdigest(),
            'analytic_infinite_CRT_or_moment_proof_checked': False,
            'short_row_moment_proved': False, 'rh_proved': False}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    content = json.dumps(run(), sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end='')


if __name__ == '__main__':
    main()
