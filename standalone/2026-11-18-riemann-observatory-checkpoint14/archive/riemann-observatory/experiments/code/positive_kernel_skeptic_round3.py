#!/usr/bin/env python3
"""Exact rational sanity checks supporting the accompanying independent proof.
These checks do not replace the infinite-product, probability, or Li proofs.
Python standard library only; no floating-point arithmetic.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

def harmonic(n):
    return sum((F(1,j) for j in range(1,n+1)), F())

def divisor_direct(n):
    return sum(n//j for j in range(1,n+1))

def divisor_hyperbola(n):
    m=isqrt(n)
    return 2*sum(n//j for j in range(1,m+1))-m*m

def main():
    # gamma < H_64-log64; log2 > 2*(1/3+1/(3*3**3)+1/(5*3**5)).
    log2_lower=2*sum((F(1,(2*k+1)*3**(2*k+1)) for k in range(3)),F())
    d_lower=harmonic(13)/2-harmonic(64)-1+6*log2_lower
    assert d_lower>0
    count_checks=[]
    for n in range(1,2001):
        assert divisor_direct(n)==divisor_hyperbola(n)
    for N in [1,2,5,10,25,50,100]:
        a=F(1,100*N*5**N)
        perturb=F(16,3)*a*a*N*5**(N-1)
        assert perturb<F(1,1152)
        assert F(1,576)-perturb>F(1,1152)
        count_checks.append({'N':N,'a':str(a),'li_perturbation_upper':str(perturb),
                             'li_baseline_lower':str(F(1,576)),
                             'li_result_lower':str(F(1,1152))})
    out={'status':'all exact rational checks passed','arithmetic':'fractions.Fraction and integers',
         'd_positive_lower':str(d_lower),'log2_strict_lower':str(log2_lower),
         'divisor_identity_checked_integer_Y':[1,2000],
         'finite_li_examples':count_checks,
         'limitations':'Checks support constants; see audit for analytic proof and exact scope.'}
    p=(Path(__file__).resolve().parents[1]/'results'/'positive_kernel_skeptic_round3.json')
    p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'d_positive_lower':str(d_lower),'output':str(p)}))
if __name__=='__main__': main()
