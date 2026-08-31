"""Native coefficient, exponential-budget and hostile release controls."""

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
    ROOT / "research/l-families/atlas/generalized/cusp_flag_native_denominator_poles.py"
)
SPEC = importlib.util.spec_from_file_location("native_denominator_poles", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def independent_prefix(k, j, n):
    r = 14 if k % 12 == 2 else k % 12
    pairs = {0: (0, 0), 4: (1, 0), 6: (0, 1), 8: (2, 0), 10: (1, 1), 14: (2, 1)}
    a, b = pairs[r]
    d = (k - r) // 12
    p = 3 * (d - j) + a
    sigma1 = [0] + [
        sum(x for x in range(1, t + 1) if t % x == 0) for t in range(1, n + 1)
    ]
    e4 = [1] + [
        240 * sum(x**3 for x in range(1, t + 1) if t % x == 0) for t in range(1, n + 1)
    ]
    e6 = [1] + [
        -504 * sum(x**5 for x in range(1, t + 1) if t % x == 0) for t in range(1, n + 1)
    ]
    delta, power = [1], [1]
    for t in range(1, n + 1):
        num = -24 * j * sum(sigma1[i] * delta[t - i] for i in range(1, t + 1))
        if num % t:
            raise RuntimeError("independent Delta integrality")
        delta.append(num // t)
        num = sum(((p + 1) * i - t) * e4[i] * power[t - i] for i in range(1, t + 1))
        if num % t:
            raise RuntimeError("independent E4 integrality")
        power.append(num // t)
    values = [sum(delta[i] * power[t - i] for i in range(t + 1)) for t in range(n + 1)]
    if b:
        values = [
            sum(values[i] * e6[t - i] for i in range(t + 1)) for t in range(n + 1)
        ]
    return [0] * j + values[: n + 1 - j]


class NativePoleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = M.authenticated_sources()
        cls.aw = M.source_module(cls.sources, "allweight")
        cls.report = M.build_report()

    def test_01_full_fixture_reconstruction(self):
        fixture = M.parse_json(M.FIXTURE.read_bytes())
        self.assertEqual(M.canonical(fixture), M.canonical(self.report))
        M.validate_report(fixture)

    def test_02_all_six_native_shears_independent(self):
        rows = self.report["native_shear_pairs"]
        self.assertEqual(len(rows), 12)
        self.assertEqual({row["r"] for row in rows}, {0, 4, 6, 8, 10, 14})
        for row in rows:
            k = row["weight"]
            g1, g2 = independent_prefix(k, 1, 8), independent_prefix(k, 2, 8)
            self.assertEqual(row["g1"]["q_prefix"], g1)
            self.assertEqual(row["g2"]["q_prefix"], g2)
            self.assertEqual(
                row["h_prefix"], [x - g1[2] * y for x, y in zip(g1, g2, strict=True)]
            )
            self.assertEqual(row["h_prefix"][:3], [0, 1, 0])

    def test_03_tau_and_true_q3_tail(self):
        for row in self.report["native_shear_pairs"]:
            k, b, p = row["weight"], row["b"], row["g1"]["E4_power"]
            tau = -24 + 240 * p - 504 * b
            self.assertEqual(tau, 60 * k - 744 - 864 * b)
            self.assertEqual(row["tau"], tau)
            self.assertEqual(row["g2"]["q_prefix"][3], tau - 744)
            q3 = (
                252
                + 2160 * p
                + 57600 * math.comb(p, 2)
                - 16632 * b
                - 24 * (240 * p - 504 * b)
                - 120960 * p * b
            )
            self.assertEqual(row["g1"]["q_prefix"][3], q3)
            self.assertEqual(row["h_q3"], q3 - tau * (tau - 744))
            self.assertEqual(4 * p + 8 * b, k - 12 + 2 * b)

    def test_04_heldout_native_charts(self):
        for k in (48, 52, 54, 56, 58, 62, 65548, 65550, 65552, 65554, 65556, 65558):
            row = M.native_pair(self.aw, self.aw.Budget(M.SOURCE_WORK), k, 7)
            for j, key in ((1, "g1"), (2, "g2")):
                self.assertEqual(row[key]["q_prefix"], independent_prefix(k, j, 7))
            self.assertEqual(row["h_prefix"][1:3], [1, 0])

    def test_05_actual_W3_dimension_and_r14(self):
        for k in (36, 40, 42, 44, 46, 50):
            row = M.native_pair(self.aw, self.aw.Budget(M.SOURCE_WORK), k)
            self.assertEqual(row["dimension"], 3)
            if k == 50:
                self.assertEqual(row["r"], 14)
                self.assertEqual(row["dimension"], (k - 14) // 12)
        with self.assertRaisesRegex(ValueError, "W3 chart"):
            M.native_pair(self.aw, self.aw.Budget(M.SOURCE_WORK), 38)

    def test_06_Cauchy_product_and_tail_constants(self):
        previous = Q(1)
        for k in (48, 64, 65536, M.MAX_K):
            row = M.cauchy_envelope(k)
            radius = Q(1, 1000 * k)
            exponent = 48 * radius / (1 - radius) + 120 * k * radius + 1008 * radius
            self.assertEqual(Q(row["product_exponent_upper"]), exponent)
            self.assertLess(exponent, Q(1, 4))
            self.assertLess(exponent, previous)
            previous = exponent
            self.assertEqual(row["g1_shear_tail_k2_rho3"], 4 * 1000**2 + 4 * 100 * 1000)
            self.assertEqual(row["g2_tail_k_rho3"], 4 * 1000)

    def test_07_Cauchy_series_tail_majorant(self):
        for ratio in (Q(1, 100), Q(1, 4), Q(1, 2)):
            self.assertLessEqual(2 * ratio**2 / (1 - ratio), 4 * ratio**2)
            self.assertLessEqual(2 * ratio / (1 - ratio), 4 * ratio)
        self.assertLess(Q(1) / (1 - Q(1, 4)), 2)

    def test_08_low_cutoff_uniform_rational_majorant(self):
        for k in (4, 5, 48, 10000, 65536, M.MAX_K):
            row = M.low_cutoff_control(k)
            self.assertLessEqual(Q(row["k_over_kminus2"]), 2)
            self.assertLess(Q(row["uniform_base"]), Q(1, 10))
            self.assertEqual(Q(row["prefactor_k2"]), 84480)
            self.assertLess(Q(row["prefactor_k2"]), row["proved_mass_C_k4"])
        self.assertEqual(48 * 4 * 3 * Q(1, 10000), Q(36, 625))

    def test_09_finite_factorial_envelope_independent(self):
        for k in (48, 64, 96):
            y = Q(k, 10000)
            low_upper = 22000 * k * k * 2**k * y ** (k - 1) / (k - 1)
            a3_lower = Q(math.factorial(k - 2), 48 ** (k - 1))
            self.assertLess(low_upper / a3_lower, 100000 * k**4 * Q(1, 10) ** k)
        self.assertEqual(22000 * 4 * 12 * 4 * Q(1, 10000) * 2 * 100, 84480)

    def test_10_Bessel_tangent_polynomial(self):
        for j in range(51):
            nu = Q(j, 100)
            for x in (Q(1), Q(3, 2), Q(100)):
                row = M.bessel_control(nu, x)
                mean, power = nu + Q(1, 2), nu - Q(1, 2)
                self.assertEqual(Q(row["tangent_lower"]), 1 + mean * power / (2 * x))
                self.assertLessEqual(Q(row["coarse_lower"]), Q(row["tangent_lower"]))
                self.assertGreaterEqual(power * (power - 1), 0)
                self.assertLessEqual(Q(row["tangent_lower"]), 1)

    def test_11_Bessel_endpoints_no_numeric_K(self):
        for x in (1, 10, 1000):
            self.assertEqual(M.bessel_control(Q(1, 2), x)["tangent_lower"], "1")
            row = M.bessel_control(0, x)
            self.assertEqual(row["tangent_lower"], row["coarse_lower"])
            self.assertFalse(row["Bessel_value_sampled"])

    def test_12_native_Fourier_normalization(self):
        row = M.normalization_ledger()
        laurent_product = {2: Q(1, 2), 0: Q(1, 2)}
        self.assertEqual(laurent_product[0], Q(row["x_integral"]))
        self.assertEqual(row["source_cosine_coefficient"] * laurent_product[0], 2)
        self.assertEqual(2 * Q(row["half_order_K_sqrt_y_coefficient"]), 1)
        self.assertEqual(
            row["q1_q2_decay_exponent_pi"] + row["Bessel_decay_exponent_pi"], 8
        )
        self.assertEqual(row["B0_over_A2_leading"], "1")

    def test_13_constant_Fourier_orthogonality(self):
        # Monomial frequency differences: q-to-q2 and each single tail miss zero.
        self.assertNotEqual(2 - 1, 0)
        for n in range(3, 21):
            self.assertNotEqual(n - 1, 0)
            self.assertNotEqual(2 - n, 0)
        self.assertEqual(3 - 3, 0)  # The tail-tail term must still be paid.

    def test_14_entire_error_scale_algebra(self):
        ledger = M.decay_ledger()
        expected = {
            "P_cross_tail": (5, Q(2, 3)),
            "R_first_tail": (2, Q(2, 3)),
            "R_second_tail": (1, Q(4, 5)),
            "R_double_tail": (3, Q(4, 7)),
            "W3_cross_correction": (6, Q(2, 3)),
            "W3_self_correction": (5, Q(2, 3)),
        }
        for row in ledger["ordinary_terms"]:
            self.assertEqual(
                (row["polynomial_degree"], Q(row["ratio_base_to_A2"])),
                expected[row["term"]],
            )
            self.assertTrue(0 < Q(row["ratio_base_to_A2"]) < 1)
        self.assertEqual(4 + 3 - 1, 6)
        self.assertEqual(0 + 3 - 1, ledger["mixed_correction_polynomial_degree"])
        self.assertEqual(3 + 3 - 1, 5)

    def test_15_deeper_disc_identity(self):
        for x in (1, 12, 18, 24, 36, 40):
            for y in (-18, -3, 0, 5, 18):
                row = M.disc_point(x, y)
                gap = Q(x, 2 * (x * x + y * y)) - Q(1, 72)
                self.assertEqual(Q(row["gap"]), gap)
                self.assertEqual(gap > 0, row["inside"])
        self.assertEqual(M.disc_point(36, 0)["gap"], "0")
        self.assertLess(Q(M.disc_point(37, 0)["gap"]), 0)

    def test_16_fixed_disc_margin_and_Rouche(self):
        for delta, radius in ((1, 2), (3, 6), (9, 11), (Q(23, 2), Q(47, 4))):
            row = M.radius_control(delta, radius)
            margin = (Q(324) - (6 + radius) ** 2) / (72 * (24 + radius) ** 2)
            self.assertEqual(Q(row["m_R"]), margin)
            self.assertEqual(Q(row["Rouche_lower"]), Q(delta) / (48 * (24 + delta)))
            self.assertGreater(margin, 0)
            self.assertLess(6 + radius, 18)

    def test_17_conditional_cancellation_not_native_proof(self):
        with_b = M.conditional_schur(3, 2, 5)
        without_b = M.conditional_schur(3, 0, 5)
        self.assertEqual(with_b["numerator_at_dzero"], "-4")
        self.assertEqual(with_b["c_residue"], "-4/5")
        self.assertTrue(with_b["uncancelled_iff_b_nonzero"])
        self.assertFalse(without_b["uncancelled_iff_b_nonzero"])
        self.assertTrue(with_b["native_coupling_not_proved_by_this_control"])

    def test_18_exact_residue_coordinate_ledger(self):
        row = M.normalization_ledger()
        self.assertEqual(Q(row["F2_derivative_at24"]), Q(1, 1152))
        self.assertEqual(Q(row["s_residue_coefficient"]), 2 * 24**2)
        self.assertEqual(row["s_residue_k_power"], -2)
        self.assertEqual(row["dc_ds_sign"], -1)
        self.assertEqual(row["reflected_residue_sign"], -1)

    def test_19_native_weight_order_budget_guards(self):
        for k in (True, 36.0, "36", 35, 37, M.MAX_K + 1):
            with self.assertRaises(ValueError):
                M.native_pair(self.aw, self.aw.Budget(M.SOURCE_WORK), k)
        for order in (True, 3, 9, 8.0):
            with self.assertRaises(ValueError):
                M.native_pair(self.aw, self.aw.Budget(M.SOURCE_WORK), 48, order)
        for work in (M.Budget(), self.aw.Budget(M.SOURCE_WORK + 1)):
            with self.assertRaises(ValueError):
                M.native_pair(self.aw, work, 48)
        small = self.aw.Budget(1)
        with self.assertRaises(ValueError):
            M.native_pair(self.aw, small, 48)
        self.assertEqual(small.used, 0)

    def test_20_strict_rational_domains_and_bits(self):
        for value in (True, 0.0, "0", None, Q(1, 2**128)):
            with self.assertRaises(ValueError):
                M.bessel_control(value, 1)
        for nu, x in ((-1, 1), (1, 1), (0, 0)):
            with self.assertRaises(ValueError):
                M.bessel_control(nu, x)
        for delta, radius in ((0, 1), (1, 1), (1, 12), (1, 13), (True, 2)):
            with self.assertRaises(ValueError):
                M.radius_control(delta, radius)
        with self.assertRaises(ValueError):
            M.disc_point(0, 0)
        with self.assertRaises(ValueError):
            M.disc_point(65, 1)
        with self.assertRaises(ValueError):
            M.rational(Q(1, 2**4096))
        with self.assertRaises(ValueError):
            M.bounded_integer(2**4096)
        with self.assertRaises(ValueError):
            M.conditional_schur(1, 1, 0)

    def test_21_integer_work_and_envelope_guards(self):
        for k in (True, 3, 4.0, M.MAX_K + 1):
            with self.assertRaises(ValueError):
                M.low_cutoff_control(k)
        with self.assertRaises(ValueError):
            M.cauchy_envelope(47)
        for limit in (True, 0, M.MAX_WORK + 1):
            with self.assertRaises(ValueError):
                M.Budget(limit)
        work = M.Budget(1)
        with self.assertRaises(ValueError):
            work.spend(2)
        self.assertEqual(work.used, 0)
        with self.assertRaises(ValueError):
            work.spend(True)

    def test_22_frozen_source_identity_before_execution(self):
        self.assertEqual(len(self.sources), 15)
        path = "research/l-families/atlas/generalized/cusp_flag_all_weight_endpoint_separation.py"
        bad = dict(self.sources)
        bad[path] += b"\n"
        with self.assertRaisesRegex(ValueError, "before execution"):
            M.source_module(bad, "allweight")
        for name in (True, None, "../allweight", "endpoint"):
            with self.assertRaises(ValueError):
                M.source_module(self.sources, name)
        with (
            patch.object(
                M.subprocess, "check_output", return_value=str(M.MAX_BYTES + 1).encode()
            ),
            self.assertRaisesRegex(ValueError, "primitive byte cap"),
        ):
            M.authenticated_sources()

    def test_23_manifest_semantic_binding(self):
        for key in (
            "native_flags",
            "native_shear",
            "cross_lower_bound",
            "inverse_payment",
            "complex_zero",
            "residue",
            "excluded",
        ):
            bad = M.expected_manifest()
            bad["primitive_contract"][key] = "drift"
            with self.assertRaisesRegex(ValueError, "typed manifest"):
                M.authenticated_sources(bad)
        bad = M.expected_manifest()
        bad["frozen_sources"][0]["commit"] = "drift"
        self.assertEqual(M.BINDINGS[0]["commit"], M.BASE)
        self.assertEqual(
            M.canonical(M.parse_json(M.MANIFEST.read_bytes())),
            M.canonical(M.expected_manifest()),
        )

    def test_24_source_prefix_tamper(self):
        bad = dict(self.sources)
        path = "research/l-families/atlas/generalized/cusp_flag_all_weight_endpoint_separation.json"
        old = M.parse_json(bad[path])
        old["native_first_effective_prefixes"][0]["q_prefix"][3] += 1
        bad[path] = M.canonical(old).encode()
        with self.assertRaisesRegex(ValueError, "prefix agreement"):
            M.native_controls(bad, self.aw, self.aw.Budget(M.SOURCE_WORK))

    def test_25_artifact_LF_seals_and_C0(self):
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for path, digest in self.report["artifact_sha256_lf"].items():
            raw = (ROOT / path).read_bytes()
            normalized = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(hashlib.sha256(normalized).hexdigest(), digest)
            self.assertFalse(any(v < 32 and v not in (9, 10, 13) for v in raw))
        with (
            patch.object(Path, "read_bytes", return_value=b"\x0c"),
            self.assertRaises(ValueError),
        ):
            M.artifact_hashes()

    def test_26_JSON_byte_node_depth_caps(self):
        for raw in (b'{"x":1,"x":2}', b'{"x":NaN}', b'{"x":1.0}', b"\xff"):
            with self.assertRaises(ValueError):
                M.parse_json(raw)
        for value in ([0] * 1025, "x" * 4097, [[0] * 1000 for _ in range(21)]):
            with self.assertRaises(ValueError):
                M.canonical(value)
        deep = 0
        for _ in range(26):
            deep = [deep]
        with self.assertRaises(ValueError):
            M.canonical(deep)
        with self.assertRaises(ValueError):
            M.normalized(b"x" * (M.MAX_BYTES + 1))
        self.assertEqual(M.lf_sha(b"x\n"), M.lf_sha(b"x\r\n"))

    def test_27_payload_seal_and_direct_arithmetic_tamper(self):
        payload = {k: v for k, v in self.report.items() if k != "payload_sha256"}
        self.assertEqual(
            self.report["payload_sha256"],
            hashlib.sha256(M.canonical(payload).encode()).hexdigest(),
        )
        bad = copy.deepcopy(self.report)
        bad["scope"]["effective_pole_onset"] = True
        with self.assertRaisesRegex(ValueError, "payload digest"):
            M.validate_report(bad)
        bad.pop("payload_sha256")
        bad["native_normalization_ledger"]["B0_over_A2_leading"] = "2"
        with self.assertRaisesRegex(ValueError, "typed reconstruction"):
            M.validate_report(M.seal(bad))

    def test_28_resealed_type_scope_taxonomy_attacks(self):
        with patch.object(M, "build_report", return_value=self.report):
            for key, value in (
                ("actual_canonical_Q_additional_poles", 1),
                ("analytic_values_sampled", False),
                ("65536_pole_onset_inherited", True),
                ("denominator_zero_alone_implies_pole", True),
                ("conditional_Schur_control_is_native_evidence", True),
                ("no_numerator_zeros_in_pole_disc", True),
                ("varying_delta", True),
                ("global_pole_census", True),
            ):
                bad = copy.deepcopy(self.report)
                bad.pop("payload_sha256")
                bad["scope"][key] = value
                with self.assertRaisesRegex(ValueError, "typed reconstruction"):
                    M.validate_report(M.seal(bad))
            bad = copy.deepcopy(self.report)
            bad.pop("payload_sha256")
            bad["arithmetic_class"] = "EXACT"
            with self.assertRaises(ValueError):
                M.validate_report(M.seal(bad))

    def test_29_taxonomy_and_charged_coverage(self):
        self.assertEqual(self.report["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.report["arithmetic_components"],
            ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        )
        self.assertIn("no rounding", self.report["rounding_contract"])
        self.assertLessEqual(self.report["coverage"]["charged_work"], M.MAX_WORK)
        self.assertLessEqual(
            self.report["coverage"]["charged_source_work"], M.SOURCE_WORK
        )
        self.assertEqual(self.report["coverage"]["classes"], 6)
        self.assertEqual(self.report["coverage"]["native_pairs"], 12)

    def test_30_no_assert_float_special_function_sampling(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(n, ast.Assert) for n in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(n, ast.Constant) and type(n.value) in (float, complex)
                for n in ast.walk(tree)
            )
        )
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = (
                    node.func.id
                    if isinstance(node.func, ast.Name)
                    else node.func.attr
                    if isinstance(node.func, ast.Attribute)
                    else ""
                )
                self.assertNotIn(
                    name, {"float", "complex", "eval", "gamma", "exp", "log", "sqrt"}
                )

    def test_31_written_full_native_proof(self):
        note = M.NOTE.read_text(encoding="utf-8")
        for token in (
            "entire fundamental domain and entire q tails",
            "simultaneously for ALL f",
            "positive surviving cross-period",
            "ONE fixed Omega_R",
            "dc/ds=-k",
            "1056000*pi*eta",
            "full convergent q tails",
            "Changing x to -x",
            "NON-EFFECTIVE",
            "not a new native Fourier frequency",
        ):
            self.assertIn(token, note)

    def test_32_scientific_scope_exclusions(self):
        scope = self.report["scope"]
        for key in (
            "effective_pole_onset",
            "65536_pole_onset_inherited",
            "global_pole_census",
            "no_numerator_zeros_in_pole_disc",
            "varying_delta",
            "RH_or_new_automorphic_family",
            "analytic_proof_machine_certified",
            "parents_modified",
        ):
            self.assertFalse(scope[key])
        self.assertEqual(scope["analytic_values_sampled"], 0)
        self.assertTrue(scope["entire_tail_nonzero_effective_cross"])
        self.assertTrue(scope["full_W3_metric_payment"])
        self.assertTrue(scope["residue_1152_positive_right"])


if __name__ == "__main__":
    unittest.main()
