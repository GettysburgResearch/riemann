"""Exact hostile tests, not numerical evidence for the analytic limits."""

import ast
import copy
import importlib.util
import tempfile
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/exploratory/xi_high_derivative_saddle_closure.py"
SPEC = importlib.util.spec_from_file_location("xi_high_derivative_packet", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class XiHighDerivativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def test_raw_rational_types_and_input_caps(self):
        for value in (True, 1.0, 1j, "1", None):
            with self.subTest(value=value), self.assertRaises(TypeError):
                M.rational(value)
        with self.assertRaises(ValueError):
            M.rational(2**M.INPUT_BITS)
        with self.assertRaises(ValueError):
            M.rational(F(1, 2**M.INPUT_BITS))
        self.assertEqual(M.rational(F(3, 7)), F(3, 7))

    def test_intermediate_guard(self):
        for bad in (True, 1.0, "2"):
            with self.subTest(bad=bad), self.assertRaises(TypeError):
                M.checked(bad)
        with self.assertRaises(ValueError):
            M.checked(F(2**M.INTERMEDIATE_BITS))

    def test_coordinate_domain(self):
        for args in ((1, 64), (2, 63), (True, 64), (2, 64.0), (2, -1)):
            with self.subTest(args=args), self.assertRaises((ValueError, TypeError)):
                M.coordinates(*args)
        self.assertEqual(M.coordinates(2, 64), (F(2), F(64)))

    def test_order_guard_precedes_factorial_work(self):
        for order in (True, 1, 13, 10**9, 2.0, F(2)):
            with (
                self.subTest(order=order),
                patch.object(
                    M.math, "factorial", side_effect=AssertionError("allocated")
                ),
                self.assertRaises(ValueError),
            ):
                M.direct_logratio(2, 64, order)

    def test_raw_series_trailing_contamination_rejected(self):
        for values in ((1, False), (1, 0.0), (), (1,) * 14, iter((1, 2))):
            with (
                self.subTest(values=values),
                self.assertRaises((TypeError, ValueError)),
            ):
                M.series(values)
        self.assertEqual(M.series((0, F(1, 3), 0)), (F(0), F(1, 3), F(0)))

    def test_hand_taylor_coefficients(self):
        row = M.saddle_control(2, 64, 4)
        self.assertEqual(
            row["logratio_coefficients"],
            (F(0), F(0), F(-169, 2), F(-121, 3), F(-149, 6)),
        )
        self.assertEqual(row["precision"], 169)
        self.assertEqual(row["sigma_squared"], F(1, 169))

    def test_all_predeclared_independent_series(self):
        for args in M.CASES:
            with self.subTest(args=args):
                self.assertEqual(
                    M.direct_logratio(*args), M.integrated_logderivative(*args)
                )

    def test_heldout_nonintegral_and_max_order(self):
        for a, s in ((F(9, 4), F(513, 2)), (F(101, 7), F(8193, 8))):
            row = M.saddle_control(a, s, 12)
            self.assertEqual(
                row["logratio_coefficients"], row["independent_coefficients"]
            )
            self.assertTrue(
                row["coordinates_are_not_claimed_actual_transcendental_saddles"]
            )

    def test_precision_and_dominated_limit_boundaries(self):
        row = M.saddle_control(2, 64, 2)
        self.assertEqual(row["S_sigma_squared"], F(64, 169))
        self.assertEqual(row["square_of_S_times_sigma_lower_bound"], F(4096, 169))
        for a, s, order in M.CASES:
            row = M.saddle_control(a, s, order)
            self.assertLessEqual(F(64, 169), row["S_sigma_squared"])
            self.assertLess(row["S_sigma_squared"], F(1, 2))

    def test_series_tamper_fails_explicitly(self):
        with (
            patch.object(M, "integrated_logderivative", return_value=(F(0),) * 5),
            self.assertRaises(ArithmeticError),
        ):
            M.saddle_control(2, 64, 4)

    def test_curvature_exact_rational_reserve(self):
        row = M.curvature_control()
        self.assertEqual(row["combined_coefficient"], F(12323, 3600))
        self.assertLess(row["combined_coefficient"], 4)
        self.assertEqual(row["global_loss_coefficient"], F(1, 16))

    def test_moment_majorants_independent_integers(self):
        row = M.moment_majorants()
        self.assertEqual(row["M1"], 25758000)
        self.assertEqual(row["M2"], 168980256)
        self.assertEqual(row["S_min_for_B_one"], 1024)
        self.assertFalse(
            row["limits_or_transcendental_integrals_numerically_evaluated"]
        )

    def test_worst_case_laguerre_reserve(self):
        e = F(1, 32)
        loss = e * (2 + e) + e * (1 + e) + e
        self.assertEqual(1 - loss, F(447, 512))
        self.assertGreater(1 - loss, F(1, 2))

    def test_accepted_budget_and_dependent_beta(self):
        m1 = M.moment_majorants()["M1"]
        alpha = F(1, 1024 * m1)
        for j in range(1, 9):
            row = M.perturbation_budget(j * alpha, alpha)
            self.assertTrue(row["accepted_sufficient_budget"])
            self.assertEqual(row["dependent_beta"], alpha**2)
            self.assertGreater(row["rouche_margin"], 0)
            self.assertGreater(row["laguerre_relative_reserve"], F(1, 2))

    def test_oversize_budget_not_certified(self):
        row = M.perturbation_budget(1, 1)
        self.assertFalse(row["accepted_sufficient_budget"])
        self.assertLess(row["rouche_margin"], 0)

    def test_budget_domain_and_geometry_guards(self):
        for args in ((-1, 1), (1, 0), (F(1, 2), 1), (True, 1), (1, 1.0)):
            with self.subTest(args=args), self.assertRaises((ValueError, TypeError)):
                M.perturbation_budget(*args)

    def test_repaired_tail_threshold_is_fixed_and_height_expanded(self):
        row = M.repaired_tail_budget(F(1, 32), F(1, 256), F(1, 256))
        self.assertEqual(row["complex_error_bound"], F(1, 64))
        self.assertGreater(row["real_laguerre_reserve_lower_bound"], F(1, 3))
        self.assertTrue(row["requires_Hstar_max_H_disk_radius"])
        self.assertTrue(row["requires_holomorphic_neighborhood_not_just_one_moment"])

    def test_repaired_tail_raw_and_margin_guards(self):
        for args in (
            (-1, 0, 0),
            (F(1, 31), 0, 0),
            (0, F(1, 255), 0),
            (0, 0, F(1, 255)),
            (0, False, 0),
            (0, 0, 0.0),
        ):
            with self.subTest(args=args), self.assertRaises((ValueError, TypeError)):
                M.repaired_tail_budget(*args)

    def test_gaussian_moments_not_saddle_samples(self):
        self.assertEqual(
            [row["standard_normal_moment"] for row in M.gaussian_control(4)],
            [1, 1, 3, 15, 105],
        )
        self.assertEqual(
            M.gaussian_control(0), [{"power": 0, "standard_normal_moment": 1}]
        )
        for bad in (True, -1, 9, 2.0):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                M.gaussian_control(bad)

    def test_fixed_four_sigma_strict_threshold(self):
        row = M.fixed_window_control(4)
        self.assertEqual(row["strict_dyadic_upper_bound"], F(1, 256))
        self.assertTrue(row["below_fixed_1_over_256_eventually"])
        self.assertFalse(row["fixed_C_tail_tends_to_zero"])
        self.assertFalse(row["exponential_in_k_decay"])
        self.assertFalse(M.fixed_window_control(2)["below_fixed_1_over_256_eventually"])

    def test_fixed_window_caps_and_raw_types(self):
        for bad in (True, 1, 3, 14, 4.0, F(4)):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                M.fixed_window_control(bad)

    def test_full_disk_countercontrol_strict_integer_signs(self):
        row = M.disk_height_countercontrol()
        self.assertEqual(row["R_frequency"] % 4, 3)
        self.assertLess(row["H"], row["disk_radius"])
        self.assertEqual(row["tail_c_exact"], F(1, 2**20))
        self.assertGreater(row["epsilon_sinh_R_over_four_strict_lower_bound"], 1)
        self.assertLess(
            row["central_derivative_loss_strict_upper_bound"], row["tail_c_exact"]
        )
        self.assertLess(row["original_phase_upper_using_exp_below_two"], F(1, 256))

    def test_actual_parity_and_zero_order(self):
        rows = M.parity_control(4)
        self.assertEqual(
            [row["actual_derivative_cos_sin"] for row in rows],
            [(1, 0), (0, -1), (-1, 0), (0, 1), (1, 0)],
        )
        self.assertEqual(rows[1]["normalized_F_cos_sin"], (0, 1))
        self.assertEqual(rows[1]["actual_scalar_sign"], -1)
        with self.assertRaises(ValueError):
            M.parity_control(True)

    def test_retained_descent_counterexamples(self):
        row = M.descent_countercontrols()
        self.assertEqual(
            row["parent_derivative_defect_endpoint"], ((0, 1, 2, 1), (0, 3, 4, 1))
        )
        self.assertFalse(row["descent_discharge"])

    def test_all_frozen_source_authentication(self):
        row = M.authenticate_sources()
        self.assertEqual(row["source_count"], 7)
        self.assertFalse(row["remote_bytes_authenticated"])

    def test_manifest_mutation_rejected_before_git(self):
        candidates = []
        r = M.expected_manifest()
        r["sources"][0]["commit"] = "0" * 40
        candidates.append(r)
        r = M.expected_manifest()
        r["external_contracts"][0]["remote_bytes_authenticated"] = 0
        candidates.append(r)
        r = M.expected_manifest()
        r["extra"] = True
        candidates.append(r)
        with patch.object(
            M.subprocess, "check_output", side_effect=AssertionError("git reached")
        ):
            for r in candidates:
                with self.subTest(r=r), self.assertRaises(ValueError):
                    M.authenticate_sources(r)

    def test_blob_tamper_rejected(self):
        with (
            patch.object(
                M.subprocess, "check_output", side_effect=[b"0" * 40, b"wrong"]
            ),
            self.assertRaises(ValueError),
        ):
            M.authenticate_sources(M.expected_manifest())

    def test_lf_and_canonical_json_contracts(self):
        self.assertEqual(M.sha256_lf(b"a\r\nb\r\n"), M.sha256_lf(b"a\nb\n"))
        self.assertEqual(M.canonical({"b": 2, "a": 1}), M.canonical({"a": 1, "b": 2}))
        self.assertNotEqual(M.canonical({"x": False}), M.canonical({"x": 0}))
        self.assertNotEqual(M.canonical({"x": 1}), M.canonical({"x": 1.0}))

    def test_strict_json_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "input.json"
            for raw in (
                '{"x":1,"x":2}',
                '{"x":NaN}',
                '{"x":Infinity}',
                '{"x":-Infinity}',
            ):
                path.write_text(raw, encoding="utf-8")
                with self.subTest(raw=raw), self.assertRaises(ValueError):
                    M.read_json(path)

    def test_fixture_exact_rebuild(self):
        self.assertEqual(M.canonical(self.report), M.canonical(M.read_json(M.FIXTURE)))
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)

    def test_complete_report_typed_mutations_rejected(self):
        candidates = []
        for field, value in (
            ("saddle_coordinate_cases", 4.0),
            ("unbounded_search", 0),
            ("Taylor_coefficients_compared", 33),
        ):
            r = copy.deepcopy(self.report)
            r["coverage"][field] = value
            candidates.append(r)
        r = copy.deepcopy(self.report)
        r["scope"]["fixed_C_sigma_tail_exponentially_small_in_k"] = True
        candidates.append(r)
        r = copy.deepcopy(self.report)
        r["saddle_controls"][0]["precision"] = "338/2"
        candidates.append(r)
        with patch.object(M, "build_report", return_value=self.report):
            for r in candidates:
                with self.subTest(r=r), self.assertRaises(ValueError):
                    M.validate_report(r)

    def test_coverage_and_scientific_boundaries(self):
        self.assertEqual(self.report["coverage"]["Taylor_coefficients_compared"], 34)
        self.assertEqual(self.report["coverage"]["perturbation_budgets"], 8)
        self.assertEqual(
            self.report["normalization"]["half_line_cosine_multiple_of_phi0"], 4
        )
        self.assertEqual(self.report["arithmetic_class"], "EXACT_RATIONAL")
        self.assertTrue(self.report["scope"]["fixed_H_one_half_allowed"])
        for field in (
            "fixed_C_sigma_tail_exponentially_small_in_k",
            "exact_rectangle_endpoint_count_claimed",
            "full_theta_kernel_log_concavity_assumed",
            "old_complex_moving_ray_theorem_imported",
            "finite_controls_are_actual_transcendental_saddles",
            "analytic_proof_formally_machine_verified",
            "XICURV107110_discharged",
            "reverse_Rolle_descent_discharged",
            "source_Pick_transfer",
            "RH_or_percentage",
            "cosine_universality_novelty_claim",
        ):
            self.assertIs(self.report["scope"][field], False)

    def test_no_optimized_away_predicates_or_float_solver(self):
        raw = PATH.read_text(encoding="utf-8")
        self.assertFalse(
            any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(raw)))
        )
        self.assertNotIn("float(", raw)
        self.assertNotIn("import scipy", raw)


if __name__ == "__main__":
    unittest.main()
