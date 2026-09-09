#!/usr/bin/env python3
"""Bounded algebra and complete finite norm checks; no RH proof checker."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
from fractions import Fraction as F

ROOT = Path(__file__).resolve().parent
FILES = {'PROOF.md','README.md','SOURCES.json','verify.py','result.json','SHA256SUMS'}
BITS = 112
SCALE = 1 << BITS


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def obj(pairs):
    d = {}
    for k, v in pairs:
        require(k not in d, 'duplicate JSON key')
        d[k] = v
    return d


def load(path):
    return json.loads(Path(path).read_text(), object_pairs_hook=obj)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))


class IV:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        require(self.lo <= self.hi, 'inverted interval')
    def __add__(self, other):
        other = other if isinstance(other, IV) else IV(other)
        return IV(self.lo+other.lo, self.hi+other.hi)
    __radd__ = __add__
    def __neg__(self):
        return IV(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + - (other if isinstance(other, IV) else IV(other))
    def __rsub__(self, other):
        return IV(other) + -self
    def __mul__(self, other):
        other = other if isinstance(other, IV) else IV(other)
        p = [a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return IV(min(p), max(p))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = other if isinstance(other, IV) else IV(other)
        require(not other.lo <= 0 <= other.hi, 'division interval contains zero')
        return self * IV(1/other.hi,1/other.lo)
    def __rtruediv__(self, other):
        return IV(other) / self
    def square(self):
        hi = max(self.lo*self.lo,self.hi*self.hi)
        lo = F(0) if self.lo <= 0 <= self.hi else min(self.lo*self.lo,self.hi*self.hi)
        return IV(lo,hi)
    def contains(self,x):
        return self.lo <= x <= self.hi
    def coarse(self, digits=10):
        d = 10**digits
        low = (self.lo.numerator*d)//self.lo.denominator
        high = -((-self.hi.numerator*d)//self.hi.denominator)
        def text(n):
            s = '-' if n < 0 else ''
            n = abs(n)
            return f'{s}{n//d}.{n%d:0{digits}d}'
        return [text(low),text(high)]


def log_iv(x, terms=180):
    x=F(x)
    require(x>=1, 'log test primitive is restricted to x>=1')
    q=(x-1)/(x+1)
    s=sum((2*q**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    err=2*q**(2*terms+1)/(F(2*terms+1)*(1-q*q))
    return IV(s,s+err)


def atan_iv(q, terms=50):
    q=F(q)
    require(0<q<1, 'atan range')
    s=sum(((-1)**k*q**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    next_term=(-1)**terms*q**(2*terms+1)/F(2*terms+1)
    return IV(min(s,s+next_term),max(s,s+next_term))


def period_weight(Q,r,K):
    require(type(Q) is int and type(r) is int and type(K) is int,'strict integer')
    require(Q>=1 and 1<=r<=Q and K>=1,'period range')
    low=0
    for k in range(K):
        n=r+k*Q
        low += SCALE//(n*(n+1))
    # Every finite summand is rounded outward separately; all of the tail remains.
    return IV(F(low,SCALE),F(low+K,SCALE)+F(1,Q*(r+Q*(K-1))))


def linadd(a,b): return (a[0]+b[0],a[1]+b[1])
def linscale(c,a): return (c*a[0],c*a[1])


def mu(n):
    value, d = 1, 2
    while d*d<=n:
        if n%d==0:
            n//=d
            if n%d==0:
                return 0
            value=-value
        d+=1
    return -value if n>1 else value


def solve(A,b):
    n=len(b)
    rows=[list(map(F,A[i]))+[F(b[i])] for i in range(n)]
    for k in range(n):
        j=next((j for j in range(k,n) if rows[j][k]),None)
        require(j is not None,'singular rational matrix')
        rows[k],rows[j]=rows[j],rows[k]
        pivot=rows[k][k]
        rows[k]=[v/pivot for v in rows[k]]
        for j in range(n):
            if j!=k:
                factor=rows[j][k]
                rows[j]=[rows[j][r]-factor*rows[k][r] for r in range(n+1)]
    return [rows[i][-1] for i in range(n)]


def reconstruct():
    groups=[]
    l=log_iv(2); l3=log_iv(3)
    pi=16*atan_iv(F(1,5))-4*atan_iv(F(1,239))
    require(F(69,100)<l.lo<l.hi<F(7,10),'log enclosure')
    require(F(314,100)<pi.lo<pi.hi<F(315,100),'pi enclosure')
    # This also catches dependency-related interval-square mistakes.
    require(IV(-1,2).square().lo==0,'interval square')
    groups.append('outward elementary primitives')

    # Independent finite Mobius/divisor checks, including the delayed endpoint.
    horizons=0
    for Y in range(2,21):
        p={n:F(mu(n)) for n in range(1,Y)}
        p[Y]=-Y*sum((v/F(n) for n,v in p.items()),F(0))
        require(sum((v/F(n) for n,v in p.items()),F(0))==0,'balance')
        for j in range(1,Y):
            for x in (F(j),F(j)+F(1,4),F(j)+F(3,4)):
                val=sum(v*(x//n) for n,v in p.items())
                require(val==1,'literal initial horizon')
                horizons+=1
    groups.append('finite divisor identity and exact delayed horizon')

    # All coefficients below are affine rational functions of t. Algebra is exact.
    C={1:(F(1),F(0)),2:(F(-1),F(0)),3:(F(-1),F(0)),
       4:(F(-2),F(4)),8:(F(8,3),F(-8))}
    balance=(F(0),F(0))
    for n,c in C.items(): balance=linadd(balance,linscale(F(1,n),c))
    require(balance==(0,0),'symbolic p4 balance')
    # -sum c_n log(n)/n reduces to t*log2+log2/2+log3/3=1.
    l2coef=(F(0),F(0)); l3coef=(F(0),F(0))
    for n,c in C.items():
        n0=n; e2=e3=0
        while n0%2==0: n0//=2; e2+=1
        while n0%3==0: n0//=3; e3+=1
        require(n0==1,'small support prime factor')
        l2coef=linadd(l2coef,linscale(F(-e2,n),c))
        l3coef=linadd(l3coef,linscale(F(-e3,n),c))
    require(l2coef==(F(1,2),F(1)) and l3coef==(F(1,3),0),'symbolic jet')
    def cell(r):
        v=(F(1),F(0))
        for n,c in C.items(): v=linadd(v,linscale(-(r//n),c))
        return v
    require(all(cell(r)==(0,0) for r in (1,2,3)),'p4 prefix')
    require(all(cell(r+24)==cell(r) for r in range(1,49)),'period identity')
    require(cell(24)==(1,0),'period final cell')
    groups.append('exact p4 prefix, two jets, and full period')

    t=(1-l/F(2)-l3/F(3))/l
    E4=IV(0)
    K=2048
    for r in range(1,25):
        c,d=cell(r)
        E4 += period_weight(24,r,K)*(c+d*t).square()
    require(F(57,1000)<E4.lo and E4.hi<F(59,1000),'complete p4 norm interval')
    groups.append('p4 positive energy: all 24 cells plus all infinite tails')

    h=1/l
    closed=(4-pi)/2*(h-1)
    closed_cells=(pi/8-l/4)*(3-2*h).square()+(3*l/4-pi/8)*(2-2*h).square()+(1-pi/8-3*l/4)
    require((closed-closed_cells).contains(0),'p2 closed formula enclosure')
    E2=period_weight(4,2,K)*(3-2*h).square()+period_weight(4,3,K)*(2-2*h).square()+period_weight(4,4,K)
    require(E2.lo<closed.lo<=closed.hi<E2.hi,'p2 independent tail/closed agreement')
    require(F(189,1000)<closed.lo and closed.hi<F(191,1000),'p2 norm interval')
    groups.append('p2 periodic series independently encloses the closed formula')

    # General delayed-jet algebra. Rational nodes are synthetic, NOT zeta zeros.
    jet_cases=0
    for a in (F(1,8),F(1,4),F(1,3)):
        rho=a+F(1,2)
        for L in (F(0),F(1,2),F(2)):
            for q in range(1,5):
                b=[sum((F(math.comb(k,j))*L**(k-j)*(-1)**j*math.factorial(j)/rho**(j+1)
                        for j in range(k+1)),F(0)) for k in range(q)]
                H=[[F((-1)**(k+j)*math.factorial(k+j))/(2*a)**(k+j+1)
                    for j in range(q)] for k in range(q)]
                x=solve(H,b)
                gram=sum((b[i]*x[i] for i in range(q)),F(0))
                P=[sum((F(math.comb(j,k))*(2*a)**k*b[k]/math.factorial(k)
                        for k in range(j+1)),F(0)) for j in range(q)]
                lag=2*a*sum((v*v for v in P),F(0))
                require(gram==lag and gram>0,'sharp jet norm identity')
                if q==1: require(gram==2*a/rho**2,'single point normalization')
                jet_cases+=1
    groups.append('independent Gram and Laguerre costs for synthetic jets')

    # Two-node kernel orientation and exact first-order normal equations.
    nodes=[F(1,5),F(1,3)]
    H=[[1/(x+y) for y in nodes] for x in nodes]
    y=[1/(x+F(1,2)) for x in nodes]
    c=solve(H,y)
    require(all(sum(H[i][j]*c[j] for j in range(2))==y[i] for i in range(2)),'Gram constraints')
    require(sum(y[i]*c[i] for i in range(2))>=max(y[i]**2/H[i][i] for i in range(2)),'extra constraints')
    groups.append('simultaneous positive Gram constraints')

    # Reconstruct the displayed exact norm expression symbolically by rational evaluations.
    # These fixtures corroborate algebra; the paper proves the identity for every l.
    for h0 in (F(7,5),F(3,2),F(5,3),F(2)):
        l0=1/h0
        for pi0 in (F(3),F(22,7)):
            expr=(pi0/8-l0/4)*(3-2*h0)**2+(3*l0/4-pi0/8)*(2-2*h0)**2+1-pi0/8-3*l0/4
            require(expr==(4-pi0)*(h0-1)/2,'closed norm algebra')
    groups.append('finite exact closed-form algebra controls')

    return {
      'status':'COMPONENT_CHECKS_ONLY',
      'rh_proved':False,'signed_count_bound_proved':False,'subpower_norm_proved':False,
      'parent':'d1a45dba9c028f52c0f1cdb2c1bc0b2c0d2652c4',
      'groups':groups,'group_count':len(groups),
      'literal_horizon_points':horizons,'synthetic_jet_cases':jet_cases,
      'period_weight_terms_per_cell':K,'outward_binary_bits':BITS,
      'p2_exact_energy_enclosure':closed.coarse(),
      'p2_independent_series_enclosure':E2.coarse(),
      'p4_complete_energy_enclosure':E4.coarse(),
      'scope':'Two finite norm certificates and bounded algebra; no zeta-zero or unbounded estimate computation.'}


def check_manifest():
    require(not any(p.is_symlink() for p in ROOT.iterdir()),'symlink')
    actual={p.name for p in ROOT.iterdir()}
    require(actual==FILES,'unexpected or missing package path')
    rows=(ROOT/'SHA256SUMS').read_text().splitlines()
    seen=set()
    for row in rows:
        digest,name=row.split('  ',1)
        require(name in FILES-{'SHA256SUMS'} and name not in seen,'manifest inventory')
        seen.add(name)
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,'changed '+name)
    require(seen==FILES-{'SHA256SUMS'},'incomplete manifest')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',type=Path)
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    require(bool(args.write) != bool(args.check),'choose --write or --check')
    result=reconstruct()
    if args.write:
        args.write.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:
        check_manifest()
        stored=load(args.check)
        require(canonical(stored)==canonical(result),'result mismatch')
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
