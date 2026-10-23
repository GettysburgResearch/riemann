#!/usr/bin/env python3
"""Exact local oldform Fourier identities; not an analytic theorem checker."""
from fractions import Fraction as F
from itertools import product
from math import prod
import json


def demand(ok, name):
    if not ok:
        raise RuntimeError(name)


def aa(v, x):
    if v < 0:
        return F(0)
    return sum(x ** (v-2*j) for j in range(v+1))


def local(v, q, x):
    return (q*aa(v-2, x)-aa(v-1, x)/x)/(q*x*x-1)


def mu(m):
    return (-1)**m.bit_count()


def main():
    checks=0
    qs=[5,9,13]
    masks=range(8)
    norms={m:prod(q for i,q in enumerate(qs) if m>>i&1) for m in masks}
    for l in masks:
        demand(sum(mu(d)*mu(e) for d in masks for e in masks if d|e==l)
               ==mu(l), "complete lcm Mobius convolution")
        checks+=1
    for xs in product([F(1,2),F(1),F(2)],repeat=3):
        for vals in product(range(4),repeat=3):
            # Two independent descriptions: the full e|d oldform expansion,
            # and the product of one-prime Fourier recurrences.
            direct={}
            for d in masks:
                result=F(0)
                for e in masks:
                    if e & d != e:
                        continue
                    rem=[v-(2-((e>>i)&1) if d>>i&1 else 0)
                         for i,v in enumerate(vals)]
                    if min(rem)<0:
                        continue
                    factor=F(mu(e))
                    for i,(q,x,v) in enumerate(zip(qs,xs,rem)):
                        factor*=aa(v,x)
                        if d>>i&1:
                            # e=1: -x^-1; e=0: q. The sign is in mu(e).
                            factor*=(1/x if e>>i&1 else q)/(q*x*x-1)
                    result+=factor
                direct[d]=result
                via_local=prod(local(v,q,x) if d>>i&1 else aa(v,x)
                               for i,(q,x,v) in enumerate(zip(qs,xs,vals)))
                demand(result==via_local,"complete divisor expansion")
                if any(d>>i&1 and vals[i]==0 for i in range(3)):
                    demand(result==0,"literal d divides k support")
                    checks+=1
                checks+=1
            for cutoff in [1,5,9,13,45,65,117,585]:
                active=[d for d in masks if norms[d]<=cutoff]
                grouped={l:0 for l in masks}
                pair_sum=F(0)
                for d in active:
                    for e in active:
                        grouped[d|e]+=mu(d)*mu(e)
                        pair_sum+=mu(d)*mu(e)*direct[d|e]
                demand(pair_sum==sum(grouped[l]*direct[l] for l in masks),
                       "quadratic section retains all cross terms")
                demand(all(abs(grouped[l])<=3**l.bit_count() for l in masks),
                       "three-choice local coefficient bound")
                checks+=2
                cutoff_linear=sum(mu(d)*direct[d] for d in active)
                full_linear=sum(mu(d)*direct[d] for d in masks)
                demand(all(abs(grouped[l]-(mu(l) if l in active else 0))
                           <=4**l.bit_count() for l in masks),
                       "four-choice finite-difference bound")
                demand(all(abs(grouped[l]-mu(l))<=4**l.bit_count()
                           for l in masks), "four-choice limit-difference bound")
                checks+=2
                support_radical=sum(1<<i for i,v in enumerate(vals) if v)
                if norms[support_radical]<=cutoff:
                    demand(pair_sum==cutoff_linear==full_linear,
                           "exact low-frequency agreement")
                    checks+=1
    print(json.dumps({"arithmetic":"EXACT_RATIONAL","checks":checks,
                      "analytic_certification":False,
                      "prime_norms":qs,"local_spectral_parameters":["1/2","1","2"],
                      "valuation_range":[0,3],"cutoffs":[1,5,9,13,45,65,117,585]},
                     indent=2,sort_keys=True))


if __name__=="__main__":
    main()
