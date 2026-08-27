from __future__ import annotations

import importlib.util
import json
import subprocess
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_truncated_beta_zero_tube_residue_law.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("beta_zero_tube", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load beta zero-tube producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class TruncatedBetaZeroTubeResidueLawTest(unittest.TestCase):
    def test_frozen_source(self) -> None:
        subject.check_source_contract()

    def test_cauchy_masses(self) -> None:
        self.assertEqual(subject.cauchy_mass_over_pi(1), Fraction(1))
        self.assertEqual(subject.cauchy_mass_over_pi(2), Fraction(1, 2))
        self.assertEqual(subject.cauchy_mass_over_pi(3), Fraction(3, 8))
        self.assertEqual(subject.cauchy_mass_over_pi(4), Fraction(5, 16))

    def test_real_c_central_binomial_coefficients(self) -> None:
        self.assertEqual(
            [subject.real_c_residue_coefficient(m) for m in range(1, 7)],
            [1, 2, 6, 20, 70, 252],
        )

    def test_fixed_notch_constants(self) -> None:
        self.assertEqual(subject.notch_real_c_coefficient(2, 1), Fraction(1, 2))
        self.assertEqual(subject.notch_real_c_coefficient(3, 1), Fraction(1, 2))
        self.assertEqual(subject.notch_real_c_coefficient(3, 2), Fraction(3, 8))
        self.assertEqual(subject.notch_real_c_coefficient(4, 3), Fraction(5, 16))

    def test_O_one_over_c_threshold(self) -> None:
        rows = subject.notch_table()
        for row in rows:
            multiplicity = row["multiplicity"]
            half_order = row["notch_weight_order"] // 2
            self.assertEqual(
                row["compatible_with_O_1_over_c"],
                multiplicity <= half_order + 1,
            )

    def test_autocorrelation_notch_and_leakage(self) -> None:
        panel = subject.autocorrelation_panel()
        self.assertEqual(panel["autocorrelation_notch_order"], 4)
        self.assertEqual(Fraction(panel["absolute_lag_moment"]), -4)
        self.assertEqual(Fraction(panel["cumulative_norm_square"]), 2)
        self.assertEqual(Fraction(panel["max_tilt_linear_coefficient"]), 2)

    def test_toy_residue_powers(self) -> None:
        rows = subject.toy_residue_panel()["real_c_rows"]
        self.assertEqual([row["power_of_c"] for row in rows], [-1, -3, -5, -7])
        self.assertEqual(
            [Fraction(row["coefficient"]) for row in rows],
            [Fraction(15, 4), Fraction(15, 2), Fraction(45, 2), Fraction(75)],
        )

    def test_fixture_and_scope(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(result, fixture)
        self.assertTrue(result["scope"]["height_window_fixed"])
        self.assertFalse(result["scope"]["critical_zeros_computed"])
        self.assertFalse(result["scope"]["infinite_t_tail_controlled"])
        self.assertFalse(result["scope"]["O_1_over_c_bound_proved"])
        self.assertFalse(result["scope"]["rh_or_grh_proved"])

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.cauchy_mass_over_pi(0)
        with self.assertRaises(ValueError):
            subject.notch_mass_over_pi(2, 2)
        with self.assertRaises(ValueError):
            subject.discrete_autocorrelation(())

    def test_producer_check(self) -> None:
        completed = subprocess.run(
            ["python", "-B", str(SCRIPT), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=15,
        )
        self.assertEqual(completed.stdout, "")


if __name__ == "__main__":
    unittest.main()
