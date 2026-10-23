"""Exact Bernstein certificate for two logistic prime-power polynomials.

All acceptance arithmetic is integer/Fraction arithmetic.  A decimal
rendering is informational only.  No transcendental evaluation is used.
"""
from fractions import Fraction as Q
from pathlib import Path
import math, json, hashlib

C=[4,-8,2,20,-9,-34,27,91,-27,-201,32,895,1949,2389,1896,949,239]
NORM=sum(c*c for c in C)
A=[Q(1)]+[Q(2*sum(C[j]*C[j+k] for j in range(17-k)),NORM) for k in range(1,17)]

def check(ok,label):
    if not ok: raise RuntimeError(label)

def log_bounds(x):
    z=Q(x-1,x+1)
    lo=sum((2*z**(2*j+1)/(2*j+1) for j in range(80)),Q(0))
    return lo,lo+2*z**161/(161*(1-z*z))

def chebyshev_polys(n):
    ts=[[1],[0,1]]
    for k in range(2,n+1):
        a=[0]+[2*x for x in ts[-1]]
        for j,x in enumerate(ts[-2]): a[j]-=x
        ts.append(a)
    return ts[:n+1]

def bernstein(p,M,lower):
    n=16*M
    ts=chebyshev_polys(n)
    power=[Q(0)]*(n+1)
    for m in range(1,M+1):
        for k,a in enumerate(A):
            for j,t in enumerate(ts[m*k]):power[j]+=a*t/(p**m+1)
    power[0]-=lower
    # y=2u-1, u in [0,1].
    unit=[sum((power[j]*math.comb(j,i)*2**i*(-1)**(j-i)
               for j in range(i,n+1)),Q(0)) for i in range(n+1)]
    b=[sum((unit[i]*Q(math.comb(k,i),math.comb(n,i))
            for i in range(k+1)),Q(0)) for k in range(n+1)]
    denom=math.lcm(*(x.denominator for x in b))
    return [int(x*denom) for x in b],denom

def halve(b,denom):
    n=len(b)-1
    row=b[:]
    left=[row[0]<<n]; right=[row[-1]<<n]
    for j in range(1,n+1):
        row=[row[i]+row[i+1] for i in range(len(row)-1)]
        left.append(row[0]<<(n-j));right.append(row[-1]<<(n-j))
    return left,list(reversed(right)),denom<<n

def certify(p,M,lower):
    b,denom=bernstein(p,M,lower)
    todo=[(b,denom,Q(0),Q(1),0)]
    accepted=[];nodes=0
    while todo:
        b,denom,l,h,depth=todo.pop();nodes+=1
        if min(b)>0:
            accepted.append((l,h,Q(min(b),denom)))
            continue
        check(depth<30,'unresolved Bernstein subinterval')
        left,right,d=halve(b,denom);mid=(l+h)/2
        todo.extend([(left,d,l,mid,depth+1),(right,d,mid,h,depth+1)])
    accepted.sort()
    check(accepted[0][0]==0 and accepted[-1][1]==1,'endpoint coverage')
    check(all(accepted[i][1]==accepted[i+1][0] for i in range(len(accepted)-1)), 'gap-free exact coverage')
    return {'prime':p,'powers':M,'lower_bound':str(lower),'degree':16*M,
            'nodes':nodes,'accepted_intervals':len(accepted),
            'minimum_Bernstein_reserve':str(min(v for _,_,v in accepted)),
            'intervals':[[str(l),str(h),str(v)] for l,h,v in accepted]}

def main():
    check(NORM==14912370 and all(a>=0 for a in A),'source polynomial')
    check(A[1]==Q(865534,497079) and sum(A[1:])==Q(2919857,828465),'source coefficients')
    rows=[certify(2,10,Q(27,125)),certify(3,6,Q(19,400))]
    # False claim G2 >= 10 is disproved at u=1 (x=0).
    b,d=bernstein(2,10,Q(10))
    check(b[-1]<0,'negative control: false lower bound')
    log2=log_bounds(2);log3=log_bounds(3)
    check(log2[0]>Q(6931,10000) and log2[1]<Q(1733,2500),'log 2 bounds')
    check(log3[0]>Q(5493,5000) and log3[1]<Q(10987,10000),'log 3 bounds')
    linear=Q(567,100)*(Q(27,125)*Q(6931,10000)+Q(19,400)*Q(5493,5000))
    cubic=175*sum(A)*(Q(1733,2500)**3*sum((Q(m*m,2**m+1) for m in range(1,11)),Q(0))
            +Q(10987,10000)**3*sum((Q(m*m,3**m+1) for m in range(1,7)),Q(0)))
    check(linear>Q(11447,10000) and cubic<2775,'prime lower bound constants')
    check(175*(Q(3,400)*10*Q(1733,2500))**2<Q(567,100),'positive p2 Taylor lower')
    check(175*(Q(3,400)*6*Q(10987,10000))**2<Q(567,100),'positive p3 Taylor lower')
    out={'status':'PASS','scope':'exact minima for G_p(x)=sum_m P(mx)/(p^m+1), all real x',
         'arithmetic':'integer Bernstein coefficients and exact dyadic subdivision',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'positive_checks':8,'negative_controls':1,'prime_linear_lower':'11447/10000',
         'prime_cubic_upper':'2775','certificates':rows}
    dest=Path(__file__).with_name('LOGISTIC_PRIME_MINIMA.json')
    dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({**out,'certificates':[{k:v for k,v in r.items() if k!='intervals'} for r in rows]},indent=2))

if __name__=='__main__':main()
