"""Six-class exact identities and hostile guards; no analytic value samples."""

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
    / "research/l-families/atlas/generalized/cusp_flag_all_weight_endpoint_separation.py"
)
SPEC = importlib.util.spec_from_file_location("all_weight_endpoint", SOURCE)
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


class AllWeightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = M.authenticated_sources()
        cls.endpoint = M.source_module(cls.sources, "endpoint")
        cls.family = M.source_module(cls.sources, "family")
        cls.report = M.build_report()

    def test_01_fixture(self):
        fixture = M.parse_json(M.FIXTURE.read_bytes())
        self.assertEqual(M.canonical(fixture), M.canonical(self.report))
        M.validate_report(fixture)

    def test_02_six_class_first_weights(self):
        rows = M.class_onsets()
        self.assertEqual(
            {r["r"]: r["first_weight"] for r in rows},
            {0: 65544, 4: 65536, 6: 65538, 8: 65540, 10: 65542, 14: 65546},
        )
        self.assertEqual(
            sorted(r["first_weight"] for r in rows), list(range(65536, 65548, 2))
        )
        for row in rows:
            self.assertEqual(row["r"], 4 * row["a"] + 6 * row["b"])
            self.assertEqual(row["first_weight"], 12 * row["dimension"] + row["r"])
            self.assertLess(row["first_weight"] - 12, M.K)

    def test_03_r14_not_r2(self):
        for k in (38, 50, 65546, 65558):
            weight, d, r, a, b = M.parameters(k)
            self.assertEqual((weight, r, a, b), (k, 14, 2, 1))
            self.assertEqual(d, (k - 14) // 12)
            self.assertNotEqual(d, k // 12)

    def test_04_exponent_identities(self):
        for d in (2, 3, 5461, 5462):
            for r, (a, b) in M.RESIDUAL.items():
                row = M.exponent_ledger(12 * d + r)
                p = 3 * d - 3 + a
                self.assertEqual(row["low_power_of2"], 4 * p + 8 * b)
                self.assertEqual(row["low_power_of2"], row["weight"] - 12 + 2 * b)
                self.assertLessEqual(row["low_power_of2"], row["weight"])
                self.assertEqual(
                    row["high_E4_square_power"], row["weight"] // 2 - 6 - 3 * b
                )
                self.assertLessEqual(2 * p, row["weight"] // 2)

    def test_05_power_sum_identity_by_independent_series(self):
        for power in range(1, 6):
            numerator, denominator = M.power_sum_numerator(power)
            for n in range(1, 31):
                coefficient = sum(
                    c * math.comb(n - i + denominator - 1, denominator - 1)
                    for i, c in enumerate(numerator)
                    if i <= n
                )
                self.assertEqual(coefficient, n**power)
        self.assertEqual(M.power_sum_numerator(5), ([0, 1, 26, 66, 26, 1], 6))

    def test_06_exact_S5_endpoint(self):
        rho = Q(1, 100)
        expected = (1 + 26 * rho + 66 * rho**2 + 26 * rho**3 + rho**4) / (1 - rho) ** 6
        row = M.s5_envelope(rho)
        self.assertEqual(Q(row["S5"]), expected)
        self.assertLess(expected, Q(8, 5))
        self.assertEqual(504 * Q(5, 4) * Q(8, 5), 1008)
        self.assertEqual(1 + Q(1008, 100), Q(277, 25))
        self.assertLess(Q(277, 25), 16)

    def test_07_S5_monotonicity_polynomial(self):
        p = [1, 26, 66, 26, 1]
        derivative = [i * p[i] for i in range(1, len(p))]
        numerator = [0] * 5
        for i, v in enumerate(derivative):
            numerator[i] += v
            numerator[i + 1] -= v
        for i, v in enumerate(p):
            numerator[i] += 6 * v
        self.assertTrue(all(v > 0 for v in numerator))
        previous = Q(0)
        for r in (Q(0), Q(1, 10000), Q(1, 200), Q(1, 100)):
            value = Q(M.s5_envelope(r)["S5"])
            self.assertGreater(value, previous)
            previous = value

    def test_08_divisor_majorant_exact_controls(self):
        for n in range(1, 101):
            sigma = sum(d**5 for d in range(1, n + 1) if n % d == 0)
            self.assertLessEqual(Q(sigma, n**5), Q(5, 4))
            self.assertEqual(
                Q(sigma, n**5),
                sum((Q(1, d**5) for d in range(1, n + 1) if n % d == 0), Q(0)),
            )

    def test_09_uniform_modular_envelopes(self):
        for row in self.report["squared_and_complex_envelopes"]:
            k, rho = row["weight"], Q(row["rho"])
            p = M.exponent_ledger(k)
            actual = (
                48 * rho / (1 - rho) + 960 * p["E4_power"] * rho + 2016 * p["b"] * rho
            )
            uniform = 48 * rho / (1 - rho) + 240 * k * rho + 2016 * rho
            self.assertEqual(Q(row["actual_squared_u"]), actual)
            self.assertEqual(Q(row["uniform_squared_u"]), uniform)
            self.assertLessEqual(actual, uniform)
            self.assertLessEqual(uniform, 289 * k * rho)
            self.assertLessEqual(Q(2065), 49 * k)
            self.assertLess(Q(row["u_bound"]), Q(1, 1000))

    def test_10_lower_product_bound(self):
        for row in self.report["squared_and_complex_envelopes"]:
            k, rho = row["weight"], Q(row["rho"])
            errors = (48 * rho / (1 - rho), 240 * k * rho, 2016 * rho)
            self.assertTrue(all(0 <= e < 1 for e in errors))
            product = math.prod(1 - e for e in errors)
            self.assertGreaterEqual(product, 1 - sum(errors))
            self.assertEqual(1 - sum(errors), Q(row["squared_lower"]))
            self.assertEqual(1 / (1 - sum(errors)), Q(row["squared_upper"]))

    def test_11_complex_not_modulus_only(self):
        for k in range(65536, 65548, 2):
            row = M.modular_envelope(k, Q(1, k**6))
            self.assertEqual(2 * Q(row["complex_v"]), Q(row["actual_squared_u"]))
            self.assertEqual(row["complex_ratio_error_upper"], row["actual_squared_u"])
            zero = M.modular_envelope(k, 0)
            self.assertEqual(zero["complex_v"], "0")
            self.assertEqual(zero["squared_lower"], "1")
            self.assertFalse(row["modulus_only_argument"])

    def test_12_native_first_coefficients(self):
        for key in ("native_CF_small_prefixes", "native_first_effective_prefixes"):
            for row in self.report[key]:
                j, p, b = row["delta_power"], row["E4_power"], row["b"]
                q = row["q_prefix"]
                self.assertEqual(q[:j], [0] * j)
                self.assertEqual(q[j], 1)
                self.assertEqual(q[j + 1], -24 * j + 240 * p - 504 * b)
                self.assertEqual(row["is_in_W"], j == 2)

    def test_13_independent_all_six_prefixes(self):
        for key in ("native_CF_small_prefixes", "native_first_effective_prefixes"):
            for row in self.report[key]:
                self.assertEqual(
                    row["q_prefix"],
                    independent_prefix(
                        row["weight"], row["delta_power"], row["q_order"]
                    ),
                )
        self.assertEqual(self.report["coverage"]["native_small_prefixes"], 24)
        self.assertEqual(self.report["coverage"]["native_effective_prefixes"], 12)

    def test_14_heldout_class_prefixes(self):
        for d in (4, 5463):
            for r in M.RESIDUAL:
                for j in (1, 2):
                    row = M.native_prefix(12 * d + r, j, 7, M.Budget())
                    self.assertEqual(
                        row["q_prefix"], independent_prefix(12 * d + r, j, 7)
                    )

    def test_15_EP_r0_overlap(self):
        path = "research/l-families/atlas/generalized/cusp_flag_effective_endpoint_separation.json"
        old = M.parse_json(self.sources[path])
        for row in old["effective_weight_q_prefixes"]:
            new = M.native_prefix(row["weight"], row["delta_power"], 8, M.Budget())
            self.assertEqual(new["q_prefix"], row["q_prefix"])

    def test_16_E6_factor_not_dropped(self):
        plain = M.native_prefix(24, 1, 8, M.Budget())["q_prefix"]
        with_e6 = M.native_prefix(30, 1, 8, M.Budget())["q_prefix"]
        self.assertEqual(with_e6[2] - plain[2], -504)
        self.assertNotEqual(with_e6, plain)

    def test_17_exact_EP_reserve_transfer(self):
        for row in self.report["effective_transfers"]:
            old = self.endpoint.onset_certificate(row["weight"])
            for key, value in row["unchanged_EP_integer_bounds"].items():
                self.assertEqual(value, old[key])
            self.assertFalse(row["EP_multiple12_scope_blindly_inherited"])
            self.assertTrue(row["native_class_decoded_here"])
        self.assertEqual(
            self.report["unchanged_Lambda_bounds"], self.endpoint.lambda_constants()
        )

    def test_18_location_constants_unchanged(self):
        row = self.report["unchanged_location_ledger"]
        self.assertEqual(row, self.endpoint.location_ledger())
        self.assertEqual(row["first_scale"], 12)
        self.assertEqual(row["log_k_over_4pi_shift"], "288")
        self.assertEqual(row["Lambda_prime2_over_pi_shift"], "1728")
        self.assertFalse(row["uniqueness_or_simplicity"])
        self.assertTrue(self.report["scope"]["same_C12_no_residue_shift"])

    def test_19_taxonomy_scope_and_work(self):
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
        self.assertFalse(self.report["scope"]["effective_fine_asymptotic_onset"])
        self.assertFalse(self.report["scope"]["6144_certified"])

    def test_20_weight_and_class_guards(self):
        for k in (True, False, 24.0, "24", 23, 25, 26, M.MAX_K + 1):
            with self.assertRaises(ValueError):
                M.parameters(k)
        for k in (24, 28, 30, 32, 34, 38):
            self.assertEqual(M.parameters(k)[1], 2)
        self.assertEqual(M.parameters(65536)[2], 4)

    def test_21_radial_caps(self):
        for rho in (True, 0.0, "0", -1, Q(1, 99), Q(1, 2**128)):
            with self.assertRaises(ValueError):
                M.s5_envelope(rho)
        with self.assertRaises(ValueError):
            M.modular_envelope(65536, Q(1, 100))
        with self.assertRaises(ValueError):
            M.modular_envelope(24, 0)
        with self.assertRaises(ValueError):
            M.rational(Q(1, 2**4096))

    def test_22_polynomial_and_order_guards(self):
        for args in ((65536, True, 8), (65536, 3, 8), (65536, 1, 9), (65536, 2, 2)):
            with self.assertRaises(ValueError):
                M.native_prefix(*args, M.Budget())
        for p in (True, 0, 6, 5.0):
            with self.assertRaises(ValueError):
                M.power_sum_numerator(p)
        with self.assertRaises(ValueError):
            M.convolution([2**4095], [2], 0, M.Budget())
        with self.assertRaises(ValueError):
            M.unit_power([0], 1, 0, M.Budget())

    def test_23_work_and_integer_guards(self):
        work = M.Budget(1)
        with self.assertRaisesRegex(ValueError, "before expansion"):
            M.native_prefix(65536, 1, 8, work)
        self.assertEqual(work.used, 0)
        for bad in (True, 0, M.MAX_WORK + 1):
            with self.assertRaises(ValueError):
                M.Budget(bad)
        for bad in (True, 1.0, 2**4096):
            with self.assertRaises(ValueError):
                M.bigint(bad)
        with self.assertRaises(ValueError):
            M.Budget().spend(True)

    def test_24_source_identity_before_execution(self):
        self.assertEqual(len(self.sources), 10)
        bad = dict(self.sources)
        path = "research/l-families/atlas/generalized/cusp_flag_effective_endpoint_separation.py"
        bad[path] = bad[path] + b"\n"
        with self.assertRaisesRegex(ValueError, "before execution"):
            M.source_module(bad, "endpoint")
        with (
            patch.object(
                M.subprocess, "check_output", return_value=str(M.MAX_BYTES + 1).encode()
            ),
            self.assertRaisesRegex(ValueError, "primitive byte cap"),
        ):
            M.authenticated_sources()

    def test_25_typed_manifest_tamper(self):
        for key, value in (
            ("r14", "r2"),
            ("effective", "6144"),
            ("new_modular_input", "omit E6"),
            ("asymptotic", "residue shift"),
        ):
            bad = M.expected_manifest()
            bad["primitive_contract"][key] = value
            with self.assertRaisesRegex(ValueError, "typed manifest"):
                M.authenticated_sources(bad)
        bad = M.expected_manifest()
        bad["extra"] = 1
        with self.assertRaises(ValueError):
            M.authenticated_sources(bad)
        self.assertEqual(
            M.canonical(M.parse_json(M.MANIFEST.read_bytes())),
            M.canonical(M.expected_manifest()),
        )

    def test_26_artifact_seals_and_control_chars(self):
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for path, digest in self.report["artifact_sha256_lf"].items():
            raw = (ROOT / path).read_bytes()
            self.assertEqual(M.lf_sha(raw), digest)
            self.assertFalse(any(v < 32 and v not in (9, 10, 13) for v in raw))
        with (
            patch.object(Path, "read_bytes", return_value=b"\x0c"),
            self.assertRaisesRegex(ValueError, "control character"),
        ):
            M.artifact_hashes()

    def test_27_JSON_and_byte_firewalls(self):
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
        self.assertEqual(M.lf_sha(b"a\nb\n"), M.lf_sha(b"a\r\nb\r\n"))

    def test_28_payload_seal(self):
        payload = {k: v for k, v in self.report.items() if k != "payload_sha256"}
        self.assertEqual(
            self.report["payload_sha256"],
            hashlib.sha256(M.canonical(payload).encode()).hexdigest(),
        )
        bad = copy.deepcopy(self.report)
        bad["scope"]["first_weight"] = 6144
        with self.assertRaisesRegex(ValueError, "payload digest"):
            M.validate_report(bad)
        with self.assertRaises(ValueError):
            M.seal(self.report)

    def test_29_resealed_semantic_tamper(self):
        with patch.object(M, "build_report", return_value=self.report):
            for key, value in (
                ("same_C12_no_residue_shift", False),
                ("complex_not_modulus_only", False),
                ("every_even_weight_ge65536", 1),
                ("r14_not_r2", False),
                ("6144_certified", True),
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
            bad = copy.deepcopy(self.report)
            bad.pop("payload_sha256")
            bad["six_class_onsets"][0]["first_weight"] = 65536
            with self.assertRaises(ValueError):
                M.validate_report(M.seal(bad))

    def test_30_fixed_source_enum(self):
        for name in (True, "other", "../family", None):
            with self.assertRaises(ValueError):
                M.source_module(self.sources, name)
        first = M.expected_manifest()
        first["frozen_sources"][0]["path"] = "drift"
        self.assertNotEqual(M.BINDINGS[0]["path"], "drift")

    def test_31_no_float_assert_or_analytic_sampling(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(n, ast.Assert) for n in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(n, ast.Constant) and type(n.value) is float
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
                    name, {"float", "eval", "gamma", "lgamma", "exp", "log", "sqrt"}
                )

    def test_32_written_native_scope(self):
        note = M.NOTE.read_text(encoding="utf-8")
        for token in (
            "EVERY even integer",
            "FOURTEEN, not two",
            "no r-dependent shift",
            "COMPLEX ratio",
            "uniformly over ALL f in W",
            "No uniqueness, simplicity",
            "no EP, UQ, CZ or CF source is edited",
        ):
            self.assertIn(token, note)
        self.assertFalse(self.report["scope"]["parents_modified"])
        self.assertFalse(self.report["scope"]["all_odd_or_small_weights"])
        self.assertFalse(self.report["scope"]["analytic_limits_machine_certified"])
        self.assertEqual(self.report["scope"]["analytic_values_sampled"], 0)


if __name__ == "__main__":
    unittest.main()
