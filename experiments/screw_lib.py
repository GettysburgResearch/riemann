#!/usr/bin/env python3
"""Shared pure-Python screw-function machinery for the X-9503 audit.

Standard library only: no NumPy, MPFR, FLINT or special-function package.
This is binary64 DISCOVERY code.  Nothing here is a proof producer; every
claim that depends on a sign or an ordering must be replayed with directed
arithmetic before it is used as a certificate.

Psi is evaluated from D-9501.1 independently of `screw_fir_toeplitz_recon.py`
so that the two implementations can be compared as a cross-check.
"""
import bisect
import math

EULER_GAMMA = 0.5772156649015328606065120900824024310422
CATALAN = 0.9159655941772190150546035149323841107741
PSI_QUARTER = -EULER_GAMMA - math.pi / 2.0 - 3.0 * math.log(2.0)
C_CONST = math.pi * math.pi + 8.0 * CATALAN
B_LIN = 0.5 * (PSI_QUARTER - math.log(math.pi))


def integer_nth_root(value, degree):
    if value < 2:
        return value
    lo, hi = 0, 1 << ((value.bit_length() + degree - 1) // degree)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid ** degree <= value:
            lo = mid
        else:
            hi = mid
    return lo


class Psi:
    """Psi(t) via D-9501.1, prefix sums over prime powers."""

    def __init__(self, limit):
        self.limit = limit
        flags = bytearray(b"\x01") * (limit + 1)
        flags[0:2] = b"\x00\x00"
        for p in range(2, math.isqrt(limit) + 1):
            if flags[p]:
                flags[p * p:: p] = b"\x00" * (((limit - p * p) // p) + 1)
        tab = []
        self.n_primes = 0
        for p in range(2, limit + 1):
            if not flags[p]:
                continue
            self.n_primes += 1
            lp = math.log(p)
            q = p
            while q <= limit:
                tab.append((q, lp))
                q *= p
        tab.sort()
        self.n_pp = len(tab)
        self.tau = [math.log(q) for q, _ in tab]
        self.P0 = [0.0]
        self.P1 = [0.0]
        s0 = s1 = 0.0
        for (q, lp), lq in zip(tab, self.tau):
            w = lp / math.sqrt(q)
            s0 += w
            s1 += w * lq
            self.P0.append(s0)
            self.P1.append(s1)

    def smooth(self, t):
        tot = 0.0
        m = 0
        while True:
            d = 4 * m + 1
            e = d * t / 2.0
            if e > 60.0:
                break
            term = math.exp(-e) / (d * d)
            tot += term
            if term < 1e-19:
                break
            m += 1
        return (4.0 * (math.exp(t / 2.0) + math.exp(-t / 2.0) - 2.0)
                + B_LIN * t + C_CONST / 4.0 - 4.0 * tot)

    def __call__(self, t):
        t = abs(t)
        if t == 0.0:
            return 0.0
        j = bisect.bisect_right(self.tau, t)
        if j == len(self.tau) and t > self.tau[-1]:
            # caller must guarantee e^t <= limit
            if math.exp(t) > self.limit + 1:
                raise ValueError(f"t={t} exceeds prime table (limit={self.limit})")
        return self.smooth(t) - (t * self.P0[j] - self.P1[j])


def screw_toeplitz(psi, n, h):
    """H^{(n)}_{ij}(h) = Psi((i-j+1)h)+Psi((i-j-1)h)-2 Psi((i-j)h)."""
    a = [psi((k + 1) * h) + psi((k - 1) * h) - 2.0 * psi(k * h)
         for k in range(n)]
    return [[a[abs(i - j)] for j in range(n)] for i in range(n)]


def jacobi_eig(mat, sweeps=100, tol=1e-16):
    """Cyclic Jacobi for real symmetric matrices. Returns (vals, vecs-by-column)."""
    n = len(mat)
    a = [row[:] for row in mat]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(sweeps):
        off = math.sqrt(sum(a[i][j] ** 2
                            for i in range(n) for j in range(n) if i != j))
        nrm = math.sqrt(sum(a[i][j] ** 2 for i in range(n) for j in range(n)))
        if nrm == 0.0 or off <= tol * nrm:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(a[p][q]) < 1e-300:
                    continue
                theta = (a[q][q] - a[p][p]) / (2.0 * a[p][q])
                t = (1.0 if theta >= 0 else -1.0) / (
                    abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p] = c * akp - s * akq
                    a[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k] = c * apk - s * aqk
                    a[q][k] = s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = v[k][p], v[k][q]
                    v[k][p] = c * vkp - s * vkq
                    v[k][q] = s * vkp + c * vkq
    vals = [a[i][i] for i in range(n)]
    return vals, v


def rayleigh(mat, x):
    n = len(mat)
    num = 0.0
    for i in range(n):
        row = mat[i]
        acc = 0.0
        for j in range(n):
            acc += row[j] * x[j]
        num += x[i] * acc
    den = sum(xi * xi for xi in x)
    return num / den
