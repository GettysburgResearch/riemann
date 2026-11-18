#!/usr/bin/env python3
"""An exact witness for the printed unit-step geometric-majorant problem.
It concerns |(1+1/s)^n|*2^-Re(s), not the oscillatory L'/L itself.
Standard library only; no floating point or transcendental evaluation.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

def main():
    n=10000; sigma=3
    # T in[100,101], y=T² in[10000,10201]. For s=3+iT,
    # |1+1/(s+1)|² / |1+1/s|² =1+(2y-31)/(y+16)².
    epsilon_lower=F(2*10000-31,(10201+16)**2)
    assert epsilon_lower>F(1,6000)
    binomial_lower=1+F(n,6000)+F(comb(n,2),6000**2)
    assert binomial_lower==F(9733,2400)>4
    # Therefore squared kernel ratio>4, so kernel ratio>2 and the
    # product envelope with the Dirichlet decay factor1/2 increases.
    # For the alternate T>=2sqrt n: exp(n/T²)<=exp(1/4)<4/3,
    # using exp(x)<1/(1-x) at0<x<1; resulting envelope ratio<2/3.
    repaired_ratio_upper=F(1,2)/(1-F(1,4))
    assert repaired_ratio_upper==F(2,3)<1
    out={'status':'exact witness passed','n':n,'sigma':sigma,
         'T_interval':['100','101'],'kernel_ratio_squared_lower':str(binomial_lower),
         'kernel_ratio_squared_lower_exceeds':'4',
         'inner_increment_lower':str(epsilon_lower),
         'repaired_envelope_ratio_strict_upper':str(repaired_ratio_upper),
         'scope':'Proves increase of the supplied absolute majorant under original height; does not prove increase of the actual oscillatory L derivative, or falsity of the final theorem.'}
    p=Path('/workspace/riemann-observatory/experiments/results/lagarias_contour_majorant_exact_round3.json')
    p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
