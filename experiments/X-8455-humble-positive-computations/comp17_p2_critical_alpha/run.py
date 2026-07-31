#!/usr/bin/env python3
"""C17 — high-precision hunt for α where windowed p_2(α)=0.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

C16 suggested the precursor is the even mode j=±2. Here we binary-search α*
with p_2(α*)=0 at several mpmath precisions, and compare α* to simple constants
(1, π/√e, e^{-1/4}, ...). Also check N-independence of α* (should be exact if
p_2 depends only on the integral, not on N).
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

from mpmath import mp, mpf, pi, exp, sqrt, log, nstr

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Fwin, Phi  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def p2(alpha):
    # p_2 = (-1)^2 Fwin = +Fwin
    return Fwin(alpha, 2, Phi)


def bisect_root(lo, hi, iters=40):
    flo, fhi = p2(lo), p2(hi)
    if flo * fhi > 0:
        return None, float(flo), float(fhi)
    for _ in range(iters):
        mid = (lo + hi) / 2
        fm = p2(mid)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2, float(p2((lo + hi) / 2)), float(hi - lo)


def main():
    print("=== C17 p2 critical alpha ===", flush=True)
    rows = []
    for dps in (25, 40, 60):
        mp.dps = dps
        root, fval, width = bisect_root(mpf("0.99"), mpf("1.005"), iters=50)
        # compare to constants
        cands = {
            "1": mpf(1),
            "pi/sqrt(e)": pi / sqrt(exp(1)),
            "e^(-1/4)": exp(mpf("-0.25")),
            "sqrt(pi/e)": sqrt(pi / exp(1)),
            "2/sqrt(e)": 2 / sqrt(exp(1)),
            "pi/e": pi / exp(1),
            "log(e+1)/1": log(exp(1) + 1),  # nonsense controls
            "0.9975": mpf("0.9975"),
        }
        diffs = {k: float(abs(root - v)) if root is not None else None for k, v in cands.items()}
        row = {
            "dps": dps,
            "alpha_star": nstr(root, 30) if root is not None else None,
            "p2_at_star": fval,
            "bracket_width": width,
            "abs_diff_to_constants": diffs,
            "nearest_constant": min(diffs, key=lambda k: diffs[k]) if root is not None else None,
        }
        rows.append(row)
        print(row, flush=True)

    # Also evaluate p_j for j=1..4 at alpha_star to see uniqueness
    mp.dps = 40
    root, _, _ = bisect_root(mpf("0.99"), mpf("1.005"), iters=60)
    profile = {str(j): nstr(((-1) ** j) * Fwin(root, j, Phi), 20) for j in range(0, 7)}
    # scan other j for roots in [0.9,1.1]
    other_roots = []
    for j in (1, 3, 4, 5, 6):
        # sample
        xs = [mpf("0.9") + mpf("0.01") * k for k in range(0, 21)]
        vals = [((-1) ** j) * Fwin(x, j, Phi) for x in xs]
        for a, b, fa, fb in zip(xs, xs[1:], vals, vals[1:]):
            if fa * fb < 0:
                other_roots.append({"j": j, "bracket": [nstr(a, 10), nstr(b, 10)]})

    payload = {
        "schema": "riemann.x8455.comp17.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Binary search on mpmath.quad; not a directed zero certificate. Constant comparisons are fishing.",
        "alpha_star_by_dps": rows,
        "coeff_profile_at_star": profile,
        "other_j_root_brackets_in_0.9_1.1": other_roots,
        "suggested_questions_for_other_agents": [
            "Is α* characterized by an exact stationary-phase / boundary-term condition on Φ?",
            "Why j=2 specifically — related to the quadratic leading factor in Φ ~ e^{9t/2} n^4 terms?",
            "Does α* equal half the reciprocal of the first positive zero of some transform of Φ?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp17.json").write_text(text)
    (OUT / "comp17.txt").write_text(json_dumps(rows, indent=2) + "\n")
    print("wrote", OUT / "comp17.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
