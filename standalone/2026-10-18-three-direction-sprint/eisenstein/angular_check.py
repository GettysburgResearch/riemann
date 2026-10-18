"""Complete directed cube-vector overlap, from primary lattice generators.

All omitted c and n ideals are covered by explicit analytic Gaussian tails.
These finite fixtures do not prove an asymptotic rate or a transform bound.
"""
from __future__ import annotations

import argparse
from array import array
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path
import sys

private = Path(__file__).with_name('_packages')
if private.is_dir():
    sys.path.insert(0, str(private))
from flint import arb, ctx
import flint
from verify import require, hnf_ideals, norm, hnf_mobius, prime_ideals


def smallest_primes(cap):
    spf = array('I', range(cap+1))
    for p in range(2, isqrt(cap)+1):
        if spf[p] == p:
            for n in range(p*p, cap+1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def ideal_squarefree(a, b, n, spf):
    while n > 1:
        p = spf[n]
        n //= p
        e = 1
        while n % p == 0:
            n //= p
            e += 1
        if p % 3 == 2:
            if e != 2:
                return False
        elif e > 2 or (e == 2 and (a % p or b % p)):
            return False
    return True


def primitives(cap, n_cap):
    spf = smallest_primes(cap)
    sf_count = array('i', [0])*(cap+1)
    sf_real = array('i', [0])*(cap+1)
    sf_omega = array('i', [0])*(cap+1)
    all_count = array('i', [0])*(n_cap+1)
    all_cube_real = array('q', [0])*(n_cap+1)
    all_cube_omega = array('q', [0])*(n_cap+1)
    bound = isqrt(2*cap)
    total, squarefree = 0, 0
    for b in range(-bound, bound+1):
        if b % 3:
            continue
        for a in range(-bound, bound+1):
            if (a-1) % 3:
                continue
            n = a*a-a*b+b*b
            if not (0 < n <= cap) or gcd(n, 6) != 1:
                continue
            total += 1
            if n <= n_cap:
                all_count[n] += 1
                all_cube_real[n] += a*a*a-3*a*b*b+b*b*b
                all_cube_omega[n] += 3*a*b*(a-b)
            if ideal_squarefree(a, b, n, spf):
                squarefree += 1
                sf_count[n] += 1
                sf_real[n] += a
                sf_omega[n] += b
    require(not any(sf_omega), 'Squarefree conjugate ideal columns lost.')
    require(not any(all_cube_omega), 'Cube divisor conjugate ideals lost.')
    # Independent HNF/square-prime check on the complete small prefix.
    hcap = min(512, n_cap)
    primes = prime_ideals(hcap)
    h_count = [0]*(hcap+1)
    h_sf = [0]*(hcap+1)
    for i in hnf_ideals(hcap):
        if gcd(norm(i), 6) == 1:
            h_count[norm(i)] += 1
            if hnf_mobius(i, primes):
                h_sf[norm(i)] += 1
    require(h_count == list(all_count[:hcap+1]), 'Primary generator ideal coverage differs.')
    require(h_sf == list(sf_count[:hcap+1]), 'Primary squarefree classification differs.')
    digest = hashlib.sha256()
    for values in (sf_count, sf_real, all_count, all_cube_real):
        # Stable decimal source contract; no host-endian ambiguity.
        digest.update((','.join(map(str, values))+'\n').encode('ascii'))
    return sf_count, sf_real, all_count, all_cube_real, {
        'complete_primary_norm_cap': cap, 'complete_exterior_primary_ideals': total,
        'complete_squarefree_ideals': squarefree,
        'full_cube_divisor_norm_cap': n_cap,
        'independent_complete_HNF_prefix': hcap,
        'integer_primitive_stream_sha256': digest.hexdigest()}


def show(x):
    text = x.str(65, more=True)
    require(arb(text).contains(x), 'Decimal directed enclosure lost.')
    return text


def ray_phase(n):
    require(n % 2 == 1, 'Ray norm must be odd.')
    return 1 if n % 4 == 1 else -1


def produce(scales=(64, 256, 1024, 4096), ratio=256, n_cap=256, precision=192):
    ctx.prec = precision
    max_cap = ratio*max(scales)
    sf_count, sf_real, n_count, n_cube, coverage = primitives(max_cap, n_cap)
    hconstant = arb(1)/(4*arb.pi())
    # If C/B>=R>1, the WHOLE c>C tail is <=3 hconstant exp(-log(R)^2/2)
    # *(1+1/log R). Sum all n with sum (Nn)^-2<=6.
    log_r = arb(ratio).log()
    c_tail = 18*hconstant*(-log_r*log_r/2).exp()*(1+1/log_r)
    limit = arb.pi()/(6*arb(3).sqrt())/(2*(2*arb.pi()).sqrt())
    rows = []
    for Z in scales:
        require(n_cap**3 > Z, 'Cube divisor tail must be on decreasing Gaussian side.')
        exact_norm = arb(0)
        overlap = arb(0)
        ray_overlap = arb(0)
        evaluations = 0
        for n in range(1, n_cap+1):
            if not n_count[n]:
                continue
            n3 = n*n*n
            cap = min(max_cap, (ratio*Z+n3-1)//n3)
            cap = max(cap, 1)
            s0, s1, s_ray = arb(0), arb(0), arb(0)
            for c in range(1, cap+1):
                if not sf_count[c]:
                    continue
                u = (arb(c*n3)/Z).log()
                weight = hconstant*(-u*u/2).exp()
                s0 += sf_count[c]*weight/c
                if sf_real[c]:
                    term = sf_real[c]*weight/(arb(c)*arb(c).sqrt())
                    s1 += term
                    s_ray += ray_phase(c)*term
                evaluations += 1
            exact_norm += n_count[n]*s0/(n*n)
            n_factor = arb(n_cube[n])/(arb(n)**3*arb(n).sqrt())
            # n_factor=sum theta_1(n)^3/(Nn)^2, with every n ideal kept.
            overlap += n_factor*s1
            ray_overlap += ray_phase(n)*n_factor*s_ray
        log_n = (arb(n_cap**3)/Z).log()
        n_tail = 18*hconstant/n_cap*(-log_n*log_n/2).exp()*(1+1/log_n)
        tail = c_tail+n_tail
        error = arb(0, tail.abs_upper())
        norm_ball = exact_norm+error
        overlap_ball = overlap+error
        ray_ball = ray_overlap+error
        require(norm_ball > 0, 'Complete norm positive gate failed.')
        rows.append({'Z': Z, 'complete_norm_squared': show(norm_ball),
                     'theta_1_overlap_real': show(overlap_ball),
                     'theta_1_chi_minus4_norm_overlap_real': show(ray_ball),
                     'theta_1_normalized_overlap': show(overlap_ball/norm_ball),
                     'theta_1_chi_minus4_normalized_overlap': show(ray_ball/norm_ball),
                     'complete_c_tail_bound': show(c_tail),
                     'complete_n_tail_bound': show(n_tail),
                     'integer_total_norm_pairs_evaluated': evaluations})
    return {'status': 'FINITE_DIRECTED_COMPLETE_SOURCE_FIXTURES; NO_ASYMPTOTIC_INFERENCE',
            'arithmetic': 'EXACT_PRIMARY_LATTICE_PLUS_DIRECTED_INTERVAL',
            'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'python_flint': flint.__version__, 'FLINT': flint.__FLINT_VERSION__,
            'precision_bits': precision,
            'parameters': {'scales': list(scales), 'c_cutoff_ratio': ratio,
                           'all_n_ideal_norm_cap': n_cap},
            'coverage': coverage,
            'source': 'Complete c squarefree,n unrestricted exterior ideals; c and n may share primes.',
            'angular_characters': ['alpha_I/sqrt(NI)',
                                   'chi_minus4(NI)*alpha_I/sqrt(NI)'],
            'exact_imaginary_overlap': '0 by conjugation on full primitive source',
            'proved_asymptotic_norm_limit': show(limit), 'cases': rows}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('ANGULAR_CHECKS.json'))
    parser.add_argument('--replay', type=Path)
    args = parser.parse_args()
    if args.replay:
        old = json.loads(args.replay.read_text(encoding='utf-8'))
        params = old['parameters']
        fresh = produce(tuple(params['scales']), params['c_cutoff_ratio'],
                        params['all_n_ideal_norm_cap'], old['precision_bits'])
        require(old == fresh, 'Primitive angular source replay differs.')
        longer = produce(tuple(params['scales']), 2*params['c_cutoff_ratio'],
                         2*params['all_n_ideal_norm_cap'], old['precision_bits']+64)
        containments = 0
        for a, b in zip(old['cases'], longer['cases'], strict=True):
            require(a['Z'] == b['Z'], 'Longer replay lost source scale.')
            for key in ('complete_norm_squared', 'theta_1_overlap_real',
                        'theta_1_chi_minus4_norm_overlap_real',
                        'theta_1_normalized_overlap',
                        'theta_1_chi_minus4_normalized_overlap'):
                require(arb(a[key]).contains(arb(b[key])),
                        'Longer complete angular source not contained: '+key)
                containments += 1
        result = {'status': 'PASS_PRIMITIVE_AND_LONGER_DIRECTED_REPLAY',
                  'finite_scope_only': True, 'containments': containments,
                  'original_coverage': old['coverage'], 'longer_coverage': longer['coverage'],
                  'source_report_sha256': hashlib.sha256(args.replay.read_bytes()).hexdigest(),
                  'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n', encoding='utf-8')
        print(json.dumps(result))
        return
    result = produce()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'output': str(args.output),
                      'coverage': result['coverage'], 'cases': len(result['cases'])}))


if __name__ == '__main__':
    main()
