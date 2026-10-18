#!/usr/bin/env python3
"""Finite exact checks, not certification of the infinite analytic proof."""
from __future__ import annotations
import argparse
import itertools
import json
import math
from collections import Counter
from fractions import Fraction as F
from typing import Iterable

class Failure(Exception):
    pass

COUNTS = Counter()
MUTATION = ''

def require(value: bool, group: str) -> None:
    COUNTS[group] += 1
    if not value:
        raise Failure(group)

# Q[z]/(z^2-z+1), with z a primitive sixth root.
def add(u, v): return (u[0]+v[0], u[1]+v[1])
def mul(u, v):
    a,b=u; c,d=v
    return (a*c-b*d, a*d+b*c+b*d)
def scale(a, u): return (a*u[0], a*u[1])
def conj(u): return (u[0]+u[1], -u[1])
def norm2(u): return u[0]*u[0]+u[0]*u[1]+u[1]*u[1]
ZERO=(F(0),F(0)); ONE=(F(1),F(0)); ROOT=(F(0),F(1))
def power(z, k):
    out=ONE
    for _ in range(k): out=mul(out,z)
    return out

# Deliberately independent elementary Mobius constructions.
def factor(x: int):
    out=[]; p=2
    while p*p<=x:
        if x%p==0:
            e=0
            while x%p==0: x//=p; e+=1
            out.append((p,e))
        p+=1
    if x>1: out.append((x,1))
    return out

def mu_trial(x: int) -> int:
    fs=factor(x)
    return 0 if any(e>1 for _,e in fs) else (-1)**len(fs)

def mobius(N: int):
    out=[1]*(N+1); out[0]=0
    for p in range(2,N+1):
        if len(factor(p))==1 and factor(p)[0]==(p,1):
            for j in range(p,N+1,p): out[j]*=-1
            for j in range(p*p,N+1,p*p): out[j]=0
    return out

# Full residue fields F_7 and F_13. These are convention fixtures, not the full Hecke family.
TABLES={}
for p,g in ((7,3),(13,2)):
    tab={pow(g,j,p):power(ROOT,j%6) for j in range(p-1)}
    if len(tab)!=p-1: raise Failure('primitive_generator_setup')
    TABLES[p]=tab

def character(x: int, primes=(7,), exponent=1):
    out=ONE
    for p in primes:
        if x%p==0:
            return ONE if MUTATION=='erased_mask' else ZERO
        out=mul(out,power(TABLES[p][x%p],exponent))
    return out

def cutoff(y: F):
    # This rational, nonsmooth fixture checks only the flat-head polynomial identity.
    # The analytic proof uses a fixed C-infinity cutoff instead.
    return F(1) if y<=1 else max(F(0),2-y)

def kfun(n: int, v: F):
    return max(F(1),v,1-F(1,n)+2*v/n,F(2,n)+(1-F(1,n))*v)

def p_add(a,b):
    z=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a): z[i]+=x
    for i,x in enumerate(b): z[i]+=x
    while len(z)>1 and z[-1]==0: z.pop()
    return z

def p_scale(c,a): return [c*x for x in a]
def p_mul(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    while len(z)>1 and z[-1]==0: z.pop()
    return z

def run():
    mu=mobius(1024)
    for x in range(1,1025): require(mu[x]==mu_trial(x),'complete_mobius_prefix')
    for p in (7,13):
        for exponent in range(6):
            require(character(0,(p,),exponent)==ZERO,'literal_nonunit_zero')
            for x in range(p):
                for y in range(p):
                    require(mul(character(x,(p,),exponent),character(y,(p,),exponent))==character(x*y,(p,),exponent),'full_residue_multiplicativity')
    # Conjugate and ordinary product are NOT interchangeable.
    z=character(3,(7,))
    actual=mul(z,z if MUTATION=='same_character_dual' else conj(z))
    require(actual==ONE,'dual_conjugation')
    require(mul(z,z)!=ONE,'dual_conjugation')
    for n in (3,4,6,8):
        for v in range(1,1025):
            c=e=1
            for p,j in factor(v): c*=p**(j%n); e*=p**(j//n)
            require(c*e**n==v,'complete_power_decomposition')
            if n==6:
                for primes in ((7,),(13,),(7,13)):
                    rhs=character(c,primes)
                    if any(e%p==0 for p in primes): rhs=ZERO
                    if MUTATION=='false_shared_coprimality' and math.gcd(c,e)>1: rhs=ZERO
                    require(character(v,primes)==rhs,'shared_power_mask')
    fixture_cases=0
    for A in (2,3,4,6,8):
        for X in (A,A+1,2*A):
            N=2*A*X
            direct=[ZERO]*(N+1)
            for b in range(1,2*X+1):
                for e in range(1,A+1):
                    weight=mu[e]*cutoff(F(b,X))
                    direct[b*e]=add(direct[b*e],scale(weight,character(b*e,(7,13))))
            for v in range(1,N+1):
                h=F(0)
                for e in range(1,A+1):
                    if v%e==0:
                        den=X if MUTATION=='wrong_cutoff_dilation' else e*X
                        h+=mu[e]*cutoff(F(v,den))
                require(direct[v]==scale(h,character(v,(7,13))),'complete_cutoff_convolution')
                if v<=A:
                    require(h==(1 if v==1 else 0),'exact_low_coefficient_cancellation')
            fixture_cases+=1
    # Coefficient powering preserves all ordered tuple factorizations.
    for A in (2,3,4,6,8):
        conv={1:1}
        for _ in range(3):
            nxt=Counter()
            for u,b in conv.items():
                for v in range(1,A+1): nxt[u*v]+=b*mu[v]
            conv=dict(nxt)
        tuples=Counter()
        for x,y,z in itertools.product(range(1,A+1),repeat=3): tuples[x*y*z]+=mu[x]*mu[y]*mu[z]
        for v in range(1,A**3+1): require(conv.get(v,0)==tuples.get(v,0),'complete_mollifier_cube')
    # Formal polynomial identities in n: coefficient equality, not interpolation.
    n=[F(0),F(1)]; one=[F(1)]
    D=p_add(p_scale(3,n),[-8]); An=p_add(p_scale(2,n),[-6])
    Fn=[F(-4),F(-4),F(2)]
    low=p_add(p_mul(p_add(n,[-1]),D),p_scale(F(1,2),p_mul(p_add([4],p_scale(-1,n)),An)))
    high=p_add(p_scale(2,D),p_mul(p_add(n,[-2]),An))
    gap1=p_add(p_add(Fn,p_scale(-1,p_mul(n,D))),p_scale(F(1,2),p_mul(n,An)))
    gap2=p_add(Fn,p_scale(-1,p_mul(n,An)))
    gapdual=p_add(p_add(p_scale(3,Fn),p_scale(-3,p_mul(p_add(n,one),D))),p_scale(F(1,2),p_mul(p_add(p_scale(3,n),[8]),An)))
    weights=p_add(p_scale(2,p_add(n,[-2])),p_add(n,[-4]))
    weighted_const=p_add(p_scale(2,p_mul(p_add(n,[-2]),p_add(n,[-1]))),p_scale(2,p_add(n,[-4])))
    for left,right in ((low,Fn),(high,Fn),(gap1,p_add(n,[-4])),(gap2,p_scale(2,p_add(n,[-2]))),(gapdual,p_scale(2,p_add(n,[-6]))),(weights,D),(weighted_const,Fn)):
        require(left==right,'formal_general_order_identity')
    for order in range(6,129):
        a=F(2*(order-3),3*order-8)
        f=F(2*(order*order-2*order-2),order*(3*order-8))
        require(F(1,2)<a<F(2,3),'general_order_parameters')
        main=[1-a/2,a,1-F(1,order)+(F(2,order)-F(1,2))*a,F(2,order)+(1-F(2,order))*a]
        require(max(main)==f,'all_main_monomials')
        r2=kfun(order,1-a)-a/2
        r4=kfun(order,2*(1-a))-a
        m6=max(F(1),kfun(order,3*a)-3*a/2)
        require(m6==1,'sixth_mollifier_moment')
        cost=r2+a/2 if MUTATION=='pointwise_mollifier' else (m6+r2+r4)/3
        require(cost<=f,'joint_dual_budget')
        for r in (1,2,3):
            for iq in range(21):
                q=F(iq,20)
                if q>=a:
                    scalar= -F(r,2)*(1 if MUTATION=='lost_actual_conductor' else q)+F(r,2)*(q-a)
                    require(scalar==-r*a/2,'actual_conductor_cancellation')
                    require(kfun(order,r*(q-a))<=kfun(order,r*(1-a)),'conductor_endpoint_monotonicity')
                else:
                    J=r+1
                    require(-r*q/2+J*(q-a)<=-r*a/2,'complete_subunit_tail')
        for j in range(1,17):
            aa=F(j,32); xx=F(3,4)
            mains=[1-aa/2,(aa+xx)/2,1-F(1,order)+(F(2,order)-F(1,2))*aa,F(2,order)+(F(1,2)-F(1,order))*(aa+xx)]
            require(max(mains)<=1-aa/2,'shorter_mollifier_main')
        for kk in range(1,41):
            if kk<=3: ak=a; theta=1-f
            else: ak=F(2,kk); theta=F(1,kk)
            require(kk*ak<=2,'all_fixed_order_polynomial_moment')
            require(theta>0 and theta<1,'capped_not_zero_excluding')
    # Holder checks over every two-entry rational nonnegative pair from this set.
    vals=(F(0),F(1,2),F(1),F(2))
    for m in itertools.product(vals,repeat=2):
        for r in itertools.product(vals,repeat=2):
            left=sum(x*x*y*y for x,y in zip(m,r))**3
            right=sum(x**6 for x in m)*sum(y*y for y in r)*sum(y**4 for y in r)
            require(left<=right,'three_factor_holder')
    complex_values=[ZERO,ONE,ROOT,scale(F(1,8),ONE),scale(F(1,2),ROOT),scale(F(2),ONE),(-F(1),F(1))]
    for z,m,T,k in itertools.product(complex_values,complex_values,(F(1),F(2),F(16)),range(1,9)):
        error=norm2(add(mul(z,m),scale(-1,ONE)))
        if norm2(z)==0: lhs=F(0) if MUTATION=='erased_zero_cap' else T
        else: lhs=min(norm2(z)**(-k),T)
        if norm2(z)==0: require(lhs==T,'actual_zero_keeps_cap')
        require(lhs<=2**(2*k)*norm2(m)**k+4*T*error,'pointwise_capped_transfer')
    require(F(7,8)-F(11,15)==F(17,120),'predecessor_comparison')
    require(F(4,15)>F(1,80),'larger_low_order_cap')
    require(F(1,100)<F(1,80),'no_false_all_order_cap_superiority')
    return {
      'status':'FINITE_EXACT_CHECKS_PASS_NOT_ANALYTIC_CERTIFICATION',
      'groups':dict(sorted(COUNTS.items())), 'total_predicates':sum(COUNTS.values()),
      'cutoff_cases':fixture_cases,
      'sextic':{'mollifier_exponent':'3/5','main_cutoff_exponent':'3/5','error_second_moment':'11/15','old_error_exponent':'7/8','saving':'17/120','M6':'1','R2':'7/10','R4':'1/2','cap_first_three_orders':'4/15'},
      'all_n_symbolic_polynomial_identities':7,
      'coverage':'Rational integer divisor ranges and complete F7/F13 convention fixtures; not a complete number-field family or L-value computation.',
      'rh_proved':False
    }

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mutation',default='')
    args=parser.parse_args(); MUTATION=args.mutation
    try: print(json.dumps(run(),sort_keys=True,indent=2))
    except Failure as e:
        raise SystemExit('REJECT:'+str(e))
