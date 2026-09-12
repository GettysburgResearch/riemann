"""Independent finite algebra controls; none substitutes for native_source.py."""
from fractions import Fraction as F
from itertools import product
from math import comb
from ball_core import B,Q,PI,exp,sqrt_real
from star import graph,C,poly,D,ACTIVE


def need(ok,msg):
    if not ok:raise ArithmeticError(msg)


def contains(b,x):
    return abs(F(b.a,Q)-x)+abs(F(b.b,Q))<=F(b.e,Q)


def rational_cumulants(mu):
    kk=[F(0)]*len(mu)
    for n in range(1,len(mu)):
        kk[n]=mu[n]-sum((comb(n-1,j-1)*kk[j]*mu[n-j] for j in range(1,n)),F(0))
    return kk


def run():
    arithmetic=0
    vals=[F(i,13) for i in range(-9,10)]
    for x in vals:
        for y in vals:
            for b,exact in ((B.real(x)+B.real(y),x+y),(B.real(x)*B.real(y),x*y)):
                need(contains(b,exact),'rational ball arithmetic');arithmetic+=1
            if y:
                need(contains(B.real(x)/B.real(y),x/y),'rational ball division');arithmetic+=1
    biased=0
    for m in (F(-3,4),F(-1,3),F(0),F(1,100),F(1,3),F(2,3),F(9,10)):
        mu=[F(1) if k%2==0 else m for k in range(17)]
        kk=rational_cumulants(mu)
        for k in range(1,17):
            need(poly(C[k],m)==kk[k],'biased sign recurrence');biased+=1
    enums=0;derivatives=0
    for nleaf in range(1,7):
        aa=[F(j+1,17) for j in range(nleaf)];hub=F(3,11)
        mu=[F(0)]*17;dm=[F(0)]*17
        for signs in product((-1,1),repeat=nleaf):
            prob=F(1);score=F(0)
            for j,(a,s) in enumerate(zip(aa,signs)):
                prob*=F(1,2)*(1+s*a/100)
                if j==0:score=F(s,100)/(1+s*a/100)
            y=hub+sum(a*s for a,s in zip(aa,signs))
            for k in range(0,17,2):
                mu[k]+=prob*y**k
                dm[k]+=prob*((k*y**(k-1)*signs[0] if k else 0)+y**k*score)
        ww=[D(a,[B.real(int(j==0 and r==0)) for r in range(7)]) for j,a in enumerate(aa)]
        ww.append(D(hub))
        _,mm,kk=graph(ww,16,counts=(1,)*nleaf)
        truth=rational_cumulants(mu)
        for k in range(17):
            need(contains(mm[k].v,mu[k]) and contains(kk[k].v,truth[k]),'full independent spin enumeration')
            enums+=2
            need(contains(mm[k].d[0],dm[k]),'enumeration score derivative');derivatives+=1
    coupling=0
    for m in (F(0),F(1,1024),F(1,5),F(2,3),F(1)):
        for a in (F(1,7),F(1,2),F(3,4)):
            # Explicit monotone coupling of a biased sign tau and fair eta.
            atoms=[(-1,-1,(1-m)/2),(1,-1,m/2),(1,1,F(1,2))]
            mean=sum(p*(t-e-m)*a for t,e,p in atoms)
            var=sum(p*((t-e-m)*a)**2 for t,e,p in atoms)
            need(mean==0 and var==(2*m-m*m)*a*a,'homogeneous coupling identity');coupling+=1
    phase=0
    for r in (F(1,5),F(2,3),F(5,4)):
        cx=(1-r*r)/(1+r*r);sx=2*r/(1+r*r)
        for v in (F(3,2),F(5,2),F(7,2)):
            ch=(v+1/v)/2;sh=(v-1/v)/2
            for m in (F(1,1000),F(1,3),F(2,3)):
                ep=cx*cx*(ch+m*sh)**2+sx*sx*(sh+m*ch)**2
                fp=cx*cx*(ch-m*sh)**2+sx*sx*(sh-m*ch)**2
                need(ep-fp==4*m*ch*sh>0,'star phase square identity');phase+=1
    need((exp(3).a-exp(3).e)>16*Q,'tail e^3 bound')
    need((PI.a-PI.e)>3*Q and (PI.a+PI.e)<4*Q,'pi majorants')
    for a in (F(0),F(1,5),F(3),F(19,7)):
        b=sqrt_real(a);lo=F(b.a-b.e,Q);hi=F(b.a+b.e,Q)
        need(lo*lo<=a<=hi*hi,'integer-square-root enclosure')
    # The standalone explicit disk constant used by the native producer.
    need(64*sum(n**4 for n in range(1,11))*3**14+24*sum(n*n for n in range(1,11))*3**8<2**46,'native disk majorant')
    return {'rational_ball_controls':arithmetic,'biased_sign_coefficients':biased,
            'enumerated_moments_and_cumulants':enums,'enumerated_moment_derivatives':derivatives,
            'monotone_coupling_variances':coupling,'phase_square_identities':phase,
            'elementary_and_disk_controls':7}

if __name__=='__main__':
    import json
    print(json.dumps(run(),sort_keys=True))
