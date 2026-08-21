"""Shared hard-window collision helpers (discovery arithmetic).

G_alpha(s) = 2 ∫_0^{1/(2α)} Φ(t) cos(2π α s t) dt
p_j(α)     = (-1)^j G_alpha(j)
R_N(α,s)   = Σ_{j=-N}^N p_j(α)/(j-s)
"""

from __future__ import annotations

import sys
from pathlib import Path

from mpmath import mp, mpf, pi, cos, sin, quad, diff, findroot, nstr

_SHARED = Path(__file__).resolve().parent
sys.path.insert(0, str(_SHARED))
from phi_xi import Phi, Fwin  # noqa: E402


def G(alpha, s, kern=Phi):
    """Hard-window cosine transform at real frequency parameter s."""
    return Fwin(alpha, s, kern)


def G_r(alpha, s, kern=Phi):
    """∂/∂s G_alpha(s) by differentiating under the integral."""
    T = mpf(1) / (2 * mpf(alpha))
    a = mpf(alpha)
    ss = mpf(s)

    def integrand(t):
        return kern(t) * (-2 * pi * a * t) * sin(2 * pi * a * ss * t)

    return 2 * quad(integrand, [0, T])


def coeffs(alpha, N, kern=Phi):
    """p_j = (-1)^j G(alpha, j) for j=-N..N."""
    out = {}
    for j in range(-N, N + 1):
        out[j] = ((-1) ** j) * G(alpha, j, kern)
    return out


def R(p, s):
    """R(s) = Σ p_j/(j-s)."""
    s = mpf(s)
    tot = mpf(0)
    for j, pj in p.items():
        tot += pj / (mpf(j) - s)
    return tot


def R_r(p, s):
    """∂_s R(s) = Σ p_j/(j-s)^2."""
    s = mpf(s)
    tot = mpf(0)
    for j, pj in p.items():
        d = mpf(j) - s
        tot += pj / (d * d)
    return tot


def solve_continuum(alpha0, r0, dps=50, kern=Phi):
    """Solve G(α,r)=0, ∂r G(α,r)=0."""
    mp.dps = dps

    def system(a, r):
        return G(a, r, kern), G_r(a, r, kern)

    a, r = findroot(system, (mpf(alpha0), mpf(r0)))
    # residuals
    ga, gr = G(a, r, kern), G_r(a, r, kern)
    return {
        "alpha": a,
        "r": r,
        "G": ga,
        "G_r": gr,
        "alpha_str": nstr(a, dps - 5),
        "r_str": nstr(r, dps - 5),
        "G_str": nstr(ga, 10),
        "G_r_str": nstr(gr, 10),
        "dps": dps,
    }


def solve_finite(N, alpha0, r0, dps=40, kern=Phi, maxsteps=30):
    """Solve R_N(α,r)=0, ∂r R_N(α,r)=0 by 2D Newton with mpmath."""
    mp.dps = dps
    a, r = mpf(alpha0), mpf(r0)
    history = []
    for step in range(maxsteps):
        p = coeffs(a, N, kern)
        f1, f2 = R(p, r), R_r(p, r)
        history.append(
            {
                "step": step,
                "alpha": nstr(a, 20),
                "r": nstr(r, 20),
                "R": nstr(f1, 10),
                "R_r": nstr(f2, 10),
            }
        )
        if abs(f1) < mpf("1e-25") and abs(f2) < mpf("1e-25"):
            break
        # Jacobian via finite differences in α and analytic in r for R columns
        # ∂r R = R_r, ∂rr R = 2 Σ p_j/(j-r)^3
        # ∂α R, ∂α R_r by central difference
        h = mpf("1e-10") if dps < 60 else mpf("1e-14")
        p_plus = coeffs(a + h, N, kern)
        p_minus = coeffs(a - h, N, kern)
        dR_da = (R(p_plus, r) - R(p_minus, r)) / (2 * h)
        dRr_da = (R_r(p_plus, r) - R_r(p_minus, r)) / (2 * h)
        dR_dr = f2
        dRr_dr = mpf(0)
        for j, pj in p.items():
            d = mpf(j) - r
            dRr_dr += mpf(2) * pj / (d ** 3)
        # Newton step for [R, R_r](a,r)=0
        det = dR_da * dRr_dr - dR_dr * dRr_da
        if det == 0:
            break
        da = (-f1 * dRr_dr + f2 * dR_dr) / det
        dr = (-dR_da * f2 + dRr_da * f1) / det
        # damp if huge
        if abs(da) > mpf("0.05"):
            da *= mpf("0.05") / abs(da)
        if abs(dr) > mpf("0.5"):
            dr *= mpf("0.5") / abs(dr)
        a += da
        r += dr
    p = coeffs(a, N, kern)
    return {
        "N": N,
        "alpha": a,
        "r": r,
        "alpha_str": nstr(a, 25),
        "r_str": nstr(r, 25),
        "R": nstr(R(p, r), 12),
        "R_r": nstr(R_r(p, r), 12),
        "history": history,
        "dps": dps,
    }
