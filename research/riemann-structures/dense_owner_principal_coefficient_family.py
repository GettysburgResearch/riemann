#!/usr/bin/env python3
"""Dense actual owner sums: principal coefficient moment versus literal diagonal."""

from __future__ import annotations

import argparse
import json
import subprocess
import types
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "DENSE_OWNER_PRINCIPAL_COEFFICIENT_FAMILY.md"
FIXTURE = HERE / "dense_owner_principal_coefficient_family.json"
PRIMES = HERE / "dense_owner_principal_primes.json"
SCOUT = HERE / "dense_owner_principal_scout.py"
TEST = ROOT / "tests" / "test_dense_owner_principal_coefficient_family.py"
EA = "5ef9a0800e7d0f03bfef1ad4ba467f8843a90058"
EA_PATH = "research/riemann-structures/euler_activation_source_adapter.py"
PQR = "57907ac05f7f00f147f6ede570c924ae101afec2"
PQR_PATH = "research/riemann-structures/post_quotient_principal_readout_barrier.py"
SCB = "1623f1924c62035918a94bcacf2ccad7d3bb6cf7"
SCB_PATH = "research/riemann-structures/subcritical_observed_boolean_block.json"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
SOURCES = {
    (EA,EA_PATH):"f8248cd97c4fc72ad4034d9baf83cec91396f27e",
    (PQR,PQR_PATH):"ba6dabaf09f256e1a03f5fa8ad3a96cde3a63d2b",
    (PQR,"research/riemann-structures/POST_QUOTIENT_PRINCIPAL_READOUT_BARRIER.md"):
        "3f10acfa5f7288a357287c017c7d963a0fae9172",
    (SCB,SCB_PATH):"b6464ebbd4560e50d9ad7033d051dc9cddd4a7f4",
    ("6dbab098bb057d76748d12e37900efeff571f8a9", "research/riemann-structures/NATIVE_RESTRICTED_MELLIN_OBSERVABILITY.md"):
        "88989aaa947885df02272c0bb01a31f6d1ac0694",
    ("6dbab098bb057d76748d12e37900efeff571f8a9", "research/riemann-structures/LIVE_FIXED_CONDUCTOR_MULTIPLICITY.md"):
        "c9c5f9e7e1ddab7e9a6aff629165a098fdf597a8",
    ("e365528d750fded282bd3f7261898d8455c41e0a", "research/riemann-structures/SOURCE_FIRST_BOOLEAN_PRINCIPAL_ADAPTER.md"):
        "c37145331aedf3c6a4ec0c70577a66da712a5edd",
    ("ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc", "claims/lemmas/L-102958-ratioeight-comparability-pays-both-opposite-owner-products.md"):
        "3b72653ea5f05405c587be165faf7ab2c52c3f2b",
    (FAMILY,"claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md"):
        "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (FAMILY,"claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md"):
        "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
    ("a30276a5be049749ebb2147f30f000dd5659298b", "research/l-families/atlas/function_field/FFPS_SIGNED_HISTORY_RECOMBINATION.md"):
        "c5f77f48bd19cc9af39698d4de53ae266bd42e17",
}
MAX_BYTES = 262144
LABELS = ("p","q","r","s","g","ell","rho")
LOWER = Fraction(25,11616)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def source_bytes(key):
    require(key in SOURCES,"frozen source identity")
    ref = f"{key[0]}:{key[1]}"
    size = int(subprocess.run(["git","cat-file","-s",ref],cwd=ROOT,
                             capture_output=True,text=True,check=True).stdout)
    require(0 < size <= MAX_BYTES,"source byte cap")
    raw = subprocess.run(["git","show",ref],cwd=ROOT,capture_output=True,check=True).stdout
    require(len(raw) == size,"source byte count")
    digest = sha1(b"blob "+str(size).encode()+b"\0"+raw).hexdigest()
    require(digest == SOURCES[key],"frozen source Git blob")
    return raw


def load_primitive(key,raw):
    require(key in ((EA,EA_PATH),(PQR,PQR_PATH)),"permitted executable identity")
    require(type(raw) is bytes and len(raw) <= MAX_BYTES,"bounded executable bytes")
    digest = sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
    require(digest == SOURCES[key],"authenticated executable Git blob")
    module = types.ModuleType("frozen_dense_owner_primitive")
    module.__file__ = str(ROOT/key[1])
    # Only the fixed, rehashed Git primitive above is executable.
    exec(compile(raw,f"{key[0]}:{key[1]}","exec"),module.__dict__)  # noqa: S102
    return module


def validate_primes(data):
    require(type(data) is dict and type(data["U"]) is int and data["U"] == 1 << 20,
            "fixed bounded replay horizon")
    require(type(data["candidate_cap_per_window"]) is int
            and data["candidate_cap_per_window"] == 200,"bounded acquisition cap")
    require(data["primality"] == "EXACT_TRIAL_DIVISION","fixture acquisition method")
    windows = data["windows"]
    require(type(windows) is dict and set(windows) == set(LABELS),"exact seven source windows")
    u = data["U"]
    selected = {}
    for j,label in enumerate(LABELS,1):
        row = windows[label]
        require(type(row["index"]) is int and row["index"] == j,"ordered physical label window")
        require(type(row["candidates_examined"]) is int
                and 1 <= row["candidates_examined"] <= 200,"reported bounded scout work")
        values = row["primes"]
        require(type(values) is list and len(values) == (2 if j <= 4 else 1),
                "exact bounded fixture prime count")
        require(all(type(p) is int and u < p < 2*u for p in values),"bounded exact prime integers")
        for p in values:
            require((1000+j)*u < 1000*p < (1001+j)*u,"strict cofinal prime window")
            require(all(p % d for d in range(2,isqrt(p)+1)),"independent trial-division primality")
        require(len(set(values)) == len(values),"distinct primes within window")
        selected[label] = tuple(values)
    flat = [p for values in selected.values() for p in values]
    require(len(set(flat)) == 11 and 67 not in flat,"global clean physical labels")
    return u,selected


def legendre(value,modulus):
    require(type(value) is int and type(modulus) is int
            and 2 < modulus < 1 << 22 and gcd(value,modulus) == 1,
            "bounded nonzero quadratic residue coordinate")
    result = pow(value,(modulus-1)//2,modulus)
    require(result in (1,modulus-1),"prime-field quadratic character")
    return 1 if result == 1 else -1


def class_lower_bound(left_counts,right_counts):
    require(type(left_counts) is tuple and type(right_counts) is tuple
            and len(left_counts) == len(right_counts) == 2
            and all(type(v) is int and 0 <= v <= 1000000 for v in (*left_counts,*right_counts)),
            "bounded exact class counts")
    m,n = sum(left_counts),sum(right_counts)
    require(m > 0 and n > 0,"nonempty owner lists")
    squares = sum(v*v for v in left_counts)*sum(v*v for v in right_counts)
    require(4*squares >= m*m*n*n,"distribution-free complete class partition")
    return squares


def record(algebra,data):
    u,selected = validate_primes(data)
    g,ell,rho = (selected[key][0] for key in ("g","ell","rho"))
    a,b = g*ell,g*rho
    horizon = u**6
    require(Fraction(126,125)**6 < Fraction(11,10),"cofinal physical window constant")
    require(g < Fraction(u*u,4) and u < g < ell < rho,"live common and least-prime sector")
    left_row,right_row = algebra.boolean_rows((g,ell),u),algebra.boolean_rows((g,rho),u)
    for row in (left_row,right_row):
        require(row["balanced"] == 2 and row["complete_allocations"] == 9
                and len(row["nonzero_balanced_histories"]) == 2
                and all(h["coefficient"] == 1 for h in row["nonzero_balanced_histories"]),
                "actual complete positive Boolean histories")
    left = [(p*q,Pindex) for Pindex,(p,q) in enumerate(product(selected["p"],selected["q"]))]
    right = [(r*s,Qindex) for Qindex,(r,s) in enumerate(product(selected["r"],selected["s"]))]
    require(len({p for p,_ in left}) == len(left) and len({q for q,_ in right}) == len(right),
            "distinct arithmetic owner products")
    left_counts = tuple(sum(legendre(p,rho) == sign for p,_ in left) for sign in (-1,1))
    right_counts = tuple(sum(legendre(q,ell) == sign for q,_ in right) for sign in (-1,1))
    partition_square_sum = class_lower_bound(left_counts,right_counts)
    weight = Fraction(g*g*ell*rho)*Fraction(ell+1,ell-1)*Fraction(rho+1,rho-1)
    cmin,cmax = Fraction(10,99*horizon),Fraction(1,9*horizon)
    entries = []
    by_class = {(sig,tau):[] for sig,tau in product((-1,1),repeat=2)}
    for (p,pi),(q,qi) in product(left,right):
        require(p < q < a < b and gcd(p,q*a*b) == gcd(q,p*a*b) == 1,
                "full-core owner-size and clean cross-owner conditions")
        n,m = p*a*a,q*b*b
        require(horizon < n < Fraction(11,10)*horizon
                and horizon < m < Fraction(11,10)*horizon,"native physical output window")
        sig,tau = legendre(q,ell),legendre(p,rho)
        square = Fraction(1,81*n*m)
        literal_square = Fraction(1,36**2*n*m)
        require(square == 16*literal_square
                and square == Fraction(1,9*n)*Fraction(1,9*m),"canonical coefficient/four-history normalization")
        require(cmin*cmin < square < cmax*cmax,"positive symbolic native coefficient interval")
        item = {"P":p,"Q":q,"N":n,"M":m,"index":[pi,qi],"class":[sig,tau],
                "coefficient_square":str(square),"one_literal_square":str(literal_square),
                "ratio_N_over_M":str(Fraction(n,m)),"positive_branch":True}
        entries.append(item)
        by_class[(sig,tau)].append(item)
    ratio_checks = 0
    for group in by_class.values():
        for first,second in product(group,repeat=2):
            ratio = Fraction(first["ratio_N_over_M"])/Fraction(second["ratio_N_over_M"])
            require(Fraction(10,11)**2 < ratio < Fraction(11,10)**2,
                    "all within-class frequency differences in native Gram interval")
            ratio_checks += 1
    sizes = [len(group) for group in by_class.values()]
    require(sum(size*size for size in sizes) == partition_square_sum,
            "complete independent owner class partition")
    diagonal_without_gamma = weight*sum((Fraction(row["coefficient_square"]) for row in entries),Fraction(0))/4
    lower_energy = weight*cmin*cmin*partition_square_sum
    upper_energy = 384*weight*cmax*cmax*partition_square_sum
    ratio_lower = lower_energy/(384*diagonal_without_gamma)
    count = len(entries)
    require(ratio_lower >= LOWER*count,"native class-retained diagonal amplification")
    return {"U":u,"Y":horizon,"g":g,"ell":ell,"rho":rho,"weight":str(weight),
            "left_boolean":left_row,"right_boolean":right_row,
            "left_class_counts_minus_plus":list(left_counts),
            "right_class_counts_minus_plus":list(right_counts),
            "class_pair_counts":[{"class":list(key),"pairs":len(group)} for key,group in by_class.items()],
            "class_pair_count_square_sum":partition_square_sum,
            "arithmetic_pairs":count,"literal_histories":4*count,"entries":entries,
            "native_Gram_ratio_checks":ratio_checks,
            "literal_principal_diagonal_divided_by_Gamma0":str(diagonal_without_gamma),
            "certified_principal_energy_lower":str(lower_energy),
            "certified_principal_energy_upper":str(upper_energy),
            "certified_energy_over_literal_diagonal_lower":str(ratio_lower),
            "universal_energy_over_literal_diagonal_lower":str(LOWER*count),
            "universal_energy_over_literal_diagonal_upper":4*count,
            "equal_pair_principal_correction_divided_by_Gamma0":str(3*diagonal_without_gamma),
            "positive_square_roots_rationalized":False}


def build():
    raw = {key:source_bytes(key) for key in SOURCES}
    algebra = load_primitive((EA,EA_PATH),raw[(EA,EA_PATH)])
    kernel = load_primitive((PQR,PQR_PATH),raw[(PQR,PQR_PATH)])
    bounds = kernel.kernel_bounds(json.loads(raw[(SCB,SCB_PATH)])["kernel"])
    require(PRIMES.stat().st_size <= MAX_BYTES,"prime fixture byte cap")
    data = json.loads(PRIMES.read_text(encoding="utf-8"))
    hashes = {}
    for path in (NOTE,Path(__file__),PRIMES,SCOUT,TEST):
        raw_file = path.read_bytes()
        require(len(raw_file) <= MAX_BYTES,"owned file cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(raw_file.replace(b"\r\n",b"\n")).hexdigest()
    result = {"schema":"riemann.dense_owner_principal_coefficient_family.v1",
              "sources":[{"commit":key[0],"path":key[1],"git_blob":blob} for key,blob in SOURCES.items()],
              "source_hashes":hashes,"native_kernel_bounds":bounds,"record":record(algebra,data),
              "cofinal_growth":{"principal_energy":"Theta(Y^(1/2)/log(Y)^11)",
                                 "literal_diagonal":"Theta(Y^(-1/6)/log(Y)^7)",
                                 "energy_over_diagonal":"Theta(Y^(2/3)/log(Y)^4)"},
              "all_native_owner_class_sums_retained":True,"free_coefficients_used":False,
              "growing_modulus_PNT_used":False,"prime_searches_during_replay":0,
              "full_gamma_source_identified_with_projection":False,
              "projection_proved_orthogonal_in_Mellin_norm":False,
              "full_native_principal_moment_refuted":False,"RH_conclusion":False}
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
