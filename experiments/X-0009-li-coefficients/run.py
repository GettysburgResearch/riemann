#!/usr/bin/env python3
"""
X-0009 -- Certified Li coefficients: the most compact witness format available.

Agent: claude-01
Implements/validates: T-0003.

LI'S CRITERION.  With lambda_n = sum_rho [1 - (1 - 1/rho)^n], RH is equivalent
to lambda_n >= 0 for every n >= 1.  So **a certified negative lambda_n is a
counterexample to RH, and it is a single real number.**

Nothing here needs the zeros: the lambda_n are Taylor coefficients of log xi
under z = 1 - 1/s, and xi is expanded from the certified Euler-Maclaurin Taylor
model (eta), an elementary pi-power, and log Gamma via polygamma values at 3/2.

THREE PARTS

 1. VALIDATION against the certified zeros.  The lambda_n computed from the xi
    expansion are compared with sum_rho [1-(1-1/rho)^n] over the 1517 certified
    ordinates.  The zero sum is truncated at T = 2000, so it must sit BELOW the
    exact value by the tail  ~ n^2 (log(T/2pi)+1) / (2 pi T);  checking that the
    gap has exactly that size and that exact n^2 growth is a sharp test of both
    computations.
 2. CERTIFIED VALUES with rigorous enclosures, and the sign of every one.
 3. GROWTH.  Under RH lambda_n ~ (n/2)(log n - log(2 pi) - 1 + gamma_E); a
    departure from that growth is the observable an off-critical zero would
    produce (its contribution grows like |1-1/rho|^n, i.e. EXPONENTIALLY).

Usage: python3 run.py [nmax] [tol_bits]
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
import li  # noqa: E402
from flint import arb  # noqa: E402


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    tol_bits = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    cz.set_prec(max(900, 4 * tol_bits))

    t0 = time.time()
    lam = li.li_coefficients(nmax, tol_bits=tol_bits)
    secs = round(time.time() - t0, 1)
    print(f"computed lambda_1 .. lambda_{nmax} in {secs}s")

    # ---- part 1: validation against the certified zeros -------------------
    zp = os.path.join(HERE, "..", "X-0004-lehmer-pairs", "results", "lehmer-T2000.json")
    ords = [float(z.split(" ")[0].lstrip("[")) for z in json.load(open(zp))["zeros"]]
    T = 2000.0
    checks = []
    print("  n    certified lambda_n      from zeros (T<=2000)    gap        predicted tail")
    for n in range(1, min(9, nmax + 1)):
        tot = 0.0
        for g in ords:
            for rho in (complex(0.5, g), complex(0.5, -g)):
                tot += (1 - (1 - 1 / rho) ** n).real
        v = float(lam[n - 1].real)
        tail = n * n * (math.log(T / (2 * math.pi)) + 1) / (2 * math.pi * T)
        checks.append({"n": n, "lambda": v, "from_zeros": tot,
                       "gap": v - tot, "predicted_tail": tail,
                       "ratio": (v - tot) / tail if tail else None})
        print(f"  {n:<4} {v:>20.10f}  {tot:>20.10f}  {v-tot:>10.3e}  {tail:>10.3e}")

    # ---- part 2: signs and enclosures -------------------------------------
    neg = [n for n in range(1, nmax + 1) if lam[n - 1].real < 0]
    undecided = [n for n in range(1, nmax + 1)
                 if not (lam[n - 1].real > 0) and not (lam[n - 1].real < 0)]
    print(f"\n  certified positive: {nmax - len(neg) - len(undecided)}/{nmax}"
          f"   negative: {len(neg)}   undecided: {len(undecided)}")
    if neg:
        print("  *** CERTIFIED NEGATIVE LI COEFFICIENT -- see the verification "
              "protocol before claiming anything ***")

    # ---- part 3: growth ---------------------------------------------------
    gam = float(arb.const_euler())
    rows = []
    for n in range(1, nmax + 1):
        pred = (n / 2) * (math.log(n) - math.log(2 * math.pi) - 1 + gam)
        v = float(lam[n - 1].real)
        rows.append({"n": n, "lambda": v, "rad": float(lam[n - 1].real.rad()),
                     "rh_prediction": pred,
                     "ratio": v / pred if pred else None})
    tail_rows = rows[-5:]
    print("\n  growth check (RH predicts lambda_n ~ (n/2)(log n - log 2pi - 1 + gamma)):")
    for r in tail_rows:
        print(f"    n={r['n']:<4} lambda={r['lambda']:>14.6f}  "
              f"prediction={r['rh_prediction']:>14.6f}  ratio={r['ratio']:.4f}")

    out = {"experiment": "X-0009", "agent": "claude-01", "git_sha": git_sha(),
           "python": sys.version.split()[0], "flint": __import__("flint").__version__,
           "platform": platform.platform(),
           "nmax": nmax, "tol_bits": tol_bits, "prec_bits": max(900, 4 * tol_bits),
           "seconds": secs,
           "semantics": "arb ball arithmetic throughout; the Euler-Maclaurin "
                        "remainder is propagated into the Taylor coefficients by "
                        "Cauchy on |s-1| = 1/2 (see R-0008)",
           "validation_against_zeros": checks,
           "n_certified_positive": nmax - len(neg) - len(undecided),
           "negative": neg, "undecided": undecided,
           "values": rows,
           "conclusion": ("all computed lambda_n are certified positive; "
                          "consistent with RH"
                          if not neg and not undecided else "INVESTIGATE")}
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", f"li-n{nmax}.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\n " + out["conclusion"])
    print("wrote", p)


if __name__ == "__main__":
    main()
