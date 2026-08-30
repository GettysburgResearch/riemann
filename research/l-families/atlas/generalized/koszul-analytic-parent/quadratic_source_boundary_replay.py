"""Actual S4 quadratic source, diagonal inertia and signed analytic completion."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from fractions import Fraction
from functools import cache
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
GENERALIZED = HERE.parent
PREFIX = "research/l-families/atlas/generalized/"
PINS = (
    ("da203ad2d170835499a0f4f7484f04ff787ee408",
     "koszul-analytic-parent/finite_group_boundary_replay.py",
     "e39aca60c4d2230635765a75fc82f80556f9f3df",
     "e5f7a1f22b084ba8167fa526706068132cc388705a858d65fe7eabe94d1d0db0"),
    ("da203ad2d170835499a0f4f7484f04ff787ee408",
     "koszul-analytic-parent/FINITE_GROUP_SOURCE_BOUNDARY.md",
     "33872bfcdbe77338d404d184b6548d4adb253bd0",
     "924728399218f8f19ff48d7eaf08f4388de31cd17a37126b597d84b98fce227c"),
    ("c67d858fc9f7112cf9f0b13049a97d68de0d429b",
     "global-s4-resolvent/quadratic_twist_replay.py",
     "45f38aac4d8941fa9d1972ab9d5436eeccbc5ea2",
     "b2bda3d54969f8498a16bbb8b9f744f398b0c739f13a5d29a203542a16da2c50"),
    ("c67d858fc9f7112cf9f0b13049a97d68de0d429b",
     "global-s4-resolvent/QUADRATIC_TWIST_SOURCE_AND_DIAGONAL_INERTIA.md",
     "5b1705153227e4a6fe5339304b6b879a1c1d37f6",
     "e0b07339337e4f8bc50be92091acc01c777a1ac811b20a0f8558d0fb0690b725"),
    ("c67d858fc9f7112cf9f0b13049a97d68de0d429b",
     "global-s4-resolvent/quadratic_twist_artifact.json",
     "07bdd4c56d3509511e7ac973139908df3d7a11eb",
     "a62e9450194c8a601afa2217f68b859573b5772c264030255981a8f68024f09c"),
    ("c67d858fc9f7112cf9f0b13049a97d68de0d429b",
     "global-s4-resolvent/quadratic_twist_source.json",
     "bfdb6ddf23da4244461563334472a8c5fe3af289",
     "e6aefb9d9991025169bb2a0406b46d683396185ae8af2dadb31c9c1cb046cd1b"),
)
OWNED = ("QUADRATIC_SIGNED_SOURCE_BOUNDARY.md", "QUADRATIC_SOURCE_REPLAY.md",
         "quadratic_source_boundary_replay.py", "tests/test_quadratic_source_boundary.py")
FIXTURE = HERE / "quadratic_source_boundary.verification.json"


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest(data: bytes) -> str:
    import hashlib

    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def authenticate_frozen() -> None:
    for freeze, name, blob, expected in PINS:
        resolved = subprocess.check_output(
            ["git", "rev-parse", freeze + ":" + PREFIX + name], cwd=ROOT, text=True
        ).strip()
        need(resolved == blob, "quadratic source dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "quadratic source dependency hash mismatch")
        need(digest((GENERALIZED / name).read_bytes()) == expected,
             "working quadratic source dependency changed")


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location("frozen_finite_group_quadratic", HERE / "finite_group_boundary_replay.py")
need(SPEC is not None and SPEC.loader is not None, "authenticated finite-group import failed")
F = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F)
C, R, S4, G = F.C, F.R, F.S4, F.G
TWIST_SPEC=importlib.util.spec_from_file_location(
    "frozen_s4_quadratic_geometry", GENERALIZED / "global-s4-resolvent/quadratic_twist_replay.py")
need(TWIST_SPEC is not None and TWIST_SPEC.loader is not None,
     "authenticated quadratic geometry import failed")
TWIST=importlib.util.module_from_spec(TWIST_SPEC)
TWIST_SPEC.loader.exec_module(TWIST)
TWIST_ARTIFACT=json.loads((GENERALIZED / "global-s4-resolvent/quadratic_twist_artifact.json").read_text(encoding="utf-8"))


def source_rows(cut: int) -> list[dict[str, object]]:
    R.integer(cut, 0, 96)
    rows = []
    for row in F.source_rows(cut):
        d, s, double, _, _ = row["class_traces"]
        _, sign, two, std, tw = row["multiplicities"]
        h1 = 6*sign+6*two+4*std+10*tw
        need(2*h1 == 5*d-6*s+double,"twisted source conductor identity failed")
        infinity = (d-double)//2
        need((d-double)%4 == 0,"twisted infinity eigenspaces are not equal integral halves")
        rows.append({"grade":row["grade"],"multiplicities":row["multiplicities"],
                     "h0_h1_h2":[0,h1,0],"conductor":2*d+h1,
                     "kappa":h1//2,"infinity_dimension":infinity,
                     "zero_stalk_dimension":0,
                     "comparison_untwisted_h0_h1_h2":row["h0_h1_h2"]})
    return rows


def field_parameter(q: int) -> int:
    R.integer(q,5,49)
    need(q in (5,7,25,49),"bounded residue fields required")
    return q


def infinity_trace(q: int, grade: int, power: int) -> int:
    q=field_parameter(q)
    R.integer(grade,0,96)
    R.integer(power,1,12)
    dimension=source_rows(grade)[grade]["infinity_dimension"]
    return dimension if q%4==1 or power%2==0 else 0


def infinity_polynomial(q: int, grade: int) -> list[int]:
    q=field_parameter(q)
    R.integer(grade,0,6)
    dimension=source_rows(grade)[grade]["infinity_dimension"]
    order=1 if q%4==1 else 2
    exponent=dimension//order
    out=[0]*(dimension+1)
    for k in range(exponent+1):
        out[order*k]=(-1)**k*comb(exponent,k)
    return out


def infinity_control(q: int, grade: int) -> dict[str, object]:
    q=field_parameter(q)
    R.integer(grade,0,6)
    polynomial=infinity_polynomial(q,grade)
    traces=infinity_trace(q,grade,1),infinity_trace(q,grade,2)
    need(S4.P.local_sums_from_polynomial(polynomial,2)==[-value for value in traces],
         "twisted infinity determinant loses a Frobenius power")
    return {"Q":q,"grade":grade,"dimension":len(polynomial)-1,
            "first_two_traces":list(traces),"local_denominator":polynomial,
            "zero_first_trace_does_not_mean_zero_stalk":traces[0]==0 and traces[1]>0}


def finite_grade_log(panel, z: Fraction, T: Fraction, cut: int):
    q=panel["p"]
    z,T=G.parameters(q,z,T)
    R.integer(cut,1,24)
    polynomials=panel["twisted_polynomials"]
    need(polynomials["tw"] is not None,"full degree-ten source is unavailable for this panel")
    total=Fraction(0),Fraction(0)
    for n,row in enumerate(source_rows(cut)[1:],1):
        u=T*z**n
        for name,weight in zip(("sign","two","std","tw"),row["multiplicities"][1:]):
            value=sum((c*u**i for i,c in enumerate(polynomials[name])),Fraction(0))
            interval=C.weighted_log(value,weight)
            total=total[0]+interval[0],total[1]+interval[1]
    return C.rounded(total)


def cohomology_powers(panel, cut: int) -> list[list[int]]:
    R.integer(cut,1,48)
    polynomials=panel["twisted_polynomials"]
    if polynomials["tw"] is None:
        need(cut<=4,"partial p7 source does not determine higher tw Frobenius traces")
    rows=[]
    for name in ("sign","two","std","tw"):
        poly=polynomials[name]
        if poly is None:
            poly=panel["tw_prefix_mod_T5"]
        rows.append(S4.P.local_sums_from_polynomial(poly,cut))
    return rows


def power_log(panel,z: Fraction,T: Fraction,cut: int) -> Fraction:
    z,T=G.parameters(panel["p"],z,T)
    sums=cohomology_powers(panel,cut)
    total=Fraction(0)
    for m in range(1,cut+1):
        total+=T**m*sum((a*row[m-1] for a,row in zip(F.sectors(z**m)[1:],sums)),Fraction(0))/m
    return total


def grade_tail(q: int,z: Fraction,T: Fraction,cut: int) -> Fraction:
    z,T=G.parameters(q,z,T)
    R.integer(cut,1,24)
    dimensions=F.source_sequences(cut)[0]
    remainder=F.class_values(z)[0]-sum((d*z**n for n,d in enumerate(dimensions)),Fraction(0))
    return 6*q*T*remainder/(1-q*T*z**(cut+1))


def power_tail(q: int,z: Fraction,T: Fraction,cut: int) -> Fraction:
    z,T=G.parameters(q,z,T)
    R.integer(cut,1,48)
    h=q*T*z
    cr=(F.class_values(z)[0]-1)/z
    return 6*cr*h**(cut+1)/((cut+1)*(1-h))


def determinant_control(panel,z: Fraction,T: Fraction,grade_cut=16,power_cut=24):
    z,T=G.parameters(panel["p"],z,T)
    grade=finite_grade_log(panel,z,T,grade_cut)
    ge=grade_tail(panel["p"],z,T,grade_cut)
    power=power_log(panel,z,T,power_cut)
    pe=power_tail(panel["p"],z,T,power_cut)
    need(grade[0]-ge<=power+pe and grade[1]+ge>=power-pe,
         "independent quadratic-source determinant enclosures disagree")
    return {"z":C.qjson(z),"T":C.qjson(T),"grade_cut":grade_cut,"power_cut":power_cut,
            "grade_log":C.interval_json(grade),"proved_grade_tail":C.qjson(ge),
            "power_log":C.qjson(power),"proved_power_tail":C.qjson(pe),
            "grade_zero_factor":1,"full_polynomial_source":True,
            "inside_initial_Euler_disk":panel["p"]*T<1}


def signed_constant(panel,order: int,T: Fraction,cut=24):
    R.integer(order,1,12)
    R.integer(cut,1,48)
    T=C.exact(T)
    q=panel["p"]
    need(0<T and q*T<1,"strict positive arithmetic disk required")
    sums=cohomology_powers(panel,cut)
    delta=[sum(d*row[m] for d,row in zip((1,2,3,3),sums)) for m in range(cut)]
    middle=sum((Fraction(5,12)*delta[m-1]*T**m/m**7
                for m in range(order,cut+1,order)),Fraction(0))
    h=q*T
    error=25*h**(cut+1)/((cut+1)**7*(1-h))
    return {"root_order":order,"power_cut":cut,"source_Delta_sequence":delta,
            "constant_interval":C.interval_json((middle-error,middle+error)),
            "proved_tail":C.qjson(error),
            "full_rank_ten_source":panel["twisted_polynomials"]["tw"] is not None}


def native_panel(index: int) -> dict[str, object]:
    R.integer(index,0,2)
    return _native_panel(index)


@cache
def _native_panel(index: int) -> dict[str, object]:
    frozen=TWIST_ARTIFACT["panels"][index]
    rows=[TWIST.count_source(TWIST.S.make_field(frozen["p"],m),frozen["b"],frozen["c"])
          for m in (1,2)]
    need(json.dumps(rows,sort_keys=True)==json.dumps(frozen["rows"][:2],sort_keys=True),
         "bounded quadratic source recount differs from frozen primitive source")
    return {"id":frozen["id"],"p":frozen["p"],"b":frozen["b"],"c":frozen["c"],
            "primitive_rows":rows,"twisted_polynomials":frozen["twisted_polynomials"],
            "tw_prefix_mod_T5":frozen["tw_prefix_mod_T5"],
            "frozen_extension_degrees":[row["extension"] for row in frozen["rows"]],
            "full_degree_ten_available":frozen["full_degree_ten_available"],
            "degree_ten_held_out_extensions":frozen["degree_ten_held_out_extensions"]}


def native_trace(row,z: Fraction) -> Fraction:
    values=F.class_values(z)
    by_class=dict(zip(F.CLASSES,values))
    by_class["branch_split"]=(values[0]+values[1])/2
    by_class["branch_nonsplit"]=(values[1]+values[2])/2
    total=Fraction(0)
    count=0
    for key,number in row["finite_class_census"].items():
        label,chi=key.rsplit(":chi=",1)
        character=int(chi)
        need(character in (-1,0,1),"invalid primitive quadratic character")
        total+=number*character*by_class[label]
        count+=number
    need(count==row["field_order"],"quadratic base fibre census lost points")
    if row["field_order"]%4==1:
        total+=(values[0]-values[2])/2
    return total


def fibre_controls(panel) -> list[dict[str, object]]:
    rows=[]
    grades=source_rows(12)
    powers=cohomology_powers(panel,2)
    for primitive in panel["primitive_rows"]:
        m=primitive["extension"]
        local=[primitive["twisted_stalk_sums"][name] for name in F.NAMES]
        need(local[0]==0,"quadratic P1 grade-zero source failed")
        need(local[1:]==[row[m-1] for row in powers],"primitive twisted traces disagree with frozen polynomial source")
        regular=sum(d*t for d,t in zip(F.TABLE[0],local))
        need(regular==primitive["signed_regular_source_sum"],"genus49 regular anti trace mismatch")
        infinity=[infinity_trace(primitive["field_order"],n,1) for n in range(13)]
        source_infinity=[primitive["twisted_infinity_stalk_traces"][name] for name in F.NAMES]
        for n,row in enumerate(grades):
            need(sum(a*b for a,b in zip(row["multiplicities"],source_infinity))==infinity[n],
                 "whole-source infinity trace differs from primitive constituents")
        rational=[]
        for z in (Fraction(1,10),Fraction(1,4),Fraction(-1,4)):
            w=z**m
            actual=native_trace(primitive,w)
            expected=sum((a*b for a,b in zip(F.sectors(w),local)),Fraction(0))
            need(actual==expected,"complete quadratic-source graded trace mismatch")
            rational.append({"z":C.qjson(z),"required_weight":C.qjson(w),"actual_trace":C.qjson(actual)})
        rows.append({"extension":m,"field_order":primitive["field_order"],
                     "full_fibre_controls":rational,"infinity_grade_traces":infinity,
                     "signed_regular_source_sum":regular,
                     "genus49_points":primitive["Ztilde_points_from_normalized_joint_regular_character"]})
    return rows


def finite_L(panel,value: Fraction,grade: int) -> Fraction:
    value=C.exact(value)
    R.integer(grade,0,3)
    need(panel["full_degree_ten_available"],"complete twisted finite source unavailable")
    result=Fraction(1)
    mult=source_rows(grade)[grade]["multiplicities"]
    for name,weight in zip(("sign","two","std","tw"),mult[1:]):
        poly=panel["twisted_polynomials"][name]
        factor=sum((coefficient*value**i for i,coefficient in enumerate(poly)),Fraction(0))
        result*=factor**weight
    return result


def finite_duality(panel,cut: int) -> dict[str, object]:
    R.integer(cut,0,3)
    q,z,T=panel["p"],Fraction(2,3),Fraction(1,13)
    rows=source_rows(cut)
    K=sum(row["kappa"] for row in rows)
    W=sum(row["grade"]*row["kappa"] for row in rows)
    left,right=Fraction(1),Fraction(1)
    for n in range(cut+1):
        left*=finite_L(panel,T*z**n,n)
        right*=finite_L(panel,1/(q*T*z**n),n)
    need(left==Fraction(q)**K*T**(2*K)*z**(2*W)*right,
         "actual twisted finite functional equation failed")
    return {"cut":cut,"K":K,"W":W,"source_functional_equation":True}


def build_payload() -> dict[str, object]:
    authenticate_frozen()
    panels=[]
    for index in range(3):
        panel=native_panel(index)
        full=panel["full_degree_ten_available"]
        cut=24 if full else 4
        panels.append({"source_id":panel["id"],"parameters":[panel["p"],panel["b"],panel["c"]],
                       "primitive_recount_degrees":[1,2],
                       "frozen_extension_degrees":panel["frozen_extension_degrees"],
                       "full_degree_ten_available":full,
                       "degree_ten_held_out_extensions":panel["degree_ten_held_out_extensions"],
                       "fibre_controls":fibre_controls(panel),
                       "finite_duality":[finite_duality(panel,n) for n in range(3)] if full else None,
                       "completed_determinant_controls":[determinant_control(panel,z,T)
                           for z,T in ((Fraction(1,4),Fraction(1,10)),(Fraction(1,10),Fraction(1,2)))] if full else None,
                       "signed_constants":[signed_constant(panel,h,Fraction(1,2*panel["p"]),cut) for h in range(1,5)],
                       "partial_source_limit":None if full else "four independent tw traces; no complete degree-ten determinant claimed"})
    return {"schema":"quadratic-signed-source-boundary-s4-v1",
            "provenance":{"pins":[list(pin) for pin in PINS],
                          "owned_sha256_lf":{name:digest((HERE/name).read_bytes()) for name in OWNED}},
            "source_panels":panels,"source_grade_rows":source_rows(24),
            "diagonal_infinity_controls":[infinity_control(q,n) for q in (5,7,25,49) for n in (0,1,2)],
            "primitive_field_orders_recounted_here":[5,25,7,49],
            "not_claimed":["zero first trace implies zero stalk","p7 complete degree-ten polynomial",
                           "positive signed regular counts","every root constant is nonzero",
                           "arbitrary complex-T natural boundary","same exponential Lie operator"]}


def check_payload(candidate: object) -> None:
    need(json.dumps(candidate,sort_keys=True)==json.dumps(build_payload(),sort_keys=True),
         "quadratic source fixture differs from authenticated complete replay")


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write",action="store_true")
    group.add_argument("--check",action="store_true")
    args=parser.parse_args()
    payload=build_payload()
    if args.write:
        FIXTURE.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8",newline="\n")
    else:
        need(json.dumps(json.loads(FIXTURE.read_text(encoding="utf-8")),sort_keys=True)
             ==json.dumps(payload,sort_keys=True),"quadratic source fixture mismatch")
    print("PASS actual S4 quadratic source, diagonal inertia and signed completion")


if __name__=="__main__":
    main()
