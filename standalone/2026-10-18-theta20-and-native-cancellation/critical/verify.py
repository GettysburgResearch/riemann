#!/usr/bin/env python3
"""Finite exact checks and an outward rational certificate; not an RH checker.

The sign certificate uses only integer and Fraction arithmetic. A separate
ordinary binary64 comparison checks finite Gaussian kernels by integration;
it is explicitly non-certified and never supplies an infinite theorem.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import sys

BITS=128
SCALE=1 << BITS
predicates=0

def require(ok, label):
    global predicates
    predicates += 1
    if not ok:
        raise ValueError(label)

def ceil_div(a,b):
    return -((-a)//b)

class I:
    """Closed outward interval with integer endpoints / 2**BITS."""
    __slots__=("lo","hi")
    def __init__(self,lo,hi):
        if lo>hi: raise ValueError("interval order")
        self.lo,self.hi=lo,hi
    @staticmethod
    def rat(n,d=1):
        if d<=0: raise ValueError("positive rational denominator")
        return I((n*SCALE)//d,ceil_div(n*SCALE,d))
    def __add__(self,o):
        if not isinstance(o,I): o=I.rat(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o):
        if not isinstance(o,I): o=I.rat(o)
        return self+-o
    def __mul__(self,o):
        if not isinstance(o,I): o=I.rat(o)
        pp=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(pp)//SCALE,ceil_div(max(pp),SCALE))
    __rmul__=__mul__
    def reciprocal(self):
        if self.lo<=0: raise ValueError("positive reciprocal domain")
        return I((SCALE*SCALE)//self.hi,ceil_div(SCALE*SCALE,self.lo))
    def __truediv__(self,o):
        if not isinstance(o,I): o=I.rat(o)
        return self*o.reciprocal()
    def power(self,n):
        if n<0: raise ValueError("nonnegative integer power")
        v=I.rat(1); u=self
        while n:
            if n&1: v=v*u
            n//=2
            if n: u=u*u
        return v
    def contains(self,x):
        x=F(x)
        return F(self.lo,SCALE)<=x<=F(self.hi,SCALE)
    def display(self):
        return {"lo_numerator":str(self.lo),"hi_numerator":str(self.hi),
                "denominator_power_of_two":BITS,
                "decimal_approx_lo":float(F(self.lo,SCALE)),
                "decimal_approx_hi":float(F(self.hi,SCALE))}

def log_unit_ratio(n,d):
    # 1 <= n/d <= 2. atanh t series with 0 <= t <= 1/3.
    require(d<=n<=2*d,"log reduced domain")
    t=I.rat(n-d,n+d); t2=t*t; power=t; value=I.rat(0)
    terms=32
    for j in range(terms):
        value=value+power*I.rat(2,2*j+1)
        power=power*t2
    tail=F(2,1)*F(1,3)**(2*terms+1)/((2*terms+1)*(1-F(1,9)))
    return I(value.lo,value.hi+ceil_div(tail.numerator*SCALE,tail.denominator))

LOG2=log_unit_ratio(2,1)

def log_integer(n):
    if n<1: raise ValueError("positive integer logarithm")
    k=n.bit_length()-1
    return LOG2*k+log_unit_ratio(n,1<<k)

def exp_neg(x):
    # Fixed reduction keeps all Taylor arguments in [0,1].
    require(0<=x.lo and x.hi<=16*SCALE,"exponential range")
    y=x/16
    term=I.rat(1); total=I.rat(1)
    # For 0<=y<=1, even partial sums are upper bounds and odd lower bounds.
    for j in range(1,41):
        term=term*y/I.rat(j)
        total=total+term if j%2==0 else total-term
    even=total
    term=term*y/I.rat(41)
    odd=total-term
    enclosure=I(odd.lo,even.hi)
    require(enclosure.lo>0,"positive exponential enclosure")
    return enclosure.power(16)

def factor(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,0)+1; n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def mu(n):
    ff=factor(n)
    if any(j>1 for j in ff.values()): return 0
    return -1 if len(ff)%2 else 1

def divisors(n): return [d for d in range(1,n+1) if n%d==0]

def a_product(n,mutation=""):
    if mutation=="drop_prime_powers" and any(j>1 for j in factor(n).values()):
        return F(0)
    z=F(1,n)
    for p in factor(n): z*=1-p
    return z

def a_convolution(n):
    return sum((F(mu(d)*d,n) for d in divisors(n)),F(0))

def beta(n,mutation=""):
    if mutation=="wrong_beta" and n==2: return F(-1,2)
    z=F(1)
    for p,j in factor(n).items(): z*=F(-(p*p-1),p**j*(p+2))
    return z

def local_a(p,j): return F(1) if j==0 else F(-(p-1),p**j)

def local_pair_sum(p,j,k):
    # Independent complete geometric tail after an actual finite prefix.
    count=7
    prefix=sum((local_a(p,l+j)*local_a(p,l+k)/p**l for l in range(count)),F(0))
    first=local_a(p,count+j)*local_a(p,count+k)/p**count
    return prefix+first/(1-F(1,p**3))

def exact_checks(mutation):
    # Interval primitives contain exact rational results, including signs.
    for a in [F(-7,3),F(-1,7),F(0),F(2,9),F(19,4)]:
        for b in [F(-5,9),F(1,11),F(4,3)]:
            aa=I.rat(a.numerator,a.denominator);bb=I.rat(b.numerator,b.denominator)
            require((aa+bb).contains(a+b),"interval addition")
            require((aa*bb).contains(a*b),"interval multiplication")
            if b>0: require((aa/bb).contains(a/b),"interval division")
    for n in range(1,257):
        aa=a_product(n,mutation)
        require(aa==a_convolution(n),"complete coefficient convolution")
        require(abs(aa)<=1,"coefficient one boundedness")
        recovered=sum((F(mu(d),d)*a_product(n//d,mutation) for d in divisors(n)),F(0))
        require(recovered==mu(n),"inverse dilation coefficient identity")
    for p in [2,3,5,7,11,17,29]:
        sq=local_pair_sum(p,0,0)
        require((1-F(1,p))*sq==1-F(3,p*p+p+1),"squared Euler density")
        for j in range(1,7):
            require(local_pair_sum(p,j,0)/sq==beta(p**j,mutation),"ray beta constant")
        # Both positive valuations differ from a fictitious coprime product.
        require(local_pair_sum(p,1,1)/sq!=beta(p,mutation)**2,"shared-prime negative control")
    for r in range(1,17):
        for s in range(1,17):
            if math.gcd(r,s)!=1: continue
            prime_union=set(factor(r))|set(factor(s))
            ratio=F(1)
            for p in prime_union:
                ratio*=local_pair_sum(p,factor(r).get(p,0),factor(s).get(p,0))/local_pair_sum(p,0,0)
            require(ratio==beta(r,mutation)*beta(s,mutation),"coprime primitive ray")

def sign_certificate(mutation):
    N=512
    total=I.rat(1)
    for n in range(2,N+1):
        ll=log_integer(n)
        expo=ll/2+(ll*ll)/8
        wt=exp_neg(expo)
        bb=beta(n,mutation)
        total=total+wt*I.rat(2*bb.numerator,bb.denominator)
    vv=log_integer(N)-2
    require(vv.lo>0,"tail positive Gaussian endpoint")
    exp_half=exp_neg(I.rat(1,2)).reciprocal()
    tail=8*exp_half*exp_neg(vv*vv/8)/vv
    whole=I(total.lo-tail.hi,total.hi+tail.hi)
    require(whole.lo*10>-21*SCALE,"infinite sector strict lower sign bound")
    require(whole.hi*5<-7*SCALE,"infinite sector strict upper sign bound")
    return {"terms_through":N,"finite_partial":total.display(),
            "complete_absolute_tail_upper":tail.display(),
            "infinite_bracket":whole.display(),
            "strict_certified_bounds":["-21/10","-7/5"],
            "rounding":"outward dyadic integer intervals; exact rational tail bounds"}

def adaptive_integral(fun,left,right,tol=1e-13):
    def recurse(a,b,fa,fm,fb,old,eps,depth):
        mid=(a+b)/2
        lm=(a+mid)/2;rm=(mid+b)/2
        fl=fun(lm);fr=fun(rm)
        lhs=(mid-a)*(fa+4*fl+fm)/6
        rhs=(b-mid)*(fm+4*fr+fb)/6
        delta=lhs+rhs-old
        if abs(delta)<=15*eps:
            return lhs+rhs+delta/15
        if depth<=0: raise ValueError("numerical quadrature depth")
        return (recurse(a,mid,fa,fl,fm,lhs,eps/2,depth-1)
                +recurse(mid,b,fm,fr,fb,rhs,eps/2,depth-1))
    fa=fun(left);fb=fun(right);mid=(left+right)/2;fm=fun(mid)
    return recurse(left,right,fa,fm,fb,(right-left)*(fa+4*fm+fb)/6,tol,30)

def gaussian_checks(mutation):
    residual=0.0;cases=0
    def kernel(n,m,T,c):
        v=c-0.5
        den=4 if mutation=="wrong_gaussian" else 8
        return (math.exp(2*v*v)/(2*math.sqrt(2*math.pi))*math.exp(-math.log(n/m)**2/den)
                /math.sqrt(n*m)*math.erfc(((math.log(n)+math.log(m))/2+2*v-math.log(T))/math.sqrt(2))/2)
    for n,m,T,c in [(1,1,2,0),(2,7,5,0.5),(5,12,20,1),(3,9,1.5,-1)]:
        v=c-0.5
        def term(x,k):
            u=math.log(k)-x
            return math.exp(-v*u-u*u/4)/(2*math.sqrt(math.pi*k))
        direct=adaptive_integral(lambda x:term(x,n)*term(x,m),-40,math.log(T))
        err=abs(direct-kernel(n,m,T,c));residual=max(residual,err)
        require(err<1e-10,"finite Gaussian kernel quadrature")
        cases+=1
    # Whole finite eight-coefficient quadratic form, with all ordered pairs.
    vals=[F(2,3),F(-1,2),F(5,7),F(0),F(-3,4),F(1),F(-2,5),F(7,11)]
    c=2/3;T=7;v=c-0.5
    def source(x):
        out=0.0
        for n,aa in enumerate(vals,1):
            u=math.log(n)-x
            out+=float(aa)/math.sqrt(n)*math.exp(-v*u-u*u/4)/(2*math.sqrt(math.pi))
        return out
    direct=adaptive_integral(lambda x:source(x)**2,-40,math.log(T))
    gram=sum(float(aa)*float(bb)*kernel(n,m,T,c)
             for n,aa in enumerate(vals,1) for m,bb in enumerate(vals,1))
    err=abs(direct-gram);residual=max(residual,err)
    require(err<1e-10,"complete finite quadratic form")
    cases+=1
    # Full continuum norm and cross term, by a separate numerical integration.
    for h,c in [(1,0),(1,0.5),(1.5,2/3)]:
        b=h-0.5;v=c-0.5
        exact=math.exp(2*v*v+2*b*b)*math.erfc(math.sqrt(2)*b)/(2*b)
        def jj(x):
            return (0.5*math.exp((0.5-h)*x+(1-h-c)**2)
                    *math.erfc(-(x+2*(1-h-c))/2))
        norm=adaptive_integral(lambda x:jj(x)**2,-40,40)
        cross=adaptive_integral(lambda x:jj(x)*math.exp(v*x-x*x/4)/(2*math.sqrt(math.pi)),-40,40)
        err=max(abs(norm-exact),abs(cross-b*exact));residual=max(residual,err)
        require(err<1e-10,"complete continuum finite quadrature")
        cases+=1
    return {"cases":cases,"max_absolute_difference":residual,
            "arithmetic":"ordinary binary64 adaptive Simpson; not a directed certificate",
            "integration_windows":"[-40,log T] for finite kernels; [-40,40] for continuum",
            "scope":"finite Gaussian integrations only; no zeta or asymptotic test"}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--mutation",default="",choices=["","wrong_beta","drop_prime_powers","wrong_gaussian"])
    args=parser.parse_args()
    exact_checks(args.mutation)
    cert=sign_certificate(args.mutation)
    gauss=gaussian_checks(args.mutation)
    report={"status":"PASS","explicit_predicates":predicates,
            "sign_certificate":cert,"finite_numerical_crosscheck":gauss,
            "not_checked":["Tao's analytic theorem","infinite zeta contour arguments",
                           "uniform growing additive offsets","complete critical energy upper bound"]}
    print(json.dumps(report,sort_keys=True,indent=2))

if __name__=="__main__": main()
