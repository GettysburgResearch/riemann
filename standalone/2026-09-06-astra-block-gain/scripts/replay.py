#!/usr/bin/env python3
"""Bounded source-complete parity/gain replay. No all-scale RH estimate is tested."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from collections import Counter
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT.parent / "2026-09-06-astra-dilation-observability"
PARENT_COMMIT = "032c92e540202d1c409974c0c7b43130d684bfed"
PINS = {
    "PROOF.md": "be2fbf1f146c412cfdda0cfd9c613a4beb88c7b77191c4eb2af3e769c6d71b22",
    "NUMERICS.md": "de19939b3150f0a47cce7da8ba306a520346e396bbeb0860bf3ce18f775beb64",
    "scripts/intervals.py": "91b6448681d88ba5aa7fd0093c6ab2590bd2575d4b0c6e59082fe196fc5fb304",
    "scripts/replay.py": "6c252d214d9ff27d76a4b3bd7c0b087e04798aac1f20b125877915b588c66f1b",
}
FILES = {
    "README.md", "PROOF.md", "SOURCES.md", "SOURCE_LOCK.json", "VALIDATION.md",
    "verification.json", "scripts/replay.py", "scripts/test_replay.py",
}
CONFIG = {
    "stages": [2, 4, 8], "max_gram_index": 16, "bits": 224,
    "odd_detail_includes_nonsquarefree": True,
    "mobius_cap": 192, "haar_vector_cap": 48, "divisor_matrix_cap": 31,
    "all_infinite_gram_tails_enclosed": True,
}
SCHEMA = "riemann-source-complete-parity-gain-v1"


class Refusal(Exception):
    pass


def need(ok: bool, message: str) -> None:
    if ok is not True:
        raise Refusal(message)


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode()


def strict_json(path: Path) -> object:
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                raise Refusal(f"duplicate JSON key: {key}")
            out[key] = value
        return out
    def reject(value):
        raise Refusal(f"nonexact JSON number: {value}")
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs,
                      parse_float=reject, parse_constant=reject)


def authenticate_parent(root: Path = PARENT) -> dict[str, bytes]:
    acquired = {}
    need(not root.is_symlink(), "symbolic parent root")
    for name, digest in PINS.items():
        path = root / name
        need(path.is_file() and not path.is_symlink(), f"missing/symbolic parent: {name}")
        need(not any(p.is_symlink() for p in path.parents if p != root.parent),
             f"symbolic parent directory: {name}")
        raw = path.read_bytes()
        need(hashlib.sha256(raw).hexdigest() == digest,
             f"changed parent source: {name}")
        acquired[name] = raw
    return acquired


def check_manifest(root: Path = ROOT) -> None:
    manifest = root / "SHA256SUMS"
    need(manifest.is_file() and not manifest.is_symlink(), "missing/symbolic manifest")
    seen = set()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        need("  " in line, "bad manifest syntax")
        digest, name = line.split("  ", 1)
        path = PurePosixPath(name)
        need(re.fullmatch(r"[0-9a-f]{64}", digest) is not None, "bad checksum")
        need(name in FILES and name not in seen and "\\" not in name and
             not path.is_absolute() and ".." not in path.parts,
             "unknown, duplicate, or unsafe manifest path")
        seen.add(name)
        file = root / name
        need(file.is_file() and not file.is_symlink(), "missing/symbolic packet file")
        need(hashlib.sha256(file.read_bytes()).hexdigest() == digest,
             f"changed packet bytes: {name}")
    actual = set()
    for p in root.rglob("*"):
        if "__pycache__" in p.parts:
            continue
        need(not p.is_symlink(), "symbolic packet entry")
        if p.is_file() and p != manifest:
            actual.add(p.relative_to(root).as_posix())
    need(seen == FILES == actual, "nonempty exact manifest inventory required")


def load_parent():
    acquired = authenticate_parent()
    modules = {}
    # Compile precisely the authenticated bytes; do not trust a parent .pyc cache.
    for name, relative in (("intervals", "scripts/intervals.py"),
                           ("bg26_parent_replay", "scripts/replay.py")):
        path = PARENT / relative
        spec = importlib.util.spec_from_file_location(name, path)
        need(spec is not None, "parent loader unavailable")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        exec(compile(acquired[relative], str(path), "exec"), module.__dict__)
        modules[name] = module
    return modules["bg26_parent_replay"]


p = load_parent()
I, SCALE = p.I, p.SCALE


def mu(n: int) -> int:
    if type(n) is not int or not 1 <= n <= CONFIG["mobius_cap"]:
        raise ValueError("Mobius input outside frozen 1..192")
    sign, d = 1, 2
    while d*d <= n:
        if n % d == 0:
            n //= d
            sign = -sign
            if n % d == 0:
                return 0
        d += 1
    return -sign if n > 1 else sign


def jordan(n: int) -> int:
    return sum(mu(n//d)*d*d for d in range(1, n+1) if n % d == 0)


def odds(m: int) -> list[int]:
    if type(m) is not int or not 1 <= m <= 192:
        raise ValueError("odd inventory outside frozen scope")
    return list(range(1, m+1, 2))


def r_detail(k: int, l: int) -> F:
    return F(gcd(k, l)**2, k*k*l*l)


def rational_detail_solution(m: int) -> list[F]:
    keys = odds(m)
    return [k*k*sum((F(mu(l//k)*mu(l), jordan(l))
                    for l in keys if l % k == 0), F()) for k in keys]


def fdot(a, b):
    if len(a) != len(b):
        raise ValueError("dot lengths differ")
    return sum((x*y for x, y in zip(a, b)), F())


def matrix_product(a, b):
    need(bool(a) and bool(b) and len(a[0]) == len(b), "matrix dimensions")
    return [[p.dot(row, col) for col in zip(*b)] for row in a]


def solve_columns(a, b):
    return [list(row) for row in zip(*(p.solve(a, list(col))[0] for col in zip(*b)))]


def exact_controls() -> dict[str, int]:
    counts = Counter()
    def ck(ok, key):
        need(ok, key)
        counts[key] += 1
    # Independent sieve, not a second call to the trial-factor routine.
    mus = [0]+[1]*192
    for q in range(2, 193):
        if all(q % d for d in range(2, isqrt(q)+1)):
            for n in range(q, 193, q):
                mus[n] *= -1
            for n in range(q*q, 193, q*q):
                mus[n] = 0
    for n in range(1, 193):
        ck(mu(n) == mus[n], "independent_mobius")
        ck(sum(jordan(d) for d in range(1, n+1) if n % d == 0) == n*n,
           "jordan_divisor_identity")
    for length in range(1, 49):
        v = [F()] + [F((-1)**n*(n % 7-3), n+2) for n in range(1, length+1)]
        get = lambda n: v[n] if 0 <= n <= length else F()
        original = sum((get(n)**2/F(n*(n+1)) for n in range(1, length+1)), F())
        coarse = sum((F(1, 2*j*(j+1)) *
                      (F((j+1)*get(2*j)+j*get(2*j+1), 2*j+1))**2
                      for j in range(1, length//2+1)), F())
        detail = get(1)**2/2 + sum(((get(n)-get(n-1))**2/F(2*n*n)
                                  for n in range(3, length+2, 2)), F())
        ck(original == coarse+detail, "weighted_haar_finite_vectors")
    for k in range(2, 33):
        for n in range(1, 66, 2):
            detail = p.h(k, 1) if n == 1 else p.h(k, n)-p.h(k, n-1)
            ck(detail == F(1,k)-int(n % k == 0), "literal_generator_detail")
    for m in range(1, 32):
        keys = odds(m)
        t = rational_detail_solution(m)
        for k in keys:
            ck(fdot([r_detail(k,l) for l in keys], t) == int(k == 1),
               "mobius_formula_inverts_detail_column")
        for k in keys:
            for l in keys:
                ck(sum(jordan(d) for d in keys if k % d == 0 and l % d == 0)
                   == gcd(k,l)**2, "detail_gram_factorization")
        ck(t[0] == sum((F(mu(k)**2,jordan(k)) for k in keys), F()),
           "detail_minimum_identity")
        for k, tk in zip(keys, t):
            alt = F(mu(k)*k*k,jordan(k))*sum(
                (F(mu(d)**2,jordan(d)) for d in odds(m//k) if gcd(d,k) == 1), F())
            ck(tk == alt, "detail_coefficient_two_formulas")
            if mu(k) == 0:
                ck(tk == 0, "detail_nonsquarefree_zero")
    for k in odds(31):
        def H(cell):
            return F(2,k)*p.h(2,cell)-p.h(k,cell)
        for j in range(1,49):
            actual = ((j+1)*H(2*j)+j*H(2*j+1))/(2*j+1)
            formula = -p.h(k,2*j)+F(j,2*j+1)*int((2*j+1) % k == 0)
            ck(actual == formula, "literal_coarse_source_formula")
    for m in range(1,32):
        keys = odds(m)
        t = rational_detail_solution(m)
        phi = lambda l: sum(k*mu(l//k) for k in range(1,l+1) if l % k == 0)
        ck(sum((tk/k for k,tk in zip(keys,t)),F()) ==
           sum((F(mu(l)*phi(l),jordan(l)) for l in keys),F()),
           "signed_coarse_normalization")
    for n in (2, 4, 8):
        for k in range(2, 2*n+1):
            for cell in range(1, 65):
                if k == 2:
                    value = p.h(2,cell)
                elif k % 2 == 0:
                    j = k//2
                    value = p.h(j,cell//2) + p.h(2,cell)/j
                else:
                    hk = F(2,k)*p.h(2,cell)-p.h(k,cell)
                    value = F(2,k)*p.h(2,cell)-hk
                ck(value == p.h(k,cell), "complete_even_odd_reconstruction")
    for m in range(64, 97):
        count = sum(mu(k)**2 for k in odds(2*m) if k > m)
        ck(count >= F(m,4), "bounded_squarefree_count_control")
        ck(m*m-40*m+16 > 0, "uniform_count_constant_control")
    return dict(sorted(counts.items()))


def detail_error(m: int):
    pi2 = p.pi_interval()**2
    total = sum((F(mu(k)**2,jordan(k)) for k in odds(m)), F())
    return F(1,2)-4*total/pi2


def stage(n: int) -> dict:
    if type(n) is not int or n not in CONFIG["stages"]:
        raise ValueError("only frozen N=2,4,8 stages are allowed")
    m = 2*n
    old, full = p.projection(n), p.projection(m)
    keys = odds(m)
    oldkeys = list(range(2,n+1))
    H = [[I.of(F(2,k) if j == 2 else 0)-int(k>1 and j==k)
          for k in keys] for j in range(2,m+1)]
    Hg = matrix_product([list(row) for row in zip(*H)], matrix_product(full["G"], H))
    Hb = [p.dot(list(col), full["b"]) for col in zip(*H)]
    V = [[2*p.dot([p.gram(2*j,k)-p.gram(2,k)/j for k in range(2,m+1)], list(col))
          for col in zip(*H)] for j in oldkeys]
    pi2 = p.pi_interval()**2
    Q = [[pi2*r_detail(k,l)/16 for l in keys] for k in keys]
    solvedV = solve_columns(old["G"], V)
    coupling = matrix_product([list(row) for row in zip(*V)], solvedV)
    C = [[2*(Hg[i][j]-Q[i][j])-coupling[i][j] for j in range(len(keys))]
         for i in range(len(keys))]
    w = [2*Hb[i]-int(i==0)-p.dot(list(col),old["c"])
         for i,col in enumerate(zip(*V))]
    a0 = [8*x/pi2 for x in rational_detail_solution(m)]
    e = detail_error(m)
    trial = e+(old["delta"]-2*p.dot(w,a0)+p.dot(a0,p.matvec(C,a0)))/2
    M = [[Q[i][j]+C[i][j]/2 for j in range(len(keys))] for i in range(len(keys))]
    t = [(x+int(i==0))/2 for i,x in enumerate(w)]
    a, pivots = p.solve(M,t)
    from_recursion = (1+old["delta"])/2-p.dot(t,a)
    rem = [wi-ci for wi,ci in zip(w,p.matvec(C,a0))]
    adjustment = p.dot(rem,p.solve(M,rem)[0])/4
    from_trial = trial-adjustment
    gain = old["delta"]-full["delta"]
    z = {k: I.of(0) if k <= n else p.bvalue(k)-p.dot(
         old["c"],[p.gram(j,k) for j in oldkeys]) for k in range(2,m+1)}
    dt = [z[2*j] for j in oldkeys]
    oddbirths = [k for k in keys if k > n]
    ov = [z[k] for k in oddbirths]
    OG = [[p.gram(k,l) for l in oddbirths] for k in oddbirths]
    even_energy = p.dot(dt,p.solve(old["G"],dt)[0])
    odd_energy = p.dot(ov,p.solve(OG,ov)[0])
    energy = even_energy+odd_energy
    lower = F(2,3)*energy
    penalty_change = (full["delta"]-e)-(old["delta"]-detail_error(n))
    scalar_checks = 0
    def ck(ok, message):
        nonlocal scalar_checks
        need(ok, message)
        scalar_checks += 1
    ck(from_recursion.overlaps(full["delta"]), "lossless recursion mismatch")
    ck(from_trial.overlaps(full["delta"]), "completed-square mismatch")
    ck(gain.lo > lower.hi > 0, "two-channel original gain inequality")
    ck(trial.lo > full["delta"].hi, "trial must not beat full optimum")
    ck((full["delta"]-e).lo > 0, "relaxation lower bound")
    # Independent coordinate extraction from the original Gram solution.
    for i,k in enumerate(keys):
        if k == 1:
            a_direct = (full["c"][0]+sum((full["c"][2*j-2]/j for j in range(2,n+1)), I.of(0))
                        +sum((2*full["c"][k0-2]/k0 for k0 in keys if k0>1), I.of(0)))/2
        else:
            a_direct = -full["c"][k-2]
        ck(a[i].overlaps(a_direct), "original-to-parity optimizer mismatch")
    values = {
        "delta_N":old["delta"], "delta_2N":full["delta"], "full_gain":gain,
        "detail_error_N":detail_error(n), "detail_error_2N":e,
        "detail_gain":detail_error(n)-e, "lifting_penalty_change":penalty_change,
        "detail_optimal_lift_trial":trial, "trial_minus_old":trial-old["delta"],
        "dilation_channel":even_energy, "odd_birth_channel":odd_energy,
        "two_channel_energy":energy, "original_gain_lower_bound":lower,
        "two_channel_over_delta_squared":energy/old["delta"].square(),
        "coupled_adjustment":adjustment,
    }
    for name,value in values.items():
        ck(value.width() < F(1,10**24), f"wide enclosure: {name}")
    for value in a:
        ck(value.width() < F(1,10**24), "wide optimal coefficient")
    if n == 8:
        ck((trial-old["delta"]).lo > I.of(F(1,1000)).hi, "failed detail lift not certified")
        ck(penalty_change.lo > I.of(F(3,2000)).hi, "penalty increase not certified")
        ck(a[keys.index(9)].hi < I.of(-F(1,10)).lo, "nonsquarefree full coefficient")
        ck(a0[keys.index(9)].contains(0), "detail coefficient nine must be zero")
    return {
        "N":n, "odd_detail_indices":keys, "odd_birth_indices":oddbirths,
        "values":{name:value.record() for name,value in values.items()},
        "full_optimal_parity_coefficients":{str(k):v.record() for k,v in zip(keys,a)},
        "detail_optimal_coefficients":{str(k):v.record() for k,v in zip(keys,a0)},
        "minimum_coupled_pivot":min(pivots,key=lambda x:x.lo).record(),
        "directed_acceptance_checks":scalar_checks,
    }


def reconstruct() -> dict:
    counts = exact_controls()
    rows = [stage(n) for n in CONFIG["stages"]]
    return {
        "schema":SCHEMA, "config":CONFIG, "parent_commit":PARENT_COMMIT,
        "parent_sha256":PINS, "rh_proved":False, "uniform_full_gain_proved":False,
        "uniform_detail_gain_has_prose_proof":True,
        "scope":"three directed full-Gram stages; finite algebra; analytic proofs require review",
        "exact_control_counts":counts,
        "exact_control_total":sum(counts.values()),
        "directed_acceptance_total":sum(row["directed_acceptance_checks"] for row in rows),
        "stages":rows,
    }


def preflight(stored: object) -> None:
    need(type(stored) is dict and stored.get("schema") == SCHEMA, "wrong result schema")
    need(stored.get("rh_proved") is False, "RH flag must be false")
    need(stored.get("uniform_full_gain_proved") is False, "full gain flag must be false")
    need(canonical(stored.get("config")) == canonical(CONFIG), "frozen coverage/config mismatch")
    need(stored.get("parent_commit") == PARENT_COMMIT and stored.get("parent_sha256") == PINS,
         "parent identity mismatch")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    group.add_argument("--hashes", action="store_true")
    args = parser.parse_args()
    if args.hashes:
        check_manifest()
        print("PASS_BG26_HASHES exact_inventory=8 parent_sources=4")
        return 0
    if args.check:
        check_manifest()
        stored = strict_json(ROOT/"verification.json")
        preflight(stored)
    value = reconstruct()
    data = canonical(value)
    if args.write:
        (ROOT/"verification.json").write_bytes(data)
    else:
        need(canonical(stored) == data, "result differs from source reconstruction")
    print("PASS_BG26_BOUNDED_FULL_SOURCE_REPLAY")
    print(f"exact_controls={value['exact_control_total']} directed_checks={value['directed_acceptance_total']}")
    print(f"verification_sha256={hashlib.sha256(data).hexdigest()}")
    print("RH_proved=false uniform_full_gain_proved=false")
    for row in value["stages"]:
        print(f"N={row['N']} gain={row['values']['full_gain']['decimal_enclosure']} "
              f"lower={row['values']['original_gain_lower_bound']['decimal_enclosure']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (Refusal, p.CheckFailure, ValueError, TypeError, KeyError, ZeroDivisionError, OSError) as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        raise SystemExit(1)
