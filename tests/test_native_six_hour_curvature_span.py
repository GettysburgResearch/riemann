"""Complete source span, actual physical pivots, and literal path witnesses."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/riemann-structures/native-six-hour/native_curvature_span_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_curvature_span_certificate", PATH)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class CompleteSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module, cls.acquisition, _ = R.source()
        cls.payload = R.build()

    def test_full_source_coverage_and_all_four_ranks(self):
        data = self.acquisition
        self.assertEqual(len(data["complete_ordered_records"]), 63)
        self.assertEqual(len(data["complete_half_source"]), 16)
        for key in (
            "coefficient_rank",
            "rationalized_observation_rank",
            "rectangle_rank",
            "rectangle_observation_rank",
        ):
            self.assertEqual(data[key]["rank"], 6)

    def test_complete_proof_table_and_weighted_pivots(self):
        row = R.proof_table_control(self.module, self.acquisition)
        self.assertEqual(F(row["pivot_determinant"]), F(-3, 32768))
        self.assertTrue(row["all_63_signed_coordinates_checked"])

    def test_corrupting_one_literal_source_coordinate_fails(self):
        data = copy.deepcopy(self.acquisition)
        data["coefficient_columns"][0]["complete_source_vector"][0] = "1"
        with self.assertRaises(ValueError):
            R.proof_table_control(self.module, data)

    def test_prime_power_source_and_physical_common_factor(self):
        self.assertEqual(
            self.module.half_source(4), {(0, 0, 0): F(-1, 2), (1, 0, 0): F(3, 8)}
        )
        row = self.acquisition["common_factor_control"]
        self.assertEqual(F(row["pair_4_6_u2"]), F(3, 16))
        self.assertEqual(F(row["ratio_2_over_3_u2"]), F(3, 32))
        self.assertNotEqual(
            row["ratio_2_over_3_u2"], row["wrong_unweighted_ratio_value"]
        )

    def test_every_source_column_has_exact_product_and_exchange_identities(self):
        records = self.acquisition["complete_ordered_records"]
        for row in self.acquisition["coefficient_columns"]:
            self.module.coefficient_identities(
                list(map(F, row["complete_source_vector"])), records
            )

    def test_six_rectangles_retain_all_literal_edges_and_common_paths(self):
        for rectangle in self.acquisition["rectangles"]:
            self.assertEqual(len(rectangle["original_record_integrals"]), 63)
            for row in rectangle["original_record_integrals"]:
                edges = list(map(F, row["four_monotone_edge_integrals"]))
                surface = F(row["surface_integral"])
                self.assertEqual(edges[0] + edges[1] - edges[2] - edges[3], surface)
                self.assertEqual(
                    F(row["full_j_then_i"]) - F(row["full_i_then_j"]), surface
                )

    def test_rectangle_orientation_is_not_reversible(self):
        first = self.acquisition["rectangles"][0]
        row = next(
            row
            for row in first["original_record_integrals"]
            if (row["n"], row["m"]) == (2, 3)
        )
        self.assertEqual(F(row["surface_integral"]), F(1, 128))
        self.assertNotEqual(
            F(row["full_i_then_j"]) - F(row["full_j_then_i"]),
            F(row["surface_integral"]),
        )

    def test_independent_curvature_to_rectangle_transition(self):
        data = self.acquisition
        self.assertEqual(F(data["rectangle_transition_determinant"]), F(1, 8 * 64**6))
        columns = [
            list(map(F, row["complete_source_vector"]))
            for row in data["coefficient_columns"]
        ]
        for rectangle in data["rectangles"]:
            weights = list(map(F, rectangle["coefficient_transition_column"]))
            reconstructed = [
                sum(
                    (a * column[j] for a, column in zip(weights, columns, strict=True)),
                    F(),
                )
                for j in range(63)
            ]
            self.assertEqual(
                reconstructed, list(map(F, rectangle["complete_source_vector"]))
            )

    def test_erasing_a_basis_direction_reduces_physical_rank(self):
        columns = [
            list(map(F, row["rational_ratio_image"]))
            for row in self.acquisition["coefficient_columns"]
        ]
        self.assertEqual(self.module.rank_columns(columns[:-1])["rank"], 5)

    def test_source_caps_and_coercible_parameters_rejected(self):
        for value in (True, 4.0, 26):
            with self.assertRaises(ValueError):
                self.module.half_source(value)
        with self.assertRaises(ValueError):
            self.module.poly({(3, 0, 0): 1})
        with self.assertRaises(ValueError):
            self.module.rank_columns([[F(1)]] * 13)

    def test_no_single_path_attainment_or_full_gamma_promotion(self):
        scope = self.payload["scope"]
        self.assertFalse(
            scope[
                "each_coefficient_basis_vector_claimed_as_one_monotone_path_difference"
            ]
        )
        self.assertFalse(scope["arbitrary_affine_minimizer_attainment_claimed"])
        self.assertFalse(scope["full_post_renewal_gamma_identified"])

    def test_valid_json_roundtrip_is_accepted(self):
        with patch.object(R, "build", return_value=self.payload):
            R.check(json.loads(json.dumps(self.payload)))

    def test_numeric_aliases_and_nonfinite_values_rejected(self):
        for replacement in (True, 6.0, float("nan"), float("inf")):
            value = copy.deepcopy(self.payload)
            value["scope"]["complete_finite_native_path_variation_span_dimension"] = (
                replacement
            )
            with (
                patch.object(R, "build", return_value=self.payload),
                self.assertRaises(ValueError),
            ):
                R.check(value)

    def test_changed_pivot_cannot_retain_old_digest(self):
        value = copy.deepcopy(self.payload)
        value["independent_proof_table_and_pivots"]["pivot_determinant"] = "1"
        with (
            patch.object(R, "build", return_value=self.payload),
            self.assertRaises(ValueError),
        ):
            R.check(value)

    def test_missing_extra_keys_and_non_json_containers_fail(self):
        for change in ("missing", "extra"):
            value = copy.deepcopy(self.payload)
            if change == "missing":
                del value["scope"]
            else:
                value["unexpected"] = True
            with (
                patch.object(R, "build", return_value=self.payload),
                self.assertRaises(ValueError),
            ):
                R.check(value)
        with self.assertRaises(ValueError):
            R.canonical({"x": (1, 2)})

    def test_all_authentication_precedes_source_compilation(self):
        with (
            patch.object(R, "authenticate", side_effect=ValueError("source changed")),
            patch("builtins.compile") as compiler,
        ):
            with self.assertRaises(ValueError):
                R.source()
            compiler.assert_not_called()


if __name__ == "__main__":
    unittest.main()
