#!/usr/bin/env python3
"""Bounded exact source checks; NOT an analytic or RH proof checker."""
from __future__ import annotations
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARENT_REL = "../2026-09-07-astra-balanced-hyperbola/PROOF.md"
PARENT_SHA256 = "02669fd041a1327f214c0212027bda4dac631909e1c2144e90764e55d25914ee"
LOCK = {
    "repository": "GettysburgResearch/riemann",
    "pr": 805,
    "parent_commit": "ccd0a80dbd9844d06ccd6331a15b085b9c9afa41",
    "parent_proof": "standalone/2026-09-07-astra-balanced-hyperbola/PROOF.md",
    "parent_blob": "2af125b452015a0b73483eef66b0995b6c874097",
    "parent_bytes": 17079,
    "parent_sha256": PARENT_SHA256,
}
PAYLOAD = {"PROOF.md", "README.md", "VALIDATION.md", "SOURCE_LOCK.json",
           "check.py", "verification.json"}
YS = (3, 5, 9, 17)


def fail(message: str) -> None:
    raise ValueError(message)


def strict_json(path: Path):
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                fail("duplicate JSON key")
            out[key] = value
        return out
    def no_float(value):
        fail("noninteger JSON number: " + value)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs,
                      parse_float=no_float, parse_constant=no_float)


def canonical(value) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n"


def authenticate_parent() -> None:
    p = ROOT / PARENT_REL
    if p.is_symlink() or not p.is_file():
        fail("missing or symlink parent")
    data = p.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    if len(data) != LOCK["parent_bytes"] or blob != LOCK["parent_blob"]:
        fail("parent blob/length mismatch")
    if hashlib.sha256(data).hexdigest() != PARENT_SHA256:
        fail("parent SHA-256 mismatch")


def verify_manifest() -> None:
    paths = list(ROOT.iterdir())
    if any(p.is_symlink() or not p.is_file() for p in paths):
        fail("payload contains a symlink or nonfile")
    if {p.name for p in paths} != PAYLOAD | {"SHA256SUMS"}:
        fail("payload inventory mismatch")
    seen = set()
    for line in (ROOT / "SHA256SUMS").read_text().splitlines():
        parts = line.split("  ")
        if len(parts) != 2:
            fail("malformed manifest")
        digest, name = parts
        if name not in PAYLOAD or name in seen:
            fail("unexpected or duplicate manifest path")
        seen.add(name)
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != digest:
            fail("payload digest mismatch: " + name)
    if seen != PAYLOAD:
        fail("incomplete or empty manifest")
    if canonical(strict_json(ROOT / "SOURCE_LOCK.json")) != canonical(LOCK):
        fail("source-lock drift")


def mobius_trial(n: int) -> int:
    value, p, sign = n, 2, 1
    while p * p <= value:
        if value % p == 0:
            value //= p
            sign = -sign
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    return -sign if value > 1 else sign


def mobius_sieve(cap: int) -> list[int]:
    mu = [1] * (cap + 1)
    composite = [False] * (cap + 1)
    for p in range(2, cap + 1):
        if not composite[p]:
            for n in range(p, cap + 1, p):
                composite[n] = True
                mu[n] *= -1
            for n in range(p * p, cap + 1, p * p):
                mu[n] = 0
    mu[0] = 0
    return mu


def q(x: F, mu: list[int]) -> F:
    if x.numerator // x.denominator >= len(mu):
        fail("Q request exceeds the primitive range")
    return sum((F(mu[n]) * (1 - x / n)
                for n in range(1, x.numerator // x.denominator + 1, 2)), F(0))


def w(z: F) -> F:
    return sum((z / r - 1 for r in range(1, z.numerator // z.denominator + 1, 2)), F(0))


def compute() -> dict:
    counts = Counter()
    def check(condition: bool, label: str) -> None:
        if not condition:
            fail("algebra failure: " + label)
        counts[label] += 1
    cap = max(max(YS), 2*3**2+1) ** 2
    mu = mobius_sieve(cap)
    for n in range(1, cap + 1):
        check(mu[n] == mobius_trial(n), "independent_mobius")
    rows = []
    for y in YS:
        odd = list(range(1, y + 1, 2))
        harmonic = sum((F(mu[k], k) for k in odd), F(0))
        lam = {k: F(mu[k]) - (y * harmonic if k == y else 0) for k in odd}
        check(lam[1] == 1, "first_coefficient")
        check(sum((lam[k] / k for k in odd), F(0)) == 0, "pole_cancelling_balance")
        check(abs(harmonic) <= 2, "bounded_harmonic_sum")
        value = sum((lam[a] * lam[b] * w(F(y*y, a*b))
                     for a in odd for b in odd), F(0))
        target = q(F(y*y), mu) - 2*q(F(y), mu)
        check(value == target, "quadratic_vs_long_scalar")
        coeff = [F(0)] * (y*y + 1)
        for a in odd:
            for b in odd:
                for r in range(1, y*y // (a*b) + 1, 2):
                    coeff[a*b*r] += lam[a]*lam[b]
        perron_sum = sum((coeff[n]*(F(y*y,n)-1)
                          for n in range(1,y*y+1,2)), F(0))
        check(perron_sum == value, "perron_coefficient_expansion")
        check(sum(lam.values(), F(0)) == q(F(y), mu), "total_coefficient")
        check(w(F(1)) == 0, "zero_endpoint_weight")
        # P(1)=0 implies the coefficients of both possible principal poles vanish.
        mass = sum((lam[k]/k for k in odd), F(0))
        check(mass*mass == 0, "double_pole_coefficient")
        for k in odd:
            check(F(2)*mass*lam[k]/k == 0, "formal_log_pole_coefficient")
        rows.append({"Y": y, "B": str(value), "Q_Y": str(q(F(y),mu)),
                     "Q_Y_squared": str(q(F(y*y),mu)),
                     "lambda": {str(k): str(lam[k]) for k in odd}})
    # Original grid and interpolation, checked against direct rational hinge sums.
    grids = []
    for j in (1, 2):
        ya, yb = 2*j*j+1, 2*(j+1)**2+1
        a, b = ya*ya, yb*yb
        for t in (F(1,4), F(1,2), F(3,4)):
            x = a+(b-a)*t
            linear = (1-t)*q(F(a),mu)+t*q(F(b),mu)
            green = sum((F(mu[k],k)*(min(x,k)-a)*(b-max(x,k))/(b-a)
                         for k in range(a+2,b,2)), F(0))
            check(q(x,mu)-linear == green, "exact_grid_interpolation")
            error_bound = F((b-a)**2,8*a)
            check(abs(green) <= error_bound, "interpolation_bound")
        grids.append([ya,yb])
    # Tail exponent: Y^2 (Y^(4/3))^(-3/4)=Y; tested without floating powers.
    check(F(2)-F(4,3)*F(3,4) == 1, "tail_power")
    return {"schema": "riemann-critical-line-attempt-v1",
            "rh_proved": False, "near_linear_bound_proved": False,
            "scope": {"Y": list(YS), "mobius_cap": cap,
                      "analytic_integrals_evaluated": False,
                      "external_mertens_replayed": False},
            "rows": rows, "grid_pairs": grids,
            "checks": dict(sorted(counts.items())), "check_total": sum(counts.values())}


def seal(path: Path) -> None:
    text = "".join(hashlib.sha256((path / n).read_bytes()).hexdigest()+"  "+n+"\n"
                   for n in sorted(PAYLOAD))
    (path / "SHA256SUMS").write_text(text, encoding="utf-8")


def self_test() -> None:
    cases = ("false_claim", "wrong_scalar", "missing_row", "float_alias",
             "duplicate_json", "empty_manifest", "extra_path", "parent_changed",
             "symlink")
    for case in cases:
        with tempfile.TemporaryDirectory() as td:
            top = Path(td)
            clone = top / ROOT.name
            shutil.copytree(ROOT, clone)
            parent = top / "2026-09-07-astra-balanced-hyperbola"
            parent.mkdir()
            shutil.copy2(ROOT/PARENT_REL, parent/"PROOF.md")
            command = [sys.executable] + (["-O"] if sys.flags.optimize else []) + [str(clone/"check.py")]
            if case == cases[0]:
                baseline = subprocess.run(command, capture_output=True, text=True, timeout=15)
                if baseline.returncode != 0:
                    fail("pristine copied packet failed")
            result = strict_json(clone/"verification.json")
            if case == "false_claim": result["near_linear_bound_proved"] = True
            if case == "wrong_scalar": result["rows"][0]["B"] = "0"
            if case == "missing_row": result["rows"].pop()
            if case == "float_alias": result["check_total"] = float(result["check_total"])
            (clone/"verification.json").write_text(canonical(result))
            if case == "duplicate_json":
                text = (clone/"verification.json").read_text()
                (clone/"verification.json").write_text(text.replace("{", '{"rh_proved": false,', 1))
            seal(clone)
            if case == "empty_manifest": (clone/"SHA256SUMS").write_text("")
            if case == "extra_path": (clone/"unexpected.txt").write_text("extra")
            if case == "parent_changed": (parent/"PROOF.md").write_bytes(b"changed")
            if case == "symlink":
                outside = top/"outside.txt"
                shutil.copy2(clone/"README.md", outside)
                (clone/"README.md").unlink()
                (clone/"README.md").symlink_to(outside)
            command = [sys.executable] + (["-O"] if sys.flags.optimize else []) + [str(clone/"check.py")]
            completed = subprocess.run(command, capture_output=True, text=True, timeout=15)
            if completed.returncode == 0 or "REJECT: " not in completed.stderr:
                fail("corruption was not explicitly rejected: " + case)
    print("PASS_REJECTIONS cases="+str(len(cases)))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--emit", type=Path, help="generation only; does not validate the manifest")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    authenticate_parent()
    if args.emit is not None:
        args.emit.write_text(canonical(compute()), encoding="utf-8")
        print("GENERATED_BOUNDED_FIXTURE")
        return
    verify_manifest()
    expected, actual = strict_json(ROOT/"verification.json"), compute()
    if canonical(expected) != canonical(actual):
        fail("reconstructed result mismatch")
    print("PASS_BOUNDED_SOURCE_CHECKS count="+str(actual["check_total"])+" rh_proved=false")
    if args.self_test:
        self_test()


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError, subprocess.TimeoutExpired) as exc:
        print("REJECT: "+str(exc), file=sys.stderr)
        sys.exit(1)
