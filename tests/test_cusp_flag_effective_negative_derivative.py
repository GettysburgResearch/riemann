"""Independent source reconstruction and strict certificate rejection tests."""

import ast
import copy
import importlib.util
import itertools
import math
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/cusp_flag_effective_negative_derivative.py"
)
SPEC = importlib.util.spec_from_file_location("effective_derivative", PATH)
P = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(P)


def independent_source(n=64):
    # Delta/q logarithmic derivative, independent of E4^3-E6^2.
    product = [1]
    for j in range(1, n):
        sigma = lambda h: sum(d for d in range(1, h + 1) if h % d == 0)
        numerator = -24 * sum(sigma(h) * product[j - h] for h in range(1, j + 1))
        if numerator % j:
            raise ValueError("independent Delta integrality")
        product.append(numerator // j)
    delta = [0] + product

    def mul(a, b):
        out = [0] * (n + 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b[: n + 1 - i]):
                out[i + j] += x * y
        return out

    e4 = [1] + [
        240 * sum(d**3 for d in range(1, j + 1) if j % d == 0) for j in range(1, n + 1)
    ]
    b = mul(delta, delta)
    a = mul(delta, mul(e4, mul(e4, e4)))
    return tuple(delta), tuple(x - 696 * y for x, y in zip(a, b)), tuple(b)


def convolution_prefix(g, b):
    cutoff = Q(12)

    def mul(a, c):
        out = {}
        for rho, x in a.items():
            for eta, y in c.items():
                if rho * eta <= cutoff:
                    out[rho * eta] = out.get(rho * eta, 0) + x * y
        return out

    u = {Q(n, 2): -(b[n] ** 2) for n in range(3, 25)}
    inverse = {Q(1): 1}
    power = {Q(1): 1}
    for _ in range(2):
        power = mul(power, u)
        for rho, x in power.items():
            inverse[rho] = inverse.get(rho, 0) + x
    square = {}
    for n, m in itertools.product(range(3, 9), repeat=2):
        if Q(n * m, 2) <= cutoff:
            rho = Q(n * m, 2)
            square[rho] = square.get(rho, 0) + g[n] * b[n] * g[m] * b[m]
    correction = mul(square, inverse)
    f = {Q(n): g[n] ** 2 for n in range(1, 13)}
    for rho, x in correction.items():
        f[rho] = f.get(rho, 0) - x
    f = {rho: x for rho, x in f.items() if x}
    ell = mul(f, {Q(d * d): d**46 for d in range(1, 4)})
    return f, {rho: x for rho, x in ell.items() if x}


class EffectiveDerivativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = P.q_source()
        cls.prefix = P.frequency_prefix(cls.source["g"], cls.source["b"])
        cls.mass = P.mass_certificate(cls.source["g"], cls.source["b"])
        cls.report = P.build_report()

    def test_01_full_fixture(self):
        P.validate_report(P.parse_json(P.FIXTURE.read_bytes()), self.report)

    def test_02_independent_q64(self):
        delta, g, b = independent_source()
        self.assertEqual(
            (delta, g, b), (self.source["delta"], self.source["g"], self.source["b"])
        )

    def test_03_independent_full_frequency_maps(self):
        f, ell = convolution_prefix(self.source["g"], self.source["b"])
        self.assertEqual((f, ell), (self.prefix["F"], self.prefix["L"]))

    def test_04_prefix_coverage(self):
        self.assertEqual(sum(self.prefix["ordered_word_counts"]), 27)
        self.assertEqual(self.prefix["next_depth_minimum"], Q(243, 16))
        self.assertEqual((len(self.prefix["F"]), len(self.prefix["L"])), (17, 17))

    def test_05_target_and_zeta_term(self):
        self.assertEqual(self.prefix["F"][Q(9, 2)], -((-48 * 195660) ** 2))
        self.assertEqual(self.prefix["L"][Q(9, 2)], P.ATOM)
        self.assertEqual(self.prefix["L"][Q(4)] - self.prefix["F"][Q(4)], 2**46)

    def test_06_global_majorant_constants(self):
        self.assertLessEqual(2160, 2**12)
        self.assertLessEqual(75600, 2**17)
        self.assertLessEqual(2**36 + 2**34, 1728 * 2**26)
        for n in range(1, 129):
            self.assertLessEqual(math.comb(n + 23, 23), 24 * n**23)

    def test_07_tail_rationals(self):
        rows = self.mass["rows"]
        self.assertEqual(
            rows["B_nonconstant"]["tail_rational_upper"], Q(1, 49 * 2**104)
        )
        self.assertEqual(rows["C_absolute"]["tail_rational_upper"], Q(1, 49 * 2**115))
        self.assertEqual(rows["U_absolute"]["tail_rational_upper"], Q(1, 49 * 2**30))

    def test_08_mass_pivot_excluded(self):
        self.assertLess(
            self.mass["rows"]["U_absolute"]["total_dyadic_upper"], Q(1, 2**30)
        )
        self.assertEqual(
            (self.mass["F_absolute_mass_upper"], self.mass["L_absolute_mass_upper"]),
            (2, 4),
        )

    def test_09_dyadic_rounding(self):
        for v in (Q(0), Q(1, 3), Q(17, 31), Q(123456, 7)):
            r = P.dyadic_upper(v, 40)
            self.assertLessEqual(v, r)
            self.assertLess(r - v, Q(1, 2**40))

    def test_10_log_identity_at_one(self):
        self.assertEqual(P.log_interval(Q(1)), (0, 0))

    def test_11_log_two_elementary_enclosure(self):
        lo, hi = P.log_interval(Q(2))
        self.assertGreater(lo, Q(69, 100))
        self.assertLess(hi, Q(7, 10))

    def test_12_independent_log_refinement(self):
        for value in (Q(3), Q(4), Q(9, 2), Q(5), Q(81, 8), Q(12)):
            u = (value - 1) / (value + 1)
            lower = 2 * sum(u ** (2 * j + 1) / (2 * j + 1) for j in range(96))
            upper = lower + 2 * u**193 / (193 * (1 - u * u))
            lo, hi = P.log_interval(value)
            self.assertLessEqual(lo, lower)
            self.assertLessEqual(upper, hi)

    def test_13_kernel_exponents(self):
        self.assertEqual(
            [P.kernel_gap(Q(n))["power_two_exponent"] for n in (4, 5, 12)],
            [35, 26, 1506],
        )

    def test_14_interval_gap_direction(self):
        for rho in self.prefix["F"]:
            if rho not in (1, P.STAR):
                g = P.kernel_gap(rho)
                a, b = g["ratio_interval"]
                self.assertTrue(b < 1 or a > 1)
                self.assertGreater(g["log_kernel_loss_lower"], 0)

    def test_15_exact_error_margins(self):
        cert = self.report["derivative_certificate"]["functions"]
        self.assertEqual(cert["F"]["normalized_error_integer_upper"], 345729874)
        self.assertEqual(cert["L"]["normalized_error_integer_upper"], 512443888)
        self.assertEqual(cert["F"]["normalized_derivative_upper"], -88203307492526)
        self.assertEqual(cert["L"]["normalized_derivative_upper"], -88203140778512)

    def test_16_tail_integer_majorant(self):
        cert = self.report["derivative_certificate"]["functions"]
        self.assertEqual(
            (cert["F"]["tail_integer_upper"], cert["L"]["tail_integer_upper"]), (1, 1)
        )
        self.assertLess(4 * Q(9, 2) ** 96, 2**1506)

    def test_17_low_order_does_not_pass(self):
        with self.assertRaises(ValueError):
            P.derivative_certificate(
                {name: self.prefix[name] for name in ("F", "L")}, self.mass, order=1
            )

    def test_18_source_authentication(self):
        self.assertEqual(
            P.authenticate()["schema"], "rankin-selberg-quotient-global-parent-v1"
        )
        actual = P.subprocess.check_output

        def changed_source(command, **kwargs):
            result = actual(command, **kwargs)
            return result + b"\n" if command[1] == "show" else result

        with (
            mock.patch.object(P.subprocess, "check_output", side_effect=changed_source),
            self.assertRaisesRegex(ValueError, "frozen Git blob/LF"),
        ):
            P.authenticate()

    def test_19_manifest_drift(self):
        for key, value in (("authoring_base", "0" * 40), ("extra", False)):
            manifest = copy.deepcopy(P.expected_manifest())
            manifest[key] = value
            with self.assertRaises(ValueError):
                P.authenticate(manifest)

    def test_20_q_type_caps(self):
        for value in (True, 11, 65, 12.0, Q(12), "64"):
            with self.assertRaises(ValueError):
                P.q_source(value)

    def test_21_polynomial_shape_caps(self):
        for value in ([0] * 13, (0,) * 12, (True,) * 13, (2**513,) * 13):
            with self.assertRaises(ValueError):
                P.polynomial(value, 12)

    def test_22_cutoff_caps(self):
        for value in (True, Q(13), Q(4), 12.0, Q(2**33, 2**32)):
            with self.assertRaises(ValueError):
                P.frequency_prefix(self.source["g"], self.source["b"], value)

    def test_23_log_caps(self):
        for value in (True, Q(0), Q(13), 2.0):
            with self.assertRaises(ValueError):
                P.log_interval(value)
        for terms in (True, 0, 65):
            with self.assertRaises(ValueError):
                P.log_interval(Q(2), terms)
        for bits in (True, 0, 41):
            with self.assertRaises(ValueError):
                P.log_interval(Q(2), bits=bits)

    def test_24_order_caps(self):
        for order in (True, 0, 8193, 8192.0):
            with self.assertRaises(ValueError):
                P.kernel_gap(Q(4), order)
        for rho in (Q(1), Q(9, 2)):
            with self.assertRaises(ValueError):
                P.kernel_gap(rho)
        maps = {name: dict(self.prefix[name]) for name in ("F", "L")}
        maps["F"] = {Q(1) + Q(j, 1000): 1 for j in range(65)}
        with self.assertRaises(ValueError):
            P.derivative_certificate(maps, self.mass, work=P.Budget(1))
        maps = {name: dict(self.prefix[name]) for name in ("F", "L")}
        maps["F"][Q(4)] = 2**513
        with self.assertRaises(ValueError):
            P.derivative_certificate(maps, self.mass)
        mass = dict(self.mass)
        mass["F_absolute_mass_upper"] = 2.0
        with self.assertRaisesRegex(ValueError, "fixed certified mass"):
            P.derivative_certificate(
                {name: self.prefix[name] for name in ("F", "L")}, mass
            )

    def test_25_budget_and_rational_caps(self):
        with self.assertRaises(ValueError):
            P.q_source(work=P.Budget(1))
        for value in (True, 1.0, "1", Q(1, 2**33)):
            with self.assertRaises(ValueError):
                P.rational(value)
        with self.assertRaises(ValueError):
            P.rational(2**8192, internal=True)
        with self.assertRaises(ValueError):
            P.rational(1, internal=1)

    def test_26_bad_json(self):
        for raw in (
            b'{"x":1,"x":2}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b'{"x":1.0}',
            b"\xff",
            b"[" * 18 + b"0" + b"]" * 18,
            b" " * (P.MAX_BYTES + 1),
        ):
            with self.assertRaises(ValueError):
                P.parse_json(raw)

    def test_27_resealed_report_drift(self):
        for mutation in (
            lambda r: r.update(extra=False),
            lambda r: r["coverage"].update(F_atoms=True),
            lambda r: r["scope"].update(completed_Q_claim=0),
            lambda r: r["derivative_certificate"]["functions"]["F"].update(
                normalized_error_integer_upper=1
            ),
            lambda r: r["q_rows"][2].__setitem__(2, 0),
            lambda r: r["source_bindings"][0].update(git_blob="0" * 40),
            lambda r: r["artifact_sha256_lf"].update(
                {next(iter(r["artifact_sha256_lf"])): "0" * 64}
            ),
        ):
            report = copy.deepcopy(self.report)
            report.pop("payload_sha256")
            mutation(report)
            changed = P.seal(report)
            with self.assertRaises(ValueError):
                P.validate_report(changed, self.report)

    def test_28_digest_and_missing_field(self):
        for key in ("payload_sha256", "absolute_mass", "source_bindings"):
            report = copy.deepcopy(self.report)
            report.pop(key)
            with self.assertRaises(ValueError):
                P.validate_report(report, self.report)

    def test_29_no_result_assert_or_float(self):
        tree = ast.parse(PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(n, ast.Assert) for n in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(n, ast.Constant) and type(n.value) is float
                for n in ast.walk(tree)
            )
        )

    def test_30_scope_and_work(self):
        self.assertFalse(self.report["scope"]["exact_derivative_value_sampled"])
        self.assertFalse(self.report["scope"]["completed_Q_claim"])
        self.assertTrue(self.report["scope"]["all_omitted_words_bounded"])
        self.assertLess(self.report["coverage"]["work_units"], P.MAX_WORK)
        self.assertEqual(self.report["derivative_certificate"]["order"], 8192)


if __name__ == "__main__":
    unittest.main()
