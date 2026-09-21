"""Exact rational local isometry, full-kernel checks, and normalization controls."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from math import isqrt
from core import *
from verify import trial_mu

def variance(x,w=None):
    if w is None:w=[F(1)]*len(x)
    return sum((a*a*b for a,b in zip(x,w)),F(0))-sum((a*b for a,b in zip(x,w)),F(0))**2/sum(w)

def covariance(x,y,w):
    return sum((a*b*c for a,b,c in zip(x,y,w)),F(0))-sum((a*c for a,c in zip(x,w)),F(0))*sum((b*c for b,c in zip(y,w)),F(0))/sum(w)

def local_checks():
    checks=0
    for word in product((-1,0,1),repeat=5):
        M=[];m=[];v=r=F(0)
        for k,a in enumerate(word,1):v+=a;r+=F(a,k);M.append(v);m.append(r)
        for s in range(1,6):
            for t in range(s,6):
                w=[F(1,k*(k+1)) for k in range(s,t+1)]
                need(variance(M[s-1:t],w)==variance(m[s-1:t]),'exact local variance isometry')
                need(variance(M[s-1:t],w)<=variance([F(k) for k in range(s,t+1)],w),'sharp ramp domination')
                checks+=1
    return checks

def kernel_checks():
    H=[F(0)]
    for k in range(1,65):H.append(H[-1]+F(1,k))
    checks=0
    for s,t in [(2,3),(4,8),(9,15),(16,24),(25,35),(36,63)]:
        ds=[1,2,3,5,7,11,17,29,67,101]
        w=[F(1,k*(k+1)) for k in range(s,t+1)];ones=[F(1)]*len(w)
        ks={d:[(H[k//d]-H[k])/d for k in range(s,t+1)] for d in ds}
        ps={d:[F(k//d)-F(k,d) for k in range(s,t+1)] for d in ds}
        for d in ds:
            for e in ds:
                need(covariance(ks[d],ks[e],ones)==covariance(ps[d],ps[e],w),'all-pair residual kernel')
                checks+=1
        # Above-endpoint columns are not zero after mean subtraction.
        need(variance(ks[101])>0,'above-endpoint column retained')
    return checks

def clipped_fake(Y):
    c={1:F(1)};r=F(1);n=Y
    while r:
        n+=1;a=-min(F(3),n*r);c[n]=a;r+=a/n
    need(n<=Y+(Y+1)//2,'fake support');return c

def fake_panel(Y):
    B=(Y+1)**2-1;c=clipped_fake(Y);z={}
    for d,a in c.items():
        for e,b in c.items():z[d*e]=z.get(d*e,F(0))+a*b
    need(sum((a/n for n,a in c.items()),F(0))==0,'fake balance')
    v=[F(0)]*(B+1)
    for n,a in c.items():
        if n<=B:v[n]+=2*a
    for d,a in z.items():
        for n in range(d,B+1,d):v[n]-=a
    rec=F(0);mc=F(0);q=[]
    for k in range(1,B+1):
        rec+=v[k]/k;mc+=c.get(k,F(0))/k
        if k>Y:q.append(2*mc-rec)
    total=sum((x*x for x in q),F(0));coarse=F(0)
    for s,t in cells(Y+1,B):coarse+=sum(q[s-Y-1:t-Y],F(0))**2/(t-s+1)
    need(coarse>total/2,'fake power mass remains coarse')
    return {'Y':Y,'total_Q':rat(total.numerator,total.denominator),'coarse_Q':rat(coarse.numerator,coarse.denominator),
            'residual_Q':rat((total-coarse).numerator,(total-coarse).denominator),'scope':'balanced nonnative source; not mu'}

def point_count(m,p):
    need(p%2 and (3*m)%p!=0,'good odd prime')
    c=(m*m*pow(4,-1,p))%p
    return 1+sum(sum((y*y-(x*x*x+c))%p==0 for y in range(p)) for x in range(p))

def family_panel():
    N=4095;primes=[5,7,11,13,19,23,29,31,37,41,43,47,53,59,61]
    coeff=[0]*(N+1);coeff[1]=1;counts={}
    for p in primes:
        ap=p+1-point_count(17,p);need(ap*ap<=4*p,'Hasse fixture');counts[str(p)]=ap
        nxt=coeff.copy()
        for n in range(1,N//p+1):nxt[n*p]-=ap*coeff[n]
        for n in range(1,N//(p*p)+1):nxt[n*p*p]+=p*coeff[n]
        coeff=nxt
    tau=[0]*(N+1)
    for d in range(1,N+1):
        for k in range(d,N+1,d):tau[k]+=1
    need(all(coeff[k]**2<=k*tau[k]**2 for k in range(1,N+1)),'arithmetic reciprocal cap')
    cumulative=[];x=0
    for a in coeff[1:]:x+=a;cumulative.append(x)
    total=coarse=integer(0);num=0;H=integer(0)
    for k,A in enumerate(cumulative,1):
        w=rat(2*k+1,2*k*k*(k+1)*(k+1));total=add(total,scale(w,A*A));H=add(H,rat(1,k))
    for s,t in cells(1,N):
        num+=1;u=integer(0)
        for k in range(s,t+1):u=add(u,scale(rat(2*k+1,2*k*k*(k+1)*(k+1)),cumulative[k-1]))
        W=sub(rat(1,2*s*s),rat(1,2*(t+1)**2));coarse=add(coarse,divide(square(u),W))
    residual=sub(total,coarse);bound=scale(square(square(H)),36)
    need(residual[1]>=0 and residual[0]<=bound[1],'family root-cell bound')
    return {'model':'E17 finite good-Euler inverse model; omitted primes and bad factors not modeled',
            'N':N,'measure':'dx/x^3','point_counts_a_p':counts,'cells':num,
            'full_energy':total,'coarse_energy':coarse,'residual_energy':residual,'universal_bound':bound}

def build():
    return {'schema':'RSC26-algebra-v1','local_isometry_checks':local_checks(),'kernel_pair_checks':kernel_checks(),
            'fake_controls':[fake_panel(15),fake_panel(31)],'family':family_panel()}

if __name__=='__main__':
    r=build();Path('reports').mkdir(exist_ok=True);Path('reports/algebra.json').write_text(canonical(r)+'\n')
    print(canonical(r))
