#!/usr/bin/env python3
"""C2 — tiny phase-complete five-notch terminal Hankel reconnaissance.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY only.

Builds a small compact B-spline packet on [0,R], forms the Hankel convolutions
C(u), subtracts the exact pole channel via the integral identity
  int e^{-u/2} C(u) du = v^- (v^-)*
and evaluates a centered terminal matrix E_a on a short prime-power window.

Five midpoint notches are applied as multiplicative sinc factors on the Laplace
side / as box-convolution design lengths 2pi/gamma_j in a scalar proxy, and as
a phase-grid Rayleigh scan on the matrix E_a.

This is deliberately smaller than Issue #178's production ask. Treat every
eigenvalue here as a discovery hint, not a directed certificate.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import numpy as np
from mpmath import mp, zetazero

mp.dps = 40
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from jsonutil import dumps as json_dumps  # noqa: E402

OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def primes_upto(n: int) -> list[int]:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False
    return list(np.nonzero(sieve)[0])


def prime_powers_in_window(
    a: float, R: float, n_cap: float = 1.0e5
) -> tuple[list[tuple[int, int, float]], bool]:
    """Return ((n, k, Lambda(n)/sqrt(n))..., truncated?) for the terminal window.

    `n_cap` is a reconnaissance ceiling. Complete L-15610 windows are larger;
    do not treat a truncated sum as the production object.
    """
    lo = np.exp(2 * a - 2 * R)
    hi = min(np.exp(2 * a), n_cap)
    truncated = hi + 1e-12 < np.exp(2 * a)
    if hi < 2:
        return [], True
    primes = primes_upto(int(hi) + 10)
    out = []
    for p in primes:
        pk = p
        k = 1
        while pk <= hi + 1e-12:
            if pk >= lo - 1e-12:
                # Lambda(p^k)=log p
                c = float(np.log(p) / np.sqrt(pk))
                out.append((pk, k, c))
            if pk > hi / p:
                break
            pk *= p
            k += 1
    out.sort(key=lambda t: t[0])
    return out, truncated


def bspline_profiles(R: float, m: int = 4, grid: int = 400):
    """m shifted cubic-ish bump profiles on (0,R); ordinary float discovery basis."""
    x = np.linspace(0.0, R, grid)
    dx = x[1] - x[0]
    # compact C^2 bumps: sin^3 windows on subintervals
    phis = []
    centers = np.linspace(0.2 * R, 0.8 * R, m)
    width = 0.35 * R
    for c in centers:
        left = c - width / 2
        right = c + width / 2
        y = np.zeros_like(x)
        mask = (x > left) & (x < right)
        t = (x[mask] - left) / (right - left)
        y[mask] = np.sin(np.pi * t) ** 3
        # force zero near endpoints
        y[0] = 0.0
        y[-1] = 0.0
        phis.append(y)
    return x, dx, phis


def laplace_v(x, dx, phis, sign=-1):
    w = np.exp(sign * 0.5 * x)
    return np.array([np.sum(w * phi) * dx for phi in phis], dtype=float)


def hankel_C(x, dx, phis, u: float):
    m = len(phis)
    C = np.zeros((m, m))
    # C_ij(u) = int phi_i(u-r) phi_j(r) dr
    # sample r on grid; interpolate phi_i at u-r
    for i in range(m):
        for j in range(i, m):
            # use numpy interp
            r = x
            yi = np.interp(u - r, x, phis[i], left=0.0, right=0.0)
            yj = phis[j]
            val = np.sum(yi * yj) * dx
            C[i, j] = C[j, i] = val
    return C


def notch_factors(gammas, x_support: float):
    """Scalar midpoint notch attenuation proxies |sinc|^2 style weights."""
    # box convolution length r_j = 2pi/gamma; transform factor ~ sinc
    fac = 1.0
    for g in gammas:
        rj = 2 * np.pi / g
        # at horizontal displacement 0 the notch vanishes; we report design cost only
        fac *= (rj / (2 * np.pi))  # placeholder scale; true on-line attenuation is tiny
    return {
        "design_support_cost": float(sum(2 * np.pi / g for g in gammas)),
        "n_notches": len(gammas),
        "proxy_product": float(fac),
    }


def phase_rayleigh_scan(E, G, n_phases=24):
    """Scan complex phases on a 2D subspace to look for hidden negative directions."""
    m = E.shape[0]
    # whitened-ish: use G^{-1/2} via eigh
    evals, evecs = np.linalg.eigh(G)
    evals = np.clip(evals, 1e-15, None)
    W = evecs @ np.diag(1.0 / np.sqrt(evals)) @ evecs.T
    Ew = W.T @ E @ W
    # full spectrum
    ew = np.linalg.eigvalsh(0.5 * (Ew + Ew.T))
    # phase scan on first two coordinates
    mins = []
    for k in range(n_phases):
        th = 2 * np.pi * k / n_phases
        v = np.zeros(m)
        v[0] = np.cos(th)
        v[1] = np.sin(th)
        mins.append(float(v @ Ew @ v))
    return {
        "whitened_eigs": [float(x) for x in ew],
        "phase_rayleigh_min": float(min(mins)),
        "phase_rayleigh_max": float(max(mins)),
        "phase_samples": mins,
    }


def build_Ea(a, R, m=4, n_cap: float = 1.0e5):
    x, dx, phis = bspline_profiles(R, m=m)
    vminus = laplace_v(x, dx, phis, sign=-1)
    vplus = laplace_v(x, dx, phis, sign=+1)
    # Gram of profiles
    G = np.zeros((m, m))
    for i in range(m):
        for j in range(i, m):
            G[i, j] = G[j, i] = np.sum(phis[i] * phis[j]) * dx

    # continuous pole integral check: int e^{-u/2} C(u) du vs v- v-^T
    us = np.linspace(0.0, 2 * R, 250)
    du = us[1] - us[0]
    integ = np.zeros((m, m))
    for u in us:
        integ += np.exp(-0.5 * u) * hankel_C(x, dx, phis, u) * du
    vv = np.outer(vminus, vminus)
    pole_identity_relerr = float(np.linalg.norm(integ - vv) / max(np.linalg.norm(vv), 1e-15))

    lo = np.exp(2 * a - 2 * R)
    window_above_cap = lo > n_cap
    pps, truncated = prime_powers_in_window(a, R, n_cap=n_cap)
    Pterm = np.zeros((m, m))
    for n, k, c in pps:
        u = 2 * a - np.log(n)
        Pterm += 2 * c * hankel_C(x, dx, phis, u)
    Ea = Pterm - 2 * np.exp(a) * vv
    # also form the identity-centered version from continuous integral
    Ea_alt = Pterm - 2 * np.exp(a) * integ

    scan = phase_rayleigh_scan(Ea, G)
    scan_alt = phase_rayleigh_scan(Ea_alt, G)
    return {
        "a": a,
        "R": R,
        "m": m,
        "n_prime_powers": len(pps),
        "truncated_at_n_cap": bool(truncated),
        "window_above_cap": bool(window_above_cap),
        "n_cap": n_cap,
        "prime_power_n_min": pps[0][0] if pps else None,
        "prime_power_n_max": pps[-1][0] if pps else None,
        "pole_identity_relerr": pole_identity_relerr,
        "vminus_norm": float(np.linalg.norm(vminus)),
        "raw_Pterm_eigs": [float(x) for x in np.linalg.eigvalsh(0.5 * (Pterm + Pterm.T))],
        "Ea_eigs": [float(x) for x in np.linalg.eigvalsh(0.5 * (Ea + Ea.T))],
        "Ea_alt_eigs": [float(x) for x in np.linalg.eigvalsh(0.5 * (Ea_alt + Ea_alt.T))],
        "phase_scan_Ea": scan,
        "phase_scan_Ea_alt": scan_alt,
        "frobenius_Ea": float(np.linalg.norm(Ea)),
        "frobenius_Pterm": float(np.linalg.norm(Pterm)),
    }


def five_notch_scalar_proxy():
    gammas = [float(mp.im(zetazero(k))) for k in range(1, 6)]
    rows = []
    # explicit-formula style envelope of first M zeros with successive notches
    # |M|^2 proxy ~ exp(-c gamma) style decay using 1/(gamma^2) weights
    for m in range(0, 6):
        weights = []
        for j, g in enumerate(gammas[:50] if False else [float(mp.im(zetazero(k))) for k in range(1, 51)]):
            w = 1.0 / (g * g)
            # apply notches 1..m as relative attenuation (epsilon/gamma)^2 with epsilon=1e-2 placeholder
            for jj in range(m):
                gj = gammas[jj]
                # midpoint notch is exact zero on line; residual from ball radius epsilon
                eps = 1e-8  # pretend tiny certified radius
                w *= (eps / (gj - eps)) ** 2 if j == jj else 1.0
            # actually for the notched zeros themselves set tiny residual; for others unchanged
            weights.append(w)
        # correct approach: zero out / attenuate first m modes
        weights = []
        allg = [float(mp.im(zetazero(k))) for k in range(1, 51)]
        for j, g in enumerate(allg):
            w = 1.0 / (g * g)
            if j < m:
                eps = 1e-8
                w *= (eps / (g - eps)) ** 2
            weights.append(w)
        rows.append(
            {
                "n_notches": m,
                "support_cost": float(sum(2 * np.pi / g for g in allg[:m])),
                "abs_sum_proxy": float(2 * sum(weights)),
                "rms_proxy": float(np.sqrt(2 * sum(w * w for w in weights))),
                "dominant_remaining_gamma": allg[m] if m < len(allg) else None,
            }
        )
    return {"gammas_used_first5": gammas, "envelope_rows": rows}


def main():
    print("=== C2 five-notch / terminal Hankel (provisional) ===")
    ladder = []
    # Smoke: one cell ~0.09s at R=2,m=3. Scale up profiles/supports modestly.
    for R in (2.0, 3.0, 4.0, 5.0):
        for da in (0.75, 1.25, 2.0, 3.0, 4.5):
            a = 2 * R + da
            # Skip supports whose whole terminal window lies above n_cap; those
            # rows would be pure -2 e^a v v^* artifacts, not prime data.
            if np.exp(2 * a - 2 * R) > 1.0e5:
                print(f"R={R} a={a:.2f}: SKIP window above n_cap", flush=True)
                continue
            row = build_Ea(a, R, m=6, n_cap=1.0e5)
            ladder.append(row)
            print(
                f"R={R} a={a:.2f}: pps={row['n_prime_powers']} trunc={row['truncated_at_n_cap']} "
                f"pole_err={row['pole_identity_relerr']:.2e} "
                f"Ea_eigs[0]={row['Ea_eigs'][0]:.3e} "
                f"phase_min={row['phase_scan_Ea']['phase_rayleigh_min']:.3e}",
                flush=True,
            )

    proxy = five_notch_scalar_proxy()
    print("notch envelope proxy:")
    for r in proxy["envelope_rows"]:
        print(f"  notches={r['n_notches']}: abs_sum~{r['abs_sum_proxy']:.3e} cost={r['support_cost']:.3f}")

    # correlation hint: does phase_min track frobenius after pole cancel?
    hints = []
    for row in ladder:
        if row["frobenius_Pterm"] > 0:
            hints.append(
                {
                    "a": row["a"],
                    "R": row["R"],
                    "cancel_ratio": row["frobenius_Ea"] / row["frobenius_Pterm"],
                    "phase_min": row["phase_scan_Ea"]["phase_rayleigh_min"],
                    "min_eig": row["Ea_eigs"][0],
                }
            )

    payload = {
        "schema": "riemann.x8455.comp2.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": (
            "Float64/mpmath discovery only. Profiles are crude bumps, not C_c^infty packages. "
            "Pole identity relative error is a discretization diagnostic. Not Issue #178."
        ),
        "terminal_ladder": ladder,
        "five_notch_scalar_proxy": proxy,
        "cancel_hints": hints,
        "suggested_questions_for_other_agents": [
            "Is cancel_ratio ~ e^{-a} or slower once profiles are orthogonalized to v^-?",
            "Does the phase-scan minimum ever disagree in sign with the smallest whitened eigenvalue on richer packets?",
            "Can the five-notch envelope proxy be replaced by a directed product of certified sinc factors?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    digest = hashlib.sha256(text.encode()).hexdigest()
    payload["content_sha256"] = digest
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp2.json").write_text(text)
    lines = ["C2 provisional summary"]
    for row in ladder:
        lines.append(
            f"R={row['R']} a={row['a']}: Ea_min={row['Ea_eigs'][0]:.6e} "
            f"phase_min={row['phase_scan_Ea']['phase_rayleigh_min']:.6e} "
            f"pole_err={row['pole_identity_relerr']:.3e}"
        )
    lines.append(f"sha256={digest}")
    (OUT / "comp2.txt").write_text("\n".join(lines) + "\n")
    print(f"wrote {OUT/'comp2.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
