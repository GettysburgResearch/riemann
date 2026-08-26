"""Tests for the checkerboard phase-Gram Wick spectrum."""

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
    / "ffps_checkerboard_phase_wick_spectrum.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_CHECKERBOARD_PHASE_WICK_SPECTRUM.md")

SPEC = importlib.util.spec_from_file_location(
    "ffps_checkerboard_phase_wick", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load checkerboard phase-Wick module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CheckerboardPhaseWickSpectrumTests(unittest.TestCase):
    def test_bounded_replay(self) -> None:
        report = MODULE.run_checks()
        self.assertEqual(report["status"], "EXACT_WICK_LEVERAGE_SEPARATION")
        self.assertEqual(report["resource_ledger"]["subset_rows"], 510)

    def test_two_prime_exact_spectrum(self) -> None:
        spectrum, rows = MODULE.restricted_character_spectrum((5, 13))
        self.assertEqual(rows, 12)
        self.assertEqual(dict(spectrum), {43: 1, 37: 1, 52: 4})
        minimum, minimizers, subset_rows = MODULE.subset_minimum((5, 13))
        self.assertEqual(minimum, 37)
        self.assertEqual(set(minimizers), {1, 2})
        self.assertEqual(subset_rows, 4)

    def test_two_prime_wick_and_leverage_ledgers_are_distinct(self) -> None:
        row, _ = MODULE.panel_row((5, 13))
        self.assertEqual(row["phase_atomic_diagonal"], 48)
        self.assertEqual(row["restricted_row_sum"], 43)
        self.assertEqual(row["sharp_phase_wick_repair"], 11)
        self.assertEqual(row["phase_wick_repair_fraction"], "11/48")
        self.assertEqual(row["selected_covariance_wick_repair"], 1)
        self.assertEqual(row["full_leverage"], "4/7")
        self.assertEqual(row["checkerboard_leverage"], "24/43")
        self.assertEqual(row["leverage_ratio"], "42/43")

    def test_subset_minimum_matches_full_spectrum_on_small_panels(self) -> None:
        for primes in ((5,), (5, 13), (5, 13, 17)):
            spectrum, _ = MODULE.restricted_character_spectrum(primes)
            minimum, _, _ = MODULE.subset_minimum(primes)
            self.assertEqual(min(spectrum), minimum)

    def test_exact_asymptotic_bounds_hold_on_prefixes(self) -> None:
        for length in range(1, len(MODULE.PRIME_PANEL) + 1):
            row, _ = MODULE.panel_row(MODULE.PRIME_PANEL[:length])
            repair = Fraction(row["phase_wick_repair_fraction"])
            repair_lower = Fraction(row["repair_fraction_lower_bound"])
            ratio = Fraction(row["leverage_ratio"])
            ratio_upper = Fraction(row["leverage_ratio_upper_bound"])
            self.assertGreaterEqual(repair, repair_lower)
            self.assertLessEqual(ratio, ratio_upper)
        final, _ = MODULE.panel_row(MODULE.PRIME_PANEL)
        self.assertGreater(
            Fraction(final["phase_wick_repair_fraction"]), Fraction(4, 5)
        )

    def test_invalid_panels_fail_closed(self) -> None:
        for panel in ((), (5, 5), (3,), (9,), (True,)):
            with self.assertRaises(ValueError):
                MODULE.validate_panel(panel)
        with self.assertRaises(RuntimeError):
            MODULE.restricted_character_spectrum((5, 13, 17, 29))

    def test_optimized_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("EXACT_WICK_LEVERAGE_SEPARATION", completed.stdout)

    def test_note_firewalls(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "formal product-Gram theorem",
            "Wick--leverage separation theorem",
            "does not rule out the hard-mask route",
            "OPEN / CENTRAL",
        ):
            self.assertIn(marker, note)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()
