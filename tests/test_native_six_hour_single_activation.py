"""Primitive coverage, KKT, threshold and strict acceptance falsifiers."""

import copy
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/riemann-structures/native-six-hour/single_native_activation.py"
)
SPEC = importlib.util.spec_from_file_location("single_native_activation", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class SingleActivation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = M.build()

    def test_complete_all_arity_coverage(self):
        self.assertEqual(self.payload["full_arity_range"], list(range(2, 17)))
        for row in self.payload["panels"]:
            self.assertEqual(sum(row["full_enumeration_coverage"]), 1 << row["arity"])

    def test_held_out_central_three_is_refuted(self):
        broken = [
            r["arity"]
            for r in self.payload["panels"]
            if not r["pre_run_hypothesis_survived"]
        ]
        self.assertEqual(broken, [11, 13, 15])

    def test_single_coordinate_and_all_strict_slacks(self):
        for row in self.payload["panels"]:
            if row["arity"] in (11, 13, 15):
                r = row["arity"]
                self.assertEqual(
                    row["activation"], ["0"] * (r // 2) + ["1"] + ["0"] * (r // 2)
                )
                self.assertTrue(
                    all(F(s) > 0 for i, s in enumerate(row["slacks_Bq"]) if i != r // 2)
                )

    def test_every_declared_reflection_support(self):
        for row in self.payload["panels"]:
            self.assertEqual(
                row["all_reflection_supports"], (1 << ((row["arity"] + 1) // 2)) - 1
            )

    def test_source_allocation_counts_remain_complete(self):
        for row in self.payload["cofinal_proof_thresholds"]:
            self.assertEqual(
                row["source_allocations"], 2 * row["nonzero_vertex_allocations"]
            )
            self.assertFalse(row["finite_prime_search_performed"])

    def test_general_M_thresholds_are_exact(self):
        for value in (F(1, 100), F(1), F(100)):
            for r, mu in ((11, 90), (13, 1858), (15, 22274)):
                row = M.threshold(r, mu, value)
                self.assertLess(F(row["inactive_gradient_perturbation_upper"]), 2 * mu)

    def test_changed_matrix_breaks_literal_KKT(self):
        matrix, _ = M.complete_matrix(3)
        matrix[0][0] += 1
        with self.assertRaises(ValueError):
            M.kkt(matrix, ["1/4", "1/2", "1/4"], ["0", "0", "0"])

    def test_missing_activation_is_rejected(self):
        matrix, _ = M.complete_matrix(3)
        with self.assertRaises(ValueError):
            M.kkt(matrix, ["1/4", "1/4", "1/4"], ["0", "0", "0"])

    def test_boolean_and_out_of_range_arities_rejected(self):
        for r in (True, 1, 17, 3.0):
            with self.assertRaises(ValueError):
                M.complete_matrix(r)

    def test_incorrect_source_pin_is_rejected(self):
        pins = dict(M.PINS)
        pins["arithmetic_arity_scout.py"] = "0" * 40
        with patch.object(M, "PINS", pins), self.assertRaises(ValueError):
            M.source()

    def test_canonical_bool_alias_rejected(self):
        altered = copy.deepcopy(self.payload)
        altered["panels"][0]["every_matrix_entry_equal"] = 1
        with (
            patch.object(M, "build", return_value=self.payload),
            self.assertRaises(ValueError),
        ):
            M.check(altered)

    def test_canonical_float_alias_rejected(self):
        altered = copy.deepcopy(self.payload)
        altered["full_arity_range"][0] = 2.0
        with (
            patch.object(M, "build", return_value=self.payload),
            self.assertRaises(ValueError),
        ):
            M.check(altered)

    def test_nonfinite_json_rejected(self):
        with self.assertRaises(ValueError):
            M.canonical({"x": float("nan")})

    def test_missing_coverage_rejected(self):
        altered = copy.deepcopy(self.payload)
        altered["panels"].pop()
        with (
            patch.object(M, "build", return_value=self.payload),
            self.assertRaises(ValueError),
        ):
            M.check(altered)

    def test_invalid_threshold_inputs_rejected(self):
        for r, mu, v in (
            (True, 90, 1),
            (11, 0, 1),
            (11, 90, True),
            (11, 90, 0),
            (17, 1, 1),
        ):
            with self.assertRaises(ValueError):
                M.threshold(r, mu, v)


if __name__ == "__main__":
    unittest.main()
