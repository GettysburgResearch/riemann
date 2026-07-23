#!/usr/bin/env python3
"""Independent numerical validation of the L-2801 compact correction formulas.

This module is deliberately separate from X-0701/X-0801. It uses direct cell
integrals and mpmath only for non-rigorous validation at moderate carriers. The
proof-producing part of this contribution is verify_correction_budget.py.
"""
from __future__ import annotations

from typing import Sequence

import mpmath as mp


def cell_transform(z, left, right):
    z = mp.mpc(z)
    if z == 0:
        return right - left
    return (mp.e ** (2j * mp.pi * z * right) - mp.e ** (2j * mp.pi * z * left)) / (2j * mp.pi * z)


def W(z, vector: Sequence[complex], L):
    L = mp.mpf(L)
    delta = L / (2 * mp.pi)
    K = len(vector)
    h = delta / K
    total = 0
    for j, value in enumerate(vector):
        left = -delta / 2 + j * h
        total += mp.mpc(value) * cell_transform(z, left, left + h)
    return total


def autocorrelation_normalized(t, vector: Sequence[complex], L):
    """Return R_v(t/(4*pi))/h for t in [0,2L]."""
    L = mp.mpf(L)
    t = mp.mpf(t)
    K = len(vector)
    if t < 0 or t > 2 * L:
        return mp.mpc(0)
    r = K * t / (2 * L)
    if r >= K:
        return mp.mpc(0)
    d = int(mp.floor(r))
    f = r - d
    vv = [mp.mpc(x) for x in vector]

    def a(lag):
        if lag >= K:
            return mp.mpc(0)
        return mp.fsum(vv[j + lag] * mp.conj(vv[j]) for j in range(K - lag))

    return (1 - f) * a(d) + f * a(d + 1)


def B(t, vector: Sequence[complex], L, T):
    return mp.re(mp.e ** (-0.5j * mp.mpf(T) * t) * autocorrelation_normalized(t, vector, L))


def arch_compact_normalized(vector: Sequence[complex], L, T, *, dps=60):
    with mp.workdps(dps):
        L = mp.mpf(L)
        norm2 = mp.fsum(abs(mp.mpc(x)) ** 2 for x in vector)

        def integrand(t):
            t = mp.mpf(t)
            if t == 0:
                # The two singular parts cancel. Symmetric extrapolation is
                # validation-only; a rigorous producer must use a Taylor ball.
                eps = mp.power(10, -(mp.mp.dps // 3))
                return integrand(eps)
            return mp.e ** (-t) * norm2 / t - mp.e ** (-t / 4) / (-mp.expm1(-t)) * B(t, vector, L, T)

        # Split at every cell-overlap knot.
        knots = [2 * L * j / len(vector) for j in range(len(vector) + 1)]
        integral = mp.fsum(mp.quad(integrand, [knots[j], knots[j + 1]]) for j in range(len(vector)))
        return (integral + norm2 * mp.e1(2 * L) - norm2 * mp.log(mp.pi)) / (2 * mp.pi)


def pole_compact_normalized(vector: Sequence[complex], L, T, *, dps=60):
    with mp.workdps(dps):
        L = mp.mpf(L)
        knots = [2 * L * j / len(vector) for j in range(len(vector) + 1)]
        integral = mp.fsum(
            mp.quad(lambda t: mp.cosh(t / 4) * B(t, vector, L, T), [knots[j], knots[j + 1]])
            for j in range(len(vector))
        )
        return integral / mp.pi


def pole_finite_normalized(vector: Sequence[complex], L, T, *, dps=60):
    with mp.workdps(dps):
        L = mp.mpf(L)
        delta = L / (2 * mp.pi)
        h = delta / len(vector)
        plus = W(-mp.mpf(T) + 0.5j, vector, L)
        minus = W(-mp.mpf(T) - 0.5j, vector, L)
        return 2 * mp.re(plus * mp.conj(minus)) / h


def arch_real_line_normalized(vector: Sequence[complex], L, T, *, dps=60):
    """Slow direct real-line control, not a rigorous quadrature."""
    with mp.workdps(dps):
        L = mp.mpf(L)
        T = mp.mpf(T)
        delta = L / (2 * mp.pi)
        h = delta / len(vector)

        def density(u):
            return abs(W(u, vector, L)) ** 2 / h

        def H(r):
            return mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * r)) - mp.log(mp.pi)

        f = lambda u: H(T + u) * density(u)
        R = mp.mpf(200)
        points = [-mp.inf, -R, -20, -5, 0, 5, 20, R, mp.inf]
        return mp.quad(f, points) / (2 * mp.pi)


def arch_triangular_cancellation_safe(L, T, *, dps=60):
    """Independent K=1 cancellation-safe scalar formula from direct algebra."""
    with mp.workdps(dps):
        L = mp.mpf(L)
        T = mp.mpf(T)

        def b_l(t):
            t = mp.mpf(t)
            if t == 0:
                return mp.mpf(1) / 4 - 1 / (2 * L)
            return mp.e ** (-t / 4) / (-mp.expm1(-t)) * (1 - t / (2 * L)) - 1 / t

        def integrand(t):
            t = mp.mpf(t)
            if t == 0:
                eps = mp.power(10, -(mp.mp.dps // 3))
                return integrand(eps)
            phase = mp.cos(T * t / 2)
            return (mp.e ** (-t) - phase) / t - b_l(t) * phase

        return (mp.quad(integrand, [0, 2 * L]) + mp.e1(2 * L) - mp.log(mp.pi)) / (2 * mp.pi)
