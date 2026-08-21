#!/usr/bin/env python3
from fractions import Fraction
from dataclasses import dataclass
from math import isqrt
import json, hashlib

@dataclass(frozen=True)
class Q2:
    a: Fraction
    b: Fraction = Fraction(0)
    def __add__(self, o):
        o = coerce(o); return Q2(self.a+o.a, self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-coerce(o))
    def __rsub__(self,o): return coerce(o)-self
    def __mul__(self,o):
        o=coerce(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=coerce(o); den=o.a*o.a-2*o.b*o.b
        if den==0: raise ZeroDivisionError
        return Q2((self.a*o.a-2*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def is_zero(self): return self.a==0 and self.b==0
    def pair(self): return [str(self.a),str(self.b)]

def coerce(x):
    if isinstance(x,Q2): return x
    return Q2(Fraction(x))

SQ2=Q2(Fraction(0),Fraction(1))

def pmul(p,q):
    out=[Q2(Fraction(0)) for _ in range(len(p)+len(q)-1)]
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]=out[i+j]+a*b
    return out

def ppow(p,n):
    out=[Q2(Fraction(1))]
    for _ in range(n): out=pmul(out,p)
    return out

def mobius(n):
    x=n; p=2; count=0
    while p*p<=x:
        if x%p==0:
            x//=p; count+=1
            if x%p==0: return 0
            while x%p==0: x//=p
        p+=1
    if x>1: count+=1
    return -1 if count%2 else 1

def b_coeff(n,Rpoly):
    out=Q2(Fraction(0)); pow2=1
    for c in Rpoly:
        if n%pow2==0:
            out += c*mobius(n//pow2)
        pow2*=2
    return out

def eps(n): return 1 if n%2 else -1

def dirichlet_conv_eps_b(n,Rpoly):
    s=Q2(Fraction(0))
    for d in range(1,n+1):
        if n%d==0: s += eps(d)*b_coeff(n//d,Rpoly)
    return s

def euler_transform(seq,R):
    a=[Fraction(x) for x in seq]
    S=sum((1 if i%2==0 else -1)*x for i,x in enumerate(a))
    vals=a+[Fraction(0)]*R
    rhs=Fraction(0)
    cur=vals
    for j in range(R):
        rhs += cur[0]/(2**(j+1))
        cur=[cur[i]-cur[i+1] for i in range(len(cur)-1)]
    rem=sum((1 if i%2==0 else -1)*x for i,x in enumerate(cur))/(2**R)
    return S,rhs+rem

def eta_lower_24():
    D=10**8
    s=Fraction(0)
    for n in range(1,25):
        root_floor=isqrt(n*D*D)
        if n%2==1:
            root_ceil=root_floor if root_floor*root_floor==n*D*D else root_floor+1
            term=Fraction(D,root_ceil)
        else:
            term=Fraction(D,root_floor)
        s += term if n%2==1 else -term
    return s

def main():
    Rpoly=pmul([Q2(1),Q2(-2)],ppow([Q2(1),-SQ2],2))
    expected=[Q2(1),-(Q2(2)+2*SQ2),Q2(2)+4*SQ2,Q2(-4)]
    assert Rpoly==expected

    Dpoly=pmul([Q2(1),Q2(-2)],Rpoly)
    for n in range(1,257):
        got=dirichlet_conv_eps_b(n,Rpoly)
        j=(n.bit_length()-1) if n&(n-1)==0 else None
        want=Dpoly[j] if j is not None and j<len(Dpoly) else Q2(0)
        assert got==want,(n,got,want)

    inv=[Q2(1)]
    local=pmul([Q2(1),Q2(-1)],Rpoly)
    for n in range(1,33):
        s=Q2(0)
        for j in range(1,min(n,len(local)-1)+1): s += local[j]*inv[n-j]
        inv.append(-s/local[0])
        assert inv[-1].a>=0 and inv[-1].b>=0

    checks=0
    for N in range(1,25):
        seq=[Fraction((7*i*i+3*i+5)%19-9, i+3) for i in range(1,N+1)]
        for R in range(1,min(8,N+3)):
            lhs,rhs=euler_transform(seq,R)
            assert lhs==rhs
            checks+=1

    low=eta_lower_24()
    assert low>Fraction(1,2),low
    kappa_upper=2*(1-low)
    assert kappa_upper<1

    result={
      "verdict":"EXACT_BOUNDARY_BSPLINE_ALGEBRA_VERIFIED",
      "R_polynomial":[x.pair() for x in Rpoly],
      "D_polynomial":[x.pair() for x in Dpoly],
      "dirichlet_convolution_checks":256,
      "positive_inverse_2adic_coefficients":len(inv),
      "finite_euler_transform_checks":checks,
      "eta_half_rational_lower":str(low),
      "paired_mass_upper":str(kappa_upper),
      "scope":"Finite exact algebra only. This does not prove the source-specific reflected remainder contraction, a cofinal energy bound, or RH."
    }
    canonical=json.dumps(result,sort_keys=True,separators=(",",":"))
    result["proof_object_sha256"]=hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__': main()
