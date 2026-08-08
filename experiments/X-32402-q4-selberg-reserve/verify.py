#!/usr/bin/env python3
"""
Exact interval replay for L-32405/L-32407 (Q=4 balanced reserve and physical transference).

Standard library only. All transcendental quantities are enclosed by
Fraction-based atanh series and then converted to fixed-point integer intervals.

The script verifies every balanced row
    4 <= n <= 4734,
    ceil(n/4) <= j <= floor(n/2),
the other half following by j <-> n-j symmetry.
"""
from fractions import Fraction
import hashlib
import json
import math

N = 4734
SCALE = 10**24
TERMS = 55


def floor_fraction(x):
    return x.numerator // x.denominator


def ceil_fraction(x):
    return -((-x.numerator) // x.denominator)


def atanh_log_interval(y):
    """Return exact Fraction bounds for log(y), 1 <= y < 2."""
    x = (y - 1) / (y + 1)
    x2 = x * x
    term = x
    total = Fraction(0)
    for r in range(TERMS):
        total += term / (2 * r + 1)
        term *= x2
    lo = 2 * total
    rem = 2 * term / ((2 * TERMS + 1) * (1 - x2))
    return lo, lo + rem


LOG2_LO, LOG2_HI = atanh_log_interval(Fraction(2, 1))


def log_integer_scaled(n):
    """Rigorous fixed-point interval for natural log(n)."""
    if n == 1:
        return 0, 0
    k = n.bit_length() - 1
    y = Fraction(n, 1 << k)
    lo_y, hi_y = atanh_log_interval(y)
    lo = k * LOG2_LO + lo_y
    hi = k * LOG2_HI + hi_y
    return floor_fraction(lo * SCALE), ceil_fraction(hi * SCALE)


def sieve_spf(limit):
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(limit) + 1):
        if spf[p] == p:
            for m in range(p * p, limit + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


SPF = sieve_spf(N)
PRIMES = [p for p in range(2, N + 1) if SPF[p] == p]
LOG_INTERVAL = {p: log_integer_scaled(p) for p in PRIMES}


def prime_power_representation(n):
    p = SPF[n]
    m = n
    exponent = 0
    while m % p == 0:
        m //= p
        exponent += 1
    if m != 1:
        return None
    return p, exponent


def mul_lo(a, b):
    return (a * b) // SCALE


def mul_hi(a, b):
    return (a * b + SCALE - 1) // SCALE


# Lambda_4(n) = Lambda(n) + log(4) sum_r (4^r-1) 1_{n=4^r}.
lam_lo = [0] * (N + 1)
lam_hi = [0] * (N + 1)

for p in PRIMES:
    lo, hi = LOG_INTERVAL[p]
    q = p
    while q <= N:
        lam_lo[q] += lo
        lam_hi[q] += hi
        if q > N // p:
            break
        q *= p

log2_lo, log2_hi = LOG_INTERVAL[2]
q = 4
while q <= N:
    coeff = 2 * (q - 1)  # log(4)*(q-1) = 2(q-1) log 2
    lam_lo[q] += coeff * log2_lo
    lam_hi[q] += coeff * log2_hi
    if q > N // 4:
        break
    q *= 4

lambda_support = [n for n in range(2, N + 1) if lam_hi[n] != 0]

# C_4 = Lambda_4 log + Lambda_4 * Lambda_4.
C_lo = [0] * (N + 1)
C_hi = [0] * (N + 1)

for n in lambda_support:
    rep = prime_power_representation(n)
    if rep is None:
        raise AssertionError(("lambda support is not a prime power", n))
    p, exponent = rep
    lp_lo, lp_hi = LOG_INTERVAL[p]
    ln_lo = exponent * lp_lo
    ln_hi = exponent * lp_hi
    C_lo[n] += mul_lo(lam_lo[n], ln_lo)
    C_hi[n] += mul_hi(lam_hi[n], ln_hi)

for a in lambda_support:
    for b in lambda_support:
        product = a * b
        if product > N:
            break
        C_lo[product] += mul_lo(lam_lo[a], lam_lo[b])
        C_hi[product] += mul_hi(lam_hi[a], lam_hi[b])

# Physical current coefficients c_4 = e_4 * Lambda_4, where
# e_4(1)=1 and e_4(4^r)=-3.
phys_lo = [0] * (N + 1)
phys_hi = [0] * (N + 1)
for n in range(2, N + 1):
    lo = lam_lo[n]
    hi = lam_hi[n]
    q = 4
    while q <= n:
        if n % q == 0:
            lo -= 3 * lam_hi[n // q]
            hi -= 3 * lam_lo[n // q]
        if q > n // 4:
            break
        q *= 4
    phys_lo[n] = lo
    phys_hi[n] = hi

# Floor/carry primitives:
# sum_q f(q) floor(M/q) = sum_{m<=M} sum_{q|m} f(q).
def cumulative_floor_intervals(coeff_lo, coeff_hi):
    divisor_lo = [0] * (N + 1)
    divisor_hi = [0] * (N + 1)
    for d in range(2, N + 1):
        if coeff_lo[d] == 0 and coeff_hi[d] == 0:
            continue
        for m in range(d, N + 1, d):
            divisor_lo[m] += coeff_lo[d]
            divisor_hi[m] += coeff_hi[d]
    prefix_lo = [0] * (N + 1)
    prefix_hi = [0] * (N + 1)
    for m in range(1, N + 1):
        prefix_lo[m] = prefix_lo[m - 1] + divisor_lo[m]
        prefix_hi[m] = prefix_hi[m - 1] + divisor_hi[m]
    return prefix_lo, prefix_hi


PREF1_LO, PREF1_HI = cumulative_floor_intervals(lam_lo, lam_hi)
PREF2_LO, PREF2_HI = cumulative_floor_intervals(C_lo, C_hi)
PHYS_LO, PHYS_HI = cumulative_floor_intervals(phys_lo, phys_hi)

rows = 0
minimum_margin = None
minimum_row = None
maximum_physical_ratio = Fraction(0)
maximum_physical_row = None

for n in range(4, N + 1):
    for j in range((n + 3) // 4, n // 2 + 1):
        k = n - j
        P_lo = PREF1_LO[n] - PREF1_HI[j] - PREF1_HI[k]
        S_hi = PREF2_HI[n] - PREF2_LO[j] - PREF2_LO[k]
        margin = P_lo * P_lo - S_hi * SCALE
        rows += 1
        if P_lo <= 0 or margin <= 0:
            raise AssertionError(
                ("balanced reserve failure", n, j, P_lo, S_hi, margin)
            )
        if minimum_margin is None or margin < minimum_margin:
            minimum_margin = margin
            minimum_row = (n, j, P_lo, S_hi)

        Q_lo = PHYS_LO[n] - PHYS_HI[j] - PHYS_HI[k]
        Q_hi = PHYS_HI[n] - PHYS_LO[j] - PHYS_LO[k]
        Q_abs = max(abs(Q_lo), abs(Q_hi))
        if Q_abs * Q_abs > 4 * margin:
            raise AssertionError(
                ("physical transference failure", n, j, Q_lo, Q_hi, margin)
            )
        ratio = Fraction(Q_abs * Q_abs, margin)
        if ratio > maximum_physical_ratio:
            maximum_physical_ratio = ratio
            maximum_physical_row = (n, j)

# Rational gates used by the analytic tail proof.
assert Fraction(69, 100) < LOG2_LO
assert LOG2_HI < Fraction(1733, 2500)

log4735_lo, log4735_hi = log_integer_scaled(4735)
assert log4735_hi < Fraction(847, 100) * SCALE

ratio_upper = (
    Fraction(240)
    * Fraction(847, 100)
    / (Fraction(4735) * Fraction(69, 100) ** 2)
)
assert ratio_upper == Fraction(1355200, 1502889)
assert ratio_upper < Fraction(19, 20)

result = {
    "classification": "PASS_EXACT_Q4_BALANCED_SELBERG_KUMMER_RESERVE",
    "finite_endpoint": N,
    "balanced_rows": rows,
    "scale": SCALE,
    "atanh_terms": TERMS,
    "minimum_row": [minimum_row[0], minimum_row[1]],
    "minimum_margin_scaled_square": minimum_margin,
    "tail_ratio_upper": [ratio_upper.numerator, ratio_upper.denominator],
    "physical_transference_finite_constant": 4,
    "maximum_physical_ratio_row": [
        maximum_physical_row[0], maximum_physical_row[1]
    ],
    "maximum_physical_ratio_interval_upper": [
        maximum_physical_ratio.numerator, maximum_physical_ratio.denominator
    ],
}
payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
result["result_sha256"] = hashlib.sha256(payload).hexdigest()

print(json.dumps(result, indent=2, sort_keys=True))
