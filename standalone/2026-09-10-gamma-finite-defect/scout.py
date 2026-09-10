#!/usr/bin/env python3
"""NONCERTIFYING centered-fourth-stage root scout; not an accepting program.

mpmath primitives and Gaussian quadrature are not outward enclosures. Two grids
use one primitive backend. No global census, Rouché count, or xi zero is claimed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
import mpmath as mp

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    mp.mp.dps=120;N=4;m=8;B=16
    to_mp=lambda q:mp.mpf(q.numerator)/q.denominator
    rows=[]
    for n in range(1,N+1):
        b=Q(2*factorial(N)**2,factorial(N-n)*factorial(N+n))**2
        c=1-2*n*n*sum((Q(1,k*k-n*n) for k in range(1,N+1) if k!=n),Q(0))
        rows.append((n,to_mp(b),to_mp(c)))
    hs=[Q(1)]+[Q(0)]*96
    for a in [B-n*n for n in range(1,N+1) for _ in range(2)]:
        for k in range(1,len(hs)):hs[k]+=a*hs[k-1]
    coeff=[to_mp(hs[k]*factorial(m-1)/Q(factorial(m+k-1))) for k in range(len(hs))]
    a0=mp.mpf(factorial(N)**4)/factorial(m-1)
    def f(x):
        if x<mp.mpf(1)/16:
            return a0*x**7*mp.exp(-16*x)*mp.polyval(list(reversed(coeff)),x)
        return mp.fsum(b*n*n*(n*n*x+c-1)*mp.exp(-n*n*x) for n,b,c in rows)
    tau=mp.pi**2/3-mp.mpf(205)/72;T=mp.log(mp.pi/tau)/2
    def grid(order,cells):
        roots,weights=mp.gauss_quadrature(order,'legendre');data=[]
        for j in range(cells):
            a=mp.pi*j/(2*cells);b=mp.pi*(j+1)/(2*cells)
            for r,w in zip(roots,weights):
                theta=(a+b)/2+(b-a)*r/2;t=T*mp.sin(theta)
                x=mp.pi*mp.exp(2*t)-tau;y=mp.pi*mp.exp(-2*t)-tau
                fx,fy=f(x),f(y)
                if fx<=0 or fy<=0:raise ArithmeticError('positive density lost to scout rounding')
                data.append((t,w*(b-a)/2*T*mp.cos(theta)*mp.sqrt(fx*fy)))
        Z=mp.fsum(w for t,w in data)
        return lambda z:mp.fsum(w*mp.cos(z*t) for t,w in data)/Z
    grids=[(32,6),(40,8)];functions=[grid(*g) for g in grids]
    seed=mp.mpc('30.44805680701155406000392','0.6599780503713255679275726')
    roots=[mp.findroot(F,(seed,seed+mp.mpf('.001')),tol=mp.mpf('1e-95'),maxsteps=30) for F in functions]
    dec=lambda x:mp.nstr(x,65)
    result={'status':'EXPLORATORY_NON_DIRECTED_NO_ROOT_COUNT',
            'source':'exact centered N=4 gamma construction','N':N,'precision_digits':120,
            'mpmath_version':mp.__version__,'quadrature_grids':[{'order':a,'cells':b} for a,b in grids],
            'tau':dec(tau),'T':dec(T),
            'apparent_roots':[{'real':dec(z.real),'imag':dec(z.imag)} for z in roots],
            'disagreement':dec(abs(roots[0]-roots[1])),
            'cross_grid_residual':dec(abs(functions[1](roots[0]))),
            'derivative_second_grid':{'real':dec(mp.diff(functions[1],roots[1]).real),
                                      'imag':dec(mp.diff(functions[1],roots[1]).imag)},
            'density_small_argument_method':'positive tilted simplex series, 97 terms; nondirected',
            'outward_arithmetic':False,'quadrature_error_certified':False,'root_count_certified':False,
            'complete_nonreal_census':False,'actual_xi_zero':False,'rh_proved':False}
    args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('SCOUT_FINISHED_NOT_A_CERTIFICATE')

if __name__=='__main__':main()
