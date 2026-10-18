#!/usr/bin/env python3
"""Exact all-signed-source flux and Mellin integration-by-parts controls.

Finite parameters H=16,Y=256,D=4096 are deliberately explicit; a run
does not certify the asymptotic short-interval squarefree theorem or the
infinite Weyl/Sobolev estimate. Every native cell is tested.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json
import subprocess
import sys

import verify as v


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--report')
    p.add_argument('--mutation', default='none')
    p.add_argument('--mutations', action='store_true')
    args = p.parse_args()
    counts = Counter()

    def need(ok, name):
        counts[name] += 1
        if not ok:
            raise RuntimeError('REJECT:' + name)

    y, d0, h = 256, 4096, 16
    mu = v.mu_sieve(y)
    z = Counter()
    for a in range(1, y+1):
        for b in range(1, y+1):
            z[a*b] += mu[a]*mu[b]
    targets = {n:c for n,c in z.items() if d0 <= n < 2*d0 and c}
    for n,c in targets.items():
        direct = sum(v.mu_trial(a)*v.mu_trial(n//a) for a in v.divisors(n)
                     if a <= y and n//a <= y)
        need(c == direct, 'complete_signed_old_product')

    delta = defaultdict(F)
    mass = F(0)
    gap = 0
    shared = 0
    minimum_good = h
    reference_pairs = set()
    for n,c in sorted(targets.items()):
        r = isqrt(n)
        t = (r+1)*(r+2)-n
        k0 = 0
        while (k0+1)*(k0+2) <= t:
            k0 += 1
        refs = [(r+1-k, r+2+k) for k in range(k0,k0+h)
                if mu[r+1-k]*mu[r+2+k]]
        need(bool(refs), 'finite_squarefree_reference_exists')
        minimum_good = min(minimum_good, len(refs))
        alpha = F(c,n)
        mass += abs(alpha)
        delta[n] += alpha
        for a,b in refs:
            need(1 <= a < b <= y, 'actual_squarefree_old_inputs')
            need(mu[a]*mu[b] != 0, 'nonzero_actual_input_sign')
            gap = max(gap,abs(a*b-n))
            reference_pairs.add((a,b))
            shared += int(__import__('math').gcd(a,b) > 1)
            divisor = len(refs)+(args.mutation == 'wrong_probability')
            delta[a*b] -= alpha/divisor
    delta = {n:c for n,c in delta.items() if c}
    need(sum(delta.values(),F(0)) == 0, 'exact_zero_total_transport_mass')
    need(any(c > 0 for c in targets.values()) and
         any(c < 0 for c in targets.values()), 'signed_target_fixture')
    need(shared > 0, 'shared_reference_primes_retained')

    lo, hi = min(delta), max(delta)
    flux = [F(0)]*(hi+1)
    current = F(0)
    for n in range(hi+1):
        current += delta.get(n, F(0))
        flux[n] = -current if args.mutation == 'wrong_flux_sign' else current
    need(flux[-1] == 0, 'compact_flux_right_endpoint')
    variation = sum((abs(c) for c in delta.values()), F(0))
    need(variation <= 2*mass, 'absolute_flux_variation_resource')
    sup = max(map(abs,flux))
    maxz = max(map(abs,targets.values()))
    need(sup <= F(maxz*(2*gap+2),d0), 'integer_localization_sup_resource')
    norm2 = sum((a*a for a in flux),F(0))
    need(norm2 <= (hi-lo)*sup*sup, 'complete_compact_flux_energy_resource')

    # Exact independent Mellin normalization: integer moments and log moment.
    for power in (1,2,3,-1):
        measure = sum((c*F(n)**power for n,c in delta.items()),F(0))
        integral = sum((flux[n]*(F(n+1)**power-F(n)**power)/power
                        for n in range(lo,hi)), F(0))
        need(measure == -power*integral, 'exact_mellin_derivative_sign_and_power')
    logs = sum((v.log_int(n)*c for n,c in delta.items()),v.Linear())
    primitive_logs = sum(((v.log_int(n+1)-v.log_int(n))*flux[n]
                          for n in range(lo,hi)),v.Linear())
    need(logs == -primitive_logs, 'formal_log_moment_integration_by_parts')

    # Producer: every full harmonic jump. Consumer: complete cumulative flux
    # at all rational arguments k/j; integrality makes floor(k/j) exact.
    end = (y+1)**2
    events = defaultdict(F)
    for n,c in delta.items():
        maximum = (end-1)//n
        if args.mutation == 'truncate_harmonic_jumps':
            maximum = max(0,maximum-1)
        for j in range(1,maximum+1):
            events[j*n] += c/j
    harmonic = F(0)
    for k in range(1,end):
        harmonic += events.get(k,F(0))
        if k <= y:
            continue
        replay = F(0)
        for j in range(1,k//lo+1):
            u = k//j
            if u < len(flux):
                replay += flux[u]/j
        need(harmonic == replay, 'every_native_cell_flux_kernel_identity')
    report = {
        'status':'PASS', 'arithmetic':'EXACT_RATIONAL_AND_FORMAL_PRIME_LOGS',
        'Y':y, 'product_block':[d0,2*d0], 'finite_H':h,
        'targets':len(targets), 'negative_targets':sum(c < 0 for c in targets.values()),
        'reference_pairs':len(reference_pairs), 'shared_reference_edges':shared,
        'minimum_good_references':minimum_good, 'actual_max_gap':gap,
        'complete_native_cells':end-y-1,
        'total_checks_including_guards':sum(counts.values()), 'gates':dict(counts),
        'not_certified':['unbounded squarefree density','Weyl bound proof',
                         'infinite fractional Sobolev bound','complete balanced contraction','RH']}
    if args.mutations:
        report['mutations'] = []
        for mutation in ('wrong_probability','wrong_flux_sign','truncate_harmonic_jumps'):
            out = subprocess.run([sys.executable,__file__,'--mutation',mutation],
                                 text=True,capture_output=True)
            need(out.returncode != 0 and 'REJECT:' in out.stderr,
                 'negative_control_rejected')
            report['mutations'].append({'mutation':mutation,'status':'REJECTED',
                'gate':out.stderr.split('REJECT:')[-1].splitlines()[0]})
    if args.report:
        Path(args.report).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
