#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path
import mpmath as mp

mp.mp.dps=120
ROOT=Path(__file__).resolve().parent

def e_integer(n:int)->mp.mpf:
    return 2*mp.fsum(1/mp.sqrt(k) for k in range(1,n+1))-4*mp.sqrt(n)+3

def decrement_closed(n:int)->mp.mpf:
    return 2/(mp.sqrt(n+1)*(mp.sqrt(n+1)+mp.sqrt(n))**2)

def dec_integrand(t:mp.mpf,n:int)->mp.mpf:
    if t==0:return mp.mpf('0')
    num=-mp.expm1(-t)-t*mp.e**(-t)
    return (2/mp.sqrt(mp.pi))*mp.e**(-n*t)*num/t**mp.mpf('1.5')

def decrement_integral(n:int)->mp.mpf:
    return mp.quad(lambda t:dec_integrand(t,n),[0,1,mp.inf])

def smooth_integral(y:mp.mpf)->mp.mpf:
    einf=3+2*mp.zeta(mp.mpf('0.5'))
    def f(t):
        if t==0:return mp.mpf('0')
        num=-mp.expm1(-t)-t*mp.e**(-t)
        den=-mp.expm1(-t)
        return (2/mp.sqrt(mp.pi))*mp.e**(-y*t)*num/(den*t**mp.mpf('1.5'))
    return einf+mp.quad(f,[0,1,mp.inf])

def smooth_hurwitz(y:mp.mpf)->mp.mpf:
    return 3+2*mp.zeta(mp.mpf('0.5'))-2*mp.zeta(mp.mpf('0.5'),y+1)-4*mp.sqrt(y)

def reset(y:mp.mpf)->mp.mpf:
    n=int(mp.floor(y))
    return 2*(mp.zeta(mp.mpf('0.5'),n+1)-mp.zeta(mp.mpf('0.5'),y+1))

def main()->None:
    maxerr=mp.mpf('0')
    for n in [1,2,3,5,13,31,100]:
        direct=e_integer(n)-e_integer(n+1)
        maxerr=max(maxerr,abs(direct-decrement_closed(n)),abs(direct-decrement_integral(n)))
        maxerr=max(maxerr,abs(smooth_integral(mp.mpf(n))-e_integer(n)))
        maxerr=max(maxerr,abs(smooth_hurwitz(mp.mpf(n))-e_integer(n)))
    if maxerr>=mp.mpf('1e-55'):raise AssertionError(maxerr)
    reset_checks=[]
    for n in [1,2,7,31]:
        for frac in ['0.125','0.5','0.875']:
            y=mp.mpf(n)+mp.mpf(frac)
            r=reset(y)
            if not (r>0 and r<2/mp.sqrt(n+1)):raise AssertionError((y,r))
            reset_checks.append((str(y),mp.nstr(r,50)))
    # Exact filter endpoint signs.
    if not ((3-4*mp.sqrt(mp.mpf(4))/mp.mpf(4))==1):raise AssertionError('left')
    if not ((3-4*mp.sqrt(mp.mpf(16))/mp.mpf(8))==1):raise AssertionError('left2')
    # Optimal hinge majorant and shell constants.
    for y in [-20,-1,0,6,7,12,50]:
        if max(mp.mpf(y)-6,0)>mp.mpf(y)**2/24+mp.mpf('1e-80'):raise AssertionError('hinge')
    cstar=3/mp.pi**2*(4*mp.log(2)+3*mp.sqrt(2)-6)
    if not (cstar>mp.mpf('0.3085') and cstar<mp.mpf('0.3087')):raise AssertionError(cstar)
    kappa=(16-6*mp.sqrt(2))/15
    # rho_*'(2)=1/kappa.
    rho_prime=15/(2*mp.sqrt(2)*(4*mp.sqrt(2)-3))
    if abs(rho_prime*kappa-1)>mp.mpf('1e-100'):raise AssertionError('kappa')
    # Coefficient-majorization controls for local fractional Euler factors.
    for tau in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('1.3')]:
        for m in [1,2]:
            for r in range(0,12):
                pos=mp.fprod(m*tau+j for j in range(r))/mp.factorial(r) if r else mp.mpf(1)
                neg=mp.fprod(j-m*tau for j in range(r))/mp.factorial(r) if r else mp.mpf(1)
                if abs(neg)>pos+mp.mpf('1e-100'):raise AssertionError((tau,m,r,pos,neg))
    alpha={1:mp.mpf(6),2:-9/mp.sqrt(2),4:mp.mpf(3)/2}
    def K(T,m,n):
        return mp.fsum(alpha[r]*alpha[s]*max(mp.log(T/max(r*m,s*n)),0) for r in alpha for s in alpha)
    gram=[[K(mp.mpf(1000),m,n) for n in [1,2,3,5]] for m in [1,2,3,5]]
    mineig=min(mp.eigsy(mp.matrix(gram),eigvals_only=True))
    if mineig<-mp.mpf('1e-70'):raise AssertionError(mineig)
    payload={
      'verdict':'PASS_T98070_NEGATIVE_MASS_EULER_HURWITZ_ALGEBRA',
      'max_identity_error':mp.nstr(maxerr,60),
      'e_infinity':mp.nstr(3+2*mp.zeta(mp.mpf('0.5')),60),
      'c_star':mp.nstr(cstar,60),
      'kappa':mp.nstr(kappa,60),
      'reset_checks':reset_checks,
      'gram_min_eigenvalue':mp.nstr(mineig,60),
      'rh_established':False,
      'open':['DPE67','VHL67','cross-kernel upper estimate','GPC67'],
    }
    blob=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    payload['proof_object_sha256']=hashlib.sha256(blob).hexdigest()
    out=ROOT/'results'/'verification.json'
    out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(payload['verdict'])
    print(payload['proof_object_sha256'])

if __name__=='__main__':main()
