#!/usr/bin/env python3
"""Ordinary mpmath checks of HBR28 analytic identities; NOT certificates.

The two precisions share one backend. No directed rounding, proven integral
remainder, zero isolation, or continuum coverage is claimed.
"""
from __future__ import annotations
import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
import mpmath as mp


def d_coeff(k: int) -> list[int]:
    d=[1]
    for ell in range(1,k):
        nxt=[0]*(len(d)+1)
        for j,c in enumerate(d):
            nxt[j]-=ell*ell*c
            nxt[j+1]+=c
        d=nxt
    return d


def B_coeff(m: int) -> list[Fraction]:
    out=[Fraction(0)]*m
    for k in range(1,m+1):
        a=Fraction(math.comb(m-1,k-1)*2**(2*k),math.factorial(2*k-1))
        for j,c in enumerate(d_coeff(k)):
            out[j]+=a*c
    return out


def xi(s):
    if s==0 or s==1:
        return mp.mpf('0.5')
    if mp.re(s)<mp.mpf('0.5'):
        s=1-s
    return s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)/2


def R(j: int,s):
    if j==0:
        return mp.power(2,-s)-1
    if s==-2*j:
        return mp.power(mp.pi,-j)*(2*j)*mp.log(2)*2**(2*j)*mp.rf(mp.mpf('1.5'),j)
    return mp.power(mp.pi,-j)*s/(s+2*j)*mp.rf((3-s-2*j)/2,j)*(mp.power(2,-s)-2**(2*j))


def shifted(m: int,s):
    return mp.power(mp.mpf(2)/3,m)/4*sum(
        (mp.mpf(c.numerator)/c.denominator)*R(j,s)*xi(s+2*j)
        for j,c in enumerate(B_coeff(m)))


def integral(m: int,q):
    fun=lambda u: mp.power(u,1-2*q)*mp.tanh(u)**(2*m-2)/mp.cosh(u)**2 if u else mp.mpf(0)
    val=mp.quad(fun,[0,mp.mpf('.25'),1,3,8,mp.inf])
    return mp.power(mp.mpf(2)/3,m)*mp.power(mp.pi/4,q)*mp.rgamma(-q)*val


def run(dps: int) -> dict:
    mp.mp.dps=dps
    cases=[]
    for m in range(1,7):
        for re,im in [('-0.4','0.7'),('0.15','1.25'),('0.35','4.1')]:
            q=mp.mpc(re,im)
            left=integral(m,q)
            right=shifted(m,2*q)
            rel=abs(left-right)/max(abs(left),abs(right),mp.mpf('1e-100'))
            if not rel<mp.power(10,-dps+15):
                raise ValueError(f'shift identity discrepancy m={m}, q={q}: {rel}')
            cases.append({'m':m,'q_re':re,'q_im':im,'relative_discrepancy':mp.nstr(rel,12),
                          'G_re':mp.nstr(mp.re(left),35),'G_im':mp.nstr(mp.im(left),35)})
    removable=[]
    for j in range(1,7):
        s=-2*j
        extrap=R(j,s+mp.mpf('1e-20'))
        val=R(j,mp.mpf(s))
        err=abs(extrap-val)/max(abs(val),mp.mpf('1e-100'))
        if not err<mp.mpf('1e-18'):
            raise ValueError('removable coefficient check failed')
        removable.append(mp.nstr(err,12))
    # Normalization at q=m: moment exponent is zero.
    integer=[]
    for m in range(1,7):
        target=mp.power(mp.pi/6,m)*(-1)**m*math.factorial(m)/2
        err=abs(shifted(m,mp.mpf(2*m))-target)/abs(target)
        if not err<mp.power(10,-dps+15):
            raise ValueError('integer normalization discrepancy')
        integer.append(mp.nstr(err,12))
    return {'dps':dps,'mpmath_version':mp.__version__,'complex_integral_cases':cases,
            'removable_coefficients_relative_discrepancies':removable,
            'integer_normalization_relative_discrepancies':integer,
            'maximum_integral_relative_discrepancy':mp.nstr(max(mp.mpf(c['relative_discrepancy']) for c in cases),12)}


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dps',type=int,default=70)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if not 40<=a.dps<=200:
        ap.error('--dps must be in [40,200]')
    result={'status':'ordinary floating diagnostics only; not a proof or zero certificate', 'result':run(a.dps)}
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print('DIAGNOSTIC PASS',a.dps,'digits, 18 integral pairs; max relative discrepancy',result['result']['maximum_integral_relative_discrepancy'])

if __name__=='__main__':
    main()
