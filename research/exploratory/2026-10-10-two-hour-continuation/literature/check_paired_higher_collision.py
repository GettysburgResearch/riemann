"""Exact complete paired-slot controls; no source moment is asserted."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json


def need(ok, detail):
    if not ok:
        raise ArithmeticError(detail)


def mul(z, w):
    a, b = z
    c, d = w
    return a*c-b*d, a*d+b*c-b*d


def conj(z):
    a, b = z
    return a-b, -b


def norm(z):
    a, b = z
    return a*a-a*b+b*b


def factor(z, q):
    return F(1)-F(z[0], q), -F(z[1], q)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve()
    prior = here.with_name('PRIME_SLOT_CANCELLATION.md')
    prior_hash = 'd37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13'
    need(hashlib.sha256(prior.read_bytes()).hexdigest() == prior_hash,
         'frozen all-pair source factorization')
    units = [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
    counts = []
    strict = total = 0
    for k in range(1,5):
        count = 0
        for q in (7,13,19,31):
            x = F(1,q)
            for a in units:
                for phases in product(units, repeat=k):
                    left = [mul(a,v) for v in phases]
                    slots = left+[conj(z) for z in left]
                    complete = (F(1),F(0))
                    for i in range(2*k):
                        for j in range(i+1,2*k):
                            complete = mul(complete,factor(mul(slots[i],slots[j]),q))
                    same = mixed = F(1)
                    for i in range(k):
                        for j in range(i+1,k):
                            same *= norm(factor(mul(mul(a,a),mul(phases[i],phases[j])),q))
                            mixed *= norm(factor(mul(phases[i],conj(phases[j])),q))
                    reunited = (1-x)**k*same*mixed
                    bound = (1-x)**(k*(2-k))*(1-x*x)**(k*(k-1))*mixed
                    need(complete == (reunited,0),'all source pair factors exactly reunited')
                    need(0 < reunited <= bound,'higher-k exponents and exact triangle bound')
                    if len(set(phases)) == 1:
                        need(bound == (1-x)**k*(1-x*x)**(k*(k-1)),
                             'common-frequency cancellation of positive exponent')
                    strict += reunited < bound
                    count += 1
        counts.append({'k':k,'slots':2*k,'exact_complete_pair_controls':count,
                       'endpoint_positive_log_exponent':k*(k-2),
                       'moving_mask_loglog_exponent':k*(k-1),
                       'cluster_log_exponent':-k})
        total += count
    record = dict(status='PASS_EXACT_PAIRED_HIGHER_COLLISION_CONTROLS',
                  total_exact_complete_pair_controls=total,
                  strict_triangle_controls=strict,orders=counts,
                  actual_prime_norms=[7,13,19,31],sextic_phase_controls=6,
                  proof_sha256=hashlib.sha256(here.with_name('PAIRED_HIGHER_MOMENT_COLLISION.md').read_bytes()).hexdigest(),
                  checker_sha256=hashlib.sha256(here.read_bytes()).hexdigest(),
                  frozen_source_factorization_sha256=prior_hash,
                  arbitrary_ray_phase_bound_proved_by_finite_checker=False,
                  classical_reciprocal_zeta_proof_rebuilt=False,
                  independent_2k_frequency_trace_proved=False,
                  generalized_moment_proved=False,rh_proved=False)
    args.output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(record['status'])


if __name__ == '__main__':
    main()
