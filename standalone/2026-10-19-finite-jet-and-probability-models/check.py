#!/usr/bin/env python3
"""Exact component checks, NOT an independent theta-source certificate.

Only the standard library is required. Run:
    python check.py --output results.json

The analytic infinite-dimensional results are proved in the Markdown notes.
This program checks finite algebra, a transcribed source adapter, and an exact
synthetic probability-law example. It does not certify RH or a zeta zero.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent

def qq(s: str | int) -> Q:
    return Q(s)

def assert_record(records: list[dict], name: str, predicate: bool, detail: str = "") -> None:
    if not predicate:
        raise AssertionError(name + ": " + detail)
    records.append({"name": name, "status": "PASS", "detail": detail})

def cpow(z: tuple[Q, Q], n: int) -> tuple[Q, Q]:
    out = (Q(1), Q(0))
    for _ in range(n):
        out = (out[0]*z[0]-out[1]*z[1], out[0]*z[1]+out[1]*z[0])
    return out

def cmul(z: tuple[Q,Q], w: tuple[Q,Q]) -> tuple[Q,Q]:
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]

def divisor_count(x: int) -> int:
    if x <= 0:
        return 0
    r = isqrt(x)
    return 2*sum(x//j for j in range(1,r+1))-r*r

def harmonic_zero_count_brute(x: int, N: int) -> int:
    # Counts pairs n>N, j positive odd, with n*j <= x.
    return sum((x//n+1)//2 for n in range(N+1,x+1))

def harmonic_zero_count_fast(x: int, N: int) -> int:
    return divisor_count(x)-divisor_count(x//2)-sum((x//n+1)//2 for n in range(1,N+1))

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=HERE/"results.json")
    args=parser.parse_args()
    records=[]
    src=json.loads((HERE/"source_excerpt.json").read_text())
    rho=qq(src["source_cube_radius"])
    width=qq(src["truncation_width"])
    intervals=[(qq(x)-rho,qq(x)+width+rho) for x in src["decimal_truncations"]]
    amin=Q(1,1000); amax=Q(1,8); sep=Q(1,2000)
    assert_record(records,"12 transcribed active-node intervals are positive and bounded",
                  len(intervals)==12 and all(lo>amin and hi<amax for lo,hi in intervals))
    ordered=sorted(intervals)
    assert_record(records,"all active-node separations exceed 1/2000",
                  all(ordered[i+1][0]-ordered[i][1]>sep for i in range(11)))
    # J = diag(2,...,13) V diag(b_j). Lagrange-coefficient bound.
    J_inverse_bound=(1+amax)**11/(2*amin*sep**11)
    R_bound=2*J_inverse_bound
    assert_record(records,"conditional preconditioner norm bound < 10^40",R_bound<10**40,
                  "Uses the source assertion ||I-RJ|| < 1; does not load the original R.")
    T=10**25; B=Q(2,5); vmin=Q(1,25)
    abs_c_upper=1/(vmin*(T*T+B*B))
    beta=qq(src["reported_beta_coarsened_upper"])
    L=qq(src["reported_L_coarsened_upper"])
    perturbation=2*Q(10**40)*abs_c_upper**2
    ratio=(beta+L*rho+perturbation)/rho
    assert_record(records,"moment-equation contraction perturbation has strict slack",
                  ratio<Q(1,1000000),
                  "Imported beta and L are coarsened reported bounds, not independently replayed.")
    assert_record(records,"pair-envelope sector condition for T=10^25, B=2/5",
                  2*T*B <= T*T-B*B)
    excess=16*T*T*B*B/(vmin*vmin*(T*T+B*B)**4)
    q2=qq(src["reported_Q2_upper"])
    assert_record(records,"inserted-pair canonical mass stays below 7/400",
                  q2+excess<Q(7,400))
    # Exact complex rational checks of the insertion geometry, at many scales.
    geometry_cases=0
    for tt in [3,7,100,10**6,10**25]:
        for bb in [Q(1,7),Q(1,3),Q(2,5)]:
            v=Q(1,23)
            den=v*(tt*tt+bb*bb)**2
            c=(Q(tt*tt-bb*bb)/den, -2*tt*bb/den)
            z2=(Q(tt*tt-bb*bb),2*tt*bb)
            assert_record(records,f"exact pair geometry T={tt}, B={bb}",
                          cmul(c,(v*z2[0],v*z2[1]))==(Q(1),Q(0)) and
                          2*(c[0]*c[0]+c[1]*c[1])-2*(c[0]*c[0]-c[1]*c[1])==4*c[1]*c[1] and
                          c[0]>0 and c[1]*c[1]<=c[0]*c[0])
            geometry_cases+=1
    # Sub-Gaussian coefficient proof reduced to exact inequalities on q>=1/3.
    dfact=1
    for k in range(1,101):
        dfact*=2*k-1
        if dfact<3**(k-1):
            raise AssertionError("three-atom moment domination")
    assert_record(records,"three-atom Gaussian domination through k=100",True,
                  "The note supplies the all-k induction; this finite loop is only a regression check.")
    # Exact synthetic four-moment repair with two Rademacher weights.
    # Old a=4/5, b=3/5: variance 1 and fourth cumulant -2*337/625.
    q=Q(49,100); w=Q(1,100)
    s2=1-q*w*w
    s4=Q(337,625)+(q-3*q*q)*w**4/2
    disc=2*s4-s2*s2
    assert_record(records,"synthetic two-weight fourth-cumulant repair is feasible",
                  disc>0 and s2>0 and s2*s2>disc,
                  "Squared weights are (s2 +/- sqrt(disc))/2. This is NOT a theta fit.")
    assert_record(records,"synthetic repaired variance and fourth moment are exact",
                  s2+q*w*w==1 and -2*s4+(q-3*q*q)*w**4==-2*Q(337,625))
    count_cases=0
    for n in [0,1,3,10,40]:
        for x in range(max(1,n),1001):
            if harmonic_zero_count_brute(x,n)!=harmonic_zero_count_fast(x,n):
                raise AssertionError(f"harmonic zero-count identity: N={n}, X={x}")
            count_cases+=1
    assert_record(records,"exact harmonic zero-count identity",True,f"{count_cases} integer cases checked.")
    all_files=[p for p in HERE.iterdir() if p.is_file() and p.name not in {args.output.name,"MANIFEST.json"}]
    out={
        "status":"COMPONENT_CHECKS_PASS; THETA_SOURCE_REPLAY_NOT_RUN",
        "new_zeta_zero_free_region":False,
        "RH_proved":False,
        "off_critical_zeta_zero_found":False,
        "github_written":False,
        "source_commit":src["source_commit"],
        "arithmetic":"Python fractions.Fraction, exact integer arithmetic",
        "checks":records,
        "case_counts":{"pair_geometry":geometry_cases,"harmonic_integer_cases":count_cases},
        "contraction_budget_ratio_upper":str(ratio),
        "contraction_budget_ratio_float_for_display":float(ratio),
        "reserve_guard_not_replayed":"The original full-cube minimum a must exceed 2/[v(T^2+B^2)]. The qualitative theorem only needs sufficiently large T.",
        "limitations":[
            "Original infinite theta integrals and complete source certificate were not recomputed.",
            "The probability theorem is analytic and source-qualified; its enormous finite Ising model was not numerically instantiated.",
            "No all-order theta feasibility, new zeta strip, or RH conclusion is asserted.",
            "No external mathematical independence or worldwide novelty review was performed."
        ],
        "file_sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in all_files}
    }
    args.output.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({"status":out["status"],"checks":len(records),"harmonic_cases":count_cases,
                      "contraction_budget_ratio":float(ratio),"output":str(args.output)},indent=2))

if __name__=="__main__":
    main()
