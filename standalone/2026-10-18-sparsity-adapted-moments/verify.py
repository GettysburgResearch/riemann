"""Exact finite regressions. This is NOT a verifier for the analytic inputs."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Q
import json
from math import gcd

MUTATION = ''
COUNTS: Counter[str] = Counter()


def need(ok: bool, gate: str) -> None:
    if not ok:
        raise AssertionError(gate)
    COUNTS[gate] += 1


def lines(n: int) -> list[tuple[Q, Q]]:
    return [(Q(1), Q(0)), (Q(0), Q(1)),
            (1-Q(1,n), Q(2,n)), (Q(2,n), 1-Q(1,n))]


def kn(n: int, v: Q) -> Q:
    return max(c+s*v for c,s in lines(n))


def crossing(n: int, nu: Q) -> Q:
    if nu >= Q(1,2):
        return 1-nu
    if nu >= Q(1,n):
        return (n-1-n*nu)/(n-2)
    return 2-n*nu


def phi_closed(n: int, nu: Q, ell: Q, sigma: Q) -> Q:
    v = crossing(n, nu)
    if MUTATION == 'wrong_crossing':
        v += Q(1,17)
    if ell <= v:
        return nu+2*(1-sigma)*ell
    return max(nu+2*(1-sigma)*v, kn(n,ell)+(1-2*sigma)*ell)


def phi_by_breakpoints(n: int, nu: Q, ell: Q, sigma: Q) -> Q:
    # Independent finite maximization of the ORIGINAL piecewise-affine formula.
    ls = lines(n)+[(nu,Q(1))]
    vertices = {Q(0),ell}
    for c,s in ls:
        for d,t in ls:
            if s != t:
                v = (d-c)/(s-t)
                if 0 <= v <= ell:
                    vertices.add(v)
    choice = max if MUTATION == 'min_to_max' else min
    return max((1-2*sigma)*v+choice(nu+v,kn(n,v)) for v in vertices)


# Rational polynomial arithmetic used to authenticate identities for ALL n.
def trim(p):
    p = list(map(Q,p))
    while len(p)>1 and not p[-1]: p.pop()
    return tuple(p)


def padd(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])


def pmul(a,b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j] += x*y
    return trim(c)


class RF:
    def __init__(self, num, den=(1,)):
        self.num = trim(num if isinstance(num,(tuple,list)) else (num,))
        self.den = trim(den)
        if self.den == (Q(0),): raise ValueError('zero denominator polynomial')
    @staticmethod
    def cast(x): return x if isinstance(x,RF) else RF(x)
    def __add__(self,x):
        x=self.cast(x)
        return RF(padd(pmul(self.num,x.den),pmul(x.num,self.den)),pmul(self.den,x.den))
    __radd__=__add__
    def __neg__(self): return RF(tuple(-x for x in self.num),self.den)
    def __sub__(self,x): return self+-self.cast(x)
    def __rsub__(self,x): return self.cast(x)+-self
    def __mul__(self,x):
        x=self.cast(x)
        return RF(pmul(self.num,x.num),pmul(self.den,x.den))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.cast(x)
        return RF(pmul(self.num,x.den),pmul(self.den,x.num))
    def __rtruediv__(self,x): return self.cast(x)/self
    def __eq__(self,x):
        x=self.cast(x)
        return pmul(self.num,x.den)==pmul(x.num,self.den)


def params(n):
    a=(4*n-14)/(5*n-16)
    b=(6*n-20)/(5*n-16)
    g=3*(n*n-2*n-4)/(n*(5*n-16))
    lam=Q(1,2)+1/(2*n)
    c=Q(3,4)-1/(2*n)
    d=Q(1,4)+1/(2*n)
    first=(c+(lam-Q(3,4))*b)/(1-d)
    second=(c+(lam-Q(3,4))*b+a/(2*n))*Q(4,3)
    return a,b,g,lam,c,d,first,second


def rational_identities():
    n=RF((0,1)); a,b,g,lam,c,d,g0,g1=params(n)
    identities=[
      (g0,1-(n-2)*b/(3*n-2)),
      (g1,g),
      (a-g,(n-6)*(n-2)/(n*(5*n-16))),
      (g-g0,2*(n-6)*(n-2)/(n*(3*n-2)*(5*n-16))),
      (g-b/2,4*(n-3)/(n*(5*n-16))),
      (g-(1-a/2),3*(n-4)/(n*(5*n-16))),
      (Q(2)/n+(Q(1,2)-1/n)*b,g),
      (1-1/n+(Q(-1,2)+2/n)*a,g),
    ]
    for x,y in identities: need(x==y,'polynomial_density_identity')


def factor(x: int) -> dict[int,int]:
    out={}; p=2
    while p*p<=x:
        while x%p==0: out[p]=out.get(p,0)+1; x//=p
        p+=1
    if x>1: out[x]=out.get(x,0)+1
    return out


def mobius(x: int) -> int:
    fs=factor(x)
    return 0 if any(e>1 for e in fs.values()) else (-1)**len(fs)


def split_power(x: int,n: int) -> tuple[int,int]:
    c=d=1
    for p,e in factor(x).items():
        c*=p**(e%n); d*=p**(e//n)
    return c,d


def root_power(alpha: int|None,e: int,n: int) -> int|None:
    if e==0: return 0
    return None if alpha is None else alpha*e%n


def decomposed_character(alpha: int|None,e: int,n: int) -> int|None:
    r,j=e%n,e//n
    if MUTATION=='false_coprimality' and r and j: return None
    if MUTATION=='erased_mask' and j and alpha is None: return root_power(0,r,n)
    if j and alpha is None: return None
    return root_power(alpha,r,n)


def prefix_blocks(end: int) -> list[tuple[int,int]]:
    out=[]; start=0
    while start<end:
        size=1 << ((end-start).bit_length()-1)
        out.append((start,start+size)); start+=size
    if MUTATION=='duplicated_interval' and out: out.append(out[-1])
    return out


def main():
    global MUTATION
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mutation',default='')
    MUTATION=parser.parse_args().mutation
    allowed={'','wrong_crossing','min_to_max','dual_sign','erased_mask',
             'false_coprimality','full_row_mollifier','wrong_holder',
             'duplicated_interval'}
    if MUTATION not in allowed: raise ValueError('unknown mutation')
    rational_identities()
    for n in range(3,19):
        nus=sorted({Q(j,12) for j in range(13)}|{Q(1,n),Q(1,2)})
        for nu in nus:
            for r in range(1,9):
                for sigma in (Q(1,2),Q(7,12),Q(2,3),Q(3,4),Q(9,10)):
                    need(phi_closed(n,nu,Q(r,2),sigma)==
                         phi_by_breakpoints(n,nu,Q(r,2),sigma),'selected_envelope')
    for nu in (Q(j,120) for j in range(121)):
        expected=(nu+Q(1,2) if nu<=Q(1,6) else
                  Q(5,8)+nu/4 if nu<=Q(1,2) else Q(1,2)+nu/2)
        need(phi_closed(6,nu,Q(1),Q(3,4))==expected,'sextic_example')
    need(Q(1,2)*Q(3,4)+Q(3,4)/4==Q(9,16),'same_order_first_mean')
    need(Q(1,2)*Q(7,8)+Q(1,8)==Q(9,16),'eighth_moment_overlap')
    for r in range(1,9):
        for sigma in (Q(1,2),Q(7,12),Q(3,4),Q(9,10)):
            for qexp in (Q(j,8) for j in range(9)):
                for j in range(9):
                    v=qexp*r*Q(j,16)
                    outer=qexp*r*(1-2*sigma)
                    if MUTATION=='dual_sign': outer=-outer
                    need(outer+(2*sigma-1)*v <= (1-2*sigma)*v,'actual_dual_conductor')
    table=[]
    for ni in range(6,129):
        n=Q(ni); a,b,g,lam,c,d,g0,g1=params(n)
        need(Q(1,2)<a<1<b and Q(1,2)<lam<Q(3,4) and 0<g<1,'density_parameters')
        if MUTATION=='wrong_holder': d=Q(1,4)
        need(d==Q(1,4)+1/(2*n),'selected_holder_power')
        costs=[g0,g1,b/2,1-a/2,2/n+(Q(1,2)-1/n)*b,
               1-1/n+(Q(-1,2)+2/n)*a]
        if MUTATION=='full_row_mollifier':
            costs[0]=(Q(3,4)+(lam-Q(3,4))*b)*Q(4,3)
        need(max(costs)<=g,'complete_detector_budget')
        if ni in (6,8,10,12,16,32,64,128):
            table.append({'n':ni,'A_exponent':str(a),'B_exponent':str(b),
                          'density_exponent':str(g),'costs':[str(x) for x in costs]})
        for aa in (Q(1,2),Q(2,3),Q(5,7),Q(4,5),Q(1)):
            need((1-aa)+(2*aa-1)/n>=0 and (1-3/n)*(1-aa)>=0,'mollifier_dominance')
    for n in (3,4,6,8,10):
        for alpha in [None,*range(n)]:
            for e in range(4*n+1):
                need(root_power(alpha,e,n)==decomposed_character(alpha,e,n),'literal_power_mask')
        for x in range(1,513):
            c,d=split_power(x,n)
            # Independent enumeration of every integer n-th-power divisor.
            ds=[j for j in range(1,x+1) if j**n<=x and x%(j**n)==0]
            oracle=max(ds)
            need(d==oracle and c*d**n==x and all(e<n for e in factor(c).values()),
                 'complete_rational_power_decomposition')
    for cap in (1,3,8,17,32,64):
        for x in range(1,129):
            ds=[d for d in range(1,min(cap,x)+1) if x%d==0]
            coeff=sum(mobius(d) for d in ds)
            if x<=cap: need(coeff==int(x==1),'detector_initial_annihilation')
            # Removing primes 2 and 3 is a zero mask in BOTH factors.
            conv=sum(mobius(d)*int(gcd(d,6)==1)*int(gcd(x//d,6)==1) for d in ds)
            need(conv==coeff*int(gcd(x,6)==1),'detector_common_mask')
    for size in range(1,66):
        weights=[1+(j%7)**2 for j in range(size)]
        for end in range(size+1):
            blocks=prefix_blocks(end)
            covered=[j for a,b in blocks for j in range(a,b)]
            need(covered==list(range(end)),'prefix_disjointness')
            for d in (1,2,3):
                expected=sum(weights[j] for j in range(end) if (j+1)%(d**3)==0)
                actual=sum(sum(weights[j] for j in range(a,b) if (j+1)%(d**3)==0)
                           for a,b in blocks)
                need(actual==expected,'dilated_prefix_square_mass')
    need(Q(8,11)-Q(5,7)==Q(1,77),'comparison_DF')
    need(Q(395,552)-Q(5,7)==Q(5,3864),'comparison_shifted')
    need(Q(43,60)-Q(5,7)==Q(1,420),'comparison_central')
    report={'status':'PASS_FINITE_ALGEBRA_ONLY','analytic_inputs_verified':False,
            'independent_mathematical_review':False,'checks':dict(sorted(COUNTS.items())),
            'total_predicates':sum(COUNTS.values()),'density_table':table,
            'scope':'Exact exponents, formal polynomial identities, abstract roots/nonunit masks, rational-integer fixtures. No L-values, zeros or full number-field census.'}
    print(json.dumps(report,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
