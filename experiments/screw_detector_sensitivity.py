#!/usr/bin/env python3
"""X-9507: detection thresholds of all four screw interfaces of Issue #95.

Issue #95 proposed four finite RH-disproof interfaces over one screw table:

  (a) scalar          Psi(t) >= 0
  (b) anchored Gram   S_ij = Psi(t_i)+Psi(t_j)-Psi(t_i-t_j)  is PSD   (L-9501)
  (c) conditional     sum_i c_i = 0  =>  c^T D c <= 0,  D_ij=Psi(t_i-t_j)
      negative type                                                   (L-9501)
  (d) Schoenberg      K_ij = exp(-lambda D_ij)  is PSD for all lambda>0 (L-9502)

None of them has ever been evaluated against an actual RH violation.  This
experiment builds a controlled counterfactual and measures the smallest
violation each interface can see.

COUNTERFACTUAL.  In Suzuki's variable gamma = (rho - 1/2)/i, an on-line double
zero at gamma_0 (that is, rho = 1/2 +- i gamma_0 each doubled) splits, as the
real part moves off 1/2 by delta, into the off-line quadruple

    gamma in { +-(gamma_0 - i delta),  +-(gamma_0 + i delta) }.

Replacing the on-line double pair by that quadruple changes Psi by

    Delta_delta(t) = 4 Re[ (1-cos((gamma_0+i delta) t)) / (gamma_0+i delta)^2 ]
                   - 4 (1-cos(gamma_0 t)) / gamma_0^2,

which vanishes identically at delta = 0.  Psi_delta = Psi + Delta_delta is then
a one-parameter family that equals the true screw function at delta = 0 and
encodes an off-critical zero for delta > 0.  This is the standard local model
of a zero leaving the line; it presupposes a double zero, which is itself
unproved, and it is used here only as a common yardstick against which the four
detectors can be compared on equal terms.

Standard library only; IEEE binary64; DISCOVERY code, not a certificate.

Usage:
    python3 experiments/screw_detector_sensitivity.py \
        --json-out experiments/results/X-9507-detector-sensitivity/sensitivity.json
"""
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
import platform
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from screw_lib import Psi, jacobi_eig

GAMMA_1 = 14.134725141734693


def make_psi_delta(psi, g0, delta):
    """Psi with one on-line double zero pair at g0 moved off the line by delta."""
    gc = complex(g0, delta)
    gc2 = gc * gc

    def f(t):
        base = psi(t)
        off = 4.0 * ((1.0 - cmath.cos(gc * t)) / gc2).real
        on = 4.0 * (1.0 - math.cos(g0 * t)) / (g0 * g0)
        return base + off - on
    return f


def zero_sum_basis(m):
    return [[(1.0 if i == k else (-1.0 if i == k + 1 else 0.0))
             for k in range(m - 1)] for i in range(m)]


def congruence(U, M):
    m, r = len(U), len(U[0])
    MU = [[sum(M[i][k] * U[k][j] for k in range(m)) for j in range(r)]
          for i in range(m)]
    return [[sum(U[k][i] * MU[k][j] for k in range(m)) for j in range(r)]
            for i in range(r)]


# ---------------------------------------------------------------- detectors
def det_scalar(pd, span, grid=4000):
    """min_t Psi_delta(t) over (0, span]; fires when negative."""
    return min(pd(span * i / grid) for i in range(1, grid + 1))


def det_gram(pd, t):
    """lambda_min of the anchored screw matrix S (L-9501 interface 2)."""
    m = len(t)
    S = [[pd(t[i]) + pd(t[j]) - pd(t[i] - t[j]) for j in range(m)]
         for i in range(m)]
    return min(jacobi_eig(S)[0])


def det_cnt(pd, t):
    """lambda_min of -D restricted to the zero-sum cone (L-9501 interface 3)."""
    m = len(t)
    A = [[-pd(t[i] - t[j]) for j in range(m)] for i in range(m)]
    return min(jacobi_eig(congruence(zero_sum_basis(m), A))[0])


def det_gauss(pd, t, scales):
    """min over lambda of lambda_min(exp(-lambda D))  (L-9502 interface 4).

    lambda is swept as a fraction of 1/M with M = max|D_ij|, which is exactly
    the range L-9502.3's transfer moat is stated for (`lambda M <= 1`), and
    which also keeps exp(-lambda D) in binary64 range once Psi_delta goes
    negative.
    """
    m = len(t)
    D = [[pd(t[i] - t[j]) for j in range(m)] for i in range(m)]
    M = max(abs(D[i][j]) for i in range(m) for j in range(m))
    if M == 0.0:
        return 0.0, None
    best, arg = float("inf"), None
    for s in scales:
        lam = s / M
        K = [[math.exp(-lam * D[i][j]) for j in range(m)] for i in range(m)]
        v = min(jacobi_eig(K)[0])
        if v < best:
            best, arg = v, lam
    return best, arg


def threshold(fn, lo=0.0, hi=1.0, iters=40):
    """Smallest delta in [lo,hi] at which fn(delta) < 0, or None."""
    if fn(hi) >= 0.0:
        return None
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if fn(mid) < 0.0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m", type=int, default=16)
    ap.add_argument("--span", type=float, default=12.0)
    ap.add_argument("--g0", type=float, default=GAMMA_1)
    ap.add_argument("--json-out", default=None)
    args = ap.parse_args()

    digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    psi = Psi(int(math.exp(args.span + 0.5)) + 2)
    m, span = args.m, args.span
    h = span / (m - 1)
    t = [j * h for j in range(m)]
    # lambda = s/M with s in (0,1], per L-9502.3's `lambda M <= 1`
    lambdas = [10 ** (-3.0 + 3.0 * k / 24) for k in range(25)]
    print(f"nodes m={m}, h={h:.5f}, span={span}, perturbed zero "
          f"gamma_0={args.g0:.9f}")
    print(f"prime powers <= {psi.limit}: {psi.n_pp}\n")

    # sanity: delta = 0 must reproduce the unperturbed screw function
    p0 = make_psi_delta(psi, args.g0, 0.0)
    err = max(abs(p0(span * i / 50) - psi(span * i / 50)) for i in range(1, 51))
    print(f"[check] |Psi_0 - Psi| max over grid = {err:.3e}   (must be 0)")
    base = {"scalar": det_scalar(p0, span), "gram": det_gram(p0, t),
            "cnt": det_cnt(p0, t), "gauss": det_gauss(p0, t, lambdas)[0]}
    print(f"[check] unperturbed margins (all must be >= 0):")
    for k, v in base.items():
        print(f"          {k:<8} {v:+.6e}")

    print(f"\ndetection thresholds in delta = Re(rho) - 1/2:")
    print(f"{'interface':<34} {'delta*':>12} {'Re(rho)':>10}")
    res = {}
    for name, fn in (
            ("(a) scalar  Psi(t) < 0",
             lambda d: det_scalar(make_psi_delta(psi, args.g0, d), span)),
            ("(b) anchored Gram  lam_min(S)<0",
             lambda d: det_gram(make_psi_delta(psi, args.g0, d), t)),
            ("(c) conditional negative type",
             lambda d: det_cnt(make_psi_delta(psi, args.g0, d), t)),
            ("(d) Schoenberg-Gaussian",
             lambda d: det_gauss(make_psi_delta(psi, args.g0, d), t,
                                 lambdas)[0])):
        th = threshold(fn)
        res[name] = th
        if th is None:
            print(f"{name:<34} {'none <=1':>12} {'-':>10}")
        else:
            print(f"{name:<34} {th:>12.6f} {0.5+th:>10.6f}")

    # Schoenberg equivalence check: (c) and (d) must fire together
    print(f"\n[Schoenberg] (c) and (d) are equivalent predicates:")
    print(f"  D conditionally negative definite  <=>  exp(-lambda D) PSD "
          f"for all lambda > 0")
    print(f"{'delta':>10} {'lam_min CNT':>15} {'min_lam lam_min(K)':>20} "
          f"{'argmin lambda':>14} {'agree':>7}")
    rows = []
    tc = res["(c) conditional negative type"]
    if tc is not None:
        for d in (tc * 0.9, tc * 0.99, tc * 1.01, tc * 1.1, tc * 1.5):
            pd = make_psi_delta(psi, args.g0, d)
            c = det_cnt(pd, t)
            g, lam = det_gauss(pd, t, lambdas)
            agree = (c < 0) == (g < 0)
            rows.append({"delta": d, "cnt": c, "gauss": g, "lambda": lam,
                         "agree": agree})
            print(f"{d:>10.6f} {c:>15.3e} {g:>20.3e} {lam:>14.4g} "
                  f"{str(agree):>7}")

    out = {"experiment": "X-9507", "agent": "claude-09",
           "script_sha256": digest,
           "environment": {"python": platform.python_version(),
                           "platform": platform.platform(),
                           "third_party_libraries": "none (standard library only)",
                           "arithmetic": "IEEE binary64"},
           "status": "EMPIRICAL - binary64 reconnaissance, not a certificate",
           "m": m, "h": h, "span": span, "gamma_0": args.g0,
           "delta0_reproduction_error": err,
           "unperturbed_margins": base,
           "thresholds": res, "schoenberg_rows": rows}
    if args.json_out:
        p = Path(args.json_out)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(out, indent=1, sort_keys=True))
        print(f"\nwrote {args.json_out}")


if __name__ == "__main__":
    main()
