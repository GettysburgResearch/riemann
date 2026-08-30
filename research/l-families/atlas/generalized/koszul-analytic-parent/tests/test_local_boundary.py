"""Exact continuation residue controls and independent critical constants."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "local_parent_boundary", HERE / "local_boundary_replay.py"
)
L = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(L)


class LocalResidueTests(unittest.TestCase):
    def test_first_boundary_exponent(self):
        for p in range(2, 7):
            self.assertEqual(
                L.residue_control(p, p)["regularized_log_derivative_residue"], [1, p]
            )

    def test_prime_lifts_are_fractional(self):
        for p in range(2, 7):
            for prime in (7, 11, 13, 17, 31):
                result = L.residue_control(p, prime)
                self.assertEqual(
                    result["regularized_log_derivative_residue"], [1, prime]
                )
                self.assertTrue(result["nonintegral_regularized_monodromy_exponent"])

    def test_not_every_index_is_a_branch(self):
        self.assertEqual(
            L.residue_control(2, 4)["regularized_log_derivative_residue"], [0, 1]
        )
        self.assertEqual(
            L.residue_control(3, 6)["regularized_log_derivative_residue"], [0, 1]
        )

    def test_primitive_and_regularized_branch_sets_differ(self):
        result = L.residue_control(3, 4)
        self.assertEqual(result["primitive_derivative_residue"], [0, 1])
        self.assertEqual(result["regularized_log_derivative_residue"], [1, 4])

    def test_no_regularized_poles_below_first_order(self):
        self.assertEqual(
            L.residue_control(5, 3)["regularized_log_derivative_residue"], [0, 1]
        )

    def test_source_deviations_agree_with_first_packet(self):
        self.assertEqual(
            [L.deviation(2, n) for n in range(1, 25)],
            [L.R.multiplicity(n) for n in range(1, 25)],
        )

    def test_rank_nine_source_is_explicitly_allowed(self):
        self.assertEqual(L.deviation(8, 1), 18)


class FractionalCutoffTests(unittest.TestCase):
    def test_quadratic_critical_point(self):
        L.constant_control(4, 2, (Fraction(0), Fraction(1, 2)), Fraction(1, 2))

    def test_cubic_real_critical_point(self):
        result = L.constant_control(
            8, 3, (Fraction(-1, 2), Fraction(0)), Fraction(1, 2)
        )
        self.assertEqual(result["critical_exponent"], [1, 3])
        self.assertFalse(result["ordinary_Sp_at_point"])

    def test_quartic_gaussian_critical_point(self):
        L.constant_control(4, 4, (Fraction(1, 2), Fraction(1, 2)), Fraction(5, 7))

    def test_conjugate_critical_point(self):
        positive, ep = L.parent_constant(
            4, 2, (Fraction(0), Fraction(1, 2)), Fraction(1, 2)
        )
        negative, en = L.parent_constant(
            4, 2, (Fraction(0), Fraction(-1, 2)), Fraction(1, 2)
        )
        self.assertEqual(positive, (negative[0], -negative[1]))
        self.assertEqual(ep, en)

    def test_false_critical_point_rejected(self):
        with self.assertRaises(ValueError):
            L.checked_case(4, 2, (Fraction(1, 2), Fraction(0)), Fraction(1, 2))

    def test_false_radius_bound_rejected(self):
        with self.assertRaises(ValueError):
            L.checked_case(4, 4, (Fraction(1, 2), Fraction(1, 2)), Fraction(7, 10))

    def test_tail_outside_convergence_domain_rejected(self):
        with self.assertRaises(ValueError):
            L.checked_case(4, 2, (Fraction(0), Fraction(1, 2)), Fraction(9, 10))

    def test_caps_and_types(self):
        for q, degree in ((9, 4), (4, 65), (True, 4), (4, 2.0)):
            with (
                self.subTest(q=q, degree=degree),
                self.assertRaises((TypeError, ValueError)),
            ):
                L.deviation(q, degree)

    def test_frozen_sources(self):
        L.authenticate_frozen()

    def test_forged_fixture(self):
        with self.assertRaises(ValueError):
            L.check_payload(
                {"schema": "koszul-local-natural-boundary-v1", "status": "PASS"}
            )


if __name__ == "__main__":
    unittest.main()
