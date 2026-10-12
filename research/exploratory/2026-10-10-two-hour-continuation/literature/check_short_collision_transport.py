"""Exact ideal coefficient controls for short collision transport."""
from collections import Counter
from itertools import product, combinations_with_replacement
from pathlib import Path
import argparse
import hashlib
import json


def need(ok, label):
    if not ok:
        raise ArithmeticError(label)


def local_q(exponents):
    return 1-sum(e>0 for e in exponents)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve()
    factor_proof = here.with_name('PRIME_SLOT_CANCELLATION.md')
    factor_hash = 'd37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13'
    need(hashlib.sha256(factor_proof.read_bytes()).hexdigest()==factor_hash,
         'frozen exact source finite factorization')
    rapid_proof = here.with_name('SUBCRITICAL_RAPID_COLLISION_DECAY.md')
    rapid_hash = 'a41b84b54f0e4052e6700887bad5cd82552ab452744f29c1b5f70e68cbf0735e'
    need(hashlib.sha256(rapid_proof.read_bytes()).hexdigest()==rapid_hash,
         'frozen analytic rapid source tube')

    local_controls = 0
    for r in (2,4):
        for exponents in product(range(4),repeat=r):
            positive = [i for i,e in enumerate(exponents) if e]
            coefficient = 0
            for choose in product((0,1),repeat=len(positive)):
                lower = list(exponents)
                for selected,i in zip(choose,positive):
                    lower[i] -= selected
                coefficient += (-1)**sum(choose)*local_q(lower)
            expected = 1 if not any(exponents) else (-1 if sum(exponents)==1 else 0)
            need(coefficient==expected,'complete local collision series times single factors')
            local_controls += 1

    # All good prime ideals below 13 outside source bad primes 2,3.
    # The equal norm entries remain distinct prime-ideal labels.
    norms = (7,7,13,13)
    Y = 13
    high_controls = 0
    for i,j in combinations_with_replacement(range(4),2):
        need(norms[i]*norms[j]>Y,'every omitted nontrivial single-factor product stays above window')
        high_controls += 1
    orders = []
    for r in (2,4,6):
        count = repeated = nonzero = 0
        for word in product(range(5),repeat=r):
            active = [i for i,p in enumerate(word) if p]
            target = (-1)**len(active) if len({word[i] for i in active})==len(active) else 0
            transported = 0
            for choose in product((0,1),repeat=len(active)):
                residual = Counter(word[i] for selected,i in zip(choose,active) if not selected)
                value = (-1)**sum(choose)
                for p in range(1,5):
                    value *= 1-residual[p]
                transported += value
            need(transported==target,'short single polynomials retain every low-column source coefficient')
            count += 1
            repeated += target==0
            nonzero += target!=0
        orders.append(dict(slots=r,complete_low_column_controls=count,
                           canceled_repeated_prime_allocations=repeated,
                           retained_coprime_allocations=nonzero))
    record = dict(status='PASS_EXACT_SHORT_POLYNOMIAL_COLLISION_TRANSPORT',
                  actual_distinct_prime_ideal_norms=list(norms),column_norm_cutoff=Y,
                  local_collision_series_controls=local_controls,
                  omitted_high_single_term_controls=high_controls,orders=orders,
                  total_low_column_controls=sum(x['complete_low_column_controls'] for x in orders),
                  multiplicative_source_phases_symbolically_retained=True,
                  proof_sha256=hashlib.sha256(here.with_name('SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md').read_bytes()).hexdigest(),
                  checker_sha256=hashlib.sha256(here.read_bytes()).hexdigest(),
                  source_factorization_sha256=factor_hash,
                  analytic_rapid_source_tube_sha256=rapid_hash,
                  asymptotic_tube_estimate_proved_by_finite_checker=False,
                  original_Euler_and_short_integrands_equal_pointwise=False,
                  complementary_frequency_region_bounded=False,
                  generalized_moment_proved=False,rh_proved=False)
    args.output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(record['status'])


if __name__=='__main__':
    main()
