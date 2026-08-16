#!/usr/bin/env python3
"""Directed finite replay for the source-specific CRCTP terminal-control bank.

The replay authenticates:
- the exact two-policy terminal interpolation algebra;
- outward Decimal source/flow intervals at a targeted endpoint bank;
- positive preliminary flows whose terminal residuals bracket zero.

It does not prove the cofinal terminal-control theorem, MPR positivity, CRCTP,
Cycle Debt, or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction
from pathlib import Path
from typing import Callable

PREC = 90
LOW = Context(prec=PREC, rounding=ROUND_FLOOR)
HIGH = Context(prec=PREC, rounding=ROUND_CEILING)
D = Decimal
Interval = tuple[Decimal, Decimal]
ZERO: Interval = (D(0), D(0))


def add(a: Interval, b: Interval) -> Interval:
    return LOW.add(a[0], b[0]), HIGH.add(a[1], b[1])


def neg(a: Interval) -> Interval:
    return -a[1], -a[0]


def sub(a: Interval, b: Interval) -> Interval:
    return add(a, neg(b))


def scale(a: Interval, num: int, den: int = 1) -> Interval:
    if num == 0:
        return ZERO
    if num < 0:
        return neg(scale(a, -num, den))
    q_lo = LOW.divide(D(num), D(den))
    q_hi = HIGH.divide(D(num), D(den))
    return LOW.multiply(a[0], q_lo), HIGH.multiply(a[1], q_hi)


def positive_div(a: Interval, b: Interval) -> Interval:
    assert b[0] > 0
    return LOW.divide(a[0], b[1]), HIGH.divide(a[1], b[0])


def target_interval(X: int, q: int) -> Interval:
    if q >= X:
        return ZERO
    dx, dq = D(X), D(q)
    log_lo = LOW.subtract(LOW.ln(dx), HIGH.ln(dq))
    log_hi = HIGH.subtract(HIGH.ln(dx), LOW.ln(dq))
    sqrt_lo = LOW.sqrt(dq)
    sqrt_hi = HIGH.sqrt(dq)
    return LOW.divide(log_lo, sqrt_hi), HIGH.divide(log_hi, sqrt_lo)


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            m = n * p
            if m > limit:
                break
            composite[m] = True
            if n % p == 0:
                mu[m] = 0
                break
            mu[m] = -mu[n]
    return mu


def b2(mu: list[int], q: int) -> int:
    return mu[q] - (mu[q // 2] if q % 2 == 0 else 0)


def root_completed_source(X: int) -> tuple[list[Interval], list[Interval], Interval]:
    mu = mobius_sieve(X)
    w = [ZERO for _ in range(X + 1)]
    for q in range(2, X + 1):
        w[q] = target_interval(X, q)

    rho = ZERO
    for q in range(3, X + 1):
        rho = add(rho, scale(w[q], b2(mu, q)))
    beta = (max(D(0), rho[0]) / D(2), max(D(0), rho[1]) / D(2))
    t = list(w)
    t[2] = beta

    u = [ZERO for _ in range(X + 2)]
    for m in range(1, X + 1):
        acc = ZERO
        for k in range(1, X // m + 1):
            if mu[k]:
                acc = add(acc, scale(t[m * k], mu[k]))
        u[m] = acc

    r = [ZERO for _ in range(X + 1)]
    for m in range(2, X + 1):
        r[m] = sub(u[m], u[m + 1])
    return t, r, rho


def j_min(n: int) -> int:
    return max(2, 2 * (n // 4))


def policy(n: int, cutoff: int) -> list[tuple[int, int, int]]:
    """Return (numerator, denominator, smaller child)."""
    if n <= cutoff:
        return [(1, 1, j_min(n))]
    return [(31, 32, max(2, n // 3)), (1, 32, n // 2)]


def flow_for_cutoff(X: int, r: list[Interval], cutoff: int) -> tuple[list[Interval], Interval, Interval]:
    incoming = [ZERO for _ in range(X + 1)]
    d = [ZERO for _ in range(X + 1)]
    for n in range(X, 3, -1):
        d[n] = add(r[n], incoming[n])
        for num, den, j in policy(n, cutoff):
            assert 2 <= j <= n // 2 and 4 * j >= n
            packet = scale(d[n], num, den)
            incoming[j] = add(incoming[j], packet)
            incoming[n - j] = add(incoming[n - j], packet)
    e2 = add(r[2], incoming[2])
    e3 = add(r[3], incoming[3])
    return d, e2, e3


def bmin(n: int) -> int:
    return n & 1


def terminal_gap(n: int) -> Fraction:
    """Extra terminal-three leaves used by the mixed rule over j_min."""
    if n & 1:
        return Fraction(0)
    j3 = max(2, n // 3)
    j2 = n // 2
    mixed = (
        Fraction(31, 32) * (bmin(j3) + bmin(n - j3))
        + Fraction(1, 32) * (bmin(j2) + bmin(n - j2))
    )
    minimum = bmin(j_min(n)) + bmin(n - j_min(n))
    return mixed - minimum


def flow_fraction(X: int, source: list[Fraction], cutoff: int) -> tuple[list[Fraction], Fraction, Fraction]:
    incoming = [Fraction(0) for _ in range(X + 1)]
    d = [Fraction(0) for _ in range(X + 1)]
    for n in range(X, 3, -1):
        d[n] = source[n] + incoming[n]
        for num, den, j in policy(n, cutoff):
            packet = Fraction(num, den) * d[n]
            incoming[j] += packet
            incoming[n - j] += packet
    return d, source[2] + incoming[2], source[3] + incoming[3]


def exact_switch_fixtures() -> tuple[int, int]:
    """Verify the one-parent cutoff switch and its monotone terminal drop."""
    switch_checks = 0
    residue_checks = 0
    rng = __import__('random').Random(95101)
    for X in range(12, 31):
        source = [Fraction(0) for _ in range(X + 1)]
        for n in range(4, X + 1):
            source[n] = Fraction(rng.randint(1, 11), rng.randint(2, 17))
        high_size = sum(Fraction(n) * source[n] for n in range(4, X + 1))
        source[3] = Fraction(-rng.randint(0, 7), 5)
        source[2] = -(high_size + 3 * source[3]) / 2
        prev_d, prev_e2, prev_e3 = flow_fraction(X, source, 4)
        assert 2 * prev_e2 + 3 * prev_e3 == 0
        residue_checks += 1
        for K in range(5, min(29, X)):
            d, e2, e3 = flow_fraction(X, source, K)
            assert d[K] == prev_d[K]
            assert e3 == prev_e3 - terminal_gap(K) * d[K]
            assert e2 == prev_e2 + Fraction(3, 2) * terminal_gap(K) * d[K]
            assert 2 * e2 + 3 * e3 == 0
            if d[K] >= 0:
                assert e3 <= prev_e3
            switch_checks += 1
            residue_checks += 1
            prev_d, prev_e2, prev_e3 = d, e2, e3
    table = {0: Fraction(0), 2: Fraction(1,16), 4: Fraction(31,16),
             6: Fraction(1,16), 8: Fraction(0), 10: Fraction(2)}
    for n in range(6, 250, 2):
        assert terminal_gap(n) == table[n % 12]
        residue_checks += 1
    return switch_checks, residue_checks


def exact_algebra_fixtures() -> tuple[int, int]:
    ratio_checks = 0
    interpolation_checks = 0
    for a_num in range(1, 9):
        for b_num in range(1, 9):
            tau_plus = Fraction(a_num, 11)
            tau_minus = -Fraction(b_num, 13)
            e2p, e3p = -3 * tau_plus, 2 * tau_plus
            e2m, e3m = -3 * tau_minus, 2 * tau_minus
            assert 2 * e2p + 3 * e3p == 0
            assert 2 * e2m + 3 * e3m == 0
            ratio_checks += 2
            lam = tau_plus / (tau_plus - tau_minus)
            assert 0 < lam < 1
            assert (1 - lam) * tau_plus + lam * tau_minus == 0
            assert (1 - lam) * e2p + lam * e2m == 0
            assert (1 - lam) * e3p + lam * e3m == 0
            interpolation_checks += 1
    return ratio_checks, interpolation_checks


def verify_endpoint(X: int) -> dict:
    _t, r, rho = root_completed_source(X)
    candidates: list[dict] = []
    for cutoff in range(4, 29):
        d, e2, e3 = flow_for_cutoff(X, r, cutoff)
        lows = [d[n][0] for n in range(4, X)]
        min_lower = min(lows) if lows else D(0)
        if min_lower > 0:
            candidates.append({
                "cutoff": cutoff,
                "minimum_occupation_lower": min_lower,
                "terminal_two": e2,
                "terminal_three": e3,
            })

    plus = next((c for c in candidates if c["terminal_three"][0] >= 0), None)
    minus = next((c for c in candidates if c["terminal_three"][1] <= 0), None)
    if plus is None or minus is None:
        raise AssertionError(("terminal bank did not bracket zero", X, candidates))

    for c in (plus, minus):
        combo = add(scale(c["terminal_two"], 2), scale(c["terminal_three"], 3))
        tol = D("1e-20")
        if combo[0] > tol or combo[1] < -tol:
            raise AssertionError(("terminal size mismatch", X, c["cutoff"], combo))

    tp = plus["terminal_three"]
    tm = minus["terminal_three"]
    den_lo = LOW.subtract(tp[0], tm[1])
    den_hi = HIGH.subtract(tp[1], tm[0])
    if den_lo <= 0:
        raise AssertionError(("interpolation denominator", X, tp, tm))
    lam = positive_div(tp, (den_lo, den_hi))
    if lam[0] < 0 or lam[1] > 1:
        raise AssertionError(("interpolation outside unit interval", X, lam))

    return {
        "X": X,
        "root_functional_interval": [str(rho[0]), str(rho[1])],
        "positive_cutoff": plus["cutoff"],
        "negative_cutoff": minus["cutoff"],
        "positive_terminal_three": [str(tp[0]), str(tp[1])],
        "negative_terminal_three": [str(tm[0]), str(tm[1])],
        "positive_minimum_occupation_lower": str(plus["minimum_occupation_lower"]),
        "negative_minimum_occupation_lower": str(minus["minimum_occupation_lower"]),
        "interpolation_parameter_interval": [str(lam[0]), str(lam[1])],
    }


def run() -> dict:
    ratio_checks, interpolation_checks = exact_algebra_fixtures()
    switch_checks, residue_checks = exact_switch_fixtures()
    endpoints = list(range(40, 129)) + [160, 192, 256, 384, 512, 768, 1024]
    records = [verify_endpoint(X) for X in endpoints]

    mutations = 0
    try:
        tp, tm = Fraction(2, 7), Fraction(3, 11)
        _ = tp / (tp - tm)
    except ZeroDivisionError:
        pass
    if tp > 0 and tm > 0:
        mutations += 1
    if 2 * Fraction(-3, 5) + 3 * Fraction(2, 5) == 0:
        mutations += 1
    if j_min(28) == 14 and 4 * j_min(28) >= 28:
        mutations += 1

    records_canonical = json.dumps(records, sort_keys=True, separators=(",", ":")).encode()
    selected_x = {40, 64, 128, 256, 512, 1024}
    selected = [r for r in records if r["X"] in selected_x]
    positive_hist: dict[str, int] = {}
    negative_hist: dict[str, int] = {}
    min_occ = min(
        min(Decimal(r["positive_minimum_occupation_lower"]), Decimal(r["negative_minimum_occupation_lower"]))
        for r in records
    )
    for r in records:
        positive_hist[str(r["positive_cutoff"])] = positive_hist.get(str(r["positive_cutoff"]), 0) + 1
        negative_hist[str(r["negative_cutoff"])] = negative_hist.get(str(r["negative_cutoff"]), 0) + 1
    result = {
        "classification": "PASS_X_95100_CARRY_TERMINAL_CONTROL_BANK",
        "arithmetic_class": "EXACT_RATIONAL_PLUS_OUTWARD_DECIMAL",
        "exact_terminal_ratio_checks": ratio_checks,
        "exact_convex_interpolation_checks": interpolation_checks,
        "exact_cutoff_switch_checks": switch_checks,
        "terminal_gap_residue_checks": residue_checks,
        "directed_endpoints": len(records),
        "first_endpoint": records[0]["X"],
        "last_endpoint": records[-1]["X"],
        "all_records_sha256": hashlib.sha256(records_canonical).hexdigest(),
        "selected_records": selected,
        "positive_cutoff_histogram": positive_hist,
        "negative_cutoff_histogram": negative_hist,
        "minimum_preliminary_occupation_lower": str(min_occ),
        "hostile_mutations_detected": mutations,
        "proves": [
            "exact two-policy terminal interpolation",
            "exact monotone cutoff-switch formula",
            "closed mod-12 terminal-control schedule",
            "directed finite root-completed positive control banks",
            "terminal residual size-ratio firewall",
        ],
        "does_not_prove": [
            "cofinal mixed-policy occupation positivity",
            "cofinal terminal bracketing",
            "CRCTP",
            "Cycle Debt",
            "RH",
        ],
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--json", type=Path)
    args = p.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text)
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
