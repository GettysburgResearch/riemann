#!/usr/bin/env python3
"""Carrier-localized compact-support Weil Gram family.

The exact kernel formulas in this file are mathematical finite expressions.
The NumPy search routines use ordinary floating point and are discovery tools,
not proof certificates.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import mpmath as mp

try:
    import numpy as np
except ImportError:  # exact-kernel users need not install NumPy
    np = None

from triangular import prime_powers_up_to, primes_up_to, sinc_pi


def carrier_f_transform(z, frequency, delta):
    """Fourier transform of 1_[−delta/2,delta/2](x) cos(2*pi*a*x)."""
    z = mp.mpc(z)
    frequency = mp.mpf(frequency)
    delta = mp.mpf(delta)
    return delta / 2 * (sinc_pi(delta * (z - frequency)) + sinc_pi(delta * (z + frequency)))


def convolution_kernel(xi, a, b, delta):
    """Exact compact convolution C_ab(xi), supported on |xi|<=delta."""
    xi = mp.mpf(xi)
    a = mp.mpf(a)
    b = mp.mpf(b)
    delta = mp.mpf(delta)
    if abs(xi) > delta:
        return mp.mpf(0)
    ell = delta - abs(xi)
    if ell == 0:
        return mp.mpf(0)
    return ell / 2 * (
        sinc_pi((a + b) * ell) * mp.cos(mp.pi * (a - b) * xi)
        + sinc_pi((a - b) * ell) * mp.cos(mp.pi * (a + b) * xi)
    )


def gram_entry(a, b, delta):
    return convolution_kernel(0, a, b, delta)


def prime_entry(a, b, c):
    """Complete exact finite prime-power entry, evaluated with mpmath."""
    c = mp.mpf(c)
    L = mp.log(c)
    delta = L / (2 * mp.pi)
    total = mp.mpf(0)
    for item in prime_powers_up_to(c):
        xi = mp.log(item.q) / (2 * mp.pi)
        total += item.mangoldt_weight * convolution_kernel(xi, a, b, delta)
    return -total / mp.pi


def pole_entry(a, b, delta):
    return 2 * mp.re(carrier_f_transform(mp.j / 2, a, delta) * carrier_f_transform(mp.j / 2, b, delta))


def arch_entry_compact(a, b, L, *, dps=80):
    """Exact compact archimedean formula, ordinary mpmath evaluation."""
    with mp.workdps(dps):
        a = mp.mpf(a)
        b = mp.mpf(b)
        L = mp.mpf(L)
        delta = L / (2 * mp.pi)
        G = gram_entry(a, b, delta)

        def integrand(t):
            t = mp.mpf(t)
            if t == 0:
                # Used only in non-rigorous validation. Interval code should
                # replace this extrapolation by an explicit Taylor enclosure.
                h = mp.power(10, -(mp.mp.dps // 3))
                return integrand(h)
            return (
                mp.exp(-t) * G / t
                - mp.exp(-t / 4) / (-mp.expm1(-t))
                * convolution_kernel(t / (4 * mp.pi), a, b, delta)
            )

        value = mp.quad(integrand, [0, 2 * L]) + G * mp.e1(2 * L) - G * mp.log(mp.pi)
        return +value / (2 * mp.pi)


@dataclass(frozen=True)
class LeadingCoefficients:
    c: int
    q: "np.ndarray"
    logs: "np.ndarray"
    amplitudes: "np.ndarray"
    t: "np.ndarray"
    edge: "np.ndarray"


def build_leading_coefficients(c: int) -> LeadingCoefficients:
    """Generate every prime-power coefficient through integer cutoff c."""
    if np is None:
        raise RuntimeError("NumPy is required for discovery routines")
    if not isinstance(c, int) or isinstance(c, bool) or c < 2:
        raise ValueError("c must be an integer at least 2")
    L = math.log(c)
    qs: list[int] = []
    ps_base: list[int] = []
    for p in primes_up_to(c):
        q = p
        while q <= c:
            qs.append(q)
            ps_base.append(p)
            if q > c // p:
                break
            q *= p
    order = np.argsort(np.asarray(qs, dtype=np.int64))
    q_array = np.asarray(qs, dtype=np.float64)[order]
    p_array = np.asarray(ps_base, dtype=np.float64)[order]
    logs = np.log(q_array)
    edge = 1 - logs / L
    amplitudes = np.log(p_array) / np.sqrt(q_array) * edge / math.pi
    mask = amplitudes > 0
    return LeadingCoefficients(
        c,
        q_array.astype(np.int64)[mask],
        logs[mask],
        amplitudes[mask],
        (logs / L)[mask],
        edge[mask],
    )


def leading_prime_matrix(carrier: int | float, N: int, coeffs: LeadingCoefficients, *, chunk: int = 50_000):
    """Complete dominant high-carrier prime matrix using all prime powers.

    Long-double range reduction is used before evaluating cosine in double
    precision. This improves phase accuracy but is still not an interval
    computation.
    """
    if np is None:
        raise RuntimeError("NumPy is required")
    if N < 0:
        raise ValueError("N must be nonnegative")
    Tld = np.longdouble(str(carrier))
    logs_ld = np.log(coeffs.q.astype(np.longdouble))
    Lld = np.log(np.longdouble(coeffs.c))
    phase = np.remainder(Tld * logs_ld, np.longdouble(2) * np.longdouble(np.pi)).astype(float)
    t_all = (logs_ld / Lld).astype(float)
    edge_all = (1 - logs_ld / Lld).astype(float)
    js = np.arange(-N, N + 1, dtype=float)
    matrix = np.zeros((len(js), len(js)), dtype=float)
    for start in range(0, len(coeffs.amplitudes), chunk):
        sl = slice(start, min(start + chunk, len(coeffs.amplitudes)))
        ph = phase[sl]
        aa = coeffs.amplitudes[sl]
        tt = t_all[sl]
        bb = edge_all[sl]
        for i, j in enumerate(js):
            for k_index, k in enumerate(js):
                matrix[i, k_index] += np.sum(
                    aa * np.sinc((j - k) * bb) * np.cos(ph + math.pi * (j + k) * tt)
                )
    return (matrix + matrix.T) / 2


def leading_normalized_minimum(carrier: int | float, N: int, coeffs: LeadingCoefficients):
    """Return alpha-lambda_max(S), the high-carrier leading screen."""
    if np is None:
        raise RuntimeError("NumPy is required")
    matrix = leading_prime_matrix(carrier, N, coeffs)
    values, vectors = np.linalg.eigh(matrix)
    alpha = math.log(float(carrier) / (2 * math.pi)) / (2 * math.pi)
    return alpha - values[-1], values[-1], vectors[:, -1]
