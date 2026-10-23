"""Exact exploratory refinement; does not modify the frozen two-prime proof."""
from pathlib import Path
import sys, math, json, hashlib
sys.path.insert(0,str(Path(__file__).resolve().parent))
import verify_logistic_prime_minima as old
from fractions import Fraction as Q

TMAX=Q(3,400)**2
DATA=[(2,10,Q(541,2500),Q(380),Q(6931,10000),Q(1733,2500)),
      (3,6,Q(477,10000),Q(140),Q(5493,5000),Q(10987,10000)),
      (5,4,Q(73,10000),Q(51),Q(16094,10000),Q(16095,10000)),
      (7,4,Q(51,25000),Q(20),Q(19459,10000),Q(19460,10000))]

def make_b(p,M,g,h,loghi,t):
    n=16*M;ts=old.chebyshev_polys(n);power=[Q(0)]*(n+1)
    for m in range(1,M+1):
        fac=(Q(567,100)-175*t*loghi**2*m*m)/Q(p**m+1)
        old.check(fac>0,'positive retained weight')
        for k,a in enumerate(old.A):
            for j,v in enumerate(ts[m*k]):power[j]+=a*v*fac
    power[0]-=Q(567,100)*g-h*t
    unit=[sum((power[j]*math.comb(j,i)*2**i*(-1)**(j-i) for j in range(i,n+1)),Q(0)) for i in range(n+1)]
    b=[sum((unit[i]*Q(math.comb(k,i),math.comb(n,i)) for i in range(k+1)),Q(0)) for k in range(n+1)]
    d=math.lcm(*(v.denominator for v in b))
    return [int(v*d) for v in b],d

def prove(row,t):
    p,M,g,h,ll,lh=row;b,d=make_b(p,M,g,h,lh,t)
    todo=[(b,d,Q(0),Q(1),0)];acc=[]
    while todo:
        b,d,l,r,dep=todo.pop()
        if min(b)>0:
            acc.append((l,r,Q(min(b),d)));continue
        old.check(dep<24,'unresolved four-prime refinement')
        le,ri,dd=old.halve(b,d);mi=(l+r)/2
        todo.extend([(le,dd,l,mi,dep+1),(ri,dd,mi,r,dep+1)])
    acc.sort();old.check(acc[0][0]==0 and acc[-1][1]==1,'coverage endpoints')
    old.check(all(acc[j][1]==acc[j+1][0] for j in range(len(acc)-1)),'gap-free cover')
    return {'prime':p,'eta_squared':str(t),'intervals':[[str(x) for x in a] for a in acc]}

def main():
    certificates=[]
    for row in DATA:
        p,M,g,h,ll,lh=row
        logs=old.log_bounds(p)
        old.check(ll<logs[0] and logs[1]<lh,'rational log bounds')
        for t in [Q(0),TMAX]:certificates.append(prove(row,t))
    linear=Q(567,100)*sum((g*ll for p,M,g,h,ll,lh in DATA),Q(0))
    cubic=sum((h*lh for p,M,g,h,ll,lh in DATA),Q(0))
    old.check(linear>Q(1236,1000) and cubic<540,'refined combined constants')
    out={'status':'PASS','scope':'prime side >= 1.236 eta-540 eta^3 for eta<=.0075',
         'linear_rational':str(linear),'cubic_rational':str(cubic),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'dependency_sha256':hashlib.sha256(Path(old.__file__).read_bytes()).hexdigest(),
         'certificates':certificates}
    Path(__file__).with_name('LOGISTIC_FOUR_PRIME_REFINEMENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print({k:v for k,v in out.items() if k!='certificates'})

if __name__=='__main__':main()
