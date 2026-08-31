"""Substantive source-map and false-parent controls for the Chow module."""

import importlib.util
import json
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "research/l-families/atlas/generalized/segre-hadamard-source"
SPEC = importlib.util.spec_from_file_location(
    "segre_hadamard_source", HERE / "replay.py"
)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class ExactModuleControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cube = R.koszul_source(3, 3, 2)
        cls.binary = R.koszul_source(2, 3, 2)

    def test_orbit_sum_is_literal_symmetric_source(self):
        self.assertEqual(R.orbit_words((1, 1)), ((0, 1), (1, 0)))
        self.assertEqual(R.orbit_words((2, 0)), ((0, 0),))

    def test_orbit_sum_multiplication_is_not_scalar_fit(self):
        product = R.source_product(((1, 0), (0, 1)), (1, 1))
        self.assertEqual(dict(product), {((2, 0), (0, 2)): 1, ((1, 1), (1, 1)): 1})

    def test_source_products_commute_before_koszul_cancellation(self):
        record = ((0, 0), (0, 0))
        products = []
        for left, right in (((2, 0), (1, 1)), ((1, 1), (2, 0))):
            result = {}
            for mid, a in R.source_product(record, left).items():
                for out, b in R.source_product(mid, right).items():
                    result[out] = result.get(out, 0) + a * b
            products.append(result)
        self.assertEqual(*products)

    def test_exact_chow_chain_dimensions(self):
        self.assertEqual(self.cube["chain_dimensions"], [216, 270, 45])
        self.assertTrue(self.cube["source_d_squared_zero"])

    def test_false_no_degree_two_generator_betti_guess_is_rejected(self):
        quotient = self.cube["homology_factor_class_traces"][0]
        self.assertGreater(quotient["identity"], 0)
        fixed_numerator = (
            quotient["identity"]
            + 3 * quotient["transposition"]
            + 2 * quotient["three_cycle"]
        )
        self.assertEqual(fixed_numerator % 6, 0)
        self.assertGreaterEqual(fixed_numerator // 6, 1)

    def test_actual_binary_quotient_and_higher_tor(self):
        traces = self.binary["homology_factor_class_traces"]
        self.assertEqual(
            traces[0], {"identity": 1, "transposition": -1, "three_cycle": 1}
        )
        self.assertTrue(all(row["identity"] == 0 for row in traces[1:]))

    def test_image_trace_uses_preserved_image_not_ambient_trace(self):
        image = R.ImageSpace([{0: 1, 1: 1}, {0: 2, 1: 2}])
        self.assertEqual(image.rank, 1)
        self.assertEqual(image.trace({0: 1, 1: 0}), 1)

    def test_image_action_refuses_noninvariant_subspace(self):
        image = R.ImageSpace([{0: 1}])
        with self.assertRaisesRegex(ValueError, "preserve"):
            image.trace({0: 1})

    def test_rational_rank_is_not_modular_rank(self):
        image = R.ImageSpace([{0: 2}, {0: 1, 1: 2}])
        self.assertEqual(image.rank, 2)  # Reduction mod 2 would give rank one.
        self.assertEqual(image.coordinate({0: 1, 1: 1}, 1), 1)

    def test_factor_permutation_is_actual_record_action(self):
        record = ((1, 0), (0, 1), (1, 0))
        cycle = (1, 2, 0)
        moved = record
        for _ in range(3):
            moved = R.permute_record(moved, cycle)
        self.assertEqual(moved, record)

    def test_source_growth_cap_precedes_allocation(self):
        with self.assertRaisesRegex(ValueError, "total basis cap"):
            R.koszul_source(3, 4, 3)


class CharacterAndFunctorControls(unittest.TestCase):
    def test_binary_cube_source_character(self):
        # a=5,b=6: 1+2abT+b^3T^2.
        self.assertEqual(R.numerator((2, 3), 3)[:3], [1, 60, 216])
        self.assertEqual(R.descent_numerator(2, 3, 3), [1, 60, 216])

    def test_binary_descent_major_index_is_effective(self):
        result = R.descent_numerator(1, 1, 5)
        self.assertEqual(result, [1, 26, 66, 26, 1])
        self.assertEqual(sum(result), 120)

    def test_rank_three_cube_is_comparison_and_signed(self):
        result = R.character_control((2, 3, 5), 3)
        self.assertEqual(result["s_D_c_degree"], [10, 7, 3, 7])
        self.assertEqual(result["universal_numerator"][-1], -(30**7))
        self.assertEqual(result["comparison_or_heldout"], "comparison")

    def test_new_ternary_fourth_power_character_heldout(self):
        result = R.character_control((2, 3, 5), 4, heldout=True)
        self.assertEqual(result["s_D_c_degree"], [15, 9, 6, 12])
        self.assertEqual(result["universal_numerator"][-1], 30**16)
        self.assertTrue(result["distinct_symmetric_weights"])

    def test_collision_cancels_recurrence_not_source_module(self):
        result = R.collision_and_functor_controls()
        self.assertEqual(result["universal_vs_reduced_denominator_degrees"], [10, 7])
        self.assertEqual(result["identity_cube_universal_N"][2], -9)
        self.assertEqual(result["identity_cube_reduced_numerator"], [1, 20, 48, 20, 1])

    def test_ramification_cannot_project_generators_first(self):
        result = R.collision_and_functor_controls()
        self.assertEqual(result["ramified_invariant_dimensions"][2], 5)
        self.assertEqual(result["premature_fixed_generator_dimensions"][2], 3)

    def test_independent_factor_deformation_breaks_symmetric_base(self):
        result = R.collision_and_functor_controls()
        self.assertNotEqual(*result["mixed_symmetry_coefficients"])
        self.assertEqual(*result["proportional_mixed_symmetry_coefficients"])

    def test_exact_rational_specializations(self):
        direct = R.numerator((Fraction(1, 2), Fraction(1, 3)), 3)
        self.assertEqual(direct[:3], [1, Fraction(5, 18), Fraction(1, 216)])

    def test_trivial_source_degree_zero_is_supported(self):
        self.assertEqual(R.character_control((2,), 3)["universal_numerator"], [1])
        self.assertEqual(R.character_control((2, 3, 5), 1)["universal_numerator"], [1])

    def test_actual_unipotent_substitution_has_same_trace_not_same_matrix(self):
        matrix = R.binary_unipotent(3)
        self.assertEqual(sum(matrix[i][i] for i in range(4)), 4)
        self.assertGreater(sum(abs(v) for row in matrix for v in row), 4)

    def test_invalid_inputs_fail_under_optimized_python(self):
        for values, m in (
            ((0, 1), 2),
            ((1.0, 2), 2),
            ((1, 2), True),
            ((1, 2, 3, 4), 8),
        ):
            with self.assertRaises(ValueError):
                R.numerator(values, m)
        with self.assertRaises(ValueError):
            R.compositions(True, 2)

    def test_captured_git_blobs_are_authenticated(self):
        contract = R.authenticate_sources()
        self.assertEqual(len(contract["captured_sources"]), 3)

    def test_modified_snapshot_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            sources = [
                {"commit": commit, "path": path, "snapshot": snapshot, "git_blob": blob}
                for commit, path, snapshot, blob in R.PINS
            ]
            for source in sources:
                target = base / source["snapshot"]
                target.parent.mkdir(exist_ok=True)
                target.write_text("changed", encoding="utf-8")
            (base / "sources.json").write_text(
                json.dumps({"captured_sources": sources}), encoding="utf-8"
            )
            with (
                patch.object(R, "HERE", base),
                self.assertRaisesRegex(ValueError, "blob mismatch"),
            ):
                R.authenticate_sources()

    def test_missing_source_is_not_silently_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            (base / "sources.json").write_text(
                '{"captured_sources": []}', encoding="utf-8"
            )
            with (
                patch.object(R, "HERE", base),
                self.assertRaisesRegex(ValueError, "coverage"),
            ):
                R.authenticate_sources()


if __name__ == "__main__":
    unittest.main()
