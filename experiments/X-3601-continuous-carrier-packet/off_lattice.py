#!/usr/bin/env python3
"""High-precision controls for the exact L-3601 off-lattice formulas."""
from __future__ import annotations

import mpmath as mp


def sinc(z):
    return mp.mpf(1) if z == 0 else mp.sin(z) / z


def box_sinc(x, delta):
    return mp.sqrt(delta) * sinc(mp.pi * delta * x)


def gram(ti, tj, delta):
    return sinc(mp.pi * delta * (ti - tj))


def frequency_kernel(ti, tj, xi, delta):
    if abs(xi) > delta:
        return mp.mpf(0)
    ell = delta - abs(xi)
    return (ell / delta) * sinc(mp.pi * (ti - tj) * ell) * mp.cos(mp.pi * (ti + tj) * xi)


def pole_entry(ti, tj, L):
    delta = L / (2 * mp.pi)
    return 2 * mp.re(box_sinc(mp.j / 2 - ti, delta) * box_sinc(mp.j / 2 - tj, delta))


def arch_entry(ti, tj, L):
    """Numerically evaluate the compact exact-form archimedean entry."""
    delta = L / (2 * mp.pi)
    gram_value = gram(ti, tj, delta)

    def integrand(t):
        if t == 0:
            return integrand(mp.power(10, -(mp.mp.dps // 3)))
        kernel = frequency_kernel(ti, tj, t / (4 * mp.pi), delta)
        return mp.exp(-t) * gram_value / t - mp.exp(-t / 4) * kernel / (1 - mp.exp(-t))

    return (
        mp.quad(integrand, [0, 2 * L])
        + gram_value * mp.e1(2 * L)
        - gram_value * mp.log(mp.pi)
    ) / (2 * mp.pi)


def correct_dimensionless_prime_kernel(x, y, u):
    return (1 - u) * sinc(mp.pi * (x - y) * (1 - u)) * mp.cos(mp.pi * (x + y) * u)


def naive_fractional_divided_difference(x, y, u):
    if x == y:
        return 2 * (1 - u) * mp.cos(2 * mp.pi * x * u)
    return (mp.sin(2 * mp.pi * y * u) - mp.sin(2 * mp.pi * x * u)) / (2 * mp.pi * (x - y))
