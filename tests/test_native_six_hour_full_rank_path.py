"""Independent source and corruption controls for the H450 optimum."""

from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/riemann-structures/native-six-hour/native_full_rank_path_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_full_rank_path_certificate", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FullRankPathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scout = MODULE.frozen("scout", True)
        cls.controls = MODULE.frozen("controls", True)
        cls.helper, cls.poly, cls.kernel, _, _, _ = cls.scout.sources()
        cls.calibration = json.loads(MODULE.frozen("calibration"))
        cls.heldout = json.loads(MODULE.frozen("heldout"))

    def test_complete_heldout_source_and_rank(self):
        result = MODULE.source_control(
            self.scout, self.helper, self.poly, self.controls, self.heldout
        )
        self.assertEqual(
            (result["records"], result["ratios"], result["complete_upper_pair_count"]),
            (614, 265, 35245),
        )
        self.assertEqual(result["physical_direction_rank_mod65521"], 20)

    def test_original_calibration_source(self):
        result = MODULE.source_control(
            self.scout, self.helper, self.poly, self.controls, self.calibration
        )
        self.assertEqual(
            (
                result["records"],
                result["ratios"],
                result["physical_direction_rank_mod65521"],
            ),
            (63, 45, 6),
        )

    def test_every_start_and_strict_cone(self):
        result = MODULE.validate_outcomes(self.controls, self.heldout)
        self.assertEqual(result["all_global_certificate_attempts"], list(range(16)))
        self.assertEqual(result["strict_unique_path_attempts"], list(range(16)))
        self.assertIs(result["first_global_clipping"]["lower_clipped"], True)
        self.assertIs(result["first_global_clipping"]["upper_clipped"], True)

    def test_actual_kernel_stream(self):
        result = MODULE.stream_control(self.scout, self.kernel)
        self.assertEqual(result["complete_upper_pair_count"], 3)
        self.assertIs(result["physical_denominator_retained"], True)

    def test_full_source_prime_powers(self):
        self.assertIn(256, MODULE.smooth_numbers(450))
        self.assertEqual(self.scout.exponents(256), (8, 0, 0))
        with self.assertRaises(ValueError):
            self.scout.exponents(512)
        with self.assertRaises(ValueError):
            self.scout.half_source(self.poly, 7)
        with self.assertRaises(ValueError):
            MODULE.smooth_numbers(450.0)

    def test_half_source_square_coefficients(self):
        coefficients = [self.scout.root_coefficient(j) for j in range(9)]
        self.assertEqual(
            [
                sum(coefficients[j] * coefficients[n - j] for j in range(n + 1))
                for n in range(9)
            ],
            [F(1), F(-1)] + [F()] * 7,
        )

    def test_missing_ordered_record_rejected(self):
        data = copy.deepcopy(self.heldout)
        data["all_ordered_records"].pop()
        with self.assertRaises(ValueError):
            MODULE.source_control(
                self.scout, self.helper, self.poly, self.controls, data
            )

    def test_altered_alias_weight_rejected(self):
        data = copy.deepcopy(self.calibration)
        rows = data["all21_physical_rational_columns"]
        i, j = next(
            (i, j)
            for i, row in enumerate(rows)
            for j, value in enumerate(row)
            if value != "0"
        )
        rows[i][j] = str(F(rows[i][j]) + 1)
        with self.assertRaises(ValueError):
            MODULE.source_control(
                self.scout, self.helper, self.poly, self.controls, data
            )

    def test_false_full_cone_rejected(self):
        data = copy.deepcopy(self.heldout)
        data["all16_declared_start_outcomes"][0]["certificate"][
            "global_all_path_source_optimum_certified"
        ] = False
        with self.assertRaises(ValueError):
            MODULE.validate_outcomes(self.controls, data)

    def test_root_box_corruption_rejected(self):
        data = copy.deepcopy(self.heldout)
        data["all16_declared_start_outcomes"][0]["certificate"]["root_box"][0][
            "upper"
        ] = "100"
        with self.assertRaises(ValueError):
            MODULE.validate_outcomes(self.controls, data)

    def test_witness_selection_cannot_skip_first_root(self):
        data = copy.deepcopy(self.heldout)
        data["first_certified_root_witness_index"] = 1
        with self.assertRaises(ValueError):
            MODULE.validate_outcomes(self.controls, data)

    def test_full_gamma_and_all_height_claims_rejected(self):
        for flag in (
            "full_gamma_identified",
            "all_height_optimizer_persistence_claimed",
            "original_measure_replaced",
        ):
            with self.subTest(flag=flag):
                data = copy.deepcopy(self.heldout)
                data[flag] = True
                with self.assertRaises(ValueError):
                    MODULE.validate_outcomes(self.controls, data)

    def test_rank_exact_denominators_and_dependencies(self):
        self.assertEqual(MODULE.rank_mod65521([[F(1, 2), F(2, 3)], [F(3, 4), F(1)]]), 1)
        self.assertEqual(MODULE.rank_mod65521([[F(1), F()], [F(), F(1)]]), 2)
        with self.assertRaises(ValueError):
            MODULE.rank_mod65521([[F(1, 65521)]])

    def test_typed_counts_and_measure_two(self):
        with self.assertRaises(ValueError):
            MODULE.equal({"count": 614}, {"count": 614.0})
        result = self.controls.monomial_control(self.helper)
        self.assertEqual((result["cases"], result["literal_measure_factor"]), (1728, 2))


if __name__ == "__main__":
    unittest.main()
