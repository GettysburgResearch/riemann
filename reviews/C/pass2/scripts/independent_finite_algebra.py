#!/usr/bin/env python3
"""Independent symbolic coefficient check; no imported research implementation.

Variables represent commuting weighted dilation operators, not prime data.
Finite ranks 0..8 corroborate the separately written all-finite induction.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def product_minus_variables(n):
    p={():1}
    for j in range(n):
        nxt=defaultdict(int)
        for mon,coef in p.items():
            nxt[mon]+=coef;nxt[mon+(j,) ]-=coef
        p=dict(nxt)
    return p

def owner_expansion(n):
    # Every nonempty squarefree monomial has a unique largest variable.
    p=defaultdict(int);p[()]=1
    for owner in range(n):
        for mask in range(1<<owner):
            mon=tuple(j for j in range(owner) if (mask>>j)&1)+(owner,)
            p[mon]+= -1 if mask.bit_count()%2==0 else 1
    return dict(p)

def main():
    checks=[]
    for n in range(9):
        left=product_minus_variables(n);right=owner_expansion(n)
        if left!=right: raise ValueError('symbolic owner identity failed')
        checks.append({'rank':n,'coefficient_count':len(left),'equal':True})
    # Independently expand 5(2a-1-b)+(5b-a-1-3a²), coefficient by coefficient.
    p2={(1,0):2,(0,0):-1,(0,1):-1}
    three_p3={(0,1):5,(1,0):-1,(0,0):-1,(2,0):-3}
    lhs=defaultdict(int)
    for m,c in p2.items(): lhs[m]+=5*c
    for m,c in three_p3.items(): lhs[m]+=c
    lhs={m:c for m,c in lhs.items() if c}
    rhs=defaultdict(int)
    for i,a in ((1,1),(0,-1)):
        for j,b in ((1,1),(0,-2)):rhs[(i+j,0)]+=-3*a*b
    if dict(rhs)!=lhs:raise ValueError('five-three polynomial identity failed')
    # Sufficient error sign: R >= -M + bound, |E| <= bound => M+E+R >=0.
    # The weaker R >= -M - bound is not sufficient.
    M=Fraction(2);bound=Fraction(1);E=-bound;R=-M-bound
    if not M+E+R<0:raise ValueError('wrong-sign control failed')
    data={'arithmetic_class':'EXACT_INTEGER_POLYNOMIAL_AND_RATIONAL',
          'finite_owner_checks':checks,'total_owner_coefficients':sum(x['coefficient_count'] for x in checks),
          'five_three_coefficients':{str(k):v for k,v in sorted(lhs.items())},
          'optional_abs_error_bound_requires_positive_sign':True,
          'bad_sign_counterexample':{'M':str(M),'E':str(E),'bound':str(bound),'R':str(R),'sum':str(M+E+R)},
          'native_annular_source_recomputed':False,'PNT_or_Mertens_proved':False,'RH_proved':False}
    (ROOT/'reports/independent_finite_algebra.json').write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'finite_ranks':9,'coefficient_checks':data['total_owner_coefficients'],'five_three_identity':True,'RH_proved':False}))
if __name__=='__main__':main()
