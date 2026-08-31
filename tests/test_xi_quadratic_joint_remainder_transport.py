"""Independent exact controls and hostile replay checks for joint remainder."""

from __future__ import annotations

import copy
import importlib.util
import math
import subprocess
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/exploratory/xi_quadratic_joint_remainder_transport.py"
SPEC = importlib.util.spec_from_file_location("joint_remainder", PATH)
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


def cmul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def cpow(a, n):
    out = Q(1), Q(0)
    for _ in range(n):
        out = cmul(out, a)
    return out


def cscale(a, r):
    return a[0] * r, a[1] * r


def cadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def integral_tau_power(power, other):
    # Integrate tau^power*(1-tau)^other by its finite binomial expansion.
    return sum(
        (Q((-1) ** h * math.comb(other, h), power + h + 1) for h in range(other + 1)),
        Q(0),
    )


class JointRemainderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fresh = m.build_report()
        cls.parent, cls.closure = m.authenticate()

    def test_01_fresh_fixture_identity(self):
        self.assertEqual(
            m.canonical(m.decode(m.FIXTURE.read_bytes())), m.canonical(self.fresh)
        )
        self.assertTrue(m.check_report(m.decode(m.FIXTURE.read_bytes())))

    def test_02_analytic_integral_identity_on_monomials(self):
        for n in range(3, 13):
            derivative = n * (n - 1) * (n - 2)
            for x, y in ((Q(1, 3), Q(1, 2)), (Q(-2), Q(3, 4)), (Q(0), Q(1))):
                for lam in (Q(1, 2), Q(1), Q(7, 3)):
                    w = x, y
                    direct = cadd(cpow(w, n), cmul((Q(0), -lam * n), cpow(w, n - 1)))
                    joint = cadd(
                        cscale(
                            cpow(w, n), derivative * integral_tau_power(2, n - 3) / 2
                        ),
                        cmul(
                            (Q(0), -lam * derivative * integral_tau_power(1, n - 3)),
                            cpow(w, n - 1),
                        ),
                    )
                    self.assertEqual(joint, direct)

    def test_03_exact_disc_factor_controls(self):
        directions = (
            (Q(1), Q(0)),
            (Q(-1), Q(0)),
            (Q(0), Q(1)),
            (Q(0), Q(-1)),
            (Q(3, 5), Q(4, 5)),
            (Q(-5, 13), Q(12, 13)),
        )
        for lam, y, r in (
            (Q(1), Q(1, 2), Q(1, 4)),
            (Q(2), Q(3, 2), Q(1, 8)),
            (Q(1, 2), Q(1, 3), Q(1, 10)),
        ):
            for tau in (Q(i, 16) for i in range(17)):
                for ux, uy in directions:
                    real = tau * r * ux / 2
                    imag = tau * (y + r * uy) / 2 - lam
                    rhs = lam - tau * (y - r) / 2
                    self.assertGreater(rhs, 0)
                    self.assertLessEqual(real * real + imag * imag, rhs * rhs)

    def test_04_center_hypothesis_is_essential(self):
        # The formula is not extended to arbitrary y: its proposed RHS is negative here.
        self.assertLess(Q(1) - (Q(10) - Q(1, 4)) / 2, 0)

    def test_05_exact_strict_improvement_control(self):
        control = m.exact_control()
        self.assertEqual(m.interval(control["joint_error"]), (Q(11, 128),) * 2)
        self.assertEqual(m.interval(control["old_error"]), (Q(15, 128),) * 2)
        self.assertEqual(m.interval(control["margin"]), (Q(12, 128),) * 2)
        self.assertLess(Q(4, 15), Q(1, 3))
        self.assertLess(Q(1, 3), Q(4, 11))

    def test_06_general_improvement_is_y_over_three(self):
        for lam in (Q(1), Q(2), Q(7, 3)):
            for y in (lam / 5, lam / 3, lam * Q(3, 4)):
                for ratio in m.RATIOS:
                    r = ratio * y
                    old = lam / 2 + (y + r) / 6
                    joint = lam / 2 - (y - r) / 6
                    self.assertEqual(old - joint, y / 3)
                    self.assertGreater(joint, 0)

    def test_07_outward_square_root(self):
        for q in (Q(0), Q(1), Q(2), Q(3, 7), Q(1, 2**1100), Q(2**120 + 1, 7)):
            lo, hi = m.square_root((q, q))
            self.assertLessEqual(lo * lo, q)
            self.assertGreaterEqual(hi * hi, q)
            self.assertLessEqual(hi - lo, Q(1, 2**m.SQRT_BITS))
        self.assertEqual(m.square_root((Q(9, 16), Q(9, 16))), (Q(3, 4), Q(3, 4)))
        with self.assertRaises(ValueError):
            m.square_root((Q(-1), Q(1)))

    def test_08_interval_corners(self):
        for a in ((Q(-2), Q(3)), (Q(1, 4), Q(5, 3))):
            for b in ((Q(-7), Q(-2)), (Q(1), Q(4, 3))):
                expected = sorted(x * y for x in a for y in b)
                self.assertEqual(m.mul(a, b), (expected[0], expected[-1]))
                expected_div = sorted(x / y for x in a for y in b)
                self.assertEqual(m.div(a, b), (expected_div[0], expected_div[-1]))
        with self.assertRaises(ValueError):
            m.div(m.point(1), (Q(-1), Q(1)))
        with self.assertRaises(ValueError):
            m.meet((Q(0), Q(1)), (Q(2), Q(3)))

    def test_09_full_parent_rectangle_not_midpoint(self):
        center = [[0, 1], [1, 2]]
        t, y = m.point(0), m.point(Q(1, 2))
        self.assertTrue(m.containment(t, y, m.point(Q(1, 4)), center, [1, 10])[2])
        self.assertFalse(m.containment(t, y, m.point(Q(1, 10)), center, [1, 10])[2])
        self.assertFalse(
            m.containment((Q(-1), Q(1)), y, m.point(Q(1, 4)), center, [1, 100])[2]
        )

    def test_10_complete_390_coverage(self):
        keys = [
            (r["node"], m.unpair(r["ratio"]), r["bits"]) for r in self.fresh["records"]
        ]
        self.assertEqual(
            keys, [(n, r, b) for n in range(26) for r in m.RATIOS for b in m.TIERS]
        )
        self.assertEqual(len(set(keys)), 390)

    def test_11_all_inherited_bounds_noncertifying(self):
        summary = self.fresh["summary"]
        self.assertEqual(summary["joint_certified_cells"], 0)
        self.assertEqual(summary["joint_noncertified_cells"], 390)
        self.assertEqual(summary["joint_matched_cells"], 0)
        for record in self.fresh["records"]:
            self.assertEqual(record["status"], "NOT_CERTIFIED_INHERITED_BOUND")
            self.assertIs(record["transport_certified"], False)
            self.assertEqual(record["old_outcome"]["status"], "FAILED")
            self.assertIs(record["old_outcome"]["transport_certified"], False)

    def test_12_m3_region_never_enlarged(self):
        for record in self.fresh["records"]:
            h = m.interval(record["y"])[1] + m.interval(record["r"])[1]
            self.assertLessEqual(h, m.unpair(record["source_region_radius"]))
            self.assertGreaterEqual(m.unpair(record["source_M3_upper"]), 0)

    def test_13_inherited_critical_arithmetic(self):
        for node in self.parent["records"]:
            t = m.source_record(node)
            self.assertEqual(t[1] - t[0], 2 * m.EPS)
        bad = copy.deepcopy(self.parent["records"][0])
        bad["critical"]["attempts"][0]["left"] = [1, 1]
        with self.assertRaises(ValueError):
            m.source_record(bad)

    def test_14_exact_comparison_independently(self):
        for record in self.fresh["records"]:
            lam = m.interval(record["lambda"])
            y, r = m.interval(record["y"]), m.interval(record["r"])
            factor = lam[1] / 2 - (y[0] - r[1]) / 6
            h = y[1] + r[1]
            error = m.unpair(record["source_M3_upper"]) * h * h * factor
            self.assertEqual(error, m.interval(record["joint_error"])[1])
            self.assertGreaterEqual(error, m.interval(record["model_margin"])[0])

    def test_15_source_closure_and_design(self):
        self.assertEqual(self.fresh["frozen_sources"], m.BINDINGS)
        self.assertEqual(
            self.fresh["inherited_QT_payload_sha256"], self.parent["payload_sha256"]
        )
        self.assertIn(m.DESIGN, {p["commit"] for p in self.closure})
        self.assertGreater(len(self.closure), len(m.BINDINGS))
        for pin in m.BINDINGS:
            self.assertEqual(m.digest(m.lf(m.read_source(pin))), pin["sha256_lf"])

    def test_16_four_artifact_seals(self):
        self.assertEqual(len(self.fresh["artifacts"]), 4)
        for path, expected in self.fresh["artifacts"].items():
            self.assertEqual(m.digest(m.lf((ROOT / path).read_bytes())), expected)

    def test_17_strict_rational_types_and_canonical_pairs(self):
        for value in (True, 1.0, "1", None):
            with self.assertRaises(ValueError):
                m.rational(value)
        for value in ([True, 1], [1, True], [1, 0], [2, 4], [-1, -2], [1], (1, 2)):
            with self.assertRaises(ValueError):
                m.unpair(value)
        with self.assertRaises(ValueError):
            m.interval([[2, 1], [1, 1]])

    def test_18_json_duplicate_float_nonfinite(self):
        for raw in (b'{"a":1,"a":2}', b'{"a":1.0}', b'{"a":NaN}', b'{"a":Infinity}'):
            with self.assertRaises(ValueError):
                m.decode(raw)
        with self.assertRaises(ValueError):
            m.decode("{}")

    def test_19_caps(self):
        with patch.object(m, "MAX_BYTES", 2), self.assertRaises(ValueError):
            m.decode(b'{"a":1}')
        with patch.object(m, "MAX_BITS", 3), self.assertRaises(ValueError):
            m.rational(8)
        with patch.object(m, "MAX_NODES", 2), self.assertRaises(ValueError):
            m.canonical([1, 2])
        nested = 0
        for _ in range(30):
            nested = [nested]
        with self.assertRaises(ValueError):
            m.canonical(nested)
        with self.assertRaises(ValueError):
            m.canonical("a" * 4097)

    def test_20_source_hash_tampering(self):
        for field, bad in (("git_blob", "0" * 40), ("sha256_lf", "0" * 64)):
            pin = dict(m.BINDINGS[0])
            pin[field] = bad
            with self.assertRaises(ValueError):
                m.read_source(pin)

    def test_21_source_path_guards(self):
        for bad in (
            "../README.md",
            "./README.md",
            "/README.md",
            "x//y",
            "x\\y",
            "x:y",
            "x\x7fy",
        ):
            pin = dict(m.BINDINGS[0], path=bad)
            with self.assertRaises(ValueError):
                m.read_source(pin)

    def test_22_tree_object_is_not_commit(self):
        tree = subprocess.check_output(
            ["git", "rev-parse", m.BASE + "^{tree}"], cwd=ROOT, text=True
        ).strip()
        with self.assertRaises(ValueError):
            m.read_source(dict(m.BINDINGS[0], commit=tree))

    def test_23_manifest_mutation(self):
        bad = copy.deepcopy(m.manifest())
        bad["contract"]["rounding"] = "ordinary floats"
        with (
            patch.object(Path, "read_bytes", return_value=m.canonical(bad)),
            self.assertRaises(ValueError),
        ):
            m.authenticate()

    def test_24_resealed_hostiles(self):
        # A fresh independent reconstruction is built once in setUpClass; each forged
        # candidate is fully resealed, then compared through the real checker.
        def mutate(report, which):
            record = report["records"][0]
            if which == 0:
                report["contract"]["rounding"] = "none"
            elif which == 1:
                record["transport_certified"] = True
            elif which == 2:
                record["source_M3_upper"] = [0, 1]
            elif which == 3:
                record["ratio"] = [1, 17]
            elif which == 4:
                record["joint_error"] = [[0, 1], [0, 1]]
            elif which == 5:
                record["old_outcome"]["status"] = "PASS"
            elif which == 6:
                report["records"].pop()
            elif which == 7:
                report["records"].reverse()
            elif which == 8:
                report["summary"]["joint_certified_cells"] = 1
            elif which == 9:
                record["matched_parent_root"] = True
            elif which == 10:
                report["artifacts"][next(iter(report["artifacts"]))] = "0" * 64
            else:
                report["inherited_QT_payload_sha256"] = "0" * 64

        for which in range(12):
            bad = copy.deepcopy(self.fresh)
            mutate(bad, which)
            unsigned = {k: v for k, v in bad.items() if k != "payload_sha256"}
            bad["payload_sha256"] = m.digest(m.canonical(unsigned))
            with (
                patch.object(m, "build_report", return_value=self.fresh),
                self.assertRaises(ValueError),
            ):
                m.check_report(bad)

    def test_25_bad_unsealed_payload(self):
        bad = copy.deepcopy(self.fresh)
        bad["payload_sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            m.check_report(bad)

    def test_26_inherited_domain_failure_is_closed(self):
        node = self.parent["records"][0]
        group = node["quadratic"][0]
        attempt = copy.deepcopy(group["attempts"][0])
        attempt["third_derivative"]["radius_upper"] = [0, 1]
        with self.assertRaises(ValueError):
            m.cell(node, group, attempt, node["jet_tiers"][0], m.source_record(node))

    def test_27_boolean_tier_rejected(self):
        node = self.parent["records"][0]
        group = node["quadratic"][0]
        attempt = copy.deepcopy(group["attempts"][0])
        attempt["bits"] = True
        with self.assertRaises(ValueError):
            m.cell(node, group, attempt, node["jet_tiers"][0], m.source_record(node))

    def test_28_text_controls_and_scope(self):
        for path in (m.NOTE, PATH, m.MANIFEST, m.FIXTURE, Path(__file__)):
            m.lf(path.read_bytes())
        self.assertIn("NOT impossibility", m.CONTRACT["nonpass"])
        self.assertIn("no parent special-function", m.CONTRACT["inheritance"])
        self.assertEqual(m.CONTRACT["arithmetic_class"], "MIXED")


if __name__ == "__main__":
    unittest.main()
