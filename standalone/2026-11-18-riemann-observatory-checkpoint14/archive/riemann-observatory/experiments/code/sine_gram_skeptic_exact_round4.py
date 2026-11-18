#!/usr/bin/env python3
"""Exact algebra checks accompanying the sine-Gram review, not a stochastic simulation."""
from fractions import Fraction as F
from math import factorial,comb
from pathlib import Path
import json

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def main():
    p=[F(1),F(-7,4),F(2,3)]; p2=mul(p,p)
    q=[-x for x in p2];q[0]+=1
    moments=[F(1),F(1),F(4,3),F(2),F(13,4)]
    Ep2=sum(x*y for x,y in zip(p2,moments))
    Eq=sum(x*y for x,y in zip(q,moments))
    assert Ep2==F(5,36) and Eq==F(31,36)
    assert sum(p[j]*moments[j+1] for j in range(3))==0
    assert sum(p[j]*moments[j+2] for j in range(3))==0
    # (p')²=(8/3)(p+19/128), exact polynomial identity.
    dp=[p[1],2*p[2]]
    assert mul(dp,dp)==[F(8,3)*(p[0]+F(19,128)),F(8,3)*p[1],F(8,3)*p[2]]
    # On active |p|<=sqrt2<3/2, (q')²<(64/3)(3/2+19/128)=211/6<36.
    derivative_square_upper=F(64,3)*(F(3,2)+F(19,128))
    assert derivative_square_upper==F(211,6)<36
    bells=[1]
    for n in range(1,31):bells.append(sum(comb(n-1,k)*bells[k] for k in range(n)))
    assert all(bells[n]<=factorial(n) for n in range(1,31))
    out={'status':'exact arithmetic checks passed','p_coefficients':[str(x) for x in p],
         'q_coefficients':[str(x) for x in q],'integral_p_squared':str(Ep2),
         'integral_q':str(Eq),'simple_charge_lower':str(2*Eq-1),
         'clipped_q_global_Lipschitz_bound':6,'active_derivative_square_upper':str(derivative_square_upper),
         'Bell_factorial_checked_orders':[1,30],
         'scope':'Polynomial and finite combinatorial bookkeeping only. The uniform moment bound, Riesz input, no-atom theorem and limiting claims are analytic proofs in the audit.'}
    f=Path('/workspace/riemann-observatory/experiments/results/sine_gram_skeptic_exact_round4.json')
    f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
