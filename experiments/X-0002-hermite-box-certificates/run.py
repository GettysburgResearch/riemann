#!/usr/bin/env python3
"""
X-0002 -- Hermite-Hankel box certificates for zeta (T-0001).

Agent: claude-01

For each rectangle D symmetric about the critical line we compute, in certified
ball arithmetic:

  q_k = (1/2 pi i) INT_{dD} w(s)^k (eta'/eta)(s) ds,   w(s) = (s-1/2-ic)/(ir),

i.e. the power sums of the *normalised* zero ordinates, then form the Hankel
matrix H = (q_{i+j}) and certify its definiteness by an interval LDL^T.

  verdict PD       -> every zero in D is on the critical line  (RH holds in D)
  verdict NOT_PSD  -> a certified off-critical zero exists in D  (COUNTEREXAMPLE)
  verdict UNDECIDED-> the certificate is inconclusive at this quadrature effort

Part 1 runs on zeta.  Part 2 is a *detector validation* on synthetic
polynomials with deliberately planted off-critical zeros: a detector that never
fires proves nothing, so we check that it does fire, and we measure the
smallest displacement delta it can certify at a given quadrature effort.

Usage: python3 run.py [nsub]
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
import hermite as H  # noqa: E402
from flint import acb, arb  # noqa: E402


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def synth(roots):
    def f(s):
        p = acb(1)
        for r in roots:
            p = p * (s - r)
        return p

    def fp(s):
        tot = acb(0)
        for i, _ in enumerate(roots):
            p = acb(1)
            for j, r2 in enumerate(roots):
                if i != j:
                    p = p * (s - r2)
            tot += p
        return tot

    return f, fp


def main():
    nsub = int(sys.argv[1]) if len(sys.argv) > 1 else 32
    cz.set_prec(250)
    out = {
        "experiment": "X-0002",
        "agent": "claude-01",
        "git_sha": git_sha(),
        "python": sys.version.split()[0],
        "flint": __import__("flint").__version__,
        "platform": platform.platform(),
        "prec_bits": 250,
        "nsub": nsub,
        "semantics": "arb/acb ball arithmetic; Gauss-2 quadrature with certified "
        "Cauchy remainder; eta = (s-1)zeta via Taylor-model enclosures (L-0006)",
        "zeta_boxes": [],
        "detector_validation": [],
    }

    print("=== part 1: zeta boxes ===")
    for (x0, x1, y0, y1) in [
        ("0.2", "0.8", "12", "23"),
        ("0.2", "0.8", "23", "29"),
        ("0.2", "0.8", "12", "35"),
        ("0.25", "0.75", "36", "48"),
    ]:
        t = time.time()
        rec = {"box": [x0, x1, y0, y1]}
        try:
            r = H.box_certificate(x0, x1, y0, y1, panel_len="0.3", rad="0.1", nsub=nsub)
            rec.update(N=r["N"], verdict=r["verdict"], pivots=r["pivots"],
                       moments=r["moments"])
        except Exception as e:
            rec.update(error=f"{type(e).__name__}: {e}")
        rec["seconds"] = round(time.time() - t, 1)
        out["zeta_boxes"].append(rec)
        print(f"  [{x0},{x1}]x[{y0},{y1}]: "
              f"{rec.get('verdict', rec.get('error'))!s:.90} N={rec.get('N')} "
              f"({rec['seconds']}s)")

    print("=== part 2: detector validation on planted off-line zeros ===")
    base = ["1", "3"]
    for label, extra in [
        ("none (all on line)", []),
        ("delta=0.1", ["0.1"]),
        ("delta=0.03", ["0.03"]),
        ("delta=0.01", ["0.01"]),
        ("delta=0.003", ["0.003"]),
    ]:
        roots = [acb("0.5", t) for t in base]
        for d in extra:
            roots += [acb(arb("0.5") - arb(d), "2"), acb(arb("0.5") + arb(d), "2")]
        if not extra:
            roots += [acb("0.5", "2")]
        f, fp = synth(roots)
        t = time.time()
        rec = {"planted": label}
        try:
            r = H.box_certificate("0.1", "0.9", "0.5", "3.5", f=f, fp=fp,
                                  panel_len="0.2", rad="0.15", nsub=nsub)
            rec.update(N=r["N"], verdict=r["verdict"], pivots=r["pivots"])
        except Exception as e:
            rec.update(error=f"{type(e).__name__}: {e}")
        rec["seconds"] = round(time.time() - t, 1)
        out["detector_validation"].append(rec)
        print(f"  {label:20s} -> {rec.get('verdict', rec.get('error'))!s:.70} "
              f"({rec['seconds']}s)")

    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    path = os.path.join(HERE, "results", f"certificates-nsub{nsub}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", path)


if __name__ == "__main__":
    main()
