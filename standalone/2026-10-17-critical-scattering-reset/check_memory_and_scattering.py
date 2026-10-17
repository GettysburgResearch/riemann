#!/usr/bin/env python3
"""Exact prime-log and all-pass controls; separate binary64 Gaussian check."""
import json
import math
from fractions import Fraction as Q


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sieve(nmax):
    spf = list(range(nmax + 1))
    for p in range(2, math.isqrt(nmax) + 1):
        if spf[p] == p:
            for n in range(p * p, nmax + 1, p):
                if spf[n] == n:
                    spf[n] = p
    facts = [{} for _ in range(nmax + 1)]
    mobius = [0] * (nmax + 1)
    mobius[1] = 1
    for n in range(2, nmax + 1):
        p = spf[n]
        facts[n] = dict(facts[n // p])
        facts[n][p] = facts[n].get(p, 0) + 1
        mobius[n] = 0 if any(e > 1 for e in facts[n].values()) else (-1) ** len(facts[n])
    return facts, mobius


def main():
    nmax = 512
    facts, mu = sieve(nmax)
    prime_log_checks = 0
    caught_reversed_sign = False
    for n in range(1, nmax + 1):
        for p, exponent in facts[n].items():
            lhs = sum(mu[n // (p ** k)] for k in range(1, exponent + 1))
            rhs = -mu[n] * exponent
            require(lhs == rhs, f"prime-log coefficient at n={n}, p={p}")
            prime_log_checks += 1
            caught_reversed_sign |= lhs != mu[n] * exponent
    require(caught_reversed_sign, "wrong convolution sign was not rejected")

    allpass_checks = 0
    parameters = [(Q(1, 4), Q(3, 4)), (Q(1, 3), Q(2, 3)), (Q(2, 5), Q(7, 5)), (Q(1), Q(1))]
    for a, b in parameters:
        c, d = (b - a) / (a + b), 2 * a / (a + b)
        require(c * c / (2 * b) + d * d / (2 * a) == 1 / (2 * b), "boundary isometry")
        require(d > 0, "nonzero causal residue")
        for r in [Q(2), Q(3), Q(5, 2)]:
            require((r + a) / ((r - a) * (r + b)) == c / (r + b) + d / (r - a), "partial fractions")
            allpass_checks += 1
        allpass_checks += 2
    a, b = parameters[0]
    c, d = (b - a) / (a + b), 2 * a / (a + b)
    require(c * c / (2 * b) != 1 / (2 * b), "discarded negative-time mass control")

    # Independent finite coefficient regrouping. The delayed inner sum is
    # restricted by dm<=nmax, so this checks the exact finite identity,
    # without pretending that it is the complete infinite memory.
    prime_powers = [(n, math.log(next(iter(f)))) for n, f in enumerate(facts) if n >= 2 and len(f) == 1]
    points = [-2.0, 0.0, 1.0, 3.0, math.log(64), math.log(256)]
    residuals = []
    wrong_residuals = []
    norm = 1 / (2 * math.sqrt(math.pi))
    for u in points:
        gv, derivative = 0.0, 0.0
        for n in range(1, nmax + 1):
            y = u - math.log(n)
            term = mu[n] / math.sqrt(n) * norm * math.exp(-y * y / 4)
            gv += term
            derivative += -y * term / 2
        memory = 0.0
        for d, lam in prime_powers:
            inner = 0.0
            for m in range(1, nmax // d + 1):
                y = u - math.log(d * m)
                inner += mu[m] / math.sqrt(m) * norm * math.exp(-y * y / 4)
            memory += lam / math.sqrt(d) * inner
        residuals.append(abs(2 * derivative + u * gv + memory))
        wrong_residuals.append(abs(2 * derivative + u * gv - memory))
    require(max(residuals) < 2e-12, "Gaussian finite convolution mismatch")
    require(max(wrong_residuals) > 1e-3, "wrong signed memory was not rejected")
    print(json.dumps({
        "status": "PASS",
        "exact_integer_prime_log_checks": prime_log_checks,
        "complete_integer_prefix": nmax,
        "exact_rational_allpass_checks": allpass_checks,
        "negative_controls": ["reversed Mobius convolution sign", "discarded negative-time boundary energy", "reversed Gaussian memory sign"],
        "binary64_gaussian_points": points,
        "binary64_max_finite_identity_residual": max(residuals),
        "limitations": "Exact finite algebra and separate non-directed binary64 normalization only; no infinite tail computation, zeta zero census, or RH-strength upper estimate."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
