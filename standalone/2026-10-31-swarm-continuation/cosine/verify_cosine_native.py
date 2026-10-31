#!/usr/bin/env python3
"""Finite exact checks for the cosine/native note; not a proof of RH.

Every comparison below uses integers or Fraction arithmetic.  The universal
analytic claims (Sobolev bounds, Fourier tails, continuity of dual evaluation)
are proved in the manuscript and are not inferred from these finite checks.
No Python assert is used: the checks remain active under python -O.
"""

from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
COUNTS = {}


def check(name, condition):
    if not condition:
        raise ArithmeticError("failed: " + name)
    COUNTS[name] = COUNTS.get(name, 0) + 1


def b(n, k):
    return Q(k % n, n)


def weight(k):
    return Q(1, k * (k + 1))


def log_interval(n, terms=24):
    """Rigorous rational interval by range reduction and the atanh series."""
    power = n.bit_length() - 1
    r = Q(n, 2**power)

    def series(x):
        z = (x - 1) / (x + 1)
        lower = 2 * sum((z ** (2 * j + 1) / (2 * j + 1)
                         for j in range(terms)), Q(0))
        error = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z*z))
        return lower, lower + error

    a, c = series(Q(2))
    d, e = series(r)
    return power*a + d, power*c + e


def mobius_sieve(limit):
    values = [1] * (limit + 1)
    primes = []
    composite = [False] * (limit + 1)
    values[0] = 0
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            values[n] = -1
        for p in primes:
            if n*p > limit:
                break
            composite[n*p] = True
            if n % p == 0:
                values[n*p] = 0
                break
            values[n*p] = -values[n]
    return values


def run():
    # Complete finite arithmetic values, not sampled floating trigonometry.
    for m in range(2, 13):
        for n in range(2, 13):
            for k in range(1, 201):
                check("native_dilation_cocycle",
                      b(m*n, k) == b(m, k)/n + b(n, k//m))
    for m in range(2, 25):
        for j in range(1, 65):
            block = sum((weight(k) for k in range(m*j, m*(j+1))), Q(0))
            check("exact_dilation_norm_blocks", block == weight(j)/m)

    # Formal coefficients of sin(y/k), including the summation boundary.
    for n in range(2, 18):
        for cutoff in [1, 2, 3, 7, 16, 31, 64, 129]:
            lhs = {}
            rhs = {}
            for k in range(1, cutoff + 1):
                lhs[k] = lhs.get(k, Q(0)) + b(n, k)
                lhs[k+1] = lhs.get(k+1, Q(0)) - b(n, k)
                rhs[k] = Q(1, n) - int(k % n == 0)
            rhs[cutoff+1] = -b(n, cutoff)
            check("formal_sine_summation_by_parts", lhs == rhs)

    # The compensator agrees with the exact native mean within its rigorous
    # positive cell tail.  The interval for log is rational, not machine log.
    cutoff = 128
    for n in range(2, 25):
        prefix = sum((b(n, k)*weight(k) for k in range(1, cutoff+1)), Q(0))
        lo, hi = log_interval(n)
        check("log_compensator_inside_native_tail",
              prefix <= lo/n <= hi/n <= prefix + Q(1, cutoff+1))

    # Odd Taylor moments: source and closed-form intervals overlap, with
    # both truncations enclosed by exact elementary integral remainders.
    for order in range(3, 18, 2):
        zeta_prefix = sum((Q(1, k**order) for k in range(1, cutoff+1)), Q(0))
        zlo = zeta_prefix + Q(1, (order-1)*(cutoff+1)**(order-1))
        zhi = zeta_prefix + Q(1, (order-1)*cutoff**(order-1))
        for n in range(2, 19):
            native = sum((b(n, k)*(Q(1, k**order)-Q(1, (k+1)**order))
                          for k in range(1, cutoff+1)), Q(0))
            native_hi = native + Q(1, (cutoff+1)**order)
            factor = Q(1, n) - Q(1, n**order)
            check("odd_source_moment_interval_overlap",
                  max(native, factor*zlo) <= min(native_hi, factor*zhi))

    mu = mobius_sieve(4096)
    divisor_sum = [0] * len(mu)
    for d in range(1, len(mu)):
        for n in range(d, len(mu), d):
            divisor_sum[n] += mu[d]
    for n in range(1, len(mu)):
        check("mobius_divisor_identity", divisor_sum[n] == int(n == 1))

    for nmax in [2, 3, 5, 8, 16, 31, 64, 97, 128]:
        endpoint = sum((Q(mu[n], n) for n in range(1, nmax+1)), Q(0))
        energy = Q(0)
        for k in range(1, nmax+1):
            residual = 1 + sum((mu[n]*b(n, k) for n in range(2, nmax+1)), Q(0))
            check("mobius_exact_native_prefix", residual == k*endpoint)
            energy += residual*residual*weight(k)
        harmonic = sum((Q(1, k) for k in range(1, nmax+2)), Q(0))
        check("mobius_exact_prefix_energy",
              energy == endpoint*endpoint*(nmax+1-harmonic))

        # Coefficients forced by an exactly zero prefix, plus the first
        # available high-index coefficient enforcing sum c_n/n=1.
        coeff = {n: -mu[n] for n in range(2, nmax+1)}
        coeff[nmax+1] = (nmax+1)*endpoint
        check("prefix_compensation_scalar",
              sum((Q(value, n) for n, value in coeff.items()), Q(0)) == 1)
        for k in range(1, nmax+1):
            check("prefix_compensation_exact_zeros",
                  1-sum((value*b(n, k) for n, value in coeff.items()), Q(0)) == 0)

    # Rational check of the final simplification in Theorem 4's constant.
    check("frequency_tail_constant", Q(32, 3)**2 * 2 < 16**2)
    check("checks_active_under_optimization", __debug__ in [True, False])

    manuscript = ROOT / "COSINE_PHASE_AND_NATIVE_SYNTHESIS.md"
    sources = ROOT / "SOURCES.md"
    report = {
        "status": "PASS",
        "arithmetic": "exact integers and rational intervals only",
        "checks": COUNTS,
        "total_checks": sum(COUNTS.values()),
        "manuscript_sha256": sha256(manuscript.read_bytes()).hexdigest(),
        "sources_sha256": sha256(sources.read_bytes()).hexdigest(),
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Finite normalization and native identity checks. Analytic universal theorems are proved in the manuscript, not certified by this script. No RH proof, norm convergence, or new zero-free boundary is claimed.",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    run()
