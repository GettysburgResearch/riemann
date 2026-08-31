"""Independent finite identities and fail-closed release tests."""

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
SOURCE = ROOT / "research/exploratory/hardy_low_pass_height_equivalence.py"
SPEC = importlib.util.spec_from_file_location("lp_tested", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def determinant(a):
    n = len(a)
    out = Q(0)
    for p in itertools.permutations(range(n)):
        sign = (-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        out += sign * math.prod(a[i][p[i]] for i in range(n))
    return out


def adjugate_inverse(a):
    n = len(a)
    d = determinant(a)
    if n == 1:
        return [[1 / a[0][0]]]
    return [
        [
            (-1) ** (i + j)
            * determinant(
                [[a[u][v] for v in range(n) if v != i] for u in range(n) if u != j]
            )
            / d
            for j in range(n)
        ]
        for i in range(n)
    ]


def independent_partial(nodes, y):
    """Taylor expansion at each denominator root; no linear-system solve."""

    def product(factors):
        out = [Q(1)]
        for f in factors:
            nxt = [Q(0)] * (len(out) + 1)
            for i, a in enumerate(out):
                nxt[i] += f * a
                nxt[i + 1] += a
            out = nxt
        return out

    def translated(p, center, order):
        return [
            sum(Q(p[j]) * math.comb(j, k) * center ** (j - k) for j in range(k, len(p)))
            for k in range(order)
        ]

    den = product([(eta + y) ** 2 for eta, m in nodes for _ in range(m)])
    num = product([(eta - y) ** 2 for eta, m in nodes for _ in range(m)])
    numerator = [a - b for a, b in zip(den, num)]
    total, parts = Q(0), []
    for eta, m in nodes:
        scale = eta + y
        other = product([(e + y) ** 2 for e, q in nodes if e != eta for _ in range(q)])
        p = translated(numerator, -(scale**2), m)
        q = translated(other, -(scale**2), m)
        h = []
        for n in range(m):
            h.append((p[n] - sum(q[j] * h[n - j] for j in range(1, n + 1))) / q[0])
        integral = 1 / scale
        for order in range(1, m + 1):
            if order > 1:
                integral *= Q(2 * order - 3, 2 * (order - 1)) / scale**2
            coefficient = h[m - order]
            total += coefficient * integral / (4 * y)
            parts.append((scale, order, coefficient, integral))
    return total, parts


class LowPassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def test_01_fixture_and_seal(self):
        fixture = M.parse_json(M.FIXTURE.read_bytes())
        M.validate_report(fixture)
        self.assertEqual(M.canonical(fixture), M.canonical(self.report))

    def test_02_all_Gram_inverses_by_adjugates(self):
        for row in self.report["finite_Gram_bridge_controls"]:
            g = [[Q(x) for x in r] for r in row["Gram"]]
            inverse = [[Q(x) for x in r] for r in row["Gram_inverse"]]
            self.assertEqual(inverse, adjugate_inverse(g))
            for i in range(1, len(g) + 1):
                self.assertGreater(determinant([r[:i] for r in g[:i]]), 0)

    def test_03_all_partial_fractions_by_local_Taylor(self):
        for row in self.report["finite_Gram_bridge_controls"]:
            nodes = [(Q(eta), m) for eta, m in row["nodes_eta_multiplicity"]]
            total, parts = independent_partial(nodes, Q(row["y"]))
            self.assertEqual(total, Q(row["shifted_Gram_trace"]))
            self.assertEqual(
                parts,
                [
                    (
                        Q(r["scale"]),
                        r["order"],
                        Q(r["coefficient"]),
                        Q(r["basis_integral_over_pi"]),
                    )
                    for r in row["partial_fractions_in_x_squared"]
                ],
            )

    def test_04_independent_shifted_Gram_trace(self):
        for row in self.report["finite_Gram_bridge_controls"]:
            nodes = [(Q(eta), m) for eta, m in row["nodes_eta_multiplicity"]]
            modes = [(eta, r) for eta, m in nodes for r in range(m)]
            y = Q(row["y"])
            g = [
                [
                    Q(math.factorial(r + s), math.factorial(r) * math.factorial(s))
                    / (eta + other) ** (r + s + 1)
                    for other, s in modes
                ]
                for eta, r in modes
            ]
            gy = [
                [
                    Q(math.factorial(r + s), math.factorial(r) * math.factorial(s))
                    / (eta + other + 2 * y) ** (r + s + 1)
                    for other, s in modes
                ]
                for eta, r in modes
            ]
            inv = adjugate_inverse(g)
            trace = sum(
                inv[i][j] * gy[j][i] for i in range(len(g)) for j in range(len(g))
            )
            self.assertEqual(trace, Q(row["horizontal_defect_integral_over_4pi_y"]))

    def test_05_heldout_confluent_and_simple_models(self):
        for nodes in (
            [(Q(2, 3), 4)],
            [(Q(1, 3), 1), (Q(7, 3), 2)],
            [(1, 1), (Q(3, 2), 1), (Q(5, 2), 1)],
        ):
            for y in (Q(1, 3), Q(5, 2)):
                row = M.finite_control(nodes, y)
                exact_nodes = [(Q(eta), m) for eta, m in nodes]
                self.assertEqual(
                    Q(row["shifted_Gram_trace"]), independent_partial(exact_nodes, y)[0]
                )

    def test_06_origin_counts_multiplicity(self):
        for row in self.report["finite_Gram_bridge_controls"]:
            height = sum(Q(eta) * m for eta, m in row["nodes_eta_multiplicity"])
            self.assertEqual(Q(row["origin"]), 2 * height)
            self.assertTrue(row["negative_square_derivative_verified"])

    def test_07_one_factor_normalization(self):
        for eta in (Q(1, 3), Q(1), Q(7, 2)):
            for y in (Q(1, 2), Q(1), Q(3)):
                row = M.finite_control([(eta, 1)], y)
                self.assertEqual(Q(row["shifted_Gram_trace"]), eta / (eta + y))
                self.assertEqual(Q(row["log_integral_over_2pi"]), min(y, eta))

    def test_08_factor_translation_and_zero(self):
        self.assertEqual(M.factor_control(0, 2, 0, 2)["modulus_squared"], "0")
        for a, x in ((Q(-3), Q(5)), (Q(2, 3), Q(-1, 2))):
            left = M.factor_control(a, Q(3, 2), x, 2)
            right = M.factor_control(a + 1, Q(3, 2), x + 1, 2)
            self.assertEqual(left["defect"], right["defect"])
            self.assertEqual(Q(left["defect"]) + Q(left["modulus_squared"]), 1)

    def test_09_product_telescoping_and_repetition(self):
        factors = [(0, Q(1, 2), 1, 2), (2, 3, 1, 2), (2, 3, 1, 2)]
        row = M.product_control(factors)
        direct = math.prod(
            Q((x - a) ** 2 + (y - eta) ** 2, (x - a) ** 2 + (y + eta) ** 2)
            for a, eta, x, y in factors
        )
        self.assertEqual(Q(row["modulus_squared"]), direct)
        self.assertEqual(Q(row["defect"]), 1 - direct)

    def test_10_log_integral_overlap_y_equals_eta(self):
        row = M.finite_control([(1, 2), (3, 1)], 1)
        self.assertEqual(Q(row["log_integral_over_2pi"]), 3)
        self.assertEqual(M.factor_control(0, 1, 0, 1)["log_singularity_on_line"], True)

    def test_11_Lipschitz_disjoint_area(self):
        for row in self.report["real_inequality_controls"]:
            e, y = Q(row["epsilon"]), Q(row["y"])
            half = Q(row["half_interval_width"])
            self.assertEqual(half * 2 * (e / 2), Q(row["disjoint_interval_mass_lower"]))
            self.assertEqual(half / y, e / 2)
            self.assertGreaterEqual(Q(row["q_minus_half_negative_log_derivative"]), 0)

    def test_12_weighted_tail_coefficient(self):
        for y in (Q(1, 3), Q(2)):
            for L in (Q(1, 2), Q(4)):
                row = M.real_inequality_control(Q(1, 4), y, L)
                self.assertEqual(
                    Q(row["weighted_trace_bound_per_A"]), 1 + 1 / (2 * y * L)
                )
                self.assertFalse(row["exponentials_or_logs_evaluated"])

    def test_13_delay_endpoints(self):
        self.assertIs(M.delay_control(3, 3)["T_and_C_identically_zero"], True)
        self.assertIs(M.delay_control(3, 4)["T_and_C_identically_zero"], True)
        self.assertIs(M.delay_control(3, 2)["T_and_C_identically_zero"], False)
        self.assertEqual(M.delay_control(3, 2)["remaining_input_low_pass_length"], "1")

    def test_14_lacunary_exact_Gram_bounds(self):
        for n in range(1, 9):
            row = M.lacunary_control(n)
            g = [[Q(x) for x in r] for r in row["Gram"]]
            for i in range(n):
                self.assertEqual(g[i][i], 1)
                self.assertLess(sum(abs(g[i][j]) for j in range(n) if j != i), Q(4, 15))
                for j in range(n):
                    if j != i:
                        self.assertLessEqual(g[i][j], 2 * Q(1, 16) ** abs(i - j))

    def test_15_lacunary_small_principal_minors(self):
        g = [[Q(x) for x in r] for r in M.lacunary_control(4)["Gram"]]
        for n in range(1, 5):
            lower = [
                [g[i][j] - Q(11, 15) * int(i == j) for j in range(n)] for i in range(n)
            ]
            upper = [
                [Q(19, 15) * int(i == j) - g[i][j] for j in range(n)] for i in range(n)
            ]
            self.assertGreater(determinant(lower), 0)
            self.assertGreater(determinant(upper), 0)

    def test_16_strict_rational_types_bits(self):
        for value in (True, False, 1.0, "1", None, 2**32, Q(1, 2**32)):
            with self.assertRaises(ValueError):
                M.exact(value)
        with self.assertRaises(ValueError):
            M.exact(2**4096, internal=True)
        with self.assertRaises(ValueError):
            M.exact(1, internal=1)

    def test_17_node_caps_duplicates_and_types(self):
        for nodes in (
            [],
            [(1, True)],
            [(0, 1)],
            [(1, 5)],
            [(1, 3), (2, 2)],
            [(1, 1), (Q(1), 1)],
            [(33, 1)],
            [(1, 1, 1)],
        ):
            with self.assertRaises(ValueError):
                M.finite_control(nodes, 1)

    def test_18_matrix_and_polynomial_guards(self):
        for a in ([], [[]], [[1, 2]], [[True]], [[1]] * 5):
            with self.assertRaises(ValueError):
                M.matrix(a)
        for cap in (True, 5, 1.0):
            with self.assertRaises(ValueError):
                M.matrix([[1]], max_size=cap)
        with self.assertRaises(ValueError):
            M.solve([[0]], [1], M.Budget())
        with self.assertRaises(ValueError):
            M.poly_mul([1] * 5, [1] * 2, M.Budget())
        with self.assertRaises(ValueError):
            M.product_polynomial([1] * 5, M.Budget())
        with self.assertRaises(ValueError):
            M.product_polynomial([], object())

    def test_19_work_cap_precharged(self):
        work = M.Budget(1)
        with self.assertRaises(ValueError):
            M.gram_data([(1, 2)], 1, work)
        self.assertEqual(work.used, 0)
        for v in (True, 0, 200001, 1.0):
            with self.assertRaises(ValueError):
                M.Budget(v)
        with self.assertRaises(ValueError):
            M.finite_control([(1, 1)], 1, object())

    def test_20_scalar_and_prefix_domains(self):
        calls = [
            lambda: M.factor_control(33, 1, 0, 1),
            lambda: M.factor_control(0, 1, 0, 0),
            lambda: M.real_inequality_control(Q(3, 4), 1, 1),
            lambda: M.delay_control(1, -1),
            lambda: M.delay_control(1, True),
            lambda: M.lacunary_control(True),
            lambda: M.lacunary_control(9),
            lambda: M.product_control([(0, 1, 0, 1)] * 9),
        ]
        for f in calls:
            with self.assertRaises(ValueError):
                f()

    def test_21_sources_and_artifact_locks(self):
        M.authenticated_sources()
        self.assertEqual(len(M.BINDINGS), 2)
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for path, digest in self.report["artifact_sha256_lf"].items():
            raw = (
                (ROOT / path).read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            )
            self.assertEqual(hashlib.sha256(raw).hexdigest(), digest)

    def test_22_manifest_semantic_and_type_tampering(self):
        for field, value in (
            ("object", "physical"),
            ("height", "weighted"),
            ("Xi_corollary", "unconditional"),
        ):
            manifest = M.expected_manifest()
            manifest["primitive_contract"][field] = value
            with self.assertRaises(ValueError):
                M.authenticated_sources(manifest)
        manifest = M.expected_manifest()
        manifest["external_context"][0]["remote_bytes_authenticated"] = 0
        with self.assertRaises(ValueError):
            M.authenticated_sources(manifest)

    def test_23_primitive_bytes_fail_closed(self):
        with (
            patch.object(M.subprocess, "check_output", side_effect=[b"1", b"x"]),
            self.assertRaisesRegex(ValueError, "primitive identity"),
        ):
            M.authenticated_sources()
        with patch.object(
            M.subprocess, "check_output", return_value=b"2000001"
        ) as mocked:
            with self.assertRaisesRegex(ValueError, "byte cap"):
                M.authenticated_sources()
            self.assertEqual(mocked.call_count, 1)

    def test_24_duplicate_nonfinite_and_float_JSON(self):
        for raw in (
            b'{"x":1,"x":2}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b'{"x":1.0}',
            b'{"x":1e3}',
            b"{",
        ):
            with self.assertRaises(ValueError):
                M.parse_json(raw)

    def test_25_JSON_size_shape_and_depth(self):
        for raw in (b" " * 2000001, b"[" * 26 + b"0" + b"]" * 26):
            with self.assertRaises(ValueError):
                M.parse_json(raw)
        for data in ([0] * 1025, {"x": "a" * 4097}, 2**4096, {1: "x"}):
            with self.assertRaises(ValueError):
                M.canonical(data)

    def test_26_LF_stability_and_manifest_copy(self):
        self.assertEqual(M.lf_sha(b"a\r\nb\r"), M.lf_sha(b"a\nb\n"))
        manifest = M.expected_manifest()
        manifest["frozen_sources"][0]["commit"] = "x"
        self.assertNotEqual(M.BINDINGS[0]["commit"], "x")
        self.assertEqual(M.parse_json(M.MANIFEST.read_bytes()), M.expected_manifest())

    def test_27_digest_tamper_and_reseal(self):
        data = copy.deepcopy(self.report)
        data["payload_sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            M.validate_report(data)
        with self.assertRaises(ValueError):
            M.seal(self.report)

    def test_28_resealed_mathematical_tampering(self):
        variants = []
        for field, value in (
            ("origin", "0"),
            ("shifted_Gram_trace", "1"),
            ("horizontal_defect_integral_over_4pi_y", "2"),
            ("log_integral_over_2pi", "7"),
            ("Lyapunov_verified", 1),
        ):
            data = copy.deepcopy(self.report)
            data.pop("payload_sha256")
            data["finite_Gram_bridge_controls"][0][field] = value
            variants.append(data)
        with patch.object(M, "build_report", return_value=self.report):
            for data in variants:
                with self.assertRaisesRegex(ValueError, "typed reconstruction"):
                    M.validate_report(M.seal(data))

    def test_29_resealed_scope_type_and_cap_tampering(self):
        variants = []
        for section, key, value in (
            ("scope", "bare_U_equals_one", False),
            ("scope", "corrected_P_U_physical_capture", True),
            ("scope", "native_reduced_denominator_determined", True),
            ("scope", "infinite_height_implies_every_shifted_band_infinite", True),
            ("scope", "numerical_transcendental_samples", False),
            ("caps", "work", True),
        ):
            data = copy.deepcopy(self.report)
            data.pop("payload_sha256")
            data[section][key] = value
            variants.append(data)
        with patch.object(M, "build_report", return_value=self.report):
            for data in variants:
                with self.assertRaises(ValueError):
                    M.validate_report(M.seal(data))

    def test_30_exact_taxonomy_and_coverage(self):
        self.assertEqual(self.report["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.report["arithmetic_components"],
            ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        )
        self.assertEqual(self.report["coverage"]["confluent_Gram_models"], 7)
        self.assertLessEqual(self.report["coverage"]["charged_work"], M.MAX_WORK)
        self.assertIn("no rounding", self.report["rounding_contract"])

    def test_31_scope_firewalls(self):
        scope = self.report["scope"]
        for key in (
            "meromorphic_real_boundary_extension_required",
            "infinite_height_implies_every_shifted_band_infinite",
            "arbitrary_inner_numerator_lower_bound",
            "corrected_P_U_physical_capture",
            "native_reduced_denominator_determined",
            "RH_or_critical_line_claim",
            "analytic_limits_machine_certified",
            "novelty_or_new_abstract_theory_claim",
        ):
            self.assertIs(scope[key], False)
        self.assertIs(scope["Xi_unreduced_corollary_requires_GH_premise"], True)
        self.assertEqual(scope["band"], "[0,L], fixed L>0")

    def test_32_no_assert_float_or_transcendental_calls(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(n, ast.Assert) for n in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(n, ast.Constant) and type(n.value) is float
                for n in ast.walk(tree)
            )
        )
        prohibited = {"exp", "log", "sqrt", "gamma", "sin", "cos"}
        self.assertFalse(
            any(
                isinstance(n, ast.Call)
                and isinstance(n.func, ast.Attribute)
                and n.func.attr in prohibited
                for n in ast.walk(tree)
            )
        )


if __name__ == "__main__":
    unittest.main()
