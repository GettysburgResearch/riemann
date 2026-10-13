#!/usr/bin/env python3
"""Finite exact identities, not evidence for the open asymptotic estimate.

The native test uses ALL squarefree columns below the indicated cap SUPPORTED
ON five named prime ideals. It does not use all Eisenstein ideals below that cap.
All predicates remain active with python -O. Standard library only.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb
import json

COUNTS: Counter[str] = Counter()

def require(test: bool, label: str) -> None:
    COUNTS[label] += 1
    if not test:
        raise ArithmeticError(label)

# Z[omega], omega^2+omega+1=0. 1+omega is a primitive sixth root.
def add(x, y): return (x[0]+y[0], x[1]+y[1])
def scale(x, n): return (x[0]*n, x[1]*n)
def mul(x, y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c-b*d)
def conj(x): return (x[0]-x[1], -x[1])
def norm(x): return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def fpow(x, n, modulus):
    r=(1,0)
    while n:
        if n&1:
            r=tuple(a%modulus for a in mul(r,x))
        x=tuple(a%modulus for a in mul(x,x)); n//=2
    return r
ROOTS=[(1,0)]
for _ in range(5): ROOTS.append(mul(ROOTS[-1],(1,1)))
# (label, norm, underlying characteristic, omega residue if split)
PRIMES=[('7a',7,7,2),('7b',7,7,4),('13a',13,13,3),('13b',13,13,9),('5i',25,5,None)]

def symbol(u, p):
    _,q,ell,r=p
    if r is not None:
        x=(u[0]+r*u[1])%ell
        if x==0: return (0,0)
        value=pow(x,(q-1)//6,ell)
        for j,z in enumerate(ROOTS):
            if (z[0]+r*z[1])%ell==value: return ROOTS[j]
    else:
        x=tuple(a%ell for a in u)
        if x==(0,0): return (0,0)
        value=fpow(x,(q-1)//6,ell)
        for z in ROOTS:
            if tuple(a%ell for a in z)==value: return z
    raise ArithmeticError('symbol_not_sixth_root')

def columns(X, excluded=0):
    result=[]
    for mask in range(1<<len(PRIMES)):
        if mask&excluded: continue
        n=1
        for j,p in enumerate(PRIMES):
            if mask>>j&1: n*=p[1]
        if n<=X: result.append((n,mask))
    return result

def key_of(t, k, extra_left=None):
    counts=[0]*len(PRIMES); charge=[0]*len(PRIMES)
    for i,(_,m) in enumerate(t):
        for j in range(len(PRIMES)):
            if m>>j&1:
                counts[j]+=1; charge[j]+=(1 if i<k else -1)
    sign=(-1)**sum(counts)
    if extra_left is not None:
        counts[extra_left]+=1; charge[extra_left]+=1
    support=sum((1<<j) for j,c in enumerate(counts) if c)
    return counts,(tuple(c%6 for c in charge),support),sign

def clean(c): return Counter({a:b for a,b in c.items() if b})
def cadd(a,b,factor=1):
    r=a.copy()
    for x,n in b.items(): r[x]+=factor*n
    return clean(r)
def counter_conj(c):
    r=Counter()
    for (exps,mask),n in c.items(): r[(tuple(-e%6 for e in exps),mask)]+=n
    return clean(r)

def eval_counter(c, u):
    chars=[symbol(u,p) for p in PRIMES]
    powers=[]
    for ch in chars:
        pw=[(1,0)]
        for _ in range(5): pw.append(mul(pw[-1],ch))
        powers.append(pw)
    out=(0,0)
    for (exps,mask),n in c.items():
        if any(mask>>j&1 and chars[j]==(0,0) for j in range(len(PRIMES))): continue
        val=(1,0)
        for j,e in enumerate(exps): val=mul(val,powers[j][e])
        out=add(out,scale(val,n))
    return out

def polynomial(cols,u):
    chars=[symbol(u,p) for p in PRIMES]
    result=(0,0)
    for _,m in cols:
        z=(((-1)**m.bit_count()),0)
        for j,ch in enumerate(chars):
            if m>>j&1: z=mul(z,ch)
        result=add(result,z)
    return result

def tuple_counters(X,k,y,excluded=0):
    cols=columns(X,excluded)
    full=Counter(); selected=Counter(); residual=Counter(); parity=Counter()
    abs_by_mask=Counter()
    for t in product(cols,repeat=2*k):
        counts,key,sgn=key_of(t,k)
        full[key]+=sgn
        if all(c!=1 or PRIMES[j][1]<=y for j,c in enumerate(counts)):
            selected[key]+=sgn; abs_by_mask[key[1]]+=1
        # Earlier projection domains, for exact comparison only.
        if all(e==0 or PRIMES[j][1]<=y for j,e in enumerate(key[0])): residual[key]+=sgn
        if all(c%2==0 or PRIMES[j][1]<=y for j,c in enumerate(counts)): parity[key]+=sgn
    return cols,clean(full),clean(selected),clean(residual),clean(parity),abs_by_mask

def rooted_counter(X,k,y,excluded=0,drop_exclusion=False):
    gamma=Counter()
    for j,p in enumerate(PRIMES):
        if p[1]<=y or excluded>>j&1: continue
        ex=excluded if drop_exclusion else excluded|(1<<j)
        short=columns(X//p[1],ex); others=columns(X,ex)
        for m in short:
            for tail in product(others,repeat=2*k-1):
                t=(m,)+tail
                counts,key,sgn=key_of(t,k,extra_left=j)
                if any(counts[z]==1 for z in range(j+1,len(PRIMES))): continue
                gamma[key]+=sgn
    return clean(gamma)

def local_tests():
    for k in range(1,41):
        coefficients=[comb(2*k,j) if j!=1 else 0 for j in range(2*k+1)]
        require(coefficients[2]==k*(2*k-1),'quadratic_local_coefficient')
        for den in (2,3,5,11,97):
            r=Fraction(1,den)
            v=sum(c*r**j for j,c in enumerate(coefficients))
            require(v==(1+r)**(2*k)-2*k*r,'local_factor_identity')
            # Finite rational version of the exponential-tail bound, r<=1/(2k).
            if 2*k*r<=1:
                require(v-1<=Fraction(3,2)*(2*k*r)**2,'uniform_local_quadratic_bound')
    # Strictly larger sector: (p*q,p;p,1), q=7a, p=13a.
    t=((91,(1<<0)|(1<<2)),(13,1<<2),(13,1<<2),(1,0))
    counts,key,_=key_of(t,2)
    require(all(c!=1 or PRIMES[j][1]<=7 for j,c in enumerate(counts)), 'strict_enlargement_new_sector')
    require(not all(e==0 or PRIMES[j][1]<=7 for j,e in enumerate(key[0])), 'strict_enlargement_not_sextic_projection')
    require(not all(c%2==0 or PRIMES[j][1]<=7 for j,c in enumerate(counts)), 'strict_enlargement_not_sign_projection')
    require(any(c==1 for c in counts),'strict_enlargement_not_global_no_singletons')
    # Every subset with no singleton contains all allowed character/parity subsets.
    for k in range(1,9):
        for a in range(k+1):
            for b in range(k+1):
                if (a-b)%6==0: require(a+b!=1,'sextic_domain_inclusion')
                if (a+b)%2==0: require(a+b!=1,'parity_domain_inclusion')

def arithmetic_tests():
    rows=sorted((a,b) for a in range(-5,6) for b in range(-5,6) if 0<norm((a,b))<=13)
    require(len(rows)==54,'all_element_rows_norm_13')
    for u in rows:
        for p in PRIMES:
            ch=symbol(u,p)
            require(ch==(0,0) or norm(ch)==1,'literal_nonunit_or_unit')
            # Exact multiplicativity with every other tested row.
            for v in rows:
                require(symbol(mul(u,v),p)==mul(ch,symbol(v,p)), 'actual_local_symbol_multiplicativity')
    diagnostics=[]
    masks=(0,1<<0,(1<<0)|(1<<3))
    for X,k in ((25,1),(25,2),(25,3),(91,2)):
        for ex in masks:
            for y in (0,7,13,25):
                cols,full,E,R6,parity,absolute=tuple_counters(X,k,y,ex)
                gamma=rooted_counter(X,k,y,ex)
                root=cadd(gamma,counter_conj(gamma))
                root=Counter({key:-k*n for key,n in root.items()})
                require(cadd(E,root)==full,'largest_singleton_symbolic_identity')
                active_rows=rows if X==25 else rows[::6]
                totals={'native':0,'selected':0,'sextic_projection':0,'sign_projection':0,'rooted_remainder':0}
                for u in active_rows:
                    actual=norm(polynomial(cols,u))**k
                    ev=eval_counter(E,u); fv=eval_counter(full,u); rv=eval_counter(root,u)
                    require(fv==(actual,0),'full_actual_native_moment')
                    require(ev[1]==0 and rv[1]==0,'selected_and_rooted_real')
                    require(add(ev,rv)==fv,'actual_row_root_identity')
                    forbidden=sum(1<<j for j,p in enumerate(PRIMES) if symbol(u,p)==(0,0))
                    bound=sum(v for m,v in absolute.items() if not m&forbidden)
                    require(abs(ev[0])<=bound,'absolute_selected_majorant')
                    totals['native']+=actual; totals['selected']+=ev[0]
                    totals['sextic_projection']+=eval_counter(R6,u)[0]
                    totals['sign_projection']+=eval_counter(parity,u)[0]
                    totals['rooted_remainder']+=rv[0]
                diagnostics.append({'X':X,'k':k,'y':y,'excluded_mask':ex,'columns':len(cols),'rows':len(active_rows),**totals})
    # Three false substitutions must differ from the correct finite polynomial.
    cols,full,E,_,_,_=tuple_counters(91,2,7)
    gamma=rooted_counter(91,2,7)
    plus=cadd(gamma,counter_conj(gamma))
    wrong_sign=Counter({a:2*b for a,b in plus.items()})
    require(cadd(E,wrong_sign)!=full,'negative_control_wrong_mobius_root_sign')
    bad=rooted_counter(91,2,7,drop_exclusion=True)
    bad=Counter({a:-2*b for a,b in cadd(bad,counter_conj(bad)).items()})
    require(cadd(E,bad)!=full,'negative_control_dropped_prime_exclusion')
    require(symbol((2,0),PRIMES[0])!=symbol((2,0),PRIMES[1]),'negative_control_equal_norm_primes_not_identical')
    # With an all-principal charge, the support still deletes nonunit rows.
    support_key=((0,0,0,0,0),1<<0)
    require(eval_counter(Counter({support_key:1}),(7,0))==(0,0),'negative_control_charge_zero_does_not_erase_mask')
    return diagnostics

def main():
    local_tests(); diagnostics=arithmetic_tests()
    print(json.dumps({'scope':'Exact finite algebra only; not an asymptotic moment experiment.',
      'columns':'All squarefree products below X of ONLY 7a,7b,13a,13b,5i; no claim of all native columns.',
      'arithmetic':'Integer pairs in Z[omega] and fractions.Fraction; active under -O.',
      'predicate_counts':dict(sorted(COUNTS.items())), 'total_predicates':sum(COUNTS.values()),
      'diagnostics':diagnostics},indent=2,sort_keys=True))
if __name__=='__main__': main()
