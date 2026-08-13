#!/usr/bin/env python3
"""Directed certificate for global positivity of the canonical P_61 finite-Euler row.

This script uses only the Python standard library.  It proves the finite gates
used in L-91364.  The analytic inequalities reducing the infinite problem to
these gates are stated and proved in the theorem file; this checker verifies
all finite constants, cells, and interval inequalities.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt, prod
from pathlib import Path
import json
import time

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
P61 = prod(PRIMES)
SCALE = 10**26
LOG_TERMS = 72
FINITE_ROW_MAX = 510
ASYMPTOTIC_ROW_MIN = FINITE_ROW_MAX + 1
QUOTIENT_SPLIT = 67


def floor_fraction_scaled(x: Fraction) -> int:
    return (x.numerator * SCALE) // x.denominator


def ceil_fraction_scaled(x: Fraction) -> int:
    return -((-x.numerator * SCALE) // x.denominator)


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


Interval = tuple[int, int]


def iadd(a: Interval, b: Interval) -> Interval:
    return a[0] + b[0], a[1] + b[1]


def ineg(a: Interval) -> Interval:
    return -a[1], -a[0]


def isub(a: Interval, b: Interval) -> Interval:
    return iadd(a, ineg(b))


def imul(a: Interval, b: Interval) -> Interval:
    products = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(products) // SCALE, ceil_div(max(products), SCALE)


def ifraction(x: Fraction) -> Interval:
    return floor_fraction_scaled(x), ceil_fraction_scaled(x)


def iinteger(x: int) -> Interval:
    return x * SCALE, x * SCALE


def iscale(a: Interval, x: Fraction) -> Interval:
    if x >= 0:
        return (
            (a[0] * x.numerator) // x.denominator,
            ceil_div(a[1] * x.numerator, x.denominator),
        )
    return ineg(iscale(a, -x))


def ireciprocal(a: Interval) -> Interval:
    assert a[0] > 0
    return (SCALE * SCALE) // a[1], ceil_div(SCALE * SCALE, a[0])


def idiv(a: Interval, b: Interval) -> Interval:
    return imul(a, ireciprocal(b))


def isqrt_integer(n: int) -> Interval:
    q = n * SCALE * SCALE
    lo = isqrt(q)
    hi = lo if lo * lo == q else lo + 1
    return lo, hi


def ilog_fraction(x: Fraction) -> Interval:
    assert x > 0
    exponent = 0
    y = x
    while y >= 2:
        y /= 2
        exponent += 1
    while y < 1:
        y *= 2
        exponent -= 1

    def base(z: Fraction) -> tuple[Fraction, Fraction]:
        z2 = z * z
        power = z
        partial = Fraction(0)
        for k in range(LOG_TERMS):
            partial += power / Fraction(2 * k + 1)
            power *= z2
        partial *= 2
        tail = 2 * power / (Fraction(2 * LOG_TERMS + 1) * (1 - z2))
        return partial, partial + tail

    lo, hi = base((y - 1) / (y + 1))
    log2_lo, log2_hi = base(Fraction(1, 3))
    if exponent >= 0:
        lo += exponent * log2_lo
        hi += exponent * log2_hi
    else:
        lo += exponent * log2_hi
        hi += exponent * log2_lo
    return floor_fraction_scaled(lo), ceil_fraction_scaled(hi)


def ilog_integer(n: int) -> Interval:
    return ilog_fraction(Fraction(n))


def ilog_successive_ratio(n: int) -> Interval:
    z = Fraction(1, 2 * n + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for k in range(LOG_TERMS):
        partial += power / Fraction(2 * k + 1)
        power *= z2
        tail = 2 * power / (Fraction(2 * k + 3) * (1 - z2))
        if tail * SCALE < Fraction(1, 4):
            break
    lower = 2 * partial
    upper = lower + tail
    return floor_fraction_scaled(lower), ceil_fraction_scaled(upper)


def interval_abs_upper(a: Interval) -> int:
    return max(abs(a[0]), abs(a[1]))


@dataclass(frozen=True)
class DivisorEntry:
    value: int
    mu: int
    sqrt: Interval
    invsqrt: Interval
    log: Interval
    invsqrt_log: Interval


def build_divisors() -> list[DivisorEntry]:
    prime_logs = {p: ilog_integer(p) for p in PRIMES}
    raw: list[tuple[int, int, int, int]] = [(1, 1, 0, 0)]
    for p in PRIMES:
        lp = prime_logs[p]
        raw += [(d * p, -mu, lo + lp[0], hi + lp[1]) for d, mu, lo, hi in list(raw)]
    raw.sort()
    entries = []
    for d, mu, lo, hi in raw:
        sq = isqrt_integer(d)
        inv = ireciprocal(sq)
        lg = (lo, hi)
        entries.append(DivisorEntry(d, mu, sq, inv, lg, imul(inv, lg)))
    assert len(entries) == 2**18
    return entries


def eval_F(a_num: int, b: Interval, c: Interval, sq: Interval, lg: Interval) -> Interval:
    term1 = iscale(sq, Fraction(8 * a_num, P61))
    coef = iadd(iinteger(7), iscale(lg, Fraction(3, 2)))
    return iadd(isub(term1, imul(coef, b)), iscale(c, Fraction(3, 2)))


def eval_H(a_num: int, b: Interval, c: Interval, sq: Interval, lg: Interval) -> Interval:
    return isub(eval_F(a_num, b, c, sq, lg), iscale(sq, Fraction(3, 4)))


def derivative_numerator(a_num: int, b: Interval, sq: Interval, subtract: Fraction) -> Interval:
    return isub(iscale(sq, Fraction(8 * a_num, P61) - subtract), iscale(b, Fraction(3)))


def certify_asymptotic_profile(entries: list[DivisorEntry]) -> dict:
    cache = {e.value: (e.sqrt, e.log) for e in entries}
    cache[2] = isqrt_integer(2), ilog_integer(2)
    cache[67] = isqrt_integer(67), ilog_integer(67)
    a_num = 0
    b = (0, 0)
    c = (0, 0)
    compact_min = None
    global_min = None
    compact_checks = global_checks = stationary_exclusions = 0
    for index, entry in enumerate(entries):
        a_num += entry.mu * (P61 // entry.value)
        b = iadd(b, iscale(entry.invsqrt, Fraction(entry.mu)))
        c = iadd(c, iscale(entry.invsqrt_log, Fraction(entry.mu)))
        nxt = entries[index + 1].value if index + 1 < len(entries) else None
        if entry.value < 67:
            left = max(entry.value, 2)
            right = min(nxt if nxt is not None else 67, 67)
            if left <= right:
                for u in {left, right}:
                    val = eval_F(a_num, b, c, *cache[u])
                    rec = (val[0], u, entry.value)
                    if compact_min is None or rec[0] < compact_min[0]: compact_min = rec
                    compact_checks += 1
                c0 = Fraction(8 * a_num, P61)
                if c0 > 0:
                    assert not (b[0] <= 0 <= b[1])
                    if b[0] > 0:
                        dl = derivative_numerator(a_num, b, cache[left][0], Fraction(0))
                        dr = derivative_numerator(a_num, b, cache[right][0], Fraction(0))
                        assert dl[0] >= 0 or dr[1] <= 0
                        stationary_exclusions += 1
        if nxt is not None and nxt >= 67:
            left, right = max(entry.value, 67), nxt
            for u in {left, right}:
                val = eval_H(a_num, b, c, *cache[u])
                rec = (val[0], u, entry.value)
                if global_min is None or rec[0] < global_min[0]: global_min = rec
                global_checks += 1
            c0 = Fraction(8 * a_num, P61) - Fraction(3, 4)
            if c0 > 0:
                assert not (b[0] <= 0 <= b[1])
                if b[0] > 0:
                    dl = derivative_numerator(a_num, b, cache[left][0], Fraction(3, 4))
                    dr = derivative_numerator(a_num, b, cache[right][0], Fraction(3, 4))
                    assert dl[0] >= 0 or dr[1] <= 0
                    stationary_exclusions += 1
    last = entries[-1]
    assert derivative_numerator(a_num, b, last.sqrt, Fraction(3, 4))[0] > 0
    val = eval_H(a_num, b, c, last.sqrt, last.log)
    if global_min is None or val[0] < global_min[0]: global_min = (val[0], last.value, last.value)
    global_checks += 1
    assert compact_min[0] > ceil_fraction_scaled(Fraction(5, 2))
    assert global_min[0] > ceil_fraction_scaled(Fraction(3, 20))
    return {
        "compact_endpoint_checks": compact_checks,
        "global_endpoint_checks": global_checks,
        "stationary_minimum_exclusions": stationary_exclusions,
        "compact_F_minimum_lower": compact_min[0] / SCALE,
        "compact_F_minimum_u": compact_min[1],
        "compact_F_minimum_cell_start": compact_min[2],
        "global_F_minus_3over4_sqrt_minimum_lower": global_min[0] / SCALE,
        "global_minimum_u": global_min[1],
        "global_minimum_cell_start": global_min[2],
    }


def certify_corridors(entries: list[DivisorEntry]) -> dict:
    total_sqrt = compact_sqrt = (0, 0)
    total_rec = compact_rec = Fraction(0)
    positive = []
    for e in entries:
        total_sqrt = iadd(total_sqrt, e.invsqrt)
        total_rec += Fraction(1, e.value)
        if e.value <= 67:
            compact_sqrt = iadd(compact_sqrt, e.invsqrt)
            compact_rec += Fraction(1, e.value)
        if e.mu == 1: positive.append((e.value, e.invsqrt))
    assert total_sqrt[1] < 60 * SCALE and total_rec < 5
    assert compact_sqrt[1] < 10 * SCALE and compact_rec < 4
    left = 0
    compact_best = (0, None, [])
    global_best = (0, None, [])
    for right, (d, _) in enumerate(positive):
        while left <= right and positive[left][0] * 512 <= d * 511: left += 1
        window = positive[left:right + 1]
        upper = sum(x[1][1] for x in window)
        if 2 <= d <= 67 and upper > compact_best[0]: compact_best = (upper, d, [x[0] for x in window])
        if d >= 67:
            subwindow = [x for x in window if x[0] >= 67]
            upper2 = sum(x[1][1] for x in subwindow)
            if upper2 > global_best[0]: global_best = (upper2, d, [x[0] for x in subwindow])
    assert compact_best[0] < floor_fraction_scaled(Fraction(5, 12))
    assert global_best[0] < floor_fraction_scaled(Fraction(1, 8))
    sqrt_ratio = idiv(isqrt_integer(512), isqrt_integer(511))
    q = isub(isub(iscale(sqrt_ratio, Fraction(8)), iinteger(7)), iscale(ilog_fraction(Fraction(512, 511)), Fraction(3, 2)))
    assert q[1] < floor_fraction_scaled(Fraction(101, 100))
    compact_margin = Fraction(5, 2) - Fraction(624, 510) - Fraction(101, 240)
    global_margin = Fraction(3, 4) - Fraction(310, 510) - Fraction(1, 32)
    assert compact_margin == Fraction(3491, 4080) > 0
    assert global_margin == Fraction(181, 1632) > 0
    return {
        "total_abs_sqrt_divisor_mass_upper": total_sqrt[1] / SCALE,
        "total_abs_reciprocal_divisor_mass": str(total_rec),
        "compact_abs_sqrt_divisor_mass_upper": compact_sqrt[1] / SCALE,
        "compact_abs_reciprocal_divisor_mass": str(compact_rec),
        "compact_activation_strip_upper": compact_best[0] / SCALE,
        "compact_activation_strip_at": compact_best[1],
        "compact_activation_strip_divisors": compact_best[2],
        "global_activation_strip_upper": global_best[0] / SCALE,
        "global_activation_strip_at": global_best[1],
        "global_activation_strip_divisors": global_best[2],
        "q_512_over_511_upper": q[1] / SCALE,
        "large_row_compact_margin": str(compact_margin),
        "large_row_global_margin": str(global_margin),
    }


def precompute(maximum: int):
    inv = [None] * (maximum + 1)
    logs = [None] * (maximum + 1)
    ratios = [None] * (maximum + 1)
    logs[1] = (0, 0)
    for n in range(1, maximum + 1):
        inv[n] = ireciprocal(isqrt_integer(n))
        if n < maximum:
            ratios[n] = ilog_successive_ratio(n)
            logs[n + 1] = iadd(logs[n], ratios[n])
    return inv, logs, ratios


def certify_finite_rows(entries, inv, ratios):
    small = [(e.value, e.mu) for e in entries if e.value <= 67]
    checks = 0
    minimum = None
    for j in range(2, FINITE_ROW_MAX + 1):
        top = 67 * j
        coeff = [0] * (top + 1)
        for d, mu in small:
            mmax = top // d
            if mmax < j: continue
            coeff[d * j] += mu * j * (j + 1)
            if j + 1 <= mmax: coeff[d * (j + 1)] += -mu * (j + 1) * (j - 2)
            for m in range(j + 2, mmax + 1): coeff[d * m] += 2 * mu
        value = slope = (0, 0)
        for n in range(j, top):
            if coeff[n]: slope = iadd(slope, iscale(inv[n], Fraction(coeff[n])))
            nxt = iadd(value, imul(slope, ratios[n]))
            assert value[0] >= 0 and nxt[0] >= 0
            if n + 1 >= 2 * j:
                rec = (nxt[0], j, n + 1)
                if minimum is None or rec[0] < minimum[0]: minimum = rec
            value = nxt
            checks += 1
    return {
        "finite_row_maximum_j": FINITE_ROW_MAX,
        "finite_compact_interval_checks": checks,
        "minimum_positive_scaled_row_lower": minimum[0] / SCALE,
        "minimum_positive_scaled_row_j": minimum[1],
        "minimum_positive_scaled_row_X": minimum[2],
        "scaled_row_definition": "j(j-1) D_(P61,X)(j)",
    }


def boundary_weights(j, inv):
    c = Fraction(2, j * (j - 1))
    result = [(m, iscale(inv[m], -c)) for m in range(1, j)]
    result.append((j, iscale(inv[j], Fraction(j + 2, j))))
    result.append((j + 1, ineg(inv[j + 1])))
    return result


def kantorovich_upper(j, inv, logs):
    weights = boundary_weights(j, inv)
    total = moment = (0, 0)
    for m, w in weights:
        total = iadd(total, w)
        moment = iadd(moment, imul(w, logs[m]))
    ordered = sorted(weights, key=lambda x: -x[0])
    mids = [(m, (w[0] + w[1]) / (2 * SCALE)) for m, w in ordered]
    s = sum(w for _, w in mids)
    from math import log
    cumul = []
    gaps = []
    run = 0.0
    for i, (m, w) in enumerate(mids):
        run += w
        cumul.append(run)
        if i + 1 < len(mids): gaps.append(log(m / mids[i + 1][0]))
    left = [0.0] * len(mids)
    run = 0.0
    for i in range(1, len(mids)):
        run += abs(cumul[i - 1]) * gaps[i - 1]
        left[i] = run
    right = [0.0] * len(mids)
    run = 0.0
    for i in range(len(mids) - 2, -1, -1):
        run += abs(cumul[i] - s) * gaps[i]
        right[i] = run
    anchor = min(range(len(mids)), key=lambda i: left[i] + right[i])
    others = (0, 0)
    for i, (_, w) in enumerate(ordered):
        if i != anchor: others = iadd(others, w)
    adjusted = [(m, ineg(others) if i == anchor else w) for i, (m, w) in enumerate(ordered)]
    cumulative = (0, 0)
    W = 0
    for i, (m, w) in enumerate(adjusted):
        cumulative = iadd(cumulative, w)
        if i + 1 < len(adjusted):
            gap = isub(logs[m], logs[adjusted[i + 1][0]])
            W += ceil_div(interval_abs_upper(cumulative) * gap[1], SCALE)
    return total, moment, W, anchor


def certify_green(entries, inv, logs):
    maximum = 67 * FINITE_ROW_MAX
    Apre = [(0, 0)] * (maximum + 1)
    Bpre = [(0, 0)] * (maximum + 1)
    A = B = (0, 0)
    for n in range(1, maximum + 1):
        if gcd(n, P61) == 1:
            A = iadd(A, inv[n])
            B = iadd(B, imul(inv[n], logs[n]))
        Apre[n], Bpre[n] = A, B
    beta = (SCALE, SCALE)
    for p in PRIMES: beta = imul(beta, isub((SCALE, SCALE), inv[p]))
    assert beta[0] > 0 and beta[1] < floor_fraction_scaled(Fraction(1, 400))
    minimum = None
    for j in range(2, FINITE_ROW_MAX + 1):
        c = Fraction(2, j * (j - 1))
        total, moment, W, anchor = kantorovich_upper(j, inv, logs)
        kappa = iadd(iscale(Apre[67 * j], c), imul(beta, total))
        assert kappa[0] > 0
        lower = imul(kappa, iadd(logs[67], logs[j]))
        lower = isub(lower, iscale(Bpre[67 * j], c))
        lower = isub(lower, imul(beta, moment))
        lower = isub(lower, (0, ceil_div(7 * interval_abs_upper(total), 6)))
        lower = isub(lower, (0, ceil_div(27 * W, 20)))
        assert lower[0] > 0
        rec = (lower[0], j, kappa[0], W, anchor)
        if minimum is None or rec[0] < minimum[0]: minimum = rec
    return {
        "finite_green_tail_rows": FINITE_ROW_MAX - 1,
        "green_tail_start": "X=67j",
        "minimum_green_tail_lower": minimum[0] / SCALE,
        "minimum_green_tail_j": minimum[1],
        "minimum_log_coefficient_lower": minimum[2] / SCALE,
        "wasserstein_upper_at_minimum": minimum[3] / SCALE,
        "anchor_index_at_minimum": minimum[4],
        "beta_61_lower": beta[0] / SCALE,
        "beta_61_upper": beta[1] / SCALE,
    }


def main():
    started = time.time()
    entries = build_divisors()
    asym = certify_asymptotic_profile(entries)
    corridors = certify_corridors(entries)
    inv, logs, ratios = precompute(67 * FINITE_ROW_MAX)
    finite = certify_finite_rows(entries, inv, ratios)
    green = certify_green(entries, inv, logs)
    result = {
        "classification": "PASS_P61_CANONICAL_FINITE_EULER_ROW_GLOBAL_POSITIVITY",
        "small_prime_block": PRIMES,
        "divisor_states": len(entries),
        "finite_row_cutoff": FINITE_ROW_MAX,
        "asymptotic_row_start": ASYMPTOTIC_ROW_MIN,
        "elapsed_seconds": time.time() - started,
        "asymptotic_profile": asym,
        "mass_and_activation_corridors": corridors,
        "finite_compact_rows": finite,
        "finite_green_tails": green,
        "scope": "The directed gates certify the finite inputs to L-91364. They do not audit the imported literal-entropy benchmark, endpoint-port normalization, CFFP, or RH.",
    }
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(out)


if __name__ == "__main__":
    main()
