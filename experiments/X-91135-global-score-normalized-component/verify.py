#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt
import json
from pathlib import Path

DEN=10**70


def sqrt_interval(n):
    lo=isqrt(n*DEN*DEN)
    hi=lo if lo*lo==n*DEN*DEN else lo+1
    return Fraction(lo,DEN),Fraction(hi,DEN)


def invsqrt_interval(n):
    lo,hi=sqrt_interval(n)
    return Fraction(1,hi),Fraction(1,lo)


def log_interval(x,terms=180):
    exponent=0
    y=x
    while y>=2:
        y/=2;exponent+=1
    while y<1:
        y*=2;exponent-=1
    def base(z):
        z2=z*z;power=z;partial=Fraction(0)
        for k in range(terms):
            partial += power/Fraction(2*k+1)
            power *= z2
        partial*=2
        tail=2*power/(Fraction(2*terms+1)*(1-z2))
        return partial,partial+tail
    lo,hi=base((y-1)/(y+1))
    l2lo,l2hi=base(Fraction(1,3))
    if exponent>=0:return lo+exponent*l2lo,hi+exponent*l2hi
    return lo+exponent*l2hi,hi+exponent*l2lo


def main():
    log83_lo,_=log_interval(Fraction(83))
    minimum=None
    for j in range(2,67):
        c=Fraction(2,j*(j-1))
        h_lo=Fraction(0);hlog_hi=Fraction(0)
        for m in range(1,j):
            inv_lo,inv_hi=invsqrt_interval(m)
            h_lo += inv_lo
            l_lo,l_hi=log_interval(Fraction(m))
            hlog_hi += inv_hi*l_hi
        sj_lo,sj_hi=sqrt_interval(j)
        sj1_lo,sj1_hi=sqrt_interval(j+1)
        a_lo=Fraction(j+2,j)/sj_hi
        a_hi=Fraction(j+2,j)/sj_lo
        b_lo=Fraction(1,1)/sj1_hi
        b_hi=Fraction(1,1)/sj1_lo
        eta_lo=c*(1+h_lo)-a_hi+b_lo
        assert eta_lo>0
        lj_lo,_=log_interval(Fraction(j))
        _,lj1_hi=log_interval(Fraction(j+1))
        K_hi=-4*c+c*hlog_hi-a_lo*lj_lo+b_hi*lj1_hi
        bracket=5*eta_lo*log83_lo-22*c-10*eta_lo-5*K_hi
        assert bracket>0,(j,bracket)
        record=(bracket,j,eta_lo,K_hi)
        if minimum is None or record[0]<minimum[0]:minimum=record
    result={
      'classification':'PASS_GLOBAL_SCORE_NORMALIZED_COMPONENT_MONOTONICITY_REDUCTION',
      'rows_checked':65,
      'large_Y_start':83,
      'minimum_row':minimum[1],
      'minimum_bracket_lower':str(minimum[0]),
      'minimum_bracket_decimal':float(minimum[0]),
      'eta_lower_at_minimum':str(minimum[2]),
      'K_upper_at_minimum':str(minimum[3]),
      'scope':(
        'Exact Fraction arithmetic and directed square-root/logarithm intervals '
        'certify the 65 fixed large-Y gates. Together with the imported finite '
        'window theorem and the analytic inequalities in L-91359, this proves '
        'global single-endpoint score-normalized component monotonicity. It does '
        'not prove bounded-inner causal monotonicity, the full determinant, or RH.'),
    }
    out=Path(__file__).resolve().parent/'results'/'verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['classification']);print(out)

if __name__=='__main__':main()
