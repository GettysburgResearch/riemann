"""Exact four-prime gain for the weighted Ford detector.

Acceptance uses only integer/Fraction arithmetic and Bernstein subdivision.
The kernel assumptions w0>=6, ||w''||<=70 are separate analytic inputs.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib, json, math, runpy

BASE=Path(__file__).resolve().parents[1]/'three-hour-boundary'
old=runpy.run_path(str(BASE/'verify_logistic_prime_minima.py'))
check,chebyshev,halve,logs=(old[k] for k in ('check','chebyshev_polys','halve','log_bounds'))
C=[3500513104,-5906953599,-1574092731,18166603739,6213449589,
   -38436761903,-16088159026,168141762350,447056663730,616860378424,
   541372347258,298691298328,83048065550]
E=10**14
N=sum(c*c for c in C)+13*E
AK=[Q(1)]+[Q(2*(sum(C[j]*C[j+k] for j in range(13-k))+(13-k)*E),N) for k in range(1,13)]
# Targets are deliberately below the exploratory minima. For a fixed prime,
# the target g-h*t and every coefficient depend affinely on t=lambda^2.
DATA=[(2,10,Q(262,1000),Q(11),Q(6931,10000),Q(1733,2500)),
      (3,6,Q(527,10000),Q(4),Q(5493,5000),Q(10987,10000)),
      (5,5,Q(755,100000),Q(2),Q(16094,10000),Q(16095,10000)),
      (7,4,Q(218,100000),Q(1),Q(19459,10000),Q(19460,10000))]

def coefficients(row,t):
    p,M,g,h,ll,lh=row
    n=12*M; ts=chebyshev(n); power=[Q(0)]*(n+1)
    for m in range(1,M+1):
        weight=Q(1,p**m-1)-Q(35,6)*t*lh**2*m*m/Q(p**m)
        check(weight>0,'positive retained weight')
        for k,ak in enumerate(AK):
            for j,v in enumerate(ts[m*k]): power[j]+=ak*v*weight
    power[0]-=g-h*t
    unit=[sum((power[j]*math.comb(j,i)*2**i*(-1)**(j-i) for j in range(i,n+1)),Q(0)) for i in range(n+1)]
    bern=[sum((unit[i]*Q(math.comb(k,i),math.comb(n,i)) for i in range(k+1)),Q(0)) for k in range(n+1)]
    denominator=math.lcm(*(x.denominator for x in bern))
    return [int(x*denominator) for x in bern],denominator

def prove(row,t):
    b,d=coefficients(row,t)
    pending=[(b,d,Q(0),Q(1),0)]; accepted=[]
    while pending:
        b,d,l,h,depth=pending.pop()
        if min(b)>0:
            accepted.append([l,h,Q(min(b),d)]);continue
        check(depth<30,'unresolved Bernstein interval')
        left,right,dd=halve(b,d);mid=(l+h)/2
        pending.extend([(left,dd,l,mid,depth+1),(right,dd,mid,h,depth+1)])
    accepted.sort()
    check(accepted[0][0]==0 and accepted[-1][1]==1,'coverage endpoints')
    check(all(accepted[j][1]==accepted[j+1][0] for j in range(len(accepted)-1)),'gap-free exact cover')
    return {'prime':row[0],'lambda_squared':str(t),'intervals':[[str(v) for v in x] for x in accepted]}

def main():
    check(N==1000000001299439064580929 and all(x>0 for x in AK),'exact polynomial')
    certificates=[]
    for row in DATA:
        p,M,g,h,ll,lh=row
        lo,hi=logs(p);check(ll<lo and hi<lh,'rational logarithms')
        for t in (Q(0),Q(1,160**2)):certificates.append(prove(row,t))
    linear=sum((g*ll for p,M,g,h,ll,lh in DATA),Q(0))
    cubic=sum((h*lh for p,M,g,h,ll,lh in DATA),Q(0))
    check(linear>Q(255,1000),'combined linear gain')
    check(cubic<18,'combined cubic loss')
    false=list(DATA[0]);false[2]=Q(100)
    b,d=coefficients(false,Q(0));check(b[-1]<0,'false-target negative control')
    out={'status':'PASS','scope':'prime gain >=.255*lambda-18*lambda^3, given w0>=6 and curvature<=70',
         'arithmetic':'exact integer and Fraction Bernstein subdivision',
         'domain':'0<=lambda<=1/160, every real phase',
         'linear_lower':str(linear),'cubic_upper':str(cubic),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'dependency_sha256':hashlib.sha256((BASE/'verify_logistic_prime_minima.py').read_bytes()).hexdigest(),
         'negative_controls':1,'certificates':certificates}
    Path(__file__).with_name('FORD_PRIME_GAIN_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='certificates'},indent=2))

if __name__=='__main__':main()
