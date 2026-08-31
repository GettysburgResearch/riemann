"""Complete native occupation-law controls and rejected source counterfeits."""

import copy
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/riemann-structures/native-six-hour/native_occupation_moments.py"
SPEC = importlib.util.spec_from_file_location("native_occupation_under_test", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class OccupationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = M.build()
        cls.module, cls.data, _ = M.authenticate()
        cls.paths = cls.result["fixed_paths"]
        cls.byname = {row["name"]: row for row in cls.paths}

    def test_complete_source_domain(self):
        self.assertEqual(len(self.result["complete_ordered_records"]), 63)
        self.assertEqual(
            {(r["n"], r["m"]) for r in self.result["complete_ordered_records"]},
            {(r["m"], r["n"]) for r in self.result["complete_ordered_records"]},
        )

    def test_all_thirty_words_unique(self):
        self.assertEqual(len({tuple(row["word"]) for row in self.result["words"]}), 30)

    def test_all_twenty_declared_paths_retained(self):
        self.assertEqual(len(self.paths), 20)
        self.assertEqual(len(self.byname), 20)

    def test_complete_nonnegative_probability_laws(self):
        for row in self.paths:
            law = list(map(F, row["all_word_probabilities"]))
            self.assertEqual(len(law), 30)
            self.assertTrue(all(p >= 0 for p in law))
            self.assertEqual(sum(law, F()), 1)

    def test_diagonal_iid_word_law(self):
        self.assertEqual(
            list(map(F, self.byname["diagonal"]["all_word_probabilities"])),
            [F(1, 30)] * 30,
        )

    def test_six_axis_laws_are_deterministic(self):
        axes = [row for row in self.paths if row["name"].startswith("axis_")]
        self.assertEqual(len(axes), 6)
        for row in axes:
            self.assertEqual(
                sorted(map(F, row["all_word_probabilities"])), [F()] * 29 + [F(1)]
            )

    def test_all_independent_word_expectations(self):
        for row in self.paths:
            self.assertEqual(row["moments"], row["word_expectations"])

    def test_all_complete_source_and_ratio_vectors(self):
        for row in self.paths:
            self.assertEqual(len(row["complete_source"]), 63)
            self.assertEqual(
                len(row["physical_rational_ratio_image"]),
                len(self.result["ratio_order"]),
            )

    def test_reference_zero_moments(self):
        self.assertEqual(self.byname["axis_235"]["moments"], ["0"] * 6)

    def test_eleven_curved_constructive_samples(self):
        curves = [row for row in self.paths if row["name"].startswith("curve_")]
        self.assertEqual(len(curves), 11)
        for row in curves:
            a, b, c, d, e, f = map(F, row["moments"])
            self.assertEqual(b, a - a**3 / (2 * c) if a else 0)
            self.assertEqual((d, e, f), (0, 0, 0))

    def test_curved_lower_boundary_sharp(self):
        for a in (F(1, 4), F(1, 2), F(3, 4)):
            moments = M.path_moments(self.module, M.curve_path(a, a * a))
            self.assertEqual(moments, (a, a / 2, a * a, F(), F(), F()))

    def test_order_counterfeit_jensen_failure(self):
        bad = self.result["counterfeit"]
        self.assertEqual(bad["word"], [3, 2, 2, 3, 5])
        self.assertEqual(F(bad["Jensen_slack"]), F(-1, 4))
        self.assertIs(bad["native_path_claimed"], False)

    def test_counterfeit_is_physically_distinct_from_curved_source(self):
        records = self.data["complete_ordered_records"]
        ratios = [(row["a"], row["b"]) for row in self.data["ratio_order"]]
        fake = list(map(F, self.result["counterfeit"]["formal_affine_source"]))
        true = list(map(F, self.byname["curve_1/2_1/4"]["complete_source"]))
        observed = self.module.ratio_image(
            [a - b for a, b in zip(fake, true, strict=True)], records, ratios
        )
        self.assertTrue(any(observed))
        self.assertNotEqual(observed[ratios.index((1, 2))], 0)

    def test_factorial_omission_fails_probability_normalization(self):
        self.assertEqual(F(self.result["missing_factorial_total_probability"]), F(1, 4))

    def test_nonmonotone_segment_rejected(self):
        with self.assertRaises(ValueError):
            M.valid_path(
                self.module,
                (M.ORIGIN, (F(3, 4), F(1, 2), F()), (F(1, 2), F(3, 4), F()), M.END),
            )

    def test_incomplete_path_rejected(self):
        with self.assertRaises(ValueError):
            M.valid_path(self.module, (M.ORIGIN, (F(1), F(1), F())))

    def test_false_curved_projection_rejected(self):
        with self.assertRaises(ValueError):
            M.curve_path(F(1, 2), F(1, 8))

    def test_missing_C_half_factor_changes_original_source(self):
        columns = [
            list(map(F, col["complete_source_vector"]))
            for col in self.data["coefficient_columns"]
        ]
        reference = list(map(F, self.byname["axis_235"]["complete_source"]))
        true = list(map(F, self.byname["diagonal"]["complete_source"]))
        moments = list(map(F, self.byname["diagonal"]["moments"]))
        moments[2] *= 2
        wrong = M.affine_source(self.module, reference, columns, moments)
        index = next(
            i
            for i, row in enumerate(self.data["complete_ordered_records"])
            if (row["n"], row["m"]) == (3, 6)
        )
        self.assertEqual(wrong[index] - true[index], F(1, 24))

    def test_corrected_common_factor_weight_is_essential(self):
        records = self.data["complete_ordered_records"]
        ratios = [(row["a"], row["b"]) for row in self.data["ratio_order"]]
        column = list(
            map(F, self.data["coefficient_columns"][1]["complete_source_vector"])
        )
        self.assertNotEqual(
            self.module.ratio_image(column, records, ratios),
            self.module.ratio_image(column, records, ratios, physical=False),
        )

    def test_whole_artifact_mutation_rejected(self):
        candidate = copy.deepcopy(self.result)
        candidate["fixed_paths"][0]["complete_source"][0] = "1"
        with self.assertRaises(ValueError):
            M.strict_equal(candidate, self.result)

    def test_typed_bool_and_float_aliases_rejected(self):
        for wrong in (True, 1.0):
            with self.assertRaises(ValueError):
                M.strict_equal({"value": wrong}, {"value": 1})

    def test_json_duplicate_float_nonfinite_rejected(self):
        for text in ('{"a":1,"a":1}', '{"a":1.0}', '{"a":NaN}'):
            with self.assertRaises(ValueError):
                M.strict_load(text)

    def test_owned_proof_and_test_bindings(self):
        self.assertEqual(len(self.result["owned_sha256_lf"]), 5)
        self.assertIn(
            "research/riemann-structures/native-six-hour/NATIVE_OCCUPATION_MOMENTS.md",
            self.result["owned_sha256_lf"],
        )

    def test_scope_preserves_unresolved_native_body_and_decoder(self):
        scope = self.result["scope"]
        self.assertIs(scope["all_native_moment_body_claimed_as_word_polytope"], False)
        self.assertIs(scope["six_dimensional_body_fully_characterized"], False)
        self.assertIs(scope["full_post_renewal_gamma_decoder_identified"], False)


if __name__ == "__main__":
    unittest.main()
