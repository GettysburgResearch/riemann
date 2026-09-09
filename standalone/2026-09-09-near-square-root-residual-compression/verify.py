#!/usr/bin/env python3
"""Bounded exact controls for SC1--SC4. Not an analytic or RH proof checker.

--emit reconstructs the mathematical record; --check also authenticates the
complete sealed packet. No external modules, numerical zeta, or float inputs.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import sys

FILES = {"PROOF.md", "README.md", "REVIEW.md", "SOURCES.json", "VALIDATION.md",
         "verify.py", "test_rejections.py", "result.json", "SHA256SUMS"}
ROOT = Path(__file__).resolve().parent
PARENT = "db175de165a9077e709b1cb482998171ffc0c6e7"

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))

def add(a, b):
    return [x+y for x, y in zip(a, b)]

def sub(a, b):
    return [x-y for x, y in zip(a, b)]

def scale(q, a):
    return [q*x for x in a]

def orthogonal(rows):
    basis = []
    for row in rows:
        v = list(map(F, row))
        for b in basis:
            v = sub(v, scale(dot(v, b)/dot(b, b), b))
        if dot(v, v):
            basis.append(v)
    return basis

def project(v, basis):
    out = [F(0)]*len(v)
    for b in basis:
        out = add(out, scale(dot(v, b)/dot(b, b), b))
    return out

def poly_mul(p, q):
    out = [F(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out

def poly_pow(p, k):
    q = [F(1)]
    for _ in range(k):
        q = poly_mul(q, p)
    return q

def mobius_sieve(n):
    mu, primes = [1]*(n+1), [True]*(n+1)
    mu[0] = 0
    for p in range(2, n+1):
        if primes[p]:
            for k in range(p, n+1, p):
                primes[k] = False
                mu[k] *= -1
            for k in range(p*p, n+1, p*p):
                mu[k] = 0
    return mu

def factor(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out

def mobius_trial(n):
    fac = factor(n)
    return 0 if any(v > 1 for v in fac.values()) else (-1)**len(fac)

def enc(q):
    q = F(q)
    return f"{q.numerator}/{q.denominator}"

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)

def fingerprint(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()

def reconstruct():
    groups = {}
    panels = []
    # These are actual geometric integer nodes n_j=4*4^j. In coordinates
    # b_j=c_(n_j)/sqrt(n_j), S is Euclidean and all roots are rational.
    # Safe derivatives factor log 4; critical jets factor (log 4)^k.
    count = 0
    for m in range(4, 10):
        for centered in (False, True):
            rows = [[F(1, 2**(j+1)) for j in range(m)],
                    [F(j, 2**(j+1)) for j in range(m)]]
            if centered:
                rows.append([F(2**(j+1)) for j in range(m)])
            safe = orthogonal(rows)
            def pv(v):
                return sub(v, project(v, safe))
            raw = [F(2*j-3, j+1) for j in range(m)]
            v = pv(raw)
            anchor = project([F((j+1)**2, j+2) for j in range(m)], safe)
            for k in range(1, min(5, m)):
                critical = [pv([F(j**h) for j in range(m)]) for h in range(k)]
                retained = orthogonal(critical)
                pc = project(v, retained)
                rem = sub(v, pc)
                require(len(retained) <= k, "rank budget")
                for row in rows:
                    require(dot(row, pc) == 0 and dot(row, rem) == 0,
                            "safe constraints not preserved")
                for h in range(k):
                    require(dot([F(j**h) for j in range(m)], rem) == 0,
                            "critical jet not removed")
                require(project(pc, retained) == pc, "projection not idempotent")
                require(dot(pc, rem) == 0, "projection not orthogonal")
                require(dot(v, v) == dot(pc, pc)+dot(rem, rem), "Pythagoras")
                require(dot(add(anchor, pc), add(anchor, pc)) <=
                        dot(add(anchor, v), add(anchor, v)), "affine budget increased")
                for row in rows:
                    require(dot(row, add(anchor, pc)) == dot(row, anchor),
                            "affine constraint changed")
                w = pv([F(3-j, j+3) for j in range(m)])
                require(dot(project(v, retained), w) == dot(v, project(w, retained)),
                        "projection not self-adjoint")
                panels.append([m, centered, k, len(retained), enc(dot(rem, rem))])
                count += 1
    groups["exact_geometric_source_projection_panels"] = count
    projection_hash = fingerprint(panels)

    count = 0
    for k in range(1, 13):
        p = poly_mul(poly_mul(poly_pow([1, -1], k), poly_pow([1, -2], 2)),
                     [1, F(-1, 2)])
        for h in range(k):
            require(sum(p[j]*j**h for j in range(len(p))) == 0,
                    "geometric critical jet")
        require(sum(p[j]*F(1, 2**j) for j in range(len(p))) == 0, "balance")
        require(sum(j*p[j]*F(1, 2**j) for j in range(len(p))) == 0,
                "safe derivative")
        require(sum(p[j]*2**j for j in range(len(p))) == 0, "centering")
        c = [2**(j+1)*p[j] for j in range(len(p))]
        require(sum(c[j]**2/F(4*4**j) for j in range(len(c))) == dot(p, p),
                "source metric")
        count += 1
    groups["geometric_finite_difference_jet_polynomials"] = count

    for k in range(1, 65):
        require(F(k, 12)**k / math.factorial(k) <= F(1, 4**k),
                "finite Taylor budget")
    groups["finite_factorial_Taylor_budgets"] = 64

    rank = F(3, 5)
    exponents = {
        "power_rank_example": enc(rank),
        "squared_operator_power": enc(1-2*rank),
        "operator_power": enc((1-2*rank)/2),
        "near_square_root_log_rank": 2,
        "squared_operator_log_power": -3,
        "budgeted_error_log_power": -1}
    require(1-2*rank == F(-1, 5), "squared singular exponent")
    require((1-2*rank)/2 == F(-1, 10), "norm exponent")
    require(1-2*F(1, 2) == 0, "square-root threshold")
    require(1-2*2 == -3, "logarithmic squared error")
    require(F(-3+1, 2) == -1, "logarithmic budgeted norm error")
    groups["rational_rank_and_error_identities"] = 5

    # Finite exact source-form spectral ordering: no zeta eigenvalues supplied.
    spectral_count = 0
    for dim in range(2, 9):
        eig = [F((dim-j)**2, j+1) for j in range(dim)]
        for eta in (F(1, 4), F(1, 2)):
            hat = [v*(1+eta*((-1)**j)) for j, v in enumerate(eig)]
            order = sorted(range(dim), key=lambda j: hat[j], reverse=True)
            for r in range(1, dim):
                remainder = max(eig[j] for j in order[r:])
                require(remainder <= hat[order[r]]/(1-eta), "a posteriori bound")
                require(hat[order[r]] <= (1+eta)*eig[r], "eigenvalue ordering")
                k = r//2
                require((r+1-k)*eig[r] <= sum(eig[k:]), "trace-tail counting")
                spectral_count += 1
    groups["finite_spectral_trace_and_form_transfer_panels"] = spectral_count

    # The exact complete-period mean in RC, here with homogeneous target b=0.
    period_records = []
    for n in (2, 4, 6, 8, 10):
        period = math.lcm(*range(1, n+1))
        for case in range(3):
            c = [F(0)]+[F((case+2)*j % 5-2, j+1) for j in range(1, n+1)]
            c[1] -= sum((c[j]/j for j in range(1, n+1)), F(0))
            mean = sum((sum(c[j]*(x//j) for j in range(1, n+1)))**2
                       for x in range(period))/period
            v = sum(c)**2/4
            for d in range(1, n+1):
                j2 = d*d
                for prime in factor(d):
                    j2 = j2*(prime*prime-1)//(prime*prime)
                row = sum((c[j]/j for j in range(d, n+1, d)), F(0))
                v += F(j2, 12)*row**2
            require(mean == v, "full rational period mean")
            period_records.append([n, case, period, enc(v)])
    groups["complete_small_period_mean_panels"] = len(period_records)

    mu = mobius_sieve(256)
    for n in range(1, 257):
        require(mu[n] == mobius_trial(n), "Mobius producer disagreement")
    groups["independent_Mobius_values"] = 256
    for j in range(1, 129):
        require(sum(mu[n]*(j//n) for n in range(1, j+1)) == 1,
                "literal floor prefix")
    groups["native_floor_prefix_identities"] = 128

    graph_records = []
    for y, n in [(2, 8), (3, 12), (4, 16), (5, 20), (8, 32)]:
        for case in range(3):
            c = [F(0)]*(n+1)
            for j in range(y, n+1):
                c[j] = F(((case+2)*j) % 7-3, j-y+1)
            c[y] -= y*sum((c[j]/j for j in range(y, n+1)), F(0))
            require(sum((c[j]/j for j in range(1, n+1)), F(0)) == 0,
                    "graph test not balanced")
            edges, expanded, below = defaultdict(F), defaultdict(F), defaultdict(F)
            for r in range(2, n+1):
                fac = factor(r)
                if len(fac) != 1:
                    continue
                p = next(iter(fac))
                for j in range(1, n//r+1):
                    child = r*j
                    edges[p] += (c[child]-c[j])**2/child
                    expanded[p] += c[j]**2/child - 2*c[child]*c[j]/child
                    if j < y <= child:
                        below[p] += c[child]**2/child
            for child in range(1, n+1):
                for p, a in factor(child).items():
                    expanded[p] += a*c[child]**2/child
            require(dict(edges) == dict(expanded), "complete prime-power expansion")
            for p in edges:
                require(edges[p] >= below[p], "discarded squares negative")
            graph_records.append([y, n, case,
                                  {str(p): enc(v) for p, v in sorted(edges.items())}])
    groups["complete_formal_prime_log_graph_panels"] = len(graph_records)
    return {
        "packet": "near-square-root-residual-compression-SC1-SC4",
        "parent_sha": PARENT,
        "status": "PROPOSED_COMPONENT_PROOFS_REVIEW_REQUIRED",
        "rh_proved": False,
        "arithmetic_upper_bound_proved": False,
        "actual_zeta_norms_computed": 0,
        "new_numerical_minima": 0,
        "external_analytic_input": "Classical approximate functional equation, DLMF 25.9.3; analytic identity imported",
        "groups": groups,
        "bounded_panels": sum(groups.values()),
        "projection_fingerprint": projection_hash,
        "graph_fingerprint": fingerprint(graph_records),
        "period_fingerprint": fingerprint(period_records),
        "exponents": exponents,
        "coverage_note": "Finite algebra only. No numerical all-scale or RH inference."}

def unique_pairs(pairs):
    d = {}
    for k, v in pairs:
        require(k not in d, f"duplicate JSON key: {k}")
        d[k] = v
    return d

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs,
                      parse_float=lambda s: (_ for _ in ()).throw(ValueError("float rejected")))

def same_typed(a, b):
    require(type(a) is type(b), "JSON type alias")
    if isinstance(a, dict):
        require(a.keys() == b.keys(), "JSON fields")
        for k in a:
            same_typed(a[k], b[k])
    elif isinstance(a, list):
        require(len(a) == len(b), "JSON list length")
        for x, y in zip(a, b):
            same_typed(x, y)
    else:
        require(a == b, "reconstructed value mismatch")

def authenticate():
    require(not Path(__file__).is_symlink(), "checker symlink")
    entries = list(ROOT.iterdir())
    require({p.name for p in entries} == FILES, "packet inventory")
    require(all(p.is_file() and not p.is_symlink() for p in entries), "nonregular packet")
    lines = (ROOT/"SHA256SUMS").read_text().splitlines()
    hashes = {}
    for line in lines:
        h, name = line.split("  ")
        require(len(h) == 64 and all(c in "0123456789abcdef" for c in h), "hash format")
        require(name not in hashes, "duplicate manifest path")
        hashes[name] = h
    require(set(hashes) == FILES-{"SHA256SUMS"}, "manifest coverage")
    for name, h in hashes.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == h,
                f"file hash: {name}")
    source = load_json(ROOT/"SOURCES.json")
    require(source["parent"]["sha"] == PARENT, "parent identity")

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    modes = ap.add_mutually_exclusive_group(required=True)
    modes.add_argument("--emit", action="store_true")
    modes.add_argument("--check", type=Path)
    args = ap.parse_args()
    obj = reconstruct()
    if args.emit:
        print(json.dumps(obj, indent=2, sort_keys=True))
    else:
        authenticate()
        same_typed(load_json(args.check), obj)
        print("PASS_BOUNDED_COMPONENT_CONTROLS", obj["bounded_panels"], fingerprint(obj))

if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError, ZeroDivisionError) as exc:
        print("REJECT:", str(exc), file=sys.stderr)
        sys.exit(1)
