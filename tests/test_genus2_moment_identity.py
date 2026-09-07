"""Focused exact tests for the all-odd-prime-power genus-two moment identity."""

from __future__ import annotations

import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_moment_identity as identity  # noqa: E402


def irreducible_quadratic_count(q: int) -> int:
    return q * (q - 1) // 2


class NineRowCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = identity.build_certificate()

    def test_all_nine_factorization_rows_and_aggregates(self) -> None:
        expected = {
            "L^4": (
                1,
                1,
                0,
                lambda q, i: q,
                lambda q, i: q**2 * (q - 1),
                lambda q, i: q * (q - 1),
                lambda q, i: q**4 * (q - 1),
            ),
            "L^2 M^2": (
                3,
                2,
                0,
                lambda q, i: q * (q - 1) // 2,
                lambda q, i: q * (q - 1) ** 2,
                lambda q, i: Fraction(q * (q - 1) * (q - 2), 2),
                lambda q, i: q**3 * (q - 1) ** 2,
            ),
            "Q^2": (
                1,
                0,
                1,
                lambda q, i: i,
                lambda q, i: q**3 - q,
                lambda q, i: i * q,
                lambda q, i: q**3 * (q**2 - 1),
            ),
            "L^3 M": (
                2,
                2,
                0,
                lambda q, i: q * (q - 1),
                lambda q, i: 0,
                lambda q, i: -q * (q - 1),
                lambda q, i: 0,
            ),
            "Q L^2": (
                2,
                1,
                1,
                lambda q, i: q * i,
                lambda q, i: 0,
                lambda q, i: Fraction(-q * (q - 1) ** 2, 2),
                lambda q, i: 0,
            ),
            "L M N^2": (
                4,
                3,
                0,
                lambda q, i: q * (q - 1) * (q - 2) // 2,
                lambda q, i: 0,
                lambda q, i: Fraction(-q * (q - 1) * (q - 3), 2),
                lambda q, i: 0,
            ),
            "Q_1 Q_2": (
                2,
                0,
                2,
                lambda q, i: i * (i - 1) // 2,
                lambda q, i: -q,
                lambda q, i: Fraction(-q * (q**2 - 1), 8),
                lambda q, i: 0,
            ),
            "Q L M": (
                2,
                2,
                1,
                lambda q, i: i * q * (q - 1) // 2,
                lambda q, i: -q,
                lambda q, i: Fraction(q * (q - 1) ** 2, 4),
                lambda q, i: 0,
            ),
            "L M N R": (
                6,
                4,
                0,
                lambda q, i: q * (q - 1) * (q - 2) * (q - 3) // 24,
                lambda q, i: -q,
                lambda q, i: Fraction(q * (q - 1) * (q - 3), 8),
                lambda q, i: 0,
            ),
        }
        self.assertEqual(len(self.certificate.rows), identity.HARD_ROW_LIMIT)
        self.assertEqual({row.label for row in self.certificate.rows}, set(expected))
        for q in (3, 5, 7, 9, 11):
            i = irreducible_quadratic_count(q)
            for row in self.certificate.rows:
                weight, linear, quadratic, count, c3, c1_total, c5 = expected[row.label]
                self.assertEqual(row.weight, weight)
                self.assertEqual(row.linear_support, linear)
                self.assertEqual(row.quadratic_support, quadratic)
                self.assertEqual(row.count.evaluate(q), count(q, i))
                self.assertEqual(row.c3_each.evaluate(q), c3(q, i))
                self.assertEqual(row.c1_total.evaluate(q), c1_total(q, i))
                self.assertEqual(row.c5_each.evaluate(q), c5(q, i))

    def test_each_row_correction_and_delta_are_reconstructed(self) -> None:
        for q in (3, 5, 7, 9, 11, 13):
            reconstructed_delta = Fraction(0)
            for row in self.certificate.rows:
                count = row.count.evaluate(q)
                c3_each = row.c3_each.evaluate(q)
                c1_total = row.c1_total.evaluate(q)
                moebius_degree_two = (
                    row.linear_support * (row.linear_support + 1) // 2
                    + row.quadratic_support
                    - q * row.linear_support
                )
                correction = row.weight * (
                    -(q - row.linear_support) * count * c3_each
                    + moebius_degree_two * c1_total
                )
                self.assertEqual(row.correction.evaluate(q), correction)
                reconstructed_delta += correction
            target = -q * (q - 1) * (q**4 - q**3 - q**2 + 3 * q + 1)
            self.assertEqual(reconstructed_delta, target)
            self.assertEqual(self.certificate.delta.evaluate(q), target)

    def test_t0_and_total_b_squared_are_reconstructed(self) -> None:
        for q in (3, 5, 7, 9, 11, 13):
            t0 = sum(
                row.weight * row.count.evaluate(q) * row.c5_each.evaluate(q)
                for row in self.certificate.rows
            )
            target_t0 = q**4 * (q - 1) * (2 * q**2 - 2 * q + 1)
            target_b2 = (
                q**4 * (q - 1) * (2 * q**2 - 3 * q + 2)
                + q * (q - 1) * (q**2 - 3 * q - 1)
            )
            self.assertEqual(t0, target_t0)
            self.assertEqual(self.certificate.t0.evaluate(q), target_t0)
            self.assertEqual(self.certificate.sum_b_squared.evaluate(q), target_b2)


class MomentFormulaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = identity.build_certificate()

    def test_a_squared_euler_product_coefficients_and_total(self) -> None:
        for q in (3, 5, 7, 9, 11, 13):
            diagonal = q**5 - 2 * q**4 + 2 * q**3 - 2 * q**2 + 2 * q - 1
            off_diagonal = 2 * q - 3
            total = q * diagonal + q * (q - 1) * off_diagonal
            target = q**4 * (q - 1) ** 2 + q * (q - 1) * (q**2 + q - 2)
            self.assertEqual(self.certificate.a_diagonal_coefficient.evaluate(q), diagonal)
            self.assertEqual(self.certificate.a_off_diagonal_coefficient.evaluate(q), off_diagonal)
            self.assertEqual(total, target)
            self.assertEqual(self.certificate.sum_a_squared.evaluate(q), target)

    def test_b_first_moment_three_quadratic_rows_are_reconstructed(self) -> None:
        expected = {
            "L^2": (
                1,
                0,
                lambda q: q,
                lambda q: q - 1,
                lambda q: q**2 * (q - 1),
                lambda q: q**4 * (q - 1),
                lambda q: (
                    q**5 - 2 * q**4 + 2 * q**3 - 2 * q**2 + 2 * q - 1
                ),
            ),
            "L M": (
                2,
                0,
                lambda q: q * (q - 1) // 2,
                lambda q: -1,
                lambda q: 0,
                lambda q: 0,
                lambda q: 2 * q - 3,
            ),
            "Q": (
                0,
                1,
                lambda q: q * (q - 1) // 2,
                lambda q: -1,
                lambda q: 0,
                lambda q: 0,
                lambda q: -1,
            ),
        }
        self.assertEqual(
            len(self.certificate.quadratic_rows),
            identity.HARD_QUADRATIC_ROW_LIMIT,
        )
        self.assertEqual(
            tuple(row.label for row in self.certificate.quadratic_rows),
            tuple(expected),
        )
        for q in (3, 5, 7, 9, 11, 13):
            reconstructed = Fraction(0)
            for row in self.certificate.quadratic_rows:
                linear, quadratic, count, c1, c3, c5, sieve = expected[row.label]
                self.assertEqual(row.linear_support, linear)
                self.assertEqual(row.quadratic_support, quadratic)
                self.assertEqual(row.count.evaluate(q), count(q))
                self.assertEqual(row.c1_each.evaluate(q), c1(q))
                self.assertEqual(row.c3_each.evaluate(q), c3(q))
                self.assertEqual(row.c5_each.evaluate(q), c5(q))
                reconstructed_sieve = (
                    c5(q)
                    - (q - linear) * c3(q)
                    + (
                        linear * (linear + 1) // 2
                        + quadratic
                        - q * linear
                    )
                    * c1(q)
                )
                self.assertEqual(reconstructed_sieve, sieve(q))
                self.assertEqual(row.sieve_value.evaluate(q), reconstructed_sieve)
                contribution = count(q) * reconstructed_sieve
                self.assertEqual(row.contribution.evaluate(q), contribution)
                reconstructed += contribution
            target = q * (q - 1) * (q**4 - q**3 + q**2 - 1)
            self.assertEqual(reconstructed, target)
            self.assertEqual(self.certificate.sum_b.evaluate(q), target)

    def test_a_fourth_reweights_exactly_the_five_linear_quartic_rows(self) -> None:
        ordered_weights = {
            "L^4": 1,
            "L^3 M": 4,
            "L^2 M^2": 6,
            "L M N^2": 12,
            "L M N R": 24,
        }
        for q in (3, 5, 7, 9, 11, 13):
            principal = 0
            correction = 0
            for row in self.certificate.rows:
                if row.label not in ordered_weights:
                    continue
                weight = ordered_weights[row.label]
                count = row.count.evaluate(q)
                c3 = row.c3_each.evaluate(q)
                c1_total = row.c1_total.evaluate(q)
                principal += weight * count * row.c5_each.evaluate(q)
                moebius_degree_two = (
                    row.linear_support * (row.linear_support + 1) // 2
                    + row.quadratic_support
                    - q * row.linear_support
                )
                correction += weight * (
                    -(q - row.linear_support) * count * c3
                    + moebius_degree_two * c1_total
                )
            target = q * (q - 1) * (q + 1) * (
                3 * q**4 - 10 * q**3 + 15 * q**2 - 3 * q - 11
            )
            self.assertEqual(self.certificate.a_fourth_t0.evaluate(q), principal)
            self.assertEqual(self.certificate.a_fourth_delta.evaluate(q), correction)
            self.assertEqual(principal + correction, target)
            self.assertEqual(self.certificate.sum_a_fourth.evaluate(q), target)

    def test_a_squared_b_reweights_seven_quartic_rows(self) -> None:
        tuple_weights = {
            "L^4": 1,
            "L^2 M^2": 4,
            "L^3 M": 3,
            "Q L^2": 1,
            "L M N^2": 7,
            "Q L M": 2,
            "L M N R": 12,
        }
        for q in (3, 5, 7, 9, 11, 13):
            principal = 0
            correction = 0
            for row in self.certificate.rows:
                if row.label not in tuple_weights:
                    continue
                weight = tuple_weights[row.label]
                principal += weight * row.count.evaluate(q) * row.c5_each.evaluate(q)
                moebius_degree_two = (
                    row.linear_support * (row.linear_support + 1) // 2
                    + row.quadratic_support
                    - q * row.linear_support
                )
                correction += weight * (
                    -(q - row.linear_support)
                    * row.count.evaluate(q)
                    * row.c3_each.evaluate(q)
                    + moebius_degree_two * row.c1_total.evaluate(q)
                )
            target = q * (q - 1) * (q + 1) * (q**2 - 2 * q + 3) * (
                2 * q**2 - 2 * q - 1
            )
            self.assertEqual(self.certificate.a_squared_b_t0.evaluate(q), principal)
            self.assertEqual(
                self.certificate.a_squared_b_delta.evaluate(q), correction
            )
            self.assertEqual(principal + correction, target)
            self.assertEqual(self.certificate.sum_a_squared_b.evaluate(q), target)

    def test_all_five_mean_identities(self) -> None:
        for q in (3, 5, 7, 9, 11, 13):
            totals = self.certificate.totals_at(q)
            self.assertEqual(totals["member_count"], q**5 - q**4)
            self.assertEqual(
                totals["mean_a_squared"],
                q - 1 + Fraction(q**2 + q - 2, q**3),
            )
            self.assertEqual(
                totals["mean_a_fourth"],
                3 * q**2
                - 7 * q
                + 5
                + Fraction(12, q)
                - Fraction(14, q**2)
                - Fraction(11, q**3),
            )
            self.assertEqual(
                totals["mean_a_squared_b"],
                Fraction(
                    (q + 1)
                    * (q**2 - 2 * q + 3)
                    * (2 * q**2 - 2 * q - 1),
                    q**3,
                ),
            )
            self.assertEqual(
                totals["mean_b"],
                q - 1 + Fraction(q**2 - 1, q**3),
            )
            self.assertEqual(
                totals["mean_b_squared"],
                2 * q**2 - 3 * q + 2 + Fraction(q**2 - 3 * q - 1, q**3),
            )
            self.assertEqual(
                totals["mean_K"],
                -(q - 1) ** 2 + Fraction(q + 1, q**3),
            )
            self.assertEqual(
                totals["sum_K"],
                q * totals["sum_a_squared"] - totals["sum_b_squared"],
            )

    def test_q3_q5_q7_exact_totals(self) -> None:
        expected = {
            3: (162, 384, 2112, 1584, 372, 1776, -624),
            5: (2500, 10560, 116880, 84240, 10480, 92680, -39880),
            7: (14406, 88704, 1503936, 1059744, 88452, 1139208, -518280),
        }
        for q, (members, sum_a2, sum_a4, sum_a2b, sum_b, sum_b2, sum_k) in expected.items():
            totals = self.certificate.totals_at(q)
            self.assertEqual(
                (
                    totals["member_count"],
                    totals["sum_a_squared"],
                    totals["sum_a_fourth"],
                    totals["sum_a_squared_b"],
                    totals["sum_b"],
                    totals["sum_b_squared"],
                    totals["sum_K"],
                ),
                (members, sum_a2, sum_a4, sum_a2b, sum_b, sum_b2, sum_k),
            )


class ResourceFirewallTests(unittest.TestCase):
    def test_symbolic_budget_degree_and_scope_guards(self) -> None:
        with self.assertRaises(identity.ResourceLimitError):
            identity.build_certificate(operation_limit=1)
        with self.assertRaises(identity.ResourceLimitError):
            identity.build_certificate(
                operation_limit=identity.HARD_OPERATION_LIMIT + 1
            )
        algebra = identity.ExactAlgebra()
        with self.assertRaises(identity.ResourceLimitError):
            algebra.power(identity.polynomial(0, 1), identity.HARD_DEGREE_LIMIT + 1)
        certificate = identity.build_certificate()
        with self.assertRaisesRegex(ValueError, "odd q"):
            certificate.totals_at(4)

    def test_certificate_is_small_and_has_no_enumerator_dependency(self) -> None:
        certificate = identity.build_certificate()
        self.assertLess(certificate.operations_used, identity.HARD_OPERATION_LIMIT)
        source = (FUNCTION_FIELD / "genus2_moment_identity.py").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("import itertools", source)
        self.assertNotIn("import sympy", source)
        self.assertNotIn("genus2_q_scan", source)


class SignDensityCorollaryTests(unittest.TestCase):
    def test_shifted_polynomial_and_exact_frozen_bounds(self) -> None:
        moment_certificate = identity.build_certificate()
        certificate = identity.build_sign_density_certificate(moment_certificate)
        self.assertEqual(
            certificate.mean_deficit_numerator.coefficients,
            tuple(map(Fraction, (-1, -1, 0, 1, -2, 1))),
        )
        self.assertEqual(
            certificate.shifted_positive_polynomial.coefficients,
            tuple(map(Fraction, (104, 215, 171, 67, 13, 1))),
        )
        self.assertEqual(certificate.range_lower_bound, -20)
        self.assertEqual(certificate.proportion_denominator, 20)
        self.assertEqual(certificate.lower_bound_at(3), Fraction(26, 1215))
        self.assertEqual(certificate.lower_bound_at(5), Fraction(997, 31250))
        self.assertEqual(certificate.lower_bound_at(7), Fraction(617, 16807))
        q_times_q_minus_one = identity.polynomial(0, -1, 1)
        algebra = identity.ExactAlgebra(operation_limit=100)
        self.assertEqual(
            algebra.negate(moment_certificate.sum_k),
            algebra.multiply(q_times_q_minus_one, certificate.mean_deficit_numerator),
        )

    def test_scope_and_positivity_guards(self) -> None:
        certificate = identity.build_sign_density_certificate()
        for q in (3, 5, 7, 9, 11, 13):
            with self.subTest(q=q):
                self.assertGreater(certificate.lower_bound_at(q), 0)
                self.assertLess(certificate.lower_bound_at(q), Fraction(1, 20))
        for q in (0, 2, 4):
            with self.subTest(q=q):
                with self.assertRaisesRegex(ValueError, "odd q"):
                    certificate.lower_bound_at(q)

    def test_composite_odd_input_is_only_a_formal_polynomial_specialization(self) -> None:
        certificate = identity.build_sign_density_certificate()
        q = 15
        numerator = q**5 - 2 * q**4 + q**3 - q - 1
        self.assertEqual(certificate.lower_bound_at(q), Fraction(numerator, 20 * q**5))
        self.assertIn("family semantics require a prime power", certificate.lower_bound_at.__doc__)


if __name__ == "__main__":
    unittest.main()
