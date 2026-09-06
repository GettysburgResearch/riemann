#!/usr/bin/env python3
"""Bounded reconstruction of the literal infinite Gram entries and witnesses.

Run --write once to emit verification.json; --check independently reconstructs
it from these formulas. The checker does not import a repository producer.
It proves no unbounded gain inequality, convergence rate, or RH statement.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from math import gcd
from pathlib import Path

# Explicit local import also works in isolated (-I -S) interpreter mode.
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from intervals import (I, BITS, DIGAMMA_SHIFT, EM_ORDER, LOG_TERMS, SCALE,
                       bernoulli, log_q, pi_interval, psi_q)

ROOT = HERE.parent
MAX_N = 16
STAGES = (2, 3, 4, 8, 16)
DOUBLINGS = (2, 4, 8)
CONFIG = {"max_n": MAX_N, "stages": list(STAGES), "doublings": list(DOUBLINGS),
          "bits": BITS, "log_terms": LOG_TERMS,
          "digamma_shift": DIGAMMA_SHIFT, "em_order": EM_ORDER,
          "exact_dilation_m_max": 7, "exact_dilation_k_max": 16,
          "exact_dilation_n_max": 100, "biorthogonal_max": 24,
          "coarse_gram_prefix": 1024}


class CheckFailure(Exception):
    pass


def need(condition: bool, label: str) -> None:
    if condition is not True:
        raise CheckFailure(label)


def dot(a: list[I], b: list[I]) -> I:
    if len(a) != len(b):
        raise ValueError("dot-product length mismatch")
    return sum((x*y for x, y in zip(a, b)), I.of(0))


def matvec(a: list[list[I]], b: list[I]) -> list[I]:
    return [dot(row, b) for row in a]


def solve(a: list[list[I]], b: list[I]) -> tuple[list[I], list[I]]:
    """Outward interval elimination; reject any nonpositive pivot enclosure."""
    n = len(b)
    if n == 0 or len(a) != n or any(len(row) != n for row in a):
        raise ValueError("nonempty square matrix required")
    t, rhs, pivots = [row[:] for row in a], b[:], []
    for k in range(n):
        pivot = t[k][k]
        need(pivot.lo > 0, f"nonpositive or unresolved pivot {k}")
        pivots.append(pivot)
        for j in range(k+1, n):
            factor = t[j][k]/pivot
            for l in range(k+1, n):
                t[j][l] -= factor*t[k][l]
            rhs[j] -= factor*rhs[k]
            t[j][k] = I.of(0)  # The exact Gaussian-eliminated entry is zero.
    x = [I.of(0) for _ in range(n)]
    for k in range(n-1, -1, -1):
        x[k] = (rhs[k]-dot(t[k][k+1:], x[k+1:]))/t[k][k]
    return x, pivots


@lru_cache(maxsize=4096, typed=True)
def gram(j: int, k: int) -> I:
    if not (type(j) is int and type(k) is int and 2 <= j <= MAX_N and 2 <= k <= MAX_N):
        raise ValueError("Gram query outside frozen 2..16 domain")
    if j > k:
        return gram(k, j)
    period = j*k//gcd(j, k)
    out = I.of(0)
    for r in range(1, period):
        a = F((r % j)*(r % k), j*k)
        if a:
            out += a*(psi_q(F(r+1, period))-psi_q(F(r, period)))/period
    return out


def bvalue(k: int) -> I:
    return log_q(F(k))/k


def h(k: int, n: int) -> F:
    return F(n % k, k)


def mobius(n: int) -> int:
    if type(n) is not int or n < 1:
        raise ValueError("positive integer required")
    sign, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def phi(d: int) -> dict[int, int]:
    out = {d: -d*(d+1)}
    if d > 1:
        out[d-1] = d*(d-1)
    return out


def dual(q: int) -> dict[int, int]:
    out: dict[int, int] = {}
    for d in range(1, q+1):
        if q % d == 0:
            for n, v in phi(d).items():
                out[n] = out.get(n, 0)+mobius(q//d)*v
    return {n: v for n, v in sorted(out.items()) if v}


def exact_controls() -> dict[str, int]:
    counts = {"dilation_identity": 0, "finite_vector_dilation_norm": 0,
              "biorthogonality": 0, "dual_target": 0,
              "mobius_independent": 0, "special_witness": 0}
    for m in range(2, 8):
        for k in range(2, 17):
            for n in range(101):
                need(h(k, n//m) == h(m*k, n)-h(m,n)/k, "dilation identity")
                counts["dilation_identity"] += 1
        v = [F(0)]+[F((-1)**n*(n+1), n+2) for n in range(1, 10)]
        original = sum(v[n]**2/F(n*(n+1)) for n in range(1, len(v)))
        dilated = sum(v[n//m]**2/F(n*(n+1))
                      for n in range(1, m*len(v)))
        need(dilated == original/m, "dilation norm")
        counts["finite_vector_dilation_norm"] += 1
    # A separate inclusion/exclusion sieve to test the trial-factor Mobius routine.
    mu = [0]+[1]*24
    primes = [p for p in range(2,25) if all(p%d for d in range(2,p))]
    for p in primes:
        for n in range(p,25,p):
            mu[n] *= -1
        for n in range(p*p,25,p*p):
            mu[n] = 0
    for q in range(1,25):
        need(mu[q] == mobius(q), "Mobius routines disagree")
        counts["mobius_independent"] += 1
    for q in range(2,25):
        f = dual(q)
        target = sum(F(v, n*(n+1)) for n,v in f.items())
        need(target == -mobius(q), "dual target")
        counts["dual_target"] += 1
        for k in range(2,25):
            value = sum(h(k,n)*F(v,n*(n+1)) for n,v in f.items())
            need(value == int(k==q), "biorthogonality")
            counts["biorthogonality"] += 1
    for q, norm in [(2,14),(3,20),(5,52),(7,100),(11,244)]:
        need(sum(F(v*v,n*(n+1)) for n,v in dual(q).items()) == norm, "dual norm")
        counts["special_witness"] += 1
    need(dual(5) == {1:2,4:20,5:-30}, "five witness source")
    counts["special_witness"] += 1
    return counts


def projection(n: int) -> dict[str, object]:
    keys = list(range(2,n+1))
    g = [[gram(j,k) for k in keys] for j in keys]
    b = [bvalue(k) for k in keys]
    c, pivots = solve(g,b)
    delta = 1-dot(b,c)
    first = sum((c[k-2]/k for k in keys), I.of(0))
    need(delta.lo > 0 and delta.hi < SCALE, "finite distance range")
    need(delta.width() < F(1,10**25), "distance enclosure too wide")
    need(first.width() < F(1,10**25), "first-cell enclosure too wide")
    return {"keys": keys, "G": g, "b": b, "c": c, "pivots": pivots,
            "delta": delta, "first": first}


def doubling(n: int, a: dict, aa: dict) -> dict[str, object]:
    old, new = list(range(2,n+1)), list(range(n+1,2*n+1))
    g, b, c, delta = a["G"], a["b"], a["c"], a["delta"]
    C = [[gram(i,k) for k in new] for i in old]
    D = [[gram(i,k) for k in new] for i in new]
    columns = [[C[i][j] for i in range(len(old))] for j in range(len(new))]
    sols = [solve(g,col)[0] for col in columns]
    schur = [[D[i][j]-dot(columns[i],sols[j]) for j in range(len(new))]
             for i in range(len(new))]
    z = [bvalue(k)-dot(columns[j],c) for j,k in enumerate(new)]
    inv_z, schur_pivots = solve(schur,z)
    gain = dot(z,inv_z)
    difference = delta-aa["delta"]
    need(gain.lo > 0, "unresolved positive Schur gain")
    need(gain.overlaps(difference), "Schur/direct gain mismatch")
    need(gain.width() < F(1,10**25), "Schur interval too wide")
    H = [[gram(i,2*k)-gram(i,2)/k for k in old] for i in old]
    d = matvec(H,c)
    L = (1-delta)/2-dot(c,d)
    eta = (1-delta)/2-dot(d,solve(g,d)[0])
    need(eta.lo > 0, "unresolved nonzero dilation innovation")
    one_gain = L.square()/eta
    need((gain-one_gain).lo >= 0, "scalar direction gain exceeds full gain")
    first_defect = 1-a["first"]
    threshold = (1-1/I.of(2).sqrt())*delta-first_defect/2
    if threshold.lo >= 0:
        non_stagnation = 2*threshold.square()/(1-delta)
    elif threshold.hi <= 0:
        non_stagnation = I.of(0)
    else:
        non_stagnation = 2*I(0,threshold.hi).square()/(1-delta)
    need((gain-non_stagnation).lo >= 0, "non-stagnation bound exceeds full gain")
    if n == 8:
        need(L.hi < 0, "N=8 negative leakage not certified")
        need((one_gain/gain).hi < I.of(F(32,1000)).lo,
             "N=8 one-dilation contribution bound not certified")
    # These are finite tests, not extrapolated rate estimates.
    return {"N": n, "delta_gain": gain.record(), "relative_gain": (gain/delta).record(),
            "gain_over_delta_squared": (gain/delta.square()).record(),
            "dilation_leakage": L.record(), "dilation_innovation_norm_squared": eta.record(),
            "one_dilation_gain": one_gain.record(),
            "non_stagnation_lower_bound": non_stagnation.record(),
            "one_dilation_fraction_of_full_gain": (one_gain/gain).record(),
            "schur_pivot_lower_min": min(p.lo for p in schur_pivots).__str__()}


def interval_controls() -> dict[str, int]:
    count = 0
    vals = [F(a,b) for a in range(-5,6) for b in (1,3,7)]
    for a in vals:
        for b in vals:
            for value, exact in [(I.of(a)+b,a+b),(I.of(a)-b,a-b),(I.of(a)*b,a*b)]:
                need(value.contains(exact), "rational interval arithmetic")
                count += 1
            if b:
                need((I.of(a)/b).contains(a/b), "rational interval division")
                count += 1
    for a in [F(0), F(1,7), F(2), F(3), F(52)]:
        root = I.of(a).sqrt()
        need(F(root.lo**2,SCALE*SCALE) <= a <= F(root.hi**2,SCALE*SCALE), "sqrt enclosure")
        count += 1
    need(bernoulli()[2] == F(1,6) and bernoulli()[32] == F(-7709321041217,510), "Bernoulli source")
    count += 1
    for a,b in [(2,2),(2,3),(3,5),(17,31)]:
        need(log_q(F(a*b)).overlaps(log_q(F(a))+log_q(F(b))), "log consistency")
        count += 1
    for x in [F(1,3),F(1,2),F(1),F(3,2),F(7,3)]:
        need((psi_q(x+1)-psi_q(x)).overlaps(I.of(1/x)), "psi recurrence")
        count += 1
    pi, root3 = pi_interval(), I.of(3).sqrt()
    closed = {(2,2):log_q(F(2))/4,
              (2,3):log_q(F(2))/6+log_q(F(3))/12-pi/(18*root3),
              (3,3):2*log_q(F(3))/9-pi/(27*root3)}
    for pair, val in closed.items():
        need(gram(*pair).overlaps(val), "closed-form Gram cross-check")
        count += 1
    prefix_count = 0
    for j in range(2,MAX_N+1):
        for k in range(j,MAX_N+1):
            partial = sum((I.of(h(j,n)*h(k,n)/F(n*(n+1))) for n in range(1,1025)), I.of(0))
            coarse = I(partial.lo, (partial+F(1,1025)).hi)
            whole = gram(j,k)
            need(coarse.lo <= whole.lo <= whole.hi <= coarse.hi, "periodic Gram/coarse prefix")
            prefix_count += 1
    return {"interval_and_function_consistency": count,
            "full_gram_vs_coarse_prefix": prefix_count}


def reconstruct() -> dict[str, object]:
    controls = exact_controls()
    controls.update(interval_controls())
    projections = {n:projection(n) for n in STAGES}
    need(projections[2]["first"].contains(1), "N=2 closed first cell")
    need(projections[3]["first"].lo > SCALE, "N=3 overshoot not certified")
    need(projections[2]["delta"].overlaps(1-log_q(F(2))), "N=2 exact distance")
    records = []
    for n, a in projections.items():
        records.append({"N": n, "delta": a["delta"].record(),
                        "g_first_cell": a["first"].record(),
                        "first_cell_defect": (1-a["first"]).record(),
                        "pivot_lower_min": str(min(p.lo for p in a["pivots"]))})
    return {"schema": "riemann-dilation-observability-v1", "config":CONFIG,
            "scientific_status":"PROPOSED_COMPONENT_PROOFS_REVIEW_REQUIRED",
            "rh_proved":False, "uniform_gain_proved":False,
            "arithmetic":"OUTWARD_DYADIC_INTEGER_INTERVALS_WITH_PROVED_ANALYTIC_REMAINDERS",
            "controls":controls, "control_total":sum(controls.values()),
            "projections":records,
            "doublings":[doubling(n,projections[n],projections[2*n]) for n in DOUBLINGS],
            "sparse_dictionary_witness":{"alphabet":[2,3],"omitted_index":5,
                                          "dual_values":{"1":2,"4":20,"5":-30},
                                          "dual_norm_squared":"52", "target_pairing":"1",
                                          "distance_squared_lower":"1/52"}}


def strict_json(path: Path) -> object:
    def pairs(entries):
        out = {}
        for k,v in entries:
            if k in out:
                raise ValueError(f"duplicate JSON key: {k}")
            out[k]=v
        return out
    def no_float(s):
        raise ValueError(f"floating/NaN JSON value forbidden: {s}")
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs,
                      parse_float=no_float, parse_constant=no_float)


def canonical(value: object) -> bytes:
    return (json.dumps(value,sort_keys=True,indent=2,ensure_ascii=True)+"\n").encode()


def check_hashes() -> None:
    sums = ROOT/"SHA256SUMS"
    if not sums.is_file():
        raise CheckFailure("missing SHA256SUMS")
    seen = set()
    for line in sums.read_text().splitlines():
        digest, name = line.split("  ",1)
        if name in seen or name.startswith("/") or ".." in Path(name).parts:
            raise CheckFailure("duplicate/unsafe checksum path")
        seen.add(name)
        p = ROOT/name
        need(p.is_file() and not p.is_symlink(), f"missing or symbolic input {name}")
        need(hashlib.sha256(p.read_bytes()).hexdigest() == digest, f"changed bytes {name}")
    actual = {str(p.relative_to(ROOT)) for p in ROOT.rglob("*")
              if p.is_file() and "__pycache__" not in p.parts and p != sums}
    need(actual == seen, "checksum manifest coverage drift")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write",action="store_true")
    group.add_argument("--check",action="store_true")
    group.add_argument("--hashes",action="store_true")
    args = parser.parse_args()
    if args.hashes:
        check_hashes()
        print("PASS_DILATION_PACKET_HASHES")
        return 0
    if args.check:
        check_hashes()
        stored = strict_json(ROOT/"verification.json")
        need(type(stored) is dict, "verification must be an object")
        need(stored.get("rh_proved") is False, "RH flag must be false")
        need(stored.get("uniform_gain_proved") is False, "uniform gain flag must be false")
        need(stored.get("schema") == "riemann-dilation-observability-v1", "wrong schema")
        need(canonical(stored.get("config")) == canonical(CONFIG), "frozen config drift")
    value = reconstruct()
    data = canonical(value)
    if args.write:
        (ROOT/"verification.json").write_bytes(data)
    else:
        need(canonical(stored) == data, "stored verification does not equal reconstructed result")
    print("PASS_DILATION_OBSERVABILITY_FINITE_REPLAY")
    print(f"controls={value['control_total']} max_N={MAX_N} RH_proved=false uniform_gain_proved=false")
    print(f"verification_sha256={hashlib.sha256(data).hexdigest()}")
    for row in value["projections"]:
        print(f"N={row['N']}: delta={row['delta']['decimal_enclosure']} g(1)={row['g_first_cell']['decimal_enclosure']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (CheckFailure,ValueError,TypeError,KeyError,ZeroDivisionError,OSError) as exc:
        print(f"REFUSED: {exc}",file=sys.stderr)
        raise SystemExit(1)
