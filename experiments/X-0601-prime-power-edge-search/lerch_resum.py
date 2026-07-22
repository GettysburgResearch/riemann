#!/usr/bin/env python3
"""Exact Lerch-transcendent resummation of X-0601 correction sums.

Numerical values returned by mpmath are not directed-rounding enclosures.
"""
from __future__ import annotations

import mpmath as mp


def sums_lerch(n: int, L: int | str | mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    """Return ``(G_S, G_CC, G_X1, G_X2)`` from the exact Lerch formulas."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    L_value = mp.mpf(L)
    if not mp.isfinite(L_value) or L_value <= 0:
        raise ValueError("L must be finite and positive")

    z = mp.exp(-2 * L_value)
    b = mp.mpf("0.25")
    prefactor = mp.exp(-L_value / 2)
    if n == 0:
        phi_1 = mp.lerchphi(z, 1, b)
        phi_2 = mp.lerchphi(z, 2, b)
        return (
            prefactor * phi_2 / 4,
            mp.mpf(0),
            prefactor * phi_1 / 2,
            prefactor * phi_2 / 4,
        )

    u = mp.pi * n / L_value
    phi_minus = mp.lerchphi(z, 1, b - 1j * u)
    phi_plus = mp.lerchphi(z, 1, b + 1j * u)
    phi2_minus = mp.lerchphi(z, 2, b - 1j * u)
    phi2_plus = mp.lerchphi(z, 2, b + 1j * u)
    phi_zero = mp.lerchphi(z, 1, b)

    g_s = prefactor * (phi_minus - phi_plus) / (8j * u)
    g_cc = prefactor / 2 * (phi_zero - (phi_minus + phi_plus) / 2)
    g_x1 = prefactor * (phi_minus + phi_plus) / 4
    g_x2 = prefactor * (phi2_minus + phi2_plus) / 8
    return tuple(mp.mpf(mp.re(value)) for value in (g_s, g_cc, g_x1, g_x2))
