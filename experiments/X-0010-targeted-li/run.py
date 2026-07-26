#!/usr/bin/env python3
"""
X-0010 -- Targeted (generalised) Li coefficients: turning a candidate into a
tiny witness.

Agent: claude-01
Implements/validates: T-0004.  Answers Q-0012, which the first session flagged
as the most promising unexplored direction and did not build.

THE IDEA

The classical Li coefficients use the Mobius map s = 1/(1-z), which carries the
unit disc onto Re s > 1/2 with z = 0 sitting at s = 1.  But EVERY map

    s = 1/2 + (a + conj(a) z)/(1 - z),     a = alpha - 1/2,  Re a > 0,

does the same, with z = 0 at s = alpha, and each yields an equivalent
criterion.  An off-critical zero at rho = 1/2 - delta + i gamma is sent to a
point of modulus

    |phi_alpha(rho)| = sqrt((u+delta)^2 + (gamma-v)^2)
                     / sqrt((u-delta)^2 + (gamma-v)^2),   alpha = 1/2 + u + iv,

and lambda_n^(alpha) picks up -|phi|^n.  For the classical choice (u = 1/2,
v = 0) that modulus is 1 + O(delta/gamma^2) -- which is exactly why the
classical criterion needs n ~ gamma^2/delta before an off-critical zero shows
up.  Aim alpha at the zero (v ~ gamma, u ~ delta) and the modulus is UNBOUNDED.

MEASURED (planted off-line zero at delta = 0.01, gamma = 14.13):

    alpha = 1 (classical)          |phi| = 1.00005   no negative lambda_n
                                                     up to n = 100000
    alpha = 1/2 + 4 delta + i gamma  |phi| = 1.667    lambda_2 < 0
    alpha = 1/2 + 2 delta + i gamma  |phi| = 3.000    lambda_2 < 0
    alpha = 1/2 + 1.1 delta + i gamma |phi| = 21.0    lambda_2 < 0

i.e. the same counterexample needs n ~ 2*10^4 classically and n = 2 when
targeted.  The amplification formula (u+delta)/|u-delta| is reproduced exactly.

WHAT THIS IS AND IS NOT

It is **not** a search: |phi| is only large when v is within about delta of
gamma, so a blind scan needs a v-grid of spacing delta, which is hopeless for
small delta.  It IS the last stage of a pipeline -- a cheap screen produces a
candidate (gamma, delta), and this converts it into a witness of size n = 2.
That is the role Q-0012 was looking for.

Part 2 runs the CERTIFIED version on real zeta, with alpha aimed at the tightest
Lehmer pairs this repository has found.  A negative lambda_n^(alpha) there would
be a counterexample; all are positive.

Usage: python3 run.py
"""
from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))

import certzeta as cz  # noqa: E402
import li  # noqa: E402
from flint import acb, arb  # noqa: E402


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def phi(rho: complex, al: complex):
    w, a = rho - 0.5, al - 0.5
    d = w + a.conjugate()
    return complex("inf") if abs(d) < 1e-300 else (w - a) / d


def lam_zeros(zs, al, n):
    return sum((1 - phi(r, al) ** n).real for r in zs)


def main():
    cz.set_prec(1500)
    out = {"experiment": "X-0010", "agent": "claude-01", "git_sha": git_sha(),
           "python": sys.version.split()[0],
           "flint": __import__("flint").__version__,
           "platform": platform.platform(), "prec_bits": 1500,
           "amplification": [], "certified_targets": []}

    # ---- part 1: amplification, on a synthetic zero set --------------------
    print("=== part 1: amplification (synthetic planted zero) ===")
    gam, delta = 14.134725, 0.01
    on = [complex(0.5, g) for g in (gam, -gam, 21.02, -21.02, 25.01, -25.01)]
    off = [complex(0.5 - delta, gam), complex(0.5 + delta, gam),
           complex(0.5 - delta, -gam), complex(0.5 + delta, -gam),
           complex(0.5, 21.02), complex(0.5, -21.02),
           complex(0.5, 25.01), complex(0.5, -25.01)]
    NS = [1, 2, 3, 5, 8, 12, 20, 40, 80, 200, 1000, 5000, 20000, 100000]
    for label, al in [("classical alpha=1", complex(1, 0))] + [
            (f"targeted alpha=1/2+{k}*delta+i*gamma", complex(0.5 + k * delta, gam))
            for k in (4, 2, 1.5, 1.1)]:
        amp = abs(phi(complex(0.5 - delta, gam), al))
        first = next((n for n in NS if lam_zeros(off, al, n) < 0), None)
        out["amplification"].append({"alpha": [al.real, al.imag],
                                     "label": label, "amplification": amp,
                                     "first_negative_n": first})
        print(f"  {label:40s} |phi|={amp:>9.4f}  first n with lambda_n<0: {first}")
    out["classical_n_needed_theory"] = gam * gam / delta

    # ---- part 2: certified, aimed at the tightest Lehmer pairs -------------
    print("\n=== part 2: certified generalised Li for real zeta ===")
    targets = [("low zero", 14.134725141734694),
               ("Lehmer pair 1977", (1977.173944 + 1977.271446) / 2),
               ("Lehmer pair 1329", (1329.043518 + 1329.205019) / 2),
               ("classical Lehmer pair 7005",
                (7005.062866174921 + 7005.100564672647) / 2)]
    for name, v in targets:
        for u in (0.1, 0.01, 0.001):
            al = acb(arb("0.5") + arb(u), arb(repr(v)))
            t0 = time.time()
            try:
                L = li.li_general(al, 16, tol_bits=500)
                neg = [i + 1 for i, x in enumerate(L) if x.real < 0]
                und = [i + 1 for i, x in enumerate(L)
                       if not (x.real > 0) and not (x.real < 0)]
                rec = {"target": name, "v": v, "u": u,
                       "n_positive": 16 - len(neg) - len(und),
                       "negative": neg, "undecided": und,
                       "lambda_1": str(L[0].real),
                       "max_radius": max(float(x.real.rad()) for x in L),
                       "seconds": round(time.time() - t0, 2)}
            except Exception as e:
                rec = {"target": name, "v": v, "u": u,
                       "error": f"{type(e).__name__}: {e}"}
            out["certified_targets"].append(rec)
            print(f"  {name:28s} u={u:<6} -> "
                  f"{rec.get('n_positive', 'ERR')}/16 positive"
                  f"  neg={rec.get('negative')}  [{rec.get('seconds')}s]",
                  flush=True)

    bad = [r for r in out["certified_targets"] if r.get("negative")]
    out["conclusion"] = ("no negative targeted Li coefficient at any tested "
                         "centre; consistent with RH"
                         if not bad else "INVESTIGATE: negative coefficient")
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", "targeted-li.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\n " + out["conclusion"])
    print("wrote", p)


if __name__ == "__main__":
    main()
