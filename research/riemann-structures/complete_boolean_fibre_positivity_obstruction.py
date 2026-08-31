#!/usr/bin/env python3
"""Complete canonical rough-fibre rigidity, positive readout, and decoder boundary."""

from __future__ import annotations

import argparse
import json
import subprocess
import types
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
from math import comb, gcd, isqrt, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "COMPLETE_BOOLEAN_FIBRE_POSITIVITY_OBSTRUCTION.md"
FIXTURE = HERE / "complete_boolean_fibre_positivity_obstruction.json"
TEST = ROOT / "tests" / "test_complete_boolean_fibre_positivity_obstruction.py"
EA = "5ef9a0800e7d0f03bfef1ad4ba467f8843a90058"
EA_PATH = "research/riemann-structures/euler_activation_source_adapter.py"
DENSE = "1fea3c9ce079325d19f5b43c6daa59c76afff921"
DENSE_PATH = "research/riemann-structures/dense_owner_principal_coefficient_family.py"
DENSE_JSON = "research/riemann-structures/dense_owner_principal_coefficient_family.json"
DENSE_PRIMES = "research/riemann-structures/dense_owner_principal_primes.json"
PREDECESSOR = "5b25f2dace65dd4d46e16d566f2dc7a34b98f41d"
SOURCES = {
    (EA,EA_PATH):"f8248cd97c4fc72ad4034d9baf83cec91396f27e",
    (DENSE,DENSE_PATH):"93a9a117068164df7745c117c1007b5f4f060bea",
    (DENSE,DENSE_JSON):"1c289fb3c7d8e959b010267751834ebad6914ec5",
    (DENSE,DENSE_PRIMES):"148303e449046c2282d0851166d5b0286058908b",
    (DENSE,"research/riemann-structures/DENSE_OWNER_PRINCIPAL_COEFFICIENT_FAMILY.md"):
        "c1eeffbc6aa814f860875d58205e97a4d945dc2c",
    (PREDECESSOR,"research/l-families/atlas/function_field/FFPS_CANONICAL_BOOLEAN_PRINCIPAL_DIAGONAL.md"):
        "47014e5aeadccd6f9e64eae061b2ef5f0e86bfdb",
    (PREDECESSOR,"research/exploratory/NATIVE_BOOLEAN_DECODER_DIAGNOSTIC.md"):
        "7cebffd3b6b0db96128755e392f622029a74435a",
    ("86cac1d64364015ec2cc0f8fbb6fc75dc041c12b", "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md"):
        "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    ("86cac1d64364015ec2cc0f8fbb6fc75dc041c12b", "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md"):
        "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
    ("ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc", "claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md"):
        "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
}
MAX_BYTES = 262144


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value,sort_keys=True,separators=(",", ":"),allow_nan=False)


def source_bytes(key):
    require(key in SOURCES,"frozen source identity")
    ref = f"{key[0]}:{key[1]}"
    size = int(subprocess.run(["git","cat-file","-s",ref],cwd=ROOT,
                             capture_output=True,text=True,check=True).stdout)
    require(0 < size <= MAX_BYTES,"source byte cap")
    raw = subprocess.run(["git","show",ref],cwd=ROOT,capture_output=True,check=True).stdout
    require(len(raw) == size,"source byte count")
    digest = sha1(b"blob "+str(size).encode()+b"\0"+raw).hexdigest()
    require(digest == SOURCES[key],"exact frozen Git blob")
    return raw


def load_primitive(key,raw):
    require(key in ((EA,EA_PATH),(DENSE,DENSE_PATH)),"permitted source executable")
    require(type(raw) is bytes and len(raw) <= MAX_BYTES,"bounded source executable bytes")
    digest = sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
    require(digest == SOURCES[key],"authenticated source executable")
    module = types.ModuleType("frozen_complete_boolean_primitive")
    module.__file__ = str(ROOT/key[1])
    # Only exact independently rehashed frozen Git source is executed.
    exec(compile(raw,f"{key[0]}:{key[1]}","exec"),module.__dict__)  # noqa: S102
    return module


def prime(value):
    require(type(value) is int and 2 <= value <= 10000,"bounded physical prime")
    require(all(value % d for d in range(2,isqrt(value)+1)),"exact prime verification")
    return value


def kernel_transform_identity():
    zero = (Fraction(0),Fraction(0))

    def add(x,y):
        return x[0]+y[0],x[1]+y[1]

    def scale(x,k):
        return x[0]*k,x[1]*k

    def multiply(x,y):
        return x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0]

    constants = ((8,0),(-8,-8),(0,8))
    roots = ((-4,0),(0,4),(-2,0))
    endpoints = ((1,0),(0,1),(2,0),(0,2))
    a,b = [zero]*4,[zero]*4
    for j,(constant,root) in enumerate(zip(constants,roots,strict=True)):
        a[j] = add(a[j],scale(constant,-1))
        a[j+1] = add(a[j+1],constant)
        b[j] = add(b[j],scale(multiply(root,endpoints[j]),-1))
        b[j+1] = add(b[j+1],multiply(root,endpoints[j+1]))
    c = [zero]*4
    for i,x in enumerate(((1,0),(-2,0),(1,0))):
        for j,y in enumerate(((-1,0),(0,1))):
            c[i+j] = add(c[i+j],scale(multiply(x,y),4))
    require(a == [scale(x,2) for x in c] and b == [scale(x,-1) for x in c],
            "literal kernel Mellin numerator factorization")
    def serialize(polynomial):
        return [[str(x),str(y)] for x,y in polynomial]
    return {"basis":"1,sqrt(2)","A_numerator":serialize(a),
            "B_numerator":serialize(b),"C_polynomial":serialize(c),
            "factored_C":"4(r-1)^2(sqrt(2)r-1)",
            "Mellin_transform":"(s+1)C(2^s)/(s(s+1/2))",
            "first_slope_divided_by_log2_squared":["-8","8"],
            "Fourier_zero_order_at_zero":1,
            "small_interval_measure_asymptotic":"alpha^2 delta^3/(3pi)",
            "floating_evaluations":False}


def rough_parity(algebra,labels,cutoff):
    require(type(cutoff) is int and 2 <= cutoff <= 1024,"bounded exact cutoff")
    require(type(labels) is tuple and 1 <= len(labels) <= 4,"bounded rough support")
    require(len(set(labels)) == len(labels),"squarefree distinct support")
    for p in labels:
        require(prime(p) > cutoff,"every core prime exceeds cutoff")
    rows = algebra.boolean_rows(labels,cutoff)
    expected = 1+(-1)**len(labels)
    require(rows["balanced"] == expected and rows["twice_truncated_mu"] == 0
            and rows["truncated_double_convolution"] == 1,
            "complete rough Boolean parity identity")
    if len(labels) >= 4:
        require(6*prod(labels)**2 > 16*cutoff**6,
                "four rough factors excluded by physical horizon and minimum owner")
    return {"labels":list(labels),"cutoff":cutoff,"rows":rows,
            "balanced":expected,"canonical_coefficient":str(Fraction(expected,comb(len(labels)+2,2))),
            "depth_four_horizon_excluded":len(labels) >= 4}


def zero_cofactor_chart(algebra):
    cutoff,g,ell,extra,rho = 256,257,263,269,271
    owners = (2,3,241,251)
    labels = (g,ell,extra,rho,*owners)
    require(len(set(labels)) == len(labels) and 67 not in labels,"clean zero cofactor chart")
    for p in labels:
        prime(p)
    p,q = prod(owners[:2]),prod(owners[2:])
    c,d = ell*extra,rho
    a,b = g*c,g*d
    n,m = p*a*a,q*b*b
    horizon = cutoff**6
    require(ell < extra and ell < rho and min((ell,extra)) == ell,
            "unchanged least-prime phase under genuine extra cofactor")
    require(gcd(c,d) == gcd(g,c*d) == gcd(p,q*a*b) == gcd(q,p*a*b) == 1,
            "native clean tuple")
    require(n <= 16*horizon and m <= 16*horizon
            and Fraction(1,8) < Fraction(n,m) < 8 and p <= a and q <= b,
            "complete candidate physical mask")
    left = rough_parity(algebra,(g,ell,extra),cutoff)
    right = rough_parity(algebra,(g,rho),cutoff)
    lh,rh = left["rows"]["nonzero_balanced_histories"],right["rows"]["nonzero_balanced_histories"]
    require(len(lh) == 12 and len(rh) == 2,"complete zero cofactor history coverage")
    coefficients = [Fraction(x["coefficient"]*y["coefficient"],comb(5,2)*comb(4,2))
                    for x,y in product(lh,rh)]
    require(sum(coefficients,Fraction(0)) == 0
            and coefficients.count(Fraction(1,60)) == coefficients.count(Fraction(-1,60)) == 12,
            "actual complete cofactor row cancels before physical readout")
    return {"U":cutoff,"Y":horizon,"P":p,"Q":q,"g":g,"c":c,"d":d,
            "ell":ell,"rho":rho,"N":n,"M":m,"ratio":str(Fraction(n,m)),
            "left":left,"right":right,"bilateral_histories":len(coefficients),
            "signed_bilateral_coefficients_before_physical_factor":[str(x) for x in coefficients],
            "complete_canonical_coefficient":"0",
            "literal_history_diagonal":str(sum((x*x for x in coefficients),Fraction(0))/Fraction(n*m)),
            "cofactor_deleted_by_mask":False}


def build():
    raw = {key:source_bytes(key) for key in SOURCES}
    algebra = load_primitive((EA,EA_PATH),raw[(EA,EA_PATH)])
    dense = load_primitive((DENSE,DENSE_PATH),raw[(DENSE,DENSE_PATH)])
    inherited = json.loads(raw[(DENSE,DENSE_JSON)])
    require(inherited["schema"] == "riemann.dense_owner_principal_coefficient_family.v1",
            "frozen dense source schema")
    dense_record = dense.record(algebra,json.loads(raw[(DENSE,DENSE_PRIMES)]))
    require(canonical(dense_record) == canonical(inherited["record"]),
            "independent replay of complete dense owner/class source")
    parity = [rough_parity(algebra,(257,263,269,271)[:k],256) for k in range(1,5)]
    require([r["balanced"] for r in parity] == [0,2,0,2],"rough parity and horizon combination")
    hashes = {}
    for path in (NOTE,Path(__file__),TEST):
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES,"owned file cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(data.replace(b"\r\n",b"\n")).hexdigest()
    result = {"schema":"riemann.complete_boolean_fibre_positivity.v1",
              "sources":[{"commit":key[0],"path":key[1],"git_blob":blob} for key,blob in SOURCES.items()],
              "source_hashes":hashes,"rough_parity_controls":parity,
              "exact_kernel_transform":kernel_transform_identity(),
              "genuine_zero_cofactor_chart":zero_cofactor_chart(algebra),
              "inherited_dense_source_record":dense_record,
              "candidate":"COMPLETE_CLEAN_CANONICAL_BOOLEAN_TUPLE_FAMILY",
              "mask":"N,M<=16Y;1/8<N/M<8;P<=gc;Q<=gd",
              "mask_time_independent_nonnegative":True,
              "dense_block_mask_equals_one":True,
              "all_selected_fibre_core_cofactors_classified":True,
              "positive_frequency_cone":"abs(t)<1/(2log8)",
              "cone_measure_positivity":"PROVED_BY_COMPACT_SUPPORT_ENTIRE_FOURIER_AND_NONZERO_KERNEL",
              "cone_measure_numerically_estimated":False,
              "complete_candidate_moment_lower":"Omega(Y^(1/2)/log(Y)^11)",
              "complete_unmasked_candidate_moment_lower":"Omega(Y^(1/2)/log(Y)^14)",
              "complete_candidate_matching_upper_claimed":False,
              "conditional_native_subpower_decoder_error_lower":"Omega(Y^(1/4)/log(Y)^(11/2))",
              "conditional_unmasked_decoder_error_lower":"Omega(Y^(1/4)/log(Y)^7)",
              "full_native_gamma_identification_asserted":False,
              "full_native_moment_lower_bound_asserted":False,"RH_conclusion":False}
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write",action="store_true")
    group.add_argument("--check",action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        FIXTURE.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES,"artifact cap")
        candidate = json.loads(FIXTURE.read_text(encoding="utf-8"))
        require(canonical(candidate) == canonical(result),"strict typed canonical replay")
    print(json.dumps({"status":"PASS","proof_object_sha256":result["proof_object_sha256"]}))


if __name__ == "__main__":
    main()
