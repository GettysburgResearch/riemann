"""Tests for the sharp Wick-centered domination boundary."""

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
    / "ffps_wick_centered_domination_boundary.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_WICK_CENTERED_DOMINATION_BOUNDARY.md")

SPEC = importlib.util.spec_from_file_location("ffps_wick_boundary", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load Wick boundary module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class WickCenteredDominationBoundaryTests(unittest.TestCase):
    def test_all_bounded_collision_blocks(self) -> None:
        report = MODULE.run_checks()
        self.assertEqual(report["status"], "EXACT_SHARP_WICK_DOMINATION_BOUNDARY")
        self.assertGreater(report["finite_replay"]["rows"], 400)

    def test_ternary_double_collision_has_both_signs(self) -> None:
        row = MODULE.collision_blocks(3, 2, 2)
        self.assertEqual(row["u"], "1/2")
        self.assertEqual(row["positive_eigenvalue"], "1/2")
        self.assertEqual(row["negative_eigenvalue"], "-1/2")

    def test_collision_multiplicity_spectrum(self) -> None:
        row = MODULE.collision_blocks(8, 3, 7)
        u_value = Fraction(8, 3) - 1
        self.assertEqual(row["positive_eigenvalue"], str(6 * u_value))
        self.assertEqual(row["negative_eigenvalue"], str(-u_value))
        self.assertEqual(row["negative_multiplicity"], 6)

    def test_two_exact_witnesses(self) -> None:
        u_value = Fraction(5, 2) - 1
        centered = MODULE.scale(
            u_value,
            MODULE.subtract(MODULE.all_ones(2), MODULE.identity(2)),
        )
        self.assertEqual(
            MODULE.quadratic_form(centered, (Fraction(1), Fraction(1))),
            2 * u_value,
        )
        self.assertEqual(
            MODULE.quadratic_form(centered, (Fraction(1), Fraction(-1))),
            -2 * u_value,
        )

    def test_invalid_inputs_fail_closed(self) -> None:
        for args in ((1, 1, 2), (3, 0, 2), (3, 3, 2), (3, 2, 1)):
            with self.assertRaises(ValueError):
                MODULE.collision_blocks(*args)

    def test_optimized_producer_replays(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("EXACT_SHARP_WICK_DOMINATION_BOUNDARY", completed.stdout)

    def test_note_firewalls(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "sharp constant one",
            "affine diagonal subtraction",
            "no varying-place sum",
            "OPEN / RH-BEARING",
            "No external novelty or priority claim",
        ):
            self.assertIn(marker, note)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()
