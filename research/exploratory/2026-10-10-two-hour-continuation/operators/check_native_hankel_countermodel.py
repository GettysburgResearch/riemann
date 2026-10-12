#!/usr/bin/env python3
"""Exact rational synthetic obstruction to all scalar signs implying RH."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as Q

def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def inv(x):
    d=x[0]**2+x[1]**2
    return x[0]/d,-x[1]/d

def power(x,n):
    v=(Q(1),Q(0))
    for _ in range(n):v=mul(v,x)
    return v

def require(c,s):
    if not c:raise ArithmeticError(s)

def run():
    r=(Q(100),Q(1,2));x=inv(mul(r,r));x0=Q(1,225);target=mul((Q(0),Q(1)),r)
    v=mul(target,inv((x[0]-x0,x[1])));B=v[1]/x[1];A=v[0]-B*x[0]
    coef=[-x0*A,A-x0*B,B]
    def evaluate(z):
        ans=(Q(0),Q(0))
        for k,c in enumerate(coef):ans=add(ans,mul((c,Q(0)),power(z,k)))
        return ans
    require(evaluate((x0,Q(0)))==(Q(0),Q(0)),'real node annihilated')
    require(evaluate(x)==target,'exact complex interpolation')
    require(mul(x,mul(target,target))==(Q(-1),Q(0)),'exact negative complex contribution')
    def p(k):return x0**k+2*power(x,k)[0]
    contraction=sum(coef[i]*coef[j]*p(i+j+1) for i in range(3) for j in range(3))
    require(contraction==-2,'complete negative Hankel form')
    require(2*Q(900,40001)<1,'all-order scalar domination')
    require(all(p(k)>0 for k in range(1,65)),'first64 exact scalar signs')
    return {'status':'EXACT_SYNTHETIC_ALL_SCALAR_SIGN_OBSTRUCTION_PASS','root_representatives':['15','100+i/2','100-i/2'],
       'classical_vertical_strip_halfwidth':'1/2','minimum_real_root_height':'15',
       'quadratic_coefficients':[str(c) for c in coef],'complete_hankel_quadratic_form':'-2',
       'scalar_signs':'strictlypositiveforALLk>=1bygeometricdomination','exact_scalar_controls':64,
       'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'not_proved':['actual-Xi native Hankel positivity','RH']}
if __name__=='__main__':print(json.dumps(run(),indent=2))
