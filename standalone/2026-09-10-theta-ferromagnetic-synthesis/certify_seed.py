#!/usr/bin/env python3
"""Directed theta moments + a six-moment ferromagnetic seed; not an RH proof.
All arithmetic used for acceptance is integer/Fraction outward arithmetic.
"""
from fractions import Fraction as F
from math import factorial, comb, isqrt
import argparse, json, hashlib
from pathlib import Path

BITS=128
S=1<<BITS

def ceildiv(a,b):
    return -((-a)//b)

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=int(lo);self.hi=int(lo if hi is None else hi)
        if self.lo>self.hi: raise ValueError('reversed interval')
    @staticmethod
    def point(x):
        x=F(x)
        return I(x.numerator*S//x.denominator,ceildiv(x.numerator*S,x.denominator))
    @staticmethod
    def bounds(a,b):
        a=F(a);b=F(b)
        return I(a.numerator*S//a.denominator,ceildiv(b.numerator*S,b.denominator))
    def __add__(self,y):
        y=asI(y);return I(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,y):return self+-asI(y)
    def __rsub__(self,y):return asI(y)+-self
    def __mul__(self,y):
        y=asI(y);v=[self.lo*y.lo,self.lo*y.hi,self.hi*y.lo,self.hi*y.hi]
        return I(min(v)//S,ceildiv(max(v),S))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi:raise ValueError('division through zero')
        return I(S*S//self.hi,ceildiv(S*S,self.lo))
    def __truediv__(self,y):return self*asI(y).inv()
    def __pow__(self,n):
        if type(n) is not int or n<0:raise ValueError('nonnegative integer power required')
        r=I.point(1);a=self
        while n:
            if n&1:r=r*a
            n//=2
            if n:a=a*a
        return r
    def widened(self,r):
        r=F(r);n=ceildiv(r.numerator*S,r.denominator)
        return I(self.lo-n,self.hi+n)
    def sqrt(self):
        if self.lo<0:raise ValueError("sqrt of negative interval")
        lo=isqrt(self.lo*S);hi=isqrt(self.hi*S)
        if hi*hi<self.hi*S:hi+=1
        return I(lo,hi)
    def contains(self,x):
        x=F(x);return F(self.lo,S)<=x<=F(self.hi,S)
    def decimal(self,digits=15):
        k=10**digits
        def fmt(a):
            return ('-' if a<0 else '')+str(abs(a)//k)+'.'+str(abs(a)%k).zfill(digits)
        return [fmt(self.lo*k//S),fmt(ceildiv(self.hi*k,S))]
    def raw(self):return [str(self.lo),str(self.hi)]

def asI(x):return x if isinstance(x,I) else I.point(x)

def exp_at(x):
    # x is an exact dyadic endpoint, not a float.
    if x==0:return I.point(1)
    # e>2 gives exp(x)<=2^-BITS for x<=-BITS.
    if x<=-BITS*S:return I(0,1)
    r=max(0,(8*abs(x)).bit_length()-BITS)
    while 8*abs(x)>S*(1<<r):r+=1
    y=I(x//(1<<r),ceildiv(x,1<<r))
    if max(abs(y.lo),abs(y.hi))*8>S:raise ValueError('exp reduction failed')
    term=I.point(1);total=term
    for j in range(1,33):
        term=term*y/j;total=total+term
    # For |y|<=1/8 the omitted tail is <=2 |y|^33/33!.
    rem=F(2,8**33*factorial(33));total=total.widened(rem)
    if total.lo<=0:raise ValueError('nonpositive reduced exponential')
    for _ in range(r):total=total*total
    return total

def exp(x):
    x=asI(x)
    if x.hi<=-BITS*S:return I(0,1)
    if x.hi<=0:
        # exp is 1-Lipschitz on the negative half-line.
        a=exp_at(x.lo)
        return I(a.lo,min(S,a.hi+x.hi-x.lo))
    return I(exp_at(x.lo).lo,exp_at(x.hi).hi)

def atan_inv(k):
    x=F(1,k);a=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(110)),F(0))
    rem=x**221/221
    return I.bounds(a,a+rem) # 110 terms: final sign negative; next positive.

def pi_interval():return 16*atan_inv(5)-4*atan_inv(239)

def derivative_L1_bounds():
    # P_(j+1)=2Q P_j'+(1/2-2Q)P_j.
    p={1:F(-6),2:F(4)};out=[]
    for _ in range(5):
        out.append(6*sum(abs(c)*factorial(k-1) for k,c in p.items()))
        q={}
        for k,c in p.items():
            q[k]=q.get(k,F(0))+(2*k+F(1,2))*c
            q[k+1]=q.get(k+1,F(0))-2*c
        p=q
    return out

def theta_moments(cells=16384):
    if cells<2 or cells%2:raise ValueError('positive even cell count needed')
    pi=pi_interval();h=F(2,cells);orders=[0,2,4,6,8]
    sums={m:I.point(0) for m in orders}
    # Pointwise positive t>=0 source; first four terms are computed.
    for j in range(cells+1):
        t=F(2*j,cells);et=exp(I.point(2*t));factor=exp(I.point(t/2))
        ph=I.point(0)
        for n in range(1,5):
            q=pi*(n*n)*et
            ph=ph+factor*(4*q*q-6*q)*exp(-q)
        weight=1 if j in (0,cells) else (4 if j%2 else 2)
        for m in orders:sums[m]=sums[m]+weight*(t**m)*ph
    Bs=derivative_L1_bounds();raw={};budgets={}
    for m in orders:
        C=sum(F(comb(4,j)*factorial(m),factorial(m-j))*2**(m-j)*Bs[4-j]
              for j in range(min(4,m)+1))
        error=2*h**4*C/72
        v=(2*h/3)*sums[m]
        # Complete omitted-index and physical tails, each nonnegative.
        # t^m <= m! exp(t); Q substitution gives 4m! Gamma(3,Q0).
        tail_indices=8*factorial(m)*10202*exp(-75)
        tail_physical=8*factorial(m)*105626*exp(-150)
        tail_hi=tail_indices.hi+tail_physical.hi
        v=v.widened(error);v=I(v.lo,v.hi+tail_hi)
        raw[m]=v;budgets[m]=str(error)
    mu={m:(raw[m]/raw[0] if m else I.point(1)) for m in orders}
    v=mu[2];c4=mu[4]-3*v*v;c6=mu[6]-15*mu[4]*v+30*v**3
    A=-c4/v**2;B=c6/v**3
    return {'raw':raw,'mu':mu,'variance':v,'A':A,'B':B,'budgets':budgets,'pi':pi}

def cluster(q):
    # q=exp(2J), q>=1; exact magnetization distribution of K8.
    q=asI(q);weights=[comb(8,k)*q**((2*k-8)**2//4) for k in range(9)]
    Z=sum(weights,I.point(0));mu={}
    for j in [2,4,6,8]:mu[j]=sum((w*(2*k-8)**j for k,w in enumerate(weights)),I.point(0))/Z
    c2=mu[2];c4=mu[4]-3*c2**2;c6=mu[6]-15*mu[4]*c2+30*c2**3
    return c2,c4,c6

def need(ok,s):
    if not ok:raise ValueError(s)

def certify(cells=16384):
    d=theta_moments(cells);A=d['A'];B=d['B']
    need(A.lo>0 and B.lo>0,'theta cumulant signs')
    target=B**2/A**3
    q0=F(11,10);q1=F(1101,1000)
    l=cluster(q0);r=cluster(q1)
    L=l[2]**2/(-l[1])**3;R=r[2]**2/(-r[1])**3
    need(L.hi<target.lo and target.hi<R.lo,'IVT endpoint signs')
    # Subdivide parameter interval. Full interval arithmetic proves signs
    # and nonnegative Gaussian variance at EVERY possible IVT root.
    ratio_upper=I.point(0);c6lower=None
    cloud=4096
    def finite_params(q):
        c2,c4,c6=cluster(q);d4=-c4;D=d4+2*c2**2/cloud
        radical=D*A-2*d4/cloud
        need(radical.lo>0,'strictly positive finite-bath radical')
        t=(2*c2/cloud+radical.sqrt())/D
        gamma=1-c2*t
        return t,gamma,c6*t**3+16*gamma**3/cloud**2
    fleft=finite_params(q0);fright=finite_params(q1)
    need(fleft[2].hi<B.lo and fright[2].lo>B.hi,'finite Ising IVT bracket')
    gmin=None;gmax=None
    for j in range(128):
        q=I.bounds(q0+(q1-q0)*F(j,128),q0+(q1-q0)*F(j+1,128))
        c2,c4,c6=cluster(q)
        need(c4.hi<0 and c6.lo>0,'cluster cumulant signs')
        u=A*c2**2/(-c4)
        need(u.hi<S,'positive Gaussian variance')
        ratio_upper=I(max(ratio_upper.lo,u.lo),max(ratio_upper.hi,u.hi))
        c6lower=c6.lo if c6lower is None else min(c6lower,c6.lo)
        t,gamma,c6out=finite_params(q)
        need(t.lo>0 and gamma.lo>S//3 and gamma.hi<2*S//5,'finite positive scale/variance')
        gmin=gamma.lo if gmin is None else min(gmin,gamma.lo)
        gmax=gamma.hi if gmax is None else max(gmax,gamma.hi)
    return {
      'schema':1,'status':'PROPOSED_SIX_MOMENT_SEED_NOT_RH',
      'bits':BITS,'cells':cells,'theta_terms_computed':4,'interval':[0,2],
      'pi':d['pi'].decimal(18),
      'theta_moments':{str(m):d['mu'][m].decimal(18) for m in d['mu']},
      'simpson_errors':{str(m):v for m,v in d['budgets'].items()},
      'standardized_negative_fourth_cumulant':A.decimal(12),
      'standardized_sixth_cumulant':B.decimal(12),
      'target_ratio_squared':target.decimal(12),
      'left_cluster_ratio_squared':L.decimal(12),
      'right_cluster_ratio_squared':R.decimal(12),
      'q_interval':[str(q0),str(q1)],
      'cluster_variance_fraction_squared_upper':str(F(ratio_upper.hi,S)),
      'parameter_subintervals':128,
      'finite_seed_total_spins':cloud+8,'isolated_cloud_spins':cloud,
      'finite_left_sixth_cumulant':fleft[2].decimal(12),
      'finite_right_sixth_cumulant':fright[2].decimal(12),
      'cloud_variance_range':I(gmin,gmax).decimal(12),
      'matched_even_moments_exactly':[2,4,6],
      'matching_meaning':'exact finite 4104-spin graph existence by IVT with explicit algebraic scale formulas; neither uniqueness nor a numerically instantiated root is claimed',
      'rh_proved':False,'all_order_synthesis_proved':False,
    }

def strict_json(path):
    def pairs(items):
        out={}
        for k,v in items:
            need(k not in out,'duplicate JSON key')
            out[k]=v
        return out
    def no_float(value):raise ValueError('floating JSON literal')
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs,
                      parse_float=no_float,parse_constant=no_float)

def authenticate():
    root=Path(__file__).resolve().parent
    names={'README.md','PROPOSAL.md','REVIEW.md','SOURCES.json','VALIDATION.md',
           'certify_seed.py','seed_certificate.json','test_seed.py','SHA256SUMS'}
    need({p.name for p in root.iterdir()}==names,'packet inventory')
    need(all((root/name).is_file() and not (root/name).is_symlink() for name in names),
         'non-regular packet entry')
    entries={}
    for line in (root/'SHA256SUMS').read_text().splitlines():
        h,name=line.split('  ',1)
        need(name not in entries and name in names-{'SHA256SUMS'},'manifest entry')
        entries[name]=h
    need(set(entries)==names-{'SHA256SUMS'},'manifest coverage')
    for name,h in entries.items():
        f=root/name
        need(f.is_file() and not f.is_symlink(),'not a regular file')
        need(hashlib.sha256(f.read_bytes()).hexdigest()==h,'hash mismatch: '+name)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--emit',action='store_true',help='producer only, no authentication')
    group.add_argument('--check',type=Path)
    ap.add_argument('--cells',type=int,default=16384,help='producer override only')
    args=ap.parse_args()
    if args.check:
        need(args.cells==16384,'accepting quadrature must use the frozen coverage')
        authenticate()
    result=certify(args.cells)
    if args.check:
        got=strict_json(args.check)
        need(json.dumps(got,sort_keys=True,separators=(',',':'))==
             json.dumps(result,sort_keys=True,separators=(',',':')),'result mismatch')
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
