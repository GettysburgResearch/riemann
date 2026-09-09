"""Source-only rational interval jets; no zero tables or floating acceptance.
See SOURCE_COMPILER.md for analytic tails. All matrices use the full source.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, isqrt
import argparse, hashlib, json

BITS = 640
SCALE = 1 << BITS

def require(test: bool, message: str) -> None:
    if not test:
        raise ValueError(message)

def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)

@dataclass(frozen=True)
class I:
    lo: int
    hi: int
    def __post_init__(self):
        require(type(self.lo) is int and type(self.hi) is int and self.lo <= self.hi, 'invalid interval')
    @staticmethod
    def of(x=0):
        if isinstance(x, I): return x
        require(type(x) is int or isinstance(x,F), 'exact numeric type required')
        q = F(x)
        return I(q.numerator*SCALE//q.denominator, ceil_div(q.numerator*SCALE,q.denominator))
    def __add__(self, other):
        o=I.of(other); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,other): return self+-I.of(other)
    def __rsub__(self,other): return I.of(other)+-self
    def __mul__(self,other):
        o=I.of(other); p=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(p)//SCALE,ceil_div(max(p),SCALE))
    __rmul__=__mul__
    def reciprocal(self):
        require(not self.lo <= 0 <= self.hi, 'division interval contains zero')
        return I(SCALE*SCALE//self.hi,ceil_div(SCALE*SCALE,self.lo))
    def __truediv__(self,other): return self*I.of(other).reciprocal()
    def __rtruediv__(self,other): return I.of(other)*self.reciprocal()
    def widen(self, radius):
        r=I.of(radius).hi; require(r>=0,'negative radius'); return I(self.lo-r,self.hi+r)
    def width(self): return F(self.hi-self.lo,SCALE)
    def bounds(self, digits=80):
        d=10**digits
        def txt(n):
            whole,part=divmod(abs(n),d)
            return ('-' if n<0 else '')+str(whole)+'.'+str(part).zfill(digits)
        return [txt(self.lo*d//SCALE),txt(ceil_div(self.hi*d,SCALE))]
    def mid(self): return F(self.lo+self.hi,2*SCALE)

@lru_cache(None)
def log_rational(q: F) -> I:
    q=F(q); require(q>0,'log domain'); e=0
    while q>=2: q/=2; e+=1
    while q<1: q*=2; e-=1
    def series(t):
        sm=F(0); power=t; j=0
        while True:
            sm+=power/F(2*j+1); j+=1; power*=t*t
            tail=2*abs(power)/(F(2*j+1)*(1-t*t))
            if tail < F(1,1 << (BITS+8)): break
        val=2*sm
        return I.of(val).widen(tail)
    # On [1,2), t>=0; symmetric widening remains outward.
    ans=series((q-1)/(q+1))
    if e: ans+=e*series(F(1,3))
    return ans

@lru_cache(None)
def sqrt_rational(q: F) -> I:
    q=F(q); require(q>=0,'sqrt domain')
    v=isqrt(q.numerator*SCALE*SCALE//q.denominator)
    return I(v, v if v*v*q.denominator==q.numerator*SCALE*SCALE else v+1)

@lru_cache(None)
def pi_interval() -> I:
    def atan(t):
        sm=F(0); power=t; j=0
        while True:
            sm+=((-1)**j)*power/F(2*j+1); j+=1; power*=t*t
            tail=power/F(2*j+1)
            if tail<F(1,1 << (BITS+8)): break
        return I.of(sm).widen(tail)
    return 16*atan(F(1,5))-4*atan(F(1,239))

def log_interval(q: I) -> I:
    require(q.lo>0,'log interval domain')
    return I(log_rational(F(q.lo,SCALE)).lo,log_rational(F(q.hi,SCALE)).hi)

@lru_cache(None)
def bernoulli(j: int) -> F:
    if j==0: return F(1)
    return -sum((F(comb(j+1,k))*bernoulli(k) for k in range(j)),F(0))/F(j+1)

def const(x, n): return [I.of(x)]+[I.of(0)]*n

def add(a,b):
    require(len(a)==len(b),'series shape'); return [x+y for x,y in zip(a,b)]

def scale(a,x): return [v*x for v in a]

def mul(a,b):
    require(len(a)==len(b),'series shape'); n=len(a)
    return [sum((a[j]*b[k-j] for j in range(k+1)),I.of(0)) for k in range(n)]

def inv(a):
    out=[1/a[0]]
    for k in range(1,len(a)):
        out.append(-sum((a[j]*out[k-j] for j in range(1,k+1)),I.of(0))/a[0])
    return out

def div(a,b): return mul(a,inv(b))

def exp_zero(a):
    require(a[0].lo==a[0].hi==0,'exp requires zero constant'); out=[I.of(1)]
    for k in range(1,len(a)):
        out.append(sum((j*a[j]*out[k-j] for j in range(1,k+1)),I.of(0))/k)
    return out

def log_series(a):
    n=len(a)-1; require(a[0].lo>0,'log series constant')
    if not n: return [log_interval(a[0])]
    d=[(j+1)*a[j+1] for j in range(n)]
    quot=mul(d,inv(a)[:n])
    return [log_interval(a[0])]+[quot[j-1]/j for j in range(1,n+1)]

def compose(a,b):
    require(b[0].lo==b[0].hi==0,'compose requires zero constant')
    out=const(0,len(b)-1)
    for c in reversed(a):
        out=mul(out,b); out[0]+=c
    return out

def s_series(center, degree): return [I.of(center)]+[I.of(2)]*degree

def n_minus_s(k,center,degree):
    # Only half-integer centers 3/2,2,5/2 are supported by this producer.
    require(center in (F(3,2),F(2),F(5,2)),'unsupported safe center')
    h=const(0,degree); lk=log_rational(F(k))
    for j in range(1,degree+1): h[j]=-2*lk
    base=I.of(F(1,k*k)) if center==2 else I.of(F(1,k**int(center)))/sqrt_rational(F(k))
    return scale(exp_zero(h),base)

def zeta_em(center,degree,M,K):
    s=s_series(center,degree); total=const(0,degree)
    for k in range(1,K): total=add(total,n_minus_s(k,center,degree))
    sm1=s.copy(); sm1[0]-=1
    bracket=scale(inv(sm1),K); bracket[0]+=F(1,2)
    product=const(1,degree)
    for j in range(2*M-1):
        factor=s.copy(); factor[0]+=j
        product=mul(product,scale(factor,F(1,K)))
        if j%2==0:
            h=(j+2)//2
            bracket=add(bracket,scale(product,bernoulli(2*h)/factorial(2*h)))
    return add(total,mul(n_minus_s(K,center,degree),bracket))

def psi_em(center,degree,M,K):
    # v=s/2; shift to v+K before the Bernoulli expansion.
    v=scale(s_series(center,degree),F(1,2)); z=v.copy(); z[0]+=K
    iz=inv(z); result=add(log_series(z),scale(iz,F(-1,2)))
    iz2=mul(iz,iz); power=const(1,degree)
    for j in range(1,M+1):
        power=mul(power,iz2)
        result=add(result,scale(power,-bernoulli(2*j)/F(2*j)))
    for j in range(K):
        den=v.copy(); den[0]+=j
        result=add(result,scale(inv(den),-1))
    return result

def parameters(degree,guard):
    require(type(degree) is int and 0<=degree<=32,'degree cap is 32')
    require(type(guard) is int and 0<=guard<=512,'guard cap is 512')
    M=degree+(guard+3)//4+4; K=2*M+3
    return M,K,F(4,36**M)

def logxi_jet(center,degree,guard):
    M,K,delta=parameters(degree,guard)
    zz=zeta_em(center,degree+1,M,K)
    dzz=[(j+1)*zz[j+1] for j in range(degree+1)]
    fac=const(F(1,2),degree)
    if degree>=1: fac[1]=I.of(-1)
    if degree>=2: fac[2]=I.of(F(1,2))
    dz=mul(fac,div(dzz,zz[:degree+1]))
    psi=psi_em(center,degree,M,K)
    s=s_series(center,degree); sm1=s.copy(); sm1[0]-=1
    L=add(add(inv(s),inv(sm1)),add(scale(psi,F(1,2)),dz))
    L[0]-=log_interval(pi_interval())/2
    # Proof: logarithm-ratio Cauchy bound 55(j+1)delta*8^j;
    # shifted digamma remainder <=delta, contributing delta/2.
    return [a.widen((F(55*(j+1))+F(1,2))*delta*8**j) for j,a in enumerate(L)]

def mobius_coefficients(degree,guard):
    M,K,delta=parameters(degree,guard)
    zz=zeta_em(F(3,2),degree,M,K)
    q=n_minus_s(67,F(3,2),degree)
    local=scale(q,-1); local[0]+=1
    a=mul(inv(mul(zz,local)),[I.of(1)]*(degree+1))
    ans=[x.widen(36*delta*8**j) for j,x in enumerate(a)]
    target=F(1,2**(degree+guard))
    require(all(x.width()<=target for x in ans),'insufficient interval precision')
    return ans,{'degree':degree,'guard':guard,'M':M,'K':K,'delta':str(delta),'width_target':str(target)}

def invariant_moments(degree,guard):
    L=logxi_jet(F(2),degree,guard)
    h=const(0,degree)
    if degree: h[1]=I.of(F(1,3))
    for j in range(2,degree+1):
        h[j]=-sum((h[k]*h[j-k] for k in range(1,j)),I.of(0))/3
    den=h.copy(); den[0]+=2
    z=div(h,den); d=scale(h,2); d[0]+=3
    q=div(compose(L,z),d)
    return [x*((-1)**j) for j,x in enumerate(q)]

def hardy_matrix(size,guard):
    require(type(size) is int and 1<=size<=16,'matrix size cap')
    n=size-1; L=logxi_jet(F(5,2),n,guard)
    Lb=logxi_jet(F(2),0,guard)[0]
    r=[I.of(2)]*size
    den=scale(mul(r,r),-1); den[0]+=F(9,4)
    c=div(add(L,scale(r,-F(2,3)*Lb)),den)
    A=[[I.of(0) for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            source=(c[i] if j==0 else I.of(0))+(c[j] if i==0 else I.of(0))
            A[i][j]=source+((A[i-1][j] if i else I.of(0))+(A[i][j-1] if j else I.of(0)))/2
    return A,c

def ldl_pivots(A):
    n=len(A); L=[[I.of(int(i==j)) for j in range(n)] for i in range(n)]; piv=[]
    for j in range(n):
        p=A[j][j]-sum((L[j][k]*L[j][k]*piv[k] for k in range(j)),I.of(0))
        require(p.lo>0,'positive pivot not certified')
        piv.append(p)
        for i in range(j+1,n):
            L[i][j]=(A[i][j]-sum((L[i][k]*L[j][k]*piv[k] for k in range(j)),I.of(0)))/p
    return piv

def produce():
    a,meta=mobius_coefficients(12,96)
    moments=invariant_moments(9,192)
    # Positive diagonal congruence improves conditioning without changing signs.
    H=[[moments[i+j]*(200**(i+j)) for j in range(5)] for i in range(5)]
    Hp=[[moments[i+j+1]*(200**(i+j+1)) for j in range(5)] for i in range(5)]
    hp=ldl_pivots(H); hpp=ldl_pivots(Hp)
    A,c=hardy_matrix(8,192); ap=ldl_pivots(A)
    E=sum((v*v for v in a),I.of(0))
    # All quantities are reconstructed, not read from stored PASS fields.
    return {'schema':1,'RH_proved':False,'arithmetic':'OUTWARD_BINARY_RATIONAL_INTERVALS_WITH_PROVED_ANALYTIC_TAILS',
      'bits':BITS,'mobius_parameters':meta,
      'mobius_coefficients':[v.bounds() for v in a],'energy_through_12':E.bounds(),
      'invariant_moments':[v.bounds() for v in moments],
      'H5_LDL_pivots':[v.bounds() for v in hp],'Hplus5_LDL_pivots':[v.bounds() for v in hpp],
      'Hardy8_LDL_pivots':[v.bounds() for v in ap],
      'Hardy8_source_c':[v.bounds() for v in c],
      'finite_positive_pivots':18,'global_sign_estimate_proved':False}

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--output'); p.add_argument('--check'); args=p.parse_args()
    result=produce(); data=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.check:
        from pathlib import Path
        require(Path(args.check).read_text()==data,'saved result differs from fresh source computation')
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(data)
    print(data,end='')
