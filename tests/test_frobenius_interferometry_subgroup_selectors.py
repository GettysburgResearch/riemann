"""Focused exact tests for the Frobenius-interferometry selector theorem."""

from __future__ import annotations

import importlib
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "research" / "l-families" / "atlas" / "function_field"
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

subject = importlib.import_module("frobenius_interferometry_subgroup_selectors")


class FrobeniusInterferometrySubgroupSelectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.packet = subject.build_packet()

    def test_su2_frequency_kernel(self) -> None:
        guard = subject.ResourceGuard()
        context = subject.HaarContext(guard)
        for left in range(1, subject.MAX_TOTAL_FREQUENCY + 1):
            one = {(left,): 1, (-left,): 1}
            self.assertEqual(
                subject.weyl_integral(one, context.a1_density, 2, guard),
                subject.su2_trace_mean(left),
            )
            for right in range(1, subject.MAX_TOTAL_FREQUENCY + 1):
                two = {(right,): 1, (-right,): 1}
                product = subject.laurent_multiply(one, two, guard)
                self.assertEqual(
                    subject.weyl_integral(
                        product, context.a1_density, 2, guard
                    ),
                    subject.su2_trace_pair_mean(left, right),
                )

    def test_complete_raw_cap_and_two_nontrivial_ambient_nulls(self) -> None:
        raw = self.packet["raw_cap"]
        self.assertEqual(raw["maximum_total_frequency"], 10)
        self.assertEqual(raw["complete_pair_count"], 25)
        self.assertEqual(
            raw["ambient_zero_nontrivial_subgroup_contrasts"],
            [[2, 4], [2, 8]],
        )
        observed = {
            tuple(row["frequencies"]): tuple(row["signature"])
            for row in raw["nonzero_signatures"]
        }
        self.assertEqual(observed, subject.EXPECTED_NONZERO_RAW_SIGNATURES)

    def test_closed_subgroup_formulas_match_all_raw_rows(self) -> None:
        guard = subject.ResourceGuard()
        context = subject.HaarContext(guard)
        for total in range(2, subject.MAX_TOTAL_FREQUENCY + 1):
            for left in range(1, total // 2 + 1):
                right = total - left
                signature = context.signature(
                    subject.interferometer(left, right, guard)
                )
                self.assertEqual(
                    signature[1],
                    subject.product_interferometer_mean(left, right),
                )
                self.assertEqual(
                    signature[2],
                    subject.su2_embedding_interferometer_mean(
                        1, 1, left, right
                    ),
                )
                self.assertEqual(
                    signature[3],
                    subject.su2_embedding_interferometer_mean(
                        3, 1, left, right
                    ),
                )

    def test_all_frequency_sym3_root_resonance_ladders(self) -> None:
        packet = self.packet["sym3_root_resonance_ladders"]
        target = [0, 0, 0, 2, 0, 0, 0]
        for branch, first_base in (("outer", 2), ("inner", 4)):
            rows = packet["bounded_replay"][branch]
            self.assertEqual(
                [row["base"] for row in rows],
                list(range(first_base, subject.MAX_ROOT_LADDER_BASE + 1)),
            )
            for row in rows:
                self.assertEqual(
                    tuple(row["frequencies"]),
                    subject.sym3_root_resonance_pair(row["base"], branch),
                )
                self.assertEqual(row["raw_signature"], [0, 0, 0, -1, 0, 0, 0])
                self.assertEqual(row["selector_signature"], target)
        with self.assertRaises(ValueError):
            subject.sym3_root_resonance_pair(1, "outer")
        with self.assertRaises(ValueError):
            subject.sym3_root_resonance_pair(3, "inner")
        with self.assertRaises(ValueError):
            subject.sym3_root_resonance_pair(4, "unknown")

    def test_selector_matrix_is_exactly_two_times_identity(self) -> None:
        signatures = self.packet["selectors"]["signatures"]
        self.assertEqual(
            signatures,
            {
                name: list(expected)
                for name, expected in subject.SELECTOR_EXPECTATIONS.items()
            },
        )
        matrix = [
            [
                signatures[name][column]
                for column in (1, 2, 3)
            ]
            for name in subject.SELECTOR_EXPECTATIONS
        ]
        self.assertEqual(matrix, [[2, 0, 0], [0, 2, 0], [0, 0, 2]])
        for signature in signatures.values():
            self.assertEqual(signature[0], 0)
            self.assertEqual(signature[4:], [0, 0, 0])

    def test_ambient_gram_is_exact_and_positive_definite(self) -> None:
        gram = self.packet["selectors"]["ambient_gram"]
        self.assertEqual(gram, [list(row) for row in subject.EXPECTED_AMBIENT_GRAM])
        first_minor = gram[0][0]
        second_minor = gram[0][0] * gram[1][1] - gram[0][1] * gram[1][0]
        determinant = (
            gram[0][0] * (gram[1][1] * gram[2][2] - gram[1][2] * gram[2][1])
            - gram[0][1] * (gram[1][0] * gram[2][2] - gram[1][2] * gram[2][0])
            + gram[0][2] * (gram[1][0] * gram[2][1] - gram[1][1] * gram[2][0])
        )
        self.assertEqual((first_minor, second_minor, determinant), (24, 752, 29312))

    def test_bounded_support_no_go_is_over_rationals(self) -> None:
        records = self.packet["selectors"]["bounded_support_minimality"]
        self.assertEqual(
            {
                name: record["minimum_rational_support"]
                for name, record in records.items()
            },
            {
                "product_selector": 2,
                "doubled_selector": 3,
                "sym3_selector": 1,
            },
        )
        self.assertIn(
            [[2, 2], [4, 4]], records["product_selector"]["witnesses"]
        )
        self.assertIn(
            [[1, 1], [1, 5], [4, 4]],
            records["doubled_selector"]["witnesses"],
        )
        self.assertEqual(
            records["sym3_selector"]["witnesses"], [[[2, 8]]]
        )

    def test_root_free_coefficient_adapter_on_exact_reciprocal_spectra(self) -> None:
        def evaluate(
            polynomial: dict[tuple[int, ...], int], x: Fraction, y: Fraction
        ) -> Fraction:
            return sum(
                Fraction(coefficient) * x**exponent[0] * y**exponent[1]
                for exponent, coefficient in polynomial.items()
            )

        guard = subject.ResourceGuard()
        context = subject.HaarContext(guard)
        raw = subject._raw_polynomials(context)
        selectors = subject.selector_polynomials(raw, guard)
        for x, y in (
            (Fraction(1), Fraction(1)),
            (Fraction(1), Fraction(-1)),
            (Fraction(2), Fraction(3)),
            (Fraction(-2), Fraction(5, 2)),
        ):
            p_one = x + 1 / x + y + 1 / y
            p_two = x * x + x**-2 + y * y + y**-2
            e_two = (p_one * p_one - p_two) / 2
            observed = subject.selector_values_from_coefficients(p_one, e_two)
            observed_squared = (
                subject.selector_values_from_squared_first_elementary(
                    p_one * p_one, e_two
                )
            )
            expected = {
                name: evaluate(polynomial, x, y)
                for name, polynomial in selectors.items()
            }
            self.assertEqual(observed, expected)
            self.assertEqual(observed_squared, expected)

        adapter = self.packet["selectors"]["coefficient_adapter"]
        self.assertIn("no roots", adapter["method"])
        self.assertIn("A=e1^2", adapter["rational_even_form"])

    def test_projection_claim_is_mean_not_pointwise_vanishing(self) -> None:
        normalization = self.packet["normalization"]
        self.assertIn("constant/trivial-isotypic", normalization["projection_scope"])
        guard = subject.ResourceGuard()
        context = subject.HaarContext(guard)
        raw = subject._raw_polynomials(context)
        selectors = subject.selector_polynomials(raw, guard)
        self.assertTrue(all(selectors.values()))
        self.assertNotEqual(selectors["doubled_selector"], {})
        self.assertNotEqual(selectors["sym3_selector"], {})

    def test_resource_and_epistemic_contract(self) -> None:
        resource = self.packet["resource_contract"]
        self.assertFalse(resource["finite_field_enumeration"])
        self.assertFalse(resource["root_finding"])
        self.assertFalse(resource["random_sampling"])
        self.assertFalse(resource["external_data"])
        self.assertLess(
            resource["accounted_work_total"],
            resource["accounted_work_cap_exclusive"],
        )
        self.assertIn("neither prove arithmetic monodromy", self.packet["firewall"])

    def test_validation_rejects_bad_inputs_under_optimized_mode(self) -> None:
        with self.assertRaises(TypeError):
            subject.trace_power(True)
        with self.assertRaises(ValueError):
            subject.trace_power(0)
        with self.assertRaises(ValueError):
            subject.interferometer(3, 2, subject.ResourceGuard())
        with self.assertRaises(ValueError):
            subject.su2_embedding_interferometer_mean(0, 1, 2, 4)
        with self.assertRaises(RuntimeError):
            guard = subject.ResourceGuard(cap=2)
            guard.charge("one")
            guard.charge("two")


if __name__ == "__main__":
    unittest.main()
