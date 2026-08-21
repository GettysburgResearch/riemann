"""Shared Phi / Xi / window helpers for X-8455 reconnaissance.

Discovery arithmetic only. Not a certified special-functions library.
"""

from __future__ import annotations

from mpmath import mp, mpf, pi, zeta, gamma, exp, cos, quad, zetazero, nstr


def xi_half(s):
    return mpf("0.5") * s * (s - 1) * pi ** (-s / 2) * gamma(s / 2) * zeta(s)


def Xi(z):
    return (xi_half(mpf("0.5") + 1j * mpf(z))).real


def Phi(t):
    t = abs(mpf(t))
    tot = mpf(0)
    for n in range(1, 60):
        en = exp(2 * t)
        term = (4 * pi**2 * n**4 * exp(mpf("4.5") * t) - 6 * pi * n**2 * exp(mpf("2.5") * t)) * exp(
            -pi * n**2 * en
        )
        tot += term
        if n > 4 and abs(term) < mpf("1e-45") * max(abs(tot), mpf(1)):
            break
    return tot


def Phi_gaussian(t, sigma=mpf("0.5")):
    """Control kernel with no arithmetic zeros in its transform."""
    t = mpf(t)
    return exp(-(t * t) / (2 * sigma * sigma))


def Fwin(alpha, j, kernel=Phi):
    T = mpf(1) / (2 * mpf(alpha))
    return 2 * quad(lambda t: kernel(t) * cos(2 * pi * mpf(alpha) * j * t), [0, T])


def gammas(M=20):
    return [mp.im(zetazero(k)) for k in range(1, M + 1)]
