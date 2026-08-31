#!/usr/bin/env python3
"""Exact source-first Boolean completion, gauge quotient, and principal diagonal."""

from __future__ import annotations

import argparse
import json
import subprocess
import types
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations, product
from math import comb, gcd, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "SOURCE_FIRST_BOOLEAN_PRINCIPAL_ADAPTER.md"
FIXTURE = HERE / "source_first_boolean_principal_adapter.json"
TEST = ROOT / "tests" / "test_source_first_boolean_principal_adapter.py"
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
EA = "5ef9a0800e7d0f03bfef1ad4ba467f8843a90058"
GC = "e501c45ecc39f71b3f26abfe952366eb529c7c2d"
SCB = "1623f1924c62035918a94bcacf2ccad7d3bb6cf7"
EA_PATH = "research/riemann-structures/euler_activation_source_adapter.py"
GC_PATH = "research/riemann-structures/gauge_connection_source_transport.py"
SCB_PATH = "research/riemann-structures/subcritical_observed_boolean_block.json"
SOURCES = {
    (EA, EA_PATH): "f8248cd97c4fc72ad4034d9baf83cec91396f27e",
    (GC, GC_PATH): "c379b6cd50c06ec29cf316e55e85157424b3563b",
    (SCB, SCB_PATH): "b6464ebbd4560e50d9ad7033d051dc9cddd4a7f4",
    (OLD, "claims/lemmas/L-102706-euler-half-divisor-homotopies-are-subcritically-gauge-equivalent.md"):
        "6192bec36636e2d35b2aba4fdd64eb4bcf93c2d9",
    (OLD, "claims/lemmas/L-102746-wick-tail-has-a-canonical-equal-pair-owner.md"):
        "db018c64dde45ff4ad17541eb6ba00b4f6fa9d49",
    (OLD, "claims/lemmas/L-102951-harmonic-critical-class-is-the-squarefree-boolean-euler-class.md"):
        "1a2f15e7b5fcb0a3fb17d20668c3735065d14224",
    (OLD, "claims/lemmas/L-102952-owner-excluded-boolean-vaughan-coefficients-are-universal.md"):
        "8e0de55d193d6f9dafd025235dac8ab48e687081",
    (OLD, "claims/lemmas/L-102954-hodge-boolean-reduction-leaves-one-owner-indexed-restriction.md"):
        "65c63098dcea20bfe8a189355c86fe663908b00b",
    (OLD, "claims/lemmas/L-102962-canonical-equal-pair-gauge-is-horizon-safe-on-the-boolean-balanced-source.md"):
        "d8f4557df6dc37e6b605b1821c5b8ab028136398",
    (FAMILY, "claims/lemmas/L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md"):
        "346cc52420ec65457c2a5accc045d4a85635cc24",
    (FAMILY, "claims/lemmas/L-106026-mellin-plancherel-normal-form-for-owner-conductor-moment.md"):
        "388c7e166a0e6e534d7e908685f71a16de246575",
    (FAMILY, "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md"):
        "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
}
MAX_BYTES = 262144
ZERO, ONE = Fraction(0), Fraction(1)


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


def load_primitive(key, raw):
    require(key in ((EA, EA_PATH), (GC, GC_PATH)), "executable identity")
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "executable byte cap")
    digest = sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    require(digest == SOURCES[key], "executable Git blob")
    module = types.ModuleType("frozen_source_first_primitive")
    module.__file__ = str(ROOT / key[1])
    # Execution is restricted to these exact rehashed frozen Git primitives.
    exec(compile(raw, f"{key[0]}:{key[1]}", "exec"), module.__dict__)  # noqa: S102
    return module


def scalar(algebra, poly, factor):
    require(type(factor) is Fraction, "exact scalar")
    return algebra.trim(tuple(factor * x for x in poly))


def evaluate(poly, tau):
    require(type(tau) is Fraction and 0 <= tau <= 1, "exact homotopy point")
    return sum((x * tau**i for i,x in enumerate(poly)), ZERO)


def independent_labels(labels):
    # Primality is inherited from the authenticated source panels. This guard
    # independently prevents set operations from misrepresenting arithmetic gcd.
    require(type(labels) is tuple and 1 <= len(labels) <= 12
            and all(type(p) is int and 2 < p and p % 2 and p.bit_length() <= 128 for p in labels),
            "bounded odd physical label types")
    require(all(gcd(p,q) == 1 for p,q in combinations(set(labels),2)),
            "distinct physical labels must be arithmetically coprime")


def gauge_quotient(gauge):
    local = gauge.local_record()
    coefficients = [tuple(Fraction(x) for x in poly) for poly in local["g_x_coefficients"]]
    algebra = gauge.load_algebra()
    derivatives = [algebra.derivative(poly) for poly in coefficients]
    require(coefficients[1] == (ZERO,), "actual local gauge has no linear coefficient")
    origins = tuple(product(range(3), repeat=3))
    targets = tuple(product(range(2), repeat=3))
    checks = 0
    for tau in (Fraction(0), Fraction(1,3), Fraction(1,2), Fraction(1)):
        g = [evaluate(poly, tau) for poly in coefficients]
        dg = [evaluate(poly, tau) for poly in derivatives]
        for target in targets:
            for origin in origins:
                if any(old > new for old,new in zip(origin,target,strict=True)):
                    value, derivative = ZERO, ZERO
                else:
                    deltas = [new-old for old,new in zip(origin,target,strict=True)]
                    value = prod((g[d] for d in deltas), start=ONE)
                    derivative = sum((dg[deltas[j]] * prod((g[deltas[k]] for k in range(3) if k != j), start=ONE)
                                      for j in range(3)), ZERO)
                require(value == int(origin == target) and derivative == 0,
                        "raw squarefree quotient gauge/connection identity")
                checks += 1
    return {"local_source": local, "raw_columns": len(origins),
            "squarefree_rows": len(targets), "exact_scalar_checks": checks}


def completed_path(algebra, core, owners, cutoff):
    require(type(core) is tuple and type(owners) is tuple and len(owners) == 2,
            "retained owner/core tuples")
    require(len(set(core + owners)) == len(core) + 2, "clean physically squarefree support")
    require(all(type(p) is int and p > 2 and p % 2 and p.bit_length() <= 128
                for p in core + owners), "odd physical label type/range")
    independent_labels(core + owners)
    rows = algebra.boolean_rows(core, cutoff)
    depth = len(core) + 2
    share = Fraction(1, comb(depth, 2))
    mu = (-1)**len(core)
    multiplier = Fraction(rows["balanced"], mu)
    tau = (ZERO, ONE)
    raw_sf = scalar(algebra, algebra.power(tau, depth), Fraction(mu))
    completed = scalar(algebra, raw_sf, share * multiplier)
    derivative = algebra.derivative(completed)
    total = algebra.integral(derivative)
    owner = algebra.integral(scalar(algebra, derivative, Fraction(2, depth)))
    cores = algebra.integral(scalar(algebra, derivative, Fraction(depth-2, depth)))
    expected = share * rows["balanced"]
    require(total == expected and owner + cores == expected,
            "source-first full derivative recovers completed coefficient")
    mixed_raw = algebra.multiply(algebra.power(tau, 2), algebra.power((ONE, -ONE), len(core)))
    mixed_raw = scalar(algebra, mixed_raw, Fraction(mu))
    mixed_total = algebra.integral(algebra.derivative(mixed_raw))
    require(mixed_total == 0, "different raw mixed-monomial projection")
    history_energy = sum(h["coefficient"]**2 for h in rows["nonzero_balanced_histories"])
    require(history_energy <= 9**len(core), "complete Boolean-history squared bound")
    require(abs(rows["balanced"]) <= 2 * 3**len(core), "safe Boolean coefficient bound")
    p, a = prod(owners), prod(core)
    return {"core": list(core), "owners": list(owners), "cutoff": cutoff,
            "support_depth": depth, "P": p, "a": a, "N": p*a*a,
            "share": str(share), "Boolean_multiplier": str(multiplier),
            "rows": rows, "source_first_tau_polynomial_times_sqrt_N": [str(x) for x in completed],
            "full_integral_times_sqrt_N": str(total),
            "owner_integral_times_sqrt_N": str(owner),
            "core_integral_times_sqrt_N": str(cores),
            "raw_mixed_monomial_full_integral": str(mixed_total),
            "history_energy": history_energy,
            "coefficient_square": str(expected**2 / (p*a*a)),
            "raw_Euler_coefficient_square": str(Fraction(1,p*a))}


def completion_ratio(left, right):
    require(type(left) is tuple and type(right) is tuple and left and right,
            "nonempty retained cores")
    require(len(set(left)) == len(left) and len(set(right)) == len(right),
            "squarefree core labels")
    require(len(left) <= 6 and len(right) <= 6
            and all(type(p) is int and 2 < p and p % 2 and p.bit_length() <= 128 for p in left + right),
            "bounded odd physical labels")
    independent_labels(left + right)
    common = set(left).intersection(right)
    c_labels, d_labels = set(left)-common, set(right)-common
    require(c_labels and d_labels, "two nontrivial reduced cores")
    ell, rho = min(c_labels), min(d_labels)
    require(ell != rho and ell > 2 and rho > 2 and ell % 2 and rho % 2,
            "distinct odd phase labels")
    a, b, g = prod(left), prod(right), prod(common)
    c, d = prod(c_labels), prod(d_labels)
    c_ell, c_rho = Fraction(ell+1,ell-1), Fraction(rho+1,rho-1)
    weight = g*g*ell*rho*c_ell*c_rho
    ratio = weight / (a*b)
    require(ratio == Fraction(ell*rho,c*d)*c_ell*c_rho and ratio <= 3,
            "exact actual principal completion norm")
    return {"a":a,"b":b,"g":g,"c":c,"d":d,"ell":ell,"rho":rho,
            "weight":str(weight),"squared_completion_norm_ratio":str(ratio)}


def owner_column(algebra, support, cutoff):
    require(type(support) is tuple and 3 <= len(support) <= 6
            and len(set(support)) == len(support), "bounded raw squarefree column")
    independent_labels(support)
    k = len(support)
    share = Fraction(1, comb(k,2))
    coefficient_energy, history_energy = ZERO, ZERO
    for owners in combinations(support,2):
        core = tuple(p for p in support if p not in owners)
        rows = algebra.boolean_rows(core,cutoff)
        coefficient_energy += share**2 * rows["balanced"]**2
        history_energy += share**2 * sum(h["coefficient"]**2 for h in rows["nonzero_balanced_histories"])
    require(comb(k,2)*share**2 == share <= 1, "canonical owner splitting contraction")
    require(coefficient_energy <= 4*9**(k-2) and history_energy <= 9**(k-2),
            "whole owner-column Boolean bounds")
    return {"support":list(support),"unordered_pairs":comb(k,2),
            "owner_only_column_energy":str(share),
            "coefficient_column_energy_before_completion":str(coefficient_energy),
            "history_column_energy_before_completion":str(history_energy)}


def build():
    raw = {key: source_bytes(key) for key in SOURCES}
    algebra = load_primitive((EA,EA_PATH),raw[(EA,EA_PATH)])
    gauge = load_primitive((GC,GC_PATH),raw[(GC,GC_PATH)])
    quotient = gauge_quotient(gauge)
    frozen = json.loads(raw[(SCB,SCB_PATH)])
    require(frozen["proof_object_sha256"] == "3385b68dd20c2c10a361eac3afda8aa1f5b3ba767649ed7d7016913650ace388",
            "frozen native panel proof object")
    examples = []
    for panel in frozen["panels"]:
        p = {key:value["prime"] for key,value in panel["primes"].items()}
        left = completed_path(algebra,(p["A"],p["B"],p["ell"]),(p["p"],p["q"]),panel["U"])
        right = completed_path(algebra,(p["A"],p["B"],p["rho"]),(p["r"],p["s"]),panel["U"])
        for side in (left,right):
            require(side["full_integral_times_sqrt_N"] == "-1/5"
                    and side["owner_integral_times_sqrt_N"] == "-2/25"
                    and side["core_integral_times_sqrt_N"] == "-3/25",
                    "actual SCB source-first coefficient and same-sign activations")
        require(left["N"] == panel["N"] and right["N"] == panel["M"],
                "literal native completion outputs")
        ratio = completion_ratio(tuple(left["core"]),tuple(right["core"]))
        share_product = Fraction(left["share"])*Fraction(right["share"])
        principal_coefficient_ratio = Fraction(ratio["squared_completion_norm_ratio"])*share_product**2*16
        principal_history_ratio = Fraction(ratio["squared_completion_norm_ratio"])*share_product**2*4
        examples.append({"j":panel["j"],"left":left,"right":right,"completion":ratio,
                         "bilateral_coefficient_diagonal_over_raw_diagonal":str(principal_coefficient_ratio),
                         "bilateral_history_diagonal_over_raw_diagonal":str(principal_history_ratio)})
    sharp = completion_ratio((3,7,11),(5,7,11))
    require(sharp["squared_completion_norm_ratio"] == "3", "sharp bare completion constant")
    columns = [owner_column(algebra,support,10) for support in ((3,5,7,11,13),(3,5,7,11,13,17))]
    hashes = {}
    for path in (NOTE,Path(__file__),TEST):
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES,"local source cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(data.replace(b"\r\n",b"\n")).hexdigest()
    result = {"schema":"riemann.source_first_boolean_principal_adapter.v1",
              "sources":[{"commit":key[0],"path":key[1],"git_blob":blob} for key,blob in SOURCES.items()],
              "source_hashes":hashes,"raw_quotient_replay":quotient,
              "authenticated_native_source_examples":examples,"sharp_completion_control":sharp,
              "complete_owner_column_controls":columns,
              "source_first_induced_gauge":"identity",
              "canonical_completed_Boolean_source_cancels":False,
              "same_sign_owner_core_derivative_split":True,
              "complete_Boolean_factor_histories_retained":True,
              "ambient_postcompletion_gauge_identified_with_induced_gauge":False,
              "complete_native_gamma_measure_adapter_asserted":False,
              "full_principal_family_square_bound_asserted":False,"RH_conclusion":False}
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
        require(canonical(candidate)==canonical(result),"exact canonical replay")
    print(json.dumps({"status":"PASS","proof_object_sha256":result["proof_object_sha256"]}))


if __name__ == "__main__":
    main()
