#!/usr/bin/env python3
"""Uncertified finite high-precision quadrature checks, not an infinite census."""
from __future__ import annotations
import json
from pathlib import Path
import sys
import mpmath as mp
sys.path.insert(0,str(Path(__file__).resolve().parent))
import check as exact

mp.mp.dps=55

def mm(f):
    return mp.mpf(f.numerator)/f.denominator

def channel_case(m:int,profile:str,D:int)->dict:
    p,q=7,13
    Lp=exact.norm_local(p,m,profile,False)
    Lq=exact.norm_local(q,m,profile,False)
    # Complete finite common-core fixture: e_p,e_q in {0,1,m}, and
    # one common factor 19^e with e in {0,1,2}. No unlisted cores are included.
    Lr=exact.norm_local(19,m,profile,False)
    records=[]
    for i in (0,1,m):
        for j in (0,1,m):
            for er in (0,1,2):
                k=p**i*q**j*19**er
                pp=exact.mul(Lp.get(i+1,exact.ZERO),exact.conj(Lp.get(i,exact.ZERO)))
                qq=exact.mul(Lq.get(j,exact.ZERO),exact.conj(Lq.get(j+1,exact.ZERO)))
                zz=exact.scale(exact.mul(pp,qq),exact.norm2(Lr.get(er,exact.ZERO)))
                if zz[1] != 0 or zz[0]<0:
                    raise RuntimeError('finite exact sign mismatch')
                coefficient=mp.mpf(zz[0])/(p*q*k*k)
                if coefficient:
                    records.append((mp.log(p*k),mp.log(q*k),coefficient))
    c=mp.mpf(5)/6; beta=2*c-1; top=mp.log(D)
    kappa=mp.exp(beta*beta/2)/(2*mp.sqrt(2*mp.pi))
    Phi=lambda x:mp.erfc(-x/mp.sqrt(2))/2
    kernel=mp.fsum(g*kappa*mp.exp(-(a+b)/2-(a-b)**2/8)*Phi(top-(a+b)/2-beta)
                   for a,b,g in records)
    def integrand(x):
        return mp.fsum(g*mp.exp(beta*x-c*(a+b)-((x-a)**2+(x-b)**2)/4)/(4*mp.pi)
                       for a,b,g in records)
    # Centers of the completed squares are used only to help quadrature;
    # the integrand itself is the uncompleted physical Gaussian expression.
    breaks=[mp.ninf]+sorted(set([mp.mpf(0),top]+[
        (a+b)/2+beta for a,b,_ in records if 0<(a+b)/2+beta<top]))
    quad=mp.quad(integrand,breaks)
    err=abs(quad-kernel)/max(1,abs(kernel))
    if err>mp.mpf('1e-40'):
        raise RuntimeError('quadrature/kernel mismatch')
    return {'m':m,'profile':profile,'D':D,'nonzero_common_core_terms':len(records),
            'finite_kernel':mp.nstr(kernel,25),'finite_quadrature':mp.nstr(quad,25),
            'relative_discrepancy_below_1e_40':True}

if __name__=='__main__':
    out={'status':'PASS','precision_digits':55,'certified_intervals':False,
         'scope':'Finite common-core fixtures only; no infinite tail or asymptotic validation.',
         'cases':[channel_case(4,'unit',64),channel_case(4,'complex',4096),
                  channel_case(6,'complex',100000)]}
    print(json.dumps(out,indent=2,sort_keys=True))
