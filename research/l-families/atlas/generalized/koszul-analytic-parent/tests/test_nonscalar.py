"""Native source and boundary controls for the involution family."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "nonscalar_radius", HERE / "nonscalar_replay.py"
)
N = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(N)


class NativeInvolutionTests(unittest.TestCase):
    def test_source_even_part(self):
        self.assertEqual(N.native_sequence(3, 6, True), [1, 0, 6, 0, 15, 0, 28])

    def test_native_rational_numerator(self):
        self.assertEqual(N.native_control(3)["source_even_numerator"], [1, 0, 3, 0])
        self.assertEqual(N.native_control(4)["source_even_numerator"], [1, 0, 6, 0, 1])

    def test_actual_low_grade_lie_characters(self):
        rows = N.source_characters(3, 3)
        self.assertEqual([row[1] for row in rows], [0, -3, 0])
        self.assertEqual([row[0] for row in rows], [6, 3, 2])

    def test_all_involution_eigenspaces_are_actual(self):
        for k in (3, 4, 5):
            for n, (dimension, trace, plus, minus) in enumerate(
                N.source_characters(k, 64), 1
            ):
                self.assertEqual(plus + minus, dimension)
                self.assertEqual(plus - minus, trace)
                self.assertGreaterEqual(minus, 0)
                self.assertGreaterEqual(plus, 0)
                if n % 2:
                    self.assertEqual(trace, 0)

    def test_wrong_identity_action_is_detected(self):
        dimension, trace, _, _ = N.source_characters(3, 2)[1]
        self.assertNotEqual(trace, dimension)

    def test_rank_and_degree_caps(self):
        for k, degree in ((2, 12), (6, 12), (3, 65), (True, 4)):
            with (
                self.subTest(k=k, degree=degree),
                self.assertRaises((TypeError, ValueError)),
            ):
                N.source_characters(k, degree)


class NonscalarBoundaryTests(unittest.TestCase):
    def test_paired_odd_boundary_block(self):
        interval = N.finite_log(2)
        expected = N.C.log_interval(Fraction(1, 8))
        self.assertLessEqual(interval[0], expected[1])
        self.assertGreaterEqual(interval[1], expected[0])

    def test_exact_nonscalar_regular_part(self):
        result = N.boundary_control(64)
        self.assertFalse(result["ordinary_trace_class"])
        self.assertTrue(result["Schatten_two"])
        self.assertLess(Fraction(*result["proved_absolute_log_error"]), Fraction(1, 10))

    def test_odd_and_even_cutoffs_use_floor(self):
        N.boundary_control(63)
        N.boundary_control(64)

    def test_real_point_past_trace_class(self):
        result = N.real_control(Fraction(11, 20), 64)
        self.assertFalse(result["ordinary_trace_class"])
        self.assertTrue(result["within_nonscalar_grade_radius"])

    def test_heldout_real_point(self):
        N.real_control(Fraction(9, 16), 48)

    def test_past_nonscalar_radius_rejected(self):
        with self.assertRaises(ValueError):
            N.real_control(Fraction(7, 12), 32)

    def test_log1p_exact_control(self):
        low, high = N.log1p_interval(Fraction(1, 3))
        reference = N.C.log_interval(Fraction(4, 3))
        self.assertLessEqual(low, reference[1])
        self.assertGreaterEqual(high, reference[0])

    def test_log1p_invalid_domain(self):
        for value in (Fraction(-1), Fraction(1), True, 0.25):
            with self.subTest(value=value), self.assertRaises(ValueError):
                N.log1p_interval(value)

    def test_frozen_sources(self):
        N.authenticate_frozen()

    def test_forged_fixture(self):
        with self.assertRaises(ValueError):
            N.check_payload(
                {"schema": "koszul-nonscalar-grade-radius-v1", "status": "PASS"}
            )


if __name__ == "__main__":
    unittest.main()
