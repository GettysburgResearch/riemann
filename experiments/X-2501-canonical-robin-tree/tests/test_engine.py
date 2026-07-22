from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import hashlib
import json
import unittest

from certmath import RobinParameters, exp_nonnegative, log_fraction, robin_rhs
from search import CertificateSearch, first_primes, prime_power_abundancy
from verify import IndependentVerifier

FAST = RobinParameters(bits=160, log_terms=56, exp_terms=56, harmonic_cutoff=30_000)


def refresh_digest(certificate: dict[str, object]) -> None:
    body = dict(certificate)
    body.pop("certificate_sha256", None)
    certificate["certificate_sha256"] = hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def decode_streams(certificate: dict[str, object]) -> list[tuple[int, str, tuple[int, ...]]]:
    result: list[tuple[int, str, tuple[int, ...]]] = []
    streams = certificate["terminal_streams"]
    assert isinstance(streams, list)
    for support, stream in enumerate(streams, start=1):
        for token in stream:
            code, payload = token.split(":", 1)
            prefix = () if not payload else tuple(int(v) for v in payload.split(","))
            result.append((support, code, prefix))
    return result


def brute_force_vectors(n_max: int, support: int) -> list[tuple[int, ...]]:
    primes = first_primes(support)
    result: list[tuple[int, ...]] = []

    def visit(prefix: tuple[int, ...], product: int, previous: int | None) -> None:
        depth = len(prefix)
        if depth == support:
            result.append(prefix)
            return
        p = primes[depth]
        tail = 1
        for q in primes[depth + 1 :]:
            tail *= q
        exponent = 1
        candidates: list[int] = []
        while product * p**exponent * tail <= n_max:
            if previous is None or exponent <= previous:
                candidates.append(exponent)
            exponent += 1
        for value in reversed(candidates):
            visit(prefix + (value,), product * p**value, value)

    visit((), 1, None)
    return result


class MathTests(unittest.TestCase):
    def test_prime_generation(self) -> None:
        self.assertEqual(first_primes(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_prime_power_factor(self) -> None:
        self.assertEqual(prime_power_abundancy(2, 3), Fraction(15, 8))
        self.assertEqual(prime_power_abundancy(3, 2), Fraction(13, 9))

    def test_log_and_exp_containment(self) -> None:
        log2 = log_fraction(Fraction(2), bits=160, terms=56)
        exp_log2 = exp_nonnegative(log2, terms=56)
        self.assertTrue(exp_log2.contains_fraction(Fraction(2)))

    def test_robin_calibration_5041(self) -> None:
        rhs = robin_rhs(5041, FAST)
        self.assertTrue(rhs.lower_gt_fraction(Fraction(224, 65)))


class CoverageTests(unittest.TestCase):
    def build(self, n_max: int = 50_000) -> dict[str, object]:
        return CertificateSearch(n_max, FAST).run()

    def test_search_and_independent_verify(self) -> None:
        certificate = self.build()
        result = IndependentVerifier(certificate).verify()
        self.assertTrue(result["verified"])
        self.assertEqual(certificate["counts"]["unresolved_leaves"], 0)
        self.assertEqual(certificate["counts"]["violation_leaves"], 0)

    def test_small_box_has_prune(self) -> None:
        certificate = self.build(1_000_000)
        self.assertGreater(certificate["counts"]["prunes"], 0)
        IndependentVerifier(certificate).verify()

    def test_bruteforce_leaf_partition(self) -> None:
        n_max = 100_000
        certificate = self.build(n_max)
        decoded = decode_streams(certificate)
        by_support: dict[int, list[tuple[str, tuple[int, ...]]]] = {}
        for support, code, prefix in decoded:
            by_support.setdefault(support, []).append((code, prefix))
        for support in range(1, certificate["finite_region"]["canonical_support_max"] + 1):
            vectors = brute_force_vectors(n_max, support)
            terminals = by_support[support]
            for vector in vectors:
                covering = [
                    (code, prefix)
                    for code, prefix in terminals
                    if (code == "P" and vector[: len(prefix)] == prefix)
                    or (code != "P" and vector == prefix)
                ]
                self.assertEqual(len(covering), 1, (support, vector, covering))

    def test_missing_terminal_rejected(self) -> None:
        certificate = self.build()
        certificate["terminal_streams"][-1].pop()
        refresh_digest(certificate)
        with self.assertRaises(ValueError):
            IndependentVerifier(certificate).verify()

    def test_reordered_terminal_rejected(self) -> None:
        certificate = self.build()
        stream = next(s for s in certificate["terminal_streams"] if len(s) >= 2)
        stream[0], stream[1] = stream[1], stream[0]
        refresh_digest(certificate)
        with self.assertRaises(ValueError):
            IndependentVerifier(certificate).verify()

    def test_forged_root_prune_rejected(self) -> None:
        certificate = self.build(1_000_000)
        certificate["terminal_streams"][0] = ["P:"]
        certificate["counts"] = dict(certificate["counts"])
        refresh_digest(certificate)
        with self.assertRaises(ValueError):
            IndependentVerifier(certificate).verify()

    def test_tight_summary_tampering_rejected(self) -> None:
        certificate = self.build()
        certificate["strict_terminal_normalized_ratio_upper"] = None
        refresh_digest(certificate)
        with self.assertRaises(ValueError):
            IndependentVerifier(certificate).verify()


if __name__ == "__main__":
    unittest.main()
