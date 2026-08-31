"""Exact arithmetic and hostile release checks, not sampled analytic proofs."""

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
    ROOT
    / "research/l-families/atlas/generalized/cusp_flag_effective_endpoint_separation.py"
)
SPEC = importlib.util.spec_from_file_location("effective_endpoint_tested", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def independent_prefix(k, j, n):
    e = k // 4 - 3 * j
    sigma1 = [0] + [
        sum(a for a in range(1, b + 1) if b % a == 0) for b in range(1, n + 1)
    ]
    a = [1] + [
        240 * sum(a**3 for a in range(1, b + 1) if b % a == 0) for b in range(1, n + 1)
    ]
    delta, eisenstein = [1], [1]
    for b in range(1, n + 1):
        numerator = -24 * j * sum(sigma1[a] * delta[b - a] for a in range(1, b + 1))
        if numerator % b:
            raise RuntimeError("Delta logarithmic recurrence integrality")
        delta.append(numerator // b)
        numerator = sum(
            ((e + 1) * i - b) * a[i] * eisenstein[b - i] for i in range(1, b + 1)
        )
        if numerator % b:
            raise RuntimeError("E4 differential recurrence integrality")
        eisenstein.append(numerator // b)
    values = [
        sum(delta[a] * eisenstein[b - a] for a in range(b + 1)) for b in range(n + 1)
    ]
    return [0] * j + values[: n + 1 - j]


class EffectiveEndpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = M.authenticated_sources()
        cls.report = M.build_report()

    def test_01_full_fixture(self):
        fixture = M.parse_json(M.FIXTURE.read_bytes())
        self.assertEqual(M.canonical(fixture), M.canonical(self.report))
        M.validate_report(fixture)

    def test_02_Lambda_integral_envelopes(self):
        row = self.report["Lambda_envelope_constants"]
        self.assertEqual(row["lower_Gamma_argument_interval"], ["1/4", "1/2"])
        self.assertLess(Q(1, 4) ** -1 + Q(1, 2), row["lower_Gamma_upper"])
        self.assertEqual(Q(1, 4) ** -2 + 1, row["lower_abs_Gamma_prime_upper"])
        self.assertLess(Q(17 + 2 * 5, 2), row["lower_abs_F_prime_upper"])
        self.assertLess(Q(3, 4) ** -1 + Q(1, 2), row["upper_Gamma_upper"])
        self.assertLess(Q(3, 4) ** -2 + 1, row["upper_abs_Gamma_prime_upper"])
        self.assertEqual(4 * 3 + 2 * 6, row["abs_Lambda_prime_upper"])
        self.assertEqual(14 + 5, row["D_Laurent_error_upper"])
        self.assertEqual(
            2 * row["abs_Lambda_prime_upper"], row["C_error_coefficient_times_epsilon"]
        )
        self.assertFalse(row["analytic_integrals_machine_evaluated"])

    def test_03_effective_onset_exact_signs(self):
        for k in (M.K, 65544, 65556, 100000, M.MAX_K):
            row = M.onset_certificate(k)
            self.assertEqual(Q(row["all_W_upper"]), -Q(k, 144) + 60)
            self.assertEqual(Q(row["witness_lower"]), Q(773 * k, 72000) - Q(2019, 100))
            self.assertLess(Q(row["all_W_upper"]), 0)
            self.assertGreater(Q(row["witness_lower"]), 0)
            self.assertEqual(row["is_admissible_weight12d"], k % 12 == 0)

    def test_04_all_integer_induction_polynomials(self):
        row = self.report["all_integer_induction"]
        self.assertEqual(row["ratio_gap_coefficients_ascending"], [-1, -2, 1])
        self.assertEqual(row["forward_difference_coefficients_ascending"], [-1, 2])
        for k in (3, 4, 5, 17, 65536, 1048576):
            gap = 2 * k * k - (k + 1) ** 2
            self.assertEqual(gap, k * k - 2 * k - 1)
            self.assertGreater(gap, 0)
            self.assertEqual(((k + 1) ** 2 - 2 * (k + 1) - 1) - gap, 2 * k - 1)
        self.assertEqual(4**2, 2**4)
        self.assertEqual(row["first_admissible_weight"], 65544)
        self.assertGreaterEqual(65544, M.K)
        self.assertLess(65544 - 12, M.K)

    def test_05_low_mass_and_exponent_budget(self):
        self.assertEqual(M.K, 2**16)
        self.assertLess(Q(96 * 16, M.K), Q(1, 32))
        self.assertLess(3**16, 2**26)
        for k in (M.K, M.K + 1, 65544, M.MAX_K):
            row = M.onset_certificate(k)
            self.assertEqual(row["comparison_power2_exponent_upper"], 26 - 4 * k)
            self.assertLessEqual(26 - 4 * k, -10)
            self.assertLess(Q(row["modular_error_u_upper"]), Q(1, 1000))
        self.assertLess(Q(1, 1024), Q(1, 1000))
        self.assertLess(Q(18 * 16, M.K), Q(1, 200))

    def test_06_both_Jensen_factors_and_sign_margin(self):
        self.assertGreater(Q(998, 1003), Q(99, 100))
        self.assertGreater(Q(99, 100) * Q(999, 1000) * Q(199, 200), Q(49, 50))
        self.assertLess(Q(200, 199), Q(101, 100))
        self.assertEqual(Q(19, 20) * Q(49, 50) / 24 - Q(101, 100) / 36, Q(773, 72000))
        self.assertEqual(19 * Q(101, 100) + 1, Q(2019, 100))
        self.assertLess(Q(864, M.K), Q(1, 40))

    def test_07_complete_denominator_error(self):
        self.assertLess(Q(2, 3) + 1 + 36 + 19 + Q(1, 2) + 1, 60)
        self.assertLess(19, Q(M.K, 36))
        self.assertLess(-Q(M.K, 144) + 60, 0)
        self.assertGreater(M.K, 8640)
        self.assertFalse(self.report["scope"]["6144_inherited"])
        self.assertFalse(self.report["scope"]["optimal_onset"])

    def test_08_native_threshold_prefix_first_terms(self):
        for row in self.report["effective_weight_q_prefixes"]:
            k, j = row["weight"], row["delta_power"]
            values = row["q_prefix"]
            self.assertEqual(k % 12, 0)
            self.assertEqual(values[:j], [0] * j)
            self.assertEqual(values[j], 1)
            self.assertEqual(values[j + 1], -24 * j + 240 * (k // 4 - 3 * j))
            self.assertEqual(row["is_in_W"], j >= 2)
            self.assertFalse(row["period_or_special_function_sample"])

    def test_09_independent_logarithmic_differential_prefixes(self):
        for key in ("frozen_overlap_q_prefixes", "effective_weight_q_prefixes"):
            for row in self.report[key]:
                self.assertEqual(
                    row["q_prefix"],
                    independent_prefix(
                        row["weight"], row["delta_power"], row["q_order"]
                    ),
                )

    def test_10_heldout_actual_prefixes(self):
        for k in (24, 48, 65568, 77760):
            for j in (1, 2):
                for order in (j + 1, 5, 7):
                    row = M.native_prefix(k, j, order, M.Budget())
                    self.assertEqual(row["q_prefix"], independent_prefix(k, j, order))

    def test_11_frozen_native_overlap(self):
        path = "research/l-families/atlas/generalized/cusp_flag_uncancelled_off_central_real_zeros.json"
        parent = M.parse_json(self.sources[path])["native_modular_prefixes"]
        current = self.report["frozen_overlap_q_prefixes"]
        self.assertEqual(len(parent), 8)
        for old, row in zip(parent, current, strict=True):
            self.assertEqual(row["q_prefix"], old["q_prefix"])
            self.assertEqual(row["weight"], 12 * old["dimension"])

    def test_12_power_unit_independent_binomial(self):
        for order in (0, 1, 4, 8):
            series = [math.comb(2, i) if i <= 2 else 0 for i in range(order + 1)]
            for exponent in (0, 1, 3, 19, M.MAX_K):
                expected = [
                    math.comb(2 * exponent, i) if i <= 2 * exponent else 0
                    for i in range(order + 1)
                ]
                self.assertEqual(
                    M.unit_power(series, exponent, order, M.Budget()), expected
                )

    def test_13_uniform_scale_coefficients(self):
        for c in (Q(3), Q(23, 2), Q(12), Q(25, 2), Q(18), Q(47, 2)):
            row = M.scale_ledger(c)
            self.assertEqual(
                Q(row["leading_k_coefficient"]), Q(1, 6) * Q(1, 4) - 1 / (2 * c)
            )
            self.assertEqual(
                Q(row["log_k_over_4pi_coefficient"]), -c * Q(1, 24) - Q(1, 2)
            )
            self.assertEqual(Q(row["constant_rational"]), -Q(1, 24))
            self.assertEqual(Q(row["Lambda_prime2_over_pi_coefficient"]), -2 * c / 4)
            self.assertFalse(row["uniform_as_c_approaches0_or24"])

    def test_14_independent_formal_product_coefficients(self):
        for c in (Q(6), Q(12), Q(18)):
            row = M.scale_ledger(c)
            # C=(pi/6)-2cP/k; M1=(k-1-cL)/(4pi).
            # D=-k/(2c)+B0; Meps=1+cL/k. Keep k,L,1,B0,P/pi.
            product = {
                "k": Q(1, 6) * Q(1, 4) - 1 / (2 * c),
                "L": -Q(1, 6) * c / 4 - Q(1, 2),
                "1": -Q(1, 6) * Q(1, 4),
                "B0": Q(1),
                "P/pi": -2 * c / 4,
            }
            for token, key in (
                ("k", "leading_k_coefficient"),
                ("L", "log_k_over_4pi_coefficient"),
                ("1", "constant_rational"),
                ("B0", "B0_coefficient"),
                ("P/pi", "Lambda_prime2_over_pi_coefficient"),
            ):
                self.assertEqual(product[token], Q(row[key]))

    def test_15_location_shift_and_scope(self):
        row = self.report["location_ledger"]
        self.assertEqual(M.scale_ledger(12)["leading_k_coefficient"], "0")
        self.assertEqual(Q(M.scale_ledger(12)["leading_c_derivative"]), Q(1, 288))
        self.assertEqual(row["log_k_over_4pi_shift"], "288")
        self.assertEqual(row["B0_shift"], "-288")
        self.assertEqual(row["rational_shift"], "12")
        self.assertEqual(row["Lambda_prime2_over_pi_shift"], "1728")
        self.assertEqual(row["epsilon_error"], "O(log^2(k)/k^3)")
        self.assertFalse(row["effective_asymptotic_error_or_onset"])
        self.assertFalse(row["uniqueness_or_simplicity"])

    def test_16_arbitrary_fixed_decay_orders(self):
        for row in self.report["arbitrary_fixed_order_ledgers"]:
            order, A = row["requested_fixed_order"], row["chosen_fixed_integer_A"]
            self.assertGreater(6 * A, order + 3)
            self.assertLess(row["cross_upper_power_from_pi_gt3"], -order)
            self.assertEqual(row["dimension_factor"], 0)
            self.assertFalse(row["A_depends_on_k"])
            self.assertTrue(row["complex_ratio_not_modulus_only"])
        self.assertEqual(len(self.report["arbitrary_fixed_order_ledgers"]), 33)

    def test_17_strict_integer_and_bit_types(self):
        for bad in (True, False, 1.0, "1", None):
            with self.assertRaises(ValueError):
                M.bigint(bad)
            with self.assertRaises(ValueError):
                M.rational(bad)
        for bad in (2**4096, -(2**4096)):
            with self.assertRaises(ValueError):
                M.bigint(bad)
        with self.assertRaises(ValueError):
            M.rational(Q(1, 2**4096))
        for bad in (True, 0, M.MAX_WORK + 1):
            with self.assertRaises(ValueError):
                M.Budget(bad)
        with self.assertRaises(ValueError):
            M.Budget().spend(True)

    def test_18_native_caps_and_types(self):
        for args in (
            (True, 1, 8),
            (12, 1, 8),
            (25, 1, 8),
            (M.MAX_K + 1, 1, 8),
            (24, True, 8),
            (24, 3, 8),
            (24, 1, True),
            (24, 1, 9),
            (24, 2, 2),
        ):
            with self.assertRaises(ValueError):
                M.native_prefix(*args, M.Budget())
        for bad in (True, M.K - 1, M.MAX_K + 1):
            with self.assertRaises(ValueError):
                M.onset_certificate(bad)
        for bad in (True, -1, 33, 1.0):
            with self.assertRaises(ValueError):
                M.decoupling_order(bad)

    def test_19_charged_work_before_expansion(self):
        work = M.Budget(1)
        with self.assertRaisesRegex(ValueError, "before expansion"):
            M.native_prefix(65544, 1, 8, work)
        self.assertEqual(work.used, 0)
        work = M.Budget(1)
        with self.assertRaises(ValueError):
            M.convolution([1] * 9, [1] * 9, 8, work)
        self.assertEqual(work.used, 0)
        self.assertLessEqual(self.report["coverage"]["charged_work"], M.MAX_WORK)

    def test_20_polynomial_shape_and_internal_bits(self):
        for left, right, order in (
            ([], [], 0),
            ([1], [1], 1),
            ([True], [1], 0),
            ([1.0], [1], 0),
        ):
            with self.assertRaises(ValueError):
                M.convolution(left, right, order, M.Budget())
        with self.assertRaises(ValueError):
            M.convolution([2**4095], [2], 0, M.Budget())
        for row, e, n in (([0], 1, 0), ([1], True, 0), ([1], M.MAX_K + 1, 0)):
            with self.assertRaises(ValueError):
                M.unit_power(row, e, n, M.Budget())

    def test_21_compact_c_caps(self):
        for c in (True, 0, 24, -1, 25, 12.0, "12", Q(1, 2**4096), Q(1, 2**4095)):
            with self.assertRaises(ValueError):
                M.scale_ledger(c)

    def test_22_manifest_semantic_and_type_drift(self):
        for key, value in (
            ("effective_threshold", "6144"),
            ("uniform_space", "basis only"),
            ("new_cross_input", "modulus only"),
            ("location", "unique"),
        ):
            bad = M.expected_manifest()
            bad["primitive_contract"][key] = value
            with self.assertRaisesRegex(ValueError, "typed manifest"):
                M.authenticated_sources(bad)
        bad = M.expected_manifest()
        bad["external_context"][0]["remote_bytes_authenticated"] = 0
        with self.assertRaises(ValueError):
            M.authenticated_sources(bad)
        bad = M.expected_manifest()
        bad["extra"] = True
        with self.assertRaises(ValueError):
            M.authenticated_sources(bad)

    def test_23_literal_source_byte_and_size_authentication(self):
        self.assertEqual(len(self.sources), 10)
        real = M.subprocess.check_output

        def altered(args, **kwargs):
            raw = real(args, **kwargs)
            return raw + b"\n" if args[1] == "show" else raw

        with (
            patch.object(M.subprocess, "check_output", side_effect=altered),
            self.assertRaisesRegex(ValueError, "primitive identity"),
        ):
            M.authenticated_sources()
        with (
            patch.object(
                M.subprocess, "check_output", return_value=str(M.MAX_BYTES + 1).encode()
            ),
            self.assertRaisesRegex(ValueError, "primitive byte cap"),
        ):
            M.authenticated_sources()

    def test_24_artifact_seals_and_control_characters(self):
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for path, digest in self.report["artifact_sha256_lf"].items():
            raw = (ROOT / path).read_bytes()
            self.assertFalse(any(v < 32 and v not in (9, 10, 13) for v in raw))
            self.assertEqual(M.lf_sha(raw), digest)
        with (
            patch.object(Path, "read_bytes", return_value=b"\x0c"),
            self.assertRaisesRegex(ValueError, "control character"),
        ):
            M.artifact_hashes()

    def test_25_JSON_duplicates_nonfinite_and_numbers(self):
        for raw in (
            b'{"a":1,"a":2}',
            b'{"a":NaN}',
            b'{"a":Infinity}',
            b'{"a":1.0}',
            b'{"a":1e3}',
            b"\xff",
        ):
            with self.assertRaises(ValueError):
                M.parse_json(raw)
        with self.assertRaises(ValueError):
            M.parse_json(("[" + str(2**4096) + "]").encode())

    def test_26_JSON_resource_guards(self):
        for value in ("a" * 4097, [0] * 1025, {str(i): 0 for i in range(1025)}):
            with self.assertRaises(ValueError):
                M.canonical(value)
        deep = 0
        for _ in range(26):
            deep = [deep]
        with self.assertRaises(ValueError):
            M.canonical(deep)
        with self.assertRaises(ValueError):
            M.canonical([[0] * 1000 for _ in range(21)])
        with self.assertRaises(ValueError):
            M.normalized(b"a" * (M.MAX_BYTES + 1))
        with self.assertRaises(ValueError):
            M.normalized("text")

    def test_27_LF_normalization_and_manifest_copy(self):
        self.assertEqual(M.lf_sha(b"a\nb\n"), M.lf_sha(b"a\r\nb\r\n"))
        self.assertEqual(M.lf_sha(b"a\nb\n"), M.lf_sha(b"a\rb\r"))
        bad = M.expected_manifest()
        bad["frozen_sources"][0]["path"] = "drift"
        self.assertNotEqual(M.BINDINGS[0]["path"], "drift")
        self.assertEqual(
            M.canonical(M.parse_json(M.MANIFEST.read_bytes())),
            M.canonical(M.expected_manifest()),
        )

    def test_28_payload_digest(self):
        payload = {k: v for k, v in self.report.items() if k != "payload_sha256"}
        self.assertEqual(
            self.report["payload_sha256"],
            hashlib.sha256(M.canonical(payload).encode()).hexdigest(),
        )
        bad = copy.deepcopy(self.report)
        bad["scope"]["threshold_K"] = 6144
        with self.assertRaisesRegex(ValueError, "payload digest"):
            M.validate_report(bad)
        with self.assertRaises(ValueError):
            M.seal(self.report)

    def test_29_resealed_mathematical_drift(self):
        paths = [
            ("Lambda_envelope_constants", "D_Laurent_error_upper", 18),
            ("Lambda_envelope_constants", "abs_Lambda_prime_upper", 23),
            ("location_ledger", "log_k_over_4pi_shift", "144"),
            ("location_ledger", "rational_shift", "0"),
            ("scope", "Schur_cross_uniform_all_W", False),
            ("scope", "complex_modular_ratio_proved", False),
            ("scope", "uniqueness_or_simplicity", True),
            ("scope", "asymptotic_error_onset_effective", True),
            ("all_integer_induction", "first_admissible_weight", 65536),
        ]
        with patch.object(M, "build_report", return_value=self.report):
            for parent, key, value in paths:
                bad = copy.deepcopy(self.report)
                bad.pop("payload_sha256")
                bad[parent][key] = value
                with self.assertRaisesRegex(ValueError, "typed reconstruction"):
                    M.validate_report(M.seal(bad))

    def test_30_taxonomy_and_typed_reconstruction(self):
        self.assertEqual(self.report["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.report["arithmetic_components"],
            ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        )
        self.assertIn("no rounding", self.report["rounding_contract"])
        with patch.object(M, "build_report", return_value=self.report):
            for key, value in (
                ("arithmetic_class", "EXACT"),
                ("arithmetic_components", ["EXACT_RATIONAL"]),
                ("rounding_contract", "rounded"),
            ):
                bad = copy.deepcopy(self.report)
                bad.pop("payload_sha256")
                bad[key] = value
                with self.assertRaises(ValueError):
                    M.validate_report(M.seal(bad))
            bad = copy.deepcopy(self.report)
            bad.pop("payload_sha256")
            bad["scope"]["actual_uncancelled_pair_effective"] = 1
            with self.assertRaises(ValueError):
                M.validate_report(M.seal(bad))

    def test_31_no_assert_float_or_analytic_sampling(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(n, ast.Assert) for n in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(n, ast.Constant) and type(n.value) is float
                for n in ast.walk(tree)
            )
        )
        forbidden = {
            "eval",
            "float",
            "gamma",
            "lgamma",
            "log",
            "exp",
            "sin",
            "cos",
            "sqrt",
        }
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = (
                    node.func.id
                    if isinstance(node.func, ast.Name)
                    else node.func.attr
                    if isinstance(node.func, ast.Attribute)
                    else ""
                )
                self.assertNotIn(name, forbidden)

    def test_32_proof_native_quantifiers_and_boundaries(self):
        note = M.NOTE.read_text(encoding="utf-8")
        for token in (
            "EVERY multiple k=12d>=K=2^16=65536",
            "first admissible weight covered is 65544",
            "uniformly over c in J and ALL f in W",
            "complex ratio itself",
            "a FIXED positive integer A",
            "No uniqueness, simplicity",
            "independent frozen-SHA",
            "not an optimal onset",
            "does NOT inherit",
        ):
            self.assertIn(token, note)
        self.assertFalse(
            self.report["scope"]["analytic_limits_integrals_machine_certified"]
        )
        self.assertFalse(self.report["scope"]["parent_files_modified"])
        self.assertFalse(self.report["scope"]["endpoint_escaping_c_sequences_excluded"])
        self.assertEqual(
            self.report["scope"]["actual_period_zero_Gamma_zeta_Bessel_samples"], 0
        )


if __name__ == "__main__":
    unittest.main()
