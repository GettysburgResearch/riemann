#!/usr/bin/env python3
"""Exact finite algebra checks, NOT certification of the analytic input.

Standard library only. No assert statements: negative controls also run under -O.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json

MUTATIONS = ('wrong-conjugate','erase-mask','force-coprime','missing-low-end',
             'old-length','omit-dual-high','principal-as-dual','false-all-orders')

class Checks:
    def __init__(self): self.count=Counter()
    def need(self, group, label, condition):
        if not condition: raise ValueError(f'{group}: {label}')
        self.count[group]+=1


def k(n,v):
    v=F(v)
    return max(F(1),v,1-F(1,n)+2*v/n,F(2,n)+(1-F(1,n))*v)


def budget(n,d,r,a,x,p,mutation=None):
    d,a,x=map(F,(d,a,x))
    m=max(F(1),k(n,p*r*a)-d*p*r*a)
    b=k(n,r*(1-x))-d*r*x
    c=k(n,2*r*(1-x))-2*d*r*x
    lo=k(n,r*a)-d*r*a
    hi=k(n,r*(a+x))-d*r*(a+x)
    if mutation=='missing-low-end':lo=hi
    if mutation=='omit-dual-high':c=F(0)
    mixed=(m+(p-2)*b+c)/p
    g=max(lo,hi,mixed,F(0),r*a*(1-d))
    return dict(m=m,b=b,c=c,lo=lo,hi=hi,mixed=mixed,G=g)


def zadd(u,v):return u[0]+v[0],u[1]+v[1]
def zmul(u,v):
    # omega=e^(i*pi/3), omega^2=omega-1.
    a,b=u;c,d=v
    return a*c-b*d,a*d+b*c+b*d

def zconj(u):return u[0]+u[1],-u[1]
def znorm(u):return u[0]*u[0]+u[0]*u[1]+u[1]*u[1]
def zpow(u,j):
    out=(1,0)
    while j:
        if j&1:out=zmul(out,u)
        u=zmul(u,u);j//=2
    return out


def mu(n):
    ans=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;ans=-ans
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    return -ans if n>1 else ans


def dconv(a,b):
    out={}
    for i,v in a.items():
        for j,w in b.items():out[i*j]=out.get(i*j,F(0))+v*w
    return {i:v for i,v in out.items() if v}


def flat(n,X):
    # Finite identity fixture only; this piecewise-linear profile is NOT the
    # smooth analytic profile in the theorem.
    if n<=X:return F(1)
    if n>=2*X:return F(0)
    return F(2)-F(n,X)


def run(mutation=None):
    c=Checks();tables=[]
    cases=[(1,F(3,5),F(3,5),3,F(11,15)),
           (2,F(1,5),F(1,2),5,F(4,5)),
           (3,F(19,291),F(293,582),11,F(175,194))]
    for r,a,x,p,target in cases:
        if mutation=='old-length' and r==2:a=x=F(3,5)
        v=budget(6,F(1,2),r,a,x,p,mutation)
        c.need('specializations',f'legal {r}',0<a<=x<=1 and p>=2)
        c.need('specializations',f'complete exponent {r}',v['G']==target)
        c.need('specializations',f'lower exponent {r}',v['lo']==target)
        c.need('specializations',f'upper exponent {r}',v['hi']==target)
        c.need('specializations',f'mixed exponent {r}',v['mixed']==target)
        tables.append(dict(r=r,a=str(a),x=str(x),p=p,**{q:str(z) for q,z in v.items()}))
    # A targeted dyad where dropping the lower endpoint changes the estimate.
    t=budget(6,F(1,2),1,F(1,5),F(1,2),5,mutation)
    c.need('endpoint-guards','low main block is not deleted',t['lo']==F(9,10))
    # Powers of the positive principal pole are NOT covered by the dual lemma.
    actual_principal=F(3,5); claimed_dual=F(1,2)
    principal_paid=claimed_dual if mutation=='principal-as-dual' else actual_principal
    c.need('principal','pole contribution retained separately',principal_paid==actual_principal and actual_principal>claimed_dual)

    # Exact maximization over ALL breakpoints, rather than a sampled maximum.
    for n,r,a,x,d in product([3,4,6,10],[1,2,3],[F(1,10),F(1,5)],[F(1,2),F(3,5)],[F(1,5),F(1,2)]):
        left,right=r*a,r*(a+x)
        pts=[left,right]+[b for b in [F(1,2),F(1),F(2)] if left<b<right]
        c.need('convex-endpoints',str((n,r,a,x,d)),max(k(n,v)-d*v for v in pts)==max(k(n,left)-d*left,k(n,right)-d*right))

    # Validate the symbolic all-n identities on a declared finite list;
    # the manuscript supplies their algebraic proof for all n.
    general=[]
    for n in range(6,65):
        a=F(2*n-6,3*n-8); theta=F(2*(n*n-2*n-2),n*(3*n-8))
        z=budget(n,F(1,2),1,a,a,3)
        c.need('general-order','a range',F(3,5)<=a<F(2,3))
        c.need('general-order','main exponent',z['lo']==z['hi']==theta)
        c.need('general-order','m3 exact deficit',k(n,3*a)-3*a/2==1-F(n-2,n*(3*n-8)))
        c.need('general-order','mixed deficit',z['mixed']==theta-F(2*(n-6),3*n*(3*n-8)))
        c.need('general-order','full result',z['G']==theta)
        for aa,xx in [(F(1,5),F(1,2)),(F(3,5),F(4,5)),(F(7,10),F(7,10))]:
            l=1-F(1,n)+(F(2,n)-F(1,2))*aa
            u=F(2,n)+(F(1,2)-F(1,n))*(aa+xx)
            w=F(2*n-4,3*n-8)
            target=theta+F((n-4)*(n-2),2*n*(3*n-8))*(xx-aa)
            c.need('general-order','exact lower certificate',w*l+(1-w)*u==target and target>=theta)
        if n in [6,8,10,12,32,64]:general.append({'n':n,'a':str(a),'error_exponent':str(theta)})

    # All-order line threshold: necessity and explicit sufficiency fixtures.
    thresholds=[]
    for n,r in product([3,4,6,8,12],range(1,13)):
        star=2*(k(n,F(r,2))-1)/r
        sigma=F(1,2)+star/2
        expected=(F(1,2) if r==1 else F(1,2)+F(1,2*n) if r==2 else F(2,3)+F(1,6*n) if r==3 else 1-F(1,r))
        if mutation=='false-all-orders' and n==6 and r==4:expected=F(1,2)
        c.need('line-threshold','closed formula',sigma==expected)
        # Necessity proof fixtures at and below the exact threshold.
        for d in sorted(set([star,star/2])):
            for a,x,p in [(F(1,20),F(1,4),2),(F(1,20),F(1,2),5),(F(1,20),F(3,4),11)]:
                c.need('line-threshold','no saving in envelope',budget(n,d,r,a,x,p)['G']>=1)
        # Construct an explicit positive a rather than numerically optimize it.
        d=(1+star)/2; B=k(n,F(r,2))-d*r/2; C=k(n,F(r))-d*r
        T=1+C-2*B; rat=T/(1-B); p=max(2,rat.numerator//rat.denominator+1)
        a=F(1,4*p*r)
        for _ in range(80):
            z=budget(n,d,r,a,F(1,2),p)
            if z['G']<1:break
            a/=2
        c.need('line-threshold','explicit saving exists',z['G']<1 and a>0 and p*r*a<=F(1,2))
        if n==6:thresholds.append({'r':r,'sigma_threshold':str(sigma)})

    # Sharp fourth-error certificate, both x ranges and integer Holder p.
    for a,x,p in product([F(j,20) for j in range(1,11)],[F(j,20) for j in range(1,21)],[2,3,5,11,31]):
        if a>x:continue
        z=budget(6,F(1,2),2,a,x,p)
        c.need('fourth-floor','complete 4/5 floor',z['G']>=F(4,5))
        if x<=F(1,2):
            low=2-8*x/3+max(F(1,p),a)-2*x/(3*p)
            c.need('fourth-floor','mixed intermediate',z['mixed']>=low>=F(2,3)+2*a/3)
        else:
            c.need('fourth-floor','upper main intermediate',z['hi']>=F(2,3)+2*a/3)
        c.need('fourth-floor','convex lower certificate',F(2,5)*(1-a)+F(3,5)*(F(2,3)+2*a/3)==F(4,5))

    # Full finite integer coefficient identities, not just the cancelled band.
    for A,X in [(2,2),(3,4),(4,7),(5,5),(7,9)]:
        pp={j:flat(j,X) for j in range(1,2*X+1) if flat(j,X)}
        mm={j:F(mu(j)) for j in range(1,A+1) if mu(j)}
        got=dconv(pp,mm);got[1]=got.get(1,F(0))-1
        got={j:v for j,v in got.items() if v}
        for n in range(1,2*A*X+2):
            h=sum(F(mu(e))*flat(n//e,X) for e in range(1,min(n,A)+1) if n%e==0)
            wanted=h-(1 if n==1 else 0)
            c.need('integer-source','complete coefficient',got.get(n,F(0))==wanted)
            if n<=A:c.need('integer-source','exact low cancellation',wanted==0)
        power={(1):F(1)}
        for r in range(1,4 if A<=3 else 3):
            power=dconv(power,got)
            c.need('integer-source','entire powered support',all(A**r<n<=(2*A*X)**r for n in power))
    for n in range(1,257):
        c.need('integer-source','Mobius divisor inversion',sum(mu(d) for d in range(1,n+1) if n%d==0)==(1 if n==1 else 0))

    # Literal sixth roots, including zero. Finite local algebra fixtures.
    roots=[zpow((0,1),j) for j in range(6)];states=[(0,0)]+roots
    for u,v,j in product(states,states,range(1,5)):
        lhs=zmul(u,zpow(v,6*j))
        if mutation=='force-coprime' and u!=(1,0) and v!=(1,0):lhs=(0,0)
        mask=1 if mutation=='erase-mask' else int(v!=(0,0))
        rhs=(u[0]*mask,u[1]*mask)
        c.need('local-masks','full sixth-power identity',lhs==rhs)
    w=(0,1)
    true=zmul(w,zconj(w)); put=zmul(w,w) if mutation=='wrong-conjugate' else true
    c.need('mixed-character','dual conjugation not collapsed',put==(1,0))

    # Mixed Holder is checked directly, with complex inputs, by integer powers.
    pairs=list(product([(0,0),(1,0),(0,1),(1,1),(-1,1)],repeat=2))
    for offset in range(0,len(pairs)-3):
        arr=pairs[offset:offset+4]
        for r,p in product([1,2,3],[2,3,5,11]):
            left=sum(znorm(m)**r*znorm(v)**r for m,v in arr)
            right=sum(znorm(m)**(p*r) for m,v in arr)*sum(znorm(v)**r for m,v in arr)**(p-2)*sum(znorm(v)**(2*r) for m,v in arr)
            c.need('mixed-holder','exact complex array',left**p<=right)

    # Q is smaller than U as often as it is comparable: negative prefactor kept.
    for j,d,x,q in product([1,2,3,4],[F(1,5),F(1,2)],[F(1,2),F(3,5),F(4,5)],[F(i,8) for i in range(1,9)]):
        if q>=x:
            band=-j*d*x+k(6,j*(q-x)); full=-j*d*x+k(6,j*(1-x))
            c.need('actual-conductors','monotone actual-Q bound',band<=full)
        else:
            J=8*j+2
            tail=1-j*d*q+J*(q-x)
            c.need('actual-conductors','subunit dual tail',tail<=1-j*d*x)

    return {'status':'FINITE ALGEBRA ONLY; proposed analytic deductions require independent review',
            'predicate_count':sum(c.count.values()),'groups':dict(sorted(c.count.items())),
            'specializations':tables,'general_order':general,'sextic_thresholds':thresholds,
            'scope':'Complete declared finite integer convolutions, local root masks, exact Holder and exponent algebra. No real L-values or zeros. General theorems use written proofs, not finite grids.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--mutation',choices=MUTATIONS)
    args=parser.parse_args()
    print(json.dumps(run(args.mutation),sort_keys=True,indent=2))
