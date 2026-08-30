#!/usr/bin/env python3
"""Actual Boolean off-history conductor traces with exact principal cancellation."""

from __future__ import annotations

import argparse
import json
import subprocess
import types
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import permutations, product
from math import comb, gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "NATIVE_OFF_ATOMIC_CONDUCTOR_CANCELLATION.md"
FIXTURE = HERE / "native_off_atomic_conductor_cancellation.json"
TEST = ROOT / "tests" / "test_native_off_atomic_conductor_cancellation.py"
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
EA = "5ef9a0800e7d0f03bfef1ad4ba467f8843a90058"
EA_PATH = "research/riemann-structures/euler_activation_source_adapter.py"
SCB = "1623f1924c62035918a94bcacf2ccad7d3bb6cf7"
SCB_PATH = "research/riemann-structures/subcritical_observed_boolean_block.json"
SOURCES = {
    ("a30276a5be049749ebb2147f30f000dd5659298b", "research/l-families/atlas/function_field/FFPS_SIGNED_HISTORY_RECOMBINATION.md"):
        "c5f77f48bd19cc9af39698d4de53ae266bd42e17",
    (EA, EA_PATH): "f8248cd97c4fc72ad4034d9baf83cec91396f27e",
    ("e365528d750fded282bd3f7261898d8455c41e0a", "research/riemann-structures/SOURCE_FIRST_BOOLEAN_PRINCIPAL_ADAPTER.md"):
        "c37145331aedf3c6a4ec0c70577a66da712a5edd",
    ("6dbab098bb057d76748d12e37900efeff571f8a9", "research/riemann-structures/LIVE_FIXED_CONDUCTOR_MULTIPLICITY.md"):
        "c9c5f9e7e1ddab7e9a6aff629165a098fdf597a8",
    (SCB, SCB_PATH): "b6464ebbd4560e50d9ad7033d051dc9cddd4a7f4",
    (OLD, "claims/lemmas/L-102958-ratioeight-comparability-pays-both-opposite-owner-products.md"):
        "3b72653ea5f05405c587be165faf7ab2c52c3f2b",
    (FAMILY, "claims/lemmas/L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md"):
        "346cc52420ec65457c2a5accc045d4a85635cc24",
    (FAMILY, "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md"):
        "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (FAMILY, "claims/lemmas/L-106191-source-dual-centered-double-incidence-correlation.md"):
        "85c4ef92ead7d8b235f9c195c3c0acd16d16030f",
    (FAMILY, "claims/lemmas/L-106131-wick-normal-ordering-additive-kummer-decomposition.md"):
        "37722c3f36ec7d1681f34d4329a3795e5028f7ae",
    (FAMILY, "claims/refutations/R-106131-complete-gauss-family-atomic-ledger-carries-phase-cardinality.md"):
        "8dde14dd382e0c4fc1bb54d5da21de85ea002f41",
    (FAMILY, "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md"):
        "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
}
MAX_BYTES = 262144
MAX_PRIME = 10000
P, Q = 323, 143


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def source_bytes(key):
    require(key in SOURCES, "frozen source identity")
    ref = f"{key[0]}:{key[1]}"
    size = int(subprocess.run(["git", "cat-file", "-s", ref], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout)
    require(0 < size <= MAX_BYTES, "source byte cap")
    raw = subprocess.run(["git", "show", ref], cwd=ROOT,
                         capture_output=True, check=True).stdout
    require(len(raw) == size, "source byte count")
    digest = sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest()
    require(digest == SOURCES[key], "frozen source Git blob")
    return raw


def load_algebra(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "bounded executable bytes")
    digest = sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    require(digest == SOURCES[(EA,EA_PATH)], "authenticated Boolean primitive")
    module = types.ModuleType("frozen_off_atomic_boolean")
    module.__file__ = str(ROOT / EA_PATH)
    # Only this exact rehashed frozen Git primitive is executable.
    exec(compile(raw, f"{EA}:{EA_PATH}", "exec"), module.__dict__)  # noqa: S102
    return module


def prime(value):
    require(type(value) is int and 2 < value <= MAX_PRIME, "bounded odd prime candidate")
    require(all(value % d for d in range(2,isqrt(value)+1)), "exact trial-division primality")
    return value


def character_weights(q):
    q = prime(q)
    principal = Fraction(q+1,q-1)
    each_nonprincipal = Fraction(2*q,q-1)
    nonprincipal_count = (q-3)//2
    nonprincipal = nonprincipal_count*each_nonprincipal
    require(principal+nonprincipal == q-1, "complete even-character weight")
    return {"principal":principal,"nonprincipal":nonprincipal,
            "nonprincipal_count":nonprincipal_count,"nonprincipal_each":each_nonprincipal}


def window_constants():
    bounds = {
        "N_lower": P*Fraction(7,125)**2,
        "N_upper": P*Fraction(101,100)**2*Fraction(57,1000)**2,
        "M_lower": Q*Fraction(21,250)**2,
        "M_upper": Q*Fraction(101,100)**2*Fraction(17,200)**2,
    }
    require(all(1 < x < Fraction(11,10) for x in bounds.values()), "cofinal physical shell constants")
    count_constant = Fraction(1,100)*Fraction(1,1000)*Fraction(1,1000)/4
    require(count_constant == Fraction(1,400000000), "PNT three-interval leading count")
    return {**{k:str(v) for k,v in bounds.items()},
            "PNT_count_constant_U5_over_log3":str(count_constant)}


def record(algebra, cutoff=256, common=257, ell=3691, rho=5521):
    require(type(cutoff) is int and 32 <= cutoff <= 1024
            and cutoff & (cutoff-1) == 0, "bounded dyadic cutoff")
    common,ell,rho = (prime(q) for q in (common,ell,rho))
    owners = (prime(17),prime(19),prime(11),prime(13))
    require(len({common,ell,rho,*owners,67}) == 8, "clean distinct physical labels")
    require(cutoff < common < Fraction(101,100)*cutoff
            and Fraction(7,125)*cutoff**2 < ell < Fraction(57,1000)*cutoff**2
            and Fraction(21,250)*cutoff**2 < rho < Fraction(17,200)*cutoff**2,
            "declared cofinal source windows")
    require(cutoff < common < ell < rho and common < Fraction(cutoff**2,4),
            "balanced primes and live common-core window")
    a,b = common*ell,common*rho
    n,m = P*a*a,Q*b*b
    horizon = cutoff**6
    require(horizon < n < Fraction(11,10)*horizon and horizon < m < Fraction(11,10)*horizon,
            "same physical shell")
    require(P <= a and Q <= b and P <= 2*b and Q <= 2*a,
            "full-core owner inequalities")
    require(gcd(a,b) == common and gcd(P,Q*a*b) == gcd(Q,P*a*b) == 1,
            "native clean core/owner incidence")
    left,right = algebra.boolean_rows((common,ell),cutoff),algebra.boolean_rows((common,rho),cutoff)
    for rows,phase in ((left,ell),(right,rho)):
        require(rows["complete_allocations"] == 9 and rows["balanced"] == 2,
                "complete two-prime balanced row")
        require(canonical(rows["nonzero_balanced_histories"]) == canonical([
            {"groups":[[common],[phase],[]],"coefficient":1},
            {"groups":[[phase],[common],[]],"coefficient":1},
        ]), "exact two positive ordered histories")
    share = Fraction(1,comb(4,2))
    one_literal_square = share**4/Fraction(n*m)
    require(one_literal_square == Fraction(1,36**2*n*m), "native one-history coefficient square")
    histories = list(product(range(2),repeat=2))
    off_count = len(list(permutations(histories,2)))
    require(off_count == 12, "literal off-atomic ordered pairs")
    off = off_count*one_literal_square
    diagonal = len(histories)*one_literal_square
    merged = len(histories)**2*one_literal_square
    require(off == Fraction(1,108*n*m) and merged-diagonal == off,
            "literal Wick versus merged new atom")
    wl,wr = character_weights(ell),character_weights(rho)
    outside = common**2*ell*rho
    additive = outside*(ell-1)*(rho-1)*off
    principal = outside*wl["principal"]*wr["principal"]*off
    mixed = outside*(wl["principal"]*wr["nonprincipal"]
                     +wl["nonprincipal"]*wr["principal"])*off
    double = outside*wl["nonprincipal"]*wr["nonprincipal"]*off
    require(additive == principal+mixed+double and mixed+double > 0,
            "complete native four-channel identity")
    compact_a = Fraction(1,108*P*Q*common**2)*(1-Fraction(1,ell))*(1-Fraction(1,rho))
    compact_p = wl["principal"]*wr["principal"]/Fraction(108*P*Q*common**2*ell*rho)
    source_dual_off = (common*ell*rho)**2*off
    incidence = (1-Fraction(1,ell))*(1-Fraction(1,rho))*source_dual_off
    require(additive == compact_a == incidence and principal == compact_p,
            "independent physical/compact/source-dual normalizations")
    sig = pow(Q,(ell-1)//2,ell)
    tau = pow(P,(rho-1)//2,rho)
    require(sig in (1,ell-1) and tau in (1,rho-1), "actual owner quadratic classes")
    return {"U":cutoff,"Y":horizon,"g":common,"ell":ell,"rho":rho,
            "owners":{"P":[17,19],"Q":[11,13]},"a":a,"b":b,"N":n,"M":m,
            "fibre":[common,ell,rho,1 if sig==1 else -1,1 if tau==1 else -1],
            "raw_residues":[(-Q*rho*rho)%ell,(P*ell*ell)%rho],
            "left_boolean":left,"right_boolean":right,"canonical_share":str(share),
            "one_literal_coefficient_square":str(one_literal_square),
            "literal_histories":4,"off_atomic_ordered_pairs":off_count,
            "arithmetic_pairs_in_fibre":1,"distinct_output_pairs_in_fibre":0,
            "literal_diagonal_without_weights":str(diagonal),
            "merged_new_diagonal_without_weights":str(merged),
            "literal_off_atomic_without_weights":str(off),
            "merged_new_wick_form_without_weights":"0",
            "A_divided_by_Gamma0":str(additive),"P_divided_by_Gamma0":str(principal),
            "mixed_divided_by_Gamma0":str(mixed),"NN_divided_by_Gamma0":str(double),
            "K_divided_by_Gamma0":str(mixed+double),
            "P_over_A":str(principal/additive),
            "principal_literal_diagonal_divided_by_Gamma0":str(principal/3),
            "principal_full_energy_divided_by_Gamma0":str(4*principal/3),
            "even_character_weights":{
                "ell":{key:str(value) for key,value in wl.items()},
                "rho":{key:str(value) for key,value in wr.items()}},
            "primality_method":"BOUNDED_TRIAL_DIVISION_NO_SEARCH"}


def build():
    raw = {key:source_bytes(key) for key in SOURCES}
    algebra = load_algebra(raw[(EA,EA_PATH)])
    kernel = json.loads(raw[(SCB,SCB_PATH)])["kernel"]
    require(canonical(kernel["norm_constant"]) == '["-288","0"]'
            and canonical(kernel["norm_log2_coefficient"]) == '["384","128"]',
            "native symbolic Gram mass")
    hashes = {}
    for path in (NOTE,Path(__file__),TEST):
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES,"local file cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(data.replace(b"\r\n",b"\n")).hexdigest()
    result = {"schema":"riemann.native_off_atomic_conductor_cancellation.v1",
              "sources":[{"commit":key[0],"path":key[1],"git_blob":blob} for key,blob in SOURCES.items()],
              "source_hashes":hashes,"cofinal_window_constants":window_constants(),
              "record":record(algebra),"Gamma0":"(384+128sqrt(2))*log(2)-288",
              "cofinal_growth":{"A":"Theta(Y^(1/2)/log(Y)^3)",
                                 "K":"Theta(Y^(1/2)/log(Y)^3)",
                                 "P":"Theta(Y^(-1/6)/log(Y)^3)",
                                 "P_over_A":"Theta(Y^(-2/3))"},
              "whole_source_gamma_bound_asserted":False,"global_WCEQ_refuted":False,
              "whole_source_moment_counterexample":False,"prime_searches":0,
              "literal_diagonal_retained":True,"RH_conclusion":False}
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
        require(canonical(json.loads(FIXTURE.read_text(encoding="utf-8"))) == canonical(result),
                "exact typed canonical replay")
    print(json.dumps({"status":"PASS","proof_object_sha256":result["proof_object_sha256"]}))


if __name__ == "__main__":
    main()
