"""Shared certified-arithmetic helpers for the off-line zero hunt (E1/E2/E3).

All arithmetic is Arb ball arithmetic via python-flint. A "certified negative"
means the ENTIRE ball lies strictly below zero, which python-flint's `<`
operator decides (it returns True only when the comparison holds for every
point of the ball). Midpoints are reported for orientation only and are never
an acceptance input.
"""

import json
import os

from flint import acb, acb_series, arb, ctx

# ---------------------------------------------------------------- environment

DEFAULT_PREC = 220


def set_prec(prec=DEFAULT_PREC, cap=2, threads=1):
    ctx.prec = prec
    ctx.cap = cap
    ctx.threads = threads


# ------------------------------------------------------------- ball reporting


def ball(x):
    """Serialize an arb as an exact-ish interval record."""
    return {
        "mid": float(arb(x).mid()),
        "rad": float(arb(x).rad()),
        "lower": float(arb(x).lower()),
        "upper": float(arb(x).upper()),
    }


def certified_negative(x):
    """True only if every point of the ball is < 0."""
    return bool(arb(x) < 0)


def certified_positive(x):
    return bool(arb(x) > 0)


def excludes_zero(z):
    """True only if the complex ball z is certainly nonzero."""
    return bool(acb(z).abs_lower() > 0)


# ------------------------------------------------------------------ xi'/xi(s)

# xi(s) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s)
# F(s)  = xi'/xi = 1/s + 1/(s-1) - (1/2)log(pi) + (1/2)psi(s/2) + zeta'/zeta(s)
# This is the normalization fixed in
# research/integrated/xi/derivative-free-pick-loewner.md.


def xi_log_deriv(s):
    """Certified enclosure of F(s) = xi'(s)/xi(s).

    Returns (F, ok). ok is False when the zeta enclosure fails to justify the
    division, i.e. when the ball for zeta(s) contains zero. The packet rejects
    such points rather than silently repairing them.
    """
    s = acb(s)
    ser = acb_series([s, 1]).zeta()
    z0, z1 = ser[0], ser[1]
    if not excludes_zero(z0):
        return None, False
    F = 1 / s + 1 / (s - 1) - acb.pi().log() / 2 + (s / 2).digamma() / 2 + z1 / z0
    return F, True


def R_of(T, x, prec=None):
    """R_T(x) = Re F(1/2 + x + i T), with x > 0 strictly right of the line."""
    if prec is not None:
        ctx.prec = prec
    s = acb(arb(1) / 2 + x, T)
    F, ok = xi_log_deriv(s)
    if not ok:
        return None, False
    return F.real, True


# --------------------------------------------------------------- json helpers


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
    os.replace(tmp, path)
