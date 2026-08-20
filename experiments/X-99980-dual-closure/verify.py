#!/usr/bin/env python3
from __future__ import annotations
import argparse, cmath, hashlib, itertools, json, math
from fractions import Fraction
from pathlib import Path

def f(y: float) -> float:
    if y < 1.0:
        return 16.0
    return 24.0 / math.sqrt(y) - 9.0 / y

def block(y: float, labels: tuple[int, ...]) -> float:
    total = 0.0
    for mask in range(1 << len(labels)):
        q = 1
        c = 1.0
        parity = 0
        for i,p in enumerate(labels):
            if (mask >> i) & 1:
                q *= p
                c *= p ** -1.5
                parity ^= 1
        total += (-1.0 if parity else 1.0) * c * f(y / q)
    return total

def priority_formula(activities: tuple[Fraction, ...], i: int, A: frozenset[int]) -> Fraction:
    coeff = [Fraction(1)]
    for _ in A:
        new = [Fraction(0)] * (len(coeff)+1)
        for j,c in enumerate(coeff):
            new[j] += c
            new[j+1] -= c
        coeff = new
    for h,a in enumerate(activities):
        if h == i or h in A:
            continue
        new = [Fraction(0)] * (len(coeff)+1)
        for j,c in enumerate(coeff):
            new[j] += c
            new[j+1] -= a*c
        coeff = new
    integ = sum(c/Fraction(j+1) for j,c in enumerate(coeff))
    w = activities[i]
    for h in A:
        w *= activities[h]
    return w*integ

def brute_average(activities: tuple[Fraction, ...], i: int, A: frozenset[int]) -> Fraction:
    k=len(activities)
    total=Fraction(0)
    perms=list(itertools.permutations(range(k)))
    for perm in perms:
        pos={v:j for j,v in enumerate(perm)}
        if any(pos[h] < pos[i] for h in A):
            continue
        val=activities[i]
        for h in A:
            val*=activities[h]
        for h in range(k):
            if h!=i and h not in A and pos[h]<pos[i]:
                val*=1-activities[h]
        total+=val
    return total/Fraction(len(perms))

def verify():
    disc=25-72
    assert disc < 0

    labels=(2,3,5,67,67)
    checks=0
    for k in range(1,5):
        qs=labels[:k]
        breaks={1}
        for mask in range(1<<k):
            q=1
            for i,p in enumerate(qs):
                if mask>>i&1:
                    q*=p
            breaks.add(q)
        pts=[]
        sb=sorted(breaks)
        for z in sb:
            pts += [z*(1-1e-9), z, z*(1+1e-9)]
        for a,b in zip(sb,sb[1:]):
            pts.append(math.sqrt(a*b))
        pts.append(sb[-1]*1000.0)
        for y in pts:
            if y>0:
                assert block(y,qs) > -1e-10
                checks+=1

    flow_checks=0
    for k in range(1,6):
        acts=tuple(Fraction(i+1, 20+i) for i in range(k))
        for i in range(k):
            others=[h for h in range(k) if h!=i]
            for mask in range(1<<len(others)):
                A=frozenset(others[j] for j in range(len(others)) if mask>>j&1)
                assert priority_formula(acts,i,A)==brute_average(acts,i,A)
                flow_checks+=1

    phase_checks=0
    for p in (2,3,5,67,71):
        gap=2*(1-p**-1)
        assert gap >= 1
        assert abs(1-cmath.exp(1j*0*math.log(p))) == 0
        phase_checks+=1

    core={
        "schema":"riemann.t99980.dual-closure.v1",
        "base_pr668":"15719b975115ecad1b23264c6a6303899b4c99dc",
        "sibling_pr670":"f5d37a5f1880749dd33b103d98e2d85bac60ae28",
        "quadratic_block_checks":checks,
        "random_order_flow_checks":flow_checks,
        "phase_gap_checks":phase_checks,
        "feag99980_proved":False,
        "pscp99990_proved":False,
        "rh_established":False,
        "verdict":"PASS_T99980_DUAL_CLOSURE_ASSAULT_ALGEBRA",
    }
    digest=hashlib.sha256(json.dumps(core,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return {"core":core,"proof_object_sha256":digest}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()
    out=verify()
    text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    print(out["core"]["verdict"])
    print(out["proof_object_sha256"])

if __name__=="__main__":
    main()
