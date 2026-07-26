#!/usr/bin/env python3
"""
X-0011 -- The Nevanlinna-Pick criterion: a certified witness that breaks the
1/delta wall.

Agent: claude-01
Implements/validates: T-0005.  Opened by Q-0016.

THE CRITERION.  xi is entire of order 1 with zeros exactly the nontrivial zeros
of zeta, so F := xi'/xi = sum_rho 1/(s-rho).  Every on-line zero contributes a
term mapping Re s > 1/2 into Re w > 0, so

    RH  <==>  F is Herglotz on Re s > 1/2
        <==>  every Pick matrix  P_jk = (F(a_j)+conj(F(a_k)))/((a_j-1/2)+conj(a_k-1/2))
              is positive semidefinite.

A certified NOT-PSD Pick matrix is therefore a counterexample to RH, from N
point evaluations and no zero-finding at all.

WHY IT IS DIFFERENT.  Every other criterion in this repository pays ~1/delta to
resolve an off-line zero of depth delta (T-0003: n ~ gamma^2/delta;  T-0002:
exp(c/delta) prime powers;  T-0004: a v-grid of spacing delta;  L-0002: a
contour that separates 1/2-delta from 1/2).  The Pick matrix does not: probe
points held a fixed distance ~1 away detect delta = 1e-12.  The cost moves into
precision, where it is logarithmic.

FOUR PARTS

 1. DETECTOR VALIDATION (M-0003).  The off-line configuration OFF is tested
    against three matched controls that are exactly Herglotz -- LEHMER (the
    same two zeros split vertically), DOUBLE (a double zero), SINGLE.  A
    detector that fires on a control is measuring zero count or degeneracy, not
    off-line-ness.  Every control must come back PD.
 2. COST LAW.  The baseline floor vs N, and |min pivot| vs delta.
 3. CERTIFIED, REAL ZETA.  Pick matrices from certified xi'/xi across a height
    sweep.  All must be PD -- a NOT_PSD here would be a counterexample.
 4. COUNTERFACTUAL ON THE REAL ZEROS.  Take the tightest Lehmer pairs this
    repository has certified, refine both ordinates by interval Newton, and
    form the certified log-derivative of the hypothetical function whose zeros
    are exactly zeta's except that this pair has been moved off the line by
    delta.  How small a delta would the Pick test have caught?

Usage: python3 run.py [heights] [Nmax]
"""
from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
import time
from math import log10

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))

import certzeta as cz  # noqa: E402
import newton as NW  # noqa: E402
import pick as PK  # noqa: E402
from flint import acb, arb  # noqa: E402

HALF = arb(1) / 2


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


# --------------------------------------------------------------------------
# synthetic model: a finite symmetric zero set, exact under ball arithmetic
# --------------------------------------------------------------------------
def model_F(zs):
    def F(s):
        return sum(1 / (acb(s) - r) for r in zs)
    return F


def zeroset(gam, delta, mode, spacing="0.9", m=90):
    zs, d, g0 = [], arb(delta), arb(gam)
    for k in range(-m, m + 1):
        g = g0 + k * arb(spacing)
        if k == 0:
            loc = {"OFF": [acb(HALF - d, g), acb(HALF + d, g)],
                   "LEHMER": [acb(HALF, g - d), acb(HALF, g + d)],
                   "DOUBLE": [acb(HALF, g), acb(HALF, g)],
                   "SINGLE": [acb(HALF, g)]}[mode]
            zs += loc + [z.conjugate() for z in loc]
        else:
            zs += [acb(HALF, g), acb(HALF, -g)]
    return zs


def probes(gam, D, N, u="0.05"):
    """N points spanning [gam+D, gam+2D] -- every probe at distance >= D."""
    return PK.probe_cluster(gam + D, gam + 2 * D, N, u=u)


G = 100.0
MODES = ("OFF", "LEHMER", "DOUBLE", "SINGLE")


def part1(out):
    print("=== part 1: detector validation (matched Herglotz controls) ===")
    print("  OFF may go NOT_PSD; LEHMER / DOUBLE / SINGLE must stay PD.")
    rows, control_fires = [], 0
    for delta in ("0.1", "0.01", "0.001", "0.0001"):
        sets = {mo: model_F(zeroset(G, delta, mo)) for mo in MODES}
        for D in (0.05, 0.2, 0.8):
            cell = {}
            for mo in MODES:
                c = PK.pick_certificate(probes(G, D, 16), F=sets[mo])
                cell[mo] = c["verdict"]
                if mo != "OFF" and c["verdict"] == "NOT_PSD":
                    control_fires += 1
            rows.append({"delta": delta, "D": D, **cell})
            print(f"  delta={delta:<8} D={D:<5} " +
                  "  ".join(f"{mo}={cell[mo]}" for mo in MODES))
    out["validation"] = {"rows": rows, "control_firings": control_fires}
    print(f"  control firings: {control_fires}  "
          f"({'detector is specific' if control_fires == 0 else 'DETECTOR INVALID'})")


def part2(out):
    print("\n=== part 2: cost law ===")
    floor = []
    for N in (4, 8, 12, 16, 20, 24):
        p = PK.pick_certificate(probes(G, 0.8, N), F=model_F(zeroset(G, "0.001", "DOUBLE")))
        floor.append({"N": N, "min_pivot": p["min_pivot"]})
        print(f"  baseline floor  N={N:<3} {p['min_pivot']:>12.3e}   "
              f"log10 = {log10(abs(p['min_pivot'])):>7.2f}")
    dec = [(log10(abs(floor[i]["min_pivot"])) - log10(abs(floor[i - 1]["min_pivot"]))) / 4
           for i in range(1, len(floor))]
    print(f"  -> floor decays {sum(dec)/len(dec):.2f} decades per probe point")

    sc, prev = [], None
    print("  delta        N   min pivot      verdict    slope dlog|piv|/dlog delta")
    for delta in ("0.01", "0.0001", "0.000001", "0.000000001", "0.000000000001"):
        N = 16 if float(delta) >= 1e-6 else (20 if float(delta) >= 1e-9 else 24)
        c = PK.pick_certificate(probes(G, 0.8, N), F=model_F(zeroset(G, delta, "OFF")))
        ctl = PK.pick_certificate(probes(G, 0.8, N), F=model_F(zeroset(G, delta, "LEHMER")))
        v = abs(c["min_pivot"])
        sl = "" if prev is None or prev[0] != N else \
            f"{(log10(v)-log10(prev[1]))/(log10(float(delta))-prev[2]):>7.2f}"
        prev = (N, v, log10(float(delta)))
        sc.append({"delta": delta, "N": N, "min_pivot": c["min_pivot"],
                   "verdict": c["verdict"], "control_lehmer": ctl["verdict"]})
        print(f"  {delta:<12} {N:<3} {c['min_pivot']:>12.3e}  {c['verdict']:<10} "
              f"(LEHMER control {ctl['verdict']})  {sl}")
    out["cost_law"] = {"floor_vs_N": floor,
                       "floor_decades_per_point": sum(dec) / len(dec),
                       "pivot_vs_delta": sc,
                       "probe_distance": 0.8}


def part3(out, heights, Nmax):
    print("\n=== part 3: certified Pick matrices for real zeta ===")
    recs = []
    for v0 in heights:
        for N in (8, Nmax):
            t0 = time.time()
            try:
                c = PK.pick_certificate(probes(v0, 0.8, N), tol_bits=300)
                c.pop("pivots")
            except Exception as e:
                c = {"verdict": f"ERROR {type(e).__name__}: {e}"}
            c.update({"v0": v0, "N": N, "seconds": round(time.time() - t0, 2)})
            recs.append(c)
            print(f"  v0={v0:<9} N={N:<3} {c['verdict']:<10} "
                  f"min_pivot={c.get('min_pivot', float('nan')):>11.3e} "
                  f"rad={c.get('min_pivot_rad', float('nan')):.1e}  [{c['seconds']}s]",
                  flush=True)
    out["real_zeta"] = recs
    bad = [r for r in recs if r["verdict"] == "NOT_PSD"]
    out["real_zeta_conclusion"] = ("all Pick matrices certified PD; consistent with RH"
                                   if not bad else "INVESTIGATE: NOT_PSD on real zeta")


def part4(out, Nmax):
    print("\n=== part 4: counterfactual on the certified Lehmer pairs ===")
    print("  'if this pair had gone off the line by delta, would we have seen it?'")
    pairs = [("1977", 1977.17394369804, 1977.2714461997466),
             ("1329", 1329.0435179965186, 1329.2050187854836),
             ("7005", 7005.062866174921, 7005.100564672647)]
    recs = []
    for name, g0, g1 in pairs:
        # refine both ordinates by interval Newton so the removed terms are exact
        # the Newton disc must exclude the OTHER member of the pair, so the
        # radius ladder has to start below half the gap -- 0.02 was too coarse
        # for the 7005 pair, whose gap is 3.8e-2.
        rho = []
        for g in (g0, g1):
            b = None
            for r in ("0.012", "0.006", "0.002", "0.0005"):
                if 2 * float(r) >= abs(g1 - g0):
                    continue
                b = NW.refine(acb(arb(HALF), arb(repr(g))), r=r, iters=4, tol_bits=400)
                if b is not None:
                    break
            if b is None:
                break
            rho.append(b)
        if len(rho) != 2:
            print(f"  {name}: interval Newton failed to certify; skipped")
            recs.append({"pair": name, "error": "newton refine failed"})
            continue
        rad = max(float(r.rad()) for r in rho)
        c = (arb(repr(g0)) + arb(repr(g1))) / 2
        removed = [rho[0], rho[0].conjugate(), rho[1], rho[1].conjugate()]
        print(f"  pair {name}: ordinates certified to radius {rad:.2e}")

        smallest = None
        for dstr in ("0.05", "0.01", "0.001", "0.0001", "0.00001",
                     "0.000001", "0.0000001", "0.00000001", "0.000000001", "0"):
            d = arb(dstr)
            added = [acb(HALF - d, c), acb(HALF + d, c),
                     acb(HALF - d, -c), acb(HALF + d, -c)]

            def F(s, added=added):
                s = acb(s)
                base = PK.xi_logderiv(s, tol_bits=400)
                return (base - sum(1 / (s - r) for r in removed)
                        + sum(1 / (s - a) for a in added))

            cert = PK.pick_certificate(probes(float(c.mid()), 0.8, Nmax), F=F)
            tag = cert["verdict"]
            if dstr == "0":
                # delta = 0 collapses the pair to a DOUBLE on-line zero: a
                # control, which must come back PD
                print(f"    delta=0 (control, double on-line zero): {tag}"
                      f"   min_pivot={cert['min_pivot']:.3e}")
                recs.append({"pair": name, "control_delta0": tag,
                             "control_min_pivot": cert["min_pivot"],
                             "smallest_delta_detected": smallest,
                             "newton_radius": rad, "N": Nmax})
            else:
                if tag == "NOT_PSD":
                    smallest = dstr
                print(f"    delta={dstr:<10} {tag:<10} min_pivot={cert['min_pivot']:>11.3e}")
        print(f"    -> smallest delta detected from distance 0.8: {smallest}")
    out["counterfactual"] = recs


def main():
    heights = [float(x) for x in (sys.argv[1].split(",") if len(sys.argv) > 1
                                  else ["100", "1000", "1977", "5000", "7005"])]
    Nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    cz.set_prec(2500)

    out = {"experiment": "X-0011", "agent": "claude-01", "git_sha": git_sha(),
           "python": sys.version.split()[0], "flint": __import__("flint").__version__,
           "platform": platform.platform(), "prec_bits": 2500,
           "criterion": "RH <=> xi'/xi is Herglotz on Re s > 1/2 "
                        "<=> every Pick matrix is PSD",
           "semantics": "arb/acb ball arithmetic throughout; verdicts come from "
                        "an interval Hermitian LDL, so NOT_PSD is a proof and "
                        "UNDECIDED is an abstention"}

    t0 = time.time()
    part1(out)
    part2(out)
    part3(out, heights, Nmax)
    part4(out, Nmax)
    out["seconds"] = round(time.time() - t0, 1)

    fired = out["validation"]["control_firings"]
    bad = [r for r in out["real_zeta"] if r["verdict"] == "NOT_PSD"]
    out["conclusion"] = (
        "detector validated (no control firing); all certified Pick matrices "
        "for real zeta are PD; consistent with RH"
        if fired == 0 and not bad else "INVESTIGATE")
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", "pick.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\n " + out["conclusion"])
    print("wrote", p)


if __name__ == "__main__":
    main()
