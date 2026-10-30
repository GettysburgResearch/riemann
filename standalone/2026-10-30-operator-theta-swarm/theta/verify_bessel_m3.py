#!/usr/bin/env python3
"""Exact rational interval signs for actual theta-sampled M=3 impedances.

Reuses the checked interval primitives from verify_polya_obstruction.py;
all source theta tails and modified-Bessel series tails are bounded here.
This proves success/failure of one sufficient boundary criterion, not RH.
"""
import contextlib,io,runpy,json
from fractions import Fraction as F
from math import isqrt,factorial
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    dep=runpy.run_path(str(Path(__file__).with_name('verify_polya_obstruction.py')))
I=dep['I']; PI=dep['PI']; expi=dep['exp_interval'];Q=dep['Q']

def root_interval(x,n=2):
    def floorroot(t):
        v=(t*Q**n).numerator//(t*Q**n).denominator
        if n==2:return isqrt(v)
        if n==4:return isqrt(isqrt(v))
        raise ValueError(n)
    return I(F(floorroot(x.lo),Q),F(floorroot(x.hi)+1,Q))

def source(x):
    x=I(x);Y=x+root_interval(1+x*x);Y4=root_interval(Y,4)
    value=I(0)
    for n in range(1,5):
        value+=(4*PI**2*n**4*Y**2-6*PI*n*n*Y)*Y4*expi(-PI*n*n*Y)
    # Positive source tail. For n>=5, each term <=40*n^4*Y^(9/4)*exp(-3*n^2*Y).
    # Adjacent-bound ratio <=(6/5)^4*exp(-33)<1/2 since Y>=1.
    tail=80*5**4*Y**2*Y4*expi(-75*I(Y.lo))
    return I(value.lo,value.hi+tail.hi)

def ibessel(n,a):
    term=(a/2)**n/F(factorial(n)); s=term
    for k in range(1,181):
        term*=a*a/(4*k*(n+k));s+=term
    nxt=term*a*a/(4*181*(n+181))
    ratio=a*a/(4*182*(n+182))
    if not 0<=ratio<1:raise ArithmeticError('Bessel tail ratio')
    return I(s,s+nxt/(1-ratio))

def sign_one(a):
    c=[ibessel(n,a)*source(F(n)/a) for n in range(4)]
    c=[v/c[0] for v in c]
    c0,c1,c2,c3=c
    A0=c0+2*c2+8*c3/a;A1=4*c2/(a*a)+24*c3/(a**3)
    B0=2*c1+4*c2/a+2*c3+16*c3/(a*a);B1=8*c3/(a*a)
    Delta=A0*B1-A1*B0
    wanted='positive' if a>=20 else 'negative'
    if wanted=='positive' and not Delta.lo>0:raise ArithmeticError(('wrong sign',a))
    if wanted=='negative' and not Delta.hi<0:raise ArithmeticError(('wrong sign',a))
    for v in c:
        if not v.lo>0:raise ArithmeticError('coefficient positivity')
    return {'a':str(a),'M':3,'coefficients_normalized_by_c0':True,
            'Delta_definition':'(c0+2*c2+8*c3/a)*(8*c3/a^2) - (4*c2/a^2+24*c3/a^3)*(2*c1+4*c2/a+2*c3+16*c3/a^2)',
            'Delta_lower_rational':str(Delta.lo),'Delta_upper_rational':str(Delta.hi),
            'Delta_lower_float_display':float(Delta.lo),'Delta_upper_float_display':float(Delta.hi),
            'strict_sign':wanted,'sufficient_positive_boundary_gate':wanted=='negative'}

rows=[sign_one(a) for a in [F(1,4),F(1,2),F(1),F(2),F(5),F(10),F(20),F(50)]]
print(json.dumps({'status':'PASS','arithmetic':'rational outward intervals; full theta and Bessel tails bounded',
                  'criterion_orientation':'Delta<0 gives positive residue; Delta>0 gives negative residue',
                  'rows':rows,
                  'scope':'exact signs for finite M=3 actual source approximants; no RH, no global cofinal result; failed sufficient gate does not imply nonreal zeros'},indent=2))
