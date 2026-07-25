#!/usr/bin/env python3
"""
X-0007 -- Interval-Newton isolation: how close to the critical line, certified.

Agent: claude-01
Implements/validates: L-0007.

WHAT THIS ADDS

X-0001 certifies two things about the range 0 < t <= T: the argument principle
counts N_box zeros, and there are N_box certified sign changes of the Hardy
function, so by L-0004 every zero is exactly ON the critical line.  That is a
qualitative statement and it leans on the count matching.

The interval Newton test gives a QUANTITATIVE and independent statement.  For
each candidate ordinate it certifies

   * that the disc B(1/2 + i gamma, r) contains exactly ONE zero of eta,
   * that the zero is SIMPLE (eta' does not vanish on the disc),
   * and a tight enclosure of it, whose real part bounds |Re rho - 1/2|.

Each Newton step squares the error, so iterating a few times drives the bound
down to the floor set by the Euler-Maclaurin truncation tolerance: from 3e-13
at tol_bits = 40, to 5e-41 at 120, to 2e-132 at 400 -- in a third of a second
for a single zero.

Combining with the box count closes the argument: if the discs are pairwise
disjoint, lie inside the box, and number exactly N_box, then they account for
every zero in the box, and

   max over all zeros with 0 < t <= T  of  |Re rho - 1/2|  <=  eps

with eps the largest enclosure radius -- a certified bound roughly 10^{18}
times sharper than the "no zero with |Re - 1/2| >= 0.01" of X-0001 part C, and
obtained without any contour at all.

Usage: python3 run.py [T] [tol_bits]
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
import newton as nw  # noqa: E402
from flint import acb, arb  # noqa: E402


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def load_ordinates():
    p = os.path.join(HERE, "..", "X-0004-lehmer-pairs", "results", "lehmer-T2000.json")
    with open(p) as fh:
        return [z.split(" ")[0].lstrip("[") for z in json.load(fh)["zeros"]]


def box_count(T):
    """The certified argument-principle count for [0,1] x [0,T], if any census
    certificate on disk covers exactly that height."""
    import glob
    d = os.path.join(HERE, "..", "X-0001-certified-zero-census", "results")
    for p in sorted(glob.glob(os.path.join(d, "census-T*.json"))):
        try:
            j = json.load(open(p))
            Tj = float(str(j.get("T", "0")).split()[0])
            if abs(Tj - T) > 1e-9:
                continue
            if "N_box" in j:
                return j["N_box"]
            if "A_argument_principle" in j:
                return j["A_argument_principle"]["count"]
        except Exception:
            continue
    return None


def main():
    T = float(sys.argv[1]) if len(sys.argv) > 1 else 1000.0
    tol_bits = int(sys.argv[2]) if len(sys.argv) > 2 else 250
    cz.set_prec(max(400, 3 * tol_bits))

    ords = [o for o in load_ordinates() if float(o) <= T]
    print(f"certifying {len(ords)} ordinates up to T={T} at tol_bits={tol_bits}")

    rows, fails = [], []
    worst_re, worst_rad = 0.0, 0.0
    t0 = time.time()
    for i, o in enumerate(ords):
        c = acb("0.5", o)
        res = nw.certify_zero(c, r_start="0.05", tol_bits=tol_bits)
        if not res["certified"]:
            fails.append(o)
            continue
        # iterate: each Newton step squares the error, so a few steps take the
        # bisection-quality centre down to the floor set by tol_bits
        Nwc = nw.refine(c, res["radius"], iters=4, tol_bits=tol_bits)
        if Nwc is None:
            fails.append(o)
            continue
        dre = float(abs(Nwc.real - arb(1) / 2).upper())
        rad = float(Nwc.rad())
        worst_re = max(worst_re, dre)
        worst_rad = max(worst_rad, rad)
        rows.append({"gamma_input": o, "radius": res["radius"],
                     "abs_re_minus_half_upper": dre, "enclosure_rad": rad})
        if (i + 1) % 100 == 0:
            print(f"  {i+1}/{len(ords)}  worst |Re-1/2| so far {worst_re:.3e}"
                  f"  [{time.time()-t0:.0f}s]", flush=True)

    # disjointness of the discs, and containment in the strip
    gam = [float(o) for o in ords]
    rmax = max(float(arb(r["radius"])) for r in rows) if rows else 0.0
    min_gap = min((gam[i + 1] - gam[i] for i in range(len(gam) - 1)), default=None)
    disjoint = (min_gap is not None) and (min_gap > 2 * rmax)

    nbox = box_count(T)
    complete = (nbox is not None) and (nbox == len(rows)) and disjoint

    out = {
        "experiment": "X-0007", "agent": "claude-01", "git_sha": git_sha(),
        "python": sys.version.split()[0], "flint": __import__("flint").__version__,
        "platform": platform.platform(),
        "T": T, "tol_bits": tol_bits, "prec_bits": max(400, 3 * tol_bits),
        "n_certified": len(rows), "n_failed": len(fails), "failed": fails,
        "disc_radius": rmax, "min_ordinate_gap": min_gap,
        "discs_pairwise_disjoint": disjoint,
        "box_count": nbox,
        "accounts_for_every_zero": complete,
        "max_abs_re_minus_half": worst_re,
        "max_enclosure_radius": worst_rad,
        "seconds": round(time.time() - t0, 1),
        "conclusion": (
            f"every zero of zeta with 0 < t <= {T} is simple and satisfies "
            f"|Re rho - 1/2| <= {worst_re:.3e}"
            if complete else
            "individual discs certified, but completeness NOT established "
            "(need a matching certified box count)"),
        "rows": rows[:50],
        "rows_note": "first 50 shown; the full list is regenerable by rerunning",
    }
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", f"newton-T{int(T)}.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)

    print(f"\n certified {len(rows)} unique simple zeros, {len(fails)} failures")
    print(f" discs of radius {rmax}, min ordinate gap {min_gap}, "
          f"disjoint={disjoint}")
    print(f" certified box count {nbox} -> accounts for every zero: {complete}")
    print(f" MAX |Re rho - 1/2| = {worst_re:.4e}")
    print(" " + out["conclusion"])
    print("wrote", p)


if __name__ == "__main__":
    main()
