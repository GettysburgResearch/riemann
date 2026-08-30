"""Actual quadratic graded algebra, colour law and positive scalar resonances."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from fractions import Fraction
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
PINS = (
    ("c0b197918936d8ad360f462702855020fb26ac67", "quadratic_source_boundary_replay.py",
     "ff1e2d706b6e2cbd1cf5cd80a57f45bfe05e80f1",
     "eee8c86ec416691d5c1da7a28ae81d6ede973250350519e3a7ce92ef64cfda4a"),
    ("c0b197918936d8ad360f462702855020fb26ac67", "QUADRATIC_SIGNED_SOURCE_BOUNDARY.md",
     "c01204c7467e1663fd10722c06fd6efd69dbbe81",
     "ff388a6f83788c8ef7fa8d3b39d48ab27b4b04206bdc816c677308d33da54a57"),
)
OWNED = ("COHERENT_QUADRATIC_GRADED_ALGEBRA.md", "COHERENT_QUADRATIC_REPLAY.md",
         "coherent_quadratic_replay.py", "tests/test_coherent_quadratic.py")
FIXTURE = HERE / "coherent_quadratic.verification.json"


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
        need(resolved == blob, "coherent quadratic dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "coherent quadratic dependency hash mismatch")
        need(digest((HERE / name).read_bytes()) == expected,
             "working coherent quadratic dependency changed")


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location("frozen_quadratic_coherent", HERE / "quadratic_source_boundary_replay.py")
need(SPEC is not None and SPEC.loader is not None, "authenticated quadratic import failed")
Q = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(Q)
F, C, R, G = Q.F, Q.C, Q.R, Q.G


def colour_product(n: int, epsilon: int, m: int, eta: int) -> tuple[int, int]:
    R.integer(n, 0, 48)
    R.integer(m, 0, 48)
    R.integer(epsilon, 0, 1)
    R.integer(eta, 0, 1)
    return n + m, (epsilon + eta) % 2


def source_rows(cut: int) -> list[dict[str, object]]:
    R.integer(cut, 0, 96)
    old, fixed = F.source_rows(cut), Q.source_rows(cut)
    rows = []
    for n, (untwisted, twisted) in enumerate(zip(old, fixed)):
        selected = twisted if n % 2 else untwisted
        rows.append({"grade": n, "colour": n % 2,
                     "multiplicities": selected["multiplicities"],
                     "h0_h1_h2": selected["h0_h1_h2"],
                     "kappa": selected["kappa"],
                     "source": "fixed_quadratic" if n % 2 else "untwisted",
                     "fixed_module_h0_h1_h2": twisted["h0_h1_h2"],
                     "principal_pole_multiplicity": selected["h0_h1_h2"][0]})
    return rows


def parity_sectors(z: Fraction):
    plus, minus = F.sectors(z), F.sectors(-C.exact(z))
    return tuple((a + b) / 2 for a, b in zip(plus, minus)), tuple((a - b) / 2 for a, b in zip(plus, minus))


def infinity_trace(q: int, grade: int, power: int) -> int:
    q = Q.field_parameter(q)
    R.integer(grade, 0, 96)
    R.integer(power, 1, 12)
    if grade % 2:
        return Q.infinity_trace(q, grade, power)
    d, transposition, double, _, _ = F.source_rows(grade)[grade]["class_traces"]
    return (d + double) // 2 if q % 4 == 1 or power % 2 == 0 else transposition


def infinity_polynomial(q: int, grade: int) -> list[int]:
    q = Q.field_parameter(q)
    R.integer(grade, 0, 2)
    first, dimension = infinity_trace(q, grade, 1), infinity_trace(q, grade, 2)
    need((dimension - first) % 2 == 0, "infinity eigenvalue multiplicities not integral")
    positive, negative = (dimension + first) // 2, (dimension - first) // 2
    out = [0] * (dimension + 1)
    for i in range(positive + 1):
        for j in range(negative + 1):
            out[i + j] += (-1)**i * comb(positive, i) * comb(negative, j)
    need(F.S4.P.local_sums_from_polynomial(out, 2) == [-first, -dimension],
         "coherent infinity polynomial loses a Frobenius power")
    return out


def native_pair(index: int):
    R.integer(index, 0, 2)
    old, fixed = F.native_panel(index), Q.native_panel(index)
    need((old["p"], old["b"], old["c"]) == (fixed["p"], fixed["b"], fixed["c"]),
         "old and quadratic source parameters disagree")
    return old, fixed


def power_data(index: int, cut: int):
    R.integer(index, 0, 2)
    R.integer(cut, 1, 48)
    old, fixed = native_pair(index)
    old_data, quadratic = F.power_data(old, cut), Q.cohomology_powers(fixed, cut)
    out = []
    for m, (local, zcount) in enumerate(old_data, 1):
        twisted = [0] + [row[m - 1] for row in quadratic]
        delta = sum(d * t for d, t in zip(F.TABLE[0], twisted))
        joint = zcount + delta
        opposite = 2 * zcount - joint
        need(0 <= joint <= 2 * zcount and opposite >= 0,
             "actual quadratic double-cover scalar weights lost positivity")
        if m <= 2:
            row = fixed["primitive_rows"][m - 1]
            need(joint == row["Ztilde_points_from_normalized_joint_regular_character"],
                 "joint source trace differs from normalized primitive count")
            need(delta == row["signed_regular_source_sum"],
                 "quadratic signed source trace differs from primitive count")
        out.append({"extension": m, "untwisted_local": local, "fixed_local": twisted,
                    "Z_points": zcount, "Ztilde_points": joint,
                    "opposite_scalar_points": opposite,
                    "constant_twist_points": joint if m % 2 == 0 else opposite})
    return out


def native_trace(old, fixed, z: Fraction) -> Fraction:
    z = C.exact(z)
    return (F.native_trace(old, z) + F.native_trace(old, -z)
            + Q.native_trace(fixed, z) - Q.native_trace(fixed, -z)) / 2


def fibre_controls(index: int):
    old, fixed = native_pair(index)
    data = power_data(index, 2)
    rows = []
    for m, (oldrow, fixedrow, powers) in enumerate(zip(old["primitive_rows"], fixed["primitive_rows"], data), 1):
        probes = []
        for z in (Fraction(1, 10), Fraction(1, 4), Fraction(-1, 4)):
            w = z**m
            even, odd = parity_sectors(w)
            actual = native_trace(oldrow, fixedrow, w)
            expected = sum((a*b+c*d for a,b,c,d in zip(even,powers["untwisted_local"],odd,powers["fixed_local"])), Fraction(0))
            need(actual == expected, "full coherent source fibre sum differs from cohomology")
            probes.append({"z": C.qjson(z), "required_weight": C.qjson(w), "trace": C.qjson(actual)})
        rows.append({"extension": m, "field_order": fixedrow["field_order"],
                     "probes": probes, "constant_twist_points": powers["constant_twist_points"],
                     "Z_points": powers["Z_points"], "Ztilde_points": powers["Ztilde_points"],
                     "opposite_scalar_points": powers["opposite_scalar_points"]})
    return rows


def positive_grade_log(index: int, z: Fraction, T: Fraction, cut: int):
    old, fixed = native_pair(index)
    z,T = G.parameters(old["p"], z,T)
    R.integer(cut, 1, 24)
    need(fixed["full_degree_ten_available"], "complete quadratic determinant unavailable")
    total = Fraction(0), Fraction(0)
    for n,row in enumerate(source_rows(cut)[1:],1):
        u=T*z**n
        if n%2:
            pairs = [(fixed["twisted_polynomials"][name], weight)
                     for name,weight in zip(("sign","two","std","tw"),row["multiplicities"][1:])]
        else:
            pairs = [(old["polynomials"][name], weight)
                     for name,weight in zip(("D","R","E","tw"),row["multiplicities"][1:])]
            pairs += [([1,-1],-row["multiplicities"][0]),([1,-old["p"]],-row["multiplicities"][0])]
        for polynomial, weight in pairs:
            value=sum((coefficient*u**i for i,coefficient in enumerate(polynomial)),Fraction(0))
            interval=C.weighted_log(value,weight)
            total=total[0]+interval[0],total[1]+interval[1]
    return C.rounded(total)


def positive_power_log(index: int,z: Fraction,T: Fraction,cut: int) -> Fraction:
    old,_ = native_pair(index)
    z,T = G.parameters(old["p"],z,T)
    total=Fraction(0)
    for row in power_data(index,cut):
        m=row["extension"]
        even,odd=parity_sectors(z**m)
        value=sum((a*b+c*d for a,b,c,d in zip(even,row["untwisted_local"],odd,row["fixed_local"])),Fraction(0))
        total+=T**m*(value-(old["p"]**m+1))/m
    return total


def determinant_control(index: int,z: Fraction,T: Fraction,grade_cut=16,power_cut=24):
    old,_=native_pair(index)
    q=old["p"]
    z,T=G.parameters(q,z,T)
    need((1-T)*(1-q*T)!=0,"explicit grade-zero principal pole")
    grade=positive_grade_log(index,z,T,grade_cut)
    ge=Q.grade_tail(q,z,T,grade_cut)
    power=positive_power_log(index,z,T,power_cut)
    pe=Q.power_tail(q,z,T,power_cut)
    need(grade[0]-ge<=power+pe and grade[1]+ge>=power-pe,
         "independent coherent determinant enclosures disagree")
    return {"z":C.qjson(z),"T":C.qjson(T),"grade_cut":grade_cut,"power_cut":power_cut,
            "positive_grade_log":C.interval_json(grade),"proved_grade_tail":C.qjson(ge),
            "positive_power_log":C.qjson(power),"proved_power_tail":C.qjson(pe),
            "separate_signed_grade_zero_factor":C.qjson(1/((1-T)*(1-q*T))),
            "inside_initial_Euler_disk":q*T<1}


def finite_L(index: int,value: Fraction,grade: int) -> Fraction:
    R.integer(grade,0,3)
    old,fixed=native_pair(index)
    return Q.finite_L(fixed,value,grade) if grade%2 else F.finite_L(old,value,grade)


def finite_duality(index: int,cut: int):
    R.integer(cut,0,3)
    old,_=native_pair(index)
    q,z,T=old["p"],Fraction(2,3),Fraction(1,13)
    rows=source_rows(cut)
    K=sum(row["kappa"] for row in rows)
    W=sum(row["grade"]*row["kappa"] for row in rows)
    left,right=Fraction(1),Fraction(1)
    for n in range(cut+1):
        left*=finite_L(index,T*z**n,n)
        right*=finite_L(index,1/(q*T*z**n),n)
    need(left==Fraction(q)**K*T**(2*K)*z**(2*W)*right,"coherent finite source duality failed")
    return {"cut":cut,"K":K,"W":W,"source_functional_equation":True}


def boundary_constant(index: int,order: int,T: Fraction,cut=24):
    R.integer(order,1,2)
    T=C.exact(T)
    old,_=native_pair(index)
    q=old["p"]
    need(0<T and q*T<1,"strict positive arithmetic disk required")
    middle=Fraction(0)
    missing=Fraction(0)
    for row in power_data(index,cut):
        m=row["extension"]
        use_opposite=order==2 and m%2==1
        points=row["opposite_scalar_points"] if use_opposite else row["Ztilde_points"]
        term=Fraction(5,24)*points*T**m/m**7
        middle+=term
        if use_opposite:
            missing+=term
    h=q*T
    error=20*h**(cut+1)/((cut+1)**7*(1-h))
    return {"root_order":order,"power_cut":cut,"constant_interval":C.interval_json((middle-error,middle+error)),
            "proved_tail":C.qjson(error),"omitted_by_identity_only":C.qjson(missing)}


def radial_control(index: int,order: int,radius: Fraction,T: Fraction,cut=24):
    R.integer(order,1,2)
    radius,T=C.exact(radius),C.exact(T)
    old,_=native_pair(index)
    q=old["p"]
    need(Fraction(9,10)<=radius<1 and 0<T and q*T<1,"bounded radial disk required")
    z=radius if order==1 else -radius
    total=Fraction(0)
    for row in power_data(index,cut):
        m=row["extension"]
        even,odd=parity_sectors(z**m)
        total+=T**m*sum((a*b+c*d for a,b,c,d in zip(even,row["untwisted_local"],odd,row["fixed_local"])),Fraction(0))/m
    middle=(1-radius)**6*total
    h=q*T
    error=20*h**(cut+1)/((cut+1)*(1-h))
    target=boundary_constant(index,order,T,cut)
    lo,hi=[Fraction(*pair) for pair in target["constant_interval"]]
    need(lo>0 and middle-error>hi/2,"radial interval did not exceed half actual positive limit")
    return {"root_order":order,"radius":C.qjson(radius),"T":C.qjson(T),
            "observed_interval":C.interval_json((middle-error,middle+error)),
            "boundary_constant":target,"above_half_actual_constant":True}


def build_payload():
    authenticate_frozen()
    panels=[]
    for index in range(3):
        old,fixed=native_pair(index)
        full=fixed["full_degree_ten_available"]
        cut=24 if full else 4
        T=Fraction(1,2*old["p"])
        panels.append({"parameters":[old["p"],old["b"],old["c"]],
                       "full_degree_ten_available":full,"fibre_controls":fibre_controls(index),
                       "scalar_source_rows":power_data(index,cut),
                       "finite_duality":[finite_duality(index,n) for n in range(3)] if full else None,
                       "determinant_controls":[determinant_control(index,z,t)
                           for z,t in ((Fraction(1,4),Fraction(1,10)),(Fraction(1,10),Fraction(1,2)))] if full else None,
                       "positive_constants":[boundary_constant(index,h,T,cut) for h in (1,2)],
                       "radial_controls":[radial_control(index,h,Fraction(999,1000),T) for h in (1,2)] if full else None})
    return {"schema":"coherent-quadratic-graded-source-v1",
            "provenance":{"pins":[list(pin) for pin in PINS],
                          "owned_sha256_lf":{name:digest((HERE/name).read_bytes()) for name in OWNED}},
            "source_grade_rows":source_rows(24),"source_panels":panels,
            "infinity_polynomials":[{"Q":q,"grade":n,"denominator":infinity_polynomial(q,n)} for q in (5,7) for n in range(3)],
            "colour_controls":[{"left":[n,n%2],"right":[m,m%2],"product":list(colour_product(n,n%2,m,m%2))} for n in range(3) for m in range(3)],
            "not_claimed":["fixed twist is closed under its own multiplication","chi once equals chi to the grade",
                           "identity-only scalar resonance on the joint group","p7 full degree-ten determinant",
                           "all-complex-T natural boundary","same exponential Lie operator"]}


def check_payload(candidate: object):
    need(json.dumps(candidate,sort_keys=True)==json.dumps(build_payload(),sort_keys=True),
         "coherent quadratic fixture differs from complete authenticated replay")


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
             "coherent quadratic fixture mismatch")
    print("PASS actual coherent quadratic graded algebra and scalar resonances")


if __name__=="__main__":
    main()
