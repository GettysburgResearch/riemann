from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_derangement_selector_finite_l1_optimization.py"
)
SPEC = importlib.util.spec_from_file_location("derangement_selector_l1", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class DerangementSelectorFiniteL1OptimizationTest(unittest.TestCase):
    def test_frozen_source_blobs(self) -> None:
        subject.check_source_blobs()

    def test_character_table_primitives(self) -> None:
        self.assertEqual(subject.character((3, 1), (4,)), -1)
        self.assertEqual(subject.character((2, 2), (4,)), 0)
        self.assertEqual(subject.character((3, 1), (1, 1, 1, 1)), 3)
        self.assertEqual(subject.dimension((3, 1)), 3)
        self.assertEqual(subject.centralizer_size((2, 2)), 8)

    def test_exact_selector_is_feasible_with_expected_mass(self) -> None:
        for degree in range(subject.MIN_DEGREE, subject.MAX_DEGREE + 1):
            coefficients = subject.selector_coefficients(degree)
            self.assertEqual(
                subject.weighted_l1(coefficients),
                Fraction(2 ** (degree - 1), degree),
            )
            for cycle_type in subject.partitions(degree):
                expected = int(cycle_type == (degree,))
                self.assertEqual(
                    subject.evaluate_coefficients(coefficients, cycle_type),
                    expected,
                )

    def test_exact_duals_and_unique_optima(self) -> None:
        for degree in range(subject.MIN_DEGREE, subject.MAX_DEGREE + 1):
            panel = subject.verify_degree(degree)
            self.assertEqual(panel["optimum_to_exact_cycle_ratio"], "1")
            self.assertTrue(panel["unique_optimizer"])
            if degree >= 4:
                self.assertEqual(
                    panel["minimum_relative_nonhook_dual_slack"],
                    str(subject.EXPECTED_STRICT_SLACK[degree]),
                )

    def test_hook_only_dual_ansatz_has_exact_first_failure(self) -> None:
        for degree in range(2, 8):
            self.assertTrue(subject.hook_only_branching_diagnostic(degree)["feasible"])
        degree_eight = subject.hook_only_branching_diagnostic(8)
        self.assertFalse(degree_eight["feasible"])
        self.assertEqual(degree_eight["maximum_nonhook_capacity_ratio"], "6/5")
        self.assertEqual(degree_eight["first_violation_k"], 1)

    def test_scope_resource_caps_and_guards(self) -> None:
        result = subject.run(check_sources=False)
        self.assertFalse(result["finite_theorem"]["all_d_claim"])
        self.assertFalse(result["scope"]["rh_proved"])
        self.assertEqual(result["resource_caps"]["maximum_degree"], 10)
        self.assertEqual(result["resource_caps"]["maximum_irreducibles"], 42)
        self.assertEqual(result["resource_caps"]["external_lp_calls_in_replay"], 0)
        with self.assertRaises(ValueError):
            subject.selector_coefficients(11)
        with self.assertRaises(ValueError):
            subject.validate_degree(True)


if __name__ == "__main__":
    unittest.main()
