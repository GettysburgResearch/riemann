"""Original finite source metric, all shared paths, and nonlinear quotient boundary."""

import importlib.util
import json
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/riemann-structures/native-six-hour"
    / "global_tangent_metric_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_six_hour_tangent_metric", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeTangentMetricTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scout = M.scout_module()
        cls.source = cls.scout.frozen_module()
        cls.discovery = json.loads(M.frozen_bytes(M.DISCOVERY, M.DISCOVERY_BLOB))
        cls.baseline, cls.tangents, cls.selected, cls.metric = cls.scout.tangent_metric(
            cls.source
        )

    def test_complete_preregistered_global_paths_are_retained(self):
        rows = self.discovery["all_fixed_paths"]
        self.assertEqual(len(rows), 18)
        for row in rows:
            self.assertEqual(len(row["all63_records"]), 63)
            self.assertEqual(
                len({record["ratio"] for record in row["all63_records"]}), 45
            )
            self.assertTrue(
                all(
                    record["n"] * record["m"] == record["K"] <= 25
                    for record in row["all63_records"]
                )
            )

    def test_literal_physical_tangent_witnesses_detect_exactly_two_differences(self):
        rows = M.tangent_witnesses(self.source)
        self.assertEqual(
            [row["integer_incidence_after_multiplying_48_sqrtK"] for row in rows],
            [(1, -1, 0), (1, 0, -1)],
        )
        for ratio in self.baseline:
            total = {}
            for p in self.source.PRIMES:
                total = self.source.ra(total, self.tangents[p][ratio])
            self.assertFalse(total)

    def test_actual_quotient_metric_is_positive_and_selected_direction_descends(self):
        self.assertEqual(self.metric["exact_rank"], 2)
        self.assertGreater(
            F(self.metric["quotient_metric_determinant_interval"]["lower"]), 0
        )
        self.assertLess(
            F(self.metric["selected_first_variation_interval"]["upper"]), -F(584, 100)
        )
        self.assertEqual(sum(self.selected), 0)
        self.assertTrue(all(abs(x) <= 1 for x in self.selected))
        self.assertEqual(self.selected, (F(69, 125), F(56, 125), F(-1)))
        comparison = next(
            row
            for row in self.discovery["comparison_to_frozen_best_axis"]
            if row["epsilon"] == ["69/125", "56/125", "-1"]
        )
        self.assertGreater(
            F(comparison["best_frozen_axis_minus_energy_interval"]["lower"]), F(17, 10)
        )
        M.replay_equal(self.metric, self.discovery["tangent"])

    def test_actual_common_reparameterizations_preserve_the_full_readout(self):
        for value in (F(1, 2), F(-1, 2)):
            _, field, _, _ = self.scout.native_field(self.source, (value, value, value))
            self.assertEqual(field, self.baseline)

    def test_common_affine_shift_survives_physical_coalescence(self):
        first, second = (F(1, 2), F(), F(-1, 2)), (F(3, 4), F(1, 4), F(-1, 4))
        rows1, f1, _, _ = self.scout.native_field(self.source, first)
        rows2, f2, _, _ = self.scout.native_field(self.source, second)
        c1 = F(
            next(
                row["coefficient_before_physical_weight"]
                for row in rows1
                if (row["n"], row["m"]) == (2, 6)
            )
        )
        c2 = F(
            next(
                row["coefficient_before_physical_weight"]
                for row in rows2
                if (row["n"], row["m"]) == (2, 6)
            )
        )
        self.assertEqual(c2 - c1, F(1, 1920))
        defect = self.scout.field_add(self.source, f2, f1, -1)
        self.assertEqual(
            defect[F(1, 3)],
            self.source.rs(self.source.sqrt_rational(F(1, 12)), F(1, 1920)),
        )
        same_ratio = [row for row in rows2 if F(row["ratio"]) == F(1, 3)]
        self.assertEqual([(row["n"], row["m"]) for row in same_ratio], [(1, 3), (2, 6)])
        self.assertEqual(F(same_ratio[0]["coefficient_before_physical_weight"]), 0)

    def test_closed_mixed_square_formula_matches_all_executed_paths(self):
        for path in self.discovery["all_fixed_paths"]:
            values = tuple(map(F, path["epsilon"]))
            for target, index in (((2, 6), 1), ((2, 10), 2)):
                record = next(
                    row
                    for row in path["all63_records"]
                    if (row["n"], row["m"]) == target
                )
                self.assertEqual(
                    F(record["coefficient_before_physical_weight"]),
                    M.literal_mixed_square(values[0], values[index]),
                )

    def test_independent_one_coordinate_source_polynomial_is_recovered(self):
        for p, value in ((2, F(1)), (3, F(-1, 2)), (5, F(-1))):
            old = self.source.native_field(p)[0]
            parameters = tuple(value if q == p else F() for q in self.source.PRIMES)
            new = self.scout.native_field(self.source, parameters)[0]
            for left, right in zip(old, new, strict=True):
                self.assertEqual((left["n"], left["m"]), (right["n"], right["m"]))
                expected = sum(
                    F(x) * value**j
                    for j, x in enumerate(
                        left["epsilon_coefficients_before_physical_weight"]
                    )
                )
                self.assertEqual(
                    expected, F(right["coefficient_before_physical_weight"])
                )

    def test_every_product_endpoint_is_unchanged_for_every_shared_path(self):
        reference = self.discovery["all_fixed_paths"][0]["all_product_endpoints"]
        self.assertTrue(
            all(
                path["all_product_endpoints"] == reference
                for path in self.discovery["all_fixed_paths"]
            )
        )

    def test_fixed_joint_path_improves_the_best_frozen_axis_in_original_energy(self):
        comparison = next(
            row
            for row in self.discovery["comparison_to_frozen_best_axis"]
            if row["epsilon"] == ["1", "0", "-1"]
        )
        self.assertGreater(
            F(comparison["best_frozen_axis_minus_energy_interval"]["lower"]),
            F(274, 100),
        )
        path = next(
            row
            for row in self.discovery["all_fixed_paths"]
            if row["epsilon"] == ["1", "0", "-1"]
        )
        self.assertGreater(
            F(path["baseline_minus_energy_interval"]["lower"]), F(616, 100)
        )

    def test_literal_and_coalesced_diagonal_resolutions_are_distinct(self):
        for path in self.discovery["all_fixed_paths"]:
            ledger = path["four_distinct_diagonals_before_Gamma0"]
            self.assertEqual(
                set(ledger),
                {
                    "primitive_2ds_site",
                    "integrated_site",
                    "integrated_pair",
                    "ratio_coalesced",
                },
            )
            self.assertTrue(all(F(value) >= 0 for value in ledger.values()))
            self.assertFalse(path["diagonals_identified_with_T106140"])
        ledger = self.discovery["all_fixed_paths"][0][
            "four_distinct_diagonals_before_Gamma0"
        ]
        self.assertGreater(len(set(ledger.values())), 1)

    def test_path_variation_is_odd_in_the_original_physical_ratio(self):
        _, field, _, _ = self.scout.native_field(self.source, (F(1), F(), F(-1)))
        difference = self.scout.field_add(self.source, field, self.baseline, -1)
        self.assertTrue(
            all(
                not self.source.ra(value, difference[1 / ratio])
                for ratio, value in difference.items()
            )
        )

    def test_source_parameter_and_polynomial_caps(self):
        for bad in ((True, 0, 0), (0.0, 0, 0), (2, 0, 0), (0, 0)):
            with self.assertRaises(ValueError):
                self.scout.schedule_tuple(bad)
        with self.assertRaises(ValueError):
            self.scout.poly([F(1)] * 10)
        with self.assertRaises(ValueError):
            M.literal_mixed_square(True, 0)

    def test_typed_artifact_and_inherited_executable_authentication(self):
        with self.assertRaises(ValueError):
            M.replay_equal({"rank": 2}, {"rank": 2.0})
        with patch.object(M, "SCOUT_BLOB", "0" * 40), self.assertRaises(ValueError):
            M.scout_module()


if __name__ == "__main__":
    unittest.main()
