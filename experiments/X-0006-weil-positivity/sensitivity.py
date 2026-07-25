#!/usr/bin/env python3
"""
X-0006c -- The cost law of the Weil matched filter, measured.

Agent: claude-01

T-0002 says the filter h(r) = a^2 sinc^{2m}(a(r-gamma_0)/2) has main-lobe half
width 2 pi / a, while the prime sum runs to e^{m a + |d|}.  So narrowing the
filter -- which is what buys sensitivity, because a wide filter averages the
suspect zero together with its neighbours -- costs primes exponentially in `a`.

This experiment measures the actual trade.  At a fixed height gamma_0 = 100,
where X-0004 supplies every certified ordinate needed, we sweep the filter
width and record:

  * the number of prime powers the certified computation needs;
  * the certified verdict and min pivot of the prime-side matrix;
  * the smallest planted displacement the criterion detects, measured on the
    zero side (M-0003), which is the only honest measure of what a null result
    from this method is worth.

The reference scale is the mean zero spacing at height T,
    2 pi / log(T / 2 pi)  =  2.27  at  T = 100,
so a = log(T/2pi) = 2.77 is the filter width that just resolves individual
zeros there.

STATUS: prime-side matrices CERTIFIED; the planted-zero sweep is float
arithmetic, since it measures the criterion rather than the arithmetic.

Usage: python3 sensitivity.py
"""
from __future__ import annotations

import cmath
import json
import math
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))

import hermite as Herm  # noqa: E402
import weil  # noqa: E402
import weil_mod as wm  # noqa: E402
from flint import arb, ctx  # noqa: E402

GAMMA0 = 100.0


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def load_ordinates():
    p = os.path.join(HERE, "..", "X-0004-lehmer-pairs", "results", "lehmer-T2000.json")
    with open(p) as fh:
        return [float(z.split(" ")[0].lstrip("[")) for z in json.load(fh)["zeros"]]


def sinc(z):
    return 1.0 if abs(z) < 1e-14 else cmath.sin(z) / z


def zero_matrix(a, shifts, m, g0, zeros, di=None, delta=0.0):
    M = len(shifts)
    Q = [[0.0] * M for _ in range(M)]
    for idx, gam in enumerate(zeros):
        if di is not None and idx == di and delta > 0:
            rs = [complex(gam, -delta), complex(gam, delta),
                  complex(-gam, -delta), complex(-gam, delta)]
        else:
            rs = [complex(gam, 0.0), complex(-gam, 0.0)]
        for r in rs:
            base = (a ** 2) * sinc(a * (r - g0) / 2) ** (2 * m)
            for j in range(M):
                for k in range(M):
                    Q[j][k] += (base * cmath.exp(1j * (r - g0) *
                                                 (shifts[j] - shifts[k]))).real
    return Q


def ldl(Q):
    n = len(Q)
    A = [r[:] for r in Q]
    piv = []
    for k in range(n):
        p = A[k][k]
        piv.append(p)
        if abs(p) < 1e-300:
            break
        for i in range(k + 1, n):
            f = A[i][k] / p
            for j in range(k, n):
                A[i][j] -= f * A[k][j]
    return piv


def main():
    ctx.prec = 300
    ords = load_ordinates()
    # the zero closest to gamma0, which is the one we displace
    target = min(range(len(ords)), key=lambda i: abs(ords[i] - GAMMA0))
    spacing = 2 * math.pi / math.log(GAMMA0 / (2 * math.pi))
    print(f"height {GAMMA0}: nearest certified zero gamma = {ords[target]:.6f}, "
          f"mean spacing {spacing:.4f}, so a = {math.log(GAMMA0/(2*math.pi)):.3f} "
          f"just resolves it")

    out = {"experiment": "X-0006c", "agent": "claude-01", "git_sha": git_sha(),
           "gamma0": GAMMA0, "target_zero": ords[target],
           "mean_spacing": spacing,
           "resolving_a": math.log(GAMMA0 / (2 * math.pi)), "rows": []}

    m, M, s = 3, 10, 0.4
    shifts = [s * j for j in range(M)]
    for a in [0.5, 1.0, 1.5, 2.0, 2.77, 3.5]:
        rec = {"a": a, "filter_half_width": 2 * math.pi / a,
               "resolves_spacing": (2 * math.pi / a) <= spacing}
        supp = m * a + s * (M - 1)
        rec["support_of_g"] = supp
        rec["n_prime_powers"] = len(weil.prime_powers(round(supp + 1e-9, 9)))

        # certified prime-side matrix
        t0 = time.time()
        try:
            N = max(4000, int(130 * GAMMA0))
            Q = wm.weil_matrix_mod(a, shifts, GAMMA0, m=m, N=N, K=1)
            v, piv = Herm.ldl_signs(Q)
            rec.update(verdict=v,
                       min_pivot=min(float(x.mid()) for x in piv),
                       pivot_unc=max(float(x.rad()) for x in piv))
        except Exception as e:
            rec.update(error=f"{type(e).__name__}: {e}")
        rec["certified_seconds"] = round(time.time() - t0, 1)

        # zero-side planted sweep
        base = ldl(zero_matrix(a, shifts, m, GAMMA0, ords))
        rec["zero_side_baseline_min_pivot"] = min(base)
        floor = None
        for d in [1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001,
                  0.0005, 0.0002, 0.0001]:
            piv = ldl(zero_matrix(a, shifts, m, GAMMA0, ords, di=target, delta=d))
            if any(p < 0 for p in piv):
                floor = d
        rec["detection_floor_delta"] = floor
        out["rows"].append(rec)
        print(f"  a={a:<5} width={rec['filter_half_width']:5.2f} "
              f"({'resolves' if rec['resolves_spacing'] else 'wider than'} spacing)  "
              f"{rec['n_prime_powers']:>7} prime powers  "
              f"{rec.get('verdict','ERR'):>9}  floor delta={floor}"
              f"  [{rec['certified_seconds']}s]", flush=True)

    ok = [r for r in out["rows"] if r.get("detection_floor_delta")]
    if len(ok) >= 2:
        out["trade"] = (
            f"detection floor fell from {ok[0]['detection_floor_delta']} at "
            f"{ok[0]['n_prime_powers']} prime powers to "
            f"{ok[-1]['detection_floor_delta']} at {ok[-1]['n_prime_powers']} "
            "prime powers")
        print("\n " + out["trade"])

    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", "cost-law.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", p)


if __name__ == "__main__":
    main()
