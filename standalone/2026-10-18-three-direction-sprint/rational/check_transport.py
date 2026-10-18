#!/usr/bin/env python3
"""Exact finite pair-transport, divisor resource and complete-mask replay.

The finite H defaults to floor(sqrt(Y)); no asymptotic squarefree theorem is
certified by a run. Every good reference, shared input prime, old product and
canonical denominator is constructed explicitly. Optional python-flint
certifies the complete full-kernel energy on the native physical window.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path
import hashlib
import json
import subprocess
import sys

import verify as v


COUNTS = Counter()
MUTATION = 'none'
MUTATIONS = ('drop_shared_references', 'wrong_probability', 'even_reference_sum',
             'drop_above_prefix_products', 'omit_strip_boundary',
             'truncate_canonical_divisors')


def need(ok, gate):
    COUNTS[gate] += 1
    if not ok:
        raise RuntimeError('REJECT:' + gate)


def add_value(out, key, value):
    out[key] = out.get(key, F(0)) + value
    if not out[key]:
        del out[key]


def canonical(alpha):
    out = {}
    for d, value in alpha.items():
        ds = (d,) if MUTATION == 'truncate_canonical_divisors' else v.divisors(d)
        for q in ds:
            add_value(out, q, value)
    return out


def core_parts(q):
    r = s = 1
    for p, e in v.factors(q):
        need(e <= 2, 'cubefree_complete_support')
        if e == 2:
            r *= p
        else:
            s *= p
    return r, s


def triples(s):
    out = [(1, 1, 1)]
    for p, e in v.factors(s):
        need(e == 1, 'squarefree_core_partition')
        out = [(p*a, b, c) for a,b,c in out] + [(a,p*b,c) for a,b,c in out] \
            + [(a,b,p*c) for a,b,c in out]
    return out


def integer_root(n, degree):
    lo, hi = 0, 1
    while hi ** degree <= n:
        hi *= 2
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid ** degree <= n:
            lo = mid
        else:
            hi = mid
    return lo


def directed_energy(alpha, y, gap, dependency_dir):
    sys.path.insert(0, str(dependency_dir.resolve()))
    import flint
    from flint import arb, ctx
    need(flint.__version__ == '0.9.0', 'pinned_directed_backend')
    ctx.prec = 192
    def ball(q):
        return arb(q.numerator)/q.denominator
    const = arb(0)
    events = defaultdict(F)
    end = (y+1)**2
    for d, coefficient in alpha.items():
        const += ball(coefficient)*arb(d).log()
        for j in range(1, (end-1)//d+1):
            events[j*d] += coefficient/j
    start = y+1
    h = sum((jump for k,jump in events.items() if k <= start), F(0))
    energy = arb(0)
    left = start
    amplitude_bound = arb(120)*(gap+1)/(y*y)
    for k in sorted(k for k in events if start < k < end) + [end]:
        value = const+ball(h)
        need(abs(value) <= amplitude_bound, 'directed_complete_kernel_bound')
        energy += (k-left)*value*value
        if k != end:
            h += events[k]
        left = k
    upper = arb(28800)*(gap+1)**2/(y*y)
    need(energy >= 0 and energy <= upper, 'directed_complete_kernel_energy')
    encoded = energy.str(50, more=True)
    need(arb(encoded).contains(energy), 'directed_receipt_enclosure')
    return {'arithmetic': 'DIRECTED_INTERVAL', 'precision_bits': 192,
            'python_flint': flint.__version__, 'physical_window': [start,end-1],
            'complete_kernel_energy': encoded, 'all_harmonic_jump_cells': len(events),
            'source_and_physical_tail': 'none omitted inside the declared native window'}


def run(y, width, dependency_dir=None):
    need(y >= 1024 and width >= 1 and width <= isqrt(y), 'finite_input_domain')
    # A real squarefree old pair shows why the lattice-strip boundary term
    # is necessary for the stated coefficient class, even if the coarser
    # area bound happens to cover this run's diffuse population.
    fixture_a,fixture_b=1021,1022
    need(v.mu_trial(fixture_a)!=0 and v.mu_trial(fixture_b)!=0,
         'nonzero_old_pair_boundary_fixture')
    fixture_q=fixture_a*fixture_b
    fixture_r,fixture_s=core_parts(fixture_q)
    fixture_bound=F(0)
    for u,vv,w in triples(fixture_s):
        fixture_bound += F(2*1024,fixture_q*w)
        if MUTATION != 'omit_strip_boundary':
            fixture_bound += F(1024,fixture_r*w*max(u,vv))
    need(fixture_bound>=1,'necessary_strip_boundary_old_pair_fixture')
    mu = v.mu_sieve(y)
    need(all(mu[n] == v.mu_trial(n) for n in range(1,y+1)), 'independent_primitive_mu')
    primes = [p for p in range(y//2+1,y+1) if v.factors(p) == ((p,1),)]
    root_upper = isqrt(y)
    if root_upper*root_upper < y:
        root_upper += 1
    threshold = y*y-20*y*root_upper
    need(threshold > y*y//4, 'nonempty_theoretical_interior_range')
    target_alpha, reference_pairs = {}, {}
    probability_load = defaultdict(F)
    target_pairs, boundary = [], []
    minimum_good = width
    maximum_gap = maximum_strip = 0
    construction_hash = hashlib.sha256()
    shared_references = 0
    for at,p in enumerate(primes):
        for ell in primes[at+1:]:
            n = p*ell
            if n > threshold:
                boundary.append((p,ell))
                continue
            r = isqrt(n)
            t = (r+1)*(r+2)-n
            k0 = (isqrt(1+4*t)-1)//2
            need(k0*(k0+1) <= t < (k0+1)*(k0+2), 'exact_almost_square_index')
            good = []
            independently_good = []
            for k in range(k0,k0+width):
                a,b = r+1-k,r+2+k
                if MUTATION == 'even_reference_sum':
                    a -= 1
                need(1 <= a < b <= y, 'every_reference_is_old_input')
                need((a+b)%2 == 1, 'odd_reference_sum')
                if mu[a] and mu[b]:
                    independently_good.append((a,b))
                    if MUTATION != 'drop_shared_references' or gcd(a,b) == 1:
                        good.append((a,b))
            need(good == independently_good, 'complete_good_reference_set')
            need(len(good)*5 >= width, 'finite_squarefree_density_gate')
            minimum_good = min(minimum_good,len(good))
            probability = F(1,len(good))
            if MUTATION == 'wrong_probability':
                probability = F(1)
            need(probability*len(good) == 1, 'exact_target_probability_mass')
            target_pairs.append((p,ell))
            add_value(target_alpha,n,F(2,n))
            for a,b in good:
                m = a*b
                need(mu[a]*mu[b] != 0, 'actual_nonzero_mobius_reference')
                need(m%2 == 0 and n%2 == 1, 'even_reference_odd_target')
                need(m != n, 'distinct_target_and_reference_product')
                delta = abs(m-n)
                maximum_gap = max(maximum_gap,delta)
                maximum_strip = max(maximum_strip,b-a)
                need(delta <= 8*root_upper*width, 'complete_product_gap')
                need(b-a <= 7*root_upper, 'complete_balanced_strip')
                probability_load[a,b] += probability
                if MUTATION != 'drop_above_prefix_products' or m <= y:
                    add_value(reference_pairs,(a,b),-F(2,n)*probability)
                if gcd(a,b)>1:
                    shared_references += 1
                construction_hash.update(f'{n}:{a}:{b}:{probability};'.encode())
    need(bool(target_pairs) and shared_references > 0, 'nonvacuous_interior_and_shared_primes')
    load_bound = F(5*(2*maximum_gap+1),width)
    need(all(load <= load_bound for load in probability_load.values()), 'complete_fractional_load_bound')
    reference_alpha = {}
    input_replay = target_alpha.copy()
    max_input_weight = F(1)
    for (a,b),coefficient in reference_pairs.items():
        add_value(reference_alpha,a*b,coefficient)
        weight = coefficient*(a*b)/(2*mu[a]*mu[b])
        need(abs(weight) <= 4*probability_load[a,b], 'actual_ordered_input_weight_bound')
        max_input_weight = max(max_input_weight,abs(weight))
        add_value(input_replay,a*b,2*weight*F(mu[a]*mu[b],a*b))
    alpha = target_alpha.copy()
    for d,value in reference_alpha.items():
        add_value(alpha,d,value)
    need(input_replay == alpha, 'complete_ordered_pair_reconstruction')
    need(sum(alpha.values(),F(0)) == 0, 'zero_q1_and_logx_coefficient')
    ctarget,cref,c = canonical(target_alpha),canonical(reference_alpha),canonical(alpha)
    need(c.get(1,F(0)) == 0, 'complete_canonical_centering')
    recovered = {}
    for q,coefficient in c.items():
        for d in v.divisors(q):
            add_value(recovered,d,coefficient*v.mu_trial(q//d))
    need(recovered == alpha, 'full_reduced_denominator_inverse')
    shared_square_count = 0
    incidence_counts = Counter()
    for a,b in reference_pairs:
        for q in v.divisors(a*b):
            incidence_counts[q] += 1
    largest_reference_coefficient = max(abs(x) for x in reference_pairs.values())
    for q,count in incidence_counts.items():
        r,s = core_parts(q)
        strip_bound = F(0)
        for u,vv,w in triples(s):
            first = F(2*y*maximum_strip,r*r*s*w)
            boundary_term = F(y,r*w*max(u,vv))
            need((w*max(u,vv))**2 >= s, 'retained_square_root_boundary_factor')
            strip_bound += first
            if MUTATION != 'omit_strip_boundary':
                strip_bound += boundary_term
        need(count <= strip_bound, 'complete_strip_lattice_count')
        need(abs(cref[q]) <= largest_reference_coefficient*strip_bound,
             'complete_coefficient_from_strip_resource')
        if r>1:
            shared_square_count += 1
            need(r <= maximum_strip, 'all_shared_square_core_support')
    need(shared_square_count>0,'nonvacuous_squared_denominator_population')
    for p in primes:
        for ell in primes:
            if p>=ell:
                continue
            q=p*ell
            need(cref.get(q,F(0)) == 0, 'all_even_reference_target_divisibility_excluded')
            need(c.get(q,F(0)) == (F(2,q) if (p,ell) in target_pairs else 0),
                 'all_interior_target_coefficients_retained')
    resource_rows = []
    thresholds = {2,7,31,127,511,1024}
    x=y+1
    while x<(y+1)**2:
        thresholds.add(integer_root(x**13,24))
        x*=2
    for qmax in sorted(thresholds):
        mass=sum((q*q*value*value for q,value in c.items() if 2<=q<=qmax),F(0))
        h_upper=1+qmax.bit_length()
        upper=4*largest_reference_coefficient**2 \
            *((2*y*maximum_strip)**2*qmax+y*y*qmax*qmax)*h_upper**8+32*qmax
        need(mass<=upper,'complete_low_denominator_square_resource')
        resource_rows.append({'Q':qmax,'actual_mass_num':str(mass.numerator),
                              'actual_mass_den':str(mass.denominator)})
    # Boundary canonical source is its literal S_(pl), including all lower R terms.
    final_alpha=alpha.copy()
    for p,ell in boundary:
        coefficient=F(2,p*ell)
        for d,sign in ((p*ell,1),(p,-1),(ell,-1),(1,1)):
            add_value(final_alpha,d,sign*coefficient)
    final_c=canonical(final_alpha)
    for at,p in enumerate(primes):
        for ell in primes[at+1:]:
            need(final_c.get(p*ell,F(0))==F(2,p*ell),'all_boundary_and_interior_targets_retained')
    need(final_c.get(1,F(0))==0,'final_boundary_centering')
    masks=[]
    x=y+1
    while x<(y+1)**2:
        qmax=integer_root(x**13,24)
        for score in (1,2,5,17):
            kept={q:value for q,value in final_c.items()
                  if q>qmax and v.core(q)>score}
            for at,p in enumerate(primes):
                for ell in primes[at+1:]:
                    q=p*ell
                    original=F(2,q) if q>qmax and v.core(q)>score else F(0)
                    need(original-kept.get(q,F(0))==0,'exact_native_mask_target_removal')
            masks.append({'annular_X':x,'Q':qmax,'S':score,'complete_retained_coefficients':len(kept)})
        x*=2
    report={'status':'PASS','arithmetic':'EXACT_RATIONAL_OLD_PAIR_AND_DIVISOR_RESOURCES',
            'Y':y,'finite_H':width,'top_prime_count':len(primes),
            'interior_targets':len(target_pairs),'boundary_targets':len(boundary),
            'minimum_good_reference_count':minimum_good,
            'distinct_reference_pairs':len(reference_pairs),
            'shared_reference_edges':shared_references,'squared_denominator_count':shared_square_count,
            'maximum_actual_gap':maximum_gap,'maximum_actual_strip':maximum_strip,
            'maximum_actual_input_weight':{'num':str(max_input_weight.numerator),'den':str(max_input_weight.denominator)},
            'canonical_denominator_count':len(c),'all_mask_cases':masks,
            'coefficient_resources':resource_rows,
            'construction_sha256':construction_hash.hexdigest(),
            'not_proved':['asymptotic squarefree interval theorem','uniform asymptotic reference density',
                          'full rough-core contraction','RH']}
    if dependency_dir is not None:
        report['directed_full_kernel']=directed_energy(alpha,y,maximum_gap,dependency_dir)
    report['checks_by_gate']=dict(sorted(COUNTS.items()))
    report['total_checks_including_guards']=sum(COUNTS.values())
    return report


def main():
    global MUTATION
    a=argparse.ArgumentParser()
    a.add_argument('--Y',type=int,default=1024)
    a.add_argument('--H',type=int,default=32)
    a.add_argument('--dependency-dir',type=Path)
    a.add_argument('--mutate',choices=('none',)+MUTATIONS,default='none')
    a.add_argument('--mutations',action='store_true')
    a.add_argument('--report',type=Path)
    z=a.parse_args()
    MUTATION=z.mutate
    report=run(z.Y,z.H,z.dependency_dir)
    if z.mutations:
        rows=[]
        for mutation in MUTATIONS:
            r=subprocess.run([sys.executable,'-B','-O',str(Path(__file__).resolve()),
                              '--Y',str(z.Y),'--H',str(z.H),'--mutate',mutation],capture_output=True,text=True)
            need(r.returncode!=0 and 'REJECT:' in r.stderr,'mutation_rejected')
            rows.append({'mutation':mutation,'status':'REJECTED',
                         'gate':r.stderr.rsplit('REJECT:',1)[-1].splitlines()[0]})
        report['mutations']=rows
    encoded=json.dumps(report,sort_keys=True,indent=2)+'\n'
    if z.report:
        z.report.write_text(encoded,encoding='utf-8',newline='\n')
    # Resource fractions remain in the file, not the progress stream.
    print(json.dumps({k:v for k,v in report.items() if k!='coefficient_resources'},indent=2),end='\n')


if __name__=='__main__':
    main()
