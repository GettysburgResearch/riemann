"""Tests for exact first-boundary trace-zero extinction."""

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
    / "quadratic_family_first_boundary_trace_zero_density.py"
)
NOTE_PATH = MODULE_PATH.with_name(
    "QUADRATIC_FAMILY_FIRST_BOUNDARY_TRACE_ZERO_DENSITY.md"
)

SPEC = importlib.util.spec_from_file_location(
    "quadratic_family_first_boundary_trace_zero_density", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load first-boundary module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class QuadraticFamilyFirstBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = MODULE.build_report()

    def test_exceptional_n3_counts(self) -> None:
        expected = {
            3: (72, 30, 102, 162),
            5: (1024, 406, 1430, 2500),
            7: (5712, 2184, 7896, 14406),
        }
        for row in self.report["exceptional_n3_prime_field_controls"]:
            self.assertEqual(
                (
                    row["support_forced"],
                    row["first_boundary_trace_zero"],
                    row["all_raw_zeros_in_first_two_strata"],
                    row["squarefree_quintics"],
                ),
                expected[row["q"]],
            )

    def test_even_first_boundary_is_positive(self) -> None:
        for n_value in range(4, 18, 2):
            for multiplicity in (1, 2, 4):
                row = MODULE.first_boundary_certificate(5, n_value, multiplicity)
                self.assertTrue(row["nonzero"])
                self.assertEqual(row["residual"], f"{multiplicity}*D_0={multiplicity}")

    def test_odd_first_boundary_has_odd_D1(self) -> None:
        for n_value in range(5, 18, 2):
            row = MODULE.first_boundary_certificate(7, n_value, 3)
            self.assertTrue(row["nonzero"])
            self.assertEqual(row["D_1_parity"], 1)
            self.assertGreaterEqual(row["h"], 2)

    def test_n3_is_the_unique_unresolved_symbolic_row(self) -> None:
        row = MODULE.first_boundary_certificate(3, 3, 1)
        self.assertIsNone(row["nonzero"])
        self.assertIn("unique exception", row["certificate"])

    def test_invalid_inputs_fail_closed(self) -> None:
        for args in ((2, 5, 1), (3, 1, 1), (3, 5, 0), (True, 5, 1)):
            with self.assertRaises(ValueError):
                MODULE.first_boundary_certificate(*args)
        with self.assertRaises(ValueError):
            MODULE.exceptional_quintic_control(11)

    def test_source_locks_and_note_boundaries(self) -> None:
        MODULE._check_source_blobs()
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "entire first boundary is nonzero",
            "sum of exactly `q` values",
            "first boundary contributes no additional",
            "O_j\\!\\left({q^M\\over M^2}\\right)",
            "no fixed number of boundary layers",
            "second boundary",
            "not zeros of an individual L-function",
        ):
            self.assertIn(marker, note)

    def test_optimized_mode_replays_same_control(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=12.0,
        )
        self.assertIn("EXACT_FIRST_BOUNDARY_EXTINCTION", completed.stdout)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()
