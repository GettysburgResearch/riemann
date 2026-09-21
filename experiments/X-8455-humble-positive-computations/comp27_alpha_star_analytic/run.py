#!/usr/bin/env python3
"""C27 — analytic-ish probes for α*: stationary phase / boundary / n=1,2 moments.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY / fishing for a closed form

α* solves ∫_0^T Φ(t) cos(4π α t) dt = 0 with T=1/(2α).
Try:
  A) replace Φ by its n=1 leading boundary asymptotic
  B) integrate-by-parts boundary predictor
  C) match α* to roots of simple special functions involving T
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

from mpmath import mp, mpf, pi, exp, cos, sin, quad, nstr, findroot, besselj, sqrt, ei, log

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Phi  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 50
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)

ALPHA_STAR = mpf("0.997545089247478429239635033809")


def moment2(alpha, kern=Phi):
    T = mpf(1) / (2 * mpf(alpha))
    return 2 * quad(lambda t: kern(t) * cos(4 * pi * mpf(alpha) * t), [0, T])


def phi1(t):
    """n=1 term only."""
    t = abs(mpf(t))
    en = exp(2 * t)
    return (4 * pi**2 * exp(mpf("4.5") * t) - 6 * pi * exp(mpf("2.5") * t)) * exp(-pi * en)


def phi12(t):
    t = abs(mpf(t))
    tot = mpf(0)
    for n in (1, 2):
        en = exp(2 * t)
        tot += (4 * pi**2 * n**4 * exp(mpf("4.5") * t) - 6 * pi * n**2 * exp(mpf("2.5") * t)) * exp(
            -pi * n**2 * en
        )
    return tot


def bisect(kern, lo=mpf("0.99"), hi=mpf("1.01"), iters=60):
    flo, fhi = moment2(lo, kern), moment2(hi, kern)
    if flo * fhi > 0:
        # widen
        lo, hi = mpf("0.9"), mpf("1.1")
        flo, fhi = moment2(lo, kern), moment2(hi, kern)
        if flo * fhi > 0:
            return None
    for _ in range(iters):
        mid = (lo + hi) / 2
        fm = moment2(mid, kern)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def boundary_predictor():
    """Crude: after 2 integrations by parts, zeros near cos(4π α T)=0 with T=1/(2α),
    i.e. cos(2π)=1 always — so boundary alone is vacuous. Try sin(4π α T)/(4π α)=0
    doesn't help. Instead use Phi'(T) sin(...) + ... predictor by scanning residual.
    """
    # Evaluate whether F2(α) ≈ c * Phi(T) * sin(2π)/α + smoother — always 0 leading.
    # Try matching α* via Phi(T*)/Phi(0) ratios etc.
    Tstar = mpf(1) / (2 * ALPHA_STAR)
    checks = {
        "T_star": nstr(Tstar, 30),
        "Phi_T": nstr(Phi(Tstar), 20),
        "Phi_0": nstr(Phi(0), 20),
        "4pi_alpha_T": nstr(4 * pi * ALPHA_STAR * Tstar, 20),  # should be 2π
        "ratio_PhiT_Phi0": nstr(Phi(Tstar) / Phi(0), 20),
    }
    return checks


def special_function_fishing():
    a = ALPHA_STAR
    T = 1 / (2 * a)
    cands = {}
    # Bessel J0 roots
    # first positive root of J0 ~ 2.40482555739
    j0 = mpf("2.4048255576957727686216318793265")
    cands["j0/(2*pi)"] = j0 / (2 * pi)
    cands["j0/pi - 1?"] = j0 / pi  # nonsense scale
    cands["1 - 1/(2*pi*e)"] = 1 - 1 / (2 * pi * exp(1))
    cands["1 - 1/(pi*e)"] = 1 - 1 / (pi * exp(1))
    cands["1 - 1/(4*e)"] = 1 - 1 / (4 * exp(1))
    cands["1 - 1/(e^2)"] = 1 - exp(-2)
    cands["T_star*pi"] = T * pi
    cands["exp(-T_star)"] = exp(-T)
    cands["exp(-pi*exp(2*T))"] = exp(-pi * exp(2 * T))
    # distance of each candidate interpreted as alpha-like
    alpha_like = {
        "j0/(2*pi)": j0 / (2 * pi),
        "1-1/(2*pi*e)": 1 - 1 / (2 * pi * exp(1)),
        "1-1/(pi*e)": 1 - 1 / (pi * exp(1)),
        "1-1/(4*e)": 1 - 1 / (4 * exp(1)),
        "1-exp(-2)": 1 - exp(-2),
        "1-1/(8)": mpf("0.875"),
        "cos(1)": cos(1),
        "2/sqrt(e)/2": 1 / sqrt(exp(1)),  # e^{-1/2}
        "exp(-1/400)": exp(mpf("-0.0025")),
        "1-1/(pi^4)": 1 - 1 / (pi**4),
        "1-1/(4*pi^4)": 1 - 1 / (4 * pi**4),
        "1-1/(2*pi^4)": 1 - 1 / (2 * pi**4),
    }
    diffs = {k: float(abs(v - a)) for k, v in alpha_like.items()}
    return {
        "checks_at_star": cands,
        "alpha_like_diffs": diffs,
        "nearest": min(diffs, key=diffs.get),
        "nearest_diff": diffs[min(diffs, key=diffs.get)],
    }


def main():
    print("=== C27 alpha* analytic probes ===", flush=True)
    roots = {
        "full_Phi": nstr(bisect(Phi), 30),
        "phi1": nstr(bisect(phi1), 30),
        "phi12": nstr(bisect(phi12), 30),
    }
    print("roots", roots, flush=True)
    # relative errors
    rel = {k: float(abs(mpf(v) - ALPHA_STAR)) for k, v in roots.items()}
    boundary = boundary_predictor()
    fish = special_function_fishing()
    print("rel", rel, flush=True)
    print("nearest fish", fish["nearest"], fish["nearest_diff"], flush=True)

    # Try solving for alpha via findroot on moment2
    try:
        r = findroot(lambda a: moment2(a, Phi), ALPHA_STAR)
        findroot_val = nstr(r, 35)
    except Exception as exc:  # noqa: BLE001
        findroot_val = f"failed:{exc}"

    payload = {
        "schema": "riemann.x8455.comp27.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Constant fishing is not mathematics. Relative root comparisons are the serious part.",
        "alpha_star_ref": nstr(ALPHA_STAR, 30),
        "roots": roots,
        "abs_diff_to_ref": rel,
        "boundary_checks": boundary,
        "fishing": fish,
        "findroot": findroot_val,
        "suggested_questions_for_other_agents": [
            "Write the exact n=1+n=2 incomplete-gamma form of the j=2 hard-window moment.",
            "Is α* algebraic over Q(π,e), or transcendental of a new kind?",
            "Does α_def have a similar moment characterization (vanishing soft eigenvalue)?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp27.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp27.txt").write_text(json_dumps({"roots": roots, "rel": rel, "nearest": fish["nearest"]}, indent=2) + "\n")
    print("wrote", OUT / "comp27.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
