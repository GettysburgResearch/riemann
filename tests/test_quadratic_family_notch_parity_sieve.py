"""Tests for the exact all-profile odd-notch parity sieve."""

from __future__ import annotations

import ast
import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_notch_parity_sieve.py"
)
NOTE_PATH = MODULE_PATH.with_name("QUADRATIC_FAMILY_NOTCH_PARITY_SIEVE.md")

SPEC = importlib.util.spec_from_file_location(
    "quadratic_family_notch_parity_sieve", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load notch parity-sieve module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class QuadraticFamilyNotchParitySieveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = MODULE.build_report()

    def test_all_bounded_profiles_match_three_parity_adapters(self) -> None:
        profile_count = 0
        for n_value in range(2, 9):
            for degrees in MODULE.integer_partitions(2 * n_value - 1):
                row = MODULE.profile_parity_certificate(n_value, degrees)
                profile_count += 1
                self.assertEqual(row["S_parity"], row["binary_subset_parity"])
                self.assertEqual(
                    row["S_parity"],
                    row["a_n_parity"] ^ row["a_n_minus_1_parity"],
                )
        self.assertGreater(profile_count, 250)

    def test_binary_product_equals_geometric_inverse(self) -> None:
        degrees = [2, 2, 5]
        coefficients = MODULE.profile_a_parities(degrees, 30)
        for target in range(31):
            self.assertEqual(
                coefficients[target], MODULE.subset_sum_parity(degrees, target)
            )

    def test_all_family_degrees_for_odd_conductors(self) -> None:
        rows_checked = 0
        for conductor_degree in range(3, 12, 2):
            for degrees in MODULE.integer_partitions(conductor_degree):
                for family_degree in range(11):
                    row = MODULE.general_parity_certificate(family_degree, degrees)
                    self.assertEqual(
                        row["S_parity"],
                        row["a_r_parity"] ^ row["a_r_minus_1_parity"],
                    )
                    self.assertEqual(row["S_parity"], row["binary_subset_parity"])
                    rows_checked += 1
        self.assertGreater(rows_checked, 1_000)

    def test_support_irreducible_profile_is_parity_even(self) -> None:
        for n_value in range(2, 16):
            row = MODULE.profile_parity_certificate(n_value, [2 * n_value - 1])
            self.assertEqual(row["S_parity"], 0)
            self.assertFalse(row["certified_nonzero"])

    def test_shallow_collapse_to_middle_degree_multiplicity(self) -> None:
        rows_checked = 0
        for n_value in range(4, 24):
            h_value = n_value // 2
            epsilon = n_value % 2
            for depth in range(h_value):
                if h_value <= 3 * depth + epsilon:
                    continue
                d_value = h_value - depth
                profile = [d_value, 2 * n_value - 1 - d_value]
                row = MODULE.shallow_layer_certificate(n_value, depth, profile)
                self.assertTrue(row["condition_h_gt_3j_plus_epsilon"])
                self.assertEqual(row["S_parity"], row["m_h_parity"])
                rows_checked += 1
        self.assertGreater(rows_checked, 20)

    def test_shallow_odd_m_h_is_nonzero_certificate(self) -> None:
        row = MODULE.shallow_layer_certificate(10, 1, [4, 5, 10])
        self.assertTrue(row["condition_h_gt_3j_plus_epsilon"])
        self.assertEqual(row["m_h"], 1)
        self.assertEqual(row["S_parity"], 1)
        self.assertTrue(row["certified_nonzero_from_m_h"])

    def test_split_profile_lucas_bit_control(self) -> None:
        odd_rows = []
        for n_value in range(2, 40):
            row = MODULE.split_profile_certificate(n_value)
            self.assertEqual(row["S_parity"], int(row["no_binary_carry"]))
            if row["S_parity"]:
                odd_rows.append(n_value)
        self.assertEqual(odd_rows[:4], [2, 6, 10, 18])

    def test_invalid_inputs_fail_closed(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.profile_parity_certificate(3, [5, 1])
        with self.assertRaises(ValueError):
            MODULE.subset_sum_parity([], 4)
        with self.assertRaises(ValueError):
            MODULE.shallow_layer_certificate(8, 1, [2, 13])
        with self.assertRaises(ValueError):
            MODULE.split_profile_certificate(True)
        with self.assertRaises(ValueError):
            MODULE.general_parity_certificate(3, [2, 2])

    def test_report_resources_and_firewalls(self) -> None:
        resources = self.report["resource_contract"]
        self.assertLessEqual(
            resources["integer_degree_profiles"], resources["maximum_profiles"]
        )
        self.assertLessEqual(
            resources["coefficient_states"], resources["maximum_coefficient_states"]
        )
        self.assertLessEqual(
            resources["general_family_degree_rows"],
            resources["maximum_general_rows"],
        )
        for key in (
            "finite_fields_enumerated",
            "irreducibles_enumerated",
            "polynomials_enumerated",
            "curves_enumerated",
            "zeros_enumerated",
        ):
            self.assertEqual(resources[key], 0)
        self.assertTrue(
            any(
                "necessary but not sufficient" in row
                for row in self.report["firewalls"]
            )
        )

    def test_source_lock_and_note_contract(self) -> None:
        MODULE._check_source_blob()
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "all-profile congruence",
            "labelled binary atoms",
            "h>3j+\\varepsilon",
            "every raw zero lies",
            "No numerical density follows",
            "not zeros of an individual `L`-function",
            "known or folklore",
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
        self.assertIn("EXACT_ALL_PROFILE_MOD_TWO_SIEVE", completed.stdout)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()
