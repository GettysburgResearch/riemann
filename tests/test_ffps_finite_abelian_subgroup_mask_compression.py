"""Tests for finite-abelian subgroup-mask compression."""

from __future__ import annotations

import ast
import importlib.util
import subprocess
import sys
import unittest
from fractions import Fraction
from itertools import pairwise
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_finite_abelian_subgroup_mask_compression.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_FINITE_ABELIAN_SUBGROUP_MASK_COMPRESSION.md")

SPEC = importlib.util.spec_from_file_location("ffps_abelian_mask", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load finite-abelian mask module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FiniteAbelianSubgroupMaskCompressionTests(unittest.TestCase):
    def test_bounded_replay(self) -> None:
        report = MODULE.run_checks()
        self.assertEqual(
            report["schema"],
            "riemann.function_field.ffps_finite_abelian_subgroup_mask.v2",
        )
        self.assertEqual(report["status"], "EXACT_FINITE_ABELIAN_SUBGROUP_COMPRESSION")
        self.assertEqual(len(report["dimensions"]), 8)
        self.assertEqual(report["dimensions"][-1]["group_order"], 256)
        self.assertEqual(report["dimensions"][-1]["retained_group_order"], 128)
        self.assertNotIn("ambient_order", report["dimensions"][-1])

    def test_top_walsh_support_only(self) -> None:
        for dimension in range(1, 7):
            group_order = 1 << dimension
            support = [
                label
                for label in range(group_order)
                if MODULE.walsh_coefficient(dimension, label)
            ]
            self.assertEqual(support, [0, group_order - 1])

    def test_autocorrelation_is_principal_plus_top(self) -> None:
        dimension = 5
        top = (1 << dimension) - 1
        for shift in range(1 << dimension):
            self.assertEqual(
                MODULE.autocorrelation(dimension, shift),
                1 + MODULE.character(top, shift),
            )

    def test_two_prime_control(self) -> None:
        row = MODULE.panel_row((5, 13))
        self.assertEqual(row["native_amplitude"], 12)
        self.assertNotIn("ambient_order", row)
        self.assertEqual(row["hard_leverage"], "24/43")
        self.assertEqual(row["full_leverage"], "4/7")
        self.assertLess(Fraction(row["hard_leverage"]), Fraction(row["full_leverage"]))

    def test_exact_wick_spectrum_witness(self) -> None:
        witness, matrix_entries = MODULE.wick_spectrum_witness()
        self.assertEqual(witness["matrix"], ((0, 1), (1, 0)))
        self.assertEqual(witness["positive_eigenvalue"], 1)
        self.assertEqual(witness["negative_eigenvalue"], -1)
        self.assertEqual(witness["sharp_diagonal_repair"], 1)
        self.assertEqual(matrix_entries, 4)

    def test_direct_checkerboard_restricted_gram(self) -> None:
        control, matrix_entries = MODULE.direct_checkerboard_5_13()
        self.assertEqual(control["native_amplitude"], 12)
        self.assertEqual(control["retained_coordinates"], 6)
        self.assertEqual(control["restricted_gram_energy"], 258)
        self.assertEqual(control["restricted_row_sum"], "43")
        self.assertEqual(control["optimizer_weight"], "2")
        self.assertEqual(control["restricted_leverage"], "24/43")
        self.assertEqual(control["complete_tensor_leverage"], "4/7")
        self.assertEqual(matrix_entries, 220)

    def test_prime_panel_ratio_decreases(self) -> None:
        rows = [
            MODULE.panel_row(MODULE.PRIME_PANEL[:length])
            for length in range(2, len(MODULE.PRIME_PANEL) + 1)
        ]
        ratios = [Fraction(row["hard_to_full_ratio"]) for row in rows]
        self.assertTrue(all(right < left for left, right in pairwise(ratios)))

    def test_invalid_inputs_fail_closed(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.normalized_mask(0, 0)
        with self.assertRaises(ValueError):
            MODULE.walsh_coefficient(2, 4)
        with self.assertRaises(ValueError):
            MODULE.autocorrelation(2, 4)
        with self.assertRaises(ValueError):
            MODULE.panel_row((5, 7))

    def test_optimized_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("EXACT_FINITE_ABELIAN_SUBGROUP_COMPRESSION", completed.stdout)

    def test_note_firewalls(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "checkerboard compression",
            "does **not** prove",
            "Rank compression is therefore",
            "native amplitude",
            "independently reconstructs the `(5,13)` restricted Gram",
            "No external novelty or priority claim",
        ):
            self.assertIn(marker, note)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()
