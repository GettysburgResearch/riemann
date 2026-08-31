"""Complete native affine floor, source moments and fixed halfspace certificate."""

import copy
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/riemann-structures/native-six-hour/native_affine_floor_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_affine_floor_certificate", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeAffineFloorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = M.build()
        cls.replay = cls.payload["complete_primitive_replay"]
        cls.source = cls.payload["independent_literal_source_feasibility"]

    def test_all_four_inputs_authenticated_before_compilation(self):
        self.assertEqual(len(self.payload["sources"]), 4)
        with (
            patch.object(M, "authenticate", side_effect=ValueError("bad source")),
            patch("builtins.compile") as compiler,
        ):
            with self.assertRaisesRegex(ValueError, "bad source"):
                M.load_source()
            compiler.assert_not_called()

    def test_all63_physical_records_and_six_directions_retained(self):
        records = self.replay["complete_ordered_records"]
        self.assertEqual(len(records), 63)
        self.assertEqual(len({F(row["n"], row["m"]) for row in records}), 45)
        self.assertTrue(
            all(row["product"] == row["n"] * row["m"] <= 25 for row in records)
        )
        self.assertEqual(len(self.replay["basis_order"]), 6)
        self.assertTrue(
            all(
                len(row["complete_source_vector"]) == 63
                for row in self.replay["basis_order"]
            )
        )

    def test_original_metric_positive_pivots_and_exact_symmetry(self):
        pivots = self.replay["positive_elimination_pivots"]
        self.assertEqual(len(pivots), 6)
        self.assertTrue(all(M.interval(row)[0] > 0 for row in pivots))
        matrix = self.replay["exact_Gram"]
        self.assertTrue(
            all(matrix[i][j] == matrix[j][i] for i in range(6) for j in range(6))
        )
        self.assertTrue(self.replay["all_six_even_odd_cross_terms_exactly_zero"])

    def test_affine_floor_is_certified_but_not_source_attainable(self):
        lower, upper = M.interval(self.replay["affine_energy_floor"])
        self.assertLess(F(10220, 100), lower)
        self.assertLess(upper, F(10222, 100))
        moments = [M.interval(row) for row in self.replay["affine_occupation_moments"]]
        self.assertLess(moments[2][1], -19)
        self.assertGreater(moments[1][0], 3)
        self.assertGreater(moments[4][0], 7)

    def test_fixed_halfspace_gap_and_actual_quadratic_bracket(self):
        scope = self.payload["certified_numerical_scope"]
        self.assertGreater(
            F(scope["certified_best_single_halfspace"]["certified_lower"]),
            F(13877, 100),
        )
        self.assertEqual(
            scope["certified_best_single_halfspace"]["name"], "Gram_square_-1/2_1"
        )
        self.assertLess(
            M.interval(scope["actual_quadratic_energy_interval"])[1], F(16056, 100)
        )
        self.assertFalse(scope["infimum_attainment_or_optimizer_claimed"])

    def test_all65_preregistered_halfspaces_and_statuses_retained(self):
        rows = self.replay["halfspaces"]
        self.assertEqual(len(rows), 65)
        self.assertEqual(len({row["name"] for row in rows}), 65)
        self.assertTrue(
            all(
                row["status"]
                in {"strictly_violated", "affine_point_satisfies", "uncertified_sign"}
                for row in rows
            )
        )
        self.assertTrue(
            all(M.interval(row["dual_squared_norm"])[0] > 0 for row in rows)
        )
        selected = next(row for row in rows if row["name"] == "Gram_square_-1/2_1")
        self.assertEqual(selected["L"], ["-1", "2", "-2", "0", "0", "0"])
        self.assertEqual(F(selected["b"]), F(1, 12))

    def test_actual_diagonal_and_quadratic_moments_independently(self):
        rows = {row["name"]: row for row in self.source["actual_paths"]}
        diagonal = list(map(F, rows["diagonal"]["occupation_moments_A_B_C_D_E_F"]))
        quadratic = list(
            map(F, rows["quadratic_1_0_minus1"]["occupation_moments_A_B_C_D_E_F"])
        )
        self.assertEqual(
            diagonal, [F(1, 2), F(1, 3), F(1, 3), F(1, 2), F(1, 3), F(1, 2)]
        )
        self.assertEqual(
            quadratic, [F(1, 3), F(7, 30), F(1, 6), F(1, 6), F(2, 15), F(1, 3)]
        )
        self.assertEqual(rows["axis_235"]["coordinates_A_B_C_half_D_E_F"], ["0"] * 6)

    def test_actual_all_path_controls_reconstruct_every_record(self):
        self.assertEqual(len(self.source["actual_paths"]), 8)
        self.assertTrue(
            all(
                row["all63_source_records_reconstructed"]
                for row in self.source["actual_paths"]
            )
        )
        for row in self.source["actual_paths"]:
            self.assertEqual(len(row["all65_halfspace_slacks"]), 65)
            self.assertTrue(
                all(
                    F(item["exact_slack"]) >= 0
                    for item in row["all65_halfspace_slacks"]
                )
            )
        self.assertFalse(self.source["coordinate_reconstruction_used_as_metric"])

    def test_mixed_moment_C_half_convention_is_required(self):
        row = next(
            row for row in self.source["actual_paths"] if row["name"] == "diagonal"
        )
        coordinates = list(map(F, row["coordinates_A_B_C_half_D_E_F"]))
        moments = list(map(F, row["occupation_moments_A_B_C_D_E_F"]))
        self.assertEqual(2 * coordinates[2], moments[2])
        self.assertNotEqual(coordinates[2], moments[2])
        columns = [row["complete_source_vector"] for row in self.replay["basis_order"]]
        reference = list(map(F, self.replay["actual_paths"][0]["complete_source"]))
        actual = next(
            row for row in self.replay["actual_paths"] if row["name"] == "diagonal"
        )
        counterfeit = [
            reference[i] + sum(moments[j] * F(columns[j][i]) for j in range(6))
            for i in range(63)
        ]
        self.assertNotEqual(counterfeit, list(map(F, actual["complete_source"])))

    def test_fixed_ratio16_gives_positive_distance_obstruction(self):
        fixed = self.source["fixed_ratio16"]
        self.assertEqual(fixed["ordered_pair"], [16, 1])
        self.assertEqual(F(fixed["unweighted_coefficient"]), F(11, 64))
        self.assertEqual(F(fixed["physical_amplitude"]), F(11, 256))
        self.assertTrue(fixed["all_six_variations_zero"])

    def test_source_coordinate_solution_checks_unselected_rows(self):
        columns = [row["complete_source_vector"] for row in self.replay["basis_order"]]
        reference = self.replay["actual_paths"][0]["complete_source"]
        value = list(self.replay["actual_paths"][-1]["complete_source"])
        pivots = self.source["source_pivot_indices"]
        index = next(i for i in range(63) if i not in pivots)
        value[index] = str(F(value[index]) + 1)
        with self.assertRaisesRegex(ValueError, "every source record"):
            M.source_coordinates(columns, reference, value, pivots)

    def test_exact_solver_handles_permuted_pivots_and_singularity(self):
        matrix = [[int(j == 5 - i) for j in range(6)] for i in range(6)]
        self.assertEqual(
            M.solve_exact(matrix, [1, 2, 3, 4, 5, 6]), list(map(F, [6, 5, 4, 3, 2, 1]))
        )
        with self.assertRaisesRegex(ValueError, "rank six"):
            M.solve_exact([[0] * 6 for _ in range(6)], [0] * 6)

    def test_numeric_claims_fail_if_only_display_midpoint_agrees(self):
        bad = copy.deepcopy(self.replay)
        bad["affine_energy_floor"]["upper"] = "103"
        with self.assertRaisesRegex(ValueError, "102.20"):
            M.certify_bounds(bad)
        bad = copy.deepcopy(self.replay)
        bad["affine_occupation_moments"][2]["upper"] = "0"
        with self.assertRaisesRegex(ValueError, "impossible"):
            M.certify_bounds(bad)

    def test_literal_types_and_exact_rational_limits(self):
        for bad in (True, 1.0, None):
            with self.assertRaises(ValueError):
                M.rational(bad)
        with self.assertRaises(ValueError):
            M.rational(1 << 4097)
        with self.assertRaises(ValueError):
            M.solve_exact([[1]], [1])

    def test_canonical_payload_scope_and_numeric_aliases(self):
        for replacement in (True, 1.0):
            with self.assertRaises(ValueError):
                M.replay_equal({"rank": replacement}, {"rank": 1})
        for raw in (b'{"a":1,"a":2}', b'{"a":NaN}', b'{"a":Infinity}', b'{"a":1e999}'):
            with self.assertRaises(ValueError):
                M.read_json(raw)
        self.assertFalse(self.payload["scope"]["finite_panel_proves_all_path_optimum"])
        self.assertFalse(self.payload["scope"]["complete_retained_gamma_identified"])

    def test_complete_proof_object_and_source_readback(self):
        body = {
            key: value
            for key, value in self.payload.items()
            if key != "proof_object_sha256"
        }
        self.assertEqual(
            M.sha256(M.canonical(body).encode()).hexdigest(),
            self.payload["proof_object_sha256"],
        )
        M.replay_equal(M.read_json(M.canonical(self.payload).encode()), self.payload)
        self.assertEqual(
            self.payload["sources"][0]["commit"],
            "46c8453e3976d242479202bf4d58489282a64d2a",
        )


if __name__ == "__main__":
    unittest.main()
