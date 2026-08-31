"""Exact source normalization and the inherited opposite-owner count."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "canonical_anchor_diagonal_saturation.py"
)
SPEC = importlib.util.spec_from_file_location("canonical_anchor_saturation", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class CanonicalAnchorDiagonalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.native = json.loads(M.source_bytes((M.DENSE, M.DENSE_JSON)))
        cls.control = M.dense_control(cls.native)

    def test_all_opposite_owners_are_counted_once(self):
        control = self.control
        self.assertEqual(control["arithmetic_pairs"], 16)
        self.assertEqual(control["opposite_owner_count"], 4)
        self.assertEqual(Fraction(control["H_all_Q_over_one_Q"]), 4)
        per_q = [Fraction(row["value"]) for row in control["per_Q_H_over_Gamma0"]]
        self.assertEqual(len(set(per_q)), 1)
        self.assertEqual(sum(per_q), Fraction(control["H_direct_over_Gamma0"]))

    def test_physical_sum_equals_independent_factored_sum(self):
        self.assertEqual(
            Fraction(self.control["H_direct_over_Gamma0"]),
            Fraction(self.control["H_factorized_over_Gamma0"]),
        )
        direct = sum(
            Fraction(row["principal_weight"])
            * Fraction(row["left_coefficient_square"])
            * Fraction(row["right_coefficient_square"])
            for row in self.control["all_pair_checks"]
        )
        self.assertEqual(direct, Fraction(self.control["H_direct_over_Gamma0"]))

    def test_principal_gauss_normalization_is_not_dropped(self):
        ell = self.control["ell"]
        factor = Fraction(ell + 1, ell - 1)
        self.assertEqual(Fraction(self.control["principal_c_ell"]), factor)
        self.assertGreater(factor, 1)
        for row in self.control["all_pair_checks"]:
            expected = self.control["g"] ** 2 * ell * row["Q"] * factor
            self.assertEqual(Fraction(row["principal_weight"]), expected)

    def test_literal_anchor_and_both_atom_diagonals_remain_distinct(self):
        value = Fraction(self.control["H_direct_over_Gamma0"])
        self.assertEqual(self.control["literal_histories"], 64)
        self.assertEqual(
            Fraction(self.control["literal_left_anchor_over_Gamma0"]), value / 2
        )
        self.assertEqual(
            Fraction(self.control["literal_both_atom_over_Gamma0"]), value / 4
        )

    def test_tail_coherence_control_is_not_atomic_or_a_new_prime_source(self):
        row = M.reciprocal_tail_bounds([101, 103, 107, 109])
        lower = Fraction(row["coherent_lower"])
        atomic = Fraction(row["atomic_over_Gamma0"])
        self.assertGreater(lower, atomic)
        self.assertLessEqual(lower, 4 * atomic)
        self.assertEqual(Fraction(row["coherent_upper"]), 384 * lower)
        self.assertFalse(row["new_native_prime_source_claimed"])
        self.assertFalse(self.control["cofinal_tail_coherence_inferred_from_fixture"])

    def test_changed_physical_index_or_coefficient_is_rejected(self):
        for key, value in (
            ("N", self.native["record"]["entries"][0]["N"] + 1),
            ("coefficient_square", "1"),
            ("class", [True, 1]),
        ):
            native = copy.deepcopy(self.native)
            native["record"]["entries"][0][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                M.dense_control(native)

    def test_missing_opposite_owner_and_counter_type_are_rejected(self):
        missing = copy.deepcopy(self.native)
        missing["record"]["entries"].pop()
        with self.assertRaises(ValueError):
            M.dense_control(missing)
        wrong = copy.deepcopy(self.native)
        wrong["record"]["literal_histories"] = 64.0
        with self.assertRaises(ValueError):
            M.dense_control(wrong)

    def test_bounded_exact_inputs_and_tail_frequency_gate(self):
        for value in (True, 1.0, 0, -1, 1 << 129):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.integer(value)
        for values in ([], [1] * 33, [101, 101], [100, 110], [True]):
            with self.subTest(values=values), self.assertRaises(ValueError):
                M.reciprocal_tail_bounds(values)

    def test_source_blob_and_typed_json_counterfeits_are_rejected(self):
        key = (M.DENSE, M.DENSE_JSON)
        with patch.dict(M.SOURCES, {key: "0" * 40}), self.assertRaises(ValueError):
            M.source_bytes(key)
        for value in (True, 1.0):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.replay_equal({"count": value}, {"count": 1})

    def test_prior_retractions_and_restricted_scope_are_preserved(self):
        result = M.build()
        self.assertEqual(result["prior_retractions"], ["R-106095", "R-106110"])
        self.assertEqual(len(result["sources"]), 7)
        self.assertFalse(result["new_historical_error_claimed"])
        self.assertFalse(result["full_native_gamma_identification_claimed"])
        self.assertFalse(result["unrestricted_tail_lower_bound_claimed"])
        self.assertFalse(result["corrected_dual_amplified_moment_refuted"])


if __name__ == "__main__":
    unittest.main()
