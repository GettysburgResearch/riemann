"""Exact finite algebra and hostile guards; no analytic onset or zero sampling."""

import ast
import copy
import hashlib
import importlib.util
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "research/l-families/atlas/generalized/cusp_flag_uncancelled_off_central_real_zeros.py"
)
SPEC = importlib.util.spec_from_file_location("uncancelled_cusp_tested", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def recurrence_polynomial(m):
    row = [1]
    for j in range(1, m + 1):
        row = [j * v for v in row] + [1]
    return row


def stripped_tail(m, c):
    value = 1 / c
    for j in range(1, m + 1):
        value = (1 + j * value) / c
    return value


class UncancelledTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = M.authenticated_sources()
        cls.family = M.source_module(cls.sources, "family")
        cls.cusp = M.source_module(cls.sources, "cusp")
        cls.report = M.build_report()

    def test_01_complete_fixture(self):
        fixture = M.parse_json(M.FIXTURE.read_bytes())
        self.assertEqual(M.canonical(fixture), M.canonical(self.report))
        M.validate_report(fixture)

    def test_02_tail_polynomials_independent_recurrence(self):
        for m in range(13):
            self.assertEqual(M.tail_polynomial(m, M.Budget()), recurrence_polynomial(m))
        self.assertEqual(M.tail_polynomial(0, M.Budget()), [1])
        self.assertEqual(M.tail_polynomial(3, M.Budget()), [6, 6, 3, 1])

    def test_03_all_tail_ratios_by_integral_recurrence(self):
        for row in self.report["incomplete_Gamma_tail_controls"]:
            m, c = row["m"], Q(row["rational_c_control"])
            independent = stripped_tail(m + 1, c) / stripped_tail(m, c)
            self.assertEqual(independent, Q(row["tail_ratio_after_exp_cancellation"]))
            self.assertLessEqual(independent, 1 + (m + 1) / c)

    def test_04_polynomial_gap_and_boundary_case(self):
        for row in self.report["incomplete_Gamma_tail_controls"]:
            m = row["m"]
            p, nxt = recurrence_polynomial(m), recurrence_polynomial(m + 1)
            lhs = [0] + p
            for j, coefficient in enumerate(p):
                lhs[j] += (m + 1) * coefficient
            gap = [a - b for a, b in zip(lhs, nxt)]
            self.assertEqual(row["gap_coefficients"], gap)
            self.assertTrue(all(v >= 0 for v in gap))
            if m == 0:
                self.assertEqual(gap, [0, 0])
                self.assertEqual(
                    row["tail_ratio_after_exp_cancellation"],
                    row["upper_one_plus_m1_over_c"],
                )

    def test_05_heldout_tail_parameters(self):
        for m in (0, 2, 7, 11):
            for c in (Q(1, 31), Q(11, 7), Q(31)):
                row = M.tail_control(m, c)
                self.assertEqual(
                    Q(row["tail_ratio_after_exp_cancellation"]),
                    stripped_tail(m + 1, c) / stripped_tail(m, c),
                )
                self.assertFalse(row["c_equals_actual_4pi_n"])

    def test_06_native_leading_signs_and_pi_cancellation(self):
        row = self.report["native_scale_window"]
        self.assertEqual(Q(row["epsilon_times_k"]), 18)
        self.assertEqual(
            Q(row["q1_witness_leading_margin"]), Q(1, 6) * Q(1, 4) - Q(1, 36)
        )
        self.assertEqual(
            Q(row["all_W_upper_leading_margin"]), Q(1, 6) * Q(1, 8) - Q(1, 36)
        )
        self.assertEqual(row["q1_moment_pi_exponent"] + row["Lambda2_pi_exponent"], 0)
        self.assertEqual(row["q1_witness_leading_margin"], "1/72")
        self.assertEqual(row["all_W_upper_leading_margin"], "-1/144")

    def test_07_strict_scale_window_not_endpoints(self):
        for c in (Q(121, 10), Q(37, 2), Q(239, 10)):
            row = M.cutoff_window(c)
            self.assertGreater(Q(row["q1_witness_leading_margin"]), 0)
            self.assertLess(Q(row["all_W_upper_leading_margin"]), 0)
            self.assertFalse(row["finite_onset_certified"])
        for c in (12, 24, 11, 25):
            with self.assertRaises(ValueError):
                M.cutoff_window(c)

    def test_08_native_Miller_flags_from_other_parent_construction(self):
        for panel in self.report["native_small_Miller_flags"]:
            d, order = panel["dimension"], panel["q_order"]
            rows = [
                self.cusp.native_prefix(d, j, order, self.cusp.Budget())["q_prefix"]
                for j in range(1, d + 1)
            ]
            for i in range(d):
                for j in range(i + 1, d):
                    scale = rows[i][j + 1]
                    rows[i] = [a - scale * b for a, b in zip(rows[i], rows[j])]
            self.assertEqual(rows, panel["Miller_rows"])
            self.assertEqual(rows[1:], panel["W_rows"])
            self.assertTrue(all(row[1] == 0 for row in rows[1:]))
            self.assertEqual(rows[0][1], 1)

    def test_09_high_weight_actual_prefix_first_two_terms(self):
        for row in self.report["native_modular_prefixes"]:
            j, d = row["delta_power"], row["dimension"]
            q = row["q_prefix"]
            self.assertEqual(q[:j], [0] * j)
            self.assertEqual(q[j], 1)
            self.assertEqual(q[j + 1], -24 * j + 720 * (d - j))
            self.assertEqual(row["is_in_W"], j >= 2)
            self.assertFalse(row["period_or_eigenvalue_evaluated"])

    def test_10_relative_envelope_exact_arithmetic(self):
        for row in self.report["high_cusp_relative_envelopes"]:
            k, r = row["weight"], Q(row["radial_surrogate"])
            u = 48 * r / (1 - r) + 240 * k * r
            self.assertEqual(u, Q(row["u"]))
            self.assertLessEqual(u, Q(289, k**5))
            self.assertEqual(Q(row["h_over_q_squared_lower"]), 1 - u)
            self.assertEqual(Q(row["h_over_q_squared_upper"]), 1 / (1 - u))
            self.assertLessEqual(1 / (1 - u) - 1, 2 * u)
            self.assertFalse(row["exponential_or_modular_value_sample"])

    def test_11_relative_envelope_zero_and_Bernoulli(self):
        self.assertEqual(M.modular_envelope(24, 0)["u"], "0")
        for k in (24, 48, 96):
            r = Q(1, k**6)
            p = k // 2 - 6
            self.assertGreaterEqual((1 - 480 * r) ** p, 1 - 240 * k * r)
            delta_lower = 1 - 48 * r / (1 - r)
            e4_lower = 1 - 240 * k * r
            u = Q(M.modular_envelope(k, r)["u"])
            self.assertGreaterEqual(delta_lower * e4_lower, 1 - u)

    def test_12_uniform_Fourier_and_product_constants(self):
        c = self.report["uniform_rational_constants"]
        self.assertEqual(
            Q(c["Fourier_remainder_at_radial_boundary"]),
            2 * Q(1, 100) / (1 - Q(1, 100)) ** 2,
        )
        self.assertLess(Q(c["Fourier_remainder_at_radial_boundary"]), 1)
        self.assertEqual(
            Q(c["Delta48_product_coefficient_at_radial_boundary"]), 48 / (1 - Q(1, 100))
        )
        self.assertLess(Q(c["Delta48_product_coefficient_at_radial_boundary"]), 49)
        self.assertEqual(c["combined_k5_error_coefficient"], 49 + 240)

    def test_13_exact_source_and_coverage(self):
        self.assertEqual(len(M.BINDINGS), 10)
        self.assertEqual(self.report["coverage"]["tail_polynomial_models"], 48)
        self.assertEqual(self.report["coverage"]["native_small_flag_models"], 3)
        self.assertEqual(self.report["coverage"]["native_modular_prefixes"], 8)
        for key, maximum in (
            ("charged_work", M.MAX_WORK),
            ("charged_family_work", M.FAMILY_WORK),
            ("charged_cusp_work", M.CUSP_WORK),
        ):
            self.assertLessEqual(self.report["coverage"][key], maximum)

    def test_14_no_inherited_explicit_onset(self):
        scope = self.report["scope"]
        self.assertEqual(scope["onset_type"], "existential k0, not computed")
        self.assertIs(scope["explicit_6144_onset_inherited"], False)
        self.assertIn("eventually", scope["interval"])
        self.assertTrue(scope["whole_W_negativity_near1_by_written_uniform_proof"])
        self.assertTrue(scope["actual_canonical_quotient_uncancelled_real_zero_pair"])

    def test_15_integer_rational_and_budget_guards(self):
        for bad in (True, False, 1.0, "1", None):
            with self.assertRaises(ValueError):
                M.rational(bad)
        for bad in (2**4096, Q(1, 2**4096)):
            with self.assertRaises(ValueError):
                M.rational(bad)
        for bad in (True, 0, M.MAX_WORK + 1):
            with self.assertRaises(ValueError):
                M.Budget(bad)
        with self.assertRaises(ValueError):
            M.Budget().spend(True)

    def test_16_polynomial_caps_and_precharge(self):
        for m in (True, -1, 13, 1.0):
            with self.assertRaises(ValueError):
                M.tail_polynomial(m, M.Budget())
        for m in (True, -1, 12, 1.0):
            with self.assertRaises(ValueError):
                M.tail_control(m, 1)
        work = M.Budget(1)
        with self.assertRaisesRegex(ValueError, "before expansion"):
            M.tail_polynomial(12, work)
        self.assertEqual(work.used, 0)

    def test_17_evaluation_and_scale_guards(self):
        for poly in ([], [1] * 14, [True], [1.0]):
            with self.assertRaises(ValueError):
                M.evaluate(poly, 1, M.Budget())
        for c in (True, 0, -1, 33, Q(1, 2**4096)):
            with self.assertRaises(ValueError):
                M.tail_control(1, c)
        for c in (True, 18.0, "18"):
            with self.assertRaises(ValueError):
                M.cutoff_window(c)

    def test_18_modular_caps(self):
        for k, r in (
            (True, 0),
            (12, 0),
            (25, 0),
            (12289, 0),
            (24, True),
            (24, -1),
            (24, Q(1, 100)),
            (24, 0.0),
        ):
            with self.assertRaises(ValueError):
                M.modular_envelope(k, r)
        with self.assertRaises(ValueError):
            M.tail_control(1, 1, object())

    def test_19_ten_primitive_and_four_artifact_seals(self):
        M.authenticated_sources()
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for path, digest in self.report["artifact_sha256_lf"].items():
            raw = (
                (ROOT / path).read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            )
            self.assertEqual(hashlib.sha256(raw).hexdigest(), digest)
        self.assertEqual(
            M.canonical(self.report["frozen_sources"]), M.canonical(M.BINDINGS)
        )

    def test_20_manifest_semantic_and_type_guards(self):
        for key, value in (
            ("new_uniform_gate", "basis vectors only"),
            ("onset", "6144"),
            ("object", "generic flag"),
        ):
            data = M.expected_manifest()
            data["primitive_contract"][key] = value
            with self.assertRaisesRegex(ValueError, "typed manifest"):
                M.authenticated_sources(data)
        data = M.expected_manifest()
        data["external_context"][0]["remote_bytes_authenticated"] = 0
        with self.assertRaises(ValueError):
            M.authenticated_sources(data)

    def test_21_source_byte_and_constructor_tamper(self):
        with (
            patch.object(M.subprocess, "check_output", side_effect=[b"1", b"x"]),
            self.assertRaisesRegex(ValueError, "primitive identity"),
        ):
            M.authenticated_sources()
        with patch.object(
            M.subprocess, "check_output", return_value=b"2000001"
        ) as mocked:
            with self.assertRaisesRegex(ValueError, "primitive byte cap"):
                M.authenticated_sources()
            self.assertEqual(mocked.call_count, 1)
        for name, stem in (
            ("family", "cusp_flag_quotient_global_family"),
            ("cusp", "cusp_period_off_central_real_zeros"),
        ):
            data = dict(self.sources)
            data["research/l-families/atlas/generalized/" + stem + ".py"] = (
                b"raise RuntimeError('not executed')"
            )
            with self.assertRaisesRegex(ValueError, "constructor identity"):
                M.source_module(data, name)
        for bad in (True, "other", None):
            with self.assertRaises(ValueError):
                M.source_module(self.sources, bad)

    def test_22_JSON_numeric_and_duplicate_guards(self):
        for raw in (
            b'{"x":1,"x":2}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b'{"x":-Infinity}',
            b'{"x":1.0}',
            b'{"x":1e2}',
            b"\xff",
            b"{",
        ):
            with self.assertRaises(ValueError):
                M.parse_json(raw)

    def test_23_JSON_resource_caps(self):
        for data in (
            [0] * 1025,
            {"x": "a" * 4097},
            {1: 0},
            2**4096,
            [[0] * 100 for _ in range(201)],
            ["a" * 4096] * 489,
        ):
            with self.assertRaises(ValueError):
                M.canonical(data)
        for raw in (b" " * 2000001, b"[" * 26 + b"0" + b"]" * 26):
            with self.assertRaises(ValueError):
                M.parse_json(raw)

    def test_24_LF_stability_and_manifest_copy(self):
        self.assertEqual(M.lf_sha(b"a\nb\n"), M.lf_sha(b"a\r\nb\r\n"))
        self.assertEqual(M.lf_sha(b"a\nb\n"), M.lf_sha(b"a\rb\r"))
        data = M.expected_manifest()
        data["frozen_sources"][0]["commit"] = "0" * 40
        data["external_context"][0]["role"] = "changed"
        self.assertNotEqual(M.BINDINGS[0]["commit"], "0" * 40)
        self.assertNotEqual(M.EXTERNAL[0]["role"], "changed")
        self.assertEqual(M.parse_json(M.MANIFEST.read_bytes()), M.expected_manifest())

    def test_25_payload_digest_and_schema_guards(self):
        data = copy.deepcopy(self.report)
        data["payload_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "payload digest"):
            M.validate_report(data)
        with self.assertRaises(ValueError):
            M.seal(self.report)
        with self.assertRaises(ValueError):
            M.validate_report([])

    def test_26_resealed_math_and_source_scope_tamper(self):
        variants = []
        for section, key, value in (
            ("native_scale_window", "all_W_upper_leading_margin", "1/144"),
            ("native_scale_window", "q1_witness_leading_margin", "0"),
            ("scope", "explicit_6144_onset_inherited", True),
            ("scope", "first_coefficient_flag_replaced", True),
            ("scope", "whole_W_negativity_near1_by_written_uniform_proof", False),
            ("scope", "period_Gamma_Bessel_eigenvalue_or_zero_samples", False),
            ("caps", "work", True),
        ):
            data = copy.deepcopy(self.report)
            data.pop("payload_sha256")
            data[section][key] = value
            variants.append(data)
        data = copy.deepcopy(self.report)
        data.pop("payload_sha256")
        data["incomplete_Gamma_tail_controls"][0]["P_m"] = [0]
        variants.append(data)
        with patch.object(M, "build_report", return_value=self.report):
            for data in variants:
                with self.assertRaisesRegex(ValueError, "typed reconstruction"):
                    M.validate_report(M.seal(data))

    def test_27_resealed_metadata_and_artifact_tamper(self):
        variants = []
        for key, value in (
            ("schema", "other"),
            ("arithmetic_class", "EXACT"),
            ("status", "APPROVED"),
            ("rounding_contract", "float"),
        ):
            data = copy.deepcopy(self.report)
            data.pop("payload_sha256")
            data[key] = value
            variants.append(data)
        data = copy.deepcopy(self.report)
        data.pop("payload_sha256")
        data["artifact_sha256_lf"][next(iter(data["artifact_sha256_lf"]))] = "0" * 64
        variants.append(data)
        with patch.object(M, "build_report", return_value=self.report):
            for data in variants:
                with self.assertRaises(ValueError):
                    M.validate_report(M.seal(data))

    def test_28_canonical_arithmetic_and_scope(self):
        self.assertEqual(self.report["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.report["arithmetic_components"],
            ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        )
        self.assertIn("no rounding", self.report["rounding_contract"])
        for key in (
            "single_vector_outside_W_used_as_sufficient",
            "simplicity_or_uniqueness_asserted",
            "analytic_limits_or_integrals_machine_certified",
            "all_weights_or_all_minors_claim",
            "zeta_RH_counterexample",
            "new_automorphic_family_or_exhaustive_novelty",
            "parent_files_modified",
        ):
            self.assertIs(self.report["scope"][key], False)

    def test_29_artifact_control_characters(self):
        for path in (M.NOTE, M.MANIFEST, M.FIXTURE, M.TEST, SOURCE):
            raw = path.read_bytes()
            self.assertFalse(any(v < 32 and v not in (9, 10, 13) for v in raw))
        with (
            patch.object(Path, "read_bytes", return_value=b"invalid\x0ccontrol"),
            self.assertRaisesRegex(ValueError, "control character"),
        ):
            M.artifact_hashes()

    def test_30_proof_preserves_native_quantifiers(self):
        note = M.NOTE.read_text(encoding="utf-8")
        for token in (
            "EVERY nonzero f in W",
            "epsilon AND f",
            "uniformly for beta in [0,1]",
            "exists an onset k_0",
            "not an indefinite minimization principle",
            "No bound\non the individual coefficients",
        ):
            self.assertIn(token, note)
        self.assertIn(r"\frac1{72}", note)
        self.assertIn("a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717", note)

    def test_31_no_assert_float_or_analytic_sampling(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(n, ast.Assert) for n in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(n, ast.Constant) and type(n.value) is float
                for n in ast.walk(tree)
            )
        )
        prohibited = {
            "exp",
            "log",
            "gamma",
            "lgamma",
            "sin",
            "cos",
            "sqrt",
            "quad",
            "eig",
            "eigvals",
        }
        self.assertFalse(
            any(
                isinstance(n, ast.Call)
                and isinstance(n.func, ast.Attribute)
                and n.func.attr in prohibited
                for n in ast.walk(tree)
            )
        )

    def test_32_onset_and_generic_flag_remain_excluded_in_manifest(self):
        contract = M.expected_manifest()["primitive_contract"]
        self.assertIn("no generic flag replacement", contract["object"])
        self.assertIn("all W Parseval", contract["new_uniform_gate"])
        self.assertIn("no coefficient freedom", contract["new_uniform_gate"])
        self.assertIn("no numerical onset", contract["onset"])
        self.assertEqual(M.BASE, "a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717")


if __name__ == "__main__":
    unittest.main()
