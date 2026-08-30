"""Source twists, ramification, held-out fields and signed completion controls."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "twisted_global", HERE / "twisted_global_replay.py"
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class TwistedSourceTests(unittest.TestCase):
    def test_actual_genus_nine_positive_difference(self):
        row = M.count_twisted(5, 1, 1, 1)
        self.assertEqual(row["counts"]["Z"], 12)
        self.assertEqual(row["counts"]["Ztilde"], 24)
        self.assertEqual(row["Delta"], 12)

    def test_heldout_symmetric_source_zero_difference(self):
        row = M.count_twisted(5, -1, 0, 1)
        self.assertEqual(row["counts"]["Z"], 6)
        self.assertEqual(row["counts"]["Ztilde"], 6)
        M.fibre_control(M.native_source(5, -1, 0))

    def test_odd_extensions_can_have_zero_difference(self):
        for params in ((7, 1, 1), (7, 4, 4)):
            for degree in (1, 3):
                row = M.count_twisted(*params, degree)
                self.assertEqual(row["Delta"], 0)
                self.assertEqual(row["counts"]["C"], row["counts"]["E"])

    def test_new_ramified_stalks_are_zero(self):
        for params in M.SOURCES:
            for row in M.native_source(*params)["primitive_rows"]:
                self.assertEqual(row["twisted_stalks_at_zero_and_infinity"], [0, 0])
                zero_rows = [
                    item for item in row["finite_fibre_histogram"] if item["chi_u"] == 0
                ]
                self.assertEqual(sum(item["number"] for item in zero_rows), 1)

    def test_complete_histograms_include_all_base_points(self):
        for params in M.SOURCES:
            for row in M.native_source(*params)["primitive_rows"]:
                self.assertEqual(
                    sum(item["number"] for item in row["finite_fibre_histogram"]),
                    row["field_order"],
                )

    def test_degree_three_is_held_out(self):
        for params in M.SOURCES:
            source = M.native_source(*params)
            for index, name in enumerate(("Dchi", "Prym")):
                traces = M.power_traces(source["polynomials"][name], 3)
                self.assertEqual(
                    -traces[2],
                    source["primitive_rows"][2]["local_sums_Dchi_Prym"][index],
                )

    def test_regular_source_decomposition_is_primitive(self):
        for params in M.SOURCES:
            for row in M.native_source(*params)["primitive_rows"]:
                sign, std = row["local_sums_Dchi_Prym"]
                self.assertEqual(row["Delta"], sign + 2 * std)

    def test_reciprocal_quartics_have_actual_weight(self):
        for params in M.SOURCES:
            source = M.native_source(*params)
            for poly in source["polynomials"].values():
                self.assertTrue(M.P.quartic_weil(list(poly), params[0]))

    def test_all_grade_stalk_identity(self):
        for params in M.SOURCES:
            rows = M.fibre_control(M.native_source(*params))
            self.assertEqual([row["degree"] for row in rows], [1, 2, 3])
            for row in rows:
                self.assertEqual(row["finite_grade_traces"][0], 0)

    def test_twist_once_is_not_twist_to_grade_power(self):
        row = M.twist_order_control()
        self.assertEqual(row["actual_post_source_twist_h0_h1_h2"], [0, 32, 0])
        self.assertEqual(row["wrong_input_twist_h0_h1_h2"], [4, 16, 4])
        self.assertNotEqual(
            row["actual_identity_chi_minus_one_trace"], row["wrong_chi_squared_trace"]
        )

    def test_source_validation_precedes_warm_cache(self):
        M.native_source(5, 1, 1)
        for params in ((5.0, 1, 1), (5, True, 1), (7, 0, 1), (5, 2, 2)):
            with (
                self.subTest(params=params),
                self.assertRaises((ValueError, TypeError)),
            ):
                M.native_source(*params)

    def test_field_degree_caps_precede_allocation(self):
        for degree in (True, 1.0, 0, 4):
            with (
                self.subTest(degree=degree),
                self.assertRaises((ValueError, TypeError)),
            ):
                M.count_twisted(5, 1, 1, degree)


class EntireCompletionTests(unittest.TestCase):
    def test_entire_completion_has_no_grade_zero_pole(self):
        source = M.native_source(5, 1, 1)
        result = M.determinant_control(source, Fraction(1, 10), Fraction(1, 5))
        self.assertEqual(result["grade_zero_factor"], 1)
        self.assertFalse(result["has_denominator"])

    def test_ordinary_determinant_beyond_initial_euler_region(self):
        for p in (5, 7):
            result = M.determinant_control(
                M.native_source(p, 1, 1), Fraction(1, 10), Fraction(1, 2)
            )
            self.assertFalse(result["inside_initial_Euler_T_disk"])
            self.assertLess(Fraction(*result["proved_grade_tail"]), Fraction(1, 10**10))

    def test_independent_grade_and_power_constructions(self):
        result = M.determinant_control(
            M.native_source(7, 4, 4), Fraction(1, 4), Fraction(1, 10)
        )
        self.assertLess(Fraction(*result["proved_power_tail"]), Fraction(1, 10**10))

    def test_first_power_is_complete_twisted_fibre_trace(self):
        source = M.native_source(5, 1, 1)
        z, T = Fraction(1, 4), Fraction(1, 100)
        self.assertEqual(
            M.power_log(source, z, T, 1),
            T * M.fibre_trace(source["primitive_rows"][0], z),
        )

    def test_T_zero_has_trivial_determinant(self):
        source = M.native_source(5, 1, 1)
        self.assertEqual(
            M.finite_grade_log(source, Fraction(1, 4), Fraction(0), 12), (0, 0)
        )
        self.assertEqual(M.power_log(source, Fraction(1, 4), Fraction(0), 12), 0)

    def test_degree_weight_uses_z_to_extension_degree(self):
        rows = M.fibre_control(M.native_source(5, 1, 1))
        for row in rows[1:]:
            for control in row["all_grade_controls"]:
                z = Fraction(*control["z"])
                self.assertEqual(
                    Fraction(*control["required_weight"]), z ** row["degree"]
                )

    def test_signed_constants_are_not_assumed_positive(self):
        source = M.native_source(5, 1, 1)
        rows = M.signed_constants(source, Fraction(1, 10))["constant_controls"]
        self.assertEqual(rows[0]["certified_sign"], 1)
        self.assertTrue(any(row["certified_sign"] != 1 for row in rows))

    def test_signed_sequence_contains_actual_zero_odd_terms(self):
        result = M.signed_constants(M.native_source(7, 1, 1), Fraction(1, 14))
        self.assertEqual(result["source_Delta_sequence"][::2], [0] * 12)

    def test_invalid_analytic_and_trace_controls(self):
        source = M.native_source(7, 1, 1)
        with self.assertRaises(ValueError):
            M.determinant_control(source, Fraction(1, 3), Fraction(1))
        with self.assertRaises(ValueError):
            M.signed_constants(source, Fraction(1, 7))
        with self.assertRaises(ValueError):
            M.power_traces((1, 1000, 0, 5000, 25), 24)
        with self.assertRaises(ValueError):
            M.power_traces(source["polynomials"]["Dchi"], 49)

    def test_primitive_newton_rejects_inexact_values(self):
        for sums in ([True, 2], [1.0, 2], [1], [1000, 1000]):
            with (
                self.subTest(sums=sums),
                self.assertRaises((ValueError, TypeError, ArithmeticError)),
            ):
                M.quartic_from_counts(5, sums)

    def test_frozen_source_authentication(self):
        M.authenticate_frozen()

    def test_forged_fixture_rejected(self):
        with self.assertRaises(ValueError):
            M.check_payload(
                {
                    "schema": "actual-ramified-twist-global-completion-v1",
                    "status": "PASS",
                }
            )


if __name__ == "__main__":
    unittest.main()
