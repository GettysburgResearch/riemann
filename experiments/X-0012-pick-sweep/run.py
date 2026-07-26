#!/usr/bin/env python3
"""
X-0012 -- The Pick sweep: searching for an off-line zero without finding a
single zero.

Agent: claude-01
Implements: Z-0007, the search T-0005 makes possible.  Item 0 of CURRENT_STATE
section 6.

WHAT IS NEW HERE.  Every other search in this repository must first locate
zeros: the census scans for sign changes and bisects (X-0001), the box
criteria integrate around contours (X-0002), interval Newton needs a starting
disc (X-0007).  This one evaluates xi'/xi at 16 points per cluster, builds a
Pick matrix, and reads a sign.  Nothing is located; no contour is traversed; no
prime is summed.

MEASURED COVERAGE (synthetic, height 100, N = 16, cluster spanning [c, c+0.8]):

    delta >= 1e-3   detected for a pair anywhere in  [c-1.8, c+2.2]
    delta >= 1e-6   detected for a pair anywhere in  [c-0.8, c+2.2]
    delta >= 1e-9   detected for a pair anywhere in  [c-0.3, c+1.7]

with the matched on-line control (DOUBLE) certified PD in every cell.  So a
step of 2.0 tiles the line at the 1e-9 level, and that is the step used.

TWO PARTS

 1. THE SWEEP.  Certified Pick verdicts across a height band.  Every cluster
    must be PD; a NOT_PSD is a P1 alert and, subject to the verification
    protocol, a counterexample to RH.
 2. SENSITIVITY AT THE SWEPT HEIGHT, AGAINST THE REAL BACKGROUND.  The coverage
    numbers above were measured on a synthetic zero set at height 100.  Zeros
    are denser at height 10^4, so the sensitivity must be re-measured where the
    sweep actually runs.  Take the certified real F, add an off-line quadruple
    of depth delta at the cluster (OFF), and separately add the matched on-line
    double (DOUBLE).  OFF must fire, DOUBLE must not.

Usage: python3 run.py [t0] [t1] [step] [N]
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
import pick as PK  # noqa: E402
from flint import acb, arb  # noqa: E402

HALF = arb(1) / 2
WIDTH = 0.8


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def sweep(t0, t1, step, N, tol_bits, out):
    print(f"=== part 1: certified Pick sweep over [{t0}, {t1}], step {step} ===")
    recs, alerts = [], []
    c = t0
    while c < t1:
        al = PK.probe_cluster(c, c + WIDTH, N)
        s0 = time.time()
        try:
            r = PK.pick_certificate(al, tol_bits=tol_bits)
            r.pop("pivots")
        except Exception as e:
            r = {"verdict": f"ERROR {type(e).__name__}", "min_pivot": float("nan"),
                 "min_pivot_rad": float("nan"), "error": str(e)[:200]}
        r.update({"cluster_lo": c, "cluster_hi": c + WIDTH,
                  "seconds": round(time.time() - s0, 2)})
        recs.append(r)
        if r["verdict"] == "NOT_PSD":
            alerts.append(r)
            print(f"  *** [{c:.1f},{c+WIDTH:.1f}] NOT_PSD  min_pivot="
                  f"{r['min_pivot']:.4e} -- P1 ALERT ***", flush=True)
        elif r["verdict"] != "PD":
            print(f"  [{c:.1f},{c+WIDTH:.1f}] {r['verdict']}  "
                  f"({r.get('error','')})", flush=True)
        c += step
    npd = sum(1 for r in recs if r["verdict"] == "PD")
    tot = sum(r["seconds"] for r in recs)
    print(f"  {npd}/{len(recs)} clusters certified PD in {tot:.0f}s "
          f"({tot/max(1,len(recs)):.1f}s per cluster, "
          f"{tot/max(1e-9,(t1-t0)):.2f}s per unit height)")
    if not alerts:
        print("  no alert: no certified NOT-PSD Pick matrix in the swept band")
    out["sweep"] = {"t0": t0, "t1": t1, "step": step, "N": N,
                    "cluster_width": WIDTH, "n_clusters": len(recs),
                    "n_pd": npd, "alerts": alerts, "seconds": round(tot, 1),
                    "clusters": recs}
    return recs


def sensitivity(t0, N, tol_bits, out):
    print("\n=== part 2: sensitivity at the swept height, real background ===")
    print("  OFF must fire, the matched on-line DOUBLE must not.")
    c = arb(repr(t0 + 0.4))
    al = PK.probe_cluster(t0 + 1.0, t0 + 1.8, N)
    rows = []
    for dstr in ("0.01", "0.0001", "0.000001", "0.00000001", "0.000000001"):
        d = arb(dstr)
        off = [acb(HALF - d, c), acb(HALF + d, c),
               acb(HALF - d, -c), acb(HALF + d, -c)]
        dbl = [acb(HALF, c), acb(HALF, c), acb(HALF, -c), acb(HALF, -c)]

        def mk(extra):
            def F(s):
                s = acb(s)
                return PK.xi_logderiv(s, tol_bits=tol_bits) + sum(1 / (s - z) for z in extra)
            return F

        a = PK.pick_certificate(al, F=mk(off))
        b = PK.pick_certificate(al, F=mk(dbl))
        rows.append({"delta": dstr, "off": a["verdict"], "double": b["verdict"],
                     "off_min_pivot": a["min_pivot"], "double_min_pivot": b["min_pivot"]})
        print(f"  delta={dstr:<12} OFF={a['verdict']:<10} ({a['min_pivot']:>11.3e})   "
              f"DOUBLE={b['verdict']:<10} ({b['min_pivot']:>11.3e})", flush=True)
    det = [r["delta"] for r in rows if r["off"] == "NOT_PSD"]
    fired = [r["delta"] for r in rows if r["double"] == "NOT_PSD"]
    out["sensitivity"] = {"height": t0, "rows": rows,
                          "smallest_delta_detected": det[-1] if det else None,
                          "control_firings": len(fired)}
    print(f"  smallest delta detected at this height: {det[-1] if det else 'none'}"
          f"   (control firings: {len(fired)})")


def main():
    t0 = float(sys.argv[1]) if len(sys.argv) > 1 else 10000.0
    t1 = float(sys.argv[2]) if len(sys.argv) > 2 else 10060.0
    step = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
    N = int(sys.argv[4]) if len(sys.argv) > 4 else 16
    tol_bits = 300
    cz.set_prec(2000)

    out = {"experiment": "X-0012", "agent": "claude-01", "git_sha": git_sha(),
           "python": sys.version.split()[0], "flint": __import__("flint").__version__,
           "platform": platform.platform(), "prec_bits": 2000, "tol_bits": tol_bits,
           "criterion": "T-0005: RH <=> every Pick matrix of xi'/xi is PSD",
           "semantics": "arb/acb ball arithmetic; NOT_PSD is a proof, "
                        "UNDECIDED is an abstention",
           "note": "this band lies ABOVE the certified census (T = 5000), so no "
                   "other result in this repository covers it"}

    sweep(t0, t1, step, N, tol_bits, out)
    sensitivity(t0, N, tol_bits, out)

    alerts = out["sweep"]["alerts"]
    out["conclusion"] = (
        f"no certified NOT-PSD Pick matrix in [{t0}, {t1}]; consistent with RH"
        if not alerts else f"P1 ALERT: {len(alerts)} NOT_PSD cluster(s)")
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", f"sweep-{int(t0)}-{int(t1)}.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\n " + out["conclusion"])
    print("wrote", p)


if __name__ == "__main__":
    main()
