"""Complete native source fibers, physical enrichment and strict acceptance."""

import copy
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/riemann-structures/native-six-hour/synchronization_fiber_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_sync_fiber_certificate", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeSynchronizationFiberTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = M.build()
        cls.replay = cls.payload["complete_frozen_source_replay"]
        cls.source, _, _ = M.load_source()

    def test_all_four_sources_authenticated_before_compilation(self):
        self.assertEqual(len(self.payload["sources"]), 4)
        with (
            patch.object(M, "authenticate", side_effect=ValueError("bad source")),
            patch("builtins.compile") as compiler,
        ):
            with self.assertRaisesRegex(ValueError, "bad source"):
                M.load_source()
            compiler.assert_not_called()

    def test_complete_two_horizon_censuses_not_only_selected_ratios(self):
        for horizon, expected in ((60, 140), (300, 474)):
            rows = self.replay[f"horizon{horizon}_complete_records"]
            self.assertEqual(rows, M.census(horizon))
            self.assertEqual(len(rows), expected)
            self.assertTrue(all(row["n"] * row["m"] <= horizon for row in rows))

    def test_marked_moment_kernel_has_positive_full_Gram_and_missing_moment(self):
        data = self.payload["independent_moment_controls"]
        values = list(map(F, data["independent_P_moments"]))
        self.assertTrue(all(values[j] == 0 for j in (0, 1, 3, 4)))
        self.assertNotEqual(values[2], 0)
        self.assertTrue(
            all(F(value) > 0 for value in data["full_Gram_leading_principal_minors"])
        )

    def test_changed_polynomial_coefficient_is_not_a_moment_certificate(self):
        bad = copy.deepcopy(self.replay)
        entry = bad["exact_path_construction"]["P_coefficients"][0]
        entry[1] = str(F(entry[1]) + 1)
        with self.assertRaisesRegex(ValueError, "source P"):
            M.moment_controls(bad)

    def test_actual_monotone_schedules_and_four_common_moments(self):
        data = self.payload["independent_moment_controls"]
        self.assertGreater(F(data["derivative_bound_coefficient"]), 2)
        for name in ("w_plus", "w_minus"):
            value = M.polynomial(self.replay[name])
            self.assertEqual(value.get(0, F()), 0)
            self.assertEqual(sum(value.values()), 1)
        self.assertEqual(
            self.replay["four_sufficient_original_moments"]["plus"],
            self.replay["four_sufficient_original_moments"]["minus"],
        )

    def test_initial_v_activation_is_required_even_when_differences_cancel(self):
        rows = self.replay["horizon60_complete_records"]
        index = next(i for i, row in enumerate(rows) if (row["n"], row["m"]) == (3, 1))
        complete = F(
            self.replay["horizon60_original_and_synchronized_sources"]["plus"][index]
        )
        schedules = ({1: F(1)}, {0: F(1)}, M.polynomial(self.replay["w_plus"]))
        omitted = self.source.pair_integral(
            self.source.path_source(3, schedules), self.source.path_source(1, schedules)
        )
        self.assertEqual(complete, -1)
        self.assertEqual(omitted, 0)

    def test_all_original_pair_coefficients_and_observed_fields_agree(self):
        values = self.replay["horizon60_original_and_synchronized_sources"]
        self.assertEqual(values["plus"], values["minus"])
        rows = self.replay["horizon60_complete_records"]
        difference = [
            F(a) - F(b) for a, b in zip(values["plus"], values["minus"], strict=True)
        ]
        self.assertFalse(any(M.coalesce(difference, rows).values()))

    def test_original_physical_common_factor_weight_changes_the_answer(self):
        data = self.payload["independent_physical_obstruction"]
        self.assertEqual(data["ratio3_over5_pairs"], [[3, 5], [6, 10]])
        self.assertEqual(F(data["correct_rational_amplitude"]), F(1, 16243587360))
        self.assertNotEqual(
            F(data["wrong_unweighted_amplitude"]), F(data["correct_rational_amplitude"])
        )
        self.assertEqual(
            F(data["physical_squared_amplitude"]), F(1, 15 * 16243587360**2)
        )

    def test_measured_literal_and_physical_ranks_both_three_to_seven(self):
        for expected, panel in zip(
            (3, 7), self.payload["independent_enrichment_controls"], strict=True
        ):
            self.assertEqual(panel["literal_rank"]["rank"], expected)
            self.assertEqual(panel["physical_rank"]["rank"], expected)
            self.assertEqual(panel["complete_record_count"], 474)

    def test_exact_rank_algorithm_retains_dependent_columns(self):
        self.assertEqual(M.rank([[1, 0, 1], [2, 0, 2], [0, 1, 1]])["rank"], 2)
        self.assertEqual(M.determinant([[0, 1], [2, 0]]), -2)
        self.assertEqual(M.determinant([[1, 1], [1, 1]]), 0)

    def test_missing_top_curvature_is_not_counted_as_a_direction(self):
        before, after = self.replay["curvature_enrichment"]
        self.assertNotIn([1, 1], before["curvature_monomials"])
        self.assertNotIn([3, 1], after["curvature_monomials"])
        self.assertEqual(len(after["curvature_monomials"]), 7)

    def test_all_seven_rectangles_have_complete_source_area_witnesses(self):
        panel = self.replay["curvature_enrichment"][1]
        self.assertEqual(len(panel["actual_rectangle_witnesses"]), 7)
        self.assertTrue(
            all(
                len(row["source_difference"]) == 474
                for row in panel["actual_rectangle_witnesses"]
            )
        )
        bad = copy.deepcopy(self.replay)
        vector = bad["curvature_enrichment"][1]["actual_rectangle_witnesses"][0][
            "source_difference"
        ]
        vector[0] = str(F(vector[0]) + 1)
        with self.assertRaisesRegex(ValueError, "every actual witness record"):
            M.enrichment_controls(bad)

    def test_wrong_frozen_object_is_rejected_before_executable_source(self):
        pins = dict(M.PINS)
        pins[next(iter(pins))] = "0" * 40
        with patch.object(M, "PINS", pins), patch("builtins.compile") as compiler:
            with self.assertRaisesRegex(ValueError, "authentication"):
                M.load_source()
            compiler.assert_not_called()

    def test_duplicate_float_and_nonfinite_json_are_rejected(self):
        for raw in (
            b'{"x":1,"x":2}',
            b'{"x":1.0}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b'{"x":1e999}',
        ):
            with self.assertRaises(ValueError):
                M.read_json(raw)

    def test_numeric_alias_and_bounded_exact_domains(self):
        for value in (True, 1.0):
            with self.assertRaises(ValueError):
                M.replay_equal({"rank": value}, {"rank": 1})
            with self.assertRaises(ValueError):
                M.exact(value)
        with self.assertRaises(ValueError):
            M.exact(1 << 4097)
        with self.assertRaises(ValueError):
            M.polynomial([[True, "1"]])

    def test_full_proof_object_and_scope_are_bound(self):
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
        scope = self.payload["scope"]
        self.assertTrue(
            scope["allheight_original_equality_from_proof_not_finite_extrapolation"]
        )
        self.assertFalse(scope["H25_source_retraction_refuted"])
        self.assertFalse(scope["full_retained_gamma_decoder_identified"])
        self.assertEqual(len(self.payload["owned_sha256_lf"]), 3)


if __name__ == "__main__":
    unittest.main()
