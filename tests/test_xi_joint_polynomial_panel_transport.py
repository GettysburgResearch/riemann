"""Fixed26 panel completeness, known-control and fresh-replay controls."""

import ast
import copy
import importlib.util
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "research/exploratory"
sys.path.insert(0, str(HERE))
SPEC = importlib.util.spec_from_file_location(
    "panel", HERE / "xi_joint_polynomial_panel_transport.py"
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def reseal(v):
    v = copy.deepcopy(v)
    v.pop("payload_sha256", None)
    v["payload_sha256"] = M.oa.digest(M.canonical(v))
    return v


class PanelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.decode(M.FIXTURE.read_bytes())

    def test_01_full_fresh_reconstruction(self):
        self.assertTrue(M.check_report(self.report))

    def test_02_literal_sources(self):
        M.authenticate()
        self.assertEqual(len(M.BINDINGS), 6)

    def test_03_complete26_and25_denominator(self):
        records = self.report["records"]
        self.assertEqual([r["index"] for r in records], list(range(26)))
        self.assertEqual(M.summary(records), self.report["summary"])
        self.assertEqual(self.report["summary"]["primary_untried_points"], 25)
        self.assertEqual(self.report["summary"]["primary_matched_passes"], 7)
        self.assertEqual(self.report["summary"]["total_matched_passes"], 8)
        self.assertEqual(self.report["summary"]["evaluated_arc_count"], 1664)
        self.assertEqual(self.report["summary"]["passing_arc_count"], 650)

    def test_04_known_control_not_untried(self):
        records = self.report["records"]
        self.assertEqual(records[19]["selection"], "KNOWN_CONTROL")
        self.assertEqual(sum(r["selection"] == "PRIMARY_UNTRIED" for r in records), 25)
        self.assertTrue(records[19]["matched_transport_certified"])

    def test_05_all64slots_and_failure_retention(self):
        for r in self.report["records"]:
            self.assertEqual([v["index"] for v in r["arcs"]], list(range(64)))
            if "guard_failure" in r:
                self.assertFalse(r["matched_transport_certified"])
            for arc in r["arcs"]:
                if arc["strict_pass"]:
                    self.assertLess(Q(*arc["error_upper"]), Q(*r["margin_lower"]))
                if arc["status"] == "NOT_EVALUATED_DUE_GUARD":
                    self.assertFalse(arc["strict_pass"])

    def test_06_full_t_interval(self):
        for r in self.report["records"]:
            if "T" not in r:
                continue
            c, eps = Q(*r["critical"]["center"]), Q(*r["critical"]["radius"])
            self.assertLessEqual(Q(*r["T"][0]), c - eps)
            self.assertGreaterEqual(Q(*r["T"][1]), c + eps)
            self.assertEqual(len(r["real_coefficients_0_to39"]), 40)

    def test_07_all_inherited_covers(self):
        for r in self.report["records"]:
            self.assertEqual(r["cover"]["finite_cells"], 256)
            self.assertEqual(r["cover"]["failed_cells"], [])

    def test_08_full_rectangle_every_success(self):
        for r in self.report["records"]:
            if r["matched_transport_certified"]:
                self.assertTrue(r["transport_certified"])
                self.assertTrue(r["parent_matched"])
                self.assertLess(
                    Q(*r["parent_displacement_upper"]), Q(*r["radius_lower"])
                )

    def test_09_fresh_resealed_false_arc_rejected(self):
        attack = copy.deepcopy(self.report)
        attack["records"][19]["arcs"][0]["error_upper"] = [0, 1]
        with self.assertRaisesRegex(
            ValueError, "fresh full26 primitive reconstruction"
        ):
            M.check_report(reseal(attack))

    def test_10_fresh_resealed_false_heldout_label_rejected(self):
        attack = copy.deepcopy(self.report)
        attack["records"][19]["selection"] = "PRIMARY_UNTRIED"
        with self.assertRaisesRegex(
            ValueError, "fresh full26 primitive reconstruction"
        ):
            M.check_report(reseal(attack))

    def test_11_numeric_and_duplicate_json_guards(self):
        for raw in (b'{"x":1.0}', b'{"x":NaN}', b'{"x":1,"x":2}'):
            with self.assertRaises(ValueError):
                M.decode(raw)

    def test_12_caps_and_types(self):
        for value in ({"x": 1 << 4097}, [0] * 8001, {"x": "\u03bb"}, {1: 2}):
            with self.assertRaises(ValueError):
                M.canonical(value)
        with self.assertRaises(ValueError):
            M.decode("{}")
        deep = 0
        for _ in range(26):
            deep = [deep]
        with self.assertRaises(ValueError):
            M.canonical(deep)

    def test_13_order_and_scope_guards(self):
        with self.assertRaises(ValueError):
            M.summary(self.report["records"][:-1])
        self.assertIn("no innerness", M.CONTRACT["source_quantifiers"])
        self.assertEqual(M.CONTRACT["bits"], 512)
        self.assertEqual(M.CONTRACT["closed_arcs"], 64)

    def test_14_exact_inherited_algebra_controls(self):
        self.assertEqual(M.jp.exact_controls(), self.report["inherited_exact_controls"])

    def test_15_no_assert_acceptance(self):
        tree = ast.parse((HERE / "xi_joint_polynomial_panel_transport.py").read_text())
        self.assertFalse(any(isinstance(v, ast.Assert) for v in ast.walk(tree)))

    def test_16_primitive_hashes_and_no_boolean_integer_alias(self):
        for r in self.report["records"]:
            if "full_signed_jet_sha256" in r:
                self.assertEqual(len(r["full_signed_jet_sha256"]), 64)
            if "full_arc_stream_sha256" in r:
                self.assertEqual(len(r["full_arc_stream_sha256"]), 64)
        self.assertNotEqual(M.canonical({"i": True}), M.canonical({"i": 1}))


if __name__ == "__main__":
    unittest.main()
