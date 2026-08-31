"""Exact independent algebra and fail-closed release tests."""

from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import itertools
import math
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "research/l-families/atlas/generalized/cusp_flag_signed_riemann_von_mangoldt.py"
)
SPEC = importlib.util.spec_from_file_location("cusp_flag_signed_count", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def permutation_det(value):
    n = len(value)
    answer = Q(0)
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        answer += (-1) ** inversions * math.prod(value[i][perm[i]] for i in range(n))
    return answer


class SignedCountTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = M.authenticated_sources()
        cls.family = M.frozen_family(cls.sources)
        cls.report = M.build_report()

    def test_01_frozen_fixture(self):
        fixture = M.parse_json(M.FIXTURE.read_bytes())
        self.assertEqual(M.canonical(fixture), M.canonical(self.report))
        M.validate_report(fixture)

    def test_02_all_native_panels_rank_one_determinant_lemma(self):
        for panel in self.report["native_panels"]:
            d, r = panel["dimension"], panel["residual"]
            rows = self.family.miller_basis(d, r)
            p, n = math.factorial(d), d + 1
            for start, control in enumerate(panel["determinants"]):
                tail_mass = sum(
                    Q(rows[j - 1][n] ** 2 * j**2, n**2) for j in range(1 + start, d + 1)
                )
                expected = (1 + tail_mass) / p**2
                with self.subTest(weight=panel["weight"], start=start):
                    self.assertEqual(Q(control["finite_Gram_determinant"]), expected)
                    self.assertEqual(Q(control["Cauchy_Binet_weighted_sum"]), expected)

    def test_03_all_native_minor_maps_independent_replacement_rule(self):
        for panel in self.report["native_panels"]:
            d, r = panel["dimension"], panel["residual"]
            rows = self.family.miller_basis(d, r)
            p, n = math.factorial(d), d + 1
            for start, control in enumerate(panel["determinants"]):
                expected = {p: Q(1)}
                for j in range(1 + start, d + 1):
                    if rows[j - 1][n]:
                        expected[p * n // j] = Q(rows[j - 1][n] ** 2)
                self.assertEqual(
                    {int(k): Q(v) for k, v in control["coefficient_map"].items()},
                    expected,
                )
                self.assertEqual(control["leading_product"], p)
                self.assertEqual(control["leading_coefficient"], 1)

    def test_04_heldout_cauchy_binet_frequency_collision(self):
        value = [[1, 2, 3, 4], [2, -1, 1, 0]]
        nodes = [1, 2, 3, 6]
        expected = {2: Q(25), 3: Q(25), 6: Q(89), 12: Q(16), 18: Q(16)}
        self.assertEqual(M.cb_coefficients(value, nodes), expected)
        weighted = sum(
            coefficient / frequency**2 for frequency, coefficient in expected.items()
        )
        self.assertEqual(M.gram_determinant(value, nodes), weighted)

    def test_05_heldout_gaussian_against_permutation(self):
        matrices = (
            [[0, 1], [2, 3]],
            [[1, 2], [2, 4]],
            [[2, 1, 0], [3, -1, 4], [1, 2, 3]],
            [[1, 2, 3, 4], [0, 1, -1, 2], [2, 0, 1, 3], [1, 1, 0, 2]],
            [[Q(1, 2), Q(1, 3)], [Q(-2, 5), Q(7, 4)]],
        )
        for value in matrices:
            self.assertEqual(M.determinant(value), permutation_det(value))

    def test_06_smallest_rank_and_zero_column(self):
        self.assertEqual(M.determinant([[7]]), Q(7))
        self.assertEqual(
            M.cb_coefficients([[0, 1, -48]], [1, 2, 3]), {2: Q(1), 3: Q(2304)}
        )
        self.assertEqual(M.cb_coefficients([[0, 0]], [1, 2]), {})
        first = self.report["native_panels"][0]["determinants"]
        self.assertEqual([row["leading_product"] for row in first], [2, 2])
        self.assertEqual(first[1]["retained_nodes"], [2, 3])
        self.assertTrue(first[1]["W_n1_zero_column_checked"])

    def test_07_exceptional_top_tail_zero_retained(self):
        for d, r in ((10, 4), (20, 8)):
            panel = next(
                p
                for p in self.report["native_panels"]
                if (p["dimension"], p["residual"]) == (d, r)
            )
            p, n = math.factorial(d), d + 1
            rows = self.family.miller_basis(d, r)
            self.assertEqual(rows[-1][n], 0)
            for control in panel["determinants"]:
                self.assertNotIn(str(p * n // d), control["coefficient_map"])
                self.assertIn(str(p * n // (d - 1)), control["coefficient_map"])
                self.assertEqual(control["leading_product"], p)

    def test_08_native_coverage_and_full_basis_digests(self):
        panels = self.report["native_panels"]
        self.assertEqual(
            [(p["dimension"], p["residual"]) for p in panels], list(M.PANELS)
        )
        for panel in panels:
            rows = self.family.miller_basis(panel["dimension"], panel["residual"])
            raw = M.canonical([list(row) for row in rows]).encode()
            self.assertEqual(
                hashlib.sha256(raw).hexdigest(),
                panel["complete_basis_sha256_canonical_json"],
            )
        self.assertEqual(self.report["coverage"]["native_determinants"], 40)

    def test_09_phase_gamma_factor_and_conductor_ledger(self):
        for panel in self.report["native_panels"]:
            phase = panel["phase"]
            for row in phase["determinants"]:
                rank = row["rank"]
                arguments = row["gamma_arguments"]
                self.assertEqual(sum(a["multiplicity"] for a in arguments), 2 * rank)
                self.assertEqual(
                    [a["shift"] for a in arguments], [0, panel["weight"] - 1]
                )
                self.assertEqual(row["phase_T_log_T"], 2 * rank)
                self.assertEqual(row["phase_T"], -2 * rank)
                self.assertEqual(row["phase_T_log_2"], -2 * rank)
                self.assertEqual(row["phase_T_log_pi"], -2 * rank)
                self.assertEqual(row["phase_T_log_P"], -1)

    def test_10_equal_factorial_cancellation_not_minor_factorial(self):
        for d in (2, 3, 10, 20):
            phase = M.phase_ledger(d, 0)
            full, minor = phase["determinants"]
            self.assertEqual(full["P"], minor["P"])
            self.assertEqual(full["P"], math.factorial(d))
            self.assertNotEqual(minor["P"], math.factorial(d - 1))
            self.assertEqual(phase["quotient_difference"]["phase_T_log_P"], 0)
            self.assertEqual(
                phase["quotient_difference"]["positive_count_pi_multiplier"], 2
            )
            self.assertFalse(phase["logs_pi_gamma_or_phase_evaluated"])

    def test_11_strip_gamma_exponent_and_jensen_geometry(self):
        for rank in (1, 2, 20):
            for c in (Q(3), Q(7, 2), Q(8)):
                row = M.strip_ledger(rank, c)
                self.assertEqual(Q(row["F_left_power"]), rank * (4 * c - 2))
                self.assertEqual(Q(row["H_left_power"]), rank * (4 * c - 1))
                self.assertEqual(
                    Q(row["outer_Jensen_radius"]), 2 * Q(row["inner_Jensen_radius"])
                )
                self.assertEqual(Q(row["window_inside_gap"]), 4 * c - 2)
                self.assertGreater(Q(row["window_inside_gap"]), 0)
                self.assertFalse(row["actual_right_zero_free_abscissa_certified"])

    def test_12_non_native_exact_common_cancellation(self):
        node = (Q(1, 2), Q(3))
        result = M.signed_divisor_control({node: 7}, {node: 7}, 3)
        self.assertEqual(result["net_signed_count"], 0)
        self.assertEqual(result["net_absolute_count"], 0)
        self.assertFalse(result["actual_cusp_flag_divisor_sample"])

    def test_13_cutoff_inclusion_and_real_axis_exclusion(self):
        values = {(Q(0), Q(0)): 4, (Q(1), Q(-1)): 3, (Q(1, 3), Q(2)): 2}
        self.assertEqual(M.signed_divisor_control(values, {}, Q(3, 2))["full_count"], 0)
        self.assertEqual(M.signed_divisor_control(values, {}, 2)["full_count"], 2)
        self.assertEqual(M.signed_divisor_control(values, {}, 0)["full_count"], 0)

    def test_14_signed_count_not_monotone_or_unsigned(self):
        a = {(Q(1, 3), Q(1)): 1}
        b = {(Q(2, 3), Q(2)): 3}
        self.assertEqual(M.signed_divisor_control(a, b, 1)["net_signed_count"], 1)
        result = M.signed_divisor_control(a, b, 2)
        self.assertEqual(result["net_signed_count"], -2)
        self.assertEqual(result["net_absolute_count"], 4)

    def test_15_strict_types_and_bits(self):
        for value in (True, False, 1.0, "1", None):
            with self.assertRaises(ValueError):
                M.rational(value)
        with self.assertRaises(ValueError):
            M.rational(2**4096)
        with self.assertRaises(ValueError):
            M.rational(Q(1, 2**4096))
        for value in (True, 0, M.MAX_WORK + 1, 1.0):
            with self.assertRaises(ValueError):
                M.Budget(value)

    def test_16_matrix_shapes_and_domain_caps(self):
        for value in (
            [],
            [[]],
            [[1], [1, 2]],
            [[True]],
            [[1.0]],
            [[1] * 22],
            [[1]] * 21,
            "matrix",
        ):
            with self.assertRaises(ValueError):
                M.matrix(value)
        with self.assertRaises(ValueError):
            M.determinant([[1, 2]])
        with self.assertRaises(ValueError):
            M.cb_coefficients([[1], [2]], [1])

    def test_17_node_types_order_and_duplicates(self):
        for nodes in ([True, 2], [0, 2], [2, 1], [1, 1], [1, 22], [1.0, 2], [1]):
            with self.assertRaises(ValueError):
                M.cb_coefficients([[1, 2]], nodes)
        with self.assertRaises(ValueError):
            M.gram_determinant([[1]], [1], True)
        with self.assertRaises(ValueError):
            M.gram_determinant([[1]], [1], 5)

    def test_18_subsets_precharged_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "subset cap"):
            M.cb_coefficients([[1] * 21 for _ in range(10)], list(range(1, 22)))
        work = M.Budget(1)
        with self.assertRaisesRegex(ValueError, "before expansion"):
            M.cb_coefficients([[1, 2, 3]], [1, 2, 3], work)
        self.assertEqual(work.used, 0)
        with self.assertRaisesRegex(ValueError, "before expansion"):
            M.determinant([[1, 0], [0, 1]], M.Budget(1))

    def test_19_phase_and_strip_guards(self):
        for d, r in ((True, 0), (1, 0), (21, 0), (2, True), (2, 2)):
            with self.assertRaises(ValueError):
                M.phase_ledger(d, r)
        for rank, c in ((True, 3), (0, 3), (21, 3), (1, True), (1, 2), (1, 17)):
            with self.assertRaises(ValueError):
                M.strip_ledger(rank, c)

    def test_20_divisor_shape_type_resource_guards(self):
        node = (Q(1, 2), Q(3))
        for values in (
            {node: True},
            {node: 0},
            {node: 33},
            {(1,): 1},
            {(True, 2): 1},
            {(33, 2): 1},
            {(0, n): 1 for n in range(33)},
        ):
            with self.assertRaises(ValueError):
                M.signed_divisor_control(values, {}, 3)
        for height in (True, -1, 33, 2.0):
            with self.assertRaises(ValueError):
                M.signed_divisor_control({}, {}, height)

    def test_21_ten_source_and_four_artifact_hashes(self):
        self.assertEqual(len(M.BINDINGS), 10)
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for path, digest in self.report["artifact_sha256_lf"].items():
            raw = (
                (ROOT / path).read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            )
            self.assertEqual(hashlib.sha256(raw).hexdigest(), digest)
        self.assertEqual(
            M.canonical(self.report["frozen_sources"]), M.canonical(M.BINDINGS)
        )

    def test_22_manifest_field_and_bool_tampering(self):
        manifest = M.expected_manifest()
        manifest["external_context"][0]["remote_bytes_authenticated"] = 0
        with self.assertRaisesRegex(ValueError, "typed manifest"):
            M.authenticated_sources(manifest)
        manifest = M.expected_manifest()
        manifest["primitive_contract"]["count"] = "unsigned"
        with self.assertRaises(ValueError):
            M.authenticated_sources(manifest)
        manifest = M.expected_manifest()
        manifest["extra"] = True
        with self.assertRaises(ValueError):
            M.authenticated_sources(manifest)

    def test_23_manifest_copy_and_lf_stability(self):
        manifest = M.expected_manifest()
        manifest["frozen_sources"][0]["commit"] = "0" * 40
        manifest["external_context"][0]["role"] = "changed"
        self.assertNotEqual(M.BINDINGS[0]["commit"], "0" * 40)
        self.assertNotEqual(M.EXTERNAL[0]["role"], "changed")
        self.assertEqual(M.parse_json(M.MANIFEST.read_bytes()), M.expected_manifest())
        self.assertEqual(M.lf_sha(b"a\nb\n"), M.lf_sha(b"a\r\nb\r\n"))
        self.assertEqual(M.lf_sha(b"a\nb\n"), M.lf_sha(b"a\rb\r"))

    def test_24_primitive_identity_and_size_rejection(self):
        with (
            patch.object(M.subprocess, "check_output", side_effect=[b"1", b"x"]),
            self.assertRaisesRegex(ValueError, "primitive identity"),
        ):
            M.authenticated_sources()
        with patch.object(
            M.subprocess, "check_output", return_value=str(M.MAX_BYTES + 1).encode()
        ) as mocked:
            with self.assertRaisesRegex(ValueError, "primitive byte cap"):
                M.authenticated_sources()
            self.assertEqual(mocked.call_count, 1)

    def test_25_constructor_drift_rejected_before_execution(self):
        sources = dict(self.sources)
        path = (
            "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py"
        )
        sources[path] = b"raise RuntimeError('must never execute')\n"
        with self.assertRaisesRegex(ValueError, "constructor identity"):
            M.frozen_family(sources)

    def test_26_json_duplicates_nonfinite_floats(self):
        for raw in (
            b'{"x":1,"x":2}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b'{"x":-Infinity}',
            b'{"x":1.0}',
            b'{"x":1e2}',
            b"{",
        ):
            with self.assertRaises(ValueError):
                M.parse_json(raw)

    def test_27_json_structural_caps(self):
        for value in ([0] * 1025, {"x": "a" * 4097}, {1: "key"}, 2**4096):
            with self.assertRaises(ValueError):
                M.canonical(value)
        with self.assertRaises(ValueError):
            M.parse_json(b"[" * 30 + b"0" + b"]" * 30)
        with self.assertRaises(ValueError):
            M.parse_json(b" " * (M.MAX_BYTES + 1))

    def test_28_digest_tamper(self):
        report = copy.deepcopy(self.report)
        report["payload_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "payload digest"):
            M.validate_report(report)
        with self.assertRaises(ValueError):
            M.seal(report)

    def test_29_resealed_semantic_tamper(self):
        variants = []
        for key, value in (
            ("schema", "other"),
            ("arithmetic_class", "EXACT"),
            ("rounding_contract", "floating"),
            ("status", "APPROVED"),
        ):
            payload = copy.deepcopy(self.report)
            payload.pop("payload_sha256")
            payload[key] = value
            variants.append(payload)
        for section, key, value in (
            ("caps", "work", True),
            ("scope", "actual_period_phase_or_zero_samples", False),
            ("scope", "Q_count_assumed_monotone", True),
        ):
            payload = copy.deepcopy(self.report)
            payload.pop("payload_sha256")
            payload[section][key] = value
            variants.append(payload)
        with patch.object(M, "build_report", return_value=self.report):
            for payload in variants:
                with self.assertRaisesRegex(ValueError, "typed reconstruction"):
                    M.validate_report(M.seal(payload))

    def test_30_arithmetic_and_cap_coverage(self):
        self.assertEqual(self.report["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.report["arithmetic_components"],
            ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        )
        self.assertIn("no rounding", self.report["rounding_contract"])
        self.assertIn("symbolic", self.report["rounding_contract"])
        coverage = self.report["coverage"]
        self.assertLessEqual(coverage["charged_work"], M.MAX_WORK)
        self.assertLessEqual(coverage["charged_frozen_family_work"], M.FAMILY_WORK)
        self.assertEqual(coverage["complete_Miller_constructions"], 40)
        self.assertIs(coverage["frozen_family_report_rerun"], False)

    def test_31_scope_firewalls(self):
        scope = self.report["scope"]
        for key in (
            "real_endpoint_poles_in_positive_count",
            "Q_count_assumed_monotone",
            "unsigned_Q_count_given_same_asymptotic",
            "critical_line_density_or_RH",
            "uncancelled_or_finitely_many_poles_asserted",
            "uniform_in_weight_or_effective_error_constant",
            "numerical_analytic_proof_certificate",
            "new_abstract_theory_or_novelty_claim",
        ):
            self.assertIs(scope[key], False)
        self.assertEqual(scope["actual_period_phase_or_zero_samples"], 0)
        self.assertIn("<=T", scope["height_cutoff"])

    def test_32_no_assert_float_or_numeric_phase(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(node, ast.Constant) and type(node.value) is float
                for node in ast.walk(tree)
            )
        )
        prohibited = {"exp", "log", "gamma", "lgamma", "sin", "cos", "sqrt", "phase"}
        self.assertFalse(
            any(
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr in prohibited
                for node in ast.walk(tree)
            )
        )


if __name__ == "__main__":
    unittest.main()
