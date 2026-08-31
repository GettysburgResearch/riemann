"""Primitive covariant, invariant-base and weighted matrix controls."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/extension-order-defect/cyclic_infinity_replay.py"
)
SPEC = importlib.util.spec_from_file_location("cyclic_infinity_replay", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class CyclicInfinityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = M.build()

    def test_actual_three_source_pins(self):
        self.assertEqual(len(self.payload["sources"]), 3)
        self.assertTrue(all(len(row["blob"]) == 40 for row in self.payload["sources"]))

    def test_authentication_precedes_source_construction(self):
        with (
            patch.object(M, "authenticate", side_effect=ValueError("bad source")),
            patch.object(M, "combined_minimal") as constructor,
        ):
            with self.assertRaisesRegex(ValueError, "bad source"):
                M.build()
            constructor.assert_not_called()

    def test_literal_segre_dimensions(self):
        for n in range(9):
            self.assertEqual(len(M.segre_basis(n)), (n + 1) ** 2 * (n + 2) // 2)

    def test_even_source_degree_two_covariants(self):
        for character in (1, 2):
            self.assertEqual(len(M.segre_basis(2, character)), 6)
            self.assertEqual(sum(x[0] == 2 for x in M.covariant_minimal(character)), 6)

    def test_actual_degree_four_product_rank(self):
        for character in (1, 2):
            row = M.degree_four_old_span(character)
            self.assertEqual((row["basis_dimension"], row["old_rank"]), (25, 23))

    def test_four_literal_new_covariants(self):
        self.assertEqual(
            M.degree_four_old_span(1)["new_monomials"],
            [[4, 0, 0, 0, 4], [4, 4, 4, 0, 0]],
        )
        self.assertEqual(
            M.degree_four_old_span(2)["new_monomials"],
            [[4, 0, 4, 0, 0], [4, 4, 0, 4, 0]],
        )

    def test_held_out_generation_retains_all_monomials(self):
        for character in (1, 2):
            generators = M.covariant_minimal(character, cutoff=4)
            for n in (6, 8):
                self.assertTrue(
                    all(
                        any(M.divides(g, value) for g in generators)
                        for value in M.segre_basis(n, character)
                    )
                )

    def test_actual_full_base_minimal_quotient(self):
        expected = {str(n): {0: 1, 4: 12, 6: 16, 8: 4}.get(n, 0) for n in range(9)}
        self.assertEqual(self.payload["actual_minimal_by_degree"], expected)
        self.assertEqual(len(self.payload["actual_minimal_monomials"]), 33)

    def test_quadratic_projection_counterfeit(self):
        self.assertEqual(len(M.combined_minimal(False)), 17)
        self.assertNotEqual(M.combined_minimal(True), M.combined_minimal(False))
        self.assertTrue(
            any(M.combined_degree(x) == 3 for x in M.combined_minimal(False))
        )
        self.assertFalse(
            any(M.combined_degree(x) % 2 for x in M.combined_minimal(True))
        )

    def test_full_invariant_base_reduces_new_generators(self):
        self.assertTrue(M.reducible_over_full_base((0, 0, 0, 0, 0, 1, 1)))
        self.assertTrue(M.reducible_over_full_base((0, 0, 0, 0, 0, 3, 0)))
        self.assertFalse(M.reducible_over_full_base((0, 0, 0, 0, 0, 0, 0)))

    def test_residual_normalizer_not_just_first_trace(self):
        for row in self.payload["residual_normalizer"]:
            self.assertEqual(row["trace_square"], row["dimension"])
            self.assertEqual(row["trace"], int(row["degree"] == 0))
            if row["degree"]:
                self.assertGreater(row["dimension"], 1)
                self.assertTrue(all(len(cycle) == 2 for cycle in row["cycles"]))

    def test_residual_determinants(self):
        for row in self.payload["residual_normalizer"]:
            if row["degree"]:
                expected = [1]
                for _ in range(row["dimension"] // 2):
                    expected = M.int_polynomial_multiply(expected, [1, 0, -1])
                self.assertEqual(row["determinant"], expected)

    def test_full_Molien_series_independent_monomials(self):
        self.assertEqual(
            self.payload["full_C_dimensions_even_grades_0_to_8"],
            self.payload["independent_frozen_Molien_coefficients"],
        )
        self.assertEqual(len(M.combined_basis(0)), 1)

    def test_generic_rank_not_minimal_generator_count(self):
        row = self.payload["generic_rank_control"]
        self.assertEqual(
            row["independent_group_order"] // row["diagonal_group_order"], 3
        )
        self.assertEqual(row["minimal_generator_count"], 33)

    def test_matrix_factorization_before_quotient(self):
        d1, d2 = M.matrices()
        f = {(1, 0, 1): 1, (0, 3, 0): -1}
        self.assertEqual(M.multiply_matrix(d1, d2), [[f, {}], [{}, f]])
        self.assertEqual(M.multiply_matrix(d2, d1), [[f, {}], [{}, f]])
        self.assertNotEqual(f, {})

    def test_matrix_factorization_substitution(self):
        d1, d2 = M.matrices()
        self.assertTrue(
            all(
                not M.substitute_pq(entry)
                for row in M.multiply_matrix(d1, d2)
                for entry in row
            )
        )

    def test_wrong_relation_sign_is_caught(self):
        d1, d2 = M.matrices()
        d1[0][1] = {(0, 2, 0): 1}
        self.assertTrue(
            any(
                M.substitute_pq(entry)
                for row in M.multiply_matrix(d1, d2)
                for entry in row
            )
        )

    def test_normal_forms_retain_hypersurface_relation(self):
        self.assertEqual(M.normal_form((1, 0, 1)), (0, 3, 0))
        self.assertEqual(M.normal_form((2, 1, 1)), (1, 4, 0))
        self.assertEqual(set(M.t_basis(12)), {(2, 0, 0), (0, 3, 0), (0, 0, 2)})

    def test_F0_presentation_domain_and_kernel_dimensions(self):
        rows = [M.mf_control(n) for n in (8, 10, 14, 16)]
        self.assertEqual([len(row["F0_basis"]) for row in rows], [3, 3, 5, 5])
        self.assertEqual([row["presentation"]["nullity"] for row in rows], [1, 1, 2, 2])

    def test_exact_selected_second_kernels(self):
        for n in (8, 10, 14, 16):
            row = M.mf_control(n)
            self.assertEqual(row["presentation"]["nullity"], row["D1"]["rank"])
            self.assertEqual(row["D1"]["nullity"], row["D2"]["rank"])

    def test_wrong_weighted_shift_is_caught(self):
        d1, _ = M.matrices()
        with self.assertRaisesRegex(ValueError, "weighted degree"):
            M.graded_matrix(d1, 10, (6, 10), (2, 4))

    def test_type_and_degree_caps(self):
        for value in (True, 2.0, -1, 9):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.segre_basis(value)
        with self.assertRaises(ValueError):
            M.combined_minimal(1)
        with self.assertRaises(ValueError):
            M.t_basis(17)
        with self.assertRaises(ValueError):
            M.segre_monomial((2, 1, 1, 1, 1))

    def test_hypersurface_polynomial_caps(self):
        with self.assertRaises(ValueError):
            M.uvw_poly({(True, 0, 0): 1})
        with self.assertRaises(ValueError):
            M.uvw_poly({(6, 0, 0): 1})
        with self.assertRaises(ValueError):
            M.uvw_poly({(1, 0, 0): True})

    def test_strict_JSON_rejects_numeric_counterfeits(self):
        boolean = copy.deepcopy(self.payload)
        boolean["actual_minimal_by_degree"]["0"] = True
        floating = copy.deepcopy(self.payload)
        floating["generic_rank_control"]["minimal_generator_count"] = 33.0
        for counterfeit in (boolean, floating):
            with self.assertRaises(ValueError):
                M.verify_payload(counterfeit, self.payload)

    def test_strict_JSON_rejects_extra_or_missing_coverage(self):
        for change in ("extra", "missing"):
            counterfeit = copy.deepcopy(self.payload)
            if change == "extra":
                counterfeit["unclaimed"] = 0
            else:
                counterfeit["actual_minimal_monomials"].pop()
            with self.assertRaises(ValueError):
                M.verify_payload(counterfeit, self.payload)

    def test_JSON_reader_rejects_duplicates_floats_and_nonfinite(self):
        for raw in ('{"x":1,"x":2}', '{"x":1.0}', '{"x":NaN}', '{"x":Infinity}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                M.read_json(raw)

    def test_scope_keeps_relative_and_original_base_distinct(self):
        scope = self.payload["scope"]
        self.assertFalse(scope["old_cokernel_is_a_module_over_repaired_base"])
        self.assertFalse(scope["whole_base_free_periodic_resolution_supplied"])
        self.assertTrue(scope["relative_covariant_complex_supplied"])

    def test_full_payload_replay_accepts_exact_typed_copy(self):
        M.verify_payload(M.read_json(M.canonical(self.payload)), self.payload)


if __name__ == "__main__":
    unittest.main()
