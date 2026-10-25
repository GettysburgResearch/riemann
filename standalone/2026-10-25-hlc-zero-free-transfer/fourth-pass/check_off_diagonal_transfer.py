"""Exact finite checks for OFF_DIAGONAL_TRANSFER.md.

The model uses actual primary Eisenstein ideals, sextic symbols and
natural zeros.  Completely additive positive rational prime weights
replace logarithms, so the prime extraction and mean identity can be
checked with exact arithmetic.  Finite cutoffs are rational surrogates
for the smooth cutoffs: these checks prove no asymptotic estimate.
Every check remains active under python -O.
"""

from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json
import math


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


ZERO = (F(0), F(0))
ONE = (1, 0)


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def sub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def mul(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c - b * d)


def scale(z, a):
    return (z[0] * a, z[1] * a)


def conj(z):
    return (z[0] - z[1], -z[1])


def norm(z):
    a, b = z
    return a * a - a * b + b * b


def div(z, w):
    num = mul(z, conj(w))
    q = norm(w)
    if num[0] % q or num[1] % q:
        return None
    return (num[0] // q, num[1] // q)


def powe(z, e):
    r = ONE
    while e:
        if e & 1:
            r = mul(r, z)
        z = mul(z, z)
        e //= 2
    return r


NMAX = 230
bound = int(2 * math.sqrt(NMAX)) + 1
IDEALS = sorted(
    [(a, b) for a in range(-bound, bound + 1)
     for b in range(-bound, bound + 1)
     if a % 3 == 1 and b % 3 == 0
     and 1 <= norm((a, b)) <= NMAX
     and math.gcd(norm((a, b)), 6) == 1],
    key=lambda z: (norm(z), z),
)
PRIMES = []
FAC = {}
MU = {}
for n in IDEALS:
    if n == ONE:
        FAC[n] = {}
        MU[n] = 1
        continue
    rem = n
    ff = {}
    for p in PRIMES:
        if norm(p) > norm(rem):
            break
        while (q := div(rem, p)) is not None:
            ff[p] = ff.get(p, 0) + 1
            rem = q
    if rem != ONE:
        require(rem == n, "unlisted proper prime divisor")
        PRIMES.append(n)
        ff[n] = 1
    FAC[n] = ff
    MU[n] = 0 if any(e > 1 for e in ff.values()) else (-1) ** len(ff)


@lru_cache(None)
def divisors(n):
    ans = [ONE]
    for p, e in FAC[n].items():
        ans = [mul(d, powe(p, j)) for d in ans for j in range(e + 1)]
    return tuple(sorted(ans, key=lambda z: (norm(z), z)))


def gcd_ideal(a, b):
    out = ONE
    for p, e in FAC[a].items():
        out = mul(out, powe(p, min(e, FAC[b].get(p, 0))))
    return out


UNITS = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1)]


@lru_cache(None)
def symbol_prime(u, p):
    if div(u, p) is not None:
        return ZERO
    q = norm(p)
    require((q - 1) % 6 == 0, "sextic residue cardinality")
    v = powe(u, (q - 1) // 6)
    found = [r for r in UNITS if div(sub(v, r), p) is not None]
    require(len(found) == 1, "unique sixth root in residue field")
    return found[0]


PUNCTURE = (4, 3)  # A primary prime of norm 13.
require(PUNCTURE in PRIMES, "puncture is an actual prime ideal")


def phase_from_factors(u, factors, orientation=1):
    if factors.get(PUNCTURE, 0):
        return ZERO
    ans = ONE
    for p, e in factors.items():
        ans = mul(ans, powe(symbol_prime(u, p), e))
    return ans if orientation == 1 else conj(ans)


@lru_cache(None)
def psi(u, n, orientation=1):
    return phase_from_factors(u, FAC[n], orientation)


ROWS = [u for u in IDEALS if 7 <= norm(u) <= 49]
require(any(MU[u] == 0 for u in ROWS), "nonsquarefree physical row retained")
ROW_WEIGHTS = {u: F(5 + j, 5) for j, u in enumerate(ROWS)}


@lru_cache(None)
def kernel(n, m, orientation):
    out = ZERO
    for u in ROWS:
        out = add(out, scale(mul(psi(u, n, orientation),
                                 conj(psi(u, m, orientation))),
                             ROW_WEIGHTS[u]))
    return out


def cutoff(x):
    if x <= 1:
        return F(1)
    if x >= 2:
        return F(0)
    return 2 - x


def profile(n, D):
    y = F(norm(n), D)
    if not 1 < y < 2:
        return ZERO
    v = 4 * (y - 1) * (2 - y)
    return (v, v * y / 7)


PRIME_WEIGHT = {p: F(j + 2) for j, p in enumerate(PRIMES)}


def ell(n):
    return sum((e * PRIME_WEIGHT[p] for p, e in FAC[n].items()), F(0))


prime_identity_cases = 0
bad_coprimality_observed = False
for b in IDEALS:
    rhs = F(0)
    wrong = F(0)
    for p in FAC[b]:
        d = div(b, p)
        wrong -= MU[d] * PRIME_WEIGHT[p]
        if div(d, p) is None:
            rhs -= MU[d] * PRIME_WEIGHT[p]
    require(MU[b] * ell(b) == rhs, "prime-only additive identity")
    bad_coprimality_observed |= wrong != rhs
    prime_identity_cases += 1
require(bad_coprimality_observed, "coprimality negative control")


def finite_case(Y1, Y2, BLO, BHI, D, orientation):
    require(BLO >= 2 * Y1, "long extracted factor exceeds one")
    cols = [n for n in IDEALS if D < norm(n) < 2 * D]

    def xi(m):
        return cutoff(F(norm(m), BHI)) - cutoff(F(norm(m), BLO))

    def inverse_weight(a, b):
        return cutoff(F(norm(a), Y1)) * cutoff(F(norm(b), Y2))

    def coeff(m):
        return sum((MU[a] * MU[div(m, a)] * inverse_weight(a, div(m, a))
                    for a in divisors(m)), F(0))

    lam = {}
    expanded = {}
    repeated_m = set()
    for n in cols:
        lam[n] = sum((coeff(m) * xi(m) for m in divisors(n)), F(0))
        expanded[n] = []
        for m in divisors(n):
            x = xi(m)
            if not x:
                continue
            c = div(n, m)
            for a in divisors(m):
                b = div(m, a)
                wt = inverse_weight(a, b) * x
                if wt and MU[a] and MU[b]:
                    require(norm(b) > 1, "actual long factor is not the unit")
                    expanded[n].append((m, c, a, b, wt))
                    if MU[m] == 0:
                        repeated_m.add(m)
        collected = sum((MU[a] * MU[b] * wt
                         for m, c, a, b, wt in expanded[n]), F(0))
        require(collected == lam[n], "full-column coefficient collection")

    mean = F(0)
    for u in ROWS:
        s = ZERO
        for n in cols:
            s = add(s, scale(mul(psi(u, n, orientation), profile(n, D)), lam[n]))
        mean += ROW_WEIGHTS[u] * norm(s) / D
    diagonal = sum((lam[n] ** 2 * norm(profile(n, D)) * kernel(n, n, orientation)[0]
                    for n in cols), F(0)) / D
    require(all(kernel(n, n, orientation)[1] == 0 for n in cols),
            "natural-zero diagonal is real")
    require(mean > 0, "nonempty finite mean")

    reference = F(7)
    extracted = ZERO
    wrong_short_signs = ZERO
    reversed_mean = ZERO
    terms = determinant_cases = phase_cases = nontrivial_content = 0
    gcd_mask_control = False
    determinant_control = False
    active_cols = [n for n in cols if expanded[n]]
    for n1 in active_cols:
        for n2 in active_cols:
            vprod = mul(profile(n1, D), conj(profile(n2, D)))
            reversed_mean = add(reversed_mean,
                scale(mul(vprod, kernel(n2, n1, orientation)),
                      lam[n1] * lam[n2] / D))
            if n1 == n2:
                continue
            h = sub(n1, n2)
            require(h != ZERO and h[0] % 3 == h[1] % 3 == 0,
                    "nonzero primary-lattice shift")
            require(norm(h) <= 8 * D, "determinant norm range")
            for m1, c1, a1, b1, wt1 in expanded[n1]:
                for m2, c2, a2, b2, wt2 in expanded[n2]:
                    require(sub(mul(m1, c1), mul(m2, c2)) == h,
                            "crossed-coordinate determinant")
                    g = gcd_ideal(m1, c2)
                    l = gcd_ideal(m2, c1)
                    p01, p02 = div(m1, g), div(c2, g)
                    q01, q02 = div(m2, l), div(c1, l)
                    require(gcd_ideal(p01, p02) == gcd_ideal(q01, q02) == ONE,
                            "primitive endpoint quotients")
                    det0 = sub(mul(p01, q02), mul(q01, p02))
                    content = mul(g, l)
                    require(mul(content, det0) == h, "two-content determinant")
                    require(norm(n1) == norm(content) * norm(p01) * norm(q02),
                            "first cross-profile scale")
                    require(norm(n2) == norm(content) * norm(q01) * norm(p02),
                            "second cross-profile scale")
                    determinant_cases += 1
                    if content != ONE:
                        nontrivial_content += 1
                        determinant_control |= det0 != h
                    for u in ROWS:
                        original = mul(psi(u, n1, orientation),
                                       conj(psi(u, n2, orientation)))
                        endpoints = mul(
                            mul(psi(u, m1, orientation), conj(psi(u, c2, orientation))),
                            conj(mul(psi(u, m2, orientation), conj(psi(u, c1, orientation)))))
                        reduced = mul(psi(u, mul(p01, q02), orientation),
                                      conj(psi(u, mul(q01, p02), orientation)))
                        mask = norm(psi(u, g, orientation)) * norm(psi(u, l, orientation))
                        require(mask in (0, 1), "natural content mask is zero or one")
                        require(original == endpoints == scale(reduced, mask),
                                "conjugate endpoint and masked primitive phases")
                        gcd_mask_control |= original != reduced
                        phase_cases += 1
                    for p in FAC[b1]:
                        d = div(b1, p)
                        if div(d, p) is not None:
                            continue
                        A0 = mul(mul(a1, d), c1)
                        B0 = mul(a2, c2)
                        require(sub(mul(A0, p), mul(B0, b2)) == h,
                                "exact affine prime equation")
                        require(div(sub(mul(A0, p), h), B0) == b2,
                                "integral primary affine quotient")
                        phase = kernel(n1, n2, orientation)
                        for u in ROWS:
                            affine = mul(
                                mul(psi(u, A0, orientation), conj(psi(u, B0, orientation))),
                                mul(psi(u, p, orientation), conj(psi(u, b2, orientation))))
                            require(affine == mul(psi(u, n1, orientation),
                                                 conj(psi(u, n2, orientation))),
                                    "affine phase with natural zeros")
                        wt = (PRIME_WEIGHT[p] * reference / ell(b1)
                              * wt1 * wt2 * MU[d] * MU[b2])
                        term = scale(mul(vprod, phase), wt)
                        extracted = add(extracted, scale(term, MU[a1] * MU[a2]))
                        wrong_short_signs = add(wrong_short_signs, term)
                        terms += 1
    require(extracted[1] == 0, "complete extracted sum is real")
    require(mean == diagonal - extracted[0] / (D * reference),
            "signed extracted mean normalization")
    require(reversed_mean[1] == 0, "reversed complete mean is real")

    # Dropping repeated-prime m allocations changes the actual coefficient.
    repeated_control = any(
        lam[n] != sum((coeff(m) * xi(m) for m in divisors(n) if MU[m]), F(0))
        for n in cols)
    return {
        "parameters": [Y1, Y2, BLO, BHI, D, orientation],
        "columns": len(cols), "active_columns": len(active_cols),
        "prime_extracted_summands": terms, "determinant_cases": determinant_cases,
        "natural_phase_cases": phase_cases, "nontrivial_contents": nontrivial_content,
        "repeated_prime_m": len(repeated_m),
        "mean": str(mean), "diagonal": str(diagonal),
        "negative_controls": {
            "short_mobius_signs": wrong_short_signs != extracted,
            "conjugate_kernel": reversed_mean[0] != mean,
            "repeated_prime_m": repeated_control,
            "gcd_natural_mask": gcd_mask_control,
            "determinant_content": determinant_control,
            "overall_prime_sign": extracted != ZERO,
        },
    }


CASES = [finite_case(*args) for args in [
    (4, 40, 14, 30, 30, 1),
    (4, 40, 14, 30, 30, -1),
    (8, 110, 20, 70, 90, 1),
    (8, 110, 20, 70, 90, -1),
]]
for control in CASES[0]["negative_controls"]:
    require(any(case["negative_controls"][control] for case in CASES),
            "negative control was observable: " + control)


# A separate corpus contains genuine unequal sixth-power-resonant ideals,
# which do not occur below NMAX.  Its prime factors are still actual ideals.
small_primes = [p for p in PRIMES if norm(p) == 7]
require(len(small_primes) == 2, "two conjugate primes above seven")
p, q = small_primes
resonant_corpus = []
for e, f in product(range(13), repeat=2):
    factors = {z: k for z, k in [(p, e), (q, f)] if k}
    n = mul(powe(p, e), powe(q, f))
    core = mul(powe(p, e % 6), powe(q, f % 6))
    power = mul(powe(p, e // 6), powe(q, f // 6))
    require(n == mul(core, powe(power, 6)), "unique sixth-core factorization")
    resonant_corpus.append((n, core, factors))

resonance_pair_cases = 0
unequal_resonance_pairs = 0
natural_core_zero_control = False
for level in range(1, 16):
    target_norm = 7 ** level
    annulus = [(n, core, factors) for n, core, factors in resonant_corpus
               if target_norm - 1 < norm(n) < 2 * (target_norm - 1)]
    groups = defaultdict(list)
    for n, core, factors in annulus:
        groups[core].append((n, factors))
    pair_count = sum(len(items) ** 2 for items in groups.values())
    direct_count = sum(core1 == core2 for _, core1, _ in annulus
                       for _, core2, _ in annulus)
    require(pair_count == direct_count, "complete equal-core pair ledger")
    row_sum = F(0)
    pair_sum = ZERO
    for u in ROWS:
        for core, items in groups.items():
            s = ZERO
            for j, (n, factors) in enumerate(items):
                coefficient = F(j + 1, len(items) + 1)
                value = phase_from_factors(u, factors)
                core_factors = {z: e % 6 for z, e in factors.items() if e % 6}
                natural_core_zero_control |= value != phase_from_factors(u, core_factors)
                s = add(s, scale(value, coefficient))
            row_sum += ROW_WEIGHTS[u] * norm(s)
            for j, (n1, f1) in enumerate(items):
                for k, (n2, f2) in enumerate(items):
                    coefficient = F((j + 1) * (k + 1), (len(items) + 1) ** 2)
                    pair_sum = add(pair_sum, scale(
                        mul(phase_from_factors(u, f1), conj(phase_from_factors(u, f2))),
                        ROW_WEIGHTS[u] * coefficient))
                    unequal_resonance_pairs += n1 != n2
                    resonance_pair_cases += 1
    require(pair_sum == (row_sum, 0) and row_sum >= 0,
            "whole resonance is a nonnegative block-square sum")
    require(row_sum <= sum(ROW_WEIGHTS.values()) * pair_count,
            "bounded coefficients and natural masks give pair-count bound")
require(unequal_resonance_pairs > 0, "non-pair-diagonal resonance is present")
require(natural_core_zero_control, "sixth-power natural-zero negative control")


print(json.dumps({
    "status": "PASS: exact finite identities only; HLC-thin remains unproved",
    "primary_ideals": len(IDEALS), "prime_ideals": len(PRIMES),
    "physical_rows": len(ROWS), "prime_identity_cases": prime_identity_cases,
    "core_factorizations": len(resonant_corpus),
    "resonance_pair_cases": resonance_pair_cases,
    "unequal_resonance_pair_cases": unequal_resonance_pairs,
    "core_zero_negative_control": natural_core_zero_control,
    "coprimality_negative_control": bad_coprimality_observed,
    "finite_cases": CASES,
}, indent=2))
