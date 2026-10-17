#!/usr/bin/env python3
"""Exact finite diagnostics, not certification of the infinite theorems.

The scalar native censuses contain all good squarefree Eisenstein ideals
under each stated norm cap. Formal local splitting tests use p=49 or 121
so odd-m critical coefficients are rational; these are algebra fixtures,
not claims that 49 and 121 are rational primes. No physical theta rows.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
from math import comb, gcd, isqrt, lcm
import json

CHECKS = Counter()
MUTATE = None

def require(ok: bool, group: str, detail: object = None) -> None:
    if not ok:
        raise RuntimeError(f'{group}: {detail}')
    CHECKS[group] += 1

def primes(n: int) -> list[int]:
    sieve = bytearray(b'\1') * (n + 1)
    sieve[:2] = b'\0\0'
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\0' * ((n-p*p)//p+1)
    return [i for i in range(2, n+1) if sieve[i]]

def compositions(total: int, slots: int):
    if slots == 1:
        yield (total,)
    else:
        for a in range(total + 1):
            for tail in compositions(total-a, slots-1):
                yield (a,) + tail

def conv(a, b, cap):
    out = [Q(0)] * (cap + 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[:cap-i+1]):
                if y:
                    out[i+j] += x*y
    return out

def local_majorant(p: int, degrees: tuple[int, ...], m: int, cap: int):
    b = [Q(1)] + [Q(0)]*cap
    for f in degrees:
        q = p**f
        root = isqrt(q)
        require(root*root == q, 'formal_square_norm')
        a = [Q(0)]*(cap+1)
        for j in range(cap//(m*f)+1):
            e = m*j*f
            a[e] += Q(1, q**j)
            if e+f <= cap:
                a[e+f] += Q(1, q**j*root)
        b = conv(b, a, cap)
    return b

def pmul(a, b, k: int, cap: int):
    out = defaultdict(Q)
    for x, c in a.items():
        for y, d in b.items():
            z = tuple(i+j for i,j in zip(x,y))
            if sum(z[:k]) <= cap and sum(z[k:]) <= cap:
                out[z] += c*d
    return {z:c for z,c in out.items() if c}

def pinv(v, k: int, cap: int):
    zero = (0,)*(2*k)
    tail = {z:-c for z,c in v.items() if z != zero}
    out = {zero:Q(1)}
    power = dict(out)
    for _ in range(cap):
        power = pmul(power, tail, k, cap)
        for z,c in power.items():
            out[z] = out.get(z,Q(0)) + c
    return {z:c for z,c in out.items() if c}

def local_tests():
    cases = 0
    for p, deg, m, k in product((49,121), ((1,1),(2,),(1,2),(1,1,1),(3,)), (2,3,4,6), (1,2)):
        cap = 4
        b = local_majorant(p,deg,m,cap)
        zero = (0,)*(2*k)
        qp = {}
        for e in range(cap+1):
            slots = list(compositions(e,k))
            for a in slots:
                ca = Q(1)
                for t in a: ca *= b[t]
                for d in slots:
                    cd = Q(1)
                    for t in d: cd *= b[t]
                    if ca*cd: qp[a+d] = ca*cd
        tensor = []
        for f in deg:
            for g in deg:
                tensor += [lcm(f,g)] * gcd(f,g)
        vp = {zero:Q(1)}
        for i,j,h in product(range(k),range(k),tensor):
            z = [0]*(2*k); z[i]=z[k+j]=h
            vp = pmul(vp,{zero:Q(1),tuple(z):-Q(1,p**h)},k,cap)
        if MUTATE == 'tensor':
            # Erase one true inverse degree-one contribution.
            z = [0]*(2*k); z[0]=z[k]=1
            vp[tuple(z)] = vp.get(tuple(z),Q(0)) + Q(1,p)
        hp = pmul(qp,vp,k,cap)
        require(pmul(hp,pinv(vp,k,cap),k,cap)==qp,'local_exact_factorization',(p,deg,m,k))
        for z,c in hp.items():
            require(sum(z[:k])==sum(z[k:]),'local_balance')
            require(sum(z[:k]) != 1,'cancelled_first_degree',(p,deg,m,k,z,c))
        for i,j in product(range(k),repeat=2):
            z=[0]*(2*k);z[i]=z[k+j]=1
            expected=Q(deg.count(1)**2,p)
            require(qp.get(tuple(z),Q(0))==expected,'tensor_degree_one')
        cases += 1
    return cases

def matrices(rows: tuple[int,...], cols: tuple[int,...]):
    k=len(rows); a=[0]*(k*k)
    def go(pos, rleft, cleft):
        if pos==k*k:
            yield tuple(a);return
        i,j=divmod(pos,k)
        for v in range(min(rleft[i],cleft[j])+1):
            a[pos]=v
            r=list(rleft);c=list(cleft);r[i]-=v;c[j]-=v
            yield from go(pos+1,tuple(r),tuple(c))
    yield from go(0,rows,cols)

def transport_tests():
    cap_sets=[(r,c) for r in product(range(4),repeat=2) for c in product(range(4),repeat=2)]
    cap_sets += [((v,)*3,(v,)*3) for v in range(4)]
    cap_sets += [((0,2,3),(1,1,3)),((3,2,1),(2,3,2))]
    cases=0; count=0
    for rows,cols in cap_sets:
        k=len(rows); seen=set(); by_delta=Counter()
        for a in matrices(rows,cols):
            s=sum(a)
            rd=tuple(rows[i]-sum(a[i*k:(i+1)*k]) for i in range(k))
            cd=tuple(cols[j]-sum(a[j::k]) for j in range(k))
            nw=tuple(a[i*k+j] for i in range(k-1) for j in range(k-1))
            key=(s,rd[:-1],cd[:-1],nw)
            if MUTATE=='dimension':key=(s,rd[:-1],cd[:-1])
            require(key not in seen,'transport_injection',(rows,cols,key))
            seen.add(key)
            d2=sum(rows)+sum(cols)-2*s
            require(d2>=0 and d2==sum(rd)+sum(cd),'transport_deficit')
            by_delta[d2]+=1;count+=1
        for d2,n in by_delta.items():
            upper=(1+max(rows+cols))**((k-1)**2)*(1+d2)**(2*k-2)
            require(n<=upper,'transport_count_bound',(rows,cols,d2,n,upper))
        cases+=1
    return {'caps':cases,'feasible_matrices':count}

def native_ideals(cap: int):
    ps=[]
    for p in primes(cap):
        if p in (2,3):continue
        if p%3==1:ps.extend([(p,f'{p}a'),(p,f'{p}b')])
        elif p*p<=cap:ps.append((p*p,f'{p}i'))
    ps.sort()
    ideals=[(1,1,())]
    for q,name in ps:
        ideals += [(n*q,-s,fac+(name,)) for n,s,fac in ideals if n*q<=cap]
    return ideals

def rational_native(cap: int):
    a=[0]*(cap+1);a[1]=1
    for p in primes(cap):
        if p in (2,3):continue
        terms=[(1,1)]
        if p%3==1:terms += [(p,-2),(p*p,1)]
        elif p*p<=cap:terms += [(p*p,-1 if MUTATE!='inert_sign' else 1)]
        out=[0]*(cap+1)
        for n,c in enumerate(a):
            if c:
                for q,v in terms:
                    if n*q<=cap:out[n*q]+=c*v
        a=out
    return a

def multiplicative_power(a: dict[int,int], k: int):
    b={1:1}
    for _ in range(k):
        out=defaultdict(int)
        for n,c in b.items():
            for m,d in a.items():out[n*m]+=c*d
        b=dict(out)
    return b

def native_tests():
    ideals=native_ideals(1024)
    fibers=defaultdict(list)
    for n,s,fac in ideals:fibers[n].append(s)
    a=rational_native(1024)
    for n in range(1,1025):
        vals=fibers.get(n,[])
        require(sum(vals)==a[n],'complete_native_fiber',(n,vals,a[n]))
        require(not vals or len(set(vals))==1,'norm_determines_sign',n)
        require(abs(a[n])==len(vals),'no_native_fiber_cancellation',n)
    reports=[]
    for x in (32,64,128,256,512,1024):
        c={n:a[n] for n in range(x//2+1,x+1) if a[n]}
        for k in ((1,2,3) if x<=128 else (1,2)):
            signed=multiplicative_power(c,k)
            absolute=multiplicative_power({n:abs(v) for n,v in c.items()},k)
            require({n:abs(v) for n,v in signed.items()}==absolute,'all_order_product_norm_sign',(x,k))
            diag=sum(v*v for v in signed.values())
            if x<=64:
                raw=defaultdict(int)
                selected=[(n,s) for n,s,_ in ideals if x/2<n<=x]
                for tup in product(selected,repeat=k):
                    n=s=1
                    for v,c0 in tup:n*=v;s*=c0
                    raw[n]+=s
                require(dict(raw)==signed,'direct_ideal_tuple_reconstruction',(x,k))
            reports.append({'X':x,'order':2*k,'ideals':sum(len(fibers.get(n,[])) for n in c),
                            'norms':len(c),'product_norms':len(signed),'norm_block':diag,
                            'principal_fixed_twist_moment':sum(c.values())**(2*k)})
    # The elementary lower-bound transport map with ALL coprime 2x2
    # arrays from a complete small set, not an asymptotic experiment.
    entries=(1,7,13,19,31,37)
    seen={}
    for a,b,c,d in product(entries,repeat=4):
        vals=(a,b,c,d)
        if any(gcd(vals[i],vals[j])!=1 for i in range(4) for j in range(i)):continue
        left=(a*b,c*d);right=(a*c,b*d)
        require((gcd(left[0],right[0]),gcd(left[0],right[1]),gcd(left[1],right[0]),gcd(left[1],right[1]))==vals,
                'coprime_transport_recovery')
        key=left+right
        require(key not in seen,'coprime_transport_injection');seen[key]=vals
    return {'cap':1024,'all_good_squarefree_ideals':len(ideals),'cases':reports,'coprime_transport_arrays':len(seen)}

def elementary_tests():
    # Exact lower bound e^2 > 7 from a finite positive Taylor sum.
    term=Q(1);s=term
    for j in range(1,6):term*=Q(2,j);s+=term
    require(s>7,'gaussian_gram_rational_constant')
    # Audit every possible local supported degree at split/inert primes,
    # including exponents beyond squarefree PRODUCT ideals.
    for f in (1,2):
        for k in range(1,5):
            options=list(product((0,1),repeat=k*(2 if f==1 else 1)))
            for a,b in product(options,repeat=2):
                ea=f*sum(a);eb=f*sum(b)
                if ea==eb:require((-1)**(sum(a)+sum(b))==1,'local_native_tuple_sign')
    # Lower-box lattice variation is constructed independently of the
    # upper-box enumerator. Every perturbed matrix retains its margins.
    for k in (2,3):
        L=1000
        base=[[L//k+int((j-i)%k<L%k) for j in range(k)] for i in range(k)]
        for v in product((-1,0,1),repeat=(k-1)**2):
            a=[r[:] for r in base]
            for i,j in product(range(k-1),repeat=2):a[i][j]+=v[i*(k-1)+j]
            for i in range(k-1):a[i][-1]=L-sum(a[i][:-1])
            for j in range(k-1):a[-1][j]=L-sum(a[i][j] for i in range(k-1))
            a[-1][-1]=L-sum(a[-1][:-1])
            require(all(sum(r)==L for r in a) and all(sum(a[i][j] for i in range(k))==L for j in range(k)),
                    'lower_box_margins')
            require(all(L/(2*k)<=x<=2*L/k for row in a for x in row),'lower_box_interior')

def main():
    global MUTATE
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mutate',choices=('tensor','dimension','inert_sign'))
    args=parser.parse_args();MUTATE=args.mutate
    local=local_tests(); transport=transport_tests(); native=native_tests(); elementary_tests()
    result={'status':'PASS','scope':'Exact finite algebra and native principal arithmetic; not analytic certification.',
            'local_cases':local,'transport':transport,'native':native,'predicates':dict(sorted(CHECKS.items())),
            'total_predicates':sum(CHECKS.values())}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
