#!/usr/bin/env python3
"""
X-0016 -- One positivity number, three unrelated computations: points, zeros,
primes.

Agent: claude-02
Implements: the first (demonstration) stage of Q-0018.

THE NUMBER.  Fix probes a_1..a_N with Re a_j > 1 and any direction v.  The
Pick form q = v* P v of xi'/xi is, by L-0009(iii) summed over the zeros under
the Hadamard identity (X-0013),

    q = sum_rho |Ahat_v(gamma_rho)|^2        (if RH; in general sum_rho h_v(rho)),

and because Re a_j > 1 puts the probes in the half-plane of absolute
convergence of  zeta'/zeta(s) = -sum_n Lambda(n) n^{-s},

    q = 2 Re sum_j conj(v_j) S_j G(a_j)  -  sum_n Lambda(n) W(n),

    S_j = sum_k v_k/(a_j' + conj(a_k')),
    G(s) = -log(pi)/2 + psi(s/2 + 1)/2 + 1/(s-1),
    W(n) = 2 Re sum_j conj(v_j) S_j n^{-a_j} ,

with NO use of the explicit formula and no convention risk: the identity is
just  xi'/xi = G + zeta'/zeta  termwise under the Dirichlet series.  So the
same real number is computable from

    ACCESS 1: N certified Euler-Maclaurin evaluations of xi'/xi   (T-0005),
    ACCESS 2: a prime sieve and Gamma-function values             (primes only),
    ACCESS 3: the certified zero census plus a density tail       (zeros only).

The three share no code and no mathematical input beyond zeta itself.  Their
agreement cross-validates the analytic evaluator, the census, AND the sieve
against each other in a single scalar.

WHY Re a ~ 2 AND NOT 1.05.  The raw Dirichlet tail decays like
X^{1-Re a} log X: at Re a = 1.05 reaching 1e-6 needs X ~ e^{276}; at
Re a = 2.05 it needs ~1e7.  Probes near the 1-line -- where the detection
response is strongest -- need the smoothed (explicit-formula) version, which
is the open half of Q-0018.

Usage: python3 run.py [X]
"""
from __future__ import annotations

import json
import math
import os
import platform
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))

import certzeta as cz  # noqa: E402
import pick as PK  # noqa: E402
from flint import acb, arb  # noqa: E402

HALF = arb(1) / 2


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def main():
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000_000
    cz.set_prec(600)
    al = [acb(arb("2.05"), arb(repr(99.0 + 0.4 * j))) for j in range(6)]
    v = [acb(arb("0.4"), arb("-0.9")), acb(arb("1.1"), arb("0.3")),
         acb(arb("-0.6"), arb("0.2")), acb(arb("0.8"), arb("0.7")),
         acb(arb("0.2"), arb("-0.5")), acb(arb("-0.3"), arb("1.0"))]
    N = len(al)
    ap = [a - acb(HALF) for a in al]
    S = [sum(v[k] / (ap[j] + ap[k].conjugate()) for k in range(N))
         for j in range(N)]

    # ---- access 1: certified point values ---------------------------------
    t0 = time.time()
    q1 = PK.tuned_form(al, v, tol_bits=250)
    vv = sum((z * z.conjugate()).real for z in v)
    q1 = float((q1 * vv).mid())
    t1 = round(time.time() - t0, 1)

    # ---- access 2: primes + Gamma -----------------------------------------
    t0 = time.time()
    arch = 0.0
    for j in range(N):
        Gj = (-acb(arb.pi().log()) / 2 + (al[j] / 2 + 1).polygamma(acb(0)) / 2
              + 1 / (al[j] - 1))
        arch += float((2 * (v[j].conjugate() * S[j] * Gj).real).mid())
    cj = [complex(float(v[j].conjugate().real.mid()),
                  float(v[j].conjugate().imag.mid()))
          * complex(float(S[j].real.mid()), float(S[j].imag.mid()))
          for j in range(N)]
    aj = [complex(float(a.real.mid()), float(a.imag.mid())) for a in al]
    sieve = bytearray([1]) * (X + 1)
    sieve[0] = sieve[1] = 0
    for p in range(2, int(X ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
    prime_sum = 0.0
    for p in range(2, X + 1):
        if not sieve[p]:
            continue
        lp, pk = math.log(p), p
        while pk <= X:
            lnn = math.log(pk)
            w = sum(2 * (cj[j] * complex(math.cos(-aj[j].imag * lnn),
                                         math.sin(-aj[j].imag * lnn))
                         * (pk ** (-aj[j].real))).real for j in range(N))
            prime_sum += lp * w
            pk *= p
    q2 = arch - prime_sum
    sig = min(a.real for a in aj)
    C = 2 * sum(abs(c) for c in cj)
    tail2 = C * (math.log(X) / (sig - 1) + 1 / (sig - 1) ** 2) * X ** (1 - sig)
    t2 = round(time.time() - t0, 1)

    # ---- access 3: certified zeros + density tail -------------------------
    t0 = time.time()

    def Ahat2(g):
        A = sum(v[j].conjugate() / (ap[j] - acb(0, 1) * acb(arb(repr(g))))
                for j in range(N))
        return float((A * A.conjugate()).real.mid())

    zp = os.path.join(HERE, "..", "X-0004-lehmer-pairs", "results", "zeros-T5000.json")
    ords = []
    for s in json.load(open(zp))["zeros"]:
        seg = s[s.index("[") + 1:s.index("]")]
        ords.append(float(seg.split("+/-")[0]))
    Z = sum(Ahat2(g) + Ahat2(-g) for g in ords)
    t, tl = 5000.0, 0.0
    while t < 2e7:
        step = t * 0.01
        tl += (Ahat2(t) + Ahat2(-t)) * math.log(t / (2 * math.pi)) / (2 * math.pi) * step
        t += step
    q3 = Z + tl
    t3 = round(time.time() - t0, 1)

    print(f"ACCESS 1 (xi'/xi points, certified) : {q1:.10f}  [{t1}s]")
    print(f"ACCESS 2 (primes to {X:.0e} + Gamma): {q2:.10f}  [{t2}s]  "
          f"tail bound {tail2:.1e}")
    print(f"ACCESS 3 (4520 certified zeros+tail): {q3:.10f}  [{t3}s]")
    print(f"ratios: primes/points = {q2/q1:.8f}   zeros/points = {q3/q1:.8f}")

    ok = abs(q2 - q1) < tail2 + 1e-9 and abs(q3 / q1 - 1) < 1e-4
    out = {"experiment": "X-0016", "agent": "claude-02", "git_sha": git_sha(),
           "python": sys.version.split()[0],
           "platform": platform.platform(),
           "probes_re": 2.05, "N": N, "X": X,
           "q_points": q1, "q_primes": q2, "q_zeros_plus_tail": q3,
           "prime_tail_bound": tail2,
           "ratio_primes_points": q2 / q1, "ratio_zeros_points": q3 / q1,
           "semantics": "access 1 fully certified; access 2 float prime sum "
                        "with a rigorous-form tail bound (certified "
                        "implementation is the Q-0018 handoff); access 3 "
                        "float with a density-model tail",
           "conclusion": ("one scalar, three disjoint computations, "
                          "agreement within stated bounds" if ok
                          else "INVESTIGATE: accesses disagree")}
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", "three-access.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\n " + out["conclusion"])
    print("wrote", p)


if __name__ == "__main__":
    main()
