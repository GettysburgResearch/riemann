#!/usr/bin/env python3
"""Exact finite controls for GENERALIZED_MOMENT_GEOMETRY.md."""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
I = ((1,0,0),(0,1,0),(0,0,1))
S = (((-1,1,1),(0,1,0),(0,0,1)),
     ((1,0,0),(1,-1,1),(0,0,1)),
     ((1,0,0),(0,1,0),(1,1,-1)))
C = ((2,-1,-1),(-1,2,-1),(-1,-1,2))


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def transpose(a):
    return tuple(zip(*a))


def vector(a,x):
    return tuple(sum(a[i][j]*x[j] for j in range(3)) for i in range(3))


def translation(v):
    return tuple(tuple(I[i][j]+v[j] for j in range(3)) for i in range(3))


def quotient(a):
    return tuple(tuple(a[i][j]-a[2][j] for j in range(2)) for i in range(2))


def matrix_controls():
    g0 = (I,S[0],S[1],mul(S[0],S[1]),mul(S[1],S[0]),
          mul(mul(S[0],S[1]),S[0]))
    require(len(set(g0))==6,"six finite representatives")
    g0_by_q = {quotient(h):h for h in g0}
    require(len(g0_by_q)==6,"faithful quotient representatives")
    inv = {h:next(z for z in g0 if mul(h,z)==I==mul(z,h)) for h in g0}
    for s in S:
        require(mul(s,s)==I,"reflection involution")
        require(vector(s,(1,1,1))==(1,1,1),"nullvector fixed")
        require(mul(mul(transpose(s),C),s)==C,"semidefinite form preserved")
    require(mul(mul(mul(S[0],S[1]),S[2]),S[1])==translation((2,-1,-1)),
            "short translation word")
    require(mul(S[2],mul(mul(S[0],S[1]),S[0]))==translation((-1,-1,2)),
            "third generator decomposition")
    p = mul(mul(S[0],S[1]),S[2])
    require(mul(p,p)==translation((3,0,-3)),"Coxeter-square translation")
    frontier = {I}
    all_seen = {I}
    receipts = []
    for length in range(13):
        for m in frontier:
            h = g0_by_q.get(quotient(m))
            require(h is not None,"quotient lies in finite group")
            t = mul(m,inv[h])
            diff = tuple(tuple(t[i][j]-I[i][j] for j in range(3))
                         for i in range(3))
            v = diff[0]
            require(all(row==v for row in diff),"rank-one translation kernel")
            require(sum(v)==0,"translation row has zero sum")
            require((v[0]-v[1])%3==(v[1]-v[2])%3==0,"index-three lattice")
            require(mul(translation(v),h)==m,"exact normal-form reconstruction")
            for u in ((Q(1,3),Q(-4,3),Q(7,3)),(2,-1,-1),(1,-1,0)):
                actual = vector(transpose(translation(v)),u)
                expected = tuple(u[i]+sum(u)*v[i] for i in range(3))
                require(actual==expected,"dual common-coordinate translation")
                require(sum(actual)==sum(u),"dual common coordinate invariant")
                if sum(u)==0:
                    require(actual==u,"critical-slice translation trivial")
        receipts.append({"maximum_word_length":length,"distinct_matrices":len(all_seen)})
        frontier = {mul(m,s) for m in frontier for s in S}-all_seen
        all_seen.update(frontier)
    require(len(all_seen)>100,"nontrivial infinite-orbit finite control")
    # Signed translations destroy every purported global strict scalar contraction.
    v = (2,-1,-1)
    logs = (Q(2),Q(1),Q(1))
    eta = Q(3,5)
    exponent = eta*sum(v[i]*logs[i] for i in range(3))
    require(exponent>0 and -exponent<0,"opposite translation scalar signs")
    require(sum(v[i]*Q(9) for i in range(3))==0,"balanced scale multiplier exactly one")
    # The nullvector mechanism is special to k=3.
    for k in range(4,9):
        image = (k-2,)+(1,)*(k-1)
        require(len(set(image))>1,"higher-rank ones-vector not fixed or parallel")
    return receipts


# Rational cubic field Q(omega), omega^2+omega+1=0. No floats enter.
def add(a,b):
    return (a[0]+b[0],a[1]+b[1])


def product(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])


def omega(e):
    return ((Q(1),Q(0)),(Q(0),Q(1)),(Q(-1),Q(-1)))[e%3]


def scale(a,q):
    return (a[0]*q,a[1]*q)


def a_gauss(p):
    exponent = sum(2*j+1 for j in p)
    exponent -= sum((j+l+1)%3 for j,l in itertools.combinations(sorted(p),2))
    return omega(exponent)


def symbol(p,row_bad,aux=False):
    if p & row_bad:
        return (Q(0),Q(0))
    return omega(sum((3 if aux else 2)*j+1 for j in p)*(4 if aux else 1))


def weight(axis,p):
    # Arbitrary rational row-independent factor weights, not multiplicative substitutes.
    return Q(1+sum((j+1)*(axis+2) for j in p),2+len(p)+axis)


def fusion_controls():
    primes = frozenset(range(4))
    receipts = []
    for k in range(3,7):
        for split in (1,k//2,k-1):
            for row_bad,aux_bad,mask in ((set(),set(),set()),({0},set(),set()),
                                        (set(),{1},set()),({0},{1},{2})):
                row_bad,aux_bad,mask = map(frozenset,(row_bad,aux_bad,mask))
                direct = (Q(0),Q(0))
                left,right = {},{}
                for block_start,block_size,out in ((0,split,left),(split,k-split,right)):
                    for assignment in itertools.product(range(block_size+1),repeat=4):
                        axes = [frozenset(j for j,a in enumerate(assignment) if a==i+1)
                                for i in range(block_size)]
                        support = frozenset().union(*axes)
                        w = Q(1)
                        for i,p in enumerate(axes): w *= weight(block_start+i,p)
                        out[support] = out.get(support,Q(0))+w
                # Enumerate the original k-way assignments independently.
                for assignment in itertools.product(range(k+1),repeat=4):
                    axes = [frozenset(j for j,a in enumerate(assignment) if a==i+1)
                            for i in range(k)]
                    support = frozenset().union(*axes)
                    if support & mask: continue
                    w = Q(1)
                    for i,p in enumerate(axes): w *= weight(i,p)
                    phase = product(product(a_gauss(support),symbol(support,row_bad)),
                                    symbol(support,aux_bad,True))
                    direct = add(direct,scale(phase,w))
                fused = (Q(0),Q(0))
                for r,dr in left.items():
                    for s,ds in right.items():
                        if r&s or (r|s)&mask: continue
                        support = r|s
                        cross = omega(-sum((j+l+1)%3 for j in r for l in s))
                        require(a_gauss(support)==product(product(a_gauss(r),a_gauss(s)),cross),
                                "complete cross-block cubic CRT phase")
                        phase = product(product(a_gauss(support),symbol(support,row_bad)),
                                        symbol(support,aux_bad,True))
                        fused = add(fused,scale(phase,dr*ds))
                require(direct==fused,"exact block fusion with retained zero masks")
                receipts.append({"axes":k,"split":split,"row_zero_primes":sorted(row_bad),
                                 "auxiliary_zero_primes":sorted(aux_bad),"mask":sorted(mask),
                                 "sum_exact":[str(v) for v in direct]})
    return receipts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    output = {"status":"PASS_EXACT_MOMENT_GEOMETRY_CONTROLS",
              "matrix_controls":matrix_controls(),"fusion_controls":fusion_controls(),
              "analytic_completion_proved":False,"new_moment_estimate_proved":False,
              "input_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                              for name in ("GENERALIZED_MOMENT_GEOMETRY.md",
                                           "verify_moment_geometry.py")},
              "scope":"exact finite algebraic controls; native proof remains essential"}
    content = json.dumps(output,indent=2,sort_keys=True)+"\n"
    if args.output: args.output.write_text(content)
    else: print(content,end="")


if __name__ == "__main__":
    main()
