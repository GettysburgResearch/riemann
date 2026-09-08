#!/usr/bin/env python3
"""Reviewer-written exact checks; no research module, network or zero oracle.

These reconstruct finite algebra, not infinite analytic estimates, historical
campaigns, or a proof of RH. SymPy is used only for exact polynomial identities.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json
from math import isqrt
import platform
import sys
import sympy as sp

COUNTS: Counter[str] = Counter()


def check(ok: bool, group: str, message: str) -> None:
    if not ok:
        raise ValueError(group + ': ' + message)
    COUNTS[group] += 1


def zero(expr, group: str, label: str) -> None:
    check(sp.cancel(expr) == 0, group, label)


def jordan() -> None:
    s, y, r = sp.symbols('s y r')
    p = y-y**2/4+y**3/18-y**4/96
    j = sp.integrate(p, (y, 0, y))
    L = 2*(1-s-r*y+p)+2*((1-s)*y-r*y*y/2+j)-2*r
    bar = L.subs(r, 2/(s+2))
    zero(p.subs(y, 2)-sp.Rational(23,18), 'jordan', 'p(2)')
    zero(j.subs(y, 2)-sp.Rational(67,45), 'jordan', 'j(2)')
    zero(sp.diff(p,y,2)+sp.Rational(5,18)+(y-sp.Rational(4,3))**2/8,
         'jordan', 'global p concavity identity')
    zero(sp.diff(p,y)+sp.diff(p,y,2)-sp.Rational(1,2)+y*(y*y-y+4)/24,
         'jordan', 'p prime plus p double prime')
    zero(sp.diff(L,y,2)-(-2*r+2*(sp.diff(p,y,2)+sp.diff(p,y))),
         'jordan', 'L concavity reduction')
    zero(sp.diff(bar,s)-(-2*(1+y)+2*(y*y+2*y+2)/(s+2)**2),
         'jordan', 'scale derivative')
    zero(10*(1+y)-3*(y*y+2*y+2)-(2-y)*(3*y+2),
         'jordan', 'uniform scale derivative sign on [0,2]')
    num = 1440-2160*s-1160*s*s-30*s**3-s**4-3*s**5
    zero(bar.subs(y,s)-s*num/(720*(s+2)), 'jordan', 'left endpoint')
    zero(num.subs(s,sp.Rational(1,2))-sp.Rational(2115,32), 'jordan', 'left numerator')
    check(Q(2115,32)/1800 == Q(47,1280), 'jordan', 'small-scale margin')
    zero(bar.subs(y,2)+(90*s*s+7*s-46)/(15*(s+2)), 'jordan', 'right endpoint')
    zero(bar.subs({s:sp.Rational(1,2),y:2})-sp.Rational(8,15), 'jordan', 'right small-scale')
    zero(bar.subs({s:sp.Rational(2,3),y:sp.Rational(19,20)})-sp.Rational(1068867,256000000),
         'jordan', 'connecting endpoint')
    check(Q(1068867,256000000)>Q(1,256), 'jordan', 'connecting margin')
    zero(bar.subs({s:sp.Rational(2,3),y:2})-sp.Rational(1,30), 'jordan', 'connecting endpoint at two')
    zero((sp.Rational(157,45)-2*s-6/(s+2)).subs(s,sp.Rational(1,2))-sp.Rational(4,45),
         'jordan', 'small-scale infinite-y reserve')
    zero((sp.Rational(323,45)-4*s-12/(s+2)).subs(s,sp.Rational(2,3))-sp.Rational(1,90),
         'jordan', 'connecting infinite-y reserve')
    check(2*Q(3,25)+Q(616,625)*Q(4,3)-Q(3,2)==Q(203,3750), 'jordan', 'large-scale margin')
    check(Q(275,14)>Q(34,9)**2, 'jordan', 'original coefficient dominates required margin')
    P=(s+1)*(s+2)*(s+3)
    zero(P/(s+4)-(s*s+2*s+3-6/(s+4)), 'jordan', 'Euler--Maclaurin rational term')
    check(Q(1,12)+Q(1,75)==Q(29,300) and Q(1,9)-Q(29,300)==Q(13,900),
          'jordan', 'prime-deletion constants')
    q=sp.symbols('q')
    zero((q+1)/((q+s)*(q+s+1)) * (q+s+1)/(q+1)-1/(q+s),
         'jordan', 'gamma recurrence grouping rational part')


def mobius_values(N: int) -> list[int]:
    mu=[1]*(N+1); mu[0]=0
    for p in range(2,N+1):
        if all(p % d for d in range(2, isqrt(p)+1)):
            for k in range(p,N+1,p):mu[k]*=-1
            for k in range(p*p,N+1,p*p):mu[k]=0
    return mu


def floor_and_domain() -> None:
    mu=mobius_values(512)
    m=Q(0); S=Q(0); signed=Q(0); diagonal=Q(0)
    for n in range(1,513):
        m += Q(mu[n],n); S+=m*m; signed+=mu[n]*m; diagonal+=Q(mu[n]*mu[n],n)
        check(sum(mu[d]*(n//d) for d in range(1,n+1))==1, 'arithmetic', 'Mobius-floor inversion')
        check(abs(m)<=1, 'arithmetic', 'bounded harmonic Mobius sum')
        check(S==(n+1)*m*m-2*signed+diagonal, 'arithmetic', 'complete input-work identity')
    for N in (1,2,4,8,16,32,64,128):
        X=N+1
        cs=[Q(0)]+[Q(mu[n]) for n in range(1,X)] + [-X*sum((Q(mu[n],n) for n in range(1,X)),Q(0))]
        check(sum((cs[n]/n for n in range(1,X+1)),Q(0))==0, 'arithmetic', 'compact inverse terminal balance')
        for k in range(1,X):
            a=sum((cs[n] for n in range(1,X+1) if k%n==0),Q(0))
            check(a==(1 if k==1 else 0), 'arithmetic', 'compact inverse exact full prefix')
    beta,gamma=sp.symbols('beta gamma', real=True)
    c=beta-sp.Rational(1,2)
    zero(1/(2*c)-1/(beta**2+gamma**2)-((beta-1)**2+gamma**2)/(2*c*(beta**2+gamma**2)),
         'hardy', 'projected value kernel with derivative-normalization condition')
    Y=sp.symbols('Y', positive=True)
    M,F,l=sp.symbols('M F l')
    b=(F-1)/l; a=-M-b
    zero(M+a+b,'hardy','two-index balance')
    # sum mu(n) log(n)/n = log(Y)*M-F.
    zero(-(sp.log(Y)*M-F)-a*sp.log(Y)-b*(sp.log(Y)+l)-1,
         'hardy','two-index derivative equals one')
    z,beta_s,delta=sp.symbols('z beta_s delta')
    zero((z+beta_s)**2/((z+beta_s-1)*(z+1))-
         (1+1/((2-beta_s)*(z+beta_s-1))-(1-beta_s)**2/((2-beta_s)*(z+1))),
         'hardy','inverse distribution rational split')


def inv00(mat: list[list[Q]]) -> Q:
    a=[row[:]+[Q(int(i==j)) for j in range(len(mat))] for i,row in enumerate(mat)]
    n=len(a)
    for k in range(n):
        pivot=next(i for i in range(k,n) if a[i][k])
        a[k],a[pivot]=a[pivot],a[k]
        v=a[k][k];a[k]=[x/v for x in a[k]]
        for i in range(n):
            if i!=k:
                v=a[i][k];a[i]=[x-v*y for x,y in zip(a[i],a[k])]
    return a[0][n]


def projection_controls() -> None:
    prior=Q(1)
    for n in range(1,17):
        g=[[Q(5 if i==j else -2 if abs(i-j)==1 else 0) for j in range(n)] for i in range(n)]
        err=1-inv00(g)
        exact=Q(3*4**n,4**(n+1)-1)
        check(err==exact, 'projection', 'exact tridiagonal projection')
        check(err-Q(3,4)==Q(3,4*(4**(n+1)-1)), 'projection', 'excess vs nonzero intrinsic floor')
        check(Q(3,4)<err<=prior,'projection','finite improvement does not imply zero floor');prior=err
    for n in range(1,9):
        g=[[Q(9,2) if i==j else Q(-3) if abs(i-j)==1 else Q(1) if abs(i-j)==2 else Q(0)
            for j in range(n)] for i in range(n)]
        e=1-Q(1,2)*inv00(g)
        check(e>Q(3,4),'projection','two positive sources retain nonzero defect')
        if n<=2:check(e==[Q(8,9),Q(4,5)][n-1],'projection','declared first two errors')


def square_grid() -> None:
    n,t=sp.symbols('n t', positive=True)
    w=1/n**2-1/(n+1)**2
    zero(w-(2*n+1)/(n*n*(n+1)**2),'square_grid','exact cell weight')
    for expr,den,label in ((n**3*w-1,(n+1)**2,'weight lower'),(2-n**3*w,(n+1)**2,'weight upper')):
        pol=sp.Poly(sp.cancel(expr*den).subs(n,t+2),t)
        check(all(c>=0 for c in pol.all_coeffs()) and pol.eval(0)>0, 'square_grid',label)
    check(Q(125,8)*Q(7,4)==Q(875,32)<28,'square_grid','complete variance tail constant')
    check(4*28==112,'square_grid','held-endpoint versus mean tail constant')
    z=sp.symbols('z')
    zero((1-sp.Rational(1,2)/(z+1))*(1+sp.Rational(1,2)/(z+sp.Rational(1,2)))-1,
         'square_grid','causal weighted-prime/ordinary-prime inverse')
    # Fixed local detail does not control arbitrary cumulative levels.
    weights=[Q(1,5),Q(1,3),Q(7,15)];values=[Q(-2),Q(0),Q(3)]
    mean=sum((w*x for w,x in zip(weights,values)),Q(0))
    detail=sum((w*(x-mean)**2 for w,x in zip(weights,values)),Q(0))
    for shift in (0,10,1000):
        energy=sum((w*(x+shift)**2 for w,x in zip(weights,values)),Q(0))
        check(energy==(mean+shift)**2+detail, 'square_grid','orthogonal mean/detail includes old level')


def multiply(a: tuple[int,int], b: tuple[int,int], k: int) -> tuple[int,int]:
    return (a[0]*b[0]+k*a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def scale(a: tuple[int,int], m: int) -> tuple[int,int]:return(m*a[0],m*a[1])

def minus(a,b):return(a[0]-b[0],a[1]-b[1])

def dickson(z: tuple[int,int], n: int, k: int):
    a,b=(2,0),z
    if n==0:return a
    for _ in range(1,n):a,b=b,minus(multiply(z,b,k),a)
    return b


def graph(x,y,z,r,k):
    for sig in (-1,1):
        if x==scale(dickson(z,r+1,k),sig**r) and y==scale(z,sig):return True
        if x==scale(z,sig**r) and y==scale(minus(multiply(z,z,k),(2,0)),sig):return True
    return False


def spectral_difference(a,b,c,r):
    left=Counter((e*a+b*(r-2*j))%24 for e in (-1,1) for j in range(r+1))
    right=Counter((c*(2*r+1-2*j))%24 for j in range(2*r+2))
    return tuple(left[h]-right[h] for h in range(24))


def affine_solutions(f,d):
    if not any(d):return 'ALL' if not any(f) else 'NONE'
    i=next(i for i,v in enumerate(d) if v)
    k=-Q(f[i],d[i])
    if k>=0 and k.denominator==1 and all(f0+k*d0==0 for f0,d0 in zip(f,d)):
        return 'ISOLATED_'+str(k.numerator)
    return 'NONE'


def all_rank() -> dict:
    alphabets={1:{(-2,0):12,(-1,0):8,(0,0):6,(1,0):4,(2,0):0},
               2:{(0,-1):9,(0,0):6,(0,1):3},
               3:{(0,-1):10,(0,0):6,(0,1):2},
               5:{(0,0):6}}
    table={}; admitted=0; nongraph=0
    for k,alpha in alphabets.items():
        per=[]
        for r0 in range(1,25):
            count=0
            for x,y,z in product(alpha,repeat=3):
                a,b,c=alpha[x],alpha[y],alpha[z]
                f=spectral_difference(a,b,c,r0)
                f24=spectral_difference(a,b,c,r0+24)
                d=tuple(v-u for u,v in zip(f,f24))
                sol=affine_solutions(f,d)
                check(not sol.startswith('ISOLATED'), 'torsion','no lost isolated higher-rank solution')
                expected=graph(x,y,z,r0,k) or (k==2 and x==(0,0) and y!=(0,0) and z!=(0,0) and r0%4==3)
                check((sol=='ALL')==expected, 'torsion','complete affine family vs graph/exception')
                if sol=='ALL':count+=1;admitted+=1
                if sol=='ALL' and not graph(x,y,z,r0,k):nongraph+=1
                # Bounded additional test of the proven progression formula.
                f72=spectral_difference(a,b,c,r0+72)
                check(f72==tuple(v+3*dv for v,dv in zip(f,d)), 'torsion','affine progression reconstruction')
            per.append(count)
        table[str(k)]=per
    check(table['1'][:6]==[12,15,12,11,16,11], 'torsion','square-class-one count table')
    check(table['2']==[8,7]*12, 'torsion','square-class-two count table')
    check(table['3']==[0,5]*12, 'torsion','square-class-three count table')
    check(table['5']==[0,1]*12, 'torsion','other square-class count table')
    return {'affine_rows':4320,'admitted_affine_families':admitted,
            'nongraph_affine_families':nongraph,'per_residue_counts':table,
            'isolated_nonnegative_rank_quotients':0}


def entropy_and_schur() -> None:
    x=sp.symbols('x')
    lower=2-x*x-(x+1-x*x)**2
    zero(lower-(1-x)**3*(1+x), 'entropy', 'sharp ramp lower factorization')
    zero(lower-(1-x*x)**3/4-(1-x)**3*(1+x)*(1-(1+x)**2/4),
         'entropy', 'cubic sensitivity comparison')
    for r in range(1,13):
        check(sum(sp.binomial(r,k)*2**k for k in range(r+1))==3**r,
              'entropy', 'late-tail jet-filter total-variation majorant')
    check(Q(3,2)**2/Q(3,4)==3, 'operator', 'general simultaneous residual constant')
    check(Q(3,2)**2/Q(6,5)==Q(15,8), 'operator', 'specified window residual constant')
    check(Q(3,4)*4==3, 'operator', 'periodic dual normalization')


def quantitative_budgets() -> None:
    s=Q(1,16)
    check(2*s<Q(1,5) and 2*s<Q(1,2),'budgets','Sobolev source/Blaschke summability')
    check(Q(4,3)*s/8-s/3==-s/6,'budgets','clipped inverse high-frequency exponent')
    check(1+4*(-Q(3,8))==-Q(1,2),'budgets','full residual high-frequency tail')
    check((Q(1025,1024)*Q(761,128))<6,'budgets','late-tail perturbation L1 margin')
    check((Q(1025,1024)**2*Q(157,32))<5,'budgets','late-tail perturbation L2 margin')
    for ell in range(1,25):
        L=23+6*ell;a=16+4*ell;n=2**ell-1
        check(L<=2**(ell+4),'budgets','small-value zero-count budget')
        check(Q(96*n*(n+1)*L,2**a)<=Q(3,256),'budgets','small-value exceptional arc budget')


def main() -> None:
    jordan();floor_and_domain();projection_controls();square_grid()
    torsion=all_rank();quantitative_budgets();entropy_and_schur()
    result={'marker':'PASS_REVIEWER_EXACT_RECONSTRUCTIONS','python':platform.python_version(),
            'sympy':sp.__version__,'groups':dict(COUNTS),'checks':sum(COUNTS.values()),
            'torsion_classification':torsion,'research_modules_executed':False,
            'full_repository_checkout':False,'infinite_analytic_proofs_machine_checked':False,
            'fresh_research_certificates':False,'lean_build':False,'rh_proved':False}
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=='__main__':main()
