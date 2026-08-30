"""Native S3 character, grade-band and positive rational block controls."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("s3_cutoff", HERE / "s3_cutoff_replay.py")
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)


def overlaps(left, right):
    return left[0] <= right[1] and left[1] >= right[0]


class SourceCharacterTests(unittest.TestCase):
    def test_actual_s3_low_characters(self):
        self.assertEqual([C.source_grade(n, 2)[1] for n in (1, 2, 3)], [0, 1, 0])
        self.assertEqual([C.source_grade(n, 3)[1] for n in (1, 2, 3)], [0, 0, -1])

    def test_source_adams_and_full_pbw_identities(self):
        self.assertEqual(C.character_control()["source_Adams_and_PBW_degree"], 24)

    def test_every_bounded_source_eigenspace_is_integral(self):
        for n in range(1, 257):
            for d in (2, 3):
                dimension, trace, eigen = C.source_grade(n, d)
                self.assertEqual(sum(eigen), dimension)
                self.assertGreaterEqual(min(eigen), 0)
                if n % d:
                    self.assertEqual(trace, 0)
                    self.assertEqual(len(set(eigen)), 1)

    def test_source_dimension_grows_without_expanded_states(self):
        dimension, _, eigen = C.source_grade(256, 3)
        self.assertGreater(dimension, 2**240)
        self.assertEqual(len(eigen), 3)

    def test_actual_permutation_action_differs_from_previous_identity_W(self):
        self.assertEqual(C.source_grade(2, 2)[1], 1)
        self.assertNotEqual(C.source_grade(2, 2)[1], -3)

    def test_warm_cache_does_not_bypass_type_checks(self):
        C.source_grade(1, 2)
        C.finite_log(2, 2)
        for n in (True, 1.0):
            with self.subTest(n=n), self.assertRaises((TypeError, ValueError)):
                C.source_grade(n, 2)
        with self.assertRaises((TypeError, ValueError)):
            C.finite_log(2, 2.0)
        with self.assertRaises((TypeError, ValueError)):
            C.finite_log(2, 2, -0.5)

    def test_source_bounds(self):
        for n, d in ((257, 2), (0, 2), (3, 4)):
            with self.subTest(n=n, d=d), self.assertRaises((TypeError, ValueError)):
                C.source_grade(n, d)


class NativeBlockTests(unittest.TestCase):
    def test_first_two_whole_grades_are_one_third(self):
        reference = C.weighted_log(Fraction(1, 3))
        self.assertTrue(overlaps(C.finite_log(2, 2), reference))
        self.assertTrue(overlaps(C.finite_log(3, 2), reference))

    def test_cycle_third_grade_restores_four_ninths(self):
        self.assertTrue(overlaps(C.finite_log(3, 3), C.weighted_log(Fraction(4, 9))))

    def test_harmonic_band_uses_actual_grade_floor(self):
        self.assertEqual(C.finite_band(2, 2, Fraction(-1, 2)), Fraction(1, 4))
        self.assertEqual(C.finite_band(3, 2, Fraction(-1, 2)), Fraction(1, 2))
        self.assertNotEqual(
            C.finite_band(3, 255, Fraction(-1, 2)),
            C.finite_band(3, 256, Fraction(-1, 2)),
        )

    def test_critical_corrected_log_has_small_certified_error(self):
        for d in (2, 3):
            result = C.cutoff_control(d, 256)
            self.assertLess(
                Fraction(*result["proved_absolute_log_error"]), Fraction(1, 100)
            )
            self.assertFalse(result["source_operator_trace_class"])
            self.assertTrue(result["Abel_limit_differs"])

    def test_both_exterior_ray_controls(self):
        for d, x in ((2, Fraction(9, 16)), (3, Fraction(64, 125))):
            for sign in (-1, 1):
                result = C.cutoff_control(d, 256, sign * x)
                self.assertLess(
                    Fraction(*result["proved_absolute_log_error"]), Fraction(1, 100)
                )

    def test_positive_and_negative_y_bands_are_distinct(self):
        self.assertGreater(C.finite_band(2, 32, Fraction(-9, 16)), 0)
        self.assertGreater(C.finite_band(2, 32, Fraction(9, 16)), 0)
        self.assertLess(C.finite_band(2, 33, Fraction(9, 16)), 0)

    def test_invalid_source_and_remainder_radii(self):
        with self.assertRaises(ValueError):
            C.finite_log(2, 16, Fraction(2, 3))
        with self.assertRaises(ValueError):
            C.error_bound(2, 32, Fraction(-1, 2), Fraction(2, 3), Fraction(3, 4))
        with self.assertRaises(ValueError):
            C.error_bound(3, 32, Fraction(-1, 2), Fraction(4, 5), Fraction(9, 10))


class ExactLogTests(unittest.TestCase):
    def test_zero_and_negative_weights(self):
        self.assertEqual(C.weighted_log(Fraction(3, 2), 0), (0, 0))
        positive = C.weighted_log(Fraction(3, 2), 7)
        negative = C.weighted_log(Fraction(3, 2), -7)
        self.assertEqual(negative, (-positive[1], -positive[0]))

    def test_weighted_tiny_log_does_not_round_before_multiplication(self):
        interval = C.weighted_log(1 + Fraction(1, 2**200), 2**200)
        self.assertLessEqual(interval[0], 1)
        self.assertGreaterEqual(interval[1], 1 - Fraction(1, 2**199))
        self.assertGreater(interval[0], Fraction(99, 100))

    def test_log_multiplicativity_independent_control(self):
        first = C.weighted_log(Fraction(3, 2))
        second = C.weighted_log(Fraction(1, 2))
        product = C.weighted_log(Fraction(3, 4))
        self.assertTrue(overlaps((first[0] + second[0], first[1] + second[1]), product))

    def test_invalid_log_inputs_fail_closed(self):
        for value in (0, -1, True, 1.5, Fraction(1, 9)):
            with self.subTest(value=value), self.assertRaises((TypeError, ValueError)):
                C.weighted_log(value)
        with self.assertRaises(ValueError):
            C.weighted_log(Fraction(2), 2**600)

    def test_authentication(self):
        C.authenticate_frozen()

    def test_forged_fixture(self):
        with self.assertRaises(ValueError):
            C.check_payload(
                {"schema": "native-s3-grade-cutoff-anomaly-v1", "status": "PASS"}
            )


if __name__ == "__main__":
    unittest.main()
