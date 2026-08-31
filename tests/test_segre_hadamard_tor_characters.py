"""Complete weight/class source matching, canonical duality, and Euler traps."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/segre-hadamard-source/tor_character_replay.py"
)
SPEC = importlib.util.spec_from_file_location("segre_tor_characters", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class SchurSourceCharacters(unittest.TestCase):
    def test_interlacing_patterns_recover_the_actual_low_schur_dimensions(self):
        expected = {
            (2, 1, 0): 8,
            (3, 3, 0): 10,
            (4, 1, 1): 10,
            (5, 3, 1): 27,
            (4, 3, 2): 8,
        }
        for lam, dimension in expected.items():
            self.assertEqual(sum(M.schur_weights(lam).values()), dimension)

    def test_determinant_weight_is_not_erased_by_signed_numerator(self):
        self.assertEqual(M.schur_weights((2, 2, 2)), {(2, 2, 2): 1})
        row = M.weights_of_terms(M.LOWER[(0, 2)])
        self.assertEqual(row[(2, 2, 2)], [2, 0, 2])

    def test_partition_validation_precedes_cached_computation(self):
        M.schur_weights((2, 1, 0))
        for lam in ((2.0, 1, 0), (2, True, 0), (1, 2, 0), (8, 0, 0)):
            with self.subTest(lam=lam), self.assertRaises(ValueError):
                M.schur_weights(lam)

    def test_low_grade_class_characters_are_not_only_dimensions(self):
        records = M.table_record(M.LOWER)
        values = {
            (row["homological_degree"], row["internal_degree"]): row["class_traces"]
            for row in records
        }
        self.assertEqual(values[(0, 1)], [17, -1, -7])
        self.assertEqual(values[(0, 2)], [11, -9, 11])
        self.assertEqual(values[(1, 2)], [20, 0, -10])
        self.assertEqual(values[(1, 3)], [65, -25, 35])

    def test_complete_frozen_primitive_weight_rows_match_the_table(self):
        self.assertEqual(len(M.check_primitive_panels(M.authenticate_source())), 9)

    def test_missing_primitive_grade_is_not_silently_completed_by_duality(self):
        source = copy.deepcopy(M.authenticate_source())
        source["result"]["literal_koszul_sources"] = [
            row
            for row in source["result"]["literal_koszul_sources"]
            if (row["dimension"], row["factor_count"], row["grade"]) != (3, 3, 3)
        ]
        with self.assertRaisesRegex(ValueError, "coverage"):
            M.check_primitive_panels(source)

    def test_wrong_homology_character_is_rejected_before_scalar_euler_checks(self):
        source = copy.deepcopy(M.authenticate_source())
        panel = next(
            row
            for row in source["result"]["literal_koszul_sources"]
            if (row["dimension"], row["factor_count"], row["grade"]) == (3, 3, 2)
        )
        row = next(
            row for row in panel["homology_weight_rows"] if row["weight"] == [2, 2, 2]
        )
        row["homology"][0]["identity"] = 1
        with self.assertRaisesRegex(ValueError, "weight/class"):
            M.check_primitive_panels(source)


class CompleteDualityAndClassicalComponent(unittest.TestCase):
    def test_top_twist_is_det_seven_and_factor_sign_is_trivial(self):
        table = M.full_table()
        self.assertEqual(table[(3, 7)], (((7, 7, 7), "trivial"),))
        self.assertFalse(M.check_duality(table)["factor_permutation_sign_twist"])

    def test_all_ten_nonzero_bidegrees_have_the_expected_total_free_ranks(self):
        rows = M.table_record(M.full_table())
        self.assertEqual(len(rows), 10)
        self.assertEqual(
            [
                sum(
                    row["class_traces"][0]
                    for row in rows
                    if row["homological_degree"] == i
                )
                for i in range(4)
            ],
            [29, 85, 85, 29],
        )

    def test_dual_partition_complements_reversed_highest_weight(self):
        self.assertEqual(M.dual_partition((5, 3, 1)), (6, 4, 2))
        self.assertEqual(M.dual_partition(M.dual_partition((5, 3, 1))), (5, 3, 1))

    def test_spurious_factor_sign_twist_breaks_actual_duality(self):
        table = M.full_table()
        table[(3, 7)] = (((7, 7, 7), "sign"),)
        with self.assertRaisesRegex(ValueError, "duality"):
            M.check_duality(table)

    def test_classical_normalization_generator_and_last_two_terms_are_retained(self):
        rows = M.normalization_sector(M.full_table())
        self.assertEqual(len(rows), 6)
        self.assertEqual(rows[1], {"i": 0, "j": 2, "partitions": [[2, 2, 2]]})
        self.assertEqual(
            rows[-2:],
            [
                {"i": 3, "j": 5, "partitions": [[5, 5, 5]]},
                {"i": 3, "j": 7, "partitions": [[7, 7, 7]]},
            ],
        )


class EulerAndProvenanceControls(unittest.TestCase):
    def test_scalar_identity_numerator_is_generator_minus_relation_character(self):
        row = M.euler_control((1, 1, 1))["classes"][0]
        self.assertEqual(row["numerator"], [1, 17, -9, -65, 65, 9, -17, -1])

    def test_all_tensor_cycle_classes_agree_at_generic_and_collision_inputs(self):
        for values in ((2, 3, 5), (1, -1, 2), (2, 2, 3)):
            row = M.euler_control(values)
            self.assertEqual(len(row["classes"]), 3)
            self.assertTrue(
                all(part["tail_through_degree10_zero"] for part in row["classes"])
            )

    def test_diagonal_controls_refuse_singular_and_inexact_values(self):
        for values in ((1, 0, 2), (True, 2, 3), (1.0, 2, 3), (1, 2)):
            with self.subTest(values=values), self.assertRaises(ValueError):
                M.euler_control(values)

    def test_source_authentication_precedes_artifact_interpretation(self):
        with (
            patch.object(M.subprocess, "check_output", return_value="wrong\n"),
            self.assertRaisesRegex(ValueError, "Git object"),
        ):
            M.authenticate_source()

    def test_working_primitive_bytes_are_not_trusted_from_a_good_revision_alone(self):
        with (
            patch.object(M.subprocess, "check_output", return_value=M.PINS[0][1]),
            patch.object(M, "canonical_bytes", return_value=b"wrong"),
            self.assertRaisesRegex(ValueError, "source bytes"),
        ):
            M.authenticate_source()

    def test_payload_distinguishes_characters_from_minimal_differential_maps(self):
        row = M.build_payload()
        self.assertTrue(row["all_Tor_characters_determined"])
        self.assertFalse(row["minimal_differential_matrices_constructed"])
        self.assertFalse(row["new_large_chain_elimination_performed"])
        self.assertFalse(row["arithmetic_S3_source_identified"])

    def test_payload_rejects_false_claim_and_boolean_rank_alias(self):
        row = M.build_payload()
        bad = copy.deepcopy(row)
        bad["minimal_differential_matrices_constructed"] = True
        with self.assertRaises(ValueError):
            M.check_payload(bad)
        bad = copy.deepcopy(row)
        bad["complete_Tor_table"][0]["class_traces"][0] = True
        with self.assertRaises(ValueError):
            M.check_payload(bad)


if __name__ == "__main__":
    unittest.main()
