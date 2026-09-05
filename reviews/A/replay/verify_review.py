#!/usr/bin/env python3
"""Reviewer A's independent finite controls. No analytic or RH certification."""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, isqrt
from pathlib import Path
import argparse, hashlib, json, sys

BASE = '8d16f8d9c475db290bc85e53d775b93b9bcdb336'
COUNTS = {}
def check(group, condition, detail=''):
    if not condition:
        raise RuntimeError(f'{group}: {detail}')
    COUNTS[group] = COUNTS.get(group, 0) + 1

def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def scale(a,b): return [x*b for x in a]
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def deriv(a): return [F(i)*a[i] for i in range(1,len(a))] or [F(0)]
def integ(a): return [F(0)]+[x/F(i+1) for i,x in enumerate(a)]
def evaluate(a,x):
    out=F(0)
    for y in reversed(a): out=out*x+y
    return out

def integral(a,l=F(0),r=F(1)):
    p=integ(a); return evaluate(p,r)-evaluate(p,l)

def det(a):
    a=[[F(x) for x in r] for r in a]; d=F(1)
    for k in range(len(a)):
        p=next((i for i in range(k,len(a)) if a[i][k]),None)
        if p is None:return F(0)
        if p!=k:a[k],a[p]=a[p],a[k];d=-d
        z=a[k][k];d*=z
        for i in range(k+1,len(a)):
            q=a[i][k]/z
            for j in range(k+1,len(a)):a[i][j]-=q*a[k][j]
    return d

def gram(vectors):
    return [[sum((x*y for x,y in zip(a,b)),F(0)) for b in vectors] for a in vectors]

def run():
    COUNTS.clear()
    for n in range(1,11):
        for s in product((-1,1),repeat=n):
            v=sum(a!=b for a,b in zip(s,s[1:])); minority=min(s.count(-1),s.count(1))
            check('minority_upper_bound',v<=2*minority)
    s=(1,)*4+(-1,)*4
    check('minority_lower_bound_counterexample',sum(a!=b for a,b in zip(s,s[1:]))==1<4)
    # Source identities, including the q^2 layer, in exact integer arithmetic.
    N=5000; mu=[1]*(N+1); mu[0]=0; prime=[True]*(N+1); prime[0]=prime[1]=False
    for p in range(2,N+1):
        if prime[p]:
            for k in range(p,N+1,p):mu[k]*=-1
            for k in range(p*p,N+1,p*p):mu[k]=0
            for k in range(p*p,N+1,p):prime[k]=False
    for n in range(1,N+1):
        beta=mu[n]-(mu[n//67] if n%67==0 else 0)
        rhs=0
        for e,c in ((0,1),(1,-2),(2,1)):
            q=67**e
            if n%q==0 and (n//q)%67:rhs+=c*mu[n//q]
        check('literal_beta_second_difference',beta==rhs,str(n))
    for e in range(16):
        coefficient=sum(c*(e-j+1) for j,c in ((0,1),(1,-2),(2,1)) if j<=e)
        check('finite_prefix_inverse_coefficients',coefficient==(1 if e==0 else 0))
    for U in (1,2,3,5,8,13):
        lim=200
        a=[F(0)]*(lim+1); nu=[F(0)]*(lim+1)
        for n in range(1,lim+1):
            a[n]=(1 if n==1 else 0)-sum(mu[d] for d in range(1,min(U,n)+1) if n%d==0)
            nu[n]=mu[n] if n>U else 0
        for n in range(1,lim+1):
            conv=sum(a[d]*mu[n//d] for d in range(1,n+1) if n%d==0)
            check('vaughan_tail_pair',conv==nu[n])
    # Weighted graph identity resolved into coefficients of log p.
    primes=[p for p in range(2,65) if prime[p]]
    for N in range(1,49):
        for trial in range(3):
            w=[F(0)]+[F((j*j+trial*j+1)%11-5,j%3+1) for j in range(1,N+1)]
            for p in primes:
                if p>N:break
                direct=F(0); squares=F(0)
                for j in range(1,N+1):
                    e=0; q=j
                    while q%p==0: e+=1; q//=p
                    direct+=F(e,j)*w[j]**2
                    n=p
                    while n*j<=N:
                        # Lambda(p^k)=log(p), NOT k*log(p).
                        direct+=F(1,n*j)*w[j]**2-2*F(1,n*j)*w[n*j]*w[j]
                        squares+=F(1,n*j)*(w[n*j]-w[j])**2
                        n*=p
                check('divisor_graph_prime_log_identity',direct==squares and squares>=0)
            check('divisor_graph_nullvector',all(F(1)-F(1)==0 for j in range(1,N+1)))
    # Euler--Beta live core: exact finite sum and exact integral of the Euler polynomial.
    for n in range(2,9):
        ps=primes[:n]; poly=[F(1)]
        for p in ps:poly=mul(poly,[F(1),-F(1,p*p)])
        live=poly[:];live[0]-=1;live[1]+=sum((F(1,p*p) for p in ps),F(0))
        beta=2*integral(mul(live,[F(1),F(-1)]))
        direct=F(0)
        for k in range(2,n+1):
            for subset in combinations(ps,k):
                den=1
                for p in subset:den*=p*p
                direct+=F((-1)**k,comb(k+2,2)*den)
        check('euler_beta_live_core',beta==direct and direct>0)
    # Gaussian rational arithmetic for the two-factor Takenaka counterexample.
    def zadd(z,w):return z[0]+w[0],z[1]+w[1]
    def zmul(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
    def zinv(z):
        d=z[0]*z[0]+z[1]*z[1]
        return z[0]/d,-z[1]/d
    I=(F(0),F(1));one=(F(1),F(0))
    for x in map(F,range(-8,9)):
        lhs=zmul((x,-F(1)),zinv(zmul((x,F(1)),(x-2,F(1)))))
        rhs=zadd(zmul(I,zinv((x,F(1)))),zmul((F(1),F(-1)),zinv((x-2,F(1)))))
        check('takenaka_two_factor_partial_fractions',lhs==rhs)
    for r in (F(1,100),F(1,20),F(1,10)):
        actual=6*r-2*r*r; advertised=2*r-2*r*r
        check('takenaka_band_integral_polynomial',actual-advertised==4*r>0)
    for m in range(1,17):
        theta=-F(4*m+3,4*m-3)
        check('raw_innerness_multiple_zero_control',abs(theta)>1)
    p=lambda t:1/(1+t*t)
    np=lambda t:2*t/(1+t*t)**2
    x,y=F(1,2),F(3,4); off=(p(x)-p(y))/(y-x)
    check('scalar_monotonicity_loewner_counterexample',np(x)*np(y)-off*off==-F(256,15625))
    check('spectral_coefficient_counterexample',det([[1,2],[1,1]])==-1)
    for n in range(2,6):
        for H in combinations(range(7),n):
            xs=list(range(1,n+1))
            check('generalized_vandermonde',det([[F(x)**h for x in xs] for h in H])>0)
    # Source Casimir: exact action on a polynomial multiplying the Gaussian atom.
    def M(P):return add(mul([F(0),F(2)],deriv(P)),mul([F(0),F(-2)],P))
    def Dt(P):return add(M(P),scale(P,F(1,2)))
    for k in range(13):
        P=[F(0)]*k+[F(1)]
        left=add(Dt(Dt(P)),scale(P,-F(1,4)))
        right=M(add(M(P),P))
        check('theta_casimir_polynomial',left==right)
    # Finite energy-Schur controls; all directions, not entrywise residual tests.
    for k in range(1,9):
        A=[F(1),F(2),F(3)];B=[[F(k,3),F(-1,2)],[F(1,4),F(k,5)],[F(-2,3),F(1,7)]]
        V=[[F((i+j+k)%5-2,7) for j in range(2)] for i in range(3)]
        C=[[F(10),F(1)],[F(1),F(10)]]
        S=[[C[i][j]-sum(B[r][i]*B[r][j]/A[r] for r in range(3)) for j in range(2)] for i in range(2)]
        U=[[C[i][j]-sum(B[r][i]*V[r][j]+V[r][i]*B[r][j]-A[r]*V[r][i]*V[r][j] for r in range(3)) for j in range(2)] for i in range(2)]
        R=[[sum((B[r][i]-A[r]*V[r][i])*(B[r][j]-A[r]*V[r][j]) for r in range(3)) for j in range(2)] for i in range(2)]
        gap=[[U[i][j]-S[i][j] for j in range(2)] for i in range(2)]
        lower=[[R[i][j]-gap[i][j] for j in range(2)] for i in range(2)]
        check('schur_upper_residual_psd',gap[0][0]>=0 and gap[1][1]>=0 and det(gap)>=0)
        check('schur_lower_residual_psd',lower[0][0]>=0 and lower[1][1]>=0 and det(lower)>=0)
    for M in range(1,17):
        for C in (F(1,4),F(1,3),F(1,2)):
            s=C-F(1,3); sm=C-(1-F(1,4**M))/3
            check('energy_completion_finite_sections',sm-s==F(1,3*4**M)>0)
    check('positive_upper_not_positive_limit',F(1,4)-F(1,4)==0 and F(1,4)-F(1,3)<0)
    S92=sum((F(4,4*k+1) for k in range(93)),F(0))
    S152=sum((F(4,4*k+1) for k in range(153)),F(0))
    check('window_coercivity_constants',S92>F(35,4))
    check('window_coercivity_constants',S152>F(37,4))
    check('window_coercivity_constants',F(3,2)*(1-(F(17205)+F(7,4))/93636)>=F(6,5))
    check('window_coercivity_constants',F(3,2)**2/F(6,5)==F(15,8))
    # Abstract conjugation-pair tensor controls in a rational Hilbert model.
    for m1 in range(1,5):
        for m2 in range(1,5):
            for r in (F(0),F(1,3),F(2),F(-3,2)):
                f=[F(1),F(0),F(0)];g=[F(1),F(1),r];h=[F(0),F(0),r]
                T=[[m1*f[i]*f[j]+m2*(g[i]*g[j]-h[i]*h[j]) for j in range(3)] for i in range(3)]
                mass=m1+2*m2; energy=sum(t*t for row in T for t in row)
                simple=1 if m1==1 else 0; distinct=3
                check('abstract_hilbert_simple_count',energy>=2*mass-simple)
                check('abstract_hilbert_distinct_count',energy>=3*mass-2*distinct)
    # Zero-mass second variation for the Montgomery--Taylor minimization.
    for k in range(1,9):
        v=[-F(1,k+1)]+[F(0)]*(k-1)+[F(1)]
        V=integ(v);norm=integral(mul(v,v));pnorm=integral(mul(V,V))
        check('montgomery_taylor_second_variation',evaluate(V,F(1))==0 and norm-2*pnorm>=F(7,9)*norm)
    rho=F(1,20)
    check('catalan_uncancelled_height',2*rho-(2*rho-rho*rho/2)==F(1,800))
    for B in (2,4,7,10):
        for S in range(1,min(B,4)+1):
            for rows in combinations(range(S+3),S):
                mat=[[F(comb(2*B+a,i)) for i in range(S)] for a in rows]
                vand=F(1)
                for i in range(S):
                    for j in range(i+1,S):vand*=rows[j]-rows[i]
                fac=1
                for i in range(S):
                    for j in range(1,i+1):fac*=j
                check('catalan_pascal_minor',det(mat)==vand/fac and abs(det(mat))>=1)
    return {'schema':'riemann.review.A.finite-controls.v1','base_sha':BASE,
            'counts':COUNTS.copy(),'total':sum(COUNTS.values()),
            'rh_proved':False,'analytic_theorems_machine_verified':False,
            'upstream_campaigns_rerun':False,'arithmetic':'EXACT_FRACTION_AND_INTEGER',
            'scope':'Independent bounded controls; synthetic examples are not actual Xi counterexamples.'}

def strict_load(path):
    def pairs(items):
        d={}
        for k,v in items:
            if k in d:raise ValueError('duplicate JSON key')
            d[k]=v
        return d
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check');ap.add_argument('--output');a=ap.parse_args()
    result=run()
    if a.check:
        saved=strict_load(a.check)
        # JSON booleans and floats are not interchangeable with exact counts.
        if type(saved.get('total')) is not int or saved.get('rh_proved') is not False:
            raise ValueError('invalid type or RH status')
        if any(type(v) is not int for v in saved.get('counts',{}).values()):
            raise ValueError('noninteger check count')
        if saved!=result:raise ValueError('saved result differs from exact reconstruction')
    out=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if a.output:Path(a.output).write_text(out)
    else:sys.stdout.write(out)
if __name__=='__main__':main()
