"""Exact finite checks for the HLC transfer packet.

Standard library only. Arithmetic is rational, with exact pairs representing
Q(i). Logarithms of primes are formal commuting variables. These checks
validate finite identities and normalization, not an asymptotic estimate.
The character/projection example is a synthetic rational-field control,
not a finite computation of the Eisenstein family.
"""

from fractions import Fraction as F
from math import gcd, prod
from collections import defaultdict
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def factor(n):
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def mobius(n):
    ff = factor(n)
    return 0 if any(e > 1 for e in ff.values()) else (-1) ** len(ff)


def mul_poly(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for j, aj in enumerate(a):
        for k, bk in enumerate(b):
            out[j + k] += aj * bk
    return out


def derivative(a):
    return [F(j) * a[j] for j in range(1, len(a))] or [F(0)]


def evaluate(a, z):
    out = F(0)
    for aj in reversed(a):
        out = out * z + aj
    return out


def band_formula(primes, rho):
    pgf = [F(1)]
    for p in primes:
        theta = F(1, p - 1)
        pgf = mul_poly(pgf, [1 - theta, theta])
    first, second = derivative(pgf), derivative(derivative(pgf))
    v = sum((F(1, p) for p in primes), F(0))
    mean = evaluate(first, rho) / v
    ratio = (
        evaluate(first, rho * rho)
        + rho * rho * evaluate(second, rho * rho)
    ) / evaluate(first, rho) ** 2
    support = 1 - pgf[0]
    require(ratio >= 1 / support, "finite support lower bound")
    return mean, ratio


def crt_case(groups, rho):
    primes = [p for group in groups for band in group for p in band]
    require(len(primes) == len(set(primes)), "prime bands must be disjoint")
    modulus = prod(primes)
    means = []
    ratios = []
    for group in groups:
        entries = [band_formula(band, rho) for band in group]
        means.append(prod(m for m, _ in entries))
        ratios.append(prod(r for _, r in entries))
    count = 0
    direct_means = [F(0)] * len(groups)
    direct_variance = F(0)
    for a in range(modulus):
        if gcd(a, modulus) != 1:
            continue
        count += 1
        normalized = []
        for j, group in enumerate(groups):
            value = F(1)
            for band in group:
                number = sum((a + 2) % p == 0 for p in band)
                v = sum((F(1, p) for p in band), F(0))
                mark = F(0) if number == 0 else number * rho ** (number - 1) / v
                value *= mark
            direct_means[j] += value
            normalized.append(value / means[j])
        direct_variance += (sum(normalized, F(0)) / len(groups) - 1) ** 2
    direct_means = [v / count for v in direct_means]
    direct_variance /= count
    formula_variance = sum((r - 1 for r in ratios), F(0)) / len(groups) ** 2
    require(direct_means == means, "CRT means differ from generating polynomial")
    require(direct_variance == formula_variance, "CRT variance identity failed")
    return {
        "modulus": modulus, "reduced_residues": count, "rho": str(rho),
        "groups": groups, "variance": str(direct_variance),
    }


def check_mobius_prime_identities(limit):
    for n in range(1, limit + 1):
        ff = factor(n)
        mu = mobius(n)
        for p, exponent in ff.items():
            target = mu * exponent
            prime_only = -mobius(n // p) if gcd(n // p, p) == 1 else 0
            prime_powers = -sum(mobius(n // (p ** j)) for j in range(1, exponent + 1))
            require(prime_only == target, "coprime prime identity")
            require(prime_powers == target, "prime-power identity")
    # A required failure: without coprimality, p^2 creates a false term.
    require(-mobius(2) != mobius(4) * 2, "negative control did not fail")
    # Formal log-prime coefficients of sum Lambda(n) mu(n) equal -theta(x).
    coefficients = defaultdict(int)
    for n in range(2, limit + 1):
        ff = factor(n)
        if len(ff) == 1:
            coefficients[next(iter(ff))] += mobius(n)
    require(all(v == -1 for v in coefficients.values()), "zero-shift identity")
    return {"integers_checked": limit, "prime_log_coefficients": len(coefficients)}


ZERO = (F(0), F(0))
ONE = (F(1), F(0))
I = (F(0), F(1))


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def scale(z, a):
    return z[0] * a, z[1] * a


def conjugate(z):
    return z[0], -z[1]


def multiply(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def power(z, k):
    value = ONE
    for _ in range(k):
        value = multiply(value, z)
    return value


def inner_linear_first(a, b):
    out = ZERO
    for z, w in zip(a, b):
        out = add(out, multiply(z, conjugate(w)))
    return out


def character(n, row):
    if n % 5 == 0 or n % 7 == 0:
        return ZERO
    base = {1: ONE, 2: I, 4: (-F(1), F(0)), 3: (F(0), -F(1))}[n % 5]
    return power(base, row)


SQRT_WEIGHTS = [F(1), F(2), F(1, 2), F(3, 2)]
FRAME = [ONE, I, (F(1), F(1)), (F(2), -F(1))]
FRAME_NORM = inner_linear_first(FRAME, FRAME)[0]


def column(n, projected):
    vector = [scale(character(n, r), w) for r, w in enumerate(SQRT_WEIGHTS)]
    if not projected:
        return vector
    coefficient = scale(inner_linear_first(vector, FRAME), 1 / FRAME_NORM)
    return [add(z, scale(multiply(v, coefficient), -1)) for z, v in zip(vector, FRAME)]


def add_log_product(poly, a_logs, b_logs, coefficient):
    for p, ep in a_logs.items():
        for q, eq in b_logs.items():
            key = tuple(sorted((p, q)))
            poly[key] = add(poly.get(key, ZERO), scale(coefficient, ep * eq))
            if poly[key] == ZERO:
                del poly[key]


def finite_native_control(D, projected):
    # Choose V(n/D)=R(n/D)*log n. Its prime logarithms remain formal.
    numbers = list(range(D + 1, 2 * D))
    profile = {n: F((n - D) ** 2 * (2 * D - n) ** 2, D ** 4) for n in numbers}
    columns = {n: column(n, projected) for n in numbers}
    kernel = {(n, m): inner_linear_first(columns[n], columns[m])
              for n in numbers for m in numbers}
    moment, diagonal, affine = {}, {}, {}
    for n in numbers:
        raw_norm = inner_linear_first(column(n, False), column(n, False))[0]
        require(0 <= kernel[n, n][0] <= raw_norm, "projection diagonal contraction")
        for m in numbers:
            c = scale(kernel[n, m], F(mobius(n) * mobius(m), D) * profile[n] * profile[m])
            add_log_product(moment, factor(n), factor(m), c)
            if n == m:
                add_log_product(diagonal, factor(n), factor(m), c)
    primes = [p for p in range(2, 2 * D) if factor(p) == {p: 1}]
    triple_count = 0
    # Independently enumerate (a,p,h); do not reuse square expansion.
    for a in range(1, D):
        for p in primes:
            n = a * p
            if n not in profile or gcd(a, p) != 1:
                continue
            for row in range(4):
                require(multiply(character(a, row), character(p, row)) == character(n, row),
                        "character multiplicativity with natural zeros")
            for h in range(-D, D + 1):
                m = n + h
                if h == 0 or m not in profile:
                    continue
                triple_count += 1
                c = scale(kernel[n, m], F(mobius(a) * mobius(m), D) * profile[n] * profile[m])
                add_log_product(affine, {p: 1}, factor(m), c)
    all_keys = set(moment) | set(diagonal) | set(affine)
    for key in all_keys:
        residual = add(add(moment.get(key, ZERO), scale(diagonal.get(key, ZERO), -1)),
                       affine.get(key, ZERO))
        require(residual == ZERO, "I = diagonal - affine/(D log D)")
        require(moment.get(key, ZERO)[1] == 0, "Hermitian moment must be real")
        require(affine.get(key, ZERO)[1] == 0, "complete affine sum must be real")
    require(bool(moment), "synthetic moment should not be vacuous")
    return {"D": D, "projected": projected, "affine_triples": triple_count,
            "formal_log_monomials": len(all_keys)}


def main():
    crt = [
        crt_case([[[3, 5, 7]]], F(1, 2)),
        crt_case([[[3, 5]], [[7, 11]]], F(2, 3)),
        crt_case([[[3, 5], [7]], [[11], [13]]], F(1, 2)),
    ]
    arithmetic = check_mobius_prime_identities(2000)
    controls = [finite_native_control(D, projected)
                for D in (10, 17, 23) for projected in (False, True)]
    b, theta, alpha = F(7, 8), F(49, 50), F(1, 2)
    recurrence = [b]
    for _ in range(3):
        b = max(alpha, 2 * b + 1 - 2 * theta)
        recurrence.append(b)
    require(recurrence == [F(7, 8), F(79, 100), F(31, 50), F(1, 2)],
            "exact conditional recurrence")
    print(json.dumps({
        "status": "PASS", "scope": "finite identities only; no asymptotic bound",
        "arithmetic": "EXACT_RATIONAL with formal prime logarithms",
        "crt_cases": crt, "mobius_checks": arithmetic,
        "synthetic_native_controls": controls,
        "conditional_recurrence": [str(v) for v in recurrence],
    }, indent=2))


if __name__ == "__main__":
    main()
