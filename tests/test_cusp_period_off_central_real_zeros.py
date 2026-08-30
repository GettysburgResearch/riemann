"""Independent finite controls and fail-closed tests, not a period zero census."""

import ast
import copy
import hashlib
import importlib.util
import math
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT / "research/l-families/atlas/generalized/cusp_period_off_central_real_zeros.py"
)
SPEC = importlib.util.spec_from_file_location("cusp_period_real_zero_tested", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def multiply(a, b, order):
    return [sum(a[j] * b[n - j] for j in range(n + 1)) for n in range(order + 1)]


def binomial_power(one_plus, exponent, order):
    tail = [0] + list(one_plus[1:])
    power, out = [1] + [0] * order, [1] + [0] * order
    for j in range(1, min(exponent, order) + 1):
        power = multiply(power, tail, order)
        out = [x + math.comb(exponent, j) * y for x, y in zip(out, power)]
    return out


class CuspPeriodRealZeroTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = M.authenticated_sources()
        cls.family = M.frozen_family(cls.sources)
        cls.report = M.build_report()

    def test_01_full_fixture_reconstruction(self):
        fixture = M.parse_json(M.FIXTURE.read_bytes())
        self.assertEqual(M.canonical(fixture), M.canonical(self.report))
        M.validate_report(fixture)

    def test_02_native_primitives_three_formulas(self):
        delta, e4 = M.primitives(8, M.Budget())
        self.assertEqual(delta[:6], (0, 1, -24, 252, -1472, 4830))
        self.assertEqual(e4[:5], (1, 240, 2160, 6720, 17520))
        frozen_delta, frozen_e4, _ = self.family.primitives(8, self.family.Budget())
        self.assertEqual((delta, e4), (frozen_delta, frozen_e4))
        product = [1] + [0] * 7
        for n in range(1, 8):
            factor = [0] * 8
            for j in range(8 // n + 1):
                if n * j < 8:
                    factor[n * j] = (-1) ** j * math.comb(24, j)
            product = multiply(product, factor, 7)
        self.assertEqual(list(delta), [0] + product)

    def test_03_all_prefixes_independent_binomial_expansion(self):
        for row in self.report["native_prefixes"]:
            order, j, exponent = row["q_order"], row["delta_power"], row["E4_power"]
            delta, e4, _ = self.family.primitives(order, self.family.Budget())
            dp = [1] + [0] * order
            for _ in range(j):
                dp = multiply(dp, delta, order)
            expected = multiply(dp, binomial_power(e4, exponent, order), order)
            self.assertEqual(row["q_prefix"], expected)

    def test_04_leading_three_native_coefficients(self):
        for row in self.report["native_prefixes"]:
            j, m, q = row["delta_power"], row["E4_power"], row["q_prefix"]
            self.assertEqual(q[:j], [0] * j)
            self.assertEqual(q[j], 1)
            self.assertEqual(q[j + 1], -24 * j + 240 * m)
            second = (
                288 * j * j - 36 * j + 2160 * m + 57600 * math.comb(m, 2) - 5760 * j * m
            )
            self.assertEqual(q[j + 2], second)

    def test_05_g1_not_Miller_fd_and_exact_W(self):
        for row in self.report["native_prefixes"]:
            self.assertIs(row["is_in_W"], row["delta_power"] >= 2)
            self.assertEqual(row["first_coefficient"], int(row["delta_power"] == 1))
            self.assertIs(
                row["Miller_f_d_identification"], row["delta_power"] == row["dimension"]
            )
        f = self.family.miller_basis(3, 0)
        h = M.native_prefix(3, 1, 5, M.Budget())["q_prefix"]
        self.assertNotEqual(h, list(f[-1]))
        self.assertEqual(f[-1][:3], (0, 0, 0))
        self.assertEqual(h[1], 1)

    def test_06_positive_Taylor_reductions(self):
        for row in self.report["constant_controls"]["positive_Taylor_lower_sums"]:
            exact = sum(
                (Q(row["x"] ** n, math.factorial(n)) for n in range(row["degree"] + 1)),
                Q(0),
            )
            self.assertEqual(Q(row["sum"]), exact)
            self.assertGreater(exact, row["exceeds"])
        self.assertEqual(M.taylor_lower(0, 0, M.Budget()), 1)

    def test_07_fourth_power_sum_generating_polynomial(self):
        coefficients = [n**4 for n in range(13)]
        denominator = [(-1) ** j * math.comb(5, j) for j in range(6)] + [0] * 7
        product = multiply(coefficients, denominator, 12)
        self.assertEqual(product, [0, 1, 11, 11, 1] + [0] * 8)

    def test_08_exact_radial_majorants_and_zero_endpoint(self):
        row = M.envelope(Q(1, 100))
        self.assertEqual(Q(row["E4_minus_one_bound"]), Q(2962936000, 1056655611))
        self.assertLess(Q(row["E4_cofactor"]), 2)
        self.assertEqual(Q(row["Delta_over_q_lower"]), Q(25, 33))
        self.assertEqual(Q(row["E_star_Fourier_tail_bound"]), Q(4, 99))
        zero = M.envelope(0)
        self.assertEqual(Q(zero["E4_cofactor"]), 1)
        self.assertEqual(Q(zero["Delta_over_q_lower"]), 1)
        self.assertEqual(Q(zero["E_star_Fourier_tail_bound"]), 0)

    def test_09_compact_and_cusp_reserves(self):
        controls = self.report["constant_controls"]
        self.assertEqual(controls["compact_E_star_absolute_bound"], 6 * (4 + 3) + 1)
        self.assertLess(2 * 43, controls["compact_mass_upper_coefficient"])
        self.assertEqual(32 * 2, controls["compact_mass_base"])
        self.assertGreater(5 * Q(1, 2) - 1, 1)
        self.assertGreater(Q(6144, 16), 32)
        self.assertLess(Q(controls["Bernoulli_error_at_k24_upper"]), Q(1, 2))

    def test_10_positive_mass_algebra_no_transcendental_evaluation(self):
        c = self.report["constant_controls"]
        self.assertEqual(Q(c["positive_slab_coefficient"]), Q(1, 8))
        self.assertEqual(Q(16**2, 8), c["positive_mass_elementary_coefficient"])
        self.assertEqual(16 * 3, c["positive_mass_elementary_base_divisor"])
        self.assertEqual(48 * 64, c["threshold_base_divisor"])
        self.assertEqual(Q(100, 32), Q(25, 8))
        self.assertEqual(c["positive_slab_native_measure_power"], "k-2")

    def test_11_threshold_base_exact_exponent_comparison(self):
        c = self.report["constant_controls"]
        self.assertEqual(c["threshold_k"], 12 * c["threshold_d"])
        self.assertEqual(c["threshold_d"], 512)
        self.assertLess(3**16, 2**26)
        self.assertLess(6144**2, 2**26)
        self.assertLess(Q(25, 8), 2**2)
        self.assertEqual(c["combined_required_power2_exponent"], 2 + 26 + 26)
        self.assertGreater(
            c["available_power2_exponent"], c["combined_required_power2_exponent"]
        )

    def test_12_induction_polynomial_identity_not_finite_coverage_claim(self):
        for k in (3, 7, 27, 6144, 6145, 12288):
            row = M.threshold_row(k)
            self.assertEqual(row["monotonicity_gap"], 2 * k**2 - (k + 1) ** 2)
            self.assertEqual(
                (k + 1) ** 2 - 2 * (k + 1) - 1 - row["monotonicity_gap"], 2 * k - 1
            )
            self.assertGreater(Q(row["ratio_for_2_power_over_square"]), 1)
        self.assertEqual(
            self.report["constant_controls"][
                "monotonicity_polynomial_coefficients_low_first"
            ],
            [-1, -2, 1],
        )
        self.assertTrue(
            self.report["constant_controls"][
                "all_integer_k_threshold_proved_in_note_not_enumerated"
            ]
        )

    def test_13_Poisson_signed_pair_enumeration(self):
        for row in self.report["Poisson_sign_pair_controls"]:
            n = row["n"]
            pairs = [
                (m, ell)
                for m in range(-n, n + 1)
                for ell in range(-n, n + 1)
                if m * ell == n
            ]
            self.assertEqual(len(pairs), 2 * row["tau"])
            self.assertEqual(
                2 * len(pairs), row["cosine_K0_coefficient_without_sqrt_y"]
            )
        self.assertEqual(
            M.poisson_control(1)["cosine_K0_coefficient_without_sqrt_y"], 4
        )
        self.assertEqual(M.poisson_control(16)["tau"], 5)

    def test_14_native_coverage_caps_do_not_bound_theorem(self):
        self.assertEqual(
            [
                (r["dimension"], r["delta_power"])
                for r in self.report["native_prefixes"]
            ],
            list(M.PANELS),
        )
        self.assertEqual(self.report["coverage"]["native_prefixes"], 10)
        self.assertFalse(
            self.report["coverage"]["complete_high_weight_Miller_basis_constructed"]
        )
        self.assertIn(
            "d>=512", self.report["scope"]["actual_full_period_zero_by_written_proof"]
        )
        self.assertIn("each fixed", self.report["scope"]["W_witness_threshold"])

    def test_15_strict_rational_and_integer_bits(self):
        for value in (True, False, 1.0, "1", None):
            with self.assertRaises(ValueError):
                M.rational(value)
        for value in (2**4096, Q(1, 2**4096)):
            with self.assertRaises(ValueError):
                M.rational(value)
        self.assertEqual(M.rational(2**4095), 2**4095)
        for value in (True, 0, M.MAX_WORK + 1, 1.0):
            with self.assertRaises(ValueError):
                M.Budget(value)

    def test_16_prefix_domain_and_shape_guards(self):
        for d, j, order in (
            (True, 1, 8),
            (1, 1, 8),
            (1025, 1, 8),
            (2, True, 8),
            (2, 0, 8),
            (2, 3, 8),
            (9, 9, 8),
            (2, 1, 3),
            (2, 1, 9),
            (2, 1, True),
        ):
            with self.assertRaises(ValueError):
                M.native_prefix(d, j, order, M.Budget())
        for row in ([1], [True] * 5, [1.0] * 5, [2**4096] * 5, "11111"):
            with self.assertRaises(ValueError):
                M.polynomial(row, 4)

    def test_17_power_and_primitive_work_guards(self):
        row = [1, 2, 0, 0, 0]
        for exponent in (True, -1, 3073, 1.0):
            with self.assertRaises(ValueError):
                M.qpower(row, exponent, 4, M.Budget())
        self.assertEqual(M.qpower(row, 0, 4, M.Budget()), (1, 0, 0, 0, 0))
        work = M.Budget(1)
        with self.assertRaisesRegex(ValueError, "before expansion"):
            M.primitives(8, work)
        self.assertEqual(work.used, 0)
        with self.assertRaises(ValueError):
            M.qmul(row, row, 4, None)

    def test_18_taylor_and_envelope_guards(self):
        for x, degree in ((True, 4), (-1, 4), (9, 4), (3, True), (3, -1), (3, 13)):
            with self.assertRaises(ValueError):
                M.taylor_lower(x, degree, M.Budget())
        for r in (True, -1, Q(1, 99), 0.0):
            with self.assertRaises(ValueError):
                M.envelope(r)
        with self.assertRaisesRegex(ValueError, "before expansion"):
            M.taylor_lower(3, 12, M.Budget(1))

    def test_19_threshold_and_Poisson_caps(self):
        for k in (True, 2, 12289, 3.0):
            with self.assertRaises(ValueError):
                M.threshold_row(k)
        for n in (True, 0, 33, 1.0):
            with self.assertRaises(ValueError):
                M.poisson_control(n)
        with self.assertRaises(ValueError):
            M.constant_controls(None)

    def test_20_seven_source_four_artifact_hashes(self):
        self.assertEqual(len(M.BINDINGS), 7)
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for path, digest in self.report["artifact_sha256_lf"].items():
            raw = (
                (ROOT / path).read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            )
            self.assertEqual(hashlib.sha256(raw).hexdigest(), digest)
        self.assertEqual(
            M.canonical(self.report["frozen_sources"]), M.canonical(M.BINDINGS)
        )

    def test_21_manifest_type_and_semantic_tamper(self):
        for key, value in (
            ("normalization", "coefficient2"),
            ("flag_boundary", "uncancelled"),
            ("measure", "dy"),
        ):
            manifest = M.expected_manifest()
            manifest["primitive_contract"][key] = value
            with self.assertRaisesRegex(ValueError, "typed manifest"):
                M.authenticated_sources(manifest)
        manifest = M.expected_manifest()
        manifest["external_context"][0]["remote_bytes_authenticated"] = 0
        with self.assertRaises(ValueError):
            M.authenticated_sources(manifest)

    def test_22_manifest_copy_and_newlines(self):
        manifest = M.expected_manifest()
        manifest["frozen_sources"][0]["commit"] = "0" * 40
        manifest["external_context"][0]["role"] = "different"
        self.assertNotEqual(M.BINDINGS[0]["commit"], "0" * 40)
        self.assertNotEqual(M.EXTERNAL[0]["role"], "different")
        self.assertEqual(M.parse_json(M.MANIFEST.read_bytes()), M.expected_manifest())
        self.assertEqual(M.lf_sha(b"a\nb\n"), M.lf_sha(b"a\r\nb\r\n"))
        self.assertEqual(M.lf_sha(b"a\nb\n"), M.lf_sha(b"a\rb\r"))

    def test_23_source_identity_size_and_constructor_guards(self):
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
        sources = dict(self.sources)
        sources[
            "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py"
        ] = b"raise RuntimeError('never run')\n"
        with self.assertRaisesRegex(ValueError, "constructor identity"):
            M.frozen_family(sources)

    def test_24_json_duplicate_nonfinite_and_float_guards(self):
        for raw in (
            b'{"x":1,"x":2}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b'{"x":-Infinity}',
            b'{"x":1.0}',
            b'{"x":1e2}',
            b"{",
            b"\xff",
        ):
            with self.assertRaises(ValueError):
                M.parse_json(raw)

    def test_25_json_structural_and_byte_caps(self):
        for value in ([0] * 1025, {"x": "a" * 4097}, {1: "key"}, 2**4096):
            with self.assertRaises(ValueError):
                M.canonical(value)
        for raw in (b"[" * 30 + b"0" + b"]" * 30, b" " * (M.MAX_BYTES + 1)):
            with self.assertRaises(ValueError):
                M.parse_json(raw)
        with self.assertRaises(ValueError):
            M.normalized("not bytes")
        with self.assertRaisesRegex(ValueError, "total JSON node cap"):
            M.canonical([[0] * 100 for _ in range(201)])
        with self.assertRaisesRegex(ValueError, "total JSON text byte cap"):
            M.canonical(["a" * 4096] * 489)

    def test_26_digest_and_resealing_guards(self):
        report = copy.deepcopy(self.report)
        report["payload_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "payload digest"):
            M.validate_report(report)
        with self.assertRaises(ValueError):
            M.seal(report)
        with self.assertRaises(ValueError):
            M.validate_report([])

    def test_27_resealed_exact_constant_and_prefix_tamper(self):
        payloads = []
        for key, value in (
            ("threshold_d", 511),
            ("threshold_k", 6143),
            ("positive_slab_coefficient", "1/4"),
            ("positive_slab_native_measure_power", "k"),
        ):
            payload = copy.deepcopy(self.report)
            payload.pop("payload_sha256")
            payload["constant_controls"][key] = value
            payloads.append(payload)
        payload = copy.deepcopy(self.report)
        payload.pop("payload_sha256")
        payload["native_prefixes"][0]["q_prefix"][1] = 0
        payloads.append(payload)
        payload = copy.deepcopy(self.report)
        payload.pop("payload_sha256")
        payload["Poisson_sign_pair_controls"][0][
            "cosine_K0_coefficient_without_sqrt_y"
        ] = 2
        payloads.append(payload)
        with patch.object(M, "build_report", return_value=self.report):
            for payload in payloads:
                with self.assertRaisesRegex(ValueError, "typed reconstruction"):
                    M.validate_report(M.seal(payload))

    def test_28_resealed_schema_taxonomy_artifact_and_type_tamper(self):
        payloads = []
        for key, value in (
            ("schema", "other"),
            ("status", "APPROVED"),
            ("arithmetic_class", "EXACT"),
            ("rounding_contract", "floating"),
        ):
            payload = copy.deepcopy(self.report)
            payload.pop("payload_sha256")
            payload[key] = value
            payloads.append(payload)
        for section, key, value in (
            ("caps", "dimension", True),
            ("scope", "numeric_period_or_zero_samples", False),
            ("scope", "Q_uncancelled_zero_or_pole_asserted", True),
        ):
            payload = copy.deepcopy(self.report)
            payload.pop("payload_sha256")
            payload[section][key] = value
            payloads.append(payload)
        payload = copy.deepcopy(self.report)
        payload.pop("payload_sha256")
        path = next(iter(payload["artifact_sha256_lf"]))
        payload["artifact_sha256_lf"][path] = "0" * 64
        payloads.append(payload)
        with patch.object(M, "build_report", return_value=self.report):
            for payload in payloads:
                with self.assertRaisesRegex(ValueError, "typed reconstruction"):
                    M.validate_report(M.seal(payload))

    def test_29_canonical_arithmetic_and_resource_report(self):
        self.assertEqual(self.report["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.report["arithmetic_components"],
            ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        )
        self.assertIn("no rounding", self.report["rounding_contract"])
        self.assertIn("symbolic", self.report["rounding_contract"])
        self.assertLessEqual(self.report["coverage"]["charged_work"], M.MAX_WORK)
        self.assertLessEqual(
            self.report["coverage"]["charged_frozen_primitive_work"], M.FAMILY_WORK
        )

    def test_30_scope_firewalls(self):
        for key in (
            "analytic_continuation_inertia_integrals_machine_certified",
            "Q_uncancelled_zero_or_pole_asserted",
            "relative_inertia_gap_asserted",
            "W_negative_definite_at_center_assumed",
            "simplicity_uniqueness_or_optimal_onset",
            "zeta_RH_counterexample",
            "new_automorphic_family_or_exhaustive_novelty",
            "all_weights_all_minors_or_general_structures",
            "finite_controls_prove_analytic_limits",
        ):
            self.assertIs(self.report["scope"][key], False)
        self.assertEqual(self.report["scope"]["numeric_period_or_zero_samples"], 0)
        self.assertTrue(self.report["scope"]["h_d_is_CF_g1_not_Miller_f_d"])

    def test_31_no_assert_float_or_transcendental_sampling(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(node, ast.Constant) and type(node.value) is float
                for node in ast.walk(tree)
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
            "eig",
            "eigvals",
            "quad",
        }
        self.assertFalse(
            any(
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr in prohibited
                for node in ast.walk(tree)
            )
        )

    def test_32_full_note_preserves_analytic_and_flag_contract(self):
        note = M.NOTE.read_text(encoding="utf-8")
        for token in (
            "h_d is CF1's g_1, NOT Miller f_d",
            "largest eigenvalue is continuous",
            "factor-two",
            "relative positive-inertia gap",
            "CZ18",
            "EVERY integer k>=6144",
        ):
            self.assertIn(token, note)
        self.assertEqual(M.BASE, "24bfc73fc9aa3ba115902340affa8727dfa18970")
        self.assertEqual(len(self.report["Poisson_sign_pair_controls"]), 32)


if __name__ == "__main__":
    unittest.main()
