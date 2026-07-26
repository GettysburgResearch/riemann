#!/usr/bin/env python3
"""
X-0016b -- The prime-side access, certified.

Agent: claude-02

X-0016 demonstrated the three-access agreement with a FLOAT prime sum.  This
script recomputes access 2 entirely in ball arithmetic with a certified tail,
so that the statement becomes certificate-grade:

    q_points  and  q_primes + [certified tail interval]  must overlap.

THE TAIL BOUND (proved here, used below).  For sigma > 1 and X >= 3:

    0  <=  sum_{n > X} Lambda(n) n^{-sigma}
       <=  sum_{n > X} log(n) n^{-sigma}                    (Lambda <= log)
       <=  integral_X^inf log(t) t^{-sigma} dt  +  log(X) X^{-sigma}

since t -> log(t) t^{-sigma} is decreasing for t >= e^{1/(sigma-1)} >= e (each
summand is bounded by the integral over [n-1, n] once the integrand is
decreasing, leaving at most the single term at the first n > X).  The
integral is exact:

    integral_X^inf log(t) t^{-sigma} dt
        =  X^{1-sigma} [ log(X)/(sigma-1) + 1/(sigma-1)^2 ].

The prime-side weight satisfies |W(n)| <= C n^{-sigma_min} with
C = 2 sum_j |v_j| |S_j| and sigma_min = min_j Re a_j, so the omitted tail of
the weighted sum lies in the interval [-C * TAIL, +C * TAIL] -- wait: each
W(n) has no fixed sign, so the two-sided bound is what is used.

Everything else is a finite sum of ball operations.

Usage: python3 certify.py [X]
"""
from __future__ import annotations

import json
import os
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
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
    cz.set_prec(300)
    al = [acb(arb("2.05"), arb(repr(99.0 + 0.4 * j))) for j in range(6)]
    v = [acb(arb("0.4"), arb("-0.9")), acb(arb("1.1"), arb("0.3")),
         acb(arb("-0.6"), arb("0.2")), acb(arb("0.8"), arb("0.7")),
         acb(arb("0.2"), arb("-0.5")), acb(arb("-0.3"), arb("1.0"))]
    N = len(al)
    ap = [a - acb(HALF) for a in al]
    S = [sum(v[k] / (ap[j] + ap[k].conjugate()) for k in range(N))
         for j in range(N)]
    cjS = [v[j].conjugate() * S[j] for j in range(N)]

    # access 1: certified points
    q1 = PK.tuned_form(al, v, tol_bits=250)
    vv = sum((z * z.conjugate()).real for z in v)
    q1 = (q1 * vv).real

    # access 2, certified: archimedean part
    arch = arb(0)
    for j in range(N):
        Gj = (-acb(arb.pi().log()) / 2 + (al[j] / 2 + 1).polygamma(acb(0)) / 2
              + 1 / (al[j] - 1))
        arch += 2 * (cjS[j] * Gj).real

    # prime powers by sieve (indices are exact integers; only the weights are
    # balls)
    t0 = time.time()
    sieve = bytearray([1]) * (X + 1)
    sieve[0] = sieve[1] = 0
    for p in range(2, int(X ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
    psum = arb(0)
    npp = 0
    for p in range(2, X + 1):
        if not sieve[p]:
            continue
        lp = arb(p).log()
        pk = p
        while pk <= X:
            lnn = arb(pk).log()
            w = arb(0)
            for j in range(N):
                w += 2 * (cjS[j] * (-al[j] * lnn).exp()).real
            psum += lp * w
            npp += 1
            pk *= p
    secs = round(time.time() - t0, 1)

    # certified tail interval
    sig = min((a.real for a in al), key=lambda r: float(r.mid()))
    C = 2 * sum(abs(v[j]) * abs(S[j]) for j in range(N))
    Xa = arb(X)
    integral = Xa ** (1 - sig) * (Xa.log() / (sig - 1) + 1 / (sig - 1) ** 2)
    tail_mag = (C * (integral + Xa.log() * Xa ** (-sig))).upper()
    tail = arb(0, tail_mag)          # symmetric interval [-tail_mag, +tail_mag]

    q2 = arch - psum + tail
    agree = q1.overlaps(q2)
    print(f"access 1 (points, certified):      {str(q1)[:40]}")
    print(f"access 2 (primes to {X}, certified): {str(q2)[:40]}")
    print(f"  {npp} prime powers in {secs}s; tail interval +/- {float(tail_mag):.2e}")
    print(f"  certified overlap: {agree}")

    out = {"experiment": "X-0016b", "agent": "claude-02", "git_sha": git_sha(),
           "prec_bits": 300, "X": X, "n_prime_powers": npp,
           "q_points": str(q1), "q_primes_with_tail": str(q2),
           "tail_halfwidth": float(tail_mag), "seconds_primes": secs,
           "certified_overlap": bool(agree),
           "conclusion": ("the prime-side access is now certified and "
                          "overlaps the certified point-side value; the "
                          "Q-0018 Re-a~2 case is closed"
                          if agree else "INVESTIGATE: certified values disagree")}
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    fp = os.path.join(HERE, "results", "three-access-certified.json")
    with open(fp, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\n " + out["conclusion"])
    print("wrote", fp)


if __name__ == "__main__":
    main()
