#!/usr/bin/env python3
"""Exact rational witness for generic finite Li positivity blindness.
No external packages. Decimals are display only. See li_advocate.md for proof.
"""
import json
from fractions import Fraction
from pathlib import Path

def quartet_li(n):
    # Re((61+32i)^n), computed entirely in integers.
    x,y=1,0
    for _ in range(n):
        x,y=61*x-32*y,32*x+61*y
    return 4-2*Fraction(x)*(Fraction(1,65**n)+Fraction(1,73**n))

def main():
    prefix=[quartet_li(n) for n in range(1,12)]
    assert all(q>=0 for q in prefix)
    q91=quartet_li(91)
    upper=q91+4*91
    assert upper<0
    result={
      'status':'exact rational checks; analytic baseline bounds proved in campaign note',
      'model':'cosh(s-1/2)/cosh(1/2) times normalized quartet beta=1/4,T=2',
      'nonnegative_quartet_prefix':11,
      'prefix_numerators':[str(q.numerator) for q in prefix],
      'prefix_denominators':[str(q.denominator) for q in prefix],
      'negative_total_coefficient_index':91,
      'quartet_lambda_91_approx':float(q91),
      'strict_upper_bound_lambda_91_approx':float(upper),
      'upper_bound_exact_numerator':str(upper.numerator),
      'upper_bound_exact_denominator':str(upper.denominator),
      'novelty_claim':False,
      'arithmetic_zeta_conclusion':None,
    }
    out=Path(__file__).resolve().parents[1]/'results'/'li_advocate_exact.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if 'numerator' not in k and 'denominator' not in k},indent=2))
if __name__=='__main__': main()
