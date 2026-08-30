"""Actual finite functional equations and source-count boundary controls."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "global_boundary", HERE / "global_boundary_replay.py"
)
B = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(B)


class FiniteDualityTests(unittest.TestCase):
    def test_grade_zero_prefactor_is_retained(self):
        self.assertEqual(B.kappa(0), -1)
        self.assertEqual(B.prefactor_exponents(0), (-1, 0))

    def test_exact_first_source_prefactor_moments(self):
        self.assertEqual([B.kappa(n) for n in range(5)], [-1, 2, 4, 13, 22])
        self.assertEqual(B.prefactor_exponents(4), (40, 137))

    def test_periodic_closed_form_against_direct_source_sum(self):
        for n in range(257):
            self.assertEqual(
                B.prefactor_exponents(n),
                (
                    sum(B.kappa(j) for j in range(n + 1)),
                    sum(j * B.kappa(j) for j in range(n + 1)),
                ),
            )

    def test_power_sum_formulas(self):
        for degree in range(1, 5):
            for n in (0, 1, 7, 31):
                self.assertEqual(
                    B.sum_power(n, degree), sum(j**degree for j in range(n + 1))
                )

    def test_actual_finite_functional_equations(self):
        for q in (5, 7):
            for cut in range(5):
                self.assertTrue(
                    B.duality_control(B.G.native_source(q, 1, 1), cut)[
                        "exact_reciprocal_identity"
                    ]
                )

    def test_finite_identity_heldout_arithmetic_source(self):
        self.assertTrue(
            B.duality_control(B.G.native_source(7, 4, 4), 3)[
                "exact_reciprocal_identity"
            ]
        )

    def test_prefactor_and_finite_product_caps(self):
        with self.assertRaises((TypeError, ValueError)):
            B.prefactor_exponents(True)
        with self.assertRaises(ValueError):
            B.prefactor_exponents(257)
        with self.assertRaises(ValueError):
            B.finite_global(
                B.G.native_source(5, 1, 1), Fraction(1, 4), Fraction(1, 5), 2
            )


class ActualClosureBoundaryTests(unittest.TestCase):
    def test_primitive_closure_counts(self):
        self.assertEqual(B.closure_counts(B.G.native_source(5, 1, 1), 2), [12, 38])

    def test_even_extensions_keep_infinity_points(self):
        counts = B.closure_counts(B.G.native_source(7, 1, 1), 24)
        self.assertTrue(all(counts[m - 1] >= 2 for m in range(2, 25, 2)))

    def test_all_bounded_root_orders_have_positive_constants(self):
        source = B.G.native_source(5, 1, 1)
        T = Fraction(1, 10)
        for order in range(1, 13):
            low, high = B.constant_interval(source, T, order, 24)
            self.assertGreaterEqual(low, T ** (2 * order) / (2 * order) ** 5)
            self.assertGreater(high, low)

    def test_identity_root_uses_actual_genus_three_count(self):
        low, _ = B.constant_interval(B.G.native_source(5, 1, 1), Fraction(1, 10), 1, 24)
        self.assertGreater(low, Fraction(3, 5))

    def test_proved_positive_radial_regime(self):
        source = B.G.native_source(5, 1, 1)
        for order in (1, 2, 3):
            self.assertTrue(
                B.radial_control(source, Fraction(1, 10), Fraction(99, 100), order)[
                    "finite_probe_real_part_above_half_positive_constant"
                ]
            )

    def test_root_order_and_T_hypotheses_are_real_constraints(self):
        source = B.G.native_source(5, 1, 1)
        for T in (Fraction(0), Fraction(-1, 10), Fraction(1, 5), 0.1):
            with self.subTest(T=T), self.assertRaises((TypeError, ValueError)):
                B.constant_interval(source, T, 1, 24)
        with self.assertRaises(ValueError):
            B.constant_interval(source, Fraction(1, 10), 12, 12)


class ExactCyclotomicTests(unittest.TestCase):
    def test_actual_third_root_arithmetic(self):
        self.assertEqual(B.power(B.OMEGA, 3), B.ONE)
        self.assertEqual(B.add(B.add(B.ONE, B.OMEGA), B.power(B.OMEGA, 2)), B.ZERO)
        self.assertEqual(B.real_part(B.OMEGA), Fraction(-1, 2))

    def test_eisenstein_inverse(self):
        for value in (
            (Fraction(2), Fraction(3)),
            B.OMEGA,
            (Fraction(1, 3), Fraction(-2, 5)),
        ):
            self.assertEqual(B.multiply(value, B.inverse(value)), B.ONE)
        with self.assertRaises(ValueError):
            B.inverse(B.ZERO)

    def test_rational_source_functions_at_zero(self):
        self.assertEqual(B.source_rational_functions(B.ZERO), (B.ONE, B.ONE, B.ONE))

    def test_radial_cache_keeps_type_and_domain_checks(self):
        B.radial_functions(Fraction(99, 100), 1, 24)
        with self.assertRaises((TypeError, ValueError)):
            B.radial_functions(0.99, 1, 24)
        with self.assertRaises(ValueError):
            B.radial_functions(Fraction(1), 1, 24)
        with self.assertRaises(ValueError):
            B.radial_functions(Fraction(99, 100), 4, 24)

    def test_tail_and_constant_output_is_bounded_exact(self):
        result = B.radial_control(
            B.G.native_source(7, 1, 1), Fraction(1, 14), Fraction(999, 1000), 3
        )
        self.assertLess(
            Fraction(*result["scaled_log_absolute_tail"]), Fraction(1, 10**7)
        )
        self.assertEqual(
            len(result["finite_scaled_log_Eisenstein_coordinate_intervals"]), 2
        )

    def test_frozen_source_authentication(self):
        B.authenticate_frozen()

    def test_forged_fixture(self):
        with self.assertRaises(ValueError):
            B.check_payload(
                {
                    "schema": "source-global-duality-and-grading-boundary-v1",
                    "status": "PASS",
                }
            )


if __name__ == "__main__":
    unittest.main()
