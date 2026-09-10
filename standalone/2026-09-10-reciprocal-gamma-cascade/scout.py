#!/usr/bin/env python3
"""NON-CERTIFYING numerical scout. Requires mpmath; no accepting zero test.

Two high-precision quadrature grids evaluate the same defining density.
No outward primitive or quadrature error is enclosed. Agreement is diagnostic,
not proof of a nonreal zero or an exhaustive zero census. No zeta oracle is used.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from math import factorial
from pathlib import Path
import json
import mpmath as mp


def density(N):
    rows=[]
    for n in range(1,N+1):
        b=Fraction(2*factorial(N)**2,factorial(N-n)*factorial(N+n))**2
        c=1-2*n*n*sum((Fraction(1,k*k-n*n) for k in range(1,N+1) if k!=n),Fraction(0))
        rows.append((n,mp.mpf(b.numerator)/b.denominator,mp.mpf(c.numerator)/c.denominator))
    return lambda x:mp.fsum(b*n*n*(n*n*x+c-1)*mp.exp(-n*n*x) for n,b,c in rows)


def samples(N,order,cells,cutoff=3):
    roots,weights=mp.gauss_quadrature(order,'legendre')
    f=density(N); out=[]
    for j in range(cells):
        a=mp.mpf(cutoff)*j/cells; b=mp.mpf(cutoff)*(j+1)/cells
        mid=(a+b)/2; half=(b-a)/2
        for r,w in zip(roots,weights):
            t=mid+half*r
            x=mp.pi*mp.exp(2*t); y=mp.pi*mp.exp(-2*t)
            p,q=f(x),f(y)
            if p<=0 or q<=0:raise ArithmeticError('Cancellation lost density positivity: increase precision')
            out.append((t,half*w*mp.sqrt(p*q)))
    return out


def transform(data):
    total=mp.fsum(w for t,w in data)
    return lambda z:mp.fsum(w*mp.cos(z*t) for t,w in data)/total


def run():
    mp.mp.dps=90
    data1=samples(4,160,1)
    data2=samples(4,32,12)
    f1,f2=transform(data1),transform(data2)
    start=(mp.mpc('28.05','2.62'),mp.mpc('28.06','2.62'))
    z1=mp.findroot(f1,start,tol=mp.mpf('1e-70'))
    z2=mp.findroot(f2,start,tol=mp.mpf('1e-70'))
    dec=lambda v:mp.nstr(v,50)
    tracks={}
    for N in [1,2,4,8,16]:
        data=data1 if N==4 else samples(N,96,1)
        ff=transform(data)
        seed={1:'11.87',2:'12.74',4:'13.37',8:'13.72',16:'13.91'}[N]
        z=mp.findroot(ff,(mp.mpf(seed)-mp.mpf('.02'),mp.mpf(seed)+mp.mpf('.02')),tol=mp.mpf('1e-55'),maxsteps=60)
        tracks[str(N)]=dec(z)
    return {
        'status':'EXPLORATORY_NON_DIRECTED_NO_ZERO_CERTIFICATE',
        'mpmath_version':mp.__version__,
        'decimal_precision':90,
        'quadrature_cutoff':3,
        'grids':[{'order':160,'cells':1},{'order':32,'cells':12}],
        'apparent_N4_root_single':{'real':dec(z1.real),'imag':dec(z1.imag)},
        'apparent_N4_root_composite':{'real':dec(z2.real),'imag':dec(z2.imag)},
        'root_disagreement':dec(abs(z1-z2)),
        'composite_residual_at_own_root':dec(abs(f2(z2))),
        'single_residual_at_composite_root':dec(abs(f1(z2))),
        'tracked_first_real_roots':tracks,
        'quadrature_error_certified':False,
        'primitive_rounding_certified':False,
        'root_count_certified':False,
        'complete_zero_census':False,
        'zeta_oracle_used':False,
        'rh_proved':False
    }

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.write_text(json.dumps(run(),sort_keys=True,indent=2)+'\n')
    print('SCOUT_COMPLETE_NOT_A_CERTIFICATE')
