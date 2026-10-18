"""Directed complete theta moments through any requested fixed even degree.

The only extension of #994's six-index protocol is the finite moment list.
The primitive and all explicit cell, time and index remainder formulas stay
unchanged. See PROOF.md for why the same estimates cover every fixed degree.
"""
from pathlib import Path
import sys, json, argparse
from fractions import Fraction as F
from math import comb, factorial
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited'))
import pr886_primitive as b
I=b.I; SCALE=b.SCALE; COUNTS=(32,24,16,12,8,6)

def reconstruct(degree=24):
    b.require(type(degree) is int and degree>=2 and degree%2==0,'positive even degree')
    pi=b.pi_interval(); b.require(pi.lo>3*SCALE and pi.hi<4*SCALE,'pi')
    js=tuple(range(0,degree+1,2)); totals={j:I.coerce(0) for j in js}
    for n,cnt in enumerate(COUNTS,1):
        for k in range(cnt):
            center=F(2*k+1,32); d=b.cell_density(n,center,pi)
            for j in js: totals[j]+=b.integrate_moment(d,center,j)
        print('DIRECTED_INDEX_COMPLETE',n,flush=True)
    errs={}
    for j in js:
        e=I.rat(16*10**11*2**j,4**(b.DEGREE+1))/F(3,4)
        tails=I.coerce(0)
        for n,cnt in enumerate(COUNTS,1):
            U=F(cnt,16); q=pi*n*n; E=b.exp(2*I.coerce(U)); lam=2*q*E-F(9,2)
            b.require(lam.lo>0,'positive time exponent')
            tails+=8*q*q*b.exp(F(9,2)*I.coerce(U)-q*E)*sum(
                (comb(j,k)*U**(j-k)*factorial(k)/lam**(k+1) for k in range(j+1)),I.coerce(0))
        omitted=16*pi*pi*7**4*b.exp(-49*pi)*factorial(j)/(98*pi-F(9,2))**(j+1)
        totals[j]=I(totals[j].lo-e.hi,totals[j].hi+e.hi+tails.hi+omitted.hi)
        errs[str(j)]={'taylor':e.record(),'time':tails.record(),'index':omitted.record()}
    b.require(totals[0].lo>0,'positive source normalization')
    mu={j:totals[j]/totals[0] for j in js[1:]};v=mu[2]
    mom=[I.coerce(0) for _ in range(degree+1)];mom[0]=I.coerce(1)
    for r in range(1,degree//2+1):mom[2*r]=mu[2*r]/v**r
    kap=b.cumulants(mom);unit=b.cumulants([F(int(n%2==0)) for n in range(degree+1)])
    ss=[kap[2*r]/unit[2*r] for r in range(1,degree//2+1)]
    return {'status':'DIRECTED_COMPLETE_SOURCE','bits':b.BITS,'degree':degree,
        'taylor_degree':b.DEGREE,'explicit_theta_indices':6,'counts':list(COUNTS),
        'raw':{str(k):x.record() for k,x in totals.items()},'variance':v.record(),
        'standardized_cumulant_ratios':[x.record() for x in ss],
        'standardized_moments':[x.record() for x in mom], 'tails':errs}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--degree',type=int,default=24);p.add_argument('--emit',type=Path,required=True);a=p.parse_args()
    out=reconstruct(a.degree);a.emit.write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    print('DIRECTED_SOURCE_WRITTEN',a.emit,flush=True)
    for r,(lo,hi) in enumerate(out['standardized_cumulant_ratios'],1):
        print(r,float(F(lo+hi,2*SCALE)),float(F(hi-lo,SCALE)),flush=True)
