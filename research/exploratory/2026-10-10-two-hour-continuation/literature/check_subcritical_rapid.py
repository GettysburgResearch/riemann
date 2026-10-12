"""Independent finite product multiplicities for the rapid Euler lemma."""
from collections import Counter
from itertools import product
from math import comb, prod
from pathlib import Path
import argparse
import hashlib
import json
from flint import arb, ctx


def need(ok, detail):
    if not ok:
        raise ArithmeticError(detail)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    ctx.prec = 192
    here = Path(__file__).resolve()
    prior = here.with_name('PRIME_SLOT_SUBCRITICAL_TUBE.md')
    prior_hash = '5aca641b5c58e8d2efaf643c660d98cb5970235478bd9e0622e1d6014c4a1c28'
    need(hashlib.sha256(prior.read_bytes()).hexdigest() == prior_hash,
         'frozen all-row subcritical source tube')
    # Good prime ideals at norm <=31: two distinct ideals over each split
    # prime, and the single inert ideal over 5. Their algebraic labels keep
    # equal norms from collapsing two distinct prime-ideal slots.
    prime_norms = (7,7,13,13,19,19,25,31,31)
    dimension = len(prime_norms)
    ideals = [tuple(0 for _ in prime_norms)]
    ideals += [tuple(int(i==j) for i in range(dimension)) for j in range(dimension)]
    alpha = arb(4)/5
    weights = [(-alpha*arb(q).log()).exp() for q in prime_norms]
    A = arb(1)+sum(weights)
    Z = arb(1)
    for w in weights:
        Z /= 1-w
    records = []
    complete_divisor_controls = 0
    for m in range(1,6):
        counts = Counter()
        for factors in product(ideals,repeat=m):
            exponents = tuple(sum(f[i] for f in factors) for i in range(dimension))
            counts[exponents] += 1
        need(sum(counts.values()) == len(ideals)**m,'complete ordered product census')
        weighted_restricted = distinct = arb(0)
        for exponents,multiplicity in counts.items():
            complete_divisor = prod(comb(e+m-1,m-1) for e in exponents)
            need(multiplicity <= complete_divisor,'restricted multiplicity versus full ordered ideal divisor')
            need(complete_divisor <= m**sum(exponents),
                 'elementary stars-and-bars versus m^e bound')
            value = arb(1)
            for w,e in zip(weights,exponents):
                value *= w**e
            distinct += value
            weighted_restricted += multiplicity*value
            complete_divisor_controls += 1
        need(abs(weighted_restricted-A**m) < arb('1e-45'),
             'independent product census reconstructs weighted short-ideal power')
        need(Z > distinct,'positive Euler product contains every distinct restricted product')
        max_multiplicity = max(counts.values())
        need(max_multiplicity*distinct >= weighted_restricted-arb('1e-45'),
             'multiplicity removal pays exactly once')
        need(Z > A**m/max_multiplicity,
             'directed finite positive product lower bound after multiplicity cost')
        records.append(dict(m=m,ordered_products=len(ideals)**m,
                            distinct_product_ideals=len(counts),
                            maximum_restricted_multiplicity=max_multiplicity))
    record = dict(status='PASS_EXACT_SUBCRITICAL_RAPID_PRODUCT_CONTROLS',
                  precision_bits=192,alpha_exact=[4,5],cutoff=31,
                  distinct_prime_ideal_norms=list(prime_norms),
                  short_good_ideal_count=len(ideals),orders=records,
                  complete_divisor_controls=complete_divisor_controls,
                  positive_finite_Euler_ball=Z.str(40,more=True),
                  weighted_short_ideal_sum_ball=A.str(40,more=True),
                  proof_sha256=hashlib.sha256(here.with_name('SUBCRITICAL_RAPID_COLLISION_DECAY.md').read_bytes()).hexdigest(),
                  checker_sha256=hashlib.sha256(here.read_bytes()).hexdigest(),
                  frozen_source_tube_sha256=prior_hash,
                  asymptotic_divisor_bound_proved_by_finite_checker=False,
                  arbitrary_power_decay_proved_by_finite_checker=False,
                  individual_reciprocal_factors_bounded=False,
                  generalized_moment_proved=False,rh_proved=False)
    args.output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(record['status'])


if __name__ == '__main__':
    main()
