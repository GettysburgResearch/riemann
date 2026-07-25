#!/usr/bin/env python3
"""High-precision validation kernels for L-3602.

This is ordinary mpmath arithmetic for discovery and regression, not a directed
interval implementation.
"""
from __future__ import annotations

import mpmath as mp


def legendre_values(nmax: int, x: mp.mpf) -> list[mp.mpf]:
    if nmax < 0:
        return []
    values = [mp.mpf(1)]
    if nmax == 0:
        return values
    values.append(x)
    for n in range(1, nmax):
        values.append(((2 * n + 1) * x * values[n] - n * values[n - 1]) / (n + 1))
    return values


def overlap_matrix(order: int, s: mp.mpf) -> mp.matrix:
    """Compute the normalized shifted-Legendre overlap in O(order^2)."""
    s = mp.mpf(s)
    if order < 0:
        raise ValueError("order must be nonnegative")
    if not (0 <= s <= 1):
        raise ValueError("s must lie in [0,1]")
    a = 2 * s - 1
    p = legendre_values(2 * order + 1, a)
    rows: list[list[mp.mpf]] = []
    row0 = [mp.mpf(0)] * (2 * order + 1)
    row0[0] = 1 - a
    for n in range(1, 2 * order + 1):
        row0[n] = (p[n - 1] - p[n + 1]) / (2 * n + 1)
    rows.append(row0)
    for m in range(order):
        max_n = 2 * order - m - 1
        nxt = [mp.mpf(0)] * (max_n + 1)
        for n in range(max_n + 1):
            xp = ((n + 1) * rows[m][n + 1] + (n * rows[m][n - 1] if n else 0)) / (2 * n + 1)
            shifted = xp - 2 * s * rows[m][n]
            nxt[n] = ((2 * m + 1) * shifted - (m * rows[m - 1][n] if m else 0)) / (m + 1)
        rows.append(nxt)
    out = mp.matrix(order + 1)
    for m in range(order + 1):
        for n in range(order + 1):
            scale = mp.sqrt((2 * m + 1) * (2 * n + 1)) / 2
            direct = scale * rows[m][n]
            transpose = scale * rows[n][m]
            out[m, n] = (direct + (-1) ** (m + n) * transpose) / 2
    return out


def carrier_kernel(order: int, s: mp.mpf, phase: mp.mpf) -> mp.matrix:
    """Return the real symmetric L-3602 carrier kernel."""
    overlap = overlap_matrix(order, s)
    out = mp.matrix(order + 1)
    for m in range(order + 1):
        for n in range(order + 1):
            out[m, n] = overlap[m, n] * mp.cos(phase - mp.pi * (m - n) / 2)
    return out


def basis_value(n: int, z: mp.mpf | mp.mpc, carrier: mp.mpf, delta: mp.mpf):
    """Evaluate Phi_n,T by its compact Legendre integral."""
    norm = mp.sqrt((2 * n + 1) / delta)
    return (-mp.j) ** n * mp.quad(
        lambda eta: norm * mp.legendre(n, 2 * eta / delta)
        * mp.exp(2 * mp.pi * mp.j * (z - carrier) * eta),
        [-delta / 2, delta / 2],
    )
