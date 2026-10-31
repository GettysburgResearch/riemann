#!/usr/bin/env python3
"""Full-source rational interval certificate for a local Bessel boundary gate.

Reconstructs all weights, counts every denominator zero in a complex disk by
Graeffe/Pellet, isolates that many real poles with positive residues, and proves
the sign on the entire boundary semicircle by Bernstein subdivision. No sampled
complex grid and no approximate special function enters an acceptance decision.
"""
from fractions import Fraction as F
from math import comb, factorial, isqrt
from pathlib import Path
import argparse, contextlib, hashlib, io, json, runpy, sys

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--a',type=int,default=20)
parser.add_argument('--order',type=int,default=100)
parser.add_argument('--radius',type=int,default=500,help='Energy disk radius')
parser.add_argument('--verbose',action='store_true')
args=parser.parse_args()
parent=Path(__file__).resolve().parents[1]
dependency=parent/'riemann/standalone/2026-10-30-operator-theta-swarm/theta/verify_polya_obstruction.py'
if not dependency.exists():
    dependency=parent.parent/'2026-10-30-operator-theta-swarm/theta/verify_polya_obstruction.py'
with contextlib.redirect_stdout(io.StringIO()):dep=runpy.run_path(str(dependency))
I=dep['I'];Q=10**130
# Configure the same reviewed outward-grid arithmetic at a finer precision.
# This changes only the isolated loaded namespace, never the dependency file.
I.__init__.__globals__['Q']=Q
PI=16*dep['atan_inv'](5,130)-4*dep['atan_inv'](239,130)
expi=dep['exp_interval']

def root(x,n=2):
    def lower(t):
        q=t*Q**n;v=q.numerator//q.denominator
        return isqrt(v) if n==2 else isqrt(isqrt(v))
    return I(F(lower(x.lo),Q),F(lower(x.hi)+1,Q))

def source(x):
    x=I(x);Y=x+root(1+x*x);Y4=root(Y,4)
    value=I(0)
    for k in range(1,8):
        value+=(4*PI**2*k**4*Y**2-6*PI*k*k*Y)*Y4*expi(-PI*k*k*Y)
    # First omitted index 8. All terms are positive, with adjacent upper-bound
    # ratio <= (9/8)^4 exp(-51) < 1/2 for Y>=1.
    tail=80*8**4*Y**2*Y4*expi(-192*I(Y.lo))
    return I(value.lo,value.hi+tail.hi)

def ibessel(n,a):
    term=(a/2)**n/F(factorial(n));s=term
    for k in range(1,181):term*=a*a/(4*k*(n+k));s+=term
    nxt=term*a*a/(4*181*(n+181));ratio=a*a/(4*182*(n+182))
    if not 0<=ratio<1:raise ArithmeticError('Bessel remainder ratio')
    return I(s,s+nxt/(1-ratio))

def add(p,q):
    r=[I(0)]*max(len(p),len(q))
    for j,v in enumerate(p):r[j]+=v
    for j,v in enumerate(q):r[j]+=v
    return r

def scale(p,v):return [v*x for x in p]

def mul(p,q):
    r=[I(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r

def ev(p,x):
    x=I(x) if not isinstance(x,I) else x;r=I(0)
    for c in reversed(p):r=r*x+c
    return r

def derivative(p):return [j*p[j] for j in range(1,len(p))]
def abs_hi(x):return max(abs(x.lo),abs(x.hi))
def abs_lo(x):return min(abs(x.lo),abs(x.hi)) if x.lo*x.hi>0 else F(0)
def sign(x):return 1 if x.lo>0 else -1 if x.hi<0 else 0

def polynomials(a,M,R):
    c=[ibessel(n,a)*source(F(n)/a) for n in range(M+1)]
    if any(v.lo<=0 for v in c):raise ArithmeticError('Coefficient enclosure not positive')
    c=[v/c[0] for v in c]
    # These polynomial recurrences are exact rational: v=nu/a.
    pp,qq=[F(1)],[F(0)];p,q=[F(0),F(1)],[-1/a]
    A=[I(1)];B=[I(0)]
    def fadd(p,q):
        r=[F(0)]*max(len(p),len(q))
        for j,v in enumerate(p):r[j]+=v
        for j,v in enumerate(q):r[j]+=v
        return r
    for n in range(1,M+1):
        A=add(A,[2*(-1)**j*v*c[n]*(R/a**2)**j for j,v in enumerate(p[::2])])
        B=add(B,[2*(-1)**j*v*c[n]*(R/a**2)**j for j,v in enumerate(q[::2])])
        pn=fadd(pp,fadd([2*F(n)/a*v for v in p],[F(0)]+[2*v for v in p]))
        qn=fadd(qq,fadd([2*F(n)/a*v for v in q],[F(0)]+[2*v for v in q]))
        pp,p=p,pn;qq,q=q,qn
    factor=max(abs_hi(v) for v in A+B)
    return [v/factor for v in A],[v/factor for v in B]

def graeffe_count(B):
    p=B[:]
    for step in range(11):
        highs=[abs_hi(v) for v in p]
        for k,v in enumerate(p):
            margin=abs_lo(v)-(sum(highs)-highs[k])
            if margin>0:return {'rounds':step,'zero_count':k,'strict_margin':str(margin)}
        if step==10:break
        even=mul(p[::2],p[::2]);odd=[I(0)]+mul(p[1::2],p[1::2])
        p=add(even,scale(odd,-1));factor=max(abs_hi(v) for v in p)
        if factor==0:raise ArithmeticError('zero Graeffe polynomial')
        p=[v/factor for v in p]
    raise ArithmeticError('No strict Graeffe/Pellet root count')

def real_poles(A,B,R,count):
    pairs=[];lo=F(0);old=sign(ev(B,lo))
    if not old:raise ArithmeticError('Denominator vanishes at zero or unresolved sign')
    for j in range(1,int(R)+1):
        hi=F(j,R);new=sign(ev(B,hi))
        if not new:raise ArithmeticError('Unresolved grid endpoint sign')
        if new!=old:pairs.append((lo,hi,old))
        lo=hi;old=new
    if len(pairs)!=count:raise ArithmeticError(('Incomplete real root coverage',len(pairs),count))
    results=[];Bp=derivative(B)
    for lo,hi,sgn in pairs:
        for iteration in range(256):
            interval=I(lo,hi);av=ev(A,interval);dv=ev(Bp,interval)
            gamma=-R*av/dv if sign(av) and sign(dv) else None
            if gamma is not None and gamma.hi<0:raise ArithmeticError('Certified negative residue')
            if hi-lo<F(1,10**12) and gamma is not None and gamma.lo>0:break
            mid=(lo+hi)/2;bm=ev(B,mid);s=sign(bm)
            if not s:
                if not sign(dv):raise ArithmeticError('Root refinement loses directed sign')
                # Interval mean-value theorem encloses the root even if its
                # midpoint sign is smaller than the coefficient uncertainty.
                enclosure=I(mid)-bm/dv
                newlo=max(lo,enclosure.lo);newhi=min(hi,enclosure.hi)
                if newhi<=newlo or newhi-newlo>=F(9,10)*(hi-lo):
                    raise ArithmeticError('Insufficient precision for a positive residue')
                lo,hi=newlo,newhi
                sgn=sign(ev(B,lo))
                if not sgn:raise ArithmeticError('Interval-Newton endpoint unresolved')
            elif s==sgn:lo=mid
            else:hi=mid
        else:raise ArithmeticError('Residue refinement iteration limit')
        results.append({'E_lo':str(R*lo),'E_hi':str(R*hi),'residue_lo':str(gamma.lo),'residue_hi':str(gamma.hi)})
    return results

def circle_polynomial(A,B):
    n=max(len(A),len(B));A=A+[I(0)]*(n-len(A));B=B+[I(0)]*(n-len(B))
    c=[sum((A[k+d]*B[k]-A[k]*B[k+d] for k in range(n-d)),I(0)) for d in range(1,n)]
    U0=[I(1)];U1=[I(0),I(2)];h=[I(0)]
    for j,v in enumerate(c):
        U=U0 if j==0 else U1;h=add(h,scale(U,v))
        if j>0:U0,U1=U1,add([I(0)]+scale(U1,2),scale(U0,-1))
    return h

def bernstein_positive(h):
    d=len(h)-1
    # x=2t-1, followed by power-to-Bernstein conversion on 0<=t<=1.
    q=[sum(((-1)**(j-k)*comb(j,k)*h[j] for j in range(k,d+1)),I(0))*2**k for k in range(d+1)]
    b=[sum((F(comb(k,j),comb(d,j))*q[j] for j in range(k+1)),I(0)) for k in range(d+1)]
    stack=[(b,0)];leaves=0;maximum=0;bound=None
    while stack:
        p,depth=stack.pop();lower=min(v.lo for v in p)
        if lower>0:
            leaves+=1;maximum=max(maximum,depth);bound=lower if bound is None else min(bound,lower);continue
        if max(v.hi for v in p)<0:raise ArithmeticError('Negative Bernstein cell')
        if depth>=48:raise ArithmeticError('Bernstein proof depth exhausted')
        left=[p[0]];right=[p[-1]];row=p
        while len(row)>1:
            row=[(row[k]+row[k+1])/2 for k in range(len(row)-1)]
            left.append(row[0]);right.append(row[-1])
        stack.append((list(reversed(right)),depth+1));stack.append((left,depth+1))
    return {'degree':d,'accepted_cells':leaves,'maximum_depth':maximum,'strict_lower_bound':str(bound)}

def main():
    a=F(args.a);M=args.order;R=F(args.radius)
    if a<=0 or M<3 or R<=0:raise ValueError('positive parameters, M>=3 required')
    A,B=polynomials(a,M,R)
    if args.verbose:print('source coefficients and boundary polynomials reconstructed',file=sys.stderr,flush=True)
    count=graeffe_count(B)
    if args.verbose:print('complete complex-disk denominator zero count:',count['zero_count'],file=sys.stderr,flush=True)
    poles=real_poles(A,B,R,count['zero_count'])
    if args.verbose:print('all real poles and positive residues enclosed',file=sys.stderr,flush=True)
    boundary=bernstein_positive(circle_polynomial(A,B))
    report={'status':'PASS','arithmetic':'outward rational intervals; complete theta and Bessel tails',
      'a':str(a),'M':M,'energy_radius':str(R),'z_radius_squared':str(4*R),
      'source_dependency_sha256':hashlib.sha256(dependency.read_bytes()).hexdigest(),'grid_decimal_digits':130,
      'graeffe_pellet':count,'complete_real_poles':poles,'whole_semicircle_bernstein':boundary,
      'conclusion':'Every zero of the complete actual-source Bessel transform in |z|^2<=4R is real; the disk contains no nonreal denominator pole or common factor.',
      'not_proved':['RH','any new zero-free region for zeta','unbounded cofinal local gate','global real-rootedness of this finite transform']}
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
