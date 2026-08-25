"""Exact tests for the bounded Sym5 multi-prime collision filter."""

from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "research" / "l-families" / "atlas" / "function_field"
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

subject = importlib.import_module("elliptic_sym5_multiprime_collision_filter")


class EllipticSym5MultiprimeCollisionFilterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_locked_source_and_local_collision(self) -> None:
        self.assertEqual(
            self.fixture["locked_local_collision"],
            {
                "q": 31,
                "left_trace": -7,
                "right_trace": 3,
                "scalar_trace": 5544,
                "first_separating_coefficient_degree": 2,
            },
        )
        lock = self.fixture["source_locks"]
        self.assertEqual(lock["file_sha256_lf"], subject.EXPECTED_SOURCE_SHA256_LF)
        self.assertEqual(
            subject.symmetric_power_trace(-7, 31, 5),
            subject.symmetric_power_trace(3, 31, 5),
        )
        self.assertEqual(subject.symmetric_power_trace(3, 31, 5), 5544)

    def test_complete_bounded_model_realizations(self) -> None:
        box = self.fixture["model_box"]
        left = [(row["A"], row["B"]) for row in box["left_trace_models"]]
        right = [(row["A"], row["B"]) for row in box["right_trace_models"]]
        self.assertEqual(left, [(-4, 4), (-3, -3), (3, 1)])
        self.assertEqual(right, [(-1, -1), (2, -4), (3, -2), (4, -2)])
        self.assertEqual(box["cross_pair_count"], 12)
        guard = subject.ResourceGuard()
        buckets = subject.models_for_traces((-7, 3), 31, 4, guard)
        self.assertEqual(buckets[-7], tuple(left))
        self.assertEqual(buckets[3], tuple(right))

    def test_every_cross_pair_splits_on_the_auxiliary_panel(self) -> None:
        panel = self.fixture["auxiliary_filter"]
        self.assertEqual(panel["primes_in_order"], [5, 7, 11, 17])
        self.assertTrue(panel["all_cross_pairs_separated"])
        self.assertEqual(
            panel["first_separator_counts"],
            {"5": 4, "7": 6, "11": 1, "17": 1},
        )
        self.assertEqual(len(panel["pairs"]), 12)
        for pair in panel["pairs"]:
            first = pair["first_auxiliary_separating_prime"]
            row = next(
                item
                for item in pair["auxiliary_rows"]
                if item["prime"] == first
            )
            self.assertEqual(row["status"], "GOOD_REDUCTION")
            self.assertFalse(row["sym5_scalar_equal"])

    def test_trace_recurrence_matches_closed_sym5_formula(self) -> None:
        for q in (5, 7, 11, 17, 31):
            for trace in range(-2 * int(q**0.5), 2 * int(q**0.5) + 1):
                expected = trace**5 - 4 * q * trace**3 + 3 * q**2 * trace
                self.assertEqual(
                    subject.symmetric_power_trace(trace, q, 5),
                    expected,
                )

    def test_resource_and_claim_firewalls(self) -> None:
        resource = self.fixture["resource_contract"]
        self.assertLess(
            resource["accounted_source_atoms"],
            resource["exclusive_source_atom_cap"],
        )
        self.assertFalse(resource["random_sampling"])
        self.assertTrue(resource["finite_field_model_enumeration"])
        self.assertIn("81 short-Weierstrass", resource["enumeration_scope"])
        self.assertEqual(resource["largest_field"], 31)
        self.assertIn(
            "classification of all multi-prime spectral twins",
            self.fixture["interpretation"]["not_proved"],
        )

    def test_fail_closed_domains_under_optimized_python(self) -> None:
        with self.assertRaises(ValueError):
            subject.legendre_symbol(1, 9)
        with self.assertRaises(ValueError):
            subject.has_good_reduction((1, 1), 2)
        with self.assertRaises(ValueError):
            subject.symmetric_power_trace(1, 5, -1)
        with self.assertRaises(RuntimeError):
            subject.ResourceGuard(cap=2).charge("too_large", 2)


if __name__ == "__main__":
    unittest.main()
