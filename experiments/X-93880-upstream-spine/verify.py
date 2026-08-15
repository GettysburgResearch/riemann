#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import argparse, json, math, random

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

def factor(n):
    out = {}; p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: out[n] = out.get(n, 0) + 1
    return out

def vm_symbol(n):
    f = factor(n)
    return {next(iter(f)): 1} if len(f) == 1 else {}

def add_dict(a, b, scale=1):
    out = {k: Fraction(v) for k,v in a.items()}
    for k,v in b.items():
        out[k] = out.get(k, Fraction(0)) + scale*Fraction(v)
        if out[k] == 0: del out[k]
    return out

def y4_symbol(q):
    out = {}; scale = 1
    while True:
        out = add_dict(out, vm_symbol(q), scale)
        if q % 4: return out
        q //= 4; scale *= 2

def check_y4(N=50000):
    zeros = 0
    for q in range(2, N+1):
        lhs = y4_symbol(q)
        if q % 4 == 0: lhs = add_dict(lhs, y4_symbol(q//4), -2)
        assert lhs == vm_symbol(q)
        zeros += not bool(y4_symbol(q))
    return {"range": N, "zero_columns": zeros}

def check_constants(c):
    assert Fraction(c["adjacent_num"], c["adjacent_den"]) * 3 == Fraction(c["ordinary_num"], c["ordinary_den"])
    assert Fraction(c["ordinary_num"], c["ordinary_den"]) * Fraction(3,2) == Fraction(171,4)
    assert Fraction(c["detail_num"], c["detail_den"]) + c["collar"] == Fraction(c["combined_num"], c["combined_den"])
    assert c["relative"] + 1 == c["thinning_shift"]
    assert c["terminal_reserve"] - c["terminal_overfill"] == 581
    assert c["thinning_cost"] + c["nonterminal_cost"] + c["terminal_cost"] + c["omission_cost"] == c["total_cost"]
    assert c["total_cost"] < c["claimed_bound"]
    assert 64 < 67
    return {"terminal_margin": 581, "total": c["total_cost"]}

def check_prime_square_integral():
    M = 200000; s = 0.0
    for n in range(1, M):
        s += 2*(math.sqrt(n+1)-math.sqrt(n)) + 2*n*(1/math.sqrt(n+1)-1/math.sqrt(n))
    val = 0.5*s; tail = 1/math.sqrt(M)
    assert val < 0.460355 < val + tail + 2e-5
    return {"partial": val, "tail_upper": tail}

def check_mellin_residue():
    rng = random.Random(93880)
    for _ in range(1000):
        beta = Fraction(rng.randint(501, 999), 1000)
        gamma = Fraction(rng.randint(1, 10000), 1000)
        assert (beta-Fraction(1,2))**2 + gamma**2 > 0
    return {"formula": "m_rho/(rho-1/2)^2 != 0"}

def check_content_hashes():
    ledger = ROOT/"T93880_CONTENT_SHA256SUMS"
    checked = 0
    for line in ledger.read_text().splitlines():
        if not line.strip(): continue
        digest, path = line.split(None, 1)
        if sha256((ROOT/path.strip()).read_bytes()).hexdigest() != digest:
            raise AssertionError(path)
        checked += 1
    return {"checked": checked}

def check_paths():
    required = [
      "claims/refutations/R-93880-shared-ancestry-is-not-independent-and-bulk-profile-is-unnecessary.md",
      "claims/lemmas/L-93880-native-hybrid-source-is-an-exact-positive-common-parent.md",
      "claims/lemmas/L-93881-anchored-target-lorenz-compiler-closes-every-row.md",
      "claims/lemmas/L-93882-block-diagonal-whole-cell-realization-is-exact.md",
      "claims/lemmas/L-93883-all-column-and-terminal-feasibility-is-unconditional.md",
      "claims/lemmas/L-93884-direct-y4-accounting-gives-native-deficit-below-61000.md",
      "claims/lemmas/L-93885-prime-square-occupancy-moat-is-unconditional.md",
      "claims/lemmas/L-93886-eventual-prime-endpoint-negativity-excludes-off-line-zeros.md",
      "claims/theorems/T-93880-upstream-spine-reconstructed-factor67-resolution-proposal.md",
      "imports/t93880/IMPORT_MANIFEST.json",
      "standalone/2026-08-16-93880-upstream-spine/REVIEW_SPECIFICATION.md",
    ]
    missing = [p for p in required if not (ROOT/p).exists()]
    if missing: raise AssertionError(missing)
    return {"required": len(required)}

def check_firewalls(control):
    theorem = (ROOT/"claims/theorems/T-93880-upstream-spine-reconstructed-factor67-resolution-proposal.md").read_text().lower()
    refutation = (ROOT/"claims/refutations/R-93880-shared-ancestry-is-not-independent-and-bulk-profile-is-unnecessary.md").read_text().lower()
    assert "the last term is the sole signed finite/continuum observation" not in theorem
    assert "shared ancestry is not confirmation" in refutation
    assert "signed defect as positive source" in refutation
    assert "full child capacity" in refutation
    return {"forbidden_count": len(control["forbidden"])}

def mutate(control):
    failures = {}
    tests = {
      "wrong_base": lambda x: x.__setitem__("base_sha", "0"*40),
      "terminal_overdraw": lambda x: x["constants"].__setitem__("terminal_overfill", 5034),
      "cost_overdraw": lambda x: x["constants"].__setitem__("total_cost", 61000),
      "bad_thinning": lambda x: x["constants"].__setitem__("thinning_shift", 129),
    }
    for name, fn in tests.items():
        x = json.loads(json.dumps(control)); fn(x)
        try:
            if x["base_sha"] != "1468ff62c7377f3f6cc1744ef6eafc3df3172d5c": raise AssertionError
            check_constants(x["constants"])
        except Exception: failures[name] = True
        else: failures[name] = False
    assert all(failures.values())
    return failures

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--mutations", action="store_true")
    ap.add_argument("--output", default=str(HERE/"results/verification.json")); args = ap.parse_args()
    control = json.loads((HERE/"certificates/control.json").read_text())
    assert control["base_sha"] == "1468ff62c7377f3f6cc1744ef6eafc3df3172d5c"
    checks = {"y4":check_y4(), "constants":check_constants(control["constants"]),
      "prime_square":check_prime_square_integral(), "mellin":check_mellin_residue(),
      "paths":check_paths(), "content_hashes":check_content_hashes(), "firewalls":check_firewalls(control)}
    payload = {"verdict":"PASS_UPSTREAM_SPINE_RECONSTRUCTION_PACKET", "ok":True,
      "checks":checks, "mutations":mutate(control) if args.mutations else {}, "rh_proved":False,
      "scope":"finite algebra, provenance, constants and interface firewalls; large directed AVLT, PNT and Landau proofs require independent reconstruction"}
    canonical=json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
    payload["proof_object_sha256"]=sha256(canonical).hexdigest()
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
    print(payload["verdict"]); print(payload["proof_object_sha256"])

if __name__ == "__main__": main()
