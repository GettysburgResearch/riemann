#!/usr/bin/env python3
"""Exact finite diagnostics; not proofs of asymptotic moment inequalities.

Standard library only. All mathematical comparisons use fractions.Fraction.
The function require remains active under python -O.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json
from math import isqrt
from pathlib import Path

COUNTS: Counter[str] = Counter()


def require(value: bool, group: str) -> None:
    COUNTS[group] += 1
    if not value:
        raise ArithmeticError(f"Failed exact predicate: {group}")


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b'\x01') * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            for j in range(p*p, n+1, p):
                sieve[j] = 0
    return [p for p in range(2, n+1) if sieve[p]]


def prime_ideals(bound: int) -> list[tuple[str, int]]:
    out: list[tuple[str, int]] = []
    for p in primes_upto(bound):
        if p == 3:
            out.append(('3r', 3))
        elif p % 3 == 1:
            out.extend([(f'{p}a', p), (f'{p}b', p)])
        elif p*p <= bound:
            out.append((f'{p}i', p*p))
    return sorted(out, key=lambda z: (z[1], z[0]))


def ideals_upto(bound: int, ps: list[tuple[str, int]]):
    """Distinct prime ideals are never coalesced by their equal norms."""
    ideals = [(1, ())]
    for label, q in ps:
        old = list(ideals)
        for n, fac in old:
            v, e = n*q, 1
            while v <= bound:
                ideals.append((v, fac + ((label, e),)))
                v *= q
                e += 1
    return sorted(ideals)


def support(fac) -> frozenset[str]:
    return frozenset(p for p, _ in fac)


def mobius_table(n: int) -> list[int]:
    mu = [1]*(n+1)
    mu[0] = 0
    for p in primes_upto(n):
        for m in range(p, n+1, p):
            mu[m] = -mu[m]
        for m in range(p*p, n+1, p*p):
            mu[m] = 0
    return mu


def mertens(n: int) -> list[Q]:
    mu = mobius_table(n)
    vals = [Q(0)]
    for j in range(1, n+1):
        vals.append(vals[-1]+mu[j])
    return vals


def geometric_action(f: list[Q], q: int, ratio: Q=Q(1)) -> list[Q]:
    """sum_{j>=1} ratio^(j-1) S_q^j f, exactly at all integer horizons."""
    d = len(f)-1
    out = [Q(0)]*(d+1)
    power, weight = q, Q(1)
    while power <= d:
        for n in range(power, d+1):
            out[n] += weight*f[n//power]
        power *= q
        weight *= ratio
    return out


def plus(f: list[Q], g: list[Q], weight: Q=Q(1)) -> list[Q]:
    return [a+weight*b for a,b in zip(f,g)]


def mean_action(f: list[Q], ps) -> list[Q]:
    out = f[:]
    for _, q in ps:
        out = plus(out, geometric_action(out,q), Q(1,q))
    return out


def inverse_mean(f: list[Q], ps) -> list[Q]:
    out = f[:]
    for _, q in ps:
        out = plus(out, geometric_action(out,q,Q(q-1,q)), -Q(1,q))
    return out


def replica_action(f: list[Q], ps, bits) -> list[Q]:
    out = f[:]
    for (_,q), bit in zip(ps,bits):
        if bit:
            out = plus(out, geometric_action(out,q))
    return out


def mask_probability(ps, bits) -> Q:
    out = Q(1)
    for (_,q), bit in zip(ps,bits):
        out *= Q(1,q) if bit else Q(q-1,q)
    return out


def exact_density_moments():
    b = 512
    ps = prime_ideals(b)
    norms = dict(ps)
    ideals = ideals_upto(b,ps)
    multiplicities = Counter(n for n,_ in ideals)
    for n in range(1,b+1):
        ak = sum(0 if d%3 == 0 else (1 if d%3 == 1 else -1)
                 for d in range(1,n+1) if n%d == 0)
        require(multiplicities[n] == ak,'Eisenstein_ideal_count_by_norm')
    qset = {'3r'}
    d = 24
    f = mertens(d)
    columns = [(n,support(fac),f[d//n]) for n,fac in ideals
               if n<=d and not support(fac)&qset]
    active = [(label,q) for label,q in ps if q<=d and label not in qset]
    model = []
    for bits in product((0,1),repeat=len(active)):
        chosen = {p for (p,_),bit in zip(active,bits) if bit}
        val = sum((a for _,s,a in columns if s<=chosen),Q(0))
        model.append((mask_probability(active,bits),val))
    require(sum(p for p,_ in model)==1,'model_probability_total')
    rads: dict[frozenset[str],int] = {}
    diagnostics = []
    for y in (16,32,64,128,512):
        ws = [support(fac) for n,fac in ideals if y<2*n and n<=y and not support(fac)&qset]
        j = len(ws)
        require(j>0,'nonempty_physical_annulus')
        actual = [sum((a for _,s,a in columns if s<=w),Q(0)) for w in ws]
        probabilities = {}
        def prob(s):
            if s not in probabilities:
                probabilities[s] = Q(sum(s<=w for w in ws),j)
            return probabilities[s]
        row = {'D':d,'Y':y,'base_count':j,'moments':{}}
        for r in range(1,5):
            physical = sum((v**r for v in actual),Q(0))/j
            independent = sum((p*v**r for p,v in model),Q(0))
            exp_ph,exp_in,defect = Q(0),Q(0),Q(0)
            for terms in product(columns,repeat=r):
                s = frozenset().union(*(t[1] for t in terms))
                if s not in rads:
                    rad = 1
                    for label in s:
                        rad *= norms[label]
                    rads[s]=rad
                rad = rads[s]
                a=Q(1)
                for _,_,v in terms:
                    a*=v
                pa=prob(s)
                exp_ph+=a*pa
                exp_in+=a/rad
                defect+=a*(pa-Q(1,rad))
                if rad>y:
                    require(pa==0,'high_radical_physical_probability_zero')
            require(physical==exp_ph,'physical_joint_moment_expansion')
            require(independent==exp_in,'independent_joint_moment_expansion')
            require(physical-independent==defect,'exact_r_linear_discrepancy')
            row['moments'][str(r)]={'physical':str(physical),'model':str(independent),'defect':str(defect)}
        # Check the literal counting formula using the same full ideal set.
        for s,pa in probabilities.items():
            rad=rads[s]
            num=sum(y<2*rad*n and rad*n<=y and not support(fac)&qset for n,fac in ideals)
            require(pa==Q(num,j),'annulus_divisibility_count_identity')
        diagnostics.append(row)
    require(any('a' in p for p in norms if norms[p]==7) and sum(q==7 for _,q in ps)==2,
            'split_prime_norms_kept_separate')
    return diagnostics


def orthogonal_identities():
    ps=[('2i',4),('7a',7),('7b',7),('13a',13)]
    d=256
    functions={'Mertens':mertens(d),
               'positive_growth':[Q(n) for n in range(d+1)],
               'signed_rational':[Q(0)]+[Q((-1)**n*(n%7),n%5+1) for n in range(1,d+1)]}
    selected=(7,16,28,49,64,91,196,256)
    result={}
    for name,f in functions.items():
        mg=mean_action(inverse_mean(f,ps),ps)
        for n in range(d+1):
            require(mg[n]==f[n],'causal_mean_inverse')
        features={}
        for subset in product((0,1),repeat=len(ps)):
            g=f[:]
            var=Q(1)
            for (_,q),bit in zip(ps,subset):
                if bit:
                    g=geometric_action(g,q,Q(q-1,q))
                    var*=Q(q-1,q*q)
            features[subset]=(g,var)
        moments={n:[Q(0),Q(0),Q(0)] for n in selected}
        for bits in product((0,1),repeat=len(ps)):
            prob=mask_probability(ps,bits)
            c=inverse_mean(replica_action(f,ps,bits),ps)
            expansion=[Q(0)]*(d+1)
            for subset,(g,_) in features.items():
                weight=Q(1)
                for (_,q),inc,bit in zip(ps,subset,bits):
                    if inc:
                        weight*=Q(bit)-Q(1,q)
                for n in range(d+1):
                    expansion[n]+=weight*g[n]
            for n in range(d+1):
                require(c[n]==expansion[n],'centered_operator_factorization')
            for n in selected:
                moments[n][0]+=prob*c[n]
                moments[n][1]+=prob*c[n]**2
                moments[n][2]+=prob*c[n]**4
        for n in selected:
            energy=sum((v*g[n]**2 for g,v in features.values()),Q(0))
            require(moments[n][0]==f[n],'coherent_mean_exact')
            require(moments[n][1]==energy,'orthogonal_energy_exact')
            require(moments[n][2]>=f[n]**4,'Jensen_fourth_moment_lower_bound')
        # Verify all orthogonal basis pairings, including same-norm prime ideals.
        keys=list(features)
        for a in keys:
            for b in keys:
                av=Q(0)
                for bits in product((0,1),repeat=len(ps)):
                    term=mask_probability(ps,bits)
                    for (_,q),ia,ib,x in zip(ps,a,b,bits):
                        if ia:term*=Q(x)-Q(1,q)
                        if ib:term*=Q(x)-Q(1,q)
                    av+=term
                expected=features[a][1] if a==b else Q(0)
                require(av==expected,'Bernoulli_basis_orthogonality')
        result[name]={'D':d,'mean':str(moments[d][0]),
                      'second_moment':str(moments[d][1]),
                      'coherent_square':str(f[d]**2),
                      'innovation_energy':str(moments[d][1]-f[d]**2),
                      'fourth_moment':str(moments[d][2])}
    # The two 7-ideal masks must not be identified: selecting just one contributes
    # I+R_7; selecting both contributes (I+R_7)^2, different on a genuine source.
    f=functions['positive_growth']
    once=replica_action(f,ps,(0,1,0,0))
    twice=replica_action(f,ps,(0,1,1,0))
    require(once[49]!=twice[49],'reject_collapsed_equal_norm_masks')
    # Repeated powers of the SAME ideal do not introduce independent masks.
    require(Q(1,4)!=Q(1,4)**2,'reject_independent_prime_power_masks')
    return result


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    data={'scope':'exact finite algebra only; no asymptotic or RH verification',
          'arithmetic':'fractions.Fraction; explicit predicates active under -O',
          'density_diagnostics':exact_density_moments(),
          'finite_prime_decomposition':orthogonal_identities()}
    data['predicate_counts']=dict(sorted(COUNTS.items()))
    data['total_exact_predicates']=sum(COUNTS.values())
    text=json.dumps(data,sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    else:
        print(text,end='')


if __name__=='__main__':
    main()
