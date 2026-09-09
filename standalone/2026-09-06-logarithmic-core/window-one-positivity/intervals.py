"""Small outward dyadic interval backend; no floating point in acceptance."""
from fractions import Fraction
from math import factorial,comb
BITS=192
S=1<<BITS

def floorq(q): return q.numerator//q.denominator

def ceilq(q): return -((-q.numerator)//q.denominator)

class I:
    __slots__=('lo','hi')
    def __init__(self,x=0):
        if isinstance(x,I): self.lo,self.hi=x.lo,x.hi;return
        if isinstance(x,(bool,float)):raise TypeError('exact input required')
        x=Fraction(x); self.lo=floorq(x*S);self.hi=ceilq(x*S)
    @classmethod
    def raw(cls,a,b):
        if a>b:raise ValueError('reversed interval')
        z=object.__new__(cls);z.lo,z.hi=int(a),int(b);return z
    def __add__(self,y):
        y=I(y);return I.raw(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self):return I.raw(-self.hi,-self.lo)
    def __sub__(self,y):return self+-I(y)
    def __rsub__(self,y):return I(y)+-self
    def __mul__(self,y):
        y=I(y);v=[self.lo*y.lo,self.lo*y.hi,self.hi*y.lo,self.hi*y.hi]
        return I.raw(min(v)//S,-((-max(v))//S))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError('interval contains zero')
        return I.raw(S*S//self.hi,-((-S*S)//self.lo))
    def __truediv__(self,y):return self*I(y).inv()
    def __rtruediv__(self,y):return I(y)*self.inv()
    def __pow__(self,n):
        if not isinstance(n,int) or isinstance(n,bool):raise TypeError('integer power')
        if n<0:return self.inv()**(-n)
        if n==0:return I(1)
        # generic interval multiplication remains outward even across zero
        out=I(1);base=self
        while n:
            if n&1:out=out*base
            base=base*base;n//=2
        return out
    def abs(self):
        if self.lo>=0:return self
        if self.hi<=0:return -self
        return I.raw(0,max(-self.lo,self.hi))
    def widen(self,e):
        e=I(e)
        if e.lo<0:raise ValueError('negative radius')
        return I.raw(self.lo-e.hi,self.hi+e.hi)
    def low(self):return Fraction(self.lo,S)
    def high(self):return Fraction(self.hi,S)
    def bounds(self):return [str(self.low()),str(self.high())]

def atan_small(x,terms=160):
    x=I(x)
    if x.abs().hi>S//2:raise ValueError('atan range')
    t=x;v=I(0);x2=x*x
    for k in range(terms):
        v+=t/(2*k+1);t=-t*x2
    return v.widen(x.abs()**(2*terms+1)/(2*terms+1)/(1-x.abs()**2))

PI=16*atan_small(Fraction(1,5))-4*atan_small(Fraction(1,239))

def log_unit(x):
    x=I(x)
    if x.lo<S or x.hi>2*S:raise ValueError('log unit range')
    z=(x-1)/(x+1);q=z*z;t=z;v=I(0)
    for k in range(80):v+=t/(2*k+1);t=t*q
    return (2*v).widen(2*I(Fraction(1,3))**161/Fraction(161)/(1-Fraction(1,9)))
LOG2=log_unit(I(2))

def log_pos(x):
    x=I(x)
    if x.lo<=0:raise ValueError('positive log input')
    # monotonicity, exact rational endpoints, independently scaled
    def endpoint(t):
        k=t.numerator.bit_length()-t.denominator.bit_length()
        if t<Fraction(2)**k:k-=1
        u=t/Fraction(2)**k
        return log_unit(I(u))+k*LOG2
    a=endpoint(x.low());b=endpoint(x.high());return I.raw(a.lo,b.hi)

def exp_i(x):
    x=I(x)
    return _exp_cached(x.lo,x.hi)

from functools import lru_cache
@lru_cache(maxsize=8192)
def _exp_cached(lo,hi):
    x=I.raw(lo,hi)
    if x.lo<0<x.hi:
        return I.raw(exp_i(I.raw(x.lo,x.lo)).lo,exp_i(I.raw(x.hi,x.hi)).hi)
    if x.hi<=-128*S:return I.raw(0,1<<(BITS-128))
    if x.lo<0:return exp_i(-x).inv()
    if x.hi>1024*S:raise ValueError('exp range')
    k=0;y=x
    while y.hi>S//2:y=y/2;k+=1
    term=I(1);v=I(1)
    for j in range(1,90):term=term*y/j;v+=term
    # exp(y)<=2 and Taylor remainder <=2*(1/2)^90/90!
    v=v.widen(Fraction(2,2**90*factorial(90)))
    for _ in range(k):v=v*v
    return v

def sincos(x):
    x=I(x)
    return _trig_cached(x.lo,x.hi)

@lru_cache(maxsize=8192)
def _trig_cached(lo,hi):
    x=I.raw(lo,hi)
    # chosen integer is not a numerical assertion; identity holds for every q
    q=(2*(x.lo+x.hi)+(PI.lo+PI.hi)//2)//(PI.lo+PI.hi)
    r=x-q*PI/2
    if r.abs().hi>S:raise ValueError('trig reduced range')
    rr=r*r;ct=I(1);st=r;cv=ct;sv=st
    for k in range(1,40):
        ct=-ct*rr/((2*k-1)*(2*k));st=-st*rr/((2*k)*(2*k+1))
        cv+=ct;sv+=st
    cv=cv.widen(Fraction(1,factorial(80)));sv=sv.widen(Fraction(1,factorial(80)))
    q%=4
    return [(sv,cv),(cv,-sv),(-sv,-cv),(-cv,sv)][q]

def cos_i(x):return sincos(x)[1]
def sinh(x):return (exp_i(x)-exp_i(-I(x)))/2
def cosh(x):return (exp_i(x)+exp_i(-I(x)))/2

def bernoulli(n):
    arr=[Fraction(1)]
    for m in range(1,n+1):arr.append(-sum(Fraction(comb(m+1,k))*arr[k] for k in range(m))/Fraction(m+1))
    return arr
BERN=bernoulli(40)

# psi asymptotic through B_38, remainder bounded by DLMF 5.11(ii):
# sec^(41)(arg(z)/2)<=2^21 when Re(z)>0.
def psi_real(a,y):
    a=I(a);y=I(y);z=a+64
    denom=z*z+y*y;ir=z/denom;ii=-y/denom
    v=log_pos(denom)/2-ir/2
    # powers of (z+iy)^-2
    qr=ir*ir-ii*ii;qi=2*ir*ii;pr=I(1);pm=I(0)
    for k in range(1,20):
        pr,pm=pr*qr-pm*qi,pr*qi+pm*qr
        v-=I(BERN[2*k])/ (2*k)*pr
    err=I(2**21*abs(BERN[40])/40)/(z**40)
    v=v.widen(err)
    for k in range(64):v-=(a+k)/((a+k)**2+y*y)
    return v
GAMMA=-psi_real(1,0)
CB=(1-GAMMA-log_pos(2*PI))/3

def p2_interval():
    # Euler--Maclaurin zeta derivative at 2; all constants exact intervals.
    N=64;m=20;l=log_pos(N)
    v=-sum((log_pos(n)/n**2 for n in range(1,N)),I(0))-(l+1)/N-l/(2*N*N)
    for k in range(1,m+1):
        hs=sum((Fraction(1,j) for j in range(2,2*k+1)),Fraction(0))
        v+=I(BERN[2*k])*I(Fraction(1,N**(2*k+1)))*(hs-l)
    prod=Fraction(1)
    for j in range(2*m):prod*=Fraction(9,4)+j
    # |s-2|=1/4, |R| <= |B_40|/40! prod / (40*N^40)
    err=4*abs(BERN[2*m])*prod/Fraction(factorial(2*m)*2*m*N**(2*m))
    v=v.widen(err)
    return -6*v/(PI*PI)
P2=p2_interval()
