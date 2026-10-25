"""Exact finite checks for ROOT_COUNT_REFINEMENT.md.

These tests cover finite congruences, gcd and normalization ledgers.
The Fourier bounds and asymptotic estimates are proved in the note;
they are not inferred from finite experiments.  No floating point or
assert statements are used.  The checks remain active under python -O.
"""

from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import gcd, prod
import json


COUNTS = Counter()


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def phi(n):
    return sum(gcd(a, n) == 1 for a in range(n))


def prime_divisors(n):
    ans = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            ans.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        ans.append(n)
    return ans


def squarefree(n):
    return all(n % (p * p) for p in prime_divisors(n))


def normalized_completion(u, v):
    require(u >= 2 and v >= 2 and gcd(u, v) == 1, "valid primitive root")
    c = -pow(v, -1, u) % u
    d = (1 + v * c) // u
    require(u * d - v * c == 1 and 0 <= c < u, "normalized completion")
    return u, c, v, d


def fourth_moment_combinatorics():
    for m in range(2, 33):
        units = [y for y in range(m) if gcd(y, m) == 1]
        inv = {y: pow(y, -1, m) for y in units}
        pair_classes = Counter(((y + z) % m, (inv[y] + inv[z]) % m)
                               for y, z in product(units, repeat=2))
        tm = sum(n * n for n in pair_classes.values())
        triple_count = 0
        images = Counter()
        for y1, y2, z1 in product(units, repeat=3):
            z2 = (y1 + y2 - z1) % m
            if z2 not in inv:
                continue
            inverse_equal = (inv[y1] + inv[y2] - inv[z1] - inv[z2]) % m == 0
            factors = ((y1 + y2) % m, (z1 - y1) % m, (z1 - y2) % m)
            require(inverse_equal == (prod(factors) % m == 0),
                    "unit inverse equation equals three-factor divisibility")
            if inverse_equal:
                triple_count += 1
                images[factors] += 1
            COUNTS["unit_quadruple_eliminations"] += 1
        require(triple_count == tm, "fourth-moment zero-frequency count")
        require(max(images.values(), default=0) <= 2, "linear-map kernel at most two")
        ordered_factors = [(d1, d2, m // (d1 * d2))
                           for d1 in divisors(m) for d2 in divisors(m // d1)]
        require(tm <= 2 * m * m * len(ordered_factors), "elementary fourth-moment majorant")
        for h, k in product(range(m), repeat=2):
            orbit = {(h * s % m, k * inv[s] % m) for s in units}
            require(len(orbit) == phi(m // gcd(gcd(h, k), m)), "exact unit orbit cardinality")
            hist = Counter((h * y + k * inv[y]) % m for y in units)
            # Check the exact change of variable at every unit s, including
            # frequencies with gcd and the pair (0,0).
            for s in units:
                orbit_hist = Counter(((h * s) * y + (k * inv[s]) * inv[y]) % m
                                     for y in units)
                require(hist == orbit_hist, "Kloosterman unit-orbit phase histogram")
                COUNTS["unit_orbit_phase_checks"] += 1
            COUNTS["unit_orbit_cardinalities"] += 1
        COUNTS["fourth_moment_moduli"] += 1


def congruences_and_all_frequencies():
    moduli = [1, 2, 3, 5, 6, 7, 10, 15, 21, 30]
    wrong_gcd_control = False
    for ss in moduli:
        require(squarefree(ss), "squarefree prescribed modulus")
        for u in range(2, 20):
            # Use distinct actual matrix classes so every datum is valid.
            matrices = {tuple(x % ss for x in normalized_completion(u, v))
                        for v in range(2, 20) if gcd(u, v) == 1}
            for u0, c0, v0, d0 in matrices:
                s1, s2 = gcd(u, ss), ss // gcd(u, ss)
                mm, nn = u * s1, s2
                nn_inv = pow(nn, -1, mm)
                mm_inv = pow(mm, -1, nn) if nn > 1 else 0
                cc = u * d0 - 1
                require(gcd(cc, mm) == gcd(nn, mm) == 1, "CRT unit coefficients")
                actual = set()
                for t in range(u):
                    c = c0 + ss * t
                    if gcd(c, u) != 1:
                        continue
                    numerator = cc - c * v0
                    require(numerator % ss == 0, "matrix congruence implies integral lift")
                    jv = (numerator // ss) * pow(c, -1, u) % u
                    v = v0 + ss * jv
                    require((c * v - cc) % (u * ss) == 0, "literal R_u congruence")
                    actual.add((c, v))
                expected_size = F(u)
                for p in prime_divisors(u):
                    if ss % p:
                        expected_size *= F(p - 1, p)
                require(len(actual) == expected_size, "exact zero frequency cardinality")

                reconstructed = set()
                for y in range(mm):
                    if gcd(y, mm) != 1 or (y - c0) % s1:
                        continue
                    vy = cc * pow(y, -1, mm) % mm
                    c = (y * nn * nn_inv + (c0 % nn) * mm * mm_inv) % (u * ss)
                    v = (vy * nn * nn_inv + (v0 % nn) * mm * mm_inv) % (u * ss)
                    reconstructed.add((c, v))
                    for h, k in ((0, 0), (1, 0), (0, -1), (u, 2 * u), (-2 * u, u), (1, -1)):
                        phase = (nn * nn_inv * (h * y + k * vy)
                                 + mm * mm_inv * (h * (c0 % nn) + k * (v0 % nn)))
                        require((h * c + k * v - phase) % (u * ss) == 0,
                                "exact CRT Fourier phase")
                        COUNTS["CRT_fourier_phase_checks"] += 1
                require(actual == reconstructed, "exact CRT parametrization of R_u")

                freqs = (-2 * u, -u, -1, 0, 1, u, 2 * u, 3 * u + 1)
                for h, k in product(freqs, repeat=2):
                    for j in range(s1):
                        lhs = gcd(gcd(nn_inv * h + j * u, nn_inv * k * cc), mm)
                        base = gcd(gcd(h, k), u)
                        require(lhs <= s1 * base, "all-frequency gcd inequality")
                        wrong_gcd_control |= lhs > base
                        if (h, k) != (0, 0):
                            ds = [d for d in divisors(u) if h % d == k % d == 0]
                            require(base in ds, "positive divisor majorant contains exact gcd")
                        COUNTS["all_frequency_gcd_checks"] += 1
                COUNTS["fixed_u_congruence_cases"] += 1
    require(wrong_gcd_control, "cannot discard s1 in fixed-u Fourier estimate")
    COUNTS["negative_controls"] += 1


def progression_gcd_ledger():
    scales = [F(a) for a in range(2, 61)] + [F(5, 2), F(17, 3), F(43, 7)]
    for aa in scales:
        low = -(-aa.numerator // aa.denominator)
        high = (16 * aa).numerator // (16 * aa).denominator
        for ss in range(1, 81):
            if not squarefree(ss):
                continue
            for u0 in range(ss):
                first = low + (u0 - low) % ss
                count = 0 if first > high else (high - first) // ss + 1
                dd = gcd(u0, ss)
                require(count <= 15 * aa / ss + 1, "progression cardinality with endpoints")
                if count:
                    require(dd <= 16 * aa and dd <= ss, "nonempty progression controls its fixed gcd")
                    require(all(gcd(first + j * ss, ss) == dd for j in range(count)),
                            "modulus gcd is constant along progression")
                require(count * dd <= 31 * aa, "summed gcd loses no modulus factor")
                COUNTS["progression_gcd_cases"] += 1


def completion_involution():
    for u, v in product(range(2, 65), repeat=2):
        if gcd(u, v) != 1:
            continue
        _, c, _, d = normalized_completion(u, v)
        swapped = (v, v - d, u, u - c)
        require(swapped == normalized_completion(v, u), "normalized scale-swap matrix")
        require(F(v - d, v) == 1 - F(c, u) - F(1, u * v), "exact scale-swap root-ratio correction")
        require((u, u - (u - c), v, v - (v - d)) == (u, c, v, d), "scale swap is involutive")
        for ss in (1, 2, 3, 6, 10, 15):
            require((v * (u - c) - u * (v - d)) % ss == 1 % ss,
                    "scale swap preserves matrix congruence determinant")
            COUNTS["scale_swap_moduli"] += 1
        COUNTS["scale_swap_completions"] += 1


def line_of_kernel(a, b, p):
    # A kernel vector is (b,-a); normalize its first nonzero coordinate.
    x, y = b % p, -a % p
    require(x or y, "nonzero row defines a projective line")
    return (1, y * pow(x, -1, p) % p) if x else (0, 1)


def matrix_and_line_cardinalities():
    for ss in (1, 2, 3, 5, 6, 10):
        count = sum((u * d - v * c) % ss == 1 % ss
                    for u, c, v, d in product(range(ss), repeat=4))
        expected = prod(p * (p * p - 1) for p in prime_divisors(ss))
        require(count == expected, "SL2 squarefree cardinality")
        COUNTS["matrix_cardinality_moduli"] += 1
    matrices2 = [g for g in product(range(2), repeat=4)
                 if (g[0] * g[3] - g[2] * g[1]) % 2 == 1]
    require(sum(u == v == 1 for u, c, v, d in matrices2) == 2, "two odd-column classes at two")
    for p in (3, 5, 7, 11, 13):
        by_line = Counter()
        for u, c, v, d in product(range(p), repeat=4):
            if (u * d - v * c) % p != 1:
                continue
            by_line[line_of_kernel(u, -2 * c, p)] += 1
        require(len(by_line) == p + 1, "projective line cardinality")
        require(all(n == p * (p - 1) for n in by_line.values()), "actual classes per prescribed line")
        require(F(p * (p - 1), p * (p * p - 1)) == F(1, p + 1), "once-only local line probability")
        COUNTS["local_line_cardinality_checks"] += len(by_line)
    for ss in (1, 3, 5, 7, 15, 21, 35, 105):
        allowed = 2 * prod(p * (p - 1) for p in prime_divisors(ss))
        total = 6 * prod(p * (p * p - 1) for p in prime_divisors(ss))
        require(allowed <= 2 * ss * ss, "line-class discrepancy uses S squared")
        require(F(allowed, total) == F(1, 3) * prod(F(1, p + 1) for p in prime_divisors(ss)),
                "full parity and projective-line density")
        COUNTS["CRT_line_normalizations"] += 1


def harmonic_progressions_and_budgets():
    for length in range(1, 45):
        harmonic = sum((F(1, n) for n in range(1, length + 1)), F(0))
        for dd in range(1, 65):
            direct = sum((F(1, abs(n)) for n in range(-length, length + 1)
                          if n and n % dd == 0), F(0))
            factored = F(2, dd) * sum((F(1, n) for n in range(1, length // dd + 1)), F(0))
            require(direct == factored <= F(2, dd) * harmonic,
                    "nonzero Fourier progression carries reciprocal d")
            COUNTS["harmonic_progression_checks"] += 1
    for kappa, jj, delta in product((F(3, 4), F(1, 2)), range(1, 9), (F(1, 4), F(1, 2))):
        beta = F(1, 800)
        direct = (jj + 3) * beta + (jj + 1) * beta + 2 * (jj + 3) * beta - (1 - kappa) * delta
        require(direct == (4 * jj + 10) * beta - (1 - kappa) * delta, "exact refined triangle error budget")
        COUNTS["triangle_exponent_budgets"] += 1
        common = (jj + 4) * beta + (jj + 1) * beta + 2 * (jj + 4) * beta - (1 - kappa) * delta
        require(common == (4 * jj + 13) * beta - (1 - kappa) * delta,
                "exact both-endpoint-list common-D budget")
        COUNTS["common_D_exponent_budgets"] += 1
    require(14 * F(1, 800) - F(1, 16) == -F(9, 200), "elementary printed band budget")
    require(14 * F(1, 800) - F(1, 8) == -F(43, 400), "classical printed band budget")
    require(14 * F(1, 400) - F(1, 16) == -F(11, 400), "stronger elementary band budget")
    require(14 * F(1, 400) - F(1, 8) == -F(9, 100), "stronger classical band budget")
    require(17 * F(1, 400) - F(1, 16) == -F(1, 50), "full common-D elementary band budget")
    require(17 * F(1, 400) - F(1, 8) == -F(33, 400), "full common-D classical band budget")
    require(F(1, 800) < F(1, 50) < F(33, 400), "main common-D power is the limiting example term")
    # Both Fourier axes are actual nonzero modes. Treating them as the
    # double-nonzero sum would omit their one-dimensional contributions.
    require(gcd(gcd(0, 6), 12) == 6, "Fourier-axis gcd is not the zero mode")
    require(F(2, 5) != F(2, 25), "axis progression has one reciprocal divisor")
    COUNTS["negative_controls"] += 2
    COUNTS["explicit_triangle_examples"] += 6


def main():
    fourth_moment_combinatorics()
    congruences_and_all_frequencies()
    progression_gcd_ledger()
    completion_involution()
    matrix_and_line_cardinalities()
    harmonic_progressions_and_budgets()
    print(json.dumps({
        "status": "PASS: exact finite identities; analytic estimates are proved in the note",
        "counts": dict(sorted(COUNTS.items())),
        "scope": "root counting and the stated fixed-depth raw triangle; no full HLC or zero-free claim",
    }, indent=2))


if __name__ == "__main__":
    main()
