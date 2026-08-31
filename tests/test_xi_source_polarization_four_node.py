"""Strict bounded controls, not a machine proof of global source positivity."""

from __future__ import annotations

import copy
import itertools
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "research" / "exploratory")
)
import xi_source_polarization_four_node as p


class SourcePolarizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.value = p.build()

    def reseal(self, value):
        value["payload_sha256"] = p.sha(
            p.canonical({k: v for k, v in value.items() if k != "payload_sha256"})
        )
        return value

    def test_01_frozen_fixture_fresh(self):
        self.assertTrue(p.validate(p.load(p.FIXTURE)))

    def test_02_exact_grid_coverage(self):
        self.assertEqual(self.value["exact"]["grid_count"], 6 * 3**4)

    def test_03_model_coverage(self):
        self.assertEqual(len(self.value["exact"]["models"]), 30)

    def test_04_native_coverage(self):
        self.assertEqual(
            [row["x"] for row in self.value["native"]],
            [[p.pack(x) for x in row] for row in p.PANELS],
        )

    def test_05_all_principal_coverage(self):
        expected = [
            list(c) for n in range(1, 5) for c in itertools.combinations(range(4), n)
        ]
        for row in self.value["native"]:
            self.assertEqual([c["indices"] for c in row["principal"]], expected)

    def test_06_all_principal_positive(self):
        for row in self.value["native"]:
            for cell in row["principal"]:
                self.assertEqual(cell["status"], "POSITIVE")
                self.assertGreater(p.unpack(cell["enclosure"][0]), 0)

    def test_07_native_factors_negative(self):
        for row in self.value["native"]:
            for key in ("A", "B", "Dp", "Dtp"):
                self.assertLess(p.unpack(row["factors"][key][1]), 0)

    def test_08_gaussian_rank_one(self):
        for row in self.value["exact"]["models"]:
            if row["model"] == "gaussian_rank_one":
                for key in ("A", "B", "det", "delta"):
                    self.assertEqual(p.unpack(row["values"][key]), 0)

    def test_09_one_atom_rank_two(self):
        for row in self.value["exact"]["models"]:
            if row["model"] == "one_atom":
                self.assertEqual(p.unpack(row["values"]["delta"]), 0)
                self.assertEqual(p.unpack(row["values"]["det"]), 0)

    def test_10_rank_three_models(self):
        for row in self.value["exact"]["models"]:
            if row["model"] in ("constant_one_atom", "zero_one_atom"):
                self.assertGreater(p.unpack(row["values"]["delta"]), 0)
                self.assertEqual(p.unpack(row["values"]["det"]), 0)

    def test_11_two_atom_rank_four(self):
        for row in self.value["exact"]["models"]:
            if row["model"] == "two_atoms":
                self.assertGreater(p.unpack(row["values"]["det"]), 0)

    def test_12_volterra_coefficients(self):
        for row in self.value["exact"]["volterra_determinants"]:
            u, v = map(Q, (row["u"], row["v"]))
            self.assertEqual(
                p.elimination([[2 * u, u + v], [u + v, 2 * v]]), row["det"]
            )
            self.assertLess(row["det"], 0)

    def test_13_discovery_exact(self):
        self.assertEqual(
            p.unpack(self.value["exact"]["discovery"]["det"]), Q(386681, 1102500)
        )

    def test_14_sources_exact(self):
        self.assertEqual(
            p.canonical(p.load(p.MANIFEST)), p.canonical(p.source_manifest())
        )

    def test_15_roundtrip_rational(self):
        for q in (Q(0), Q(-17, 23), Q(2**600, 7)):
            self.assertEqual(p.unpack(p.pack(q)), q)

    def test_16_bool_rational_rejected(self):
        with self.assertRaises(ValueError):
            p.unpack([True, 1])

    def test_17_float_rational_rejected(self):
        with self.assertRaises(ValueError):
            p.unpack([1.0, 1])

    def test_18_unreduced_rational_rejected(self):
        with self.assertRaises(ValueError):
            p.unpack([2, 4])

    def test_19_denominator_rejected(self):
        for denominator in (0, -1):
            with self.assertRaises(ValueError):
                p.unpack([1, denominator])

    def test_20_integer_cap(self):
        with self.assertRaises(ValueError):
            p.validate_tree(1 << 4096)

    def test_21_depth_cap(self):
        value = 0
        for _ in range(26):
            value = [value]
        with self.assertRaises(ValueError):
            p.validate_tree(value)

    def test_22_float_tree_rejected(self):
        with self.assertRaises(ValueError):
            p.validate_tree({"a": 0.25})

    def test_23_matrix_cap(self):
        with self.assertRaises(ValueError):
            p.determinant([[Q(0)] * 5 for _ in range(5)])

    def test_24_native_domain(self):
        for x in (Q(1, 2), Q(129), 1, True, 0.75):
            with self.assertRaises(ValueError):
                p.native_jet(x)

    def test_25_node_order(self):
        with self.assertRaises(ValueError):
            p.algebra((Q(1), Q(1), Q(2), Q(3)), [Q(1)] * 4)

    def test_26_resealed_native_value(self):
        value = copy.deepcopy(self.value)
        value["native"][0]["factors"]["A"][0][0] += 1
        with self.assertRaises(ValueError):
            p.validate(self.reseal(value))

    def test_27_resealed_missing_panel(self):
        value = copy.deepcopy(self.value)
        value["native"].pop()
        with self.assertRaises(ValueError):
            p.validate(self.reseal(value))

    def test_28_resealed_false_status(self):
        value = copy.deepcopy(self.value)
        value["native"][0]["principal"][0]["status"] = "NEGATIVE"
        with self.assertRaises(ValueError):
            p.validate(self.reseal(value))

    def test_29_resealed_bool_coverage(self):
        value = copy.deepcopy(self.value)
        value["native"][0]["index"] = False
        with self.assertRaises(ValueError):
            p.validate(self.reseal(value))

    def test_30_resealed_contract(self):
        value = copy.deepcopy(self.value)
        value["contract"]["caps"]["bits"] = 1024
        with self.assertRaises(ValueError):
            p.validate(self.reseal(value))

    def test_31_resealed_artifact(self):
        value = copy.deepcopy(self.value)
        value["artifacts"][0]["sha256_lf"] = "0" * 64
        with self.assertRaises(ValueError):
            p.validate(self.reseal(value))

    def test_32_changed_primitive(self):
        with (
            mock.patch.object(p, "source_manifest", return_value={"schema": "forged"}),
            self.assertRaises(ValueError),
        ):
            p.validate(self.value)


if __name__ == "__main__":
    unittest.main()
