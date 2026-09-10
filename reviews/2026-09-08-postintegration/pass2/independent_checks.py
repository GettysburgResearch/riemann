#!/usr/bin/env python3
"""Independent bounded rational reconstruction for review pass 2.

No research checker is imported. Infinite theorems still require REPORT.md's
arguments. The N=32 certificate uses independent directed logarithms and exact
matrix inverses, not the author's trial or numerical backend.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd, lcm, isqrt
from functools import lru_cache
import hashlib
import json

COUNTS: dict[str, int] = {}

def require(ok, message):
    if not ok:
        raise ValueError(message)

def check(group, ok, message):
    require(ok, group + ': ' + message)
    COUNTS[group] = COUNTS.get(group, 0) + 1

def factor(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out

def mu(n):
    f=factor(n)
    return 0 if any(k>1 for k in f.values()) else (-1)**len(f)

def primes(N):return [p for p in range(2,N+1) if factor(p)=={p:1}]
def norm(z):return sum(a*a for a in z)
def minus(x,y):return tuple(a-b for a,b in zip(x,y))
def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))

def covariance_checks():
    for m in range(1,17):
        for n in range(1,17):
            Q=lcm(m,n);x=[F(j%m,m) for j in range(Q)];y=[F(j%n,n) for j in range(Q)]
            mx=sum(x)/Q;my=sum(y)/Q
            cov=sum((a-mx)*(b-my) for a,b in zip(x,y))/Q
            check('CRT_covariance',cov==F(gcd(m,n)**2-1,12*m*n),'residue covariance')
    controls=[]
    for N in range(2,9):
        Q=lcm(*range(1,N+1));CN=N*N*(1+2*(N-1).bit_length())
        for seed in range(3):
            a=[F(0)]+[F((i*i+seed*3)%11-5,7) for i in range(1,N+1)]
            a[1]=-sum((a[n]/n for n in range(2,N+1)),F(0));b=F(seed-1,3)
            def u(j):return b-sum(a[n]*(j//n) for n in range(1,N+1))
            def j2(d):return d*d*__import__('functools').reduce(lambda x,p:x*(1-F(1,p*p)),factor(d),F(1))
            V=(b+sum(a)/2)**2+sum(j2(d)*sum(a[n]/n for n in range(d,N+1,d))**2 for d in range(1,N+1))/12
            samples=[u(j)**2 for j in range(Q)]
            check('RC_period_mean',sum(samples)/Q==V,'complete mean')
            for H in (1,7,31):
                for length in (1,13,Q+3):
                    d=sum(u(j)**2 for j in range(H,H+length))-length*V
                    check('RC_block_discrepancy',abs(d)<=CN*V,'uniform block control')
            # A finite tail sum with a conservative complete remaining bound.
            H=13;T=4096
            tail=sum((u(j)**2/F(j*(j+1)) for j in range(H,T)),F(0))
            lo=V/H-F(CN)*V/(H*(H+1));hi=V/H+F(CN)*V/(H*(H+1))
            check('RC_tail_overlap',tail<=hi and tail+max(samples)/T>=lo,'complete tail enclosure consistency')
            controls.append((N,seed,str(V)))
    for H in range(2,18):
        a=[F(mu(n)) for n in range(1,H)];a.append(-H*sum((a[n-1]/n for n in range(1,H)),F(0)))
        u=lambda j:F(1)-sum(a[n-1]*(j//n) for n in range(1,H+1))
        check('RC_false_cutoff_control',all(u(j)==0 for j in range(1,H)) and u(lcm(*range(1,H+1)))==1,'bare window is not full norm')
        check('RC_centering_jet',F(1,H)-F(4,2*H)+F(4,4*H)==0 and 1-4+4==1,'balance and center')
        for j in range(17):
            check('RC_centering_values',j-4*(j//2)+4*(j//4)==(0,1,-2,-1)[j%4],'four-cell response')
    for Y in range(2,65):
        M=sum((F(mu(n),n) for n in range(1,Y)),F(0));S=sum(mu(n) for n in range(1,Y))
        A=F(3*Y-1,2);c=F(-2-S)/A;bb=c+M;aa=-c-2*M
        coef={n:F(mu(n)) for n in range(1,Y)}
        for n in range(Y,2*Y):
            coef[n]=coef.get(n,F(0))+aa*F(n,Y)
            coef[2*n]=coef.get(2*n,F(0))+2*bb*F(n,Y)
        check('RC_centered_completion',sum(coef.values())==-2 and sum(v/n for n,v in coef.items())==0,'two constraints')
        check('RC_centered_completion',all(coef[n]==mu(n) for n in range(1,Y)) and max(abs(v) for v in coef.values())<9,'prefix/coefficients')
    return hashlib.sha256(json.dumps(controls).encode()).hexdigest()

def divisor_checks():
    for p in (2,3,5,7):
        q=F(1,p)
        for m in range(1,9):
            vectors=[[F(1)]*(m+1)]
            for j in range(1,m+1):
                A=sum((q**l for l in range(1,m-j+2)),F(0))
                u=[F(0) if e<j-1 else -A if e==j-1 else F(1) for e in range(m+1)]
                Lu=[sum((u[e]-u[k] for k in range(e)),F(0))+sum((q**(k-e)*(u[e]-u[k]) for k in range(e+1,m+1)),F(0)) for e in range(m+1)]
                check('DPG_power_spectrum',Lu==[(j+A)*z for z in u],'exact eigenvector')
                check('DPG_power_spectrum',all(sum(q**e*u[e]*v[e] for e in range(m+1))==0 for v in vectors),'weighted orthogonality')
                vectors.append(u)
    supports=[list(range(1,N+1)) for N in range(2,33)]
    supports += [[n for n in range(1,121) if all(p in (2,3,5) for p in factor(n))], [d for d in range(1,361) if 360%d==0]]
    for S in supports:
        for a in S[1:]:
            p=min(factor(a));desc=[]
            for n in S:
                k=n
                while k>1 and k!=a:
                    pp=min(factor(k));k//=pp**factor(k)[pp]
                if k==a:desc.append(n)
            expected=[n for n in S if n%a==0 and all(q<p for q in factor(n//a))]
            check('divisor_tree',desc==expected,'full power least-prime tree')
        f={n:(F((n*n)%11-5,7),F((3*n)%7-3,5)) for n in S}
        for p in sorted({q for n in S for q in factor(n)}):
            energy=F(0);diag=F(0);cross=F(0)
            for n in S:
                e=factor(n).get(p,0);up=sum((F(1,p**k) for k in range(1,8) if n*p**k in S),F(0))
                diag+=(e+up)*F(1,n)*norm(f[n])
                for k in range(1,e+1):
                    j=n//p**k;energy+=F(1,n)*norm(minus(f[n],f[j]));cross+=2*F(1,n)*dot(f[n],f[j])
            check('divisor_full_form',energy==diag-cross,'each log-prime coefficient')
    check('divisor_missing_support_control',not any(6==p**k for p in primes(6) for k in range(1,4)),'{1,6} has no edges')

@lru_cache(None)
def log_bounds(n):
    require(type(n) is int and n>=1,'positive integer log input')
    k=n.bit_length()-1;y=F(n,2**k)
    def series(y):
        z=(y-1)/(y+1)
        lower=2*sum((z**(2*j+1)/F(2*j+1) for j in range(64)),F(0))
        return lower,lower+2*z**129/(129*(1-z*z))
    l,h=series(y);l2,h2=series(F(2));l+=k*l2;h+=k*h2
    scale=1<<112
    return F((l*scale).__floor__(),scale),F((h*scale).__ceil__(),scale)

def matrix(n):return [[F(0) for _ in range(n)] for _ in range(n)]

def solve_positive(A,b):
    n=len(A);D=[];L=matrix(n)
    for j in range(n):
        L[j][j]=1;dj=A[j][j]-sum((L[j][k]**2*D[k] for k in range(j)),F(0))
        require(dj>0,'nonpositive exact LDL pivot');D.append(dj)
        for i in range(j+1,n):L[i][j]=(A[i][j]-sum((L[i][k]*L[j][k]*D[k] for k in range(j)),F(0)))/dj
    y=[]
    for j in range(n):y.append(b[j]-sum((L[j][k]*y[k] for k in range(j)),F(0)))
    z=[v/d for v,d in zip(y,D)];x=[F(0)]*n
    for j in range(n-1,-1,-1):x[j]=z[j]-sum((L[k][j]*x[k] for k in range(j+1,n)),F(0))
    require(all(dot(row,x)==v for row,v in zip(A,b)),'exact solution residual')
    return x,D

def decimal_bounds(lo,hi,d=18):
    scale=10**d
    def render(v):
        sign='-' if v<0 else '';v=abs(v)
        return sign+str(v//scale)+'.'+str(v%scale).zfill(d)
    return [render((lo*scale).__floor__()),render((hi*scale).__ceil__())]

def inverse32():
    N=32;n=N-1;Klo=matrix(n);Khi=matrix(n);Kcheap=matrix(n);edge_count=0
    basis={j:([F(-1,i) for i in range(2,N+1)] if j==1 else [F(int(i==j)) for i in range(2,N+1)]) for j in range(1,N+1)}
    for p in primes(N):
        lo,hi=log_bounds(p);cheap=F(2,3)*(p.bit_length()-1)
        for k in range(1,N.bit_length()):
            q=p**k
            for j in range(1,N//q+1):
                target=j*q;v=[a-b for a,b in zip(basis[target],basis[j])];edge_count+=1
                for ii in range(n):
                    for jj in range(n):
                        vv=v[ii]*v[jj]/target
                        Klo[ii][jj]+=lo*vv;Khi[ii][jj]+=hi*vv;Kcheap[ii][jj]+=cheap*vv
    M=[[F(int(i==j),i)+F(1,i*j) for j in range(2,N+1)] for i in range(2,N+1)]
    gap=[[Kcheap[i][j]-M[i][j]/384 for j in range(n)] for i in range(n)]
    b=[F(1)]+[F(0)]*(n-1)
    _,piv=solve_positive(gap,b)
    xhi,ph=solve_positive(Khi,b);xlo,pl=solve_positive(Klo,b)
    lower=xhi[0];upper=xlo[0]
    check('ADG32_independent_certificate',edge_count==65,'complete edge count')
    check('ADG32_independent_certificate',lower<=upper and upper-lower<F(1,10**27),'inverse bracket width')
    check('ADG32_independent_certificate',lower>F('0.7444806194657') and upper<F('0.7444806194659'),'advertised enclosure')
    return {'N':N,'dimension':n,'prime_power_edges':edge_count,'primes':primes(N),'inverse_quadratic_outward_decimal':decimal_bounds(lower,upper),
            'exact_positive_pivots':len(piv)+len(ph)+len(pl),'cheap_gap':'Kcheap - M/384 > 0',
            'inverse_interval_sha256':hashlib.sha256((str(lower)+'\n'+str(upper)).encode()).hexdigest(),
            'method':'independent 112-bit rational log endpoints; exact LDL and inverse order; no author trial or checker'}

def finite_constants():
    for n in range(1,513):
        ell=n.bit_length();L=23+6*ell
        check('analytic_integer_budgets',L<=2**(ell+4),'ST exceptional-set budget')
        K=n-1;k=(n-1).bit_length();J=168*k*k+2904*k+12513
        check('analytic_integer_budgets',J==4*(42*k*k+726*k+3128)+1,'FC rational floor exponent')
    coeff=[F(x,10000) for x in (4284,-1839,-1199,-742,-371)]
    check('FC_feedback_atom',sum(coeff)==F(133,10000) and -sum(coeff)**2==F(-17689,100000000),'actual feedthrough atom')
    return {'fixed_feedback_atom':'-17689/100000000'}

# Rational polynomial checks of the complete endpoint multiplier and the two
# equivalent physical-correlation coordinates (not prime-phase independence).
def padd(a,b):
    return [(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))]
def pscale(a,c):return [v*c for v in a]
def pmul(a,b):
    ans=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[i+j]+=x*y
    return ans
def ppow(a,n):
    ans=[F(1)]
    for _ in range(n):ans=pmul(ans,a)
    return ans
def pdiff(a):return [i*a[i] for i in range(1,len(a))] or [F(0)]
def pint(a,lo,hi):return sum((x*(hi**(i+1)-lo**(i+1))/(i+1) for i,x in enumerate(a)),F(0))
def multiplier_and_coordinate_checks():
    eta=padd(pscale(ppow([F(-1),F(3)],2),3),pscale(ppow([F(-1),F(3)],3),-2))
    for L in [F(1),F(3,2),F(2),F(3),F(5),F(17)]:
        chi=padd([F(1)],padd(pscale(ppow([F(-1),1/L],2),-3),pscale(ppow([F(-1),1/L],3),2)))
        pieces=[(pscale(pmul([F(0),F(1)],eta),-2),F(1,3),F(2,3)),([F(0),F(-2)],F(2,3),L),(pscale(pmul([F(0),F(1)],chi),-2),L,2*L)]
        value=F(0)
        for poly,lo,hi in pieces:
            z=padd(poly,pscale(pdiff(pdiff(poly)),-1));value+=pint(pmul(z,z),lo,hi)
        check('EPD_multiplier',value==F(1142,315)*L**3+F(768,35)*L+F(463514,1215)+F(624,5)/L,'full polynomial integral')
        check('EPD_multiplier',value<576*L**3,'constant24')
    for N in range(2,17):
        mass={n:F((n*n+2*n)%9-4,5) for n in range(2,N+1)}
        cosnorm=sum((v*w*(F(min(n,m),max(n,m))+F(1,n*m))/2 for n,v in mass.items() for m,w in mass.items()),F(0))
        c=sum((v/n for n,v in mass.items()),F(0));forward=F(0);running=F(0)
        for n in range(2,N+1):
            running+=n*mass[n]
            forward+=running**2/2*(F(1,n*n)-(F(1,(n+1)**2) if n<N else F(0)))
        backward=c*c
        for n in range(1,N):
            tail=sum((v/k for k,v in mass.items() if k>n),F(0))
            backward+=F((n+1)**2-n*n,2)*tail*tail
        check('EPD_PDS_same_norm',cosnorm==backward==forward+c*c/2,'same complete physical norm')


def main():
    digest=covariance_checks();divisor_checks();multiplier_and_coordinate_checks();constants=finite_constants();inv=inverse32()
    result={'schema':'riemann.review.pass2.independent.v1','marker':'PASS_INDEPENDENT_BOUNDED_RECONSTRUCTIONS',
            'case_counts':COUNTS,'total_assertions':sum(COUNTS.values()),'period_control_digest':digest,
            'inverse32':inv,'constants':constants,'rh_proved':False,'infinite_theorems_machine_proved':False,
            'author_checkers_imported':False,'full_repository_checkout':False}
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=='__main__':main()
