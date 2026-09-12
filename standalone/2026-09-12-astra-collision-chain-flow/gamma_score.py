"""Tail-complete positive series for the centered consecutive-stage gamma score.

Rational inputs only. This does not evaluate a whole Fourier contour, locate
zeros, or establish a sign for the nonreal-zero production integral.
"""
from fractions import Fraction as Q
from math import factorial
from exact_interval import I,log_q
from research_algebra import coeff_product,poch,require


def score(N,u,w,K=64):
    if type(N) is not int or N<2 or type(K) is not int or K<1:raise ValueError('N>=2, K>=1')
    if isinstance(u,(float,bool)) or isinstance(w,(float,bool)):raise TypeError('rational inputs required')
    u=Q(u);w=Q(w)
    if not 0<=u<=2 or w<=0:raise ValueError('shape must be in [0,2], w positive')
    B=(N+1)**2;nu=2*N+u;v=(B-1)*w
    r=v/(K+2)
    if r>=1:raise ValueError('increase K so (B-1)w<K+2')
    hk=coeff_product([B-n*n for n in range(1,N+1) for _ in range(2)],K)
    S=Q(0);SK=Q(0);SH=Q(0);H=Q(0)
    for k in range(K+1):
        term=hk[k]*w**k/poch(nu,k)
        if k:H+=1/(nu+k-1)
        S+=term;SK+=k*term;SH+=H*term
    first=v**(K+1)/factorial(K+1)
    r0=first/(1-r);r1=first*((K+1)/(1-r)+r/(1-r)**2)
    def positive_interval(a,b):return I(I.q(a).lo,I.q(b).hi)
    ss=positive_interval(S,S+r0)
    ek=positive_interval(SK,SK+r1)/ss
    eh=positive_interval(SH,SH+r1/(2*N))/ss
    out=log_q(w)+(nu-1+ek)/(B*w)-eh
    return {'S':ss,'mean_K':ek,'mean_H':eh,'score_without_constant':out,
            'full_series_tail':I.q(r0),'full_K_tail':I.q(r1)}


def report():
    count=0;max_tail=Q(0);examples=[]
    for N in (2,3,5):
        for u in (Q(0),Q(1,2),Q(2)):
            for w in (Q(1,20),Q(1,4)):
                a=score(N,u,w,64);b=score(N,u,w,96)
                for key in ('S','mean_K','mean_H','score_without_constant'):
                    require(max(a[key].lo,b[key].lo)<=min(a[key].hi,b[key].hi),'two full positive enclosures must overlap')
                require(a['S'].lo>0,'positive score denominator')
                count+=1
                if N==3 and w==Q(1,4):
                    examples.append({'N':N,'u':str(u),'w':str(w),'score_without_constant':a['score_without_constant'].bounds(),
                                     'series_tail':a['full_series_tail'].bounds()})
    return {'complete_positive_score_panels':count,'orders_compared':[64,96],
            'comparisons_are_same_backend_not_independent_review':True,'examples':examples,
            'actual_Fourier_integral_or_zero_track_computed':False}
