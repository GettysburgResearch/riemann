#!/usr/bin/env python3
"""Carrier-shifted triangular Guinand--Weil test family.

Discovery arithmetic uses mpmath and is NOT directed-rounding interval
arithmetic.  No sign emitted by this module is a proof certificate.

Fourier convention:
    g(z) = integral g_hat(xi) exp(2*pi*i*z*xi) dxi.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import mpmath as mp


@dataclass(frozen=True)
class PrimePower:
    q: int
    p: int
    exponent: int

    @property
    def mangoldt_weight(self) -> mp.mpf:
        return mp.log(self.p) / mp.sqrt(self.q)


def primes_up_to(limit: int) -> list[int]:
    if not isinstance(limit, int) or isinstance(limit, bool) or limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def prime_powers_up_to(c: int | str | mp.mpf) -> list[PrimePower]:
    value = mp.mpf(c)
    if not mp.isfinite(value) or value < 2:
        raise ValueError("c must be finite and at least 2")
    bound = int(mp.floor(value))
    out: list[PrimePower] = []
    for p in primes_up_to(bound):
        q = p
        exponent = 1
        while q <= value:
            out.append(PrimePower(q=q, p=p, exponent=exponent))
            if q > bound // p:
                break
            q *= p
            exponent += 1
    out.sort(key=lambda item: item.q)
    return out


def sinc_pi(x: int | float | mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    """Normalized sinc: sin(pi*x)/(pi*x), analytically continued at zero."""
    x = mp.mpc(x)
    if x == 0:
        return mp.mpf(1)
    value = mp.sin(mp.pi * x) / (mp.pi * x)
    return mp.re(value) if mp.im(x) == 0 else value


def triangle_hat(xi: int | str | mp.mpf, delta: int | str | mp.mpf) -> mp.mpf:
    xi = mp.mpf(xi)
    delta = mp.mpf(delta)
    if delta <= 0:
        raise ValueError("delta must be positive")
    return max(mp.mpf(0), 1 - abs(xi) / delta)


def h_delta(z: int | float | mp.mpf | mp.mpc, delta: int | str | mp.mpf) -> mp.mpf | mp.mpc:
    """Inverse transform of the triangular Fourier weight."""
    delta = mp.mpf(delta)
    return delta * sinc_pi(delta * mp.mpc(z)) ** 2


def g_carrier(z: int | float | mp.mpf | mp.mpc, carrier: int | str | mp.mpf, delta: int | str | mp.mpf):
    carrier = mp.mpf(carrier)
    return (h_delta(mp.mpc(z) - carrier, delta) + h_delta(mp.mpc(z) + carrier, delta)) / 2


def prime_term(carrier: int | str | mp.mpf, c: int | str | mp.mpf) -> mp.mpf:
    """Complete finite prime-power contribution for the triangular family."""
    carrier = mp.mpf(carrier)
    c = mp.mpf(c)
    L = mp.log(c)
    total = mp.mpf(0)
    for item in prime_powers_up_to(c):
        edge = 1 - mp.log(item.q) / L
        total += item.mangoldt_weight * edge * mp.cos(carrier * mp.log(item.q))
    return -total / mp.pi


def pole_term(carrier: int | str | mp.mpf, L: int | str | mp.mpf) -> mp.mpf:
    L = mp.mpf(L)
    delta = L / (2 * mp.pi)
    return 2 * mp.re(g_carrier(mp.j / 2, carrier, delta))


def _b_series(t: mp.mpf, L: mp.mpf) -> mp.mpf:
    """Local Taylor series for the removable b_L singularity."""
    return (
        mp.mpf("0.25") - 1 / (2 * L)
        + t * (-mp.mpf(1) / 96 - 1 / (8 * L))
        + t**2 * (-mp.mpf(1) / 128 + 1 / (192 * L))
        + t**3 * (mp.mpf(7) / 92160 + 1 / (256 * L))
        + t**4 * (mp.mpf(5) / 24576 - mp.mpf(7) / (184320 * L))
    )


def b_weight(t: int | str | mp.mpf, L: int | str | mp.mpf) -> mp.mpf:
    t = mp.mpf(t)
    L = mp.mpf(L)
    if L <= 0:
        raise ValueError("L must be positive")
    if t == 0:
        return mp.mpf("0.25") - 1 / (2 * L)
    if abs(t) < mp.mpf("1e-8"):
        return _b_series(t, L)
    return mp.exp(-t / 4) / (-mp.expm1(-t)) * (1 - t / (2 * L)) - 1 / t


def arch_compact(carrier: int | str | mp.mpf, L: int | str | mp.mpf, *, dps: int = 80) -> mp.mpf:
    """Compact exact-form archimedean term, evaluated non-rigorously.

    This uses the cancellation-safe unreduced integrand.  It is useful for
    moderate carriers and normalization tests.  Very-high-carrier proof work
    needs an interval oscillatory-integral implementation, not mpmath.quad.
    """
    if dps < 30:
        raise ValueError("dps must be at least 30")
    with mp.workdps(dps):
        carrier = mp.mpf(carrier)
        L = mp.mpf(L)
        omega = carrier / 2
        X = 2 * L

        def integrand(t):
            t = mp.mpf(t)
            if t == 0:
                return -1 - b_weight(0, L)
            cosine = mp.cos(omega * t)
            return (mp.exp(-t) - cosine) / t - b_weight(t, L) * cosine

        points = [mp.mpf(0)]
        if carrier != 0:
            period = 2 * mp.pi / abs(omega)
            pieces = min(2000, max(1, int(mp.ceil(X / period))))
            points.extend(X * k / pieces for k in range(1, pieces))
        points.append(X)
        value = mp.quad(integrand, points) + mp.e1(X) - mp.log(mp.pi)
        return +value / (2 * mp.pi)


def arch_reduced(carrier: int | str | mp.mpf, L: int | str | mp.mpf, *, dps: int = 80) -> mp.mpf:
    """Equivalent Ci reduction for nonzero carrier; non-rigorous evaluation."""
    with mp.workdps(dps):
        carrier = mp.mpf(carrier)
        L = mp.mpf(L)
        if carrier == 0:
            return arch_compact(0, L, dps=dps)
        integral = mp.quad(lambda t: b_weight(t, L) * mp.cos(carrier * t / 2), [0, 2 * L])
        return +(mp.log(abs(carrier) / (2 * mp.pi)) - mp.ci(abs(carrier) * L) - integral) / (2 * mp.pi)


def weil_value(carrier: int | str | mp.mpf, c: int | str | mp.mpf, *, dps: int = 80) -> mp.mpf:
    """Complete scalar explicit-formula value, ordinary arbitrary precision."""
    with mp.workdps(dps):
        c = mp.mpf(c)
        L = mp.log(c)
        return +(prime_term(carrier, c) + pole_term(carrier, L) + arch_compact(carrier, L, dps=dps))
