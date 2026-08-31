"""Exact independent Taylor routes and hostile source/scope acceptance."""

from __future__ import annotations

import copy
import importlib.util
import math
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/theta_positive_source_real_zero_firewall.py"
)
SPEC = importlib.util.spec_from_file_location("zf", PATH)
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


def bounds(row):
    return tuple(Q(v) for v in row)


def independent_exp(x, n=16):
    lo = sum((x**j / Q(math.factorial(j)) for j in range(n + 1)), Q(0))
    hi = lo + x ** (n + 1) / Q(math.factorial(n + 1)) / (1 - x / Q(n + 2))
    return lo, hi


def independent_z(a, s):
    if s in (0, 1):
        return Q(1, 2), Q(1, 2)
    e, f = independent_exp(s), independent_exp(1 - s)
    return (
        Q(1, 2) + a * (1 - (1 - s) * e[1] - s * f[1]),
        Q(1, 2) + a * (1 - (1 - s) * e[0] - s * f[0]),
    )


def reseal(v):
    v.pop("payload_sha256", None)
    v["payload_sha256"] = m.digest(m.canonical(v))
    return v


class Firewall(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = m.decode(m.file_bytes(ROOT / (m.DIR + m.STEM + ".json")))
        cls.fresh = m.fixture()

    def setUp(self):
        m.WORK = 0

    def test_01_fresh_replay(self):
        self.assertEqual(self.report, self.fresh)
        self.assertTrue(m.check(self.report))

    def test_02_fixed_complete_panel(self):
        self.assertEqual(
            [r["x"] for r in self.report["exponential_enclosures"]],
            ["1/8", "3/8", "1/2", "5/8", "7/8", "1"],
        )
        self.assertEqual(len(self.report["Z_sign_panel"]), 9)
        self.assertEqual(len(self.report["monotonicity_margins"]), 9)
        self.assertEqual(len(self.report["candidate_brackets"]), 2)

    def test_03_independent_taylor_factorials(self):
        for row in self.report["exponential_enclosures"]:
            x = Q(row["x"])
            self.assertEqual(row["N"], 16)
            self.assertEqual(bounds(row["enclosure"]), independent_exp(x))
            lo, hi = bounds(row["enclosure"])
            self.assertLess(lo, hi)
            s18 = sum(x**j / Q(math.factorial(j)) for j in range(19))
            self.assertLess(lo, s18)
            self.assertLess(s18, hi)

    def test_04_threshold_exact_bound(self):
        lo, hi = independent_exp(Q(1, 2))
        ac = (1 / (2 * (hi - 1)), 1 / (2 * (lo - 1)))
        self.assertEqual(ac, bounds(self.report["A_c_enclosure"]))
        self.assertGreater(ac[0], Q(3, 4))
        self.assertLess(ac[1], Q(4, 5))

    def test_05_independent_nine_signs(self):
        expected = [1, 1, 1, 1, -1, -1, -1, -1, -1]
        self.assertEqual([r["sign"] for r in self.report["Z_sign_panel"]], expected)
        for row in self.report["Z_sign_panel"]:
            v = independent_z(Q(row["A"]), Q(row["s"]))
            self.assertEqual(v, bounds(row["enclosure"]))
            self.assertTrue(v[0] > 0 if row["sign"] == 1 else v[1] < 0)

    def test_06_failed_bracket_preserved(self):
        a, b = self.report["candidate_brackets"]
        self.assertTrue(a["opposite_signs"])
        self.assertFalse(b["opposite_signs"])
        self.assertEqual(a["candidate"], b["candidate"])
        self.assertEqual(b["endpoint_signs"], [-1, -1])
        self.assertFalse(b["preregistered_expected_success"])
        self.assertEqual(self.report["coverage"]["candidate_failures"], 1)

    def test_07_all_endpoints_exact(self):
        for a in (Q(1, 2), Q(1), Q(2)):
            self.assertEqual(m.z_bounds(a, 0), (Q(1, 2), Q(1, 2)))
            self.assertEqual(m.z_bounds(a, 1), (Q(1, 2), Q(1, 2)))

    def test_08_reflected_enclosures(self):
        for a in (Q(1, 2), Q(1), Q(2)):
            for s in (Q(1, 8), Q(3, 8), Q(1, 2)):
                self.assertEqual(m.z_bounds(a, s), m.z_bounds(a, 1 - s))

    def test_09_monotonicity_margins(self):
        for row in self.report["monotonicity_margins"]:
            b, z = Q(row["b_squared"]), Q(row["z"])
            self.assertEqual(Q(row["margin"]), 2 - b / 4 + b * z * z)
            self.assertGreaterEqual(Q(row["margin"]), Q(row["lower_bound"]))
            self.assertGreater(Q(row["lower_bound"]), 0)
        self.assertEqual(
            sum(r["b_squared"] == "8" for r in self.report["monotonicity_margins"]), 3
        )

    def test_10_formal_antiderivative(self):
        f = self.report["formal"]
        p = [Q(x) for x in f["J2_antiderivative_x"]]
        self.assertEqual([p[1] + p[0] / 2, 2 * p[2] + p[1] / 2, p[2] / 2], [0, 0, 1])
        self.assertEqual(f["J2_E"], ["-16", "10"])
        self.assertEqual(f["curvature_E"], ["0", "3/2"])

    def test_11_formal_pitchfork(self):
        f = self.report["formal"]
        self.assertEqual(f["pitchfork_numerator_E"], ["4", "-8", "4"])
        self.assertEqual(f["pitchfork_denominator_E"], ["0", "3"])
        for e in (Q(3, 2), Q(2), Q(5, 2)):
            j0, j2 = 2 * e - 2, 10 * e - 16
            c = 2 * j0 - j2 / 4
            self.assertEqual(c, 3 * e / 2)
            self.assertEqual(j0 * j0 / (2 * c), 4 * (e - 1) ** 2 / (3 * e))

    def test_12_reflection_formal(self):
        f = self.report["formal"]
        self.assertEqual(f["reflection_original"], f["reflection_transformed"])
        self.assertEqual(m.reflect([1, 2, 3]), [6, -8, 3])
        self.assertEqual(
            m.reflect(m.reflect([1, 2, 3, 4, 5, 6, 7, 8])), [1, 2, 3, 4, 5, 6, 7, 8]
        )

    def test_13_scope_contract(self):
        c = self.report["contract"]
        self.assertEqual(c["arithmetic_class"], "MIXED")
        self.assertEqual(
            c["components"], ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"]
        )
        self.assertEqual(c["rounding"], "none")
        for key in (
            "analytic_proof_machine_certified",
            "actual_modular_source",
            "RH_counterexample",
            "all_complex_zero_count",
        ):
            self.assertFalse(c[key])
        self.assertTrue(c["smooth_persistence_is_written_existence_proof"])

    def test_14_seals(self):
        m.authenticate()
        self.assertEqual(len(m.BINDINGS), 6)
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for path, d in self.report["artifact_sha256_lf"].items():
            self.assertEqual(d, m.digest(m.lf(m.file_bytes(ROOT / path))))
        v = copy.deepcopy(self.report)
        d = v.pop("payload_sha256")
        self.assertEqual(d, m.digest(m.canonical(v)))

    def test_15_each_frozen_source_tamper(self):
        original = m.subprocess.check_output
        for row in m.BINDINGS:

            def bad(args, selected=row, **kw):
                raw = original(args, **kw)
                return (
                    raw + b" "
                    if args[-1] == selected["commit"] + ":" + selected["path"]
                    else raw
                )

            with (
                self.subTest(path=row["path"]),
                mock.patch.object(m.subprocess, "check_output", side_effect=bad),
                self.assertRaises(ValueError),
            ):
                m.authenticate()

    def test_16_manifest_tamper(self):
        original = m.file_bytes
        bad = m.manifest()
        bad["contract"]["actual_modular_source"] = True
        path = ROOT / (m.DIR + m.STEM + ".sources.json")
        with (
            mock.patch.object(
                m,
                "file_bytes",
                side_effect=lambda p: m.canonical(bad) if p == path else original(p),
            ),
            self.assertRaises(ValueError),
        ):
            m.authenticate()

    def test_17_each_artifact_tamper(self):
        original = m.file_bytes
        for target in m.ARTIFACTS:

            def bad(path, selected=target):
                raw = original(path)
                return raw + b" " if path == ROOT / selected else raw

            with (
                mock.patch.object(m, "file_bytes", side_effect=bad),
                self.assertRaises(ValueError),
            ):
                m.check(self.report)

    def test_18_resealed_coverage_attacks(self):
        for key in (
            "exponential_enclosures",
            "Z_sign_panel",
            "candidate_brackets",
            "monotonicity_margins",
        ):
            bad = copy.deepcopy(self.report)
            bad[key] = bad[key][:-1]
            with self.subTest(key=key), self.assertRaises(ValueError):
                m.check(reseal(bad))

    def test_19_resealed_science_attacks(self):
        for key in (
            "actual_modular_source",
            "RH_counterexample",
            "all_complex_zero_count",
            "analytic_proof_machine_certified",
        ):
            bad = copy.deepcopy(self.report)
            bad["contract"][key] = True
            with self.subTest(key=key), self.assertRaises(ValueError):
                m.check(reseal(bad))

    def test_20_resealed_value_and_failure_attacks(self):
        bad = copy.deepcopy(self.report)
        bad["candidate_brackets"][1]["opposite_signs"] = True
        with self.assertRaises(ValueError):
            m.check(reseal(bad))
        bad = copy.deepcopy(self.report)
        bad["Z_sign_panel"][0]["enclosure"][0] = "0"
        with self.assertRaises(ValueError):
            m.check(reseal(bad))
        bad = copy.deepcopy(self.report)
        bad["work_units"] = True
        with self.assertRaises(ValueError):
            m.check(reseal(bad))

    def test_21_rational_and_integer_types(self):
        for value in (True, False, 1.0, "1", None, complex(1)):
            with self.assertRaises(ValueError):
                m.rational(value)
        for value in (True, 1.0, "2"):
            with self.assertRaises(ValueError):
                m.integer(value, 1, 32)

    def test_22_taylor_order_and_point_guards(self):
        for x in (-1, Q(9, 8), True, 0.5):
            with self.assertRaises(ValueError):
                m.exp_bounds(x)
        for n in (0, 33, True, 16.0):
            with self.assertRaises(ValueError):
                m.exp_bounds(Q(1, 2), n)
        self.assertEqual(m.exp_bounds(0), (1, 1))

    def test_23_interval_and_sign_guards(self):
        for value in ([], [1], [2, 1], [True, 2], "12"):
            with self.assertRaises(ValueError):
                m.interval(value)
        for value in ((-1, 1), (0, 0)):
            with self.assertRaises(ValueError):
                m.sign(value)
        self.assertEqual(m.scale((1, 2), -3), (-6, -3))

    def test_24_amplitude_and_position_caps(self):
        for a, s in (
            (0, Q(1, 2)),
            (-1, Q(1, 2)),
            (5, Q(1, 2)),
            (True, Q(1, 2)),
            (1, -1),
            (1, 2),
        ):
            with self.assertRaises(ValueError):
                m.z_bounds(a, s)

    def test_25_polynomial_and_bit_caps(self):
        for p in ([], [1] * 9, [True], [1.0]):
            with self.assertRaises(ValueError):
                m.polynomial(p)
        with self.assertRaises(ValueError):
            m.polymul([1] * 8, [1, 1])
        with self.assertRaises(ValueError):
            m.polymul([1 << 3000], [1 << 3000])
        with self.assertRaises(ValueError):
            m.rational(1 << 4096)
        with self.assertRaises(ValueError):
            m.rational(Q(1, 1 << 4096))

    def test_26_work_and_json_caps(self):
        m.WORK = m.CAPS["work_units"]
        with self.assertRaises(ValueError):
            m.exp_bounds(Q(1, 2))
        m.WORK = 0
        for v in ("x" * 4097, [0] * 2001, 1 << 4096):
            with self.assertRaises(ValueError):
                m.typed(v)
        nested = 0
        for _ in range(26):
            nested = [nested]
        with self.assertRaises(ValueError):
            m.typed(nested)
        with mock.patch.dict(m.CAPS, json_nodes=2), self.assertRaises(ValueError):
            m.typed([1, 2])
        with self.assertRaises(ValueError):
            m.decode(b" " * 1000001)

    def test_27_json_strictness(self):
        for raw in (b'{"a":1,"a":2}', b"NaN", b"1.0", b"null", b"Infinity"):
            with self.assertRaises(ValueError):
                m.decode(raw)
        with self.assertRaises(ValueError):
            m.decode("not bytes")
        with self.assertRaises(ValueError):
            m.typed({"v": None})

    def test_28_LF_and_canonical(self):
        self.assertEqual(m.lf(b"a\r\nb\n"), b"a\nb\n")
        self.assertEqual(m.canonical({"b": 1, "a": 2}), b'{"a":2,"b":1}')
        self.assertEqual(m.decode(m.canonical(self.report)), self.report)


if __name__ == "__main__":
    unittest.main()
