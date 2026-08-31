"""Hostile exact checks; the unbounded analytic proof remains in the note."""

import copy
import importlib.util
import json
import subprocess
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/exploratory/xi_confluent_source_band_obstruction.py"
SPEC = importlib.util.spec_from_file_location("xi_confluent_band", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class XiConfluentSourceBandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = MODULE.build_report()

    def test_all_ten_primitive_bindings_authenticate(self):
        self.assertEqual(MODULE.authenticate_sources()["source_count"], 10)
        sources = MODULE.expected_manifest()["sources"]
        source = next(
            row for row in sources if row["role"] == "reviewed_actual_Xi_concentration"
        )
        review = next(
            row for row in sources if row["role"] == "independent_concentration_review"
        )
        self.assertEqual(source["commit"], "3b6972320899a82c6caa3a98e2ada5ff703a605a")
        self.assertEqual(review["commit"], "f3d074190e64a97ac935b93c5b628568cde90858")

    def test_laguerre_initial_and_max_public_order(self):
        self.assertEqual(MODULE.laguerre(0), (1,))
        self.assertEqual(MODULE.laguerre(1), (1, -1))
        self.assertEqual(MODULE.laguerre(2), (1, -2, Fraction(1, 2)))
        self.assertEqual(
            MODULE.exp_integral(MODULE.p_mul(MODULE.laguerre(8), MODULE.laguerre(8))), 1
        )

    def test_all_cross_integrals_and_energies(self):
        for j in range(8):
            data = MODULE.laguerre_control(j)
            self.assertEqual(data["norm_squared"], 1)
            self.assertEqual(data["first_moment"], 2 * j + 1)
            self.assertEqual(data["derivative_energy"], Fraction(2 * j + 1, 4))
            for k in range(8):
                self.assertEqual(
                    MODULE.exp_integral(
                        MODULE.p_mul(MODULE.laguerre(j), MODULE.laguerre(k))
                    ),
                    int(j == k),
                )

    def test_q1_and_all_q_squared_constants(self):
        for q in range(1, 9):
            self.assertEqual(
                MODULE.multiplicity_control(q)["sum_of_odd_constants"], q * q
            )
        self.assertEqual(MODULE.model_matrices(1)[0], ((Fraction(1, 2),),))

    def test_native_q2_matrices_and_outer_debt(self):
        data = MODULE.metric_control(2)
        self.assertEqual(data["C_outer_jet"], ((2, 1), (0, 2)))
        self.assertEqual(
            data["V_inner_jet"],
            ((Fraction(1, 3), Fraction(-4, 9)), (0, Fraction(1, 3))),
        )
        self.assertEqual(data["native_total_charge"], Fraction(82, 81))
        self.assertEqual(data["incorrect_outer_dropped_charge"], Fraction(172, 81))
        self.assertEqual(
            data["regularized_determinant_native_and_outer"], Fraction(161, 324)
        )
        self.assertEqual(
            data["native_band_trace_constant_and_minus_exp_minus_two"], (2, 6)
        )
        self.assertEqual(data["incorrect_dropped_outer_band_trace"], (12, 44))
        self.assertTrue(all(data["noncommuting_pairs"].values()))

    def test_held_out_q4_complete_matrix_control(self):
        data = MODULE.metric_control(4)
        self.assertEqual(data["native_total_charge"], Fraction(19684, 6561))
        self.assertEqual(data["incorrect_outer_dropped_charge"], Fraction(113788, 6561))
        self.assertEqual(
            data["regularized_determinant_native_and_outer"], Fraction(13121, 104976)
        )
        self.assertTrue(data["G_positive_and_inner_Pick_semidefinite_exact_minors"])

    def test_exact_source_covariance_at_held_out_taus(self):
        for q in (2, 3, 4):
            g, h, c, v = MODULE.model_matrices(q)
            go, jr = MODULE.congruence(g, c), MODULE.m_mul(c, v)
            for tau in (Fraction(1, 4), Fraction(3, 4)):
                native = MODULE.determinant(
                    MODULE.m_add(g, MODULE.m_scale(MODULE.congruence(g, v), -tau))
                ) / MODULE.determinant(g)
                outer = MODULE.determinant(
                    MODULE.m_add(go, MODULE.m_scale(MODULE.congruence(g, jr), -tau))
                ) / MODULE.determinant(go)
                self.assertEqual(native, outer)
            self.assertEqual(
                MODULE.source_trace(g, v, h), MODULE.source_trace(go, jr, h)
            )

    def test_source_jet_covariance_also_for_complex_adjoint_algebra_in_note_only(self):
        # The exact checker is deliberately real-rational, not a hidden complex backend.
        self.assertIn("real rational matrices", self.report["arithmetic_domain"])
        with self.assertRaises(TypeError):
            MODULE.matrix(((1 + 0j,),))

    def test_physical_inner_projection_countercontrol(self):
        data = MODULE.inner_noncommutator(1, 2)
        self.assertEqual(data["tail_commutator_coefficient_of_exp_minus_s"], 2)
        self.assertEqual(data["squared_tail_norm_coefficient"], 2)
        self.assertEqual(data["squared_tail_norm_exponent"], -4)
        data = MODULE.inner_noncommutator(Fraction(1, 3), Fraction(5, 6))
        self.assertEqual(data["tail_commutator_coefficient_of_exp_minus_s"], 1)
        self.assertEqual(data["squared_tail_norm_coefficient"], Fraction(1, 2))

    def test_envelope_center_width_and_offset(self):
        data = MODULE.envelope_constants(5, 1)
        self.assertEqual(data["p_limit"], Fraction(1, 10))
        self.assertEqual(data["pi_times_lower_shift_coefficient"], Fraction(-9, 4))
        self.assertEqual(data["pi_times_upper_shift_coefficient"], Fraction(11, 4))
        self.assertEqual(data["pi_times_center_shift_coefficient"], Fraction(1, 4))
        self.assertEqual(data["pi_times_log_width_coefficient"], 5)
        for k in range(1, 16, 2):
            for m in (Fraction(1, 2), 1, 2):
                row = MODULE.envelope_constants(k, m)
                self.assertEqual(row["pi_times_log_width_coefficient"], k * m)

    def test_order_and_resource_guards(self):
        for value in (True, False, -1, 9, 2**1000, 1.0, Fraction(1)):
            with self.assertRaises(ValueError):
                MODULE.multiplicity_control(value)
        for value in (True, -1, 9, 1.0, Fraction(1)):
            with self.assertRaises(ValueError):
                MODULE.laguerre(value)
        for value in (True, 0, 1, 5, 2.0, Fraction(2)):
            with self.assertRaises(ValueError):
                MODULE.metric_control(value)
        for value in (0, 2, 16, True, Fraction(5), 5.0):
            with self.assertRaises(ValueError):
                MODULE.envelope_constants(value, 1)

    def test_exact_inputs_and_bit_caps(self):
        for value in (True, False, 0.0, 1.0, float("nan"), float("inf"), "1", None):
            with self.assertRaises(TypeError):
                MODULE.exact(value)
        for value in (2**128, Fraction(1, 2**128)):
            with self.assertRaises(ValueError):
                MODULE.exact(value)
        self.assertEqual(MODULE.exact(2**127), 2**127)

    def test_polynomial_validates_trailing_raw_values(self):
        for poly in ((1, False), (1, 0.0), (1, None)):
            with self.assertRaises(TypeError):
                MODULE.polynomial(poly)
        for poly in ((), tuple(range(21))):
            with self.assertRaises(ValueError):
                MODULE.polynomial(poly)
        with self.assertRaises(TypeError):
            MODULE.polynomial("1")
        with self.assertRaises(ValueError):
            MODULE.p_mul((1,) * 20, (1, 1))

    def test_matrix_shapes_and_exact_guards(self):
        for data in ((), ((1, 2),), ((1,), (2,)), tuple((1,) * 5 for _ in range(5))):
            with self.assertRaises(ValueError):
                MODULE.matrix(data)
        with self.assertRaises(TypeError):
            MODULE.matrix(((True,),))
        with self.assertRaises(ValueError):
            MODULE.inverse(((1, 1), (1, 1)))
        with self.assertRaises(ValueError):
            MODULE.principal_minors(((1, 1), (0, 1)))
        with self.assertRaises(ValueError):
            MODULE.m_mul(((1,),), ((1, 0), (0, 1)))

    def test_band_domain_and_zero_tolerance_guards(self):
        for a, b in ((-1, 2), (1, 1), (2, 1)):
            with self.assertRaises(ValueError):
                MODULE.inner_noncommutator(a, b)
        for m in (0, -1):
            with self.assertRaises(ValueError):
                MODULE.envelope_constants(5, m)
        self.assertEqual(
            MODULE.inner_noncommutator(0, 1)["squared_tail_norm_coefficient"], 2
        )

    def test_manifest_omissions_reordered_roles_and_type_drift_fail(self):
        manifest = MODULE.expected_manifest()
        manifest["sources"].pop()
        with self.assertRaises(ValueError):
            MODULE.authenticate_sources(manifest)
        manifest = MODULE.expected_manifest()
        manifest["sources"][0]["role"] = "synthetic_not_native"
        with self.assertRaises(ValueError):
            MODULE.authenticate_sources(manifest)
        manifest = MODULE.expected_manifest()
        manifest["external_formulas"][0]["remote_content_machine_authenticated"] = 0
        with self.assertRaises(ValueError):
            MODULE.authenticate_sources(manifest)

    def test_blob_mismatch_digest_mismatch_and_missing_source_fail(self):
        with (
            mock.patch.object(MODULE.subprocess, "check_output", return_value=b"bad\n"),
            self.assertRaises(ValueError),
        ):
            MODULE.authenticate_sources()
        expected_blob = MODULE.SOURCE_ROWS[0][3].encode() + b"\n"
        with (
            mock.patch.object(
                MODULE.subprocess,
                "check_output",
                side_effect=[expected_blob, b"bad content\n"],
            ),
            self.assertRaises(ValueError),
        ):
            MODULE.authenticate_sources()
        with (
            mock.patch.object(
                MODULE.subprocess,
                "check_output",
                side_effect=subprocess.CalledProcessError(128, "git"),
            ),
            self.assertRaises(subprocess.CalledProcessError),
        ):
            MODULE.authenticate_sources()

    def test_lf_hash_is_crlf_invariant(self):
        self.assertEqual(MODULE.sha256_lf(b"a\r\nb\r\n"), MODULE.sha256_lf(b"a\nb\n"))
        self.assertNotEqual(MODULE.sha256_lf(b"a\nb\n"), MODULE.sha256_lf(b"a\nb"))

    def test_json_duplicate_nonfinite_and_typed_contract(self):
        for raw in ('{"x":1,"x":2}', '{"x":NaN}', '{"x":Infinity}'):
            with (
                mock.patch.object(Path, "read_text", return_value=raw),
                self.assertRaises(ValueError),
            ):
                MODULE.read_json(Path("unused.json"))
        self.assertNotEqual(MODULE.canonical({"x": False}), MODULE.canonical({"x": 0}))
        self.assertNotEqual(MODULE.canonical({"x": 1.0}), MODULE.canonical({"x": 1}))

    def test_fixture_complete_replay(self):
        MODULE.validate_report(MODULE.read_json(MODULE.FIXTURE))
        self.assertEqual(self.report["coverage"]["cross_orthogonality_cells"], 64)
        self.assertEqual(len(self.report["native_metric_controls"]), 2)
        self.assertEqual(len(self.report["fixed_order_envelope_constants"]), 24)

    def test_scope_and_arithmetic_mutations_rejected(self):
        for section, key, value in (
            ("scope", "physical_inner_weighted_band_Gram_controlled", True),
            ("scope", "arbitrary_distinct_node_clusters", True),
            ("scope", "literal_source_J_R_coefficients_not_free", False),
            ("scope", "floating_point_Xi_samples", False),
        ):
            report = copy.deepcopy(self.report)
            report[section][key] = value
            with self.assertRaises(ValueError):
                MODULE.validate_report(report)
        report = copy.deepcopy(self.report)
        report["arithmetic_class"] = "DIRECTED_INTERVAL"
        with self.assertRaises(ValueError):
            MODULE.validate_report(report)

    def test_finite_coverage_value_and_artifact_hash_mutations_rejected(self):
        report = copy.deepcopy(self.report)
        report["Laguerre_cross_orthogonality"].pop()
        with self.assertRaises(ValueError):
            MODULE.validate_report(report)
        report = copy.deepcopy(self.report)
        report["native_metric_controls"][0]["native_total_charge"] = "0"
        with self.assertRaises(ValueError):
            MODULE.validate_report(report)
        report = copy.deepcopy(self.report)
        first = next(iter(report["artifact_sha256_lf"]))
        report["artifact_sha256_lf"][first] = "0" * 64
        with self.assertRaises(ValueError):
            MODULE.validate_report(report)

    def test_plain_json_serialization_has_no_binary_float(self):
        self.assertEqual(json.loads(json.dumps(self.report)), self.report)
        self.assertEqual(self.report["arithmetic_class"], "EXACT_RATIONAL")
        self.assertIn("no rounded transcendental", self.report["rounding_contract"])
        self.assertFalse(
            self.report["scope"]["analytic_proof_formally_machine_verified"]
        )


if __name__ == "__main__":
    unittest.main()
