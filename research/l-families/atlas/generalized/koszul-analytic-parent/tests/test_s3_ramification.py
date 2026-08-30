"""Independent finite-source, failed-adapter, and arithmetic-stalk controls."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "s3_ramification", HERE / "s3_ramification_replay.py"
)
S = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(S)


class SourceRepresentationTests(unittest.TestCase):
    def test_all_permutation_matrices_preserve_augmentation_action(self):
        for first in S.GROUP:
            for second in S.GROUP:
                composed = tuple(first[second[j]] for j in range(3))
                a = S.source_matrices(first)[0]
                b = S.source_matrices(second)[0]
                actual = tuple(
                    tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
                    for i in range(2)
                )
                self.assertEqual(actual, S.source_matrices(composed)[0])

    def test_native_matrix_character_denominators(self):
        expected = {
            (0, 1, 2): ([1, -2, 1], [1, -3, 3, -1]),
            (1, 0, 2): ([1, 0, -1], [1, -1, -1, 1]),
            (1, 2, 0): ([1, 1, 1], [1, 0, 0, -1]),
        }
        for perm, denominators in expected.items():
            self.assertEqual(
                tuple(S.determinant_polynomial(m) for m in S.source_matrices(perm)),
                denominators,
            )

    def test_symmetric_power_characters(self):
        seq = S.source_sequences(6)
        self.assertEqual(seq["s"], (1, 0, 2, 0, 3, 0, 4))
        self.assertEqual(seq["c"], (1, 0, 0, 1, 0, 0, 1))
        self.assertEqual(seq["e"][:4], (1, 6, 18, 40))

    def test_source_lie_quotient_characters(self):
        self.assertEqual(S.native_low_lie(), [[6, 0, 0], [3, 1, 0], [2, 0, -1]])

    def test_full_fusion_rules(self):
        self.assertEqual(S.fusion((0, 0, 1), (0, 0, 1)), (1, 1, 1))
        self.assertEqual(S.fusion((0, 1, 0), (0, 0, 1)), (0, 0, 1))
        self.assertEqual(S.fusion((0, 1, 0), (0, 1, 0)), (1, 0, 0))

    def test_full_koszul_inverse_heldout_degree(self):
        self.assertTrue(S.fusion_control(17)["full_fusion_inverse"])

    def test_noncharacter_is_rejected(self):
        for characters in ((1, 1, 0), (0, 1, 0), (True, 0, 0)):
            with (
                self.subTest(characters=characters),
                self.assertRaises((TypeError, ValueError)),
            ):
                S.irreducibles(characters)

    def test_primitive_caps_before_expansion(self):
        for value in (25, -1, True, 3.0):
            with self.subTest(value=value), self.assertRaises((TypeError, ValueError)):
                S.source_sequences(value)
        with self.assertRaises(ValueError):
            S.source_matrices((0, 0, 2))


class RamificationTests(unittest.TestCase):
    def test_c2_input_and_lie_shortcuts_both_fail(self):
        result = S.ramification_control(2)
        self.assertEqual(result["actual_invariant_R_dimensions_0_1_2"], [1, 3, 10])
        self.assertEqual(result["naive_input_invariant_dimensions_0_1_2"], [1, 2, 3])
        self.assertEqual(result["invariant_Lie_fake_degree2"], 4)
        self.assertEqual(result["minimum_new_degree2_generators"], 4)

    def test_c3_input_and_lie_shortcuts_both_fail(self):
        result = S.ramification_control(3)
        self.assertEqual(result["actual_invariant_R_dimensions_0_1_2"], [1, 2, 6])
        self.assertEqual(result["naive_input_invariant_dimensions_0_1_2"], [1, 0, 0])
        self.assertEqual(result["invariant_Lie_fake_degree2"], 2)
        self.assertEqual(result["minimum_new_degree2_generators"], 3)

    def test_full_invariant_tensor_terms(self):
        self.assertEqual(
            S.ramification_control(2)["full_invariant_Koszul_degree2_terms"],
            [10, 18, 8],
        )
        self.assertEqual(
            S.ramification_control(3)["full_invariant_Koszul_degree2_terms"], [6, 12, 6]
        )

    def test_dropped_nontrivial_tensor_sectors_are_visible(self):
        self.assertEqual(S.ramification_control(2)["dropped_tensor_sector_Euler"], 9)
        self.assertEqual(S.ramification_control(3)["dropped_tensor_sector_Euler"], 8)

    def test_infinity_dimension_is_not_always_trace(self):
        self.assertEqual(S.infinity_trace(5, 2), [1, 0, 2])
        self.assertEqual(S.infinity_trace(7, 2), [1, 2, 6])
        self.assertNotEqual(
            S.infinity_trace(5, 1)[1],
            S.source_rows(1)[1]["infinite_invariant_dimension"],
        )

    def test_extension_field_restores_trivial_coset(self):
        self.assertEqual(S.infinity_trace(25, 12), S.infinity_trace(7, 12))
        self.assertEqual(S.infinity_trace(125, 12), S.infinity_trace(5, 12))

    def test_invalid_field_sizes(self):
        for q in (1, 3, 9, 10, 15, True, 5.0, 4097):
            with self.subTest(q=q), self.assertRaises((TypeError, ValueError)):
                S.infinity_trace(q, 2)


class ArithmeticFamilyTests(unittest.TestCase):
    def test_finite_grade_one_global_family(self):
        row = S.source_rows(1)[1]
        self.assertEqual(row["global_L_exponents_ZP1_PD_PE"], [1, 1, 2])
        self.assertEqual(row["tame_conductor_degree"], 16)
        self.assertEqual(row["h0_h1_h2_dimensions"], [1, 6, 1])

    def test_grade_zero_is_constant_source(self):
        row = S.source_rows(0)[0]
        self.assertEqual(row["global_L_exponents_ZP1_PD_PE"], [1, 0, 0])
        self.assertEqual(row["h0_h1_h2_dimensions"], [1, 0, 1])
        self.assertEqual(row["tame_conductor_degree"], 0)

    def test_global_cohomology_ledger_heldout(self):
        row = S.source_rows(19)[19]
        d, t, _ = row["characters_e_s_c"]
        a, b, c = row["multiplicities_1_sign_std"]
        self.assertEqual(row["h0_h1_h2_dimensions"], [a, d - t, a])
        self.assertEqual(d - t, 2 * b + 2 * c)

    def test_local_determinants_heldout_grades_and_fields(self):
        for q in (11, 13):
            for place in (*S.CLASSES, "finite_branch", "infinity"):
                with self.subTest(q=q, place=place):
                    S.determinant_trace_check(5, place, q)

    def test_infinity_sign_changes_actual_denominator(self):
        self.assertEqual(S.local_denominator(1, "infinity", 5, 2), [1, 0, -1])
        self.assertEqual(S.local_denominator(1, "infinity", 7, 2), [1, -2, 1])

    def test_finite_branch_is_not_unramified_reflection_factor(self):
        self.assertNotEqual(
            S.local_denominator(1, "finite_branch", 5), S.local_denominator(1, "s", 5)
        )

    def test_unknown_or_excessive_local_case_rejected(self):
        with self.assertRaises(ValueError):
            S.local_denominator(7, "e")
        with self.assertRaises(ValueError):
            S.local_denominator(1, "unknown")

    def test_frozen_source_authentication(self):
        S.authenticate_frozen()

    def test_forged_fixture_cannot_self_certify(self):
        with self.assertRaises(ValueError):
            S.check_payload(
                {"schema": "koszul-s3-ramification-finite-family-v1", "status": "PASS"}
            )


if __name__ == "__main__":
    unittest.main()
