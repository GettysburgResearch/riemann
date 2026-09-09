#!/usr/bin/env python3
"""Exact producer for EPC26; every displayed energy includes the final tail.

No RH claim is checked. Producer and verifier were authored in this session.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def canonical(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def sha(obj: object) -> str:
    return hashlib.sha256(canonical(obj)).hexdigest()


def frac(x: F) -> list[int]:
    return [x.numerator, x.denominator]


def clean(a: dict[int, F]) -> dict[int, F]:
    return {n: F(x) for n, x in a.items() if x}


def add(a: dict[int, F], b: dict[int, F], c: int = 1) -> dict[int, F]:
    z = a.copy()
    for n, x in b.items():
        z[n] = z.get(n, F()) + c*x
    return clean(z)


def mul(a: dict[int, F], b: dict[int, F]) -> dict[int, F]:
    out: dict[int, F] = {}
    for n, x in a.items():
        for m, y in b.items():
            out[n*m] = out.get(n*m, F()) + x*y
    return clean(out)


def rows(a: dict[int, F]) -> list[list[int]]:
    return [[n, x.numerator, x.denominator] for n, x in sorted(a.items())]


def norm(a: dict[int, F]) -> F:
    """Integer-event cell integration, followed by the complete constant tail."""
    ids = sorted(a)
    cumulative = value = F()
    for i, n in enumerate(ids):
        cumulative += a[n]
        cell = F(1, n) - F(1, ids[i+1]) if i+1 < len(ids) else F(1, n)
        value += cumulative*cumulative*cell
    return value


def pair(a: dict[int, F], b: dict[int, F]) -> F:
    return sum((x*y/F(max(n, m)) for n, x in a.items() for m, y in b.items()), F())


def at_one(a: dict[int, F]) -> F:
    return sum((x/F(n) for n, x in a.items()), F())


def sieve(N: int) -> tuple[list[int], list[int]]:
    prime = [True]*(N+1)
    prime[:2] = [False, False]
    ps = []
    for p in range(2, N+1):
        if prime[p]:
            ps.append(p)
            for k in range(p*p, N+1, p):
                prime[k] = False
    mu = [1]*(N+1)
    mu[0] = 0
    for p in ps:
        for k in range(p, N+1, p):
            mu[k] *= -1
        for k in range(p*p, N+1, p*p):
            mu[k] = 0
    return ps, mu


def targets(Y: int, mu: list[int]) -> tuple[dict, dict, F, F, F]:
    a = clean({n: F(mu[n]) for n in range(1, Y+1)})
    M = sum(mu[1:Y+1])
    core = add(a, {Y+1: F(-M)})
    jet = add(a, {Y+1: -(Y+1)*at_one(a)})
    running = 0
    E = c = F()
    for n in range(1, Y+1):
        running += mu[n]
        E += F(running*running, n*(n+1))
        c += F(running, n*(n+1))
    Fjet = E+(Y+1)*c*c
    need(norm(core) == E and norm(jet) == Fjet, "optimal completion energies")
    need(at_one(jet) == 0, "safe-point zero")
    need(norm(a) == E+F(M*M, Y+1), "native tail identity")
    return core, jet, E, Fjet, c


def build() -> dict:
    ps, mu = sieve(256)
    native = []
    panels = []
    for Y in range(1, 257):
        core, jet, E, Ej, c = targets(Y, mu)
        a = clean({n: F(mu[n]) for n in range(1, Y+1)})
        if Y <= 16:
            need(norm(a) == pair(a, a), "max-kernel native energy")
        row = [Y, sum(mu[1:Y+1]), frac(E), frac(Ej), frac(c)]
        native.append(row)
        if Y in (1, 2, 3, 5, 7, 11, 32, 128, 256):
            panels.append(row)
    projections = []
    for Y in (1, 2, 3, 5, 8, 16, 32):
        core, jet, E, Ej, c = targets(Y, mu)
        for t in (-3, 1, 5):
            d = Y+3
            err = {d: F(t), 2*d: F(1-t), 3*d+1: F(-2)}
            need(norm(add(core, err)) == E+norm(err), "free projection Pythagoras")
            jeterr = {d: F(t*d), 2*d: F(-2*t*d)}
            need(at_one(jeterr) == 0, "jet perturbation constraint")
            need(norm(add(jet, jeterr)) == Ej+norm(jeterr), "jet projection Pythagoras")
            need(pair(core, err) == pair(jet, jeterr) == 0, "orthogonality")
            projections.append([Y, t, frac(norm(err)), frac(norm(jeterr))])
    finite = []
    expansions = []
    for Y in (2, 3, 5, 7, 11, 13, 17, 19):
        primes = [p for p in ps if p <= Y]
        core, jet, E, Ej, _ = targets(Y, mu)
        for scale in (1, 4, 64):
            H = scale*Y*Y
            factors = []
            D = {1: F(1)}
            upper_product = F(1)
            for p in primes:
                m, q = 1, p
                while q <= H:
                    m += 1
                    q *= p
                need(q > H and q//p <= H and m >= 3, "minimal prime-power lift")
                factors.append([p, m, q])
                D = mul(D, {1: F(1), q: F(-1)})
                root = isqrt(q)
                need(root > 0 and root*root <= q < (root+1)**2, "root enclosure")
                upper_product *= 1+F(1, root)
            eta_hi = upper_product-1
            for label, C, optimum in (("free", core, E), ("zero_at_one", jet, Ej)):
                out = mul(C, D)
                error = add(out, C, -1)
                measured = norm(out)
                need(measured == optimum+norm(error), "complete repaired energy")
                need(0 <= measured-optimum <= optimum*eta_hi*eta_hi, "whole-norm relative bound")
                need(all(out.get(n, 0) == mu[n] for n in range(1, Y+1)), "native prefix preserved")
                if label == "zero_at_one":
                    need(at_one(out) == 0, "zero preserved by product")
                if Y <= 5:
                    need(pair(C, error) == 0 and pair(out, out) == measured, "complete pair replay")
                full_B = Y <= 7 and scale == 1
                B_count = B_max = None
                if full_B:
                    Euler = G = {1: F(1)}
                    for p, m, q in factors:
                        Euler = mul(Euler, {1: F(1), p: F(-1)})
                        G = mul(G, {p**j: F(1) for j in range(m)})
                    B = mul(C, G)
                    coefficient_cap = F(2*Y) if label == "free" else Y+(Y+1)*sum((F(1,n) for n in range(1,Y+1)),F())
                    need(all(abs(v) <= coefficient_cap for v in B.values()), "repair coefficient budget")
                    need(mul(Euler, B) == out, "entire Euler-repair expansion")
                    need(all(B.get(n, 0) == int(n == 1) for n in range(1, Y+1)), "late-only B")
                    B_count, B_max = len(B), max(B)
                    expansions.append([Y, label, sha(rows(B)), B_count, B_max])
                finite.append({"Y": Y, "H": H, "kind": label, "factors": factors,
                               "optimum": frac(optimum), "energy": frac(measured),
                               "relative_excess": frac(measured/optimum-1), "eta_upper": frac(eta_hi),
                               "output_terms": len(out), "output_max_index": max(out),
                               "output_sha256": sha(rows(out)), "full_B_expanded": full_B,
                               "B_terms": B_count, "B_max_index": B_max})
    # Controls distinguish literal tails, the prefix, and the extra constraint.
    need(norm({1: F(1)}) == 1, "terminal source tail")
    need(targets(3, mu)[2] == F(7, 12), "Y=3 optimum")
    need(at_one(targets(3, mu)[0]) == F(5, 12), "zero total is not zero at s=1")
    wrong = mul(targets(5, mu)[0], {1: F(1), 4: F(-1)})
    need(wrong.get(4, 0) != mu[4], "early factor must spoil prefix")
    return {"schema": "EPC26/v1", "status": "PROPOSED_NOT_RH_PROOF",
            "scope": {"complete_finite_output_energy": True, "all_Y_by_finite_test": False,
                      "full_repository_validation": False, "independent_mathematical_review": False},
            "native": {"prefix_count": 256, "rows_sha256": sha(native), "panels": panels},
            "projection": {"cases": len(projections), "rows_sha256": sha(projections)},
            "repairs": finite, "expanded_B": expansions,
            "controls": {"one_atom_full_energy": [1, 1], "Y3_free_optimum": [7, 12],
                         "Y3_safe_zero_optimum": [23, 18], "Y3_core_value_at_one": [5, 12],
                         "early_factor_rejected": True}}



def compact(full: dict) -> dict:
    selected = [row for row in full["repairs"] if row["Y"] in (7,19) and row["H"] == 64*row["Y"]**2]
    return {**{k: v for k,v in full.items() if k != "repairs"},
            "repairs": {"case_count": len(full["repairs"]), "rows_sha256": sha(full["repairs"]),
                        "panels": selected}, "full_reconstruction_sha256": sha(full)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--emit", type=Path, help="write a regenerated report; not validation")
    ap.add_argument("--check", type=Path, help="compare without changing the artifact")
    ap.add_argument("--full-output", type=Path, help="all 48 reconstructed case records")
    args = ap.parse_args()
    need(args.emit is not None or args.check is not None, "choose --emit or --check")
    full = build()
    body = compact(full)
    if args.full_output:
        args.full_output.write_bytes(canonical(full)+b"\n")
    report = {"body": body, "sha256": sha(body)}
    if args.check:
        need(canonical(json.loads(args.check.read_text())) == canonical(report), "canonical report mismatch")
    if args.emit:
        args.emit.parent.mkdir(parents=True, exist_ok=True)
        args.emit.write_bytes(canonical(report)+b"\n")
    print("PRODUCER PASS", report["sha256"])
    print("prefixes", body["native"]["prefix_count"], "repairs", body["repairs"]["case_count"],
          "complete_B_expansions", len(body["expanded_B"]))


if __name__ == "__main__":
    main()
