"""Exact prime-power bounds for the separate rational degree-12 detector."""
from pathlib import Path
import sys, math, json, hashlib
sys.path.insert(0,str(Path(__file__).resolve().parent))
import verify_logistic_prime_minima as old
from fractions import Fraction as Q

C=[3500513104,-5906953599,-1574092731,18166603739,6213449589,
   -38436761903,-16088159026,168141762350,447056663730,616860378424,
   541372347258,298691298328,83048065550]
EXTRA=10**14
NORM=sum(c*c for c in C)+13*EXTRA
A=[Q(1)]+[Q(2*(sum(C[j]*C[j+k] for j in range(13-k))+(13-k)*EXTRA),NORM) for k in range(1,13)]
TMAX=Q(3,400)**2
DATA=[(2,10,Q(1097,5000),Q(60),Q(6931,10000),Q(1733,2500)),
      (3,6,Q(4913,100000),Q(22),Q(5493,5000),Q(10987,10000)),
      (5,5,Q(747,100000),Q(9),Q(16094,10000),Q(16095,10000)),
      (7,4,Q(43,20000),Q(4),Q(19459,10000),Q(19460,10000))]

def make_b(p,M,g,h,loghi,t):
    n=12*M;ts=old.chebyshev_polys(n);power=[Q(0)]*(n+1)
    for m in range(1,M+1):
        fac=(Q(567,100)-Q(51,2)*t*loghi**2*m*m)/Q(p**m+1)
        old.check(fac>0,'positive retained weight')
        for k,a in enumerate(A):
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
        old.check(dep<24,'unresolved degree12 prime refinement')
        le,ri,dd=old.halve(b,d);mi=(l+r)/2
        todo.extend([(le,dd,l,mi,dep+1),(ri,dd,mi,r,dep+1)])
    acc.sort();old.check(acc[0][0]==0 and acc[-1][1]==1,'coverage endpoints')
    old.check(all(acc[j][1]==acc[j+1][0] for j in range(len(acc)-1)),'gap-free cover')
    return {'prime':p,'eta_squared':str(t),'intervals':[[str(x) for x in a] for a in acc]}

def main():
    old.check(A[0]==1 and all(a>0 for a in A),'normalized positive coefficients')
    old.check(A[1]>1 and sum(A[1:])<4,'coefficient size bounds')
    certificates=[]
    for row in DATA:
        p,M,g,h,ll,lh=row
        logs=old.log_bounds(p)
        old.check(ll<logs[0] and logs[1]<lh,'rational log bounds')
        for t in [Q(0),TMAX]:certificates.append(prove(row,t))
    linear=Q(567,100)*sum((g*ll for p,M,g,h,ll,lh in DATA),Q(0))
    cubic=sum((h*lh for p,M,g,h,ll,lh in DATA),Q(0))
    old.check(linear>Q(126,100) and cubic<90,'combined degree12 prime constants')
    b,d=make_b(2,10,Q(10),Q(0),Q(1733,2500),Q(0))
    old.check(b[-1]<0,'negative control: false endpoint bound')
    out={'status':'PASS','scope':'degree12 prime side >1.26 eta-90 eta^3 for eta<=.0075',
         'linear_rational':str(linear),'cubic_rational':str(cubic),'negative_controls':1,
         'degree':12,'integer_coefficients':C,'auxiliary_square_weight':EXTRA,
         'normalization':str(NORM),'cosine_coefficients':[str(a) for a in A],
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'dependency_sha256':hashlib.sha256(Path(old.__file__).read_bytes()).hexdigest(),
         'certificates':certificates}
    Path(__file__).with_name('LOGISTIC_DEGREE12_PRIME_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print({k:v for k,v in out.items() if k not in ['certificates','cosine_coefficients','integer_coefficients']})

if __name__=='__main__':main()
