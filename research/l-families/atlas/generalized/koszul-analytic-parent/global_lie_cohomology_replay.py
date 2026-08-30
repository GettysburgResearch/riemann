"""Actual arithmetic Koszul Lie source and its ramified global branch gate."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from fractions import Fraction
from math import comb
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
PREFIX="research/l-families/atlas/generalized/koszul-analytic-parent/"
FREEZE="e2b0ef1b35fa46e81a1f1b447a70f42dd3b92c2e"
PINS=(
    ("global_cohomology_replay.py","87fd6d661a88e7830d234963b8dce16b49caa8f2",
     "da202437478ed4a199deb4b2f05ca2e7ce1062faa5d60c1c29bd80c4a8aacf66"),
    ("GLOBAL_COHOMOLOGICAL_COMPLETION.md","8ecc724afc29e048097d955b8eb7a872d26f79a7",
     "fadf5a3e609ce64b6c49cb848186495bab579cba5fdb5a5e594638b635469d66"),
)
OWNED=("GLOBAL_KOSZUL_LIE_COHOMOLOGY.md","S3_LIE_RAMIFICATION_CORRECTION.md",
       "GLOBAL_LIE_REPLAY.md","global_lie_cohomology_replay.py","tests/test_global_lie_cohomology.py")
FIXTURE=HERE/"global_lie_cohomology.verification.json"


def need(condition: bool,message: str):
    if not condition:
        raise ValueError(message)


def digest(data: bytes):
    import hashlib

    return hashlib.sha256(data.replace(b"\r\n",b"\n")).hexdigest()


def authenticate_frozen():
    for name,blob,expected in PINS:
        actual=subprocess.check_output(["git","rev-parse",FREEZE+":"+PREFIX+name],cwd=ROOT,text=True).strip()
        need(actual==blob,"arithmetic Lie dependency blob mismatch")
        frozen=subprocess.check_output(["git","cat-file","blob",blob],cwd=ROOT)
        need(digest(frozen)==expected,"arithmetic Lie dependency hash mismatch")
        need(digest((HERE/name).read_bytes())==expected,"working arithmetic Lie source changed")


authenticate_frozen()
SPEC=importlib.util.spec_from_file_location("frozen_global_lie_source",HERE/"global_cohomology_replay.py")
need(SPEC is not None and SPEC.loader is not None,"authenticated global source import failed")
G=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G)
C,R=G.C,G.R


def lie_rows(cut: int):
    R.integer(cut,1,96)
    rows=[]
    for n in range(1,cut+1):
        dimension,s,_=C.source_grade(n,2)
        second,c,_=C.source_grade(n,3)
        need(dimension==second,"source character dimensions disagree")
        numerators=(dimension+3*s+2*c,dimension-3*s+2*c,2*(dimension-c))
        need(all(x>=0 and x%6==0 for x in numerators),"actual Lie multiplicities not nonnegative integral")
        a,b,std=(x//6 for x in numerators)
        need(a+b+2*std==dimension,"Lie source dimension lost")
        h1=2*b+2*std
        rows.append({"grade":n,"parity_sign":(-1)**(n+1),
                     "class_traces":[dimension,s,c],"multiplicities":[a,b,std],
                     "h0_h1_h2":[a,h1,a],"kappa":b+std-a,
                     "C2_invariants":a+std,"C3_invariants":a+b,
                     "C3_residual_transposition_trace":a-b})
    return rows


def multiply(left,right,cut: int):
    out=[0]*(cut+1)
    for i,a in enumerate(left[:cut+1]):
        for j,b in enumerate(right[:cut+1-i]):
            out[i+j]+=a*b
    return out


def power(poly,exponent: int,cut: int):
    R.integer(exponent,0,3)
    out=[1]+[0]*cut
    for _ in range(exponent):
        out=multiply(out,poly,cut)
    return out


def substituted(poly,order: int,cut: int):
    out=[0]*(cut+1)
    for i,a in enumerate(poly):
        if order*i<=cut:
            out[order*i]=a
    return out


def binomial_factor(order: int,exponent: int,eigenvalue: int,cut: int):
    out=[0]*(cut+1)
    for k in range(cut//order+1):
        coefficient=(-1)**k*comb(exponent,k) if exponent>=0 and k<=exponent else 0
        if exponent<0:
            coefficient=comb(-exponent+k-1,k)
        out[order*k]=coefficient*eigenvalue**k
    return out


def local_parent(kind: str,cut: int):
    need(kind in ("e","s","c","C2","C3","C3s"),"unknown actual inertia/holonomy class")
    R.integer(cut,1,24)
    out=[1]+[0]*cut
    for row in lie_rows(cut):
        n=row["grade"]
        dimension,s,c=row["class_traces"]
        sign=(-1)**n
        if kind=="e":
            factors=[(n,sign*dimension,1)]
        elif kind=="s":
            factors=[(n,sign*(dimension+s)//2,1),(n,sign*(dimension-s)//2,-1)]
        elif kind=="c":
            invariant=(dimension+2*c)//3
            other=(dimension-c)//3
            factors=[(n,sign*(invariant-other),1),(3*n,sign*other,1)]
        elif kind in ("C2","C3"):
            dimension=row["C2_invariants"] if kind=="C2" else row["C3_invariants"]
            factors=[(n,sign*dimension,1)]
        else:
            dimension=row["C3_invariants"]
            need((dimension-s)%2==0,"residual infinity eigenmultiplicities not integral")
            factors=[(n,sign*(dimension+s)//2,1),(n,sign*(dimension-s)//2,-1)]
        for order,exponent,eigenvalue in factors:
            if order<=cut:
                out=multiply(out,binomial_factor(order,exponent,eigenvalue,cut),cut)
    return out


def segre_series(kind: str,cut: int):
    need(kind in ("e","s","c","C2","C3","C3s"),"unknown Segre inertia class")
    R.integer(cut,1,24)
    fe=[(n+1)*comb(n+2,2) for n in range(cut+1)]
    fs=[n//2+1 if n%2==0 else 0 for n in range(cut+1)]
    fc=[int(n%3==0) for n in range(cut+1)]
    if kind=="C2":
        return [(a+b)//2 for a,b in zip(fe,fs)]
    if kind=="C3":
        return [(a+2*b)//3 for a,b in zip(fe,fc)]
    return {"e":fe,"s":fs,"c":fc,"C3s":fs}[kind]


def local_controls(cut=12):
    R.integer(cut,2,24)
    series={kind:local_parent(kind,cut) for kind in ("e","s","c","C2","C3","C3s")}
    for kind in ("e","s","c"):
        need(series[kind]==segre_series(kind,cut),"unramified source PBW identity failed")
    e,s,c,sd2,sd3,sd3s=(series[k] for k in ("e","s","c","C2","C3","C3s"))
    need(multiply(power(sd2,2,cut),substituted(e,2,cut),cut)==
         multiply(multiply(substituted(sd2,2,cut),s,cut),e,cut),"C2 Mahler source identity failed")
    need(multiply(power(sd3,3,cut),substituted(e,3,cut),cut)==
         multiply(multiply(substituted(sd3,3,cut),power(c,2,cut),cut),e,cut),"C3 Mahler source identity failed")
    need(multiply(power(sd3s,2,cut),substituted(e,2,cut),cut)==
         multiply(power(s,2,cut),substituted(sd3,2,cut),cut),"residual-infinity Mahler identity failed")
    defects=[]
    for kind in ("C2","C3","C3s"):
        actual,wrong=series[kind],segre_series(kind,cut)
        need(actual[1]==wrong[1] and actual[2]!=wrong[2],"grade-two ramification defect was lost")
        defects.append({"source":kind,"actual_parent":actual,"full_invariant_Segre":wrong,
                        "first_failed_grade":2,"degree_two_difference":actual[2]-wrong[2]})
    return {"cut":cut,"unramified_PBW_controls":{k:series[k] for k in ("e","s","c")},
            "ramified_defects":defects,"all_three_Mahler_identities":True}


def native_source(index: int):
    R.integer(index,0,2)
    return G.native_source(*G.SOURCES[index])


def fibre_controls(index: int,cut=12):
    source=native_source(index)
    R.integer(cut,1,48)
    grades=lie_rows(cut)
    out=[]
    for row in source["primitive_rows"]:
        q=row["field_order"]
        traces=[]
        for grade in grades:
            dim,s,c=grade["class_traces"]
            a,b,std=grade["multiplicities"]
            values={(3,1):dim,(1,-1):s,(0,1):c,(2,0):a+std}
            actual=sum(item["number"]*values[item["distinct_roots"],item["sign_trace"]]
                       for item in row["finite_fibre_histogram"])
            actual+=a+b if q%3==1 else a-b
            expected=a*(q+1)+b*(row["counts"]["D"]-q-1)+std*(row["counts"]["E"]-q-1)
            need(actual==expected,"actual Lie finite-fibre trace differs from cohomology")
            traces.append(actual)
        need(traces[0]==row["counts"]["Z"],"M1 is not the actual regular closure source")
        branches=sum(item["number"] for item in row["finite_fibre_histogram"] if (item["distinct_roots"],item["sign_trace"])==(2,0))
        need(branches%2==0,"nonzero finite branch points failed plus-minus pairing")
        infinity=2 if q%3==1 else 0
        need((row["counts"]["Z"]-infinity)%6==0,"normalized closure congruence failed")
        alpha=Fraction(row["counts"]["Z"],6)
        need(q%3!=1 or alpha.denominator==3,"cubic branch exponent became integral")
        out.append({"extension":row["degree"],"field_order":q,"full_Lie_fibre_traces":traces,
                    "Z_points":row["counts"]["Z"],"finite_rational_branch_points":branches,
                    "infinity_points":infinity,"first_boundary_exponent":C.qjson(alpha),
                    "cubic_branch_obstruction_proved":q%3==1})
    return out


def finite_L(source,value: Fraction,grade: int):
    value=C.exact(value)
    R.integer(grade,1,6)
    q=source["parameters_p_A_B"][0]
    need((1-value)*(1-q*value)!=0,"explicit finite Lie principal pole")
    a,b,std=lie_rows(grade)[-1]["multiplicities"]
    result=((1-value)*(1-q*value))**(-a)
    for name,weight in (("D",b),("E",std)):
        polynomial=source["polynomials"][name]
        result*=sum((coefficient*value**i for i,coefficient in enumerate(polynomial)),Fraction(0))**weight
    return result


def finite_duality(index: int,cut: int):
    R.integer(cut,1,6)
    source=native_source(index)
    q,z,T=source["parameters_p_A_B"][0],Fraction(2,3),Fraction(1,13)
    rows=lie_rows(cut)
    K=sum(row["parity_sign"]*row["kappa"] for row in rows)
    W=sum(row["grade"]*row["parity_sign"]*row["kappa"] for row in rows)
    left,right=Fraction(1),Fraction(1)
    for row in rows:
        n,sign=row["grade"],row["parity_sign"]
        left*=finite_L(source,T*z**n,n)**sign
        right*=finite_L(source,1/(q*T*z**n),n)**sign
    need(left==Fraction(q)**K*T**(2*K)*z**(2*W)*right,"finite arithmetic Lie duality failed")
    return {"cut":cut,"K":K,"W":W,"source_functional_equation":True}


def logarithm_control(index: int,r: Fraction,grade_cut=16,power_cut=20):
    source=native_source(index)
    q=source["parameters_p_A_B"][0]
    r=C.exact(r)
    need(0<r<Fraction(1,2*q),"strict bounded positive Lie Euler disk required")
    R.integer(grade_cut,2,24)
    R.integer(power_cut,2,48)
    rows=lie_rows(grade_cut)
    grade=Fraction(0),Fraction(0)
    for row in rows:
        n,sign=row["grade"],row["parity_sign"]
        a,b,std=row["multiplicities"]
        u=r**n
        pairs=[(1-u,-sign*a),(1-q*u,-sign*a)]
        for name,weight in (("D",b),("E",std)):
            poly=source["polynomials"][name]
            pairs.append((sum((coefficient*u**j for j,coefficient in enumerate(poly)),Fraction(0)),sign*weight))
        for value,weight in pairs:
            interval=C.weighted_log(value,weight)
            grade=grade[0]+interval[0],grade[1]+interval[1]
    ed=G.frobenius_traces(source["polynomials"]["D"],power_cut)
    ee=G.frobenius_traces(source["polynomials"]["E"],power_cut)
    middle=Fraction(0)
    power_error=Fraction(0)
    for row in rows:
        n,sign=row["grade"],row["parity_sign"]
        a,b,std=row["multiplicities"]
        for m in range(1,power_cut+1):
            middle+=sign*(a*(q**m+1)-b*ed[m-1]-std*ee[m-1])*r**(n*m)/m
        x=q*r**n
        power_error+=2*row["class_traces"][0]*x**(power_cut+1)/((power_cut+1)*(1-x))
    need(grade[0]<=middle+power_error and grade[1]>=middle-power_error,
         "independent finite arithmetic Lie log enclosures disagree")
    grade_error=6*q*(2*r)**(grade_cut+1)/((1-2*r)*(1-q*r**(grade_cut+1)))
    return {"r":C.qjson(r),"T":1,"grade_cut":grade_cut,"power_cut":power_cut,
            "finite_grade_log":C.interval_json(grade),"finite_power_log":C.qjson(middle),
            "proved_power_tail":C.qjson(power_error),"proved_infinite_grade_tail":C.qjson(grade_error)}


def branch_gate(index: int):
    source=native_source(index)
    q=source["parameters_p_A_B"][0]
    row=source["primitive_rows"][0]
    eD,eE=-source["polynomials"]["D"][1],-source["polynomials"]["E"][1]
    alpha=Fraction(1+q-eD-2*eE,6)
    need(alpha==Fraction(row["counts"]["Z"],6),"closure source branch exponent disagrees")
    r=Fraction(3,5)
    N=6
    need(2*r*r<1 and q*r**(N+1)<1,"finite-grade continuation split outside its proof domain")
    at_tau=[]
    for n in range(1,N+1):
        value=finite_L(source,Fraction(-1,2)**n,n)
        need(value!=0,"finite source factor vanishes at the first grading branch")
        at_tau.append(C.qjson(value))
    remainder_bound=6*q*q*(2*r*r)**(N+1)/((1-q*r**(N+1))*(1-2*r*r))
    return {"Q":q,"alpha":C.qjson(alpha),"continuation_radius":C.qjson(r),
            "removed_grade_cut":N,"finite_factors_at_minus_half":at_tau,
            "uniform_higher_power_remainder_bound":C.qjson(remainder_bound),
            "nonmeromorphic_cubic_branch":q%3==1,
            "integer_exponent_is_not_claimed_to_prove_a_branch":q%3==2}


def compact_support_controls(index: int,cut=12):
    source=native_source(index)
    R.integer(cut,1,48)
    grades=lie_rows(cut)
    outputs=[]
    for primitive,closed in zip(source["primitive_rows"],fibre_controls(index,cut)):
        q=primitive["field_order"]
        branch_count=closed["finite_rational_branch_points"]
        split_count=sum(item["number"] for item in primitive["finite_fibre_histogram"]
                        if (item["distinct_roots"],item["sign_trace"])==(3,1))
        i=int(q%3==1)
        zcount=primitive["counts"]["Z"]
        need(zcount==6*split_count+3*branch_count+2*i,"actual split/branch/closure identity failed")
        alpha=Fraction(zcount,6)
        corrected=alpha-Fraction(branch_count,2)-Fraction(i,3)
        need(corrected==split_count,"ramified correction did not remove the fractional first exponent")
        rows=[]
        for grade,closed_trace in zip(grades,closed["full_Lie_fibre_traces"]):
            dim,s,c=grade["class_traces"]
            a,b,std=grade["multiplicities"]
            boundary_trace=branch_count*(a+std)+(a+b if i else a-b)
            values={(3,1):dim,(1,-1):s,(0,1):c}
            actual=sum(item["number"]*values[item["distinct_roots"],item["sign_trace"]]
                       for item in primitive["finite_fibre_histogram"]
                       if (item["distinct_roots"],item["sign_trace"])!=(2,0))
            need(actual==closed_trace-boundary_trace,"compact-support trace did not remove actual bad fibres")
            compact_h1=a+3*dim
            need(compact_h1==4*a+3*b+6*std,"compact-support localization dimension failed")
            h1_closed_trace=a*(q+1)-closed_trace
            h1_compact_trace=h1_closed_trace+boundary_trace-a
            need(actual==a*q-h1_compact_trace,"compact-support source cohomology trace mismatch")
            rows.append({"grade":grade["grade"],"h0_h1_h2":[0,compact_h1,a],
                         "full_geometric_boundary_dimension":5*a+b+4*std,
                         "rational_boundary_trace":boundary_trace,
                         "actual_unramified_trace":actual,"compact_H1_trace":h1_compact_trace})
        tau=Fraction(-1,2)
        fe=(1+2*tau)/(1-tau)**4
        fs=1/(1-tau*tau)**2
        fc=1/(1-tau**3)
        local_values=[(fe+fs)/2,(fe+2*fc)/3,fs]
        need(local_values==[Fraction(8,9),Fraction(16,27),Fraction(16,9)],
             "actual invariant Segre factor values at the first boundary changed")
        outputs.append({"extension":primitive["degree"],"field_order":q,
                        "unramified_split_rational_places":split_count,
                        "rational_finite_branch_places":branch_count,"split_infinity_indicator":i,
                        "closed_Lie_exponent":C.qjson(alpha),
                        "bad_parent_exponent":C.qjson(Fraction(branch_count,2)+Fraction(i,3)),
                        "corrected_Segre_exact_zero_order":split_count,
                        "bad_Segre_values_at_minus_half":[C.qjson(value) for value in local_values],
                        "compact_support_source_rows":rows})
    return outputs


def build_payload():
    authenticate_frozen()
    panels=[]
    for index in range(3):
        source=native_source(index)
        q=source["parameters_p_A_B"][0]
        panels.append({"parameters":source["parameters_p_A_B"],"primitive_fields_recounted":[q,q*q],
                       "cohomological_fibre_controls":fibre_controls(index),
                       "finite_duality":[finite_duality(index,n) for n in (1,2,3,4)],
                       "ordinary_log_control":logarithm_control(index,Fraction(1,4*q)),
                       "global_first_branch_gate":branch_gate(index),
                       "compact_support_and_corrected_boundary":compact_support_controls(index)})
    return {"schema":"actual-global-koszul-lie-cohomology-v1",
            "provenance":{"freeze":FREEZE,"pins":[list(pin) for pin in PINS],
                          "owned_sha256_lf":{name:digest((HERE/name).read_bytes()) for name in OWNED}},
            "actual_Lie_cohomology_rows":lie_rows(32),"local_ramification":local_controls(),
            "source_panels":panels,"max_primitive_field_order":49,
            "not_claimed":["polynomial-growth R_n and exponential M_n are the same operator",
                           "PBW commutes with inertia invariants","one invariant-input Euler factor at bad places",
                           "no finite poles between zero and the first grading boundary",
                           "integer first exponent proves a branch","cohomology of an infinite-rank sheaf"]}


def check_payload(candidate: object):
    need(json.dumps(candidate,sort_keys=True)==json.dumps(build_payload(),sort_keys=True),
         "arithmetic Lie fixture differs from complete authenticated source replay")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write",action="store_true")
    group.add_argument("--check",action="store_true")
    args=parser.parse_args()
    payload=build_payload()
    if args.write:
        FIXTURE.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8",newline="\n")
    else:
        need(json.dumps(json.loads(FIXTURE.read_text(encoding="utf-8")),sort_keys=True)==json.dumps(payload,sort_keys=True),
             "arithmetic Lie fixture mismatch")
    print("PASS actual global Koszul Lie cohomology, ramification and cubic branch gate")


if __name__=="__main__":
    main()
