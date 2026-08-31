"""Source-range regression and exact bounded local-frame controls."""

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
    / "fixed_core_owner_range_correction.py"
)
SPEC = importlib.util.spec_from_file_location("fixed_core_range", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class FixedCoreOwnerRangeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.native = json.loads(M.source_bytes((M.DENSE, M.DENSE_JSON)))
        cls.control = M.dense_control(cls.native)

    def test_actual_source_ranges_retain_the_common_core(self):
        control = self.control
        self.assertEqual(control["arithmetic_pairs"], 16)
        self.assertEqual(control["literal_histories"], 64)
        for row in control["all_pair_range_witnesses"]:
            self.assertGreater(
                Fraction(row["P_over_reduced_d"]), Fraction(9, 10) * control["g"]
            )
            self.assertGreater(
                Fraction(row["Q_over_reduced_c"]), Fraction(9, 10) * control["g"]
            )
            self.assertLessEqual(Fraction(row["P_over_full_b"]), 2)
            self.assertLessEqual(Fraction(row["Q_over_full_a"]), 2)

    def test_omitted_factor_is_exactly_g_squared_in_residue_capacity(self):
        for g in (1, 2, 3, 11):
            with self.subTest(g=g):
                row = M.small_capacity_control(g)
                self.assertEqual(Fraction(row["capacity_ratio"]), g * g)
                self.assertEqual(row["correct_frame_capacity"], 140 * g * g)

    def test_corrected_weight_does_not_retain_the_old_inverse_square(self):
        row = M.interval_bounds(3, 5, 7, 5, 7)
        self.assertEqual(row["P_max"], 42)
        self.assertEqual(row["Q_max"], 30)
        self.assertEqual(row["source_weight_after_cancellation"], "1")
        self.assertFalse(row["extra_uniform_g_inverse_square"])

    def test_exact_gauss_factor_and_actual_class_pigeonhole(self):
        self.assertEqual(M.gauss_factor(3, 5), Fraction(5, 8))
        self.assertGreaterEqual(
            Fraction(self.control["gauss_factor_relative_to_principal"]),
            Fraction(9, 16),
        )
        self.assertGreaterEqual(
            4 * self.control["selected_class_pairs"], self.control["arithmetic_pairs"]
        )
        self.assertGreater(
            Fraction(self.control["weighted_nonzero_additive_class_lower"]), 0
        )
        self.assertFalse(self.control["phase_family_enumerated"])

    def test_source_index_change_is_rejected(self):
        candidate = copy.deepcopy(self.native)
        candidate["record"]["entries"][0]["N"] += 1
        with self.assertRaises(ValueError):
            M.dense_control(candidate)

    def test_literal_share_or_quadratic_class_change_is_rejected(self):
        for key, value in (("one_literal_square", "1"), ("class", [1, -1])):
            candidate = copy.deepcopy(self.native)
            candidate["record"]["entries"][0][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                M.dense_control(candidate)

    def test_numeric_aliases_and_unbounded_work_are_rejected(self):
        for bad in (True, 3.0, 0, 1 << 129):
            with self.subTest(value=bad), self.assertRaises(ValueError):
                M.integer(bad)
        for bad in (9, 2000001, True):
            with self.subTest(phase=bad), self.assertRaises(ValueError):
                M.phase_prime(bad)
        with self.assertRaises(ValueError):
            M.residue_counts(10001, 5)
        with self.assertRaises(ValueError):
            M.interval_bounds(5, 5, 7, 5, 7)

    def test_hostile_json_numeric_type_changes_do_not_compare_equal(self):
        self.assertNotEqual(M.canonical({"a": 1}), M.canonical({"a": True}))
        self.assertNotEqual(M.canonical({"a": 1}), M.canonical({"a": 1.0}))
        with self.assertRaises(ValueError):
            M.canonical({"a": float("nan")})

    def test_source_identity_failure_is_not_silently_accepted(self):
        key = (M.DENSE, M.DENSE_JSON)
        with patch.dict(M.SOURCES, {key: "0" * 40}), self.assertRaises(ValueError):
            M.source_bytes(key)

    def test_bound_packet_preserves_the_logical_scope(self):
        result = M.build()
        self.assertFalse(result["abstract_short_interval_lemma_refuted"])
        self.assertFalse(result["full_native_gamma_identification_claimed"])
        self.assertFalse(result["full_native_moment_refuted"])
        self.assertFalse(result["RH_conclusion"])
        self.assertEqual(result["corrected_ranges"], "P<=2gd,Q<=2gc")
        self.assertEqual(len(result["sources"]), 6)
        self.assertEqual(len(result["proof_object_sha256"]), 64)


if __name__ == "__main__":
    unittest.main()
