#!/usr/bin/env python3
"""Pure-Python Riemann zero ordinates via Euler-Maclaurin + Hardy Z sign changes.

Standard library only.  These ordinates are binary64 DISCOVERY data: a sign
change of a floating-point Hardy Z evaluation is not a certified zero bin.
They are used here only to (a) audit the D-9501.1 normalization against the
zero-side expansion and (b) evaluate the L-9507 zero-accounting ratio in
reconnaissance mode.  A certifying run needs directed enclosures of Z and an
interval bisection, which this file deliberately does not claim to provide.

Self-check: the zero count is compared against N(T) = theta(T)/pi + 1 + S(T);
a large |S(T)| means ordinates were missed by the scan step.
"""
import cmath
import json
import math
import sys

BERN = [1.0 / 6, -1.0 / 30, 1.0 / 42, -1.0 / 30, 5.0 / 66,
        -691.0 / 2730, 7.0 / 6, -3617.0 / 510, 43867.0 / 798]

_LOGN = [0.0, 0.0]
_INVSQ = [0.0, 1.0]


def _extend(nmax):
    while len(_LOGN) <= nmax:
        k = len(_LOGN)
        _LOGN.append(math.log(k))
        _INVSQ.append(1.0 / math.sqrt(k))


def log_gamma(z):
    """Complex log Gamma via shifted Stirling."""
    shift = 0.0
    while abs(z) < 12.0:
        shift += cmath.log(z)
        z += 1.0
    s = (z - 0.5) * cmath.log(z) - z + 0.5 * math.log(2.0 * math.pi)
    zp = z
    z2 = z * z
    for k in range(1, 9):
        s += BERN[k - 1] / (2 * k * (2 * k - 1) * zp)
        zp *= z2
    return s - shift


def theta(t):
    """Riemann-Siegel theta."""
    return log_gamma(complex(0.25, t / 2.0)).imag - t * math.log(math.pi) / 2.0


def zeta_half(t, terms=8):
    """zeta(1/2 + i t) by Euler-Maclaurin."""
    N = max(12, int(abs(t)) + 8)
    _extend(N)
    s = complex(0.5, t)
    tot = 0.0 + 0.0j
    for n in range(1, N):
        ang = -t * _LOGN[n]
        tot += _INVSQ[n] * complex(math.cos(ang), math.sin(ang))
    logN = math.log(N)
    Npow = math.exp(-0.5 * logN) * complex(math.cos(-t * logN),
                                           math.sin(-t * logN))   # N^{-s}
    tot += 0.5 * Npow
    tot += Npow * N / (s - 1.0)                                    # N^{1-s}/(s-1)
    fac = s
    term = Npow / N                                                # N^{-s-1}
    for k in range(1, terms + 1):
        tot += BERN[k - 1] / math.factorial(2 * k) * fac * term
        fac *= (s + 2 * k - 1) * (s + 2 * k)
        term /= (N * N)
    return tot


def Z(t):
    """Hardy Z function (real)."""
    return (cmath.exp(complex(0.0, theta(t))) * zeta_half(t)).real


def find_zeros(tmax, step=0.05, tol=1e-11):
    zs = []
    t = 8.0
    prev = Z(t)
    while t < tmax:
        t2 = t + step
        cur = Z(t2)
        if prev == 0.0:
            zs.append(t)
        elif prev * cur < 0.0:
            a, b, fa = t, t2, prev
            while b - a > tol:
                m = 0.5 * (a + b)
                fm = Z(m)
                if fm == 0.0:
                    a = b = m
                    break
                if fa * fm < 0.0:
                    b = m
                else:
                    a, fa = m, fm
            zs.append(0.5 * (a + b))
        t, prev = t2, cur
    return zs


def main():
    tmax = float(sys.argv[1]) if len(sys.argv) > 1 else 1000.0
    out = sys.argv[2] if len(sys.argv) > 2 else "zeros.json"
    zs = find_zeros(tmax)
    # Riemann-von Mangoldt self-check: N(T) ~ theta(T)/pi + 1
    predicted = theta(tmax) / math.pi + 1.0
    print(f"found {len(zs)} zeros with 0 < gamma < {tmax}")
    print(f"N(T) = theta(T)/pi + 1 = {predicted:.4f}  (S(T) should be small)")
    print(f"discrepancy S(T) = {len(zs) - predicted:+.4f}")
    print("first 5:", [f"{g:.12f}" for g in zs[:5]])
    with open(out, "w") as fh:
        json.dump({"tmax": tmax, "count": len(zs),
                   "vonmangoldt": predicted, "zeros": zs}, fh)
    print("written", out)


if __name__ == "__main__":
    main()
