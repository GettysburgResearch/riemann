#!/usr/bin/env python3
"""C20 — does α*(p2=0) already come from the n=1 term of Φ?"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

from mpmath import mp, mpf, pi, exp, cos, quad, nstr

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Phi  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 40
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def phi_trunc(t, K):
    t = abs(mpf(t))
    tot = mpf(0)
    for n in range(1, K + 1):
        en = exp(2 * t)
        tot += (4 * pi**2 * n**4 * exp(mpf("4.5") * t) - 6 * pi * n**2 * exp(mpf("2.5") * t)) * exp(
            -pi * n**2 * en
        )
    return tot


def F2(alpha, kern):
    T = mpf(1) / (2 * mpf(alpha))
    return 2 * quad(lambda t: kern(t) * cos(4 * pi * mpf(alpha) * t), [0, T])


def bisect(kern, lo=mpf("0.99"), hi=mpf("1.005"), iters=45):
    flo, fhi = F2(lo, kern), F2(hi, kern)
    if flo * fhi > 0:
        return None
    for _ in range(iters):
        mid = (lo + hi) / 2
        fm = F2(mid, kern)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def main():
    print("=== C20 alpha* vs truncation ===", flush=True)
    rows = []
    for K in [1, 2, 3, 5, 10, 20, "full"]:
        kern = Phi if K == "full" else (lambda t, K=K: phi_trunc(t, K))
        root = bisect(kern)
        rows.append({"K": K, "alpha_star": None if root is None else nstr(root, 28)})
        print(rows[-1], flush=True)
    full = mpf(rows[-1]["alpha_star"])
    for r in rows:
        if r["alpha_star"]:
            r["diff_from_full"] = float(abs(mpf(r["alpha_star"]) - full))
    payload = {
        "schema": "riemann.x8455.comp20.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Binary search on mpmath.quad of the j=2 hard-window cosine moment.",
        "rows": rows,
        "suggested_questions_for_other_agents": [
            "If K=1 already matches α* to many digits, the precursor is an archimedean/θ_1 event.",
            "Can α* be solved from an incomplete-gamma / boundary-term equation for n=1?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp20.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp20.txt").write_text("\n".join(f"{r}" for r in rows) + "\n")
    print("wrote", OUT / "comp20.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
