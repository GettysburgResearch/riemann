"""Exact source charts, nonflat fibre, covariant quotient and ladder controls."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/extension-order-defect/normalization_replay.py"
)
SPEC = importlib.util.spec_from_file_location("normalization_replay", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NormalizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = M.build()

    def test_six_exact_source_bindings(self):
        self.assertEqual(len(self.payload["sources"]), 6)
        self.assertTrue(all(len(row["blob"]) == 40 for row in self.payload["sources"]))
        self.assertEqual(
            self.payload["sources"][0]["commit"],
            "d4fcbe331751e1e506cc2f38864c0c1580df92e8",
        )

    def test_authentication_before_any_source_import_or_construction(self):
        with (
            patch.object(M, "authenticate", side_effect=ValueError("bad source")),
            patch.object(M, "load_frozen_c6") as loader,
            patch.object(M, "source_lie_rows") as constructor,
        ):
            with self.assertRaisesRegex(ValueError, "bad source"):
                M.build()
            loader.assert_not_called()
            constructor.assert_not_called()

    def test_actual_six_coordinate_weights(self):
        self.assertEqual(self.payload["fixed_locus"]["weights"], [1, 2, 0, 2, 0, 1])
        self.assertEqual(
            self.payload["fixed_locus"]["coordinate_order"],
            ["a", "b", "c", "d", "e", "f"],
        )

    def test_actual_minors_leave_two_axes(self):
        row = self.payload["fixed_locus"]
        self.assertEqual(
            row["fixed_specialization"],
            [[], [], [{"coefficient": -1, "exponents": [0, 0, 1, 0, 1, 0]}]],
        )
        self.assertEqual(row["geometric_fixed_codimension_A"], 3)
        self.assertFalse(row["scheme_fixed_A_reduced_claimed"])

    def test_scaled_source_chart_relations(self):
        rows = M.chart_relations()
        self.assertEqual(
            [row["left"] for row in rows], [[3, 3, 0], [3, 1, 1], [6, 0, 3], [0, 3, 3]]
        )
        self.assertTrue(all(row["left"] == row["right"] for row in rows))

    def test_all_bounded_chart_monomials_round_trip(self):
        for row in self.payload["scaled_source_chart"]["bounded_monomials"]:
            z, p, q = row["z_p_q"]
            s, x, y = row["s_x_y"]
            self.assertEqual((3 * s + x + 2 * y, x, y), (z, p, q))
            self.assertEqual((2 * z + p + 2 * q) % 3, 0)

    def test_chart_requires_the_inverted_base_unit(self):
        self.assertEqual(M.chart_reduce((0, 3, 0)), (-1, 3, 0))
        self.assertEqual(M.chart_reduce((0, 0, 3)), (-2, 0, 3))
        with self.assertRaisesRegex(ValueError, "diagonal invariant"):
            M.chart_reduce((0, 1, 0))

    def test_wrong_chart_weight_is_caught(self):
        with self.assertRaisesRegex(ValueError, "scaled A2"):
            M.chart_relations(1)

    def test_actual_fibre_multiplication_relations(self):
        row = self.payload["actual_origin_fibre"]
        p, q = row["multiplication_p"], row["multiplication_q"]
        zero = [[0] * 5 for _ in range(5)]
        self.assertEqual(M.matrix_product(M.matrix_product(p, p), p), zero)
        self.assertEqual(M.matrix_product(M.matrix_product(q, q), q), zero)
        self.assertEqual(M.matrix_product(p, q), zero)
        self.assertNotEqual(M.matrix_product(p, p), zero)

    def test_nonflat_fibre_is_not_vertex_or_generic_rank(self):
        row = self.payload["actual_origin_fibre"]
        self.assertEqual(
            (
                row["generic_field_degree"],
                row["fibre_length"],
                row["full_homogeneous_vertex_minimum"],
            ),
            (3, 5, 33),
        )
        self.assertFalse(row["finite_flat_at_origin"])

    def test_residual_action_preserves_full_multiplication(self):
        row = self.payload["actual_origin_fibre"]
        phi = row["residual_phi"]
        self.assertEqual(M.matrix_product(phi, phi), M.identity(5))
        self.assertEqual(
            M.matrix_product(M.matrix_product(phi, row["multiplication_p"]), phi),
            row["multiplication_q"],
        )
        self.assertEqual(row["phi_characteristic_polynomial"], [1, -1, -2, 2, 1, -1])

    def test_cyclic_fibre_trace_retains_opposed_weights(self):
        row = self.payload["actual_origin_fibre"]
        self.assertEqual(row["C3_weights"], [0, 1, 2, 2, 1])
        self.assertEqual(row["C3_trace_in_basis_1_omega"], [-1, 0])
        self.assertEqual(row["C3_characteristic_polynomial"], [1, 1, 1, -1, -1, -1])

    def test_actual_single_standard_pair_full_polynomial(self):
        self.assertEqual(
            self.payload["actual_C6_minimal_polynomial"], [1, 0, 0, 0, 12, 0, 16, 0, 4]
        )
        self.assertEqual(
            self.payload["literal_polynomial_covariant_controls"][0][
                "minimal_polynomial"
            ],
            self.payload["actual_C6_minimal_polynomial"],
        )

    def test_linear_only_counterfeit_misses_sixteen_generators(self):
        row = self.payload["literal_polynomial_covariant_controls"][0]
        self.assertEqual(sum(row["linear_only_lower_bound"]), 17)
        self.assertEqual(sum(row["minimal_polynomial"]), 33)
        self.assertFalse(row["linear_only_is_full"])

    def test_same_charge_squares_and_mixed_pairs_survive(self):
        source = ((1, 1), (3, 1))
        result = M.literal_covariants(source)
        self.assertEqual(sorted(result[2]), [(0, 2), (1, 1), (2, 0)])
        self.assertEqual(sorted(result[1]), [(0, 1), (1, 0)])

    def test_opposite_pair_and_equal_triple_are_base_factors(self):
        source = ((2, 1), (2, 2))
        self.assertEqual(M.positive_invariant_divisor((1, 1), source), (1, 1))
        self.assertEqual(M.positive_invariant_divisor((3, 0), source), (3, 0))
        self.assertIsNone(M.positive_invariant_divisor((2, 0), source))

    def test_arbitrary_trivial_variables_do_not_add_module_generators(self):
        without = ((2, 1), (2, 2))
        with_trivial = ((1, 0), (2, 1), (2, 2), (7, 0))
        self.assertEqual(
            M.general_minimal_formula(without), M.general_minimal_formula(with_trivial)
        )
        self.assertEqual(M.general_minimal_formula(((1, 0), (2, 0))), [1])

    def test_all_literal_survivors_have_length_at_most_two(self):
        for row in self.payload["literal_polynomial_covariant_controls"]:
            for key in ("literal_Pbar1", "literal_Pbar2"):
                self.assertTrue(all(1 <= sum(value) <= 2 for value in row[key]))
        self.assertEqual(M.literal_covariants(((3, 2),), 8), {1: [(2,)], 2: [(1,)]})

    def test_actual_A_covariant_source_before_series_formula(self):
        for row in self.payload["actual_A_covariants"]:
            self.assertEqual(row["polynomial"], [0, 0, 6, 0, 2])
            self.assertEqual(len(row["monomials"]), 8)

    def test_first_four_actual_PBW_representations(self):
        rows = self.payload["independent_PBW_source_rows"]
        self.assertEqual(
            [row["multiplicities"] for row in rows[:4]],
            [[1, 1, 2], [1, 0, 1], [0, 0, 1], [0, 1, 1]],
        )
        self.assertEqual(
            [row["class_traces"] for row in rows[:4]],
            [[6, 0, 0], [3, 1, 0], [2, 0, -1], [3, -1, 0]],
        )

    def test_all_sixteen_source_rows_are_independently_reconstructed(self):
        self.assertTrue(self.payload["all_sixteen_rows_match_frozen_source"])
        self.assertEqual(len(self.payload["independent_PBW_source_rows"]), 16)
        for row in self.payload["independent_PBW_source_rows"]:
            a, b, c = row["multiplicities"]
            self.assertEqual(a + b + 2 * c, row["class_traces"][0])
        self.assertEqual(M.power_class(1, 2), 0)
        self.assertEqual(M.power_class(2, 3), 0)

    def test_actual_first_cutoff_matches_literal_C6_module(self):
        rows = self.payload["actual_ladder_minimal_polynomials"]
        self.assertEqual(
            rows[0]["full_minimal_polynomial"],
            self.payload["actual_C6_minimal_polynomial"],
        )
        self.assertEqual(rows[0]["C_polynomial"], [0, 0, 1])

    def test_held_out_cutoff_keeps_quadratic_generators_compressed(self):
        row = self.payload["actual_ladder_minimal_polynomials"][-1]
        self.assertEqual(row["cutoff"], 16)
        self.assertEqual(len(row["full_minimal_polynomial"]), 37)
        c16 = row["C_polynomial"][16]
        self.assertEqual(row["full_minimal_polynomial"][36], 2 * (c16 * c16 + c16))
        self.assertFalse(row["expanded_Lie_generator_basis"])
        self.assertEqual(row["generic_field_degree"], 3)

    def test_harmonic_calibration_does_not_claim_fitted_remainder(self):
        row = self.payload["asymptotic_calibration"]
        self.assertEqual(row["leading_constant_even_half_grade"], [13, 144])
        self.assertFalse(row["asymptotic_fitted_from_samples"])
        self.assertFalse(row["uniform_O_remainder_claimed"])

    def test_primitive_types_fail_before_construction(self):
        for value in (True, 2.0, "2"):
            with self.assertRaises(ValueError):
                M.source_lie_rows(value)
            with self.assertRaises(ValueError):
                M.generators(((2, value),))
            with self.assertRaises(ValueError):
                M.chart_reduce((0, value, 0))
        with self.assertRaises(ValueError):
            M.matrix_product([[True]], [[1]])

    def test_declared_caps_are_enforced(self):
        for call in (
            lambda: M.source_lie_rows(17),
            lambda: M.generators(((2, 1),) * 7),
            lambda: M.chart_reduce((9, 0, 0)),
            lambda: M.literal_covariants(((2, 1),), 9),
            lambda: M.poly_multiply([1] * 20, [1] * 20),
            lambda: M.identity(17),
        ):
            with self.assertRaises(ValueError):
                call()

    def test_strict_fixture_acceptance_rejects_numeric_aliases(self):
        for replacement in (True, 1.0):
            bad = copy.deepcopy(self.payload)
            bad["actual_C6_minimal_polynomial"][0] = replacement
            with self.assertRaisesRegex(ValueError, "strict full"):
                M.verify_payload(bad, self.payload)
        M.verify_payload(M.read_json(M.canonical(self.payload)), self.payload)

    def test_duplicate_float_nonfinite_and_scope_controls(self):
        for raw in ('{"a":1,"a":2}', '{"a":1.0}', '{"a":NaN}', '{"a":Infinity}'):
            with self.assertRaises(ValueError):
                M.read_json(raw)
        scope = self.payload["scope"]
        self.assertFalse(scope["arbitrary_Euler_source_uniqueness"])
        self.assertFalse(scope["old_C_over_B_cokernel_is_a_Bprime_module"])
        self.assertFalse(scope["analytic_frame_selected_by_normalization"])


if __name__ == "__main__":
    unittest.main()
