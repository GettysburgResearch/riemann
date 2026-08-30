"""Exact and hostile controls for critical graded-product statements."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "critical_grade_boundary", HERE / "critical_boundary_replay.py"
)
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)


class RationalLogTests(unittest.TestCase):
    def test_log_one(self):
        self.assertEqual(C.log_interval(1), (0, 0))

    def test_log_two_elementary_integral_bounds(self):
        low, high = C.log_interval(2)
        self.assertGreater(low, Fraction(2, 3))
        self.assertLess(high, Fraction(7, 10))

    def test_inverse_and_power_identities_enclosed(self):
        two = C.log_interval(2)
        half = C.log_interval(Fraction(1, 2))
        self.assertLessEqual(two[0] + half[0], 0)
        self.assertGreaterEqual(two[1] + half[1], 0)
        power = C.log_interval(1024)
        self.assertLessEqual(power[0], 10 * two[1])
        self.assertGreaterEqual(power[1], 10 * two[0])

    def test_directed_rounding_both_signs(self):
        rounded = C.rounded((Fraction(-1, 3), Fraction(1, 3)), 6)
        self.assertLessEqual(rounded[0], Fraction(-1, 3))
        self.assertGreaterEqual(rounded[1], Fraction(1, 3))

    def test_invalid_logs_rejected(self):
        for value in (0, -1, True, 0.5):
            with self.subTest(value=value), self.assertRaises((TypeError, ValueError)):
                C.log_interval(value)


class CriticalSourceTests(unittest.TestCase):
    def test_block_distribution_stays_compressed(self):
        result = C.distribution_control(4, 24)
        self.assertGreater(result["singular_value_count"], 10**10)
        self.assertFalse(result["expanded_singular_value_list"])

    def test_two_endpoint_constants_are_distinct(self):
        result = C.distribution_control(2, 16)
        low = [Fraction(*value) for value in result["theorem_liminf"]]
        high = [Fraction(*value) for value in result["theorem_limsup"]]
        self.assertLess(low[1], high[0])

    def test_first_boundary_constant_is_native_derivative(self):
        result = C.boundary_rate_control(2, 16)
        self.assertEqual(result["rho_Fprime_at_negative_rho"], [16, 81])

    def test_other_rank_strips(self):
        for q in (3, 4):
            result = C.boundary_rate_control(q, 16)
            self.assertEqual(
                Fraction(*result["rho_Fprime_at_negative_rho"]),
                (1 + Fraction(1, q)) ** (-(q + 2)),
            )

    def test_real_and_complex_critical_arcs(self):
        for phase in (C.R.ONE, C.R.I, C.R.neg(C.R.I)):
            C.arc_control(phase)

    def test_heldout_critical_phase(self):
        C.arc_control((Fraction(3, 5), Fraction(4, 5)))

    def test_exceptional_zero_cannot_enter_arc_check(self):
        with self.assertRaises(ValueError):
            C.arc_control(C.R.neg(C.R.ONE))

    def test_nonunit_phase_rejected(self):
        with self.assertRaises(ValueError):
            C.arc_control((1, 1))

    def test_caps_prevent_expanded_state(self):
        for q, cut in ((1, 8), (5, 8), (2, 25), (True, 8)):
            with self.subTest(q=q, cut=cut), self.assertRaises((TypeError, ValueError)):
                C.distribution_control(q, cut)

    def test_frozen_source_authenticated(self):
        C.authenticate_frozen()

    def test_forged_critical_fixture_rejected(self):
        with self.assertRaises(ValueError):
            C.check_payload(
                {"schema": "koszul-critical-grade-boundary-v1", "status": "PASS"}
            )


if __name__ == "__main__":
    unittest.main()
