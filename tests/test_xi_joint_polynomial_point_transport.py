"""Bounded scientific replay and adversarial controls for the selected JP point."""

import ast
import copy
import importlib.util
import math
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "research/exploratory"
sys.path.insert(0, str(HERE))
SPEC = importlib.util.spec_from_file_location(
    "jp", HERE / "xi_joint_polynomial_point_transport.py"
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def q(pair):
    return Q(*pair)


def reseal(value):
    value = copy.deepcopy(value)
    value.pop("payload_sha256", None)
    value["payload_sha256"] = M.oa.digest(M.canonical(value))
    return value


class JointPolynomialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.decode(M.FIXTURE.read_bytes())
        cls.record = cls.report["record"]

    def test_01_full_fresh_replay(self):
        self.assertTrue(M.check_report(self.report))

    def test_02_authenticate_literal_sources_runtime(self):
        M.authenticate()
        self.assertEqual(len(M.BINDINGS), 8)

    def test_03_exact64_coverage(self):
        arcs = self.record["arcs"]
        self.assertEqual([a["index"] for a in arcs], list(range(64)))
        self.assertEqual(q(arcs[0]["pi_interval"][0]), 0)
        self.assertEqual(q(arcs[-1]["pi_interval"][1]), 2)
        for j, arc in enumerate(arcs):
            self.assertEqual(list(map(q, arc["pi_interval"])), [Q(j, 32), Q(j + 1, 32)])
            if j:
                self.assertEqual(arcs[j - 1]["pi_interval"][1], arc["pi_interval"][0])

    def test_04_every_exact_strict_comparison(self):
        for arc in self.record["arcs"]:
            self.assertIs(arc["strict_pass"], True)
            self.assertLess(q(arc["error_upper"]), q(arc["margin_lower"]))
            self.assertEqual(
                q(arc["error_upper"]), q(arc["polynomial_upper"]) + q(arc["tail_upper"])
            )
            self.assertEqual(
                q(arc["error_over_margin"]),
                q(arc["error_upper"]) / q(arc["margin_lower"]),
            )

    def test_05_exact_explanatory_bounds(self):
        self.assertLess(
            max(q(a["error_over_margin"]) for a in self.record["arcs"]), Q(4, 5)
        )
        self.assertLess(
            q(self.record["parent_displacement_upper"])
            / q(self.record["radius_lower"]),
            Q(3, 10),
        )

    def test_06_full_unknown_t_not_midpoint(self):
        center = q(self.record["inherited_critical"]["center"])
        eps = q(self.record["inherited_critical"]["radius"])
        self.assertEqual(eps, Q(1, 2**120))
        self.assertLessEqual(q(self.record["T"][0]), center - eps)
        self.assertGreaterEqual(q(self.record["T"][1]), center + eps)
        self.assertLess(q(self.record["T"][0]), q(self.record["T"][1]))

    def test_07_signed40_and_source_equation(self):
        coeff = self.record["fresh_signed_Xi_coefficients_0_to39"]
        self.assertEqual(len(coeff), 40)
        for v in coeff:
            self.assertLessEqual(q(v["imag"][0]), 0)
            self.assertGreaterEqual(q(v["imag"][1]), 0)
        self.assertLessEqual(q(coeff[6]["real"][0]), 0)
        self.assertGreaterEqual(q(coeff[6]["real"][1]), 0)
        for v in self.record["fresh_joint_coefficients_0_to31"][:2]:
            self.assertEqual(v, {"real": [[0, 1], [0, 1]], "imag": [[0, 1], [0, 1]]})

    def test_08_inherited_cover_complete(self):
        cover = self.record["inherited_cover"]
        self.assertEqual(cover["finite_cells"], 256)
        self.assertEqual(cover["cells_attempted"], 256)
        self.assertEqual(cover["failed_cells"], [])
        self.assertEqual(len(cover["ordered_cell_stream_sha256"]), 64)

    def test_09_parent_full_rectangle_strict(self):
        self.assertIs(self.record["parent_matched"], True)
        self.assertLess(
            q(self.record["parent_displacement_upper"]), q(self.record["radius_lower"])
        )
        self.assertIs(self.record["matched_transport_certified"], True)

    def test_10_independent_rational_tail_comparison(self):
        with M.ha.precision(512):
            for h in (Q(1, 16), Q(1, 4), Q(1, 2), Q(3, 4)):
                m, lam, R, N = Q(3, 5), Q(2, 3), Q(7, 8), 32
                x = h / R
                exact = (
                    m
                    * x**N
                    * (
                        math.factorial(5) * math.comb(N + 5, 5) / (R**5 * (1 - x) ** 6)
                        + lam
                        * math.factorial(6)
                        * math.comb(N + 6, 6)
                        / (R**6 * (1 - x) ** 7)
                    )
                )
                upper = M.joint_tail(m, h, M.oa.qarb(lam))
                self.assertGreaterEqual(upper, exact)
                self.assertLess(upper - exact, exact / 2**450)

    def test_11_two_routes_exact_polynomial_controls(self):
        self.assertEqual(M.exact_controls(), self.report["exact_controls"])
        self.assertEqual(
            self.report["exact_controls"]["exact_polynomial_evaluation_equalities"], 8
        )
        self.assertEqual(self.report["exact_controls"]["binomial_inequalities"], 130)

    def test_12_horner_vs_direct_polynomial_sum(self):
        with M.ha.precision(512):
            coeff = [M.acb(j - 5, j + 2) for j in range(32)]
            z = M.acb(M.oa.qarb(Q(1, 8)), M.oa.qarb(Q(1, 16)))
            direct = sum((v * z**j for j, v in enumerate(coeff)), M.acb(0))
            self.assertTrue((M.horner(coeff, z) - direct).contains(0))

    def test_13_true_preregistration_correction(self):
        self.assertEqual(M.PREREG, "689a93971cdd741a2b154f9506672667aa1a32dc")
        self.assertEqual(M.CORRECTION, "f8003a2569ba8cd9c62516d6f72aa8dfca9ce7b4")
        self.assertEqual(M.manifest()["preregistration_correction"], M.CORRECTION)

    def test_14_fully_resealed_false_arc_freshly_rejected(self):
        attack = copy.deepcopy(self.report)
        attack["record"]["arcs"][0]["error_upper"] = [0, 1]
        with self.assertRaisesRegex(ValueError, "fresh primitive reconstruction"):
            M.check_report(reseal(attack))

    def test_15_fully_resealed_midpoint_jet_freshly_rejected(self):
        attack = copy.deepcopy(self.report)
        attack["record"]["T"][1] = copy.deepcopy(attack["record"]["T"][0])
        with self.assertRaisesRegex(ValueError, "fresh primitive reconstruction"):
            M.check_report(reseal(attack))

    def test_16_duplicate_keys(self):
        with self.assertRaises(ValueError):
            M.decode(b'{"x":1,"x":2}')

    def test_17_float_and_nonfinite_json(self):
        for text in (b'{"x":1.0}', b'{"x":1e2}', b'{"x":NaN}', b'{"x":Infinity}'):
            with self.assertRaises(ValueError):
                M.decode(text)

    def test_18_json_integer_cap(self):
        with self.assertRaises(ValueError):
            M.canonical({"x": 1 << 4097})

    def test_19_json_container_cap(self):
        with self.assertRaises(ValueError):
            M.canonical([0] * 4097)

    def test_20_json_depth_cap(self):
        value = 0
        for _ in range(26):
            value = [value]
        with self.assertRaises(ValueError):
            M.canonical(value)

    def test_21_json_bytes_type_cap(self):
        for raw in ("{}", bytearray(b"{}"), b" " * (M.MAX_BYTES + 1)):
            with self.assertRaises(ValueError):
                M.decode(raw)

    def test_22_string_and_key_guards(self):
        for value in ({"x": "a" * 4097}, {"x": "\u03bb"}, {1: "x"}, {"\u03bb": 1}):
            with self.assertRaises(ValueError):
                M.canonical(value)

    def test_23_strict_rational_pairs(self):
        for value in ([True, 1], [1, True], [1, 0], [2, 4], [1, -2], [1, 2, 3]):
            with self.assertRaises(ValueError):
                M.oa.unpair(value)

    def test_24_fixed_arc_guard(self):
        with M.ha.precision(512):
            for index in (True, -1, 64, Q(1)):
                with self.assertRaises(ValueError):
                    M.arc_angle(index)
        with M.ha.precision(256), self.assertRaises(ValueError):
            M.arc_angle(0)

    def test_25_tail_domain_guard(self):
        with M.ha.precision(512):
            for h in (Q(-1), Q(7, 8), Q(1)):
                with self.assertRaises(ValueError):
                    M.joint_tail(Q(1), h, M.arb(1))
            with self.assertRaises(ValueError):
                M.joint_tail(True, Q(1, 8), M.arb(1))
            with self.assertRaises(ValueError):
                M.joint_tail(Q(1), Q(1, 8), M.arb(-1))

    def test_26_zero_tail_at_h_zero(self):
        with M.ha.precision(512):
            self.assertEqual(M.joint_tail(Q(1), Q(0), M.arb(1)), 0)

    def test_27_signed_coefficient_guards(self):
        with M.ha.precision(512):
            for values in ([M.acb(0)] * 39, [M.acb(0, 1)] * 40):
                with self.assertRaises(ValueError):
                    M.joint_coefficients(values, M.arb(1))

    def test_28_manifest_tampering_blocks_before_native(self):
        original = M.BINDINGS
        with (
            mock.patch.object(M, "BINDINGS", original[:-1]),
            self.assertRaisesRegex(ValueError, "manifest mismatch"),
        ):
            M.authenticate()

    def test_29_payload_seal_guard(self):
        attack = copy.deepcopy(self.report)
        attack["summary"]["passing_arcs"] = 63
        with self.assertRaisesRegex(ValueError, "payload seal"):
            M.check_report(attack)

    def test_30_boolean_integer_not_equal_in_canonical(self):
        self.assertNotEqual(M.canonical({"node": True}), M.canonical({"node": 1}))
        self.assertNotEqual(M.canonical({"node": False}), M.canonical({"node": 0}))

    def test_31_no_assert_acceptance(self):
        tree = ast.parse((HERE / "xi_joint_polynomial_point_transport.py").read_text())
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))

    def test_32_scope_and_single_fixed_panel(self):
        self.assertEqual(self.report["summary"]["passing_arcs"], 64)
        self.assertEqual(self.report["summary"]["failed_arcs"], [])
        self.assertIs(M.CONTRACT["no_innerness_premise"], True)
        self.assertEqual(
            M.CONTRACT["panel"],
            {"node_index": 19, "bits": 512, "ratio": [1, 2], "terms": 32, "arcs": 64},
        )


if __name__ == "__main__":
    unittest.main()
