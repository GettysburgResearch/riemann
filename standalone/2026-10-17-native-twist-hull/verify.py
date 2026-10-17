#!/usr/bin/env python3
"""Exact diagnostics and a rational certificate for an actual native twist peak.

No numerical test certifies the infinite hull/density theorems. The finite
arithmetic includes COMPLETE good squarefree ideal columns through norm 512,
and ALL ideal-generated sixth-power rows with generator ideal norm <=32.
That row set is a subset, not the full element ball of norm 32**6.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial, gcd, isqrt, lcm, log, pi
import json

COUNTS = Counter()
MUTATION = None

def require(value, group, detail=None):
    if not value:
        raise RuntimeError(f'{group}: {detail}')
    COUNTS[group] += 1

def primes(cap):
    s=bytearray(b'\1')*(cap+1)
    if cap>=0:s[0]=0
    if cap>=1:s[1]=0
    for p in range(2,isqrt(cap)+1):
        if s[p]:s[p*p:cap+1:p]=b'\0'*((cap-p*p)//p+1)
    return [p for p in range(2,cap+1) if s[p]]

def mul(x,y):
    a,b=x;c,d=y
    return a*c-b*d,a*d+b*c-b*d

def norm(x):
    a,b=x
    return a*a-a*b+b*b

def power(x,n):
    y=(1,0)
    while n:
        if n&1:y=mul(y,x)
        x=mul(x,x);n//=2
    return y

UNITS=((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1))

def canon(x):return min(mul(x,u) for u in UNITS)

def divides(p,x):
    a,b=p
    n=norm(p)
    v=mul(x,(a-b,-b))
    return v[0]%n==0 and v[1]%n==0

def divide(p,x):
    a,b=p;n=norm(p);v=mul(x,(a-b,-b))
    if v[0]%n or v[1]%n:raise ValueError('not divisible')
    return v[0]//n,v[1]//n

def lattice_ideals(cap):
    bound=2*isqrt(cap)+2
    return sorted({canon((a,b)) for a in range(-bound,bound+1)
                   for b in range(-bound,bound+1) if 0<norm((a,b))<=cap},key=lambda x:(norm(x),x))

def prime_ideals(cap):
    lat=lattice_ideals(cap);by_norm={}
    for a in lat:by_norm.setdefault(norm(a),[]).append(a)
    out=[]
    for p in primes(cap):
        if p==3:gens=by_norm.get(3,[]);f=1
        elif p%3==1:gens=by_norm.get(p,[]);f=1
        elif p*p<=cap:gens=[canon((p,0))];f=2
        else:continue
        expected=2 if p%3==1 else 1
        require(len(gens)==expected,'prime_splitting',(p,gens))
        for a in gens:out.append((p,p**f,f,a))
    return sorted(out,key=lambda t:(t[1],t[3]))

def native_columns(cap,ps):
    columns=[(1,1,(1,0),())]
    used_split=False
    for p,q,f,g in ps:
        if p in (2,3):continue
        if MUTATION=='collapse_conjugates' and p==7 and not used_split:
            used_split=True;continue
        columns += [(n*q,-sgn,mul(a,g),fac+(g,)) for n,sgn,a,fac in columns if n*q<=cap]
    return [(n,s,canon(a),f) for n,s,a,f in columns]

def classify_lattice_squarefree(cap,ps):
    good={}
    for a in lattice_ideals(cap):
        x=a;total=0;ok=True
        for p,q,f,g in ps:
            v=0
            while divides(g,x):
                x=divide(g,x);v+=1
            if v>1 or (v and p in (2,3)):ok=False
            total+=v
        require(norm(x)==1,'complete_prime_factorization',a)
        if ok:good[a]=(-1)**total
    return good

def phase_of_norm(n):
    phase=Q(0)
    for p in primes(n):
        e=0
        while n%p==0:n//=p;e+=1
        if e:
            if p%3==2:
                phase += Q(e,1 if MUTATION=='inert_phase' else 2)
            else:phase += e
    return phase

def pow_mod_ring(x,n,p):
    y=(1,0);x=(x[0]%p,x[1]%p)
    while n:
        if n&1:
            y=mul(y,x);y=(y[0]%p,y[1]%p)
        x=mul(x,x);x=(x[0]%p,x[1]%p);n//=2
    return y

def sixth_character_on_sixth_row(u,p,q,f,g):
    if f==1:
        root=next(r for r in range(p) if (r*r+r+1)%p==0 and (g[0]+g[1]*r)%p==0)
        v=(u[0]+u[1]*root)%p
        out=pow(v,(q-1)//6,p)
        require(out in (0,1),'sixth_power_split_value')
        return out
    out=pow_mod_ring(u,(q-1)//6,p)
    require(out in ((0,0),(1,0)),'sixth_power_inert_value')
    return int(out==(1,0))

def compatibility_tests():
    cases=0
    for size in (1,2,3):
        for fs in product(range(1,7),repeat=size):
            g=gcd(*fs) if size>1 else fs[0]
            criterion=all((f//g)%2 for f in fs)
            L=lcm(*fs)
            solutions=[h for h in range(2*L) if all((f*h-L)%(2*L)==0 for f in fs)]
            require(bool(solutions)==criterion,'residue_degree_criterion',fs)
            cases+=1
    require(not any((h-2)%4==0 and (2*h-2)%4==0 for h in range(4)),'non_galois_1_2_control')
    return cases

def fourier_tests():
    cases=0
    for M in range(1,9):
        coeff={h:Q(comb(2*M,M+h),4**M) for h in range(-M,M+1)}
        require(sum(coeff.values())==1,'bump_absolute_mass')
        require(coeff[0]>=Q(1,2*M+1),'bump_constant_lower_bound')
        for r in (1,2,3):
            direct=sum((__import__('functools').reduce(lambda a,h:a*coeff[h],hs,Q(1))
                        for hs in product(range(-M,M+1),repeat=r) if all(h==0 for h in hs)),Q(0))
            expected=coeff[0]**r
            require(direct==expected,'tensor_constant_coefficient')
            require(Q(2,8)*Q(1,2*M+1)**r==Q(1,4)*Q(1,2*M+1)**r,'effective_mean_error')
            cases+=1
    # All possible signed log frequencies for this finite primitive set.
    ps=(2,3,5)
    for hs in product(range(-3,4),repeat=3):
        a=b=1
        for p,h in zip(ps,hs):
            if h>=0:a*=p**h
            else:b*=p**(-h)
        require((a==b)==(hs==(0,0,0)),'integer_frequency_noncollision',hs)
        require(max(a,b)<=30**3,'integer_frequency_height')
        if a!=b:require(abs(a-b)>=1,'frequency_separation_integer_step')
    return cases

def arithmetic_tests():
    cap=512;ps=prime_ideals(cap)
    cols=native_columns(cap,ps)
    lat=classify_lattice_squarefree(cap,ps)
    require(len({a for _,_,a,_ in cols})==len(cols),'distinct_native_ideals')
    require({a:s for _,s,a,_ in cols}==lat,'complete_native_lattice_census')
    for n,s,a,fac in cols:
        require(norm(a)==n,'norm_matches_ideal')
        theta=phase_of_norm(n)
        require(theta.denominator==1 and (-1)**theta.numerator==s,'native_phase_alignment',(n,s,theta))
    rows=lattice_ideals(32);seen=set()
    good_ps=[x for x in ps if x[0] not in (2,3) and x[1]<=128]
    row_records=[]
    for b in rows:
        u=power(b,6)
        require(u not in seen,'sixth_row_injection',b);seen.add(u)
        require(norm(u)==norm(b)**6,'sixth_row_physical_norm')
        for e in UNITS:require(power(mul(b,e),6)==u,'unit_independent_sixth_row')
        values={}
        for p,q,f,g in good_ps:
            v=sixth_character_on_sixth_row(u,p,q,f,g)
            require(v==int(not divides(g,b)),'actual_nonunit_zero',(b,g))
            values[g]=v
        for n,sgn,a,fac in cols:
            if n>128:continue
            actual=1
            for g in fac:actual*=values[g]
            if MUTATION=='erase_mask':actual=1
            expected=int(all(not divides(g,b) for g in fac))
            require(actual==expected,'composite_sixth_row_mask',(b,a))
        row_records.append({'generator':list(b),'ideal_norm':norm(b),'row':list(u),'row_norm':norm(u)})
    jensen=[]
    for X,B,k in product((16,32,64,128,256),(4,8,16,32),(1,2,3)):
        bs=[b for b in rows if norm(b)<=B]
        ns=[c for c in cols if X/2<c[0]<=X]
        counts=[sum(all(not divides(g,b) for g in fac) for _,_,_,fac in ns) for b in bs]
        pairs=sum(counts);lhs=sum(v**(2*k) for v in counts)
        require(lhs*len(bs)**(2*k-1)>=pairs**(2*k),'exact_replica_jensen',(X,B,k))
        if k==1:jensen.append({'X':X,'B':B,'columns':len(ns),'sixth_rows':len(bs),'coprime_pairs':pairs})
    for q in (7,13,25,31,49):
        lhs=1-Q(1,q)+(1-Q(1,q))**2/q
        require(lhs==1-Q(2,q*q)+Q(1,q**3),'local_pair_density')
    window=Counter()
    for n,s,a,fac in cols:
        if 32<n<=64:window[n]+=s
    require(dict(window)=={37:-2,43:-2,49:1,61:-2},'complete_peak_window',dict(window))
    require(sum(window.values())==-5 and sum(abs(v) for v in window.values())==7,'native_and_unsigned_peak_values')
    require(Q(2)-Q(5,6)==Q(7,6),'physical_width_h1')
    require(Q(2)-Q(5,6)*Q(21,20)==Q(9,8),'physical_width_h21_20')
    return {'all_good_squarefree_ideals_through_512':len(cols),
            'all_ideal_generated_sixth_rows_through_generator_norm_32':len(rows),
            'row_records':row_records,'complete_rectangles':jensen}

# The interval endpoints below are exact rational numbers. Floating-point
# angle reduction selects an integer only; its validity is checked afterwards.
def floor_scaled(x,scale):return Q((x.numerator*scale)//x.denominator,scale)
def ceil_scaled(x,scale):return -floor_scaled(-x,scale)

def log_interval(n):
    if n<1:raise ValueError('positive integer required')
    a=n.bit_length()-1;unit=2**a
    def atanh_log(z):
        J=70;s=Q(0);v=z
        for j in range(J):s+=2*v/(2*j+1);v*=z*z
        tail=2*v/((2*J+1)*(1-z*z))
        return s,s+tail
    l2,u2=atanh_log(Q(1,3));l,u=atanh_log(Q(n-unit,n+unit))
    return floor_scaled(a*l2+l,10**50),ceil_scaled(a*u2+u,10**50)

def pi_interval():
    def atan_interval(d):
        J=70;x=Q(1,d);s=sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(J)),Q(0))
        nxt=(-1)**J*x**(2*J+1)/(2*J+1)
        return min(s,s+nxt),max(s,s+nxt)
    a,b=atan_interval(5);c,d=atan_interval(239)
    return floor_scaled(16*a-4*d,10**50),ceil_scaled(16*b-4*c,10**50)

def cos_interval(t,n,anchor):
    ln,un=log_interval(n);la,ua=log_interval(anchor)
    lo=t*(ln-ua);hi=t*(un-la)
    pl,pu=pi_interval()
    m=round(t*log(n/anchor)/(2*pi)) # selector, not a bound
    if m>=0:lo-=2*m*pu;hi-=2*m*pl
    else:lo-=2*m*pl;hi-=2*m*pu
    require(-4<lo<=hi<4,'certified_angle_reduction',(n,m))
    mid=(lo+hi)/2;rad=(hi-lo)/2;J=32
    s=sum(((-1)**j*mid**(2*j)/factorial(2*j) for j in range(J+1)),Q(0))
    err=abs(mid)**(2*J+2)/factorial(2*J+2)+rad
    return floor_scaled(s-err,10**38),ceil_scaled(s+err,10**38)

def decimal_bounds(lo,hi,digits=24):
    scale=10**digits
    def fmt(n):
        sign='-' if n<0 else '';n=abs(n)
        return f'{sign}{n//scale}.{n%scale:0{digits}d}'
    lower=(lo.numerator*scale)//lo.denominator
    upper=-((-hi.numerator*scale)//hi.denominator)
    return [fmt(lower),fmt(upper)]

def peak_certificate():
    t=0 if MUTATION=='fake_peak' else 842800609
    intervals=[cos_interval(t,n,49) for n in (37,43,61)]
    lo=1-2*sum(u for l,u in intervals)
    hi=1-2*sum(l for l,u in intervals)
    require(lo>Q(6999,1000),'rigorous_actual_native_peak',decimal_bounds(lo,hi))
    require(hi<7,'peak_below_unsigned_maximum')
    return {'twist_center_integer':t,'column_cap':64,'anchor_norm':49,
            'proven_real_part_interval':decimal_bounds(lo,hi),
            'threshold':'6999/1000','native_at_zero':-5,'unsigned_maximum':7,
            'method':'Exact Fraction logarithm/atan series, Machin pi, certified angle reduction, cosine Taylor remainder.'}

def main():
    c=compatibility_tests();f=fourier_tests();a=arithmetic_tests();p=peak_certificate()
    return {'status':'PASS: finite algebra, arithmetic, and rational peak certificate',
            'compatibility_cases':c,'finite_bump_cases':f,'arithmetic':a,'peak_certificate':p,
            'counts':dict(sorted(COUNTS.items())),'total_predicates':sum(COUNTS.values()),
            'limits':['Not a proof of an infinite asymptotic or RH.',
                      'The row set is the complete stated sixth-power subset, not a complete large physical ball.',
                      'The actual peak does not certify the whole prime-phase approximation box.',
                      'Same-author written proof and checker; no independent referee or proof assistant.']}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--mutation',choices=('inert_phase','collapse_conjugates','erase_mask','fake_peak'))
    args=parser.parse_args();MUTATION=args.mutation
    print(json.dumps(main(),sort_keys=True,indent=2))
