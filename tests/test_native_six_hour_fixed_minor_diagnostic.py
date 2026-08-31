"""Eight acceptance and mathematical controls for the frozen-tail diagnosis."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/riemann-structures/native-six-hour/native_fixed_minor_diagnostic.py"
)
SPEC = importlib.util.spec_from_file_location("native_fixed_minor_diagnostic", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class FixedMinorDiagnosticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record, cls.provenance, cls.utility = M.source()
        cls.diagnostic = M.validate_record(cls.record)

    def test_actual_frozen_extrema_and_unchanged_outcome(self):
        result = self.diagnostic
        self.assertEqual(result["diagnostic_status"], "PASS")
        self.assertEqual(
            result["source_status_preserved"], "UNKNOWN_TAIL_NOT_CONTRACTIVE"
        )
        self.assertGreater(F(result["exact_extrema"]["minimum_comparison_row_sum"]), 3)
        self.assertLess(
            F(result["exact_extrema"]["maximum_local_remainder"]), F(3, 10**25)
        )
        self.assertEqual(
            result["strict_coarse_bounds"]["inverse_amplified_local_floor_less_than"],
            "1/2500000",
        )
        self.assertFalse(result["scope"]["all_future_rank_certified"])
        self.assertFalse(result["scope"]["inverse_reconstructed"])
        self.assertLessEqual(
            result["maximum_smooth_alias"], result["maximum_alias_cutoff"]
        )
        self.assertTrue(
            any(
                row["maximum_alias"] > row["alias_indices"][-1]
                for row in self.record["result"]["rows"]
            )
        )

    def test_all_authentication_before_decoder_compilation(self):
        with (
            patch.object(
                M, "authenticate", side_effect=M.Refusal("bad frozen artifact")
            ),
            patch("builtins.compile") as compiler,
            patch.object(M, "decode") as decoder,
            self.assertRaises(M.Refusal),
        ):
            M.source()
        compiler.assert_not_called()
        decoder.assert_not_called()

    def test_complete_body_digest_and_numeric_json_counterfeits(self):
        altered = copy.deepcopy(self.record)
        altered["result"]["horizon"] = True
        with self.assertRaises(M.Refusal):
            M.decode(M.canonical(altered).encode(), self.utility)
        altered["result"]["horizon"] = float(2**48)
        with self.assertRaises(M.Refusal):
            M.decode(M.canonical(altered).encode(), self.utility)
        for raw in (b'{"x":1,"x":2}', b'{"x":NaN}', b'{"x":1.0}'):
            with self.subTest(raw=raw), self.assertRaises(M.Refusal):
                M.decode(raw, self.utility)
        with self.assertRaises(M.Refusal):
            M.equal({"x": True}, {"x": 1})

    def test_inverse_bound_and_matrix_shape_reject(self):
        for change in ("bound", "dimension", "noncanonical"):
            altered = copy.deepcopy(self.record)
            inverse = altered["result"]["contraction"]["inverse"]["matrix"]
            if change == "bound":
                inverse[0][0] = str(10**14)
            elif change == "dimension":
                inverse.pop()
            else:
                inverse[0][0] = "0/1"
            with self.subTest(change=change), self.assertRaises(M.Refusal):
                M.validate_record(altered)

    def test_local_cutoff_remainder_and_duplicate_table_reject(self):
        for change in ("cutoff", "remainder", "identity", "duplicate"):
            altered = copy.deepcopy(self.record)
            tables = altered["result"]["local_tables"]
            if change == "cutoff":
                tables[0]["terms"].pop()
            elif change == "remainder":
                tables[0]["remainder"] = str(F(3, 10**25))
                tables[0]["upper"] = str(F(tables[0]["partial"]) + F(3, 10**25))
            elif change == "identity":
                tables[0]["partial"] = "0"
            else:
                tables[1] = copy.deepcopy(tables[0])
            with self.subTest(change=change), self.assertRaises(M.Refusal):
                M.validate_record(altered)

    def test_actual_selection_and_alias_bound_reject(self):
        for change in ("selection", "bool", "large", "unsorted", "nonsmooth", "cutoff"):
            altered = copy.deepcopy(self.record)
            aliases = altered["result"]["rows"][0]["alias_indices"]
            if change == "selection":
                altered["selection"]["coordinate_indices"][0] = True
            elif change == "bool":
                aliases[0] = True
            elif change == "large":
                aliases[-1] = 2**24 + 1
            elif change == "unsorted":
                aliases[1] = aliases[0]
            elif change == "cutoff":
                altered["result"]["rows"][0]["maximum_alias"] += 1
            else:
                aliases[1] = 7
            with self.subTest(change=change), self.assertRaises(M.Refusal):
                M.validate_record(altered)

    def test_row_sum_weighting_obstruction_and_unknown_preservation(self):
        for change in ("small_sum", "inconsistent_sum", "false_pass"):
            altered = copy.deepcopy(self.record)
            item = altered["result"]["contraction"]
            if change == "small_sum":
                item["absolute_inverse_times_tail"][0] = ["3"] + ["0"] * 19
                item["row_sums"][0] = "3"
            elif change == "inconsistent_sum":
                item["row_sums"][0] = "4"
            else:
                item["status"] = "PASS"
                item["all_future_horizons_certified"] = True
            with self.subTest(change=change), self.assertRaises(M.Refusal):
                M.validate_record(altered)

    def test_literal_curvature_scalar_bounds_and_strict_floor_arithmetic(self):
        values = [M.scalar_sum(coordinate) for coordinate in M.COORDINATES]
        self.assertEqual(len(values), 36)
        self.assertEqual(values.count(0), 9)
        self.assertEqual(values.count(2), 27)
        self.assertTrue(all(values[index] == 2 for index in M.INDICES))
        self.assertLess(2 * 3 * F(2) ** 2 * F(3, 10**25), F(1, 10**23))
        self.assertEqual(400 * 10**14 * F(1, 10**23), F(4, 10**7))


if __name__ == "__main__":
    unittest.main()
