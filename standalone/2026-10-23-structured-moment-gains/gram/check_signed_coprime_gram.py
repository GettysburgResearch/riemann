#!/usr/bin/env python3
"""Exact finite diagnostics for SIGNED_COPRIME_GRAM.md.

This checks local arithmetic and an informative exponent comparison. It is
not a numerical proof of a uniform analytic estimate or a zero-free region.
Only Python's standard library is used. All character arithmetic is exact in
Z[zeta_6], with zeta_6^2=zeta_6-1; no floating-point tolerances occur.
"""

from fractions import Fraction as F


ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
ZERO = (0, 0)
ONE = (1, 0)


def demand(condition, context):
    if not condition:
        raise AssertionError(context)


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c + b * d


def scale(z, n):
    return n * z[0], n * z[1]


def norm_squared(z):
    return z[0] ** 2 + z[0] * z[1] + z[1] ** 2


def sextic_logs(p):
    """Discrete logs of nonzero elements of the prime field, modulo six."""
    demand(p % 12 == 1, ("source-compatible residue norm", p))
    for g in range(2, p):
        orbit = [pow(g, k, p) for k in range(p - 1)]
        if len(set(orbit)) == p - 1:
            return {x: k % 6 for k, x in enumerate(orbit)}
    raise AssertionError("Prime field has no generator")


def valuation(n, p):
    if n == 0:
        return None
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def field_lift_correlation(p, i, h, frequency, logs):
    """Sum the character values over the actual final residue equation.

    Division by the common p-power leaves p^(min(i,h)-1) lifts for
    each final-digit solution. The character sum is enumerated directly;
    its value is not supplied by the proposed case table.
    """
    c = min(i, h)
    if frequency % (p ** c):
        return ZERO
    k = (frequency // (p ** c)) % p
    ax = 1 if h == c else 0
    ay = 1 if i == c else 0
    answer = ZERO
    for x in range(1, p):
        for y in range(1, p):
            if (ax * x - ay * y - k) % p == 0:
                answer = add(answer, ROOTS[(i * logs[x] - h * logs[y]) % 6])
    return scale(answer, p ** (c - 1))


def raw_correlation(p, i, h, frequency, logs):
    """Enumerate the original congruence modulo p^i and p^h.

    For each x there is at most one y with
    p^h*x-p^i*y = frequency mod p^(i+h).
    This separately checks the last-digit/lift reduction at small powers.
    """
    u, v = p ** i, p ** h
    answer = ZERO
    for x in range(u):
        if not x % p:
            continue
        numerator = v * x - frequency
        if numerator % u:
            continue
        y = (numerator // u) % v
        if not y % p:
            continue
        answer = add(answer, ROOTS[(i * logs[x % p] - h * logs[y % p]) % 6])
    return answer


def expected_magnitude(p, i, h, frequency):
    c = min(i, h)
    t = valuation(frequency, p)
    if t is not None and t < c:
        return 0
    if i == h:
        if t is None or t > c:
            return p ** (c - 1) * (p - 1)
        return p ** (c - 1) * ((p - 2) if c % 6 == 0 else 1)
    return p ** (c - 1) * (p - 1) if c % 6 == 0 and t == c else 0


def check_correlations():
    field_cases = 0
    raw_cases = 0
    coverage = {"nonprincipal_equal": 0, "principal_equal": 0,
                "unequal_left": 0, "unequal_right": 0, "zero": 0}
    for p in (13, 37):
        logs = sextic_logs(p)
        for i in range(1, 15):
            for h in range(1, 15):
                c = min(i, h)
                # Distinct unit frequencies test phases, not only valuations.
                frequencies = {0, 1, p ** (c - 1), p ** c,
                               2 * p ** c, p ** (c + 1)}
                for frequency in frequencies:
                    actual = field_lift_correlation(p, i, h, frequency, logs)
                    expected = expected_magnitude(p, i, h, frequency)
                    demand(norm_squared(actual) == expected ** 2,
                           (p, i, h, frequency, actual, expected))
                    field_cases += 1
                    if not expected:
                        coverage["zero"] += 1
                    elif i == h:
                        key = "principal_equal" if i % 6 == 0 else "nonprincipal_equal"
                        coverage[key] += 1
                    else:
                        coverage["unequal_left" if i > h else "unequal_right"] += 1
                    if max(i, h) <= 2:
                        demand(raw_correlation(p, i, h, frequency, logs) == actual,
                               ("original-modulus mismatch", p, i, h, frequency))
                        raw_cases += 1
    demand(all(coverage.values()), ("missing local branch", coverage))
    return field_cases, raw_cases, coverage


def polynomial_product(a, b, cutoff):
    result = {}
    for (i, j), z in a.items():
        for (k, ell), w in b.items():
            if i + k <= cutoff and j + ell <= cutoff:
                key = i + k, j + ell
                result[key] = add(result.get(key, ZERO), mul(z, w))
    return {k: z for k, z in result.items() if z != ZERO}


def check_euler_masks():
    cutoff = 5
    unit = {(0, 0): ONE}
    numerator = {(0, 0): ONE, (1, 1): (-1, 0)}
    inverse_numerator = {(k, k): ONE for k in range(cutoff + 1)}
    cases = 0
    for character_power in range(6):
        l1 = {(i, 0): ROOTS[(character_power * i) % 6]
              for i in range(cutoff + 1)}
        l2 = {(0, j): ROOTS[(-character_power * j) % 6]
              for j in range(cutoff + 1)}
        coprime_factor = polynomial_product(
            polynomial_product(l1, l2, cutoff), numerator, cutoff)
        expected = {(i, 0): z for (i, _), z in l1.items()}
        expected.update({(0, j): z for (_, j), z in l2.items()})
        demand(coprime_factor == expected, ("coprime Euler factor", character_power))

        remove1 = {(0, 0): ONE,
                   (1, 0): scale(ROOTS[character_power], -1)}
        remove2 = {(0, 0): ONE,
                   (0, 1): scale(ROOTS[-character_power % 6], -1)}
        deleted = polynomial_product(coprime_factor, remove1, cutoff)
        deleted = polynomial_product(deleted, remove2, cutoff)
        # Omitting the extra reciprocal finite factor would leave 1-XY.
        demand(deleted == numerator and deleted != unit,
               ("uncorrected deleted prime", character_power))
        corrected = polynomial_product(deleted, inverse_numerator, cutoff)
        demand(corrected == unit, ("corrected deleted prime", character_power))
        cases += 1
    return cases


def informative_exponent_case():
    # A physical point excluded by the old additive restriction, with
    # a known common boundary beta=7/8. This compares direct exponents;
    # it does not verify the distinct high-side closure inequalities.
    beta, ell, b = F(7, 8), F(1, 6), F(2, 5)
    lx, ly = (1 - ell - b) / 2, (1 - ell + b) / 2
    demand(lx > ell and ell <= F(1, 5) and b >= 0, "physical inequalities")
    principal = b / 6
    old_np = 2 * b - ly
    new_np = (1 + beta / 2) * b - (2 - beta) * ly
    central_np = b - ly
    demand(old_np > principal > new_np, "nonprincipal term changes regime")
    demand(central_np < 0, "central term absorbed")
    old_direct = lx / 2 + max(F(0), principal, old_np) / 2
    new_direct = lx / 2 + principal / 2
    demand((old_direct, new_direct) == (F(1, 5), F(17, 120)), "direct exponents")
    demand(old_direct - new_direct == F(7, 120), "direct exponent gain")
    return {"ell": ell, "b": b, "lx": lx, "ly": ly,
            "old_nonprincipal": old_np, "principal": principal,
            "new_nonprincipal": new_np, "central_nonprincipal": central_np,
            "old_direct": old_direct, "new_direct": new_direct,
            "direct_gain": old_direct - new_direct}


def main():
    field_cases, raw_cases, coverage = check_correlations()
    mask_cases = check_euler_masks()
    exponents = informative_exponent_case()
    print("Exact sextic final-digit correlations:", field_cases, "passed")
    print("Independent original-modulus enumerations:", raw_cases, "passed")
    print("Local branch coverage:", coverage)
    print("Coprime Euler factors and deleted-prime corrections:", mask_cases, "passed")
    print("Physical direct-exponent comparison:")
    for key, value in exponents.items():
        print(f"  {key}: {value}")
    print("Finite checks passed. Analytic implications remain dependent on the stated source inputs.")


if __name__ == "__main__":
    main()
