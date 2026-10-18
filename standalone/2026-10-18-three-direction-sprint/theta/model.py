"""Complete connected-hub moments with generic exact polynomial scalars.

Adapted from #994 connected_blocks.py/tree_core.py, pinned in INHERITED.json.
This version makes the degree, counts and active chart explicit and handles
the derivative of x**1 at x=0 without evaluating Decimal(0)**0.
"""
from math import comb

class Dual:
    __slots__=('v','d')
    def __init__(self,v,d):self.v=v;self.d=tuple(d)
    def __add__(self,o):
        if isinstance(o,Dual):return Dual(self.v+o.v,[a+b for a,b in zip(self.d,o.d)])
        return Dual(self.v+o,self.d)
    __radd__=__add__
    def __neg__(self):return Dual(-self.v,[-a for a in self.d])
    def __sub__(self,o):return self+-o
    def __rsub__(self,o):return -self+o
    def __mul__(self,o):
        if isinstance(o,Dual):return Dual(self.v*o.v,[a*o.v+self.v*b for a,b in zip(self.d,o.d)])
        return Dual(self.v*o,[a*o for a in self.d])
    __rmul__=__mul__
    def __truediv__(self,o):return Dual(self.v/o,[a/o for a in self.d])
    def __pow__(self,n):
        if n==0:return Dual(self.v*0+1,[a*0 for a in self.d])
        if n==1:return self
        vn=self.v**(n-1);return Dual(vn*self.v,[n*vn*a for a in self.d])

def cumulants(mu):
    zero=mu[0]*0;out=[zero for _ in mu]
    for n in range(1,len(mu)):
        out[n]=mu[n]-sum((comb(n-1,j-1)*out[j]*mu[n-j] for j in range(1,n)),zero)
    return out

def moments(kap):
    zero=kap[0]*0;out=[zero+1]
    for n in range(1,len(kap)):
        out.append(sum((comb(n-1,j-1)*kap[j]*out[n-j] for j in range(1,n+1)),zero))
    return out

def unit_cumulants(degree):return cumulants([int(n%2==0) for n in range(degree+1)])

def evaluate(z,counts,eta,degree):
    if len(z)!=3*len(counts):raise ValueError('complete parameter list required')
    if degree<2 or degree%2:raise ValueError('positive even degree required')
    zero=z[0]*0;one=zero+1;eta=one*eta;total=[zero]*(degree+1)
    for i,count in enumerate(counts):
        A,B,p=z[3*i:3*i+3]
        mu=[one]+[(A**n if i==0 else p*A**n+(one-p)*B**n)*(one if n%2==0 else eta) for n in range(1,degree+1)]
        kap=cumulants(mu);total=[x+count*y for x,y in zip(total,kap)]
    conditional=moments(total)
    raw=[x if n%2==0 else zero for n,x in enumerate(conditional)]
    kap=cumulants(raw);unit=unit_cumulants(degree)
    return [kap[2*r]/unit[2*r] for r in range(1,degree//2+1)],raw

def jet(z,counts,eta,degree,active):
    zero=z[0]*0;one=zero+1
    zz=[Dual(x,[one if j==k else zero for k in active]) for j,x in enumerate(z)]
    val,raw=evaluate(zz,counts,eta,degree)
    return [x.v for x in val],[list(x.d) for x in val],[x.v for x in raw]

def convolve_raw(a,b):
    degree=min(len(a),len(b))-1;zero=a[0]*0
    return [sum((comb(n,j)*a[j]*b[n-j] for j in range(n+1)),zero) for n in range(degree+1)]

def direct_assembly(z,counts,eta,degree):
    """Independent raw-series multiplication, no cumulant recurrence."""
    zero=z[0]*0;one=zero+1;out=[one]+[zero]*degree
    for i,count in enumerate(counts):
        A,B,p=z[3*i:3*i+3]
        base=[one]+[(A**n if i==0 else p*A**n+(one-p)*B**n)*(one if n%2==0 else eta) for n in range(1,degree+1)]
        power=[one]+[zero]*degree;k=count
        while k:
            if k%2:power=convolve_raw(power,base)
            k//=2
            if k:base=convolve_raw(base,base)
        out=convolve_raw(out,power)
    return [x if n%2==0 else zero for n,x in enumerate(out)]
