#!/usr/bin/env python3
"""Reconstruct finite norm/optimality enclosures with integer-directed arithmetic.
No floating-point or special-function oracle enters acceptance. The paper supplies
Euler--Maclaurin remainder and all infinite-dimensional claims.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path

BITS = 192
S = 1 << BITS
BERNOULLI = [(1,6),(-1,30),(1,42),(-1,30),(5,66),(-691,2730),(7,6),(-3617,510)]
ROOT = Path(__file__).resolve().parent


def require(p: bool, msg: str) -> None:
    if not p:
        raise ValueError(msg)


def ceildiv(a: int, b: int) -> int:
    require(b > 0, 'positive denominator required')
    return -((-a)//b)


class I:
    __slots__=('lo','hi')
    def __init__(self, lo: int, hi: int):
        require(type(lo) is int and type(hi) is int and lo <= hi, 'bad interval')
        self.lo,self.hi=lo,hi
    @staticmethod
    def q(n=0,d=1):
        if isinstance(n,F):
            return I.q(n.numerator,n.denominator)
        if d < 0:n,d=-n,-d
        require(type(n) is int and type(d) is int and d>0, 'rational required')
        return I((n*S)//d,ceildiv(n*S,d))
    def __add__(self,v):
        if not isinstance(v,I):v=I.q(v)
        return I(self.lo+v.lo,self.hi+v.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,v):return self+-as_i(v)
    def __rsub__(self,v):return as_i(v)+-self
    def __mul__(self,v):
        v=as_i(v)
        z=[self.lo*v.lo,self.lo*v.hi,self.hi*v.lo,self.hi*v.hi]
        return I(min(z)//S,ceildiv(max(z),S))
    __rmul__=__mul__
    def __truediv__(self,v):
        v=as_i(v)
        require(v.lo>0 or v.hi<0,'division through zero')
        if v.hi<0:return (-self)/(-v)
        return self*I((S*S)//v.hi,ceildiv(S*S,v.lo))
    def square(self):
        vals=[self.lo*self.lo,self.hi*self.hi]
        return I(0 if self.lo<=0<=self.hi else min(vals)//S,ceildiv(max(vals),S))
    def widen(self,n:int):return I(self.lo-n,self.hi+n)
    def encloses(self,x:F):return self.lo*x.denominator<=x.numerator*S<=self.hi*x.denominator
    def exact(self):return [str(F(self.lo,S)),str(F(self.hi,S))]
    def decimal(self,digits=15):
        a=10**digits
        def fmt(n):
            sign='-' if n<0 else '';n=abs(n)
            return f'{sign}{n//a}.{n%a:0{digits}d}'
        return [fmt(self.lo*a//S),fmt(ceildiv(self.hi*a,S))]


def as_i(v):return v if isinstance(v,I) else I.q(v)


def atanh_log(z_num:int,z_den:int,terms:int)->I:
    # 2 atanh(z), z>=0; tail <=2 z^(2t+1)/((2t+1)(1-z^2)).
    require(0<=z_num<z_den,'atanh domain')
    if not z_num:return I.q(0)
    z=I.q(z_num,z_den);zz=z*z;power=z;acc=I.q(0)
    for j in range(terms):
        acc+=power/I.q(2*j+1);power=power*zz
    num=2*pow(z_num,2*terms+1)*z_den*z_den
    den=(2*terms+1)*pow(z_den,2*terms+1)*(z_den*z_den-z_num*z_num)
    ans=2*acc
    return I(ans.lo,ans.hi+ceildiv(num*S,den))


@lru_cache(None)
def log_int(n:int)->I:
    require(type(n)is int and n>=1,'positive integer log')
    if n==1:return I.q(0)
    if n==2:return atanh_log(1,3,100)
    k=n.bit_length()-1;d=1<<k
    return k*log_int(2)+atanh_log(n-d,n+d,100)


@lru_cache(None)
def weight(q:int,r:int)->I:
    require(1<=r<=q,'period residue')
    K=32;acc=I.q(0)
    for k in range(K):
        a=r+q*k;acc+=I.q(1,a*(a+1))
    a=r+q*K
    acc+=atanh_log(1,2*a+1,20)/q+I.q(1,2*a*(a+1))
    last=0
    for j,(bn,bd) in enumerate(BERNOULLI,1):
        num=bn*pow(q,2*j-1)*(pow(a+1,2*j)-pow(a,2*j))
        den=bd*(2*j)*pow(a,2*j)*pow(a+1,2*j)
        acc+=I.q(num,den)
        last=ceildiv(abs(num)*S,den)
    # Standard EM including B16 term; bound the full remainder by that term.
    ans=acc.widen(last)
    require(ans.lo>0,'weight failed positive enclosure')
    return ans


def mu_trial(n:int)->int:
    require(n>=1,'mu domain');sign=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
        p+=1
    return -sign if n>1 else sign


def gram(N:int):
    G={}
    for n in range(2,N+1):
        for m in range(2,n+1):
            q=math.lcm(n,m);acc=I.q(0)
            for r in range(1,q+1):
                num=(r%n)*(r%m)
                if num:acc+=weight(q,r)*I.q(num,n*m)
            G[n,m]=G[m,n]=acc
    return G


def rational(s):
    require(type(s)is str,'rational strings only')
    f=F(s);require(str(f)==s,'canonical rational required');return f


def coeffs(case):
    Y,N=case['Y'],case['N']
    require(type(Y)is int and type(N)is int and Y>=2 and N==2*Y,'case domain')
    require(set(case['free'])=={str(n) for n in range(Y+1,N)},'free support')
    a={n:I.q(mu_trial(n)) for n in range(1,Y)}
    for n in range(Y+1,N):a[n]=I.q(rational(case['free'][str(n)]))
    s0=sum((v/n for n,v in a.items()),I.q(0))
    s1=sum((v*log_int(n)/n for n,v in a.items()),I.q(0))
    y=(-1-s1+s0*log_int(Y))/log_int(2)
    x=-s0-y
    a[Y]=Y*x;a[N]=N*y
    # These are checks of interval algebra; exact feasibility is proved by formula.
    require(sum((a[n]/n for n in a),I.q(0)).encloses(F(0)),'balance enclosure')
    require(sum((-a[n]*log_int(n)/n for n in a),I.q(0)).encloses(F(1)),'jet enclosure')
    return a


def certificate(case):
    Y,N=case['Y'],case['N'];a=coeffs(case);G=gram(N)
    E=I.q(-1)
    for n in range(2,N+1):
        E+=a[n].square()*G[n,n]
        for m in range(2,n):E+=2*a[n]*a[m]*G[n,m]
    dual=[I.q(rational(v)) for v in case['dual']]
    require(len(dual)==2,'dual length')
    rho=I.q(0)
    for n in range(Y,N+1):
        res=sum((G[n,m]*a[m] for m in range(2,N+1)),I.q(0))-dual[0]/n-dual[1]*log_int(n)/n
        rho+=res.square()
    inv_lambda=4*(N//Y)**2*N*(N+1)
    opt=I(E.lo-inv_lambda*rho.hi,E.hi)
    require(opt.lo>0,'not a positive minimum certificate')
    require(opt.hi-opt.lo<ceildiv(S,10**10),'minimum enclosure too wide')
    return {'Y':Y,'N':N,'energy_exact':E.exact(),'energy_decimal':E.decimal(),
            'minimum_exact':opt.exact(),'minimum_decimal':opt.decimal(),
            'coercivity':str(F(1,inv_lambda)), 'squared_stationarity_upper':str(F(rho.hi,S)),
            'max_pair_period':max(math.lcm(m,n) for n in range(2,N+1) for m in range(2,n+1)),
            'unused_global_period':math.lcm(*range(1,N+1))}


def controls():
    out={}
    fixtures=0
    # Primitive rational enclosure operations checked against exact Fraction.
    vals=[F(-7,5),F(-1,3),F(0),F(2,7),F(5,2)]
    for a in vals:
      for b in vals:
        require((I.q(a)+I.q(b)).encloses(a+b),'add')
        require((I.q(a)*I.q(b)).encloses(a*b),'multiply')
        if b:require((I.q(a)/I.q(b)).encloses(a/b),'divide')
        fixtures+=1
    out['rational_pairs']=fixtures
    require((2*log_int(2)-log_int(4)).encloses(F(0)),'log scaling')
    # Independent direct sums plus elementary infinite-tail enclosure.
    for q in range(1,13):
      sw=I.q(0)
      for r in range(1,q+1):
        a=sum((F(1,(r+k*q)*(r+1+k*q)) for k in range(256)),F(0))
        hi=a+F(1,q*(r+255*q))
        w=weight(q,r)
        require(w.lo>=I.q(a).lo and w.hi<=I.q(hi).hi,'EM outside elementary enclosure')
        sw+=w
      require(sw.encloses(F(1)),'period mass')
    out['period_weight_residues']=sum(range(1,13))
    # All balanced tail examples: exact finite first-cell bound vs coefficient norm.
    cases=0
    for Y in range(2,13):
      for N in range(Y+1,3*Y+1):
        a={Y:F(1),N:-F(N,Y)}
        A=[sum((v*(j//n) for n,v in a.items()),F(0)) for j in range(N+1)]
        finite=sum((A[j]**2/F(j*(j+1)) for j in range(1,N+1)),F(0))
        coeff=sum((x*x for x in a.values()),F(0))
        require(finite>=coeff/F(4*(N//Y)**2*N*(N+1)),'coercivity fixture')
        # Exact triangular Mobius inversion, including all endpoint jumps.
        for j in range(Y,N+1):
          recovered=sum((mu_trial(k)*(A[j//k]-A[j//k-1]) for k in range(1,j+1) if j%k==0),F(0))
          require(recovered==a.get(j,F(0)),'inversion')
        cases+=1
    out['finite_coercivity_packets']=cases
    # Norm of the oblique projection, using rational c^2 in (0,1).
    for v in [F(1,4),F(1,2),F(3,4),F(7,8)]:
      # In basis {1,pulse}, E(A+B pulse)=A^2+v(2AB+B^2).
      for A in [-2,-1,0,1,2]:
        for B in [-2,-1,0,1,2]:
          before=A*A+v*(2*A*B+B*B)
          # P(A+B pulse)=A(1-pulse/v).
          after=A*A*(1/v-1)
          require(after<=before/v,'projection norm')
      out['projection_rational_packets']=100
    # Determinant form of normalized two-point Hardy interpolation.
    for alpha in [F(1,10),F(1,4),F(2,5)]:
      for gamma in [F(1),F(3),F(7)]:
        # det of [1,1/rho;1/conj rho,1/(2alpha)]
        absrho=(alpha+F(1,2))**2+gamma**2
        absrho1=(alpha-F(1,2))**2+gamma**2
        require(F(1,2*alpha)-1/absrho==absrho1/(2*alpha*absrho),'Hardy Schur identity')
    out['hardy_schur_packets']=9
    return out


def strict_equal(a,b):
    if type(a) is not type(b):return False
    if isinstance(a,dict):return set(a)==set(b) and all(strict_equal(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(strict_equal(x,y) for x,y in zip(a,b))
    return a==b


def check_manifest():
    manifest=ROOT/'SHA256SUMS'
    if not manifest.is_file():raise ValueError('missing manifest')
    expected={}
    for line in manifest.read_text().splitlines():
        parts=line.split('  ')
        require(len(parts)==2,'manifest syntax')
        digest,name=parts
        require(name and '/' not in name and '\\' not in name and name not in expected,'manifest path')
        require(len(digest)==64 and all(c in '0123456789abcdef' for c in digest),'manifest digest')
        expected[name]=digest
    actual={p.name for p in ROOT.iterdir()}
    required={'PROOF.md','README.md','SOURCES.json','VALIDATION.md','candidates.json','result.json','verify.py','test_rejections.py'}
    require(set(expected)==required,'manifest coverage')
    require(actual==required|{'SHA256SUMS'},'file coverage')
    require(expected,'empty manifest')
    for name,digest in expected.items():
        p=ROOT/name
        require(p.is_file() and not p.is_symlink(),'invalid file')
        require(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'changed file: '+name)


def no_duplicates(pairs):
    d={}
    for k,v in pairs:
        require(k not in d,'duplicate JSON key');d[k]=v
    return d


def load(path):
    return json.loads(Path(path).read_text(),object_pairs_hook=no_duplicates,
                      parse_float=lambda x: (_ for _ in ()).throw(ValueError('float forbidden')))


def run(only=None):
    data=load(ROOT/'candidates.json')
    require(data['status']=='rational candidates, not numerical proof inputs','candidate status')
    cases=data['cases'];require([x['Y'] for x in cases]==[2,4,8,16],'candidate coverage')
    result={'status':'bounded component verification; RH and global energy upper bound unproved',
      'rh_proved':False,'unbounded_energy_bound_proved':False,'bits':BITS,
      'controls':controls(),'certificates':[]}
    for c in cases:
        if only is None or c['Y']==only:result['certificates'].append(certificate(c))
    return result


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',type=Path);ap.add_argument('--check',type=Path);ap.add_argument('--only',type=int)
    args=ap.parse_args()
    saved=None
    if args.check:
        check_manifest()
        require(args.only is None,'cannot accept partial run as full')
        saved=load(args.check)
        require(type(saved.get('rh_proved'))is bool and saved['rh_proved'] is False,'false RH status')
        require(type(saved.get('unbounded_energy_bound_proved'))is bool and saved['unbounded_energy_bound_proved'] is False,'false upper bound')
        require(type(saved.get('bits'))is int and saved['bits']==BITS,'integer precision')
    res=run(args.only)
    text=json.dumps(res,indent=2,sort_keys=True)+'\n'
    if args.write:args.write.write_text(text)
    if args.check:
        require(strict_equal(saved,res),'reconstructed result mismatch')
    print(text,end='')

if __name__=='__main__':main()
