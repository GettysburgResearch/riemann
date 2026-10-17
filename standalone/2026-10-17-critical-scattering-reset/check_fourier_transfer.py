#!/usr/bin/env python3
"""Exact finite checks for FOURIER_TRANSFER_AND_COVARIANCE.md.

This does not verify Davenport, limits, Banach-algebra convergence, or RH.
All checks use Fraction; no floating-point tolerance is used.
"""
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json


COUNTS = Counter()


def require(ok, name):
    COUNTS[name] += 1
    if not ok:
        raise RuntimeError(f"FAILED: {name}")


def factors(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            k = 0
            while n % p == 0:
                n //= p
                k += 1
            out.append((p, k))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def mul_series(a, b, length):
    c = [Q(0)] * length
    for i in range(min(len(a), length)):
        for j in range(min(len(b), length - i)):
            c[i + j] += a[i] * b[j]
    return c


def inv_series(a, length):
    require(a[0] == 1, "unit-constant-term")
    c = [Q(1)] + [Q(0)] * (length - 1)
    for k in range(1, length):
        c[k] = -sum(a[j] * c[k - j]
                    for j in range(1, min(k + 1, len(a))))
    return c


def phase(p, profile):
    if profile == 0:
        return Q(1)
    if profile == 1:
        return Q(-1 if p % 3 == 1 else 1)
    if profile == 2:
        return Q(0 if p % 3 == 1 else -1)
    return Q(-1 if p % 4 == 1 else 1, 2)


def xi(p, character):
    if character == "principal":
        return Q(1)
    return Q(0 if p % 2 == 0 else (1 if p % 4 == 1 else -1))


def local(family, m, p, profile, character, excluded, length):
    f = [Q(1)] + [Q(0)] * (length - 1)
    a = f.copy()
    if p in excluded:
        return f, a
    x = xi(p, character)
    require(abs(x) == 1, "conductor-primes-excluded")
    z = phase(p, profile)
    power = z * p ** ((m - 2) // 2)
    a[1] = -x
    if family == "native":
        return a.copy(), a
    if family == "coupled":
        f[1] = -(1 - Q(1, p)) * x
        if m < length:
            f[m] = -power
    elif family == "two-channel":
        f[1] = -x
        if m < length:
            f[m] = -power
        if m + 1 < length:
            f[m + 1] = x * power
    else:
        for k in range(length):
            if k >= 1 and (k - 1) % m == 0:
                f[k] = -(1 - Q(1, p)) * x * power ** ((k - 1) // m)
    return f, a


def direct_supported(family, m, n, profile, character, excluded):
    value = Q(1)
    for p, k in factors(n):
        if p in excluded:
            return Q(0)
        x = xi(p, character)
        z = phase(p, profile)
        alpha = (m - 2) // 2
        if family == "native":
            if k != 1:
                return Q(0)
            value *= -x
        elif family == "coupled":
            if k == 1:
                value *= -x * (1 - Q(1, p))
            elif k == m:
                value *= -z * p ** alpha
            else:
                return Q(0)
        elif family == "two-channel":
            if k == 1:
                value *= -x
            elif k == m:
                value *= -z * p ** alpha
            elif k == m + 1:
                value *= x * z * p ** alpha
            else:
                return Q(0)
        else:
            if k % m != 1:
                return Q(0)
            d_exp = (k - 1) // m
            value *= -x * (1 - Q(1, p)) * z ** d_exp * p ** (alpha * d_exp)
    return value


def dirichlet_conv(a, b):
    limit = len(a) - 1
    out = [Q(0)] * (limit + 1)
    for d in range(1, limit + 1):
        for r in range(1, limit // d + 1):
            out[d * r] += a[d] * b[r]
    return out


def build(family, m, profile, character, excluded, limit):
    prime_cache = {}
    arrays = [[Q(0), Q(1)] + [Q(0)] * (limit - 1) for _ in range(4)]
    for n in range(2, limit + 1):
        vals = [Q(1)] * 4
        for p, k in factors(n):
            if p not in prime_cache:
                f, a = local(family, m, p, profile, character, excluded, 21)
                b = mul_series(f, inv_series(a, 21), 21)
                c = inv_series(b, 21)
                require(mul_series(a, b, 21) == f, "exact-local-ratio")
                require(mul_series(f, c, 21) == a, "exact-local-inverse")
                prime_cache[p] = (f, a, b, c)
            for j, row in enumerate(prime_cache[p]):
                vals[j] *= row[k]
        for j, val in enumerate(vals):
            arrays[j][n] = val
        require(vals[0] == direct_supported(
            family, m, n, profile, character, excluded), "independent-support-formula")
    f, a, b, c = arrays
    require(dirichlet_conv(a, b) == f, "global-forward-convolution")
    require(dirichlet_conv(f, c) == a, "global-inverse-convolution")
    # Uniform-alpha identity checked as a formal Fourier polynomial modulo
    # x^period-1, including the exact alpha -> d*alpha multiplication.
    for period in (2, 3, 5, 16, 31):
        left = [Q(0)] * period
        right = [Q(0)] * period
        wrong_phase = [Q(0)] * period
        for n in range(1, limit + 1):
            left[n % period] += f[n]
        for d in range(1, limit + 1):
            for r in range(1, limit // d + 1):
                right[(d * r) % period] += b[d] * a[r]
                wrong_phase[r % period] += b[d] * a[r]
        require(left == right, "dilation-of-Fourier-phase")
        if family == "coupled" and m == 2 and profile == 0 and period == 31:
            require(left != wrong_phase, "negative-control-undilated-phase")
    return f


def covariance_checks(f, g):
    nmax = min(len(f), len(g)) - 1
    correlation = {}
    for h in range(-nmax + 1, nmax):
        correlation[h] = sum(f[n] * g[n + h]
                             for n in range(1, nmax + 1)
                             if 1 <= n + h <= nmax)
    add_conv = [Q(0)] * (2 * nmax + 1)
    for n in range(1, nmax + 1):
        for m in range(1, nmax + 1):
            add_conv[n + m] += f[n] * g[m]
    require(sum(v * v for v in correlation.values())
            == sum(v * v for v in add_conv), "exact-Parseval-cross-correlation")
    require(sum(correlation.values()) == sum(f) * sum(g),
            "complete-signed-all-shift-identity")
    for width in (2, 5, 11):
        left = sum(Q(width - abs(h), width) * value
                   for h, value in correlation.items() if abs(h) < width)
        right = Q(0)
        for origin in range(2 - width, nmax + 1):
            sf = sum(f[origin + j] for j in range(width)
                     if 1 <= origin + j <= nmax)
            sg = sum(g[origin + j] for j in range(width)
                     if 1 <= origin + j <= nmax)
            right += sf * sg / width
        require(left == right, "complete-Fejer-filter-identity")
    return correlation


def main():
    fixtures = []
    digest = hashlib.sha256()
    for family in ("native", "coupled", "two-channel", "geometric"):
        for m in (2, 4, 6):
            for character, excluded in (("principal", set()), ("mod4", {2, 3})):
                for profile in range(4):
                    f = build(family, m, profile, character, excluded, 256)
                    digest.update((family + str(m) + character + str(profile)).encode())
                    digest.update(";".join(map(str, f)).encode())
                    if profile == 0 and character == "principal" and m == 2:
                        fixtures.append(f[:49])
    for f in fixtures:
        for g in fixtures:
            covariance_checks(f, g)
    corr = covariance_checks(fixtures[0], fixtures[0])
    require(sum(abs(v) for v in corr.values()) != sum(corr.values()),
            "negative-control-discard-correlation-signs")
    require(sum(v for h, v in corr.items() if h >= 0) != sum(corr.values()),
            "negative-control-drop-one-orientation")
    require(corr[0] != sum(corr.values()), "negative-control-diagonal-only")
    f, _ = local("two-channel", 6, 2, 0, "principal", set(), 21)
    require(f[7] != 0, "shared-prime-powers-retained")
    f, _ = local("geometric", 6, 2, 0, "principal", set(), 21)
    require(f[13] != 0 and f[19] != 0, "full-geometric-local-tail-retained")
    return {
        "status": "PASS_EXACT_FINITE_IDENTITIES",
        "coefficient_cases": 96,
        "integer_cap": 256,
        "covariance_cap": 48,
        "local_coefficient_degree": 20,
        "case_digest_sha256": digest.hexdigest(),
        "checks": dict(sorted(COUNTS.items())),
        "scope": {
            "floating_point_used": False,
            "profiles_checked": "real rational phases 0, +/-1, +/-1/2",
            "even_degrees_checked": [2, 4, 6],
            "complex_profiles_in_theorem": "covered analytically, not by this finite fixture",
            "davenport_proof_rebuilt": False,
            "asymptotic_or_infinite_product_verified_by_code": False,
            "rh_proved": False,
        },
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
