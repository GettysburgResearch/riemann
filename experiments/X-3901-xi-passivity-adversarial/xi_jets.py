#!/usr/bin/env python3
"""Ordinary high-precision Riemann--Siegel xi-jet reconnaissance.

STATUS: discovery arithmetic only. mpmath values are not directed balls.
"""
from __future__ import annotations

import math
import mpmath as mp
from mpmath.functions.rszeta import Rzeta_simul


def simultaneous_zeta_jet(s: mp.mpc, order: int = 2) -> list[mp.mpc]:
    """Assemble zeta derivatives through order 0, 1, 2, or 4 in one RS call."""
    if order not in (0, 1, 2, 4):
        raise ValueError("implemented orders are 0, 1, 2, and 4")
    ctx = mp.mp
    x, y = Rzeta_simul(ctx, s, order)
    sigma = ctx.re(s)
    t = ctx.im(s)
    theta = ctx.siegeltheta(t - ctx.j * (sigma - ctx.mpf("0.5")))
    p1 = (ctx.psi(0, s / 2) + ctx.psi(0, (1 - s) / 2)) / 4 - ctx.log(ctx.pi) / 2
    exponential = ctx.expj(-2 * theta)

    z0 = x[0] + exponential * y[0]
    if order == 0:
        return [z0]
    z1 = x[1] + exponential * (-y[1] - 2 * p1 * y[0])
    if order == 1:
        return [z0, z1]

    p2 = ctx.j * (ctx.psi(1, s / 2) - ctx.psi(1, (1 - s) / 2)) / 8
    z2 = x[2] + exponential * (
        y[2] + 4 * p1 * y[1] + 4 * p1**2 * y[0] + 2j * p2 * y[0]
    )
    if order == 2:
        return [z0, z1, z2]

    p3 = -(ctx.psi(2, s / 2) + ctx.psi(2, (1 - s) / 2)) / 16
    p4 = -ctx.j * (ctx.psi(3, s / 2) - ctx.psi(3, (1 - s) / 2)) / 32
    z3 = x[3] + exponential * (
        -y[3]
        - 6 * p1 * y[2]
        - 12 * p1**2 * y[1]
        - 8 * p1**3 * y[0]
        - 6j * p2 * y[1]
        - 12j * p1 * p2 * y[0]
        + 2 * p3 * y[0]
    )
    z4 = x[4] + exponential * (
        y[4]
        + 8 * p1 * y[3]
        + 24 * p1**2 * y[2]
        + 32 * p1**3 * y[1]
        + 16 * p1**4 * y[0]
        + 12j * p2 * y[2]
        + 48j * p1 * p2 * y[1]
        + 48j * p1**2 * p2 * y[0]
        - 12 * p2**2 * y[0]
        - 8 * p3 * y[1]
        - 16 * p1 * p3 * y[0]
        - 2j * p4 * y[0]
    )
    return [z0, z1, z2, z3, z4]


def xi_logderivative_jet(
    s: mp.mpc, order: int = 1
) -> tuple[list[mp.mpc], mp.mpc]:
    """Return F=xi'/xi derivatives through order 0, 1, or 3."""
    if order not in (0, 1, 3):
        raise ValueError("implemented F-jet orders are 0, 1, and 3")
    z = simultaneous_zeta_jet(s, 0 if order == 0 else 2 if order == 1 else 4)
    ratios = [value / z[0] for value in z]
    q: list[mp.mpc] = []
    if order == 0:
        z1 = simultaneous_zeta_jet(s, 1)[1]
        q.append(z1 / z[0])
    else:
        q.append(ratios[1])
        q.append(ratios[2] - ratios[1] ** 2)
        if order == 3:
            q.append(ratios[3] - 3 * ratios[2] * ratios[1] + 2 * ratios[1] ** 3)
            q.append(
                ratios[4]
                - 4 * ratios[3] * ratios[1]
                - 3 * ratios[2] ** 2
                + 12 * ratios[2] * ratios[1] ** 2
                - 6 * ratios[1] ** 4
            )

    result: list[mp.mpc] = []
    for k in range(order + 1):
        completion = (-1) ** k * math.factorial(k) * (
            1 / s ** (k + 1) + 1 / (s - 1) ** (k + 1)
        )
        if k == 0:
            completion -= mp.log(mp.pi) / 2
        completion += mp.polygamma(k, s / 2) / (2 ** (k + 1))
        result.append(completion + q[k])
    return result, z[0]


def stieltjes_moments(
    f_jet: list[mp.mpc], x: mp.mpf, maximum: int
) -> list[mp.mpf]:
    """Convert one F jet using the exact L-4102 coefficients."""
    if maximum >= len(f_jet):
        raise ValueError("F jet is too short")
    moments: list[mp.mpf] = []
    for n in range(maximum + 1):
        value = mp.mpf("0")
        for k in range(n + 1):
            coefficient = (
                (-1) ** k
                * mp.factorial(2 * n - k)
                / (
                    mp.power(2, 2 * n - k)
                    * mp.factorial(n)
                    * mp.factorial(k)
                    * mp.factorial(n - k)
                )
            )
            value += coefficient * mp.re(f_jet[k]) / x ** (2 * n - k + 1)
        moments.append(value)
    return moments
