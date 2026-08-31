"""Exact finite controls; the smooth bump theorem is reviewed from prose."""

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
import xi_five_node_schwarzian_no_go as p


class FiveNodeNoGoTests(unittest.TestCase):
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

    def test_02_discovery_disclosed(self):
        self.assertIn(
            "scouted before preregistration", self.value["contract"]["discovery"]
        )

    def test_03_discovery_all_proper_positive(self):
        self.assertTrue(
            all(
                p.unpack(cell["det"]) > 0
                for cell in self.value["discovery"]["minors"][:-1]
            )
        )

    def test_04_discovery_full_negative(self):
        self.assertLess(p.unpack(self.value["discovery"]["minors"][-1]["det"]), 0)

    def test_05_discovery_exact_value(self):
        self.assertEqual(
            p.unpack(self.value["discovery"]["minors"][-1]["det"]),
            Q(-84039, 69417224890000000000),
        )

    def test_06_heldout_labels(self):
        self.assertEqual(
            [row["label"] for row in self.value["heldout"]], ["A", "B", "C"]
        )

    def test_07_heldout_complete_minors(self):
        expected = [
            list(c) for n in range(1, 6) for c in itertools.combinations(range(5), n)
        ]
        for row in self.value["heldout"]:
            self.assertEqual([cell["indices"] for cell in row["minors"]], expected)

    def test_07b_heldout_outcomes(self):
        for row in self.value["heldout"]:
            self.assertTrue(
                all(p.unpack(cell["det"]) > 0 for cell in row["minors"][:-1])
            )
        self.assertLess(p.unpack(self.value["heldout"][0]["minors"][-1]["det"]), 0)
        self.assertLess(p.unpack(self.value["heldout"][1]["minors"][-1]["det"]), 0)
        self.assertGreater(p.unpack(self.value["heldout"][2]["minors"][-1]["det"]), 0)

    def test_08_polynomial_coverage(self):
        self.assertEqual(len(self.value["polynomials"]["discovery_base"]), 5)
        self.assertEqual(len(self.value["polynomials"]["heldout_base"]), 5)

    def test_09_polynomial_checks(self):
        for rows in self.value["polynomials"].values():
            for row in rows:
                self.assertEqual(len(row["checks"]), 3)

    def test_10_discovery_linear(self):
        self.assertEqual(
            p.unpack(self.value["polynomials"]["discovery_base"][0]["linear"]),
            Q(-243, 2169288277812500),
        )

    def test_11_discovery_quadratic(self):
        self.assertEqual(
            p.unpack(self.value["polynomials"]["discovery_base"][0]["quadratic"]),
            Q(-483, 533978653000000),
        )

    def test_12_regular_residual(self):
        row = self.value["residual"]["regular"]
        self.assertEqual(
            p.unpack(row["residual_identity"]),
            p.unpack(row["anchor_det"]) * p.unpack(row["full_det"]),
        )

    def test_13_singular_residual(self):
        row = self.value["residual"]["singular"]
        self.assertEqual(p.unpack(row["anchor_det"]), 0)
        self.assertEqual(p.unpack(row["residual_identity"]), 0)

    def test_14_wrong_orientation_differs(self):
        row = self.value["residual"]["regular"]
        self.assertNotEqual(
            p.unpack(row["wrong_orientation"]), p.unpack(row["residual_identity"])
        )

    def test_15_source_manifest_fresh(self):
        self.assertEqual(p.load(p.MANIFEST), p.source_manifest())

    def test_16_artifact_seals(self):
        self.assertEqual(self.value["artifacts"], p.artifact_seals())

    def test_17_payload_seal(self):
        payload = {k: v for k, v in self.value.items() if k != "payload_sha256"}
        self.assertEqual(self.value["payload_sha256"], p.sha(p.canonical(payload)))

    def test_18_duplicate_key_rejected(self):
        with (
            mock.patch.object(p.Path, "read_bytes", return_value=b'{"a":1,"a":2}'),
            self.assertRaises(ValueError),
        ):
            p.load(p.FIXTURE)

    def test_19_nonfinite_rejected(self):
        with (
            mock.patch.object(p.Path, "read_bytes", return_value=b'{"a":NaN}'),
            self.assertRaises(ValueError),
        ):
            p.load(p.FIXTURE)

    def test_20_noncanonical_rational_rejected(self):
        with self.assertRaises(ValueError):
            p.unpack([2, 2])

    def test_21_contract_reseal_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["contract"]["xi_boundary"] = "actual"
        with self.assertRaises(ValueError):
            p.validate(self.reseal(bad))

    def test_22_discovery_reseal_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["discovery"]["minors"][-1]["det"] = [0, 1]
        with self.assertRaises(ValueError):
            p.validate(self.reseal(bad))

    def test_23_heldout_reseal_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["heldout"][0]["label"] = "moved"
        with self.assertRaises(ValueError):
            p.validate(self.reseal(bad))

    def test_24_source_reseal_rejected(self):
        bad = copy.deepcopy(p.load(p.MANIFEST))
        bad["sources"][0]["commit"] = "0" * 40
        with (
            mock.patch.object(p, "load", return_value=bad),
            self.assertRaises(ValueError),
        ):
            p.validate(self.value)

    def test_25_determinant_routes(self):
        a = [[Q(1), Q(2), Q(3)], [Q(2), Q(5), Q(7)], [Q(3), Q(7), Q(11)]]
        self.assertEqual(p.det_elimination(a), p.det_permutation(a))

    def test_26_adjugate_identity(self):
        a = [[Q(2), Q(1)], [Q(1), Q(3)]]
        adj = p.adjugate(a)
        self.assertEqual(
            [
                [sum(a[i][k] * adj[k][j] for k in range(2)) for j in range(2)]
                for i in range(2)
            ],
            [[Q(5), Q(0)], [Q(0), Q(5)]],
        )


if __name__ == "__main__":
    unittest.main()
