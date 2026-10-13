#!/usr/bin/env python3
"""Independent global assemblies for the finite degree census.
The primitive ideal/residue helper is shared, not an independent number-field backend.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import importlib.util
import json

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("degree_census",HERE/"degree_census.py")
d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
c=d.c
checks=Counter()

def need(ok,label):
    checks[label]+=1
    if not ok:
        raise ValueError(label)

# Z[omega,Z]/(omega^2+omega+1, Z^2+4Z+9).
# Z=-2+i sqrt(5), and the tested unit phase is z=Z/3.
def mul(x,y):
    out=[0]*4
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            oi,zi=i%2,i//2
            oj,zj=j%2,j//2
            os=((oi+oj,1),) if oi+oj<2 else ((0,-1),(1,-1))
            zs=((zi+zj,1),) if zi+zj<2 else ((0,-9),(1,-4))
            for o,co in os:
                for z,cz in zs:
                    out[o+2*z]+=a*b*co*cz
    return tuple(out)

def conjugate(x):
    # omega -> -1-omega, Z -> -4-Z.
    basis=((1,0,0,0),(-1,-1,0,0),(-4,0,-1,0),(4,4,1,1))
    return tuple(sum(x[j]*basis[j][i] for j in range(4)) for i in range(4))

def direct_phase_witness():
    D,H=256,338
    ps=c.prime_ideals(D);rows=c.element_rows(H)
    cols=[fac for n,fac,_ in c.ideals_through(D,ps)
          if D<2*n and all(e==1 for j,e in fac)]
    total=[0]*4
    native=0
    for u in rows:
        prime=[0,0];composite=[0,0]
        for fac in cols:
            need(len(fac) in (1,2),"witness_degree_cap")
            r=c.ROOTS[c.phase(u,fac,ps)]
            dest=prime if len(fac)==1 else composite
            dest[0]+=r[0];dest[1]+=r[1]
        # 9 A(z)=3 Z P+Z^2 C=-9 C+Z(3P-4C).
        value=(-9*composite[0],-9*composite[1],
               3*prime[0]-4*composite[0],3*prime[1]-4*composite[1])
        squared=mul(value,conjugate(value))
        fourth=mul(squared,squared)
        total=[x+y for x,y in zip(total,fourth)]
        a,b=composite[0]-prime[0],composite[1]-prime[1]
        native+=(a*a-a*b+b*b)**2
    need(total[1:]==[0,0,0],"phase_witness_rationality")
    phase=Q(total[0],9**4)
    need(native==3021246,"direct_mobius_value")
    need(phase==Q(8892106,3),"direct_algebraic_phase_value")
    need(Q(native)-phase==Q(171632,3),"strict_finite_phase_improvement")
    return {"D":D,"H":H,"native":native,
            "other_phase_moment":[phase.numerator,phase.denominator],
            "saving":[171632,3],"phase":"(-2+i sqrt(5))/3"}

def brute_gram_and_singletons(D,H):
    ps=c.prime_ideals(D);rows=c.element_rows(H)
    cols=[fac for n,fac,_ in c.ideals_through(D,ps)
          if D<2*n and all(e==1 for j,e in fac)]
    degree=[len(f) for f in cols]
    phases=[[c.phase(u,f,ps) for u in rows] for f in cols]
    size=2*max(degree)+1
    full=[[0]*size for _ in range(size)]
    ns=[[0]*size for _ in range(size)]
    two_real=(2,1,-1,-2,-1,1)
    for a,b,e,f in product(range(len(cols)),repeat=4):
        counts=Counter()
        for index in (a,b,e,f):
            counts.update(j for j,power in cols[index])
        nos=all(m!=1 for m in counts.values())
        kernel=0
        for p,q,r,s in zip(phases[a],phases[b],phases[e],phases[f]):
            if 6 not in (p,q,r,s):
                kernel+=two_real[(p+q-r-s)%6]
        left,right=degree[a]+degree[b],degree[e]+degree[f]
        full[left][right]+=kernel
        if nos:
            ns[left][right]+=kernel
        checks["ordered_quartets_reconstructed"]+=1
    for mat in (full,ns):
        for row in mat:
            for j,value in enumerate(row):
                need(value%2==0,"integer_real_gram")
                row[j]//=2
    calc=d.run_case(D,H,True)
    need(full==calc["degree_gram"],"tuple_versus_degree_gram")
    need(ns==calc["no_singleton_degree_gram"],"tuple_versus_product_singleton_gram")
    # Literal unit action, including all zeros.
    for index,fac in enumerate(cols):
        norm=1
        for j,e in fac:
            norm*=ps[j][0]**e
        charge=((norm-1)//6)%6
        for u in rows:
            eu=(u[0]-u[1],u[0])
            before=c.phase(u,fac,ps);after=c.phase(eu,fac,ps)
            need(after==(6 if before==6 else (before+charge)%6),
                 "literal_unit_action")
    return {"D":D,"H":H,"columns":len(cols),"rows":len(rows),
            "singleton":calc["singleton_mobius"]}

def main():
    report=json.loads((HERE/"results.json").read_text())
    small=[brute_gram_and_singletons(32,13),brute_gram_and_singletons(64,79)]
    witness=direct_phase_witness()
    byD={r["D"]:r for r in report["cases"]}
    r=byD[256]
    need(r["singleton_mobius"]==-14088,"negative_singleton_sector")
    need(byD[64]["singleton_mobius"]==2496,"positive_singleton_sector")
    need(r["degree_gram"][4][4]-r["no_singleton_degree_gram"][4][4]==-9744,
         "singleton_matrix_not_positive_semidefinite")
    need(r["degree_diagonal"]!=r["M4_mobius"],
         "discarding_degree_interference_changes_source")
    need(byD[8192]["M4_mobius"]==114923460372,"parent_largest_moment_agreement")
    need(byD[8192]["degree_diagonal"]==1652703692676,"largest_degree_diagonal")
    # Recompute a full middle case without trusting its saved fields.
    need(d.run_case(256,338,True)==r,"saved_case_full_reconstruction")
    for badD,badH in ((True,1),(0,1),(64,0),(9000,1),(64,20001)):
        try:
            d.degree_gram(badD,badH)
        except (ValueError,OverflowError):
            checks["resource_or_type_guard_rejection"]+=1
        else:
            raise ValueError("missing guard")
    print(json.dumps({"status":"PASS_FINITE_GLOBAL_RECONSTRUCTIONS",
        "scope":"Independent tuple/grade/product assemblies sharing one authenticated arithmetic helper; not independent mathematical review.",
        "checks":dict(sorted(checks.items())),"small_cases":small,
        "phase_witness":witness},sort_keys=True,indent=2))

if __name__=="__main__":
    main()
