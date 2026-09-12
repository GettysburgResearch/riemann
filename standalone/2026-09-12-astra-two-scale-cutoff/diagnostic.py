#!/usr/bin/env python3
"""NONCERTIFYING DDE/quadrature diagnostics for HBR29.

The origin is initialized with its leading Taylor term, the real r tail is
truncated, and no interval error bounds are attached to ODE or quadrature.
At c=2047 the binary64 epsilon underflows to zero. None of these values enters
mathematical acceptance in check.py; hashes bind retained exploration only.
"""
from __future__ import annotations
import argparse
import bisect
import json
import math
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.special import gamma


def logcosh(x):
    return math.log1p(2*math.sinh(x/2)**2)


def compute(c: int, fine: bool):
    ell=math.log(2*c)
    eps=math.ldexp(1.0,-c) if c<1075 else 0.0
    delta=3*eps*c*(c+2)/(16-(6*c+16)*eps)
    r0=1e-4; rmax=2*ell+40
    segments=[]; ends=[]
    def history(r):
        if r<=r0: return delta*r*r/6
        k=min(bisect.bisect_right(ends,r),len(segments)-1)
        return float(segments[k](r)[0])
    def rhs(r,y):
        q=math.exp(-r/2)
        logb=logcosh(r/2)-2*logcosh(r/4)-math.log(2)
        logA=math.log(c)-math.log1p(-eps)+c*logb+math.log(q)-math.log1p(-q*q)
        A=math.exp(logA)
        B=c*eps/((1-eps)*math.sinh(r))
        lr=c*(logb+math.log(2))+logcosh(r/2)
        difference=B*math.expm1(lr) if B>0 and abs(lr)<0.1 else A-B
        return [difference-A*history(r/2)+B*y[0]]
    lo=r0; state=[delta*r0*r0/6]
    rtol=2e-12 if fine else 2e-10
    while lo<rmax:
        hi=min(2*lo,rmax)
        sol=solve_ivp(rhs,(lo,hi),state,method='DOP853',rtol=rtol,
                      atol=rtol/100,max_step=0.06 if fine else 0.15,dense_output=True)
        if not sol.success: raise RuntimeError(sol.message)
        segments.append(sol.sol); ends.append(hi); state=sol.y[:,-1]; lo=hi
    order=48 if fine else 24
    nodes,weights=np.polynomial.legendre.leggauss(order)
    ncell=math.ceil(rmax/0.25); step=rmax/ncell
    centers=(np.arange(ncell)+.5)*step
    r=(centers[:,None]+nodes[None,:]*step/2).ravel()
    qw=np.tile(weights*step/2,ncell)
    cdf=np.array([history(float(t)) for t in r])
    logtanh=np.log(-np.expm1(-r))-np.log1p(np.exp(-r))
    fc=np.exp(math.log(2*c)-r+(c-1)*logtanh-2*np.log1p(np.exp(-r)))
    panels=[]
    def pair(z): return [float(np.real(z)),float(np.imag(z))]
    for sigma in [0.,.5,1.]:
        for t in [0.,.5,1.]:
            s=complex(sigma,t*ell)
            comparison=np.sum(qw*fc*np.exp((1-s)*np.log(r/ell)))
            correction=np.sum(qw*c*fc*cdf*np.exp((1-s)*np.log(r/(2*ell))))
            native=comparison-2**(1-s)/c*correction
            panels.append({'sigma':sigma,'tau_over_ell':t,
              'normalized_comparison':pair(comparison),
              'normalized_native':pair(native),'sharp_scaled_correction':pair(correction),
              'gamma1':pair(gamma(1+1j*t)),'gamma2':pair(gamma(2+1j*t))})
    return {'c':c,'m':(c+1)//2,'ell':ell,'r_max':rmax,'quadrature_cells':ncell,
      'quadrature_order':order,'epsilon_underflowed':eps==0,
      'cdf_at_shifted_points':{str(x):history(2*ell+x) for x in [-4,0,4]},
      'cdf_at_r_max':history(rmax),'panels':panels}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--fine',action='store_true')
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    result={'status':'NONCERTIFYING_EXPLORATION','numpy':np.__version__,
      'scipy':scipy.__version__,'configuration':'fine' if args.fine else 'coarse',
      'omissions':['unbounded ODE/interpolation error','leading-term origin initialization',
                   'finite r tail','nondirected quadrature','binary64 epsilon underflow at c=2047'],
      'runs':[compute(c,args.fine) for c in [31,127,511,2047]]}
    args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print('NONCERTIFYING',result['configuration'],'36 complex panels')

if __name__=='__main__': main()
