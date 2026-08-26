"""Tests for the exact odd-notch factor-depth phase diagram."""

from __future__ import annotations

import ast
import importlib.util
import subprocess
import sys
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
    / "quadratic_family_notch_depth_phase_diagram.py"
)
NOTE_PATH = MODULE_PATH.with_name("QUADRATIC_FAMILY_NOTCH_DEPTH_PHASE_DIAGRAM.md")

SPEC = importlib.util.spec_from_file_location(
    "quadratic_family_notch_depth_phase_diagram", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load notch-depth phase-diagram module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class QuadraticFamilyNotchDepthPhaseDiagramTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = MODULE.build_report()

    def test_rough_majorant_recurrence_and_bound(self) -> None:
        for d_value in range(1, 13):
            coefficients = MODULE.rough_majorant_coefficients(d_value, 72)
            self.assertEqual(coefficients[0], 1)
            self.assertTrue(all(value == 0 for value in coefficients[1:d_value]))
            for degree in range(d_value, len(coefficients)):
                recurrence_sum = sum(
                    coefficients[degree - part] for part in range(d_value, degree + 1)
                )
                self.assertEqual(degree * coefficients[degree], recurrence_sum)
                self.assertLessEqual(coefficients[degree], Fraction(1, d_value))

    def test_d1_majorant_is_exact_geometric_series(self) -> None:
        coefficients = MODULE.rough_majorant_coefficients(1, 40)
        self.assertTrue(all(value == 1 for value in coefficients))

    def test_depth_scans_even_and_odd_exterior_indices(self) -> None:
        for n_value in range(4, 24):
            epsilon = n_value % 2
            for depth in range(n_value // 2):
                row = MODULE.notch_layer_certificate(n_value, depth)
                self.assertEqual(row["top_exterior_index"], 2 * depth + epsilon)
                self.assertEqual(row["all_residual_indices"][-1], epsilon)
                self.assertEqual(row["minimum_degree_d"], row["h"] - row["depth_j"])

    def test_layer_set_uses_harmonic_square_budget(self) -> None:
        row = MODULE.layer_set_bound_certificate(5, 101, [20, 21, 22])
        expected = Fraction(1, 20**2) + Fraction(1, 21**2) + Fraction(1, 22**2)
        self.assertEqual(row["harmonic_square_budget"], str(expected))
        self.assertEqual(row["coarse_budget"], str(Fraction(3, 20**2)))

    def test_invalid_inputs_fail_closed(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.rough_majorant_coefficients(0, 5)
        with self.assertRaises(ValueError):
            MODULE.notch_layer_certificate(4, 2)
        with self.assertRaises(ValueError):
            MODULE.layer_set_bound_certificate(3, 7, [4])
        with self.assertRaises(ValueError):
            MODULE.layer_set_bound_certificate(True, 9, [2])

    def test_report_resource_and_claim_firewalls(self) -> None:
        resources = self.report["resource_contract"]
        self.assertLessEqual(
            resources["rational_recurrence_states"],
            resources["maximum_rational_states"],
        )
        for key in (
            "finite_fields_enumerated",
            "irreducibles_enumerated",
            "polynomials_enumerated",
            "curves_enumerated",
            "zeros_enumerated",
        ):
            self.assertEqual(resources[key], 0)
        theorem = self.report["exact_theorem"]
        self.assertIn("q^M/d^2", theorem["exact_layer"])
        self.assertIn("D_(2j+epsilon)", theorem["top_channel"])

    def test_source_locks_and_note_contract(self) -> None:
        MODULE._check_source_blobs()
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "harmonic-square budget",
            "primitive exterior channel",
            "macroscopic number of such layers",
            "does not claim that",
            "known or folklore",
            "do not count zeros",
        ):
            self.assertIn(marker, note)

    def test_optimized_mode_replays_same_theorem(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=8.0,
        )
        self.assertIn("EXACT_UNIFORM_LAYER_BOUND", completed.stdout)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()
