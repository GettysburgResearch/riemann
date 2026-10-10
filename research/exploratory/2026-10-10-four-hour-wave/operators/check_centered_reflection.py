#!/usr/bin/env python3
"""Exact rational checks for the centered parity coercivity constants.

The source/reflection proof is in CENTERED_REFLECTION_REDUCTION.md. This
checker pays no new numerical phase sweep: its precondition is the separately
reviewed global supporting line P V_2 >= (4/5)x-244.
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path


def require(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def exact(value):
    return str(value.numerator) + '/' + str(value.denominator)


def run():
    b=F(3,2)
    pi=F(6283,2000)
    alpha=F(4,5)
    cost=F(244)
    k_even=b*(alpha-cost/(7*pi)**2)
    k_odd=b*(alpha-cost/(6*pi)**2)
    require(k_even>F(2,5),'even primitive coercivity exceeds2/5')
    require(k_odd>F(1,6),'odd primitive coercivity exceeds1/6')
    require(b*b/F(2,5)==F(45,8),'even residual coefficient')
    require(b*b/F(1,6)==F(27,2),'odd residual coefficient')
    m=5
    even=2+sum(j%2==1 for j in range(1,m+1))
    odd=1+sum(j%2==0 for j in range(1,m+1))
    require((even,odd)==(5,3),'centered complement dimensions5+3')
    return {'status':'CENTERED_PARITY_CONSTANTS_ACCEPT',
      'scope':'conditional on reviewed supporting line and source/reflection identities',
      'length':'1','removed_sines':m,'even_dimension':even,'odd_dimension':odd,
      'pi_lower':exact(pi),'even_primitive_kappa_lower':exact(k_even),
      'odd_primitive_kappa_lower':exact(k_odd),'reported_even_kappa':'2/5',
      'reported_odd_kappa':'1/6','even_residual_cost':'45/8',
      'odd_residual_cost':'27/2','finite_effective_sign':'not certified',
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();result=run()
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
