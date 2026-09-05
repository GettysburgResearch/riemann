#!/usr/bin/env python3
"""Recompute bounded exact controls. No finite control proves the analytic limits.
Standard library only. Acceptance never depends on Python assert statements.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent
PARENT_SHA256 = "45013f55becc7f6e0b12ebf2847b2688680084bd87d56160c3e41344cefeec71"


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(n: int, low: int = 0, high: int = 4096) -> int:
    need(type(n) is int and low <= n <= high, "integer outside certified cap")
    return n


def primes(n: int) -> list[int]:
    integer(n)
    a = [True] * (n + 1)
    if n >= 0:
        a[0] = False
    if n >= 1:
        a[1] = False
    for p in range(2, math.isqrt(n) + 1):
        if a[p]:
            for k in range(p * p, n + 1, p):
                a[k] = False
    return [p for p in range(2, n + 1) if a[p]]


def mobius(n: int) -> int:
    integer(n, 1)
    parity = 0
    for p in range(2, math.isqrt(n) + 1):
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            parity += 1
    if n > 1:
        parity += 1
    return (-1) ** parity


def muq(n: int, q: int) -> int:
    return 0 if n % q == 0 else mobius(n)


def convolution(a: list, b: list, cap: int) -> list:
    integer(cap)
    c = [0] * (cap + 1)
    for i in range(1, min(cap + 1, len(a))):
        for j in range(1, min(cap // i + 1, len(b))):
            c[i * j] += a[i] * b[j]
    return c


def finite_euler(x: int, q: int, cap: int) -> list[int]:
    """Independently expand the literal signed local factors."""
    integer(x, 2)
    integer(cap)
    c = [0] * (cap + 1)
    if cap >= 1:
        c[1] = 1
    for p in primes(x):
        if p != q:
            old = c[:]
            for n in range(1, cap // p + 1):
                c[p * n] -= old[n]
    return c


def rough_vector(x: int, cap: int) -> list[int]:
    c = [0] + [1] * cap
    for p in primes(x):
        for n in range(p, cap + 1, p):
            c[n] = 0
    return c


def prefix(a: list) -> list:
    total = 0
    out = []
    for value in a:
        total += value
        out.append(total)
    return out


def g_value(y: Q, q: int) -> Q:
    need(type(y) is Q and 1 <= y <= 4096, "rational physical endpoint required")
    n = y.numerator // y.denominator
    return sum((Q(muq(k, q), k) - Q(muq(k, q), 1) / y for k in range(1, n + 1)), Q(0))


def poly_mul(a: list[Q], b: list[Q], n: int) -> list[Q]:
    c = [Q(0)] * (n + 1)
    for i in range(min(n + 1, len(a))):
        for j in range(min(n - i + 1, len(b))):
            c[i + j] += a[i] * b[j]
    return c


def poly_exp(a: list[Q], n: int) -> list[Q]:
    need(a[0] == 0, "formal exponential requires zero constant")
    e = [Q(0)] * (n + 1)
    e[0] = Q(1)
    for k in range(1, n + 1):
        e[k] = sum((j * a[j] * e[k - j] for j in range(1, min(k + 1, len(a)))), Q(0)) / k
    return e


def poly_exp_independent(a: list[Q], n: int) -> list[Q]:
    out = [Q(0)] * (n + 1)
    term = [Q(0)] * (n + 1)
    term[0] = Q(1)
    for k in range(n + 1):
        out = [x + y / math.factorial(k) for x, y in zip(out, term)]
        term = poly_mul(term, a, n)
    return out


def logarithm_interval(x: Q, n: int = 36) -> tuple[Q, Q]:
    need(type(x) is Q and x >= 1, "log interval accepts rationals at least one")
    integer(n, 1, 128)
    z = (x - 1) / (x + 1)
    value = 2 * sum((z ** (2 * k + 1) / (2 * k + 1) for k in range(n)), Q(0))
    tail = 2 * z ** (2 * n + 1) / ((2 * n + 1) * (1 - z * z))
    return value, value + tail


def strict_json_equal(a, b) -> bool:
    if type(a) is not type(b):
        return False
    if type(a) is dict:
        return a.keys() == b.keys() and all(strict_json_equal(a[k], b[k]) for k in a)
    if type(a) is list:
        return len(a) == len(b) and all(strict_json_equal(x, y) for x, y in zip(a, b))
    return a == b


def no_duplicate_keys(pairs):
    out = {}
    for key, value in pairs:
        need(key not in out, "duplicate JSON key")
        out[key] = value
    return out


def authenticate_parent() -> None:
    p = ROOT.parent / "pass6-euler-energy-attack" / "PROOF.md"
    need(p.exists(), "parent proof missing")
    need(hashlib.sha256(p.read_bytes()).hexdigest() == PARENT_SHA256, "parent proof hash mismatch")


def manifest() -> None:
    rows = (ROOT / "SHA256SUMS").read_text().splitlines()
    listed = set()
    for row in rows:
        digest, name = row.split("  ", 1)
        need(name not in listed and Path(name).name == name, "duplicate or invalid manifest path")
        listed.add(name)
        need(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, f"hash mismatch: {name}")
    actual = {p.name for p in ROOT.iterdir() if p.is_file() and p.name != "SHA256SUMS"}
    need(listed == actual, "inexact manifest coverage")


def recompute() -> dict:
    authenticate_parent()
    counts: dict[str, int] = {}
    checks = 0

    def check(category: str, condition: bool) -> None:
        nonlocal checks
        need(condition, category)
        counts[category] = counts.get(category, 0) + 1
        checks += 1

    # Exact full-support Dirichlet convolution, including powers of rough primes.
    cap = 256
    for q, x in [(2, 2), (3, 5), (5, 11), (67, 67), (67, 71)]:
        a = [0] + [muq(n, q) for n in range(1, cap + 1)]
        direct = finite_euler(x, q, cap)
        combined = convolution(a, rough_vector(x, cap), cap)
        for n in range(1, cap + 1):
            check("rough_convolution", direct[n] == combined[n])
        check("faithful_initial_horizon", direct[:x + 1] == a[:x + 1])

    # Missing primes are regrouped before evaluating the exact signed sum.
    for q, x in [(2, 3), (3, 5), (5, 7), (67, 67)]:
        limit = min(x * x - 1, 384)
        ps = primes(limit)
        mq = prefix([0] + [muq(n, q) for n in range(1, limit + 1)])
        mx = prefix(finite_euler(x, q, limit))
        for y in range(x, limit + 1):
            tail = sum(mq[y // p] for p in ps if x < p <= y)
            grouped = sum(muq(m, q) * sum(x < p <= y // m for p in ps) for m in range(1, y // x + 1))
            check("first_missing_prime_shell", mx[y] - mq[y] == tail == grouped)

    # Omitting rough prime powers really breaks the convolution after X^2.
    q, x, cap = 2, 3, 30
    a = [0] + [muq(n, q) for n in range(1, cap + 1)]
    wrong = [0] * (cap + 1)
    wrong[1] = 1
    for p in primes(cap):
        if p > x:
            wrong[p] = 1
    check("rough_power_rejection", convolution(a, wrong, cap)[25] != finite_euler(x, q, cap)[25])

    # Actual signed profile is a continuous primitive despite arithmetic jumps.
    for q in (2, 3, 67):
        m = 0
        for n in range(1, 97):
            m += muq(n, q)
            check("profile_primitive", g_value(Q(n + 1), q) - g_value(Q(n), q) == m * (Q(1, n) - Q(1, n + 1)))
    for denominator in range(2, 18):
        for numerator in range(denominator, 2 * denominator):
            y = Q(numerator, denominator)
            check("profile_first_interval", g_value(y, 67) == 1 - 1 / y)

    low, high = logarithm_interval(Q(2))
    check("positive_profile_constant", low - Q(5, 8) > Q(1, 16))
    check("log_interval_width", high - low < Q(1, 10 ** 30))
    buchstab_norm = Q(1, 3) * (1 - Q(1, 8))
    check("buchstab_norm_lower", buchstab_norm == Q(7, 24))
    check("buchstab_norm_upper", buchstab_norm + Q(1, 2) == Q(19, 24))
    check("noncontractive_correction", Q(1, 6) - Q(2, 135) == Q(41, 270) > 0)

    # Entire correction: e^(-gamma) C(z)=z exp(-Ein(z)); no branch ambiguity.
    order = 20
    ein = [Q(0)] + [Q((-1) ** (k + 1), k * math.factorial(k)) for k in range(1, order + 1)]
    minus = [-x for x in ein]
    rho_transform = poly_exp(minus, order)
    independent = poly_exp_independent(minus, order)
    inverse = poly_mul(rho_transform, poly_exp(ein, order), order)
    c = [Q(0)] + rho_transform[:-1]
    e_minus_z = [Q((-1) ** k, math.factorial(k)) for k in range(order + 1)]
    rhs = poly_mul(c, e_minus_z, order)
    for k in range(order + 1):
        check("entire_correction_series", rho_transform[k] == independent[k])
        check("entire_correction_inverse", inverse[k] == (1 if k == 0 else 0))
        check("balanced_log_derivative", k * c[k] == rhs[k])
    check("simple_pole_zero_normalization", c[0] == 0 and c[1] == 1)

    # exp(H) times exp(-H)=1 for a finite delay series; all delay layers retained.
    for delay in (2, 3, 5):
        n = 18
        h = [Q(0)] * (n + 1)
        for j in range(delay, n + 1):
            h[j] = Q(1, j)
        rough = poly_exp(h, n)
        complete = poly_exp([-x for x in h], n)
        identity = poly_mul(rough, complete, n)
        for j in range(n + 1):
            check("all_layer_delay_inverse", identity[j] == (1 if j == 0 else 0))
        check("delay_horizon_unchanged", complete[0] == 1 and all(x == 0 for x in complete[1:delay]))

    # The actual completion's first continuum layer is not the entire completion.
    first_only = [Q(1)] + [-x for x in h[1:]]
    check("single_layer_not_complete", poly_mul(rough, first_only, n)[2 * delay] != 0)
    return {
        "status": "FINITE_CHECKS_PASS_ANALYTIC_REVIEW_PENDING",
        "arithmetic": "EXACT_INTEGER_AND_RATIONAL",
        "distinct_checks": checks,
        "categories": counts,
        "parent_sha256": PARENT_SHA256,
        "proof_sha256": hashlib.sha256((ROOT / "PROOF.md").read_bytes()).hexdigest(),
        "profile_norm_lower": "1/16 (strict)",
        "buchstab_regular_derivative_norm_interval": ["7/24", "19/24"],
        "analytic_limits_machine_proved": False,
        "critical_half_plane_bound_proved": False,
        "RH_proved": False,
    }


class RejectionTests(unittest.TestCase):
    def test_integer_bool(self):
        with self.assertRaises(ValueError): integer(True)
    def test_integer_float(self):
        with self.assertRaises(ValueError): integer(3.0)
    def test_resource_cap(self):
        with self.assertRaises(ValueError): integer(4097)
    def test_rational_endpoint(self):
        with self.assertRaises(ValueError): g_value(1.5, 67)
    def test_nonzero_exp_constant(self):
        with self.assertRaises(ValueError): poly_exp([Q(1)], 2)
    def test_duplicate_json(self):
        with self.assertRaises(ValueError): json.loads('{"a":1,"a":2}', object_pairs_hook=no_duplicate_keys)
    def test_boolean_alias(self):
        self.assertFalse(strict_json_equal({"x": 1}, {"x": True}))
    def test_float_alias(self):
        self.assertFalse(strict_json_equal([Q(1).numerator], [1.0]))
    def test_missing_field(self):
        self.assertFalse(strict_json_equal({"x": 1}, {}))
    def test_changed_status(self):
        self.assertFalse(strict_json_equal({"RH_proved": False}, {"RH_proved": True}))
    def test_parent_hash(self):
        authenticate_parent()
    def test_exp_compiler_agreement(self):
        h = [Q(0), Q(2, 3), Q(-1, 7)]
        self.assertEqual(poly_exp(h, 12), poly_exp_independent(h, 12))
        self.assertTrue(all(type(v) is Q for v in poly_exp_independent(h, 12)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path)
    parser.add_argument("--manifest", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(RejectionTests)
        outcome = unittest.TextTestRunner(verbosity=2).run(suite)
        if not outcome.wasSuccessful():
            raise SystemExit(1)
        return
    result = recompute()
    if args.check:
        saved = json.loads(args.check.read_text(), object_pairs_hook=no_duplicate_keys)
        need(strict_json_equal(result, saved), "saved result does not match recomputation")
    if args.manifest:
        manifest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
