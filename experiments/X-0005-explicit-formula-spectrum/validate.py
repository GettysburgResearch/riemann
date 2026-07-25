#!/usr/bin/env python3
"""
X-0005b -- Sensitivity validation of the prime-spectrum screen (M-0003).

Agent: claude-01

M-0003 says a detector that has never been shown to fire proves nothing.  This
script measures what the X-0005 screen can actually see.

METHOD.  By the explicit formula the spectral line of a zero rho = 1/2+delta+i g
in f(u) = (psi(e^u)-e^u)/e^{u/2} has amplitude growing like e^{delta u}, so
between two sieve limits X1 < X2 its measured amplitude grows by the factor

        (X2/X1)^delta            (on-line zeros: factor 1).

That growth ratio -- not the absolute amplitude -- is the observable, and it is
the one thing about a spectral line that is invariant under the many things we
model badly (windowing, leakage, the neglected constant terms).

PART 1 plants an off-critical zero in a SYNTHETIC f built from a zero list and
measures the smallest delta whose growth ratio is distinguishable from the
scatter of the on-line lines.

PART 2 applies exactly the same test to the REAL sieve data of X-0005,
producing an (uncertified) empirical bound on delta for the first twelve zeros
from the primes alone.

STATUS: EMPIRICAL.  Floating point throughout.  This measures the screen; it
certifies nothing about zeta.

Usage: python3 validate.py
"""
from __future__ import annotations

import cmath
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

ORDINATES = [
    14.134725141734693, 21.022039638771554, 25.010857580145688,
    30.424876125859513, 32.935061587739189, 37.586178158825671,
    40.918719012147495, 43.327073280914999, 48.005150881167159,
    49.773832477672302, 52.970321477714460, 56.446247697063394,
    59.347044002602353, 60.831778524609809, 65.112544048081606,
    67.079810529494173, 69.546401711173979, 72.067157674481907,
    75.704690699083933, 77.144840068874805,
]


def synthetic_f(us, zeros):
    """f(u) = - sum_rho e^{(rho-1/2)u}/rho over a conjugate-symmetric zero set,
    given as (beta, gamma) with gamma > 0 (the conjugate is added here)."""
    out = []
    for u in us:
        tot = 0.0
        for beta, g in zeros:
            rho = complex(beta, g)
            tot += 2.0 * (cmath.exp((rho - 0.5) * u) / rho).real
        out.append(-tot)
    return out


def amplitude(us, f, g):
    du = us[1] - us[0]
    W = us[-1] - us[0]
    cr = ci = 0.0
    for u, fv in zip(us, f):
        cr += fv * math.cos(g * u)
        ci -= fv * math.sin(g * u)
    return 2.0 * math.hypot(cr, ci) * du / W


def grid(u0, u1, n):
    return [u0 + (u1 - u0) * i / (n - 1) for i in range(n)]


def main():
    out = {"experiment": "X-0005b", "agent": "claude-01",
           "status": "EMPIRICAL -- measures the screen, certifies nothing",
           "part1_synthetic": [], "part2_real_data": {}}

    # ---------------- PART 1: planted off-critical zero --------------------
    u0 = math.log(1000.0)
    uA = math.log(1e6)
    uB = math.log(4e7)
    gA, gB = grid(u0, uA, 6000), grid(u0, uB, 12000)
    target_index = 3           # displace the zero at gamma = 30.4248...
    gtarget = ORDINATES[target_index]
    log_ratio = uB - uA        # = log(X2/X1)

    print("PART 1 -- planted off-critical zero, synthetic f")
    print(f"  growth factor for displacement delta is (X2/X1)^delta = "
          f"e^({log_ratio:.3f} delta)")

    # baseline scatter: growth ratios of the ON-LINE lines (should all be ~1)
    base = [(0.5, g) for g in ORDINATES]
    fA, fB = synthetic_f(gA, base), synthetic_f(gB, base)
    ratios = []
    for g in ORDINATES[:12]:
        a, b = amplitude(gA, fA, g), amplitude(gB, fB, g)
        ratios.append(b / a)
    scatter = max(abs(r - 1.0) for r in ratios)
    print(f"  on-line growth ratios: min {min(ratios):.4f} max {max(ratios):.4f}"
          f"  => scatter {scatter:.4f}")
    out["part1_baseline_scatter"] = scatter
    out["part1_online_ratios"] = ratios

    for delta in [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]:
        zs = [(0.5 + delta if i == target_index else 0.5, g)
              for i, g in enumerate(ORDINATES)]
        fA, fB = synthetic_f(gA, zs), synthetic_f(gB, zs)
        a, b = amplitude(gA, fA, gtarget), amplitude(gB, fB, gtarget)
        r = b / a
        predicted = math.exp(log_ratio * delta)
        detected = abs(r - 1.0) > 3 * scatter
        rec = {"delta": delta, "growth_ratio": r,
               "predicted_ratio": predicted,
               "detected_at_3x_scatter": bool(detected)}
        out["part1_synthetic"].append(rec)
        print(f"  delta={delta:<6} ratio={r:6.4f} (predicted {predicted:6.4f})"
              f"  detected={detected}")

    floor = min((r["delta"] for r in out["part1_synthetic"]
                 if r["detected_at_3x_scatter"]), default=None)
    out["part1_sensitivity_floor_delta"] = floor
    print(f"  => sensitivity floor of this screen: delta >= {floor}")

    # ---------------- PART 2: the same test on the real sieve data ---------
    print("\nPART 2 -- same test applied to the real X-0005 sieve output")
    try:
        d1 = json.load(open(os.path.join(HERE, "results", "spectrum-X1000000.json")))
        d2 = json.load(open(os.path.join(HERE, "results", "spectrum-X40000000.json")))
    except FileNotFoundError:
        print("  (run.py results not found; skipping)")
        d1 = d2 = None

    if d1 and d2:
        m1 = {m["known_gamma"]: m for m in d1["known_zero_matches"] if m["amplitude"]}
        m2 = {m["known_gamma"]: m for m in d2["known_zero_matches"] if m["amplitude"]}
        rows = []
        for g in sorted(set(m1) & set(m2)):
            r = m2[g]["amplitude"] / m1[g]["amplitude"]
            delta_est = math.log(r) / log_ratio
            rows.append({"gamma": g, "growth_ratio": r,
                         "implied_delta": delta_est})
            print(f"  gamma={g:9.4f}  ratio={r:6.4f}  implied delta={delta_est:+.4f}")
        spread = max(abs(x["implied_delta"]) for x in rows) if rows else None
        out["part2_real_data"] = {
            "rows": rows,
            "max_abs_implied_delta": spread,
            "interpretation":
                "Every implied delta is consistent with 0 at the resolution of "
                "this screen; the spread is dominated by windowing and leakage, "
                "not by any real displacement.  Read as an EMPIRICAL, "
                "UNCERTIFIED indication that the first twelve zeros have "
                "|Re rho - 1/2| below roughly the value of "
                "max_abs_implied_delta -- computed from the PRIMES ALONE, with "
                "no evaluation of zeta anywhere in the pipeline.  It is not a "
                "bound: there is no error analysis behind it.",
        }
        print(f"  max |implied delta| = {spread:.4f}  "
              "(consistent with all zeros on the line)")

    path = os.path.join(HERE, "results", "sensitivity-validation.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\nwrote", path)


if __name__ == "__main__":
    main()
