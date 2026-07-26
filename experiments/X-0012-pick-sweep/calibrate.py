#!/usr/bin/env python3
"""
X-0012b -- N-calibration at the swept height.

Agent: claude-01

X-0012 part 2 found that the sweep's sensitivity at height 1e4 is delta ~ 1e-6
at N = 16, three orders worse than the delta ~ 1e-9 measured at height 100.
T-0005 predicts the cause is the baseline floor (1.67e-28 at N = 16) rather than
precision, and therefore that the fix is MORE PROBE POINTS, since the floor
decays like 10^{-2.7N} while the signal only falls like delta^3.

That is a falsifiable prediction, and this script tests it: re-run the same
sensitivity measurement at N = 16, 20, 24 against the real certified background
and see whether the detectable delta improves by roughly three decades per four
points.  If it does not, the floor law does not transfer to real zeta at height
and the limitation in T-0005 is deeper than stated.

Usage: python3 calibrate.py [height]
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


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def main():
    t0 = float(sys.argv[1]) if len(sys.argv) > 1 else 10000.0
    tol_bits = 400
    cz.set_prec(2500)
    c = arb(repr(t0 + 0.4))

    out = {"experiment": "X-0012b", "agent": "claude-01", "git_sha": git_sha(),
           "python": sys.version.split()[0], "flint": __import__("flint").__version__,
           "platform": platform.platform(), "height": t0, "tol_bits": tol_bits,
           "prediction": "T-0005: floor ~ 10^{-2.7N}, signal ~ delta^3, so the "
                         "detectable delta should improve ~3 decades per 4 "
                         "extra probe points",
           "rows": []}

    print(f"N-calibration at height {t0}, real certified background")
    print("  OFF must fire, the matched on-line DOUBLE must not.\n")
    for N in (16, 20, 24):
        al = PK.probe_cluster(t0 + 1.0, t0 + 1.8, N)
        det, floor = None, None
        for dstr in ("0.0001", "0.000001", "0.00000001", "0.0000000001",
                     "0.000000000001"):
            d = arb(dstr)
            off = [acb(HALF - d, c), acb(HALF + d, c),
                   acb(HALF - d, -c), acb(HALF + d, -c)]
            dbl = [acb(HALF, c), acb(HALF, c), acb(HALF, -c), acb(HALF, -c)]

            def mk(extra):
                def F(s):
                    s = acb(s)
                    return (PK.xi_logderiv(s, tol_bits=tol_bits)
                            + sum(1 / (s - z) for z in extra))
                return F

            s0 = time.time()
            a = PK.pick_certificate(al, F=mk(off))
            b = PK.pick_certificate(al, F=mk(dbl))
            floor = b["min_pivot"]
            if a["verdict"] == "NOT_PSD":
                det = dstr
            out["rows"].append({"N": N, "delta": dstr, "off": a["verdict"],
                                "double": b["verdict"],
                                "off_min_pivot": a["min_pivot"],
                                "floor": b["min_pivot"]})
            print(f"  N={N:<3} delta={dstr:<15} OFF={a['verdict']:<10}"
                  f"({a['min_pivot']:>11.3e})  DOUBLE={b['verdict']:<4}"
                  f"({b['min_pivot']:>11.3e})  [{time.time()-s0:.1f}s]", flush=True)
        print(f"  -> N={N}: floor {floor:.3e}, smallest delta detected {det}\n")
        out["rows"].append({"N": N, "summary_floor": floor,
                            "smallest_delta_detected": det})

    fired = [r for r in out["rows"] if r.get("double") == "NOT_PSD"]
    out["control_firings"] = len(fired)
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", f"calibration-{int(t0)}.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"control firings: {len(fired)}")
    print("wrote", p)


if __name__ == "__main__":
    main()
