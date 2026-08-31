"""Strict finite PB replay; analytic innerness and cofinal hypotheses remain unpaid."""

from __future__ import annotations

import copy
import importlib.util
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/exploratory/xi_fixed_lambda_shrinking_physical_bands.py"
)
sys.path.insert(0, str(PATH.parent))
SPEC = importlib.util.spec_from_file_location("pb", PATH)
pb = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pb)


class PhysicalBands(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = pb.build_report()
        cls.fixture = pb.decode(pb.file_bytes(pb.FIXTURE))

    def fresh_attack(self, change):
        bad = copy.deepcopy(self.report)
        change(bad)
        bad.pop("payload_sha256")
        bad["payload_sha256"] = pb.digest(pb.canonical(bad))
        with self.assertRaises(ValueError):
            pb.check_report(bad)

    def test_01_complete_fresh_fixture(self):
        self.assertEqual(pb.canonical(self.report), pb.canonical(self.fixture))

    def test_02_preregistered_panel(self):
        self.assertEqual(pb.WIDTHS, (Q(1, 256), Q(1, 1024), Q(1, 4096)))
        self.assertEqual(pb.HEIGHTS, tuple(2**j for j in range(6, 17)))
        self.assertEqual(
            self.report["coverage"],
            {
                "nodes": 40,
                "widths": 3,
                "heights": 11,
                "grid": 1320,
                "axis": 11,
                "prefixes": [14, 22, 31, 40],
                "prefix_band_cells": 12,
                "gaps": 39,
                "memberships": 40,
            },
        )
        self.assertEqual(self.report["work_units"], 1331)

    def test_03_single_literal_calibration(self):
        self.assertEqual(self.report["parameter_anchor"], 64)
        self.assertTrue(
            all(r["parameter_anchor"] == 64 for r in self.report["inherited_nodes"])
        )
        lo, hi = pb.real_bounds(self.report["lambda_(64)"])
        self.assertTrue(0 < lo < hi < 64)

    def test_04_all_grid_cells_kept(self):
        count = 0
        self.assertEqual(
            [(b["positive_cells"], b["zero_cells"]) for b in self.report["bands"]],
            [(242, 198), (160, 280), (80, 360)],
        )
        self.assertTrue(all(b["all40_nodes_positive"] for b in self.report["bands"]))
        for band, width in zip(self.report["bands"], pb.WIDTHS):
            self.assertEqual(pb.oa.unpair(band["D"]), width)
            self.assertEqual(
                [r["node_index"] for r in band["all1320_grid_part"]], list(range(40))
            )
            for row in band["all1320_grid_part"]:
                self.assertEqual([v["h"] for v in row["witnesses"]], list(pb.HEIGHTS))
                for v in row["witnesses"]:
                    self.assertEqual(pb.oa.unpair(v["D"]), width)
                    self.assertEqual(v["positive"], pb.oa.unpair(v["norm_lower"]) > 0)
                    count += 1
            self.assertEqual(band["positive_cells"] + band["zero_cells"], 440)
        self.assertEqual(count, 1320)

    def test_05_independent_exact_prefix_aggregation(self):
        for band in self.report["bands"]:
            best = [
                max(pb.oa.unpair(v["norm_lower"]) for v in r["witnesses"])
                for r in band["all1320_grid_part"]
            ]
            self.assertEqual([pb.oa.pair(x) for x in best], band["best_node_lower"])
            for row, n, c in zip(band["prefixes"], pb.PREFIXES, pb.CEILINGS):
                trace = sum(x * x for x in best[:n]) / c
                self.assertEqual(pb.oa.unpair(row["squared_HS_lower"]), trace)
                self.assertEqual(pb.oa.unpair(row["norm_lower"]), max(best[:n]))
                self.assertEqual(pb.oa.unpair(row["Gram_ceiling"]), c)

    def test_06_strict_floors(self):
        for band in self.report["bands"]:
            for r in band["prefixes"]:
                for a, b in (
                    ("strict_norm_floor", "norm_lower"),
                    ("strict_squared_HS_floor", "squared_HS_lower"),
                ):
                    lo, hi = pb.oa.unpair(r[a]), pb.oa.unpair(r[b])
                    self.assertTrue(lo == 0 or 0 < lo < hi)
        self.assertEqual(pb.strict_floor(Q(1, 2), 2), Q(49, 100))
        self.assertEqual(pb.strict_floor(Q(0), 16), 0)

    def test_07_full_interval_geography(self):
        rows = self.report["inherited_nodes"]
        geo = self.report["geometry"]
        self.assertTrue(geo["all39gaps_certified"])
        self.assertTrue(geo["all40memberships_resolved"])
        self.assertEqual(len(geo["occupied_unit_cells"]), 40)
        self.assertEqual(len(geo["adjacent_gaps"]), 39)
        for g in geo["adjacent_gaps"]:
            left, right = rows[g["left"]], rows[g["right"]]
            gap = (
                pb.real_bounds(right["x_interval"])[0]
                - pb.real_bounds(left["x_interval"])[1]
            )
            heights = (
                pb.real_bounds(left["y_interval"])[1]
                + pb.real_bounds(right["y_interval"])[1]
            )
            self.assertEqual(pb.oa.unpair(g["gap_lower"]), gap)
            self.assertEqual(pb.oa.unpair(g["height_sum_upper"]), heights)
            self.assertEqual(g["certified"], gap >= heights)
        for m in geo["memberships"]:
            lo, hi = pb.real_bounds(rows[m["index"]]["x_interval"])
            self.assertEqual(m["lower_cell"], lo.numerator // lo.denominator)
            self.assertEqual(m["resolved"], hi < m["lower_cell"] + 1)

    def test_08_carleson_not_gram(self):
        self.assertTrue(self.report["geometry"]["Carleson_upper_is_NOT_Gram_ceiling"])
        self.assertEqual(
            pb.CEILINGS, (Q(1171, 500), Q(599, 250), Q(1207, 500), Q(121, 50))
        )
        self.assertTrue(all(c > 1 for c in pb.CEILINGS))

    def test_09_axis_source_and_alternative_routes(self):
        self.assertEqual(
            [r["h"] for r in self.report["axis_calibrations"]], list(pb.HEIGHTS)
        )
        self.assertEqual(
            [
                r["h"]
                for r in self.report["axis_calibrations"]
                if r["direct_route_checked"]
            ],
            [64, 256, 1024],
        )
        for row in self.report["axis_calibrations"]:
            lo, hi = pb.real_bounds(row["theta_axis"])
            self.assertTrue(-1 < lo < hi < 1)
            self.assertGreater(pb.real_bounds(row["log_derivative"])[0], 0)

    def test_10_source_artifact_seals(self):
        self.assertEqual(len(pb.BINDINGS), 35)
        self.assertEqual(len(self.report["artifacts"]), 4)
        self.assertEqual(pb.manifest()["direct_source_count"], 11)
        for path, sha in self.report["artifacts"].items():
            self.assertEqual(pb.digest(pb.lf(pb.file_bytes(pb.ROOT / path))), sha)

    def test_11_scope_and_arithmetic(self):
        c = self.report["contract"]
        self.assertEqual(c["arithmetic_class"], "MIXED")
        self.assertEqual(
            c["arithmetic_components"],
            [
                "DIRECTED_BALL_ENCLOSURES",
                "EXACT_RATIONAL",
                "CERTIFIED_INTEGER_COVERAGE",
            ],
        )
        for key in (
            "analytic_quantifiers_machine_certified",
            "cofinal_capture",
            "actual_innerness_proved",
            "RH",
        ):
            self.assertIs(c[key], False)
        self.assertIn("outward", c["rounding"])
        self.assertIn("UNPAID", c["inner_premise"])

    def test_12_json_numbers_and_duplicates(self):
        for raw in (b'{"x":1,"x":2}', b'{"x":1.2}', b'{"x":NaN}', b'{"x":Infinity}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                pb.decode(raw)

    def test_13_strict_rationals(self):
        for value in (True, False, 1.0, "1"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                pb.oa.rational(value)
        for value in ([True, 1], [1, True], [2, 2], [1, 0], [1, -2]):
            with self.subTest(value=value), self.assertRaises(ValueError):
                pb.oa.unpair(value)

    def test_14_bit_string_depth_caps(self):
        for value in (2**4096, "x" * 4097):
            with self.assertRaises(ValueError):
                pb.typed(value)
        deep = 0
        for _ in range(26):
            deep = [deep]
        with self.assertRaises(ValueError):
            pb.typed(deep)

    def test_15_bytes_and_lf(self):
        self.assertEqual(pb.lf(b"a\r\nb\n"), b"a\nb\n")
        for raw in ("text", b"a\x00", b"a\r", b"\x7f"):
            with self.assertRaises(ValueError):
                pb.lf(raw)
        with patch.dict(pb.CAPS, source_bytes=4), self.assertRaises(ValueError):
            pb.decode(b'{"a":1}')

    def test_16_work_and_precision_guards(self):
        with patch.object(pb, "WORK", 9999):
            pb.charge()
            with self.assertRaises(ValueError):
                pb.charge()
        for n in (True, -1, 10001):
            with self.assertRaises(ValueError):
                pb.charge(n)
        with pb.oa.precision(192), self.assertRaises(ValueError):
            pb.fixed_lambda()

    def test_17_fixed_grid_input_guards(self):
        with pb.oa.precision(256):
            for h in (True, 63, 65, 65537):
                with self.assertRaises(ValueError):
                    pb.axis_value(h, pb.arb(1))
            for w in (Q(1, 255), True, Q(-1, 256)):
                with self.assertRaises(ValueError):
                    pb.lower_bound(pb.acb(20, 1), pb.acb(1), 64, w, pb.arb(1))
            with self.assertRaises(ValueError):
                pb.lower_bound(pb.acb(20, -1), pb.acb(1), 64, Q(1, 256), pb.arb(1))
            for node, raw, axis in (
                (pb.acb(2**6000, 1), pb.acb(1), pb.arb(1)),
                (pb.acb(25, pb.arb(1) / 2), pb.acb(2**6000), pb.arb(1)),
                (pb.acb(25, pb.arb(1) / 2), pb.acb(1), pb.arb(2**6000)),
            ):
                with self.assertRaises(ValueError):
                    pb.lower_bound(node, raw, 64, Q(1, 256), axis)
            with self.assertRaises(ValueError):
                pb.axis_value(64, pb.arb(2**6000))

    def test_18_manifest_identity_fails_closed(self):
        actual = pb.file_bytes
        forged = copy.deepcopy(pb.manifest())
        forged["design"] = "0" * 40
        with (
            patch.object(
                pb,
                "file_bytes",
                side_effect=lambda p: (
                    pb.canonical(forged) if p == pb.MANIFEST else actual(p)
                ),
            ),
            self.assertRaisesRegex(ValueError, "fixed manifest"),
        ):
            pb.authenticated_sources()

    def test_19_source_bytes_fail_closed(self):
        actual = pb.read_source
        with (
            patch.object(
                pb,
                "read_source",
                side_effect=lambda row: (
                    actual(row) + b"\n" if row == pb.BINDINGS[0] else actual(row)
                ),
            ),
            self.assertRaisesRegex(ValueError, "source identity"),
        ):
            pb.authenticated_sources()

    def test_20_unsealed_mutation(self):
        bad = copy.deepcopy(self.report)
        bad["parameter_anchor"] = 32
        with self.assertRaisesRegex(ValueError, "payload seal"):
            pb.check_report(bad)

    def test_21_resealed_calibration(self):
        self.fresh_attack(lambda r: r.__setitem__("parameter_anchor", True))

    def test_22_resealed_width(self):
        self.fresh_attack(lambda r: r["bands"][0].__setitem__("D", [1, 255]))

    def test_23_resealed_omitted_cell(self):
        self.fresh_attack(
            lambda r: r["bands"][0]["all1320_grid_part"][0]["witnesses"].pop()
        )

    def test_24_resealed_forged_floor(self):
        self.fresh_attack(
            lambda r: r["bands"][0]["all1320_grid_part"][0]["witnesses"][0].__setitem__(
                "norm_lower", [1, 1]
            )
        )

    def test_25_resealed_gram_substitution(self):
        self.fresh_attack(
            lambda r: r["bands"][0]["prefixes"][0].__setitem__("Gram_ceiling", [1, 1])
        )

    def test_26_resealed_raw_substitution(self):
        self.fresh_attack(
            lambda r: r["inherited_nodes"][0].__setitem__(
                "raw_modulus", [[1, 1], [1, 1]]
            )
        )

    def test_27_resealed_axis_substitution(self):
        self.fresh_attack(
            lambda r: r["axis_calibrations"][0].__setitem__(
                "theta_axis", [[-1, 1], [-1, 1]]
            )
        )

    def test_28_resealed_geometry_claim(self):
        self.fresh_attack(
            lambda r: r["geometry"].__setitem__("global_Carleson_box_upper", 0)
        )

    def test_29_resealed_scope_promotion(self):
        self.fresh_attack(
            lambda r: r["contract"].__setitem__("actual_innerness_proved", True)
        )

    def test_30_resealed_artifact_and_source(self):
        self.fresh_attack(
            lambda r: r["artifacts"].__setitem__(next(iter(r["artifacts"])), "0" * 64)
        )

    def test_31_geometry_failure_control(self):
        rows = copy.deepcopy(self.report["inherited_nodes"])
        for r in rows:
            r["y_interval"] = [[1000, 1], [1000, 1]]
        geo = pb.geometry(rows)
        self.assertFalse(geo["all39gaps_certified"])
        self.assertEqual(geo["global_Carleson_box_upper"], 40)
        self.assertTrue(any(not r["certified"] for r in geo["adjacent_gaps"]))

    def test_32_unresolved_unit_membership_control(self):
        rows = copy.deepcopy(self.report["inherited_nodes"])
        # Translate ALL intervals by the same exact amount, preserving their order.
        first = pb.real_bounds(rows[0]["x_interval"])
        shift = (
            Q(first[0].numerator // first[0].denominator + 1)
            - (first[0] + first[1]) / 2
        )
        for r in rows:
            lo, hi = pb.real_bounds(r["x_interval"])
            r["x_interval"] = [pb.oa.pair(lo + shift), pb.oa.pair(hi + shift)]
        geo = pb.geometry(rows)
        self.assertFalse(geo["all40memberships_resolved"])
        self.assertFalse(geo["memberships"][0]["resolved"])


if __name__ == "__main__":
    unittest.main()
