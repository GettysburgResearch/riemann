"""Independent finite expansions and hostile source/cancellation guards."""

import ast
import copy
import hashlib
import importlib.util
import math
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "research/exploratory/xi_companion_generic_parameter_coprimality.py"
SPEC = importlib.util.spec_from_file_location("generic_coprimality", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def power(x, n):
    answer = (F(1), F(0))
    for _ in range(n):
        answer = mul(answer, x)
    return answer


def shifted(row, point):
    # Binomial translation, independent of producer derivative evaluation.
    return [
        tuple(
            sum(
                row[n] * math.comb(n, j) * power(point, n - j)[part]
                for n in range(j, len(row))
            )
            for part in (0, 1)
        )
        for j in range(len(row))
    ]


def independent_companion(row, point, lam, sign):
    jet = shifted(row, point) + [(F(0), F(0))]
    return [
        add(jet[j], mul((0, sign * lam * (j + 1)), jet[j + 1])) for j in range(len(row))
    ]


def independent_w(row):
    out = [F(0)] * max(1, 2 * len(row) - 7)

    def falling(n, d):
        return math.factorial(n) // math.factorial(n - d) if n >= d else 0

    for n, a in enumerate(row):
        for m, b in enumerate(row):
            degree = n + m - 6
            if degree >= 0:
                out[degree] += a * b * (falling(m, 6) - n * falling(m, 5))
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


class GenericCoprimalityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def test_01_fixture(self):
        actual = M.parse_json(M.FIXTURE.read_bytes())
        self.assertEqual(M.canonical(actual), M.canonical(self.report))
        M.validate_report(actual)

    def test_02_frozen_sources(self):
        self.assertEqual(M.authenticated_sources(), 6)
        self.assertEqual(
            {v["id"] for v in M.BINDINGS}, {"NA", "GH", "XL", "LP", "CP", "L106620"}
        )
        self.assertEqual(M.expected_manifest(), M.parse_json(M.MANIFEST.read_bytes()))

    def test_03_genuine_control(self):
        row = M.control("genuine", (0, 1), 1, M.Budget())
        self.assertTrue(row["criterion"])
        self.assertEqual(row["ratio_f_over_ifprime"], (1, 0))
        self.assertEqual(row["Theta0_local"]["genuine_zero_order"], 1)
        self.assertEqual(row["Theta5_local"]["genuine_zero_order"], 1)
        self.assertEqual(row["W_zero_order"], 1)

    def test_04_Wzero_is_not_enough(self):
        row = M.control("genuine", (0, 1), F(1, 2), M.Budget())
        self.assertEqual(row["W_value"], (0, 0))
        self.assertTrue(row["fprime_gprime_nonzero"])
        self.assertFalse(row["genuine_common_zero"])

    def test_05_nonreal_ratio(self):
        row = M.control("genuine", (1, 1), 1, M.Budget())
        self.assertNotEqual(row["ratio_f_over_ifprime"][1], 0)
        self.assertFalse(row["criterion"])

    def test_06_excess_W_multiplicity(self):
        row = M.control("excess_W_order", (0, 1), 1, M.Budget())
        self.assertTrue(row["genuine_common_zero"])
        self.assertEqual(row["W_zero_order"], 3)
        self.assertEqual(row["Theta0_local"]["genuine_zero_order"], 1)
        self.assertEqual(row["Theta5_local"]["genuine_zero_order"], 1)

    def test_07_cancelled_common_raw(self):
        for lam in (F(1, 2), F(1), F(2), F(7, 3)):
            row = M.control("cancelled_raw", (0, 1), lam, M.Budget())
            self.assertEqual(row["W_value"], (0, 0))
            self.assertFalse(row["fprime_gprime_nonzero"])
            self.assertFalse(row["genuine_common_zero"])
            for name in ("Theta0_local", "Theta5_local"):
                self.assertEqual(row[name]["h_zero_order"], 2)
                self.assertEqual(row[name]["numerator_order"], 1)
                self.assertEqual(row[name]["denominator_order"], 1)
                self.assertEqual(row[name]["regular_nonzero_value"], (-1, 0))

    def test_08_every_internal_multiplicity(self):
        for r in range(1, 9):
            row = M.cancellation_control(r, F(5, 7), M.Budget())
            self.assertEqual(row["local"]["internal_cancelled_order"], r - 1)
            self.assertEqual(row["local"]["regular_nonzero_value"], (-1, 0))

    def test_09_independent_shifted_local_jets(self):
        for row in M.CONTROLS.values():
            for b in ((F(0), F(1)), (F(1, 2), F(3, 2))):
                for lam in (F(1), F(2, 3)):
                    local = M.local_quotient(row, b, lam, M.Budget())
                    for sign, key in (
                        (-1, "numerator_order"),
                        (1, "denominator_order"),
                    ):
                        coefficients = independent_companion(row, b, lam, sign)
                        order = next(
                            j for j, value in enumerate(coefficients) if value != (0, 0)
                        )
                        self.assertEqual(local[key], order)

    def test_10_independent_W_coefficient_formula(self):
        for row in M.CONTROLS.values():
            self.assertEqual(M.wronskian(row, M.Budget()), independent_w(row))
        extra = [F(3, 5), 0, -7, 0, 2, 0, -3, 0, 1]
        self.assertEqual(M.wronskian(extra, M.Budget()), independent_w(extra))

    def test_11_closed_W_polynomials(self):
        self.assertEqual(
            M.wronskian(M.CONTROLS["genuine"], M.Budget()),
            [-3600, 0, 0, 0, 0, 0, -3600],
        )
        self.assertEqual(
            M.wronskian(M.CONTROLS["excess_W_order"], M.Budget()),
            [-3600, 0, -10800, 0, -10800, 0, -3600],
        )

    def test_12_independent_cross_product_at_complex_points(self):
        for row in M.CONTROLS.values():
            for point in ((F(1), F(2)), (F(-2), F(3, 2))):
                jet = shifted(row, point)
                f, fp = jet[0], jet[1]
                g = tuple(math.factorial(5) * x for x in jet[5])
                gp = tuple(math.factorial(6) * x for x in jet[6])
                lam = F(2, 3)
                r0, c0 = add(f, mul((0, -lam), fp)), add(f, mul((0, lam), fp))
                r5, c5 = add(g, mul((0, -lam), gp)), add(g, mul((0, lam), gp))
                lhs = add(mul(r0, c5), tuple(-x for x in mul(c0, r5)))
                rhs = mul((0, 2 * lam), shifted(independent_w(row), point)[0])
                self.assertEqual(lhs, rhs)
                self.assertTrue(
                    M.exact_bridge(row, lam, M.Budget())[
                        "R5_equals_fifth_derivative_R0"
                    ]
                )

    def test_13_constant_parameter_derivative_link(self):
        row = M.CONTROLS["cancelled_raw"]
        lam = F(3, 2)
        r0 = M.companion_coefficients(row, lam, -1, M.Budget())
        direct = [
            tuple(math.prod(range(n - 4, n + 1)) * x for x in r0[n])
            for n in range(5, len(r0))
        ]
        g = M.derivative(row, 5, M.Budget())
        self.assertEqual(direct, M.companion_coefficients(g, lam, -1, M.Budget()))

    def test_14_actual_phase_algebra_not_values(self):
        for a, b in ((1, 2), (F(1, 3), F(7, 5))):
            row = M.moment_control(a, b)
            self.assertEqual(row["i_power6"], (-1, 0))
            self.assertEqual(row["W0"], (-a * b, 0))
            self.assertFalse(row["actual_Xi_moments_evaluated"])

    def test_15_positive_moment_truncation_control(self):
        # A nonnative even atomic measure, only to test the sign identity.
        moments = [
            sum(2 * weight * node**r for node, weight in ((F(1), F(2)), (F(3), F(1))))
            for r in range(0, 9, 2)
        ]
        polynomial = [F(0)] * 9
        for j, mu in enumerate(moments):
            polynomial[2 * j] = (-1) ** j * mu / math.factorial(2 * j)
        w = M.wronskian(polynomial, M.Budget())
        self.assertEqual(w[0], -moments[0] * moments[3])

    def test_16_singleton_model_factorization(self):
        # lambda^6-1=(lambda-1)(1+...+lambda^5); all latter terms positive.
        factor = [5, 0, -1]
        cube = M.real_product(
            M.real_product(factor, factor, M.Budget()), factor, M.Budget()
        )
        self.assertEqual(cube, M.CONTROLS["real_rooted_common"])
        real_rooted = M.control("real_rooted_common", (0, 1), 1, M.Budget())
        self.assertTrue(real_rooted["genuine_common_zero"])
        self.assertEqual(real_rooted["W_zero_order"], 1)
        self.assertEqual(
            M.real_product([-1, 1], [1] * 6, M.Budget()), [-1, 0, 0, 0, 0, 0, 1]
        )
        for lam in (F(1, 3), F(1), F(3)):
            row = M.control("genuine", (0, lam), lam, M.Budget())
            self.assertEqual(row["genuine_common_zero"], lam == 1)

    def test_17_minimum_not_equality(self):
        for row in self.report["local_derivative_linked_controls"]:
            if row["genuine_common_zero"]:
                minimum = min(
                    row["Theta0_local"]["genuine_zero_order"],
                    row["Theta5_local"]["genuine_zero_order"],
                )
                self.assertLessEqual(minimum, row["W_zero_order"])
        self.assertEqual(
            self.report["local_derivative_linked_controls"][3]["W_zero_order"], 3
        )

    def test_18_scope_and_taxonomy(self):
        self.assertEqual(self.report["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.report["arithmetic_components"],
            ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
        )
        for row in self.report["local_derivative_linked_controls"]:
            self.assertFalse(row["native_Xi"])
            self.assertFalse(row["positive_kernel_surrogate"])
        self.assertFalse(self.report["scope"]["explicit_good_parameter"])

    def test_19_strict_scalar_guards(self):
        for v in (True, False, 1.0, "1", 2**32, F(1, 2**32)):
            with self.assertRaises(ValueError):
                M.rational(v)
        for v in (True, 0, -1):
            with self.assertRaises(ValueError):
                M.moment_control(v, 1)
        with self.assertRaises(ValueError):
            M.rational(F(1, 2**4096), internal=True)

    def test_20_polynomial_point_scale_guards(self):
        for row in ([], [0] * 18, [True], [1.0]):
            with self.assertRaises(ValueError):
                M.polynomial(row)
        for point in ((0,), (0, 1, 2), (0, True), (0, 0), (0, -1)):
            with self.assertRaises(ValueError):
                M.control("genuine", point, 1, M.Budget())
        for lam in (0, -1, True, 1.0):
            with self.assertRaises(ValueError):
                M.control("genuine", (0, 1), lam, M.Budget())

    def test_21_Gaussian_exactness_and_caps(self):
        self.assertEqual(M.divide((3, 4), (1, -2)), (F(-1), F(2)))
        for value in ((1,), (1, 2, 3), (True, 1), (1.0, 2)):
            with self.assertRaises(ValueError):
                M.gauss(value)
        with self.assertRaises(ValueError):
            M.divide((1, 0), (0, 0))
        with self.assertRaises(ValueError):
            M.times((2**4095, 0), (2, 0))

    def test_22_degree_and_work_caps(self):
        work = M.Budget(1)
        with self.assertRaisesRegex(ValueError, "before expansion"):
            M.control("genuine", (0, 1), 1, work)
        self.assertEqual(work.used, 0)
        for value in (True, 0, M.MAX_WORK + 1):
            with self.assertRaises(ValueError):
                M.Budget(value)
        with self.assertRaises(ValueError):
            M.real_product([1] * 18, [1] * 18, M.Budget())
        with self.assertRaises(ValueError):
            M.derivative([1], True, M.Budget())

    def test_23_source_byte_tamper_and_cap(self):
        real = M.subprocess.check_output

        def changed(args, **kw):
            raw = real(args, **kw)
            return raw + b"\n#change" if args[:2] == ["git", "show"] else raw

        with (
            patch.object(M.subprocess, "check_output", side_effect=changed),
            self.assertRaisesRegex(ValueError, "primitive identity"),
        ):
            M.authenticated_sources()
        with (
            patch.object(M.subprocess, "check_output", return_value=b"2000001"),
            self.assertRaisesRegex(ValueError, "byte cap"),
        ):
            M.authenticated_sources()

    def test_24_manifest_closed_schema(self):
        for field in ("exceptional_set", "conditional", "downstream", "lambda"):
            bad = M.expected_manifest()
            bad["primitive_contract"][field] = "unconditional physical theorem"
            with self.assertRaises(ValueError):
                M.authenticated_sources(bad)
        bad = M.expected_manifest()
        bad["extra"] = True
        with self.assertRaises(ValueError):
            M.authenticated_sources(bad)

    def test_25_artifact_seals_controls(self):
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for path, value in self.report["artifact_sha256_lf"].items():
            raw = (ROOT / path).read_bytes()
            self.assertEqual(M.lf_sha(raw), value)
            self.assertFalse(any(x < 32 and x not in (9, 10, 13) for x in raw))
        with (
            patch.object(Path, "read_bytes", return_value=b"\x0c"),
            self.assertRaises(ValueError),
        ):
            M.artifact_hashes()

    def test_26_payload_digest(self):
        payload = {k: v for k, v in self.report.items() if k != "payload_sha256"}
        self.assertEqual(
            hashlib.sha256(M.canonical(payload).encode()).hexdigest(),
            self.report["payload_sha256"],
        )
        bad = copy.deepcopy(self.report)
        bad["scope"]["explicit_good_parameter"] = True
        with self.assertRaisesRegex(ValueError, "payload digest"):
            M.validate_report(bad)

    def test_27_fresh_resealed_semantic_rejection(self):
        for path, value in (
            (
                ("scope", "corrected_physical_capture_or_fixed_lambda_HS_divergence"),
                True,
            ),
            (("scope", "exact_common_zero_equivalence"), 1),
            (("local_derivative_linked_controls", 4, "genuine_common_zero"), True),
        ):
            bad = copy.deepcopy(self.report)
            bad.pop("payload_sha256")
            target = bad
            for key in path[:-1]:
                target = target[key]
            target[path[-1]] = value
            with self.assertRaisesRegex(ValueError, "typed reconstruction"):
                M.validate_report(M.seal(bad))

    def test_28_JSON_firewalls(self):
        for raw in (
            b'{"a":1,"a":2}',
            b'{"a":NaN}',
            b'{"a":1.0}',
            b'{"a":1e9999}',
            b"\xff",
        ):
            with self.assertRaises(ValueError):
                M.parse_json(raw)
        self.assertEqual(M.lf_sha(b"a\r\nb\r\n"), M.lf_sha(b"a\nb\n"))

    def test_29_JSON_resource_caps(self):
        for value in ([0] * 1025, "x" * 4097, 2**4096, [[0] * 1000 for _ in range(21)]):
            with self.assertRaises(ValueError):
                M.canonical(value)
        deep = 0
        for _ in range(25):
            deep = [deep]
        with self.assertRaises(ValueError):
            M.canonical(deep)
        with self.assertRaises(ValueError):
            M.normalized(b"x" * (M.MAX_BYTES + 1))

    def test_30_no_float_assert_exec_or_analytic_sampling(self):
        tree = ast.parse(SOURCE.read_text())
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
                    name, {"complex", "float", "exec", "eval", "log", "exp", "gamma"}
                )

    def test_31_written_boundaries(self):
        note = M.NOTE.read_text(encoding="utf-8")
        for token in (
            "possibly empty",
            "E may be dense",
            "no open stability",
            "CP gives an explicit",
            "A countable prescribed sequence",
            "NO RH assumption",
            "not just two vanishing raw numerators",
        ):
            self.assertIn(token, note)
        self.assertFalse(self.report["scope"]["RH_or_density_conclusion"])

    def test_32_nonzero_and_enum_guards(self):
        for name in (True, None, "../genuine", "new"):
            with self.assertRaises(ValueError):
                M.control(name, (0, 1), 1, M.Budget())
        with self.assertRaises(ValueError):
            M.order_at([0], (0, 1), M.Budget())
        with self.assertRaises(ValueError):
            M.local_quotient([0], (0, 1), 1, M.Budget())
        with self.assertRaises(ValueError):
            M.cancellation_control(9, 1, M.Budget())
        self.assertLessEqual(self.report["coverage"]["charged_work"], M.MAX_WORK)


if __name__ == "__main__":
    unittest.main()
