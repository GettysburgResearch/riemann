#!/usr/bin/env python3
"""Complete theta moments, six explicit theta terms, same directed backend.

Arithmetic and cell integration are imported without alteration from PR886's
primitive.py at d998605c0718e332ac503baf078704b862f8250e. This extends the
explicit index range to six and rederives every remainder in PROOF.md.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
import json,hashlib
import pr886_primitive as b
I=b.I;SCALE=b.SCALE
COUNTS=(32,24,16,12,8,6)

def theta_moments():
    pi=b.pi_interval();b.require(pi.lo>3*SCALE and pi.hi<4*SCALE,'pi')
    js=tuple(range(0,19,2));totals={j:I.coerce(0)for j in js}
    for n,cnt in enumerate(COUNTS,1):
        for k in range(cnt):
            center=F(2*k+1,32);d=b.cell_density(n,center,pi)
            for j in js:totals[j]+=b.integrate_moment(d,center,j)
    errs={}
    for j in js:
        e=I.rat(16*10**11*2**j,4**(b.DEGREE+1))/F(3,4)
        tails=I.coerce(0)
        for n,cnt in enumerate(COUNTS,1):
            U=F(cnt,16);q=pi*n*n;E=b.exp(2*I.coerce(U));lam=2*q*E-F(9,2)
            b.require(lam.lo>0,'time exponent')
            tails+=8*q*q*b.exp(F(9,2)*I.coerce(U)-q*E)*sum(
                (comb(j,k)*U**(j-k)*factorial(k)/lam**(k+1)for k in range(j+1)),I.coerce(0))
        omitted=16*pi*pi*7**4*b.exp(-49*pi)*factorial(j)/(98*pi-F(9,2))**(j+1)
        totals[j]=I(totals[j].lo-e.hi,totals[j].hi+e.hi+tails.hi+omitted.hi)
        errs[str(j)]={'taylor':e.record(),'time':tails.record(),'index':omitted.record()}
    b.require(totals[0].lo>0,'normalization')
    mu={j:totals[j]/totals[0]for j in js[1:]}
    return totals,mu,errs

def reconstruct():
    raw,mu,tails=theta_moments();v=mu[2]
    mom=[I.coerce(0)for _ in range(19)];mom[0]=I.coerce(1)
    for r in range(1,10):mom[2*r]=mu[2*r]/v**r
    kap=b.cumulants(mom);unit=b.cumulants([F(int(n%2==0))for n in range(19)])
    ss=[kap[2*r]/unit[2*r]for r in range(1,10)]
    return {'status':'DIRECTED_COMPLETE_SOURCE','bits':b.BITS,'degree':b.DEGREE,
      'explicit_theta_indices':6,'cells':sum(COUNTS),'counts':list(COUNTS),
      'raw':{str(k):x.record()for k,x in raw.items()},'variance':v.record(),
      'standardized_cumulant_ratios':[x.record()for x in ss],
      'standardized_moments':[x.record()for x in mom],'tails':tails}

if __name__=='__main__':
    result=reconstruct();text=json.dumps(result,sort_keys=True,separators=(',',':'))+'\n'
    path=Path(__file__).resolve().parent/'theta_tight.json';path.write_text(text)
    print('COMPLETE_SIX_INDEX_SOURCE',hashlib.sha256(text.encode()).hexdigest(),flush=True)
    for r,(lo,hi)in enumerate(result['standardized_cumulant_ratios'],1):
        print(r,'width',float(F(hi-lo,SCALE)),flush=True)
