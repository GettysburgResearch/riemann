"""Actual S4 source characters, full ramification and scalar-resonance controls."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "finite_group_boundary", HERE / "finite_group_boundary_replay.py"
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class SourceCharacterTests(unittest.TestCase):
    def test_native_input_symmetric_powers(self):
        self.assertEqual([row[1] for row in M.source_sequences(2)], [12, 2, 0, 0, 0])
        self.assertEqual([row[2] for row in M.source_sequences(2)], [60, 8, 4, 0, 0])

    def test_actual_multiplicities_reconstruct_source(self):
        rows = M.source_rows(48)
        self.assertEqual(rows[0]["multiplicities"], [1, 0, 0, 0, 0])
        self.assertEqual(rows[1]["multiplicities"], [1, 0, 1, 2, 1])
        self.assertTrue(all(min(row["multiplicities"]) >= 0 for row in rows))

    def test_quasipolynomial_classes_have_expected_periods(self):
        sequences = M.source_sequences(24)
        self.assertEqual(sequences[2][1::2], (0,) * 12)
        self.assertEqual(sequences[3][3], 2)
        self.assertEqual(sequences[4][4], 1)

    def test_general_grade_conductors_match_actual_cohomology(self):
        for row in M.source_rows(48):
            a, h1, _ = row["h0_h1_h2"]
            self.assertEqual(h1, row["conductor"] - 2 * row["class_traces"][0] + 2 * a)

    def test_grade_zero_functional_exponent_is_negative_one(self):
        self.assertEqual(M.source_rows(0)[0]["kappa"], -1)

    def test_actual_rational_series_at_zero(self):
        self.assertEqual(M.class_values(Fraction(0)), (1, 1, 1, 1, 1))
        self.assertEqual(M.sectors(Fraction(0)), (1, 0, 0, 0, 0))

    def test_transposition_series_unsimplified_equals_simplified(self):
        for z in (Fraction(1, 4), Fraction(-1, 4), Fraction(2, 3)):
            value = (1 + z + 3 * z * z + z**3) / ((1 - z) ** 4 * (1 + z) ** 3)
            self.assertEqual(M.class_values(z)[1], value)

    def test_character_input_validation_before_warm_cache(self):
        M.source_sequences(12)
        for cut in (True, 12.0, -1, 97):
            with self.subTest(cut=cut), self.assertRaises((ValueError, TypeError)):
                M.source_sequences(cut)


class ActualGeometryTests(unittest.TestCase):
    def test_only_two_primitive_extensions_are_recounted(self):
        for index in range(3):
            rows = M.native_panel(index)["primitive_rows"]
            self.assertEqual([row["extension"] for row in rows], [1, 2])
            self.assertLessEqual(max(row["field_order"] for row in rows), 49)

    def test_source_panel_validation_precedes_cache(self):
        M.native_panel(1)
        for index in (True, 1.0, -1, 3):
            with self.subTest(index=index), self.assertRaises((ValueError, TypeError)):
                M.native_panel(index)

    def test_nonsplit_finite_branch_is_retained(self):
        panel = M.native_panel(2)
        row = panel["primitive_rows"][0]
        self.assertGreater(row["finite_class_census"].get("branch_nonsplit", 0), 0)
        M.fibre_controls(panel)

    def test_infinity_averages_switch_by_residue_field(self):
        rows = M.native_panel(1)["primitive_rows"]
        self.assertEqual(rows[0]["infinity_stalk_traces"]["sign"], -1)
        self.assertEqual(rows[1]["infinity_stalk_traces"]["sign"], 1)
        M.fibre_controls(M.native_panel(1))

    def test_full_fibre_series_matches_all_five_constituents(self):
        for index in range(3):
            result = M.fibre_controls(M.native_panel(index))
            for row in result:
                self.assertEqual(row["graded_traces"][0], row["field_order"] + 1)

    def test_actual_regular_source_has_degree_38(self):
        panel = M.native_panel(0)
        self.assertEqual(len(panel["polynomials"]["Z"]) - 1, 38)
        self.assertEqual(len(panel["polynomials"]["tw"]) - 1, 8)
        M.power_data(panel, 24)

    def test_actual_finite_functional_equations(self):
        for index in range(3):
            for cut in (0, 1, 2):
                self.assertTrue(
                    M.finite_duality(M.native_panel(index), cut)[
                        "source_functional_equation"
                    ]
                )

    def test_closed_point_weight_is_z_power_degree(self):
        rows = M.fibre_controls(M.native_panel(0))
        for control in rows[1]["rational_controls"]:
            z = Fraction(*control["z"])
            self.assertEqual(Fraction(*control["required_weight"]), z * z)


class BoundaryAndScalarTests(unittest.TestCase):
    def test_positive_source_constants_have_certified_lower_bounds(self):
        for index in range(3):
            panel = M.native_panel(index)
            for h in (1, 2, 3, 4):
                low, _ = M.boundary_constant(panel, h, Fraction(1, 2 * panel["p"]))
                self.assertGreater(low, 0)

    def test_sixth_order_radial_source_control(self):
        for order in (1, 2):
            result = M.radial_control(
                M.native_panel(0), order, Fraction(999, 1000), Fraction(1, 10)
            )
            self.assertTrue(result["above_half_actual_constant"])

    def test_scalar_kernel_requires_nonidentity_resonances(self):
        for q in (5, 7):
            result = M.scalar_kernel_control(q, Fraction(1, 2 * q))
            actual = Fraction(*result["actual_partial_constant"])
            wrong = Fraction(*result["wrong_identity_only"])
            self.assertGreater(actual, wrong)
            self.assertGreaterEqual(
                actual - wrong, Fraction(*result["first_omitted_term_lower_bound"])
            )

    def test_identity_only_source_coefficient_is_ten_over_24(self):
        self.assertEqual(Fraction(10, 24), Fraction(5, 12))
        z = Fraction(999, 1000)
        self.assertEqual((1 - z) ** 6 * M.class_values(z)[0], 1 + 6 * z + 3 * z * z)

    def test_analytic_control_domains_are_enforced(self):
        panel = M.native_panel(0)
        with self.assertRaises(ValueError):
            M.class_values(Fraction(1))
        with self.assertRaises(ValueError):
            M.boundary_constant(panel, 1, Fraction(1, 5))
        with self.assertRaises(ValueError):
            M.radial_control(panel, 3, Fraction(999, 1000), Fraction(1, 10))
        with self.assertRaises(ValueError):
            M.finite_duality(panel, 4)

    def test_class_table_agrees_with_frozen_arithmetic_source(self):
        self.assertEqual(tuple(M.S4.CHARACTERS[name] for name in M.CLASSES), M.TABLE)

    def test_frozen_dependencies(self):
        M.authenticate_frozen()

    def test_forged_fixture_fails(self):
        with self.assertRaises(ValueError):
            M.check_payload(
                {"schema": "finite-group-source-boundary-s4-v1", "status": "PASS"}
            )


if __name__ == "__main__":
    unittest.main()
