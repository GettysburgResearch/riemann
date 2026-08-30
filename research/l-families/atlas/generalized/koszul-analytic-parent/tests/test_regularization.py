"""Source-aware regularization checks; no floating-point transcendental calls."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "mixed_koszul_regularization", HERE / "regularization_replay.py"
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)
R = M.R


class MixedRankTests(unittest.TestCase):
    def test_independent_numerator_constructions(self):
        for ranks in ((2, 3), (3, 3), (2, 2, 2), (2, 3, 4), (1, 3, 4, 1)):
            with self.subTest(ranks=ranks):
                self.assertEqual(
                    M.numerator_difference(ranks), M.numerator_differential(ranks)
                )

    def test_known_mixed_numerators(self):
        self.assertEqual(M.numerator_difference((3, 3)), [1, 4, 1])
        self.assertEqual(M.numerator_difference((2, 2, 2)), [1, 4, 1])
        self.assertEqual(M.numerator_difference((2, 5)), [1, 4])

    def test_finite_exceptions(self):
        self.assertEqual(M.deviations((4,), 8), [4, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(M.deviations((2, 2), 8), [4, 1, 0, 0, 0, 0, 0, 0])
        self.assertEqual(M.deviations((1, 1), 8), [1, 0, 0, 0, 0, 0, 0, 0])

    def test_growth_witness_not_just_nonconstant_numerator(self):
        self.assertFalse(M.finite_profile((3, 3)))
        result = M.mixed_control((3, 3))
        self.assertGreater(result["h1"], len(result["numerator"]) - 1)
        self.assertTrue(M.finite_profile((2, 2)))

    def test_rank_one_factors_do_not_change_dimensions(self):
        self.assertEqual(M.deviations((2, 3), 12), M.deviations((1, 2, 3, 1), 12))

    def test_new_method_recovers_frozen_deviations(self):
        self.assertEqual(
            M.deviations((2, 3), 24), [R.multiplicity(n) for n in range(1, 25)]
        )

    def test_rank_order_does_not_matter(self):
        self.assertEqual(
            M.mixed_control((3, 4))["numerator"], M.mixed_control((4, 3))["numerator"]
        )

    def test_profile_caps_before_expansion(self):
        for ranks in ((), (6,), (5, 5, 5), (True, 2), (2.0, 3), [2, 3]):
            with self.subTest(ranks=ranks), self.assertRaises((TypeError, ValueError)):
                M.identity_coefficients(ranks, 12)


class RegularizationTests(unittest.TestCase):
    def test_mobius_cutoff_identity(self):
        for p in range(2, 7):
            self.assertEqual(M.a_coefficient(p, 1), 1)
            self.assertTrue(all(M.a_coefficient(p, n) == 0 for n in range(2, p)))
        self.assertEqual(
            [M.a_coefficient(2, n) for n in range(1, 25)],
            [R.mobius(n) for n in range(1, 25)],
        )

    def test_source_adams_identity(self):
        for p in (2, 3, 4, 6):
            M.adams_control((R.ONE, R.I), (R.ONE, R.neg(R.ONE), R.I), p)

    def test_heldout_gaussian_unitary_input(self):
        M.adams_control(
            ((Fraction(3, 5), Fraction(4, 5)), R.I), (R.ONE, R.ONE, R.neg(R.I)), 3
        )

    def test_direct_block_leading_sign(self):
        result = M.adams_control((R.ONE, R.ONE), (R.ONE, R.ONE, R.ONE), 2)
        self.assertEqual(
            result["regularized_log_coefficients"][2],
            R.gjson((Fraction(3), Fraction(0))),
        )
        self.assertNotEqual(
            result["regularized_log_coefficients"][2],
            R.gjson((Fraction(-3), Fraction(0))),
        )

    def test_outside_trace_class_but_inside_schatten_two(self):
        result = M.interval_control(Fraction(3, 5), 2)
        self.assertFalse(result["ordinary_trace_class"])
        self.assertGreater(Fraction(*result["source_scalar"]), 0)

    def test_scalar_zero_inside_regularized_domain(self):
        result = M.interval_control(Fraction(-1, 2), 2)
        self.assertEqual(result["source_scalar"], [0, 1])
        self.assertFalse(result["ordinary_trace_class"])
        self.assertEqual(2 * Fraction(1, 2) ** 2, Fraction(1, 2))

    def test_higher_regularization_domain(self):
        result = M.interval_control(Fraction(3, 4), 3)
        self.assertFalse(result["ordinary_trace_class"])
        with self.assertRaises(ValueError):
            M.direct_log_interval(Fraction(3, 4), 2)

    def test_regularization_domain_and_caps_rejected(self):
        for t, p in ((1, 2), (Fraction(3, 4), 2), (Fraction(-4, 5), 3)):
            with self.subTest(t=t, p=p), self.assertRaises(ValueError):
                M.adams_log_interval(t, p)
        with self.assertRaises(ValueError):
            M.direct_log_interval(Fraction(1, 2), 2, 33)

    def test_zero_parameter(self):
        self.assertEqual(M.direct_log_interval(0, 2), (0, 0))
        self.assertEqual(M.adams_log_interval(0, 2), (0, 0))

    def test_frozen_executable_authenticated(self):
        M.authenticate_frozen()

    def test_forged_companion_rejected(self):
        with self.assertRaises(ValueError):
            M.check_payload(
                {"schema": "mixed-koszul-canonical-regularization-v1", "result": True}
            )


if __name__ == "__main__":
    unittest.main()
