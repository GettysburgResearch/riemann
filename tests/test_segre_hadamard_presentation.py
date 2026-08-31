"""Actual source presentation, multiplication witnesses, and marked-section limits."""

from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/segre-hadamard-source/presentation_replay.py"
)
SPEC = importlib.util.spec_from_file_location("segre_actual_presentation", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def retained_columns(evaluation):
    return [dict(column) for column in evaluation["sparse_columns_row_coefficient"]]


def retained_relation(evaluation, column):
    domain = {
        (g, tuple(exponent)): j
        for j, (g, exponent) in enumerate(
            evaluation["domain_basis_generator_and_S_exponents"]
        )
    }
    return {
        domain[(term["generator"], tuple(term["S_exponent"]))]: term["coefficient"]
        for term in column["terms"]
    }


class PrimitiveMultiplication(unittest.TestCase):
    def test_literal_symmetric_content_has_six_distinct_words(self):
        index = M.w_contents().index((1, 1, 1))
        self.assertEqual(len(M.w_images()[index]), 6)
        self.assertEqual({coefficient for _, coefficient in M.w_images()[index]}, {1})

    def test_polynomial_square_uses_actual_multiplicities(self):
        exponent = [0] * 10
        exponent[M.w_contents().index((1, 1, 1))] = 2
        image = M.s_image(exponent)
        self.assertEqual(sum(coefficient for _, coefficient in image), 36)
        self.assertTrue(any(coefficient > 1 for _, coefficient in image))
        self.assertEqual({M.source_weight(a) for a, _ in image}, {(2, 2, 2)})

    def test_source_bases_are_complete_tensor_monomial_bases(self):
        self.assertEqual([len(M.source_basis(j)) for j in range(4)], [1, 27, 216, 1000])
        self.assertEqual(len(set(M.source_basis(3))), 1000)

    def test_caps_and_types_precede_cached_calls(self):
        M.source_basis(1)
        for value in (True, 1.0, -1, 4):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.source_basis(value)
        for value in (True, 3.0, 1, 4):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.build_maps(value)

    def test_polynomial_and_source_exponents_reject_coercion(self):
        for exponent in ([True] + [0] * 9, [1.0] + [0] * 9, [3, 1] + [0] * 8):
            with self.subTest(exponent=exponent), self.assertRaises(ValueError):
                M.s_image(exponent)
        with self.assertRaisesRegex(ValueError, "unequal"):
            M.source_weight((1, 0, 0, 0, 0, 0, 0, 0, 0))

    def test_kernel_witness_stays_in_original_column_coordinates(self):
        evaluation = {
            "columns": [{0: 1}, {1: 1}, {0: 2, 1: 3}],
            "weights": [(0, 0, 0)] * 3,
        }
        kernels, weights, stats = M.exact_kernel(evaluation)
        self.assertEqual(kernels, [{0: -2, 1: -3, 2: 1}])
        self.assertEqual(weights, [(0, 0, 0)])
        self.assertEqual((stats[0]["rank"], stats[0]["nullity"]), (2, 1))

    def test_primitive_integer_normalization_retains_sign_and_gcd(self):
        relation = M.primitive_integer({0: Fraction(2, 3), 2: Fraction(-4, 5)})
        self.assertEqual(relation, {0: -5, 2: 6})

    def test_exact_arithmetic_cap_is_enforced(self):
        with self.assertRaisesRegex(ValueError, "bit cap"):
            M.Span().add({0: Fraction(1, 1 << 5000), 1: 1})


class ActualFirstPresentation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = M.authenticate_source()
        cls.maps = M.build_maps()
        cls.evaluations = {row["grade"]: row for row in cls.maps["evaluations"]}

    def test_actual_greedy_generator_quotients(self):
        self.assertEqual(
            Counter(g["degree"] for g in self.maps["generators"]), {0: 1, 1: 17, 2: 11}
        )
        self.assertEqual(
            [
                (row["old_domain_dimension"], row["old_image_rank"])
                for row in self.maps["generator_selection"]
            ],
            [(10, 10), (225, 205)],
        )

    def test_actual_evaluation_ranks_not_signed_numerator(self):
        rows = M.summary(self.maps)["evaluations"]
        self.assertEqual(
            [(r["rows"], r["columns"], r["rank"], r["nullity"]) for r in rows],
            [(216, 236, 216, 20), (1000, 1265, 1000, 265)],
        )
        self.assertNotEqual(11 - 20, 20)

    def test_all_evaluation_columns_rebuild_from_literal_source(self):
        for grade, retained in self.evaluations.items():
            actual = M.evaluate(self.maps["generators"], grade)
            self.assertEqual(actual["columns"], retained_columns(retained))
            self.assertEqual(actual["weights"], retained["column_weights"])

    def test_every_retained_D1_column_substitutes_to_zero(self):
        for column in self.maps["D1_columns"]:
            evaluation = self.evaluations[column["degree"]]
            relation = retained_relation(evaluation, column)
            self.assertEqual(
                M.image_of_relation(retained_columns(evaluation), relation), {}
            )
            self.assertEqual(M.primitive_integer(relation), relation)

    def test_one_wrong_actual_relation_coefficient_is_detected(self):
        column = self.maps["D1_columns"][0]
        evaluation = self.evaluations[2]
        relation = retained_relation(evaluation, column)
        relation[max(relation)] += 1
        self.assertTrue(M.image_of_relation(retained_columns(evaluation), relation))

    def test_all_first_differential_entries_are_in_the_irrelevant_ideal(self):
        for column in self.maps["D1_columns"]:
            for term in column["terms"]:
                generator = self.maps["generators"][term["generator"]]
                self.assertGreater(sum(term["S_exponent"]), 0)
                self.assertEqual(
                    generator["degree"] + sum(term["S_exponent"]), column["degree"]
                )
                self.assertEqual(
                    M.add_weights(
                        generator["weight"], M.polynomial_weight(term["S_exponent"])
                    ),
                    column["weight"],
                )

    def test_old_relation_columns_are_all_actual_variable_multiples(self):
        old = self.maps["old_relation_multiplication"]
        degree_two = M.evaluate(self.maps["generators"], 2)
        degree_three = M.evaluate(self.maps["generators"], 3)
        relations = [
            retained_relation(self.evaluations[2], column)
            for column in self.maps["D1_columns"]
            if column["degree"] == 2
        ]
        self.assertEqual(len(old["sparse_columns_F0_degree3"]), 200)
        for (relation, variable), retained in zip(
            old["source_labels_relation_variable"],
            old["sparse_columns_F0_degree3"],
            strict=True,
        ):
            self.assertEqual(
                M.multiply_relation(
                    relations[relation], degree_two, degree_three, variable
                ),
                dict(retained),
            )

    def test_old_plus_new_relations_span_the_complete_cubic_kernel(self):
        old = self.maps["old_relation_multiplication"]
        span = M.Span()
        for column in old["sparse_columns_F0_degree3"]:
            self.assertTrue(span.add(dict(column)))
        self.assertEqual(len(span), 200)
        for column in self.maps["D1_columns"]:
            if column["degree"] == 3:
                self.assertTrue(
                    span.add(retained_relation(self.evaluations[3], column))
                )
        self.assertEqual(len(span), 265)
        for column in self.maps["full_degree3_kernel_basis"]:
            self.assertFalse(span.add(dict(column)))

    def test_minimal_relation_weight_dimensions_match_frozen_actual_Tor(self):
        rows = M.compare_frozen_tor(self.source, self.maps)
        self.assertEqual([row["dimension"] for row in rows], [17, 11, 20, 65])
        self.assertTrue(all(row["complete_weight_match"] for row in rows))

    def test_missing_frozen_grade_is_not_replaced_by_Betti_prediction(self):
        source = copy.deepcopy(self.source)
        source["result"]["literal_koszul_sources"] = [
            row
            for row in source["result"]["literal_koszul_sources"]
            if not (
                row["dimension"] == 3 and row["factor_count"] == 3 and row["grade"] == 3
            )
        ]
        with self.assertRaisesRegex(ValueError, "coverage"):
            M.compare_frozen_tor(source, self.maps)

    def test_marked_monomial_section_does_not_commute_with_factor_permutation(self):
        witness = self.maps["section_countercontrol"]
        chosen = {
            g["source_exponent"] for g in self.maps["generators"] if g["degree"] == 1
        }
        self.assertIn(witness["chosen_source_monomial"], chosen)
        self.assertNotIn(witness["image_source_monomial"], chosen)
        self.assertFalse(witness["equivariant_section_claimed"])
        self.assertEqual(
            M.source_weight(witness["chosen_source_monomial"]),
            M.source_weight(witness["image_source_monomial"]),
        )

    def test_all_retained_weight_blocks_respect_preregistered_caps(self):
        for evaluation in self.evaluations.values():
            self.assertEqual(
                sum(row["columns"] for row in evaluation["weight_blocks"]),
                len(evaluation["domain_basis_generator_and_S_exponents"]),
            )
            for row in evaluation["weight_blocks"]:
                self.assertLessEqual(max(row["rows"], row["columns"]), M.MAX_BLOCK)
                self.assertLessEqual(row["max_exact_bits"], M.MAX_BITS)


class ProvenanceAndStrictRecord(unittest.TestCase):
    def test_working_byte_corruption_is_rejected_before_source_use(self):
        with (
            patch.object(M, "canonical_bytes", return_value=b"counterfeit"),
            self.assertRaisesRegex(ValueError, "working source bytes"),
        ):
            M.authenticate_source()

    def test_full_record_binds_actual_matrices_and_scope(self):
        record = M.build()
        self.assertEqual(len(record["result"]["D1_columns"]), 85)
        self.assertTrue(record["scope"]["actual_source_maps"])
        self.assertFalse(
            record["scope"]["GL3_or_factor_S3_equivariant_splittings_claimed"]
        )
        self.assertFalse(
            record["scope"]["second_and_third_differential_matrices_constructed"]
        )
        self.assertTrue(M.check_payload(json.loads(M.canonical_json(record)), record))

    def test_boolean_counterfeit_with_unchanged_proof_hash_is_rejected(self):
        expected = {"coefficient": 1, "proof_object_sha256": "unchanged"}
        with self.assertRaisesRegex(ValueError, "typed canonical"):
            M.check_payload({**expected, "coefficient": True}, expected)

    def test_float_counterfeit_with_unchanged_proof_hash_is_rejected(self):
        expected = {"coefficient": 1, "proof_object_sha256": "unchanged"}
        with self.assertRaisesRegex(ValueError, "typed canonical"):
            M.check_payload({**expected, "coefficient": 1.0}, expected)

    def test_wrong_integer_coefficient_with_unchanged_proof_hash_is_rejected(self):
        expected = {"coefficient": 1, "proof_object_sha256": "unchanged"}
        with self.assertRaisesRegex(ValueError, "typed canonical"):
            M.check_payload({**expected, "coefficient": 2}, expected)

    def test_nonfinite_JSON_is_rejected(self):
        with self.assertRaises(ValueError):
            M.check_payload({"coefficient": float("nan")}, {"coefficient": 1})


if __name__ == "__main__":
    unittest.main()
