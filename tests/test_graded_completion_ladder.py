"""Independent bounded controls for the graded-completion source theorem."""

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "research/l-families/atlas/generalized/graded-completion-lab/replay.py"
SPEC = importlib.util.spec_from_file_location("graded_completion_ladder", FILE)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class GradedCompletionTests(unittest.TestCase):
    def test_odd_divisor_initial_values(self):
        self.assertEqual(
            [R.anti_dimension(n) for n in range(2, 14, 2)], [1, 2, 5, 16, 51, 170]
        )

    def test_full_character_comparison(self):
        for n in range(2, 65, 2):
            row = R.source_row(n)
            self.assertEqual(
                2 * R.anti_dimension(n), row["characters"][0] - row["characters"][1]
            )

    def test_low_grade_actual_irreducibles(self):
        self.assertEqual(R.source_row(2)["multiplicities"], [1, 0, 1])
        self.assertEqual(R.source_row(4)["multiplicities"], [0, 1, 1])
        self.assertEqual(R.source_row(8)["multiplicities"], [4, 6, 10])

    def test_error_bound_even_without_odd_divisor(self):
        for j in (1, 2, 4, 8, 16, 32, 64):
            self.assertEqual(R.anti_dimension(2 * j), 4**j // (4 * j))

    def test_nontrivial_odd_divisor(self):
        self.assertEqual(R.anti_dimension(6), (2**6 - 2**2) // 12)
        self.assertEqual(R.anti_dimension(30), (2**30 - 2**10 - 2**6 + 2**2) // 60)

    def test_multiplicity_input_caps(self):
        for bad in (True, 0, -2, 3, 130, 2.0, "2"):
            with self.assertRaises(ValueError):
                R.anti_dimension(bad)

    def test_source_class_caps(self):
        with self.assertRaises(ValueError):
            R.source_log("other", 2)
        with self.assertRaises(ValueError):
            R.source_row(65)

    def test_first_factors(self):
        q7 = R.ladder_coefficients(7, 4, 16)
        q49 = R.ladder_coefficients(49, 4, 16)
        self.assertEqual(
            [(i, v) for i, v in enumerate(q7) if v], [(0, 1), (8, 14), (16, 49)]
        )
        self.assertEqual(q49[4], 28)
        self.assertEqual(q49[8], 294)

    def test_formal_algorithms_agree(self):
        for field in (7, 49):
            self.assertEqual(
                R.ladder_coefficients(field, 32, 48),
                R.logarithmic_coefficients(field, 32, 48),
            )

    def test_stabilization_exact_first_difference(self):
        old = R.ladder_coefficients(49, 4, 16)
        new = R.ladder_coefficients(49, 6, 16)
        self.assertEqual(old[:6], new[:6])
        self.assertEqual(new[6] - old[6], 70)

    def test_base_change_keeps_grading(self):
        old = R.ladder_coefficients(7, 16, 32)
        new = R.ladder_coefficients(49, 16, 16)
        substituted = [new[i // 2] if i % 2 == 0 else 0 for i in range(33)]
        self.assertEqual(substituted, R.multiply(old, old, 32))
        self.assertNotEqual(R.ladder_coefficients(49, 16, 32), R.multiply(old, old, 32))

    def test_lattice_support(self):
        for field, modulus in ((7, 4), (49, 2)):
            for i, c in enumerate(R.ladder_coefficients(field, 32, 48)):
                if i % modulus:
                    self.assertEqual(c, 0)

    def test_point_count_infinity(self):
        data = R.point_counts()
        self.assertEqual(data["proper_counts"], [8, 8])
        self.assertEqual(data["infinity_counts"], [1, 2])
        self.assertEqual(data["F49_traces_from_squaring"], [-14, -14])
        self.assertFalse(data["F49_enumerated"])

    def test_log_interval_refines_without_float(self):
        lo, hi = R.log1p_interval(Fraction(7, 16), 8)
        fine_lo, fine_hi = R.log1p_interval(Fraction(7, 16), 16)
        self.assertLessEqual(lo, fine_lo)
        self.assertLessEqual(fine_hi, hi)
        self.assertLess(hi - lo, Fraction(1, 10**12))

    def test_outward_rounding_negative_values(self):
        value = Fraction(-1, 3)
        low, high = R.dyadic_interval(value, value, 16)
        self.assertLessEqual(low, value)
        self.assertGreaterEqual(high, value)
        self.assertEqual(high - low, Fraction(1, 2**16))

    def test_critical_products_square(self):
        first = R.critical_log_interval(7, 16)["critical_log_interval"]
        second = R.critical_log_interval(49, 16)["critical_log_interval"]
        lo1, hi1 = [Fraction(*q) for q in first]
        lo2, hi2 = [Fraction(*q) for q in second]
        self.assertLessEqual(lo2, 2 * hi1)
        self.assertGreaterEqual(hi2, 2 * lo1)

    def test_interval_caps(self):
        for bad in (Fraction(-1), Fraction(2), 0.5):
            with self.assertRaises(ValueError):
                R.log1p_interval(bad)
        with self.assertRaises(ValueError):
            R.critical_log_interval(7, 12)

    def test_strict_types(self):
        self.assertFalse(R.strict_equal({"a": True}, {"a": 1}))
        self.assertFalse(R.strict_equal({"a": 1.0}, {"a": 1}))
        self.assertFalse(R.strict_equal([1, 2], [1]))

    def test_frozen_replay_and_artifact(self):
        candidate = json.loads(R.FIXTURE.read_text())
        R.check_payload(candidate)

    def test_artifact_tamper_rejected(self):
        candidate = json.loads(R.FIXTURE.read_text())
        candidate["actual_curves"]["proper_counts"][0] = 9
        with self.assertRaises(ValueError):
            R.check_payload(candidate)


if __name__ == "__main__":
    unittest.main()
