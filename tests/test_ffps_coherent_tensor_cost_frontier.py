"""Focused exact tests for the coherent FFPS tensor cost frontier."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import ffps_coherent_tensor_cost_frontier as subject


class FFPSCoherentTensorCostFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_exact_prefix_values(self) -> None:
        expected = {
            (3,): (3, Fraction(1, 2)),
            (3, 5): (15, Fraction(1, 3)),
            (3, 5, 7): (105, Fraction(1, 4)),
            (3, 5, 7, 11): (1_155, Fraction(5, 24)),
            (3, 5, 7, 11, 13): (15_015, Fraction(5, 28)),
            (3, 5, 7, 11, 13, 17, 19): (4_849_845, Fraction(1, 7)),
        }
        for primes, (conductor, leverage) in expected.items():
            self.assertEqual(subject.squarefree_conductor(list(primes)), conductor)
            self.assertEqual(subject.squared_leverage(list(primes)), leverage)

    def test_prefix_is_optimal_for_every_small_subset_budget(self) -> None:
        primes = subject.first_odd_primes(subject.EXHAUSTIVE_PRIME_COUNT)
        comparisons = 0
        for size in range(len(primes) + 1):
            for subset in combinations(primes, size):
                budget = subject.squarefree_conductor(list(subset))
                optimum = subject.optimal_prefix_under_budget(budget)
                self.assertLessEqual(
                    subject.squared_leverage(list(optimum)),
                    subject.squared_leverage(list(subset)),
                )
                self.assertLessEqual(
                    subject.squarefree_conductor(list(optimum)), budget
                )
                comparisons += 1
        self.assertEqual(comparisons, 2**subject.EXHAUSTIVE_PRIME_COUNT)

    def test_fixed_cardinality_exchange_is_strict(self) -> None:
        prefix = subject.first_odd_primes(6)
        for count in range(1, 6):
            baseline = prefix[:count]
            shifted = prefix[1 : count + 1]
            self.assertLess(
                subject.squarefree_conductor(list(baseline)),
                subject.squarefree_conductor(list(shifted)),
            )
            self.assertLess(
                subject.squared_leverage(list(baseline)),
                subject.squared_leverage(list(shifted)),
            )

    def test_target_thresholds_are_minimal(self) -> None:
        for target in (
            Fraction(1, 2),
            Fraction(1, 3),
            Fraction(1, 4),
            Fraction(1, 5),
            Fraction(1, 10),
        ):
            row = subject.minimal_conductor_for_target(target)
            attained = Fraction(*row["attained_squared_leverage"])
            previous = Fraction(*row["previous_prefix_squared_leverage"])
            self.assertLessEqual(attained, target)
            self.assertGreater(previous, target)
            self.assertEqual(
                subject.optimal_prefix_under_budget(
                    row["minimal_squarefree_conductor"]
                ),
                tuple(row["optimal_primes"]),
            )

    def test_source_dependency_and_provenance_are_locked(self) -> None:
        self.assertEqual(
            subject._sha256_lf(subject.DEPENDENCY_PATH), subject.DEPENDENCY_LF_SHA256
        )
        locked = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(locked, self.fixture)
        for label, path in (
            ("producer_sha256_lf", Path(subject.__file__)),
            ("note_sha256_lf", subject.NOTE_PATH),
            ("test_sha256_lf", Path(__file__)),
        ):
            raw = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                locked["provenance"][label], hashlib.sha256(raw).hexdigest()
            )

    def test_scope_and_resource_caps(self) -> None:
        scope = self.fixture["scope"]
        self.assertTrue(scope["exact_budget_theorem_all_distinct_odd_primes"])
        self.assertFalse(scope["global_ffps_moment_proved"])
        self.assertFalse(scope["principal_member_individualized"])
        caps = self.fixture["provenance"]["resource_caps"]
        self.assertLessEqual(
            caps["exhaustive_subsets_used"], caps["maximum_exhaustive_subsets"]
        )

    def test_fail_closed_domains(self) -> None:
        for primes in ((2,), (3, 3), (9,)):
            with self.assertRaises(ValueError):
                subject.squared_leverage(list(primes))
        for target in (0, 1, -1, 2):
            with self.assertRaises(ValueError):
                subject.minimal_conductor_for_target(target)
        with self.assertRaises(ValueError):
            subject.optimal_prefix_under_budget(0)
        with self.assertRaises(ValueError):
            subject.exhaustive_budget_audit(subject.first_odd_primes(13))


if __name__ == "__main__":
    unittest.main()
