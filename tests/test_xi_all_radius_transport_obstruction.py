"""Finite source/all-radius-obstruction controls; analytic quantifier is separate."""

import copy
import importlib.util
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/exploratory/xi_all_radius_transport_obstruction.py"
)
sys.path.insert(0, str(PATH.parent))
SPEC = importlib.util.spec_from_file_location("qr", PATH)
qr = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(qr)


class AllRadius(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = qr.build_report()
        cls.fixture = qr.decode(qr.FIXTURE.read_bytes())

    def attack(self, change):
        value = copy.deepcopy(self.report)
        change(value)
        value.pop("payload_sha256")
        value["payload_sha256"] = qr.sha(qr.canonical(value))
        with self.assertRaises(ValueError):
            qr.check_report(value)

    def test_01_fresh_complete_fixture(self):
        self.assertEqual(qr.canonical(self.report), qr.canonical(self.fixture))

    def test_02_fixed_full_panel(self):
        rows = self.report["records"]
        self.assertEqual(len(rows), 26)
        self.assertEqual([r["index"] for r in rows], list(range(26)))
        self.assertEqual(
            [r["box_center"] for r in rows], [256] * 8 + [512] * 9 + [1024] * 9
        )
        self.assertTrue(all(qr.oa.unpair(r["radius"]) == Q(1, 2**120) for r in rows))
        self.assertEqual(self.report["coverage"]["work_units"], 234)

    def test_03_lambda_and_precision(self):
        lo, hi = qr.bounds(self.report["lambda_(64)"])
        self.assertTrue(0 < lo < hi < 1)
        self.assertEqual(qr.CAPS["precision_bits"], 1024)
        self.assertEqual(qr.CAPS["series_coefficients"], 9)

    def test_04_full_comparison_accounting(self):
        rows = self.report["records"]
        count = sum(r["status"] == "ALL_RADII_CRITERION_IMPOSSIBLE" for r in rows)
        self.assertEqual(count, self.report["summary"]["all_radii_impossible"])
        self.assertEqual(26 - count, self.report["summary"]["unresolved"])
        for r in rows:
            if "jets" not in r:
                self.assertEqual(r["status"], "UNRESOLVED")
                self.assertIn("reason", r)
                continue
            m = qr.bounds(r["normalized_third_derivative"])[0]
            B = qr.bounds(r["sharp_threshold"])[1]
            self.assertEqual(r["sharp_obstruction"], m >= B)
            self.assertEqual(r["status"] == "ALL_RADII_CRITERION_IMPOSSIBLE", m >= B)
            if r["sharp_obstruction"]:
                self.assertTrue(
                    qr.exact_comparison(r["jets"], self.report["lambda_(64)"])["sharp"]
                )

    def test_05_strict_threshold_improvement(self):
        for r in self.report["records"]:
            if "jets" in r:
                self.assertLess(
                    qr.bounds(r["sharp_threshold"])[1],
                    qr.bounds(r["coarse_threshold"])[0],
                )

    def test_06_exact_algebra_controls(self):
        x = qr.algebra_controls()
        self.assertEqual(x["rational_geometries"], 144)
        self.assertEqual(x["exact_radius_controls"], 2160)
        self.assertEqual(x["polynomial_threshold"], "2/7")

    def test_07_integer_sqrt_bounds(self):
        for i in range(65):
            a = Q(i, 17)
            lo, hi = qr.sqrt_interval((a, a), 32)
            self.assertTrue(lo * lo <= a <= hi * hi)
            self.assertLessEqual(hi - lo, Q(1, 2**32))
        for a, bits in (
            ((Q(-1), Q(1)), 32),
            ((Q(2), Q(1)), 32),
            ((Q(1), Q(2)), True),
            ((Q(1), Q(2)), 15),
        ):
            with self.assertRaises(ValueError):
                qr.sqrt_interval(a, bits)

    def test_08_interval_arithmetic(self):
        self.assertEqual(qr.mul((Q(-2), Q(3)), (Q(-4), Q(5))), (Q(-12), Q(15)))
        self.assertEqual(qr.div((Q(2), Q(4)), (Q(-2), Q(-1))), (Q(-4), Q(-1)))
        self.assertEqual(qr.abs_interval((Q(-2), Q(1))), (Q(0), Q(2)))
        with self.assertRaises(ValueError):
            qr.div((Q(1), Q(2)), (Q(-1), Q(1)))

    def test_09_scope(self):
        c = self.report["contract"]
        for key in (
            "threshold_is_exact_supremum",
            "proof_of_no_companion_root",
            "innerness_or_RH_assumed",
            "RH_proved",
            "cofinal_transport",
        ):
            self.assertIs(c[key], False)
        self.assertIs(c["post_QT_result_design"], True)
        self.assertEqual(c["arithmetic_class"], "MIXED")
        self.assertEqual(len(self.report["frozen_sources"]), 38)

    def test_10_json_types(self):
        for raw in (b"NaN", b"1.5", b"Infinity", b'{"x":1,"x":2}'):
            with self.assertRaises(ValueError):
                qr.decode(raw)
        for value in (1.1, 1j, 2**4096, "x" * 4097):
            with self.assertRaises(ValueError):
                qr.typed(value)

    def test_11_rational_shape(self):
        for value in (
            [[1, 0], [1, 1]],
            [[True, 1], [2, 1]],
            [[2, 2], [2, 1]],
            [[2, 1], [1, 1]],
            "x",
        ):
            with self.assertRaises(ValueError):
                qr.bounds(value)

    def test_12_precision_and_domain(self):
        with qr.ha.precision(256), self.assertRaises(ValueError):
            qr.sharp_threshold(qr.arb(1), qr.arb(1), qr.arb(1))
        with qr.ha.precision(1024):
            for values in (
                (qr.arb(1), qr.arb(0), qr.arb(1)),
                (True, qr.arb(1), qr.arb(1)),
            ):
                with self.assertRaises(ValueError):
                    qr.sharp_threshold(*values)

    def test_13_text_and_caps(self):
        self.assertEqual(qr.lf(b"a\r\nb\n"), b"a\nb\n")
        for raw in (b"\0", b"\x7f", b"a\rb", b"\xff", "text"):
            with self.assertRaises((ValueError, UnicodeError)):
                qr.lf(raw)
        with patch.dict(qr.CAPS, source_bytes=3), self.assertRaises(ValueError):
            qr.decode(b'{"x":1}')
        deep = 0
        for _ in range(26):
            deep = [deep]
        with self.assertRaises(ValueError):
            qr.typed(deep)

    def test_14_unsealed_forgery(self):
        bad = copy.deepcopy(self.report)
        bad["summary"]["all_radii_impossible"] = -1
        with self.assertRaisesRegex(ValueError, "payload seal"):
            qr.check_report(bad)

    def test_15_resealed_omitted_node(self):
        self.attack(lambda r: r["records"].pop())

    def test_16_resealed_summary(self):
        self.attack(lambda r: r["summary"].__setitem__("all_radii_impossible", 27))

    def test_17_resealed_rh_claim(self):
        self.attack(lambda r: r["contract"].__setitem__("RH_proved", True))

    def test_18_resealed_calibration(self):
        self.attack(lambda r: r.__setitem__("lambda_(64)", [[64, 1], [64, 1]]))

    def test_19_resealed_source_identity(self):
        self.attack(lambda r: r["frozen_sources"][0].__setitem__("sha256_lf", "0" * 64))

    def test_20_resealed_artifact(self):
        self.attack(
            lambda r: r["artifacts"].__setitem__(next(iter(r["artifacts"])), "0" * 64)
        )

    def test_21_resealed_false_root_claim(self):
        self.attack(
            lambda r: r["contract"].__setitem__("proof_of_no_companion_root", True)
        )

    def test_22_resealed_bool_integer(self):
        self.attack(lambda r: r["contract"].__setitem__("post_QT_result_design", 1))

    def test_23_source_corruption(self):
        original = qr.source
        with (
            patch.object(
                qr,
                "source",
                side_effect=lambda row: (
                    original(row) + b"\n" if row == qr.BINDINGS[0] else original(row)
                ),
            ),
            self.assertRaisesRegex(ValueError, "frozen source identity"),
        ):
            qr.authenticate()

    def test_24_declared_design_and_artifacts(self):
        self.assertEqual(
            self.report["design"], "800b5e212f61a4df9a640788d294b0bbbf37862b"
        )
        self.assertEqual(len(self.report["artifacts"]), 4)
        for path, digest in self.report["artifacts"].items():
            self.assertEqual(qr.sha(qr.lf((qr.ROOT / path).read_bytes())), digest)

    def test_25_complete_observed_outcomes_not_preregistered_predictions(self):
        self.assertEqual(
            self.report["summary"],
            {"all_radii_impossible": 18, "coarse_obstructions": 15, "unresolved": 8},
        )
        rows = self.report["records"]
        self.assertTrue(all("jets" in row and "reason" not in row for row in rows))
        self.assertEqual(
            [
                row["index"]
                for row in rows
                if row["sharp_obstruction"] and not row["coarse_obstruction"]
            ],
            [13, 14, 22],
        )
        self.assertIs(
            self.report["contract"]["target_is_QT_separate_triangle_criterion_only"],
            True,
        )
        self.assertIs(
            self.report["contract"]["joint_remainder_criterion_ruled_out"], False
        )


if __name__ == "__main__":
    unittest.main()
