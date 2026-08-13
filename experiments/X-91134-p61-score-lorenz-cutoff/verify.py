#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt
import json
from pathlib import Path

PRIMES=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
CUTOFF=10000
DEN=10**60


def divisors_with_mu():
    values=[(1,1)]
    for prime in PRIMES:
        values += [(d*prime,-mu) for d,mu in list(values)]
    return sorted(values)


def invsqrt_upper(n):
    lower=isqrt(n*DEN*DEN)
    return Fraction(DEN,lower)


def invsqrt_lower(n):
    upper=isqrt(n*DEN*DEN)
    if upper*upper<n*DEN*DEN:
        upper+=1
    return Fraction(DEN,upper)


def sqrt_lower(n):
    return Fraction(isqrt(n*DEN*DEN),DEN)


def main():
    divisors=divisors_with_mu()
    assert len(divisors)==2**18

    odd_reciprocal_total=sum(
        Fraction(1,d) for d,mu in divisors if mu==-1)
    even_reciprocal_prefix=sum(
        Fraction(1,d) for d,mu in divisors if mu==1 and d<=CUTOFF)
    a_gap=even_reciprocal_prefix-odd_reciprocal_total
    assert a_gap>0

    b_upper=Fraction(0)
    for d,mu in divisors:
        if d>CUTOFF:
            break
        if mu==1:
            b_upper += invsqrt_upper(d)
        elif mu==-1:
            b_upper -= invsqrt_lower(d)

    root=sqrt_lower(CUTOFF)
    margin=5*root*a_gap-3*b_upper-Fraction(335,1)/root
    assert margin>0

    result={
      'classification':'PASS_P61_SCORE_LORENZ_CUTOFF_10000',
      'divisor_states':len(divisors),
      'cutoff':CUTOFF,
      'A_gap':str(a_gap),
      'A_gap_decimal':float(a_gap),
      'B_directed_upper':str(b_upper),
      'B_directed_upper_decimal':float(b_upper),
      'lower_margin_at_x_10000':str(margin),
      'lower_margin_decimal':float(margin),
      'scope':(
        'Exact Fraction arithmetic and directed square-root enclosures prove '
        'the fixed-cutoff reserve. The analytic theorem then gives a uniform '
        'score-Lorenz cutoff below 10000. This does not certify the remaining '
        'row-prefix determinants or RH.'),
    }
    out=Path(__file__).resolve().parent/'results'/'verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['classification'])
    print(out)

if __name__=='__main__':main()
