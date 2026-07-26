#!/usr/bin/env python3
"""X-9503: independent audit of the screw branch + the zero-accounting ratio.

Three parts, all standard-library binary64 DISCOVERY code:

  A. Normalization audit of D-9501.1 against the zero-side expansion
     Psi(t) = sum_gamma (1 - cos(gamma t)) / gamma^2.
     Two independent routes:
       A1  mean/sup test   -- uses only the exact constant
                              sum_rho 1/(rho(1-rho)) = 2 + gamma_E - log(4 pi);
       A2  entrywise test  -- compares the prime-side Toeplitz symbol a_m
                              against the same symbol resummed over zeros.

  B. Evidence for L-9506: lambda_min(H^(n)(h)) is non-increasing in n and is
     capped by the exact Rayleigh value 2 Psi(nh) / n.

  C. Evidence for L-9507: the zero-accounting ratio
        rho_Gamma = lambda_max(Z_Gamma, H^(n)(h)),
     which RH forces to be <= 1 for every certified zero subset Gamma.

Nothing here is a proof.  A sign or ordering used as a certificate must be
replayed with directed arithmetic.

Usage:
    python3 experiments/screw_audit_and_ratio.py \
        --zeros experiments/results/X-9503-screw-audit-ratio/zeros1000.json \
        --json-out experiments/results/X-9503-screw-audit-ratio/audit.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from screw_lib import (Psi, integer_nth_root, jacobi_eig, rayleigh,
                       screw_toeplitz)
import screw_zeta_zeros as zz

EULER_GAMMA = 0.5772156649015328606065120900824024310422
# Unconditional:  sum_rho 1/(rho(1-rho)) = 2 + gamma_E - log(4 pi).
# Under RH this equals sum_gamma 1/(1/4 + gamma^2) <= S2 := sum_gamma 1/gamma^2.
B_EXACT = 2.0 + EULER_GAMMA - math.log(4.0 * math.pi)

H_STEP = math.log(2.0) / 3.0          # the gpt56-08 proof-replay resonance
N_FROZEN = 53


# ----------------------------------------------------------------- part A
def part_a(psi, tmax, grid):
    """Mean/sup audit of D-9501.1 against the zero-side expansion."""
    lo, hi, acc = float("inf"), -float("inf"), 0.0
    argmin = argmax = 0.0
    for i in range(1, grid + 1):
        t = tmax * i / grid
        v = psi(t)
        acc += v
        if v < lo:
            lo, argmin = v, t
        if v > hi:
            hi, argmax = v, t
    mean = acc / grid
    return {
        "tmax": tmax, "grid": grid,
        "psi_at_zero": psi(0.0),
        "min": lo, "argmin": argmin,
        "max": hi, "argmax": argmax,
        "mean": mean,
        "B_exact": B_EXACT,
        "mean_over_B": mean / B_EXACT,
        "sup_bound_2B": 2.0 * B_EXACT,
        "max_over_bound": hi / (2.0 * B_EXACT),
        "nonnegative": lo >= 0.0,
        "within_sup_bound": hi <= 2.0 * B_EXACT,
    }


def folded_smooth(t):
    """The gpt56-08 `smooth_a` variant: m=0 term folded into the exponentials.

    Algebraically identical to D-9501.1; recomputed here to check the folding.
    """
    from screw_lib import B_LIN, C_CONST
    tot = 0.0
    m = 1
    while True:
        d = 4 * m + 1
        e = d * t / 2.0
        if e > 60.0:
            break
        term = math.exp(-e) / (d * d)
        tot += term
        if term < 1e-19:
            break
        m += 1
    return (4.0 * (math.exp(t / 2.0) - 2.0)
            + B_LIN * t + C_CONST / 4.0 - 4.0 * tot)


# ----------------------------------------------------------------- part B
def part_b(psi, h, nmax, step):
    """Monotonicity of lambda_min and the exact 2 Psi(nh)/n ceiling."""
    rows = []
    prev = None
    monotone = True
    for n in range(2, nmax + 1):
        lam = min(jacobi_eig(screw_toeplitz(psi, n, h))[0])
        if prev is not None and lam > prev * (1.0 + 1e-12):
            monotone = False
        prev = lam
        if n % step == 0 or n == N_FROZEN:
            ceiling = 2.0 * psi(n * h) / n
            ones = [1.0] * n
            exact = rayleigh(screw_toeplitz(psi, n, h), ones)
            rows.append({
                "n": n, "lambda_min": lam,
                "ceiling_2psi_nh_over_n": ceiling,
                "allones_rayleigh": exact,
                "identity_rel_err": abs(exact - ceiling) / abs(ceiling),
                "n_lambda": n * lam, "n2_lambda": n * n * lam,
            })
    return {"monotone_nonincreasing": monotone,
            "nmax": nmax, "rows": rows,
            "S2_upper_bound_note": "RH => 0 <= Psi <= 2*S2, S2 = sum_gamma 1/gamma^2",
            "ceiling_constant_4B": 4.0 * B_EXACT}


# ----------------------------------------------------------------- part C
def zero_toeplitz(gammas, n, h):
    """Z_Gamma[j][k] = 8 sum_{gamma>0} sin^2(gamma h/2) cos((j-k) gamma h)/gamma^2.

    The factor 8 = 2 (the +-gamma pair) x 4 (from |1 - e^{i gamma h}|^2).
    With Gamma = every positive ordinate this reproduces the prime-side symbol.
    """
    a = [0.0] * n
    for g in gammas:
        w = 8.0 * math.sin(g * h / 2.0) ** 2 / (g * g)
        for m in range(n):
            a[m] += w * math.cos(m * g * h)
    return [[a[abs(i - j)] for j in range(n)] for i in range(n)], a


def cholesky(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = A[i][j] - sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                if s <= 0.0:
                    raise ValueError(f"matrix not positive definite at {i}")
                L[i][i] = math.sqrt(s)
            else:
                L[i][j] = s / L[j][j]
    return L


def _fsolve(L, b):
    n = len(L)
    x = [0.0] * n
    for i in range(n):
        x[i] = (b[i] - sum(L[i][k] * x[k] for k in range(i))) / L[i][i]
    return x


def pencil_max(Z, Hm):
    """lambda_max of the pencil (Z, H) by Cholesky congruence."""
    L = cholesky(Hm)
    n = len(Hm)
    Y = [_fsolve(L, [Z[r][c] for r in range(n)]) for c in range(n)]
    M = [_fsolve(L, [Y[k][c] for k in range(n)]) for c in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            v = 0.5 * (M[i][j] + M[j][i])
            M[i][j] = M[j][i] = v
    vals, vecs = jacobi_eig(M)
    imax = max(range(n), key=lambda i: vals[i])
    y = [vecs[r][imax] for r in range(n)]
    b = [0.0] * n
    for i in range(n - 1, -1, -1):
        b[i] = (y[i] - sum(L[k][i] * b[k] for k in range(i + 1, n))) / L[i][i]
    return vals[imax], b


def zero_tail_estimate(T):
    """Heuristic sum_{|gamma|>T} 1/gamma^2 from the Riemann-von Mangoldt density."""
    return 2.0 * (math.log(T / (2.0 * math.pi)) + 1.0) / (2.0 * math.pi * T)


def part_c(psi, zs, h, n):
    Hm = screw_toeplitz(psi, n, h)
    vals, vecs = jacobi_eig(Hm)
    lam_min, lam_max = min(vals), max(vals)
    vmin = [vecs[r][vals.index(lam_min)] for r in range(n)]

    _, aZ = zero_toeplitz(zs, n, h)
    aH = [Hm[0][k] for k in range(n)]
    entrywise = [{"m": m, "prime_side": aH[m], "zero_side": aZ[m],
                  "tail": aH[m] - aZ[m]} for m in range(n)]

    ratios = []
    for T in (30, 60, 100, 200, 300, 500, 700, 1000):
        G = [g for g in zs if g <= T]
        if not G:
            continue
        Z, _ = zero_toeplitz(G, n, h)
        rho, _b = pencil_max(Z, Hm)
        frac = rayleigh(Z, vmin) / rayleigh(Hm, vmin)
        ratios.append({"T": T, "zeros": len(G), "rho": rho,
                       "deficit": 1.0 - rho, "frozen_vector_fraction": frac,
                       "rh_violated": rho > 1.0})

    scale = sum(x * x for x in vmin)
    denom = rayleigh(Hm, vmin) * scale
    contrib = []
    for i, g in enumerate(zs):
        Z1, _ = zero_toeplitz([g], n, h)
        contrib.append((rayleigh(Z1, vmin) * scale, i + 1, g))
    contrib.sort(reverse=True)
    top = [{"rank": r, "index": i, "ordinate": g, "pair_contribution": c,
            "percent_of_mode": 100.0 * c / denom}
           for r, (c, i, g) in enumerate(contrib[:20], 1)]

    # L-9505 two-sided box feasibility: need 4 n S_T below the Rayleigh scale.
    box = []
    for T in (1e3, 1e4, 1e6, 1e8):
        S_T = zero_tail_estimate(T)
        box.append({"T": T, "S_T": S_T, "upper_box_4nS_T": 4.0 * n * S_T,
                    "ratio_to_lambda_min": 4.0 * n * S_T / lam_min,
                    "zeros_below_T": (T / (2 * math.pi))
                                     * (math.log(T / (2 * math.pi)) - 1.0)})
    return {
        "n": n, "h_symbolic": "log(2)/3", "h": h,
        "lambda_min": lam_min, "lambda_max": lam_max,
        "condition_number": lam_max / lam_min,
        "gpt56_08_reported_lambda_min": 1.9285536220e-05,
        "lambda_min_rel_diff": abs(lam_min - 1.9285536220e-05) / 1.9285536220e-05,
        "entrywise_symbol": entrywise,
        "max_abs_tail": max(abs(e["tail"]) for e in entrywise),
        "ratios": ratios,
        "top_contributions": top,
        "top5_percent": sum(t["percent_of_mode"] for t in top[:5]),
        "top20_percent": sum(t["percent_of_mode"] for t in top[:20]),
        "l9505_upper_box_feasibility": box,
    }


# ----------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tmax", type=float, default=14.0)
    ap.add_argument("--grid", type=int, default=400000)
    ap.add_argument("--nmax", type=int, default=60)
    ap.add_argument("--nstep", type=int, default=4)
    ap.add_argument("--zero-height", type=float, default=1000.0)
    ap.add_argument("--zeros", type=str, default=None)
    ap.add_argument("--json-out", type=str, default=None)
    args = ap.parse_args()

    src = Path(__file__).read_bytes()
    digest = hashlib.sha256(src).hexdigest()

    print("=" * 72)
    print("X-9503  independent screw-branch audit (binary64 reconnaissance)")
    print("=" * 72)

    # ---- part A ----
    print(f"\n[A] normalization audit of D-9501.1 (t up to {args.tmax})")
    psi_a = Psi(int(math.exp(args.tmax)) + 2)
    print(f"    prime powers <= {psi_a.limit}: {psi_a.n_pp}")
    a = part_a(psi_a, args.tmax, args.grid)
    print(f"    Psi(0)                     = {a['psi_at_zero']:.3e}")
    print(f"    min Psi                    = {a['min']:.12f} at t={a['argmin']:.6f}")
    print(f"    max Psi                    = {a['max']:.12f} at t={a['argmax']:.6f}")
    print(f"    mean Psi                   = {a['mean']:.12f}")
    print(f"    2+gamma-log(4pi)           = {B_EXACT:.12f}")
    print(f"    mean / that constant       = {a['mean_over_B']:.6f}   (-> 1 + O(1/tmax))")
    print(f"    max / 2x that constant     = {a['max_over_bound']:.6f}   (must be <= ~1)")
    print(f"    nonnegative on the grid    = {a['nonnegative']}")

    fold = max(abs(psi_a.smooth(t) - folded_smooth(t))
               for t in (0.5, 1.0, 2.0, 5.0, 9.0, 13.0))
    print(f"    folded-vs-unfolded smooth  = {fold:.3e}  (gpt56-08 m=0 folding)")
    a["folding_max_abs_diff"] = fold

    # ---- zeros ----
    if args.zeros and Path(args.zeros).exists():
        zs = json.load(open(args.zeros))["zeros"]
        print(f"\n    loaded {len(zs)} zero ordinates from {args.zeros}")
    else:
        print(f"\n    computing zero ordinates up to {args.zero_height} ...")
        zs = zz.find_zeros(args.zero_height)
        if args.zeros:
            Path(args.zeros).parent.mkdir(parents=True, exist_ok=True)
            json.dump({"tmax": args.zero_height, "count": len(zs),
                       "zeros": zs}, open(args.zeros, "w"))
    vm = zz.theta(args.zero_height) / math.pi + 1.0
    print(f"    zero count {len(zs)} vs N(T)=theta(T)/pi+1={vm:.4f}  "
          f"S(T)={len(zs)-vm:+.4f}")

    # ---- part B ----
    print(f"\n[B] L-9506: monotonicity and the 2 Psi(nh)/n ceiling  (h=log2/3)")
    cutoff = integer_nth_root(2 ** (args.nmax + 1), 3)
    psi_b = Psi(cutoff)
    print(f"    prime cutoff {cutoff}: primes={psi_b.n_primes} "
          f"prime powers={psi_b.n_pp}")
    b = part_b(psi_b, H_STEP, args.nmax, args.nstep)
    print(f"    lambda_min non-increasing in n over 2..{args.nmax}: "
          f"{b['monotone_nonincreasing']}")
    print(f"    {'n':>4} {'lambda_min':>15} {'2Psi(nh)/n':>14} "
          f"{'n*lam':>11} {'n^2*lam':>11} {'id.relerr':>10}")
    for r in b["rows"]:
        print(f"    {r['n']:>4} {r['lambda_min']:15.6e} "
              f"{r['ceiling_2psi_nh_over_n']:14.6e} {r['n_lambda']:11.3e} "
              f"{r['n2_lambda']:11.3e} {r['identity_rel_err']:10.1e}")

    # ---- part C ----
    print(f"\n[C] L-9507: zero-accounting ratio at n={N_FROZEN}, h=log2/3")
    c = part_c(psi_b, zs, H_STEP, N_FROZEN)
    print(f"    lambda_min = {c['lambda_min']:.10e}  "
          f"(gpt56-08 reported {c['gpt56_08_reported_lambda_min']:.10e}, "
          f"rel diff {c['lambda_min_rel_diff']:.2e})")
    print(f"    condition number = {c['condition_number']:.4e}")
    print(f"    entrywise prime-side vs zero-side symbol: "
          f"max |tail| = {c['max_abs_tail']:.3e}")
    print(f"    {'T':>7} {'#zeros':>7} {'rho_Gamma':>14} {'1-rho':>12} "
          f"{'frozen frac':>13} {'RH violated':>12}")
    for r in c["ratios"]:
        print(f"    {r['T']:>7} {r['zeros']:>7} {r['rho']:>14.9f} "
              f"{r['deficit']:>12.3e} {r['frozen_vector_fraction']:>13.6f} "
              f"{str(r['rh_violated']):>12}")
    print(f"\n    top-5 zeros account for  {c['top5_percent']:.2f}% of the frozen mode")
    print(f"    top-20 zeros account for {c['top20_percent']:.2f}% of the frozen mode")
    print(f"    {'rank':>4} {'index':>6} {'ordinate':>18} {'contribution':>14}")
    for t in c["top_contributions"][:5]:
        print(f"    {t['rank']:>4} {t['index']:>6} {t['ordinate']:>18.12f} "
              f"{t['pair_contribution']:>14.6e}")

    print(f"\n    L-9505 two-sided box feasibility (needs 4 n S_T << lambda_min):")
    print(f"    {'T':>10} {'S_T':>12} {'4 n S_T':>12} {'/lambda_min':>13} "
          f"{'zeros < T':>13}")
    for r in c["l9505_upper_box_feasibility"]:
        print(f"    {r['T']:>10.0e} {r['S_T']:>12.3e} {r['upper_box_4nS_T']:>12.3e} "
              f"{r['ratio_to_lambda_min']:>13.2e} {r['zeros_below_T']:>13.3e}")

    out = {
        "experiment": "X-9503",
        "agent": "claude-09",
        "script_sha256": digest,
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "third_party_libraries": "none (standard library only)",
            "arithmetic": "IEEE binary64",
        },
        "status": "EMPIRICAL - binary64 reconnaissance, not a certificate",
        "part_a_normalization_audit": a,
        "zero_ordinates": {"count": len(zs), "height": args.zero_height,
                           "von_mangoldt": vm, "S_T": len(zs) - vm},
        "part_b_vanishing_minimum": b,
        "part_c_zero_accounting_ratio": c,
    }
    if args.json_out:
        p = Path(args.json_out)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(out, indent=1, sort_keys=True))
        print(f"\nwrote {args.json_out}")


if __name__ == "__main__":
    main()
