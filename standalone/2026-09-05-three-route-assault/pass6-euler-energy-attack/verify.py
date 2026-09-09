#!/usr/bin/env python3
"""Bounded exact checks for an Euler-factor energy attack.

The infinite prime-energy asymptotic is proved in PROOF.md, not by this code.
Only standard-library integer and Fraction arithmetic enters acceptance.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
from math import isqrt
import json
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def is_prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def prime_coefficients(primes: tuple[int, ...]) -> dict[int, int]:
    require(len(primes) <= 8, "bounded checker: at most eight prime factors")
    require(len(set(primes)) == len(primes), "duplicate prime factor")
    require(all(type(p) is int and is_prime(p) for p in primes), "not distinct primes")
    coeff = {1: 1}
    for p in primes:
        old = dict(coeff)
        for n, c in old.items():
            require(n * p not in coeff, "unexpected product collision")
            coeff[n * p] = -c
    return coeff


def inverse_power(n: int, r: int) -> F:
    require(type(r) is int and 1 <= r <= 6, "bounded positive integer 2a required")
    require(type(n) is int and n >= 1, "positive integer endpoint required")
    return F(1, n**r)


def pair_energy(c: dict[int, int], r: int, Y: int | None = None) -> F:
    """Cauchy/Gram expression, not the step integral implementation."""
    if Y is not None:
        require(type(Y) is int and Y >= 1, "invalid horizon")
    ans = F(0)
    for m, cm in c.items():
        for n, cn in c.items():
            lower = max(m, n)
            if Y is None:
                ans += cm * cn * inverse_power(lower, r) / r
            elif lower < Y:
                ans += cm * cn * (inverse_power(lower, r) - inverse_power(Y, r)) / r
    return ans


def step_integral(c: dict[int, int], r: int, Y: int | None = None,
                  shifted_by: int | None = None, lower: F = F(1)) -> F:
    """Independent integration of step functions in the original x variable.

    Integrates M(x)^2 x^(-r-1), or M(x) M(x/p) x^(-r-1).
    The latter is p^(-a) times the Hilbert correlation (r=2a).
    """
    require(lower >= 1, "invalid lower endpoint")
    events = {F(1), lower} | {F(n) for n in c}
    if shifted_by is not None:
        require(type(shifted_by) is int and shifted_by >= 2, "invalid shift")
        events |= {F(shifted_by * n) for n in c}
    if Y is not None:
        require(type(Y) is int and Y >= 1, "invalid horizon")
        events.add(F(Y))
        events = {x for x in events if lower <= x <= Y}
    else:
        events = {x for x in events if x >= lower}
    points = sorted(events)
    ans = F(0)
    for i, x in enumerate(points):
        if Y is not None and x == Y:
            continue
        nxt = points[i + 1] if i + 1 < len(points) else None
        mx = sum(cn for n, cn in c.items() if F(n) <= x)
        my = mx if shifted_by is None else sum(cn for n, cn in c.items() if shifted_by * n <= x)
        weight = x**(-r) - (nxt**(-r) if nxt is not None else F(0))
        ans += mx * my * weight / r
    return ans


def mobius_trial(n: int) -> int:
    """Trial-division definition, independent of the Euler subset expansion."""
    v = n
    result = 1
    p = 2
    while p * p <= v:
        if v % p == 0:
            v //= p
            result = -result
            if v % p == 0:
                return 0
        p += 1
    if v > 1:
        result = -result
    return result


def strict_json(path: Path) -> object:
    def pairs(items):
        out = {}
        for key, value in items:
            require(key not in out, f"duplicate JSON key: {key}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=pairs)


def same_typed(a, b) -> bool:
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(same_typed(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(same_typed(x, y) for x, y in zip(a, b))
    return a == b


def run_checks() -> dict:
    counts: dict[str, int] = {}
    def check(group: str, ok: bool) -> None:
        require(ok, f"failed exact check in {group}")
        counts[group] = counts.get(group, 0) + 1

    pool = (2, 3, 5, 7)
    subsets = [s for k in range(5) for s in itertools.combinations(pool, k)]
    for primes in subsets:
        c = prime_coefficients(primes)
        for r in (1, 2, 3):
            check("independent_full_energy", pair_energy(c, r) == step_integral(c, r))
            check("positive_energy", pair_energy(c, r) > 0)
            diagonal = sum(F(cn * cn, n**r) for n, cn in c.items())
            product = F(1)
            for p in primes:
                product *= 1 + F(1, p**r)
            check("torus_diagonal", diagonal == product)
            for Y in (1, 5, 12, 30):
                check("stopped_gram", pair_energy(c, r, Y) == step_integral(c, r, Y))

    # Finite Euler updates in full and stopped physical norms, including boundary debt.
    chain = (2, 3, 5, 7, 11)
    for r in (1, 2, 3):
        primes: tuple[int, ...] = ()
        for p in chain:
            c = prime_coefficients(primes)
            new = prime_coefficients(primes + (p,))
            old_E = step_integral(c, r)
            rho = step_integral(c, r, shifted_by=p)
            check("full_prime_update", step_integral(new, r) == (1 + F(1, p**r)) * old_E - 2 * rho)
            for Y in (2, 5, 12, 30, 210):
                E0 = step_integral(c, r, Y)
                rhoY = step_integral(c, r, Y, shifted_by=p)
                B = step_integral(c, r, Y, lower=max(F(1), F(Y, p)))
                check("stopped_prime_update", step_integral(new, r, Y) == (1 + F(1, p**r)) * E0 - F(1, p**r) * B - 2 * rhoY)
            primes += (p,)

    # One complete normalized innovation ledger, retaining every sign and boundary.
    for r in (1, 2, 3):
        for Y in (2, 5, 12, 30, 210):
            primes = ()
            D = F(1)
            ledger = F(0)
            for p in chain:
                c = prime_coefficients(primes)
                D *= 1 + F(1, p**r)
                B = step_integral(c, r, Y, lower=max(F(1), F(Y, p)))
                rho = step_integral(c, r, Y, shifted_by=p)
                ledger += (F(1, p**r) * B + 2 * rho) / D
                primes += (p,)
            Ebase = (1 - F(1, Y**r)) / r
            check("normalized_ledger", step_integral(prime_coefficients(primes), r, Y) / D == Ebase - ledger)

    witnesses = []
    c23 = prime_coefficients((2, 3))
    c235 = prime_coefficients((2, 3, 5))
    for r in (1, 2, 3, 4):
        rho = step_integral(c23, r, shifted_by=5)
        expected = -(F(1, 5**r) - F(1, 6**r)) / r
        check("three_prime_negative_correlation", rho == expected and rho < 0)
        excess = step_integral(c235, r) - (1 + F(1, 5**r)) * step_integral(c23, r)
        check("three_prime_norm_excess", excess == -2 * rho and excess > 0)
        check("three_prime_stopped_witness", step_integral(c23, r, 30, shifted_by=5) == rho)
        witnesses.append({"two_a": r, "scaled_correlation": str(rho), "excess_energy": str(excess)})
    check("rational_witness_values", step_integral(c23, 2) == F(5, 12) and step_integral(c235, 2) == F(401, 900))

    # Exact horizon-faithful coefficients: primes above the observed integer cannot contribute.
    for Y in range(1, 31):
        primes = tuple(n for n in range(2, Y + 1) if is_prime(n))
        # Truncate after EACH multiplication, rather than enumerating the full primorial support.
        c = {1: 1}
        for p in primes:
            old = dict(c)
            for n, cn in old.items():
                if n * p <= Y:
                    c[n * p] = -cn
        check("horizon_faithfulness", all(c.get(n, 0) == mobius_trial(n) for n in range(1, Y + 1)))

    # Independent algebra for the square-integrable higher-prime-power error.
    for k in (2, 3, 5, 7, 11):
        t = F(1, k)
        partial = sum(t**j / j for j in range(2, 21))
        check("log_tail_majorant", partial <= t*t / (2*(1-t)))

    return {
        "status": "PASS_BOUNDED_EXACT_CONTROLS",
        "arithmetic": "EXACT_INTEGER_AND_RATIONAL",
        "counts": counts,
        "total_checks": sum(counts.values()),
        "witnesses": witnesses,
        "large_prime_sums_evaluated": False,
        "PNT_machine_proved": False,
        "infinite_asymptotic_machine_proved": False,
        "RH_proved": False,
    }


def check_manifest() -> None:
    manifest = HERE / "SHA256SUMS"
    entries = {}
    for line in manifest.read_text().splitlines():
        digest, name = line.split("  ", 1)
        require(name not in entries and Path(name).name == name, "invalid manifest entry")
        entries[name] = digest
    actual = {p.name for p in HERE.iterdir() if p.is_file() and p.name != "SHA256SUMS"}
    require(set(entries) == actual, "manifest coverage mismatch")
    for name, digest in entries.items():
        require(hashlib.sha256((HERE / name).read_bytes()).hexdigest() == digest, f"manifest hash mismatch: {name}")


class RejectionTests(unittest.TestCase):
    def test_duplicate_prime(self):
        with self.assertRaises(ValueError): prime_coefficients((2, 2))
    def test_composite(self):
        with self.assertRaises(ValueError): prime_coefficients((2, 9))
    def test_cap(self):
        with self.assertRaises(ValueError): prime_coefficients((2,3,5,7,11,13,17,19,23))
    def test_invalid_horizon(self):
        with self.assertRaises(ValueError): pair_energy({1: 1}, 2, 0)
    def test_boolean_parameter(self):
        with self.assertRaises(ValueError): inverse_power(2, True)
    def test_invalid_power(self):
        with self.assertRaises(ValueError): inverse_power(2, 0)
    def test_wrong_correlation_sign(self):
        self.assertLess(step_integral(prime_coefficients((2,3)), 2, shifted_by=5), 0)
    def test_discarded_boundary_is_wrong(self):
        c = prime_coefficients((2,3))
        actual = step_integral(prime_coefficients((2,3,5)), 2, 5)
        incorrect = (1+F(1,25))*step_integral(c,2,5)-2*step_integral(c,2,5,shifted_by=5)
        self.assertNotEqual(actual, incorrect)
    def test_json_bool_alias(self):
        self.assertFalse(same_typed({"n": 1}, {"n": True}))
    def test_json_float_alias(self):
        self.assertFalse(same_typed({"n": 1}, {"n": 1.0}))
    def test_result_mutation(self):
        expected = {"witness": "-11/1800", "RH_proved": False}
        self.assertFalse(same_typed(expected, {"witness": "11/1800", "RH_proved": False}))
    def test_duplicate_json_key(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)/"bad.json"
            p.write_text('{"n":1,"n":2}')
            with self.assertRaises(ValueError): strict_json(p)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path)
    parser.add_argument("--manifest", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(RejectionTests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        require(result.wasSuccessful(), "unit/rejection suite failed")
        return
    result = run_checks()
    if args.check:
        require(same_typed(result, strict_json(args.check)), "saved result mismatch")
    if args.manifest:
        check_manifest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
