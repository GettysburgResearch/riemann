"""Actual Chow multiplication, invariant monomials and minimal source maps."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/segre-hadamard-source/invariant_base_replay.py"
)
SPEC = importlib.util.spec_from_file_location("segre_invariant_base", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ActualChowAndBaseTests(unittest.TestCase):
    def test_literal_binary_quotient_has_both_inertia_sectors(self):
        rows = [M.binary_chow_quotient(n) for n in range(4)]
        self.assertEqual(
            [row["quotient_plus_minus"] for row in rows],
            [[1, 0], [2, 2], [0, 1], [0, 0]],
        )

    def test_actual_degree_three_columns_are_not_a_hilbert_formula(self):
        row = M.binary_chow_quotient(3)
        self.assertEqual(row["source_dimension"], 64)
        self.assertEqual(row["literal_W_multiplication_columns"], 108)
        self.assertEqual(sum(row["image_plus_minus"]), 64)

    def test_binary_degree_cap_refuses_unbounded_or_coercible_inputs(self):
        for value in (True, 1.0, -1, 4):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.binary_chow_quotient(value)

    def test_invariant_normal_forms_retain_mixed_odd_exponents(self):
        self.assertEqual(M.normal_form(3, 5), (1, 1, 2))
        self.assertEqual(M.normal_form(4, 2), (2, 0, 1))

    def test_anti_invariant_monomials_cannot_be_relabelled_as_base_elements(self):
        with self.assertRaises(ValueError):
            M.normal_form(2, 3)

    def test_relation_presentation_counts_every_even_monomial_once(self):
        rows = M.invariant_presentation()
        self.assertEqual(
            [row["normal_form_count"] for row in rows], [1, 3, 5, 7, 9, 11, 13]
        )

    def test_matrix_factorization_identity_is_before_hypersurface_reduction(self):
        row = M.matrix_factorization()
        self.assertEqual(row["D_squared"], "-(u*w-v^2)*I_2")
        self.assertTrue(row["identity_checked_before_quotient"])


class ActualResolutionTests(unittest.TestCase):
    def test_first_minimal_generators_surject_onto_the_odd_module(self):
        row = M.resolution_slice(1)
        self.assertEqual(row["free_slice_dimensions"], [2])
        self.assertEqual(row["augmentation_then_differential_ranks"], [2])

    def test_first_two_relations_are_the_actual_syzygies(self):
        row = M.resolution_slice(3)
        self.assertEqual(row["free_slice_dimensions"], [6, 2])
        self.assertEqual(row["augmentation_then_differential_ranks"], [4, 2])

    def test_seven_source_slices_are_exact_in_all_present_homological_degrees(self):
        for degree in range(1, 14, 2):
            with self.subTest(degree=degree):
                row = M.resolution_slice(degree)
                self.assertTrue(row["all_compositions_zero"])
                self.assertTrue(row["exact_in_every_present_homological_degree"])

    def test_last_bounded_slice_does_not_suppress_higher_relations(self):
        row = M.resolution_slice(13)
        self.assertEqual(
            row["augmentation_then_differential_ranks"], [14, 12, 10, 8, 6, 4, 2]
        )

    def test_wrong_first_relation_is_detected_by_augmentation(self):
        columns = M.differential_columns(3, 1)
        columns[0] = {r: abs(value) for r, value in columns[0].items()}
        self.assertTrue(any(M.compose(M.pi_columns(3), columns)))

    def test_parity_and_internal_degree_caps_fail_closed(self):
        for value in (True, 3.0, 2, 15):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.resolution_slice(value)

    def test_homological_indices_cannot_reuse_the_augmentation_as_D(self):
        with self.assertRaises(ValueError):
            M.differential_columns(3, 0)

    def test_rank_uses_exact_linear_dependence_not_column_count(self):
        self.assertEqual(M.rank([{0: 1, 1: 2}, {0: 2, 1: 4}, {1: 1}], 2), 2)
        with self.assertRaises(ValueError):
            M.rank([{0: 1.0}], 1)


class SourceHilbertAndBindingTests(unittest.TestCase):
    def test_invariant_source_and_full_base_module_agree(self):
        row = M.hilbert_controls()
        self.assertEqual(
            row["literal_source_invariants"], row["full_invariant_base_decomposition"]
        )
        self.assertEqual(row["literal_source_invariants"][:5], [1, 4, 14, 32, 63])

    def test_finite_free_counterfeit_first_fails_at_degree_four(self):
        row = M.hilbert_controls()
        self.assertEqual(row["first_false_free_difference"], 4)
        self.assertEqual(row["false_free_on_minimal_generators"][4], 67)

    def test_all_present_resolution_rows_recover_the_source_euler_series(self):
        self.assertTrue(
            M.hilbert_controls(20)["all_present_minimal_resolution_rows_used"]
        )

    def test_frozen_authentication_refuses_wrong_git_object(self):
        with (
            patch.object(M.subprocess, "check_output", return_value="wrong\n"),
            self.assertRaisesRegex(ValueError, "frozen Git"),
        ):
            M.authenticate_source()

    def test_source_bytes_are_authenticated_even_with_correct_revision_response(self):
        with (
            patch.object(M.subprocess, "check_output", return_value=M.PINS[0][1]),
            patch.object(M, "canonical_bytes", return_value=b"wrong"),
            self.assertRaisesRegex(ValueError, "working source"),
        ):
            M.authenticate_source()

    def test_complete_payload_has_only_declared_bounded_slices(self):
        row = M.build_payload()
        self.assertEqual(len(row["exact_source_resolution_slices"]), 7)
        self.assertIn(
            "infinite exact minimal resolution", row["proved_not_inferred_from_cutoff"]
        )

    def test_payload_rejects_the_false_finite_resolution_and_bool_alias(self):
        row = M.build_payload()
        bad = copy.deepcopy(row)
        bad["literal_Chow_quotient"][0]["source_dimension"] = True
        with self.assertRaises(ValueError):
            M.check_payload(bad)
        bad = copy.deepcopy(row)
        bad["exact_source_resolution_slices"] = bad["exact_source_resolution_slices"][
            :1
        ]
        with self.assertRaises(ValueError):
            M.check_payload(bad)


if __name__ == "__main__":
    unittest.main()
