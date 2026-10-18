"""All-tail degree-20 source reconstruction, using the pinned directed primitive."""
from inherited import source
from fractions import Fraction as F
from math import comb,factorial
I=source.I
SCALE=source.SCALE
DEGREE=source.DEGREE
BITS=source.BITS
pi_interval=source.pi_interval
require=source.require
cell_density=source.cell_density
integrate_moment=source.integrate_moment
exp=source.exp
cumulants=source.cumulants
def reconstruct():
    pi=pi_interval();require(pi.lo>3*SCALE and pi.hi<4*SCALE,'pi')
    counts=(32,24,16,12,8,6);js=range(0,21,2);totals={j:I.coerce(0) for j in js}
    for n,cnt in enumerate(counts,1):
        for k in range(cnt):
            center=F(2*k+1,32);d=cell_density(n,center,pi)
            for j in js:totals[j]+=integrate_moment(d,center,j)
    errs={}
    for j in js:
        e=I.rat(16*10**11*2**j,4**(DEGREE+1))/F(3,4);tails=I.coerce(0)
        for n,cnt in enumerate(counts,1):
            U=F(cnt,16);q=pi*n*n;E=exp(2*I.coerce(U));lam=2*q*E-F(9,2)
            require(lam.lo>0,'tail exponent')
            tails+=8*q*q*exp(F(9,2)*I.coerce(U)-q*E)*sum((comb(j,k)*U**(j-k)*factorial(k)/lam**(k+1) for k in range(j+1)),I.coerce(0))
        omitted=16*pi*pi*7**4*exp(-49*pi)*factorial(j)/(98*pi-F(9,2))**(j+1)
        totals[j]=I(totals[j].lo-e.hi,totals[j].hi+e.hi+tails.hi+omitted.hi)
        errs[str(j)]={'taylor':e.record(),'time':tails.record(),'index':omitted.record()}
    require(totals[0].lo>0,'normalization');mu={j:totals[j]/totals[0] for j in js if j};v=mu[2]
    require(v.lo>SCALE//25 and v.hi<SCALE//20,'variance')
    mom=[I.coerce(0) for _ in range(21)];mom[0]=I.coerce(1)
    for r in range(1,11):mom[2*r]=mu[2*r]/v**r
    kap=cumulants(mom);unit=cumulants([F(int(n%2==0)) for n in range(21)])
    ss=[kap[2*r]/unit[2*r] for r in range(1,11)]
    return {'status':'DIRECTED_FULL_SOURCE','bits':BITS,'degree':DEGREE,'cells':sum(counts),'explicit_indices':6,
            'raw':{str(j):x.record() for j,x in totals.items()},'variance':v.record(),
            'standardized_moments':[x.record() for x in mom], 's':[x.record() for x in ss], 'tails':errs}
