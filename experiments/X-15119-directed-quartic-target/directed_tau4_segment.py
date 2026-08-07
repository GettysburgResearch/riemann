#!/usr/bin/env python3
from decimal import Decimal, getcontext, localcontext, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction
import json, os, time

PREC=70
EXTRA=30
getcontext().prec=PREC

class IV:
    __slots__=('lo','hi')
    def __init__(self, lo, hi=None):
        self.lo = lo if isinstance(lo,Decimal) else Decimal(lo)
        self.hi = self.lo if hi is None else (hi if isinstance(hi,Decimal) else Decimal(hi))
        if self.lo>self.hi: raise ValueError((self.lo,self.hi))
    def __add__(self,o):
        o=asiv(o)
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_FLOOR; lo=self.lo+o.lo
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_CEILING; hi=self.hi+o.hi
        return IV(lo,hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-asiv(o))
    def __rsub__(self,o): return asiv(o)-self
    def __mul__(self,o):
        o=asiv(o)
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_FLOOR
            lo=min(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_CEILING
            hi=max(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return IV(lo,hi)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asiv(o)
        if o.lo<=0<=o.hi: raise ZeroDivisionError
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_FLOOR
            lo=min(self.lo/o.lo,self.lo/o.hi,self.hi/o.lo,self.hi/o.hi)
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_CEILING
            hi=max(self.lo/o.lo,self.lo/o.hi,self.hi/o.lo,self.hi/o.hi)
        return IV(lo,hi)
    def __rtruediv__(self,o): return asiv(o)/self
    def pow_int(self,n):
        if n<0: return IV(1)/self.pow_int(-n)
        r=IV(1); x=self
        while n:
            if n&1:r=r*x
            x=x*x;n//=2
        return r
    def exp(self): return IV(exp_lo(self.lo),exp_hi(self.hi))
    def widen(self,e):
        e=Decimal(e); return IV(self.lo-e,self.hi+e)

def asiv(x): return x if isinstance(x,IV) else IV(x)
def exp_near(x):
    with localcontext() as c:
        c.prec=PREC+EXTRA; c.rounding=ROUND_HALF_EVEN; return x.exp()
def exp_lo(x):
    y=exp_near(x)
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR; y=+y; return y.next_minus(c)
def exp_hi(x):
    y=exp_near(x)
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING; y=+y; return y.next_plus(c)
def frac_to_dec(f, rounding):
    with localcontext() as c:
        c.prec=PREC; c.rounding=rounding; return Decimal(f.numerator)/Decimal(f.denominator)
def atan_bounds(q,K):
    S=Fraction(0)
    for k in range(K+1):
        t=Fraction(1,(2*k+1)*q**(2*k+1)); S=S+t if k%2==0 else S-t
    nxt=Fraction(1,(2*K+3)*q**(2*K+3)); nxt=-nxt if (K+1)%2 else nxt
    T=S+nxt; return min(S,T),max(S,T)
a5=atan_bounds(5,110); a239=atan_bounds(239,30)
pilo=16*a5[0]-4*a239[1]; pihi=16*a5[1]-4*a239[0]
PI=IV(frac_to_dec(pilo,ROUND_FLOOR),frac_to_dec(pihi,ROUND_CEILING))

START=Decimal(os.environ.get('START','0')); END=Decimal(os.environ.get('END','1'))
H=Decimal(1)/Decimal(20000); NINT=int((END-START)/H); NMAX=8
M4={0:Decimal('2e9'),2:Decimal('1e10'),4:Decimal('5e10')}
TAIL=Decimal('1e-50')

def phi_at(u):
    Uiv=IV(u); e2=(IV(2)*Uiv).exp(); e45=(IV(Decimal('4.5'))*Uiv).exp(); e25=(IV(Decimal('2.5'))*Uiv).exp()
    total=IV(0)
    for ni in range(1,NMAX+1):
        n=Decimal(ni); n2=n*n; n4=n2*n2; z=PI*IV(n2)*e2
        total += (IV(2)*PI.pow_int(2)*IV(n4)*e45-IV(3)*PI*IV(n2)*e25)*(-z).exp()
    return total

def simpson_moments():
    sums={0:IV(0),2:IV(0),4:IV(0)}; t0=time.time()
    for i in range(NINT+1):
        u=START+H*Decimal(i); ph=phi_at(u)
        w=Decimal(1 if i==0 or i==NINT else (4 if i%2 else 2)); u2=u*u; u4=u2*u2
        sums[0]+=ph*IV(w); sums[2]+=ph*IV(w*u2); sums[4]+=ph*IV(w*u4)
        if i and i%5000==0: print('i',i,'sec',time.time()-t0,flush=True)
    out={}
    for k in [0,2,4]:
        s=sums[k]*IV(H)/IV(3)
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_CEILING
            err=(END-START)/Decimal(180)*(H**4)*M4[k]+TAIL/Decimal(2)
        out[k]=s.widen(err)
    return out

I=simpson_moments(); X={k:I[k]*IV(4) for k in I}; tau2=X[2]/X[0]
tau4=-(X[4]/X[0]-IV(3)*tau2.pow_int(2))/IV(6)
res={'precision_decimal_digits':PREC,'start':str(START),'end':str(END),'h':str(H),'subintervals':NINT,'nmax':NMAX,
 'pi':[str(PI.lo),str(PI.hi)],
 'I0':[str(I[0].lo),str(I[0].hi)],'I2':[str(I[2].lo),str(I[2].hi)],'I4':[str(I[4].lo),str(I[4].hi)],
 'xi0':[str(X[0].lo),str(X[0].hi)],'xi2':[str(X[2].lo),str(X[2].hi)],'xi4':[str(X[4].lo),str(X[4].hi)],
 'tau2':[str(tau2.lo),str(tau2.hi)],'tau4':[str(tau4.lo),str(tau4.hi)],
 'simpson_M4':{str(k):str(v) for k,v in M4.items()},'tail_budget':str(TAIL)}
print(json.dumps(res,indent=2))
