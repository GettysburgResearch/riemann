"""Actual finite fibres, global grading, and completed determinant controls."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "global_cohomology", HERE / "global_cohomology_replay.py"
)
G = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G)


class NativeSourceTests(unittest.TestCase):
    def test_primitive_f5_polynomials(self):
        source = G.native_source(5, 1, 1)
        self.assertEqual(source["polynomials"], {"E": (1, 3, 5), "D": (1, 0, 5)})

    def test_heldout_extension_prediction_uses_source_curves(self):
        source = G.native_source(5, 1, 1)
        self.assertEqual(source["primitive_rows"][1]["counts"]["E"], 27)
        self.assertEqual(source["primitive_rows"][1]["counts"]["D"], 36)

    def test_symmetric_source_heldout_from_default_panels(self):
        source = G.native_source(5, -1, 0)
        self.assertEqual(source["polynomials"]["E"], (1, 2, 5))
        G.fibre_control(source)

    def test_all_complete_fibre_sectors(self):
        for params in G.SOURCES:
            rows = G.fibre_control(G.native_source(*params))
            self.assertEqual([row["extension_degree"] for row in rows], [1, 2])
            for row in rows:
                self.assertEqual(
                    sum(x["number"] for x in row["finite_fibre_histogram"]),
                    row["field_order"],
                )

    def test_degree_two_forces_z_squared(self):
        rows = G.fibre_control(G.native_source(7, 1, 1))
        for control in rows[1]["all_grade_rational_trace_controls"]:
            self.assertTrue(control["wrong_grading_detected_when_degree2"])
            z = Fraction(*control["z"])
            self.assertEqual(
                Fraction(*control["required_weight_z_power_degree"]), z * z
            )

    def test_primitive_source_invalid_before_warm_cache(self):
        G.native_source(5, 1, 1)
        for params in (
            (5.0, 1, 1),
            (5, True, 1),
            (5, 1.0, 1),
            (7, 0, 1),
            (5, 2, 2),
            (11, 1, 1),
        ):
            with (
                self.subTest(params=params),
                self.assertRaises((TypeError, ValueError)),
            ):
                G.native_source(*params)


class CohomologyCompletionTests(unittest.TestCase):
    def test_grade_zero_is_retained(self):
        self.assertEqual(G.sectors(Fraction(0)), (1, 0, 0))
        source = G.native_source(5, 1, 1)
        control = G.determinant_control(source, Fraction(1, 10), Fraction(1, 2))
        self.assertEqual(Fraction(*control["explicit_grade_zero_ZP1"]), Fraction(-4, 3))
        self.assertTrue(control["full_global_object_includes_grade_zero"])

    def test_continuation_point_beyond_arithmetic_euler_disk(self):
        for q in (5, 7):
            result = G.determinant_control(
                G.native_source(q, 1, 1), Fraction(1, 10), Fraction(1, 2)
            )
            self.assertFalse(result["inside_initial_arithmetic_Euler_disk"])
            self.assertTrue(result["inside_positive_grade_log_disk"])
            self.assertLess(Fraction(*result["proved_grade_tail"]), Fraction(1, 10**10))
            self.assertLess(Fraction(*result["proved_power_tail"]), Fraction(1, 10**10))

    def test_independent_grade_and_power_tails(self):
        source = G.native_source(7, 4, 4)
        result = G.determinant_control(source, Fraction(1, 4), Fraction(1, 10))
        self.assertLess(Fraction(*result["proved_grade_tail"]), Fraction(1, 10**6))
        self.assertLess(Fraction(*result["proved_power_tail"]), Fraction(1, 10**10))

    def test_first_power_is_actual_graded_fibre_trace(self):
        source = G.native_source(5, 1, 1)
        z, T = Fraction(1, 4), Fraction(1, 100)
        native = G.fibre_trace(source["primitive_rows"][0], z) - 6
        self.assertEqual(G.adams_log(source, z, T, 1), T * native)

    def test_zero_T_has_zero_positive_grade_log(self):
        source = G.native_source(5, 1, 1)
        self.assertEqual(
            G.finite_grade_log(source, Fraction(1, 4), Fraction(0), 12), (0, 0)
        )
        self.assertEqual(G.adams_log(source, Fraction(1, 4), Fraction(0), 12), 0)

    def test_exact_frobenius_power_recurrence(self):
        self.assertEqual(G.frobenius_traces((1, 3, 5), 4), [-3, -1, 18, -49])
        self.assertEqual(G.frobenius_traces((1, 0, 5), 4), [0, -10, 0, 50])

    def test_invalid_positive_grade_disk_and_grade_zero_poles(self):
        source = G.native_source(7, 1, 1)
        with self.assertRaises(ValueError):
            G.determinant_control(source, Fraction(1, 4), Fraction(3, 5))
        with self.assertRaises(ValueError):
            G.determinant_control(source, Fraction(1, 10), Fraction(1, 7))
        with self.assertRaises(ValueError):
            G.sectors(Fraction(1))

    def test_source_R_and_Lie_M_are_different_spaces(self):
        d = G.S.source_sequences(24)["e"][24]
        self.assertEqual(d, 8125)
        self.assertGreater(G.R.multiplicity(24), d)


class GlobalDivisorTests(unittest.TestCase):
    def test_stacked_zero_radii_are_not_one_critical_circle(self):
        rows = G.divisor_control(5, Fraction(1, 4), 3)["finite_divisor_rows"]
        self.assertEqual(Fraction(*rows[1]["zero_radius_squared"]), Fraction(16, 5))
        self.assertEqual(Fraction(*rows[2]["zero_radius_squared"]), Fraction(256, 5))
        self.assertEqual(rows[1]["zero_multiplicity"], 6)

    def test_positive_grade_poles_do_not_disappear(self):
        result = G.divisor_control(7, Fraction(1, 4), 12)
        self.assertGreater(result["denominator_pole_count_with_multiplicity"], 2)
        self.assertTrue(
            all(
                row["each_pole_multiplicity"] > 0
                for row in result["finite_divisor_rows"]
            )
        )

    def test_noncancellation_hypothesis_is_enforced(self):
        with self.assertRaises(ValueError):
            G.divisor_control(5, Fraction(1, 2), 12)
        with self.assertRaises(ValueError):
            G.divisor_control(5, Fraction(0), 12)

    def test_weil_polynomial_and_resource_caps(self):
        with self.assertRaises(ValueError):
            G.frobenius_traces((1, 6, 5), 12)
        with self.assertRaises(ValueError):
            G.frobenius_traces((1, 3, 5), 49)
        with self.assertRaises(ValueError):
            G.divisor_control(5, Fraction(1, 4), 25)

    def test_frozen_sources(self):
        G.authenticate_frozen()

    def test_forged_fixture(self):
        with self.assertRaises(ValueError):
            G.check_payload(
                {
                    "schema": "source-global-cohomological-completion-v1",
                    "status": "PASS",
                }
            )


if __name__ == "__main__":
    unittest.main()
