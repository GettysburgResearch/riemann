"""Isolated512-bit, Taylor180 complete theta source for higher orders.

Seven explicit indices,106 cells; all Taylor, time and index tails kept.
See SOURCE_DEEP.md. No previous source or model certificate is an input.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
import argparse,hashlib,json,time
import primitive512 as b
ROOT=Path(__file__).resolve().parent
I=b.I;SCALE=b.SCALE;COUNTS=(36,24,16,12,8,6,4)

def reconstruct(degree=32):
    b.require(type(degree)is int and 2<=degree<=64 and degree%2==0,'fixed positive even degree at most64')
    b.require(b.BITS==512 and b.DEGREE==180,'exact isolated higher source precision')
    b.require(4*196**2*3**11+6*196*3**6<10**11,'whole circle density bound')
    b.require(F(2*sum(COUNTS),16)<16,'whole integration length below16')
    pi=b.pi_interval();b.require(pi.lo>3*SCALE and pi.hi<4*SCALE,'directed pi')
    js=tuple(range(0,degree+1,2));totals={j:I.coerce(0) for j in js}
    for n,count in enumerate(COUNTS,1):
        for k in range(count):
            center=F(2*k+1,32);density=b.cell_density(n,center,pi)
            for j in js:totals[j]+=b.integrate_moment(density,center,j)
        print('DEEP_DIRECTED_INDEX_COMPLETE',n,flush=True)
    errors={}
    for j in js:
        taylor=I.coerce(16*10**11*F(9,4)**j)/4**(b.DEGREE+1)/F(3,4)
        time_tail=I.coerce(0)
        for n,count in enumerate(COUNTS,1):
            U=F(count,16);q=pi*n*n;E=b.exp(2*I.coerce(U));lam=2*q*E-F(9,2)
            b.require(lam.lo>0,'all positive full time-tail decay rates')
            time_tail+=8*q*q*b.exp(F(9,2)*I.coerce(U)-q*E)*sum((comb(j,k)*U**(j-k)*factorial(k)/lam**(k+1) for k in range(j+1)),I.coerce(0))
        index_tail=16*pi*pi*8**4*b.exp(-64*pi)*factorial(j)/(128*pi-F(9,2))**(j+1)
        totals[j]=I(totals[j].lo-taylor.hi,totals[j].hi+taylor.hi+time_tail.hi+index_tail.hi)
        errors[str(j)]={'taylor':taylor.record(),'time':time_tail.record(),'index':index_tail.record()}
    b.require(totals[0].lo>0,'positive complete source normalization')
    mu={j:totals[j]/totals[0] for j in js[1:]};v=mu[2];b.require(v.lo>0,'positive source variance')
    moments=[I.coerce(0) for _ in range(degree+1)];moments[0]=I.coerce(1)
    for r in range(1,degree//2+1):moments[2*r]=mu[2*r]/v**r
    kap=b.cumulants(moments);unit=b.cumulants([F(int(n%2==0)) for n in range(degree+1)])
    ratios=[kap[2*r]/unit[2*r] for r in range(1,degree//2+1)]
    return {'status':'DIRECTED_COMPLETE_SOURCE_DEEP','bits':b.BITS,'degree':degree,'taylor_degree':b.DEGREE,'explicit_theta_indices':7,'counts':list(COUNTS),
        'raw':{str(k):x.record() for k,x in totals.items()},'variance':v.record(),'standardized_cumulant_ratios':[x.record() for x in ratios],
        'standardized_moments':[x.record() for x in moments],'tails':errors,
        'input_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['primitive512.py','source_deep.py']}}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--degree',type=int,default=32);p.add_argument('--emit',type=Path,required=True);a=p.parse_args();start=time.time();out=reconstruct(a.degree)
    txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n';a.emit.write_text(txt)
    print('DEEP_COMPLETE_SOURCE_WRITTEN',a.emit,hashlib.sha256(txt.encode()).hexdigest(),'seconds',time.time()-start,flush=True)
    for r,(lo,hi) in enumerate(out['standardized_cumulant_ratios'],1):print(r,float(F(lo+hi,2*SCALE)),float(F(hi-lo,SCALE)),flush=True)
