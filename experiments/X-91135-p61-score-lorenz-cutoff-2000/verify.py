#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt
import json
from pathlib import Path

PRIMES=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
CUTOFF=2000
DEN=10**60


def divisors_with_mu():
    values=[(1,1)]
    for prime in PRIMES:
        values += [(d*prime,-mu) for d,mu in list(values)]
    return sorted(values)


def invsqrt_scaled_interval(n):
    lower=isqrt((DEN*DEN)//n)
    while (lower+1)*(lower+1)*n <= DEN*DEN:
        lower += 1
    while lower*lower*n > DEN*DEN:
        lower -= 1
    exact=(lower*lower*n==DEN*DEN)
    return lower, lower if exact else lower+1


def sqrt_scaled_interval(n):
    lower=isqrt(n*DEN*DEN)
    exact=(lower*lower==n*DEN*DEN)
    return lower, lower if exact else lower+1


def main():
    divisors=divisors_with_mu()
    assert len(divisors)==2**18

    odd_reciprocal_total=sum(
        Fraction(1,d) for d,mu in divisors if mu==-1
    )
    even_reciprocal_prefix=sum(
        Fraction(1,d) for d,mu in divisors if mu==1 and d<=CUTOFF
    )
    a_gap=even_reciprocal_prefix-odd_reciprocal_total
    assert a_gap>0

    b_lower_scaled=0
    b_upper_scaled=0
    for d,mu in divisors:
        if d>CUTOFF:
            break
        lo,hi=invsqrt_scaled_interval(d)
        if mu==1:
            b_lower_scaled += lo
            b_upper_scaled += hi
        elif mu==-1:
            b_lower_scaled -= hi
            b_upper_scaled -= lo

    root_lower_scaled,root_upper_scaled=sqrt_scaled_interval(CUTOFF)
    root_lower=Fraction(root_lower_scaled,DEN)
    margin=(
        5*root_lower*a_gap
        -3*Fraction(b_upper_scaled,DEN)
        -Fraction(335*DEN,root_lower_scaled)
    )
    assert margin>Fraction(1,4)

    candidate_cutoffs=[d for d,mu in divisors if 2<=d<CUTOFF and mu==1]
    result={
      'classification':'PASS_P61_SCORE_LORENZ_CUTOFF_2000',
      'divisor_states':len(divisors),
      'cutoff':CUTOFF,
      'candidate_even_cutoffs_below_bound':len(candidate_cutoffs),
      'largest_candidate_even_cutoff':max(candidate_cutoffs),
      'A_gap':str(a_gap),
      'A_gap_decimal':float(a_gap),
      'B_directed_lower_scaled':str(b_lower_scaled),
      'B_directed_upper_scaled':str(b_upper_scaled),
      'B_scale_denominator':str(DEN),
      'B_directed_upper_decimal':b_upper_scaled/DEN,
      'sqrt_cutoff_lower_scaled':str(root_lower_scaled),
      'sqrt_cutoff_upper_scaled':str(root_upper_scaled),
      'sqrt_scale_denominator':str(DEN),
      'lower_margin_at_x_2000':str(margin),
      'lower_margin_decimal':float(margin),
      'scope':(
        'Exact Fraction arithmetic and fixed-denominator directed square-root '
        'enclosures prove the fixed-cutoff reserve. The analytic theorem then '
        'gives a uniform score-Lorenz cutoff below 2000. This does not certify '
        'the remaining row-prefix determinants, LRPT, or RH.'),
    }
    out=Path(__file__).resolve().parent/'results'/'verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['classification'])
    print(out)

if __name__=='__main__':main()
