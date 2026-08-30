"""Hostile exact replay; no floating evaluation is used as an analytic proof."""

import ast
import copy
import importlib.util
import io
import subprocess
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "research/exploratory/xi_positive_kernel_descent_firewall.py"
SPEC = importlib.util.spec_from_file_location("positive_kernel_firewall", PRODUCER)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class FirewallTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def test_full_source_authenticated_fixture(self):
        M.validate_report(M.read_json(M.FIXTURE))

    def test_all_eight_frozen_sources_and_reviews(self):
        self.assertEqual(M.authenticate_sources()["source_count"], 8)
        roles = {row[0] for row in M.SOURCE_ROWS}
        self.assertTrue(
            {
                "actual_kernel_review",
                "high_derivative_review",
                "literal_defect_definition",
                "literal_defect_cascade",
                "earlier_nondescent_firewall",
            }
            <= roles
        )

    def test_algebraic_root_and_full_disk(self):
        row = M.fixed_root_control()
        self.assertEqual(row["two_C0_squared_minus_three_C0_minus_one"], (0, 0))
        self.assertEqual(row["C0_squared"], (F(13, 8), F(3, 8)))
        self.assertEqual(row["imaginary_lower"], F(31, 256))
        self.assertEqual(row["imaginary_upper"], F(97, 256))
        self.assertLess(row["modulus_upper"], F(3, 2))

    def test_rouche_rational_reserves(self):
        row = M.fixed_root_control()
        self.assertEqual(row["Psecond_strict_upper"], 1872)
        self.assertEqual(row["Taylor_strict_lower"], F(107, 8192))
        self.assertEqual(row["BP_strict_lower"], F(26429, 2097152))
        self.assertEqual(row["Rouche_strict_reserve"], F(10045, 2097152))
        self.assertGreater(row["Rouche_strict_reserve"], 0)

    def test_literal_wrong_sign_extremum_reserves(self):
        row = M.fixed_defect_control()
        self.assertEqual(row["B_lower"], F(31, 32))
        self.assertEqual(row["F_strict_upper"], -F(245, 384))
        self.assertEqual(row["endpoint_Fprime_strict_reserve"], F(113, 6144))
        self.assertEqual(row["Fsecond_strict_upper"], -F(7303, 1536))

    def test_literal_r_iota_and_boundary_not_omitted(self):
        row = M.fixed_defect_control()
        self.assertEqual((row["r"], row["iota"], row["defect_r_plus_iota"]), (1, 1, 2))
        self.assertEqual(row["boundary_index"], 1)
        self.assertEqual(row["ledger_residual"], 0)
        self.assertNotEqual(0, 1 - 2)  # Dropping the boundary breaks this example.

    def test_finite_coverage_counts(self):
        coverage = self.report["coverage"]
        self.assertEqual(coverage["current_weights"], 80)
        self.assertEqual(coverage["endpoint_side_weights"], 32)
        self.assertEqual(coverage["compact_mass_budgets"], 12)
        self.assertEqual(coverage["exterior_identities"], 9)
        self.assertFalse(coverage["unbounded_computation"])

    def test_holdout_weights_including_negative_arguments(self):
        count = 0
        for k in (1, 3, 7, 15):
            for xi in (F(3, 2), F(19, 8)):
                for d in (-3 * xi, -xi, F(1, 7), xi, 3 * xi):
                    row = M.current_weight(k, xi, d)
                    self.assertEqual(row["direct"], d * (row["v"] ** k - row["u"] ** k))
                    self.assertEqual(row["direct"], row["expanded"])
                    self.assertGreaterEqual(row["direct"], 0)
                    count += 1
        self.assertEqual(count, 40)

    def test_K_one_exact_weight_and_zero_displacement(self):
        for d in (F(-7, 3), F(0), F(2, 9)):
            self.assertEqual(M.current_weight(1, F(5, 2), d)["direct"], d * d)
        self.assertEqual(M.current_weight(15, 7, 0)["direct"], 0)

    def test_endpoint_exterior_identity_at_boundary_and_holdout(self):
        self.assertEqual(M.exterior_identity(3, 1)["right"], 0)
        for x, y in ((F(7, 3), F(11, 4)), (2**63 - 1, F(19, 8))):
            row = M.exterior_identity(x, y)
            self.assertEqual(row["left"], row["right"])

    def test_exponent_budget_threshold_and_extreme_cap(self):
        row = M.exponent_budget(4 * M.R, 15, 6)
        self.assertEqual(row["square_loss_reserve_above_xi_squared_over_four"], 0)
        self.assertEqual(row["support_enclosure_total_length"], 65)
        self.assertGreater(row["support_abs_d_upper"], row["xi_formal"])
        self.assertGreater(
            M.exponent_budget(2**63 - 1, 15, 6)[
                "square_loss_reserve_above_xi_squared_over_four"
            ],
            0,
        )

    def test_compact_mass_coefficient_and_actual_mass_not_evaluated(self):
        self.assertEqual(M.MASS, 64 + F(64, 3))
        row = M.compact_mass_budget(8, 3, 2)
        self.assertEqual(
            row["m_times_relative_weighted_mass_upper_before_exp_H_a_plus_L"], 48
        )
        self.assertTrue(row["no_numeric_m_or_saddle_or_limit_evaluation"])

    def test_ratio_control_signed_observables(self):
        for j, dj in ((3, 5), (-3, 5), (3, -5), (-3, -5), (0, 0)):
            row = M.ratio_control(F(5, 7), j, F(9, 11), dj)
            self.assertEqual(
                row["direct_difference"], row["retained_denominator_difference"]
            )
            self.assertLessEqual(abs(row["direct_difference"]), row["absolute_bound"])

    def test_denominator_cannot_be_dropped(self):
        row = M.ratio_control(1, 1, 1, 0)
        self.assertEqual(row["direct_difference"], -F(1, 2))
        self.assertNotEqual(row["direct_difference"], row["DeltaJ"] / row["Z"])

    def test_ratio_zero_added_mass_algebra_edge(self):
        row = M.ratio_control(2, -3, 0, 0)
        self.assertEqual(row["direct_difference"], 0)
        self.assertEqual(row["absolute_bound"], 0)

    def test_odd_K_and_positive_xi_guards(self):
        for k in (0, 2, 16, -1, True, 3.0):
            with self.subTest(k=k), self.assertRaises((ValueError, TypeError)):
                M.current_weight(k, 1, 1)
        for xi in (0, -1, True, 1.0):
            with self.subTest(xi=xi), self.assertRaises((ValueError, TypeError)):
                M.current_weight(3, xi, 1)

    def test_exponent_and_exterior_domain_guards(self):
        for args in (
            (4 * M.R - F(1, 100), 1, 0),
            (64, 2, 1),
            (64, 1, 7),
            (64, 1, True),
        ):
            with self.subTest(args=args), self.assertRaises((ValueError, TypeError)):
                M.exponent_budget(*args)
        for args in ((1, 2), (2, F(1, 2)), (True, 2), (2, 1.0)):
            with self.subTest(args=args), self.assertRaises((ValueError, TypeError)):
                M.exterior_identity(*args)

    def test_compact_index_and_coordinate_guards(self):
        for args in (
            (65, 2, 0),
            (-1, 2, 0),
            (8, 1, 2),
            (8, 3, 7),
            (True, 2, 0),
            (8, 3, 2.0),
        ):
            with self.subTest(args=args), self.assertRaises((ValueError, TypeError)):
                M.compact_mass_budget(*args)

    def test_ratio_domain_and_type_guards(self):
        for args in (
            (0, 1, 1, 0),
            (-1, 1, 1, 0),
            (1, 1, -1, 0),
            (1, 1, 0, True),
            (1, 1.0, 0, 0),
        ):
            with self.subTest(args=args), self.assertRaises((ValueError, TypeError)):
                M.ratio_control(*args)

    def test_input_and_intermediate_caps(self):
        self.assertEqual(M.rational(2**63), 2**63)
        for value in (2**64, F(1, 2**64), True, 0.5):
            with (
                self.subTest(value=str(value)),
                self.assertRaises((ValueError, TypeError)),
            ):
                M.rational(value)
        with self.assertRaises(ValueError):
            M.checked(2**4096)
        with self.assertRaises(TypeError):
            M.checked(False)

    def test_full_scope_semantics_and_no_analytic_upgrade(self):
        scope = self.report["scope"]
        for key in (
            "frequency_kernel_real_analytic",
            "all_counterfeit_zeros_in_global_strip",
            "arithmetic_origin_or_Euler_product",
            "authentic_Xi_source_jets_or_Pick_transfer",
            "Xi_XICURV_or_descent_discharged",
            "asymptotic_limits_interchanged",
            "novelty_claim",
            "analytic_proof_formally_machine_verified",
        ):
            self.assertIs(scope[key], False)
        self.assertIs(scope["endpoint_side_abs_d_above_xi_included"], True)
        self.assertIs(scope["fixed_H_one_half_allowed"], True)
        self.assertEqual(scope["literal_first_rung_defect"], 2)

    def test_rebuilt_report_rejects_scope_and_type_mutations(self):
        mutations = [
            ("scope", "frequency_kernel_real_analytic", True),
            ("scope", "Xi_XICURV_or_descent_discharged", True),
            ("scope", "source_frequency_limit_K_fixed", False),
            ("scope", "normalized_ratio_error_retained", False),
            ("scope", "literal_first_rung_defect", 2.0),
            ("scope", "boundary_index", True),
            ("coverage", "current_weights", 79),
            ("caps", "K", 999999),
            ("source_authentication", "remote_bytes_authenticated", 0),
        ]
        with patch.object(M, "build_report", return_value=self.report):
            for section, key, value in mutations:
                candidate = copy.deepcopy(self.report)
                candidate[section][key] = value
                with self.subTest(key=key), self.assertRaises(ValueError):
                    M.validate_report(candidate)

    def test_unknown_report_field_and_changed_arithmetic_rejected(self):
        with patch.object(M, "build_report", return_value=self.report):
            for key, value in (("unrequested_field", 1), ("arithmetic_class", "EXACT")):
                candidate = copy.deepcopy(self.report)
                candidate[key] = value
                with self.assertRaises(ValueError):
                    M.validate_report(candidate)

    def test_source_contract_tampering_rejected_before_git(self):
        for kind in ("role", "commit", "sha256_lf", "scope", "external"):
            manifest = M.expected_manifest()
            if kind == "scope":
                manifest["source_scope"] = "arithmetic source transfer"
            elif kind == "external":
                manifest["external_contracts"][0]["remote_bytes_authenticated"] = 0
            else:
                manifest["sources"][0][kind] = "changed"
            with patch.object(M.subprocess, "check_output") as invoke:
                with self.subTest(kind=kind), self.assertRaises(ValueError):
                    M.authenticate_sources(manifest)
                invoke.assert_not_called()

    def test_missing_frozen_source_fails_closed(self):
        error = subprocess.CalledProcessError(128, ["git", "show"])
        with (
            patch.object(M.subprocess, "check_output", side_effect=error),
            self.assertRaises(subprocess.CalledProcessError),
        ):
            M.authenticate_sources()

    def test_wrong_source_blob_and_content_fail_closed(self):
        blob = M.SOURCE_ROWS[0][3].encode() + b"\n"
        for outputs in ((b"0" * 40 + b"\n", b"wrong"), (blob, b"wrong")):
            with (
                patch.object(M.subprocess, "check_output", side_effect=outputs),
                self.assertRaises(ValueError),
            ):
                M.authenticate_sources()

    def test_lf_hash_stable_under_windows_checkout(self):
        self.assertEqual(M.sha256_lf(b"a\r\nb\r\n"), M.sha256_lf(b"a\nb\n"))
        self.assertNotEqual(M.sha256_lf(b"a\nb\n"), M.sha256_lf(b"a\nb changed\n"))

    def test_strict_json_duplicate_nonfinite_and_byte_cap(self):
        for raw in (
            b'{"a":1,"a":2}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b" " * (M.MAX_JSON_BYTES + 1),
        ):
            with self.subTest(raw=raw[:30]), self.assertRaises(ValueError):
                M.read_json(Mock(open=Mock(return_value=io.BytesIO(raw))))

    def test_json_scalar_types_remain_distinct(self):
        self.assertNotEqual(M.canonical({"x": 1}), M.canonical({"x": True}))
        self.assertNotEqual(M.canonical({"x": 1}), M.canonical({"x": 1.0}))
        with self.assertRaises(ValueError):
            M.canonical({"x": float("nan")})

    def test_all_four_artifact_hashes_bound(self):
        hashes = self.report["artifact_sha256_lf"]
        for path in (M.NOTE, PRODUCER, M.TEST, M.MANIFEST):
            self.assertEqual(
                hashes[path.relative_to(ROOT).as_posix()],
                M.sha256_lf(path.read_bytes()),
            )
        self.assertEqual(len(hashes), 4)

    def test_no_assert_based_producer_acceptance(self):
        tree = ast.parse(PRODUCER.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()
