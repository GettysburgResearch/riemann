#!/usr/bin/env python3
"""Exact finite regression for the reciprocal-moment packet; NOT an analytic verifier."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb, gcd, isqrt
import json

COUNTS = Counter()
MUTATION = None

def check(condition, name):
    COUNTS[name] += 1
    if not condition:
        raise ValueError('FAILED: ' + name)

def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def div_exact(a, b):
    a, b = trim(a), trim(b)
    out = [F(0)] * (len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        j = len(a)-len(b)
        z = a[-1]/b[-1]
        out[j] += z
        for i, v in enumerate(b):
            a[i+j] -= z*v
        a = trim(a)
    if any(a):
        raise ValueError('Nonexact polynomial division')
    return tuple(trim(out))

@lru_cache(None)
def cyclotomic(n):
    p = [F(-1)] + [F(0)]*(n-1) + [F(1)]
    for d in range(1, n):
        if n % d == 0:
            p = div_exact(p, cyclotomic(d))
    return tuple(p)

def ring(n, a):
    a, phi = trim(a), cyclotomic(n)
    while len(a) >= len(phi):
        j, z = len(a)-len(phi), a[-1]
        for i, v in enumerate(phi):
            a[i+j] -= z*v
        a = trim(a)
    return tuple(a + [F(0)]*(len(phi)-1-len(a)))

def add(n, a, b):
    c = [F(0)]*max(len(a), len(b))
    for i,v in enumerate(a): c[i] += v
    for i,v in enumerate(b): c[i] += v
    return ring(n,c)

def mul(n, a, b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): c[i+j] += v*w
    return ring(n,c)

def scale(n,a,t): return ring(n,[t*v for v in a])
def one(n): return ring(n,[F(1)])
def zero(n): return ring(n,[F(0)])

@lru_cache(None)
def root(n,j):
    j %= n
    return ring(n,[F(0)]*j+[F(1)])

def power(n,a,k):
    r=one(n)
    while k:
        if k&1: r=mul(n,r,a)
        a=mul(n,a,a); k//=2
    return r

def primes(x):
    sieve=[True]*(x+1)
    if x>=0: sieve[0]=False
    if x>=1: sieve[1]=False
    for p in range(2,isqrt(x)+1):
        if sieve[p]:
            for j in range(p*p,x+1,p): sieve[j]=False
    return [p for p in range(2,x+1) if sieve[p]]

def factors(x):
    d, out=2,{}
    while d*d<=x:
        while x%d==0:
            out[d]=out.get(d,0)+1; x//=d
        d+=1
    if x>1: out[x]=out.get(x,0)+1
    return out

def mu(x):
    ff=factors(x)
    return 0 if any(e>1 for e in ff.values()) else (-1)**len(ff)

def exponent_checks():
    for n in range(3,17):
        for j in range(1,20):
            d=F(j,20)
            for ratio in (F(1,8),F(1,4),F(1,2)):
                a=d*ratio
                knots={a,a+F(1,2)}
                if a<=F(1,2)<=a+F(1,2): knots.add(F(1,2))
                K=lambda v:max(F(1),v,1-F(1,n)+2*v/n,F(2,n)+(1-F(1,n))*v)
                check(max(K(v)-d*v for v in knots)<=1-d*a,'main_full_breakpoints')
                # Q=U^q, dual C=Q/sqrt(U), q in [1/2,1].
                for q in (F(1,2),F(3,4),F(1)):
                    v=q-F(1,2)
                    sign=1 if MUTATION=='dual_sign' else -1
                    dual=sign*d*q+d*v+K(v)
                    check(dual<=1-d/2,'actual_conductor_dual')
                check(1-d/2+(1-d)*a<=1-d*a,'dual_mollifier_cost')
    for k in range(1,33):
        for j in range(1,20):
            d=F(j,20); c=F(1,20)
            a=min(d/8,F(1,16*k)); eta=min(d*a/4,c/4)
            tau=c/(2*k) if MUTATION=='large_cap' else c/(8*k)
            check(a<=d/2 and eta>0,'moment_parameter_domain')
            check(F(1,2)+2*k*a*(F(3,2)-d)<=F(11,16),'all_needed_polynomial_moments')
            check(1-c+2*k*tau<=1-2*eta,'bad_capped_mass')
            check(1-d*a/2<=1-2*eta,'transfer_margin')
        a=F(1,16*k)
        check(min(a/8,F(1,80))==F(1,128*k),'sextic_error_rate')
        check(2*k*F(1,160*k)==F(1,80),'sextic_common_powered_cap')
    q0=F(1,4)
    check(1-q0/(4-6*q0)==F(9,10),'density_625')
    # Algebraic proofs of the piecewise bounds reduce to these signed factors.
    for n in range(3,65):
        check(F(1,2)-F(1,n)>0,'symbolic_main_margin_coefficient')
        check(F(n,2)>1,'full_power_root_sum_converges')


def local_laws():
    cases=[]
    for n in range(3,9):
        q=next(p for p in primes(150) if (p-1)%n==0)
        g=next(g for g in range(2,q) if len({pow(g,e,q) for e in range(q-1)})==q-1)
        logs={pow(g,e,q):e for e in range(q-1)}
        omega=F((q-1)*q**(n-1),q**n-1)
        check(omega==(1-F(1,q))/(1-F(1,q**n)),'nfree_local_unit_probability')
        check(sum((q-1)*q**(n-j-1) for j in range(n))==q**n-1,'complete_compressed_valuation_census')
        for k in range(1,n+2):
            t=F(1,q)
            acc=zero(n)
            for r in range(1,q):
                z=logs[r]%n
                v=power(n,add(n,one(n),scale(n,root(n,z),-t)),k)
                vc=power(n,add(n,one(n),scale(n,root(n,-z),-t)),k)
                acc=add(n,acc,mul(n,v,vc))
            direct=add(n,scale(n,acc,F(q**(n-1),q**n-1)),scale(n,one(n),1-omega))
            unit=F(0)
            for a in range(k+1):
                for b in range(k+1):
                    keep=(a==b) if MUTATION=='equality_diagonal' else ((a-b)%n==0)
                    if keep: unit+=comb(k,a)*comb(k,b)*(-t)**(a+b)
            op=(1-F(1,q)) if MUTATION=='replace_omega' else omega
            predicted=scale(n,one(n),1-op+op*unit)
            check(direct==predicted,'finite_field_root_and_zero_moment')
            if k<n:
                check(unit==sum(F(comb(k,a)**2)*t**(2*a) for a in range(k+1)),'low_order_root_reduction')
            if k==n:
                equal=sum(F(comb(k,a)**2)*t**(2*a) for a in range(k+1))
                check(unit-equal==2*(-t)**n,'first_genuine_modular_alias')
        cases.append({'order':n,'residue_prime':q,'compressed_residues':q**n-1})
    return cases


def cutoff_checks():
    # Independent Mobius production by a divisor recursion.
    mr=[0]*1025; mr[1]=1
    for n in range(2,len(mr)):
        mr[n]=-sum(mr[d] for d in range(1,n) if n%d==0)
        check(mr[n]==mu(n),'complete_integer_mobius_census')
    for X in (4,8,16,32):
        for A in range(1,min(X,8)+1):
            cap=2*A*X
            def V(m):
                if m<=X:return F(1)
                if m>=2*X:return F(0)
                return F(2*X-m,X)
            p={b:V(b) for b in range(1,2*X+1) if gcd(b,6)==1}
            conv=[F(0)]*(cap+1)
            for b,v in p.items():
                for e in range(1,A+1):
                    if gcd(e,6)==1: conv[b*e]+=v*mr[e]
            if MUTATION!='no_unit_subtraction': conv[1]-=1
            for b in range(1,cap+1):
                h=F(0) if b<=A else sum((F(mr[e])*V(b//e) for e in range(1,A+1) if b%e==0),F(0))
                if gcd(b,6)!=1: h=F(0)
                check(conv[b]==h,'literal_flat_cutoff_highpass')
    # Actual order-three residue character modulo 7, with exterior mask at 2,3.
    n,q,g=3,7,3; logs={pow(g,e,q):e%n for e in range(q-1)}
    def chi(m,changed=False):
        if gcd(m,6*q)!=1:
            return one(n) if changed else zero(n)
        return root(n,logs[m%q])
    for b in range(1,65):
        for e in range(1,33):
            check(mul(n,chi(b),chi(e))==chi(b*e),'literal_character_multiplicativity')
    for order in range(3,9):
        for b in range(1,513):
            ff=factors(b)
            c=1; e=1
            for p,v in ff.items(): c*=p**(v%order);e*=p**(v//order)
            check(c*e**order==b,'complete_power_decomposition')
            if MUTATION=='impose_coprimality':
                check(gcd(c,e)==1,'false_coprimality_gate')
            if order==3:
                lhs=chi(b)
                rhs=mul(n,chi(c),one(n) if gcd(e,42)==1 else zero(n))
                if MUTATION=='erase_mask': rhs=chi(c,True)
                check(lhs==rhs,'power_removal_nonunit_mask')


def ideal_checks():
    # Complete integral ideals of Q(sqrt(-3)) outside primes over 2 and 3.
    cap=128
    pp=[]
    for p in primes(cap):
        if p in (2,3):continue
        if p%3==1:pp.extend([(p,'split+',p),(p,'split-',p)])
        elif p*p<=cap:pp.append((p,'inert',p*p))
    pp.sort(key=lambda z:(z[2],z[0],z[1]))
    ideals=[]
    def dfs(i,n,exps):
        if i==len(pp): ideals.append((n,tuple(exps)));return
        q=pp[i][2];v=0
        while n<=cap:
            dfs(i+1,n,exps+[v]);n*=q;v+=1
    dfs(0,1,[])
    direct=Counter(n for n,_ in ideals)
    euler=[0]*(cap+1);euler[1]=1
    for _,_,q in pp:
        prev=euler[:]
        euler=[0]*(cap+1)
        for a in range(1,cap+1):
            if not prev[a]:continue
            v=a
            while v<=cap:euler[v]+=prev[a];v*=q
    for n in range(1,cap+1):check(direct[n]==euler[n],'complete_eisenstein_norm_census')
    cols=[(n,v) for n,v in ideals if n<=32 and max(v,default=0)<=1]
    for n in (3,6):
        for (_,u),(_,v) in product(cols,repeat=2):
            label=tuple(a+(n-1)*b for a,b in zip(u,v))
            check(all(z%n==0 for z in label)==(u==v),'ideal_not_norm_diagonal')
    pplus=next(v for q,v in ideals if q==7 and v[0]==1)
    pminus=next(v for q,v in ideals if q==7 and v!=pplus)
    principal=(7==7) if MUTATION=='collapse_conjugates' else all((a-b)%6==0 for a,b in zip(pplus,pminus))
    check(not principal,'split_conjugates_must_not_collapse')
    # True tuple multiplication versus independently grouped product coefficients.
    for n,j,C in ((3,2,16),(6,2,16),(3,3,8)):
        cc=[(norm,v) for norm,v in cols if norm<=C]
        prodcoeff=defaultdict(F)
        for tt in product(cc,repeat=j):
            v=tuple(sum(x[1][i] for x in tt) for i in range(len(pp)))
            coeff=F(1)
            for norm,e in tt: coeff*=F((-1)**sum(e),norm)
            prodcoeff[v]+=coeff
        grouped=F(0)
        for v,av in prodcoeff.items():
            for w,aw in prodcoeff.items():
                if all((r-s)%n==0 for r,s in zip(v,w)):
                    om=F(1)
                    for i,(r,s) in enumerate(zip(v,w)):
                        if r or s:
                            q=pp[i][2];om*=(1-F(1,q))/(1-F(1,q**n))
                    grouped+=av*aw*om
        raw=F(0)
        for tt in product(cc,repeat=2*j):
            u=tuple(sum(x[1][i] for x in tt[:j]) for i in range(len(pp)))
            v=tuple(sum(x[1][i] for x in tt[j:]) for i in range(len(pp)))
            if any((r-s)%n for r,s in zip(u,v)):continue
            z=F(1)
            for norm,e in tt:z*=F((-1)**sum(e),norm)
            for i,(r,s) in enumerate(zip(u,v)):
                if r or s:
                    q=pp[i][2];z*=F((q-1)*q**(n-1),q**n-1)
            raw+=z
        check(raw==grouped,'complete_capped_ideal_tuple_diagonal')
    return {'all_ideals_cap':cap,'all_allowed_ideals':len(ideals),'squarefree_columns_cap_32':len(cols),'tuple_cases':3}


def main():
    global MUTATION
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mutate',choices=['dual_sign','large_cap','equality_diagonal','replace_omega','no_unit_subtraction','impose_coprimality','erase_mask','collapse_conjugates'])
    args=p.parse_args();MUTATION=args.mutate
    exponent_checks();laws=local_laws();cutoff_checks();ideals=ideal_checks()
    print(json.dumps({'status':'PASS_FINITE_ALGEBRA_ONLY','predicates':sum(COUNTS.values()),'counts':dict(sorted(COUNTS.items())),'local_law_cases':laws,'ideal_census':ideals,'analytic_proof_verified':False,'rh_proved':False},indent=2,sort_keys=True))

if __name__=='__main__':main()
