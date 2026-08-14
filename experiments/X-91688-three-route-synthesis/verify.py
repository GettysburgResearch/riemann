#!/usr/bin/env python3
"""Exact finite regression for a three-route Riemann closure synthesis.

Checks only:
A. rough-prime deletion / first-owner algebra;
B. root-Hall typed identity and universal fixed-window score-mass bound;
C. barycentric two-Hankel finite-string test and exact separator.

It does not prove SONTR/NRCT, the analytic root producer, all finite Xi
memberships, or RH.
"""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence

SCHEMA = "riemann.three-route-synthesis.v1"

def fs(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def canonical_sha(payload: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def product(values: Iterable[Fraction]) -> Fraction:
    out = Fraction(1)
    for value in values: out *= value
    return out

def route_a() -> dict[str, Any]:
    weights = (Fraction(1,2), Fraction(1,3), Fraction(1,5))
    max_exp = 3
    def base(exp: tuple[int,...]) -> Fraction:
        return product(weights[i] ** exp[i] for i in range(3))
    def filtered(exp: tuple[int,...], upto: int) -> Fraction:
        cache: dict[tuple[tuple[int,...],int],Fraction] = {}
        def rec(e: tuple[int,...], k: int) -> Fraction:
            key=(e,k)
            if key in cache: return cache[key]
            if k == 0: ans=base(e)
            else:
                i=k-1
                ans=rec(e,k-1)
                if e[i] > 0:
                    em=list(e); em[i]-=1
                    ans -= weights[i]*rec(tuple(em),k-1)
            cache[key]=ans
            return ans
        return rec(exp,upto)
    cases=filters=owners=0
    for e0 in range(max_exp+1):
      for e1 in range(max_exp+1):
       for e2 in range(max_exp+1):
        exp=(e0,e1,e2); cases += 1
        for k in range(4):
            got=filtered(exp,k)
            expected=base(exp) if all(exp[i]==0 for i in range(k)) else Fraction(0)
            if got != expected: raise AssertionError(("filter",exp,k,got,expected))
            filters += 1
        total=filtered(exp,3); child=[]
        for i in range(3):
            val=Fraction(0)
            if exp[i] > 0:
                em=list(exp); em[i]-=1
                val=weights[i]*filtered(tuple(em),i)
            child.append(val); total += val
        if total != base(exp): raise AssertionError(("telescope",exp,total,base(exp)))
        positive=[i for i,v in enumerate(child) if v]
        expected_owner=next((i for i,e in enumerate(exp) if e>0),None)
        if expected_owner is None:
            if positive or filtered(exp,3)!=base(exp): raise AssertionError(("residual",exp,child))
        elif positive != [expected_owner] or child[expected_owner] != base(exp):
            raise AssertionError(("owner",exp,child,expected_owner))
        owners += 1
    return {"weights":[fs(x) for x in weights],"exponent_box":"0..3","monomial_cases":cases,
            "filter_checks":filters,"owner_partition_checks":owners,
            "verdict":"PASS_ROUGH_PRIME_DELETION_AND_FIRST_OWNER_PARTITION"}

def left_greedy(e_nodes,e_mass,o_nodes,o_mass):
    rem=list(e_mass); flow=[[Fraction(0) for _ in e_nodes] for _ in o_nodes]
    for oi,(onode,d0) in enumerate(zip(o_nodes,o_mass)):
        demand=d0
        for ei,enode in enumerate(e_nodes):
            if enode>onode or demand==0: break
            amount=min(demand,rem[ei]); flow[oi][ei]+=amount; rem[ei]-=amount; demand-=amount
        if demand: raise ValueError("infeasible Hall control")
    return flow

def l1(v: Sequence[Fraction]) -> Fraction:
    return sum((abs(x) for x in v),Fraction(0))

def route_b() -> dict[str, Any]:
    h54=sum((Fraction(1,k) for k in range(1,55)),Fraction(0))
    if not h54<5: raise AssertionError("H54")
    if not Fraction(55)<Fraction(15,2)**2: raise AssertionError("sqrt55")
    score_bound=5*Fraction(15,2)*5
    if not score_bound<188: raise AssertionError("score bound")
    e_nodes=(1,3); o_nodes=(2,4)
    e_mass=(Fraction(4),Fraction(3)); o_mass=(Fraction(2),Fraction(1))
    ev=((Fraction(1),Fraction(0)),(Fraction(0),Fraction(1)))
    ov=((Fraction(1,2),Fraction(1,2)),(Fraction(1,3),Fraction(2,3)))
    flow=left_greedy(e_nodes,e_mass,o_nodes,o_mass)
    used=[sum((flow[oi][ei] for oi in range(2)),Fraction(0)) for ei in range(2)]
    residual=[e_mass[i]-used[i] for i in range(2)]
    signed=[Fraction(0),Fraction(0)]
    for mass,vec in zip(e_mass,ev):
        for k in range(2): signed[k]+=mass*vec[k]
    for mass,vec in zip(o_mass,ov):
        for k in range(2): signed[k]-=mass*vec[k]
    dec=[Fraction(0),Fraction(0)]
    for mass,vec in zip(residual,ev):
        for k in range(2): dec[k]+=mass*vec[k]
    for oi in range(2):
      for ei in range(2):
       for k in range(2): dec[k]+=flow[oi][ei]*(ev[ei][k]-ov[oi][k])
    if signed!=dec: raise AssertionError((signed,dec))
    M=max(l1(v) for v in (*ev,*ov)); total=sum(e_mass,Fraction(0))+sum(o_mass,Fraction(0))
    if l1(dec)>M*total: raise AssertionError("variation")
    return {"harmonic_54":fs(h54),"universal_score_mass_bound":fs(score_bound),
            "mass_54_correction_multiplier":fs(54*188),
            "synthetic_flow":[[fs(x) for x in row] for row in flow],
            "synthetic_signed_vector":[fs(x) for x in signed],
            "synthetic_total_score_mass":fs(total),"synthetic_profile_norm":fs(M),
            "verdict":"PASS_ROOT_HALL_ONE_USE_STABILITY"}

def deltas(nodes: Sequence[Fraction]) -> list[Fraction]:
    out=[]
    for j,qj in enumerate(nodes):
        d=Fraction(1)
        for i,qi in enumerate(nodes):
            if i!=j: d*=qi-qj
        if d==0: raise ValueError("distinct nodes required")
        out.append(d)
    return out

def moments(nodes,data):
    ds=deltas(nodes)
    return [sum((data[j]*((-nodes[j])**k)/ds[j] for j in range(len(nodes))),Fraction(0)) for k in range(len(nodes))]

def hankel(m,shift,size):
    return [[m[i+j+shift] for j in range(size)] for i in range(size)]

def exact_psd(matrix) -> bool:
    a=[list(r) for r in matrix]
    n=len(a)
    if any(len(r)!=n for r in a): raise ValueError("square")
    if any(a[i][j]!=a[j][i] for i in range(n) for j in range(n)): raise ValueError("symmetric")
    while a:
        n=len(a)
        for i in range(n):
            if a[i][i]<0: return False
            if a[i][i]==0 and any(a[i][j]!=0 for j in range(n)): return False
        pidx=next((i for i in range(n) if a[i][i]>0),None)
        if pidx is None: return all(x==0 for r in a for x in r)
        if pidx:
            a[0],a[pidx]=a[pidx],a[0]
            for r in a: r[0],r[pidx]=r[pidx],r[0]
        p=a[0][0]
        a=[[a[i][j]-a[i][0]*a[0][j]/p for j in range(1,n)] for i in range(1,n)]
    return True

def quadratic(A,v):
    return sum((v[i]*A[i][j]*v[j] for i in range(len(v)) for j in range(len(v))),Fraction(0))

def route_c() -> dict[str, Any]:
    nodes=[Fraction(1),Fraction(2),Fraction(4),Fraction(7),Fraction(11)]; r=nodes[0]
    atoms=[(Fraction(0),Fraction(2,5)),(Fraction(3),Fraction(1,3)),(None,Fraction(1,7))]
    def K(q,s): return Fraction(1) if s is None else (r+s)/(q+s)
    data=[sum((w*K(q,s) for s,w in atoms),Fraction(0)) for q in nodes]
    m=moments(nodes,data); h0=hankel(m,0,3); h1=hankel(m,1,2)
    if not exact_psd(h0) or not exact_psd(h1): raise AssertionError("positive string")
    bad=list(data); bad[-1]-=Fraction(1,10)
    bm=moments(nodes,bad); bh0=hankel(bm,0,3); witness=(Fraction(0),Fraction(1),Fraction(0))
    wval=quadratic(bh0,witness)
    if wval>=0 or exact_psd(bh0): raise AssertionError("negative control")
    ds=deltas(nodes); c=[nodes[j]**2/ds[j] for j in range(len(nodes))]
    dual=sum((c[j]*bad[j] for j in range(len(nodes))),Fraction(0))
    if dual!=wval or dual>=0: raise AssertionError((dual,wval))
    return {"nodes":[fs(x) for x in nodes],"positive_data":[fs(x) for x in data],
            "positive_moments":[fs(x) for x in m],"positive_h0_psd":True,"positive_h1_psd":True,
            "negative_data":[fs(x) for x in bad],"separator_polynomial":"s^2",
            "separator_coefficients":[fs(x) for x in c],"separator_value":fs(dual),
            "verdict":"PASS_FINITE_STRING_TWO_HANKEL_AND_EXACT_SEPARATOR"}

def verify(_: dict[str,Any] | None=None) -> dict[str,Any]:
    out={"schema":SCHEMA,"route_a":route_a(),"route_b":route_b(),"route_c":route_c(),
         "proof_boundary":{"sontr_nrct":"OPEN","analytic_root_endpoint_realization":"OPEN",
         "actual_xi_all_finite_string_membership":"OPEN","riemann_hypothesis":"UNPROVED"},
         "verdict":"PASS_THREE_ROUTE_STRUCTURAL_ADVANCE"}
    out["proof_object_sha256"]=canonical_sha(out)
    return out

def main():
    p=argparse.ArgumentParser(); p.add_argument("certificate",nargs="?",type=Path); p.add_argument("--output",type=Path); a=p.parse_args()
    payload=json.loads(a.certificate.read_text()) if a.certificate else None
    out=verify(payload); text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text)
    print(text,end="")
if __name__=="__main__": main()
